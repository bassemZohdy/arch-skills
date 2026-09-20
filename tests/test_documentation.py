"""Keep current inventory/version claims synchronized; historical audits stay frozen."""
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from behavioral import load_cases
from dap.contracts import EVALUATOR_VERSION, FRAMEWORK_VERSION, RUBRIC_VERSION, SCHEMA_VERSION


class DocumentationTests(unittest.TestCase):
    def test_current_skill_and_scenario_counts(self):
        manifests = sorted((ROOT / 'tests').glob('test-*.yaml'))
        cases = load_cases(manifests)
        skills = list((ROOT / 'skills').glob('arch-*/SKILL.md'))
        status = (ROOT / 'docs/project-status.md').read_text(encoding='utf-8')
        readme = (ROOT / 'README.md').read_text(encoding='utf-8')
        self.assertIn(f'{len(skills)} canonical skills', status)
        self.assertIn(f'{len(cases)} validated scenarios across {len(manifests)} manifests', status)
        self.assertIn(f'validates {len(cases)} scenarios across all {len(skills)} skills', readme)

    def test_runtime_version_matches_contract_and_current_status(self):
        version = json.loads((ROOT / 'framework/contract-version.json').read_text())
        for key, expected in (('framework_version', FRAMEWORK_VERSION), ('schema_version', SCHEMA_VERSION),
                              ('rubric_version', RUBRIC_VERSION), ('evaluator_version', EVALUATOR_VERSION)):
            self.assertEqual(version[key], expected)
        for path in ('docs/project-status.md', 'docs/dap-implementation-status.md'):
            self.assertIn('evaluator ' + EVALUATOR_VERSION, (ROOT / path).read_text(encoding='utf-8'))
