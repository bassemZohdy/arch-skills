# Architecture Skills

A collection of 33 portable Agent Skills for software architecture design, documentation, review and governance. Skills are Markdown instructions, references and reusable templates; host adapters and installation mappings are kept outside the skill content.

## Deterministic architecture framework

The [framework specification](docs/deterministic-architecture-process.md) defines the implemented reference process: a repeatable path from incomplete requirements to a reviewed, traceable architecture baseline. Determinism applies to recorded gates and score calculation; LLM reasoning does not imply a unique design.

**Current status:** the reference implementation is available. It includes versioned contracts, durable checkpoint helpers, deterministic score calculation, the `arch-evaluate` skill, report/RTM tooling and lifecycle fixtures. Host integrations remain constrained by each host's persistence and skill-loading capabilities.

| Read | Purpose |
| --- | --- |
| [Framework](docs/deterministic-architecture-process.md) | Stages, gates, records, review policy and scoring |
| [Review](docs/framework-review.md) | Corrections and repository gaps |
| [Implementation reference](docs/framework-implementation-plan.md) | Delivered integration boundaries, artifact layout and arc42 mapping |
| [DAP implementation status](docs/dap-implementation-status.md) | Completed tasks, DAP explanation and verification evidence |
| [DAP adapter contract](docs/dap-adapter-contract.md) | Optional host-neutral behavioral scenarios and versioned evidence results |
| [Skill boundaries](docs/skill-boundaries.md) | Redundancy review and responsibility boundaries |
| [TODO.md](TODO.md) | Open follow-up work only |

The execution entry point is the existing `arch-orchestrator`. `arch-evaluate` assesses process evidence; `arch-review` remains responsible for design-quality review. The framework reuses `arch-doc`, `arch-decision` and `arch-governance` without a separate agent platform.

## Quick start

Run structural validation from the repository root:

```bash
python tests/test_skills.py
```

The existing setup script creates links to `skills/` at its configured harness locations:

```bash
python scripts/setup_unified.py
```

Review those destinations before setup; `--force` can replace existing destinations. Host mappings are configuration targets, not proof that every host has been tested with every skill. See [compatibility](docs/harness-compatibility.md) and [testing guidance](docs/skill-testing.md).

## Existing skills

| Area | Skills |
| --- | --- |
| Orchestration | `arch-orchestrator` |
| Core | `arch-doc`, `arch-review`, `arch-fitness`, `arch-decision`, `arch-governance` |
| Design fundamentals | `arch-principles`, `arch-antipatterns` |
| Technical quality | `arch-security`, `arch-perf`, `arch-resilience`, `arch-test` |
| Architecture | `arch-api`, `arch-cloud`, `arch-event`, `arch-ddd`, `arch-data`, `arch-metrics`, `arch-integration`, `arch-microservices`, `arch-patterns`, `arch-refactoring` |
| Frontend | `arch-frontend` |
| Operations | `arch-observability`, `arch-migration`, `arch-devops`, `arch-cost` |
| Features and AI | `arch-features`, `arch-ai` |
| Additional quality concerns | `arch-usability`, `arch-accessibility`, `arch-compliance` |

Example requests:

```text
Use arch-doc to create C4 diagrams.
Use arch-review to review architecture trade-offs.
Use arch-decision to compare technologies against explicit requirements.
Use arch-orchestrator to coordinate a solution architecture design.
```

`arch-evaluate` is available for frozen-baseline assessment. Run `python scripts/dap_validate.py examples/greenfield/architecture` for the deterministic example.

## Repository structure

| Path | Purpose |
| --- | --- |
| `skills/` | Canonical skill definitions, references, templates and UI metadata |
| `tests/` | Structural and optional adapter-driven scenarios |
| `scripts/` | Harness detection and setup helpers |
| `docs/` | Framework specification, planning and project guides |
| `TODO.md` | Open follow-up work |
| `AGENTS.md` | Contribution instructions |

Defined scenarios and historical counts are not a current passing test result. [Skill boundaries](docs/skill-boundaries.md) records the responsibility review; [DAP implementation status](docs/dap-implementation-status.md) records the current implementation and verification evidence.

## License

MIT, as declared by the existing project documentation. The reviewed repository snapshot does not contain a root `LICENSE` file.
