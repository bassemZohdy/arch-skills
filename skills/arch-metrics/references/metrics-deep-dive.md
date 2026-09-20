# Metrics Deep Dive

**Source:** SIG Maintainability, Code Climate, SonarQube

## Complexity Metrics

| Metric | Formula | Target |
|--------|---------|--------|
| **Cyclomatic Complexity** | Decision points per function | < 10 |
| **Cognitive Complexity** | Nesting and control flow | < 15 |
| **Lines of Code** | Function/class size | < 50 lines/function |
| **Nesting Depth** | Maximum nesting level | < 4 |

## Coupling Metrics

| Metric | Formula | Interpretation |
|--------|---------|----------------|
| **Afferent Coupling (Ca)** | Incoming dependencies | How depended upon |
| **Efferent Coupling (Ce)** | Outgoing dependencies | What depends on |
| **Instability** | Ce / (Ca + Ce) | 0=stable, 1=unstable |
| **Abstractness** | Abstract / Total | 0=concrete, 1=abstract |

## Stability Formula

```
Instability = Ce / (Ca + Ce)

- 0.0 = Highly stable (no outgoing deps)
- 1.0 = Highly unstable (no incoming deps)
```

### Zone of Pain/Uselessness

| Region | Instability I | Abstractness A | Interpretation |
| --- | --- | --- | --- |
| Pain | Near 0 | Near 0 | Stable, concrete dependencies are difficult to change |
| Uselessness | Near 1 | Near 1 | Abstract elements have few dependents |

When Ca+Ce is zero, I is undefined. Thresholds depend on the role and workload,
not a universal goal to maximize abstractness or minimize outgoing dependencies.
[Definitions](https://www.ndepend.com/docs/code-metrics).

## Design Health Metrics

### SOLID Compliance

| Principle | Metric | How to Measure |
|-----------|--------|----------------|
| **SRP** | Class responsibility count | Manual review |
| **OCP** | Open for extension | Pattern analysis |
| **LSP** | Subtype substitutability | Test coverage |
| **ISP** | Interface size | Method count |
| **DIP** | Dependency direction | Dependency graph |

## Technical Debt Metrics

| Category | Metric | Measurement |
|----------|--------|-------------|
| **Code Debt** | Code smells | SonarQube |
| **Test Debt** | Coverage gaps | < 80% = debt |
| **Doc Debt** | Missing docs | Coverage % |
| **Dependency Debt** | Outdated packages | Age, CVEs |
| **Architecture Debt** | Violations | Dependency cycles |

### Debt Score

```
Debt Score = (Critical × 10) + (High × 5) + (Medium × 2) + (Low × 1)
```

## Dashboard Metrics

| Indicator | Green | Yellow | Red |
|-----------|-------|--------|-----|
| Cyclomatic Complexity | < 10 | 10-20 | > 20 |
| Test Coverage | > 80% | 60-80% | < 60% |
| Debt Score | < 50 | 50-100 | > 100 |
| Dependency Cycles | 0 | 1-2 | > 2 |

## Tools

| Tool | Purpose |
|------|---------|
| **SonarQube** | Code quality |
| **Structure101** | Architecture analysis |
| **jDepend** | Java dependencies |
| **Dependency-Cruiser** | JS/TS dependencies |
| **Pydeps** | Python dependencies |
