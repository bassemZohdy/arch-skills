# Test Pyramid Reference

## Ideal Distribution

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

| Gate | Metric | Threshold |
|------|--------|-----------|
| Coverage | Line coverage | > 80% |
| Mutation | Mutation score | > 70% |
| Performance | Test duration | < 10 min |
| Flakiness | Flaky rate | < 1% |
```
