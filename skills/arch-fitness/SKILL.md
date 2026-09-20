---
name: arch-fitness
description: Create architecture fitness functions, automated guardrails, and architecture automation. Use when encoding architectural decisions as CI/CD checks, dependency rules, runtime validations, architecture unit tests, or automating documentation generation and compliance checks that keep constraints enforced over time.
---

# Architecture Fitness Functions

Automated checks that verify architectural decisions are maintained.

**Source:** [Building Evolutionary Architectures](https://www.oreilly.com/library/view/building-evolutionary-architectures/9781491986368/) by Ford, Parsons, Kua

## DAP contribution

For a DAP invocation, read `framework/contribution-contract.md` from the outer
package root (the repository root in a source checkout). Keep standalone tasks
within their requested scope. Use `assets/template.md` and record protected decision/requirement, rule ID and scope, measurement, tolerated variance, owner, evidence output, failure action and exception expiry.
Return evidence-linked proposals and VER plans, not invented approvals or delivery proof.

## Workflow

```
1. Identify Decisions → Extract automatable rules from ADRs
2. Choose Approach → Pick static/dynamic, atomic/holistic validation
3. Implement Tests → Write the checks (ArchUnit, benchmarks, scans)
4. Integrate into CI/CD → Run every commit/build
5. Monitor and Alert → Surface failures, review and evolve rules
```

## What Are Fitness Functions?

Fitness functions are objective assessments, automated where practical that evaluate architectural characteristics. They:
- Make architecture testable and enforceable
- Run continuously (every commit, every build)
- Provide pass/fail feedback
- Scale governance without bottlenecks

Each function should name the ADR or requirement it protects, its owner, scope,
measurement definition, tolerated variance, failure action, evidence output and
expiry/review trigger. A rule that is noisy, unactionable or disconnected from a
decision becomes ignored policy.

## Types of Fitness Functions

### Atomic vs Holistic

| Type | Scope | Example |
|------|-------|---------|
| **Atomic** | Single architectural attribute | "Domain packages do not import infrastructure" |
| **Holistic** | Multiple attributes together | "System handles 1000 req/s with <200ms latency" |

### Static vs Dynamic

| Type | When Run | Example |
|------|----------|---------|
| **Static** | Code analysis time | Dependency rule checks |
| **Dynamic** | Runtime | Performance benchmarks |

### Automated vs Manual

| Type | Frequency | Example |
|------|-----------|---------|
| **Automated** | Every commit/build | ArchUnit tests |
| **Manual** | Periodic reviews | Architecture review |

## Fitness Function Patterns

### 1. Dependency Rules

**Goal:** Enforce layer/package boundaries

**ArchUnit Example (Java):**
```java
@Test
void servicesShouldNotDependOnInfrastructure() {
    noClasses()
        .that().resideInAPackage("..service..")
        .should().dependOnClassesThat()
        .resideInAPackage("..infrastructure..")
        .check(importedClasses);
}
```

**dependency-cruiser example (JavaScript/TypeScript):**
```javascript
// dependency-cruiser configuration fragment; merge into the project's config.
module.exports = {
  forbidden: [{
    name: 'services-must-not-import-infrastructure',
    severity: 'error',
    from: { path: '^src/services/' },
    to: { path: '^src/infrastructure/' }
  }]
};
```

### 2. Module Structure

**Goal:** Enforce module organization

```java
@Test
void layersShouldNotHaveCyclicDependencies() {
    slices().matching("com.example.(*)..")
        .should().beFreeOfCyclicDependencies()
        .check(importedClasses);
}
```

### 3. Naming Conventions

**Goal:** Enforce naming patterns

```java
@Test
void controllersShouldBeNamedCorrectly() {
    classes()
        .that().resideInAPackage("..controller..")
        .should().haveSimpleNameEndingWith("Controller")
        .check(importedClasses);
}
```

### 4. Performance Bounds

**Goal:** Enforce performance requirements

```java
@Test
void apiResponseTimeShouldBeUnder200ms() {
    Stopwatch timer = Stopwatch.createStarted();
    performRealApiCall(); // Supply the actual client and representative test environment
    long elapsed = timer.elapsed(TimeUnit.MILLISECONDS);
    assertThat(elapsed).isLessThan(200);
}
```

A single timed call cannot prove a p95/p99 objective. Use a representative load
profile, warm-up, sample count, error reporting and a declared environment.

### 5. Dependency Health

**Goal:** Detect reported dependency vulnerabilities, not prove freshness or safety

```yaml
# .github/workflows/dependency-check.yml
- name: Check dependencies
  run: |
    npm audit --audit-level=high
    # Fail if high vulnerabilities found
```

## Tools for Fitness Functions

| Tool | Language | Purpose |
|------|----------|---------|
| [ArchUnit](https://www.archunit.org/) | Java | Architecture unit testing |
| [dependency-cruiser](https://github.com/sverweij/dependency-cruiser) | JavaScript/TypeScript | Architecture testing & dependency rules |
| [SonarQube](https://www.sonarsource.com/) | Multi | Code quality gates |
| [Checkstyle](https://checkstyle.org/) | Java | Code style enforcement |
| [ESLint](https://eslint.org/) | JavaScript | Code quality |
| [Dependabot](https://github.com/dependabot) | Multi | Dependency updates |
| [Decision Guardian](https://github.com/DecispherHQ/decision-guardian) | Multi | ADR enforcement |

## CI/CD Integration

### GitHub Actions Example

```yaml
name: Architecture Fitness Functions

on: [push, pull_request]

jobs:
  architecture-checks:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1 # v7
      
      - name: Run ArchUnit tests
        run: ./gradlew test --tests "*ArchitectureTest*"
      
      - name: Check dependency rules
        run: ./gradlew dependencyCheck
        
      - name: Performance benchmarks
        run: ./gradlew benchmark
```

### Quality Gates

```yaml
quality-gates:
  - name: Architecture Compliance
    conditions:
      - metric: archunit-tests
        threshold: 100% pass
      - metric: dependency-vulnerabilities
        threshold: 0 critical
      - metric: code-coverage
        threshold: 80%
```

## Step 1: Identify Architectural Decisions

From your ADRs, extract decisions that can be automated:
- Layer boundaries
- Dependency rules
- Naming conventions
- Performance requirements

## Step 2: Choose Validation Approach

| Decision Type | Validation Approach |
|---------------|---------------------|
| Layer boundaries | ArchUnit dependency rules |
| Naming conventions | ArchUnit naming rules |
| Performance | Benchmark tests |
| Security | Vulnerability scanning |
| Dependencies | Dependency checking |

## Step 3: Implement Tests

Write tests that verify each decision, keeping them deterministic and fast:
- Name each test after the decision it guards (e.g. `ServicesMustNotReferenceInfrastructure`).
- Prefer real dependency-analysis tools (ArchUnit, dependency-cruiser, Spring's `BeanFactory`) over ad-hoc regex.
- Make failures self-documenting: the assertion message should state the violated rule and where to read the ADR.

## Step 4: Integrate into CI/CD

Add tests to your build pipeline so violations are caught before merge, not in production:
- Run atomic/static checks (dependency rules, naming, lint) on every commit and fail the build.
- Run heavier dynamic checks (benchmarks, contract tests) on PRs or nightly to keep PR feedback fast.
- Gate merges on the fitness-function suite, not just unit tests.

## Step 5: Monitor and Alert

Surface runtime fitness signals so drift is visible even when code passes static checks:
- Export metrics for dynamic checks (latency percentiles, error budget burn) to the observability stack.
- Alert on threshold breaches against SLOs, not raw values; page only on user-visible impact.
- Review the fitness-function set regularly and retire rules that no longer reflect current decisions.
- Make suppressions explicit, time-limited and attributable; never turn a failing guardrail into a silent warning.
- Distinguish a violated rule from a broken checker, missing input or skipped run.
  Keep required gates blocked for either failure, but assign the correct owner;
  an advisory scan with unavailable data is not a clean security result.

## Automating Other Architecture Concerns

Fitness functions are one part of architecture automation. Automate adjacent concerns in the same pipeline:

| Concern | Automation | Tools |
|---------|------------|-------|
| **Documentation** | Generate docs/diagrams from code and specs | OpenAPI Generator, SchemaSpy, Structurizr |
| **Security** | Vulnerability and dependency scanning | Snyk, Trivy, npm audit |
| **Monitoring** | Alert rules and health checks as code | Prometheus rules, CloudWatch alarms |
| **Cost** | Budget alerts and right-sizing recommendations | AWS Budgets, Compute Optimizer (see arch-cost) |
| **Policy** | Infrastructure policy as code | Open Policy Agent, Kyverno |

Read `references/automation-reference.md` for detailed automation guidance.

## Examples

- Enforce that service-layer code does not import infrastructure packages.
- Fail CI when critical dependency vulnerabilities are detected.
- Verify that p95 latency stays below the agreed threshold in a benchmark run.

## Common Gotchas

- Keep checks deterministic and cheap enough to run continuously.
- Tie each rule to a concrete architectural decision or ADR.
- Use automated checks for repeatable rules; keep subjective review separate.
- Begin with the most critical decisions and expand over time; manual checks do not scale.
- Make architecture violations fail the build so they are acted on, not ignored.
- Review and update fitness functions as the architecture evolves; treat them as guardrails that help developers, not punishment.

## Further Reading

- `references/awesome-architecture.md` — Curated external articles, videos, libraries, and samples per topic (awesome-architecture.com)
- `references/fitness-functions.md` — Fitness Functions Reference

## Cross-skill handoff

Consume accepted constraints from arch-decision and measurement definitions from arch-metrics. Return an executable check or an explicitly manual assessment, owner, evidence
output and failure disposition to arch-devops and arch-governance. Validate each
automated rule with a known violating fixture; a passing check with no matching files or
samples is unassessable, not proof of fitness.

## Related Skills

- **arch-devops** - CI/CD pipelines that host fitness functions
- **arch-metrics** - Metrics that fitness functions assert thresholds on
- **arch-decision** - Decisions that fitness functions enforce
- **arch-governance** - Governance processes that fitness functions scale
