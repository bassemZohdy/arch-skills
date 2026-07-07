# Architecture Skills

[![Tests](https://img.shields.io/badge/tests-203%20passing-brightgreen)]()
[![Skills](https://img.shields.io/badge/skills-29-blue)]()
[![Scenarios](https://img.shields.io/badge/scenarios-170-orange)]()

A comprehensive collection of 29 Codex skills for software architecture documentation, review, validation, and governance. Works with 12 AI agent harnesses.

## Quick Start

```bash
# Set up unified skills (single source of truth)
python scripts/setup_unified.py

# Run validation tests
python tests/test_skills.py
```

## Supported Harnesses

| Harness | Path |
|---------|------|
| Claude Code | `~/.claude/skills/` |
| OpenAI Codex | `~/.codex/skills/` |
| Cursor | `.cursor/rules/` |
| GitHub Copilot | `.github/copilot-instructions.md` |
| Gemini CLI | `.gemini/skills/` |
| Junie | `.agents/skills/` |
| OpenHands | `.agents/skills/` |
| OpenCode | `.config/opencode/skills/` |
| Pi | `.pi/skills/` |
| Cline | `.cline/skills/` |
| Kilo Code | `.kilo/skills/` |
| MiMoCode | `.mimocode/skills/` |

## Skills (29)

### Core (5)
arch-doc, arch-review, arch-fitness, arch-decision, arch-governance

### Technical (4)
arch-security, arch-perf, arch-resilience, arch-test

### Architecture (10)
arch-api, arch-cloud, arch-event, arch-ddd, arch-data, arch-metrics, arch-integration, arch-microservices, arch-patterns, arch-refactoring

### Frontend (1)
arch-frontend

### Operations (4)
arch-observability, arch-migration, arch-devops, arch-cost

### Features (1)
arch-features

### AI (1)
arch-ai

### NFR (3)
arch-usability, arch-accessibility, arch-compliance

## Usage

```
Use arch-doc to create C4 diagrams
Use arch-review to evaluate architecture
Use arch-decision to choose between technologies
Use arch-security for threat modeling
Use arch-perf for performance analysis
```

## Project Structure

```
arch-skills/
├── skills/          # 29 skills (source of truth)
├── tests/           # 373 total checks (203 structural, 170 scenarios)
├── scripts/         # Detection and sync scripts
├── docs/            # Documentation
├── README.md
└── AGENTS.md
```

## License

MIT
