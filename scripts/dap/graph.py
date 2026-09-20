"""Typed design-stage trace chains shared by evaluation and RTM rendering."""
from __future__ import annotations


def active(record, scope):
    return record.get("status") == "active" and record.get("scope") == scope and record.get("priority") != "wont"


def trace_coverage(records, scope, evidence):
    index = {r["id"]: r for values in records.values() for r in values if isinstance(r, dict) and "id" in r}
    links = [l for l in records["traceability"] if l.get("evidence") and all(evidence(x) for x in l["evidence"])]
    edges = {(l["from"], l["to"], l["type"]) for l in links}
    requirements = [r for r in records["requirements"] if active(r, scope)]
    constraints = [r for r in records["constraints"] if active(r, scope)]
    designs = [d for d in records["design_elements"] if active(d, scope)]
    significant = [d for d in designs if d["significance"] == "significant"]
    accepted = {d["id"] for d in records["decisions"] if d["status"] == "accepted" and d["scope"] == scope}

    def sourced(r):
        source = index.get(r["source"], {})
        kind = "requirement" if r["id"].startswith("REQ-") else "constraint"
        return (source.get("status") == "confirmed" and r["source_revision"] == str(source.get("revision"))
                and bool(source.get("evidence")) and all(evidence(x) for x in source["evidence"])
                and (source.get("id"), r["id"], f"source_to_{kind}") in edges)

    def mapped(r, d):
        rid, did = r["id"], d["id"]
        kind = "requirement" if rid.startswith("REQ-") else "constraint"
        direct = (rid, did, f"{kind}_to_design") in edges or (did, rid, f"design_to_{kind}") in edges
        choices = [aid for aid in d["decision_ids"] if aid in accepted and
                   ((rid, aid, f"{kind}_to_decision") in edges or (aid, rid, f"decision_to_{kind}") in edges) and
                   ((aid, did, "decision_to_design") in edges or (did, aid, "design_to_decision") in edges)]
        return (direct or bool(choices)) and (not d["requires_decision"] or bool(choices))

    def verification(r, d):
        return sorted(v["id"] for v in records["verification"] if v["status"] in {"planned", "passed", "failed"}
                      and v["id"] in r["verification_ids"] and r["id"] in v["targets"] and d["id"] in v["targets"]
                      and (d["id"], v["id"], "design_to_verification") in edges)

    rows = []
    for r in requirements:
        mapped_designs = [d for d in designs if mapped(r, d)]
        plans = sorted({v for d in mapped_designs for v in verification(r, d)})
        rows.append({"id": r["id"], "priority": r["priority"], "source_confirmed": sourced(r),
                     "designs": [d["id"] for d in mapped_designs], "verification": plans,
                     "decisions": sorted({a for d in mapped_designs for a in d["decision_ids"] if a in accepted}),
                     "complete": bool(sourced(r) and mapped_designs and plans)})
    backward = {d["id"] for d in significant if any(sourced(r) and mapped(r, d) for r in requirements + constraints)}

    def metric(population, covered):
        ids = {r["id"] for r in population}
        return {"assessable": bool(ids), "score": 100 * len(covered) / len(ids) if ids else None,
                "numerator": len(covered), "denominator": len(ids), "covered": sorted(covered), "uncovered": sorted(ids - covered)}

    return metric(requirements, {r["id"] for r in rows if r["complete"]}), metric(significant, backward), rows
