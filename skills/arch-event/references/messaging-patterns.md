# Messaging Patterns Reference

## Pub/Sub

```
Publisher → Topic → Subscriber A
                   → Subscriber B
```

**Use when:** Multiple consumers, loose coupling.

## Point-to-Point

```
Producer → Queue → Consumer
```

**Use when:** One competing consumer handles each delivery; processing guarantees depend on persistence, acknowledgments, retries and idempotency.

## Event Streaming

```
Producer → Stream → Consumer Group
```

**Use when:** High throughput, replay capability.

## Dead Letter Queue

Messages that fail repeatedly go to DLQ for investigation.

## Idempotency

Process repeated deliveries without repeating business effects. Couple the
deduplication record and state update atomically; external effects need their
own idempotency or reconciliation contract:

```
Transaction: claim unique event ID + business update → commit → acknowledge
```
