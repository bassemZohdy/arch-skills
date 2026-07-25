# TODO

## Status: Complete — Full review & update pass done

A second full review of all 32 skills. All systemic issues resolved: dead links fixed,
orphaned reference files cited, descriptions strengthened, diagrams converted to Mermaid.
224/224 tests pass; counts unchanged (32 skills / 224 tests / 185 scenarios).

## Skills (32)

| Category | Skills |
|----------|--------|
| Orchestration | solution-architecture-orchestrator |
| Core | arch-doc, arch-review, arch-fitness, arch-decision, arch-governance |
| Design Fundamentals | arch-principles, arch-antipatterns |
| Technical | arch-security, arch-perf, arch-resilience, arch-test |
| Architecture | arch-api, arch-cloud, arch-event, arch-ddd, arch-data, arch-metrics, arch-integration, arch-microservices, arch-patterns, arch-refactoring |
| Frontend | arch-frontend |
| Operations | arch-observability, arch-migration, arch-devops, arch-cost |
| Features & AI | arch-features, arch-ai |
| NFR | arch-usability, arch-accessibility, arch-compliance |

## Metrics

| Metric | Value |
|--------|-------|
| Skills | 32 |
| Tests | 224 |
| Scenarios | 185 |
| Total Tests | 409 |

## Cleanup Tasks

- [x] 1. Fix dead links — created missing `arch-decision` assets (`dar-expedited.md`, `adr-template.md`); moved misplaced reference pointers in `arch-ai` and `arch-devops` into their `## Further Reading` sections.
- [x] 2. Cite orphaned reference files — 49 specialized references across 28 skills were never linked from SKILL.md; all now cited in `## Further Reading` so they load on demand.
- [x] 3. Strengthen descriptions — converted 18 "Guide..." verbs to imperatives (Design/Model/Plan/etc.); enriched 5 weak descriptions with missing trigger keywords (observability, frontend, features, usability, compliance, governance).
- [x] 4. Structural consistency — normalized `arch-cloud` Related Skills to the sibling bullet format; moved out-of-order body sections in `arch-doc` and `arch-review` above Common Gotchas; expanded `arch-fitness` Step 3-5 stubs into real guidance.
- [x] 5. Convert diagrams to Mermaid — replaced 23 load-bearing ASCII-art diagrams with fenced ```mermaid blocks across 10 skills (resilience, test, devops, microservices, ddd, event, metrics, patterns, refactoring). Aligns with the Mermaid > PlantUML > Draw.io convention.
- [x] 6. De-duplication — inspected; references are mostly genuine expansions or condensed cheat-sheets, not bloat (bodies average ~190 lines, all <500). No trimming needed.
- [x] 7. Validated — 224/224 tests pass; counts unchanged (32 / 224 / 185 / 409); no file over 500 lines; all skills retain Further Reading + Related Skills.
