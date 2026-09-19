# Skill Testing Reference

Use this reference when validating an architecture-documentation skill across
different AI tools. Keep the skill contract separate from the host adapter: the
scenario describes the requested behavior and observable evidence, while the
adapter supplies discovery, model selection, credentials, tool mapping and
invocation details.

## Testing levels

### 1. Structural validation

Run deterministic checks before spending model or integration resources. Verify:

- `SKILL.md` frontmatter and naming;
- references and assets resolve from the installed skill root;
- diagrams use the repository's declared format priority;
- generated templates are complete and non-empty;
- no provider-specific metadata or installation path is required.

### 2. Activation validation

Check that the description contains discriminating architecture-documentation
triggers such as C4, arc42, ADRs, architecture views, diagrams and decision
records. Test both positive requests and nearby requests that should route to a
more specialized skill.

### 3. Behavioral validation

Run scenarios through one or more compatible external adapters in isolated,
disposable workspaces. Prefer assertions about durable artifacts and structure
over exact wording:

- expected files or directories exist;
- generated documents contain required sections and stable identifiers;
- diagrams contain the requested elements and relationships;
- ADRs contain context, decision and consequences;
- unresolved assumptions and missing evidence remain visible;
- no placeholder or unfinished output is published as complete.

Record the adapter, model, prompt, skill version, fixture revision, timestamps,
assertions and evidence locations in the external test report. Do not place
those values in `SKILL.md` or portable scenario manifests.

### 4. Integration validation

Exercise documentation with decision, review and governance skills when the
request spans those concerns. Assert that:

- the selected specialist skills have explicit reasons;
- constraints and authority boundaries are preserved;
- requirements, views, ADRs and verification records remain traceable;
- design-quality review is not presented as execution evidence;
- draft, reviewed and accepted states remain distinct.

## Portable scenario shape

Use a host-neutral scenario format. The external adapter may extend it, but the
portable portion should remain understandable without a named host or model:

```yaml
skill: ./skills/arch-doc
scenarios:
  - id: creates-c4-context
    prompt: "Create a C4 system-context view for an e-commerce platform."
    assertions:
      - type: file_exists
        path: architecture/context.md
      - type: file_contains
        path: architecture/context.md
        value: "System Context"
      - type: evidence_present
        field: assumptions
```

Use stable scenario identifiers, versioned fixtures and explicit evidence paths.
If the adapter or model is unavailable, report the scenario as unavailable;
never convert an unexecuted scenario into a pass or failure.

## Reliability and safety

- Use an isolated workspace for every run and remove secrets from fixtures.
- Prefer file, directory, JSON and exit-status assertions over prose matching.
- Repeat only scenarios whose behavior is expected to vary, and publish the
  observed pass rate with the report.
- Treat tool-call assertions as adapter-specific evidence, not as portable
  skill requirements.
- Keep live-model tests opt-in; structural checks remain the release gate.
- Review generated diagrams and documents for semantic correctness, not only
  string presence.

## Release checklist

Before publishing a documentation skill, confirm that:

1. the installed skill works without repository-relative documentation paths;
2. every scenario has a reproducible fixture and observable evidence;
3. outputs preserve requested format, terminology and authority boundaries;
4. unsupported tools are reported rather than silently simulated;
5. adapter and model details are stored only in external test configuration.
