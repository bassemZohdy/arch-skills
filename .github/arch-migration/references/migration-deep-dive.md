# Migration Deep Dive

**Source:** Martin Fowler Patterns of Legacy Displacement, Strangler Fig

## Migration Patterns

### Strangler Fig

```
Legacy System → Facade → New Components
                    ↓
              Gradually Replace
```

**Steps:**
1. Identify seam in legacy system
2. Create facade/proxy
3. Extract capability to new system
4. Route traffic to new system
5. Repeat until legacy is empty

### Branch by Abstraction

1. Create abstraction layer
2. Implement new behavior behind abstraction
3. Toggle between old and new
4. Remove old implementation

### Parallel Run

1. Run both systems
2. Compare outputs
3. Gradually shift traffic
4. Remove old system

## Migration Risk Assessment

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Data loss | Low | Critical | Backups, checksums |
| Downtime | Medium | High | Blue-green, rolling |
| Performance degradation | Medium | Medium | Load testing |
| Feature gaps | High | Medium | Feature parity list |
| Team burnout | Medium | High | Realistic timeline |

## Migration Checklist

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

## Database Migration Patterns

| Pattern | Use Case | Downtime |
|---------|----------|----------|
| **Backup/Restore** | Small databases | High |
| **Dump/Load** | Schema changes | Medium |
| **CDC** | Large databases | Low |
| **Dual Write** | Zero-downtime | None |

## Rollback Strategies

| Trigger | Action |
|---------|--------|
| Data integrity issues | Restore from backup |
| Performance degradation | Route traffic to legacy |
| Critical bugs | Toggle feature flag |
| Complete failure | Full rollback |
