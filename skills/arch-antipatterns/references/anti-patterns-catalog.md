# Anti-Patterns Catalog

Load this when diagnosing a structural problem and needing the named anti-pattern, its variants, and its canonical remedy.

## Architectural Anti-Patterns

### Big Ball of Mud

A system with no recognizable architecture: haphazardly structured, sprawling, duct-tape growth.

- **Causes**: sustained time pressure, no enforced boundaries, turnover erasing design intent.
- **Variants**: *Throwaway Code* that shipped, *Piecemeal Growth* without design checkpoints.
- **Remedy**: "sweep it under the rug" — identify coherent regions, draw intended boundaries around them, migrate incrementally (strangler fig), and enforce with architecture tests. Total rewrites usually reproduce the mud with newer syntax.

### God Object (Blob)

One class concentrates the intelligence; everything else is a data container.

- **Signals**: huge field/method counts, dependencies on most of the system, name suffixes `Manager`/`Controller`/`Util`, churn concentration in version control.
- **Remedy**: inventory responsibilities, extract one cohesive cluster at a time into collaborators, keep the original as a thin delegator until nothing routes through it.

### Distributed Monolith

Services that are deployed separately but coupled so tightly they must change and release together.

- **Signals**: shared database, chatty synchronous call chains, version lockstep, "microservices" that fail as a unit.
- **Remedy**: either redraw boundaries around business capabilities with data ownership, or honestly re-merge into a modular monolith. Both beat the status quo.

### Leaky Abstraction

An abstraction that cannot be used without understanding its implementation.

- **Signals**: callers handle implementation exceptions, configure implementation knobs, rely on call order or timing, bypass "for performance".
- **Remedy**: restate the contract in the caller's vocabulary, wrap the implementation, translate its errors, and make the fast path part of the contract — not a side channel.

### Golden Hammer

One familiar technology applied to every problem ("we're a Kafka shop").

- **Signals**: solutions named before problems; requirements contorted to fit the tool.
- **Remedy**: decision records that compare at least two credible alternatives per significant choice (see arch-decision).

### Resume-Driven Development

Technology choices made for the architects' CVs, not the system's needs. Cousin of Golden Hammer; remedy is the same: evidence-based decisions with review.

### Vendor Lock-In (as anti-pattern)

Architecture shaped so that leaving a vendor is economically impossible, without that trade being a conscious decision.

- **Remedy**: decide deliberately; where exit cost matters, keep domain logic behind ports (see arch-patterns hexagonal) even if adapters are vendor-specific.

### Cargo-Cult Architecture

Copying a famous company's architecture (Netflix microservices, Google-scale anything) without its constraints, scale, or team topology.

- **Remedy**: design from your own forces; document why each borrowed element earns its complexity.

### Premature Optimization / Speculative Generality

Complexity paid today for a requirement that may never arrive.

- **Remedy**: YAGNI (see arch-principles); optimize after measuring; generalize on the second or third real case.

## Object-Design Anti-Patterns

### Anemic Domain Model

Entities reduced to property bags; all logic in "service" classes.

- **Cost**: invariants enforced at call sites (or not), duplication of rules, no domain language in code.
- **Remedy**: push behavior to the data owner (GRASP Information Expert); use value objects; make invalid states unrepresentable (see arch-ddd).

### Partial Object

An object handed around before its invariants hold (two-phase init, "call `Initialize()` after construction").

- **Remedy**: complete construction through factories/builders; no public setters for invariant-bearing fields.

### Static Cling

Utility classes and static state masquerading as design.

- **Cost**: hidden coupling, untestable units, thread-safety hazards, order-dependent tests.
- **Remedy**: make functions pure where possible; convert stateful statics to injected instances; delete `*Util` grab-bags by moving methods to the type they envy.

### Singleton (as anti-pattern)

A global access point disguised as a pattern.

- **When harmful**: hides dependencies, couples everything to one instance, breaks testability.
- **Acceptable**: stateless, or managed by the DI container's lifetime — the pattern's sin is the global accessor, not single instancing.

### BaseBean / Inheritance Abuse

Utility behavior pushed into a base class everything must extend.

- **Remedy**: composition over inheritance; decorators and collaborators instead of `extends` (see arch-principles).

## Process Anti-Patterns

| Anti-Pattern | Description |
|--------------|-------------|
| Analysis Paralysis | Endless modeling, no delivery; fix with timeboxed decisions |
| Design by Committee | No decision owner; fix with explicit decision rights (arch-governance) |
| Ivory Tower Architecture | Designs handed down, never validated in code; fix with architects in the delivery loop |
| Death by Planning | Plan treated as the deliverable; fix with incremental milestones |
| Not Invented Here | Refusing proven solutions; fix with build-vs-buy decision records |
