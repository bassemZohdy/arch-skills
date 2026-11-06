#!/usr/bin/env python3
"""Compare two completed behavioral reports without judging unavailable runs as passes."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import sys
from behavioral_identity import execution_identity


class ComparisonError(ValueError):
    pass


def load(path: Path) -> dict:
    try:
        report = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ComparisonError(f"cannot read report {path}: {exc}") from exc
    if not isinstance(report, dict) or report.get("schema_version") != "1.0":
        raise ComparisonError(f"{path} is not a behavioral report schema 1.0")
    if report.get("complete") is not True:
        raise ComparisonError(f"{path} is incomplete")
    if not isinstance(report.get("cases"), list) or not report["cases"]:
        raise ComparisonError(f"{path} has no cases")
    return report


def identity(case: dict) -> tuple:
    attempts = case.get("attempts")
    if not isinstance(attempts, list) or not attempts:
        raise ComparisonError(f"{case.get('id', '<unknown>')} has no attempts")
    run_identity = None
    if case.get('status') not in {'error', 'unavailable'}:
        try:
            run_identity = execution_identity(case)
            runs, minimum = case.get('runs'), case.get('min_passes')
            if (type(runs) is not int or type(minimum) is not int or
                    not 1 <= minimum <= runs or len(attempts) != runs):
                raise ValueError('incomplete attempts or invalid repetition settings')
            for attempt in attempts:
                if attempt.get('status') not in {'passed', 'failed'} or not attempt.get('steps'):
                    raise ValueError('executed attempts and steps are required')
                for step in attempt['steps']:
                    if execution_identity(step) != run_identity:
                        raise ValueError('execution identity changed within case')
        except (ValueError, TypeError, AttributeError) as exc:
            raise ComparisonError(f"{case.get('id')}: {exc}") from exc
    return (case.get('skill'), case.get('manifest_sha256'), case.get('mode'),
            case.get('runs'), case.get('min_passes'), case.get('timeout'), run_identity)


def compare(baseline: dict, candidate: dict, allow_configuration_change: bool = False,
            allow_package_change: bool = False) -> dict:
    if any(case.get("status") in {"unavailable", "error"} for case in baseline["cases"]):
        raise ComparisonError("baseline contains unavailable or errored cases; establish an executed baseline first")
    before = {case.get("id"): case for case in baseline["cases"]}
    after = {case.get("id"): case for case in candidate["cases"]}
    if any(not isinstance(key, str) or not key.strip() for key in (*before, *after)) or len(before) != len(baseline["cases"]) or len(after) != len(candidate["cases"]):
        raise ComparisonError("case IDs must be unique and non-empty")
    if set(before) != set(after):
        raise ComparisonError(f"case selection differs: missing={sorted(set(before)-set(after))}, added={sorted(set(after)-set(before))}")
    regressions, improvements, unavailable, errors = [], [], [], []
    configuration, packages = [], []
    rows = []
    for case_id in sorted(before):
        old, new = before[case_id], after[case_id]
        if old.get('status') not in {'passed', 'failed'} or new.get('status') not in {'passed', 'failed', 'error', 'unavailable'}:
            raise ComparisonError(f'{case_id}: unsupported case status')
        old_id, new_id = identity(old), identity(new)
        # Unavailable/error attempts may have no observed execution identity.
        changed = old_id[:-1] != new_id[:-1] or (new_id[-1] is not None and old_id[-1] != new_id[-1])
        if changed:
            configuration.append(case_id)
        if not allow_configuration_change and changed:
            raise ComparisonError(f"configuration changed for {case_id}; use --allow-configuration-change only for an intentional new baseline")
        if not old.get('package_sha256') or not new.get('package_sha256'):
            raise ComparisonError(f'{case_id}: package hash required')
        if old['package_sha256'] != new['package_sha256']:
            packages.append(case_id)
            if not (allow_package_change or allow_configuration_change):
                raise ComparisonError(f'package changed for {case_id}; use --allow-package-change for a controlled candidate comparison')
        old_status, new_status = old.get("status"), new.get("status")
        if old_status == "passed" and new_status != "passed":
            regressions.append(case_id)
        if old_status != "passed" and new_status == "passed":
            improvements.append(case_id)
        if new_status == "unavailable":
            unavailable.append(case_id)
        if new_status == 'error':
            errors.append(case_id)
        rows.append({"id": case_id, "baseline": old_status, "candidate": new_status,
                     "baseline_pass_rate": old.get("pass_rate"), "candidate_pass_rate": new.get("pass_rate")})
    result = {"schema_version": "1.0", "compared_at": datetime.now(timezone.utc).isoformat(),
              "baseline_cases": len(before), "candidate_cases": len(after),
              "configuration_changes": configuration, "package_changes": packages, "regressions": regressions,
              "improvements": improvements, "unavailable": unavailable, "cases": rows,
              "errors": errors,
              "status": "failed" if errors else "unavailable" if unavailable else "failed" if regressions else "passed"}
    return result


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("baseline", type=Path)
    parser.add_argument("candidate", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--allow-configuration-change", action="store_true")
    parser.add_argument('--allow-package-change', action='store_true',
                        help='allow only package changes while preserving model/adapter/test settings')
    args = parser.parse_args(argv)
    try:
        result = compare(load(args.baseline), load(args.candidate), args.allow_configuration_change,
                         args.allow_package_change)
    except ComparisonError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    text = json.dumps(result, indent=2) + "\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")
    return 2 if result["status"] == "unavailable" else 1 if result["status"] == "failed" else 0


if __name__ == "__main__":
    raise SystemExit(main())
