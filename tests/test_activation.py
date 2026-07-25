#!/usr/bin/env python3
"""
Activation Tests — verify skill descriptions trigger correctly.

Checks that each skill's description contains enough trigger keywords
to be matched by AI harnesses for relevant user requests.

Run: python tests/test_activation.py
"""

import os
import re
import yaml
from pathlib import Path

SKILLS_DIR = Path(__file__).parent.parent / "skills"


def load_skill_description(skill_name):
    """Extract description from a skill's SKILL.md frontmatter."""
    skmd = SKILLS_DIR / skill_name / "SKILL.md"
    if not skmd.exists():
        return None
    content = skmd.read_text(encoding="utf-8")
    parts = content.split("---")
    if len(parts) < 3:
        return None
    try:
        fm = yaml.safe_load(parts[1])
        return fm.get("description", "")
    except Exception:
        return None


def score_description(desc, skill_name):
    """Score a description on trigger quality. Returns (score, issues)."""
    issues = []
    score = 10

    # Must have at least 3 words
    if len(desc.split()) < 5:
        issues.append("Too short (< 5 words)")
        score -= 3

    # Should mention specific use-cases or trigger phrases
    trigger_indicators = [
        "use when", "use for", "trigger when", "trigger on",
        r"\bdesign\b", r"\breview\b", r"\bplan\b", r"\bcreate\b",
        r"\bimplement\b", r"\bmigrat", r"\boptimiz", r"\bdocument\b",
        r"\btest\b", r"\bmonitor\b", r"\banalyz", r"\bassess\b",
        r"\bevaluat", r"\bmodel\b", r"\barchitect", r"\bestablish\b",
        r"\bapply\b", r"\bdefine\b", r"\bselect\b", r"\bdirect\b",
        r"\bdrive\b", r"\bengineer\b", r"\bgovern\b",
    ]
    trigger_count = sum(
        1 for p in trigger_indicators if re.search(p, desc.lower())
    )
    if trigger_count < 3:
        issues.append(f"Only {trigger_count} trigger indicators (need ≥3)")
        score -= 2

    # Should mention specific technologies/domains
    domain_keywords = [
        "REST", "GraphQL", "gRPC", "API", "microservice", "monolith",
        "cloud", "AWS", "Azure", "GCP", "Kubernetes", "Docker",
        "C4", "arc42", "TOGAF", "ADR", "Mermaid", "PlantUML",
        "STRIDE", "OWASP", "GDPR", "HIPAA", "SOC 2", "PCI",
        "DDD", "CQRS", "event sourc", "saga", "RAG", "LLM",
        "WCAG", "ARIA", "FinOps", "Terraform", "CI/CD",
        "SOLID", "GRASP", "DRY", "CAP", "circuit breaker",
        "OpenTelemetry", "SLO", "Redis", "PostgreSQL",
        "React", "Angular", "Vue", "Svelte",
        "governance", "compliance", "standard",
        "anti-pattern", "code smell", "refactor",
    ]
    domain_count = sum(
        1 for kw in domain_keywords if kw.lower() in desc.lower()
    )
    if domain_count < 2:
        issues.append(f"Only {domain_count} domain keywords (need ≥2)")
        score -= 2

    # Should not be purely generic
    generic_only_patterns = [
        r"^Design \w+ architecture\.?\s*$",
        r"^Systematic approach to \w+\.?\s*$",
    ]
    if any(re.match(p, desc) for p in generic_only_patterns):
        issues.append("Description is purely generic — needs trigger keywords")
        score -= 3

    return max(0, score), issues


def main():
    skills = sorted(
        d.name
        for d in SKILLS_DIR.iterdir()
        if d.is_dir() and d.name.startswith("arch-") and (d / "SKILL.md").exists()
    )

    print("=" * 60)
    print("Description Activation Quality Tests")
    print("=" * 60)

    results = []
    for skill in skills:
        desc = load_skill_description(skill)
        if desc is None:
            print(f"\n  ✗ {skill}: No description found")
            results.append((skill, 0, ["No description"]))
            continue

        score, issues = score_description(desc, skill)
        results.append((skill, score, issues))

        if issues:
            print(f"\n  ⚠ {skill} (score: {score}/10)")
            for issue in issues:
                print(f"    — {issue}")
            print(f"    Description: {desc[:120]}...")
        else:
            print(f"\n  ✓ {skill} (score: {score}/10)")

    # Summary
    total = len(results)
    passed = sum(1 for _, s, i in results if s >= 7)
    weak = [(name, s, i) for name, s, i in results if s < 7]

    print("\n" + "=" * 60)
    print(f"Total: {total} | Good (≥7): {passed} | Weak (<7): {len(weak)}")
    if weak:
        print("\nSkills needing description improvements:")
        for name, s, i in weak:
            print(f"  {name} (score: {s}/10): {'; '.join(i)}")
    print("=" * 60)

    return len(weak) == 0


if __name__ == "__main__":
    import sys

    success = main()
    sys.exit(0 if success else 1)
