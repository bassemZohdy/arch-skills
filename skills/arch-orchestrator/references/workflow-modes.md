# Public architecture workflows

Use one shared checkpoint and record contract for all authoring modes. This
reference adds modes to arch-orchestrator; it is not another execution engine.

## Preparation before the first interview round

Every new orchestrator invocation starts with preparation unless the user
explicitly supplies a mode and a confirmed, traceable requirements baseline.
The first response must summarize the requirement seed, classify the scope as
greenfield, brownfield or mixed, list known constraints and evidence, identify
the decision owner and expose the important gaps. It then prepares a small,
prioritized question plan covering functional goals, scope, quality attributes,
mandatory constraints, stakeholders, evidence and verification, while exposing
only the next question.

Present one prepared question and ask the user to answer it in the same
response. This marks the interview active; it is not a design response and it
must not select technologies, specialists or ADRs. Reconcile each answer into
the checkpoint before asking the next question. Once the requirements handoff
has explicit stakeholder confirmation, honor the requested stopping boundary or
continue into create/update when the user asked for it.

## Conversational question protocol

Use one active `Q` record per turn. Keep the question focused; do not combine
several independent decisions into one prompt. Each question should contain:

1. The question and a short statement of why the answer affects the
   architecture or its verification.
2. A prioritized choice list, normally no more than four options:
   - **Recommended** — the best-practice default for the stated context, with
     the reason and its main trade-off.
   - **Industry reference** — a relevant option grounded in a named standard,
     protocol, regulatory source or established industry pattern, with a link
     or source identifier when available. Omit this option when no genuine
     reference applies; never fabricate one.
   - **Alternative** — another viable choice, with the consequence that makes
     it different.
   - **Custom answer** — free text supplied by the stakeholder; always last.

Merge options when the recommended practice is also the reference-backed choice
so the list remains short. Treat every suggested choice as an assumption until
the stakeholder selects it. A free-text reply, an answer outside the list or an
explicit uncertainty is recorded as user input and may trigger a follow-up
question; do not force it into the closest option.

If the host supports structured choice controls, use them. Otherwise render the
same list as numbered or lettered Markdown choices and accept either the number,
the option text or a custom response. After each answer, acknowledge what was
recorded, retain the selected option's rationale and provenance, update linked
`REQ`/`CON`/`ASM` records, save the checkpoint and then ask the next question.
If the user requests all questions or the host cannot maintain turns, provide a
clearly ordered batch as an explicit fallback and preserve the same option order
for every question.

## Interview

Capture the seed, participants, scope, evidence access and human decision owner.
Load an existing baseline when present. Ask one question per turn, covering
business flows and architecture-driving quality attributes together across the
conversation. Capture source revision, owner, REQ/CON IDs, scenarios, Q/ASM
records and verification intent. Suggested answers remain assumptions until
confirmed.

After each received answer, reconcile the baseline and save a checkpoint. Apply
eleven per-requirement, five set-level and one stability check. Stability needs
an explicit stakeholder confirmation round with matching before/after hashes.
Exhausted budgets or unanswered blocking questions produce a blocked checkpoint.

Stop after the requirements handoff when the user requested interview only.
Do not proceed to technology selection, full design or publication without a
request covering that work. Exploratory sketches remain provisional.

## Create

Inspect existing artifacts first. Do not overwrite an existing baseline under a
new-project assumption. Prepare/interview only as needed; a supplied requirements
set still needs provenance and convergence evidence.

Select relevant specialist modules, compare eligible alternatives, create views
and ADRs together, and maintain DES/VER relationships. Route human reviews using
configured authority. Assemble twelve arc42 sections, ADR log and trace graph;
use the packaged arch-doc mapping rather than forcing the old 22-section layout.
Evaluate the candidate separately from design review. Report pending gates as
pending; publication and human acceptance are not implied by drafting completion.

## Update

Load requirements, constraints, views, ADRs, trace graph, policy, checkpoint and
prior assessments. Missing history is unproven, not permission to recreate it as
approved. Record the requested change and classify what it invalidates.

- Requirements/constraints changed: re-enter interview, then design and review.
- Design choice failed valid requirements: re-enter design, then review.
- Approval/authority changed: re-enter review.
- Editorial-only change: preserve accepted reasoning; recalculate freshness.

Use typed links to compute dependency closure, preserve record IDs and history,
and supersede accepted/rejected ADRs rather than rewriting their reasoning.
Create a new candidate revision and invalidate affected evidence. Reassess the
complete candidate before readiness; a local fix is not a global gate result.

## Evaluate routing

For process evidence use arch-evaluate; for quality attributes and trade-offs use
arch-review. For a general request covering both, report separate process and
design results. Neither path calls authoring to fill gaps during the audit.
Ask about scope only when it materially changes the assessment. A request to
evaluate does not authorize repairs, installations, messages or publication.

## Loading specialists

In a built package, read package-catalog.json for module paths. Load only the
selected module's instructions.md and relevant resources; paths inside that
module resolve from its resource_root. Deterministic scripts and framework paths
resolve from the outer installed package. Reading instructions does not require
a subagent. Delegate only when the host supports it and authorization allows it.
Record which capabilities were actually applied; unavailable capabilities remain
explicit gaps. Never claim an invocation happened merely because it was planned.

Expert installations may instead load a selected standalone skill. Keep narrow
requests narrow: a single API, ADR, diagram or performance review does not require
running all DAP stages.
