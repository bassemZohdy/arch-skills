import json
from copy import deepcopy
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from compare_behavioral import ComparisonError, compare, load


def report(status="passed", complete=True, package="p", model="m"):
    execution = {'adapter': {'id': 'adapter', 'version': '1'},
                 'model': {'id': model, 'version': '1'},
                 'execution_mode': 'response-only', 'generation': {'max_tokens': 100}}
    return {"schema_version": "1.0", "complete": complete, "cases": [{
        "id": "test/case", "skill": "arch-api", "manifest_sha256": "manifest",
        "package_sha256": package, **deepcopy(execution), "status": status,
        'runs': 1, 'min_passes': 1, 'timeout': 10, 'mode': 'explicit',
        "pass_rate": 1.0 if status == "passed" else 0.0,
        "attempts": [{"status": status, "steps": [deepcopy(execution)]}],
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

    def test_package_only_override_preserves_execution_configuration(self):
        result = compare(report(), report(package='candidate'), allow_package_change=True)
        self.assertEqual(result['package_changes'], ['test/case'])
        self.assertEqual(result['configuration_changes'], [])
        with self.assertRaises(ComparisonError):
            compare(report(), report(package='candidate', model='other'), allow_package_change=True)

    def test_later_step_identity_and_unknown_settings_are_rejected(self):
        for field, value in (('model', {'id': 'other', 'version': '1'}),
                             ('generation', {'max_tokens': 200}),
                             ('execution_mode', 'host')):
            candidate = report()
            step = deepcopy(candidate['cases'][0]['attempts'][0]['steps'][0])
            step[field] = value
            candidate['cases'][0]['attempts'][0]['steps'].append(step)
            with self.assertRaises(ComparisonError):
                compare(report(), candidate, allow_configuration_change=True)
        old = report()
        del old['cases'][0]['generation']
        with self.assertRaises(ComparisonError):
            compare(old, report())

    def test_repetition_drift_and_candidate_errors_cannot_pass(self):
        candidate = report()
        candidate['cases'][0]['runs'] = 2
        candidate['cases'][0]['attempts'] *= 2
        with self.assertRaises(ComparisonError):
            compare(report(), candidate)
        self.assertEqual(compare(report('failed'), report('error'))['status'], 'failed')

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
