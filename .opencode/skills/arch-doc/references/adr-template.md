# Architecture Decision Records (ADR) Reference

ADRs capture important architectural decisions along with their context and consequences.

**Source:** [github.com/joelparkerhenderson/architecture-decision-record](https://github.com/joelparkerhenderson/architecture-decision-record) (16k+ stars)

## What is an ADR?

An **Architecture Decision Record (ADR)** is a document that captures an important architecture decision made along with its context and consequences.

**Key Terms:**
- **AD**: Architecture Decision - a software design choice
- **ADL**: Architecture Decision Log - collection of all ADRs for a project
- **ADR**: Architecture Decision Record - the document itself
- **ASR**: Architecturally Significant Requirement - requirement with measurable effect on architecture

## ADR Lifecycle

1. **Initiating** - Identify the need for a decision
2. **Researching** - Gather information and options
3. **Evaluating** - Assess alternatives
4. **Deciding** - Make the decision
5. **Implementing** - Execute the decision
6. **Maintaining** - Review and update as needed
7. **Sunsetting** - Deprecate when no longer relevant

## MADR Template (Recommended)

The Markdown Architectural Decision Records (MADR) project provides both simple and elaborate templates.

### Simple Template

```markdown
# {short title of solved problem and solution}

## Status

{Proposed | Accepted | Deprecated | Superseded by [ADR-{number}]}

## Context

{Describe the context and problem statement. What is the issue that motivates this decision?}

## Decision

{Describe the decision that was made. State the decision clearly and concisely.}

## Consequences

{Describe the resulting context after applying the decision. What becomes easier or more difficult?}

### Positive
- {benefit 1}
- {benefit 2}

### Negative
- {tradeoff 1}
- {tradeoff 2}
```

### Elaborate Template (with options comparison)

```markdown
# {short title of solved problem and solution}

## Status

{Proposed | Accepted | Deprecated | Superseded by [ADR-{number}]}

## Context

{Describe the context and problem statement.}

## Decision Drivers

{Consider what factors influenced the decision.}

## Considered Options

{List the options that were considered.}

## Decision Outcome

{Chosen option: "X", because [justification].}

### Consequences

#### Positive
- {positive consequence 1}

#### Negative
- {negative consequence 1}

#### Neutral
- {neutral consequence 1}

## Pros and Cons of the Options

### {Option 1}

{Description}

- Good: {advantage}
- Bad: {disadvantage}

### {Option 2}

{Description}

- Good: {advantage}
- Bad: {disadvantage}

## More Information

{Links, references, or additional context.}
```

## ADR File Naming Convention

Use present tense imperative verb phrases (matches commit message format):

```
docs/adr/001-choose-database.md
docs/adr/002-use-rest-api.md
docs/adr/003-implement-caching.md
```

**Format:** `{number}-{verb-phrase}.md`

## Best Practices

### Writing Good ADRs

1. **Rationale** - Explain the reasons for the decision
2. **Specific** - Each ADR should be about ONE decision
3. **Timestamps** - Identify when items are written
4. **Immutable** - Don't alter existing info; amend or supersede

### Context Section

- Explain your organization's situation and business priorities
- Include rationale based on team skills and social factors
- Describe pros/cons in terms that align with your needs

### Consequences Section

- Explain what follows from the decision
- Include information about subsequent ADRs needed
- Include after-action review processes

### Storage

- **Store in source control** (not wiki or website)
- Keep in sync with code
- Version them alongside the codebase

### Team Practices

- **Who can create:** Any team member who understands the impact
- **When to create:** When a decision has lasting impact
- **When to skip:** Small, reversible, or already-covered decisions
- **Review cycle:** Review each ADR periodically (e.g., quarterly)

## Fitness Functions for Decisions

Fitness functions are automated checks that verify decisions are maintained.

**Example:**
- **Decision:** Use event sourcing for audit requirements
- **Fitness Function:** CI test that all state changes produce events

**Tools:**
- [ArchUnit](https://www.archunit.org/) - Java architecture unit testing
- [ArchUnitTS](https://github.com/LukasNiessen/ArchUnitTS) - TypeScript architecture testing
- [Decision Guardian](https://github.com/DecispherHQ/decision-guardian) - ADR enforcement in PRs

## ADR Tools

| Tool | Language | Description |
|------|----------|-------------|
| [adr-tools](https://github.com/npryce/adr-tools) | Bash | Command-line tools for ADRs |
| [adr-tools-python](https://bitbucket.org/tinkerer_/adr-tools-python/src/master/) | Python | Python implementation |
| [Decision Guardian](https://github.com/DecispherHQ/decision-guardian) | Multi | ADR enforcement for PRs |
| [Mneme HQ](https://github.com/TheoV823/mneme) | Multi | ADR enforcement for AI coding agents |

## Common ADR Templates

| Template | Best For | Complexity |
|----------|----------|------------|
| Michael Nygard | Simple decisions | Low |
| MADR | Detailed comparisons | Medium |
| Jeff Tyree & Art Akerman | Complex decisions | High |
| Business Case | MBA-oriented | High |
| arc42 | Integration with arc42 | Medium |

## ADR Examples

Common decisions to record:
- Programming language choice
- Database technology selection
- API style (REST, GraphQL, gRPC)
- Authentication mechanism
- Deployment strategy
- Monolith vs microservices
- Caching approach
- Message queue selection
