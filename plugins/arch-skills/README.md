# Architecture Skills plugin

Portable software architecture skills for Claude Code and Codex. The plugin exposes three skills:

- `arch-orchestrator`: interview stakeholders, create a solution architecture, or update an existing baseline.
- `arch-evaluate`: assess process completeness, traceability and evidence freshness of an architecture baseline.
- `arch-review`: review design fitness, quality attributes, trade-offs, risks and technical debt.

Thirty-one specialist modules (APIs, data, security, resilience, diagrams, decisions, fitness
functions and more) are bundled as instructions that the three skills load on demand. They are not
separate skills.

## What the plugin runs

The plugin is Markdown instructions, templates and small deterministic Python helpers in
`scripts/` inside each skill. The helpers need Python 3.10+ and PyYAML, run locally only when a
skill invokes them, and make no network calls. The plugin has no hooks, MCP servers or background processes.

## Install

```
/plugin marketplace add bassemZohdy/arch-skills
/plugin install arch-skills --marketplace bassemZohdy/arch-skills
```

## Source and license

This folder is generated from https://github.com/bassemZohdy/arch-skills with
`python scripts/build_plugin.py`. Do not edit it by hand. Licensed under MIT, see `LICENSE`.
