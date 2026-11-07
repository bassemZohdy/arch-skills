# Test Pyramid Reference

## Illustrative Pyramid Distribution

The percentages below are examples, not prescribed targets. Choose the portfolio
from product risks and feedback cost; the Testing Trophy emphasizes integration
tests instead. See [test-deep-dive.md](test-deep-dive.md).

| Level | Percentage | Speed | Cost |
|-------|------------|-------|------|
| Unit | 70% | Milliseconds | Low |
| Integration | 20% | Seconds | Medium |
| E2E | 10% | Minutes | High |

## Contract Testing

### Consumer-Driven Contracts

```
Consumer → Defines expectations → Provider → Validates
```

### Tools

| Tool | Language | Approach |
|------|----------|----------|
| Pact | Multi | Consumer-driven |
| Spring Cloud Contract | JVM | Provider-driven |
| Postman | Multi | Collection-based |

## Test Automation

### CI Pipeline

```
Commit → Lint → Unit Tests → Build → Integration → Deploy → E2E
```

### Quality Gates

Set these gates against critical behavior, test effectiveness and a measured
baseline. A coverage percentage alone is not a quality guarantee.

| Gate | Metric | Threshold |
|------|--------|-----------|
| Coverage | Line coverage | Project-defined, with critical paths reviewed |
| Mutation | Mutation score | Project-defined after a baseline |
| Performance | Test duration | Project-defined CI budget |
| Flakiness | Flaky rate | Project-defined reliability target |
