# Technical Debt Assessment Reference

## Debt Categories

### Code Debt
**Definition:** Quick fixes, workarounds, code smells in implementation.

**Indicators:**
- TODO/FIXME/HACK comments
- Copied code blocks
- Long methods (>50 lines)
- Deep nesting (>3 levels)
- Magic numbers/strings
- Unused code

**Scoring:**
| Level | Description | Impact |
|-------|-------------|--------|
| Low | Minor code smells | Development speed |
| Medium | Significant workarounds | Maintainability |
| High | Major hacks | Stability risk |
| Critical | Broken patterns | Incident risk |

### Architecture Debt
**Definition:** Shortcut designs, missing abstractions, violated principles.

**Indicators:**
- Circular dependencies
- God objects/classes
- Missing layers/abstractions
- Tight coupling
- Violated SOLID principles
- Missing design patterns

**Scoring:**
| Level | Description | Impact |
|-------|-------------|--------|
| Low | Minor principle violations | Code quality |
| Medium | Missing abstractions | Extensibility |
| High | Structural issues | Scalability |
| Critical | Fundamental flaws | System failure |

### Testing Debt
**Definition:** Missing or inadequate tests.

**Indicators:**
- Low code coverage (<60%)
- Missing integration tests
- Flaky tests
- No performance tests
- No security tests
- Manual test processes

**Scoring:**
| Level | Description | Impact |
|-------|-------------|--------|
| Low | Minor coverage gaps | Confidence |
| Medium | Missing key tests | Regression risk |
| High | Critical path untested | Quality risk |
| Critical | No tests for core | Production risk |

### Documentation Debt
**Definition:** Missing, outdated, or incomplete documentation.

**Indicators:**
- No architecture docs
- Outdated README
- Missing API documentation
- No runbooks
- Missing decision records (ADRs)
- No onboarding guides

**Scoring:**
| Level | Description | Impact |
|-------|-------------|--------|
| Low | Minor gaps | Knowledge sharing |
| Medium | Outdated docs | Onboarding speed |
| High | Missing critical docs | Operations risk |
| Critical | No documentation | System risk |

### Dependency Debt
**Definition:** Outdated, vulnerable, or unsupported dependencies.

**Indicators:**
- Outdated packages
- Known vulnerabilities
- Unsupported libraries
- License compliance issues
- Missing security patches

**Scoring:**
| Level | Description | Impact |
|-------|-------------|--------|
| Low | Minor version lag | Compatibility |
| Medium | Security vulnerabilities | Security risk |
| High | Known exploits | Incident risk |
| Critical | Active exploitation | Security breach |

### Infrastructure Debt
**Definition:** Manual processes, missing automation, outdated infrastructure.

**Indicators:**
- Manual deployments
- No CI/CD pipeline
- Missing monitoring
- No alerting
- Outdated infrastructure
- No disaster recovery

**Scoring:**
| Level | Description | Impact |
|-------|-------------|--------|
| Low | Minor manual steps | Efficiency |
| Medium | Missing automation | Reliability |
| High | No monitoring | Operations risk |
| Critical | No DR plan | Business risk |

## Assessment Process

### Step 1: Identify Debt Items
- Scan codebase for indicators
- Review documentation status
- Analyze dependencies
- Check infrastructure setup

### Step 2: Categorize Debt
- Assign each item to a category
- Note related items

### Step 3: Score Impact
- Use scoring rubric for each category
- Consider business impact
- Assess risk level

### Step 4: Prioritize Remediation
- Critical: Fix immediately
- High: Plan for next quarter
- Medium: Add to backlog
- Low: Address opportunistically

## Debt Tracking Template

```markdown
## Technical Debt Register

| ID | Category | Item | Impact | Effort | Priority | Status |
|----|----------|------|--------|--------|----------|--------|
| TD-001 | Code | Extract auth service | High | Large | High | Open |
| TD-002 | Testing | Add integration tests | High | Medium | High | In Progress |
| TD-003 | Dependency | Update React to v18 | Medium | Small | Medium | Open |
| TD-004 | Docs | Document API endpoints | Medium | Medium | Medium | Open |
| TD-005 | Infra | Add monitoring | High | Large | High | Planned |
```

## Remediation Strategies

### Incremental Improvement
- Address debt during feature work
- Boy Scout Rule: Leave code cleaner
- Small, frequent improvements

### Dedicated Sprints
- Allocate percentage of capacity
- Regular debt reduction sprints
- Balance feature and debt work

### Automated Detection
- Static analysis tools
- Dependency scanners
- Test coverage gates
- Documentation checks
