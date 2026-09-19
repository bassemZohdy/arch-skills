# Deterministic Architecture Process implementation status

Framework version: 1.0.0  
Repository: arch-skills  
Implementation baseline: 51176ba98cac296034c93c3b09d8acbca91f540d

## What DAP means

DAP is the Deterministic Architecture Process. It is a repeatable, evidence-backed operating model for turning an incomplete requirement into a reviewed architecture baseline.

It has six stages:

1. Capture the initial requirement seed.
2. Prepare the run by classifying scope, loading existing evidence and recording gaps.
3. Interview stakeholders and converge requirements using explicit quality and stability gates.
4. Develop architecture views and ADRs together.
5. Route risky or governed decisions through the configured human review authority.
6. Produce an arc42 description, ADR log, traceability graph and evaluation report.

“Deterministic” applies to the recorded state transitions, gate rules, evidence requirements and score arithmetic. It does not mean that an LLM will invent the same questions or that a system has only one valid architecture.

## Completed DAP tasks

| Task | Delivered implementation |
| --- | --- |
| DAP-001 | Versioned framework, schema and rubric contracts; configuration example; stable-ID and authority validation |
| DAP-002 | Requirements, design, decision, verification and exception record guidance; checkpoint and requirement templates; arc42 mapping; RTM generator |
| DAP-003 | Atomic checkpoints, state hashes and expected-revision conflict detection |
| DAP-004 | Orchestrator rules for greenfield, brownfield and mixed-scope preparation |
| DAP-005 | Interview round, budget, convergence, stakeholder confirmation and MoSCoW rules |
| DAP-006 | Integrated view/ADR guidance; mandatory constraints and bounded DAR sensitivity |
| DAP-007 | Fail-closed review authority and exception rules for security, privacy, compliance, cost and cross-team impact |
| DAP-008 | Requirement/design/review change routing, dependency impact and supersession guidance |
| DAP-009 | Deterministic validator and Q/D/F/B/T/A/S score calculation |
| DAP-010 | arch-evaluate skill and evaluation contract |
| DAP-011 | Input manifests, report publishing and stale-report detection |
| DAP-012 | Greenfield, brownfield, interrupted and blocking-review lifecycle fixtures |
| DAP-013 | Portable packaging and isolated validation guidance |
| DAP-014 | Deterministic tests, usage documentation and verification commands |

## Verification evidence

Executed from the repository root:

~~~text
python -m unittest discover -s tests -p test_dap.py -v
7 tests passed

python scripts/dap_validate.py examples/greenfield/architecture
overall_score: 76.0
gate.ready: true

python scripts/dap_validate.py examples/blocking-review/architecture
overall_score: 76.0
gate.ready: false
blocking finding: security review is not approved

python scripts/dap_rtm.py examples/greenfield/architecture
generated the requirements traceability matrix

python -m compileall -q scripts tests/test_dap.py
passed
~~~

Post-baseline repository validation:

~~~text
python tests/test_skills.py
371 structural checks passed across 33 skills

python -m unittest discover -s tests -p 'test_dap*.py'
12 tests passed

python tests/test_activation.py
33 descriptions scored Good or better

python scripts/dap_adapter.py validate-scenarios tests/dap-adapter-scenarios.json
5 scenarios validated

python scripts/dap_adapter.py validate-result tests/dap-adapter-result.example.json --scenario-id DAP-BEH-001
unavailable result shape validated; no live execution claimed

python -m compileall -q scripts tests
passed
~~~

Live-model adapter scenarios remain opt-in. They are separate from the deterministic DAP checks and do not change the score or gate result.

## Adapter coverage

The repository includes five host-neutral DAP behavioral scenarios covering
greenfield preparation, brownfield gaps, interrupted-session recovery,
blocking-review behavior and versioned/freshness-safe evaluation reports.
scripts/dap_adapter.py validates the scenario manifest and result contract.
Live execution remains opt-in; an unavailable adapter is reported separately
and is not presented as execution evidence.
