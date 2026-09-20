"""Evidence-backed DAP evaluation of an explicit, read-only snapshot."""
from __future__ import annotations

from datetime import datetime, timezone
from fractions import Fraction
import json
import re
from pathlib import Path

from .contracts import (ContractError, DIMENSIONS, EVALUATOR_VERSION, FILES, KINDS,
                        read_json, validate_policy, validate_records, validate_versions, validate_weights)
from .graph import active, trace_coverage
from .persistence import content_hash
from .snapshot import Snapshot, report_is_stale


def score_checks(checks, dimension):
    included = [c for c in checks if c["result"] != "not_applicable"]
    passed = sum(c["result"] == "pass" for c in included)
    return {"assessable": bool(included), "score": 100 * passed / len(included) if included else None,
            "passed": passed, "applicable": len(included), "excluded": len(checks) - len(included),
            "unknown": sum(c["result"] == "unknown" for c in included),
            "failed": sum(c["result"] == "fail" for c in included), "checks": checks}


def expected_checks(records, config, catalog):
    scope = config.get("scope")
    dims = catalog["dimensions"]
    q = dims["requirements_quality"]
    result = {d: [] for d in ("requirements_quality", "decision_coverage", "artifact_completeness")}

    def add(dimension, target, criterion):
        result[dimension].append({"id": f"{dimension}:{target}:{criterion}", "dimension": dimension,
                                  "target_id": target, "criterion": criterion})

    for req in records["requirements"]:
        if active(req, scope):
            for criterion in q["per_requirement"]:
                add("requirements_quality", req["id"], criterion)
    for criterion in q["set_level"] + q["stability"]:
        add("requirements_quality", "baseline", criterion)
    decisions = {d["id"] for d in records["decisions"] if d["scope"] == scope and d["status"] in {"proposed", "accepted", "rejected"}}
    for design in records["design_elements"]:
        if active(design, scope) and design["requires_decision"]:
            decisions.update(design["decision_ids"] or [f"missing:{design['id']}"])
    for target in sorted(decisions):
        for criterion in dims["decision_coverage"]:
            add("decision_coverage", target, criterion)
    a = dims["artifact_completeness"]
    for section in a["arc42_sections"]:
        for criterion in ("content", "evidence", "consistency"):
            add("artifact_completeness", f"arc42:{section}", criterion)
    for group in a["supporting_groups"]:
        for criterion in ("presence", "schema", "baseline"):
            add("artifact_completeness", f"records:{group}", criterion)
    return result


def assess(expected, supplied, snapshot, config, records, findings):
    trusted = {}
    allowed = {c["id"]: c for checks in expected.values() for c in checks}
    if not isinstance(supplied, dict):
        raise ContractError("assessment must be keyed by dimension")
    seen = set()
    valid_decisions = {x["id"] for x in records["decisions"]}
    authorities = {config.get("governance", {}).get("decision_authority")}
    for dimension, checks in supplied.items():
        if dimension not in expected or not isinstance(checks, list):
            raise ContractError(f"invalid assessment dimension {dimension}")
        for check in checks:
            if not isinstance(check, dict) or check.get("id") not in allowed:
                raise ContractError("unknown or anonymous assessment check")
            cid = check["id"]
            if cid in seen:
                raise ContractError(f"duplicate assessment {cid}")
            seen.add(cid)
            if any(check.get(k) != allowed[cid][k] for k in ("dimension", "target_id", "criterion")) or check["dimension"] != dimension:
                raise ContractError(f"wrong assessment target/dimension: {cid}")
            result = check.get("result")
            if result not in {"pass", "fail", "unknown", "not_applicable"}:
                raise ContractError(f"invalid assessment result: {cid}")
            if check.get("baseline_revision") != config.get("baseline_revision") or not check.get("rationale") or not check.get("assessor"):
                findings.append(f"{cid}: missing rationale/assessor or stale revision")
                continue
            evidence = check.get("evidence")
            if not isinstance(evidence, list) or not evidence or not all(snapshot.evidence(x) for x in evidence):
                findings.append(f"{cid}: evidence missing or not in frozen input set")
                continue
            if check.get("subject_hash") != snapshot.subject_hash():
                findings.append(f"{cid}: assessment subject changed")
                continue
            if dimension == "artifact_completeness" and check["target_id"].startswith("arc42:") and result == "pass":
                locators = [e for e in evidence if e.startswith("architecture.md#")]
                substantive = False
                from .snapshot import normalized
                architecture = normalized("architecture.md", snapshot.data["architecture.md"]).decode("utf-8")
                sections = snapshot.json("@rubric")["dimensions"]["artifact_completeness"]["arc42_sections"]
                section_number = sections.index(check["target_id"].split(":", 1)[1]) + 1
                for locator in locators:
                    heading = locator.split("#", 1)[1]
                    if not re.match(rf"^0?{section_number}(?:[.)]|\s|$)", heading):
                        continue
                    match = re.search(r"(?m)^##\s+" + re.escape(heading) + r"\s*$", architecture)
                    if match:
                        body = re.split(r"(?m)^##\s", architecture[match.end():], maxsplit=1)[0].strip()
                        substantive |= bool(body and not re.fullmatch(r"(?:TBD|TODO|placeholder|\[.*\])\.?", body, re.I | re.S))
                if not substantive:
                    findings.append(f"{cid}: missing substantive arc42 section evidence")
                    continue
            if result == "not_applicable":
                if check.get("authorized_by") not in authorities or not check.get("reason") or not snapshot.evidence(check.get("authorization_evidence")):
                    raise ContractError(f"{cid}: unauthorized applicability exclusion")
                if dimension == "requirements_quality":
                    raise ContractError("mandatory convergence checks cannot be waived by N/A")
            if dimension == "decision_coverage" and check["target_id"] not in valid_decisions:
                check = dict(check, result="fail", rationale="inventoried significant decision has no ADR")
            trusted[cid] = check
    return {d: [trusted.get(c["id"], dict(c, result="unknown", rationale="required check has no current valid assessment",
                                        evidence=[], baseline_revision=config.get("baseline_revision")))
                for c in checks] for d, checks in expected.items()}


def _time(value):
    try:
        stamp = datetime.fromisoformat(value.replace("Z", "+00:00"))
        return stamp if stamp.tzinfo is not None else None
    except (TypeError, ValueError, AttributeError):
        return None


def review_findings(records, reviews, state, config, snapshot):
    issues = []
    policy = config.get("governance", {})
    scope = config.get("scope")
    required = set()
    applicable = [d for d in records["decisions"] if d["scope"] == scope and d["status"] in {"accepted", "proposed"}]
    applicable += [d for d in records["design_elements"] if active(d, scope)]
    for item in applicable:
        implications = item["implications"]
        if item["id"].startswith("ADR-"):
            required.add(("architecture", item["id"]))
            if item["status"] != "accepted":
                issues.append(f"{item['id']}: significant decision is not accepted")
        for role in ("security", "privacy", "compliance", "irreversible", "high_risk", "cross_team"):
            if implications[role]:
                required.add((role, item["id"]))
        threshold = policy.get("cost_threshold", {})
        if (implications["currency"] != threshold.get("currency") or implications["horizon"] != threshold.get("horizon")
                or implications["cost"] > threshold.get("amount", -1)):
            required.add(("cost", item["id"]))
    now = datetime.now(timezone.utc)
    if not isinstance(reviews, list):
        return ["reviews must be a list of baseline-bound human dispositions"]
    for role, target in sorted(required):
        authorized = policy.get("reviewers", {}).get(role, [])
        matches = []
        for review in reviews:
            at = _time(review.get("reviewed_at"))
            expiry = _time(review.get("expires_at"))
            if (review.get("kind") == role and target in review.get("targets", [])
                    and review.get("status") == "approved" and review.get("reviewer") in authorized
                    and review.get("baseline_revision") == config.get("baseline_revision")
                    and review.get("subject_hash") == snapshot.subject_hash()
                    and at and at <= now and expiry and expiry > now
                    and review.get("evidence") and all(snapshot.evidence(e) for e in review["evidence"])):
                matches.append(review)
        if not matches:
            issues.append(f"{target}: {role} review missing, pending, stale, expired or unauthorized")
    for exception in records["exceptions"]:
        if exception["status"] in {"rejected", "expired"}:
            continue
        constraint = next((c for c in records["constraints"] if c["id"] == exception["obligation"]), {})
        if (exception["status"] != "approved" or not constraint.get("waivable")
                or exception.get("approved_by") != policy.get("decision_authority")
                or exception["baseline_revision"] != config.get("baseline_revision")
                or not _time(exception["expires_at"]) or _time(exception["expires_at"]) <= now
                or not exception["evidence"] or not all(snapshot.evidence(e) for e in exception["evidence"])):
            issues.append(f"{exception['id']}: invalid or unapproved exception")
    for kind in ("questions", "assumptions"):
        for record in records[kind]:
            if record["status"] == "open" and record["blocking"]:
                issues.append(f"{record['id']}: unresolved blocking {kind}")
    for key in ("blocking_findings", "mandatory_conflicts", "incomplete_operations", "pending_reviews"):
        if state.get(key):
            issues.append(f"{key}: {state[key]}")
    return issues


def empty_report(message):
    return {"evaluator": f"dap/{EVALUATOR_VERSION}", "generated_at": datetime.now(timezone.utc).isoformat(),
            "assessable": False, "overall_score": None, "metrics": {}, "findings": [message],
            "gate": {"ready": False, "checks": {"structural_integrity": False}, "blocking_findings": [message]},
            "input_manifest": {}}


def evaluate_project(root, config_path=None):
    try:
        return _evaluate_project(root, config_path)
    except (ValueError, KeyError, TypeError, AttributeError, OSError) as exc:
        return empty_report(f"invalid assessment/state contract: {exc}")


def _evaluate_project(root, config_path=None):
    try:
        # Reject historical wire versions before requiring the current manifest.
        # This is only a compatibility preflight; calculation revalidates frozen bytes.
        validate_versions(read_json(config_path or Path(root) / "process/config.json"))
        snapshot = Snapshot(root, config_path)
        config = snapshot.json("@config" if config_path else "process/config.json")
        validate_versions(config)
        records = {kind: snapshot.json(path) for kind, path in FILES.items()}
        validate_records(records)
        for kind in KINDS:
            for record in records[kind]:
                if record["status"] not in {"superseded", "deprecated", "rejected", "expired"}:
                    if any(not snapshot.evidence(locator) for locator in record.get("evidence", [])):
                        raise ContractError(f"{record['id']}: record evidence does not resolve in the frozen manifest")
        catalog = snapshot.json("@rubric")
        if catalog["rubric_version"] != config["versions"]["rubric"]:
            raise ContractError("rubric content/version mismatch")
    except (OSError, ValueError, KeyError, TypeError) as exc:
        return empty_report(str(exc))
    findings = []
    policy_ok = weights_ok = True
    for validator in (validate_policy, lambda c: validate_weights(c.get("weights"))):
        try:
            validator(config)
        except (ContractError, TypeError) as exc:
            findings.append(str(exc))
            if validator is validate_policy:
                policy_ok = False
            else:
                weights_ok = False
    if not snapshot.evidence(config.get("approval_evidence")):
        policy_ok = False
        findings.append("configuration approval evidence unavailable")
    expected = expected_checks(records, config, catalog)
    try:
        checks = assess(expected, snapshot.json("process/assessment.json"), snapshot, config, records, findings)
        assessment_ok = True
    except (ContractError, KeyError, TypeError) as exc:
        findings.append(str(exc))
        checks = {d: [dict(c, result="unknown") for c in rows] for d, rows in expected.items()}
        assessment_ok = False
    metrics = {d: score_checks(rows, d) for d, rows in checks.items()}
    f, b, rows = trace_coverage(records, config.get("scope"), snapshot.evidence)
    metrics.update(forward_traceability=f, backward_traceability=b,
                   traceability={"assessable": f["assessable"] and b["assessable"],
                                 "score": min(f["score"], b["score"]) if f["assessable"] and b["assessable"] else None})
    if not f["denominator"]:
        metrics["requirements_quality"]["assessable"] = False
        metrics["requirements_quality"]["score"] = None
        findings.append("required active in-scope requirement population is empty")
    envelope = snapshot.json("process/state.json")
    state = envelope.get("state", {})
    checkpoint_ok = (type(envelope.get("revision")) is int and envelope["revision"] > 0
                     and envelope.get("state_hash") == content_hash(state))
    required_state = {"run_id", "stage", "mode", "baseline_revision", "versions", "round", "elapsed_minutes",
                      "answered_questions", "pending_questions", "gate_results", "pending_reviews", "next_action",
                      "subject_hash", "stability", "blocking_findings", "mandatory_conflicts", "incomplete_operations"}
    checkpoint_ok = checkpoint_ok and required_state.issubset(state) and state.get("versions") == config["versions"]
    checkpoint_ok = checkpoint_ok and state.get("baseline_revision") == config.get("baseline_revision") and state.get("subject_hash") == snapshot.subject_hash()
    checkpoint_ok = checkpoint_ok and state.get("stage") in {"preparation", "interview", "design", "review", "documentation", "baselined"}
    checkpoint_ok = checkpoint_ok and state.get("mode") in {"interview", "create", "update"}
    checkpoint_ok = checkpoint_ok and all(isinstance(state.get(k), list) for k in (
        "answered_questions", "pending_questions", "pending_reviews", "blocking_findings", "mandatory_conflicts", "incomplete_operations"))
    history = [json.loads(line) for line in snapshot.data["process/history.jsonl"].decode("utf-8").splitlines() if line.strip()]
    checkpoint_ok = checkpoint_ok and bool(history) and all(isinstance(event, dict) and event for event in history)
    if not checkpoint_ok:
        findings.append("checkpoint integrity, schema, versions or subject baseline invalid")
    stability = state.get("stability", {})
    req_hash = content_hash({k: records[k] for k in ("requirements", "constraints", "sources")})
    owners = {r["owner"] for r in records["requirements"] if active(r, config.get("scope"))}
    stability_ok = (stability.get("confirmed") is True and owners.issubset(set(stability.get("participants", [])))
                    and bool(owners) and stability.get("before_hash") == req_hash == stability.get("after_hash")
                    and stability.get("round_id") and stability.get("evidence")
                    and all(snapshot.evidence(e) for e in stability["evidence"]))
    issues = review_findings(records, snapshot.json("process/reviews.json"), state, config, snapshot)
    findings.extend(issues)
    current = snapshot.unchanged()
    all_pass = lambda dimension: bool(checks[dimension]) and all(c["result"] in {"pass", "not_applicable"} for c in checks[dimension])
    limits = config.get("limits", {})
    budget_ok = (type(state.get("round")) is int and type(state.get("elapsed_minutes")) in (int, float)
                 and 0 <= state["round"] <= limits.get("max_interview_rounds", -1)
                 and 0 <= state["elapsed_minutes"] <= limits.get("max_interview_minutes", -1))
    current_records = all(r["baseline_revision"] == config.get("baseline_revision") for kind in KINDS
                          for r in records[kind] if r["status"] not in {"superseded", "deprecated", "rejected", "expired"})
    gates = {"configuration": policy_ok and weights_ok, "structural_integrity": checkpoint_ok and current_records and assessment_ok,
             "convergence": bool(all_pass("requirements_quality") and stability_ok and budget_ok),
             "traceability": f["score"] == 100 and b["score"] == 100,
             "decisions": all_pass("decision_coverage"), "artifacts": all_pass("artifact_completeness"),
             "reviews": not issues, "freshness": current,
             "assessable": all(metrics[d]["assessable"] for d in DIMENSIONS)}
    score = None
    if weights_ok and assessment_ok and all(metrics[d]["assessable"] for d in DIMENSIONS):
        exact = {}
        for dimension in DIMENSIONS:
            if dimension == "traceability":
                exact[dimension] = min(Fraction(f["numerator"], f["denominator"]), Fraction(b["numerator"], b["denominator"])) * 100
            else:
                m = metrics[dimension]
                exact[dimension] = Fraction(m["passed"], m["applicable"]) * 100
        score = sum(Fraction(str(config["weights"][d])) * exact[d] for d in DIMENSIONS)
    findings.extend(f"gate failed: {name}" for name, passed in gates.items() if not passed)
    return {"framework_version": config["versions"]["framework"], "schema_version": config["versions"]["schema"],
            "rubric_version": config["versions"]["rubric"], "configuration_version": config.get("configuration_version"),
            "baseline_revision": config.get("baseline_revision"), "evaluator": f"dap/{EVALUATOR_VERSION}",
            "generated_at": datetime.now(timezone.utc).isoformat(), "metrics": metrics,
            "overall_score": round(float(score), 1) if score is not None else None,
            "overall_exact": str(score) if score is not None else None, "assessable": score is not None,
            "gate": {"ready": all(gates.values()), "checks": gates, "blocking_findings": sorted(set(findings))},
            "findings": sorted(set(findings)), "trace_rows": rows, "subject_hash": snapshot.subject_hash(),
            "input_manifest": snapshot.manifest}

