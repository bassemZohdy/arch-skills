---
name: arch-fitness
description: Create architecture fitness functions, automated guardrails, and architecture automation. Use when encoding architectural decisions as CI/CD checks, dependency rules, runtime validations, architecture unit tests, or automating documentation generation and compliance checks that keep constraints enforced over time.
---

# Architecture Fitness Functions

Automated checks that verify architectural decisions are maintained.

**Source:** [Building Evolutionary Architectures](https://www.oreilly.com/library/view/building-evolutionary-architectures/9781492043447/) by Ford, Parsons, Kua

## What Are Fitness Functions?

Fitness functions are objective, automated checks that evaluate architectural characteristics. They:
- Make architecture testable and enforceable
- Run continuously (every commit, every build)
- Provide pass/fail feedback
- Scale governance without bottlenecks

## Types of Fitness Functions

### Atomic vs Holistic

| Type | Scope | Example |
|------|-------|---------|
| **Atomic** | Single architectural attribute | "Each class has single responsibility" |
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

**ArchUnitTS Example (TypeScript):**
```typescript
describe('Architecture', () => {
  it('services should not depend on infrastructure', () => {
    const rule = rule({ should: 'not depend on' })
      .from('src/services/**')
      .to('src/infrastructure/**');
    expect(rule).toPass();
  });
});
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
    // Make API call
    long elapsed = timer.elapsed(TimeUnit.MILLISECONDS);
    assertThat(elapsed).isLessThan(200);
}
```

### 5. Dependency Health

**Goal:** Ensure dependencies are up-to-date

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
| [ArchUnitTS](https://github.com/LukasNielsen/ArchUnitTS) | TypeScript | Architecture testing |
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
      - uses: actions/checkout@v3
      
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

## Creating Fitness Functions

### Step 1: Identify Architectural Decisions

From your ADRs, extract decisions that can be automated:
- Layer boundaries
- Dependency rules
- Naming conventions
- Performance requirements

### Step 2: Choose Validation Approach

| Decision Type | Validation Approach |
|---------------|---------------------|
| Layer boundaries | ArchUnit dependency rules |
| Naming conventions | ArchUnit naming rules |
| Performance | Benchmark tests |
| Security | Vulnerability scanning |
| Dependencies | Dependency checking |

### Step 3: Implement Tests

Write tests that verify each decision.

### Step 4: Integrate into CI/CD

Add tests to your build pipeline.

### Step 5: Monitor and Alert

Set up alerts for fitness function failures.

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

## Best Practices

1. **Start Small** - Begin with most critical decisions
2. **Automate Everything** - Manual checks don't scale
3. **Fail the Build** - Architecture violations should break CI
4. **Document Decisions** - Link fitness functions to ADRs
5. **Review Regularly** - Update fitness functions as architecture evolves
6. **Use as Guardrails** - Not punishment; help developers make good choices

## Related Skills

- **arch-devops** - CI/CD pipelines that host fitness functions
- **arch-metrics** - Metrics that fitness functions assert thresholds on
- **arch-decision** - Decisions that fitness functions enforce
- **arch-governance** - Governance processes that fitness functions scale
