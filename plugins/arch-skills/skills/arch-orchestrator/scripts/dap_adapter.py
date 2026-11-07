#!/usr/bin/env python3
"""Validate the host-neutral adapter contract used by optional DAP scenarios."""

from __future__ import annotations

import argparse
from datetime import datetime
import json
import sys
from pathlib import Path, PurePosixPath
from typing import Any

PROTOCOL_VERSION = "1.0.0"
SCHEMA_VERSION = "2.0"
FIXTURES = {"greenfield", "create", "brownfield", "interrupted", "blocking-review", "interview", "update"}
STATUSES = {"passed", "failed", "unavailable"}
ASSERTION_TYPES = {
    "file_exists",
    "file_contains",
    "json_path_equals",
    "response_contains",
    "response_not_contains",
    "gate_ready",
    "evidence_present",
}
FORBIDDEN_HOST_KEYS = {"harness", "model_name", "cli", "tool_api", "credential"}


class AdapterContractError(ValueError):
    """Raised when an adapter manifest or result violates the contract."""


def load_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise AdapterContractError(f"cannot read JSON file {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise AdapterContractError(f"{path} must contain a JSON object")
    return value


def _require_string(value: Any, label: str) -> None:
    if not isinstance(value, str) or not value.strip():
        raise AdapterContractError(f"{label} must be a non-empty string")


def _relative_path(value: Any, label: str) -> None:
    _require_string(value, label)
    if "\\" in value or ":" in value or PurePosixPath(value).is_absolute() or ".." in value.split("/"):
        raise AdapterContractError(f"{label} must stay within the workspace")


def _timestamp(value: Any, label: str):
    _require_string(value, label)
    try:
        result = datetime.fromisoformat(value.replace("Z", "+00:00"))
        if result.tzinfo is None:
            raise ValueError("timezone required")
        return result
    except ValueError as exc:
        raise AdapterContractError(f"{label} must be a timezone-aware ISO timestamp") from exc


def _reject_host_keys(value: Any, location: str = "manifest") -> None:
    if isinstance(value, dict):
        for key, child in value.items():
            if key in FORBIDDEN_HOST_KEYS:
                raise AdapterContractError(
                    f"{location}.{key} is host-specific; configure it in the external adapter"
                )
            _reject_host_keys(child, f"{location}.{key}")
    elif isinstance(value, list):
        for index, child in enumerate(value):
            _reject_host_keys(child, f"{location}[{index}]")


def validate_scenario_manifest(manifest: dict[str, Any]) -> dict[str, Any]:
    if manifest.get("schema_version") != SCHEMA_VERSION:
        raise AdapterContractError(f"schema_version must be {SCHEMA_VERSION!r}")
    if manifest.get("adapter_protocol_version") != PROTOCOL_VERSION:
        raise AdapterContractError(
            f"adapter_protocol_version must be {PROTOCOL_VERSION!r}"
        )
    _reject_host_keys(manifest)
    scenarios = manifest.get("scenarios")
    if not isinstance(scenarios, list) or not scenarios:
        raise AdapterContractError("scenarios must be a non-empty array")

    ids: set[str] = set()
    for index, scenario in enumerate(scenarios):
        location = f"scenarios[{index}]"
        if not isinstance(scenario, dict):
            raise AdapterContractError(f"{location} must be an object")
        for key in ("id", "name", "skill", "fixture", "prompt"):
            _require_string(scenario.get(key), f"{location}.{key}")
        scenario_id = scenario["id"]
        if scenario_id in ids:
            raise AdapterContractError(f"duplicate scenario id: {scenario_id}")
        ids.add(scenario_id)
        _relative_path(scenario["skill"], f"{location}.skill")
        if not scenario["skill"].startswith("./skills/") or len(PurePosixPath(scenario["skill"]).parts) != 2:
            raise AdapterContractError(f"{location}.skill must be a repository skill path")
        if scenario["fixture"] not in {f"generated:{name}" for name in FIXTURES}:
            raise AdapterContractError(f"{location}.fixture must name a current generated fixture")
        assertions = scenario.get("assertions")
        if not isinstance(assertions, list) or not assertions:
            raise AdapterContractError(f"{location}.assertions must be non-empty")
        for assertion_index, assertion in enumerate(assertions):
            assertion_location = f"{location}.assertions[{assertion_index}]"
            if not isinstance(assertion, dict):
                raise AdapterContractError(f"{assertion_location} must be an object")
            assertion_type = assertion.get("type")
            if not isinstance(assertion_type, str) or assertion_type not in ASSERTION_TYPES:
                raise AdapterContractError(
                    f"{assertion_location}.type is unsupported: {assertion_type!r}"
                )
            if assertion_type in {"file_exists", "file_contains", "json_path_equals"}:
                _relative_path(assertion.get("path"), f"{assertion_location}.path")
            if assertion_type in {"file_contains", "response_contains", "response_not_contains"}:
                _require_string(assertion.get("value"), f"{assertion_location}.value")
            if assertion_type == "evidence_present":
                _require_string(assertion.get("field"), f"{assertion_location}.field")
            if assertion_type == "gate_ready" and type(assertion.get("expected")) is not bool:
                raise AdapterContractError(f"{assertion_location}.expected must be boolean")
            if assertion_type == "json_path_equals":
                pointer = assertion.get("pointer")
                if (not isinstance(pointer, str) or (pointer and not pointer.startswith("/"))
                        or "expected" not in assertion):
                    raise AdapterContractError(f"{assertion_location} requires a JSON pointer and expected value")
    return {"schema_version": SCHEMA_VERSION, "scenario_count": len(scenarios)}


def _validate_version_block(value: Any, label: str) -> None:
    if not isinstance(value, dict):
        raise AdapterContractError(f"{label} must be an object")
    _require_string(value.get("id"), f"{label}.id")
    _require_string(value.get("version"), f"{label}.version")


def validate_result(result: dict[str, Any], scenario_id: str | None = None) -> dict[str, Any]:
    required = (
        "protocol_version",
        "scenario_id",
        "status",
        "run_id",
        "adapter",
        "model",
        "started_at",
        "finished_at",
        "assertions",
        "evidence",
    )
    for key in required:
        if key not in result:
            raise AdapterContractError(f"result is missing {key!r}")
    if result["protocol_version"] != PROTOCOL_VERSION:
        raise AdapterContractError(
            f"result.protocol_version must be {PROTOCOL_VERSION!r}"
        )
    _require_string(result["scenario_id"], "result.scenario_id")
    if scenario_id and result["scenario_id"] != scenario_id:
        raise AdapterContractError("result.scenario_id does not match the requested scenario")
    if not isinstance(result["status"], str) or result["status"] not in STATUSES:
        raise AdapterContractError(f"unsupported result.status: {result['status']!r}")
    _require_string(result["run_id"], "result.run_id")
    started = _timestamp(result["started_at"], "result.started_at")
    finished = _timestamp(result["finished_at"], "result.finished_at")
    if finished < started:
        raise AdapterContractError("result.finished_at precedes started_at")
    _validate_version_block(result["adapter"], "result.adapter")
    _validate_version_block(result["model"], "result.model")
    if not isinstance(result["assertions"], list):
        raise AdapterContractError("result.assertions must be an array")
    if not isinstance(result["evidence"], list):
        raise AdapterContractError("result.evidence must be an array")
    for assertion in result["assertions"]:
        if (not isinstance(assertion, dict) or not isinstance(assertion.get("type"), str)
                or assertion["type"] not in ASSERTION_TYPES
                or type(assertion.get("passed")) is not bool):
            raise AdapterContractError("result assertions require a supported type and boolean passed")
    for evidence in result["evidence"]:
        if not isinstance(evidence, dict):
            raise AdapterContractError("result evidence must be an object with a relative path")
        _relative_path(evidence.get("path"), "result.evidence.path")
    if result["status"] == "unavailable":
        _require_string(result.get("reason"), "result.reason")
        if result["assertions"]:
            raise AdapterContractError("unavailable execution cannot claim executed assertions")
    elif not result["evidence"]:
        raise AdapterContractError(
            "passed or failed executions must provide observable evidence"
        )
    else:
        if not result["assertions"]:
            raise AdapterContractError("executed results require assertion outcomes")
        passed = all(a["passed"] for a in result["assertions"])
        if (result["status"] == "passed") != passed:
            raise AdapterContractError("result status contradicts assertion outcomes")
    return {
        "scenario_id": result["scenario_id"],
        "status": result["status"],
        "adapter": result["adapter"],
        "model": result["model"],
        "evidence_count": len(result["evidence"]),
    }


def validate_execution(result: dict[str, Any], manifest: dict[str, Any], workspace: Path) -> dict[str, Any]:
    """Check that an executed result covers exactly the requested assertions and files."""
    validate_scenario_manifest(manifest)
    scenarios = {item["id"]: item for item in manifest["scenarios"]}
    scenario = scenarios.get(result.get("scenario_id"))
    if scenario is None:
        raise AdapterContractError("result.scenario_id is not present in the scenario manifest")
    summary = validate_result(result, result["scenario_id"])
    if result["status"] == "unavailable":
        return summary | {"execution_checked": False, "reason": result["reason"]}
    expected = {
        f"{scenario['id']}:{index + 1}": assertion["type"]
        for index, assertion in enumerate(scenario["assertions"])
    }
    actual = {}
    for assertion in result["assertions"]:
        assertion_id = assertion.get("assertion_id")
        _require_string(assertion_id, "result.assertions[].assertion_id")
        if assertion_id in actual:
            raise AdapterContractError(f"duplicate assertion outcome: {assertion_id}")
        if assertion_id not in expected:
            raise AdapterContractError(f"unexpected assertion outcome: {assertion_id}")
        if assertion["type"] != expected[assertion_id]:
            raise AdapterContractError(f"assertion type mismatch for {assertion_id}")
        actual[assertion_id] = assertion["type"]
    if set(actual) != set(expected):
        missing = sorted(set(expected) - set(actual))
        raise AdapterContractError(f"missing assertion outcomes: {missing}")
    workspace = workspace.resolve()
    if not workspace.is_dir():
        raise AdapterContractError(f"workspace does not exist: {workspace}")
    for evidence in result["evidence"]:
        path = workspace / PurePosixPath(evidence["path"])
        if not path.resolve().is_relative_to(workspace) or not path.is_file():
            raise AdapterContractError(f"evidence file is missing or escapes workspace: {evidence['path']}")
    return summary | {"execution_checked": True, "assertion_count": len(actual)}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    scenarios_parser = subparsers.add_parser("validate-scenarios")
    scenarios_parser.add_argument("manifest", type=Path)

    result_parser = subparsers.add_parser("validate-result")
    result_parser.add_argument("result", type=Path)
    result_parser.add_argument("--scenario-id")

    execution_parser = subparsers.add_parser("validate-execution")
    execution_parser.add_argument("result", type=Path)
    execution_parser.add_argument("manifest", type=Path)
    execution_parser.add_argument("--workspace", type=Path, required=True)

    args = parser.parse_args(argv)
    try:
        if args.command == "validate-scenarios":
            summary = validate_scenario_manifest(load_json(args.manifest))
        elif args.command == "validate-result":
            summary = validate_result(load_json(args.result), args.scenario_id)
        else:
            summary = validate_execution(load_json(args.result), load_json(args.manifest), args.workspace)
    except AdapterContractError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
