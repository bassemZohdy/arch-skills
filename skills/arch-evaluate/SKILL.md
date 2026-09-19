---
name: arch-evaluate
description: Evaluate whether a solution architecture followed the Deterministic Architecture Process and whether its recorded artifacts are complete, traceable and current. Use for DAP completeness audits, brownfield baseline assessment, requirements-to-design traceability, gate validation, score calculation, evidence-linked report publication and stale evaluation detection. Do not use it as a substitute for architecture design-quality review.
---

# Deterministic Architecture Process Evaluator

Assess a frozen architecture baseline. The evaluator reports process and artifact evidence; it does not design the system, repair the assessed files or certify delivered behavior.

## Workflow

1. Resolve the project artifact root, configuration and recorded framework/schema/rubric versions.
2. Freeze the explicit input manifest and refuse to assess a concurrent revision.
3. Run the deterministic validator and score calculator from scripts/dap_validate.py.
4. Inspect semantic checks and record evidence locators, unknowns and applicability decisions.
5. Calculate requirements quality, decision coverage, forward traceability, backward traceability, conservative traceability, artifact completeness and the configured overall score.
6. Evaluate readiness gates separately. A score never overrides a failed review, missing evidence, invalid configuration or stale baseline.
7. Write a versioned report and generated appendix only through the publishing command. Audit-only mode leaves assessed inputs unchanged.

## Required distinctions

- Process completeness is separate from design fitness; use arch-review for architecture quality and trade-offs.
- Design-stage traceability is separate from implementation and executed verification evidence.
- A missing historical record is unproven, not proof that the event never happened.
- Unknown checks receive zero credit. Approved not-applicable checks require a reason and authority.
- Won't have is a timeframe priority and cannot waive a binding security, legal, compliance or quality obligation.
- LLM confidence is commentary, not approval evidence.

## Commands

From the repository root:

  python scripts/dap_validate.py path/to/architecture
  python scripts/dap_rtm.py path/to/architecture
  python scripts/dap_publish.py path/to/architecture

Read references/evaluation-contract.md for the score and freshness contract. Use
assets/evaluation-report-template.json as the report shape when a host needs a
structured template.

## Output

Report the input manifest hash, versions, all metric numerators and denominators,
forward/backward uncovered IDs, gate status, blocking findings, stale status,
evidence gaps and the next action. Do not report an overall score when a required
dimension is not assessable.

## Evidence and boundaries

Treat the evaluator as an independent, read-only assessor of a frozen baseline.
Every pass, fail, unknown and approved not-applicable result needs a locator and
rationale. A generated report is a new artifact, not evidence that was present in
the assessed baseline. Never repair inputs, infer stakeholder intent, or convert a
score into approval.
## Assessment inputs

Treat the architecture directory as a frozen evidence set. Include the requirements, constraints, design elements, ADRs, traceability graph, verification plans, process state, review dispositions, exceptions, configuration and rubric identified by the manifest. Do not add generated reports, appendices or evaluator commentary to the assessed input set. If an expected artifact is absent, record the absence as unknown evidence and explain the resulting gate or score effect.

Check that every identifier is stable and that links point to records in the same baseline. Confirm that the configuration names the framework, schema, rubric and policy versions, and that the configured authority is present for every applicable review. A report with a valid hash but invalid configuration is not ready.

## Semantic evidence

Structural checks establish that records exist and are linked; they do not establish that a stakeholder confirmed intent or that a reviewer approved a decision. For each semantic criterion, cite the exact record, section, field or line that supports the result. Preserve the assessor's rationale when evidence is ambiguous. Use pass only when the evidence meets the criterion, fail when the evidence contradicts it, unknown when the required population or evidence is unavailable, and not-applicable only when an authorised authority recorded a reason.

Do not infer a completed interview from polished requirements, infer approval from silence, or infer implementation verification from a planned test. Keep design coverage, implementation coverage and executed verification as separate measures.

## Gate handling

Compute the configured dimensions from the frozen assessments and show each numerator, denominator, excluded population and unknown count. Apply the configured weights exactly; do not change them to improve a result. A high score cannot override a pending security, privacy, legal, compliance, cost or cross-team review. A stale manifest invalidates the report even when the calculated score is unchanged.

If a gate fails, report the blocking finding and the next evidence or human disposition required. Do not repair the assessed files during an audit-only run. An authorised publishing step may write only the generated report and appendix after the input manifest has been verified.

## Report discipline

Include framework, schema, rubric and configuration versions, the UTC assessment time, evaluator identity, input manifest hash, metric details, uncovered identifiers, evidence locators, applicability decisions, blocking findings, gate status and stale status. State the next action in operational terms. Preserve prior reports as immutable records and create a new report for every changed baseline.

Use arch-review for design quality and trade-off assessment, arch-governance for authority and exception policy, arch-decision for option analysis, and arch-doc for the architecture description. This skill evaluates recorded process evidence; it does not replace those responsibilities.

## Further Reading

- `references/evaluation-contract.md` — Versioned score, gate and freshness contract
- `assets/evaluation-report-template.json` — Structured report shape for publishing

## Related Skills

- **arch-orchestrator** — Runs the process and preserves the shared baseline
- **arch-review** — Reviews design fitness and trade-offs
- **arch-governance** — Defines decision authority and exception policy
- **arch-decision** — Records significant choices and rejected alternatives
