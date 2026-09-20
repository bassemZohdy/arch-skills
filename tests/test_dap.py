from __future__ import annotations
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import threading
import unittest

from dap_fixture import ROOT, make_project, bind_project, write
from dap.contracts import ContractError, validate_config, validate_records
from dap.persistence import ConcurrentRevisionError, content_hash, load_checkpoint, save_checkpoint
from dap.publishing import publish_report
from dap.scoring import evaluate_project, expected_checks
from dap.snapshot import Snapshot, local_path, report_is_stale
from dap.workflow import route, plan_change, interview_status


class DAPTests(unittest.TestCase):
    def test_manifest_rejects_noncanonical_and_generated_path_aliases(self):
        for name in ('./evaluations/report.json', 'evaluations//report.json',
                     'process//config.json', './requirements.json', 'requirements.json/'):
            with self.subTest(name=name), self.assertRaises(ContractError):
                local_path(self.project, name)

    def test_evidence_json_pointer_rejects_negative_and_noncanonical_indices(self):
        snapshot = Snapshot(self.project)
        self.assertTrue(snapshot.evidence('requirements.json#/0/id'))
        for index in ('-1', '00', '+0', ' 0', '0~2'):
            self.assertFalse(snapshot.evidence(f'requirements.json#/{index}/id'), index)

    def test_rtm_cannot_overwrite_an_archived_evaluation_summary(self):
        report = publish_report(self.project)
        summary = report.with_suffix('.md')
        before = summary.read_bytes()
        run = subprocess.run([sys.executable, str(ROOT / 'scripts/dap_rtm.py'), str(self.project),
                              '--output', str(summary)], capture_output=True, text=True)
        self.assertEqual(run.returncode, 2, run.stdout + run.stderr)
        self.assertEqual(summary.read_bytes(), before)

    def test_generated_evidence_and_rtm_symlink_aliases_are_rejected(self):
        report = publish_report(self.project)
        summary = report.with_suffix('.md')
        evidence_alias = self.project / 'alias.md'
        rtm_alias = self.project / 'evaluations/traceability.md'
        try:
            evidence_alias.symlink_to(summary)
            rtm_alias.symlink_to(summary)
        except OSError:
            self.skipTest('host does not permit symlink creation')
        with self.assertRaises(ContractError):
            local_path(self.project, 'alias.md')
        before = summary.read_bytes()
        run = subprocess.run([sys.executable, str(ROOT / 'scripts/dap_rtm.py'), str(self.project)],
                             capture_output=True, text=True)
        self.assertEqual(run.returncode, 2, run.stdout + run.stderr)
        self.assertEqual(summary.read_bytes(), before)

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="dap-tests-")
        self.addCleanup(self.temp.cleanup)
        self.project = make_project(Path(self.temp.name) / "architecture")

    def read(self, path):
        return json.loads((self.project / path).read_text(encoding="utf-8"))

    def change(self, path, update):
        value = self.read(path)
        update(value)
        write(self.project / path, value)

    def test_complete_positive_baseline(self):
        report = evaluate_project(self.project)
        self.assertTrue(report["gate"]["ready"], report["findings"])
        self.assertEqual(report["overall_score"], 100)
        self.assertEqual(report["metrics"]["requirements_quality"]["applicable"], 17)
        self.assertEqual(report["metrics"]["decision_coverage"]["applicable"], 10)
        self.assertEqual(report["metrics"]["artifact_completeness"]["applicable"], 60)

    def test_empty_or_placeholder_architecture_is_not_complete(self):
        path = self.project / "architecture.md"
        for body in ("# Only a heading\n", "## 1. introduction_goals\n\nTBD\n"):
            with self.subTest(body=body):
                path.write_text(body)
                bind_project(self.project)
                self.assertFalse(evaluate_project(self.project)["gate"]["ready"])

    def test_arc42_assessments_cannot_reuse_an_unrelated_section(self):
        def reuse(a):
            for check in a["artifact_completeness"]:
                if check["target_id"].startswith("arc42:"):
                    check["evidence"] = ["architecture.md#1. introduction_goals"]
        self.change("process/assessment.json", reuse)
        report = evaluate_project(self.project)
        self.assertFalse(report["gate"]["ready"])
        self.assertEqual(report["metrics"]["artifact_completeness"]["unknown"], 33)

    def test_brownfield_missing_dispositions_remain_blocked(self):
        write(self.project / "process/reviews.json", [])
        before = Snapshot(self.project).manifest
        report = evaluate_project(self.project)
        self.assertEqual(report["overall_score"], 100)
        self.assertFalse(report["gate"]["ready"])
        self.assertEqual(Snapshot(self.project).manifest, before)

    def test_pending_review_queue_blocks_without_auto_timeout_approval(self):
        envelope = self.read("process/state.json")
        envelope["state"]["pending_reviews"] = ["overdue-human-review"]
        envelope["state_hash"] = content_hash(envelope["state"])
        write(self.project / "process/state.json", envelope)
        self.assertFalse(evaluate_project(self.project)["gate"]["ready"])

    def test_historical_examples_are_explicitly_unsupported(self):
        for name in ("greenfield", "brownfield", "interrupted", "blocking-review"):
            with self.subTest(name=name):
                config = json.loads((ROOT / "examples" / name / "architecture/process/config.json").read_text())
                with self.assertRaisesRegex(ContractError, "historical assessment unavailable"):
                    validate_config(config)
                report = evaluate_project(ROOT / "examples" / name / "architecture")
                self.assertFalse(report["gate"]["ready"])
                self.assertIn("historical assessment unavailable", report["findings"][0])

    def test_all_na_artifacts_are_unassessable_not_ready(self):
        def exclude(a):
            for check in a["artifact_completeness"]:
                check.update(result="not_applicable", reason="fixture exclusion", authorized_by="fixture-human",
                             authorization_evidence="evidence.md#Review")
        self.change("process/assessment.json", exclude)
        report = evaluate_project(self.project)
        self.assertIsNone(report["overall_score"])
        self.assertFalse(report["gate"]["ready"])

    def test_mandatory_checks_cannot_be_waived(self):
        self.change("process/assessment.json", lambda a: a["requirements_quality"][0].update(result="not_applicable",
                    reason="waive", authorized_by="fixture-human", authorization_evidence="evidence.md#Review"))
        self.assertFalse(evaluate_project(self.project)["gate"]["ready"])

    def test_malformed_state_returns_blocked_report(self):
        write(self.project / "process/state.json", [])
        report = evaluate_project(self.project)
        self.assertFalse(report["gate"]["ready"])
        self.assertIsNone(report["overall_score"])

    def test_checkpoint_resume_verifies_artifacts(self):
        path = self.project / "process/state.json"
        self.assertEqual(load_checkpoint(path, self.project)["revision"], 1)
        self.change("requirements.json", lambda a: a[0].update(statement="changed"))
        with self.assertRaises(ValueError): load_checkpoint(path, self.project)

    def test_executed_verification_requires_evidence(self):
        self.change("verification.json", lambda a: a[0].update(status="passed"))
        self.assertFalse(evaluate_project(self.project)["gate"]["ready"])

    def test_unresolvable_record_evidence_blocks(self):
        self.change("decisions.json", lambda a: a[0].update(evidence=["missing.md"]))
        bind_project(self.project)
        self.assertFalse(evaluate_project(self.project)["gate"]["ready"])

    def test_failed_checks_block_independent_of_score(self):
        self.change("process/assessment.json", lambda a: a["artifact_completeness"][0].update(result="fail"))
        report = evaluate_project(self.project)
        self.assertFalse(report["gate"]["ready"])
        self.assertGreater(report["overall_score"], 99)

    def test_all_failed_checks_block(self):
        self.change("process/assessment.json", lambda a: [c.update(result="fail") for rows in a.values() for c in rows])
        report = evaluate_project(self.project)
        self.assertFalse(report["gate"]["ready"])
        self.assertEqual(report["overall_score"], 35)

    def test_omitted_checks_are_unknown_not_dropped(self):
        self.change("process/assessment.json", lambda a: a.update(requirements_quality=a["requirements_quality"][:1]))
        report = evaluate_project(self.project)
        self.assertEqual(report["metrics"]["requirements_quality"]["applicable"], 17)
        self.assertEqual(report["metrics"]["requirements_quality"]["unknown"], 16)
        self.assertFalse(report["gate"]["ready"])

    def test_anonymous_duplicate_and_wrong_target_assessments_rejected(self):
        original = self.read("process/assessment.json")
        from copy import deepcopy
        for kind in ("anonymous", "duplicate", "target"):
            with self.subTest(kind=kind):
                a = deepcopy(original)
                if kind == "anonymous": a["requirements_quality"] = [{"result": "pass"}]
                if kind == "duplicate": a["requirements_quality"].append(a["requirements_quality"][0])
                if kind == "target": a["requirements_quality"][0]["target_id"] = "REQ-999"
                write(self.project / "process/assessment.json", a)
                report = evaluate_project(self.project)
                self.assertFalse(report["gate"]["ready"])
                self.assertIsNone(report["overall_score"])

    def test_empty_required_population_is_unassessable(self):
        for path in ("requirements.json", "design-elements.json", "decisions.json", "verification.json", "traceability.json"):
            write(self.project / path, [])
        bind_project(self.project)
        report = evaluate_project(self.project)
        self.assertFalse(report["gate"]["ready"])
        self.assertIsNone(report["overall_score"])

    def test_pending_security_cannot_be_disabled(self):
        self.change("design-elements.json", lambda a: a[0]["implications"].update(security=True))
        self.change("process/config.json", lambda a: a["governance"].update(security_review_required=False))
        bind_project(self.project)
        report = evaluate_project(self.project)
        self.assertFalse(report["gate"]["ready"])
        self.assertTrue(any("security review" in x for x in report["findings"]))

    def test_all_mandatory_review_categories(self):
        for role in ("privacy", "compliance", "irreversible", "high_risk", "cross_team", "cost"):
            with self.subTest(role=role):
                self.change("design-elements.json", lambda a: a[0]["implications"].update({role: 20000 if role == "cost" else True}))
                bind_project(self.project)
                self.assertFalse(evaluate_project(self.project)["gate"]["ready"])
                self.change("design-elements.json", lambda a: a[0]["implications"].update({role: 100 if role == "cost" else False}))

    def test_invalid_review_identity_hash_expiry(self):
        original = self.read("process/reviews.json")
        for field, value in (("reviewer", "unauthorized"), ("subject_hash", "stale"), ("expires_at", "2020-01-01T00:00:00Z")):
            with self.subTest(field=field):
                rows = [dict(original[0], **{field: value})]
                write(self.project / "process/reviews.json", rows)
                self.assertFalse(evaluate_project(self.project)["gate"]["ready"])

    def test_config_invalid_weights_partial_reporting(self):
        self.change("process/config.json", lambda c: c["weights"].update(traceability=0.2))
        report = evaluate_project(self.project)
        self.assertIsNone(report["overall_score"])
        self.assertIn("requirements_quality", report["metrics"])
        self.assertFalse(report["gate"]["ready"])

    def test_config_finite_weights_and_version(self):
        config = self.read("process/config.json")
        for bad in (True, float("nan"), float("inf"), -1):
            with self.subTest(bad=bad):
                candidate = dict(config, weights=dict(config["weights"], traceability=bad))
                with self.assertRaises(ContractError): validate_config(candidate)
        config["versions"]["schema"] = "999.0.0"
        write(self.project / "process/config.json", config)
        report = evaluate_project(self.project)
        self.assertIsNone(report["overall_score"])
        self.assertIn("historical assessment unavailable", report["findings"][0])

    def test_schema_dangling_and_wrong_prefix(self):
        snapshot = Snapshot(self.project)
        from dap.contracts import FILES
        records = {k: snapshot.json(v) for k, v in FILES.items()}
        records["requirements"][0]["id"] = "ADR-001"
        with self.assertRaises(ContractError): validate_records(records)
        records["requirements"][0]["id"] = "REQ-001"
        records["traceability"][0]["to"] = "REQ-999"
        with self.assertRaises(ContractError): validate_records(records)

    def test_missing_source_and_verification_break_forward_chain(self):
        self.change("sources.json", lambda a: a[0].update(status="unconfirmed"))
        bind_project(self.project)
        self.assertEqual(evaluate_project(self.project)["metrics"]["forward_traceability"]["score"], 0)
        self.change("sources.json", lambda a: a[0].update(status="confirmed"))
        self.change("traceability.json", lambda a: a.pop())
        bind_project(self.project)
        self.assertEqual(evaluate_project(self.project)["metrics"]["forward_traceability"]["score"], 0)

    def test_adr_path_counts_without_duplicate_reverse_edges(self):
        self.change("traceability.json", lambda links: links.__setitem__(slice(None), [l for l in links if l["type"] != "requirement_to_design"]))
        bind_project(self.project)
        report = evaluate_project(self.project)
        self.assertEqual(report["metrics"]["backward_traceability"]["score"], 100)
        self.assertEqual(report["metrics"]["forward_traceability"]["score"], 100)

    def test_constraint_can_justify_a_design_without_a_duplicate_requirement(self):
        base = {k: self.read("requirements.json")[0][k] for k in
                ("owner", "source", "source_revision", "revision", "baseline_revision", "scope")}
        write(self.project / "constraints.json", [dict(base, id="CON-001", status="active",
              statement="Keep the deployment local.", binding=True, waivable=False, verification_ids=["VER-001"])])
        extra = dict(self.read("design-elements.json")[0], id="DES-002", name="Local boundary",
                     requires_decision=False, decision_ids=[])
        self.change("design-elements.json", lambda a: a.append(extra))
        def link(links):
            for source, target, kind in (("SRC-001", "CON-001", "source_to_constraint"),
                                         ("CON-001", "DES-002", "constraint_to_design")):
                links.append({"from": source, "to": target, "type": kind,
                              "rationale": "Local boundary implements local deployment.", "evidence": ["evidence.md#Trace"]})
        self.change("traceability.json", link)
        bind_project(self.project)
        report = evaluate_project(self.project)
        self.assertEqual(report["metrics"]["backward_traceability"]["numerator"], 2)
        self.assertTrue(report["gate"]["ready"], report["findings"])

    def test_nonwaivable_constraint_exception_blocks(self):
        base = {k: self.read("requirements.json")[0][k] for k in
                ("owner", "source", "source_revision", "revision", "baseline_revision")}
        write(self.project / "constraints.json", [dict(base, id="CON-001", status="active", scope="release-1",
              statement="Binding fixture obligation", binding=True, waivable=False, verification_ids=[])])
        write(self.project / "process/exceptions.json", [dict(base, id="EXC-001", status="approved",
              obligation="CON-001", reason="fixture request", residual_risk="fixture risk", controls=[],
              expires_at="2099-01-01T00:00:00Z", approved_by="fixture-human", evidence=["evidence.md#Review"])])
        bind_project(self.project)
        report = evaluate_project(self.project)
        self.assertFalse(report["gate"]["ready"])
        self.assertTrue(any("EXC-001" in finding for finding in report["findings"]))

    def test_missing_significant_decision_remains_in_denominator(self):
        self.change("design-elements.json", lambda a: a[0]["decision_ids"].append("ADR-999"))
        bind_project(self.project)
        report = evaluate_project(self.project)
        self.assertEqual(report["metrics"]["decision_coverage"]["applicable"], 20)
        self.assertEqual(report["metrics"]["decision_coverage"]["score"], 50)
        self.assertFalse(report["gate"]["ready"])

    def test_scope_and_wont_exclusion(self):
        self.change("requirements.json", lambda a: a[0].update(priority="wont"))
        bind_project(self.project)
        self.assertFalse(evaluate_project(self.project)["assessable"])

    def test_assessment_and_external_configuration_freshness(self):
        report = evaluate_project(self.project)
        self.change("process/assessment.json", lambda a: a["requirements_quality"][0].update(result="fail"))
        self.assertTrue(report_is_stale(self.project, report))
        external = Path(self.temp.name) / "policy.json"
        write(external, self.read("process/config.json"))
        report = evaluate_project(self.project, external)
        cfg = json.loads(external.read_text())
        cfg["weights"] = dict(requirements_quality=0.1, decision_coverage=0.1, traceability=0.7, artifact_completeness=0.1)
        write(external, cfg)
        self.assertTrue(report_is_stale(self.project, report))

    def test_manifest_cli_compares_external_configuration(self):
        external = Path(self.temp.name) / "policy.json"
        write(external, self.read("process/config.json"))
        report = evaluate_project(self.project, external)
        report_path = Path(self.temp.name) / "report.json"
        write(report_path, report)
        command = [sys.executable, str(ROOT / "scripts/dap_manifest.py"), str(self.project), "--compare", str(report_path)]
        run = subprocess.run(command, capture_output=True, text=True)
        self.assertEqual(run.returncode, 0, run.stderr)
        self.assertFalse(json.loads(run.stdout)["stale"])
        external.write_text(external.read_text() + "\n")
        run = subprocess.run(command, capture_output=True, text=True)
        self.assertEqual(run.returncode, 0, run.stderr)
        self.assertTrue(json.loads(run.stdout)["stale"])

    def test_unrelated_and_generated_content_do_not_invalidate(self):
        report = evaluate_project(self.project)
        (self.project / "unrelated.txt").write_text("not assessed")
        self.assertFalse(report_is_stale(self.project, report))
        architecture = self.project / "architecture.md"
        architecture.write_text(architecture.read_text() + "\n<!-- DAP EVALUATION BEGIN -->\ngenerated\n<!-- DAP EVALUATION END -->\n")
        self.assertFalse(report_is_stale(self.project, report))

    def test_subject_change_invalidates_assessments_and_approvals(self):
        self.change("requirements.json", lambda a: a[0].update(statement="Changed intent"))
        report = evaluate_project(self.project)
        self.assertFalse(report["gate"]["ready"])
        self.assertTrue(any("subject changed" in x for x in report["findings"]))

    def test_manifest_traversal_and_missing_assessed_files(self):
        self.change("process/manifest.json", lambda a: a["files"].append("../outside.json"))
        self.assertFalse(evaluate_project(self.project)["gate"]["ready"])

    def test_checkpoint_integrity(self):
        path = Path(self.temp.name) / "checkpoint.json"
        saved = save_checkpoint(path, {"stage": "interview"}, 0)
        self.assertEqual(load_checkpoint(path), saved)
        with self.assertRaises(ConcurrentRevisionError): save_checkpoint(path, {}, 0)
        saved["state"]["stage"] = "tampered"
        write(path, saved)
        with self.assertRaises(ValueError): load_checkpoint(path)
        self.change("process/state.json", lambda a: a["state"].update(stage="tampered"))
        self.assertFalse(evaluate_project(self.project)["gate"]["ready"])

    def test_concurrent_writers_only_one_commits_same_revision(self):
        path = Path(self.temp.name) / "concurrent.json"
        barrier = threading.Barrier(2)
        results = []
        def worker():
            barrier.wait()
            try:
                save_checkpoint(path, {"stage": "interview"}, 0)
                results.append("saved")
            except ConcurrentRevisionError:
                results.append("conflict")
        threads = [threading.Thread(target=worker) for _ in range(2)]
        for thread in threads: thread.start()
        for thread in threads: thread.join()
        self.assertEqual(sorted(results), ["conflict", "saved"])

    def test_interrupted_checkpoint_lock_is_preserved_for_recovery(self):
        path = Path(self.temp.name) / "interrupted.json"
        lock = path.with_suffix(".json.lock")
        lock.write_text("interrupted writer")
        with self.assertRaises(ConcurrentRevisionError):
            save_checkpoint(path, {"stage": "interview"}, 0)
        self.assertFalse(path.exists())
        self.assertEqual(lock.read_text(), "interrupted writer")

    def test_circular_only_links_do_not_justify_design(self):
        def remove_source(links):
            links[:] = [link for link in links if link["type"] != "source_to_requirement"]
            links.append(dict(links[0], **{"from": "DES-001", "to": "REQ-001", "type": "design_to_requirement"}))
        self.change("traceability.json", remove_source)
        bind_project(self.project)
        report = evaluate_project(self.project)
        self.assertEqual(report["metrics"]["backward_traceability"]["score"], 0)
        self.assertEqual(report["metrics"]["forward_traceability"]["score"], 0)
        self.assertFalse(report["gate"]["ready"])

    def test_publication_immutable_history_and_safe_destination(self):
        first = publish_report(self.project)
        second = publish_report(self.project)
        self.assertNotEqual(first, second)
        self.assertTrue(first.exists() and second.exists())
        with self.assertRaises(ContractError): publish_report(self.project, self.project / "requirements.json")
        self.assertFalse(report_is_stale(self.project, json.loads(first.read_text())))

    def test_rtm_matches_schema_and_does_not_invent_plan(self):
        run = subprocess.run([sys.executable, str(ROOT / "scripts/dap_rtm.py"), str(self.project)], capture_output=True, text=True)
        self.assertEqual(run.returncode, 0, run.stdout + run.stderr)
        self.assertIn("VER-001", (self.project / "evaluations/traceability.md").read_text())
        self.change("traceability.json", lambda a: a.pop())
        run = subprocess.run([sys.executable, str(ROOT / "scripts/dap_rtm.py"), str(self.project)], capture_output=True)
        self.assertEqual(run.returncode, 0)
        self.assertIn("MISSING", (self.project / "evaluations/traceability.md").read_text())

    def test_audit_cli_exit_status_and_no_source_mutation(self):
        before = Snapshot(self.project).manifest
        run = subprocess.run([sys.executable, str(ROOT / "scripts/dap_validate.py"), str(self.project)], capture_output=True)
        self.assertEqual(run.returncode, 0)
        self.assertEqual(Snapshot(self.project).manifest, before)
        self.change("process/assessment.json", lambda a: a["requirements_quality"][0].update(result="unknown"))
        run = subprocess.run([sys.executable, str(ROOT / "scripts/dap_validate.py"), str(self.project)], capture_output=True)
        self.assertEqual(run.returncode, 1)

    def test_interview_only_and_readonly_evaluation_routing(self):
        self.assertEqual(route("interview")["stop_after"], "requirements")
        self.assertEqual(route("create")["entry"], route("update")["entry"])
        self.assertTrue(route("evaluate")["read_only"])
        self.assertEqual(route("evaluate")["entries"], ["arch-evaluate", "arch-review"])

    def test_change_dependency_closure_and_reentry(self):
        result = plan_change(["REQ-001"], self.read("traceability.json"), "requirements")
        self.assertEqual(result["stage"], "interview")
        self.assertIn("VER-001", result["affected_ids"])
        self.assertEqual(plan_change(["ADR-001"], [], "approval")["stage"], "review")
        limits = self.read("process/config.json")["limits"]
        self.assertEqual(interview_status(8, 120, limits, False, True), "blocked")


if __name__ == "__main__":
    unittest.main()
