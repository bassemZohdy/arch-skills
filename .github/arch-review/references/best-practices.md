# Best Practices Reference

## SOLID Principles

### Single Responsibility Principle (SRP)
**Statement:** A class should have only one reason to change.

**Check:**
- [ ] Class has one clear purpose
- [ ] Methods are related to single responsibility
- [ ] Changes don't affect unrelated functionality

**Violation Signs:**
- Class does multiple things
- Changes ripple across unrelated features
- Hard to describe class purpose in one sentence

### Open/Closed Principle (OCP)
**Statement:** Open for extension, closed for modification.

**Check:**
- [ ] New features added without modifying existing code
- [ ] Extension points provided (interfaces, abstract classes)
- [ ] Plugin architecture used where appropriate

**Violation Signs:**
- Adding feature requires modifying existing classes
- Large switch/case statements
- Frequent changes to stable code

### Liskov Substitution Principle (LSP)
**Statement:** Subtypes must be substitutable for their base types.

**Check:**
- [ ] Subclasses honor base class contracts
- [ ] No unexpected behavior in subclasses
- [ ] Preconditions not strengthened, postconditions not weakened

**Violation Signs:**
- Subclass throws unexpected exceptions
- Subclass changes expected behavior
- is-a relationship is questionable

### Interface Segregation Principle (ISP)
**Statement:** Many specific interfaces better than one general-purpose.

**Check:**
- [ ] Interfaces are focused and small
- [ ] Clients don't depend on methods they don't use
- [ ] Interface hierarchies are logical

**Violation Signs:**
- Fat interfaces with many methods
- Implementations with empty methods
- Forced implementation of unused methods

### Dependency Inversion Principle (DIP)
**Statement:** Depend on abstractions, not concretions.

**Check:**
- [ ] High-level modules don't depend on low-level modules
- [ ] Both depend on abstractions
- [ ] Abstractions don't depend on details

**Violation Signs:**
- Direct instantiation of concrete classes
- Tight coupling to frameworks
- Hard to test due to concrete dependencies

## DRY (Don't Repeat Yourself)

**Check:**
- [ ] No duplicate code blocks
- [ ] Business rules defined once
- [ ] Configuration centralized
- [ ] Reusable components extracted

**Violation Signs:**
- Copy-paste code
- Similar logic in multiple places
- Same business rule defined differently

## KISS (Keep It Simple, Stupid)

**Check:**
- [ ] Code is readable and straightforward
- [ ] No unnecessary complexity
- [ ] Simple solution preferred over clever one
- [ ] YAGNI (You Aren't Gonna Need It) applied

**Violation Signs:**
- Over-engineering
- Premature optimization
- Unnecessary abstractions

## Separation of Concerns

**Check:**
- [ ] Business logic separate from infrastructure
- [ ] UI separate from business rules
- [ ] Data access separate from business logic
- [ ] Cross-cutting concerns handled separately

**Violation Signs:**
- Business logic in UI layer
- SQL in business classes
- Mixed concerns in single module

## Error Handling

**Check:**
- [ ] Errors handled at appropriate level
- [ ] Exception hierarchy used
- [ ] Meaningful error messages
- [ ] No swallowed exceptions
- [ ] Errors logged with context

**Violation Signs:**
- Empty catch blocks
- Generic exception handling
- Errors silently ignored

## Logging and Monitoring

**Check:**
- [ ] Structured logging (JSON)
- [ ] Correlation IDs for tracing
- [ ] Appropriate log levels
- [ ] Sensitive data not logged
- [ ] Metrics exposed

**Violation Signs:**
- Unstructured logs
- Missing context
- Debug logs in production
- PII in logs

## Configuration Management

**Check:**
- [ ] Configuration externalized
- [ ] Environment-specific configs separate
- [ ] Secrets not in code
- [ ] Configuration validation on startup

**Violation Signs:**
- Hardcoded values
- Config in source control
- No validation
- Default credentials

## API Design

**Check:**
- [ ] RESTful conventions followed
- [ ] Consistent naming
- [ ] Proper HTTP status codes
- [ ] Versioning strategy
- [ ] Documentation (OpenAPI/Swagger)

**Violation Signs:**
- Inconsistent naming
- Wrong HTTP methods
- Missing error responses
- No versioning
