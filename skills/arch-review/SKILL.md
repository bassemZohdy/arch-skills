---
name: arch-review
description: Review and validate software architecture implementations against best practices, design patterns, quality attributes, and industry standards. Use when evaluating an existing architecture, performing architecture reviews, identifying anti-patterns, assessing technical debt, checking compliance with architectural principles, or preparing for architecture board reviews.
---

# Architecture Review & Validation

Systematically review and validate software architecture implementations against established criteria.

## Workflow

```
1. Understand Context → System purpose, constraints, stakeholders
2. Collect Evidence → Codebase analysis, documentation review
3. Evaluate Dimensions → Patterns, quality attributes, practices, debt
4. Score & Rate → Severity ratings for findings
5. Generate Report → Structured findings with recommendations
6. Prioritize Actions → Remediation roadmap
```

## Step 1: Understand Context

Gather before reviewing:
- **System purpose**: What business goals does it serve?
- **Key requirements**: Functional and non-functional
- **Constraints**: Budget, timeline, technology, team
- **Stakeholders**: Who cares about the architecture?
- **History**: Previous decisions, known issues, technical debt

## Step 2: Collect Evidence

Analyze the codebase and documentation:

1. **Structure Analysis**
   - Directory organization and module boundaries
   - Dependency graph (inbound/outbound)
   - Package coupling metrics

2. **Code Analysis**
   - Class/component responsibilities
   - Interface usage and abstraction levels
   - Error handling patterns

3. **Configuration Analysis**
   - Environment configurations
   - Feature flags and toggles
   - Deployment patterns

4. **Documentation Review**
   - Existing architecture docs
   - ADRs and decision logs
   - API specifications

## Step 3: Evaluate Dimensions

Review across four dimensions. Read reference files for detailed checklists:
- `references/design-patterns.md`
- `references/quality-attributes.md`
- `references/best-practices.md`
- `references/tech-debt.md`

### Fitness Functions Assessment

Check if the system has architecture fitness functions:
- Are architectural decisions automated and testable?
- Are there ArchUnit/ArchUnitTS tests for dependency rules?
- Are quality gates configured in CI/CD?
- Are performance benchmarks automated?

Read `references/fitness-functions.md` for guidance on creating and evaluating fitness functions.

### 3.1 Design Patterns & Anti-patterns

**Positive Patterns to Look For:**
- SOLID principles adherence
- appropriate use of design patterns (Repository, Strategy, Factory, etc.)
- Clear separation of concerns
- Proper abstraction levels

**Anti-patterns to Detect:**
- God objects/classes doing too much
- Tight coupling between unrelated components
- Circular dependencies
- Magic numbers and hardcoded values
- Anemic domain models

### 3.2 Quality Attributes

Evaluate each relevant quality attribute:

| Attribute | Key Questions | Metrics |
|-----------|--------------|---------|
| **Performance** | Response times, throughput, resource usage | Latency, CPU/memory utilization |
| **Scalability** | Can it handle growth? Horizontal vs vertical? | Load test results, bottleneck analysis |
| **Security** | Authentication, authorization, data protection | Vulnerability scan results, OWASP compliance |
| **Availability** | Uptime requirements, failure handling | SLA compliance, recovery time |
| **Maintainability** | Code clarity, modularity, testability | Code coverage, complexity metrics |
| **Extensibility** | How easy to add new features? | Coupling metrics, plugin points |

### 3.3 Best Practices Compliance

**SOLID Principles:**
- [ ] Single Responsibility: Each class has one reason to change
- [ ] Open/Closed: Open for extension, closed for modification
- [ ] Liskov Substitution: Subtypes are substitutable
- [ ] Interface Segregation: Many specific interfaces over general ones
- [ ] Dependency Inversion: Depend on abstractions, not concretions

**Additional Practices:**
- [ ] DRY (Don't Repeat Yourself)
- [ ] KISS (Keep It Simple, Stupid)
- [ ] YAGNI (You Aren't Gonna Need It)
- [ ] Separation of Concerns
- [ ] Composition over Inheritance
- [ ] Fail Fast and Gracefully
- [ ] Defensive Programming at Boundaries

### 3.4 Technical Debt Assessment

Identify and categorize technical debt:

**Debt Categories:**
1. **Code Debt**: Quick fixes, workarounds, TODOs
2. **Architecture Debt**: Shortcut designs, missing abstractions
3. **Testing Debt**: Missing tests, low coverage, flaky tests
4. **Documentation Debt**: Missing or outdated docs
5. **Dependency Debt**: Outdated packages, security vulnerabilities
6. **Infrastructure Debt**: Manual processes, missing automation

**Scoring:**
- **Critical**: Blocks features or causes incidents
- **High**: Significant impact on velocity or quality
- **Medium**: Moderate impact, should be addressed soon
- **Low**: Minor issues, address opportunistically

## Step 4: Score & Rate

For each finding:
- **Severity**: Critical / High / Medium / Low
- **Confidence**: High / Medium / Low (based on evidence)
- **Impact**: Business / Technical / Both
- **Effort to Fix**: Large / Medium / Small

## Step 5: Generate Report

Use template from `assets/review-template.md`.

Report structure:
1. Executive Summary
2. Architecture Overview
3. Findings by Dimension
4. Findings Summary Table
5. Recommendations
6. Remediation Roadmap

## Step 6: Prioritize Actions

Create prioritized remediation plan:
1. **Immediate** (Critical issues): Fix within sprint
2. **Short-term** (High issues): Plan for next quarter
3. **Medium-term** (Medium issues): Add to backlog
4. **Long-term** (Low issues): Consider during major refactors

## Review Types

| Type | Scope | Duration | Output |
|------|-------|----------|--------|
| **Quick Scan** | High-level patterns, obvious issues | 1-2 hours | Summary with key findings |
| **Standard Review** | Full dimension evaluation | 1-2 days | Complete review report |
| **Deep Dive** | Specific concern (security, performance) | 3-5 days | Focused analysis |
| **Compliance Audit** | Standards adherence | 1-2 weeks | Audit report |
