---
name: arch-orchestrator
description: "Interview stakeholders, create solution architectures, or update existing baselines. Use for end-to-end or multi-domain architecture, modernization and migration. Unspecified architecture goals start with a requirements interview; focused artifact requests route to the relevant specialist, including arch-diagrams for diagram-first work. Route process audits to arch-evaluate and design-quality reviews to arch-review."
---

# Architecture authoring

Own mode selection, evidence/state management, specialist routing, reconciliation
and one coherent architecture. Keep domain reasoning in specialist modules.
Do not confer human approval, infer consent, or broaden an interview into design.

## Default entry contract

First resolve the requested outcome. Route process audits to arch-evaluate and
design-quality reviews to arch-review, preserving read-only scope. Route a bounded
artifact or specialist request directly through the catalog; diagram creation uses
arch-diagrams. These routes take precedence over interview preparation and do not
require full DAP. Ask only for information necessary for the requested task.

For end-to-end authoring, treat an invocation without an explicit `interview`, `create from confirmed
requirements`, or `update` outcome as a preparation request. Do not select
technology, specialists or a target architecture on the first turn.
The user only needs to state the architecture goal; infer the conversational
interview format, choice ordering and host-control fallback from this contract
instead of requiring those instructions to be repeated in every prompt.

1. Parse the initial requirement seed into a short intake summary: desired
   outcome, known scope, likely greenfield/brownfield/mixed classification,
   known constraints and evidence, stakeholders or decision owner, and unknowns.
2. State the selected mode and its reason. If the mode or scope classification
   is genuinely unclear, ask the smallest clarifying question before preparing
   the interview.
3. Prepare a prioritized question plan covering goals and scope, users and
   workflows, mandatory constraints, quality attributes, evidence and
   ownership, and success or verification. Partition related, independent
   questions into small bounded batches in the checkpoint. Keep the plan in
   the checkpoint, but expose only the next question or first related batch
   unless the user asks for the full plan.
4. Present one question at a time by default. When several questions share
   context and no answer depends on another, present a bounded group (normally
   two to four questions) or pre-plan that sequence for collection without a
   new reasoning pass after each answer. Do not group independent decisions,
   high-risk clarifications or questions whose answers can change the scope.
   Offer each question a small ordered set of choices: a recommended
   best-practice default first, a relevant reference-backed industry option
   when one genuinely applies, other viable alternatives with their trade-offs,
   and `Custom answer` as the final option. Never invent a standard, citation
   or industry claim. Inspect the active host capabilities first: when a native
   user-input or elicitation control supports a grouped form, invoke it with
   the stable questions and choices; otherwise collect the prepared questions
   sequentially or use a clearly labelled text group.
5. Mark the interview active and record each selected option or free-text answer
   and its provenance as it arrives. Persist raw answers locally, but send the
   completed batch together for reconciliation and checkpointing rather than
   performing full reconciliation after every answer. Host-required model turns
   still occur; do not claim to suppress them. Reconcile early when
   an answer is ambiguous, blocking, scope-changing or high-risk, then prepare
   the next batch. Do not produce a candidate architecture, technology
   recommendation, ADR or specialist selection until the interview has enough
   evidence and the stakeholder explicitly confirms the requirements handoff.
   A user who supplies a confirmed, traceable baseline and explicitly requests
   create or update may skip the initial conversation only after provenance and
   convergence are checked.

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

### Diagram routing

- If the requested primary artifact is a diagram or diagram-as-code source,
  select `arch-diagrams`; route focused reviews through arch-review with that
  specialist in read-only mode. Keep the
  diagram scope, baseline, source and validation status explicit.
- If diagrams support a broader create/update deliverable, keep the orchestrator
  as the owner of the coherent architecture, use `arch-diagrams` for the focused
  views, and pass its sources and evidence to `arch-doc` for document assembly.
- A diagram is not deployment or verification evidence by itself. Add the
  relevant domain specialist when the view depends on security, data, events,
  cloud placement or operational behavior.

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

## Cross-skill handoff

Use the catalog as a routing aid, not a mandatory execution chain. Capture security,
accessibility, operations and cost constraints during requirements; refine them as the
design develops. Reconcile competing specialist proposals against the same baseline and
record the chosen owner and evidence. Respect host form limits and built-in custom-
answer controls; conversational batching cannot suppress host-required model turns.

For requested external reading, load `references/awesome-architecture.md`;
community links do not replace primary evidence for a design decision.

## Related skills

- **arch-evaluate** — process evidence and readiness, read-only
- **arch-review** — design fitness and trade-offs
- **arch-doc**, **arch-diagrams**, **arch-decision**, **arch-governance** — artifact, diagram, decision and authority support
