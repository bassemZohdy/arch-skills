---
name: arch-usability
description: "Design usability, UX and user-experience architecture. Use when planning user research, evaluating journeys and information architecture, applying Nielsen heuristics, running SUS or usability testing, designing inclusive interactions, or establishing UX standards. Trigger on usability reviews, heuristic evaluations, research plans, SUS testing, or UX design."
---

# Usability Architecture

Systematic approach to designing usable systems.

## DAP contribution

For a DAP invocation, read `framework/contribution-contract.md` from the outer
package root (the repository root in a source checkout). Keep standalone tasks
within their requested scope. Use `assets/review-template.md` and record research/source IDs, participant/task context, consent/privacy boundaries, success criteria, uncertainty and observed versus heuristic findings.
Return evidence-linked proposals and VER plans, not invented approvals or delivery proof.

## Workflow

```
1. Understand Users → Who are they? What do they need?
2. Define Goals → What must users accomplish?
3. Design Structure → Information architecture
4. Design Interactions → Usability patterns
5. Validate → Usability testing
6. Iterate → Refine based on feedback
```

## Step 1: User Research

### User Types

| Type | Description | Method |
|------|-------------|--------|
| **Persona** | Fictional representative user | Interviews, surveys |
| **Journey Map** | User's experience over time | Observation, interviews |
| **Empathy Map** | User's thoughts, feelings, actions | Workshops |
| **Jobs to Be Done** | What user is trying to accomplish | Interviews |

### User Research Methods

| Method | When | Effort |
|--------|------|--------|
| **Interviews** | Explore user needs | Medium |
| **Surveys** | Validate at scale | Low |
| **Observation** | Understand actual behavior | Medium |
| **Usability Testing** | Validate designs | High |
| **A/B Testing** | Compare alternatives | Medium |

## Step 2: Usability Heuristics

### Nielsen's 10 Heuristics

| # | Heuristic | Description |
|---|-----------|-------------|
| 1 | **Visibility of System Status** | Show what's happening |
| 2 | **Match Between System and Real World** | Use user's language |
| 3 | **User Control and Freedom** | Undo, redo, escape |
| 4 | **Consistency and Standards** | Follow conventions |
| 5 | **Error Prevention** | Prevent errors before they occur |
| 6 | **Recognition Rather Than Recall** | Make options visible |
| 7 | **Flexibility and Efficiency of Use** | Shortcuts for experts |
| 8 | **Aesthetic and Minimalist Design** | Only essential info |
| 9 | **Help Users Recognize and Recover from Errors** | Clear error messages |
| 10 | **Help and Documentation** | Provide help when needed |

### Severity Rating

| Rating | Description |
|--------|-------------|
| **0** | Not a usability problem |
| **1** | Cosmetic issue |
| **2** | Minor usability problem |
| **3** | Major usability problem |
| **4** | Catastrophic usability problem |

## Step 3: Information Architecture

### Structure Patterns

| Pattern | Use Case |
|---------|----------|
| **Hierarchy** | Most common, tree structure |
| **Sequential** | Step-by-step processes |
| **Matrix** | Multiple dimensions |
| **Hub and Spoke** | Central navigation |

### Navigation Patterns

| Pattern | Description |
|---------|-------------|
| **Global** | Always visible, top-level |
| **Local** | Context-specific |
| **Breadcrumb** | Shows location in hierarchy |
| **Search** | Find by query |
| **Tags** | Folksonomy, user-generated |

## Step 4: Interaction Design

### Common Patterns

| Pattern | Use Case |
|---------|----------|
| **Wizard** | Multi-step process |
| **Progressive Disclosure** | Show details on demand |
| **Infinite Scroll** | Content browsing |
| **Lazy Loading** | Performance optimization |
| **Optimistic UI** | Assume success |

### Form Design

- Label positions (above, left, placeholder)
- Input types and validation
- Error handling and messages
- Progress indicators
- Auto-save behavior

## Step 5: Usability Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| **Task Success Rate** | > 90% | Usability testing |
| **Time on Task** | Context-dependent | Stopwatch |
| **Error Rate** | < 5% | Observation |
| **Satisfaction (SUS)** | > 80 | Survey |

## Step 6: Usability Testing

### Test Types

| Type | When | Output |
|------|------|--------|
| **Moderated** | Guided sessions | Detailed insights |
| **Unmoderated** | Remote, self-guided | Quantitative data |
| **Guerrilla** | Quick, informal | Quick feedback |
| **A/B** | Compare designs | Conversion data |

### Test Script Template

```
1. Introduction (2 min)
2. Warm-up question (3 min)
3. Task 1: [Description] (10 min)
4. Task 2: [Description] (10 min)
5. Debrief (5 min)
```

## Examples

- Run a heuristic evaluation of a checkout flow against Nielsen's 10 heuristics.
- Restructure a settings area's information architecture based on card sorting.
- Define task success and SUS targets before a redesign.

## Common Gotchas

- Five users find most usability problems; do not wait for a large study to fix obvious issues.
- What users say and what they do differ; observe behavior, not just opinions.
- Severity without frequency misprioritizes: a minor issue hit by everyone often beats a major edge case.

## Further Reading

- `references/awesome-architecture.md` — Curated external articles, videos, libraries, and samples per topic (awesome-architecture.com)
- `references/usability-heuristics.md` — Usability Heuristics Reference

## Related Skills

- **arch-accessibility** - Usable for people with disabilities
- **arch-frontend** - Component and interaction implementation

## Output template

Use `assets/review-template.md`. Populate its scope and evidence fields for DAP work;
keep missing measurements and approvals explicit.
