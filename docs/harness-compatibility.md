# Portable package compatibility

Use built packages, not isolated copies of source skill directories.
The format follows the [Agent Skills specification](https://agentskills.io/specification).
Discovery and invocation are host responsibilities; a skill does not supply a
scheduler, a subagent API, credentials or durable storage by itself.

## Distribution profiles

- Default: arch-orchestrator, arch-evaluate and arch-review are the only SKILL.md
  entry points. Other capabilities are instructions.md resources under
  references/specialists, located through package-catalog.json.
- Expert: all 33 entry points, or selected specialists using --skill. Narrow
  expert requests do not require the entire DAP workflow.
- Both: framework contracts, Python runtime/dependencies and content hashes are
  copied from one canonical source. There are no manually maintained host mirrors.

The default interface presents interview/create/update/evaluate workflows. It
does not add four engines or hide evaluation inside an authoring-only path.
No nonstandard hidden metadata is required. Hosts that discover SKILL.md entries
see three in the default output, including recursive discovery.

## Build contract

Run scripts/build_packages.py with a fresh --output and default/expert --profile.
The builder refuses an existing destination rather than deleting user data.
Install each complete generated directory with the selected host's native mechanism.
The builder does not perform installation or modify global skill locations.

Resolve references/assets relative to the current skill/module resource root;
resolve shared framework/scripts from the outer package root. Read the catalogue
before choosing module paths. A specialist is ordinary instruction content and
does not require a subagent; delegate only if supported and authorized.

Use Python 3.10+ and requirements.txt for deterministic helpers. Test scripts from
an unrelated working directory. A host without execution support can return a
plan or provisional analysis, but cannot claim the deterministic checks ran.

## Verified boundaries

Automated tests verify default/expert discovery counts, resource resolution,
bundle hashes, no-overwrite behavior and isolated evaluator execution. These are
filesystem/runtime compatibility tests, not proof that every AI host follows the
instructions correctly. Host-specific behavioral trials remain external,
optional and explicitly labelled with real execution evidence.
