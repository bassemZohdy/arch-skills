"""Versioned structural contracts; semantic judgments remain evidenced assessments."""
from __future__ import annotations

import json
import math
import re
from pathlib import Path
from jsonschema import Draft202012Validator

FRAMEWORK_VERSION = "1.0.0"
SCHEMA_VERSION = "2.0.0"
RUBRIC_VERSION = "1.0.0"
EVALUATOR_VERSION = "2.0.1"
FRAMEWORK = Path(__file__).resolve().parents[2] / "framework"
RESULTS = {"pass", "fail", "unknown", "not_applicable"}
KINDS = {"sources": "SRC", "requirements": "REQ", "constraints": "CON",
         "design_elements": "DES", "decisions": "ADR", "verification": "VER",
         "questions": "Q", "assumptions": "ASM", "exceptions": "EXC"}
FILES = {"sources": "sources.json", "requirements": "requirements.json",
         "constraints": "constraints.json", "design_elements": "design-elements.json",
         "decisions": "decisions.json", "verification": "verification.json",
         "questions": "process/questions.json", "assumptions": "process/assumptions.json",
         "exceptions": "process/exceptions.json", "traceability": "traceability.json"}
DIMENSIONS = ("requirements_quality", "decision_coverage", "traceability", "artifact_completeness")


class ContractError(ValueError):
    pass


def read_json(path):
    try:
        return json.loads(Path(path).read_text(encoding="utf-8"),
                          parse_constant=lambda x: (_ for _ in ()).throw(ValueError(x)))
    except (OSError, ValueError) as exc:
        raise ContractError(f"cannot read JSON {path}: {exc}") from exc


def require(value, label):
    if not isinstance(value, str) or not value.strip():
        raise ContractError(f"{label} must be a nonempty string")


def validate_versions(config):
    expected = {"framework": FRAMEWORK_VERSION, "schema": SCHEMA_VERSION, "rubric": RUBRIC_VERSION}
    if config.get("versions") != expected:
        raise ContractError(f"unsupported versions {config.get('versions')}; supported {expected}; historical assessment unavailable")


def validate_weights(weights):
    if not isinstance(weights, dict) or set(weights) != set(DIMENSIONS):
        raise ContractError("four explicit scoring weights are required")
    if any(type(x) not in (int, float) or not math.isfinite(x) or x < 0 for x in weights.values()):
        raise ContractError("weights must be finite nonnegative numbers, not booleans")
    from decimal import Decimal
    if sum(Decimal(str(x)) for x in weights.values()) != Decimal(1):
        raise ContractError("weights must sum to exactly 1")
    if weights["traceability"] < max(weights.values()):
        raise ContractError("traceability must be the largest weight")


def validate_policy(config):
    for key in ("configuration_version", "scope", "approved_by", "approval_evidence", "artifact_owner",
                "delivery_maintainer", "architectural_reviewer", "periodic_review_owner", "evidence_retention"):
        require(config.get(key), key)
    if type(config.get("baseline_revision")) is not int or config["baseline_revision"] < 1:
        raise ContractError("positive baseline_revision required")
    policy = config.get("governance", {})
    require(policy.get("decision_authority"), "decision_authority")
    for key in ("risk_categories", "cross_team_rule", "async_queue_owner"):
        require(policy.get(key), key)
    reviewers = policy.get("reviewers")
    if not isinstance(reviewers, dict) or not reviewers.get("architecture"):
        raise ContractError("reviewers must map review types to authorized human identities")
    for role, identities in reviewers.items():
        if not isinstance(identities, list) or not identities or any(not isinstance(x, str) or not x.strip() for x in identities):
            raise ContractError(f"invalid reviewers for {role}")
    if config["approved_by"] != policy["decision_authority"]:
        raise ContractError("configuration approval must name the configured human authority")
    threshold = policy.get("cost_threshold", {})
    if type(threshold.get("amount")) not in (int, float) or not math.isfinite(threshold["amount"]) or threshold["amount"] < 0:
        raise ContractError("explicit finite cost threshold required")
    for key in ("currency", "horizon"):
        require(threshold.get(key), f"cost_threshold.{key}")
    for key in ("max_interview_rounds", "max_interview_minutes", "periodic_review_days"):
        value = config.get("limits", {}).get(key)
        if type(value) is not int or value < 1:
            raise ContractError(f"positive {key} required")
    if type(policy.get("async_review_due_hours")) is not int or policy["async_review_due_hours"] < 1:
        raise ContractError("positive async_review_due_hours required")


def validate_config(config):
    if not isinstance(config, dict):
        raise ContractError("configuration must be an object")
    validate_versions(config)
    validate_weights(config.get("weights"))
    validate_policy(config)
    return config


def validate_id(value):
    if not isinstance(value, str) or not re.fullmatch(r"(?:SRC|REQ|CON|DES|ADR|VER|Q|ASM|EXC)-[0-9]{3,}", value):
        raise ContractError(f"invalid stable ID: {value}")


def validate_records(records):
    schema = read_json(FRAMEWORK / "project-schema.json")
    errors = sorted(Draft202012Validator(schema).iter_errors(records), key=lambda e: str(e.path))
    if errors:
        raise ContractError("; ".join(f"{'.'.join(map(str, e.path))}: {e.message}" for e in errors[:12]))
    index = {}
    for kind in KINDS:
        for item in records[kind]:
            rid = item["id"]
            if rid in index:
                raise ContractError(f"duplicate global ID {rid}")
            index[rid] = item
            if kind == "requirements" and item["type"] == "quality" and "scenario" not in item:
                raise ContractError(f"{rid}: quality scenario required")
    pairs = {"source": "SRC", "requirement": "REQ", "constraint": "CON", "design": "DES", "decision": "ADR", "verification": "VER"}
    seen = set()
    for link in records["traceability"]:
        a, b = link["type"].split("_to_")
        for end, kind in (("from", a), ("to", b)):
            target = link[end]
            if target not in index or not target.startswith(pairs[kind] + "-"):
                raise ContractError(f"invalid {link['type']} endpoint {target}")
        key = (link["from"], link["to"], link["type"])
        if key in seen:
            raise ContractError(f"duplicate trace link {key}")
        seen.add(key)
    for kind, fields in {"requirements": ("source", "verification_ids", "dependencies"),
                         "constraints": ("source", "verification_ids"),
                         "design_elements": ("decision_ids",), "verification": ("targets",),
                         "decisions": ("dependencies", "supersedes"), "exceptions": ("obligation",)}.items():
        for record in records[kind]:
            for field in fields:
                values = record[field] if isinstance(record[field], list) else [record[field]]
                for target in values:
                    if target not in index:
                        if field == "decision_ids" and re.fullmatch(r"ADR-[0-9]{3,}", target):
                            continue  # Missing significant decisions remain in the score population.
                        raise ContractError(f"{record['id']}.{field}: unresolved ID {target}")
                    expected_prefix = {"source": "SRC-", "verification_ids": "VER-", "decision_ids": "ADR-", "supersedes": "ADR-", "obligation": "CON-"}.get(field)
                    if expected_prefix and not target.startswith(expected_prefix):
                        raise ContractError(f"{record['id']}.{field}: wrong record kind {target}")
            if kind == "verification" and record["status"] in {"passed", "failed"} and not record["evidence"]:
                raise ContractError(f"{record['id']}: executed verification requires evidence")
    return records
