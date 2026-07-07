---
name: arch-test
description: Design test strategy, test pyramids, and verification standards. Use when planning unit, integration, contract, or end-to-end tests, or when reducing flakiness and setting quality gates for a system.
---

# Test Architecture

Systematic approach to designing test strategies.

## Workflow

```
1. Define Strategy → What to test and when?
2. Design Pyramid → Unit, integration, e2e balance
3. Implement Contracts → Service boundaries
4. Plan Automation → CI/CD integration
5. Measure → Coverage and effectiveness
6. Maintain → Keep tests valuable
```

## Step 1: Test Pyramid

```
        ┌─────────┐
        │   E2E   │  ← Few, slow, expensive
        ├─────────┤
        │Integration│  ← Some, medium speed
        ├─────────┤
        │  Unit   │  ← Many, fast, cheap
        └─────────┘
```

| Level | Scope | Speed | Cost | Quantity |
|-------|-------|-------|------|----------|
| **Unit** | Single function/class | Milliseconds | Low | 70% |
| **Integration** | Multiple components | Seconds | Medium | 20% |
| **E2E** | Full system | Minutes | High | 10% |

## Step 2: Test Types

### Unit Tests

Test individual components in isolation.

```python
def test_order_total():
    order = Order(items=[Item(price=10), Item(price=20)])
    assert order.total == 30
```

**Best Practices:**
- One assertion per test
- Fast execution
- No external dependencies
- Deterministic results

### Integration Tests

Test component interactions.

```python
def test_create_order():
    order = order_service.create_order(customer_id=123, items=[...])
    assert order.id is not None
    assert order.status == "created"
```

**Best Practices:**
- Test real integrations
- Use test databases/services
- Clean up after tests
- Test error scenarios

### Contract Tests

Verify service contracts between teams.

```json
{
  "provider": "OrderService",
  "consumer": "ShippingService",
  "interaction": {
    "description": "Get order by ID",
    "request": {
      "method": "GET",
      "path": "/orders/123"
    },
    "response": {
      "status": 200,
      "body": {
        "id": "123",
        "status": "shipped"
      }
    }
  }
}
```

**Tools:**
- Pact — Contract testing framework
- Spring Cloud Contract — JVM contracts

### E2E Tests

Test complete user flows.

```python
def test_purchase_flow():
    browser.goto("/products")
    browser.click(".add-to-cart")
    browser.click(".checkout")
    browser.fill("#email", "test@example.com")
    browser.click(".submit-order")
    assert browser.text(".confirmation") == "Order placed"
```

**Best Practices:**
- Test critical paths only
- Use page object model
- Parallelize when possible
- Retry flaky tests

## Step 3: Testing Patterns

### Given-When-Then

```python
def test_order_placement():
    # Given
    customer = create_customer()
    product = create_product(stock=10)
    
    # When
    order = place_order(customer, product, quantity=2)
    
    # Then
    assert order.status == "confirmed"
    assert product.stock == 8
```

### Test Data Management

| Strategy | Use Case |
|----------|----------|
| **Factories** | Create test data dynamically |
| **Fixtures** | Pre-defined test data |
| **Builders** | Complex object construction |
| **Seeds** | Database initialization |

### Mocking vs Stubbing

| Type | Purpose | Example |
|------|---------|---------|
| **Mock** | Verify interactions | Verify email sent |
| **Stub** | Provide canned responses | Return fixed user |
| **Spy** | Record calls | Count API calls |

## Step 4: Test Automation

### CI/CD Integration

```
Commit → Unit Tests → Build → Integration Tests → Deploy → E2E Tests
```

### Quality Gates

| Gate | Metric | Threshold |
|------|--------|-----------|
| **Coverage** | Line coverage | > 80% |
| **Mutation** | Mutation score | > 70% |
| **Performance** | Test duration | < 10 min |
| **Flakiness** | Flaky test rate | < 1% |

## Step 5: Anti-patterns

| Anti-pattern | Problem | Solution |
|--------------|---------|----------|
| **Test Pyramid Inversion** | Too many E2E, few unit | Balance pyramid |
| **Fragile Tests** | Break with changes | Stable selectors |
| **Slow Tests** | Block CI pipeline | Parallelize, optimize |
| **Flaky Tests** | Non-deterministic | Isolate, fix |

## Examples

- Define a test pyramid for a web app with a slow payment flow.
- Add contract tests between order and shipping services.
- Reduce flaky E2E coverage by moving logic into faster integration tests.

## Common Gotchas

- Do not over-rotate to E2E tests when unit or integration tests will catch the same behavior sooner.
- Keep selectors and test data stable so refactors do not break healthy tests.
- Separate contract tests from smoke tests; they answer different questions.

## Related Skills

- **arch-fitness** - Architecture tests as part of the suite
- **arch-refactoring** - The safety net tests provide
- **arch-devops** - Where the tests run in the pipeline

## Test Strategy Template

```markdown
## Test Strategy: [System]

### Test Pyramid
| Level | Count | Coverage | Speed |
|-------|-------|----------|-------|

### Key Flows
| Flow | Test Type | Priority |
|------|-----------|----------|

### Quality Gates
| Gate | Threshold |
|------|-----------|
```
