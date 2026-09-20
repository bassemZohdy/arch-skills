import json
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from check_diagrams import check, discover_sources, validate_source


class DiagramChecks(unittest.TestCase):
    def test_repository_mermaid_inventory_is_valid_without_renderer(self):
        report = check(ROOT)
        self.assertGreaterEqual(len(report["sources"]), 20)
        self.assertEqual(report["errors"], [])
        self.assertIsNone(report["renderer"])

    def test_fenced_and_file_sources_are_discovered(self):
        sources = discover_sources(ROOT)
        self.assertTrue(any(item["kind"] == "file" and item["path"].suffix == ".mmd" for item in sources))
        self.assertTrue(any(item["kind"] == "fence" for item in sources))

    def test_unknown_or_empty_source_is_rejected(self):
        with self.assertRaises(ValueError):
            validate_source("", "empty")
        with self.assertRaises(ValueError):
            validate_source("not-a-diagram\n", "unknown")

    def test_report_is_written_for_static_check(self):
        with tempfile.TemporaryDirectory() as directory:
            report = check(ROOT, Path(directory))
            saved = json.loads((Path(directory) / "report.json").read_text())
            self.assertEqual(saved["sources"], report["sources"])
            self.assertEqual(saved["errors"], [])

    def test_renderer_command_receives_isolated_input_and_output_paths(self):
        from check_diagrams import check
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "source"
            root.mkdir()
            (root / "sample.mmd").write_text("graph LR\n  A --> B\n", encoding="utf-8")
            output = Path(directory) / "output"
            command = [sys.executable, "-c",
                       "from pathlib import Path; import sys; "
                       "Path(sys.argv[sys.argv.index('-o') + 1]).write_text('svg')"]
            report = check(root, output, command)
            self.assertEqual(report["errors"], [])
            self.assertEqual(report["rendered"], 1)
            self.assertTrue((output / "diagram-0001.svg").is_file())


if __name__ == "__main__":
    unittest.main()
