#!/usr/bin/env python3
"""Generate the installable plugin (default profile) under plugins/arch-skills.

The plugin ships the built default packages, not the source skills: shared
framework files and specialist modules are added by scripts/build_packages.py.
Use --check in CI to fail when the committed plugin differs from a fresh build.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import shutil
import sys
import tempfile

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_packages  # noqa: E402

ROOT = build_packages.ROOT
PLUGIN_DIR = ROOT / "plugins" / "arch-skills"
PLUGIN_VERSION = "0.1.1"  # bump on every change to the generated plugin; Codex caches installs by it
REPO = "https://github.com/bassemZohdy/arch-skills"
DESCRIPTION = ("Software architecture skills: end-to-end architecture design orchestration, "
               "process evaluation, and design review with 30+ bundled specialist modules "
               "(patterns, quality attributes, security, data, integration, decisions, diagrams).")


def manifest(codex):
    data = {
        "name": "arch-skills",
        "version": PLUGIN_VERSION,
        "description": DESCRIPTION,
        "author": {"name": "Bassem Zohdy"},
        "homepage": REPO,
        "repository": REPO,
        "license": "MIT",
        "keywords": ["architecture", "design-review", "adr", "agent-skills"],
    }
    if codex:
        data["skills"] = "./skills/"
    return json.dumps(data, indent=2) + "\n"


def generate(destination: Path) -> None:
    with tempfile.TemporaryDirectory() as tmp:
        packages = Path(tmp) / "packages"
        names = build_packages.build(packages, "default")
        shutil.copytree(packages, destination / "skills")
    assert names, "no packages built"
    for folder, codex in ((".claude-plugin", False), (".codex-plugin", True)):
        target = destination / folder
        target.mkdir(parents=True)
        (target / "plugin.json").write_text(manifest(codex), encoding="utf-8")


def digest(root: Path) -> dict:
    return {p.relative_to(root).as_posix(): hashlib.sha256(p.read_bytes().replace(b"\r\n", b"\n")).hexdigest()  # ignore checkout line endings
            for p in sorted(root.rglob("*")) if p.is_file()}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="fail if plugins/arch-skills differs from a fresh build")
    args = parser.parse_args()
    if args.check:
        with tempfile.TemporaryDirectory() as tmp:
            fresh = Path(tmp) / "arch-skills"
            generate(fresh)
            want, have = digest(fresh), digest(PLUGIN_DIR) if PLUGIN_DIR.exists() else {}
        if want != have:
            changed = sorted(set(want) ^ set(have) | {k for k in want.keys() & have.keys() if want[k] != have[k]})
            print(f"plugins/arch-skills is out of date ({len(changed)} files differ, e.g. {changed[:3]}); run python scripts/build_plugin.py")
            return 1
        print("plugins/arch-skills matches a fresh build")
        return 0
    if PLUGIN_DIR.exists():
        shutil.rmtree(PLUGIN_DIR)  # generated output only; never touches sources
    PLUGIN_DIR.parent.mkdir(parents=True, exist_ok=True)
    generate(PLUGIN_DIR)
    print(f"wrote {PLUGIN_DIR.relative_to(ROOT)} (version {PLUGIN_VERSION})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
