---
name: arch-review
description: Orchestrate architecture reviews by coordinating specialized review dimensions. Use when performing comprehensive architecture reviews, evaluating system quality, preparing for architecture board reviews, or assessing overall architecture health. Delegates to specialized skills for detailed evaluation.
---

# Architecture Review

Orchestrate comprehensive architecture reviews using specialized skills.

## Workflow

```
1. Understand Context → System purpose, constraints, stakeholders
2. Define Scope → Which dimensions to review?
3. Collect Evidence → Gather information
4. Evaluate Dimensions → Use specialized skills
5. Synthesize Findings → Combine results
6. Generate Report → Structured output
7. Prioritize Actions → Remediation roadmap
```

## Step 1: Understand Context

Gather before reviewing:
- **System purpose**: What business goals does it serve?
- **Key requirements**: Functional and non-functional
- **Constraints**: Budget, timeline, technology, team
- **Stakeholders**: Who cares about the architecture?
- **History**: Previous decisions, known issues, technical debt

## Step 2: Define Scope

Select review dimensions based on context:

| Dimension | Skill | When to Review |
|-----------|-------|----------------|
| **Design Patterns** | arch-review | Always |
| **Security** | arch-security | Always |
| **Performance** | arch-perf | User-facing systems |
| **Resilience** | arch-resilience | Distributed systems |
| **Data** | arch-data | Data-intensive systems |
| **API Design** | arch-api | API-first systems |
| **Testing** | arch-test | Quality-critical systems |
| **Observability** | arch-observability | Production systems |
| **Cloud** | arch-cloud | Cloud-deployed systems |
| **DDD** | arch-ddd | Complex domains |
| **Migration** | arch-migration | Legacy modernization |
| **Metrics** | arch-metrics | Code health assessment |
| **Fitness Functions** | arch-fitness | Automated validation |

## Step 3: Collect Evidence

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

## Step 4: Evaluate Dimensions

### Design Patterns Review

**Positive Patterns to Look For:**
- SOLID principles adherence
- Appropriate use of design patterns (Repository, Strategy, Factory, etc.)
- Clear separation of concerns
- Proper abstraction levels

**Anti-patterns to Detect:**
- God objects/classes doing too much
- Tight coupling between unrelated components
- Circular dependencies
- Magic numbers and hardcoded values
- Anemic domain models

Read `references/design-patterns.md` for detailed guidance.

### Quality Attributes Review

| Attribute | Key Questions | Delegated To |
|-----------|--------------|--------------|
| **Performance** | Response times, throughput | arch-perf |
| **Security** | Authentication, authorization | arch-security |
| **Scalability** | Can it handle growth? | arch-perf |
| **Availability** | Uptime, failure handling | arch-resilience |
| **Maintainability** | Code clarity, modularity | arch-metrics |
| **Testability** | Test coverage, quality | arch-test |

Read `references/quality-attributes.md` for detailed criteria.

### Best Practices Compliance

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

Read `references/best-practices.md` for complete checklist.

### Technical Debt Assessment

**Debt Categories:**
1. **Code Debt**: Quick fixes, workarounds, TODOs
2. **Architecture Debt**: Shortcut designs, missing abstractions
3. **Testing Debt**: Missing tests, low coverage
4. **Documentation Debt**: Missing or outdated docs
5. **Dependency Debt**: Outdated packages, vulnerabilities
6. **Infrastructure Debt**: Manual processes, missing automation

Read `references/tech-debt.md` for scoring methodology.

## Step 5: Synthesize Findings

Combine results from all dimensions:

For each finding:
- **Severity**: Critical / High / Medium / Low
- **Confidence**: High / Medium / Low
- **Impact**: Business / Technical / Both
- **Effort to Fix**: Large / Medium / Small
- **Category**: Which dimension it belongs to

## Step 6: Generate Report

Use template from `assets/review-template.md`.

Report structure:
1. Executive Summary
2. Architecture Overview
3. Findings by Dimension
4. Findings Summary Table
5. Recommendations
6. Remediation Roadmap

## Step 7: Prioritize Actions

Create prioritized remediation plan:
1. **Immediate** (Critical issues): Fix within sprint
2. **Short-term** (High issues): Plan for next quarter
3. **Medium-term** (Medium issues): Add to backlog
4. **Long-term** (Low issues): Consider during major refactors

## Review Types

| Type | Scope | Duration | Output |
|------|-------|----------|--------|
| **Quick Scan** | High-level patterns | 1-2 hours | Summary |
| **Standard** | Full evaluation | 1-2 days | Complete report |
| **Deep Dive** | Specific concern | 3-5 days | Focused analysis |
| **Compliance** | Standards adherence | 1-2 weeks | Audit report |
