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

```typescript
// TypeScript ArchUnitTS Example
describe('Architecture', () => {
  it('should enforce layer dependency', () => {
    const rule = rule({ should: 'not depend on' })
      .from('src/services/**')
      .to('src/infrastructure/**');
    expect(rule).toPass();
  });
});
```

## CI Integration

```yaml
# GitHub Actions
- name: Run architecture tests
  run: ./gradlew test --tests "*ArchitectureTest*"
```
