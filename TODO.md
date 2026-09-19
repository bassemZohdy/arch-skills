# Implementation backlog

All DAP tasks are complete in the reference implementation. Framework target: 1.0.0.

References: [framework](docs/deterministic-architecture-process.md), [review](docs/framework-review.md), [implementation plan](docs/framework-implementation-plan.md), [completed work](docs/completed-work.md).

## Completed tasks

- [x] **DAP-001 — Shared contracts and configuration**
  - Added version, project schema, criteria catalogue and configuration example under framework/.
  - Implemented validation for semantic versions, weights, authority, reviewers, limits and stable IDs.
- [x] **DAP-002 — Requirements, trace graph and architecture templates**
  - Added record guidance, requirement/checkpoint templates, arc42 mapping and DAP ADR template.
  - Added deterministic RTM generation from typed trace links.
- [x] **DAP-003 — Durable state and recovery**
  - Added atomic JSON checkpoints, state hashes and expected-revision conflict detection.
  - Added interruption fixture and unit coverage.
- [x] **DAP-004 — Preparation and scope contract**
  - Integrated greenfield, brownfield and mixed-scope rules into arch-orchestrator.
  - Documented missing-evidence and evaluator-unavailable behavior.
- [x] **DAP-005 — Interview and convergence rules**
  - Added explicit round, budget, stable-baseline and stakeholder-confirmation rules to the orchestrator contract.
- [x] **DAP-006 — Design, ADR and DAR integration**
  - Updated orchestrator, ADR documentation and DAR gates/sensitivity guidance.
- [x] **DAP-007 — Review authority and exceptions**
  - Added fail-closed governance rules for security, privacy, compliance, material cost, cross-team and irreversible decisions.
- [x] **DAP-008 — Change impact and re-entry**
  - Added requirement/design/review re-entry rules, stale evidence handling and supersession guidance.
- [x] **DAP-009 — Structural validation and scoring**
  - Implemented scripts/dap_validate.py and the Q/D/F/B/T/A/S formula with explicit unknown, N/A and empty-population handling.
- [x] **DAP-010 — Process evaluator skill**
  - Added skills/arch-evaluate, UI metadata, evaluation contract and the GitHub mirror.
- [x] **DAP-011 — Reports and freshness**
  - Added input manifests, report publishing and generated RTM/report tooling; generated reports are excluded from assessed hashes.
- [x] **DAP-012 — Lifecycle examples**
  - Added greenfield, brownfield, interrupted and blocking-review fixtures.
- [x] **DAP-013 — Packaging and mirrors**
  - Added mirror validation and verified the evaluator source/mirror hash.
- [x] **DAP-014 — Validation and usage documentation**
  - Added six deterministic tests and verified validator, scorer, RTM and mirror commands.

## Verification evidence

    python -m unittest discover -s tests -p test_dap.py -v  -> 6 tests passed
    python scripts/dap_validate.py examples/greenfield/architecture -> 76.0%, ready=true
    python scripts/dap_validate.py examples/blocking-review/architecture -> 76.0%, ready=false (security review pending)
    python scripts/dap_rtm.py examples/greenfield/architecture -> generated RTM
    python scripts/check_dap_mirrors.py -> mirrors: ok

The repository's existing live-model skillprobe scenarios remain opt-in and are not represented as deterministic DAP proof. Re-run python tests/test_skills.py after syncing the complete repository tree when changing skill structure.
