---
name: arch-frontend
description: Guide frontend architecture design. Use when designing micro frontends, implementing UI patterns, selecting frontend frameworks, or establishing frontend architecture standards.
---

# Frontend Architecture

Systematic approach to frontend architecture.

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

## Step 6: Testing Strategies

| Level | Focus | Tools |
|-------|-------|-------|
| **Unit** | Individual components | Jest, Vitest |
| **Integration** | Component interactions | Testing Library |
| **E2E** | User flows | Playwright, Cypress |
| **Visual** | UI consistency | Chromatic, Percy |

## Frontend Review Template

```markdown
## Frontend Review: [Application]

### Architecture
- Style: [Monolith/Micro Frontends]
- Framework: [React/Angular/Vue]
- State Management: [Solution]

### Components
| Component | Type | Complexity |
|-----------|------|------------|

### Performance
| Metric | Target | Current |
|--------|--------|---------|

### Testing
| Level | Coverage | Tools |
|-------|----------|-------|

### Recommendations
1. [Improvement]
```
