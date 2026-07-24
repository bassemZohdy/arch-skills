# Code Smells Catalog

Load this when reviewing code at the unit level and mapping smells to refactorings.

A smell is a *surface indication* that usually corresponds to a deeper design problem — not a conviction. Judge each in context.

## Bloaters

Things that grow until they are unmanageable.

| Smell | Signal | Refactoring |
|-------|--------|-------------|
| Long Method | Doesn't fit one screen; comment-delimited sections | Extract Method |
| Large Class | Many fields, prefixes hinting at sub-groups | Extract Class / Subclass |
| Primitive Obsession | Domain ideas as string/int; validation repeated | Replace Data Value with Object (value object) |
| Long Parameter List | 4+ params, or same group recurring | Introduce Parameter Object; Preserve Whole Object |
| Data Clumps | Same fields travel together everywhere | Extract Class for the clump |

## Object-Orientation Abusers

| Smell | Signal | Refactoring |
|-------|--------|-------------|
| Switch Statements | Same type-switch in several places | Replace Conditional with Polymorphism |
| Temporary Field | Fields only set in some scenarios | Extract Class for the scenario |
| Refused Bequest | Subclass ignores inherited members | Replace Inheritance with Delegation |
| Alternative Classes, Different Interfaces | Same job, different method names | Rename / unify interfaces |
| Parallel Inheritance Hierarchies | Every subclass of A needs a subclass of B | Move Method/Field to collapse one hierarchy |

## Change Preventers

| Smell | Signal | Refactoring |
|-------|--------|-------------|
| Divergent Change | One class changed for many unrelated reasons | Extract Class per reason (SRP) |
| Shotgun Surgery | One change forces many small edits everywhere | Move Method/Field, Inline Class to consolidate |
| Parallel Change (connascence) | Two places must always change together | Consolidate or codify the relationship |

## Dispensables

| Smell | Signal | Refactoring |
|-------|--------|-------------|
| Comments | Comment explains what code should say | Extract/Rename so code self-describes |
| Duplicate Code | Same structure in two places | Extract Method/Class; Template Method |
| Lazy Class | Class doing too little | Inline Class |
| Data Class | Fields + accessors only | Move Method behavior in; encapsulate fields |
| Dead Code | Unreachable/unused | Delete (YAGNI) |
| Speculative Generality | Abstract hooks with one user | Collapse Hierarchy; Inline |

## Couplers

| Smell | Signal | Refactoring |
|-------|--------|-------------|
| Feature Envy | Method touches another object's data constantly | Move Method |
| Inappropriate Intimacy | Classes digging in each other's privates | Move Method/Field; Change Bidirectional to Unidirectional |
| Message Chains | `a.b().c().d()` trains | Hide Delegate |
| Middle Man | Class only forwards | Remove Middle Man; Inline |
| Incomplete Library Class | Library almost does what's needed | Introduce Foreign Method / Local Extension |

## Test Smells

| Smell | Signal |
|-------|--------|
| Order-dependent tests | Pass alone, fail in suite (static state — see Static Cling) |
| Test logic in production code | `if (testing)` branches |
| Overmocked tests | Test mirrors implementation, breaks on refactor |
| Assertion roulette | Many asserts, no idea which failed |

## Using the Catalog

1. Name the smell precisely — "Feature Envy toward `Order`" beats "this method is ugly".
2. Find the *root* smell: a Long Method full of Feature Envy usually resolves by Move Method, not Extract Method.
3. Apply the smallest refactoring that removes the root smell; keep tests green (see arch-refactoring).
4. Escalate recurring patterns of smells to the anti-pattern level — repeated anemic models are an architecture problem, not a method problem.
