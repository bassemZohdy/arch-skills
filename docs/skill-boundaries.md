# Skill boundaries and consolidation review

Reviewed against all 33 canonical skills in skills/*/SKILL.md.

## Review result

The skills are complementary and should remain separate. No current pair has enough responsibility overlap to justify a merge, and no skill has a scope large enough to require a split. The canonical skill files contain no references to a named assistant, model provider, CLI, installation directory or host-specific tool API.

The cleanup is therefore boundary-focused:

- host names, commands, model identifiers and tool APIs belong to adapter documentation and test configuration;
- canonical skills describe architecture inputs, reasoning, outputs and evidence;
- orchestration, design review and process evaluation remain separate;
- governance, compliance and security remain separate because they answer different questions;
- decision analysis and ADR documentation remain separate because scoring is not record keeping.

## Responsibility map

| Boundary | Keep separate because |
| --- | --- |
| arch-orchestrator / arch-review / arch-evaluate | Orchestration coordinates work; review assesses design fitness; evaluation assesses DAP process evidence and artifact completeness. |
| arch-decision / arch-governance / arch-compliance | Decision analysis compares options; governance defines authority and exceptions; compliance designs regulatory controls and auditability. |
| arch-doc / arch-decision | Documentation publishes views and ADRs; decision analysis supplies structured trade-offs and recommendation evidence. |
| arch-principles / arch-antipatterns / arch-refactoring | Principles define desired properties; anti-patterns identify violations; refactoring plans safe change. |
| arch-cloud / arch-cost / arch-devops | Cloud architecture, financial controls and delivery operations have different decisions and evidence. |
| arch-api / arch-integration / arch-event / arch-microservices | API contracts, system integration, asynchronous event flows and service topology are related but not interchangeable. |
| arch-ddd / arch-patterns | Domain modeling identifies boundaries and behavior; patterns select structural forms that can host those models. |
| arch-perf / arch-resilience / arch-observability | Performance targets, failure behavior and operational evidence require different analyses. |
| arch-frontend / arch-usability / arch-accessibility | Implementation structure, user effectiveness and inclusive access are distinct concerns. |
| arch-security / arch-compliance | Security controls protect systems; compliance maps obligations, evidence and retention. |
| arch-data / arch-ai | General data ownership and lifecycle differ from AI-specific data, model and evaluation concerns. |
| arch-features / arch-devops | Feature management controls exposure and experimentation; DevOps controls build, deploy and release operations. |

## Cleanup decisions

- No merges. Merging would make activation less precise and would mix different evidence types.
- No splits. Each skill has one primary architectural concern and its current related-skill links describe supporting boundaries.
- Clarify descriptions. Governance now points regulatory control design to arch-compliance; review and evaluation remain explicitly distinct.
- Keep adapters outside skills. Adapter-specific tests and metadata can evolve without changing the portable skill contract.

Future consolidation should require a repeated overlap finding, shared inputs and outputs, and a smaller combined activation surface. A name change or a shorter file alone is not sufficient evidence for a merge.