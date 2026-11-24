# Design Principles Deep Dive

Load this when applying or evaluating SOLID, DRY, KISS, YAGNI, CQS, or fail-fast design.

## SOLID in Practice

### Single Responsibility Principle

A unit should have one reason to change — meaning one actor whose requests can force a change.

- **Detect**: describe the class in one sentence without "and". If you can't, split it.
- **Apply**: separate orchestration from policy from mechanism; keep I/O at the edges.
- **Trap**: splitting so finely that one logical change still touches five files (cohesion loss).

### Open/Closed Principle

Add behavior by adding code, not by editing working code.

- **Mechanisms**: polymorphism, strategy injection, plugin registration, event handlers.
- **Apply where**: variation actually occurs (third integration, second discount type) — not speculatively.
- **Trap**: abstractions with one implementation are not OCP compliance, just indirection.

### Liskov Substitution Principle

A subtype must be usable wherever the base type is expected, without surprising the caller.

- **Rules**: preconditions no stronger, postconditions no weaker, invariants preserved.
- **Detect**: `Square extends Rectangle`, subtype throwing on a base-class method, callers doing `isinstance` checks.
- **Fix**: extract a common abstraction instead of inheriting, or compose.

### Interface Segregation Principle

Clients should not depend on methods they do not call.

- **Detect**: fat interfaces, `NotImplementedException`/`pass` bodies, mocking pain in tests.
- **Fix**: split into role interfaces named for the client capability (`IRead`, `IWrite`), not the implementation.

### Dependency Inversion Principle

High-level policy should not depend on low-level detail; both depend on abstractions.

- **Rule of thumb**: business logic must not import frameworks, databases, HTTP, or UI.
- **Wiring**: the composition root (startup) owns all `new` of infrastructure.
- **Trap**: an interface per concrete class in the same assembly inverts nothing — the interface must be owned by the caller's layer.

## Simplicity Principles

### DRY — Don't Repeat Yourself

Every piece of knowledge has a single, authoritative representation.

- Duplicated *knowledge* (a business rule in two places) is the violation.
- Coincidentally identical code that answers to different actors will diverge — do not unify it.
- Across service/context boundaries, prefer duplication over shared libraries that couple release cycles.

### KISS — Keep It Simple, Stupid

- Prefer the design a new team member explains correctly after one read.
- Measure simplicity by change cost, not line count.

### YAGNI — You Aren't Gonna Need It

- Do not build for hypothetical requirements; build so the likely ones are cheap to add later.
- Delete unused configuration, extension points, and parameters.
- "Simple to change later" beats "already generalized" in almost every cost model.

## Behavioral Principles

### Command-Query Separation (CQS)

- A method either performs an action (command) or returns data (query), never both.
- Exceptions: popping a stack, compare-and-set — document them deliberately.
- Architecture-level extension is CQRS; see `arch-event`.

### Fail-Fast

- Detect errors at the earliest possible point, close to their cause.
- Validate at system boundaries; crash on violated invariants in-process instead of corrupting state.
- Combine with defensive validation only at trust boundaries — fail-fast inside, defensive outside.

### Principle of Least Astonishment

- A component should behave the way its name, types, and context imply.
- Surprising side effects in getters, hidden network calls in property access, and clever operator overloads all violate it.

## Cross-Cutting Concerns

Logging, auth, validation, retries, and transactions cut across layers.

| Approach | When |
|----------|------|
| Decorator/interceptor around handlers | Uniform policies (logging, transactions) |
| Middleware pipeline | Request/response concerns |
| Explicit calls in domain code | When the concern IS business logic (e.g., auditing) |

Keep cross-cutting code out of domain types; wire it at the boundary.
