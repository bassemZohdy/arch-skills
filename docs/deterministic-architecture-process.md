# Deterministic Architecture Process Framework

19 Sep 2026 · @Bassem Reda Zohdy Hussein

## Purpose and Problem Statement

Architecture teams need a repeatable way to turn incomplete needs into justified solution designs. Established methods already support this work, but applying them consistently through an AI assistant requires explicit inputs, state, decision rules and evidence. This framework defines that operating process for solution architecture without claiming that architecture methods are absent from the industry.

The goal is a repeatable, auditable path from a requirement seed to a reviewed architecture baseline. Deterministic means that the same recorded facts, configuration, rubric and assessments produce the same gate results and score. It does not mean that an LLM always asks identical questions, produces identical prose or finds a uniquely correct architecture. This revised specification is framework version 1.0.0 and is implemented as the repository's reference baseline; [DAP implementation status](dap-implementation-status.md) records the delivered scope and evidence.

## Positioning Against Existing Standards

Reuse established architecture and requirements practices, and define the additional operating rules needed for skill-based execution. Distinguish a documentation model, a design method and an evaluation method; they solve different parts of the problem.

TOGAF provides an enterprise architecture methodology and framework. This project chooses a smaller solution-level workflow; that scope choice is not evidence that TOGAF cannot be tailored or is universally unsuitable. Source: https://www.opengroup.org/togaf

C4 provides architectural views. Its core diagrams describe static structure, while supporting diagrams include dynamic behavior and deployment. Use the views that answer stakeholder concerns; C4 is not itself the complete elicitation and governance workflow. Source: https://c4model.com/diagrams

arc42 provides twelve tailorable sections for architecture communication, including runtime behavior, deployment, quality requirements, decisions and risks. Maintain it throughout design rather than only exporting a finished result. Source: https://arc42.org/overview/

Attribute-Driven Design (ADD) is an established method for deriving architecture from functional needs, quality attributes and constraints. This framework combines such design practices with interviews, persistent records, explicit gates and an evidence-based evaluator. Its contribution is an operational integration, not the invention of requirements-driven architectural design. Source: https://www.sei.cmu.edu/library/attribute-driven-design-add-version-20/

The cited primary sources explain the roles of these approaches. The process rules, scoring formula and implementation contracts below are project-defined choices, not requirements imposed by those sources.

## Relationship to the SDLC

The architecture process runs side by side with the software development life cycle, not nested inside one of its boxes. The two tracks feed each other: SDLC stages hand inputs into the architecture process, and architecture decisions hand outputs back into SDLC stages, continuously rather than at one single handoff point.

The usual entry point is a requirement seed. Existing projects may enter through a change request, architecture review or operational finding. Preparation identifies the current baseline and resumes at the earliest stage affected by the change; it does not discard existing evidence.

## Process at a Glance

| Stage | Input | Activity | Output |
| --- | --- | --- | --- |
| 1. Requirements lifecycle | Raw need | Seed statement captured, positioned against the formal RE lifecycle | 2-3 line requirement seed |
| 2. Pre-interview preparation | Requirement seed, plus existing artifacts if any | Classify scope, inspect available evidence, calibrate questions and evaluate the existing baseline where present | Calibrated interview plan, gap report |
| 3. AI-driven interview | Calibrated plan | Iterative functional and quality-attribute elicitation using the project checklist and recorded evidence | Versioned requirement baseline, priorities, scenarios and convergence evidence |
| 4. Draft architecture | Converged requirements | Compare feasible alternatives and develop architecture views with linked decision records | Draft views and proposed ADRs |
| 5. Human review gate | Proposed ADRs, draft views and requirements | Apply explicit risk and authority rules; block affected decisions pending required human review | Review dispositions and eligible decisions |
| 6. Output artifact set | Reviewed decisions | Architecture description drafted, decisions cross-linked, traceability recorded in both directions; changes found mid-drafting routed back by the reopen rule | arc42 description, ADR log and RTM with durable supporting records |

## Stage 1: Requirements Lifecycle

Requirements do not arrive complete. They start as a brief seed statement - one or two lines, a high-level description of the solution wanted, covering only a fraction of what is actually needed. Everything else has to be drawn out afterward.

Requirements engineering includes discovering stakeholder needs, analysing and negotiating them, specifying requirements, validating them and managing change throughout the life cycle. The short seed starts this work; it is not a complete specification. The stages here are an operating model, not a verbatim lifecycle mandated by a standard.

Requirements and architecture are not strictly sequential even at this early point - there is a recognized concept of "architecture requirements", reflecting a growing realization that requirements cannot be fully specified without doing some design work alongside them. This is consistent with running the architecture process side by side with the SDLC rather than after it.

Reference: ISO/IEC/IEEE 29148:2018 defines requirements engineering processes and information items. This framework uses its published scope as a reference; a formal conformity claim would require a separate clause-level assessment against the licensed standard. https://www.iso.org/standard/72089.html

## Stage 2: Pre-Interview Preparation

Preparation starts with the seed and any available artifacts. It establishes scope, participants, evidence access, configuration and the next questions. Calibration continues when new stakeholders, constraints or uncertainties emerge; the process does not assume that preparation can eliminate later ambiguity.

- Mode classification - classify greenfield, brownfield or mixed scope from the seed and evidence; ask when unclear. Greenfield can still have enterprise constraints. Brownfield loads requirements, architecture, ADRs, RTM, operational evidence and prior evaluations where available. Record missing or stale evidence explicitly, evaluate the baseline, and assess the change plus its dependency closure.

- Technicality calibration - optionally ask the interviewee for a one-to-five self-rating and adapt vocabulary to their answers. Use business scenarios and plain-language trade-offs for nontechnical participants. Suggested defaults remain assumptions until confirmed by an authorised stakeholder; technical uncertainty goes to the relevant specialist rather than becoming an uninformed selection.

- Basic clarification - establish goals, scope, stakeholders, business criticality, mandatory constraints, available evidence and the decision owner. Persist the interview plan and open questions before proceeding. An unavailable owner or document is a recorded gap, not evidence of agreement.

## Stage 3: AI-Driven Interview Mechanism

Once the seed requirement lands, an interview phase expands it. This is one continuous interview, not two separate passes:

- Start with business outcomes, users, main functional flows and system boundaries. Raise architecture-driving quality attributes and constraints immediately when they can change those flows.

- Develop functional and non-functional requirements together as dependencies emerge. Cover failure behavior, security, privacy, accessibility, operations, integration and recovery as relevant to the system. Prioritise both requirement types for a named release or increment.

- Use an iterative clarification and validation loop. Ask a small batch of high-value questions, record answers and provenance, update the baseline, test assumptions against candidate designs, and checkpoint state. This is not reinforcement learning unless a separately specified training method actually changes a model or policy.

Research supports investigating AI-assisted elicitation, but individual experiments do not prove completeness or prescribe production stopping rules. The following distinctions govern how that evidence is used.

- LLMREI was evaluated in 33 simulated stakeholder interviews. Its reported elicitation results are evidence from that study setting, not a transferable completeness guarantee or a production approval threshold. Source: https://arxiv.org/html/2507.02564v1

- Targeted clarification - ask about an unresolved requirement, contradiction or evidence gap. Explain why the answer matters and record which baseline items it changes.

- Candidate design feedback - lightweight sketches or prototypes can expose missing requirements. Keep these hypotheses separate from accepted decisions and confirm derived requirements with the responsible stakeholder.

- Stopping behavior - use the explicit convergence and blocked-state rules below. A fixed number of rounds or a silent interviewee does not prove that the requirement set is complete.

- Human involvement - stakeholders validate intent and scope; designated reviewers handle decisions that meet escalation rules. The assistant can draft and analyse, but cannot manufacture approvals or infer consent from silence.

Research claims retained here are limited to the linked LLMREI study. Other examples from the initial draft are not relied on as evidence or as gate definitions without verification of their methods and applicability.

### Requirements Quality Checklist

The following is this framework's operational checklist, informed by requirements-engineering practice. It is not an exact list of eleven ISO/IEC/IEEE 29148 characteristics. Completeness applies to individual requirements as well as the set; correctness and conformity are checked explicitly below. Traceability, affordability and bounded scope are retained as project controls without mislabelling them as the standard's exact taxonomy.

| Characteristic | Meaning |
| --- | --- |
| Necessary | Has a justified stakeholder need, quality goal or binding constraint; optional value is still a valid need |
| Implementation free | States the needed outcome; a mandated implementation is recorded separately as a sourced constraint |
| Unambiguous | Interpretable in only one way; stated simply |
| Consistent | Does not conflict with another requirement or constraint; check relationships across the set |
| Complete | Defines enough conditions and behavior for the individual requirement; assess set coverage separately |
| Singular | States a single capability, characteristic, or constraint - not bundled |
| Feasible | Has credible feasibility evidence or a validation action; unsupported feasibility remains unresolved |
| Traceable | Has a stable ID, source and links into design and verification planning |
| Verifiable | Has a measurable acceptance criterion, method, owner and planned verification evidence |
| Affordable | Fits cost and effort constraints individually and in aggregate, with uncertainty recorded |
| Bounded | Has an explicit scope and delivery horizon; records dependencies and exclusions |

Also check correctness against the confirmed stakeholder intent and conformity to the agreed requirement format. A design-ready requirement has source, owner, priority, scope, acceptance criteria and status. Quality requirements use scenarios with stimulus, environment, affected part, expected response and a measurable response threshold. Missing evidence cannot be marked as passing.

### Convergence rule

Convergence is readiness for a defined scope and baseline, not proof that no future requirement will emerge. All three gates must pass on the same recorded baseline before it is labelled converged. Exploration may continue earlier, with provisional decisions clearly marked.

- Per-requirement gate - each in-scope active requirement passes necessity, outcome/constraint separation, unambiguity, individual completeness, singularity, correctness, conformity, feasibility, traceability, verifiability and bounded scope. Store pass, fail or unknown with evidence for each check; unknown is not pass.

- Set-level gate - validate consistency, stakeholder and scenario coverage, dependency closure, collective feasibility and affordability. Record justified exclusions and residual risks. An unaffordable individual requirement is also a problem; aggregation does not erase it.

- Stability gate - after the other checks pass, complete a confirmation round covering the agreed scope and unresolved items with the responsible stakeholders. It must produce no material addition, deletion or change, no unresolved blocking question, and an explicit baseline confirmation. Record participants, round ID and before/after baseline hashes. Silence, timeout or another LLM pass is not stakeholder confirmation.

Define a round as one question batch plus its received answers, baseline reconciliation and checkpoint. Configure maximum rounds or an elapsed-time budget. When the budget is reached, answers are unavailable or conflicts remain, persist status blocked with reasons, owner and next action; never force convergence. Any material baseline change resets stability evidence. These are framework-defined stopping rules, not an ISO-prescribed algorithm.

Reference: https://www.iso.org/standard/72089.html. This checklist is an implementation policy; the public catalogue does not establish a clause-level conformity mapping.

### Requirement Prioritisation and Exceptions

Apply MoSCoW to functional and non-functional requirements for an explicitly named timeframe. Priority is separate from applicability, acceptance status and an exception to a binding obligation. The four categories below describe delivery intent.

| Bucket | Meaning |
| --- | --- |
| Must have | Required for a viable and acceptable release within the stated scope |
| Should have | High priority, high value, but not critical to launch |
| Could have | Desirable if time/resources allow |
| Won't have this time | Agreed exclusion from this delivery timeframe; retained for scope control and later reassessment |

A Won't have classification is not a security, compliance or quality waiver. A permitted exception requires its own record: obligation, justification, approving authority, residual risk, compensating controls, expiry or review trigger, and affected baseline. The assistant cannot waive binding obligations. Unapproved or expired exceptions block affected decisions.

Do not convert MoSCoW categories into universal numerical weights. When comparing feasible options, define decision-specific criteria, scales and agreed weights separately. Must-have constraints are eligibility filters; a high aggregate score cannot offset a failed mandatory constraint.

Source: Agile Business Consortium, MoSCoW prioritisation. https://www.agilebusiness.org/resource/what-is-moscow-prioritization/

## Stage 4 Draft Architecture and Decisions

Develop the architecture views and proposed ADRs together. Identify the architecturally significant requirements, compare feasible alternatives, document trade-offs and validate high-uncertainty assumptions through analysis or prototypes. ADRs record reasoning; context, building-block, runtime and deployment views show how decisions work together.

Each architecturally significant decision has a stable ADR ID and owner, plus:

- A clear statement of the decision

- The context and problem being addressed

- Feasible alternatives considered, including a simpler option or the status quo where applicable

- Linked requirement and constraint IDs, decision criteria, evidence and uncertainty

- Implications and consequences

- Related decisions, dependencies, design-element links, review evidence and supersession links

- Status: proposed, accepted, rejected, deprecated or superseded; acceptance records authority and baseline

arc42 section 9 indexes the ADR log; the other views link to the decisions they realise. A draft or rejected ADR does not establish an approved baseline, and an ADR link without a path back to a justified requirement or constraint does not establish traceability.

Source: AWS Prescriptive Guidance, ADR process and lifecycle. https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html

## Stage 5: Human Review Gate

Use explicit, evidence-based review rules. Stakeholder confirmation validates requirements; architectural review evaluates decisions and their consequences. Reviewers see proposed ADRs together with the affected views, requirements, assumptions and verification plans.

Escalate irreversible or high-risk decisions, security/privacy/compliance implications, material cross-team impact, and cost above an explicitly configured threshold. Security review cannot be waived by a low score. A documented review of an unchanged reusable control may be referenced when its applicability is confirmed; new or changed implications require review.

Configuration specifies decision authority, risk categories, cost currency and time horizon, cross-team impact criteria, review ownership and escalation routing. Set values deliberately for the organisation and retain their version with the baseline.

- Thresholds are set explicitly and recorded as part of the framework configuration for that organisation, where the evaluator can read them.

- An unset relevant threshold or uncertain risk escalates the affected decision. Drafting and independent analysis may continue; implementation or acceptance dependent on that decision waits for the required disposition.

- Security, privacy and compliance implications always require an appropriate human review disposition. The framework does not invent legal applicability or allow an LLM to approve an exception.

Blocking review prevents acceptance and downstream use of affected decisions. An asynchronous queue allows independent work to proceed, with owner, due date and dependent items recorded; it is not automatic approval. On timeout, escalate or remain pending. Never send notifications without the user's authorisation and an available communication channel.

Use observable impact, reversibility, uncertainty and configured authority rules to select the review path. LLM self-reported confidence is commentary, not a calibrated probability or an approval gate. Low-risk acceptance is allowed only under an explicit human-approved delegation policy, with the policy ID and evidence recorded; otherwise obtain human acceptance.

These escalation rules are project policy. They complement the ADR review lifecycle described at https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html

## Stage 6: Output Artifact Set

The three primary deliverables are an architecture description, ADR log and RTM. Their supporting records are first-class durable state: requirements, sources, scenarios, assumptions, questions, interview checkpoints, configuration, approvals and exceptions. The primary documents alone cannot reconstruct missing interview or approval evidence.

- Architecture description - use the twelve arc42 sections as the default structure, adding only necessary appendices. Populate applicable sections with evidence-backed content; mark a genuinely inapplicable section with a rationale and owner rather than filling it with invented prose.

- ADR log - the reasoning layer underneath the description. arc42 holds these in its section 9 and cross-links them to the chapters where each decision shows up, which matches the intended model directly.

- Requirements Traceability Matrix - connect a confirmed source to a requirement or binding constraint, its design elements, significant ADRs where needed, and planned verification. Keep implementation and executed verification evidence separate so a design-complete chain is never presented as proof of delivery.

Traceability rule: every architecturally significant design element or assertion has a direct path, or a path through an ADR, to an approved requirement, sourced constraint or explicit risk/control need. An accepted risk/control need is registered as a requirement or constraint before baselining. An assumption is not approval. Define the element inventory before scoring; introductory prose and glossary definitions do not each need an ADR.

### Handling changes discovered mid-drafting

Requirement changes surface while the architecture is already being drafted, and the process needs a deterministic rule for where that change re-enters rather than leaving it to judgement. The rule is based on what the change invalidates, not on how many records it touches - counting touched ADRs measures volume rather than impact, and two independent decisions can matter far less than one decision the rest of the architecture rests on.

- Revise a proposed ADR while it is under discussion. For accepted or rejected ADRs, preserve the decision text; record editorial corrections as annotations and substantive changes in a new ADR with explicit supersession links and review. Never silently rewrite accepted reasoning.

- If evidence invalidates a requirement or constraint, return to Stage 3. If requirements remain valid but an architectural choice fails them, return to Stage 4 and then review. In both cases propagate impact through linked decisions, views and verification plans, and invalidate affected approvals and evaluations.

- A conflict with a Must have blocks the affected design. Determine whether the design is wrong or an authorised requirements change is needed; do not presume that the requirement is wrong or downgrade it automatically. Re-run the relevant gates and record the disposition.

Persist the change, affected IDs, reason for re-entry and baseline revisions. Continue unrelated work when dependencies permit. Superseded requirements and decisions remain discoverable, and the new baseline must reconcile the requirement set, views, ADRs and RTM before release.

### Authoring responsibility

The AI drafts and updates the description while responsible humans retain decision and requirement authority. Missing information becomes a targeted question with an owner and impact. Record unresolved items explicitly, distinguish working drafts from accepted baselines, and never present a placeholder as a completed section.

### Handoff and continuing ownership

At handover record one accountable artifact owner, the delivery maintainer and the architectural reviewer. Ownership is explicit even when multiple people contribute. Pending actions, approvals and the baseline revision travel with the handover.

- The architect owns the artifacts up to and through handover to the delivery team.

- After handover the delivery team owns day-to-day currency, while the architect remains a continuing reviewer rather than withdrawing.

The architect's continuing review is triggered two ways, and both are needed:

- Event-triggered - a change to requirements, decisions or solution evidence triggers impact assessment and proportionate review; editorial changes do not automatically reopen unrelated decisions.

- Periodic - a scheduled sweep that looks for outdated points nobody flagged, catching the drift that event triggers miss by definition.

The evaluator supports periodic review by identifying stale evidence and gaps. It does not run itself on a schedule: the organisation must name an owner and arrange manual or external scheduled execution. A missing cadence is a governance gap, not permission to fabricate a review.

## Part Two Implementation Approach

Implement this framework through skills, lightweight repository artifacts and validation scripts. A separate hosted agent platform, database or workflow service is not required. The host must support reading the skills and persisting the required records; capabilities and limitations are checked at startup.

The host supplies execution; files supply durable state. Skill instructions guide the model, while scripts validate structural rules and calculate scores from recorded assessments. Semantic judgments still require cited evidence and may require human review.

- Bootstrap each run from the current artifact manifest, configuration, requirements, architecture and checkpoint. If no checkpoint exists, reconstruct only what the evidence supports and label the remainder unknown. Starting at any stage does not authorise skipping its prerequisite gates.

- Persist draft requirements, answered questions, assumptions, interview rounds and gate results after each round and substantive change. Session memory may assist execution but is never the sole record of approvals, counters or decisions. Recovery reads the last valid checkpoint and verifies its referenced baseline.

Use portable SKILL.md entry points with concise instructions and on-demand references. Skill discovery and invocation vary by host, so compatibility must be tested rather than assumed. A host that cannot load another skill can follow an explicit documented invocation plan and report what actually ran. Specification: https://agentskills.io/specification

Write checkpoints atomically and use revision checks to avoid overwriting concurrent work. Record incomplete operations and validate the artifact manifest before resuming. If persistence is unavailable, report a non-resumable draft session and do not claim completion of persistence-dependent gates.

### Two skills, not one

Separate execution from process evaluation. In arch-skills, extend arch-orchestrator as the execution entry point and add arch-evaluate as the process evaluator. Reuse arch-decision, arch-doc and arch-governance; retain arch-review for design-quality assessment. This is the implemented reference integration; host-specific extensions remain separate.

- Execution skill - prepares the run, conducts the interview, coordinates only relevant specialists, maintains state, routes reviews and produces the primary artifacts. Existing standalone specialist requests remain available without imposing the entire workflow.

- Evaluation skill - inspects a frozen artifact baseline, produces evidence-linked findings, separate forward/backward traceability figures, dimension scores and a gate disposition. It does not repair the design or infer that a documented process event actually occurred without a record.

A separate skill creates role separation, not guaranteed independence or enforcement. A shared model can share the same blind spots. Use read-only evaluation of the assessed baseline, deterministic structural checks and human adjudication where necessary; enforce release rules through repository checks when configured.

### Internal and external auditing

Evaluation happens at two distinct levels, and they are not interchangeable.

- Internal auditing runs inside the execution skill, performed by the interviewer as it builds the architecture document. It is continuous and self-directed: checking requirements against the quality characteristics, tracking convergence, and catching gaps while the work is still forming.

- External auditing is an assessment pass separate from authoring. Freeze its input baseline, inventory evidence and gaps, and keep findings reproducible. The evaluator does not edit its assessed inputs; an explicitly authorised publishing step may write only generated evaluation output.

The evaluator can inspect an existing project without prior use of this framework. It reports artifact coverage and records absent process evidence as unknown or unproven. Missing historical records are not proof that an activity never happened, and inferred history must not receive verified credit.

Store evaluation data in a separate machine-readable report and include or link its generated summary in the architecture appendix. Record UTC timestamp, input manifest and hashes, framework/rubric/configuration versions, evaluator identity, findings and gate status. Exclude generated evaluation output from the assessed input hash to prevent self-invalidation; changes to any assessed input make the report stale. Audit-only mode returns the report without changing source artifacts.

### Scoring rubric

Score only evidence that can be assessed from the frozen baseline. Report process and artifact completeness separately from architectural fitness, approval status and implementation verification. The four dimensions below use the calculation contract at the end of this document.

- Requirements quality - evidence for the per-requirement checks, the set-level checks and the recorded stability round. A polished requirement sentence alone cannot establish stakeholder confirmation.

- Decision coverage - significant choices have complete ADRs, alternatives, consequences, evidence, owners and valid disposition. Trace links are checked in the traceability dimension to avoid counting the same metric twice.

- Traceability completeness - measured bidirectionally, as below. This is the backbone of the score.

- Artifact completeness - applicable arc42 sections and required supporting records contain meaningful, consistent content. A heading, unresolved placeholder or circular link is not completion; a justified inapplicability is reported separately.

Traceability measures the declared scope, not undiscovered requirements. Freeze the active requirement and design-element inventories before calculating coverage. Resolve stable IDs and semantic relationships rather than awarding credit merely because a URL or ID appears.

- Forward traceability - the percentage of active in-scope requirements with a confirmed source, at least one design mapping and a verification plan. Add an ADR link when the mapping embodies a significant choice. Report implementation and executed-verification coverage separately, only when actual evidence is available.

- Backward traceability - the percentage of inventoried significant design elements with a valid direct path, or a path through ADRs, to active requirements or binding constraints. Unjustified elements remain visible as scope or rationale gaps.

Always show forward and backward numerators, denominators, percentages and uncovered IDs separately. For the overall completeness calculation only, use the lower percentage as the traceability dimension. This conservative project rule prevents a strong direction from concealing a weak one.

### Positioning against architecture evaluation standards

Process completeness and design fitness answer different questions. Do not present this rubric as certification, as an architecture-quality score or as a substitute for expert evaluation.

ISO/IEC/IEEE 42030 provides an architecture evaluation framework. This project has a narrower operational focus on evidence, process records and artifact completeness, and makes no claim of conformity to that standard. Source: https://www.iso.org/standard/73436.html

ATAM examines architectural decisions and quality-attribute trade-offs. Use design review, analysis, prototypes and testing where needed to assess whether the architecture can meet its requirements. Source: https://www.sei.cmu.edu/library/atam-method-for-architecture-evaluation/

A high completeness score can coexist with an unsuitable design. Conversely, a capable design may lack evidence needed for this process baseline. Report these findings separately; only actual verification supports claims about delivered system behavior.

Reference boundary: the project rubric below is original operating policy. ISO/IEC/IEEE 42030 and ATAM provide context for design evaluation, not the formula or acceptance thresholds used here.

### The evaluator feeds preparation

Preparation invokes evaluation on the available baseline for brownfield and mixed-scope work, then uses findings to target questions. Evaluation is non-recursive: it reports missing artifacts rather than calling the execution skill to invent them. If it is unavailable, preparation records that limitation and can gather information, but cannot claim the external assessment passed.

### Versioning the framework

The framework changes as it is used, and a score produced under one version is not comparable to a score produced under another. Versioning is therefore part of the output, not an administrative detail.

- Execution and evaluation declare compatible framework, schema and rubric versions. Validate compatibility at runtime and in tests; sharing a version label alone cannot prevent implementation drift. Store immutable rubric definitions for every supported release.

- Use a major framework version change for incompatible gates, artifact contracts or scoring semantics; use minor versions for backward-compatible guidance and examples; use patches for non-semantic corrections. Also version the schema, rubric and configuration explicitly. A scoring bug fix retains its provenance and requires recalculation when it changes results.

- Record exact versions and the assessed artifact manifest in each report. Scores are comparable only with equivalent scope, evidence stage, applicability decisions, rubric and weights; equal framework versions alone are insufficient.

- For an older baseline, evaluate under its recorded rubric only when that rubric is available. Otherwise report historical assessment unavailable and offer a separately labelled current-version gap assessment. Do not fabricate a historical score or invalidate an old approval simply because the current framework differs.

Skill packaging reference: https://agentskills.io/specification. Persistence, gate enforcement and score reproducibility are implementation responsibilities defined by this framework, not guarantees supplied by a skill file.

## Organisational Configuration

Record configuration in a versioned project file with provenance and approving authority. Missing configuration has a scoped consequence: missing decision authority or risk criteria block affected acceptance; missing weights prevent an overall score; missing review cadence prevents governance readiness. Information gathering and partial dimension reporting can continue.

- Review configuration - cost threshold with currency and horizon, cross-team impact rule, risk categories, reviewer roles, asynchronous queue owner and due-time rules, and any delegated low-risk authority. Security, privacy and compliance review remains mandatory when implicated.

- Operations configuration - artifact owner, periodic review cadence, run scope, evidence-retention rules and interview round/time budget. Name who invokes periodic reviews; skills alone provide no scheduler.

- Scoring configuration - four explicit non-negative weights summing to 1, with traceability the largest weight. Do not silently invent defaults. A worked example may use requirements 0.25, decisions 0.20, traceability 0.35 and artifacts 0.20, but an organisation must explicitly adopt a configuration before an overall score is published.

Validate configuration and version compatibility before use. Record unconfigured values and their exact effects; never substitute assumptions that make a gate pass. The following contract makes the implementation and its acceptance tests concrete.

## Implementation Contract

This contract is normative for framework version 1.0.0. Repository implementation is recorded in docs/dap-implementation-status.md. No new agent service or cloud infrastructure is required.

### Durable records and identifiers

Use stable IDs for requirements (REQ), constraints (CON), design elements (DES), decisions (ADR), questions (Q), assumptions (ASM), exceptions (EXC) and verification items (VER). A record carries status, owner, source, revision and links. Preserve IDs across edits and retain superseded records. Traceability is a graph; the RTM is a readable projection of its typed links.

A requirement records its statement, type, source and source revision, stakeholder owner, priority, delivery scope, acceptance criteria, verification method/owner, dependencies and lifecycle status. Quality scenarios additionally record stimulus, environment, affected element, expected response and measurable threshold. An assumption records impact and a validation owner or trigger; it is never silently promoted to a confirmed requirement.

The checkpoint records run ID, active stage, mode, framework/schema versions, input manifest, baseline revision, current requirements, answered and pending questions, round count, gate evidence, pending reviews and next action. Record answers and reconciled state atomically after each round. Do not persist credentials or unnecessary sensitive interview content.

### Gate outcomes and transitions

Use pass, fail, unknown and not-applicable for individual checks. Not-applicable requires a reason and an authorised applicability decision; it is not a waiver of a required gate. A run is draft, blocked, ready-for-review or baselined. Baselined requires all applicable convergence checks, required reviews, valid configuration, current evaluation and structural integrity to pass. An overall completeness score never overrides a failed gate.

Baseline readiness additionally requires every active in-scope requirement to have a design mapping and verification plan, every significant design element to have justified scope, every significant decision to have a valid disposition, and all applicable artifact content checks to pass. Open blocking risks, unapproved exceptions or conflicting mandatory constraints prevent readiness regardless of score. Use the same frozen input manifest for the readiness report and its publication; record publication metadata outside that manifest.

Resume preparation from the last verified checkpoint. Requirements changes return to elicitation; design-only defects return to design; approval changes return to review. Any affected downstream evidence becomes stale. Missing persistence, unknown risk or incomplete review prevents the dependent transition without preventing independent draft work.

### Reproducible scoring

Version the complete criterion catalogue before scoring. Enumerate every assessed check with ID, dimension, target ID, applicability, result, evidence locator and reviewer rationale. Include fail and unknown checks in the denominator with zero credit; pass receives one. Approved not-applicable checks are excluded and listed with reasons. No fractional credit is used. Structural checks run in code; semantic assessments remain explicit evidence-backed judgments.

Requirements quality Q = 100 × passed applicable requirement-quality checks / all applicable requirement-quality checks. Expand the eleven per-requirement checks in Stage 3 for each active in-scope requirement, the five set-level checks once per baseline, and the stability gate once per baseline. A required empty requirement inventory is a structural failure, not vacuous success.

Decision coverage D uses ten checks for each inventoried significant decision: a uniquely identified ADR with owner, decision statement, context, alternatives, criteria, evidence and uncertainty, consequences, dependency disposition, lifecycle status, and valid review/authority disposition. D = 100 × passed applicable checks / all applicable checks. A missing ADR fails all ten checks for that decision; derive the inventory from the design as well as the ADR log so omissions cannot disappear from the denominator.

Forward coverage F = 100 × requirements with a complete design-stage trace chain / active in-scope requirements. Backward coverage B = 100 × justified significant design elements / inventoried significant design elements. Require existing IDs, valid statuses, source support, design mappings and planned verification, with an ADR for significant choices. A broken, superseded-only, circular or semantically unrelated chain fails. Traceability T = min(F, B), while F and B are always displayed separately.

Artifact completeness A assigns three checks to each applicable arc42 section: substantive scoped content, supporting evidence or justified decisions, and consistency with related records. Also assign three checks to each required supporting record group: presence, valid schema and current baseline linkage. Supporting groups are requirements/constraints, ADR index, trace graph/RTM, scenarios/verification plans, questions/assumptions, checkpoint/history, configuration, and reviews/exceptions. A = 100 × passed applicable checks / all applicable checks. A placeholder fails substantive content; a legitimate empty group needs an explicit none-applicable assertion and evidence.

Overall S = wQ×Q + wD×D + wT×T + wA×A, where configured weights sum to 1 and traceability has the largest weight. Calculate with full precision and round only displayed percentages to one decimal place. If a required population is empty, the required inventory is unavailable, weights are invalid or any necessary dimension is not assessable, show the affected metric and S as not assessable and report the gate failure. Never renormalise weights silently or turn a zero denominator into 100%.

Worked example, not an adopted configuration: Q=80, D=75, F=90, B=60 and A=100 gives T=60. With weights 0.25, 0.20, 0.35 and 0.20, S=76.0%. A pending security review still blocks the baseline even with that score. If evidence confirms a check failed, it scores zero; if the input population itself is unavailable, the affected dimension cannot be calculated.

The report lists all counts, excluded checks, unresolved findings, uncovered IDs, gate failures and unknown evidence. Repeatability applies to calculation from the same assessments and frozen inputs. Independent semantic assessment can differ; preserve disagreements and reviewer rationale rather than implying mathematical certainty about judgment.

### Evaluation freshness and publishing

Build an input manifest from the explicit assessed file set, configuration and rubric. Specify normalisation and hashing rules in the implementation. Exclude evaluation reports and the generated appendix from the hash. Persist both input and publication revisions; publishing a report does not alter its assessed baseline. Mark reports stale after any assessed requirement, ADR, design, review or configuration change, even when the architecture prose is unchanged.

### Repository integration and delivery order

Use skills/arch-orchestrator as the execution entry point, skills/arch-evaluate as the new evaluator, and shared references, schemas and scripts for versioned contracts. arch-doc provides arc42 output, arch-decision manages ADR/DAR work, arch-governance defines review policy, and arch-review remains the design-quality reviewer. Adapt the existing 22-section architecture template through an explicit mapping to arc42; preserve useful content and standalone specialist behavior.

The reference implementation covers shared contracts and configuration, durable artifact records, interview and design integration, review/change handling, deterministic scoring, evaluator/report publishing, brownfield/resume scenarios, and compatibility documentation. [DAP implementation status](dap-implementation-status.md) records the delivered task mapping and verification evidence. Tests cover happy paths and failed gates, including missing evidence, no response, invalid weights, stale reports, concurrent updates and interrupted sessions.
