# Follow-up work

Only unfinished work is listed here. Current implementation status, available commands
and repository capabilities are documented in [docs/project-status.md](docs/project-status.md).

## Live model and host integration

- Configure the endpoint/model and run the 16-call smoke workflow; record the first
  real baseline. Synthetic adapters and mocked HTTP are not live skill-quality evidence.
- Implement one actual host adapter and execute the seven DAP lifecycle scenarios,
  including fixture setup, artifact verification, preserved history and baseline
  immutability.
- Configure a host adapter for the activation manifest and retain observed routing
  traces from the host.

## Quality calibration and release evidence

- Calibrate keyword assertions on real outputs; move priority cases to typed
  decisions, artifact checks or reviewed semantic rubrics.
- Compare repeated baseline/candidate runs with identical pinned model and host
  settings before introducing a live-quality release threshold. Two or three samples
  are smoke tests, not a reliability estimate.

## Consuming-project adoption

- Run the host-neutral scenarios on each intended host and record actual model,
  adapter, routing and artifact versions.
- For real schema-1 projects, plan an explicit migration with owners; capture missing
  evidence and renew affected assessments instead of transferring approvals.
- Adopt project-specific review identities, thresholds, cadence and retention. The
  configuration example deliberately contains unapproved placeholders.

## External verification

- Recheck the 50 [currently unverified URLs](docs/audits/2026-09-20-link-recheck-latest.json)
  from an unrestricted network;
  do not treat blocked, rate-limited or timed-out probes as broken links.

## Diagram rendering coverage

- Run the manually triggered Mermaid renderer workflow and retain successful
  SVG/report evidence when GitHub can download its headless browser.
- Add equivalent pinned PlantUML and Draw.io renderer jobs only if those formats
  become required release evidence; the current static inventory covers all
  Mermaid sources.
