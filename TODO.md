# Follow-up work

The 2026-09-20 structural/DAP remediation is documented in
[the review](docs/audits/2026-09-20-remediation-review.md), including executed tests.
Do not reinterpret deterministic fixture results as live-model evidence.

The repository-side completion pass also replaced stale behavioral fixture links,
added seven generated schema-2 scenarios, tightened adapter-result checks and
provided a packaged [migration guide](framework/schema-2-migration.md). Those are
implemented; the items below depend on an actual consuming project or host choice.

The full skills/link review is documented in
[the latest audit](docs/audits/2026-09-20-full-project-review.md). Repository fixes
and regression checks are complete; external requests blocked by network/access
controls remain explicitly unverified in its evidence.

Test automation is implemented in [the runner and workflow guide](docs/test-automation.md).
Offline CI validates all 222 behavioral scenarios; the model-response workflow is
opt-in and requires configuration. Scheduled public-link audits retain evidence.

Remaining test improvements:

- Configure the endpoint/model and run the 15-call smoke workflow; record the first
  real baseline. Synthetic adapter tests are not live skill-quality evidence.
- Implement one actual host adapter, then execute the seven DAP lifecycle scenarios
  with fixture setup and preserved-baseline verification. The repository now
  enforces assertion identity and evidence-file completeness for returned results.
- Configure an actual host adapter for the activation manifest; the runner now
  accepts host-observed `skills_used` traces and has positive/negative scenarios.
- Calibrate remaining keyword assertions on real outputs; move priority cases to
  typed decisions, artifact checks or reviewed semantic rubrics.
- Compare baseline/candidate versions with identical model/host settings before
  making behavioral pass rates a release gate; `scripts/compare_behavioral.py`
  now automates the comparison and rejects drift.

Project adoption work:

- Run the host-neutral behavioral scenarios on each intended consuming host and
  record actual model/adapter versions, observed routing and artifacts.
- For real schema-1 projects, plan an explicit migration with owners; capture
  missing evidence and renew affected assessments instead of inventing history.
- Adopt project-specific review identities, thresholds, cadence and retention;
  the configuration example deliberately contains unapproved placeholders.

No global installation, host adapter, scheduler or live-model run is performed by
the package builder. Consuming-host adoption remains external to the repository.
