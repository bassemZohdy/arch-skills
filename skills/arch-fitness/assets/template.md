# Fitness Function Template

Use this template when creating architecture fitness functions.

## Template Structure

```java
// Java ArchUnit Example
@Test
void shouldEnforceLayerDependency() {
    noClasses()
        .that().resideInAPackage("..service..")
        .should().dependOnClassesThat()
        .resideInAPackage("..infrastructure..")
        .check(importedClasses);
}
```

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

## CI Integration

```yaml
# GitHub Actions
- name: Run architecture tests
  run: ./gradlew test --tests "*ArchitectureTest*"
```

## Scope, evidence and DAP handoff

For standalone use, omit inapplicable process fields; do not invent a DAP run.

| Field | Recorded value |
| --- | --- |
| Scope, run, stage and baseline revision/hash | |
| REQ / CON / DES / ADR IDs and source revisions | |
| Findings: ID, target, observed/proposed/unknown, evidence locator, rationale, uncertainty | |
| Alternatives and consequences | |
| Required human review, authority and disposition evidence | |
| Affected dependencies, supersessions and stale approvals | |
| Open Q / ASM / EXC IDs, owner and next action | |
| Contribution status: complete for scope / provisional / blocked | |

### Domain evidence

Record protected decision/requirement, rule ID and scope, measurement, tolerated variance, owner, evidence output, failure action and exception expiry.

### Verification plans and results

| VER ID | Protected IDs | Method and environment | Acceptance threshold | Owner | Planned/executed status | Actual evidence locator |
| --- | --- | --- | --- | --- | --- | --- |

Leave execution evidence empty for planned verification. A recommendation,
checkbox or generated test is not proof of implementation or human approval.
