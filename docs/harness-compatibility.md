# Portable package compatibility

Use built packages, not isolated copies of source skill directories.
The format follows the [Agent Skills specification](https://agentskills.io/specification).
Discovery and invocation are host responsibilities; a skill does not supply a
scheduler, a subagent API, credentials or durable storage by itself.

## Distribution profiles

- Default: arch-orchestrator, arch-evaluate and arch-review are the only SKILL.md
  entry points. Other capabilities are instructions.md resources under
  references/specialists, located through package-catalog.json.
- The default public entry points may load `arch-diagrams` through that catalogue
  for diagram-first creation or review; hosts still discover only the three public
  entry points.
- Expert: all 34 entry points, or selected specialists using --skill. Narrow
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
resolve shared framework and scripts/dap*.py from the outer package root.
Resolve a specialist-local script, such as arch-decision's math validator, from
that module's resource root. Related skill names are optional handoffs; a
selected expert package does not imply that every related specialist is installed. Read the catalogue
before choosing module paths. A specialist is ordinary instruction content and
does not require a subagent; delegate only if supported and authorized.

Use Python 3.10+ and requirements.txt for deterministic helpers. Test scripts from
an unrelated working directory. A host without execution support can return a
plan or provisional analysis, but cannot claim the deterministic checks ran.

## Conversational interview controls

The orchestrator's interview contract is host-neutral. It presents one active
question by default, but can prepare a bounded group of related independent
questions when that is more efficient. The adapter should separate presentation
turns from reasoning turns: prepare a batch once, collect its answers locally,
then submit the question IDs, values and provenance together for one
reconciliation when the host supports collection without model turns. Otherwise,
use the normal host turn mechanism and defer full reconciliation. A blocking,
ambiguous, scope-changing or high-risk answer may close the batch early and
trigger one partial reconciliation.

First check whether the host advertises a native user-input or elicitation
capability. A host adapter maps the ordered choices, stable option identifiers
and final free-text option to its own controls, then returns the selected values
and provenance. The skill must not print a duplicate numbered list when that
native capability is available.

Hosts without a native capability should render the same choices as numbered or
lettered text and accept the selected number, option text or a custom response.
They may render a prepared batch sequentially and collect the answers before
the next reconciliation. The checkpoint and question records remain the
portable state. Codex app-server
integrations may provide server-initiated user-input or MCP elicitation requests;
that integration belongs to the host adapter, not to the canonical skill.

## Verified boundaries

Automated tests verify default/expert discovery counts, resource resolution,
bundle hashes, no-overwrite behavior and isolated evaluator execution. These are
filesystem/runtime compatibility tests, not proof that every AI host follows the
instructions correctly. Host-specific behavioral trials remain external,
optional and explicitly labelled with real execution evidence.
