# awesome-architecture.com — Analysis & Skill Mapping

Analysis of [awesome-architecture.com](https://awesome-architecture.com/) (published version of
`mehdihadeli/awesome-software-architecture`) and how its catalog maps onto the skills in this repo.
Historical sitemap baseline (2026-07-24): **305 topic pages**. Counts and the
taxonomy below describe that baseline, not current site coverage.

## Route migration (2026-09-20)

The upstream site now uses collection pages and `/topics/<source-path-slug>`
routes. All 297 legacy topic URLs referenced by this repository were mapped to
current source files at upstream revision
`686546eb1bb1167229d409b9e9eb996a882aeadc`; the slug algorithm is defined in
`web/src/lib/content.ts`. Renamed AI topics were mapped explicitly, including
Microsoft Agent Framework, evaluation/test, skills/subagents/plugins and agent
coding. ACP now refers to Agent Client Protocol in that catalog.

The migration preserves topic-specific links. Source-route resolution is distinct
from HTTP reachability and from validating resources inside a topic hub. See the
[current audit](audits/2026-09-20-full-project-review.md) for executed checks and
network limitations. Use primary specifications for normative decisions; this
community catalog is optional further reading.

## What the Site Is

A continuously updated, community-curated catalog of software-architecture resources. Every topic
page is a link hub with sections for Resources, Articles, Videos, Libraries, Samples, and Books —
it contains no prescriptive guidance of its own. Its value to this repo is twofold:

1. **Taxonomy** — a comprehensive, community-validated map of architecture concerns.
2. **Curated deep links** — per-topic external reading, now integrated into each skill via
   `skills/<name>/references/awesome-architecture.md` (287 of 305 pages linked, 94%).

## Taxonomy → Skill Mapping

| Site Section | Pages | Mapped To |
|--------------|-------|-----------|
| `architectural-design-principles/*` (SOLID, GRASP, CAP, coupling, cohesion, DRY, KISS, YAGNI...) | 20 | arch-principles |
| `design-patterns/*` (GoF + repository, specification, mediator...) | 19 | arch-patterns |
| `cloud-design-patterns/*` (circuit breaker, bulkhead, outbox, inbox, strangler fig, BFF, sidecar...) | 13 | arch-patterns, arch-resilience, arch-event, arch-migration, arch-api |
| `actor-model-architecture/*` (Akka.NET, Orleans, ProtoActor) | 4 | arch-patterns |
| Architecture styles (`clean-architecture`, `hexagonal-architecture`, `onion-architecture`, `vertical-slice-architecture`, `modular-monolith`, `service-oriented-architecture`) | 6 | arch-patterns |
| `domain-driven-design/*` (bounded context, aggregates, value objects, domain events...) | 19 | arch-ddd |
| `event-driven-architecture`, `event-sourcing`, `cqrs`, `eventual-consistency` | 4 | arch-event |
| `messaging/*` (Kafka, RabbitMQ, NATS, ZeroMQ, AsyncAPI, CDC) | 8 | arch-event, arch-integration, arch-doc |
| `microservices/*` (boundaries, communication, API gateway, observability, resiliency, security, testing, tools) | 35 | arch-microservices, arch-api, arch-observability, arch-resilience, arch-security, arch-test, arch-frontend, arch-metrics |
| `service-mesh/*`, `service-discovery/*` | 7 | arch-microservices |
| `database/*` (sharding, replication, NoSQL, relational) | 10 | arch-data |
| `caching`, `back-pressure`, `distributed-locking`, `distributed-transactions`, `ids`, `concurrency` | 6 | arch-data, arch-resilience, arch-perf |
| `devops/*` (Docker, Kubernetes, CI/CD, GitOps, terminal) | 30 | arch-devops |
| `iaas/*` (Terraform, Pulumi, Ansible, Nomad) | 5 | arch-devops |
| `reverse-proxy-lb/*` (NGINX, HAProxy, Traefik, Envoy, YARP...) | 9 | arch-devops |
| `azure/*` | 30 | arch-cloud, arch-security |
| `cloud-native`, `cloud-best-practices`, `serverless`, `paas/*` | 7 | arch-cloud, arch-cost |
| `modeling/*` (event storming, event modeling, ER/UML diagrams, tools) | 16 | arch-doc, arch-ddd |
| `architecture-documententation` | 1 | arch-doc, arch-decision, arch-review |
| `anti-patterns/*` (big ball of mud, god object, code smells...) | 7 | arch-antipatterns, arch-refactoring, arch-migration |
| `refactoring`, `clean-code`, `code-review` | 3 | arch-refactoring, arch-principles, arch-review, arch-test |
| `ai/*` (agents, RAG, MCP, A2A/ACP, evaluation, memory, prompt engineering, self-hosting, tools) | 27 | arch-ai, arch-security |
| `micro-frontend` | 1 | arch-frontend |
| `rest`, `grpc` | 2 | arch-api, arch-integration |
| `scaling`, `algorithm`, `systems-design/*` | 4 | arch-perf, arch-review |
| `software-architecture`, `open-source` | 2 | arch-decision, arch-fitness, arch-governance, arch-review |
| `abstraction`, `object-oriented-design`, `functional`, `type-driven-design`, `design-best-practices/*` | 7 | arch-principles |

## Gaps Found & Closed

| Gap | Evidence | Resolution |
|-----|----------|------------|
| **Vertical Slice Architecture** | 0 matches in `skills/`; site has a dedicated page | Added to `arch-patterns` SKILL.md (pattern table, selection matrix, description) + full section in `references/architecture-patterns.md` |
| **Modular Monolith** | Only 3 passing mentions; site has a dedicated page | Same treatment as above in `arch-patterns` |
| Dangling pointers | `arch-antipatterns` and `arch-principles` SKILL.md pointed to non-existent `references/external-resources.md` | Removed; superseded by the new `## Further Reading` section |
| Test coverage | `arch-antipatterns` and `arch-principles` missing from the hardcoded list in `tests/test_skills.py` | Added (217 structural checks total) |

## Site Sections With No Skill Coverage

- `/others/`, `/open-source/` (partially linked from arch-governance), `/algorithm/` (linked from arch-perf),
  `/functional/`, `/object-oriented-design/`, `/type-driven-design/` (linked from arch-principles) —
  all cross-cutting; no dedicated skill warranted.
- Unused pages (7 of 305): index/hub pages (`/azure/`, `/modeling/`, `azure-resource`,
  `azure-app-service-plan`), a duplicate (`deployment-tools/jenkins`), and a dead project
  (`service-mesh/maesh`).

## Skills With No Direct Site Coverage

The catalog has no dedicated sections for **arch-accessibility**, **arch-usability**,
**arch-compliance**, **arch-features**, **arch-fitness**, **arch-metrics**, **arch-cost**,
**arch-governance**, **arch-test**, **arch-decision**. These skills got a short
`awesome-architecture.md` noting the gap and linking the closest matching sections (e.g.
arch-test → `microservices/testing`, arch-cost → `cloud-best-practices`).

## Notes

- Site URL typos are kept verbatim in links: `architecture-documententation`, `domain-stroytelling`,
  `services-boundries`, `high-availibility`, `debuging-development`.
- The `/ai/` section (27 pages incl. MCP, A2A, agent frameworks, harness engineering) is the site's
  fastest-growing area — worth re-syncing periodically.
- Future work: if dedicated skills for feature flags, FinOps, or governance tooling are ever added,
  re-check the catalog for matching sections.
