# arch-evaluate calibration — 2026-11-02

Scope: response-only behavior of `arch-evaluate` against typed JSON scenarios in
[`tests/test-arch-evaluate-calibration.yaml`](../../tests/test-arch-evaluate-calibration.yaml)
and the existing [`tests/test-arch-evaluate.yaml`](../../tests/test-arch-evaluate.yaml).
Expected values follow the packaged `scripts/dap` scorer (exact fractions on a
0..100 scale, T = min(F, B), weight validation, N/A authorization, readiness gates).

## Method

- Packages: fresh `--profile expert` builds, one per iteration.
- Runner: `scripts/behavioral.py run --limit 0` with a custom response-only
  command adapter that sends only `SKILL.md` as system context and permits no tools.
  The adapter strips a Markdown code fence around the answer before the JSON assertions run.
- Model: one small pinned model alias, chosen so that the skill's own guidance
  dominates the outcome. A provider alias is not proof of an immutable revision.
- Each run is one independent observation per scenario. Two runs at the end are a
  smoke-level stability check, not a reliability estimate.

## Results

| Iteration | Skill | Suite | Scenarios | Assertions |
| --- | --- | --- | --- | --- |
| 0 baseline | original | existing 5 | 5/5 (100%) | 6/6 |
| 0 baseline | original | calibration 28 | 23/28 (82.1%) | 50/55 (90.9%) |
| 1 | + scoring/gate rules | calibration 28 | 28/28 (100%) | 55/55 |
| 1 | original | 14 held-out transfer cases | 10/14 (71.4%) | 20/26 (76.9%) |
| 1 | + scoring/gate rules | 14 held-out transfer cases | 12/14 (85.7%) | 24/26 (92.3%) |
| 2 | + score/exact output rule | held-out, two runs | 13/14, 14/14 | 25/26, 26/26 |
| final | original | merged 42 | 33/42 (78.6%) | 70/81 (86.4%) |
| final | final | merged 42, run A | 42/42 (100%) | 81/81 |
| final | final | merged 42, run B | 42/42 (100%) | 81/81 |
| final | final | existing 5 | 5/5 (100%) | 8/8 |

## Feedback and changes

Baseline failures traced to rules that existed only in references or code:

- T was not defined in `SKILL.md`; the model refused to combine F and B.
- Authorized N/A was accepted for requirements_quality, and an unauthorized N/A was
  assumed not to block S.
- The traceability-largest weight rule (ties allowed) was unknown.
- Missing ADRs were counted as one target instead of ten failing checks.
- A planned VER was not recognized as completing a design-stage F chain.
- The relationship between `overall_score` (one-decimal number) and `overall_exact`
  (fraction string) was unspecified.

Changes:

- Added a compact "Scoring and gate rules" section to `skills/arch-evaluate/SKILL.md`
  that mirrors the packaged scorer.
- Clarified two ambiguous calibration prompts ("denominator" means counted checks).
- `json_equals` now compares JSON numbers by value (50 equals 50.0); booleans and
  strings still never equal numbers. A false negative had occurred on a correct answer.

## Boundaries

Response-only results do not prove host discovery, tool use, validator execution
or DAP lifecycle behavior. The transfer cases were written after iteration 0 and
merged into the repository manifest; future changes need fresh held-out cases.
