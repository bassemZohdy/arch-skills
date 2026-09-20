#!/usr/bin/env python3
"""Compare two completed behavioral reports without judging unavailable runs as passes."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import sys


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
    adapter = case.get("adapter", {})
    model = case.get("model", {})
    return (case.get("id"), case.get("skill"), case.get("manifest_sha256"),
            case.get("package_sha256"), adapter.get("id"), adapter.get("version"),
            model.get("id"), model.get("version"))


def compare(baseline: dict, candidate: dict, allow_configuration_change: bool = False) -> dict:
    if any(case.get("status") in {"unavailable", "error"} for case in baseline["cases"]):
        raise ComparisonError("baseline contains unavailable or errored cases; establish an executed baseline first")
    before = {case.get("id"): case for case in baseline["cases"]}
    after = {case.get("id"): case for case in candidate["cases"]}
    if None in before or None in after or len(before) != len(baseline["cases"]) or len(after) != len(candidate["cases"]):
        raise ComparisonError("case IDs must be unique and non-empty")
    if set(before) != set(after):
        raise ComparisonError(f"case selection differs: missing={sorted(set(before)-set(after))}, added={sorted(set(after)-set(before))}")
    regressions, improvements, unavailable = [], [], []
    configuration = []
    rows = []
    for case_id in sorted(before):
        old, new = before[case_id], after[case_id]
        old_id, new_id = identity(old), identity(new)
        if old_id[1:] != new_id[1:]:
            configuration.append(case_id)
        if not allow_configuration_change and old_id[1:] != new_id[1:]:
            raise ComparisonError(f"configuration changed for {case_id}; use --allow-configuration-change only for an intentional new baseline")
        old_status, new_status = old.get("status"), new.get("status")
        if old_status == "passed" and new_status != "passed":
            regressions.append(case_id)
        if old_status != "passed" and new_status == "passed":
            improvements.append(case_id)
        if new_status == "unavailable":
            unavailable.append(case_id)
        rows.append({"id": case_id, "baseline": old_status, "candidate": new_status,
                     "baseline_pass_rate": old.get("pass_rate"), "candidate_pass_rate": new.get("pass_rate")})
    result = {"schema_version": "1.0", "compared_at": datetime.now(timezone.utc).isoformat(),
              "baseline_cases": len(before), "candidate_cases": len(after),
              "configuration_changes": configuration, "regressions": regressions,
              "improvements": improvements, "unavailable": unavailable, "cases": rows,
              "status": "unavailable" if unavailable else "failed" if regressions else "passed"}
    return result


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("baseline", type=Path)
    parser.add_argument("candidate", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--allow-configuration-change", action="store_true")
    args = parser.parse_args(argv)
    try:
        result = compare(load(args.baseline), load(args.candidate), args.allow_configuration_change)
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
