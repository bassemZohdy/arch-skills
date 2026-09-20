# Follow-up work

The repository-side implementation is complete for its deterministic contracts,
fixture scope and offline automation. Current counts, operating commands and
status labels are in the [project status guide](docs/project-status.md). Historical
findings and test batches remain in the dated audit documents; do not reinterpret
synthetic fixture results as live-model evidence.

The repository now provides:

- Schema-2 DAP records, migration guidance and seven generated lifecycle fixtures.
- Offline validation for all 33 skills and 222 behavioral scenarios across 36 manifests.
- Strict host-result checks for assertion identity, status consistency and workspace
  evidence paths.
- Activation scenarios using host-observed `skills_used` traces.
- Compatible baseline/candidate comparison through `scripts/compare_behavioral.py`.
- Weekly public-link auditing with retained evidence; inaccessible responses remain
  unverified rather than being treated as broken.

## Open adoption work

These items require a real consuming host, model, project or organizational authority
and therefore cannot be completed by repository-only automation.

### Live quality and host integration

- Configure the endpoint/model and run the 15-call smoke workflow; record the first
  real baseline. Synthetic adapters and mocked HTTP are not live skill-quality evidence.
- Implement one actual host adapter and execute the seven DAP lifecycle scenarios,
  including fixture setup, artifact verification, preserved history and baseline
  immutability.
- Configure a host adapter for the activation manifest and retain observed routing
  traces from the host.

### Calibration and release evidence

- Calibrate keyword assertions on real outputs; move priority cases to typed
  decisions, artifact checks or reviewed semantic rubrics.
- Compare repeated baseline/candidate runs with identical pinned model and host
  settings before introducing a live-quality release threshold. Two or three samples
  are smoke tests, not a reliability estimate.

### Consuming-project adoption

- Run the host-neutral scenarios on each intended host and record actual model,
  adapter, routing and artifact versions.
- For real schema-1 projects, plan an explicit migration with owners; capture missing
  evidence and renew affected assessments instead of transferring approvals.
- Adopt project-specific review identities, thresholds, cadence and retention. The
  configuration example deliberately contains unapproved placeholders.

The package builder performs no global installation, host setup, scheduler
provisioning or live-model run. Those boundaries are intentional and remain outside
this repository until a consuming project supplies the required integration.
