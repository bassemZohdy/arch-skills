# Skill and scenario coverage

Reviewed: 2026-11-11. This is an inventory of checked-in skills and validated
scenario definitions, not a model or host pass-rate report. The commands in
[project status](project-status.md) produce current execution results.

The repository has **36 canonical skills** and **339 scenario definitions in 43 YAML
manifests**. Of these, 333 explicitly target a skill and 6 test activation
across a candidate set. Every canonical skill has at least one explicit
scenario. The new counts describe checked-in definitions; execute
`python scripts/behavioral.py validate` for validation evidence.
That tool checks manifests and assertions offline; it does not execute a model, observe tool calls or prove
that a host discovers the right skill.

| Skill | Explicit scenarios | Skill | Explicit scenarios |
| --- | ---: | --- | ---: |
| arch-accessibility | 6 | arch-ai | 7 |
| arch-antipatterns | 6 | arch-api | 9 |
| arch-cloud | 9 | arch-compliance | 6 |
| arch-cost | 6 | arch-data | 9 |
| arch-ddd | 9 | arch-decision | 12 |
| arch-devops | 12 | arch-diagrams | 10 |
| arch-doc | 14 | arch-evaluate | 59 |
| arch-event | 11 | arch-features | 7 |
| arch-fitness | 11 | arch-frontend | 6 |
| arch-governance | 6 | arch-integration | 6 |
| arch-metrics | 6 | arch-microservices | 6 |
| arch-migration | 6 | arch-observability | 7 |
| arch-orchestrator | 14 | arch-patterns | 6 |
| arch-perf | 6 | arch-principles | 6 |
| arch-refactoring | 6 | arch-resilience | 6 |
| arch-review | 12 | arch-security | 11 |
| arch-test | 6 | arch-usability | 6 |
| arch-interview | 4 | arch-reverse | 4 |

The six activation scenarios are separate from the explicit counts above.
Structural, contract and isolated-package checks are Python tests rather than
per-skill scenario counts; run the full offline gate with `./run-tests.ps1` or
`bash run-tests.sh`. See [skill testing](skill-testing.md) for what each layer
establishes and [test automation](test-automation.md) for optional live runs.

Skill presence is not a percentage measure of architecture quality. A concern
such as performance can route to `arch-perf` with `arch-cloud` or
`arch-resilience` as supporting specialists; security routes to
`arch-security`, accessibility to `arch-accessibility`, and process readiness to
`arch-evaluate`. These are ownership boundaries, not claims that every project
requirement or standard clause is covered. The [skill boundaries](skill-boundaries.md)
give the full responsibility map. `arch-orchestrator` coordinates authoring;
`arch-review` assesses design fitness and `arch-evaluate` assesses process
evidence. For source-link taxonomy history, see the dated
[awesome-architecture mapping](awesome-architecture-mapping.md).
