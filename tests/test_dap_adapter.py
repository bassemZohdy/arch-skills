from __future__ import annotations

import sys
from copy import deepcopy
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from dap_adapter import AdapterContractError, FIXTURES, load_json, validate_execution, validate_result, validate_scenario_manifest
from dap_fixture import SCENARIOS, make_scenario
from dap.scoring import evaluate_project
from dap.persistence import load_checkpoint


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "tests" / "dap-adapter-scenarios.json"


class DAPAdapterContractTests(unittest.TestCase):
    def test_scenario_manifest_is_valid_and_host_neutral(self):
        summary = validate_scenario_manifest(load_json(MANIFEST))
        self.assertEqual(summary["scenario_count"], 7)

    def test_generated_scenario_fixtures_are_current_and_distinct(self):
        self.assertEqual(FIXTURES, set(SCENARIOS))
        with tempfile.TemporaryDirectory() as temporary:
            for scenario in SCENARIOS:
                with self.subTest(scenario=scenario):
                    root = make_scenario(Path(temporary) / scenario, scenario)
                    report = evaluate_project(root)
                    self.assertEqual(report.get("schema_version"), "2.0.0", report["findings"])
                    self.assertEqual(report["gate"]["ready"], scenario in {"greenfield", "update"})
                    self.assertEqual(load_checkpoint(root / "process/state.json", root)["revision"], 1)
                    if scenario == "blocking-review":
                        self.assertEqual(report["overall_score"], 100)
                        self.assertTrue(any("security review" in f for f in report["findings"]))
                    if scenario == "interview":
                        self.assertEqual(load_json(root / "process/state.json")["state"]["mode"], "interview")
                    if scenario == "update":
                        self.assertTrue((root / "change-request.md").exists())
                    with self.assertRaises(ValueError):
                        make_scenario(root, scenario)

    def test_manifest_rejects_legacy_fixtures_traversal_and_incomplete_assertions(self):
        for change in (lambda s: s.update(fixture="examples/greenfield/architecture"),
                       lambda s: s.update(skill="./skills/../outside"),
                       lambda s: s["assertions"][0].update(path="../outside"),
                       lambda s: s.update(assertions=[{"type": "gate_ready", "expected": "false"}]),
                       lambda s: s.update(assertions=[{"type": "file_exists"}])):
            manifest = load_json(MANIFEST)
            change(manifest["scenarios"][0])
            with self.assertRaises(AdapterContractError):
                validate_scenario_manifest(manifest)

    def test_result_rejects_empty_contradictory_or_malformed_execution(self):
        baseline = load_json(ROOT / "tests/dap-adapter-result.example.json")
        baseline.update(status="passed", assertions=[{"type": "gate_ready", "passed": True}],
                        evidence=[{"path": "report.json"}])
        changes = ({"assertions": []}, {"assertions": [{"type": "gate_ready", "passed": False}]},
                   {"assertions": [{"type": "gate_ready", "passed": "true"}]},
                   {"evidence": [{}]}, {"evidence": [{"path": "../outside"}]},
                   {"started_at": "not-a-date"}, {"finished_at": "2020-01-01T00:00:00Z"},
                   {"status": "failed"}, {"status": "unavailable"})
        for change in changes:
            with self.subTest(change=change):
                result = deepcopy(baseline)
                result.update(change)
                with self.assertRaises(AdapterContractError):
                    validate_result(result)

    def test_passed_result_requires_versions_and_evidence(self):
        result = {
            "protocol_version": "1.0.0",
            "scenario_id": "DAP-BEH-001",
            "status": "passed",
            "run_id": "run-001",
            "adapter": {"id": "reference-adapter", "version": "1.2.0"},
            "model": {"id": "reference-model", "version": "3.4.0"},
            "started_at": "2026-09-19T00:00:00Z",
            "finished_at": "2026-09-19T00:01:00Z",
            "assertions": [{"type": "file_exists", "passed": True}],
            "evidence": [{"path": "architecture/process/state.json"}],
        }
        summary = validate_result(result, "DAP-BEH-001")
        self.assertEqual(summary["evidence_count"], 1)

    def test_unavailable_result_requires_reason(self):
        result = load_json(ROOT / "tests" / "dap-adapter-result.example.json")
        summary = validate_result(result, "DAP-BEH-001")
        self.assertEqual(summary["status"], "unavailable")
        result.pop("reason")
        with self.assertRaises(AdapterContractError):
            validate_result(result)

    def test_host_specific_fields_are_rejected_from_scenarios(self):
        manifest = load_json(MANIFEST)
        manifest["scenarios"][0]["harness"] = "named-host"
        with self.assertRaises(AdapterContractError):
            validate_scenario_manifest(manifest)

    def test_passed_result_without_evidence_is_rejected(self):
        result = {
            "protocol_version": "1.0.0",
            "scenario_id": "DAP-BEH-001",
            "status": "passed",
            "run_id": "run-001",
            "adapter": {"id": "a", "version": "1"},
            "model": {"id": "m", "version": "1"},
            "started_at": "2026-09-19T00:00:00Z",
            "finished_at": "2026-09-19T00:01:00Z",
            "assertions": [],
            "evidence": [],
        }
        with self.assertRaises(AdapterContractError):
            validate_result(result)

    def test_execution_requires_every_manifest_assertion_and_real_evidence(self):
        manifest = load_json(MANIFEST)
        scenario = manifest["scenarios"][0]
        result = {
            "protocol_version": "1.0.0", "scenario_id": scenario["id"], "status": "passed",
            "run_id": "run-001", "adapter": {"id": "a", "version": "1"},
            "model": {"id": "m", "version": "1"},
            "started_at": "2026-09-19T00:00:00Z", "finished_at": "2026-09-19T00:01:00Z",
            "assertions": [{"assertion_id": f"{scenario['id']}:1", "type": scenario["assertions"][0]["type"], "passed": True}],
            "evidence": [{"path": "report.json"}],
        }
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            (workspace / "report.json").write_text("{}")
            with self.assertRaises(AdapterContractError):
                validate_execution(result, manifest, workspace)
            result["assertions"] = [
                {"assertion_id": f"{scenario['id']}:{i + 1}", "type": assertion["type"], "passed": True}
                for i, assertion in enumerate(scenario["assertions"])
            ]
            summary = validate_execution(result, manifest, workspace)
            self.assertTrue(summary["execution_checked"])
            result["assertions"][0]["assertion_id"] = "unexpected"
            with self.assertRaises(AdapterContractError):
                validate_execution(result, manifest, workspace)

    def test_unavailable_execution_does_not_require_fixture_evidence(self):
        manifest = load_json(MANIFEST)
        result = load_json(ROOT / "tests/dap-adapter-result.example.json")
        summary = validate_execution(result, manifest, ROOT / ".cache")
        self.assertFalse(summary["execution_checked"])


if __name__ == "__main__":
    unittest.main()
