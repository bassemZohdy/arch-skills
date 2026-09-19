# Framework implementation reference

Status: implemented reference baseline. Framework target: 1.0.0. The repository now contains executable contracts, persistence, scoring, evaluation, reporting and fixtures; future work is limited to deeper host-specific integration and live-model scenario coverage.

Use the [corrected framework](deterministic-architecture-process.md) as the normative reference and [the review](framework-review.md) for the rationale. Current delivery and verification are recorded in [DAP implementation status](dap-implementation-status.md); keep [TODO.md](../TODO.md) for open follow-up work.

## Integration boundaries

Extend `arch-orchestrator` as the execution entry point and add `arch-evaluate` for process assessment. Do not add another general-purpose orchestrator, a hosted agent runtime, a database or a scheduler. Python validators fit the repository's existing script-based tooling. Keep the process generic across languages, frameworks, deployment environments and AI hosts.

| Component | Responsibility | Boundary |
| --- | --- | --- |
| `arch-orchestrator` | Preparation, interview, checkpoints, specialist selection, stage transitions | Does not invent stakeholder approval or replace specialist reasoning |
| `arch-evaluate` | Frozen-baseline process assessment, evidence-linked findings and scores | Does not repair assessed artifacts or certify design fitness |
| `arch-decision` | Alternatives, decision-specific DAR and ADR lifecycle | DAR option scores are not process completeness scores |
| `arch-doc` | arc42 views, diagrams and generated evaluation appendix | Does not convert planned verification into execution evidence |
| `arch-governance` | Review rules, owners, exceptions and configured authority | Does not treat silence or a confidence score as approval |
| `arch-review` | Design-quality and trade-off review | Remains distinct from process completeness evaluation |
| Shared contracts and scripts | Schemas, ID/link validation, state transitions, hashing and arithmetic | Works without an LLM for structural checks and score calculation |

Store source skills in `skills/`. Shared process assets must remain accessible when an individual skill is installed outside the repository: define one canonical source and package versioned copies or an explicit dependency through existing sync tooling. Do not assume a `../../docs` link will exist inside every user's installed skill directory. Update the checked-in Copilot mirrors through a deliberate sync step; do not hand-maintain competing definitions.

## Proposed target-project artifacts

These paths belong to a project being designed, not to the skill repository's own implementation documentation. A configured alternative root is allowed; the manifest records it.

| Path | Content |
| --- | --- |
| `architecture/architecture.md` | Twelve arc42 sections and a generated evaluation summary |
| `architecture/requirements.json` | Requirement and constraint records with provenance, scenarios and verification plans |
| `architecture/decisions/` | ADR files and a stable index |
| `architecture/traceability.json` | Typed relationships between source, requirement, design, ADR and verification IDs |
| `architecture/traceability.md` | Generated readable RTM from the same graph |
| `architecture/process/config.json` | Framework, schema, rubric and organisational policy versions and values |
| `architecture/process/state.json` | Atomic checkpoint, active stage, baseline, counters and next action |
| `architecture/process/history.jsonl` | Minimal answer/change/gate history without unnecessary sensitive data |
| `architecture/process/reviews.json` | Human dispositions and delegation evidence |
| `architecture/process/exceptions.json` | Explicit exceptions, authority, residual risk and expiry/review triggers |
| `architecture/evaluations/` | Versioned input manifests, criterion assessments and generated reports |

JSON is the proposed machine-readable baseline format to minimise parser dependencies; Markdown remains the human-facing format. DAP-001 freezes exact schemas and paths. RTM and appendix generation must be repeatable and must preserve content outside their generated regions.

## State and concurrency

Separate a mutable draft checkpoint from an immutable candidate baseline. Freeze the candidate's input manifest for review and evaluation. Store acceptance/publication receipts outside that manifest so publishing a report cannot change the input it describes. Later semantic changes create a new candidate and invalidate only affected evidence, with the evaluator checking the complete new baseline before readiness.

Use atomic replacement for individual records plus a manifest/revision check for a multi-file baseline. Reject or reconcile conflicting revisions rather than overwriting another contributor. Record an interrupted operation and recover from the last valid manifest. Do not use conversation memory as the sole source of answers, approval or convergence state.

## Mapping the current template into arc42

Preserve the useful content of the existing 22-section template while making arc42 the default for framework runs. Standalone `arch-doc` requests retain their requested format.

| Current template sections | Default arc42 destination |
| --- | --- |
| 1 Executive summary; 2 Business context; 3 Requirements; 5 Drivers | 1 Introduction and goals; detailed quality scenarios in 10 |
| 3 Constraints | 2 Constraints |
| 6 System context | 3 Context and scope |
| 7 Proposed architecture; 18 Alternatives | 4 Solution strategy with ADR links in 9 |
| 8 Component responsibilities; 9 Data architecture | 5 Building block view; crosscutting data rules in 8 |
| 10 Integration and communication | 6 Runtime view and 8 Crosscutting concepts |
| 12 Deployment | 7 Deployment view |
| 11 Security; 13 Reliability; 14 Performance; 15 Operations; 16 Delivery | 8 Crosscutting concepts, with scenarios in 6, deployment details in 7 and targets in 10 |
| 17 Technology decisions; 20 ADRs | 9 Architectural decisions |
| 4 Assumptions and questions; 19 Risks | 11 Risks and technical debt, with linked durable records |
| Terminology across all sections | 12 Glossary |
| 21 Roadmap; 22 Validation; skill-selection appendix | Focused appendices with links to evidence and evaluation |

## Delivered implementation map

1. **Contracts and records — DAP-001 to DAP-003.** Freeze the record, configuration and criterion definitions; provide templates; make interruption recovery reliable.
2. **Execution — DAP-004 to DAP-008.** Integrate preparation, interviews, design, review and change routing into existing skills.
3. **Assessment — DAP-009 to DAP-011.** Implement deterministic checks and arithmetic, the evaluator skill, and freshness-safe report publishing.
4. **Adoption — DAP-012 to DAP-014.** Exercise brownfield migration, package shared assets for supported hosts, and validate representative scenarios.

Task-level completion and verification are recorded in [DAP implementation status](dap-implementation-status.md). This reference describes the stable boundaries and artifact contracts; it does not preserve an obsolete implementation backlog.

## Verification reference

Use deterministic fixtures for malformed records, broken links, circular trace chains, empty populations, unknown evidence, invalid weights, stale approvals, expiry, concurrency and score arithmetic. Check the documented example: Q=80, D=75, F=90, B=60, A=100 and explicitly adopted weights 0.25/0.20/0.35/0.20 yield 76.0%.

Use behavioural tests for asking meaningful questions, preserving authority, selecting relevant specialists, recognising unavailable tools and keeping draft versus accepted status honest. Record actual harness/model versions and results; YAML scenario files alone do not prove the scenarios ran successfully. Keep live-model tests opt-in and structural checks inexpensive.

Completion requires a greenfield example, a brownfield change example and an interrupted-session example whose resulting artifacts pass the deterministic checks. Include one failing example with a high score and a blocking review so the score cannot be mistaken for approval. Re-run existing skill validation when skills change and verify packaging from an isolated installation, not just from the repository root.

Do not install skills globally as a side effect of tests. Use an isolated sync destination. The reference baseline is available; host-specific adapters and additional live-model coverage remain optional follow-up work.
