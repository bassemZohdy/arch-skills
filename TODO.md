# TODO

## Status: Complete — All-Skill Consistency & Quality Cleanup Done

Audited all 32 skills. Overall high quality (224/224 tests pass, all under 500 lines,
no broken refs). This pass fixed consistency drift and a few weak spots.

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

- [x] 1. Fix `arch-cloud` section ordering — "Further Reading"/"Related Skills" were wedged before the Step sections; moved to the end to match the canonical Workflow → Steps → Examples → Gotchas → Further Reading → Related Skills → Template order. (Content was already complete, not skeletal.)
- [x] 2. Add `## Related Skills` section to `arch-doc` and `arch-review` (the other 30 skills had it).
- [x] 3. Normalize Review Template heading wording: `arch-api` "API Design Review Template" -> "API Review Template" to match `arch-devops`/`arch-security` `<Skill> Review Template`.
- [x] 4. Fix weak verb form in `arch-devops`, `arch-api`, `arch-cloud` frontmatter descriptions: "Guide..." -> imperative ("Design...").
- [x] 5. Enrich `arch-api` description with missing trigger keywords (OpenAPI/Swagger, governance, contract, pagination/error-handling, deprecation).
- [x] 6. De-duplicate `solution-architecture-orchestrator`: replaced verbatim conflict-priority list with a pointer to `references/orchestration-playbook.md`.
- [x] 7. Normalize `arch-fitness` structure: added `## Workflow` block, promoted `### Step N` to top-level `## Step N:`, merged the standalone `## Best Practices` into `## Common Gotchas`.
- [x] 8. Run `python3 tests/test_skills.py` — 224/224 passing.
- [x] 9. Documents verified — counts (32 skills / 224 tests / 185 scenarios / 409 total) unchanged by this quality pass; no stale heading references.
- [x] 10. Commit all changes; push to GitHub.
