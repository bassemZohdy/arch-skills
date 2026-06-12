# DAR Test Document

**Document ID:** DAR-2026-06-12-test
**Date:** 2026-06-12
**Mode:** Formal
**Status:** Draft

## 1. Decision Frame

| Field | Value |
|-------|-------|
| **Decision Statement** | We need to decide between PostgreSQL and MongoDB for our user store |
| **Scope** | User authentication and profile data |
| **Constraints** | Must be SOC 2 compliant |
| **Decision Owner** | Tech Lead |

## 2. Evaluation Criteria

| ID | Criterion | Weight |
|----|-----------|:------:|
| C1 | Security & Compliance | 30 |
| C2 | Performance | 25 |
| C3 | Scalability | 25 |
| C4 | Cost | 20 |
| **Total** | | **100** |

## 3. Evaluation Matrix

| Alt | C1 (W=30) | C2 (W=25) | C3 (W=25) | C4 (W=20) | Total |
|-----|-----------|-----------|-----------|-----------|-------|
| PostgreSQL | 5 (1.50) | 4 (1.00) | 3 (0.75) | 4 (0.80) | 4.05 |
| MongoDB | 4 (1.20) | 3 (0.75) | 5 (1.25) | 3 (0.60) | 3.80 |

## Appendix B — Machine-Readable JSON Summary

```json
{
  "document_id": "DAR-2026-06-12-test",
  "status": "approved",
  "mode": "formal",
  "decision_statement": "We need to decide between PostgreSQL and MongoDB for our user store",
  "scored_criteria": [
    {"id": "C1", "name": "Security & Compliance", "weight": 30},
    {"id": "C2", "name": "Performance", "weight": 25},
    {"id": "C3", "name": "Scalability", "weight": 25},
    {"id": "C4", "name": "Cost", "weight": 20}
  ],
  "scores": {
    "PostgreSQL": {
      "C1": {"raw": 5, "weighted": 1.50, "confidence": "high"},
      "C2": {"raw": 4, "weighted": 1.00, "confidence": "medium"},
      "C3": {"raw": 3, "weighted": 0.75, "confidence": "medium"},
      "C4": {"raw": 4, "weighted": 0.80, "confidence": "high"}
    },
    "MongoDB": {
      "C1": {"raw": 4, "weighted": 1.20, "confidence": "high"},
      "C2": {"raw": 3, "weighted": 0.75, "confidence": "medium"},
      "C3": {"raw": 5, "weighted": 1.25, "confidence": "high"},
      "C4": {"raw": 3, "weighted": 0.60, "confidence": "medium"}
    }
  },
  "total_scores": {
    "PostgreSQL": 4.05,
    "MongoDB": 3.80
  },
  "ranking": ["PostgreSQL", "MongoDB"],
  "sensitivity": {
    "gap_top2": 0.25,
    "scenarios": [
      {
        "id": "A",
        "source_criterion": "C1",
        "target_criterion": "C2",
        "shift": 10,
        "adjusted_weights": {"C1": 20, "C2": 35, "C3": 25, "C4": 20},
        "total_scores": {"PostgreSQL": 3.95, "MongoDB": 3.70},
        "ranking": ["PostgreSQL", "MongoDB"],
        "ranking_change": false
      },
      {
        "id": "B",
        "source_criterion": "C2",
        "target_criterion": "C1",
        "shift": 10,
        "adjusted_weights": {"C1": 40, "C2": 15, "C3": 25, "C4": 20},
        "total_scores": {"PostgreSQL": 4.15, "MongoDB": 3.90},
        "ranking": ["PostgreSQL", "MongoDB"],
        "ranking_change": false
      }
    ]
  },
  "recommendation": "PostgreSQL"
}
```
