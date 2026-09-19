# Host adapter compatibility

The canonical skills follow the Agent Skills specification and are host-neutral. They use Markdown frontmatter, relative references and portable assets. A host adapter is responsible for discovery, installation, invocation, tool mapping and model configuration.

## Compatibility contract

Every compatible host must be able to:

1. Discover a skill by its SKILL.md frontmatter.
2. Load referenced files relative to the skill root.
3. Invoke the skill without changing its instructions.
4. Provide an isolated workspace and a way to persist requested artifacts.
5. Report unavailable tools or capabilities instead of silently simulating them.

## Adapter boundary

Host names, installation paths, command syntax, model identifiers and tool APIs belong in adapter configuration. They must not appear in canonical skills/*/SKILL.md files. The repository keeps adapter helpers in scripts/, optional host metadata in agents/, and adapter-specific scenarios outside the canonical skill contract.

Use python scripts/setup_unified.py when a supported adapter is configured. Review the generated destination before replacing an existing installation. The setup script is an adapter convenience; copying a skill directory manually is also valid.

## Packaging requirements

- Preserve the complete skill directory, including references/ and assets/.
- Resolve all internal links from the installed skill root.
- Keep host-specific metadata optional.
- Do not require repository-relative paths such as ../../docs from inside an installed skill.
- Validate an isolated copy before publishing an adapter package.

The canonical skill is the portable unit. Adapters may add launchers, aliases, metadata or test fixtures without changing the skill's behavior.