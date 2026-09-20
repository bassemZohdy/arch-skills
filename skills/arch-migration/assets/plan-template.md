# Migration Plan Template

## Migration Plan: [System Name]

### Current State
- System: [Description]
- Pain points: [List]
- Constraints: [List]

### Target State
- Goal: [Description]
- Benefits: [List]
- Success criteria: [List]

### Strategy
- Pattern: [Strangler fig / Branch by abstraction / Parallel run]
- Phases: [Number]

### Phase 1: [Name]
- Scope: [What's included]
- Timeline: [Duration]
- Risks: [List]
- Validation: [How to verify]

### Rollback Plan
- Triggers: [When to rollback]
- Process: [Steps]

## Scope, evidence and DAP handoff

For standalone use, omit inapplicable process fields; do not invent a DAP run.

| Field | Recorded value |
| --- | --- |
| Scope, run, stage and baseline revision/hash | |
| REQ / CON / DES / ADR IDs and source revisions | |
| Findings: ID, target, observed/proposed/unknown, evidence locator, rationale, uncertainty | |
| Alternatives and consequences | |
| Required human review, authority and disposition evidence | |
| Affected dependencies, supersessions and stale approvals | |
| Open Q / ASM / EXC IDs, owner and next action | |
| Contribution status: complete for scope / provisional / blocked | |

### Domain evidence

Record old/new baseline revisions, phase dependencies, owners, reconciliation evidence, quantitative cutover/rollback criteria and irreversible-step approval.

### Verification plans and results

| VER ID | Protected IDs | Method and environment | Acceptance threshold | Owner | Planned/executed status | Actual evidence locator |
| --- | --- | --- | --- | --- | --- | --- |

Leave execution evidence empty for planned verification. A recommendation,
checkbox or generated test is not proof of implementation or human approval.
