# Evaluation contract

Read the packaged framework/records.md and project-schema.json for exact inputs,
checkpoint shape and authority records. Supported versions are framework 1.0.0,
schema 2.0.0 and rubric 1.0.0; historical incompatible scoring is unavailable.

Q expands eleven checks per in-scope active requirement, five set checks and one
stakeholder stability check. D expands ten per significant decision, including
missing ADRs identified by the design inventory. A expands three per applicable
arc42 section and supporting record group. Assessment IDs bind target, criterion,
dimension, baseline/hash, assessor, rationale and frozen evidence.

Fail/unknown remain in the denominator with zero credit. Authorized N/A exclusions
are visible and cannot waive mandatory gates. Empty required populations prevent
an overall score. Never accept anonymous one-row summaries as complete catalogues.

F counts confirmed-source → REQ → DES/accepted ADR → VER plan chains. B counts
significant DES elements justified by active REQ or sourced CON, directly or
through accepted ADRs. Validate typed IDs, statuses and semantic evidence. Show
both counts and uncovered IDs; T=min(F,B). Planned verification is not delivery
evidence. Use the same graph for the generated RTM.

S=wQ×Q+wD×D+wT×T+wA×A, with explicitly approved nonnegative weights summing to one
and traceability largest. Calculate using exact fractions; round only display.

Readiness requires convergence, current reviews, valid configuration, structural
integrity, complete trace chains, valid decision dispositions, substantive
artifacts and freshness. Mandatory security/privacy/compliance implications
cannot be disabled by configuration. Unknown policy and unresolved blocking
risks, questions or exceptions prevent acceptance independently of S.

Evaluate one explicit snapshot containing assessments, config, schema and rubric.
Report evidence gaps and version/config identity. Generated outputs do not affect
their own input hash. Publishing archives immutable reports and separate summary
files; linking that summary is an authorized documentation operation, not an
audit-side source repair. Read-only evaluation never manufactures missing records.

