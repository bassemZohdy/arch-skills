# DAP adapter contract

The repository provides optional live behavioral scenarios without coupling the
canonical skills to a particular assistant, model provider, command-line
client, or tool API.

Use [test automation](test-automation.md) for the response-runner and host-adapter
protocol; this document is limited to the DAP lifecycle scenario contract.

## Contract

The versioned contract is framework/dap-adapter-contract.json. The scenario
manifest is tests/dap-adapter-scenarios.json.

Scenario manifest schema 2.0 uses `generated:<name>` fixture identifiers; the
external adapter result protocol remains 1.0.0. Historical schema-1 examples are
not current behavioral inputs. Generate the current fixture suite in a fresh
directory:

~~~sh
python tests/dap_fixture.py --suite --output .cache/dap-scenarios
python scripts/build_packages.py --profile default --output .cache/scenario-packages
~~~

For `generated:brownfield`, select `.cache/dap-scenarios/brownfield` as the
workspace (it contains `architecture/`). Resolve `./skills/arch-orchestrator` as
the stable source identifier to the built `arch-orchestrator` package. The source
path is not an installation instruction. Create a separate copy per execution.

The seven scenarios cover create, brownfield gaps, interruption, blocked review,
evaluation/publication, interview-only stopping and update impact analysis.
Fixture identities and dispositions are synthetic test inputs, never real approval.
The update fixture includes an unaccepted change request outside the frozen old
baseline; an unchanged old baseline being ready does not approve the requested change.

An adapter receives a scenario, an isolated workspace and a prompt. It invokes
the selected host and model using its own configuration, then returns a JSON
result containing:

- adapter ID and version;
- model ID and version;
- scenario and run IDs;
- start and finish timestamps;
- assertion results;
- observable evidence locations;
- passed, failed or unavailable status.

Unavailable means the adapter, model or credentials were not available. It is
reported separately from a skill failure. A passed or failed execution must
include observable evidence; a score or response text alone is insufficient.

Executed results require nonempty assertion outcomes with supported `type` and
boolean `passed`; `passed` status requires every outcome true, while `failed`
requires at least one false. Evidence objects contain a workspace-relative `path`.
Unavailable runs cannot claim executed assertions. Use ordered timezone-aware ISO
timestamps. For scenario `json_path_equals` assertions, `pointer` is a JSON Pointer
(the empty string selects the root), and `expected` is the comparison value.

The contract validator checks structure and consistency, not file existence,
completeness against a scenario, host execution or semantic truth. The adapter must
execute every requested assertion, preserve its identity/target in the outcome,
retain actual evidence and report omissions as failures. Envelope validation alone
must never be reported as a successful live behavioral test.

## Validation

Validate the scenario contract:

    python scripts/dap_adapter.py validate-scenarios tests/dap-adapter-scenarios.json

Validate an adapter result:

    python scripts/dap_adapter.py validate-result tests/dap-adapter-result.example.json --scenario-id DAP-BEH-001

The example result is intentionally unavailable; it demonstrates the required
shape and must not be reported as executed evidence.

For an executed result, also validate completeness against the requested scenario
and its workspace:

    python scripts/dap_adapter.py validate-execution result.json tests/dap-adapter-scenarios.json --workspace .cache/dap-run

This requires assertion IDs in the form `<scenario-id>:<one-based-index>` and
checks that every returned evidence path is an existing workspace-relative file.

## Host boundary

Host-specific adapters may add harness commands, model configuration,
credentials, durable state integration and human-review integration outside
this repository contract. They must emit the versioned result shape and keep
those details out of SKILL.md, the scenario manifest and the DAP scoring rules.
Until a target host supplies those capabilities, the repository's deterministic
checks remain the required release gate and the live scenarios remain opt-in.
