# DAP records and runtime contract

Supported execution contract: framework 1.0.0, schema 2.0.0, rubric 1.0.0.
Schema 2 corrects the incomplete earlier wire format; it does not invent new
normative DAP gates. Old examples are historical inputs, not ready baselines.
Migrate explicitly and obtain fresh evidence; never manufacture historical approval.
For an authorized real-project migration, follow [schema-2 migration](schema-2-migration.md).

## Artifact layout

An assessed project has an explicit process/manifest.json with a unique files
array. Include these files and every local evidence artifact cited by assessments:

- architecture.md (twelve arc42 sections by default)
- sources.json, requirements.json, constraints.json
- design-elements.json, decisions.json, verification.json, traceability.json
- process/config.json, process/state.json, process/assessment.json
- process/reviews.json, process/exceptions.json
- process/questions.json, process/assumptions.json, process/history.jsonl

The evaluator additionally snapshots the manifest itself, the installed schema
and rubric, and an external configuration if supplied. Undeclared files do not
affect evaluation. Evidence must resolve within the frozen set; capture external
evidence with its original URL, version and provenance instead of assuming a
live page is immutable. Do not put credentials into evidence records.

## Record schemas and identifiers

project-schema.json is the structural source of truth. Collections are arrays.
SRC, REQ, CON, DES, ADR, VER, Q, ASM and EXC IDs are typed and globally unique.
Records carry owner, source/source_revision, revision, baseline_revision and
status. Preserve superseded records; active records belong to the candidate.

Sources require confirmed provenance and evidence. Requirements have a named
scope, priority, acceptance criteria, verification IDs and dependencies. Quality
requirements also contain stimulus/environment/element/response/threshold.
Constraints record whether they bind the design and whether a human policy may
permit an exception. Priority is not authority to waive an obligation.

Significant designs declare whether a decision is required and list decision IDs.
Inventory significant assertions as well as named components. Missing ADR IDs
remain in the decision denominator rather than disappearing. ADRs record context,
alternatives, criteria, evidence, uncertainty, consequences, dependencies,
supersession and disposition. Significant proposals cannot become accepted through
a generated score. DES and ADR implications explicitly classify security, privacy,
compliance, reversibility, high risk, cross-team impact and cost/currency/horizon.

Verification records include method, acceptance threshold, environment, owner and
protected targets. Planned is distinct from passed/failed execution; executed
results need evidence. Questions/assumptions carry owner, impact and blocking
status. Exceptions carry obligation, residual risk, compensating controls,
authority, expiry and evidence. Non-waivable obligations cannot be excepted.

## Typed graph

Every link has from, to, type, rationale and evidence. Supported types are listed
in project-schema.json. Source links establish requirement/constraint provenance.
Requirement/constraint-to-design links or paths through accepted ADRs justify
design scope. A significant choice also needs the relevant accepted ADR path.
DES-to-VER links must agree with verification targets and requirement plans.
Reverse edges are optional; coverage is derived from the same semantic graph.
Superseded-only, dangling and circular-only paths cannot establish justification.
The generated RTM is a projection under evaluations/, not a second source of truth.

## Checkpoint and transitions

process/state.json uses {revision, state, state_hash}. state_hash is SHA-256 of
canonical sorted compact UTF-8 JSON plus newline. Use the checkpoint helper
with an explicit expected revision. Exclusive lock plus atomic replacement
prevents two cooperating writers from committing the same revision. A leftover
lock after interruption requires inspection and deliberate recovery, not timeout
approval or automatic deletion.

State records run_id, stage, mode, versions, baseline_revision, round,
elapsed_minutes, answered_questions, pending_questions, gate_results,
pending_reviews, next_action, subject_hash, stability, blocking_findings,
mandatory_conflicts and incomplete_operations. Stability records confirmed,
participants, round_id, before_hash, after_hash and evidence. Its hashes cover
requirements, constraints and sources; participants include requirement owners.

A subject hash binds substantive assessed files and contract versions. Checkpoint,
review, assessment, history, exceptions and manifest-control files are excluded
from the subject hash to avoid circular signatures, but included in the full
input manifest and freshness checks. Reconcile changes and record new dispositions;
do not copy old signatures onto changed evidence.

Interview mode stops at the requirements handoff. Create/update use the same
execution engine. Requirement changes re-enter interview, design changes re-enter
design, authority changes re-enter review. Propagate dependency impacts and
reassess the full candidate. Scripts do not conduct interviews or grant approval.

## Assessments and human reviews

process/assessment.json has requirements_quality, decision_coverage and
artifact_completeness arrays. Generate expected IDs from the rubric:
dimension:target_id:criterion. Each check also names dimension, target_id,
criterion, result, baseline_revision, subject_hash, assessor, evidence (locator
array) and rationale. Missing checks are unknown, duplicates/foreign checks
invalid. N/A requires reason, authorized_by and authorization_evidence, and cannot
waive mandatory convergence. No semantic truth is inferred from file existence.

Q expands eleven checks per active in-scope requirement plus five set checks and
one stability check. D expands ten per significant inventoried decision. A expands
three per arc42 section and three per supporting group. Scope and delivery
exclusions remain explicit. Empty required populations prevent S. Exact rational
arithmetic computes S; only display is rounded.

Use numbered level-two headings in architecture.md (1 through 12). Passing arc42
checks cite the matching section's exact heading, for example
architecture.md#3. Context and Scope. Empty/TBD sections, unrelated headings and
generated evaluation content cannot establish section completeness.

process/reviews.json is a list of dispositions with id, kind, targets, status,
reviewer, baseline_revision, subject_hash, reviewed_at, expires_at and evidence.
Kinds include architecture, security, privacy, compliance, irreversible,
high_risk, cross_team and cost. Reviewers must match the configured authority map.
All significant accepted decisions require architecture disposition; implications
add mandatory reviews. This implementation conservatively requires human reviews;
it does not auto-accept under a low-risk delegation. Unset policy escalates.
Recorded identities are assertions to adjudicate, not cryptographic authentication.

config.example.json is intentionally unapproved: complete its empty ownership and
evidence fields and explicitly adopt weights/thresholds. Missing policy blocks
readiness; invalid weights prevent S but do not suppress independent findings.

## Freshness and publication

Hash raw bytes for assessed files, except architecture.md: exclude one region
between DAP EVALUATION BEGIN/END HTML comment markers and normalize trailing
whitespace. Generated evaluations/ output is excluded entirely. Input changes,
including assessment, review, external config, rubric and schema changes,
invalidate reports. Calculation consumes one byte snapshot and checks it again
before claiming current results.

The publisher writes immutable timestamp/UUID reports and Markdown summaries
under evaluations/, then promotes latest.json after checking freshness.
Only the canonical latest destination is accepted; source overwrite is refused.
arch-doc can link the generated summary in its appendix. Publishing is explicitly
authorized and separate from read-only assessment. A failed assessment may be
published as blocked; publication is not architecture approval.
