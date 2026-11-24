# Design Patterns & Anti-patterns Reference

## Creational Patterns

### Factory Method
**Intent:** Define interface for creating objects, let subclasses decide which class to instantiate.
**When to Use:**
- Class doesn't know what objects to create
- Subclasses decide which objects to create
- You want to localize creation logic

### Abstract Factory
**Intent:** Provide interface for creating families of related objects.
**When to Use:**
- System must be independent of object creation
- System must work with multiple families of objects

### Builder
**Intent:** Separate construction of complex object from representation.
**When to Use:**
- Object has many optional parameters
- You want to avoid telescoping constructors

### Singleton
**Intent:** Ensure class has only one instance.
**When to Use:**
- Single instance needed (config, logger)
**Warning:** Often overused; prefer dependency injection.

## Structural Patterns

### Adapter
**Intent:** Convert interface of class into another interface clients expect.
**When to Use:**
- Integrate third-party libraries with incompatible interfaces
- Legacy code integration

### Facade
**Intent:** Provide unified interface to subsystem.
**When to Use:**
- Simplify complex subsystem usage
- Decouple client from subsystem implementation

### Proxy
**Intent:** Provide surrogate for another object to control access.
**When to Use:**
- Lazy initialization
- Access control
- Logging/caching

## Behavioral Patterns

### Strategy
**Intent:** Define family of algorithms, encapsulate each, make interchangeable.
**When to Use:**
- Multiple algorithms for same operation
- Algorithm selection at runtime

### Observer
**Intent:** Define one-to-many dependency so when one object changes, dependents notified.
**When to Use:**
- Event-driven systems
- Decoupled notification

### Command
**Intent:** Encapsulate request as object.
**When to Use:**
- Undo/redo functionality
- Queue operations
- Logging requests

## Anti-patterns to Detect

### God Object
**Signs:**
- Class does too many things
- High number of methods (>20)
- Multiple responsibilities
- High change frequency

**Impact:** Hard to maintain, test, understand

### Tight Coupling
**Signs:**
- Direct object creation inside classes
- Many dependencies
- Changes ripple across system

**Impact:** Fragile, hard to test, poor reuse

### Circular Dependencies
**Signs:**
- Module A depends on B, B depends on A
- Gradual initialization issues
- Compilation order sensitivity

**Impact:** Initialization problems, unclear ownership

### Magic Numbers/Strings
**Signs:**
- Hardcoded values without explanation
- Repeated literal values
- No symbolic names

**Impact:** Maintenance nightmare, error-prone

### Anemic Domain Model
**Signs:**
- Domain objects with only getters/setters
- Business logic in service classes
- Data objects without behavior

**Impact:** Loses OOP benefits, procedural code

### Spaghetti Code
**Signs:**
- Long methods (>100 lines)
- Deep nesting (>3 levels)
- Goto/break/continue abuse
- No clear structure

**Impact:** Unmaintainable, untestable
