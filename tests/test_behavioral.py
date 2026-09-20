"""Offline checks of the test harness; synthetic adapters are not live-model evidence."""
from copy import deepcopy
import io
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from behavioral import check_assertion, invoke, load_cases, main, run_cases, validate_observation
from build_packages import build
from adapters.chat_completion import complete


def observation(text='API'):
    return {'status': 'ok', 'response': text, 'execution_mode': 'response-only',
            'adapter': {'id': 'synthetic-test-double', 'version': '1'},
            'model': {'id': 'no-model-invoked', 'version': '1'}}


class BehavioralTests(unittest.TestCase):
    def test_every_skill_has_valid_scenarios(self):
        cases = load_cases(sorted((ROOT / 'tests').glob('test-*.yaml')))
        self.assertEqual({c['skill'] for c in cases if c['mode'] == 'explicit'},
                         {p.parent.name for p in (ROOT / 'skills').glob('arch-*/SKILL.md')})

    def test_manifest_rejects_silent_settings_and_invalid_assertions(self):
        template = yaml.safe_load((ROOT / 'tests/test-arch-api.yaml').read_text())
        changes = [lambda d: d['scenarios'][0]['steps'][0].update(runs=3),
                   lambda d: d['scenarios'][0].update(min_pass_rate=0.67),
                   lambda d: d['scenarios'][0].update(runs=True),
                   lambda d: d['scenarios'][0].update(runs=2, min_passes=3),
                   lambda d: d['scenarios'][0]['steps'][0].update(assertion=[]),
                   lambda d: d['scenarios'][0]['steps'][0]['assert'][0].update(type='unknown'),
                   lambda d: d.update(skill='./skills/../../outside'),
                   lambda d: d['scenarios'].append(deepcopy(d['scenarios'][0]))]
        with tempfile.TemporaryDirectory() as temp:
            file = Path(temp) / 'cases.yaml'
            for change in changes:
                data = deepcopy(template)
                change(data)
                file.write_text(yaml.safe_dump(data), encoding='utf-8')
                with self.assertRaises(ValueError):
                    load_cases([file])
            file.write_text('skill: a\nskill: b\n', encoding='utf-8')
            with self.assertRaises(ValueError):
                load_cases([file])

    def test_assertions_check_json_types_and_observed_capabilities(self):
        a = {'type': 'json_equals', 'pointer': '/a~1b/0', 'value': False}
        self.assertTrue(check_assertion(a, observation('{"a/b":[false]}')))
        self.assertFalse(check_assertion(a, observation('{"a/b":[0]}')))
        self.assertFalse(check_assertion(a, observation('not JSON')))
        self.assertTrue(check_assertion({'type': 'contains', 'value': 'api'}, observation()))
        self.assertIsNone(check_assertion({'type': 'capability_used', 'value': 'file_write'}, observation()))
        self.assertIsNone(check_assertion({'type': 'token_usage_under', 'value': 4000}, observation()))
        self.assertFalse(check_assertion({'type': 'token_usage_under', 'value': 4000},
                                        dict(observation(), total_tokens=4000)))
        with self.assertRaises(ValueError):
            validate_observation(dict(observation(), capabilities_used=['file_write']))

    def test_subprocess_adapter_transport_and_errors(self):
        with tempfile.TemporaryDirectory() as temp:
            # Exercise actual stdin/stdout transport without invoking a model.
            command = [sys.executable, '-c', 'import json,sys; r=json.load(sys.stdin); '
                       'print(json.dumps(' + repr(observation()) + '))']
            self.assertEqual(invoke(command, {'messages': []}, temp, 5)['status'], 'ok')
            self.assertEqual(invoke([str(Path(temp) / 'absent')], {}, temp, 1)['status'], 'unavailable')
            self.assertEqual(invoke([sys.executable, '-c', 'print("bad JSON")'], {}, temp, 5)['status'], 'error')
            with patch('behavioral.subprocess.run', side_effect=subprocess.TimeoutExpired('adapter', 1)):
                self.assertEqual(invoke(command, {}, temp, 1)['status'], 'error')

    def test_repeat_counts_isolation_budget_and_unavailable(self):
        case = dict(id='test', mode='explicit', skill='arch-api', skills=None, runs=3, min_passes=2, timeout=5,
                    steps=[{'prompt': 'Test', 'assert': [{'type': 'contains', 'value': 'API'}]}])
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            packages = root / 'packages'
            build(packages, profile='expert', selected=['arch-api'])
            with patch('behavioral.invoke', side_effect=[observation(), observation('wrong'), observation()]):
                report = run_cases([case], packages, root / 'results', ['synthetic'], 3)
            self.assertEqual(report['counts'], {'passed': 1})
            self.assertEqual(report['cases'][0]['pass_rate'], 2 / 3)
            self.assertEqual(len(list((root / 'results').rglob('step-1.json'))), 3)
            with self.assertRaises(ValueError):
                run_cases([case], packages, root / 'over-budget', ['synthetic'], 2)
            self.assertFalse((root / 'over-budget').exists())
            with patch('behavioral.invoke', return_value={'status': 'unavailable', 'reason': 'no model'}):
                report = run_cases([case], packages, root / 'unavailable', ['synthetic'], 3)
            self.assertEqual(report['counts'], {'unavailable': 1})

    def test_multiturn_retains_history_but_new_attempt_resets_it(self):
        case = dict(id='multi', mode='explicit', skill='arch-api', skills=None, runs=2, min_passes=2, timeout=5,
                    steps=[{'prompt': p, 'assert': [{'type': 'contains', 'value': 'API'}]}
                           for p in ['first', 'next']])
        requests = []
        def respond(command, request, workspace, timeout):
            requests.append(deepcopy(request))
            return observation()
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            build(root / 'packages', profile='expert', selected=['arch-api'])
            with patch('behavioral.invoke', side_effect=respond):
                run_cases([case], root / 'packages', root / 'results', ['synthetic'], 4)
        self.assertEqual([len(r['messages']) for r in requests], [1, 3, 1, 3])
        self.assertNotEqual(requests[0]['workspace'], requests[2]['workspace'])
        self.assertNotIn('assert', json.dumps(requests))

    def test_activation_mode_requires_host_reported_skill_trace(self):
        cases = load_cases([ROOT / 'tests/test-activation.yaml'])
        self.assertEqual({case['mode'] for case in cases}, {'activation'})
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            build(root / 'packages', profile='expert', selected=['arch-api', 'arch-security', 'arch-observability'])
            def respond(command, request, workspace, timeout):
                self.assertEqual(request['mode'], 'activation')
                return dict(observation(), execution_mode='host', skills_used=['arch-api'])
            with patch('behavioral.invoke', side_effect=respond):
                report = run_cases([cases[0]], root / 'packages', root / 'results', ['synthetic'], 1)
            self.assertEqual(report['counts'], {'passed': 1})
            self.assertEqual(report['cases'][0]['adapter']['id'], 'synthetic-test-double')

    def test_unconfigured_adapter_is_not_success_and_sends_no_request(self):
        with patch.dict(os.environ, {'ARCH_TEST_API_BASE': '', 'ARCH_TEST_MODEL': ''}), patch('adapters.chat_completion.build_opener') as network:
            self.assertEqual(complete({})['status'], 'unavailable')
            network.assert_not_called()
        with patch.dict(os.environ, {'ARCH_TEST_API_BASE': 'http://public.example/v1', 'ARCH_TEST_MODEL': 'x'}):
            self.assertEqual(complete({})['status'], 'error')

    def test_chat_adapter_builds_request_and_rejects_truncated_answers(self):
        with tempfile.TemporaryDirectory() as temp:
            (Path(temp) / 'SKILL.md').write_text('Skill instructions', encoding='utf-8')
            request = {'skill_root': temp, 'messages': [{'role': 'user', 'content': 'hello'}], 'timeout': 20}
            data = {'choices': [{'finish_reason': 'stop', 'message': {'content': 'complete answer'}}],
                    'model': 'versioned-model', 'usage': {'total_tokens': 25}}
            env = {'ARCH_TEST_API_BASE': 'https://provider.example/v1', 'ARCH_TEST_MODEL': 'chosen-model',
                   'ARCH_TEST_API_KEY': 'test-only-placeholder'}
            with patch.dict(os.environ, env, clear=True), patch('adapters.chat_completion.build_opener') as network:
                network.return_value.open.return_value = io.BytesIO(json.dumps(data).encode())
                result = complete(request)
                self.assertEqual(result['execution_mode'], 'response-only')
                self.assertEqual(result['model']['version'], 'versioned-model')
                sent = network.return_value.open.call_args.args[0]
                self.assertEqual(sent.full_url, 'https://provider.example/v1/chat/completions')
                self.assertEqual(json.loads(sent.data)['messages'][1]['content'], 'hello')
                self.assertNotIn('test-only-placeholder', json.dumps(result))
                data['choices'][0]['finish_reason'] = 'length'
                network.return_value.open.return_value = io.BytesIO(json.dumps(data).encode())
                self.assertEqual(complete(request)['status'], 'error')

    def test_cli_unavailable_exit_and_report(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            build(root / 'packages', profile='expert', selected=['arch-evaluate'])
            with patch.dict(os.environ, {'ARCH_TEST_API_BASE': '', 'ARCH_TEST_MODEL': ''}):
                code = main(['run', '--manifest', str(ROOT / 'tests/test-arch-evaluate.yaml'),
                             '--packages', str(root / 'packages'), '--output', str(root / 'reports'),
                             '--limit', '1'])
            self.assertEqual(code, 2)
            report = json.loads((root / 'reports/report.json').read_text())
            self.assertEqual(report['omitted_scenarios'], 3)
            self.assertEqual(report['counts'], {'unavailable': 1})


if __name__ == '__main__':
    unittest.main()
