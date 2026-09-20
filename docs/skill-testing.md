# Skill testing reference

Skill behavior is host-dependent, so keep the skill contract and the test adapter separate. A scenario should describe the requested behavior and observable evidence; the selected host, model, command syntax and tool names belong in the adapter configuration.

## Testing levels

### 1. Structural validation

Run the repository's deterministic checks:
~~~text
python tests/test_skills.py
~~~

Validate frontmatter, progressive disclosure, internal links, assets, metadata, naming and forbidden files without invoking a model.

The suite is offline, checks inline and Markdown resource paths across references,
and does not enforce a minimum word count or unnecessary resource directories.
Run contract and isolated-package tests with
`python -m unittest discover -s tests -p 'test_*.py' -v`.

Use `./run-tests.ps1` or `bash run-tests.sh` to run structural validation, the
complete contract/package suite and description lint together. These wrappers
stop on failure and resolve the repository from their own location. The
GitHub Actions workflow runs the wrappers and fresh default/expert builds on
Windows and Linux with Python 3.10 and 3.13.

### 2. Activation checks

Use tests/test_activation.py for a lexical description heuristic. Its scores and
advisory notes are not proof of correct host/model selection; do not pad a precise
description with irrelevant keywords to maximize the score. Keep this lint
independent of a particular host or model and measure real activation separately.

### 3. Behavioral adapter tests

The executable YAML runner and a response-only HTTP adapter are now provided.
See [test automation](test-automation.md) for exact commands and the JSON adapter
protocol. Scenario validation is part of every offline CI run and checks coverage
of all 33 skills. A custom host adapter can supply actual tool observations.

~~~sh
python scripts/behavioral.py validate
python scripts/behavioral.py run --manifest tests/test-arch-evaluate.yaml \
  --packages .cache/expert --output .cache/evaluate-results --limit 0 --max-calls 6
~~~

Prefer typed JSON assertions for discrete decisions. Response keywords remain
smoke checks, not proof of architectural quality. Record adapter/model versions
in reports, not skill instructions. File/traceability assertions belong to the
separate DAP adapter suite, which still needs an actual host adapter.

A generic scenario shape is:
~~~yaml
timeout: 180
skill: ./skills/arch-evaluate
scenarios:
  - name: missing-approval-remains-pending
    runs: 3
    min_passes: 3
    steps:
      - prompt: 'A mandatory review is unapproved. Return only JSON with boolean "ready".'
        assert:
          - type: json_equals
            pointer: /ready
            value: false
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
- Keep live-model tests opt-in; structural validation, contract/package tests and
  fresh package builds remain the required repository checks.

## Authoring rule

A canonical skill may describe inputs, outputs, decisions and evidence. It must not require a named assistant, model provider, CLI, tool API, installation directory or host-specific command. Put those details in adapter documentation, test configuration or packaging metadata.
