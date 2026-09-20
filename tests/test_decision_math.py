"""Decision arithmetic must not silently certify incomplete or rounded matrices."""
from copy import deepcopy
import importlib.util
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('decision_math', ROOT / 'skills/arch-decision/scripts/validate_math.py')
math = importlib.util.module_from_spec(spec)
spec.loader.exec_module(math)


class DecisionMathTests(unittest.TestCase):
    def setUp(self):
        self.data = math.extract_json_block((ROOT / 'tests/test-dar.md').read_text())

    def test_completed_example(self):
        self.assertEqual(math.validate_data(self.data), [])
        self.assertEqual(math.validate_file(ROOT / 'skills/arch-decision/assets/dar-document.md')[1], [])

    def test_missing_unknown_and_duplicate_criteria(self):
        for kind in ('missing', 'unknown', 'duplicate'):
            data = deepcopy(self.data)
            if kind == 'missing':
                del data['scores']['PostgreSQL']['C1']
            elif kind == 'unknown':
                data['scores']['PostgreSQL']['unknown'] = {'raw': 5, 'weighted': 0}
            else:
                data['scored_criteria'].append(data['scored_criteria'][0])
            with self.subTest(kind=kind):
                self.assertTrue(math.validate_data(data))

    def test_empty_matrices_and_malformed_values_fail_closed(self):
        for value in (None, [], {}, {'scored_criteria': []}, {'scored_criteria': [None]}):
            with self.subTest(value=value):
                self.assertTrue(math.validate_data(value))
        for value in (True, float('nan'), float('inf'), -1, 6, '4', None):
            data = deepcopy(self.data)
            data['scores']['PostgreSQL']['C1']['raw'] = value
            with self.subTest(value=value):
                self.assertTrue(math.validate_data(data))

    def test_weights_and_declared_totals_must_be_complete(self):
        for field in ('scores', 'total_scores', 'ranking'):
            data = deepcopy(self.data)
            data[field] = {} if field != 'ranking' else []
            self.assertTrue(math.validate_data(data))
        data = deepcopy(self.data)
        data['scored_criteria'][0]['weight'] = True
        self.assertTrue(math.validate_data(data))

    def test_totals_round_after_summing_not_before(self):
        data = {'scored_criteria': [{'id': 'a', 'weight': 33.33}, {'id': 'b', 'weight': 33.33}, {'id': 'c', 'weight': 33.34}],
                'scores': {'X': {c: {'raw': 1, 'weighted': .33} for c in 'abc'}},
                'total_scores': {'X': 1.00}, 'ranking': ['X']}
        self.assertEqual(math.validate_data(data), [])
        data['total_scores']['X'] = .99
        self.assertTrue(math.validate_data(data))

    def test_ranking_uses_unrounded_totals_and_accepts_exact_ties(self):
        data = {'scored_criteria': [{'id': 'a', 'weight': 100}],
                'scores': {'X': {'a': {'raw': 4.001, 'weighted': 4}}, 'Y': {'a': {'raw': 4.002, 'weighted': 4}}},
                'total_scores': {'X': 4, 'Y': 4}, 'ranking': ['Y', 'X']}
        self.assertEqual(math.validate_data(data), [])
        data['ranking'] = ['X', 'Y']
        self.assertTrue(math.validate_data(data))
        data['scores']['X']['a']['raw'] = 4.002
        self.assertEqual(math.validate_data(data), [])

    def test_invalid_transfer_and_changed_unrelated_weights(self):
        for changes in ({'shift': -10}, {'source_criterion': 'unknown'}, {'target_criterion': 'C1'},
                        {'adjusted_weights': {'C1': 20, 'C2': 35, 'C3': 24, 'C4': 21}},
                        {'adjusted_weights': {'unknown': 0}}):
            data = deepcopy(self.data)
            data['sensitivity']['scenarios'][0].update(changes)
            with self.subTest(changes=changes):
                self.assertTrue(math.validate_data(data))

    def test_sensitivity_cannot_claim_false_stability(self):
        data = deepcopy(self.data)
        data['sensitivity']['scenarios'][0]['ranking_change'] = True
        self.assertTrue(math.validate_data(data))
        data['sensitivity']['scenarios'] = []
        self.assertTrue(math.validate_data(data))

    def test_cli_input_errors_and_ambiguous_summaries(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / 'bad.md'
            for text in ('No JSON', '```json\n{\n```', '```json\nNaN\n```',
                         '```json\n{"scored_criteria": [], "scored_criteria": []}\n```'):
                path.write_text(text)
                self.assertTrue(math.validate_file(path)[1])
            original = (ROOT / 'tests/test-dar.md').read_text()
            path.write_text(original + '\n' + original)
            self.assertTrue(math.validate_file(path)[1])


if __name__ == '__main__':
    unittest.main()
