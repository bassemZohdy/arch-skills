---
name: arch-interview
description: "Interview architects and stakeholders to elicit a proposed or existing solution architecture, or interview an architecture committee to draft governance policies, principles, standards, decision options, evaluation criteria, rules, profiles and quality gates. Use for architecture discovery and governance onboarding; arch-orchestrator retains lifecycle coordination."
---

# Architecture Interview

Conduct structured, adaptive conversations to **extract architectural knowledge**,
not to approve designs or governance on an interviewee's behalf. Reuse a common
question/reconciliation mechanism for two distinct interview modes.

## Modes

- **Solution architecture:** Discover system boundaries, components, interfaces,
  integration patterns, data ownership, deployment, quality scenarios, constraints,
  significant decisions, alternatives and risks. Distinguish existing, proposed
  and mixed architecture, and identify evidence needed to confirm statements.
- **Governance:** Discover the organization's policy/reference catalog, principles,
  standards, permitted design options, evaluation dimensions, concrete rules,
  applicability conditions, gate thresholds, exceptions and approval ownership.
  Output a **draft** versioned review profile, not an enforced approved policy.

## Interview protocol

1. Classify requested mode, scope, responsible authority and known evidence.
   If ambiguity materially changes the conversation, clarify that point.
2. Prepare prioritized, adaptive questions. Ask one question by default, or a
   small related batch when answers are independent. Offer unbiased alternatives
   plus a custom answer; do not hardcode architectural preferences.
3. Capture question ID, respondent, raw answer, interpretation, evidence,
   provenance, contradictions and confirmation status. Keep facts, assumptions
   and inferred interpretations distinct.
4. Reconcile each batch: check gaps, unsupported claims, dependencies and
   conflicting answers. Ask only targeted follow-ups needed for the selected
   scope. An exhausted interview is not proof of completeness.
5. Summarize proposed structured records, unresolved issues, owners, versions,
   validation requirements and the responsible approval authority.

## Governance extraction rules

Keep **reference artifacts**, **criteria**, **testable rules**, **architecture
decision options**, **evaluation profiles** and **acceptance gates** as separate
concepts. A source document is not automatically a mandatory gate. Capture
each rule's applicability, enforcement, required evidence, severity, exception
authority and related reference provenance. For exclusive option areas, capture
one expected option per scoped area; separate orthogonal facets rather than
forcing mutually compatible patterns into competing selections.

A respondent's role label does not itself establish approval authority. Do not
treat an interview response, model confidence or silence as approval.

## Lifecycle and specialist boundaries

`arch-orchestrator` retains the DAP requirement-baseline interview,
convergence, persistence, lifecycle stages and approval contract. This skill
provides architecture/governance **discovery** records for that orchestrator,
`arch-doc`, `arch-diagrams`, `arch-governance` and `arch-review`.
It does not create a second lifecycle orchestration engine.

`arch-reverse` independently recovers technical observations from source code.
Never present a stakeholder's claim as observed implementation behavior.

## Examples

- Interview a solution architect and produce a scoped architecture description.
- Interview the architecture committee to draft rule/gate profile configuration.
