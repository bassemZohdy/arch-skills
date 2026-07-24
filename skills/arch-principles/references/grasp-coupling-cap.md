# GRASP, Coupling & Cohesion, CAP

Load this when assigning responsibilities, measuring coupling, or reasoning about distributed-system trade-offs.

## GRASP — Responsibility Assignment

Nine patterns for deciding *who does what* in an object design.

| Pattern | Assign responsibility to... | Watch out |
|---------|----------------------------|-----------|
| Information Expert | The class that has the information needed | Anemic models when ignored |
| Creator | B creates A when B aggregates/contains/records/closely uses A or has A's init data | Factories when creation is complex |
| Controller | A façade over the domain for UI-originated operations | Bloated controllers — keep them thin |
| Low Coupling | Whatever minimizes dependencies | Balance against cohesion |
| High Cohesion | Whatever keeps a unit's purposes related | Splitting too far |
| Polymorphism | Type-varying behavior behind one abstraction | Switch statements growing arms |
| Pure Fabrication | An invented service class when no domain object is the expert | Over-fabricating helpers |
| Indirection | An intermediary between two coupled units | Layers of forwarding with no policy |
| Protected Variations | A stable interface around a point of instability | Wrapping things that never vary |

### Controller vs Application Service

A GRASP controller and a DDD application service are the same idea at different scales: the first non-UI object that coordinates a use case. Keep it free of business rules — those belong in the domain.

## Coupling

Degree to which one unit depends on another.

| Type | Description | Severity |
|------|-------------|----------|
| Content | One module reaches inside another | Worst |
| Common | Shared global state | Bad |
| External | Shared external format/protocol | Moderate |
| Control | Passing flags that steer another's logic | Moderate |
| Stamp | Passing a whole structure when a field would do | Low |
| Data | Passing only needed values | Best |

**Afferent (incoming)** coupling: who depends on me — high afferent = high change impact, keep stable.
**Efferent (outgoing)** coupling: what I depend on — high efferent = fragile, hide behind abstractions.

## Cohesion

Degree to which a unit's members belong together.

| Type | Description | Quality |
|------|-------------|---------|
| Functional | All parts serve one computation | Best |
| Sequential | Output of one part feeds the next | Good |
| Communicational | Parts operate on the same data | OK |
| Procedural | Parts run in an order, unrelated data | Weak |
| Temporal | Grouped by when they run (init utils) | Poor |
| Logical | Grouped by category (all "helpers") | Poor |
| Coincidental | No relationship | Worst |

Goal: maximize cohesion *inside* a unit, minimize coupling *between* units. They trade off — splitting for coupling can destroy cohesion; judge by change cost.

## Connascence

A finer-grained coupling measure: two components are connascent if a change in one forces a change in the other.

- **Static** (name, type, meaning, position, algorithm) — visible at compile time, weaker.
- **Dynamic** (execution order, timing, value, identity) — runtime, stronger.

Rule: minimize connascence across boundaries; within a unit, weak connascence is acceptable. Prefer connascence of name over position (named args over positional), meaning over magic values.

## CAP and PACELC

### CAP

During a network **partition** (P, inevitable in distributed systems), a system must choose:

- **Consistency (C)**: every read sees the latest write or an error.
- **Availability (A)**: every request gets a non-error response, possibly stale.

| Stance | Mechanism | Example choice |
|--------|-----------|----------------|
| CP | Quorum, leader election, reject minority writes | Account balances |
| AP | Multi-leader, async replication, conflict resolution | Shopping carts, feeds |

### PACELC

Extends CAP to normal operation: **if Partition, choose A or C; Else choose Latency or Consistency.**

- A PA/EL system (Dynamo-style) favors availability and latency.
- A PC/EC system favors consistency everywhere.
- Decide per data item and operation — "read your own writes" for the author, eventual for followers is a per-operation answer.

### Consistency Spectrum

Strong → linearizability → sequential → causal → read-your-writes → monotonic reads → eventual.
Each step down buys availability and latency; each step up costs coordination. Document where each data flow sits and why.

## Persistence Ignorance

Domain types should not know how they are stored: no ORM attributes, no serialization concerns, no SQL-shaped design.

- Keeps the domain model the expert on business rules (GRASP Information Expert).
- The price is mapping; pay it at repositories, not inside the model (see `arch-ddd`).
