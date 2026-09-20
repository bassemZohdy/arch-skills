---
name: arch-orchestrator
description: "Interview stakeholders, create a solution architecture, or update an existing architecture baseline. Use for end-to-end or multi-domain architecture work, including modernization and migration. Use arch-evaluate for process audits and arch-review for design-quality reviews; narrow specialist requests do not require the full process."
---

# Architecture authoring

Own mode selection, evidence/state management, specialist routing, reconciliation
and one coherent architecture. Keep domain reasoning in specialist modules.
Do not confer human approval, infer consent, or broaden an interview into design.

## Workflow

1. Select interview, create or update from the user's requested outcome. Read
   `references/workflow-modes.md` for the selected mode and its stopping boundary.
2. Inspect available artifacts before assuming a new project. Classify greenfield,
   brownfield or mixed scope; record missing evidence and the accountable owners.
3. Read the packaged `framework/records.md` and configuration contract for DAP
   work. Verify persistence and compatible framework/schema/rubric versions.
   Use `assets/dap-requirement-template.json` and
   `assets/dap-checkpoint-template.json`; placeholders are not approved records.
4. Interview and reconcile requirements, constraints and quality scenarios.
   Save answers, provenance and checkpoints after every round. Respect the
   configured budget; silence and incomplete evidence do not establish convergence.
5. For create/update, select the minimum sufficient specialists using
   `references/skill-catalog.md`. In a built package, resolve modules through
   package-catalog.json. Record selection reasons, gaps and dependencies with
   `assets/selection-table-template.md`. Do not load all modules by default.
6. Supply relevant baseline/REQ/CON IDs, questions, evidence, protected decisions
   and expected output. Read `references/orchestration-playbook.md` for the
   contribution contract. Maintain `assets/shared-context-template.md`.
7. Develop views and proposed ADRs together. Mandatory constraints are eligibility
   gates, not weighted preferences. Resolve conflicts explicitly with alternatives,
   evidence, consequences and the configured human decision authority.
8. Review the design through arch-review and route mandatory human dispositions.
   Security/privacy/compliance, irreversible/high-risk, material cross-team and
   configured cost implications cannot be silently waived.
9. Assemble the default twelve-section arc42 description through arch-doc, with
   ADR log, trace graph and verification plans. Preserve useful content from
   `assets/solution-architecture-template.md` through the arc42 mapping; the
   22-section template is only an optional standalone presentation format.
10. Freeze a candidate, run arch-evaluate read-only, and distinguish design
    quality, process completeness and executed verification. Publish generated
    reports only when authorized. An incomplete candidate remains a draft.

## Shared state and authority

Use REQ, CON, DES, ADR, VER, Q, ASM and EXC IDs (plus SRC for source records).
Keep provenance, revisions, owners and typed relationships. Stable requirements
need per-item checks, set-level checks and explicit stakeholder confirmation on
the same baseline. Bind reviews and assessments to the frozen subject hash.
Accepted/rejected ADR reasoning is immutable; substantive changes supersede it.

The orchestrator merges proposals; only the configured human authority or an
evidenced human-approved delegation can accept a decision. An agent's confidence
and a high completeness score are not authority. Missing policy blocks dependent
acceptance without preventing independent analysis.

Update mode preserves the current baseline and follows dependency closure.
Return to interview for invalidated requirements, design for design-only changes,
and review for authority changes. Invalidate affected assessments/approvals and
evaluate the complete new candidate before readiness.

## Outputs and stopping

- Interview: scoped requirement/constraint records, scenarios, questions,
  assumptions, convergence evidence and resumable next action; stop before design.
- Create: coherent candidate views, ADRs, DES inventory, VER plans, trace graph,
  human review status and separate process/design findings.
- Update: change record, affected IDs, re-entry stage, supersessions, new candidate
  revision, stale evidence and a concise before/after explanation.

At handoff name the artifact owner, delivery maintainer, continuing architectural
reviewer, periodic-review owner/cadence and pending actions. Do not claim a
scheduler or review notification ran when the host has not performed it.

## Failure and fallback

Missing persistence yields a non-resumable draft, not a completed DAP baseline.
Missing specialists yield explicit limitations. Read bundled module instructions
directly when possible; never pretend a tool/subagent invocation occurred.
A process-only audit routes to arch-evaluate, not back through authoring.
An evaluate request never authorizes repair.

## Examples

- Interview stakeholders for a proposed order platform, stopping at confirmed requirements.
- Create an architecture from an approved brief, choosing only relevant specialists.
- Update a billing architecture for a changed residency constraint and identify affected approvals.

## Related skills

- **arch-evaluate** — process evidence and readiness, read-only
- **arch-review** — design fitness and trade-offs
- **arch-doc**, **arch-decision**, **arch-governance** — artifact, decision and authority support
