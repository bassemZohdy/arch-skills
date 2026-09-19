# Completed work before the framework baseline

Historical record from the previous repository revision. These completion claims are retained as history and were not revalidated by the framework documentation review.

---

## Final Metrics

| Category | Before | After |
|----------|--------|-------|
| Structural tests | 224 | 354 (+130) |
| Skillprobe scenarios | 185 | 220 (+35) |
| Pi harness scenarios | 0 | 7 (+7) |
| Activation tests | 0 | 32 (+32) |
| Integration/regression tests | 0 | 13 (+13) |
| `not_contains` assertions | 0 | 23 |
| `tool_called` assertions | 0 | 6 |
| `token_usage_under` assertions | 0 | 1 |
| Multi-run scenarios | 0 | 10 |
| Reference files (avg) | 2.9 | 3.0 |
| Weak descriptions (activation <7) | 7 | 0 |
| Broken links found & fixed | 0 | 2 |
| Duplicate headings fixed | 0 | 3 |

---

## Progress Log

### Batch 1 — Structural test upgrades
- Enhanced `test_skills.py` from 7 → 13 checks per skill (224 → 354 tests)
- Auto-discovers skills; fixed 3 real issues (2 duplicate headings, 1 catalog gap)
- Added: broken link checker, name conformance, description-length check, openai.yaml validation,
  forbidden-file check, line-count check, duplicate-heading checker, non-.md ref checker,
  empty-asset checker, diagram priority, skill-catalog consistency, external-link rot check

### Batch 2 — Behavioral test enhancements
- Added 23 `not_contains` negative assertions across test files
- Added 6 `tool_called: Write` assertions to doc-generating skills
- Added 10 multi-run reliability scenarios (runs: 3, min_pass_rate: 0.67)
- Added 1 `token_usage_under` assertion

### Batch 3 — Scenario expansion
- Expanded 5 thin skills from 5→8 scenarios: arch-security, arch-ddd, arch-api, arch-event, arch-cloud
- Expanded arch-data from 5→8 scenarios
- Total new scenarios: +35

### Batch 4 — Pi harness, integration & regression
- Created `tests-pi/` directory with 2 Pi-adapted test files (7 scenarios)
- Created `tests/test-integration.yaml` with 5 cross-skill orchestration scenarios
- Created `tests/test-regression.yaml` with 3 regression guard scenarios
- Created `tests/test_activation.py` — 32 description activation quality checks

### Batch 5 — Reference thickening & description fixes
- Added `decision-deep-dive.md` (arch-decision) — advanced DAR, sensitivity, anti-patterns
- Added `microservices-deep-dive.md` (arch-microservices) — decomposition, patterns, Conway's Law
- Fixed 4 weak descriptions: arch-antipatterns, arch-governance, arch-patterns, arch-usability
- Fixed 2 broken external links in arch-fitness

