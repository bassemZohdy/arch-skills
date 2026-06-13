---
name: arch-features
description: Guide feature management architecture. Use when implementing feature flags, designing feature toggles, planning feature rollouts, or establishing experimentation frameworks.
---

# Feature Management Architecture

Systematic approach to feature management.

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

## Feature Review Template

```markdown
## Feature Management Review: [System]

### Feature Flags
| Flag | Type | Status | Owner |
|------|------|--------|-------|

### Rollout Status
| Feature | Strategy | Progress | Rollback Plan |
|---------|----------|----------|---------------|

### Experiments
| Experiment | Variants | Sample Size | Status |
|------------|----------|-------------|--------|

### Recommendations
1. [Improvement]
```
