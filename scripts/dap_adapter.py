#!/usr/bin/env python3
"""Validate the host-neutral adapter contract used by optional DAP scenarios."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

PROTOCOL_VERSION = "1.0.0"
SCHEMA_VERSION = "1.0"
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
        if not scenario["skill"].startswith("./skills/"):
            raise AdapterContractError(f"{location}.skill must be a repository skill path")
        if not scenario["fixture"].startswith("examples/"):
            raise AdapterContractError(f"{location}.fixture must be an examples path")
        assertions = scenario.get("assertions")
        if not isinstance(assertions, list) or not assertions:
            raise AdapterContractError(f"{location}.assertions must be non-empty")
        for assertion_index, assertion in enumerate(assertions):
            assertion_location = f"{location}.assertions[{assertion_index}]"
            if not isinstance(assertion, dict):
                raise AdapterContractError(f"{assertion_location} must be an object")
            assertion_type = assertion.get("type")
            if assertion_type not in ASSERTION_TYPES:
                raise AdapterContractError(
                    f"{assertion_location}.type is unsupported: {assertion_type!r}"
                )
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
    if result["status"] not in STATUSES:
        raise AdapterContractError(f"unsupported result.status: {result['status']!r}")
    _require_string(result["run_id"], "result.run_id")
    _require_string(result["started_at"], "result.started_at")
    _require_string(result["finished_at"], "result.finished_at")
    _validate_version_block(result["adapter"], "result.adapter")
    _validate_version_block(result["model"], "result.model")
    if not isinstance(result["assertions"], list):
        raise AdapterContractError("result.assertions must be an array")
    if not isinstance(result["evidence"], list):
        raise AdapterContractError("result.evidence must be an array")
    if result["status"] == "unavailable":
        _require_string(result.get("reason"), "result.reason")
    elif not result["evidence"]:
        raise AdapterContractError(
            "passed or failed executions must provide observable evidence"
        )
    return {
        "scenario_id": result["scenario_id"],
        "status": result["status"],
        "adapter": result["adapter"],
        "model": result["model"],
        "evidence_count": len(result["evidence"]),
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    scenarios_parser = subparsers.add_parser("validate-scenarios")
    scenarios_parser.add_argument("manifest", type=Path)

    result_parser = subparsers.add_parser("validate-result")
    result_parser.add_argument("result", type=Path)
    result_parser.add_argument("--scenario-id")

    args = parser.parse_args(argv)
    try:
        if args.command == "validate-scenarios":
            summary = validate_scenario_manifest(load_json(args.manifest))
        else:
            summary = validate_result(load_json(args.result), args.scenario_id)
    except AdapterContractError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
