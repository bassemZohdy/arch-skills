# Explicit migration from schema 1

Use this guide only when the user authorizes migration of a real architecture
project. A process audit alone does not authorize changing it. There is no
automatic migration or transfer of approvals in the current runtime.

## Preserve the original

Keep the source baseline, checkpoint, reports, configuration and evidence unchanged
in a recoverable version or separate archive. Choose a new candidate directory and
record its relationship to the old baseline. Record the previous versions and
which historical rubric/runtime, if any, is available. Do not present a new score
as a recalculation under an unavailable old rubric.

## Reconstruct only evidenced records

Use project-schema.json and records.md from this package as the current wire
contract. Preserve stable IDs wherever their meaning is unchanged; document any
ID remapping rather than reusing an old ID for a new meaning.

| Older input | Current candidate treatment |
| --- | --- |
| Unstructured provenance | Create SRC records from captured source evidence; keep unconfirmed sources unconfirmed |
| Embedded constraints | Register CON records with scope, binding/waivable classification and named authority |
| Requirements without verification records | Create VER plans with method, environment, threshold, owner and targets; do not mark planned tests passed |
| Component/ADR lists and loose links | Inventory DES/ADR records and typed evidence-backed relationships; retain missing decisions as gaps |
| Anonymous score summaries | Do not import as passing checks; expand current Q/D/A criterion IDs and reassess against current evidence |
| Flat checkpoint or unverified hash | Reconstruct a current state from confirmed history, recording lost/unproven state and the next action |
| Historical approval | Preserve as historical evidence; obtain current authorized disposition when scope, policy or subject changes |
| Implicit file discovery | Create an explicit assessed manifest including all required records and captured local evidence |

Do not use the synthetic test generator or its bind_project helper on real data.
It deliberately supplies fictional judgments for tests, not a migration service.
Do not fill absent owners, risk classifications, policy, confirmations or reviews
with guesses to satisfy the schema. Record gaps separately while reconstructing
the candidate. An unsupported or incomplete candidate remains unassessable/blocked.

## Reassess and hand off

Adopt configuration deliberately with its authority and evidence. Bind assessments
and human dispositions to the new candidate subject hash after reviewing their
actual content. Use the checkpoint helper with an expected revision; never copy a
stale subject hash onto changed data. Renew the requirement stability confirmation
when material requirements or constraints have changed.

Evaluate the complete candidate using dap_validate.py from the installed package.
Readiness requires all applicable gates, not just a high score or valid JSON.
Record uncovered IDs, missing evidence, pending owners and next actions. Publish
only generated outputs when authorized. Retain the previous baseline and label
the new result as a current-version assessment; do not erase historical decisions.
