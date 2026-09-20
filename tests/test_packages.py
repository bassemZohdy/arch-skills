"""Validate release contents from isolated locations, not source-root assumptions."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from dap_fixture import ROOT, make_project
from test_skills import validate_skill, discover_skills
from build_packages import build, PUBLIC


class PackageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory(prefix="architecture-packages-")
        cls.root = Path(cls.temp.name)
        cls.output = cls.root / "default"
        build(cls.output)
        cls.project = make_project(cls.root / "project")

    @classmethod
    def tearDownClass(cls):
        cls.temp.cleanup()

    def test_default_has_exactly_three_discoverable_skills(self):
        entries = list(self.output.rglob("SKILL.md"))
        self.assertEqual({p.parent.name for p in entries}, set(PUBLIC))
        self.assertEqual(len(entries), 3)

    def test_bundled_modules_and_all_local_resources_resolve(self):
        for name in PUBLIC:
            package = self.output / name
            catalog = json.loads((package / "package-catalog.json").read_text())
            self.assertEqual(len(catalog), len(discover_skills(ROOT / "skills")) - 1)
            self.assertIn("arch-diagrams", catalog)
            self.assertTrue((package / catalog["arch-diagrams"]["instructions"]).is_file())
            for other, entry in catalog.items():
                self.assertTrue((package / entry["instructions"]).is_file(), other)
                self.assertFalse((package / entry["resource_root"] / "SKILL.md").exists())
                from test_skills import resource_paths
                module_root = package / entry["resource_root"]
                for document in module_root.rglob("*.md"):
                    for path in resource_paths(document.read_text(encoding="utf-8")):
                        base = package if path.startswith("framework/") or path.startswith("scripts/dap") else module_root
                        self.assertTrue((base / path).exists() or (document.parent / path).exists(),
                                        f"{name}/{other}/{document.name}: {path}")

    def test_isolated_runtime_from_unrelated_working_directory(self):
        package = self.output / "arch-evaluate"
        run = subprocess.run([sys.executable, str(package / "scripts/dap_validate.py"), str(self.project)],
                             cwd=self.root, capture_output=True, text=True)
        self.assertEqual(run.returncode, 0, run.stderr + run.stdout)
        self.assertTrue(json.loads(run.stdout)["gate"]["ready"])

    def test_bundled_decision_helper_from_unrelated_directory(self):
        helper = self.output / "arch-orchestrator/references/specialists/arch-decision/scripts/validate_math.py"
        run = subprocess.run([sys.executable, str(helper), str(ROOT / "tests/test-dar.md")],
                             cwd=self.root, capture_output=True, text=True)
        self.assertEqual(run.returncode, 0, run.stdout + run.stderr)

    def test_manifest_covers_every_shipped_file(self):
        import hashlib
        for name in PUBLIC:
            package = self.output / name
            manifest = json.loads((package / "package-manifest.json").read_text())
            shipped = {p.relative_to(package).as_posix() for p in package.rglob("*") if p.is_file()
                       and p.name != "package-manifest.json" and "__pycache__" not in p.parts}
            self.assertEqual(set(manifest["files"]), shipped)
            for relative, digest in manifest["files"].items():
                self.assertEqual(hashlib.sha256((package / relative).read_bytes()).hexdigest(), digest)

    def test_expert_profile_and_selected_specialist(self):
        destination = self.root / "expert"
        skill_count = len(discover_skills(ROOT / "skills"))
        self.assertEqual(len(build(destination, "expert")), skill_count)
        self.assertEqual(len(list(destination.rglob("SKILL.md"))), skill_count)
        single = self.root / "single"
        self.assertEqual(build(single, "expert", ["arch-api"]), ["arch-api"])
        self.assertEqual(validate_skill(single / "arch-api"), [])

    def test_existing_destination_is_not_overwritten(self):
        with self.assertRaises(ValueError):
            build(self.output)


class StructuralRegressionTests(unittest.TestCase):
    def test_short_valid_skill_does_not_require_padding_or_empty_directories(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "arch-small"
            root.mkdir()
            (root / "SKILL.md").write_text("---\nname: arch-small\ndescription: Review a bounded contract.\n---\n# Contract review\nInspect the contract and report evidenced findings.\n")
            self.assertEqual(validate_skill(root), [])
            (root / "SKILL.md").write_text("---\nname: ''\ndescription: ''\n---\n# Invalid\n")
            self.assertTrue(validate_skill(root))

    def test_missing_entry_is_discovered_and_inline_resource_is_checked(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "arch-missing"
            root.mkdir()
            self.assertEqual(discover_skills(Path(directory)), ["arch-missing"])
            self.assertTrue(validate_skill(root))
            (root / "SKILL.md").write_text("---\nname: arch-missing\ndescription: Review a contract.\n---\nRead `references/absent.md`.\n")
            self.assertTrue(any("absent.md" in x for x in validate_skill(root)))


if __name__ == "__main__":
    unittest.main()
