---
name: arch-diagrams
description: Create, review, and maintain architecture diagrams and diagram-as-code for C4, runtime and sequence flows, deployment topology, data movement, trust boundaries, state, and workflows. Use when a diagram is the primary deliverable; use arch-doc when diagrams are part of broader architecture documentation or ADR generation.
---

# Architecture Diagrams

Produce diagrams that communicate one architectural viewpoint clearly, remain
consistent with the named architecture baseline, and can be maintained as source.
Use this skill for diagram-first work; hand broader documentation and ADR assembly
to `arch-doc`.

## DAP contribution

For a DAP invocation, read `framework/contribution-contract.md` from the outer
package root. Return stable diagram IDs, viewpoint and abstraction level, baseline
and source revisions, linked REQ/CON/DES/ADR/VER IDs, assumptions, unresolved
questions, and validation status. A rendered image or diagram source is not proof
that the deployed system matches it, and a planned verification is not execution
evidence.

## Workflow

1. **Frame the view.** Identify the audience, concern, decision or question, scope,
   system boundary, desired detail and output format. Choose one primary viewpoint.
2. **Establish the baseline.** Inventory confirmed artifacts and source revisions.
   Label inferred and unresolved elements; never fill an evidence gap with a guessed
   component, connection, protocol or deployment location.
3. **Choose the diagram type.** Select the smallest view that answers the question.
   Do not mix abstraction levels merely to make one diagram look complete.
4. **Choose the notation.** Prefer repository-compatible, text-based source and
   preserve editable source alongside any rendered image.
5. **Model relationships.** Give nodes stable IDs, meaningful labels, direction,
   protocol or interaction intent, ownership where relevant, and a legend for any
   visual convention.
6. **Cross-check and validate.** Compare names, boundaries, flows and decisions
   with the baseline, related views and linked records. Check syntax/renderability,
   readability, accessibility, sensitive-data exposure and freshness metadata.
7. **Return the source and evidence.** Return the diagram source, render only when
   requested or required by the consumer, a short interpretation, assumptions,
   validation findings and the next review trigger.

For review-only requests, return findings or a proposed diff without changing
the baseline. Write or publish source/exports only within authorized targets.
If no compatible renderer is available, label syntax/render validation unexecuted;
visual inspection and plausible syntax do not establish renderability.

## View selection

| Question | View | Minimum content |
| --- | --- | --- |
| Who uses the system and what surrounds it? | C4 system context | People, target system, external systems and labelled relationships |
| What runs inside the system boundary? | C4 container | Applications, data stores, technology, ownership and protocols |
| How is one container structured? | C4 component or package | Components, interfaces, dependencies and the selected container boundary |
| How does a request or event proceed? | Sequence, runtime or event flow | Participants, order, sync/async semantics, retries, correlation and failure paths |
| Where is it deployed? | Deployment or topology | Nodes, zones, placement, network boundaries, replicas and dependencies |
| How is data shaped or transferred? | Data-flow or ER view | Data ownership, classification, direction, transformations, persistence and retention |
| How does a resource change over time? | State or lifecycle view | States, guards, transitions, owners, timeout and recovery behavior |
| Where are controls applied? | Trust-boundary view | Actor/workload identity, boundary, data classification, control and denied paths |

Use C4 terminology consistently: a container is an application or data-store
runtime boundary, not only a Docker container. Use a deployment view to show
placement and operational topology, not to imply runtime behavior that belongs in a
sequence or event view.

## Format selection

Follow the repository priority unless the user or consuming tool specifies another
format:

1. **Mermaid** for diagrams embedded in Markdown and ordinary diagram-as-code.
2. **PlantUML** when an existing repository or consumer uses PlantUML/C4-PlantUML.
3. **Draw.io** when editable visual layout or stakeholder annotation is the primary
   requirement; retain an exportable source file and identify the source of truth.

Use another text-based format only when it is already part of the target repository
or explicitly requested. Do not introduce a renderer, icon library or provider
dependency just to produce one diagram. Keep source in version control and avoid
generated-only images with no recoverable model.

## Modeling rules

- Keep one scope and one main question per diagram; split dense views instead of
  shrinking labels or combining context, container and component detail.
- Keep node names stable across views. If a view intentionally changes scope,
  preserve the identifier and state the boundary change.
- Label every relationship with an action, protocol, event or data movement. Show
  direction where it matters and distinguish synchronous calls from asynchronous
  delivery.
- Show important negative paths: rejection, timeout, retry, dead-letter, fallback,
  failure boundary or denied authorization when the view concerns that behavior.
- Use color, shape and line style as supporting cues, never as the only meaning.
  Provide a legend, text labels and concise alternative text for rendered output.
- Keep secrets, tokens, personal data and infrastructure credentials out of labels,
  examples and diagram metadata. Use classifications and logical names instead.
- Link a diagram to its source, baseline, decision records and verification plan;
  distinguish an intended design from an observed deployment or measured result.

## View-specific checks

### C4 structure

- Start with context for a new system unless the request is intentionally scoped to
  a lower level.
- Keep each level internally consistent and state the level in the title.
- Include external systems and people that influence the boundary; do not hide them
  in implementation detail.
- Record technology and protocol at container/component level where it affects a
  decision, but keep context labels business-readable.

### Runtime, event and sequence behavior

- Identify participants, trigger, ordering, correlation identity and completion
  semantics.
- Mark retry ownership, idempotency, timeout/deadline propagation, duplicate or
  out-of-order handling, and compensation when applicable.
- Do not use an arrow alone to claim delivery, durability, exactly-once processing
  or successful execution; link those claims to verification evidence.

### Deployment and trust boundaries

- Separate logical ownership from physical placement and show relevant zones,
  ingress/egress, identity boundaries and managed-service dependencies.
- Distinguish desired topology from observed topology and include the revision or
  environment used to produce the view.
- Show data classification and control intent without exposing real secrets or
  unnecessary personal information.

## Review checklist

- [ ] Audience, concern, scope and viewpoint are stated.
- [ ] Baseline revision and source locators are recorded.
- [ ] Abstraction level and diagram type are explicit.
- [ ] All nodes and relationships have meaningful, consistent labels.
- [ ] Direction, protocol, sync/async behavior and important failure paths are clear.
- [ ] Legend, alternative text and non-color semantics are present where needed.
- [ ] Diagram agrees with neighboring views and linked REQ/CON/DES/ADR records.
- [ ] Sensitive values are absent and assumptions/unresolved questions are visible.
- [ ] Source is editable, renderable and covered by a review/freshness trigger.

## Cross-skill handoff

Consume scope, requirements and constraints from `arch-orchestrator`; return diagram
IDs, linked views and unresolved evidence gaps. Give `arch-doc` views ready to embed
in arc42 or another requested document. Give `arch-decision` diagrams that clarify
alternatives and trade-offs, `arch-review` cross-view inconsistencies, `arch-security`
trust-boundary and denied-path concerns, `arch-cloud`/`arch-devops` deployment
placement, and `arch-data`/`arch-event` ownership and flow semantics.

## Examples

- Create a C4 context and container set for a public order platform.
- Review a deployment diagram for missing trust boundaries and managed dependencies.
- Convert a prose payment flow into a versioned Mermaid sequence diagram with retry,
  timeout and compensation paths.
- Produce a data-flow view that distinguishes authoritative, derived and retained data.
