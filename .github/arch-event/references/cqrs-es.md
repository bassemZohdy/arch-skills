# CQRS & Event Sourcing Reference

## CQRS

**Command Query Responsibility Segregation** — Separate read and write models.

```
Commands → Write Model → Write DB
                              ↓
Queries  ← Read Model  ← Read DB (denormalized)
```

**When to Use:**
- Different read/write patterns
- Different scaling needs
- Complex queries

**Trade-offs:**
- Eventual consistency
- Increased complexity

## Event Sourcing

Store state changes as events:

```
1. OrderCreated {orderId: 123}
2. ItemAdded {orderId: 123, item: "..."}
3. OrderSubmitted {orderId: 123}

Current State = Replay Events
```

**Benefits:**
- Complete audit trail
- Temporal queries
- Event replay

**Challenges:**
- Schema evolution
- Query complexity
