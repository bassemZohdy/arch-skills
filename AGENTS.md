# AGENTS.md

## What This Repo Is

Codex skills for software architecture: documentation generation (`arch-doc`), review/validation (`arch-review`), fitness functions (`arch-fitness`), and decision analysis (`arch-decision`). Skills are Markdown + YAML + templates — no compiled code.

## Key Commands

```powershell
# Validate skill structure (210 tests, fast, no LLM needed)
python tests/test_skills.py

# Sync skills to Codex install location
.\sync-skills.ps1

# Run skillprobe tests (requires Claude Code CLI + API key)
skillprobe run tests/test-arch-doc.yaml --harness claude-code
```

## Repo Structure

- `skills/<name>/SKILL.md` — Skill entry point. Must have YAML frontmatter with `name` and `description`.
- `skills/<name>/references/` — Detailed guides loaded on demand. Keep SKILL.md lean; move content here.
- `skills/<name>/assets/` — Templates/files used in output, not loaded into context.
- `skills/<name>/agents/openai.yaml` — UI metadata. Regenerate with `generate_openai_yaml.py`.
- `tests/` — Structural validation (`test_skills.py`) and skillprobe scenarios (`.yaml`).
- `sync-skills.ps1` — Copies skills to `~/.codex/skills/`. Run after edits.

## Skill Authoring Conventions

- Description is the **primary trigger mechanism** — include all "when to use" info there, not in body.
- Keep SKILL.md under 500 lines. Split details into `references/`.
- Use imperative/infinitive form in instructions.
- No README.md, CHANGELOG.md, or auxiliary docs inside skill dirs.
- Diagram format priority: Mermaid > PlantUML > Draw.io.

## Validation

After editing any skill:
1. `python tests/test_skills.py` — must pass all 210 checks
2. `.\sync-skills.ps1` — sync to Codex

For end-to-end testing (optional, needs Claude Code CLI):
```bash
skillprobe run tests/test-arch-<skill>.yaml --harness claude-code
```

## Gotchas

- `skillprobe` only supports `claude-code` and `cursor` harnesses — no dry-run mode.
- Windows symlinks require admin privileges or Developer Mode. Repo uses copy+sync instead.
- `quick_validate.py` lives at `~/.codex/skills/.system/skill-creator/scripts/`.
- Skills are generic (framework/language agnostic) by design.
