# Test Architecture Deep Dive

**Source:** Testing Trophy, Contract Testing, Mutation Testing

## Testing Trophy (Kent C. Dodds)

```
        ┌─────────┐
        │  E2E    │  10%
        ├─────────┤
        │Integration│  20%
        ├─────────┤
        │  Unit   │  70%
        └─────────┘
```

### Testing Levels

| Level | Scope | Speed | Cost | Quantity |
|-------|-------|-------|------|----------|
| **Unit** | Single function/class | Milliseconds | Low | 70% |
| **Integration** | Multiple components | Seconds | Medium | 20% |
| **E2E** | Full system | Minutes | High | 10% |

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
Mutation Score = Killed Mutants / Total Mutants × 100%
```

| Score | Quality |
|-------|---------|
| > 80% | Good |
| 60-80% | Acceptable |
| < 60% | Needs improvement |

## Test Anti-patterns

| Anti-pattern | Problem | Solution |
|--------------|---------|----------|
| **Test Pyramid Inversion** | Too many E2E | Balance pyramid |
| **Fragile Tests** | Break with changes | Stable selectors |
| **Slow Tests** | Block CI pipeline | Parallelize |
| **Flaky Tests** | Non-deterministic | Isolate, fix |
| **Test Interdependence** | Tests affect each other | Independent tests |
