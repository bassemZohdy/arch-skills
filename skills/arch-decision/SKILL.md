---
name: arch-decision
description: Drive structured architecture decision-making using Decision Analysis and Resolution (DAR) methodology. Combines ADR documentation with weighted scoring, gate criteria, sensitivity analysis, and a criteria library for common technology selections. Use when making architecture decisions, selecting technologies, evaluating build vs buy, choosing cloud services, or performing structured trade-off analysis.
---

# Architecture Decision Analysis

Structured decision-making for architecture and technology choices.

## Workflow

```
1. Frame Decision → Statement, scope, constraints, owner, deadline
2. Define Gates → Pass/fail knockout filters
3. List Alternatives → 2-5 viable options (always include "Do Nothing")
4. Score Criteria → Weighted matrix (weights sum to 100, scale 0-5)
5. Evaluate Matrix → Draft scores with rationale
6. Sensitivity Check → Test ranking stability
7. Recommend → Summary with tradeoffs and risks
8. Document → Generate DAR/ADR document
```

## Modes

| Mode | Use When | Criteria | Alternatives |
|------|----------|----------|--------------|
| **Expedited** | Low-stakes, reversible, single owner | 2-4 | 2-3 |
| **Formal** | Architectural, costly to reverse, multiple stakeholders | 3-7 | 2-5 |

## Stage 1: Frame the Decision

Capture before anything else:

| Field | Description |
|-------|-------------|
| **Decision Statement** | One clear sentence: "We need to decide..." |
| **Scope** | In scope / out of scope |
| **Constraints** | Hard limits that cannot change |
| **Assumptions** | Believed true but could be wrong |
| **Decision Owner** | Who makes the final call |
| **Approver(s)** | Who must sign off |
| **Deadline** | When decision must be finalized |
| **Review Triggers** | Conditions requiring revisiting |

## Stage 2: Gate Criteria (Knockout Filters)

Binary pass/fail requirements. Any alternative failing ANY gate is eliminated.

- Any number of gate criteria is allowed, including zero when no knockout constraint applies
- Must be strictly binary: "Must X" or "Must not X"
- Apply every relevant gate to every alternative. Mark a gate not applicable only with a reason and authority.

## Stage 3: List Alternatives

Enumerate 2-5 viable alternatives. Always prompt:
> "Should we include a 'Do nothing / defer' baseline option?"

Apply gate checks and eliminate failing alternatives.

## Stage 4: Scored Evaluation Criteria

**Rules:**
- Weights must sum to exactly 100
- Each criterion defines what 5 (best) and 1 (worst) looks like
- Check for overlapping criteria

**Scoring Scale:**

| Score | Meaning |
|-------|---------|
| 0 | Does not meet criterion at all |
| 1 | Poor - significant gaps |
| 2 | Below average - notable limitations |
| 3 | Acceptable - meets basic requirements |
| 4 | Good - exceeds requirements |
| 5 | Excellent - best possible |

**Confidence Rubric (Formal mode):**

| Level | Definition |
|-------|-----------|
| **High** | Measured data, benchmarks, production experience |
| **Medium** | Vendor docs, limited experience, community consensus |
| **Low** | Expert judgment only, assumption, extrapolation |

Flag: Low confidence + weight >= 20 → Consider spike/PoC before committing.

## Stage 5: Evaluate Matrix

**Formula:**
```
weighted_score = (weight / 100) × score
total_score = Σ weighted_scores [max = 5.00]
```

Proactively draft proposed scores. Present full matrix for user review.

Keep hard constraints out of the weighted score: a mandatory requirement is a
gate, not a preference. Record the evidence, confidence, assessor and date for
each score, and separate measured facts from assumptions and vendor claims.

## Stage 6: Sensitivity Check

1. Identify two highest-weight criteria (W1, W2)
2. Run two bounded perturbations. Transfer weight only within the [0, 1] interval and renormalize all weights; never create negative weights or weights above 1.
3. Recompute totals using the same eligible alternatives and check ranking stability
4. Flag if gap < 0.5 → Close call

## Stage 7: Recommendation

- Recommended alternative with scores + rationale
- Key tradeoffs vs. second-ranked alternative
- Risks and mitigations
- Assumptions that would invalidate decision
- Review triggers

## Stage 8: Document

Generate complete DAR/ADR document using templates:
- `assets/dar-document.md` - Formal mode template
- `assets/dar-expedited.md` - Expedited mode template
- `assets/adr-template.md` - MADR ADR template

## Pre-Document Validation

- [ ] Weights sum to exactly 100
- [ ] All alternatives passed gates
- [ ] Totals verified by hand (at least 2)
- [ ] Recommendation matches highest score (or override documented)
- [ ] Low-confidence + high-weight scores flagged
- [ ] Sensitivity check completed
- [ ] No overlapping criteria

## Criteria Library

See `references/criteria-library.md` for reusable evaluation bundles:
- Cloud Service Evaluation
- Open Source Library Selection
- Build vs Buy
- Infrastructure & Tooling Selection
- Security Tool Selection

## Facilitation Rules

1. One stage at a time
2. Validate at each stage
3. Propose drafts, don't just ask
4. Flag problems immediately
5. Be concise in conversation
6. Never force a recommendation
7. Verify your own math

## Examples

- Choose between PostgreSQL and DynamoDB for a new order service using a weighted matrix.
- Run a build-vs-buy analysis for an internal feature-flag platform.
- Document an expedited decision to adopt a logging library with a lightweight DAR.

## Common Gotchas

- Do not let one stakeholder's preferred option drive the criteria weights; set weights before scoring.
- Overlapping criteria double-count the same concern and skew totals.
- A close call (gap < 0.5) without a sensitivity check is a coin flip dressed as analysis.
- A precise-looking score does not create certainty; preserve dissent, evidence gaps and the trigger for revisiting the decision.

## Further Reading

- `references/awesome-architecture.md` — Curated external articles, videos, libraries, and samples per topic (awesome-architecture.com)

## Related Skills

- **arch-doc** - ADR templates and documentation frameworks
- **arch-fitness** - Encoding decisions as automated checks
- **arch-governance** - Approval workflows and decision boards
