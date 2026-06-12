# Architecture Skills

A collection of Codex skills for software architecture documentation, review, and validation.

## Skills

| Skill | Purpose | Use When |
|-------|---------|----------|
| **arch-doc** | Generate architecture documentation with diagrams | Creating docs from scratch, documenting existing systems, generating C4/arc42/TOGAF diagrams |
| **arch-review** | Review and validate architecture implementations | Evaluating existing architectures, identifying anti-patterns, assessing technical debt |
| **arch-fitness** | Create automated architecture fitness functions | Setting up architecture validation in CI/CD, writing architecture unit tests |
| **arch-decision** | Structured decision analysis (DAR methodology) | Making technology selections, build vs buy decisions, weighted scoring analysis |

## Quick Start

### Installation

Skills are installed to `~/.codex/skills/` via copies.

**Linux/Mac:**
```bash
chmod +x sync-skills.sh run-tests.sh
./sync-skills.sh
```

**Windows:**
```powershell
.\sync-skills.ps1
```

### Usage

**Generate architecture documentation:**
```
Use arch-doc to create C4 diagrams for an e-commerce platform
```

**Review an architecture:**
```
Use arch-review to evaluate this microservices architecture
```

**Create fitness functions:**
```
Use arch-fitness to create ArchUnit tests for layer dependencies
```

**Make an architecture decision:**
```
Use arch-decision to help me choose between PostgreSQL and MongoDB
```

## Project Structure

```
arch-skills/
├── README.md                      # This file
├── AGENTS.md                      # Agent instructions
├── TODO.md                        # Task tracking
├── sync-skills.ps1                # Sync script (Windows)
├── sync-skills.sh                 # Sync script (Linux/Mac)
├── run-tests.ps1                  # Test runner (Windows)
├── run-tests.sh                   # Test runner (Linux/Mac)
├── docs/                          # Project documentation
│   ├── coverage-analysis.md       # Test coverage matrix
│   └── skill-testing.md           # Skill testing guide
├── skills/
│   ├── arch-doc/                  # Architecture documentation skill
│   │   ├── SKILL.md               # Main skill instructions
│   │   ├── agents/                # UI metadata
│   │   ├── references/            # Framework guides
│   │   │   ├── c4-model.md        # C4 Model with review checklist
│   │   │   ├── arc42-template.md  # arc42 template (12 sections)
│   │   │   ├── togaf-adm.md       # TOGAF Architecture Development Method
│   │   │   ├── iso42010.md        # ISO 42010 views and viewpoints
│   │   │   ├── adr-template.md    # MADR ADR templates
│   │   │   └── skill-testing.md   # Skill testing tools guide
│   │   └── assets/                # Diagram templates
│   │       ├── mermaid-templates/
│   │       ├── plantuml-templates/
│   │       └── drawio-templates/
│   ├── arch-review/               # Architecture review skill
│   │   ├── SKILL.md
│   │   ├── agents/
│   │   ├── references/
│   │   │   ├── design-patterns.md
│   │   │   ├── quality-attributes.md
│   │   │   ├── best-practices.md
│   │   │   └── tech-debt.md
│   │   └── assets/
│   │       └── review-template.md
│   ├── arch-fitness/              # Fitness functions skill
│   │   ├── SKILL.md
│   │   ├── agents/
│   │   ├── references/
│   │   │   └── fitness-functions.md
│   │   └── assets/
│   │       └── template.md
│   └── arch-decision/             # Decision analysis skill (DAR methodology)
│       ├── SKILL.md
│       ├── agents/
│       ├── references/
│       │   └── criteria-library.md
│       ├── scripts/
│       │   └── validate_math.py
│       └── assets/
│           └── dar-document.md
└── tests/
    ├── test_skills.py             # Structural validation (28 tests)
    ├── test-arch-doc.yaml         # skillprobe scenarios (12)
    ├── test-arch-review.yaml      # skillprobe scenarios (9)
    ├── test-arch-fitness.yaml     # skillprobe scenarios (9)
    ├── test-arch-decision.yaml    # skillprobe scenarios (9)
    └── test-dar.md                # Test DAR document
```

## Features

### arch-doc

- **C4 Model**: System Context, Container, Component, Code diagrams
- **arc42**: 12-section documentation template
- **TOGAF**: Architecture Development Method phases
- **ISO 42010**: Views and viewpoints standard
- **ADRs**: MADR templates for architecture decisions
- **Diagram Formats**: Mermaid (primary), PlantUML, Draw.io

### arch-review

- **Design Patterns**: Common patterns and anti-patterns catalog
- **Quality Attributes**: ISO 25010 model with scenarios
- **Best Practices**: SOLID, DRY, KISS checklists
- **Technical Debt**: Assessment framework and scoring
- **Review Template**: Executive summary, findings, recommendations

### arch-fitness

- **ArchUnit/ArchUnitTS**: Architecture unit testing examples
- **CI/CD Integration**: GitHub Actions workflow templates
- **Dependency Rules**: Layer boundary enforcement
- **Performance Bounds**: Response time validation
- **Quality Gates**: Automated architecture checks

### arch-decision

- **DAR Methodology**: 8-stage structured decision process
- **Weighted Scoring**: Criteria with weights summing to 100
- **Gate Criteria**: Pass/fail knockout filters
- **Sensitivity Analysis**: Tests ranking stability
- **Criteria Library**: Reusable evaluation bundles

## Testing

### Structural Validation

**Linux/Mac:**
```bash
./run-tests.sh
```

**Windows:**
```powershell
.\run-tests.ps1
```

Runs 28 structural tests + DAR math validation:
- Skill directory structure
- SKILL.md existence and frontmatter
- Reference files completeness
- Asset files presence
- Content quality (word count, sections)
- DAR weighted score calculations

To run only DAR validation:
```bash
./run-tests.sh --dar-only
# or
.\run-tests.ps1 -DarOnly
```

### Skill Test Scenarios

39 test scenarios covering all skill capabilities:

| Skill | Scenarios | Coverage |
|-------|-----------|----------|
| arch-doc | 12 | 100% |
| arch-review | 9 | 100% |
| arch-fitness | 9 | 100% |
| arch-decision | 9 | 100% |
| **Total** | **39** | **100%** |

Run with skillprobe (requires Claude Code CLI):
```bash
skillprobe run tests/test-arch-doc.yaml --harness claude-code
skillprobe run tests/test-arch-review.yaml --harness claude-code
skillprobe run tests/test-arch-fitness.yaml --harness claude-code
skillprobe run tests/test-arch-decision.yaml --harness claude-code
```

### DAR Math Validation

Validate weighted scores in DAR documents:

```bash
# Included in run-tests.sh/run-tests.ps1
# Or run directly:
python skills/arch-decision/scripts/validate_math.py tests/test-dar.md
```

### Skill Testing Tools

For end-to-end testing with real LLM execution:

- **skillprobe**: `pip install skillprobe`
- **skill-eval-runner**: `npm install -g skill-eval-runner`

See `skills/arch-doc/references/skill-testing.md` for details.

## Research Sources

- [C4 Model](https://c4model.com/) - Official C4 documentation
- [arc42](https://arc42.org/) - Architecture documentation template
- [MADR](https://github.com/joelparkerhenderson/architecture-decision-record) - ADR templates
- [ArchUnit](https://www.archunit.org/) - Java architecture testing
- [ISO 25010](https://www.iso.org/standard/35733.html) - Quality model
- [DAR Skill](https://github.com/DAR_Platform/DAR_Skill) - Decision Analysis and Resolution methodology

## License

MIT
