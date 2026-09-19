from __future__ import annotations
import json
import tempfile
import unittest
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from dap.contracts import ContractError, validate_config
from dap.persistence import ConcurrentRevisionError, load_checkpoint, save_checkpoint
from dap.scoring import evaluate_project, score_checks, report_is_stale
ROOT = Path(__file__).resolve().parents[1]
FIX = ROOT / "examples"
class DAPTests(unittest.TestCase):
    def test_config_rejects_invalid_weights_and_missing_authority(self):
        config=json.loads((ROOT/"framework/config.example.json").read_text())
        config["weights"]["traceability"]=0.1
        with self.assertRaises(ContractError): validate_config(config)
        config=json.loads((ROOT/"framework/config.example.json").read_text())
        del config["governance"]["decision_authority"]
        with self.assertRaises(ContractError): validate_config(config)
    def test_score_unknown_is_zero_and_na_requires_authority(self):
        self.assertEqual(score_checks([{"result":"pass"},{"result":"unknown"}],"x")["score"],50.0)
        with self.assertRaises(ContractError): score_checks([{"result":"not_applicable"}],"x")
    def test_scoring_example_is_76(self):
        report=evaluate_project(FIX/"greenfield"/"architecture")
        self.assertEqual(report["overall_score"],76.0)
        self.assertEqual(report["metrics"]["forward_traceability"]["score"],90.0)
        self.assertEqual(report["metrics"]["backward_traceability"]["score"],60.0)
    def test_blocking_security_review_prevents_readiness(self):
        report=evaluate_project(FIX/"blocking-review"/"architecture")
        self.assertEqual(report["overall_score"],76.0)
        self.assertFalse(report["gate"]["ready"])
        self.assertIn("security review is not approved", report["gate"]["blocking_findings"])
    def test_atomic_checkpoint_and_revision_conflict(self):
        with tempfile.TemporaryDirectory() as d:
            path=Path(d)/"process/state.json"
            first=save_checkpoint(path,{"stage":"interview"},0)
            second=save_checkpoint(path,{"stage":"design"},first["revision"])
            self.assertEqual(load_checkpoint(path)["revision"],2)
            with self.assertRaises(ConcurrentRevisionError):
                save_checkpoint(path,{"stage":"bad"},first["revision"])
    def test_rtm_script_has_inputs(self):
        self.assertTrue((ROOT/"scripts/dap_rtm.py").exists())
    def test_report_becomes_stale_after_assessed_input_changes(self):
        project=FIX/"greenfield"/"architecture"
        report=evaluate_project(project)
        self.assertFalse(report_is_stale(project, report))
        path=project/"architecture.md"
        original=path.read_text()
        try:
            path.write_text(original+"\nchanged\n")
            self.assertTrue(report_is_stale(project, report))
        finally:
            path.write_text(original)
if __name__=="__main__": unittest.main()
