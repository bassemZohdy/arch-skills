---
name: arch-refactoring
description: Guide code and architecture refactoring. Use when identifying code smells, planning refactoring strategies, implementing incremental refactoring, or improving code quality.
---

# Refactoring Architecture

Systematic approach to code and architecture refactoring.

## Workflow

```
1. Identify Smells → What needs improvement?
2. Assess Impact → What's the risk?
3. Plan Strategy → How to refactor safely?
4. Implement Incrementally → Small, testable changes
5. Validate → Ensure behavior preserved
6. Document → Record changes and rationale
```

## Step 1: Code Smells

### Class-Level Smells

| Smell | Description | Refactoring |
|-------|-------------|-------------|
| **God Class** | Too many responsibilities | Extract Class |
| **Feature Envy** | Uses another class's data more than own | Move Method |
| **Data Clumps** | Same data groups in multiple places | Extract Class |
| **Divergent Change** | One class changed for many reasons | Extract Class |
| **Switch Statements** | Complex conditionals | Replace with Polymorphism |

### Method-Level Smells

| Smell | Description | Refactoring |
|-------|-------------|-------------|
| **Long Method** | Too many lines | Extract Method |
| **Duplicated Code** | Same logic in multiple places | Extract Method |
| **Long Parameter List** | Too many parameters | Introduce Parameter Object |
| **Temporary Field** | Field used only in certain cases | Extract Class |
| **Refused Bequest** | Subclass doesn't use parent's methods | Replace Inheritance with Composition |

### Object-Oriented Smells

| Smell | Description | Refactoring |
|-------|-------------|-------------|
| **Inappropriate Intimacy** | Classes know too much about each other | Move Method/Field |
| **Alternative Classes with Different Interfaces** | Similar classes with different names | Unify Interface |
| **Primitive Obsession** | Using primitives instead of objects | Replace with Value Object |
| **Speculative Generality** | Unused abstract classes/interfaces | Remove |
| **Lazy Class** | Class that does too little | Remove or Inline |

## Step 2: Architecture Smells

| Smell | Description | Refactoring |
|-------|-------------|-------------|
| **Big Ball of Mud** | No discernible structure | Extract modules incrementally |
| **God Package** | Package with too many classes | Extract modules |
| **Circular Dependencies** | A depends on B, B depends on A | Introduce interface |
| **Tangled Dependencies** | Spaghetti of dependencies | Apply Dependency Inversion |
| **Stale Layer** | Layer that's never used | Remove or restructure |

## Step 3: Refactoring Strategies

### Incremental Refactoring

| Step | Action |
|------|--------|
| 1 | Write tests for current behavior |
| 2 | Make small change |
| 3 | Run tests |
| 4 | Commit |
| 5 | Repeat |

### Strangler Fig Pattern

```
Legacy System → Facade → New Components
                    ↓
              Gradually Replace
```

### Branch by Abstraction

1. Create abstraction layer
2. Implement new behavior behind abstraction
3. Switch between old and new
4. Remove old implementation

## Step 4: Refactoring Catalog

### Composing Methods

| Refactoring | Description |
|-------------|-------------|
| **Extract Method** | Turn code fragment into its own method |
| **Inline Method** | Inverse of Extract Method |
| **Extract Variable** | Name complex expressions |
| **Inline Temp** | Replace temp with its value |
| **Split Temporary Variable** | Use different variables for different purposes |
| **Replace Method with Method Object** | Move method to its own class |

### Moving Features Between Objects

| Refactoring | Description |
|-------------|-------------|
| **Move Method** | Move method to another class |
| **Move Field** | Move field to another class |
| **Convert Procedural to Object** | Turn procedure into objects |
| **Extract Class** | Create new class from existing |
| **Inline Class** | Inverse of Extract Class |
| **Hide Delegate** | Add delegating methods |

### Organizing Data

| Refactoring | Description |
|-------------|-------------|
| **Replace Type Code with Subclasses** | Replace type code with inheritance |
| **Replace Type Code with State/Strategy** | Replace type code with state pattern |
| **Replace Magic Number with Symbolic Constant** | Name magic numbers |
| **Encapsulate Field** | Make field private with accessors |
| **Replace Data Value with Object** | Turn data into object |
| **Change Value to Reference** | Convert value to reference object |

### Simplifying Conditional Expressions

| Refactoring | Description |
|-------------|-------------|
| **Decompose Conditional** | Extract condition into method |
| **Consolidate Conditional Expression** | Combine similar conditionals |
| **Consolidate Duplicate Conditional Fragments** | Extract common code |
| **Replace Conditional with Polymorphism** | Use inheritance |
| **Introduce Null Object** | Replace null with null object |

### Simplifying Method Calls

| Refactoring | Description |
|-------------|-------------|
| **Rename Method** | Give method better name |
| **Add Parameter** | Add new parameter |
| **Remove Parameter** | Remove unused parameter |
| **Separate Query from Modifier** | Split method into query and modifier |
| **Parameterize Method** | Replace several methods with one |
| **Replace Parameter with Explicit Methods** | Replace parameter with methods |
| **Preserve Whole Object** | Pass whole object instead of parts |
| **Replace Temp with Query** | Extract expression to method |

## Step 5: Refactoring Checklist

- [ ] Tests cover current behavior
- [ ] Small, incremental changes
- [ ] Tests pass after each change
- [ ] Code review after refactoring
- [ ] Documentation updated
- [ ] No new functionality added

## Examples

- Break up a god class handling orders, pricing, and notifications.
- Plan an incremental strangler-fig refactor of a tangled module with tests as a safety net.
- Remove circular dependencies between two packages by extracting an interface.

## Common Gotchas

- Never refactor and change behavior in the same commit; tests must stay green throughout.
- Refactoring without characterization tests on legacy code is just rewriting with extra risk.
- Big-bang refactors stall; ship small reversible steps that each leave the build releasable.

## Further Reading

- `references/awesome-architecture.md` — Curated external articles, videos, libraries, and samples per topic (awesome-architecture.com)

## Related Skills

- **arch-metrics** - Measuring smells and tracking improvement
- **arch-migration** - Larger-scale system modernization
- **arch-test** - The safety net refactoring depends on

## Refactoring Review Template

```markdown
## Refactoring Review: [Component]

### Code Smells Identified
| Smell | Location | Impact |
|-------|----------|--------|

### Refactoring Plan
| Smell | Refactoring | Risk | Priority |
|-------|-------------|------|----------|

### Progress
| Refactoring | Status | Tests Pass |
|-------------|--------|------------|

### Metrics Before/After
| Metric | Before | After |
|--------|--------|-------|
```
