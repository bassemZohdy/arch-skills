# ADR-0001: Share architecture knowledge across design and evaluation

- **Status:** Proposed (not approved)
- **Date:** 2026-11-11
- **Scope:** Portable `arch-skills` lifecycle capabilities and a future architecture review web platform

## Context

The repository already supports interview/create/update with `arch-orchestrator`,
design-quality review with `arch-review`, DAP process-readiness assessment with
`arch-evaluate`, and objective checks with `arch-fitness`. The existing DAP
rubric is a versioned process-completeness contract, not an organization-specific
review-policy catalog. The future application is a SonarQube-like architecture
review platform with governance administrators and submitters.

The same reusable architecture knowledge should inform creation, change, review,
validation and automated checks. Conflating reference artifacts, criteria, rules,
decision records and gates would create inconsistent semantics and poor reuse.

## Proposed decision

- Retain **host-neutral** canonical skills and a versioned reusable architecture
  knowledge catalog in `arch-skills`; put web UI, identity, tenancy, runtime
  organization policies/profile instances, submissions and report persistence in
  the consuming application.
- Separate **reference artifacts** (sources of architectural knowledge),
  **criteria** (what to assess), **rules** (specific applicable evidence checks),
  **decision options** (configuration choices) and **quality gates** (acceptance
  thresholds). One source can justify many rules and vice versa.
- Use organization defaults and versioned evaluation profiles. Profile settings
  include applicability, mandatory/advisory/manual enforcement and one expected
  option per decision area where the area is exclusive. Distinct architecture
  facets should be separate areas rather than forced into false alternatives.
- Preserve the boundary: `arch-review` assesses candidate design quality and
  profile conformance; `arch-evaluate` independently assesses DAP evidence and
  readiness with its unchanged deterministic rubric; `arch-fitness` implements
  automatable objective checks when evidence exists. Neither a high score nor
  machine confidence grants a required human approval.
- `arch-orchestrator` and specialists consult the same catalog during creation
  and updates. Changes retain history, propagate dependency impacts, invalidate
  stale evidence and require a new review where applicable.
- Record catalog, profile, rule, source and baseline IDs/versions with every
  finding. Explicitly distinguish `pass`, `fail`, `unknown` and authorized
  `not_applicable`; quality gates may return `needs_review`. Do not infer
  deployed behavior from submitted diagrams.
- Introduce new review contracts compatibly rather than changing DAP schema
  2.0.0 and rubric 1.0.0 in place. Do not treat this ADR as implementation
  authorization or as an approved organization standard.

## Alternatives considered

1. **Implement all review logic only in the web application:** simpler initially
   but duplicates skills and makes host-based creation/review inconsistent.
2. **Merge all evaluation into the DAP rubric:** reuses code but confuses process
   completeness with architecture design fitness and breaks scoring contracts.
3. **Keep fourteen independent mandatory governance object types:** over-models
   source documents, confuses provenance with enforcement and hinders extensibility.

## Consequences and follow-up

Positive: reuse across hosts and application, clearer responsibility boundaries,
reproducible profile-specific findings and independently testable governance gates.

Costs: catalog curation and version management; profile resolver and contracts;
human-review handling; plugin rebuild/tests after canonical skill changes.

Implementation and verification are tracked in [TODO.md](../../TODO.md).
The platform review design is elaborated in
[architecture-review-model.md](../architecture-review-model.md). This proposed
ADR does not certify the skills or approve any organization's governance rules.
