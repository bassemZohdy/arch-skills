"""Regression coverage for links, anchors, resource reachability and probe results."""
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
from urllib.error import HTTPError, URLError

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from check_links import anchors, check_local, links, probe
from test_skills import unreachable_resources, validate_skill


class LinkTests(unittest.TestCase):
    def test_repository_links(self):
        self.assertEqual(check_local(ROOT)['errors'], [])

    def test_links_use_document_directory_and_validate_fragments(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / 'guide').mkdir()
            (root / 'guide/target.md').write_text('# Target\n## Detail\n')
            (root / 'guide/index.md').write_text('[ok](target.md#detail)\n[missing](target.md#absent)\n[bad](absent.md)\n')
            errors = check_local(root)['errors']
            self.assertEqual(len(errors), 2)
            self.assertTrue(any('missing anchor' in e for e in errors))
            self.assertTrue(any('missing target' in e for e in errors))

    def test_fenced_examples_inline_code_and_link_titles(self):
        text = '~~~md\n[example](absent.md)\n~~~\n`[code](absent.md)`\n[real](<file with spaces.md> "title")\n'
        self.assertEqual([target for _, target in links(text)], ['file with spaces.md'])

    def test_balanced_destinations_and_reference_links(self):
        text = '[wiki](https://example.org/Test_(topic))\n[guide][ref]\n[ref]: target.md#heading\n[broken][unknown]\n'
        found = [target for _, target in links(text)]
        self.assertIn('https://example.org/Test_(topic)', found)
        self.assertIn('target.md#heading', found)
        self.assertIn('UNDEFINED-REFERENCE:unknown', found)

    def test_duplicate_headings_and_explicit_ids(self):
        found = anchors('# A & B\n## A & B\n# A--B-1\nTitle\n=====\n<a id="custom"></a>\n```md\n# False\n```')
        self.assertTrue({'a--b', 'a--b-1', 'a--b-1-1', 'title', 'custom'} <= found)
        self.assertNotIn('false', found)

    def test_encoded_path_anchor_and_root_escape(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / 'a b.md').write_text('# Résumé\n')
            (root / 'index.md').write_text('[ok](a%20b.md#r%C3%A9sum%C3%A9)\n[bad](../escape.md)\n')
            errors = check_local(root)['errors']
            self.assertEqual(len(errors), 1)
            self.assertIn('escapes root', errors[0])

    def test_http_denials_and_network_errors_are_not_broken(self):
        for code, status in [(404, 'broken'), (410, 'broken'), (403, 'unverified'), (429, 'unverified'), (500, 'unverified')]:
            with self.subTest(code=code), patch('check_links.urlopen', side_effect=HTTPError('https://example.org', code, '', {}, None)):
                self.assertEqual(probe('https://example.org')['status'], status)
        with patch('check_links.urlopen', side_effect=URLError('timeout')):
            self.assertEqual(probe('https://example.org')['status'], 'unverified')

    def test_orphan_chain_is_not_reachable_until_entry_links_it(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / 'references').mkdir()
            (root / 'SKILL.md').write_text('# Entry\n')
            (root / 'references/a.md').write_text('Read `references/b.md`.\n')
            (root / 'references/b.md').write_text('Useful reference.\n')
            self.assertEqual(len(unreachable_resources(root)), 2)
            (root / 'SKILL.md').write_text('Read `references/a.md`.\n')
            self.assertEqual(unreachable_resources(root), [])

    def test_local_script_cannot_accidentally_resolve_to_shared_script(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            skill = root / 'skills/arch-check'
            skill.mkdir(parents=True)
            (root / 'scripts').mkdir()
            (root / 'scripts/local.py').write_text('pass\n')
            (skill / 'SKILL.md').write_text('---\nname: arch-check\ndescription: Check a contract.\n---\nUse `scripts/local.py`.\n')
            self.assertTrue(any('missing resource' in e for e in validate_skill(skill, root)))


if __name__ == '__main__':
    unittest.main()
