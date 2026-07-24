# Principles Checklist

Quick pass/fail checklist for design reviews. Copy into review notes.

## Simplicity

- [ ] No abstraction with a single implementation "for later" (YAGNI)
- [ ] No business rule encoded in two places (DRY)
- [ ] A new team member can explain each module in one sentence (KISS)
- [ ] Dead configuration and unused extension points deleted

## SOLID

- [ ] Every class states its single responsibility without "and" (SRP)
- [ ] New behavior is added by new code, not edits to working code (OCP)
- [ ] No subtype weakens a base-type guarantee (LSP)
- [ ] No client forced to implement methods it does not use (ISP)
- [ ] Business logic imports no framework, DB, HTTP, or UI packages (DIP)

## Coupling & Cohesion

- [ ] No module reaches inside another's internals (content coupling)
- [ ] No shared mutable global state (common coupling)
- [ ] Interfaces carry only the data needed (data coupling)
- [ ] Each unit's members serve one purpose (functional cohesion)
- [ ] High-afferent modules are the most stable ones

## Boundaries & Failure

- [ ] Validation happens at trust boundaries; invariants fail fast inside
- [ ] Commands do not return data; queries do not mutate (CQS)
- [ ] Consistency/availability stance documented per data flow (CAP/PACELC)
- [ ] Domain types carry no persistence annotations or SQL-shaped design
- [ ] Composition used instead of inheritance hierarchies deeper than two levels

## Scoring

| Score | Meaning |
|-------|---------|
| 18–20 checked | Healthy — keep habits |
| 13–17 | Localized violations — schedule refactors |
| <13 | Structural debt — plan remediation with arch-refactoring |
