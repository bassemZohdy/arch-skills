#!/usr/bin/env python3
"""Validate and execute optional skill scenarios through a JSON command adapter."""
from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess
import sys

import yaml

ROOT = Path(__file__).resolve().parents[1]
TYPES = {'contains', 'not_contains', 'contains_any', 'json_equals',
         'capability_used', 'token_usage_under'}


class UniqueLoader(yaml.SafeLoader):
    """Reject silent replacement of scenario settings by duplicate YAML keys."""


def unique_mapping(loader, node):
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node)
        require(isinstance(key, str) and key not in result, f'duplicate or invalid YAML key: {key}')
        result[key] = loader.construct_object(value_node)
    return result


UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def positive(value):
    return type(value) is int and value > 0


def skill_name(value):
    require(isinstance(value, str) and value.startswith('./skills/'), 'skill must be ./skills/<name>')
    name = value.removeprefix('./skills/')
    require(name.startswith('arch-') and '/' not in name and '\\' not in name,
            'invalid skill path')
    require((ROOT / 'skills' / name / 'SKILL.md').is_file(), f'unknown skill: {name}')
    return name


def load_cases(paths):
    cases, ids = [], set()
    for path in paths:
        manifest = yaml.load(path.read_text(encoding='utf-8'), Loader=UniqueLoader)
        require(isinstance(manifest, dict), f'{path}: expected mapping')
        require(not set(manifest) - {'skill', 'timeout', 'scenarios'}, f'{path}: unknown manifest setting')
        skill_name(manifest.get('skill'))
        timeout = manifest.get('timeout', 180)
        require(positive(timeout) and timeout <= 600, f'{path}: timeout must be 1..600 seconds')
        scenarios = manifest.get('scenarios')
        require(isinstance(scenarios, list) and scenarios, f'{path}: scenarios must be nonempty')
        for scenario in scenarios:
            require(isinstance(scenario, dict), 'scenario must be a mapping')
            require(not set(scenario) - {'name', 'skill', 'steps', 'runs', 'min_passes'},
                    'unknown scenario setting; use integer min_passes, not a rounded rate')
            require(isinstance(scenario.get('name'), str) and scenario['name'].strip(), 'scenario name required')
            case_id = f'{path.stem}/{scenario["name"]}'
            require(case_id not in ids, f'duplicate case: {case_id}')
            ids.add(case_id)
            skill = skill_name(scenario.get('skill', manifest['skill']))
            runs = scenario.get('runs', 1)
            minimum = scenario.get('min_passes', runs)
            require(positive(runs) and runs <= 10 and positive(minimum) and minimum <= runs,
                    f'{case_id}: require 1 <= min_passes <= runs <= 10')
            steps = scenario.get('steps')
            require(isinstance(steps, list) and steps, f'{case_id}: steps required')
            for step in steps:
                require(isinstance(step, dict) and not set(step) - {'prompt', 'assert'},
                        f'{case_id}: repeat settings belong on the scenario, not a step')
                require(isinstance(step.get('prompt'), str) and step['prompt'].strip(), 'prompt required')
                assertions = step.get('assert')
                require(isinstance(assertions, list) and assertions, 'assertions required')
                for assertion in assertions:
                    require(isinstance(assertion, dict), 'assertion must be a mapping')
                    kind = assertion.get('type')
                    require(isinstance(kind, str) and kind in TYPES, f'unsupported assertion: {kind}')
                    require(not set(assertion) - {'type', 'value', 'pointer'}, 'unknown assertion field')
                    value = assertion.get('value')
                    if kind == 'token_usage_under':
                        require(positive(value), 'token limit must be positive integer')
                    elif kind == 'contains_any':
                        require(isinstance(value, list) and value and
                                all(isinstance(v, str) and v for v in value), 'contains_any needs strings')
                    elif kind == 'json_equals':
                        pointer = assertion.get('pointer')
                        require(isinstance(pointer, str) and (not pointer or pointer.startswith('/'))
                                and 'value' in assertion, 'json_equals needs pointer and value')
                        # Ensure expected data is JSON, not YAML dates/non-finite values.
                        json.dumps(value, allow_nan=False)
                    else:
                        require(isinstance(value, str) and value.strip(), 'assertion value must be text')
            cases.append(dict(id=case_id, skill=skill, runs=runs, min_passes=minimum,
                              timeout=timeout, steps=steps, manifest_sha256=hashlib.sha256(path.read_bytes()).hexdigest()))
    return cases


def pointer_value(value, pointer):
    for part in pointer.split('/')[1:] if pointer else []:
        part = part.replace('~1', '/').replace('~0', '~')
        if isinstance(value, list):
            if not part.isdigit() or (len(part) > 1 and part.startswith('0')):
                raise ValueError('invalid array index')
            value = value[int(part)]
        else:
            value = value[part]
    return value


def check_assertion(assertion, observation):
    kind, expected = assertion['type'], assertion['value']
    response = observation['response']
    if kind == 'contains':
        return expected.casefold() in response.casefold()
    if kind == 'not_contains':
        return expected.casefold() not in response.casefold()
    if kind == 'contains_any':
        return any(v.casefold() in response.casefold() for v in expected)
    if kind == 'json_equals':
        try:
            actual = pointer_value(json.loads(response), assertion['pointer'])
            return json.dumps(actual, sort_keys=True) == json.dumps(expected, sort_keys=True)
        except (ValueError, KeyError, IndexError, TypeError):
            return False
    if kind == 'capability_used':
        if observation.get('capabilities_used') is None:
            return None
        return expected in observation['capabilities_used']
    if observation.get('total_tokens') is None:
        return None
    return observation['total_tokens'] < expected


def validate_observation(value):
    require(isinstance(value, dict), 'adapter output must be a JSON object')
    require(value.get('status') in {'ok', 'unavailable', 'error'}, 'invalid adapter status')
    if value['status'] != 'ok':
        require(isinstance(value.get('reason'), str) and value['reason'], 'adapter reason required')
        return value
    require(isinstance(value.get('response'), str) and value['response'].strip(), 'adapter returned empty response')
    for key in ('adapter', 'model'):
        require(isinstance(value.get(key), dict) and
                all(isinstance(value[key].get(k), str) and value[key][k] for k in ('id', 'version')),
                f'adapter output needs {key} id/version')
    require(value.get('execution_mode') in {'response-only', 'host'}, 'execution_mode required')
    if value.get('total_tokens') is not None:
        require(type(value['total_tokens']) is int and value['total_tokens'] >= 0, 'invalid token count')
    if value.get('capabilities_used') is not None:
        require(value['execution_mode'] == 'host' and isinstance(value['capabilities_used'], list)
                and all(isinstance(v, str) for v in value['capabilities_used']), 'invalid capability trace')
    return value


def invoke(command, request, workspace, timeout):
    try:
        process = subprocess.run(command, input=json.dumps(request), text=True, encoding='utf-8',
                                 capture_output=True, cwd=workspace, timeout=timeout, check=False)
        # Do not copy stderr into reports: adapters may log credentials there.
        if process.returncode:
            return {'status': 'error', 'reason': f'adapter exited {process.returncode}'}
        return validate_observation(json.loads(process.stdout))
    except FileNotFoundError:
        return {'status': 'unavailable', 'reason': 'adapter executable unavailable'}
    except subprocess.TimeoutExpired:
        return {'status': 'error', 'reason': 'adapter timed out'}
    except (OSError, ValueError, TypeError) as exc:
        return {'status': 'error', 'reason': f'invalid adapter execution ({type(exc).__name__})'}


def package_hash(package):
    digest = hashlib.sha256()
    for path in sorted(package.rglob('*')):
        if path.is_file() and '__pycache__' not in path.parts:
            digest.update(path.relative_to(package).as_posix().encode() + b'\0' + path.read_bytes())
    return digest.hexdigest()


def run_cases(cases, packages, output, command, max_calls):
    planned = sum(c['runs'] * len(c['steps']) for c in cases)
    require(planned <= max_calls, f'selection needs {planned} calls, above max-calls={max_calls}')
    require(cases, 'no scenarios selected')
    for case in cases:
        package = packages / case['skill']
        require((package / 'SKILL.md').is_file() and (package / 'framework').is_dir()
                and (package / 'package-manifest.json').is_file(),
                f'build the expert package first: {package}')
    output.mkdir(parents=True, exist_ok=False)
    report = {'schema_version': '1.0', 'started_at': datetime.now(timezone.utc).isoformat(),
              'planned_calls': planned, 'expected_scenarios': len(cases), 'complete': False,
              'cases': [], 'scope': 'explicit skill execution; not automatic activation'}
    (output / 'report.json').write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    for index, case in enumerate(cases):
        package = (packages / case['skill']).resolve()
        result = {k: v for k, v in case.items() if k != 'steps'}
        result.update(package_sha256=package_hash(package), attempts=[])
        for attempt in range(case['runs']):
            workspace = output / f'case-{index + 1:04d}' / f'run-{attempt + 1:02d}'
            workspace.mkdir(parents=True)
            messages, outcomes = [], []
            status = 'passed'
            for number, step in enumerate(case['steps']):
                messages.append({'role': 'user', 'content': step['prompt']})
                request = {'protocol_version': '1.0', 'skill_root': str(package),
                           'workspace': str(workspace.resolve()), 'messages': messages,
                           'timeout': case['timeout']}
                observation = invoke(command, request, workspace, case['timeout'])
                evidence = workspace / f'step-{number + 1}.json'
                evidence.write_text(json.dumps({'request': request, 'observation': observation}, indent=2) + '\n', encoding='utf-8')
                if observation['status'] != 'ok':
                    status = observation['status']
                    outcomes.append({'status': status, 'evidence': evidence.relative_to(output).as_posix()})
                    break
                assertions = [dict(a, passed=check_assertion(a, observation)) for a in step['assert']]
                outcomes.append({'assertions': assertions, 'evidence': evidence.relative_to(output).as_posix()})
                if any(a['passed'] is None for a in assertions):
                    status = 'unavailable'
                elif any(a['passed'] is False for a in assertions) and status == 'passed':
                    status = 'failed'
                messages.append({'role': 'assistant', 'content': observation['response']})
            result['attempts'].append({'status': status, 'steps': outcomes})
        counts = Counter(a['status'] for a in result['attempts'])
        result['pass_rate'] = counts['passed'] / case['runs']
        result['status'] = ('error' if counts['error'] else 'unavailable' if counts['unavailable'] else
                            'passed' if counts['passed'] >= case['min_passes'] else 'failed')
        report['cases'].append(result)
        report['counts'] = dict(Counter(c['status'] for c in report['cases']))
        report['finished_at'] = datetime.now(timezone.utc).isoformat()
        (output / 'report.json').write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    report['complete'] = True
    (output / 'report.json').write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    return report


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=['validate', 'run'])
    parser.add_argument('--manifest', type=Path, action='append')
    parser.add_argument('--packages', type=Path)
    parser.add_argument('--output', type=Path)
    parser.add_argument('--limit', type=int, default=10, help='maximum scenarios; 0 selects all')
    parser.add_argument('--max-calls', type=int, default=30)
    parser.add_argument('--adapter-command', help='JSON argv array, with absolute script paths; never a shell string')
    args = parser.parse_args(argv)
    try:
        paths = args.manifest or sorted((ROOT / 'tests').glob('test-*.yaml'))
        cases = load_cases(paths)
        if args.command == 'validate':
            covered = {c['skill'] for c in cases}
            if not args.manifest:
                expected = {p.parent.name for p in (ROOT / 'skills').glob('arch-*/SKILL.md')}
                require(covered == expected, f'scenario coverage missing: {sorted(expected - covered)}')
            print(json.dumps({'manifests': len(paths), 'scenarios': len(cases), 'skills': len(covered)}))
            return 0
        require(args.packages is not None and args.output is not None, 'run requires --packages and --output')
        require(args.limit >= 0 and args.max_calls > 0, 'invalid limit/call budget')
        command = json.loads(args.adapter_command) if args.adapter_command else [
            sys.executable, str(ROOT / 'scripts/adapters/chat_completion.py')]
        require(isinstance(command, list) and command and
                all(isinstance(v, str) and v for v in command), 'adapter command must be nonempty JSON argv')
        selected = cases[:args.limit] if args.limit else cases
        report = run_cases(selected, args.packages.resolve(), args.output.resolve(), command, args.max_calls)
        report.update(available_scenarios=len(cases), selected_scenarios=len(selected),
                      omitted_scenarios=len(cases) - len(selected))
        (args.output / 'report.json').write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
        print(json.dumps({k: report[k] for k in ('counts', 'planned_calls', 'selected_scenarios', 'omitted_scenarios')}))
        if report['counts'].get('error') or report['counts'].get('failed'):
            return 1
        return 2 if report['counts'].get('unavailable') else 0
    except (ValueError, OSError, yaml.YAMLError) as exc:
        print(f'ERROR: {exc}', file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
