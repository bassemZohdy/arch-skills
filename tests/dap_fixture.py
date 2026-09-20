"""Synthetic complete baseline for deterministic tests; no real approval is claimed."""
from copy import deepcopy
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from dap.contracts import FILES, FRAMEWORK, read_json
from dap.persistence import content_hash
from dap.scoring import expected_checks
from dap.snapshot import Snapshot, REQUIRED


def write(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


def make_project(root):
    root = Path(root)
    root.mkdir(parents=True, exist_ok=True)
    config = read_json(FRAMEWORK / "config.example.json")
    for key in ("artifact_owner", "delivery_maintainer", "architectural_reviewer", "periodic_review_owner"):
        config[key] = "fixture-human"
    config.update(approved_by="fixture-human", approval_evidence="evidence.md#Configuration", evidence_retention="one test run")
    policy = config["governance"]
    policy.update(decision_authority="fixture-human", risk_categories="high requires review; uncertainty escalates",
                  cross_team_rule="any changed cross-team contract", async_queue_owner="fixture-human")
    policy["reviewers"] = {key: ["fixture-human"] for key in policy["reviewers"]}
    base = dict(owner="fixture-human", source="SRC-001", source_revision="1", revision=1, baseline_revision=1)
    implications = dict(security=False, privacy=False, compliance=False, irreversible=False,
                        high_risk=False, cross_team=False, cost=100, currency="AED", horizon="annual")
    records = {key: [] for key in FILES}
    records["sources"] = [dict(base, id="SRC-001", source="evidence.md", status="confirmed", evidence=["evidence.md#Interview"])]
    records["requirements"] = [dict(base, id="REQ-001", statement="Return the stored greeting to the caller.",
        status="active", type="functional", priority="must", scope="release-1", acceptance_criteria=["GET returns configured greeting"],
        verification_ids=["VER-001"], dependencies=[])]
    records["design_elements"] = [dict(base, id="DES-001", name="Greeting module", status="active", scope="release-1",
        significance="significant", requires_decision=True, decision_ids=["ADR-001"], implications=deepcopy(implications))]
    records["decisions"] = [dict(base, id="ADR-001", status="accepted", scope="release-1", statement="Use a single process.",
        context="One local read operation needs no distributed coordination.", alternatives=["single module", "remote service"],
        criteria=["operational effort", "required latency"], evidence=["evidence.md#Decision"], uncertainty="Synthetic test only",
        consequences=["No network dependency; scale by process replication if required later"], dependencies=[], supersedes=[],
        implications=deepcopy(implications))]
    records["verification"] = [dict(base, id="VER-001", status="planned", method="contract test", acceptance="GET returns stored greeting",
        environment="isolated test process", targets=["REQ-001", "DES-001"], evidence=[])]
    def edge(a, b, kind):
        return dict(from_=a, to=b, type=kind, rationale="Greeting behavior is realized by its module.", evidence=["evidence.md#Trace"])
    for a, b, kind in [("SRC-001", "REQ-001", "source_to_requirement"), ("REQ-001", "DES-001", "requirement_to_design"),
                       ("REQ-001", "ADR-001", "requirement_to_decision"), ("ADR-001", "DES-001", "decision_to_design"),
                       ("DES-001", "VER-001", "design_to_verification")]:
        link = edge(a, b, kind)
        link["from"] = link.pop("from_")
        records["traceability"].append(link)
    for key, path in FILES.items():
        write(root / path, records[key])
    catalog = read_json(FRAMEWORK / "criteria-catalog.json")
    sections = catalog["dimensions"]["artifact_completeness"]["arc42_sections"]
    (root / "architecture.md").write_text("# Synthetic greeting architecture\n\n" + "\n".join(
        f"## {i}. {name}\n\nGreeting module DES-001 implements REQ-001 using ADR-001. "
        "VER-001 is a planned contract test. This synthetic fixture declares no external integration.\n"
        for i, name in enumerate(sections, 1)), encoding="utf-8")
    (root / "evidence.md").write_text("# Synthetic evidence\n\nNo real stakeholder or production approval is claimed.\n\n"
        "## Configuration\nFixture human adopts these weights and policy for this test only.\n\n"
        "## Interview\nFixture human confirms the greeting requirement and unchanged scope.\n\n"
        "## Decision\nSingle process meets the local read requirement with fewer dependencies.\n\n"
        "## Trace\nThe greeting requirement is mapped to the module and planned contract test.\n\n"
        "## Assessment\nAll semantic criteria are supplied test inputs, not an autonomous proof.\n\n"
        "## Review\nFixture human approves the single-process choice for this simulation.\n", encoding="utf-8")
    write(root / "process/config.json", config)
    write(root / "process/state.json", {})
    write(root / "process/reviews.json", [])
    write(root / "process/assessment.json", {})
    (root / "process/history.jsonl").write_text('{"round":1,"event":"synthetic confirmation"}\n', encoding="utf-8")
    write(root / "process/manifest.json", {"files": sorted(REQUIRED | {"evidence.md"})})
    bind_project(root)
    return root


def bind_project(root):
    """Fixture-only simulated re-review; never use this to approve a real baseline."""
    snapshot = Snapshot(root)
    config = snapshot.json("process/config.json")
    records = {k: snapshot.json(v) for k, v in FILES.items()}
    subject = snapshot.subject_hash()
    req_hash = content_hash({k: records[k] for k in ("requirements", "constraints", "sources")})
    state = dict(run_id="synthetic-run", stage="review", mode="create", baseline_revision=1, versions=config["versions"],
                 round=1, elapsed_minutes=5, answered_questions=[], pending_questions=[], gate_results={}, pending_reviews=[],
                 next_action="report synthetic results", subject_hash=subject, blocking_findings=[], mandatory_conflicts=[], incomplete_operations=[],
                 stability=dict(confirmed=True, participants=["fixture-human"], round_id="round-1", before_hash=req_hash,
                                after_hash=req_hash, evidence=["evidence.md#Interview"]))
    write(root / "process/state.json", dict(revision=1, state=state, state_hash=content_hash(state)))
    write(root / "process/reviews.json", [dict(id="review-1", kind="architecture", targets=["ADR-001"], status="approved",
        reviewer="fixture-human", baseline_revision=1, subject_hash=subject, reviewed_at="2026-01-01T00:00:00Z",
        expires_at="2099-01-01T00:00:00Z", evidence=["evidence.md#Review"])])
    checks = expected_checks(records, config, snapshot.json("@rubric"))
    for dimension, rows in checks.items():
        for check in rows:
            check.update(result="pass", baseline_revision=1, subject_hash=subject, assessor="fixture-assessor",
                         evidence=["evidence.md#Assessment"], rationale="Synthetic positive input for this criterion")
            if check["target_id"].startswith("arc42:"):
                sections = snapshot.json("@rubric")["dimensions"]["artifact_completeness"]["arc42_sections"]
                section = check["target_id"].split(":", 1)[1]
                check["evidence"] = [f"architecture.md#{sections.index(section) + 1}. {section}"]
    write(root / "process/assessment.json", checks)


SCENARIOS = ("greenfield", "create", "brownfield", "interrupted", "blocking-review", "interview", "update")


def make_scenario(root, scenario):
    """Generate disposable schema-2 inputs, never migrate or approve a real project."""
    root = Path(root)
    if scenario not in SCENARIOS:
        raise ValueError(f"unknown fixture: {scenario}")
    if root.exists():
        raise ValueError("fixture destination must be fresh")
    make_project(root)
    if scenario in {"create", "interview"}:
        for name in ("design-elements.json", "decisions.json"):
            write(root / name, [])
        verification = read_json(root / "verification.json")
        verification[0]["targets"] = ["REQ-001"]
        write(root / "verification.json", verification)
        write(root / "traceability.json", read_json(root / "traceability.json")[:1])
        (root / "architecture.md").write_text("# Synthetic draft; design not started\n", encoding="utf-8")
    elif scenario == "blocking-review":
        designs = read_json(root / "design-elements.json")
        designs[0]["implications"]["security"] = True
        write(root / "design-elements.json", designs)
    bind_project(root)
    envelope = read_json(root / "process/state.json")
    state = envelope["state"]
    if scenario in {"create", "interview"}:
        state.update(mode=scenario, stage="design" if scenario == "create" else "interview")
        write(root / "process/reviews.json", [])
        if scenario == "interview":
            state["stability"]["confirmed"] = False
            state["pending_questions"] = ["Confirm the response acceptance criterion with the stakeholder."]
    elif scenario == "brownfield":
        write(root / "process/reviews.json", [])
        state.update(mode="update", stage="preparation", pending_reviews=["Missing historical ADR-001 approval"])
    elif scenario == "interrupted":
        state.update(mode="interview", stage="interview", answered_questions=["Stored greeting is the scoped behavior"],
                     incomplete_operations=["Interview confirmation interrupted; reconcile before continuing"])
        state["stability"]["confirmed"] = False
    elif scenario == "update":
        # The change is proposed, not silently applied to accepted records.
        (root / "change-request.md").write_text(
            "# Synthetic change request\n\nPropose a configurable greeting language. "
            "Preserve the current baseline and obtain stakeholder confirmation and renewed review.\n",
            encoding="utf-8")
        state.update(mode="update", stage="preparation", next_action="Assess change-request.md dependency impacts")
    envelope["state_hash"] = content_hash(state)
    write(root / "process/state.json", envelope)
    return root


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Create a clearly synthetic DAP schema-2 example, never a real approval")
    parser.add_argument("--output", type=Path, required=True)
    choices = parser.add_mutually_exclusive_group()
    choices.add_argument("--scenario", choices=SCENARIOS, default="greenfield")
    choices.add_argument("--suite", action="store_true", help="Generate all synthetic scenarios in separate workspaces")
    args = parser.parse_args()
    if args.output.exists():
        parser.error("output must be a fresh directory; existing artifacts are never overwritten")
    if args.suite:
        args.output.mkdir(parents=True)
        for scenario in SCENARIOS:
            print(make_scenario(args.output / scenario / "architecture", scenario))
    else:
        print(make_scenario(args.output, args.scenario))
