# Event-Driven Design Template

## Event-Driven Architecture: [System Name]

### Events Identified
| Event | Producer | Consumers |
|-------|----------|-----------|

### Patterns Used
- Messaging: [Pub/sub, queue]
- State: [CQRS, Event Sourcing]
- Transactions: [Saga type]

### Reliability
- Idempotency: [How ensured]
- DLQ: [Configured?]
- Ordering: [Guaranteed?]

### Recommendations
1. [Improvement]

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

Record event versus command intent, schema version, producer/consumer ownership, delivery/ordering scope, replay/idempotency and compensation verification.

### Verification plans and results

| VER ID | Protected IDs | Method and environment | Acceptance threshold | Owner | Planned/executed status | Actual evidence locator |
| --- | --- | --- | --- | --- | --- | --- |

Leave execution evidence empty for planned verification. A recommendation,
checkbox or generated test is not proof of implementation or human approval.
