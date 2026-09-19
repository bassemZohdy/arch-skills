from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from dap_adapter import AdapterContractError, load_json, validate_result, validate_scenario_manifest


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "tests" / "dap-adapter-scenarios.json"


class DAPAdapterContractTests(unittest.TestCase):
    def test_scenario_manifest_is_valid_and_host_neutral(self):
        summary = validate_scenario_manifest(load_json(MANIFEST))
        self.assertEqual(summary["scenario_count"], 5)

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


if __name__ == "__main__":
    unittest.main()
