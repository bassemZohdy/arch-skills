# Specialist Skill Catalog

Stage-1 discovery metadata for the specialist skills in this repository. Read this
catalog during skill discovery; load a specialist's SKILL.md only after selecting it.

For each entry: purpose, triggers (when to select), inputs it needs, outputs it
produces, and dependencies. "Partial" marks overlap-only coverage — document the
limitation when relying on it.

## Design & Structure

| Skill | Purpose | Select When | Needs | Produces | Dependencies |
|-------|---------|-------------|-------|----------|--------------|
| arch-patterns | Architecture style selection (clean, hexagonal, layered, vertical slice, modular monolith, microservices, actor, cloud patterns) | Style undecided or must be validated | Requirements, QA priorities, constraints | Style recommendation + trade-offs | QA priorities |
| arch-principles | Design principles (SOLID, GRASP, coupling/cohesion, CAP, DRY/KISS/YAGNI) | Boundary or design-quality judgment needed | Proposed structure | Principle evaluation, violation risks | arch-patterns |
| arch-antipatterns | Anti-pattern detection (big ball of mud, god object, leaky abstractions) | Modernization, review, or legacy context | Existing/proposed structure | Anti-pattern findings, containment options | arch-principles |
| arch-ddd | Domain modeling, bounded contexts, aggregates, domain events | Non-trivial business domain | Functional requirements, domain vocabulary | Domain model, context map | Requirements analysis |

## Application & Integration

| Skill | Purpose | Select When | Needs | Produces | Dependencies |
|-------|---------|-------------|-------|----------|--------------|
| arch-microservices | Service boundaries, communication, gateway, mesh, testing strategy | Microservices or service decomposition in play | Domain model, scale, team structure | Service decomposition, communication patterns | arch-ddd, arch-patterns |
| arch-api | API design (REST, gRPC, GraphQL, gateway, versioning) | External or internal APIs required | Service boundaries, consumers | API contracts, versioning policy | arch-microservices or arch-patterns |
| arch-integration | Messaging, brokers, sync/async integration, anti-corruption layers | System-to-system integration | Existing systems, integration requirements | Integration patterns, broker choices | arch-patterns |
| arch-event | Event-driven design, event sourcing, CQRS, outbox/inbox | Async, streaming, or event-sourced requirements | Integration needs, consistency requirements | Event model, consistency strategy | arch-integration, arch-data |
| arch-frontend | Frontend architecture, micro-frontends, UI composition | Non-trivial UI surface | UX requirements, team structure | Frontend structure, composition approach | arch-api |

## Data

| Skill | Purpose | Select When | Needs | Produces | Dependencies |
|-------|---------|-------------|-------|----------|--------------|
| arch-data | Data architecture: storage selection, sharding, replication, caching, consistency | Persistent state, data ownership, residency | Data requirements, scale, consistency needs | Data ownership map, storage decisions | arch-ddd, arch-patterns |

## Quality & Cross-Cutting

| Skill | Purpose | Select When | Needs | Produces | Dependencies |
|-------|---------|-------------|-------|----------|--------------|
| arch-security | Threat modeling, security controls, secrets, supply chain | Any trust boundary; always for regulated/customer-facing | Architecture shape, data classification | Threat model, security controls | Style + deployment selected |
| arch-compliance | Regulatory compliance, data residency, auditability | Regulated industry or stated compliance constraints | Compliance requirements, data flows | Compliance controls, residency design | arch-security |
| arch-resilience | Availability, idempotency, circuit breakers, back-pressure, DR | Availability/recovery requirements exist | Failure scenarios, RTO/RPO | Resilience patterns, recovery design | Deployment architecture |
| arch-perf | Scalability, caching, concurrency, capacity | Scale or latency requirements | Expected scale, load profile | Scaling strategy, capacity plan | Deployment architecture |
| arch-observability | Logging, metrics, tracing, monitoring | Any production system | Critical flows, SLOs | Observability design | Deployment architecture |
| arch-test | Test strategy, testability of architecture | Production or mission-critical | Architecture shape | Test strategy, quality gates | Application design |
| arch-usability / arch-accessibility | UX quality, accessibility standards | Customer-facing applications | User requirements | Usability/accessibility requirements & checks | Requirements analysis |

## Platform & Delivery

| Skill | Purpose | Select When | Needs | Produces | Dependencies |
|-------|---------|-------------|-------|----------|--------------|
| arch-cloud | Cloud-native design, serverless, managed services, Azure guidance | Cloud or hybrid deployment | Environment constraints, workload profile | Cloud architecture, service selection | Style + scale known |
| arch-devops | CI/CD, containers, Kubernetes, IaC, GitOps | Any deployable system | Deployment environment, team maturity | Delivery pipeline, platform design | arch-cloud or environment known |
| arch-cost | Cost modeling, FinOps | Budget constraints or cloud deployment | Deployment + scale design | Cost model, optimization options | arch-cloud, arch-devops |

## AI

| Skill | Purpose | Select When | Needs | Produces | Dependencies |
|-------|---------|-------------|-------|----------|--------------|
| arch-ai | LLM/agent architecture, RAG, MCP, evaluation, AI safety | AI/LLM features in scope | AI requirements, data context | AI architecture, model/integration choices | arch-data, arch-security |

## Lifecycle & Governance

| Skill | Purpose | Select When | Needs | Produces | Dependencies |
|-------|---------|-------------|-------|----------|--------------|
| arch-migration | Strangler fig, modernization sequencing | Modernization/migration initiatives | Current state, target state, constraints | Migration roadmap, increment plan | arch-patterns, arch-antipatterns |
| arch-refactoring | Safe code-level restructuring toward target design | Modernization with existing codebase | Current structure, target pattern | Refactoring sequence | arch-migration |
| arch-decision | Structured trade-off analysis, ADRs | Significant or contested decisions (always on conflict) | Decision statement, options, criteria | ADRs, decision rationale | Any specialist output |
| arch-evaluate | Deterministic Architecture Process completeness and artifact-evidence assessment | A frozen DAP baseline must be evaluated independently of design authoring | Frozen architecture baseline, versioned configuration, evidence records | Read-only findings, Q/D/F/B/T/A/S scores, readiness gate and report | DAP contracts and structural validators |
| arch-doc | C4, arc42, ISO 42010, documentation automation | Documentation deliverable required (default: yes) | Synthesized architecture | Architecture documentation set | Synthesis complete |
| arch-review | Independent architecture review, quality-attribute evaluation | Validation gate; QA prioritization support | Draft architecture | Review findings, risks | Draft architecture |
| arch-fitness | Fitness functions, architecture rules in CI | Evolutionary governance requested | Validated architecture | Executable architecture rules | Final architecture |
| arch-metrics | Architecture metrics and measurement | Maintainability governance requested | Codebase/architecture access | Metric baselines, thresholds | Final architecture |
| arch-governance | Standards, guardrails, technology governance | Enterprise standards in play | Org standards, constraints | Governance model | — |
| arch-features | Feature flags and progressive delivery | Progressive rollout requirements | Delivery strategy | Feature management design | arch-devops |

## Category Mapping (Generic Request Vocabulary)

Use this when a request names capabilities rather than repo skills:

- requirements-analysis → orchestrator itself (no dedicated skill; do basic analysis, flag for review)
- domain-modeling → arch-ddd
- architecture-style-selection → arch-patterns
- application-architecture → arch-patterns + arch-principles
- microservices-architecture → arch-microservices
- integration-architecture → arch-integration
- api-design → arch-api
- event-driven-architecture → arch-event
- workflow-orchestration → arch-event + arch-integration (partial; document limitation)
- data-architecture → arch-data
- security-architecture → arch-security
- identity-access-management → arch-security (partial; document limitation)
- cloud-architecture → arch-cloud
- kubernetes-openshift-architecture → arch-devops
- reliability-resilience → arch-resilience
- scalability-performance → arch-perf
- observability → arch-observability
- devsecops-cicd → arch-devops (+ arch-security for DevSecOps controls)
- cost-architecture → arch-cost
- compliance-data-residency → arch-compliance
- ai-llm-architecture → arch-ai
- architecture-decision-records → arch-decision
- architecture-documentation → arch-doc
- architecture-review → arch-review
