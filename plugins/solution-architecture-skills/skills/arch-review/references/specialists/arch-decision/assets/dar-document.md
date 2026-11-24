# Decision Analysis and Resolution (DAR) — Formal Mode

**Document ID:** DAR-[YYYY-MM-DD]-[short-slug]
**Date:** [date]
**Mode:** Formal
**Status:** Draft | Approved | Deferred

---

## 1. Decision Frame

| Field | Value |
|-------|-------|
| **Decision Statement** | [One clear sentence] |
| **Scope** | [In scope] / [Out of scope] |
| **Constraints** | [Hard limits] |
| **Assumptions** | [Believed true but uncertain] |
| **Decision Owner** | [Name/Role] |
| **Approver(s)** | [Names] |
| **Deadline** | [Date] |
| **Review Triggers** | [Conditions to revisit] |

---

## 2. Gate Criteria

| Alternative | Gate ID | Mandatory condition | Evidence/date | Pass / Fail / Unknown | Disposition |
| --- | --- | --- | --- | --- | --- |
| [A1] | [G1] | [Condition] | [Source] | [Status] | [Eligible / excluded / pending] |

Apply every gate to every alternative, including a status-quo baseline. Unknown
is pending evidence, not a pass. Record non-applicability only with rationale and
authority; do not grant automatic exemptions to mandatory requirements.

---

## 3. Alternatives Considered

| ID | Alternative | Description | Gate Status |
|----|-------------|-------------|-------------|
| A1 | [Name] | [Brief description] | Passed/Failed |
| A2 | [Name] | [Brief description] | Passed/Failed |
| DN (optional) | Do nothing / defer | Explain relevance or infeasibility | Apply the same gates |

---

## 4. Evaluation Criteria (Scored)

| ID | Criterion | Weight | What 5 Looks Like | What 1 Looks Like |
|----|-----------|:------:|-------------------|-------------------|
| C1 | [Criterion] | [W] | [Best case] | [Worst case] |
| C2 | [Criterion] | [W] | [Best case] | [Worst case] |
| **Total** | | **100** | | |

---

## 5. Evaluation Matrix

| Alt | C1 (W=[W]) | C2 (W=[W]) | Total | Rank |
|-----|------------|------------|-------|------|
| A1 | [S] ([W]) [R] [C] | [S] ([W]) [R] [C] | [T] | [R] |
| A2 | [S] ([W]) [R] [C] | [S] ([W]) [R] [C] | [T] | [R] |

**Legend:** S=Score, W=Weighted, R=Rationale, C=Confidence (H/M/L)

---

## 6. Sensitivity Check

**Gap between top 2:** [Gap]

**Ranking Stability:**

| Scenario | Change | New Ranking | Ranking Changed? |
|----------|--------|-------------|------------------|
| A: W1 -10, W2 +10 | [Details] | [New order] | Yes/No |
| B: W1 +10, W2 -10 | [Details] | [New order] | Yes/No |

**Assessment:** [Stable/Unstable] — [Explanation]

---

## 7. Recommendation

**Recommended Alternative:** [A1/A2/Defer]

**Rationale:**
[Why this alternative scores highest, qualitative factors]

**Key Tradeoffs:**
- vs. [Second-ranked]: [Key differences]

**Risks:**
| Risk | Impact | Mitigation |
|------|--------|------------|
| [Risk 1] | [Impact] | [Mitigation] |

**Assumptions That Would Invalidate:**
- [Assumption 1]
- [Assumption 2]

**Review Triggers:**
- [When to revisit]

---

## 8. Decision

| Field | Value |
|-------|-------|
| **Status** | Proposed / Approved / Deferred |
| **Selected Alternative** | [ID] |
| **Decision Date** | [Date] |
| **Decision Owner** | [Name] |
| **Approvers** | [Names] |

---

## Appendix A — Evidence Log

| Criterion | Evidence Source | Date | Confidence |
|-----------|-----------------|------|------------|
| [C1] | [Source] | [Date] | H/M/L |

---

## Appendix B — Machine-Readable JSON Summary

The following is a synthetic, internally consistent arithmetic example. Replace
all IDs, criteria, scores and evidence before use; it conveys no approval.
Weights and shifts are percentage points. Round displayed values to two decimals
with half-up rounding; calculate totals and rankings from unrounded products.

```json
{
  "document_id": "DAR-EXAMPLE",
  "status": "draft",
  "mode": "formal",
  "decision_statement": "Synthetic comparison only",
  "scored_criteria": [
    {
      "id": "C1",
      "name": "Workload fit",
      "weight": 60
    },
    {
      "id": "C2",
      "name": "Operating effort",
      "weight": 40
    }
  ],
  "scores": {
    "A1": {
      "C1": {
        "raw": 4,
        "weighted": 2.4
      },
      "C2": {
        "raw": 5,
        "weighted": 2.0
      }
    },
    "A2": {
      "C1": {
        "raw": 3,
        "weighted": 1.8
      },
      "C2": {
        "raw": 4,
        "weighted": 1.6
      }
    }
  },
  "total_scores": {
    "A1": 4.4,
    "A2": 3.4
  },
  "ranking": [
    "A1",
    "A2"
  ],
  "sensitivity": {
    "gap_top2": 1.0,
    "scenarios": [
      {
        "id": "A",
        "source_criterion": "C1",
        "target_criterion": "C2",
        "shift": 10,
        "adjusted_weights": {
          "C1": 50,
          "C2": 50
        },
        "total_scores": {
          "A1": 4.5,
          "A2": 3.5
        },
        "ranking": [
          "A1",
          "A2"
        ],
        "ranking_change": false
      },
      {
        "id": "B",
        "source_criterion": "C2",
        "target_criterion": "C1",
        "shift": 10,
        "adjusted_weights": {
          "C1": 70,
          "C2": 30
        },
        "total_scores": {
          "A1": 4.3,
          "A2": 3.3
        },
        "ranking": [
          "A1",
          "A2"
        ],
        "ranking_change": false
      }
    ]
  },
  "recommendation": "A1"
}
```
