"""The committed Claude Code plugin must equal a fresh build from canonical sources."""
import filecmp
import json
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import build_plugin  # noqa: E402


def differences(left, right):
    cmp = filecmp.dircmp(left, right)
    found = [f"only in committed: {n}" for n in cmp.left_only] + [f"only in fresh: {n}" for n in cmp.right_only]
    found += [f"differs: {n}" for n in filecmp.cmpfiles(left, right, cmp.common_files, shallow=False)[1]]
    for sub in cmp.common_dirs:
        found += [f"{sub}/{d}" for d in differences(Path(left) / sub, Path(right) / sub)]
    return found


class PluginTests(unittest.TestCase):
    def test_committed_plugin_matches_fresh_build(self):
        with tempfile.TemporaryDirectory() as tmp:
            fresh = Path(tmp) / "plugin"
            build_plugin.build(fresh)
            self.assertEqual([], differences(ROOT / "plugins/arch-skills", fresh),
                             "regenerate with: python scripts/build_plugin.py into a fresh dir")

    def test_marketplace_points_at_plugin(self):
        market = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text(encoding="utf-8"))
        manifest = json.loads((ROOT / "plugins/arch-skills/.claude-plugin/plugin.json").read_text(encoding="utf-8"))
        entry = market["plugins"][0]
        self.assertEqual(manifest["name"], entry["name"])
        self.assertEqual(manifest["version"], entry["version"])
        self.assertTrue((ROOT / entry["source"] / ".claude-plugin/plugin.json").is_file())


if __name__ == "__main__":
    unittest.main()
