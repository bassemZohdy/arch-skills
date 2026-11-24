#!/usr/bin/env python3
"""Generate the installable plugins under plugins/ from the built default packages.

Two editions are generated:

- arch-skills: the full plugin (three skills, bundled Python helpers).
- solution-architecture-skills: a script-free edition for the Claude plugin directory,
  which accepts only text, JSON, YAML and image files from unverified organizations.
  It omits arch-evaluate, whose core is the deterministic scripts.

The plugins ship the built default packages, not the source skills: shared framework
files and specialist modules are added by scripts/build_packages.py.
Use --check in CI to fail when a committed plugin differs from a fresh build.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil
import sys
import tempfile

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_packages  # noqa: E402

ROOT = build_packages.ROOT
PLUGINS = ROOT / "plugins"
PLUGIN_VERSION = "0.1.3"  # bump on every change to a generated plugin; Codex caches installs by it
REPO = "https://github.com/bassemZohdy/arch-skills"
EDITIONS = {
    "arch-skills": {
        "skills": None,  # all default entry points
        "strip_scripts": False,
        "readme": "assets/plugin-readme.md",
        "description": ("Software architecture skills: end-to-end architecture design orchestration, "
                        "process evaluation, and design review with 30+ bundled specialist modules "
                        "(patterns, quality attributes, security, data, integration, decisions, diagrams)."),
    },
    "solution-architecture-skills": {
        "skills": ("arch-orchestrator", "arch-review"),
        "strip_scripts": True,
        "readme": "assets/plugin-readme-directory.md",
        "description": ("Interview stakeholders, create or update a solution architecture, and review design "
                        "quality with 30+ bundled specialist modules (patterns, quality attributes, security, "
                        "data, integration, decisions, diagrams). Instructions only; no scripts."),
    },
}
NOTICE = """
## Script-free edition

This edition ships without the Python helper scripts (`scripts/dap*.py`, `validate_math.py`)
because the plugin directory accepts only text, JSON, YAML and image files. Never run,
simulate or claim a deterministic check. Where an instruction names a helper script, do the
check by hand, label the result provisional, and tell the user that the full `arch-skills`
plugin from https://github.com/bassemZohdy/arch-skills bundles the scripts.

Diagram templates (`*-templates/*.mmd`, `.puml`, `.drawio`) ship with an added `.txt` suffix for
the same reason. Drop the `.txt` suffix when you save a template into the user's project.
"""


def manifest(name, description, codex):
    data = {
        "name": name,
        "version": PLUGIN_VERSION,
        "description": description,
        "author": {"name": "Bassem Zohdy"},
        "homepage": REPO,
        "repository": REPO,
        "license": "MIT",
        "keywords": ["architecture", "design-review", "adr", "agent-skills"],
    }
    if codex:
        data["skills"] = "./skills/"
    return json.dumps(data, indent=2) + "\n"


TEMPLATE_SUFFIXES = (".mmd", ".puml", ".drawio")
TEMPLATE_REFERENCE = re.compile(rb"(-templates/[\w.-]+?\.(?:mmd|puml|drawio))(?!\.txt)")


def strip_scripts(package: Path) -> None:
    """Remove executable helpers, annotate SKILL.md and rewrite the package manifest to match."""
    for path in sorted(package.rglob("*"), reverse=True):
        if path.is_file() and (path.suffix == ".py" or path.name == "requirements.txt"):
            path.unlink()
        elif path.is_dir() and not any(path.iterdir()):
            path.rmdir()
    # The directory accepts only Markdown, text, JSON, YAML and images, so diagram templates become .txt.
    for path in sorted(package.rglob("*")):
        if path.is_file() and path.suffix in TEMPLATE_SUFFIXES:
            path.rename(path.with_name(path.name + ".txt"))
    for path in sorted(package.rglob("*")):
        if path.is_file() and path.suffix in (".md", ".yaml", ".yml") or path.is_file() and path.suffix == ".json" and path.name != "package-manifest.json":
            text = path.read_bytes()
            updated = TEMPLATE_REFERENCE.sub(rb"\1.txt", text)
            if updated != text:
                path.write_bytes(updated)
    entry = package / "SKILL.md"
    entry.write_bytes(entry.read_bytes().rstrip(b"\n") + b"\n" + NOTICE.encode("utf-8"))
    manifest_path = package / "package-manifest.json"
    data = json.loads(manifest_path.read_text(encoding="utf-8"))
    data["files"] = {p.relative_to(package).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
                     for p in sorted(package.rglob("*"), key=lambda q: q.relative_to(package).as_posix())
                     if p.is_file() and p != manifest_path}
    manifest_path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8", newline="\n")


def generate(destination: Path, name: str = "arch-skills") -> None:
    edition = EDITIONS[name]
    with tempfile.TemporaryDirectory() as tmp:
        packages = Path(tmp) / "packages"
        names = build_packages.build(packages, "default")
        assert names, "no packages built"
        keep = edition["skills"] or tuple(names)
        (destination / "skills").mkdir(parents=True)
        for skill in keep:
            shutil.copytree(packages / skill, destination / "skills" / skill)
            if edition["strip_scripts"]:
                strip_scripts(destination / "skills" / skill)
    for folder, codex in ((".claude-plugin", False), (".codex-plugin", True)):
        target = destination / folder
        target.mkdir(parents=True)
        (target / "plugin.json").write_text(manifest(name, edition["description"], codex), encoding="utf-8", newline="\n")
    # The plugin directory requires a README and a listing icon inside the plugin folder.
    shutil.copyfile(ROOT / edition["readme"], destination / "README.md")
    shutil.copyfile(ROOT / "assets/plugin-icon.png", destination / ".claude-plugin/icon.png")


def digest(root: Path) -> dict:
    return {p.relative_to(root).as_posix(): hashlib.sha256(p.read_bytes().replace(b"\r\n", b"\n")).hexdigest()  # ignore checkout line endings
            for p in sorted(root.rglob("*")) if p.is_file()}


def check(name: str) -> bool:
    plugin_dir = PLUGINS / name
    with tempfile.TemporaryDirectory() as tmp:
        fresh = Path(tmp) / name
        generate(fresh, name)
        want, have = digest(fresh), digest(plugin_dir) if plugin_dir.exists() else {}
        changed = sorted(set(want) ^ set(have) | {k for k in want.keys() & have.keys() if want[k] != have[k]})
        detail = []
        for rel in changed[:3]:
            fresh_lines = (fresh / rel).read_text(encoding="utf-8", errors="replace").splitlines() if (fresh / rel).is_file() else []
            kept_lines = (plugin_dir / rel).read_text(encoding="utf-8", errors="replace").splitlines() if (plugin_dir / rel).is_file() else []
            detail += [f"{rel}: {tag} {line}" for tag, lines, other in (("fresh", fresh_lines, kept_lines), ("committed", kept_lines, fresh_lines))
                       for line in lines if line not in other][:4]
    if want != have:
        print(f"plugins/{name} is out of date ({len(changed)} files differ, e.g. {changed[:3]}); run python scripts/build_plugin.py")
        print("\n".join(detail))
        return False
    print(f"plugins/{name} matches a fresh build")
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="fail if a committed plugin differs from a fresh build")
    args = parser.parse_args()
    if args.check:
        results = [check(name) for name in EDITIONS]
        return 0 if all(results) else 1
    for name in EDITIONS:
        plugin_dir = PLUGINS / name
        if plugin_dir.exists():
            shutil.rmtree(plugin_dir)  # generated output only; never touches sources
        plugin_dir.parent.mkdir(parents=True, exist_ok=True)
        generate(plugin_dir, name)
        print(f"wrote {plugin_dir.relative_to(ROOT)} (version {PLUGIN_VERSION})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
