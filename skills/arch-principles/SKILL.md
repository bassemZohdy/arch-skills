---
name: arch-principles
description: Apply software design principles. Use when evaluating or applying SOLID, GRASP, DRY, KISS, YAGNI, coupling and cohesion, CQS, CAP theorem, IoC/DI, composition over inheritance, encapsulation, or fail-fast design.
---

# Architecture Design Principles

Systematic approach to applying and evaluating fundamental design principles.

## Workflow

```
1. Identify Concern → What quality is at risk?
2. Select Principles → Which principles apply?
3. Evaluate Current State → Where are violations?
4. Apply Principle → Refactor toward the principle
5. Verify → Confirm the quality improved
6. Document → Record principle decisions
```

## Step 1: Principle Categories

### Simplicity Principles

| Principle | Statement | Violation Signal |
|-----------|-----------|------------------|
| **KISS** | Keep it simple, stupid | Needlessly clever abstractions |
| **YAGNI** | You aren't gonna need it | Unused "flexibility" hooks |
| **DRY** | Don't repeat yourself | Copy-pasted logic drifting apart |

### Coupling & Cohesion

| Principle | Statement | Violation Signal |
|-----------|-----------|------------------|
| **High Cohesion** | Related behavior stays together | Classes with unrelated methods |
| **Low Coupling** | Minimize dependencies between units | Change ripples across modules |
| **Tell, Don't Ask** | Objects act on their own data | Chains of getters then logic |

### Abstraction Principles

| Principle | Statement | Violation Signal |
|-----------|-----------|------------------|
| **Encapsulation** | Hide internal state and decisions | Public fields, leaked invariants |
| **Dependency Inversion** | Depend on abstractions, not concretions | High-level code importing infrastructure |
| **Interface Segregation** | Small, client-specific interfaces | Fat interfaces, empty implementations |
| **Composition over Inheritance** | Assemble behavior, don't inherit it | Deep, fragile class hierarchies |

## Step 2: SOLID

| Letter | Principle | Core Rule |
|--------|-----------|-----------|
| **S** | Single Responsibility | One reason to change per unit |
| **O** | Open/Closed | Open for extension, closed for modification |
| **L** | Liskov Substitution | Subtypes must honor the base contract |
| **I** | Interface Segregation | No client forced to depend on unused methods |
| **D** | Dependency Inversion | Both levels depend on abstractions |

### Smell → Principle Mapping

| Smell | Violated Principle |
|-------|--------------------|
| God class touching everything | SRP |
| Switch on type to add behavior | OCP |
| Subtype throws on inherited method | LSP |
| `NotImplementedException` stubs | ISP |
| `new Database()` inside business logic | DIP |

## Step 3: GRASP

General Responsibility Assignment Software Patterns — who gets the responsibility?

| Pattern | Question Answered |
|---------|-------------------|
| **Information Expert** | Give it to whoever has the data |
| **Creator** | B creates A if B has the init data, records A, or closely uses A |
| **Controller** | First object beyond the UI layer handling a system operation |
| **Low Coupling** | Assign to keep dependencies low |
| **High Cohesion** | Assign to keep responsibilities focused |
| **Polymorphism** | Handle type-based variation with polymorphic operations |
| **Pure Fabrication** | Invent a service class when no domain object fits |
| **Indirection** | Insert an intermediate to decouple two units |
| **Protected Variations** | Wrap instability behind a stable interface |

## Step 4: Distributed-System Principles

### CAP Theorem

Under a network **Partition**, choose between **Consistency** and **Availability**:

| Choice | Behavior | Typical Use |
|--------|----------|-------------|
| **CP** | Reject/stale-proof responses during partition | Payments, inventory |
| **AP** | Serve possibly-stale data, reconcile later | Feeds, catalogs, sessions |

- CAP only bites during partitions; normal operation trades latency vs consistency (PACELC).
- Per-operation choice, not a per-system badge.

### Command-Query Separation (CQS)

- **Commands** change state, return nothing.
- **Queries** return data, change nothing.
- Foundation for CQRS at the architecture level (see arch-event).

## Step 5: Applying Principles

### Evaluation Checklist

| Question | If No |
|----------|-------|
| Can I name this unit's single responsibility? | Split it (SRP) |
| Does a change require edits in many modules? | Indirection or expert violation |
| Are there abstractions with one implementation "for later"? | YAGNI — delete |
| Does business logic import frameworks/infrastructure? | DIP violation |
| Is the same rule encoded in two places? | DRY violation |

### Principle Conflict Resolution

| Conflict | Resolution |
|----------|------------|
| DRY vs decoupling | Duplicate across boundaries; never couple two bounded contexts to share code |
| KISS vs flexibility | Start simple; add indirection only when the second case arrives |
| Encapsulation vs testability | Test through the public contract, not by exposing internals |
| Consistency vs availability | Decide per operation from business cost of staleness |

## Examples

- Review a service class to find SOLID violations and propose refactors.
- Decide whether a read path can be eventually consistent using CAP/PACELC reasoning.
- Apply GRASP to assign responsibilities when extracting a new domain service.
- Push back on speculative abstraction layers using YAGNI and KISS.

## Common Gotchas

- Principles are means to qualities (changeability, testability), not ends — a "principled" design that is harder to change is a failure.
- DRY is about knowledge duplication, not identical-looking code; coincidental similarity is not duplication.
- Over-applying DIP (interface for every class) adds indirection without decoupling anything real.
- CAP is not "pick two of three" in general — only during partitions.

## Further Reading

- `references/awesome-architecture.md` — Curated external articles, videos, libraries, and samples per topic (awesome-architecture.com)
- `references/design-principles.md` — Design Principles Deep Dive
- `references/grasp-coupling-cap.md` — GRASP, Coupling & Cohesion, CAP

## Related Skills

- **arch-patterns** - Architecture-level structures built on these principles
- **arch-antipatterns** - What violations of these principles look like
- **arch-review** - Where principle evaluation gets applied
- **arch-refactoring** - Fixing violations safely
- **arch-ddd** - Persistence ignorance and rich domain models

## Principle Evaluation Template

```markdown
## Principle Evaluation: [Component]

### Findings
| Location | Principle | Violation | Severity |
|----------|-----------|-----------|----------|

### Conflicts
| Principle A | Principle B | Decision | Rationale |
|-------------|-------------|----------|-----------|

### Recommended Refactorings
1. [Change] — restores [principle]
```
