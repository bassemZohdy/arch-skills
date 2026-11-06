"""Keep current inventory/version claims synchronized; historical audits stay frozen."""
import json
from collections import Counter
from pathlib import Path
import re
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from behavioral import load_cases
from check_diagrams import discover_sources
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

    def test_coverage_inventory_matches_manifests(self):
        manifests = sorted((ROOT / 'tests').glob('test-*.yaml'))
        cases = load_cases(manifests)
        coverage = (ROOT / 'docs/coverage-analysis.md').read_text(encoding='utf-8')
        explicit = Counter(case['skill'] for case in cases if case['mode'] == 'explicit')
        activation = sum(case['mode'] == 'activation' for case in cases)
        rows = re.findall(r'^\| (arch-[\w-]+) \| (\d+) \| (arch-[\w-]+) \| (\d+) \|$',
                          coverage, re.MULTILINE)
        documented = {name: int(count) for left, lc, right, rc in rows
                      for name, count in ((left, lc), (right, rc))}
        self.assertEqual(documented, explicit)
        self.assertEqual(len(rows) * 2, len(explicit))
        self.assertIn(f'{len(cases)} scenarios in {len(manifests)} YAML', coverage)
        self.assertIn(f'{sum(explicit.values())} explicitly target a skill and {activation} test activation', coverage)

    def test_diagram_and_manifest_counts_are_current(self):
        diagrams = len(discover_sources(ROOT))
        manifests = len(sorted((ROOT / 'tests').glob('test-*.yaml')))
        automation = (ROOT / 'docs/test-automation.md').read_text(encoding='utf-8')
        status = (ROOT / 'docs/project-status.md').read_text(encoding='utf-8')
        self.assertIn(f'{diagrams} Mermaid files or fenced blocks', automation)
        self.assertIn(f'{diagrams} Mermaid files/fenced blocks', status)
        self.assertIn(f'{manifests} YAML manifests', automation)

    def test_runtime_version_matches_contract_and_current_status(self):
        version = json.loads((ROOT / 'framework/contract-version.json').read_text())
        for key, expected in (('framework_version', FRAMEWORK_VERSION), ('schema_version', SCHEMA_VERSION),
                              ('rubric_version', RUBRIC_VERSION), ('evaluator_version', EVALUATOR_VERSION)):
            self.assertEqual(version[key], expected)
        for path in ('docs/project-status.md', 'docs/dap-implementation-status.md'):
            self.assertIn('evaluator ' + EVALUATOR_VERSION, (ROOT / path).read_text(encoding='utf-8'))
