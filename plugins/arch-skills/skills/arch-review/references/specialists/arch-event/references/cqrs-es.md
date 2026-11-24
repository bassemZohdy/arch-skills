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
- Eventual consistency when separate stores are updated asynchronously
- Increased complexity

CQRS separates command and query models; both can share one database. It does not
require a broker, event sourcing or eventual consistency. Specify the consistency
and freshness contract of the selected implementation.

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
