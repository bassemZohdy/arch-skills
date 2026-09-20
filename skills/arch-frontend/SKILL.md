---
name: arch-frontend
description: Design frontend architecture. Use when designing micro frontends or module federation, implementing component and design-system architecture, selecting frameworks, separating server and UI state, planning Core Web Vitals budgets, or establishing frontend testing and accessibility standards.
---

# Frontend Architecture

Systematic approach to frontend architecture.

## DAP contribution

For a DAP invocation, read `framework/contribution-contract.md` from the outer
package root (the repository root in a source checkout). Keep standalone tasks
within their requested scope. Use `assets/review-template.md` and record journey IDs, rendering/state and trust boundaries, team ownership, architecture alternatives and accessibility/performance/security verification.
Return evidence-linked proposals and VER plans, not invented approvals or delivery proof.

## Workflow

```
1. Understand Requirements → What UI is needed?
2. Select Architecture → Monolith, micro frontends, etc.
3. Choose Framework → React, Angular, Vue, etc.
4. Design Components → Component hierarchy and patterns
5. Implement State Management → How to manage state?
6. Optimize → Performance, accessibility, testing
```

## Step 1: Architecture Styles

| Style | Description | Use Case |
|-------|-------------|----------|
| **Monolithic** | Single codebase | Small teams, simple apps |
| **Micro Frontends** | Independent deployable units | Large teams, complex apps |
| **Module Federation** | Shared modules across apps | Shared dependencies |
| **Server Components** | Server-rendered components | Performance, SEO |

These are different design axes, not mutually exclusive alternatives: deployment
boundaries, composition mechanisms and rendering choices can coexist. Compare
like-for-like options and their trust, failure and release boundaries.

## Step 2: Micro Frontends

### Decomposition Strategies

| Strategy | Description | Use Case |
|----------|-------------|----------|
| **By Feature** | Feature-specific apps | Feature teams |
| **By Page** | Page-specific apps | Page-based routing |
| **By Domain** | Domain-specific apps | Domain teams |

### Integration Patterns

| Pattern | Description | Trade-off |
|---------|-------------|-----------|
| **Build-Time Integration** | Compile together | Simple, tight coupling |
| **Server-Side Integration** | Compose on server | SEO, complexity |
| **Client-Side Integration** | Compose in browser | Flexibility, complexity |

### Implementation Tools

| Tool | Description |
|------|-------------|
| **Module Federation** | Webpack built-in |
| **Single-SPA** | Framework-agnostic |
| **Web Components** | Browser native |
| **iframe** | Simple isolation |

## Step 3: Component Patterns

### Component Architecture

| Pattern | Description | Use Case |
|---------|-------------|----------|
| **Atomic Design** | Atoms, molecules, organisms | Design systems |
| **Container/Presentational** | Separate logic from UI | React apps |
| **Compound Components** | Composable components | Complex UIs |
| **Render Props** | Flexible rendering | Reusable logic |

### State Management Patterns

| Pattern | Description | Use Case |
|---------|-------------|----------|
| **Local State** | Component-level state | Simple components |
| **Context** | React context | Cross-component state |
| **Redux** | Centralized state | Complex state logic |
| **Zustand** | Lightweight state | Simple state needs |
| **Jotai** | Atomic state | Fine-grained updates |

## Step 4: Framework Selection

| Framework | Best For | Trade-offs |
|-----------|----------|------------|
| **React** | Large ecosystem, flexibility | Learning curve |
| **Angular** | Enterprise, opinionated | Verbose |
| **Vue** | Simple, progressive | Smaller ecosystem |
| **Svelte** | Performance, simplicity | Newer ecosystem |
| **Next.js** | React with SSR/SSG | Server complexity |

## Step 5: Performance Patterns

| Pattern | Description |
|---------|-------------|
| **Code Splitting** | Load code on demand |
| **Lazy Loading** | Defer non-critical resources |
| **Virtual Scrolling** | Render visible items only |
| **Image Optimization** | Lazy load, compress, format |
| **Caching** | Browser, CDN, service worker |

Define budgets from real user journeys and device/network classes. Track Core Web
Vitals and JavaScript, image and interaction cost separately; a fast synthetic
score does not prove an accessible or usable experience.

## Step 6: Testing Strategies

| Level | Focus | Tools |
|-------|-------|-------|
| **Unit** | Individual components | Jest, Vitest |
| **Integration** | Component interactions | Testing Library |
| **E2E** | User flows | Playwright, Cypress |
| **Visual** | UI consistency | Chromatic, Percy |

## Examples

- Decide between a monolithic SPA and micro frontends for a 6-team product org.
- Design a state management approach separating server cache from UI state.
- Set performance budgets and code-splitting boundaries for a slow dashboard.

## Common Gotchas

- Justify micro frontends with independent ownership, release cadence or isolation needs; team count alone is not a selection threshold.
- Server state belongs in a query cache (React Query/SWR), not in global UI state stores.
- Shared dependencies across micro frontends reintroduce the coupling you tried to remove.
- A micro frontend boundary without independent ownership, deployment or failure isolation is only an integration boundary.

## Further Reading

- `references/awesome-architecture.md` — Curated external articles, videos, libraries, and samples per topic (awesome-architecture.com)
- `references/frontend-deep-dive.md` — Frontend Architecture Deep Dive
- `references/frontend-patterns.md` — Frontend Architecture Reference

## Cross-skill handoff

Consume journeys from arch-usability, inclusive interaction requirements from arch-accessibility and contracts from arch-api. Document rendering, routing, session
ownership, cache partitioning, design-system versions and remote-module failure
behavior. Web Components and module federation do not provide a security sandbox;
involve arch-security for untrusted content and cross-origin messaging.

## Related Skills

- **arch-usability** - UX heuristics and information architecture
- **arch-accessibility** - WCAG and assistive technology support
- **arch-perf** - Performance budgets and caching
