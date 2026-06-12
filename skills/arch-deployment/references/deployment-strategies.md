# Deployment Strategies Reference

## Strategy Comparison

| Strategy | Downtime | Cost | Complexity | Rollback |
|----------|----------|------|------------|----------|
| Blue-Green | None | High | High | Instant |
| Canary | None | Low | Medium | Quick |
| Rolling | None | Low | Low | Medium |
| Recreate | Yes | Low | Low | Slow |

## CI/CD Best Practices

| Practice | Description |
|----------|-------------|
| Fast builds | < 10 minutes |
| Parallel stages | Run independent tests together |
| Artifact immutability | Same artifact across environments |
| Automated rollback | Quick recovery |
| Feature flags | Decouple deploy from release |
| Canary releases | Gradual rollout |

## Environment Parity

| Aspect | Goal |
|--------|------|
| Infrastructure | Same configuration |
| Software | Same versions |
| Data | Production-like |
| Network | Similar topology |
| Monitoring | Same visibility |
