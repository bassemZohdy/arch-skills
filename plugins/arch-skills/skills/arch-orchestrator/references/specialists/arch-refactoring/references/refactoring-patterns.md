# Refactoring Patterns Reference

## Code Smells

### Class-Level

| Smell | Description | Refactoring |
|-------|-------------|-------------|
| **God Class** | Too many responsibilities | Extract Class |
| **Feature Envy** | Uses another class's data | Move Method |
| **Data Clumps** | Same data groups in multiple places | Extract Class |
| **Long Parameter List** | Too many parameters | Introduce Parameter Object |

### Method-Level

| Smell | Description | Refactoring |
|-------|-------------|-------------|
| **Long Method** | Too many lines | Extract Method |
| **Duplicated Code** | Same logic in multiple places | Extract Method |
| **Long Parameter List** | Too many parameters | Introduce Parameter Object |

## Refactoring Catalog

### Composing Methods

| Refactoring | Description |
|-------------|-------------|
| **Extract Method** | Turn code fragment into its own method |
| **Inline Method** | Inverse of Extract Method |
| **Extract Variable** | Name complex expressions |

### Moving Features Between Objects

| Refactoring | Description |
|-------------|-------------|
| **Move Method** | Move method to another class |
| **Move Field** | Move field to another class |
| **Extract Class** | Create new class from existing |
| **Inline Class** | Inverse of Extract Class |

### Organizing Data

| Refactoring | Description |
|-------------|-------------|
| **Replace Type Code with Subclasses** | Replace type code with inheritance |
| **Encapsulate Field** | Make field private with accessors |
| **Replace Data Value with Object** | Turn data into object |

## Refactoring Checklist

- [ ] Tests cover current behavior
- [ ] Small, incremental changes
- [ ] Tests pass after each change
- [ ] Code review after refactoring
- [ ] Documentation updated
