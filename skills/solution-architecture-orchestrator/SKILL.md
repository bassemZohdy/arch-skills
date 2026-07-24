---
name: solution-architecture-orchestrator
description: Orchestrate specialist architecture skills to deliver one coherent solution architecture. Use for end-to-end architecture design requests - greenfield systems, modernization, migration, integration programs, or any request spanning multiple architecture domains that requires skill selection, coordinated execution, conflict resolution, validation, and a single consolidated deliverable.
---

# Solution Architecture Orchestrator

Coordination and quality-control layer for solution architecture work. Analyze an
architecture request, select the minimum sufficient set of specialist skills
(`arch-*`), coordinate their execution over a shared context, resolve conflicts,
and synthesize one coherent architecture.

Do NOT duplicate specialist knowledge. Own only: orchestration, context management,
decision sequencing, validation, and final synthesis.

## Workflow

```
1. Understand   → Problem, requirements, quality attributes, constraints, deliverables
2. Classify     → Request type along 6 dimensions
3. Discover     → Read lightweight skill metadata only (Stage 1)
4. Select       → Minimum sufficient skill set (Stage 2) + selection table
5. Context      → Create the shared architecture context
6. Plan         → Dependency-aware execution order
7. Execute      → Invoke skills per the invocation contract; update context after each
8. Reconcile    → Normalize outputs; detect and resolve conflicts explicitly
9. Validate     → Run the validation gates; loop back on failure
10. Synthesize  → One unified architecture document + decision record
```

## Step 1: Understand the Request

Extract into the shared context: business problem, stakeholders, functional
requirements, quality attributes, constraints, assumptions, existing systems,
expected scale, availability/recovery needs, budget, and expected deliverables.

- Do not invent requirements. Mark unknowns as explicit assumptions or open questions.
- Do not select technology before requirements are understood.
- Treat user technology preferences as inputs, not constraints, unless stated as constraints.

## Step 2: Classify the Request

Classify along all applicable dimensions; use the result to drive skill selection.

| Dimension | Values |
|-----------|--------|
| Initiative | Greenfield, modernization, migration, integration, review |
| Style tendency | Monolith, modular monolith, microservices, event-driven, serverless, workflow-based, agentic, hybrid |
| System type | Internal platform, customer-facing app, shared service, data platform, AI platform, infrastructure platform |
| Environment | Cloud, on-premises, hybrid, edge, Kubernetes, OpenShift |
| Criticality | Prototype, PoC, production, regulated, mission-critical |
| Processing | Synchronous, asynchronous, batch, streaming, long-running, human-in-the-loop |

## Step 3-4: Discover and Select Skills (Two Stages)

**Stage 1 — Discovery.** Read only lightweight metadata per skill: name, purpose,
applicable scenarios, triggers, required inputs, produced outputs, dependencies,
exclusions, estimated cost. Use `references/skill-catalog.md` for the specialist
catalog mapping to the `arch-*` skills in this repo.

**Stage 2 — Selection.** Select the minimum sufficient set. Select a skill ONLY when
at least one is true:

- The user explicitly requests its architectural area.
- A requirement or constraint directly maps to it.
- Another selected skill declares it as a dependency.
- Omitting it leaves an important quality attribute or risk unaddressed.
- An applicable quality gate requires it.

Never select a skill merely because it is available. Build the selection table
(skill, selected/skipped, reason, dependencies, order, expected contribution) from
`assets/selection-table-template.md` and include a concise version in the final result.

## Step 5: Shared Architecture Context

Create the context object from `assets/shared-context-template.md`: problem, goals,
requirements, quality attributes, constraints, assumptions, systems, tech
preferences/prohibitions, environment, security/compliance/residency, integrations,
scale, availability/recovery, budget, style, decisions made, open questions, risks,
selected skills, execution status.

- Give every skill the relevant parts of this context — never a blank slate.
- After each skill completes, merge its confirmed findings and decisions back.
- No skill may silently replace a decision the orchestrator already approved.

## Step 6: Plan Execution

Dependency-aware order. Typical sequence (skip phases with no selected skill):

```
Requirements → QA priorities → Domain/context → Style selection →
App/service/integration/data design → Security/compliance →
Deployment/platform → Reliability/scale/observability →
Delivery/CI-CD/ops → Cost & complexity review → Validation → ADRs & docs
```

Parallelize only skills with no dependency between them. Never parallelize a skill
with another whose decisions it consumes.

## Step 7: Execute per the Invocation Contract

Give each skill: problem summary, relevant requirements/constraints, existing
decisions, the specific questions it must answer, expected output structure,
decisions it MAY make, decisions it must NOT override, its dependencies, and
required evidence/rationale.

Require each skill to return: findings, recommendations, alternatives considered,
trade-offs, assumptions, risks, dependencies, proposed decisions, conflicts with
existing decisions, open questions, confidence level.

Reject and re-request outputs that are generic, contradictory, unsupported, or
unrelated to the shared context. Full contract: `references/orchestration-playbook.md`.

## Step 8: Reconcile Outputs

- Normalize terminology; remove duplicated recommendations; merge into one model.
- Detect contradictions, gaps, unsupported assumptions, unnecessary complexity.
- Resolve conflicts by the priority order in `references/orchestration-playbook.md`
  (user requirements > legal/regulatory/security > business-critical quality attributes
  > enterprise standards > operational feasibility > simplicity > cost > technology
  preference).
- Never hide conflicts. Document conflicting recommendations, cause, chosen decision,
  rejected alternative, consequences. Create an ADR (via arch-decision) for
  significant choices.
- Apply overengineering controls: before any component/broker/gateway/layer is added,
  verify which requirement needs it, which risk it mitigates, why nothing existing
  suffices, its operational cost, failure modes, and migration implications.

## Step 9: Validate

Run the full validation gate checklist in `references/orchestration-playbook.md`:
every requirement and critical quality attribute addressed, boundaries justified,
data ownership explicit, trust boundaries secured, failure/recovery defined,
complexity proportional, incrementally deliverable, no implicit major decisions.

On failure, re-invoke the relevant specialist with a targeted correction request.

## Step 10: Synthesize the Final Architecture

Produce ONE unified document using `assets/solution-architecture-template.md`
(executive summary through validation checklist, 22 sections). It must read as a
single coherent architecture — not pasted-together specialist reports. Record
decisions, rejected alternatives, risks, follow-ups. Verify the result addresses
every original requirement.

## Failure and Fallback

- Required skill unavailable: state the missing capability; use an overlapping skill
  only with documented limitations; otherwise do basic orchestrator-level analysis
  and mark the area as requiring specialist review.
- Runtime cannot invoke skills dynamically: produce the recommended execution plan,
  name the skills to apply with their required inputs, do not pretend they ran, and
  continue with the best analysis possible from available context.

## Behavioral Rules

- Do not invoke every skill; do not duplicate specialist content.
- Do not leave specialist outputs isolated — synthesis is the deliverable.
- Do not hide uncertainty; use explicit assumptions.
- Preserve traceability from requirements to decisions.
- Stay technology-neutral until technology selection is justified.
- Guide implementation without collapsing into low-level coding detail.

## Examples

- "Design a greenfield order management platform for a retailer; cloud, ~50k orders/day, PCI scope."
  → Classify (greenfield, customer-facing, cloud, production+regulated); select arch-patterns,
  arch-ddd, arch-api, arch-data, arch-security, arch-compliance, arch-cloud, arch-observability,
  arch-decision, arch-doc; skip arch-ai, arch-frontend, arch-migration.
- "Modernize our on-prem monolith toward microservices." → Add arch-migration, arch-microservices,
  arch-resilience, arch-devops; keep modular-monolith as an explicit considered alternative.
- "We need Kafka, Kubernetes, and a service mesh." → Treat as preferences, not constraints;
  verify each against requirements via overengineering controls before accepting.

## Common Gotchas

- Selecting every skill "for completeness" — the deliverable is judgment, not coverage.
- Letting a specialist quietly overturn an approved decision — all overrides are explicit and recorded.
- Pasting specialist sections together — normalize and deduplicate before synthesis.
- Technology-first answers — classification and requirements come before any tech choice.

## Further Reading

- `references/awesome-architecture.md` — Curated external articles, videos, libraries, and samples per topic (awesome-architecture.com)

## Related Skills

- **arch-review** - Independent review of the synthesized architecture
- **arch-decision** - ADRs for significant choices and resolved conflicts
- **arch-doc** - Final documentation formats (C4, arc42, ADRs)
- **arch-patterns** - Style selection specialist
- **arch-fitness** - Encoding the validated architecture as enforceable rules
