# Principles Checklist

Contextual prompts for design reviews. Record applicability, evidence and trade-offs;
an unchecked item is not automatically a defect or a DAP gate failure.

## Simplicity

- [ ] Each abstraction has a present boundary/testability/change rationale; a single implementation can be justified
- [ ] No business rule encoded in two places (DRY)
- [ ] A new team member can explain each module in one sentence (KISS)
- [ ] Dead configuration and unused extension points deleted

## SOLID

- [ ] Every class states its single responsibility without "and" (SRP)
- [ ] Expected changes have appropriate extension boundaries without speculative complexity (OCP)
- [ ] No subtype weakens a base-type guarantee (LSP)
- [ ] No client forced to implement methods it does not use (ISP)
- [ ] Business logic imports no framework, DB, HTTP, or UI packages (DIP)

## Coupling & Cohesion

- [ ] No module reaches inside another's internals (content coupling)
- [ ] No shared mutable global state (common coupling)
- [ ] Interfaces carry only the data needed (data coupling)
- [ ] Each unit's members serve one purpose (functional cohesion)
- [ ] High-afferent modules are the most stable ones

## Boundaries & Failure

- [ ] Validation happens at trust boundaries; invariants fail fast inside
- [ ] Commands do not return data; queries do not mutate (CQS)
- [ ] Consistency/availability stance documented per data flow (CAP/PACELC)
- [ ] Domain types carry no persistence annotations or SQL-shaped design
- [ ] Composition used instead of inheritance hierarchies deeper than two levels

## Disposition

Do not sum checkmarks into an architecture-health or readiness score. Rank confirmed
findings by business impact, evidence, uncertainty and remediation cost. Record
justified exceptions, owner and revisit trigger.

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

Record applicability, evidence, justified seams and exceptions, cost-of-change reasoning and protected boundary verification.

### Verification plans and results

| VER ID | Protected IDs | Method and environment | Acceptance threshold | Owner | Planned/executed status | Actual evidence locator |
| --- | --- | --- | --- | --- | --- | --- |

Leave execution evidence empty for planned verification. A recommendation,
checkbox or generated test is not proof of implementation or human approval.
