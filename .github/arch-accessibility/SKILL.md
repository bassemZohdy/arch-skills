---
name: arch-accessibility
description: Guide accessibility architecture and WCAG compliance. Use when designing accessible interfaces, implementing ARIA patterns, auditing for WCAG compliance, or supporting assistive technologies.
---

# Accessibility Architecture

Systematic approach to designing accessible systems.

## Workflow

```
1. Understand Requirements → WCAG level, user needs
2. Design Accessible UI → Semantic HTML, ARIA
3. Test with Screen Readers → Verify assistive tech
4. Audit → WCAG checklist
5. Document → Accessibility statement
6. Maintain → Regression testing
```

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
| **AA** | Acceptable | Most common legal requirement |
| **AAA** | Optimal | Highest level (often impractical) |

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

```javascript
// Move focus to element
element.focus();

// Trap focus in modal
function trapFocus(modal) {
  const focusable = modal.querySelectorAll('button, input, [tabindex]');
  const first = focusable[0];
  const last = focusable[focusable.length - 1];
  
  modal.addEventListener('keydown', (e) => {
    if (e.key === 'Tab') {
      if (e.shiftKey && document.activeElement === first) {
        e.preventDefault();
        last.focus();
      } else if (!e.shiftKey && document.activeElement === last) {
        e.preventDefault();
        first.focus();
      }
    }
  });
}
```

## Step 5: Color and Contrast

### Contrast Ratios

| Text Type | Minimum Ratio (AA) |
|-----------|-------------------|
| Normal text (< 18pt) | 4.5:1 |
| Large text (≥ 18pt) | 3:1 |
| UI components | 3:1 |

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
- Zoom to 200%
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

## Accessibility Review Template

```markdown
## Accessibility Review: [System]

### WCAG Conformance
- Target Level: [A/AA/AAA]
- Current Status: [Conforming/Partial/Non-conforming]

### Audit Results
| Principle | Pass | Fail | Notes |
|-----------|------|------|-------|

### Issues Found
| Issue | Severity | WCAG Criterion | Fix |
|-------|----------|----------------|-----|

### Recommendations
1. [High priority]
2. [Medium priority]
```
