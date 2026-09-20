# Migration Patterns Reference

## Strangler Fig Pattern

1. **Identify seam** — Find a boundary to extract
2. **Create proxy** — Route traffic through facade
3. **Extract capability** — Build new implementation
4. **Shift traffic** — Gradually move requests
5. **Remove legacy** — Decommission old system

## Branch by Abstraction

1. **Create interface** — Abstract current implementation
2. **Implement alternative** — Build new implementation
3. **Toggle** — Feature flag between implementations
4. **Validate** — Compare outputs
5. **Remove old** — Delete legacy code

## Parallel Run

1. **Replicate data** — Keep both systems in sync
2. **Run both** — Suppress candidate production side effects; retain one authoritative writer
3. **Compare** — Validate outputs match
4. **Shift traffic** — Gradually move to new
5. **Decommission** — Remove old system

## Database Migration

| Strategy | Downtime | Complexity | Use Case |
|----------|----------|------------|----------|
| **Backup/Restore** | High | Low | Small databases |
| **Dump/Load** | Medium | Low | Schema changes |
| **CDC** | Low | High | Large databases |
| **Dual Write** | Depends on validated cutover | High | Phased transition with reconciliation |
