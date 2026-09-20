# Follow-up work

The 2026-09-20 structural/DAP remediation is documented in
[the review](docs/audits/2026-09-20-remediation-review.md), including executed tests.
Do not reinterpret deterministic fixture results as live-model evidence.

The repository-side completion pass also replaced stale behavioral fixture links,
added seven generated schema-2 scenarios, tightened adapter-result checks and
provided a packaged [migration guide](framework/schema-2-migration.md). Those are
implemented; the items below depend on an actual consuming project or host choice.

Optional adoption/release work:

- Run the host-neutral behavioral scenarios on each intended consuming host and
  record actual model/adapter versions, observed routing and artifacts.
- For real schema-1 projects, plan an explicit migration with owners; capture
  missing evidence and renew affected assessments instead of inventing history.
- Adopt project-specific review identities, thresholds, cadence and retention;
  the configuration example deliberately contains unapproved placeholders.

No global installation, host adapter, scheduler or live-model run is performed by
the package builder. Consuming-host adoption remains external to the repository.
