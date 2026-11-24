# Test Architecture Deep Dive

**Source:** Testing Trophy, Contract Testing, Mutation Testing

## Choose a test portfolio

The [Testing Trophy](https://kentcdodds.com/blog/the-testing-trophy-and-testing-classifications)
emphasizes integration tests with static analysis, unit tests and a smaller E2E
layer. It is not the 70/20/10 pyramid. Choose the mix from failure risks,
feedback speed and maintenance cost; neither model mandates percentages.

### Testing Levels

| Level | Scope | Typical speed | Main purpose |
|-------|-------|---------------|--------------|
| **Unit** | Function/class | Milliseconds | Local logic and edge cases |
| **Integration** | Multiple components | Seconds | Boundary behavior and interoperability |
| **E2E** | Full system | Seconds to minutes | Critical user journeys |

## Contract Testing

### Consumer-Driven Contracts

```
Consumer → Defines expectations → Provider → Validates
```

### Tools

| Tool | Language | Approach |
|------|----------|----------|
| **Pact** | Multi | Consumer-driven |
| **Spring Cloud Contract** | JVM | Provider-driven |
| **Postman** | Multi | Collection-based |

### Contract Test Template

```yaml
# Consumer test
- provider: OrderService
  consumer: ShippingService
  interaction:
    description: Get order by ID
    request:
      method: GET
      path: /orders/123
    response:
      status: 200
      body:
        id: "123"
        status: "shipped"
```

## Mutation Testing

### Tools

| Tool | Language | Description |
|------|----------|-------------|
| **PIT** | Java | Mutation testing for JVM |
| **Stryker** | JS/TS | JavaScript mutation testing |
| **mutmut** | Python | Python mutation testing |

### Mutation Score

```
Mutation Score = Killed Mutants / Eligible Mutants × 100%
```

Define the tool's denominator, handling of invalid/equivalent mutants and
timeouts, and untested code before comparing results. Set a project-specific
mutation target after a baseline, then inspect surviving mutants in critical
paths; a single percentage is not a universal quality grade.

## Test Anti-patterns

| Anti-pattern | Problem | Solution |
|--------------|---------|----------|
| **Test Pyramid Inversion** | Too many E2E | Balance pyramid |
| **Fragile Tests** | Break with changes | Stable selectors |
| **Slow Tests** | Block CI pipeline | Parallelize |
| **Flaky Tests** | Non-deterministic | Isolate, fix |
| **Test Interdependence** | Tests affect each other | Independent tests |
