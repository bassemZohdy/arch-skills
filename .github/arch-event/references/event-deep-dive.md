# Event-Driven Architecture Deep Dive

**Source:** Enterprise Integration Patterns, Building Event-Driven Microservices

## Event Types

| Type | Description | Example |
|------|-------------|---------|
| **Domain Event** | Business-meaningful occurrence | OrderPlaced |
| **Integration Event** | Cross-boundary notification | PaymentProcessed |
| **Command** | Request to perform action | PlaceOrder |
| **Query** | Request for data | GetOrderStatus |

## Messaging Patterns

### Point-to-Point

```
Producer → Queue → Consumer
```

**Use when:** Single consumer, guaranteed processing.

### Pub/Sub

```
Publisher → Topic → Subscriber A
                   → Subscriber B
```

**Use when:** Multiple consumers, loose coupling.

### Request/Reply

```
Client → Request Queue → Service → Reply Queue → Client
```

**Use when:** Async request/response needed.

## CQRS (Command Query Responsibility Segregation)

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

## Saga Patterns

### Choreography

Each service publishes events and listens for others.

```
Order Service → OrderCreated → Payment Service
Payment Service → PaymentProcessed → Shipping Service
```

**Pros:** Simple, loose coupling.
**Cons:** Hard to track flow.

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
**Cons:** Single point of failure.

## Event Schema Design

```json
{
  "eventId": "uuid",
  "eventType": "OrderPlaced",
  "version": "1.0",
  "timestamp": "2024-01-15T10:30:00Z",
  "source": "order-service",
  "data": {
    "orderId": "123",
    "customerId": "456"
  }
}
```

## Event Reliability

### Dead Letter Queue

Messages that fail repeatedly go to DLQ for investigation.

### Idempotency

Process same event multiple times without side effects:

```
Event ID → Check if processed → Skip if yes
```

### Exactly-Once Semantics

- Idempotent producers
- Transactional outbox
- Consumer deduplication
