---
name: arch-accessibility
description: Design accessible interfaces and achieve WCAG conformance. Use when designing accessible interfaces, implementing semantic HTML and ARIA patterns, auditing WCAG 2.2 A/AA/AAA conformance, testing assistive-technology interoperability, or remediating accessibility defects.
---

# Accessibility Architecture

Systematic approach to designing accessible systems.

## DAP contribution

For a DAP invocation, read `framework/contribution-contract.md` from the outer
package root (the repository root in a source checkout). Keep standalone tasks
within their requested scope. Use `assets/review-template.md` and record WCAG edition/level, scoped journeys, criterion IDs, browser/assistive-technology context, manual evidence and remaining barriers.
Return evidence-linked proposals and VER plans, not invented approvals or delivery proof.

For DAP work, populate its scope and evidence fields; keep missing measurements and approvals explicit.

## Workflow

```
1. Understand Requirements → WCAG level, user needs
2. Design Accessible UI → Semantic HTML, ARIA
3. Test with Screen Readers → Verify assistive tech
4. Audit → WCAG checklist
5. Document → Accessibility statement
6. Maintain → Regression testing
```

Use WCAG 2.2 as the current baseline unless a contract or jurisdiction names a
different version. Map each claim to the exact success criterion and test
condition. Combine automated rules with keyboard, screen-reader, zoom/reflow and
representative disabled-user evaluation; automation alone cannot establish
conformance.

## Step 1: WCAG Overview

### WCAG Principles (POUR)

| Principle | Description |
|-----------|-------------|
| **Perceivable** | Information must be presentable |
| **Operable** | UI must be operable |
| **Understandable** | Information must be understandable |
| **Robust** | Content must be robust for assistive tech |

### Conformance Levels

| Level | Description | Requirement |
|-------|-------------|-------------|
| **A** | Minimum | Must meet for basic accessibility |
| **AA** | Includes all A and AA criteria | Confirm the jurisdictional or contractual target |
| **AAA** | Optional | Apply to named content or user needs; do not assume whole-site AAA |

## Step 2: Semantic HTML

### Landmark Regions

```html
<header>    <!-- Banner landmark -->
<nav>       <!-- Navigation landmark -->
<main>      <!-- Main content landmark -->
<aside>     <!-- Complementary landmark -->
<footer>    <!-- Content information landmark -->
<section>   <!-- Region landmark with label -->
<article>   <!-- Article landmark -->
```

### Heading Hierarchy

```html
<h1>Page Title</h1>        <!-- One per page -->
  <h2>Section</h2>         <!-- Major sections -->
    <h3>Subsection</h3>    <!-- Sub-sections -->
      <h4>Detail</h4>      <!-- Fine-grained -->
```

### Forms

```html
<label for="email">Email</label>
<input type="email" id="email" required aria-describedby="email-help">
<span id="email-help">We'll never share your email</span>
```

## Step 3: ARIA Patterns

### Common Patterns

| Pattern | Use Case | Example |
|---------|----------|---------|
| **Tab Panel** | Switching content | Settings tabs |
| **Accordion** | Collapsible sections | FAQ |
| **Modal** | Dialog overlay | Confirmation |
| **Toast** | Notifications | Success message |
| **Live Region** | Dynamic updates | Chat messages |

### ARIA States

```html
<!-- Expanded state -->
<button aria-expanded="false" aria-controls="menu">Menu</button>
<ul id="menu" hidden>...</ul>

<!-- Selected state -->
<div role="tab" aria-selected="true">Tab 1</div>

<!-- Disabled state -->
<button disabled aria-disabled="true">Action</button>
```

### Live Regions

```html
<!-- Polite: waits for user to finish -->
<div aria-live="polite">Updated</div>

<!-- Assertive: interrupts user -->
<div aria-live="assertive">Error!</div>

<!-- Status: polite, no interrupt -->
<div role="status">Loading...</div>
```

## Step 4: Keyboard Navigation

### Requirements

- All interactive elements must be keyboard accessible
- Logical tab order
- Visible focus indicators
- No keyboard traps

### Focus Management

Prefer a native modal dialog where supported. Test initial focus, Tab/Shift+Tab,
Escape and focus return to the invoking control. Custom implementations need
hidden/disabled element handling, dynamically changing content, background
inertness and a no-focusable-content fallback; a two-element Tab trap is incomplete.

## Step 5: Color and Contrast

### Contrast Ratios

| Text Type | Minimum Ratio (AA) |
|-----------|-------------------|
| Text not meeting the large-text definition | 4.5:1 |
| Large text (≥ 18pt, or ≥ 14pt bold) | 3:1 |
| Applicable non-text controls/graphics (1.4.11, with exceptions) | 3:1 |

### Don't Rely on Color Alone

```html
<!-- Bad: color only -->
<span style="color: red">Error</span>

<!-- Good: color + icon + text -->
<span class="error">
  <svg aria-hidden="true">...</svg>
  <span>Error: Invalid email</span>
</span>
```

## Step 6: Testing

### Manual Testing

- Keyboard navigation
- Screen reader testing (NVDA, VoiceOver, JAWS)
- Test text resizing to 200% and reflow at 320 CSS pixels, applying criterion-specific exceptions
- Color contrast checking

### Automated Testing

| Tool | Type |
|------|------|
| axe-core | Browser extension |
| Lighthouse | Chrome DevTools |
| Pa11y | CLI tool |

### Screen Reader Commands

| Screen Reader | Navigate | Read | Form |
|---------------|----------|------|------|
| NVDA | H (headings) | Insert+F7 | F (form fields) |
| VoiceOver | VO+Command+H | VO+A | VO+Command+Space |
| JAWS | H (headings) | Insert+F5 | Tab |

## Examples

- Audit a signup flow for WCAG 2.2 AA and produce a prioritized fix list.
- Make a custom dropdown fully keyboard- and screen-reader-operable.
- Add automated axe-core checks to CI with manual screen reader spot checks.

## Common Gotchas

- Automated tools cover only part of conformance; combine them with manual keyboard, screen-reader and task-based evaluation.
- ARIA misused is worse than no ARIA; prefer native semantic HTML first.
- Accessibility bolted on before launch costs far more than building it into components.

## Further Reading

- `references/awesome-architecture.md` — Curated external articles, videos, libraries, and samples per topic (awesome-architecture.com)
- `references/wcag-reference.md` — WCAG 2.2 scope, criteria and verification reference

The normative baseline is [W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/); use
the repository reference for routing and implementation notes.

## Cross-skill handoff

Consume the journey/component inventory from arch-usability and arch-frontend. Return
criterion-level barriers, affected journeys, reproduction steps and manual verification
to arch-test; send any legal applicability question to arch-compliance. Check focus
restoration, error recovery, reflow, target size and authentication on the actual
supported devices, not only a static page.

## Related Skills

- **arch-usability** - Overall UX quality
- **arch-frontend** - Component architecture where semantics live
- **arch-compliance** - Legal requirements (ADA, EAA, Section 508)
