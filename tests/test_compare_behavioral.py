import json
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from compare_behavioral import ComparisonError, compare, load


def report(status="passed", complete=True, package="p", model="m"):
    return {"schema_version": "1.0", "complete": complete, "cases": [{
        "id": "test/case", "skill": "arch-api", "manifest_sha256": "manifest",
        "package_sha256": package, "adapter": {"id": "adapter", "version": "1"},
        "model": {"id": model, "version": "1"}, "status": status,
        "pass_rate": 1.0 if status == "passed" else 0.0,
        "attempts": [{"status": status, "steps": []}],
    }]}


class CompareTests(unittest.TestCase):
    def test_pass_and_regression(self):
        self.assertEqual(compare(report(), report())["status"], "passed")
        result = compare(report(), report("failed"))
        self.assertEqual(result["status"], "failed")
        self.assertEqual(result["regressions"], ["test/case"])

    def test_unavailable_is_not_a_pass(self):
        result = compare(report(), report("unavailable"))
        self.assertEqual(result["status"], "unavailable")
        self.assertEqual(result["unavailable"], ["test/case"])
        with self.assertRaises(ComparisonError):
            compare(report("unavailable"), report())

    def test_configuration_and_selection_changes_are_rejected(self):
        with self.assertRaises(ComparisonError):
            compare(report(), report(package="changed"))
        self.assertEqual(compare(report(), report(package="changed"), True)["status"], "passed")
        candidate = report()
        candidate["cases"][0]["id"] = "other"
        with self.assertRaises(ComparisonError):
            compare(report(), candidate)

    def test_incomplete_or_invalid_reports_are_rejected(self):
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "report.json"
            path.write_text(json.dumps(report(complete=False)))
            with self.assertRaises(ComparisonError):
                load(path)
            path.write_text("[]")
            with self.assertRaises(ComparisonError):
                load(path)


if __name__ == "__main__":
    unittest.main()
