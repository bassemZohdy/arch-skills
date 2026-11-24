# Tactical Design Reference

## Entity vs Value Object

| Aspect | Entity | Value Object |
|--------|--------|--------------|
| Identity | Has unique ID | Compared by attributes |
| Mutability | State may change while identity persists | Immutable |
| Equality | Same ID = equal | All attributes equal |
| Example | Customer, Order | Address, Money |

## Aggregate Design Rules

1. Prefer one aggregate per transaction; validate the consistency boundary against business invariants
2. Reference by identity, not reference
3. Keep aggregates small
4. Enforce invariants within aggregate

## Repository Pattern

```python
class OrderRepository:
    def find_by_id(self, order_id) -> Order:
        raise NotImplementedError("Load aggregate and concurrency version from store")
    
    def save(self, order: Order):
        raise NotImplementedError("Persist with concurrency control")
```

## Domain Services

When logic doesn't belong to any entity:

```python
class PricingService:
    def calculate_discount(self, order, customer):
        raise NotImplementedError("Implement the domain pricing policy")
```
