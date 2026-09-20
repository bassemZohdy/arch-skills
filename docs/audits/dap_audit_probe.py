"""Reproduce the 2026-09-20 DAP audit on disposable fixture copies.

Run from any directory: python docs/audits/dap_audit_probe.py
This is a diagnostic, not a conformance suite: observations include known defects.
No source fixtures, installed skills, or product implementation are modified.
"""
from __future__ import annotations

import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
from dap.contracts import SCHEMA_VERSION, validate_records
from dap.persistence import load_checkpoint, save_checkpoint
from dap.scoring import evaluate_project, report_is_stale


def read(path):
    return json.loads(path.read_text(encoding="utf-8"))


def write(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value), encoding="utf-8")


def summarize(report):
    return {
        "ready": report["gate"]["ready"],
        "assessable": report["assessable"],
        "score": report["overall_score"],
        "scores": {k: v["score"] for k, v in report["metrics"].items()},
    }


def main():
    if SCHEMA_VERSION != "1.0.0":
        raise SystemExit("Historical probe for commit 1089b9f/schema 1 only. Captured evidence is in "
                         "2026-09-20-dap-evidence.json. Validate this implementation with "
                         "python -m unittest discover -s tests -p 'test_*.py'.")
    observations = {}
    with tempfile.TemporaryDirectory(prefix="dap-audit-", dir=ROOT) as temporary:
        scratch = Path(temporary)
        assert scratch.resolve().parent == ROOT.resolve()
        assert scratch.name.startswith("dap-audit-")

        def project(name):
            return Path(shutil.copytree(ROOT / "examples/greenfield/architecture", scratch / name))

        baseline = project("baseline")
        report = evaluate_project(baseline)
        observations["P01_arithmetic_fixture_readiness"] = summarize(report)
        observations["P01_populations"] = {
            "requirements": len(read(baseline / "requirements.json")),
            "decisions": len(read(baseline / "decisions.json")),
            "assessment_rows": {k: len(v) for k, v in read(baseline / "process/assessment.json").items()},
        }

        p = project("failed-checks")
        checks = read(p / "process/assessment.json")
        for rows in checks.values():
            for row in rows:
                row["result"] = "fail"
        write(p / "process/assessment.json", checks)
        observations["P02_all_quality_decision_artifact_checks_fail"] = summarize(evaluate_project(p))

        p = project("empty")
        for filename in ("requirements.json", "design-elements.json", "decisions.json", "traceability.json"):
            write(p / filename, [])
        observations["P03_empty_required_inventories"] = summarize(evaluate_project(p))

        p = project("one-check")
        write(p / "process/assessment.json", {k: [{"result": "pass"}] for k in checks})
        observations["P04_one_anonymous_check_per_dimension"] = summarize(evaluate_project(p))

        p = project("security")
        state = read(p / "process/state.json")
        state["security_implication"] = True
        write(p / "process/state.json", state)
        write(p / "process/reviews.json", {"security": {"status": "pending"}})
        config = read(p / "process/config.json")
        config["governance"]["security_review_required"] = False
        write(p / "process/config.json", config)
        observations["P05_security_review_disabled"] = summarize(evaluate_project(p))

        p = project("version")
        config = read(p / "process/config.json")
        config["versions"] = {k: "999.0.0" for k in config["versions"]}
        write(p / "process/config.json", config)
        observations["P06_unsupported_versions"] = summarize(evaluate_project(p))

        p = project("assessment-freshness")
        before = evaluate_project(p)
        write(p / "process/assessment.json", {k: [{"result": "fail"}] for k in checks})
        observations["P07_assessment_change"] = {
            "stale": report_is_stale(p, before),
            "before_score": before["overall_score"],
            "after_score": evaluate_project(p)["overall_score"],
        }

        p = project("external-config")
        config_path = scratch / "external-config.json"
        config = read(p / "process/config.json")
        write(config_path, config)
        before = evaluate_project(p, config_path)
        config["weights"] = dict(requirements_quality=0.1, decision_coverage=0.1, traceability=0.7, artifact_completeness=0.1)
        write(config_path, config)
        observations["P08_external_config_change"] = {
            "stale": report_is_stale(p, before),
            "before_score": before["overall_score"],
            "after_score": evaluate_project(p, config_path)["overall_score"],
        }

        invalid = {
            "requirements": [{"id": "ADR-001"}],
            "design_elements": [{"id": "ADR-001"}],
            "decisions": [{"id": "ADR-001"}],
            "traceability": [{"from": "missing", "to": "also-missing", "type": "invented"}],
        }
        try:
            validate_records(invalid)
            observations["P09_invalid_records"] = "accepted: wrong-kind IDs, cross-kind duplicates, missing fields, dangling endpoints, unknown edge type"
        except Exception as exc:
            observations["P09_invalid_records"] = f"rejected: {exc}"

        p = project("checkpoint")
        state_path = p / "process/state.json"
        state = read(state_path)
        checkpoint_path = p / "process/checkpoint.json"
        checkpoint = save_checkpoint(checkpoint_path, state, 0)
        write(state_path, checkpoint)
        observations["P10_persisted_state_envelope"] = summarize(evaluate_project(p))
        checkpoint["state"]["convergence_status"] = "tampered"
        write(checkpoint_path, checkpoint)
        observations["P11_tampered_checkpoint_hash"] = {"loaded_state": load_checkpoint(checkpoint_path)["state"]["convergence_status"]}

        p = project("rtm")
        links = read(p / "traceability.json")
        links.append({"from": "DES-001", "to": "VER-001", "type": "design_to_verification"})
        write(p / "traceability.json", links)
        subprocess.run([sys.executable, str(ROOT / "scripts/dap_rtm.py"), str(p)], check=True, capture_output=True)
        rtm = (p / "traceability.md").read_text(encoding="utf-8")
        observations["P12_rtm_schema_edge"] = {
            "verification_id_rendered": "VER-001" in rtm,
            "first_requirement_row": next(line for line in rtm.splitlines() if line.startswith("| REQ-001 |")),
        }

        p = project("publication")
        publisher = [sys.executable, str(ROOT / "scripts/dap_publish.py"), str(p)]
        subprocess.run(publisher, check=True, capture_output=True)
        write(p / "process/assessment.json", {k: [{"result": "fail"}] for k in checks})
        subprocess.run(publisher, check=True, capture_output=True)
        observations["P13_publication_history"] = {
            "report_files": sorted(x.name for x in (p / "evaluations").iterdir()),
            "previous_report_stale": read(p / "evaluations/latest.json")["previous_report_stale"],
        }

        package = scratch / "isolated-evaluator"
        shutil.copytree(ROOT / "skills/arch-evaluate", package)
        run = subprocess.run([sys.executable, "scripts/dap_validate.py", str(baseline)], cwd=package, capture_output=True, text=True)
        observations["P14_isolated_evaluator"] = {"exit_code": run.returncode, "declared_script_exists": (package / "scripts/dap_validate.py").exists()}

    inventory = []
    for directory in sorted((ROOT / "skills").glob("arch-*")):
        entry = directory / "SKILL.md"
        content = entry.read_text(encoding="utf-8")
        resources = [p for p in directory.rglob("*") if p.is_file() and p != entry]
        inline = re.findall(r"`((?:references|assets|scripts)/[^`\n]+)`", content)
        markdown = re.findall(r"\]\(((?:references|assets)/[^)]+)\)", content)
        inventory.append({
            "skill": directory.name,
            "lines": len(content.splitlines()),
            "resources": len(resources),
            "markdown_resource_links": len(markdown),
            "inline_resource_paths": len(inline),
            "missing_inline_paths": [path for path in inline if not (directory / path).exists()],
            "dap_resources_not_named_by_entry": [p.relative_to(directory).as_posix() for p in resources if "dap-" in p.name and p.name not in content],
        })
    print(json.dumps({"observations": observations, "inventory": inventory}, indent=2))


if __name__ == "__main__":
    main()
