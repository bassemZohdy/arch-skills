---
name: arch-migration
description: Guide migration planning and legacy modernization. Use when planning database migrations, modernizing legacy systems, implementing strangler fig pattern, assessing migration risks, or creating rollback strategies.
---

# Migration Planning

Systematic approach to planning and executing system migrations.

## Workflow

```
1. Assess Current State → What do we have?
2. Define Target State → Where are we going?
3. Choose Strategy → How to get there?
4. Plan Phases → Break into steps
5. Assess Risks → What could go wrong?
6. Execute & Validate → Run and verify
```

## Step 1: Assess Current State

| Dimension | Assessment |
|-----------|------------|
| **Codebase** | Size, complexity, dependencies |
| **Data** | Volume, format, relationships |
| **Infrastructure** | Servers, networks, dependencies |
| **Team** | Skills, capacity, availability |
| **Constraints** | Budget, timeline, compliance |

### Legacy Assessment Matrix

| Factor | Low (1) | Medium (3) | High (5) |
|--------|---------|------------|----------|
| **Code Quality** | Clean, tested | Mixed | Messy, untested |
| **Documentation** | Complete | Partial | None |
| **Dependencies** | Few, modern | Some outdated | Many deprecated |
| **Team Knowledge** | Deep | Some familiarity | No expertise |

## Step 2: Migration Patterns

### Strangler Fig Pattern

**Best for:** Incrementally replacing legacy systems.

```
Phase 1: Identify seam → Extract small capability
Phase 2: Route traffic → New system handles subset
Phase 3: Expand coverage → More capabilities move
Phase 4: Decommission → Remove legacy
```

### Branch by Abstraction

**Best for:** Replacing internal components without changing interfaces.

1. Create abstraction layer
2. Implement new component
3. Toggle between old/new
4. Remove abstraction

### Parallel Run

**Best for:** Validating new system matches legacy behavior.

1. Run both systems
2. Compare outputs
3. Gradually shift traffic
4. Remove old system

### Database Migration Patterns

| Pattern | Use Case |
|---------|----------|
| **Schema Migration** | Add/modify columns, tables |
| **Data Migration** | Move data between systems |
| **Dual Write** | Write to both old and new |
| **CDC** | Change Data Capture |
| **ETL** | Extract, Transform, Load |

## Step 3: Risk Assessment

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Data loss | Low | Critical | Backups, checksums |
| Downtime | Medium | High | Blue-green, rolling |
| Performance degradation | Medium | Medium | Load testing |
| Feature gaps | High | Medium | Feature parity list |
| Team burnout | Medium | High | Realistic timeline |

## Step 4: Migration Checklist

### Pre-Migration
- [ ] Backup created and verified
- [ ] Rollback plan documented
- [ ] Team aligned on process
- [ ] Monitoring in place
- [ ] Communication plan ready

### During Migration
- [ ] Progress tracked
- [ ] Errors logged
- [ ] Performance monitored
- [ ] Stakeholders updated
- [ ] Checkpoints validated

### Post-Migration
- [ ] All data verified
- [ ] Performance acceptable
- [ ] Legacy decommissioned
- [ ] Documentation updated
- [ ] Lessons learned captured

## Step 5: Rollback Strategy

| Trigger | Action |
|---------|--------|
| Data integrity issues | Restore from backup |
| Performance degradation | Route traffic to legacy |
| Critical bugs | Toggle feature flag |
| Complete failure | Full rollback |

## Examples

- Plan a strangler-fig migration of a legacy ERP module to services.
- Design a dual-write-plus-backfill database migration with verification.
- Run old and new billing engines in parallel and reconcile outputs before cutover.

## Common Gotchas

- Long-lived dual-write setups drift; add continuous reconciliation and a firm cutover date.
- A migration without a tested rollback path is a one-way door taken blind.
- Feature parity lists always miss undocumented behavior users depend on; parallel-run to find it.

## Further Reading

- `references/awesome-architecture.md` — Curated external articles, videos, libraries, and samples per topic (awesome-architecture.com)

## Related Skills

- **arch-refactoring** - Code-level restructuring within the migration
- **arch-devops** - Deployment strategies for cutover
- **arch-data** - Data movement and validation

## Migration Plan Template

```markdown
## Migration Plan: [System Name]

### Current State
- System: [Description]
- Pain points: [List]
- Constraints: [List]

### Target State
- Goal: [Description]
- Benefits: [List]
- Success criteria: [List]

### Strategy
- Pattern: [Strangler fig / Branch by abstraction / Parallel run]
- Phases: [Number]

### Phase 1: [Name]
- Scope: [What's included]
- Timeline: [Duration]
- Risks: [List]
- Validation: [How to verify]

### Rollback Plan
- Triggers: [When to rollback]
- Process: [Steps]
- Time to rollback: [Duration]
```
