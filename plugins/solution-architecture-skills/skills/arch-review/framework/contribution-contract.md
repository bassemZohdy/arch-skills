# Specialist contribution contract

Apply only when a specialist participates in a DAP run. Standalone questions,
diagrams, ADRs and focused reviews retain the user's narrower scope.

## Inputs

Receive task scope, run/mode/stage, candidate revision and subject hash, applicable
contract versions, REQ/CON IDs and source revisions, current DES/ADRs, quality
scenarios, protected decisions, available evidence and configured human authority.
Ask or record a scoped gap if needed inputs are absent. Do not invent a baseline.

## Outputs

Return findings with stable IDs, target IDs, evidence locators, rationale,
uncertainty, severity and owner. Separate observations, assumptions and proposals.
Provide proposed DES/ADR relationships, alternatives, consequences and applicable
review needs. Do not silently edit accepted records or claim approval.

For each verification proposal provide VER ID, protected REQ/CON/DES/ADR IDs,
method, measurable acceptance condition, environment, owner and lifecycle status.
Leave evidence empty while planned. Record actual execution evidence separately.
Return affected dependencies, newly stale approvals/assessments, open Q/ASM items
and next action. Use complete-for-assigned-scope, provisional or blocked, never a
library-wide readiness claim from one specialist contribution.

Populate only applicable record types. Unsupported defaults remain assumptions.
Human approval stays with the configured authority. A generic tool example is
neither a mandated technology nor authorization to install, deploy or execute it.

## Packaging

The builder copies this canonical contract and schemas into every installed
package. Resolve framework and shared `scripts/dap*.py` helpers from the outer package root, including
when reading a bundled specialist. Resolve a specialist's references/assets from
its resource_root in package-catalog.json; resolve skill-local helpers such as
the decision math validator from that same resource root. Related skill names
are optional handoffs, not recursive invocation requirements. If a selected
expert installation lacks a specialist, use existing evidence or state the gap.
Do not require a host-specific API,
global installation path or another package unless explicitly declared.
