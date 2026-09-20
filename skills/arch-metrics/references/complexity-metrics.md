# Complexity Metrics Reference

## Code Metrics

| Metric | Description | Target |
|--------|-------------|--------|
| Cyclomatic Complexity | Decision points | < 10 |
| Lines of Code | Function size | < 50 lines |
| Nesting Depth | Max nesting | < 4 |
| Coupling | Dependencies | Low |
| Cohesion | Internal unity | High |

## Architecture Metrics

| Metric | Formula | Good | Bad |
|--------|---------|------|-----|
| Afferent Coupling (Ca) | Incoming deps | Depends on role | High concentration can increase change impact |
| Efferent Coupling (Ce) | Outgoing deps | Low | High |
| Instability | Ce / (Ca + Ce) | Context-dependent | Undefined if denominator is zero |
| Abstractness | Abstract / Total | Context-dependent | Undefined if no types |

## Zone of Pain/Uselessness

| Region | Instability I | Abstractness A | Interpretation |
| --- | --- | --- | --- |
| Pain | Near 0 | Near 0 | Stable, concrete dependencies are difficult to change |
| Uselessness | Near 1 | Near 1 | Abstract elements have few dependents |

When Ca+Ce is zero, I is undefined. Thresholds depend on the role and workload,
not a universal goal to maximize abstractness or minimize outgoing dependencies.
[Definitions](https://www.ndepend.com/docs/code-metrics).
