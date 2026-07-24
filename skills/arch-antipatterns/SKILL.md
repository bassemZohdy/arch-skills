---
name: arch-antipatterns
description: Detect and remediate architecture anti-patterns and code smells. Use when identifying big ball of mud, god objects, leaky abstractions, static cling, anemic domain models, distributed monoliths, or reviewing code for structural smells and their refactoring paths.
---

# Architecture Anti-Patterns

Systematic approach to detecting, assessing, and remediating anti-patterns and code smells.

## Workflow

```
1. Detect → Find anti-pattern signals
2. Confirm → Verify it is really the anti-pattern
3. Assess Impact → What does it cost today?
4. Choose Remediation → Refactor, contain, or accept
5. Execute Safely → Incremental, tested steps
6. Prevent Recurrence → Fitness functions, reviews
```

## Step 1: Structural Anti-Patterns

| Anti-Pattern | Signal | Core Problem |
|--------------|--------|--------------|
| **Big Ball of Mud** | No visible structure; everything calls everything | Uncontrolled dependencies; change is archaeology |
| **God Object** | One class knows/does everything; others are data bags | Centralized intelligence, no cohesion |
| **Distributed Monolith** | Services deployed independently but must ship together | Worst of both worlds: distributed cost, monolith coupling |
| **Leaky Abstraction** | Callers must know implementation details to use it | Abstraction adds cost without hiding anything |
| **Static Cling** | Global/static state and utility methods everywhere | Hidden dependencies, untestable, non-reentrant |
| **Partial / Anemic Object** | "Domain" classes that are getters/setters only | Logic scattered in services; invariants unenforced |

## Step 2: Detection Signals

### Big Ball of Mud

- Cyclic dependencies between modules; no layering to enforce.
- "Where does X happen?" has no answer shorter than a call-graph dump.
- New features are added by pattern-matching nearby code, not by design.

### God Object

- One class with dozens of dependencies and methods; name like `Manager`, `Util`, `Helper`, `Common`.
- Most changes in the repo touch it; merge conflicts concentrate there.

### Leaky Abstraction

- Callers catch implementation-specific exceptions, tune implementation-specific knobs, or depend on call order.
- "All non-trivial abstractions, to some degree, are leaky" (Spolsky) — the question is whether the leak forces callers to care.

### Static Cling

- Business logic reachable only through static methods; state in static fields.
- Tests must run in sequence; parallelizing breaks them.

### Anemic Domain Model

- Entities expose every field; "services" contain all the if/else.
- Invariants enforced (or forgotten) at every call site instead of in the object.

## Step 3: Code Smells (Unit Level)

| Smell | Signal | Usual Remedy |
|-------|--------|--------------|
| **Long Method** | Can't see it on one screen | Extract method |
| **Large Class** | Too many fields/responsibilities | Extract class |
| **Feature Envy** | Method uses another object's data more than its own | Move method |
| **Data Clumps** | Same field group travels together | Introduce parameter object |
| **Primitive Obsession** | Domain concepts as strings/ints | Introduce value object |
| **Shotgun Surgery** | One change, many small edits everywhere | Move/inline to consolidate |
| **Divergent Change** | One class changed for many reasons | Split by reason (SRP) |
| **Speculative Generality** | Abstractions serving hypothetical cases | Collapse hierarchy, inline |
| **Middle Man** | Class only delegates | Remove middle man |
| **Switch Statements** | Repeated type dispatch | Polymorphism |

See `references/code-smells.md` for the full catalog.

## Step 4: Impact Assessment

| Question | Why it matters |
|----------|----------------|
| How often does this area change? | Hot spots multiply anti-pattern cost |
| What breaks when it changes? | Blast radius drives urgency |
| Is it growing? | Anti-patterns compound; a god object only gets bigger |
| Who depends on it? | External consumers constrain remediation options |

Prioritize by **change frequency × coupling radius**, not by ugliness.

## Step 5: Remediation Strategies

| Anti-Pattern | Remediation Path |
|--------------|------------------|
| Big Ball of Mud | Draw the intended boundaries, then move one responsibility at a time behind them; add architecture tests to stop regression |
| God Object | Extract cohesive clusters (one per responsibility) behind its façade; shrink it to a controller |
| Distributed Monolith | Re-merge into a modular monolith, or redraw service boundaries around business capabilities and data ownership |
| Leaky Abstraction | Redefine the contract in caller terms; wrap the implementation so its concepts never escape |
| Static Cling | Introduce instance seams, inject dependencies, push state to parameters or owned objects |
| Anemic Model | Move behavior onto the entity that owns the data (Information Expert); make invalid states unrepresentable |

Rules of engagement:

- **Never big-bang.** Strangler-fig incremental moves with tests green at every step (see arch-refactoring).
- **Containment is valid.** If a muddy area is stable and rarely touched, fence it off and stop touching it.
- **Acceptance is valid.** Document the decision with an ADR (see arch-decision) when remediation cost exceeds benefit.

## Step 6: Prevention

- Encode boundaries as automated architecture/fitness tests in CI (see arch-fitness).
- Review for smells on change, not on schedule — the diff is where they enter.
- Track known anti-patterns in a debt register with owners and revisit dates.

## Examples

- Assess whether a set of microservices is actually a distributed monolith and plan the re-merge.
- Find god-object candidates in a codebase and propose an extraction sequence.
- Review a "clean architecture" codebase for leaky abstractions between layers.
- Decide which code smells in a legacy module are worth fixing before adding a feature.

## Common Gotchas

- Not every ugly thing is an anti-pattern; an anti-pattern is a *recurring* bad solution that looked like a good idea.
- Microservices, layers, and patterns can themselves become anti-patterns when applied without the problem they solve.
- Refactoring without tests in place is how anti-patterns reproduce.
- Calling everything "tech debt" hides which items actually cost money; name the anti-pattern and its impact.

## Further Reading

- `references/awesome-architecture.md` — Curated external articles, videos, libraries, and samples per topic (awesome-architecture.com)

## Related Skills

- **arch-principles** - The principles these anti-patterns violate
- **arch-review** - Where detection happens at scale
- **arch-refactoring** - Safe execution of the remediation
- **arch-fitness** - Automated prevention in CI
- **arch-ddd** - Rich vs anemic domain models

## Anti-Pattern Assessment Template

```markdown
## Anti-Pattern Assessment: [Component]

### Detected
| Anti-Pattern | Location | Evidence | Severity |
|--------------|----------|----------|----------|

### Impact
- Change frequency: [high/med/low]
- Coupling radius: [modules affected]
- Trend: [growing/stable/shrinking]

### Decision
| Option | Cost | Benefit | Chosen? |
|--------|------|---------|---------|
| Refactor | | | |
| Contain | | | |
| Accept (ADR) | | | |

### Remediation Plan
1. [Incremental step] — [test coverage needed]
```
