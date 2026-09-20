#!/usr/bin/env python3
"""Offline structural validation of source skills and their local resources."""
from __future__ import annotations
import re
from pathlib import Path
import sys
import yaml
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from check_links import prose

ROOT = Path(__file__).resolve().parents[1]


def discover_skills(skills_dir):
    # Missing SKILL.md must be reported, not silently removed from discovery.
    return sorted(p.name for p in Path(skills_dir).iterdir() if p.is_dir() and p.name.startswith("arch-"))


def resource_paths(content):
    values = re.findall(r"\]\(([^)]+)\)", content)
    values += re.findall(r"`((?:references|assets|framework|scripts)/[^`\n]+)`", content)
    values += re.findall(r"\b(scripts/dap[_a-z/]+\.py)\b", content)
    return sorted({v.split("#", 1)[0] for v in values if not v.startswith(("http:", "https:", "#", "mailto:"))
                   and v and not any(c in v for c in "<>{}*")})


def validate_skill(directory, shared_root=None):
    directory = Path(directory)
    shared_root = Path(shared_root) if shared_root else directory
    errors = []
    entry = directory / "SKILL.md"
    if not entry.is_file():
        return ["missing SKILL.md"]
    text = entry.read_text(encoding="utf-8")
    try:
        match = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)", text, re.S)
        if not match:
            raise ValueError("missing YAML frontmatter")
        meta = yaml.safe_load(match.group(1))
        if not isinstance(meta, dict):
            raise ValueError("frontmatter must be a mapping")
        name, desc = meta.get("name"), meta.get("description")
        if not isinstance(name, str) or name != directory.name or len(name) > 64 or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
            errors.append("name must match directory and portable naming rules")
        if not isinstance(desc, str) or not desc.strip() or len(desc) > 1024:
            errors.append("description must be a nonempty string of at most 1024 characters")
    except (ValueError, yaml.YAMLError) as exc:
        errors.append(f"frontmatter: {exc}")
    if len(text.splitlines()) > 500:
        errors.append("entry point exceeds 500 lines")
    # Keep DAP asset routing in one place; a second output-template section
    # repeats the same instruction and makes the entrypoint harder to scan.
    if re.search(r"^## DAP contribution$", text, re.M) and re.search(r"^## Output template$", text, re.M):
        errors.append("duplicate output-template routing; keep it in DAP contribution")
    body = prose(text)
    headings = re.findall(r"^#{1,4}\s+(.+)$", body, re.M)
    lowered = [h.strip().lower() for h in headings]
    if len(set(lowered)) != len(lowered):
        errors.append("duplicate entry-point headings")
    for name in ("README.md", "CHANGELOG.md"):
        if (directory / name).exists():
            errors.append(f"auxiliary skill file not allowed: {name}")
    if (directory / "agents").exists() and any((directory / "agents").rglob("*")):
        errors.append("host-specific metadata must remain outside canonical packages")
    for path in directory.rglob("*"):
        if path.is_symlink():
            errors.append(f"symlink resource: {path.relative_to(directory)}")
        if path.is_file() and path.suffix in {".md", ".json", ".yaml"} and not path.stat().st_size:
            errors.append(f"empty resource: {path.relative_to(directory)}")
    for path in directory.rglob("*.md"):
        # Local resource references in all maintained documents, not just Markdown
        # links in the entry point. Code examples are not dependency declarations.
        content = path.read_text(encoding="utf-8")
        content = prose(content)
        for relative in resource_paths(content):
            base = shared_root if relative.startswith("framework/") or relative.startswith("scripts/dap") else directory
            candidate = base / relative
            if not candidate.exists() and not (path.parent / relative).exists():
                errors.append(f"{path.relative_to(directory)}: missing resource {relative}")
    # Skill names are semantic handoffs, not mandatory installed dependencies.
    canonical = shared_root / "skills"
    if canonical.is_dir():
        known = set(discover_skills(canonical))
        for name in set(re.findall(r"\barch-[a-z]+(?:-[a-z]+)*\b", body)):
            if name not in known:
                errors.append(f"unknown related skill: {name}")
    return sorted(set(errors))


def unreachable_resources(directory):
    """Walk declared resource pointers from SKILL.md; directory pointers include assets."""
    directory = Path(directory).resolve()
    reached, pending = set(), [directory / "SKILL.md"]
    while pending:
        item = pending.pop()
        if item in reached or not item.is_file():
            continue
        reached.add(item)
        if item.suffix != ".md":
            continue
        for relative in resource_paths(prose(item.read_text(encoding="utf-8"))):
            candidates = [directory / relative, item.parent / relative]
            target = next((p.resolve() for p in candidates if p.exists()), None)
            if target and target.is_relative_to(directory):
                pending.extend(target.rglob("*") if target.is_dir() else [target])
    return sorted(p.relative_to(directory).as_posix() for folder in ("references", "assets", "scripts")
                  for p in (directory / folder).rglob("*") if p.is_file()
                  and "__pycache__" not in p.parts and p not in reached)


def main():
    directory = ROOT / "skills"
    names = discover_skills(directory)
    errors = []
    for name in names:
        problems = validate_skill(directory / name, ROOT)
        print(f"{'FAIL' if problems else 'PASS'} {name}")
        errors.extend(f"{name}: {problem}" for problem in problems)
        errors.extend(f"{name}: unreachable resource {path}" for path in unreachable_resources(directory / name))
    catalog = (directory / "arch-orchestrator/references/skill-catalog.md").read_text(encoding="utf-8")
    errors.extend(f"catalog omits {name}" for name in names if name != "arch-orchestrator" and name not in catalog)
    print("\n".join(errors))
    print(f"Validated {len(names)} skills; {len(errors)} errors. External links/live behavior not tested.")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
