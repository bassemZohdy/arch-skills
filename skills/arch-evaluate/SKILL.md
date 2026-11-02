---
name: arch-evaluate
description: "Evaluate Deterministic Architecture Process completeness, traceability, evidence freshness and readiness for a frozen architecture baseline. Use for process audits, brownfield evidence-gap assessment and readiness checks, including diagram source and baseline evidence. Use arch-review for design quality; do not author or repair architecture during evaluation."
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
   Retain the actual structured report and exit code. Report a malformed response
   or failed invocation as an execution error, not as a computed failing score.
4. Review semantic assessments against their cited evidence. Structural validity
   alone cannot prove a stakeholder's intent or a human's authority. When a
   baseline contains diagrams, check that editable source, stable IDs, baseline
   or source revisions, linked records and freshness evidence are present; do
   not treat a rendered diagram as proof of deployed behavior.
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

## Scoring and gate rules

These mirror the packaged scorer; apply them when interpreting or explaining a report.

- **Validator outcome:** exit 0 with a well-formed report is ready; exit 1 with a
  well-formed report is assessed but blocked, and its computed scores remain valid
  report values; exit 2, a crash or malformed/truncated output (whatever the exit
  code) is an execution error with no score, not a zero score and never ready.
- **Dimension score:** passed ÷ counted checks × 100. Count checks, not targets: D
  is ten checks per inventoried significant decision, so a decision without an ADR
  adds ten failing checks. Fail and unknown (including missing assessments) stay
  counted with zero credit.
- **Not applicable:** excluded and reported only with a reason, an `authorized_by`
  listed in the authority map and resolvable authorization evidence. An exclusion
  lacking any of these is an invalid assessment, so no S is computed.
  requirements_quality checks are never excludable, even with full authorization.
- **Traceability:** T = min(F, B). F counts complete source → REQ → DES/accepted ADR
  → VER chains, where planned VER completes a design-stage chain but never proves
  delivery. B counts significant DES justified by active REQ or sourced CON. Only
  accepted ADRs justify; proposed, rejected or superseded ones break the chain.
- **Weights:** exactly four, nonnegative, summing to exactly 1, with traceability
  greater than or equal to every other weight. Otherwise weights are invalid and
  S is not computed, but every independent finding is still reported.
- **Overall score:** S = wQ×Q + wD×D + wT×T + wA×A in exact fractions. Report
  `overall_exact` as the exact string (for example `200/3` or `905/10`) and
  `overall_score` as its number rounded to one decimal (66.7, 90.5); never compare
  gates on the rounded value. If any dimension is unassessable or its
  population is empty, S is null; never renormalize over remaining dimensions.
- **Readiness:** all gates must pass regardless of S. Any open blocking question or
  risk, an unapproved or expired exception, a missing or stale mandatory review, or
  a reviewer outside the configured authority map blocks readiness. A review bound
  to another subject hash or baseline is stale; never carry it forward.
- **Freshness:** any change to a manifested input, including reviews, assessments,
  configuration, rubric or schema, invalidates the previous report. Only generated
  `evaluations/` output and the DAP EVALUATION BEGIN/END region of architecture.md
  are excluded.

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

## Cross-skill handoff

Consume a frozen, version-compatible DAP baseline and its declared evidence. Return each
failed gate with affected IDs, evidence gaps and a responsible next action to arch-orchestrator; return design concerns to arch-review separately. A missing runtime or
dependency produces an unavailable deterministic assessment, not a fabricated numeric
result; qualitative observations may still be reported with that limitation.

Diagram evidence gaps remain findings against the assessed baseline. Do not invoke
`arch-diagrams` to repair or rewrite inputs during evaluation; route authorized design
changes through arch-orchestrator and use `arch-diagrams` after the new baseline is
prepared.

## Related skills

- **arch-review** — independent design-quality assessment
- **arch-orchestrator** — authorized create/update work after findings
- **arch-governance**, **arch-decision**, **arch-doc**, **arch-diagrams** — policy, ADRs, documentation and diagram evidence
