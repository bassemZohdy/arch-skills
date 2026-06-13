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
| Afferent Coupling (Ca) | Incoming deps | High | Low |
| Efferent Coupling (Ce) | Outgoing deps | Low | High |
| Instability | Ce / (Ca + Ce) | 0.0 | 1.0 |
| Abstractness | Abstract / Total | High | Low |

## Zone of Pain/Uselessness

```
Abstractness ↑
    │
    │  Zone of        │
    │  Uselessness    │
    │                 │
1.0 ├─────────────────┤
    │                 │
    │                 │
0.0 ├─────────────────┤
    │  Zone of        │
    │  Pain           │
    └─────────────────┘
       0.0          1.0  Instability →
```
