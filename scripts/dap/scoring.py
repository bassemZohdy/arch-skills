from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .contracts import ContractError, read_json, validate_config, validate_records
from .persistence import content_hash

def score_checks(checks: list[dict[str, Any]], dimension: str) -> dict[str, Any]:
    if not isinstance(checks, list):
        raise ContractError(f"{dimension} checks must be an array")
    included, passed, excluded = [], 0, []
    for check in checks:
        if not isinstance(check, dict) or check.get("result") not in {"pass", "fail", "unknown", "not_applicable"}:
            raise ContractError(f"{dimension} check has invalid result")
        result = check["result"]
        if result == "not_applicable":
            if not check.get("reason") or not check.get("authorized_by"):
                raise ContractError(f"{dimension} N/A checks require reason and authorized_by")
            excluded.append(check)
            continue
        included.append(check)
        passed += result == "pass"
    if not included:
        return {"assessable": False, "score": None, "passed": 0, "applicable": 0, "excluded": len(excluded), "checks": checks}
    return {
        "assessable": True,
        "score": round(100.0 * passed / len(included), 10),
        "passed": passed,
        "applicable": len(included),
        "excluded": len(excluded),
        "checks": checks,
    }
def _coverage(requirements: list[dict[str, Any]], designs: list[dict[str, Any]], links: list[dict[str, Any]]) -> tuple[dict[str, Any], dict[str, Any]]:
    active = {r["id"] for r in requirements if r.get("status") == "active"}
    significant = {d["id"] for d in designs if d.get("status") == "active" and d.get("significance") == "significant"}
    link_pairs = {(l.get("from"), l.get("to"), l.get("type")) for l in links}
    forward_ids = {rid for rid in active if any(
        (rid, did, "requirement_to_design") in link_pairs for did in significant
    )}
    backward_ids = {did for did in significant if any(
        (did, rid, "design_to_requirement") in link_pairs for rid in active
    )}
    forward = {"score": 100.0 * len(forward_ids) / len(active) if active else None, "covered": sorted(forward_ids), "uncovered": sorted(active), "denominator": len(active), "assessable": bool(active)}
    backward = {"score": 100.0 * len(backward_ids) / len(significant) if significant else None, "covered": sorted(backward_ids), "uncovered": sorted(significant), "denominator": len(significant), "assessable": bool(significant)}
    forward["uncovered"] = sorted(active - forward_ids)
    backward["uncovered"] = sorted(significant - backward_ids)
    return forward, backward
def _manifest(root: Path, excluded: set[str]) -> dict[str, Any]:
    files = []
    for path in sorted(root.rglob("*")):
        if not path.is_file():
            continue
        rel = path.relative_to(root).as_posix()
        if rel in excluded or rel.startswith("evaluations/"):
            continue
        data = path.read_bytes()
        files.append({"path": rel, "sha256": hashlib.sha256(data).hexdigest(), "bytes": len(data)})
    return {"files": files, "sha256": content_hash(files)}
def report_is_stale(root: Path, report: dict[str, Any]) -> bool:
    current = _manifest(Path(root), {"process/assessment.json"})
    return current["sha256"] != report.get("input_manifest", {}).get("sha256")

def evaluate_project(root: Path, config_path: Path | None = None) -> dict[str, Any]:
    root = Path(root)
    config = read_json(config_path or root / "process/config.json")
    validate_config(config)
    records = {
        "requirements": read_json(root / "requirements.json"),
        "design_elements": read_json(root / "design-elements.json"),
        "decisions": read_json(root / "decisions.json"),
        "traceability": read_json(root / "traceability.json"),
    }
    records = {k: (v if isinstance(v, list) else v.get(k, v)) for k, v in records.items()}
    validate_records(records)
    assessment = read_json(root / "process/assessment.json")
    q = score_checks(assessment["requirements_quality"], "requirements_quality")
    d = score_checks(assessment["decision_coverage"], "decision_coverage")
    a = score_checks(assessment["artifact_completeness"], "artifact_completeness")
    f, b = _coverage(records["requirements"], records["design_elements"], records["traceability"])
    metrics = {"requirements_quality": q, "decision_coverage": d, "forward_traceability": f, "backward_traceability": b, "traceability": {"assessable": f["assessable"] and b["assessable"], "score": min(f["score"], b["score"]) if f["assessable"] and b["assessable"] else None}, "artifact_completeness": a}
    weights = config["weights"]
    score = None
    if all(metrics[k]["assessable"] for k in ("requirements_quality", "decision_coverage", "traceability", "artifact_completeness")):
        score = sum(float(weights[k]) * metrics[k]["score"] for k in weights)
    state = read_json(root / "process/state.json")
    reviews = read_json(root / "process/reviews.json")
    blocking = list(state.get("blocking_findings", []))
    if config["governance"].get("security_review_required") and state.get("security_implication") and not reviews.get("security", {}).get("status") == "approved":
        blocking.append("security review is not approved")
    gates = {
        "convergence": state.get("convergence_status") == "passed",
        "reviews": not blocking,
        "configuration": True,
        "structural_integrity": True,
    }
    return {
        "framework_version": config["versions"]["framework"],
        "schema_version": config["versions"]["schema"],
        "rubric_version": config["versions"]["rubric"],
        "generated_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "metrics": metrics,
        "overall_score": round(score, 1) if score is not None else None,
        "assessable": score is not None,
        "gate": {"ready": all(gates.values()), "checks": gates, "blocking_findings": sorted(set(blocking))},
        "input_manifest": _manifest(root, {"process/assessment.json"}),
    }

