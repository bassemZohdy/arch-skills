# Orchestration Playbook

Detailed contracts and policies for the orchestration workflow. Load when executing
Steps 7-10 of the skill.

## Skill Invocation Contract

### Inputs the orchestrator MUST provide to every selected skill

| Input | Description |
|-------|-------------|
| Problem summary | 2-4 sentence architecture problem statement |
| Relevant requirements | Only the requirements in this skill's scope |
| Relevant constraints | Technical, organizational, regulatory constraints that bind it |
| Existing decisions | Approved decisions it must respect |
| Specific questions | The exact questions this invocation must answer |
| Expected output | The return structure below |
| Allowed decisions | Decisions this skill may make |
| Protected decisions | Decisions it must NOT override |
| Dependencies | Which prior skill outputs it consumes |
| Evidence required | Rationale or sources expected for its recommendations |

### Required return structure from every skill

| Field | Description |
|-------|-------------|
| Findings | What it discovered about the problem |
| Recommendations | Proposed design, tied to requirements |
| Alternatives considered | At least one where the choice is non-obvious |
| Trade-offs | Cost/benefit of the recommendation |
| Assumptions | Everything it assumed beyond the shared context |
| Risks | What could make the recommendation fail |
| Dependencies | What it needs from other skills |
| Proposed decisions | ADR proposals for the configured human authority; not agent approvals |
| Baseline and trace | Run/revision/hash, relevant REQ/CON/DES/ADR IDs and impacted dependencies |
| Verification | VER plans with method, acceptance threshold, owner and planned/executed evidence |
| Evidence | Source locators, revisions, uncertainty and Q/ASM gaps |
| Review needs | Required human dispositions, authority, exceptions and next action |
| Conflicts | Where it disagrees with existing decisions |
| Open questions | What remains unresolved |
| Confidence | High / Medium / Low, with reason |

Reject and re-request outputs that are generic (not tied to the shared context),
contradictory, unsupported, or off-scope. A re-request must name the specific defect.

## Conflict-Resolution Policy

Priority order (highest first):

1. Binding legal, regulatory, security, and safety constraints (eligibility gates)
2. Confirmed user requirements; resolve conflicts through authorized clarification
3. Business-critical quality attributes
4. Existing enterprise standards
5. Operational feasibility
6. Simplicity and maintainability
7. Cost
8. Technology preference

For every conflict, record:

```
### Conflict: [short title]
- Position A: [skill] recommends [X] because [rationale]
- Position B: [skill] recommends [Y] because [rationale]
- Root cause: [why they conflict]
- Resolution: [decision] per priority [N from list above]
- Rejected: [alternative] — consequences: [what we give up]
- ADR: [link/id if significant]
```

Significant conflicts (style, boundaries, data ownership, security posture,
build-vs-buy) always produce an ADR via arch-decision.

## Overengineering Controls

Prefer the simplest architecture satisfying confirmed requirements and quality
attributes. Before adding any component, platform, abstraction layer, framework,
gateway, broker, workflow engine, service mesh, database, or agent, verify:

- Which confirmed requirement requires it?
- Which identified risk does it mitigate?
- Why can no existing component satisfy it?
- What is its operational cost (people, tooling, on-call)?
- What are its failure modes?
- What are the replacement/migration implications?

Reject components with no measurable architectural value. No future-proofing
abstractions without a realistic, named change scenario.

## Validation Gates

All must pass before final synthesis:

- [ ] Every functional requirement is addressed by at least one component
- [ ] Every critical quality attribute is addressed and measurable
- [ ] Every component has a single clear responsibility
- [ ] Service/module boundaries are justified (not arbitrary)
- [ ] Data ownership is explicit per store
- [ ] Integration patterns are consistent (no random sync/async mixing)
- [ ] Security controls cover all major trust boundaries
- [ ] Failure scenarios and recovery behavior are defined
- [ ] Deployment and operational responsibilities are assigned
- [ ] Observability covers all critical flows
- [ ] Technology choices are mutually compatible
- [ ] No selected technology violates a stated constraint
- [ ] No major decision is implicit
- [ ] Complexity is proportional to the problem
- [ ] The architecture can be delivered incrementally
- [ ] Open questions and assumptions are visible in the output

On failure: identify the failing gate, re-invoke the responsible specialist with a
targeted correction request naming the gate. Revalidate affected evidence, then
evaluate the complete new baseline before readiness. Never reuse stale approvals.

## Final Synthesis Rules

- One document, one voice. Normalize terminology across all specialist outputs
  (pick one term per concept and use it everywhere).
- Remove duplicated recommendations; keep the strongest rationale.
- Every section must trace back to requirements, quality attributes, or constraints.
- The selection table (concise version) goes in an appendix when useful.
- Verify the final document against the original request before delivery.

## Failure and Fallback Behavior

**Required skill unavailable:**

1. State which capability is missing.
2. Check the catalog for a skill with sufficient overlap.
3. Use the overlapping skill only with its limitations documented in the output.
4. Otherwise perform a basic orchestrator-level analysis.
5. Mark the affected area "requires specialist review" in the final document.

**Runtime cannot invoke skills dynamically:**

1. Generate the recommended skill execution plan (selection table + order).
2. Name each skill that should be applied and the input it requires.
3. Do NOT claim the skills were executed.
4. Continue with the best architecture analysis possible from available context,
   marking which sections are provisional pending specialist execution.
