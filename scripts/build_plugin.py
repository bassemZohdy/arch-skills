#!/usr/bin/env python3
"""Build a Claude Code plugin directory from the default portable packages.

The plugin contains only the three public entry points. Each skill directory is a
complete built package, so shared framework contracts resolve from an isolated install.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import shutil
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import build_packages  # noqa: E402

PLUGIN_NAME = "arch-skills"
VERSION = "0.1.0"
DESCRIPTION = (
    "Software architecture skills: interview stakeholders, create or update a solution "
    "architecture, evaluate process readiness and review design quality. 31 specialist "
    "modules (APIs, data, security, resilience, diagrams, decisions, fitness functions) "
    "load on demand."
)
MANIFEST = {
    "name": PLUGIN_NAME,
    "version": VERSION,
    "description": DESCRIPTION,
    "author": {"name": "Bassem Zohdy", "url": "https://github.com/bassemZohdy"},
    "homepage": "https://github.com/bassemZohdy/arch-skills",
    "repository": "https://github.com/bassemZohdy/arch-skills",
    "license": "MIT",
    "keywords": ["architecture", "software-architecture", "design-review", "adr",
                 "diagrams", "quality-attributes", "documentation"],
}


README = """# Architecture Skills plugin

Portable software architecture skills for Claude Code. The plugin exposes three skills:

- `arch-orchestrator`: interview stakeholders, create a solution architecture, or update an existing baseline.
- `arch-evaluate`: assess process completeness, traceability and evidence freshness of an architecture baseline.
- `arch-review`: review design fitness, quality attributes, trade-offs, risks and technical debt.

Thirty-one specialist modules (APIs, data, security, resilience, diagrams, decisions, fitness
functions and more) are bundled as instructions that the three skills load on demand. They are not
separate skills.

## What the plugin runs

The plugin is Markdown instructions, templates and small deterministic Python helpers in
`scripts/` inside each skill. The helpers need Python 3.10+ and PyYAML, run locally only when a
skill invokes them, and make no network calls. The plugin has no hooks, MCP servers or background processes.

## Install

```
/plugin marketplace add bassemZohdy/arch-skills
/plugin install arch-skills@arch-skills
```

## Source and license

This folder is generated from https://github.com/bassemZohdy/arch-skills with
`python scripts/build_plugin.py`. Do not edit it by hand. Licensed under MIT, see `LICENSE`.
"""


def normalize_text(skills_dir):
    """Rewrite text files with LF and refresh package hashes so output is identical on every OS."""
    for package in sorted(p for p in Path(skills_dir).iterdir() if p.is_dir()):
        manifest_path = package / "package-manifest.json"
        for path in sorted(package.rglob("*")):
            if path.is_file() and path != manifest_path:
                data = path.read_bytes()
                if b"\0" not in data and b"\r\n" in data:
                    path.write_bytes(data.replace(b"\r\n", b"\n"))
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        manifest["files"] = {p.relative_to(package).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
                             for p in sorted(package.rglob("*")) if p.is_file() and p != manifest_path}
        manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8", newline="\n")


def build(destination):
    destination = Path(destination).resolve()
    if destination.exists():
        raise ValueError("destination must not exist; choose a fresh directory (no implicit deletion/overwrite)")
    destination.mkdir(parents=True)
    names = build_packages.build(destination / "skills", "default")
    normalize_text(destination / "skills")
    manifest_dir = destination / ".claude-plugin"
    manifest_dir.mkdir()
    manifest_text = json.dumps(MANIFEST, indent=2) + "\n"
    (manifest_dir / "plugin.json").write_text(manifest_text, encoding="utf-8", newline="\n")
    (destination / "README.md").write_text(README, encoding="utf-8", newline="\n")
    shutil.copyfile(ROOT / "assets/plugin-icon.png", manifest_dir / "icon.png")  # binary
    license_bytes = (ROOT / "LICENSE").read_bytes().replace(b"\r\n", b"\n")
    (destination / "LICENSE").write_bytes(license_bytes)
    return names


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        names = build(args.output)
    except (ValueError, OSError) as exc:
        parser.exit(2, f"plugin build refused: {exc}\n")
    print(json.dumps({"output": str(args.output.resolve()), "skills": names}, indent=2))


if __name__ == "__main__":
    main()
