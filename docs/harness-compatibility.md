# Skill Harness Compatibility

## Supported Harnesses

This skill set follows the [Agent Skills specification](https://agentskills.io/specification) and works with:

| Harness | Status | Notes |
|---------|--------|-------|
| **Claude Code** | ✅ Supported | Primary development target |
| **OpenAI Codex** | ✅ Supported | Primary development target |
| **Cursor** | ✅ Supported | Use `.cursor/rules` path |
| **GitHub Copilot** | ✅ Supported | Use `.github/copilot-instructions.md` |
| **Gemini CLI** | ✅ Supported | Use `.gemini/skills` path |
| **JetBrains Junie** | ✅ Supported | Use `.agents/skills` path |
| **OpenHands** | ✅ Supported | Use `.agents/skills` path |
| **OpenCode** | ✅ Supported | Multiple path support |

## Installation Paths

| Harness | Personal Path | Project Path |
|---------|---------------|--------------|
| Claude Code | `~/.claude/skills/` | `.claude/skills/` |
| OpenAI Codex | `~/.codex/skills/` | `.codex/skills/` |
| Cursor | `~/.cursor/rules/` | `.cursor/rules/` |
| GitHub Copilot | `~/.github/copilot-instructions.md` | `.github/copilot-instructions.md` |
| Gemini CLI | `~/.gemini/skills/` | `.gemini/skills/` |
| Junie | - | `.agents/skills/` |
| OpenHands | - | `.agents/skills/` |
| OpenCode | `~/.config/opencode/skills/` | `.opencode/skills/` or `.agents/skills/` |

## Cross-Harness Compatibility

Skills follow the Agent Skills specification and are harness-agnostic. The same `SKILL.md` works across all supported harnesses.

### Key Requirements

1. **SKILL.md Format** - YAML frontmatter with `name` and `description`
2. **Progressive Disclosure** - Keep SKILL.md under 500 lines
3. **File References** - Use relative paths from skill root
4. **No Harness-Specific Code** - Avoid tool-specific commands in SKILL.md

### Installation

Use the provided scripts to sync skills to all detected harnesses:

```bash
# Detect available harnesses
python scripts/detect_harness.py

# Sync to all detected harnesses
python scripts/sync_all.py

# Sync to specific harness
python scripts/sync_all.py --harness claude-code
```

Or use platform-specific scripts:

```powershell
# Windows
.\sync-skills.ps1

# Linux/Mac
./sync-skills.sh
```
