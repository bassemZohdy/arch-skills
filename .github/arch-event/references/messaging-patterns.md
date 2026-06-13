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

**Use when:** Single consumer, guaranteed processing.

## Event Streaming

```
Producer → Stream → Consumer Group
```

**Use when:** High throughput, replay capability.

## Dead Letter Queue

Messages that fail repeatedly go to DLQ for investigation.

## Idempotency

Process same event multiple times without side effects:

```
Event ID → Check if processed → Skip if yes
```
