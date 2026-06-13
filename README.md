# Architecture Skills

[![Tests](https://img.shields.io/badge/tests-210%20passing-brightgreen)]()
[![Skills](https://img.shields.io/badge/skills-30-blue)]()
[![Scenarios](https://img.shields.io/badge/scenarios-172-orange)]()

A comprehensive collection of 30 Codex skills for software architecture documentation, review, validation, and governance. Works with 12 AI agent harnesses.

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

## Skills (30)

### Core (5)
arch-doc, arch-review, arch-fitness, arch-decision, arch-governance

### Technical (4)
arch-security, arch-perf, arch-resilience, arch-test

### Architecture (10)
arch-api, arch-cloud, arch-event, arch-ddd, arch-data, arch-metrics, arch-integration, arch-microservices, arch-patterns, arch-refactoring

### Frontend (1)
arch-frontend

### Operations (5)
arch-observability, arch-migration, arch-deployment, arch-devops, arch-cost

### Features & Automation (2)
arch-features, arch-automation

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
├── skills/          # 30 skills (source of truth)
├── tests/           # 210 structural tests, 167 scenarios
├── scripts/         # Detection and sync scripts
├── docs/            # Documentation
├── README.md
└── AGENTS.md
```

## License

MIT
