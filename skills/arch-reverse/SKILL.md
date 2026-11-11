---
name: arch-reverse
description: "Reverse engineer the as-built software architecture from existing code, repositories, build/dependency manifests, deployment artifacts and available runtime evidence. Use for code-to-architecture discovery, recovering undocumented systems, and reconstructing structure and interactions. Use arch-doc to publish and arch-review to assess quality."
---

# Architecture Reverse Engineering

Recover an **evidence-backed as-built architecture**. Discovery is read-only and
does not authorize redesign, code execution, deployment or approval.

## Workflow

1. **Establish scope.** Record repository/version, project boundaries, desired
   viewpoints, available runtime/deployment evidence and analysis permissions.
2. **Inventory technical sources.** Find modules, build manifests, dependencies,
   entry points, API contracts, database schemas, messages, configuration,
   infrastructure-as-code, tests and existing documentation.
3. **Trace structures and interactions.** Recover components and ownership,
   imports, calls, APIs, asynchronous edges, data movement and trust boundaries.
   Identify significant cycles, shared-state coupling and external dependencies.
4. **Reconstruct architectural views.** Build supported context, container,
   component, sequence, data-flow and deployment diagrams with stable IDs and
   meaningful edges. Do not infer production behavior from YAML alone.
5. **Infer design choices carefully.** Identify candidate styles, patterns,
   technology selections and trade-offs, not undocumented historical rationale
   or accepted ADRs. Compare contradictory sources.
6. **Report coverage and gaps.** Return evidence-linked facts, inferences,
   unknowns, scope exclusions and recommended verification by an owner.

## Required evidence model

For every significant component, relationship or claim: stable identifier,
source path/line or artifact locator, source revision, viewpoint, evidence
classification (`observed`, `inferred`, `unknown`), rationale, and unresolved
questions. Confidence labels require evidence-based rationale, not invented
probabilities. Distinguish code, deployed configuration, live observations and
interview claims. Never expose secrets, credentials or personal data.

Static inspection is preferred. Do not execute untrusted project code, install
dependencies or query production environments without explicit authorization.
If source access or parsing is unavailable, label limitations instead of
fabricating components, APIs, infrastructure or citations.

## Routing boundaries

- `arch-diagrams`: produce editable, validated views from the recovered model.
- `arch-doc`: assemble the verified and inferred facts into architecture docs.
- `arch-review`: independently evaluate fitness and governance conformance.
- `arch-migration`: plan modernization from the discovered current state.
- `arch-interview`: ask stakeholders about evidence gaps; preserve testimony
  separately from observations.
- `arch-orchestrator`: coordinate any separately authorized redesign/update.

## Examples

- Reconstruct boundaries and data ownership from a Spring/TypeScript monorepo.
- Recover an undocumented legacy integration architecture before migration.
- Compare source code to deployment manifests and flag runtime unknowns.
