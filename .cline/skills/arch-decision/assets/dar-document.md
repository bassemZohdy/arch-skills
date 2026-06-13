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

| ID | Gate Criterion | Rationale | Status |
|----|----------------|-----------|--------|
| G1 | [Must X] | [Why this is required] | Pass/Fail |
| G2 | [Must not X] | [Why this is excluded] | Pass/Fail |

**Exemptions:**
| Alternative | Gate | Exemption Rationale |
|-------------|------|---------------------|
| [Do Nothing] | [Gate ID] | [Why exempt] |

---

## 3. Alternatives Considered

| ID | Alternative | Description | Gate Status |
|----|-------------|-------------|-------------|
| A1 | [Name] | [Brief description] | Passed/Failed |
| A2 | [Name] | [Brief description] | Passed/Failed |
| DN | Do Nothing | Status quo baseline | Exempt |

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
| **Status** | Approved / Deferred |
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

```json
{
  "document_id": "DAR-YYYY-MM-DD-slug",
  "status": "approved",
  "mode": "formal",
  "decision_statement": "...",
  "scored_criteria": [
    {"id": "C1", "name": "...", "weight": 25}
  ],
  "scores": {
    "A1": {
      "C1": {"raw": 4, "weighted": 1.0, "confidence": "high", "rationale": "..."}
    }
  },
  "total_scores": {"A1": 4.0, "A2": 3.5},
  "ranking": ["A1", "A2"],
  "sensitivity": {
    "gap_top2": 0.5,
    "scenarios": [
      {"id": "A", "ranking_change": false}
    ]
  },
  "recommendation": "A1"
}
```
