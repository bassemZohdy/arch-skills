---
name: arch-event
description: Guide event-driven architecture design. Use when designing messaging systems, implementing CQRS or Event Sourcing, planning saga patterns, facilitating Event Storming, or implementing distributed transactions.
---

# Event-Driven Architecture

Systematic approach to designing event-driven systems.

## Workflow

```
1. Identify Events → What happens in the domain?
2. Choose Pattern → Pub/sub, streaming, CQRS?
3. Design Contracts → Event schemas and versions
4. Implement Flows → Producers, consumers, handlers
5. Handle Failures → Retries, dead letter queues
6. Monitor → Event flow visibility
```

## Step 1: Event Types

| Type | Description | Example |
|------|-------------|---------|
| **Domain Event** | Business-meaningful occurrence | OrderPlaced |
| **Integration Event** | Cross-boundary notification | PaymentProcessed |
| **Command** | Request to perform action | PlaceOrder |
| **Query** | Request for data | GetOrderStatus |

## Step 2: Messaging Patterns

### Pub/Sub

```
Publisher → Topic → Subscriber A
                   → Subscriber B
```

**Use when:** Multiple consumers, loose coupling.

### Point-to-Point

```
Producer → Queue → Consumer
```

**Use when:** Single consumer, guaranteed processing.

### Request/Reply

```
Client → Request Queue → Service → Reply Queue → Client
```

**Use when:** Async request/response needed.

## Step 3: CQRS

**Command Query Responsibility Segregation** — Separate read and write models.

```
Commands → Write Model → Write DB
                              ↓
Queries  ← Read Model  ← Read DB (denormalized)
```

**When to Use:**
- Read/write patterns differ significantly
- Different scaling needs for reads vs writes
- Complex queries on write-optimized data

**Trade-offs:**
- Eventual consistency
- Increased complexity
- More infrastructure

## Step 4: Event Sourcing

Store state changes as events, not current state.

```
Event Store:
1. OrderCreated {orderId: 123, items: [...]}
2. ItemAdded {orderId: 123, item: "..."}
3. OrderSubmitted {orderId: 123, timestamp: ...}

Current State = Replay Events
```

**Benefits:**
- Complete audit trail
- Temporal queries
- Debugging history
- Event replay

**Challenges:**
- Event schema evolution
- Snapshot management
- Query complexity

## Step 5: Saga Patterns

### Choreography

Each service publishes events and listens for others.

```
Order Service → OrderCreated → Payment Service
Payment Service → PaymentProcessed → Shipping Service
Shipping Service → ShipmentCreated → Notification Service
```

**Pros:** Simple, loose coupling.
**Cons:** Hard to track flow, debugging.

### Orchestration

Central coordinator manages the flow.

```
Saga Orchestrator:
1. Send CreateOrder to Order Service
2. Wait for OrderCreated
3. Send ProcessPayment to Payment Service
4. Wait for PaymentProcessed
5. Send ShipOrder to Shipping Service
```

**Pros:** Clear flow, easier debugging.
**Cons:** Single point of failure, tight coupling.

### Compensation

Rollback actions on failure.

| Step | Action | Compensation |
|------|--------|--------------|
| 1 | Create order | Cancel order |
| 2 | Process payment | Refund payment |
| 3 | Ship order | Return shipment |

## Step 6: Event Schema Design

```json
{
  "eventId": "uuid",
  "eventType": "OrderPlaced",
  "version": "1.0",
  "timestamp": "2024-01-15T10:30:00Z",
  "source": "order-service",
  "data": {
    "orderId": "123",
    "customerId": "456",
    "items": [...]
  }
}
```

### Schema Evolution Strategies

- **Additive changes** — Add new fields
- **Versioning** — Multiple schema versions
- **Upcasters** — Transform old events

## Step 7: Reliability

### Dead Letter Queues

Messages that fail repeatedly go to DLQ for investigation.

### Idempotency

Process same event multiple times without side effects.

```
Event ID → Check if processed → Skip if yes
```

### Exactly-Once Semantics

- Idempotent producers
- Transactional outbox
- Consumer deduplication

## Event-Driven Review Template

```markdown
## Event-Driven Architecture Review: [System]

### Events Identified
| Event | Producer | Consumers |
|-------|----------|-----------|

### Patterns Used
- Messaging: [Pub/sub, queue]
- State: [CQRS, Event Sourcing]
- Transactions: [Saga type]

### Reliability
- Idempotency: [How ensured]
- DLQ: [Configured?]
- Ordering: [Guaranteed?]

### Recommendations
1. [Improvement]
```
