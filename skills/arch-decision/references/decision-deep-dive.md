# Decision Analysis Deep Dive

Extended patterns, edge cases, and advanced DAR methodology.

## When to Escalate from Expedited to Formal

| Signal | Action |
|--------|--------|
| Multiple stakeholders disagree on criteria | Escalate to formal — run a facilitated session |
| Decision cost exceeds $50K or 2 sprints | Escalate to formal — document thoroughly |
| Reversible within a sprint | Stay expedited — document briefly |
| Single approver with authority | Stay expedited — record and move on |
| External audit/compliance requires traceability | Escalate to formal — generate full DAR |
| Technology choice locks architecture for years | Escalate to formal — run sensitivity checks |

## Advanced Sensitivity Analysis

### Tornado Diagram (Mental Model)

1. Rank criteria by weight (highest first)
2. For each criterion, vary weight by ±10 while adjusting others proportionally
3. Record ranking change at each perturbation
4. Criteria whose perturbation changes the ranking are "sensitive"

### Monte Carlo (When Data Exists)

When scores are ranges rather than points (e.g., cost: $5K-$8K/month):
1. Define distribution per criterion per alternative
2. Sample 1,000 random combinations
3. Report: "Alternative A wins in X% of simulations"

### Agreement Index

When multiple evaluators score independently:
- Fleiss' Kappa for categorical agreement
- Intraclass Correlation Coefficient (ICC) for numerical scores
- Flag scores with inter-rater disagreement > 2 points for discussion

## Decision Anti-Patterns

| Anti-Pattern | Symptom | Fix |
|--------------|---------|-----|
| **Decide-and-Defend** | Decision made before analysis; DAR written backwards | Run analysis blind: scores before revealing the preferred option |
| **Criteria Creep** | New criteria added mid-evaluation to swing the result | Freeze criteria before scoring; late additions require restart |
| **Weight Inflation** | Stakeholder inflates weight of "their" criterion | Calibrate weights via budget-allocation game (divide 100 poker chips) |
| **Confidence Inflation** | Low-confidence scores marked as medium/high | Require evidence link per score; flag unlinked scores |
| **Analysis Paralysis** | Formal DAR for trivial choice (which linter to use) | Use expedited mode; timebox to 30 minutes |

## Criteria Weight Elicitation Techniques

### Direct Rating
- Each stakeholder assigns 0-100 to each criterion
- Normalize to sum = 100
- Average across stakeholders

### Budget Allocation
- Give each stakeholder 100 "chips" to allocate
- Forces trade-off thinking
- Reveals true priorities better than direct rating

### Analytic Hierarchy Process (AHP)
- Pairwise comparison of all criteria
- Calculate eigenvector for weights
- Consistency ratio < 0.10 required
- Use for high-stakes decisions with ≥5 criteria

## Handling Uncertainty

| Situation | Approach |
|-----------|----------|
| Missing data for a score | Mark as low confidence; flag for spike/PoC |
| New alternative emerges mid-evaluation | Restart scoring; gate-check the new alternative |
| Stakeholder objects to weights | Reconcile via budget allocation; document disagreement |
| Evaluator bias suspected | Add a second evaluator; compare scores; discuss gaps > 2 |
| Technology rapidly evolving | Shorten review trigger interval; note assumptions |

## Multi-Stage Decisions

For decisions that cascade (choose platform → choose database → choose ORM):

1. Run DAR for the platform first
2. Lock the platform decision
3. Use platform constraints as gates for the database DAR
4. Lock the database decision
5. Use database constraints as gates for the ORM DAR

Never evaluate all three in one matrix — the combinatorial space explodes.

## Communicating Decisions

### For Executives
- One-page summary: decision, rationale, tradeoffs, cost, timeline
- No matrix, no sensitivity graphs
- Focus: business impact, risk, alternatives rejected

### For Engineering Teams
- Full ADR in repo (MADR format)
- Include matrix, sensitivity, and confidence
- Link to related ADRs
- Archive superseded ADRs

### For Compliance/Audit
- Signed DAR document
- Evidence links per score
- Reviewer sign-off
- Retention: 7 years (SOX) or regulation-dependent

## Tooling

| Tool | Use Case |
|------|----------|
| Spreadsheet (Excel/Sheets) | Simple weighted matrices |
| Python pandas | Monte Carlo sensitivity |
| Decision trees (Graphviz) | Sequential decisions |
| ADR tools (adr-tools, log4brains) | ADR lifecycle management |
