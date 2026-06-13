# Domain-Driven Design Deep Dive

**Source:** Eric Evans DDD, Vaughn Vernon IDDD

## Strategic Design

### Bounded Context

A boundary within which a particular domain model applies.

```
┌─────────────────────┐     ┌─────────────────────┐
│   Sales Context     │     │   Shipping Context   │
│  - Order            │────▶│  - Shipment         │
│  - Customer         │     │  - Tracking         │
└─────────────────────┘     └─────────────────────┘
```

### Context Mapping Patterns

| Pattern | Description | Use When |
|---------|-------------|----------|
| **Shared Kernel** | Shared model | Tight collaboration |
| **Customer-Supplier** | Upstream/downstream | Service dependency |
| **Conformist** | Downstream conforms | No control upstream |
| **Anti-Corruption Layer** | Translation layer | Legacy integration |
| **Open Host Service** | Public API | Multiple consumers |
| **Published Language** | Shared specification | Cross-team |

### Ubiquitous Language

Create shared language between developers and domain experts.

- Use same terms in code, docs, and conversations
- Avoid technical jargon for business concepts
- Document in glossary

## Tactical Design

### Entity vs Value Object

| Aspect | Entity | Value Object |
|--------|--------|--------------|
| Identity | Has unique ID | Compared by attributes |
| Mutability | Mutable | Immutable |
| Equality | Same ID = equal | All attributes equal |
| Example | Customer, Order | Address, Money |

### Aggregate Design Rules

1. **One aggregate per transaction** - Don't span aggregates
2. **Reference by identity** - Don't reference directly
3. **Small aggregates** - Keep minimal
4. **Invariant consistency** - All rules enforced within

### Repository Pattern

```python
class OrderRepository:
    def find_by_id(self, order_id) -> Order:
        # Load aggregate from store
    
    def save(self, order: Order):
        # Persist aggregate changes
```

### Domain Services

When logic doesn't belong to any entity:

```python
class PricingService:
    def calculate_discount(self, order, customer):
        # Logic involving multiple entities
```

## Event Storming

### Workshop Steps

1. **Big Picture** - Everyone sticks events on wall
2. **Process Modeling** - Identify commands, policies
3. **Service Definition** - Identify bounded contexts
4. **Implementation** - Design aggregates and flows

### Event Storming Notation

| Color | Meaning |
|-------|---------|
| **Orange** | Domain Event |
| **Blue** | Command |
| **Yellow** | Aggregate |
| **Green** | Read Model |
| **Red** | Policy/Rules |
| **Purple** | External System |

## DDD Smells

| Smell | Problem | Solution |
|-------|---------|----------|
| **Anemic Domain** | Logic in services | Move to entities |
| **God Aggregate** | Too much in one | Split into smaller |
| **Primitive Obsession** | Primitives instead of VOs | Create value objects |
| **Hidden Bounded Context** | No clear boundaries | Define contexts |
