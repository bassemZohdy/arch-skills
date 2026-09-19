# Skill testing reference

Skill behavior is host-dependent, so keep the skill contract and the test adapter separate. A scenario should describe the requested behavior and observable evidence; the selected host, model, command syntax and tool names belong in the adapter configuration.

## Testing levels

### 1. Structural validation

Run the repository's deterministic checks:
~~~text
python tests/test_skills.py
~~~

Validate frontmatter, progressive disclosure, internal links, assets, metadata, naming and forbidden files without invoking a model.

### 2. Activation checks

Use tests/test_activation.py to evaluate whether each description contains precise triggers and domain terms. Keep activation tests independent of a particular host or model.

### 3. Behavioral adapter tests

Run a scenario through any compatible adapter. The scenario file should contain prompts, workspace setup and observable assertions; the adapter supplies the model, timeout, credentials and invocation protocol.

Generic invocation shape:
~~~text
<adapter-runner> run tests/test-arch-doc.yaml \
  --skill-root ./skills/arch-doc \
  --model <model-id> \
  --report <output>
~~~

Prefer file, directory, JSON and exit-status assertions over exact prose. Record the adapter and model version in the test report, not in the skill instructions.

A generic scenario shape is:
~~~yaml
skill: ./skills/example
scenarios:
  - name: creates-an-architecture-record
    steps:
      - prompt: "Document the architecture decision for this system."
        assert:
          - type: file_exists
            value: architecture/decisions/001-example.md
          - type: file_contains
            value: "## Decision"
~~~

### 4. Integration checks

Exercise orchestration with a selected set of specialist skills. Assert selection reasons, preserved constraints, conflict handling, traceability and final artifacts. Run the same scenario with more than one adapter when portability is a release requirement.

### 5. DAP adapter scenarios

The optional DAP behavioral scenarios are defined in
tests/dap-adapter-scenarios.json and validated without a live model:

    python scripts/dap_adapter.py validate-scenarios tests/dap-adapter-scenarios.json

An external adapter may execute those scenarios in an isolated workspace. It
must return the versioned result shape described in
docs/dap-adapter-contract.md, including adapter/model versions and observable
evidence. Missing credentials or an unavailable host is reported as
unavailable, not as a passing or failing skill result.

## Reliability and reproducibility

- Pin adapter and model versions in the external test configuration.
- Use isolated workspaces for every scenario.
- Prefer deterministic assertions over response wording.
- Repeat non-deterministic scenarios and publish pass rates.
- Treat a missing adapter, model or credential as an unavailable test environment, not as a skill failure.
- Keep live-model tests opt-in; structural validation remains the required gate.

## Authoring rule

A canonical skill may describe inputs, outputs, decisions and evidence. It must not require a named assistant, model provider, CLI, tool API, installation directory or host-specific command. Put those details in adapter documentation, test configuration or packaging metadata.
