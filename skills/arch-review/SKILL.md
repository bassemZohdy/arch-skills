---
name: arch-review
description: "Review architecture design fitness across patterns, quality attributes, trade-offs, risks and technical debt. Use for architecture reviews, design reviews, board assessments, quality-attribute analysis and specialist review routing. Use arch-evaluate for Deterministic Architecture Process completeness and artifact evidence."
---

# Architecture Review

Orchestrate comprehensive architecture reviews using specialized skills.

## Workflow

Keep the assessed baseline read-only. Resolve bundled specialists using the
outer package's package-catalog.json; load only relevant instructions/resources.
For DAP work read `framework/contribution-contract.md` from that package root
and include target IDs, baseline/hash, evidence, uncertainty and verification
actions in `assets/review-template.md`. A recommendation is not human approval.
Report process completeness separately through arch-evaluate; do not repair
evidence gaps during review or require full DAP for a narrow standalone review.

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
| **DevOps & Deployment** | arch-devops | CI/CD and release health |
| **AI Systems** | arch-ai | Systems embedding LLMs or agents |

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

Classify each observation as confirmed evidence, an assumption, or an evidence
gap. Record the source locator and the consequence of leaving the gap unresolved;
do not turn a polished diagram or an author's confidence into proof.

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

## Review output contract

For every finding, include the evidence locator, affected quality attribute or
requirement, impact, likelihood or confidence, recommended action, owner or
decision authority, and a verification signal. Separate blockers from risks and
opportunities, and state which findings require a new ADR or human disposition.

## Review Types

| Type | Scope | Duration | Output |
|------|-------|----------|--------|
| **Quick Scan** | High-level patterns | 1-2 hours | Summary |
| **Standard** | Full evaluation | 1-2 days | Complete report |
| **Deep Dive** | Specific concern | 3-5 days | Focused analysis |
| **Compliance** | Standards adherence | 1-2 weeks | Audit report |

## Examples

- Review a monolith with high coupling, slow tests, and missing observability.
- Assess a microservices platform for resilience, security, and deployment risk.
- Prepare a concise architecture board summary with evidence-backed findings.

## Common Gotchas

- Tie every finding to evidence and impact; do not report symptoms without consequences.
- Separate implementation bugs from architectural issues unless the design causes the bug.
- Record confidence and effort so remediation can be prioritized without re-reading the full report.

## Further Reading

- `references/awesome-architecture.md` — Curated external articles, videos, libraries, and samples per topic (awesome-architecture.com)
- `references/review-methods.md` — Architecture Review Methods

## Related Skills

- **arch-doc** - Generate or update the documentation a review assesses against
- **arch-decision** - Capture review outcomes as architecture decision records
- **arch-fitness** - Turn review findings into automated, continuous checks
- **arch-governance** - Track review-driven remediation and standards adoption
- **arch-orchestrator** - Feed review results back into coordinated redesign
