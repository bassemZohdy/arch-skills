from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

FRAMEWORK_VERSION = "1.0.0"
SCHEMA_VERSION = "1.0.0"
RUBRIC_VERSION = "1.0.0"
RESULTS = {"pass", "fail", "unknown", "not_applicable"}
ID_PATTERNS = {
    "REQ": re.compile(r"^REQ-[0-9]{3,}$"),
    "CON": re.compile(r"^CON-[0-9]{3,}$"),
    "DES": re.compile(r"^DES-[0-9]{3,}$"),
    "ADR": re.compile(r"^ADR-[0-9]{3,}$"),
    "VER": re.compile(r"^VER-[0-9]{3,}$"),
    "Q": re.compile(r"^Q-[0-9]{3,}$"),
    "ASM": re.compile(r"^ASM-[0-9]{3,}$"),
    "EXC": re.compile(r"^EXC-[0-9]{3,}$"),
}
class ContractError(ValueError):
    pass
def read_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ContractError(f"missing record: {path}") from exc
    except json.JSONDecodeError as exc:
        raise ContractError(f"invalid JSON: {path}: {exc}") from exc
def _version(value: Any, name: str) -> None:
    if not isinstance(value, str) or not re.fullmatch(r"[0-9]+\.[0-9]+\.[0-9]+", value):
        raise ContractError(f"{name} must be semantic version x.y.z")
def validate_config(config: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(config, dict):
        raise ContractError("configuration must be an object")
    versions = config.get("versions")
    if not isinstance(versions, dict):
        raise ContractError("versions are required")
    for key in ("framework", "schema", "rubric"):
        _version(versions.get(key), f"versions.{key}")
    weights = config.get("weights")
    if not isinstance(weights, dict):
        raise ContractError("weights are required")
    required = ("requirements_quality", "decision_coverage", "traceability", "artifact_completeness")
    if set(weights) != set(required):
        raise ContractError(f"weights must contain exactly {required}")
    if any(not isinstance(weights[k], (int, float)) or weights[k] < 0 for k in required):
        raise ContractError("weights must be non-negative numbers")
    if abs(sum(float(weights[k]) for k in required) - 1.0) > 1e-9:
        raise ContractError("weights must sum to 1")
    if weights["traceability"] < max(weights[k] for k in required if k != "traceability"):
        raise ContractError("traceability must be the largest configured weight")
    governance = config.get("governance")
    if not isinstance(governance, dict) or not governance.get("decision_authority"):
        raise ContractError("governance.decision_authority is required")
    if not isinstance(governance.get("reviewers"), list) or not governance["reviewers"]:
        raise ContractError("governance.reviewers must contain at least one reviewer")
    limits = config.get("limits")
    if not isinstance(limits, dict):
        raise ContractError("limits are required")
    for key in ("max_interview_rounds", "max_interview_minutes", "periodic_review_days"):
        if not isinstance(limits.get(key), int) or limits[key] <= 0:
            raise ContractError(f"limits.{key} must be a positive integer")
    return config
def validate_id(value: str) -> None:
    if not isinstance(value, str):
        raise ContractError("record id must be a string")
    prefix = value.split("-", 1)[0]
    if prefix not in ID_PATTERNS or not ID_PATTERNS[prefix].fullmatch(value):
        raise ContractError(f"invalid stable id: {value}")
def validate_records(records: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(records, dict):
        raise ContractError("records must be an object")
    for kind in ("requirements", "design_elements", "decisions"):
        values = records.get(kind, [])
        if not isinstance(values, list):
            raise ContractError(f"{kind} must be an array")
        seen = set()
        for item in values:
            if not isinstance(item, dict):
                raise ContractError(f"{kind} entries must be objects")
            validate_id(item.get("id"))
            if item["id"] in seen:
                raise ContractError(f"duplicate id: {item['id']}")
            seen.add(item["id"])
    links = records.get("traceability", [])
    if not isinstance(links, list):
        raise ContractError("traceability must be an array")
    for link in links:
        if not isinstance(link, dict) or not link.get("from") or not link.get("to") or not link.get("type"):
            raise ContractError("trace links require from, to and type")
    return records

