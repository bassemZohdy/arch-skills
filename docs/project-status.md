# Project status and operating guide

Reviewed: 2026-09-20. This page is the current repository status reference. Historical
counts and findings remain in the dated audit documents; open adoption work remains
in [TODO.md](../TODO.md).

## Delivered repository capabilities

| Area | Current state | Evidence or command |
| --- | --- | --- |
| Skill library | 33 canonical skills; default profile exposes 3 entry points and expert exposes all 33 | `python scripts/build_packages.py --profile default ...` or `--profile expert ...` |
| DAP contracts | Framework 1.0.0, schema 2.0.0, rubric 1.0.0 and evaluator 2.0.0 are implemented and version-checked | [implementation status](dap-implementation-status.md), [records](../framework/records.md) |
| Deterministic validation | Structural, link, contract, lifecycle, publication and package-isolation checks run offline | `bash run-tests.sh` or `./run-tests.ps1` |
| Behavioral scenarios | 222 validated scenarios across 36 manifests, covering all 33 skills and activation cases | `python scripts/behavioral.py validate` |
| DAP adapter checks | Result envelopes can be validated for assertion identity and workspace evidence paths | `python scripts/dap_adapter.py validate-execution ...` |
| Baseline comparison | Compatible behavioral reports can be compared for selection drift and regressions | `python scripts/compare_behavioral.py baseline/report.json candidate/report.json ...` |
| Public links | Latest recorded audit: 0 confirmed broken, 36 unverified because of access or transport limits | `python scripts/check_links.py --external --output .cache/link-audit.json` |
| CI automation | Four offline matrix jobs run on pushes and pull requests; public-link auditing is weekly; model smoke tests are manual | [.github/workflows](../.github/workflows/) |

A passing offline check establishes repository and fixture invariants. It does not
prove model behavior, semantic truth, human identity, architecture fitness or a
consuming host's activation and tool traces.

## Use the implemented features

1. Install dependencies and build into a fresh directory. The builder does not
   overwrite an existing destination.

   ```sh
   python -m pip install -r requirements.txt
   python scripts/build_packages.py --profile expert --output .cache/expert
   ```

2. Run the required offline gate from the repository root:

   ```sh
   bash run-tests.sh       # Linux/macOS
   ./run-tests.ps1         # Windows
   ```

3. Validate or run behavioral scenarios. A live run requires a configured model
   endpoint; use the adapter protocol in [test automation](test-automation.md).

   ```sh
   python scripts/behavioral.py validate
   python scripts/behavioral.py run --packages .cache/expert \
     --output .cache/behavioral-results --limit 0 --max-calls 15
   ```

4. For DAP adapter executions, validate the returned result against its manifest
   and isolated workspace. `unavailable` stays explicit and is not a pass.

5. Compare a candidate report with a compatible baseline before changing a live
   quality threshold. Keep adapter, model, package, manifest, case selection and
   repeat settings pinned.

## Status and planning rules

Use these labels consistently in documentation and issue plans:

- **Implemented** — exercised by deterministic repository checks or a recorded
  fixture; describe the command and the boundary.
- **Opt-in** — available through a manual command or workflow and not a required
  release gate.
- **Adoption work** — requires a real model, host adapter, consuming project,
  organization policy or external authority; keep it in [TODO.md](../TODO.md).
- **Historical** — retained for traceability and never presented as current proof.

When skills or scenarios change, update the affected source, run the full offline
gate, refresh scenario and skill counts, and update this page only with verified
results. Do not mark a host-specific behavior implemented from a synthetic adapter
result, and do not convert an unavailable external-link probe into a broken-link
finding.
