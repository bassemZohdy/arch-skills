"""Exercise CLI failure contracts and checkpoint preservation from an unrelated cwd."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from dap_fixture import ROOT, make_project, write
from dap.persistence import save_checkpoint


class CLITests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix="dap-cli-")
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)

    def run_cli(self, script, *arguments):
        return subprocess.run(
            [sys.executable, str(ROOT / "scripts" / script), *map(str, arguments)],
            cwd=self.root, capture_output=True, text=True,
        )

    def assert_cli_error(self, result):
        self.assertEqual(result.returncode, 2, result.stdout + result.stderr)
        self.assertTrue(result.stderr.strip())
        self.assertNotIn("Traceback", result.stderr)

    def test_manifest_missing_project_is_a_cli_error(self):
        self.assert_cli_error(self.run_cli("dap_manifest.py", self.root / "missing"))

    def test_manifest_rejects_malformed_comparison(self):
        project = make_project(self.root / "architecture")
        comparison = self.root / "comparison.json"
        for content in ("invalid JSON", "[]", '{"input_manifest": null}'):
            with self.subTest(content=content):
                comparison.write_text(content, encoding="utf-8")
                self.assert_cli_error(self.run_cli("dap_manifest.py", project, "--compare", comparison))

    def test_missing_checkpoint_input_does_not_write_output(self):
        checkpoint = self.root / "checkpoint.json"
        result = self.run_cli("dap_checkpoint.py", checkpoint, "--state", self.root / "missing.json",
                              "--expected-revision", 0)
        self.assert_cli_error(result)
        self.assertFalse(checkpoint.exists())

    def test_invalid_checkpoint_state_preserves_existing_checkpoint(self):
        checkpoint = self.root / "checkpoint.json"
        save_checkpoint(checkpoint, {"stage": "interview"}, expected_revision=0)
        before = checkpoint.read_bytes()
        for state in ([], None, "invalid", 42):
            with self.subTest(state=state):
                with self.assertRaisesRegex(ValueError, "state must be an object"):
                    save_checkpoint(checkpoint, state, expected_revision=1)
                self.assertEqual(checkpoint.read_bytes(), before)
                self.assertFalse(checkpoint.with_suffix(".json.lock").exists())

    def test_checkpoint_round_trip_and_invalid_state_through_cli(self):
        checkpoint = self.root / "checkpoint.json"
        state_file = self.root / "state.json"
        state = {"stage": "interview"}
        write(state_file, state)
        result = self.run_cli("dap_checkpoint.py", checkpoint, "--state", state_file, "--expected-revision", 0)
        self.assertEqual(result.returncode, 0, result.stderr)
        shown = self.run_cli("dap_checkpoint.py", checkpoint, "--show")
        self.assertEqual(shown.returncode, 0, shown.stderr)
        self.assertEqual(json.loads(shown.stdout)["state"], state)
        before = checkpoint.read_bytes()
        write(state_file, [])
        self.assert_cli_error(self.run_cli("dap_checkpoint.py", checkpoint, "--state", state_file,
                                          "--expected-revision", 1))
        self.assertEqual(checkpoint.read_bytes(), before)

    def test_audit_output_is_rejected_before_reading_project(self):
        output = self.root / "report.json"
        result = self.run_cli("dap_validate.py", self.root / "missing", "--output", output)
        self.assert_cli_error(result)
        self.assertIn("audit is read-only", result.stderr)
        self.assertFalse(output.exists())


if __name__ == "__main__":
    unittest.main()
