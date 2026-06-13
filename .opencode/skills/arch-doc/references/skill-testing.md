# Skill Testing Reference

Structured approaches for testing AI agent skills.

## Testing Tools

### 1. skillprobe (Recommended)

**Source:** [github.com/Anyesh/skillprobe](https://github.com/Anyesh/skillprobe)

End-to-end testing for LLM skills. Launches Claude Code/Cursor as subprocesses, runs scenarios in isolated workspaces, and asserts outcomes.

**Installation:**
```bash
pip install skillprobe
# or
uv tool install skillprobe
```

**YAML Test Format:**
```yaml
harness: claude-code
model: claude-haiku-4-5-20251001
timeout: 120
skill: ./skills/my-skill

scenarios:
  - name: "skill activates on request"
    workspace: fixtures/dirty-repo
    setup:
      - run: "echo 'change' >> file.txt && git add ."
    steps:
      - prompt: "commit my changes"
        assert:
          - type: contains
            value: "commit"
          - type: tool_called
            value: "Bash"
    after:
      - type: file_exists
        value: ".git/COMMIT_EDITMSG"
```

**Assertion Types:**
- `contains` / `not_contains` - Response text
- `regex` - Pattern matching
- `tool_called` - Tool usage
- `skill_activated` - Skill loading
- `file_exists` / `file_contains` - Workspace state

**Multi-run for Reliability:**
```yaml
steps:
  - prompt: "Write a function with type hints"
    runs: 5
    min_pass_rate: 0.8
    assert:
      - type: regex
        value: "\-> "
```

**Commands:**
```bash
skillprobe run tests/my-skill.yaml      # Run tests
skillprobe measure tests/my-skill.yaml  # Measure variance
skillprobe activation tests/my-skill.yaml  # Test activation
```

### 2. skill-eval-runner (ser)

**Source:** [github.com/balyakin/skill-eval-runner](https://github.com/balyakin/skill-eval-runner)

CLI test runner with sandboxed workspaces and deterministic assertions.

**Installation:**
```bash
npm install -g skill-eval-runner
ser doctor
```

**YAML Test Format:**
```yaml
schema_version: '1.0'
name: migration-skill
skill: ./SKILL.md
adapter: claude

tests:
  - name: creates-user-migration
    prompt: 'Create a user table migration in {{WORKSPACE}}.'
    assertions:
      - type: exit_code
        expected: 0
      - type: stderr_empty
      - type: file_exists
        path: db/migrations/001_create_users.sql
      - type: file_contains
        path: db/migrations/001_create_users.sql
        contains: CREATE TABLE users
```

**Assertion Groups:**

| Group | Assertions |
|-------|------------|
| Files | `file_exists`, `file_not_exists`, `file_contains`, `file_matches_regex`, `dir_structure` |
| Process | `exit_code`, `stdout_contains`, `stderr_empty`, `command_ran`, `duration_under` |
| JSON | `json_schema`, `json_path_equals` |
| Response | `response_contains`, `response_not_contains`, `token_usage_under`, `semantic` |

**Commands:**
```bash
ser run . --adapter claude --report console,junit
ser validate .
ser list .
ser report .skilleval-reports/run.json --format html
```

### 3. skill-test-skill (Meta-testing)

**Source:** [github.com/youngfreeFJS/skill-test-skill](https://github.com/youngfreeFJS/skill-test-skill)

An Agent Skill that tests and scores other skills against the Agent Skills specification.

**Scoring Dimensions (100 points):**

| # | Dimension | Max Points |
|---|-----------|------------|
| 1 | Directory Structure | 10 |
| 2 | Frontmatter Compliance | 30 |
| 3 | Body Content Quality | 25 |
| 4 | Progressive Disclosure Design | 15 |
| 5 | Optional Directory Quality | 10 |
| 6 | Description Trigger Optimization | 10 |

**Grade Scale:**

| Score | Grade |
|-------|-------|
| 90-100 | Excellent - production-ready |
| 75-89 | Good - minor improvements |
| 60-74 | Acceptable - needs improvement |
| 40-59 | Poor - significant rework |
| 0-39 | Critical - major rewrite |

## Testing Strategy

### Level 1: Structural Validation

Use `quick_validate.py` (built-in):
```bash
python scripts/quick_validate.py path/to/skill
```

Checks:
- SKILL.md exists
- YAML frontmatter valid
- Naming conventions

### Level 2: Spec Compliance

Use `skill-test-skill` to score against specification:
- Frontmatter completeness
- Body quality
- Progressive disclosure
- Trigger optimization

### Level 3: Behavioral Testing

Use `skillprobe` or `skill-eval-runner`:
- Test skill activation
- Test skill execution
- Test output quality
- Measure reliability

### Level 4: Integration Testing

Test in real workflows:
- CI/CD integration
- Model update resilience
- Combination testing (multiple skills)

## Test Scenario Template

```yaml
# test-arch-doc.yaml
harness: claude-code
model: claude-haiku-4-5-20251001
timeout: 180
skill: ./skills/arch-doc

scenarios:
  - name: "generates C4 context diagram"
    steps:
      - prompt: "Create architecture documentation for an e-commerce system using C4 model"
        assert:
          - type: contains
            value: "C4Context"
          - type: contains
            value: "System Context"
          - type: tool_called
            value: "Write"

  - name: "selects appropriate framework"
    steps:
      - prompt: "Document a microservices platform with compliance requirements"
        assert:
          - type: contains
            value: "TOGAF"
          - type: contains
            value: "arc42"

  - name: "generates ADR for decisions"
    steps:
      - prompt: "Document architecture decisions for this system"
        assert:
          - type: contains
            value: "ADR"
          - type: contains
            value: "Context"
          - type: contains
            value: "Decision"
          - type: contains
            value: "Consequences"
```

## CI Integration

### GitHub Actions with skillprobe

```yaml
name: Skill Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm install -g @anthropic-ai/claude-code
      - uses: astral-sh/setup-uv@v4
      - run: uv tool install skillprobe
      - run: skillprobe run tests/*.yaml --harness claude-code
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
```

### GitHub Actions with ser

```yaml
name: Skill Evals

on: [push, pull_request]

jobs:
  eval:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 20
      - run: npm install -g skill-eval-runner
      - run: ser run . --adapter claude --report console,junit
        env:
          SER_ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
```

## Best Practices

1. **Start with dry-run** - Validate structure before spending tokens
2. **Test deterministically** - Prefer file/command assertions over response text
3. **Measure variance** - Use `skillprobe measure` before setting thresholds
4. **Test combinations** - Skills can interact unexpectedly
5. **CI integration** - Catch regressions on model updates
6. **Version pinning** - Pin tool versions in CI for reproducibility
