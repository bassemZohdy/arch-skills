---
name: arch-evaluate
description: Evaluate whether a solution architecture followed the Deterministic Architecture Process and whether its recorded artifacts are complete, traceable and current. Use for DAP completeness audits, brownfield baseline assessment, requirements-to-design traceability, gate validation, score calculation and stale evaluation detection. Do not use it as a substitute for architecture design-quality review.
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

