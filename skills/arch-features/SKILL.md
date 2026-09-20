---
name: arch-features
description: Design feature management architecture. Use when implementing feature flags, designing feature toggles, planning percentage/canary/ring rollouts, running A/B testing and experimentation, or establishing progressive delivery.
---

# Feature Management Architecture

Systematic approach to feature management.

## DAP contribution

For a DAP invocation, read `framework/contribution-contract.md` from the outer
package root (the repository root in a source checkout). Keep standalone tasks
within their requested scope. Use `assets/review-template.md` and record flag/experiment IDs, exposure and privacy policy, owner/expiry, guardrail thresholds, approval, kill-switch checks and removal criteria.
Return evidence-linked proposals and VER plans, not invented approvals or delivery proof.

## Workflow

```
1. Identify Features → What to toggle?
2. Select Strategy → How to toggle?
3. Implement Flags → Where to toggle?
4. Plan Rollout → How to release?
5. Monitor → Track feature usage
6. Clean Up → Remove old flags
```

## Step 1: Feature Flag Types

| Type | Description | Use Case |
|------|-------------|----------|
| **Release Flags** | Toggle features on/off | Gradual rollout |
| **Experiment Flags** | A/B testing | User experience testing |
| **Ops Flags** | Operational control | Circuit breakers, maintenance |
| **Permission Flags** | Access control | Beta users, admin features |

## Step 2: Feature Flag Patterns

### Simple Toggle

```javascript
if (featureFlag.isEnabled('new-checkout')) {
  showNewCheckout();
} else {
  showOldCheckout();
}
```

### User Segmentation

```javascript
if (featureFlag.isEnabled('beta-feature', { user: currentUser })) {
  showBetaFeature();
}
```

### Percentage Rollout

```javascript
if (featureFlag.isEnabled('gradual-rollout', { percentage: 10 })) {
  showNewFeature();
}
```

### A/B Testing

```javascript
const variant = featureFlag.getVariant('experiment-checkout', { user: currentUser });
if (variant === 'control') {
  showControlCheckout();
} else if (variant === 'treatment') {
  showTreatmentCheckout();
}
```

## Step 3: Feature Flag Architecture

### Flag Storage

| Storage | Description | Use Case |
|---------|-------------|----------|
| **Local Config** | File-based | Development |
| **Remote Config** | Server-based | Production |
| **Database** | Persistent storage | Complex rules |
| **CDN** | Edge-cached | Global distribution |

### Flag Evaluation

| Method | Description | Use Case |
|--------|-------------|----------|
| **Client-Side** | Evaluated in browser | UI features |
| **Server-Side** | Evaluated on server | Business logic |
| **Edge** | Evaluated at CDN | Global features |

## Step 4: Feature Flag Tools

| Tool | Type | Description |
|------|------|-------------|
| **LaunchDarkly** | Commercial | Feature management platform |
| **Unleash** | Open Source | Feature flag system |
| **Flagsmith** | Open Source | Feature flag service |
| **Flipper** | Open Source | Feature flags for Ruby |
| **FeatureHub** | Open Source | Feature management |

## Step 5: Feature Rollout Strategies

| Strategy | Description | Risk |
|----------|-------------|------|
| **Big Bang** | Enable for all at once | High |
| **Canary** | Small percentage first | Low |
| **Ring-Based** | Internal → Beta → GA | Medium |
| **Time-Based** | Enable at specific time | Low |

### Rollout Checklist

- [ ] Feature flag created
- [ ] Default state defined
- [ ] Rollout percentage set
- [ ] Monitoring configured
- [ ] Rollback plan ready
- [ ] Cleanup date scheduled
- [ ] Owner, expiry and kill-switch behavior recorded
- [ ] Authorization, tenant isolation and exposure logging verified
- [ ] Success and guardrail metrics defined for automatic pause or rollback

## Step 6: Feature Flag Hygiene

### Flag Lifecycle

1. **Creation** - Define flag and default state
2. **Implementation** - Add toggle logic
3. **Testing** - Test both states
4. **Rollout** - Gradually enable
5. **Monitoring** - Track usage and errors
6. **Cleanup** - Remove flag when stable

### Cleanup Checklist

- [ ] Flag enabled for all users
- [ ] No references to old code path
- [ ] Tests updated
- [ ] Documentation updated
- [ ] Flag removed from code
- [ ] Flag removed from config

## Examples

- Roll out a new checkout flow to 5% of users with automated rollback on error spikes.
- Design a ring-based rollout (internal, beta, GA) for a risky feature.
- Audit and remove stale feature flags older than two quarters.

## Common Gotchas

- Stale flags are technical debt with combinatorial test cost; schedule cleanup at creation time.
- Flags evaluated client-side leak unreleased features to anyone reading the bundle.
- A flag guarding a schema change does not make the migration reversible by itself.
- Permission flags are not a replacement for server-side authorization; treat the client as untrusted.

## Further Reading

- `references/awesome-architecture.md` — Curated external articles, videos, libraries, and samples per topic (awesome-architecture.com)
- `references/feature-management.md` — Feature Management Reference

## Related Skills

- **arch-devops** - Decoupling deploy from release
- **arch-observability** - Measuring rollout health
- **arch-test** - Testing both flag states

## Output template

Use `assets/review-template.md`. Populate its scope and evidence fields for DAP work;
keep missing measurements and approvals explicit.
