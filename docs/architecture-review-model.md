# Architecture review model — proposal

**Status:** Design proposal, 2026-11-11; not an implemented evaluation service.

## Actors and boundaries

The governance administrator (an architect, committee or other authorized owner) maintains criteria, reference materials, organization defaults, review profiles, rules and gates. The submitter (any authorized role) supplies architecture documentation, diagrams and available evidence. A future web application owns RBAC, organization-specific profile instances, storage, submissions, evaluation runs and report history. Portable `arch-skills` owns reusable knowledge and skill contracts.

## Five distinct concepts

| Concept | Meaning | Example |
| --- | --- | --- |
| Reference artifact | Sourced knowledge with provenance, scope, authority and version | Security policy, architecture principle, scoped ADR |
| Criterion | Architectural dimension to assess | Security, resilience, internal consistency |
| Rule | Evidence-testable predicate with applicability and enforcement metadata | External communications are protected by approved encryption |
| Decision area / option | Expected architecture choice in a specific scope | Topology: microservices or modular monolith |
| Gate | Threshold and acceptance condition over rule outcomes | No confirmed critical policy violations |

An evaluation profile binds rule and decision-area selections, applicability, mandatory/advisory/manual handling, exceptions and gate thresholds to a version. Missing evidence does not establish compliance. The catalog is extensible, not a claim to exhaustively list all architectural options.

## Reference classifications and dimensions

Reference sources can cover external obligations and compliance controls; organization policies and architecture/technical standards; principles, guidelines, strategies and roadmaps; reference architectures, patterns and anti-patterns; organization-wide scoped decisions and waivers.

Review dimensions can cover completeness, consistency, design fitness, security/privacy, resilience, performance/scalability, data, integration/interoperability, maintainability/evolution, deployment/operability, technology suitability, trade-offs, cost and risks.

Submission context may include a proposed architecture description, drawings, relevant requirements/constraints, scoped ADRs, quality scenarios and evidence. None of these document types is universally mandatory independent of an applicable rule.

## Decision-option selection

Each configured decision area accepts **one expected option** per scoped profile, including `not_applicable` where authorized. This is a configuration UX choice, not a claim that an entire complex solution can have only one topology or deployment model: separate the area by subsystem or profile scope where needed. Different areas combine independently.

| Decision area | Illustrative mutually exclusive choices |
| --- | --- |
| Architecture topology | Monolith, modular monolith, SOA, microservices |
| Interaction model | Synchronous, asynchronous, hybrid |
| Data ownership | Shared, independently owned, hybrid |
| Deployment model | VMs, containers, serverless, hybrid |
| Availability topology | Single site, active-passive, active-active |

Do not treat event-driven communication as a competing alternative to microservices; one refers to communication and the other to structural topology. Any preference or prohibition is established by a versioned profile rule, not the neutral option definition.

## Proposed review sequence

1. Freeze the submitted architecture and the applicable profile/catalog versions, source references, baseline revision and evidence inventory.
2. Select applicable rules and decision areas. Resolve conditional applicability explicitly.
3. Evaluate each rule with `pass`, `fail`, `unknown` or authorized `not_applicable`; retain evidence, rationale and affected design identifiers.
4. Apply configured quality gates, resulting in `pass`, `fail` or `needs_review`. Required unknowns cannot silently pass. Mandatory failures cannot be masked by weighted scores.
5. Report governance findings, independent design-quality findings, accepted exceptions, risks and needed human decisions.
6. When authorized to revise, produce a new baseline, propagate impact through requirements/constraints/design/ADRs/verification, and invalidate stale dispositions.

## Integration with existing skills

- `arch-orchestrator` and specialists reuse reference and option knowledge in creation/update, retaining significant decisions and impact history.
- `arch-review` provides read-only design-quality review and proposed profile conformance findings.
- `arch-evaluate` remains the independent deterministic DAP process-readiness evaluator under its current schema and rubric, not a replacement profile gate engine.
- `arch-fitness` maps objective, automatable checks to rule IDs while separating planned checks from executed verification.

An application-neutral result contract will need a frozen input identity, versioned profile/catalog/rules, applicability, source and evidence locators, rule outcomes, gate outcomes, human dispositions, unsupported/unavailable status and reproducible report identity. This is *planned* work in [TODO.md](../TODO.md), not an existing released API.

## Invariants

- No hardcoded universal preference for microservices, cloud, or particular technologies.
- No inferred legal applicability or fabricated compliance approvals.
- No treating LLM confidence as calibrated proof or authorization.
- No silent suppression of binding organizational controls by profile overrides.
- No conflation of process readiness, design fitness and implementation verification.
- No source skill/package drift: regenerate plugin distributions using the repository build tooling and validate before release.
