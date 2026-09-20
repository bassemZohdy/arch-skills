# AGENTS.md

## What This Repo Is

Portable Agent Skills for software architecture: documentation generation (`arch-doc`), diagram-first modeling (`arch-diagrams`), review/validation (`arch-review`), fitness functions (`arch-fitness`), decision analysis (`arch-decision`), orchestration of end-to-end design (`arch-orchestrator`), and specialized skills covering architecture concerns. Skills are Markdown + YAML + templates; host discovery, installation and invocation remain external to the canonical package.

## Key Commands

```powershell
# Validate skill structure (discovered checks, no LLM needed)
python tests/test_skills.py

# Run all offline release checks (Linux/macOS: bash run-tests.sh)
./run-tests.ps1

# Build portable packages into a fresh isolated destination
python scripts/build_packages.py --profile default --output .cache/packages-default
```

## Repo Structure

- `skills/<name>/SKILL.md` — Skill entry point. Must have YAML frontmatter with `name` and `description`.
- `skills/<name>/references/` — Detailed guides loaded on demand. Keep SKILL.md lean; move content here.
- `skills/<name>/assets/` — Templates/files used in output, not loaded into context.
- `tests/` — Structural validation (`test_skills.py`) and optional host-neutral scenario manifests (`.yaml`).
- `scripts/` — Deterministic framework validators and artifact helpers.
- `scripts/build_packages.py` — Default (three entry points) and expert packages; always use a fresh output directory.
- `framework/` — Canonical schemas, contribution contracts and versioned rubric, bundled into installed packages.

## Skill Authoring Conventions

- Description is the **primary trigger mechanism** — include all "when to use" info there, not in body.
- Keep SKILL.md under 500 lines. Split details into `references/`.
- Use imperative/infinitive form in instructions.
- No README.md, CHANGELOG.md, or auxiliary docs inside skill dirs.
- Diagram format priority: Mermaid > PlantUML > Draw.io.

## Validation

After editing any skill:
1. `python tests/test_skills.py` — must pass all applicable checks
2. Run `python -m unittest discover -s tests -p 'test_*.py'` for contract and isolated-package checks.
3. Build the default or selected expert profile before installation. Do not copy an unbuilt source skill: shared dependencies are added by the builder.

For optional automated response or host tests, use the repository runner:
~~~sh
python scripts/behavioral.py validate
python scripts/behavioral.py run --manifest tests/test-arch-evaluate.yaml --packages .cache/expert --output .cache/behavioral-results --limit 0 --max-calls 7
~~~
Configure the model or custom host adapter as described in `docs/test-automation.md`.
Response-only results do not prove host discovery, tool use or DAP lifecycle behavior.

## Gotchas

- Framework implementation is defined in `docs/deterministic-architecture-process.md`. Read it and `docs/framework-implementation-plan.md` before changing the DAP contracts.
- Extend `arch-orchestrator` for execution; add `arch-evaluate` only for process assessment. Keep design-quality review in `arch-review`.
- Do not describe planned framework behavior as available. Shared contracts must work from an isolated skill installation, not only from the repository root.
- During validation, sync into an isolated test destination rather than modifying global skill installations.

- Behavioral runners are optional external adapters; do not encode their commands, model names or tool APIs in SKILL.md.
- Windows symlinks require admin privileges or Developer Mode. Package generation copies files instead.
- Use the available Agent Skills specification validator when the target host provides one; the repository's structural suite must remain independently runnable.
- Skills are generic (framework/language agnostic) by design.
- Host-specific installation paths are adapter configuration, not part of the skill contract.
