# Frontend Architecture Reference

## Architecture Styles

| Style | Description | Use Case |
|-------|-------------|----------|
| **Monolithic** | Single codebase | Small teams, simple apps |
| **Micro Frontends** | Independent deployable units | Large teams, complex apps |
| **Module Federation** | Shared modules across apps | Shared dependencies |
| **Server Components** | Server-rendered components | Performance, SEO |

## Component Patterns

| Pattern | Description | Use Case |
|---------|-------------|----------|
| **Atomic Design** | Atoms, molecules, organisms | Design systems |
| **Container/Presentational** | Separate logic from UI | React apps |
| **Compound Components** | Composable components | Complex UIs |
| **Render Props** | Flexible rendering | Reusable logic |

## State Management

| Pattern | Description | Use Case |
|---------|-------------|----------|
| **Local State** | Component-level state | Simple components |
| **Context** | React context | Cross-component state |
| **Redux** | Centralized state | Complex state logic |
| **Zustand** | Lightweight state | Simple state needs |

## Performance Patterns

| Pattern | Description |
|---------|-------------|
| **Code Splitting** | Load code on demand |
| **Lazy Loading** | Defer non-critical resources |
| **Virtual Scrolling** | Render visible items only |
| **Image Optimization** | Lazy load, compress, format |
| **Caching** | Browser, CDN, service worker |
