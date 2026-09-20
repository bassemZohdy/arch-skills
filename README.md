# Architecture Skills

Portable architecture skills with a small default interface and optional specialist access.
Canonical instructions, references and templates remain host-neutral.

## Four workflows, three public entry points

| Workflow | Entry point | Boundary |
| --- | --- | --- |
| Interview | arch-orchestrator, interview mode | Stop at the requirement/constraint handoff |
| Create | arch-orchestrator, create mode | Develop a new candidate without inventing approval |
| Update | arch-orchestrator, update mode | Preserve history, assess dependency impacts, re-enter affected stages |
| Evaluate | arch-evaluate for process; arch-review for design | Read-only assessment; keep results separate |

The default distribution exposes only those three skills. It bundles the remaining
capabilities as selectively loaded resources, not additional discoverable SKILL.md
entry points. The expert profile exposes all 33 canonical skills, or just selected
specialists. There is one orchestration engine and one canonical source per skill.

## Build and install

Use Python 3.10+ and the declared dependencies:

~~~sh
python -m pip install -r requirements.txt
python scripts/build_packages.py --profile default --output .cache/packages-default
python scripts/build_packages.py --profile expert --skill arch-api --output .cache/packages-api
~~~

Choose a fresh output directory: the builder never deletes or overwrites an existing
destination. Install complete directories from the built output using the host's
native mechanism. Do not install source skill directories directly: shared runtime
and contracts are bundled during the build.

No host detection, provider metadata, model choice or global installation happens.
A default package contains a lightweight specialist catalogue and resource modules;
load only the relevant ones. No universal host-specific hidden flag is required.
See [packaging and compatibility](docs/harness-compatibility.md).

Example requests:

- Interview me for a customer order platform. The orchestrator supplies the
  preparation step, one-question turns or small related question batches,
  prioritized choices and host-native question controls when the host exposes
  them, while reconciling each batch together.
- Interview stakeholders and stop after confirming requirements.
- Create a solution architecture from this brief.
- Update the architecture for this changed residency requirement.
- Evaluate process readiness and design quality, without changing source artifacts.
- Expert installation: use arch-api for a focused contract review.

## DAP contracts and validation

The [Deterministic Architecture Process](docs/deterministic-architecture-process.md)
defines the stages, authority rules and evidence requirements. The runtime supports
framework 1.0.0, corrected record schema 2.0.0 and rubric 1.0.0. Prior schema-1
examples are historical fixtures, not ready baselines or transferable approvals.
See [records](framework/records.md) and [current implementation status](docs/dap-implementation-status.md).

~~~sh
python tests/test_skills.py
python -m unittest discover -s tests -p "test_*.py" -v
python tests/test_activation.py
~~~

Run the same offline checks together with `./run-tests.ps1` on Windows or
`bash run-tests.sh` on Linux/macOS. Both stop on the first failure and work from
any current directory. GitHub Actions runs these checks and builds both package
profiles on Windows and Linux with Python 3.10 and 3.13 for pushes and pull
requests to `main`.

For a clearly synthetic positive example in a fresh directory:

~~~sh
python tests/dap_fixture.py --output .cache/dap-example
python scripts/dap_validate.py .cache/dap-example
~~~

Generate all seven current workflow fixtures with
`python tests/dap_fixture.py --suite --output .cache/dap-scenarios` in a fresh
directory. They are synthetic inputs for deterministic or optional behavioral
tests, not live-model execution evidence. See the
[adapter contract](docs/dap-adapter-contract.md) and
[real-project migration guide](framework/schema-2-migration.md).

Validator exit codes: 0 ready, 1 blocked/unassessable, 2 CLI error. Semantic
assessments and human identities are supplied evidence, not automatically proven
facts. Live-model scenarios remain optional and are not implied by passing tests.

## Repository layout

| Path | Purpose |
| --- | --- |
| skills/ | 33 canonical skill definitions and domain assets |
| framework/ | Versioned schemas, rubric, shared contribution and record contracts |
| scripts/ | Portable packaging, evaluation, graph, checkpoint and publication helpers |
| tests/ | Offline structure, contract, lifecycle and isolated-package tests |
| docs/ | Process specification, audits, boundaries and usage guidance |
| examples/ | Clearly labelled historical schema-1 regression inputs |

The [audit](docs/audits/2026-09-20-dap-skill-audit.md) records the earlier defects;
the [remediation review](docs/audits/2026-09-20-remediation-review.md) records the
changes and validation. [TODO](TODO.md) distinguishes remaining adoption work.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE).

## Community

See [CONTRIBUTING](CONTRIBUTING.md) for local checks and package guidance,
[SUPPORT](SUPPORT.md) for questions, [SECURITY](SECURITY.md) for private
vulnerability reports and [CODE_OF_CONDUCT](CODE_OF_CONDUCT.md) for community
expectations.
