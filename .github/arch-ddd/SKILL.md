---
name: arch-ddd
description: Guide Domain-Driven Design modeling. Use when modeling complex domains, defining bounded contexts, designing aggregates, implementing tactical DDD patterns, or facilitating Event Storming workshops.
---

# Domain-Driven Design

Systematic approach to modeling complex business domains.

## Workflow

```
1. Explore Domain → Understand business language
2. Identify Bounded Contexts → Define boundaries
3. Map Contexts → Relationships between contexts
4. Model Aggregates → Transactional consistency boundaries
5. Define Tactical Patterns → Entities, value objects, repositories
6. Refactor → Continuous model refinement
```

## Step 1: Ubiquitous Language

Create shared language between developers and domain experts.

| Term | Definition | Example |
|------|------------|---------|
| **Entity** | Object with identity | Customer (identified by ID) |
| **Value Object** | Immutable, no identity | Address (compared by value) |
| **Aggregate** | Consistency boundary | Order (contains OrderLines) |
| **Domain Event** | Something that happened | OrderPlaced |
| **Command** | Request to do something | PlaceOrder |

## Step 2: Strategic Design

### Bounded Context

A boundary within which a particular domain model applies.

```
┌─────────────────────┐     ┌─────────────────────┐
│   Sales Context     │     │   Shipping Context   │
│                     │     │                     │
│  - Order            │────▶│  - Shipment         │
│  - Customer         │     │  - Tracking         │
│  - Product          │     │  - Warehouse        │
└─────────────────────┘     └─────────────────────┘
```

### Context Mapping Patterns

| Pattern | Description | Use When |
|---------|-------------|----------|
| **Shared Kernel** | Shared model between contexts | Tight collaboration |
| **Customer-Supplier** | Upstream/downstream dependency | Service dependency |
| **Conformist** | Downstream conforms to upstream | No control over upstream |
| **Anti-Corruption Layer** | Translation layer | Integrating legacy |
| **Open Host Service** | Public API | Multiple consumers |
| **Published Language** | Shared specification | Cross-team |

### Context Map Example

```
Sales Context ──(Customer-Supplier)──▶ Shipping Context
         │                                   │
         │                                   
         └──(Shared Kernel)── Finance Context
```

## Step 3: Tactical Design

### Aggregate Design Rules

1. **One aggregate per transaction** — Don't span aggregates
2. **Reference by identity** — Don't reference other aggregates directly
3. **Small aggregates** — Keep minimal
4. **Invariant consistency** — All rules enforced within aggregate

### Aggregate Example

```python
class Order:  # Aggregate Root
    def __init__(self, order_id, customer_id):
        self.order_id = order_id
        self.customer_id = customer_id  # Reference by ID
        self.lines = []  # OrderLine is part of aggregate
    
    def add_line(self, product_id, quantity):
        # Invariant: max 10 items per order
        if len(self.lines) >= 10:
            raise OrderLimitExceeded()
        self.lines.append(OrderLine(product_id, quantity))
```

### Entity vs Value Object

| Aspect | Entity | Value Object |
|--------|--------|--------------|
| **Identity** | Has unique ID | Compared by attributes |
| **Mutability** | Mutable | Immutable |
| **Equality** | Same ID = equal | All attributes equal |
| **Example** | Customer, Order | Address, Money, DateRange |

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
        # Business rule involving multiple entities
```

## Step 4: Event Storming

### Workshop Steps

1. **Big Picture** — Everyone sticks events on wall
2. **Process Modeling** — Identify commands, policies
3. **Service Definition** — Identify bounded contexts
4. **Implementation** — Design aggregates and flows

### Event Storming Notation

| Color | Meaning |
|-------|---------|
| **Orange** | Domain Event |
| **Blue** | Command |
| **Yellow** | Aggregate |
| **Green** | Read Model |
| **Red** | Policy/Rules |
| **Purple** | External System |

## Step 5: DDD Smells

| Smell | Problem | Solution |
|-------|---------|----------|
| **Anemic Domain** | Logic in services, not entities | Move logic to entities |
| **God Aggregate** | Too much in one aggregate | Split into smaller |
| **Primitive Obsession** | Primitives instead of VOs | Create value objects |
| **Hidden Bounded Context** | No clear boundaries | Define contexts |

## DDD Review Template

```markdown
## DDD Review: [System]

### Bounded Contexts
| Context | Responsibility | Team |
|---------|---------------|------|

### Context Map
- Relationships: [List]

### Aggregates
| Aggregate | Invariants | Commands |
|-----------|------------|----------|

### Tactical Patterns
- Value Objects: [List]
- Domain Events: [List]
- Repositories: [List]

### Recommendations
1. [Improvement]
```
