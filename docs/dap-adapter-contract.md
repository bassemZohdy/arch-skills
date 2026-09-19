# DAP adapter contract

The repository provides optional live behavioral scenarios without coupling the
canonical skills to a particular assistant, model provider, command-line
client, or tool API.

## Contract

The versioned contract is framework/dap-adapter-contract.json. The scenario
manifest is tests/dap-adapter-scenarios.json.

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

## Validation

Validate the scenario contract:

    python scripts/dap_adapter.py validate-scenarios tests/dap-adapter-scenarios.json

Validate an adapter result:

    python scripts/dap_adapter.py validate-result tests/dap-adapter-result.example.json --scenario-id DAP-BEH-001

The example result is intentionally unavailable; it demonstrates the required
shape and must not be reported as executed evidence.

## Host boundary

Host-specific adapters may add harness commands, model configuration,
credentials, durable state integration and human-review integration outside
this repository contract. They must emit the versioned result shape and keep
those details out of SKILL.md, the scenario manifest and the DAP scoring rules.
Until a target host supplies those capabilities, the repository's deterministic
checks remain the required release gate and the live scenarios remain opt-in.
