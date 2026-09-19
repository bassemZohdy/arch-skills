# AGENTS.md

## What This Repo Is

Portable Agent Skills for software architecture: documentation generation (`arch-doc`), review/validation (`arch-review`), fitness functions (`arch-fitness`), decision analysis (`arch-decision`), orchestration of end-to-end design (`arch-orchestrator`), and 28 more specialized skills covering architecture concerns. Skills are Markdown + YAML + templates; host adapters are kept in scripts and test configuration, not in skill instructions.

## Key Commands

```powershell
# Validate skill structure (discovered checks, no LLM needed)
python tests/test_skills.py

# Sync skills to Codex install location
.\sync-skills.ps1

 # Run an optional behavioral scenario through a selected host adapter
<adapter-runner> run tests/test-arch-doc.yaml --skill-root ./skills/arch-doc
```

## Repo Structure

- `skills/<name>/SKILL.md` — Skill entry point. Must have YAML frontmatter with `name` and `description`.
- `skills/<name>/references/` — Detailed guides loaded on demand. Keep SKILL.md lean; move content here.
- `skills/<name>/assets/` — Templates/files used in output, not loaded into context.
- `skills/<name>/agents/openai.yaml` — Optional UI metadata for a host adapter. Regenerate with `generate_openai_yaml.py`.
- `tests/` — Structural validation (`test_skills.py`) and optional adapter-driven scenarios (`.yaml`).
- `scripts/` — Detection and sync scripts for multiple AI harnesses.
- `sync-skills.ps1` — Copies skills to `~/.codex/skills/`. Run after edits.

## Skill Authoring Conventions

- Description is the **primary trigger mechanism** — include all "when to use" info there, not in body.
- Keep SKILL.md under 500 lines. Split details into `references/`.
- Use imperative/infinitive form in instructions.
- No README.md, CHANGELOG.md, or auxiliary docs inside skill dirs.
- Diagram format priority: Mermaid > PlantUML > Draw.io.

## Validation

After editing any skill:
1. `python tests/test_skills.py` — must pass all applicable checks
2. `.\sync-skills.ps1` — sync to Codex

For end-to-end testing, use the adapter runner available in your environment:
~~~text
<adapter-runner> run tests/test-arch-<skill>.yaml --skill-root ./skills/arch-<skill>
~~~

## Gotchas

- Framework implementation is defined in `docs/deterministic-architecture-process.md`. Read it and `docs/framework-implementation-plan.md` before changing the DAP contracts.
- Extend `arch-orchestrator` for execution; add `arch-evaluate` only for process assessment. Keep design-quality review in `arch-review`.
- Do not describe planned framework behavior as available. Shared contracts must work from an isolated skill installation, not only from the repository root.
- During validation, sync into an isolated test destination rather than modifying global skill installations.

- Behavioral runners are optional adapters; do not encode their commands, model names or tool APIs in SKILL.md.
- Windows symlinks require admin privileges or Developer Mode. Repo uses copy+sync instead.
- `quick_validate.py` lives at `~/.codex/skills/.system/skill-creator/scripts/`.
- Skills are generic (framework/language agnostic) by design.
- Host-specific installation paths are adapter configuration, not part of the skill contract.
