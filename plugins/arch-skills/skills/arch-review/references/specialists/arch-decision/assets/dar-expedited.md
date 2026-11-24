# Decision Analysis and Resolution (DAR) — Expedited Mode

Lightweight DAR for reversible, low-risk, or time-boxed decisions. Use Formal Mode (`dar-document.md`) when the decision is hard to reverse, crosses trust boundaries, or has high cost/impact.

**Document ID:** DAR-[YYYY-MM-DD]-[short-slug]
**Date:** [date]
**Mode:** Expedited
**Status:** Draft | Approved

---

## 1. Decision

| Field | Value |
|-------|-------|
| **Decision Statement** | [One clear sentence] |
| **Decision Owner** | [Name/Role] |
| **Reversibility** | Easily reversible / Hard to reverse |
| **Deadline** | [Date] |

---

## 2. Alternatives

| ID | Alternative | Notes |
|----|-------------|-------|
| A1 | [Option] | [Brief rationale] |
| A2 | [Option] | [Brief rationale] |
| DN | Do Nothing | Status quo baseline |

---

For a scored expedited comparison, record criterion IDs, weights totaling 100,
raw scores, rationale and totals using the formal template's JSON summary. For
a qualitative decision, state that no arithmetic validation was performed.
Apply hard gates to every option; include defer only when meaningful.

## 3. Recommendation

**Recommended Alternative:** [A1/A2/Defer]

**Rationale (≤ 3 bullets):**
- [Why — main driver]
- [Key tradeoff accepted]
- [Risk accepted and why it's tolerable]

**Review Trigger:** [Condition that forces a revisit, e.g. "adoption < 50% in 90 days"]

---

## 4. Approval

| Field | Value |
|-------|-------|
| **Approved By** | [Name] |
| **Date** | [Date] |
