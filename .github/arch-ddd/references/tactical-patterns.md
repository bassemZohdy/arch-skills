# Tactical Design Reference

## Entity vs Value Object

| Aspect | Entity | Value Object |
|--------|--------|--------------|
| Identity | Has unique ID | Compared by attributes |
| Mutability | Mutable | Immutable |
| Equality | Same ID = equal | All attributes equal |
| Example | Customer, Order | Address, Money |

## Aggregate Design Rules

1. One aggregate per transaction
2. Reference by identity, not reference
3. Keep aggregates small
4. Enforce invariants within aggregate

## Repository Pattern

```python
class OrderRepository:
    def find_by_id(self, order_id) -> Order:
        # Load aggregate from store
    
    def save(self, order: Order):
        # Persist aggregate changes
```

## Domain Services

When logic doesn't belong to any entity:

```python
class PricingService:
    def calculate_discount(self, order, customer):
        # Logic involving multiple entities
```
