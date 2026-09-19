# DAP project records

The reference implementation stores a project baseline as JSON records and derives
human-readable Markdown from those records. Every record has a stable ID and a
status. Superseded records remain in history.

## Requirement

Use REQ-### IDs. Record statement, type, source and source revision, stakeholder
owner, priority and named delivery scope, acceptance criteria, verification method
and owner, dependencies and lifecycle status. A quality requirement also records a
stimulus, environment, affected element, expected response and measurable threshold.

## Design element and decision

Use DES-### and ADR-### IDs. Design elements identify significant or supporting
scope. Decisions record owner, context, alternatives, criteria/evidence, uncertainty,
consequences, dependencies, status, authority and review disposition.

## Question, assumption, verification and exception

Use Q-###, ASM-###, VER-### and EXC-### IDs. Questions have an owner and impact;
assumptions have a validation trigger; verification items distinguish a planned
method from executed evidence; exceptions record obligation, justification,
authority, residual risk and expiry or review trigger.

## Trace links

Traceability is a typed graph. Valid links connect sources to requirements,
requirements to design and decisions, and design to verification. The RTM is a
projection of this graph; it is not a second source of truth.

## State transitions

Draft -> blocked, ready-for-review or baselined. Baselined requires applicable
convergence checks, required reviews, valid configuration and a current evaluation.
An overall score cannot bypass a failed gate. Requirement changes re-enter
elicitation; design defects re-enter design; approval changes re-enter review.
