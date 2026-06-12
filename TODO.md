# Architecture Skills - Task List

## Completed

### Phase 1: Workspace Setup
- [x] Create `skills/` directory structure
- [x] Scaffold `arch-doc` skill
- [x] Scaffold `arch-review` skill

### Phase 2: arch-doc — Architecture Documentation Skill
- [x] Write framework references (C4, arc42, TOGAF, ISO 42010)
- [x] Create diagram templates (Mermaid, PlantUML, Draw.io)
- [x] Write SKILL.md with workflow
- [x] Create ADR reference with MADR templates

### Phase 3: arch-review — Architecture Review Skill
- [x] Write review references (patterns, quality attributes, best practices, tech-debt)
- [x] Create review template
- [x] Write SKILL.md with workflow

### Phase 4: Research & Updates
- [x] Research C4 Model best practices (c4model.com)
- [x] Research arc42 template best practices (arc42.org)
- [x] Research ADR best practices (MADR, Thoughtworks Radar)
- [x] Research quality attributes (ISO 25010)
- [x] Research architecture fitness functions (ArchUnit)
- [x] Update C4 reference with official review checklist
- [x] Update arc42 reference with 12 sections and canvas
- [x] Create ADR reference with MADR templates
- [x] Create arch-fitness skill for automated validation
- [x] Update quality attributes with ISO 25010 model
- [x] Research skill testing tools (skillprobe, skill-eval-runner, skill-test-skill)

### Phase 5: Validation & Installation
- [x] Run `quick_validate.py` on all skills
- [x] Generate `agents/openai.yaml` for all skills
- [x] Create skill testing reference (`references/skill-testing.md`)
- [x] Install skillprobe for testing
- [x] Write test scenarios for all skills (39 total)
- [x] Run tests and validate (28/28 structural + 39 scenarios)
- [x] Install skills to `~/.codex/skills/`

### Phase 6: DAR Integration
- [x] Create arch-decision skill with DAR methodology
- [x] Copy criteria library from DAR_Skill
- [x] Copy validate_math.py script
- [x] Create DAR document template
- [x] Add test scenarios for arch-decision (9 scenarios)
- [x] Validate DAR math script works

### Phase 7: Cross-Platform Scripts
- [x] Create sync-skills.sh for Linux/Mac
- [x] Create run-tests.sh for Linux/Mac
- [x] Create validate-dar.sh for Linux/Mac
- [x] Update README.md with cross-platform instructions
- [x] Update AGENTS.md with arch-decision
- [x] Clean up unused files (dry-run test files)

## Project Status

| Metric | Value |
|--------|-------|
| Skills | 4 (arch-doc, arch-review, arch-fitness, arch-decision) |
| Structural Tests | 28 (all passing) |
| Skill Test Scenarios | 39 (30% documented, 100% coverage) |
| References | 13 files |
| Assets | 14 files |
| Scripts | 4 (validate_math.py, sync-skills.ps1/sh, run-tests.sh) |

## Files

```
arch-skills/
├── README.md
├── AGENTS.md
├── TODO.md
├── sync-skills.ps1
├── sync-skills.sh
├── run-tests.sh
├── validate-dar.sh
├── skills/
│   ├── arch-doc/
│   ├── arch-review/
│   ├── arch-fitness/
│   └── arch-decision/
└── tests/
    ├── test_skills.py
    ├── test-arch-doc.yaml
    ├── test-arch-review.yaml
    ├── test-arch-fitness.yaml
    ├── test-arch-decision.yaml
    ├── test-dar.md
    └── coverage-analysis.md
```
