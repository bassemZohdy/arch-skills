#!/usr/bin/env python3
"""Build portable default/expert packages from one canonical source tree."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ("arch-orchestrator", "arch-evaluate", "arch-review")


def copy_skill(source, destination, module=False):
    for path in sorted(source.rglob("*")):
        if path.is_symlink():
            raise ValueError(f"symlink not allowed in canonical package: {path}")
        if not path.is_file() or "__pycache__" in path.parts:
            continue
        relative = path.relative_to(source)
        if relative.parts[0] == "agents":
            raise ValueError("host metadata is not part of the portable distribution")
        if relative.name == "SKILL.md" and module:
            relative = relative.with_name("instructions.md")
        target = destination / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(path, target)


def build(destination, profile="default", selected=None):
    destination = Path(destination).resolve()
    source_roots = [ROOT / folder for folder in ('skills', 'framework', 'scripts')]
    if any(destination.is_relative_to(source.resolve()) for source in source_roots):
        raise ValueError('destination must be outside canonical source directories')
    if destination.exists():
        raise ValueError("destination must not exist; choose a fresh directory (no implicit deletion/overwrite)")
    if profile not in {"default", "expert"}:
        raise ValueError("profile must be default or expert")
    skills = {p.name: p for p in (ROOT / "skills").glob("arch-*") if p.is_dir()}
    if profile == 'default' and not set(PUBLIC).issubset(skills):
        raise ValueError('default profile requires all public source SKILL.md entries')
    for name, source in skills.items():
        if not (source / 'SKILL.md').is_file():
            raise ValueError(f'{name}: missing SKILL.md')
    for source in source_roots:
        if source.is_symlink() or any(path.is_symlink() for path in source.rglob('*')):
            raise ValueError(f'symlink not allowed in canonical source: {source}')
    for required in ('LICENSE', 'requirements.txt'):
        if not (ROOT / required).is_file() or (ROOT / required).is_symlink():
            raise ValueError(f'canonical {required} must be a regular source file')
    names = list(PUBLIC) if profile == "default" else sorted(skills)
    if selected:
        if profile != "expert" or any(n not in skills for n in selected):
            raise ValueError("--skill requires expert profile and known canonical names")
        names = sorted(set(selected))
    destination.mkdir(parents=True)
    for name in names:
        package = destination / name
        copy_skill(skills[name], package)
        if name in PUBLIC:
            catalog = {}
            for other, source in sorted(skills.items()):
                if other == name:
                    continue
                module = package / "references/specialists" / other
                copy_skill(source, module, module=True)
                catalog[other] = {"instructions": f"references/specialists/{other}/instructions.md",
                                  "resource_root": f"references/specialists/{other}"}
            (package / "package-catalog.json").write_text(json.dumps(catalog, indent=2) + "\n", encoding="utf-8")
        # Deterministic shared contracts are bundled, never resolved from the source checkout.
        shutil.copytree(ROOT / "framework", package / "framework")
        shutil.copytree(ROOT / "scripts/dap", package / "scripts/dap", ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
        for script in (ROOT / "scripts").glob("dap_*.py"):
            shutil.copyfile(script, package / "scripts" / script.name)
        shutil.copyfile(ROOT / "requirements.txt", package / "requirements.txt")
        shutil.copyfile(ROOT / "LICENSE", package / "LICENSE")
        files = {p.relative_to(package).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
                 for p in sorted(package.rglob("*")) if p.is_file()}
        (package / "package-manifest.json").write_text(json.dumps({"profile": profile, "name": name,
            "public_entry": "SKILL.md", "files": files}, indent=2) + "\n", encoding="utf-8")
    return names


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--profile", choices=("default", "expert"), default="default")
    parser.add_argument("--skill", action="append")
    args = parser.parse_args()
    try:
        names = build(args.output, args.profile, args.skill)
    except (ValueError, OSError) as exc:
        parser.exit(2, f"package build refused: {exc}\n")
    print(json.dumps({"output": str(args.output.resolve()), "profile": args.profile, "skills": names}, indent=2))


if __name__ == "__main__":
    main()
