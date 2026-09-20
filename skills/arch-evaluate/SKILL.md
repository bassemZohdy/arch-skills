---
name: arch-evaluate
description: "Evaluate Deterministic Architecture Process completeness, traceability, evidence freshness and readiness for a frozen architecture baseline. Use for process audits, brownfield evidence-gap assessment and readiness checks. Use arch-review for design quality; do not author or repair architecture during evaluation."
---

# Architecture process evaluation

Assess recorded evidence independently of authoring. Process completeness does
not certify design quality or delivered behavior. Preserve unknowns and
disagreements rather than inferring undocumented interviews or approvals.

## Workflow

1. Identify scope and the project artifact root. Load its explicit manifest,
   configuration and versions. Read `references/evaluation-contract.md`.
2. Resolve the installed package root independently of the current directory.
   Its scripts and framework contracts are bundled by the package builder.
   Install the declared Python dependencies only when authorized.
3. Run the package's scripts/dap_validate.py against the project. Exit 0 means
   ready, 1 means assessed but blocked/unassessable, and 2 means CLI failure.
4. Review semantic assessments against their cited evidence. Structural validity
   alone cannot prove a stakeholder's intent or a human's authority.
5. Report Q/D/F/B/T/A/S with counts, exclusions, unknowns, uncovered IDs, input
   hash, versions, evaluator identity and readiness gates. Never renormalize
   missing dimensions or equate a high score with readiness.
6. For an authorized report publication, use scripts/dap_publish.py. It creates
   immutable reports and an adjacent generated summary; arch-doc can link that
   summary in its evaluation appendix without changing the assessed baseline.
7. For a requested design review, route separately to arch-review. Return
   missing evidence and next actions; do not invoke authoring to fill the gaps.

## Invocation

Resolve these paths from the installed package root, not a repository checkout:

- scripts/dap_validate.py PROJECT — read-only evaluation
- scripts/dap_publish.py PROJECT — explicitly authorized generated-report write
- scripts/dap_rtm.py PROJECT — explicitly authorized derived RTM under evaluations/
- scripts/dap_manifest.py PROJECT — snapshot inspection/freshness comparison

The source checkout has the same scripts at its root for contributors. Build a
portable package before installing an individual skill; copying this source
directory alone does not include its generated dependencies.

## Evidence rules

Read `framework/records.md` for schema 2.0.0 records, source/constraint/verification
links and checkpoint envelope. Unsupported historical contracts are reported as
unavailable; never fabricate a historical score or silently migrate approvals.

Enumerate criteria from the packaged immutable rubric. Every semantic assessment
names its criterion, target, dimension, baseline revision, subject hash, assessor,
evidence locators and rationale. Unknown/fail receive zero; authorized
inapplicability is explicit and never waives mandatory convergence or review.
Cross-check significant decisions against the design inventory, not just ADRs.

Security/privacy/compliance implications always require human disposition.
Validate configured risk, irreversible, cross-team and cost review applicability;
the authoring agent cannot approve these by changing a convenience flag.
Unapproved/expired exceptions, conflicting constraints and blocked questions
prevent readiness. Missing source, design or verification evidence breaks a
design-stage trace chain. A planned test is not executed verification.

## Output

Use `assets/evaluation-report-template.json` as the minimum report shape.
Include exact counts and full-precision calculation provenance, rounding only
displayed percentages. Report freshness separately and keep previous reports.
The implementation verifies evidence existence, snapshot binding and declared
authority; it does not authenticate human identities or replace human adjudication.

## Examples

- Audit a brownfield architecture whose interview history is incomplete.
- Check a candidate that has excellent scores but a pending security review.
- Reassess after a changed requirement and identify stale approvals.

## Related skills

- **arch-review** — independent design-quality assessment
- **arch-orchestrator** — authorized create/update work after findings
- **arch-governance**, **arch-decision**, **arch-doc** — policy, ADRs and documentation
