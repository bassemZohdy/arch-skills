# Solution Architecture Skills plugin

Portable software architecture skills for Claude Code and Codex. The plugin exposes two skills:

- `arch-orchestrator`: interview stakeholders, create a solution architecture, or update an existing baseline.
- `arch-review`: review design fitness, quality attributes, trade-offs, risks and technical debt.

Thirty-one specialist modules (APIs, data, security, resilience, diagrams, decisions, fitness
functions and more) are bundled as instructions that the two skills load on demand. They are not
separate skills.

## What the plugin runs

Nothing. The plugin is Markdown instructions, templates, JSON schemas and one icon. It has no
scripts, hooks, MCP servers, network access or background processes. Deterministic checks are not
available in this edition, so results are provisional analysis. The full edition, `arch-skills`,
adds the Python helpers and the `arch-evaluate` skill for process evaluation.

## Install

```
/plugin marketplace add bassemZohdy/arch-skills
/plugin install solution-architecture-skills --marketplace bassemZohdy/arch-skills
```

## Source and license

This folder is generated from https://github.com/bassemZohdy/arch-skills with
`python scripts/build_plugin.py`. Do not edit it by hand. Licensed under MIT, see `LICENSE`.
