#!/usr/bin/env python
"""
Architecture Skills Test Suite
Validates skill structure, content, completeness, and spec compliance.
"""

import os
import re
import sys
import yaml
from pathlib import Path

# Add skill-creator scripts to path
SKILL_CREATOR_PATH = Path.home() / ".codex" / "skills" / ".system" / "skill-creator" / "scripts"
sys.path.insert(0, str(SKILL_CREATOR_PATH))


def discover_skills(skills_dir):
    """Auto-discover arch-* skill directories."""
    return sorted([
        d.name for d in skills_dir.iterdir()
        if d.is_dir() and d.name.startswith("arch-") and (d / "SKILL.md").exists()
    ])


class SkillTester:
    def __init__(self, skills_dir):
        self.skills_dir = Path(skills_dir)
        self.results = []

    # ── Existing tests ──────────────────────────────────────────────

    def test_skill_exists(self, skill_name):
        """Test that skill directory exists."""
        skill_path = self.skills_dir / skill_name
        exists = skill_path.exists() and skill_path.is_dir()
        self.results.append({
            "test": f"{skill_name} directory exists",
            "passed": exists,
            "path": str(skill_path)
        })
        return exists

    def test_skill_md_exists(self, skill_name):
        """Test that SKILL.md exists."""
        skill_path = self.skills_dir / skill_name / "SKILL.md"
        exists = skill_path.exists()
        self.results.append({
            "test": f"{skill_name}/SKILL.md exists",
            "passed": exists
        })
        return exists

    def test_frontmatter(self, skill_name):
        """Test that SKILL.md has valid frontmatter meeting Agent Skills spec."""
        skill_path = self.skills_dir / skill_name / "SKILL.md"
        if not skill_path.exists():
            self.results.append({
                "test": f"{skill_name} frontmatter",
                "passed": False,
                "error": "SKILL.md not found"
            })
            return False

        content = skill_path.read_text(encoding='utf-8')
        if not content.startswith("---"):
            self.results.append({
                "test": f"{skill_name} frontmatter",
                "passed": False,
                "error": "No frontmatter found"
            })
            return False

        try:
            parts = content.split("---")
            if len(parts) < 3:
                self.results.append({
                    "test": f"{skill_name} frontmatter",
                    "passed": False,
                    "error": "Invalid frontmatter format"
                })
                return False

            frontmatter = yaml.safe_load(parts[1])
            has_name = "name" in frontmatter
            has_description = "description" in frontmatter

            issues = []

            # Agent Skills spec: name ≤ 64 chars, lowercase a-z 0-9 hyphens
            name = frontmatter.get("name", "")
            if name:
                if len(name) > 64:
                    issues.append(f"name too long ({len(name)} > 64 chars)")
                if not re.match(r'^[a-z0-9][a-z0-9-]*[a-z0-9]$', name):
                    issues.append(f"name \"{name}\" doesn't match [a-z0-9][a-z0-9-]*[a-z0-9]")
                if "--" in name:
                    issues.append(f"name \"{name}\" contains consecutive hyphens")

            # Agent Skills spec: description ≤ 1024 chars
            desc = frontmatter.get("description", "")
            if desc:
                if len(desc) > 1024:
                    issues.append(f"description too long ({len(desc)} > 1024 chars)")

            # Trigger quality: should contain specific keywords, not just generic
            generic_patterns = [
                r'^Design \w+ architecture\.?\s*$',
                r'^Use when designing \w+\.?\s*$',
                r'^Systematic approach to \w+\.?\s*$',
            ]
            if any(re.match(p, desc) for p in generic_patterns):
                issues.append(f"description is too generic; add trigger keywords and use-cases")

            passed = has_name and has_description and len(issues) == 0

            self.results.append({
                "test": f"{skill_name} frontmatter",
                "passed": passed,
                "details": {
                    "has_name": has_name,
                    "has_description": has_description,
                    "name": name,
                    "description_length": len(desc),
                }
            })
            if issues:
                self.results[-1]["issues"] = issues
            return passed
        except Exception as e:
            self.results.append({
                "test": f"{skill_name} frontmatter",
                "passed": False,
                "error": str(e)
            })
            return False

    def test_references_dir(self, skill_name):
        """Test that references directory exists with .md files."""
        refs_path = self.skills_dir / skill_name / "references"
        if not refs_path.exists():
            self.results.append({
                "test": f"{skill_name} references directory",
                "passed": False,
                "error": "Directory not found"
            })
            return False

        all_files = list(refs_path.iterdir())
        md_files = [f for f in all_files if f.suffix == ".md"]
        non_md = [f.name for f in all_files if f.suffix != ".md" and f.name != ".gitkeep"]

        passed = len(md_files) > 0 and len(non_md) == 0
        self.results.append({
            "test": f"{skill_name} references directory",
            "passed": passed,
            "details": {
                "file_count": len(md_files),
                "files": [f.name for f in md_files],
            }
        })
        if non_md:
            self.results[-1]["details"]["non_md_files"] = non_md
            self.results[-1]["error"] = f"Non-.md files in references/: {non_md}"
        return passed

    def test_assets_dir(self, skill_name):
        """Test that assets directory exists with non-empty files."""
        assets_path = self.skills_dir / skill_name / "assets"
        if not assets_path.exists():
            self.results.append({
                "test": f"{skill_name} assets directory",
                "passed": False,
                "error": "Directory not found"
            })
            return False

        files = [f for f in assets_path.rglob("*") if f.is_file()]
        empty_files = [f.name for f in files if f.stat().st_size == 0]
        passed = len(files) > 0 and len(empty_files) == 0

        self.results.append({
            "test": f"{skill_name} assets directory",
            "passed": passed,
            "details": {
                "file_count": len(files),
            }
        })
        if empty_files:
            self.results[-1]["details"]["empty_files"] = empty_files
            self.results[-1]["error"] = f"Empty asset files: {empty_files}"
        return passed

    def test_openai_yaml(self, skill_name):
        """Test that agents/openai.yaml exists and has required fields."""
        yaml_path = self.skills_dir / skill_name / "agents" / "openai.yaml"
        if not yaml_path.exists():
            self.results.append({
                "test": f"{skill_name} agents/openai.yaml",
                "passed": False,
                "error": "File not found"
            })
            return False

        try:
            data = yaml.safe_load(yaml_path.read_text(encoding='utf-8'))
            if not data:
                self.results.append({
                    "test": f"{skill_name} agents/openai.yaml",
                    "passed": False,
                    "error": "Empty or null YAML"
                })
                return False

            interface = data.get("interface", {})
            has_display = bool(interface.get("display_name"))
            has_short = bool(interface.get("short_description"))
            passed = has_display and has_short

            self.results.append({
                "test": f"{skill_name} agents/openai.yaml",
                "passed": passed,
                "details": {
                    "has_display_name": has_display,
                    "has_short_description": has_short,
                }
            })
            return passed
        except Exception as e:
            self.results.append({
                "test": f"{skill_name} agents/openai.yaml",
                "passed": False,
                "error": f"Invalid YAML: {e}"
            })
            return False

    def test_skill_content_quality(self, skill_name):
        """Test that SKILL.md has substantial content and is under 500 lines."""
        skill_path = self.skills_dir / skill_name / "SKILL.md"
        if not skill_path.exists():
            self.results.append({
                "test": f"{skill_name} content quality",
                "passed": False,
                "error": "SKILL.md not found"
            })
            return False

        content = skill_path.read_text(encoding='utf-8')
        lines = content.split("\n")
        word_count = len(content.split())
        line_count = len(lines)

        has_workflow = any("workflow" in line.lower() for line in lines)
        has_steps = any("step" in line.lower() for line in lines)
        has_references = any("references" in line.lower() for line in lines)

        issues = []
        if word_count <= 500:
            issues.append(f"word count {word_count} ≤ 500 minimum")
        if not has_workflow:
            issues.append("missing 'Workflow' section")
        if line_count > 500:
            issues.append(f"line count {line_count} > 500 (AGENTS.md convention)")

        passed = word_count > 500 and has_workflow and line_count <= 500

        self.results.append({
            "test": f"{skill_name} content quality",
            "passed": passed,
            "details": {
                "word_count": word_count,
                "line_count": line_count,
                "has_workflow": has_workflow,
                "has_steps": has_steps,
                "has_references": has_references,
            }
        })
        if issues:
            self.results[-1]["issues"] = issues
        return passed

    # ── New tests ───────────────────────────────────────────────────

    def test_broken_internal_links(self, skill_name):
        """Test that all [text](references/X.md) and [text](assets/X) links resolve."""
        skill_path = self.skills_dir / skill_name / "SKILL.md"
        if not skill_path.exists():
            self.results.append({
                "test": f"{skill_name} broken internal links",
                "passed": False,
                "error": "SKILL.md not found"
            })
            return False

        content = skill_path.read_text(encoding='utf-8')
        broken = []

        # Check references/ links
        ref_links = re.findall(r'\[([^\]]*)\]\(references/([^)]+)\)', content)
        for link_text, ref_file in ref_links:
            ref_path = self.skills_dir / skill_name / "references" / ref_file
            if not ref_path.exists():
                broken.append(f"references/{ref_file} (from [{link_text}])")

        # Check assets/ links
        asset_links = re.findall(r'\[([^\]]*)\]\(assets/([^)]+)\)', content)
        for link_text, asset_file in asset_links:
            asset_path = self.skills_dir / skill_name / "assets" / asset_file
            if not asset_path.exists():
                broken.append(f"assets/{asset_file} (from [{link_text}])")

        passed = len(broken) == 0
        self.results.append({
            "test": f"{skill_name} broken internal links",
            "passed": passed,
            "details": {"links_checked": len(ref_links) + len(asset_links)}
        })
        if broken:
            self.results[-1]["error"] = "; ".join(broken)
        return passed

    def test_forbidden_files(self, skill_name):
        """Test that no README.md or CHANGELOG.md exists in skill dir."""
        skill_path = self.skills_dir / skill_name
        forbidden = ["README.md", "CHANGELOG.md"]
        found = [f for f in forbidden if (skill_path / f).exists()]

        passed = len(found) == 0
        self.results.append({
            "test": f"{skill_name} no forbidden files",
            "passed": passed,
        })
        if found:
            self.results[-1]["error"] = f"Forbidden files: {found}"
        return passed

    def test_duplicate_headings(self, skill_name):
        """Test that SKILL.md has no duplicate section headings (outside code blocks)."""
        skill_path = self.skills_dir / skill_name / "SKILL.md"
        if not skill_path.exists():
            self.results.append({
                "test": f"{skill_name} duplicate headings",
                "passed": False,
                "error": "SKILL.md not found"
            })
            return False

        content = skill_path.read_text(encoding='utf-8')
        # Strip fenced code blocks so template headings aren't counted
        content_no_code = re.sub(r'```[\s\S]*?```', '', content)
        headings = re.findall(r'^#{1,4}\s+(.+)$', content_no_code, re.MULTILINE)
        seen = {}
        dupes = []
        for h in headings:
            h_lower = h.lower().strip()
            if h_lower in seen:
                dupes.append(f"\"{h}\" (lines ~{seen[h_lower]}, duplicate)")
            else:
                seen[h_lower] = len(content[:content.find(h)].split('\n')) + 1

        passed = len(dupes) == 0
        self.results.append({
            "test": f"{skill_name} duplicate headings",
            "passed": passed,
            "details": {"heading_count": len(headings)}
        })
        if dupes:
            self.results[-1]["error"] = "; ".join(dupes)
        return passed

    def test_external_links(self, skill_name):
        """Check external URLs in SKILL.md return 200 (warning-only, skipped offline)."""
        skill_path = self.skills_dir / skill_name / "SKILL.md"
        if not skill_path.exists():
            return False

        content = skill_path.read_text(encoding='utf-8')
        urls = re.findall(r'\[([^\]]*)\]\((https?://[^)]+)\)', content)

        if not urls:
            return True  # Nothing to check

        # Try a quick connectivity check first
        import socket
        try:
            socket.create_connection(("8.8.8.8", 53), timeout=2)
        except OSError:
            self.results.append({
                "test": f"{skill_name} external links",
                "passed": True,
                "details": {"url_count": len(urls), "checked": False, "note": "Offline — skipped"}
            })
            return True

        import urllib.request
        import urllib.error
        broken = []
        for link_text, url in urls:
            try:
                req = urllib.request.Request(url, method='HEAD', headers={'User-Agent': 'Mozilla/5.0'})
                urllib.request.urlopen(req, timeout=5)
            except urllib.error.HTTPError as e:
                if e.code in (404, 410):
                    broken.append(f"{url} [{e.code}] (from [{link_text}])")
            except Exception:
                pass  # Connection issues, bot protection — skip

        # Always pass; broken links are reported as details
        passed = True
        self.results.append({
            "test": f"{skill_name} external links",
            "passed": passed,
            "details": {"url_count": len(urls), "broken": len(broken)}
        })
        if broken:
            self.results[-1]["error"] = "; ".join(broken[:5])
        return passed

    def test_diagram_priority(self, skill_name):
        """Test that Mermaid is preferred over PlantUML (AGENTS.md convention)."""
        skill_path = self.skills_dir / skill_name / "SKILL.md"
        if not skill_path.exists():
            return False

        content = skill_path.read_text(encoding='utf-8').lower()
        mermaid = len(re.findall(r'```mermaid', content))
        plantuml = len(re.findall(r'```plantuml', content))

        passed = plantuml <= mermaid
        self.results.append({
            "test": f"{skill_name} diagram priority (Mermaid >= PlantUML)",
            "passed": passed,
            "details": {"mermaid_blocks": mermaid, "plantuml_blocks": plantuml}
        })
        return passed

    def test_skill_catalog_consistency(self, skill_name):
        """Test that arch-orchestrator skill-catalog.md lists all existing specialist skills."""
        # Only run once (when called for arch-orchestrator)
        if skill_name != "arch-orchestrator":
            return True

        catalog_path = self.skills_dir / "arch-orchestrator" / "references" / "skill-catalog.md"
        if not catalog_path.exists():
            self.results.append({
                "test": "skill-catalog consistency",
                "passed": False,
                "error": "skill-catalog.md not found"
            })
            return False

        catalog_text = catalog_path.read_text(encoding='utf-8')
        all_skills = discover_skills(self.skills_dir)
        # The orchestrator itself is the user of the catalog, not a listed specialist
        specialist_skills = [s for s in all_skills if s != "arch-orchestrator"]

        missing = [s for s in specialist_skills if s not in catalog_text]

        passed = len(missing) == 0
        self.results.append({
            "test": "skill-catalog consistency",
            "passed": passed,
            "details": {"skills_on_disk": len(all_skills), "specialists_in_catalog": len(specialist_skills)}
        })
        if missing:
            self.results[-1]["error"] = f"Skills missing from catalog: {missing}"
        return passed

    # ── Runner ──────────────────────────────────────────────────────

    def run_all_tests(self):
        """Run all tests for all discovered skills."""
        skills = discover_skills(self.skills_dir)

        print("=" * 60)
        print("Architecture Skills Test Suite")
        print(f"Skills discovered: {len(skills)}")
        print("=" * 60)

        for skill in skills:
            print(f"\nTesting: {skill}")
            print("-" * 40)

            self.test_skill_exists(skill)
            self.test_skill_md_exists(skill)
            self.test_frontmatter(skill)
            self.test_references_dir(skill)
            self.test_assets_dir(skill)
            self.test_openai_yaml(skill)
            self.test_skill_content_quality(skill)
            # New tests
            self.test_broken_internal_links(skill)
            self.test_forbidden_files(skill)
            self.test_duplicate_headings(skill)
            self.test_diagram_priority(skill)
            self.test_skill_catalog_consistency(skill)
            self.test_external_links(skill)

        return self.results

    def print_results(self):
        """Print test results."""
        print("\n" + "=" * 60)
        print("Test Results Summary")
        print("=" * 60)

        passed = sum(1 for r in self.results if r["passed"])
        failed = sum(1 for r in self.results if not r["passed"])
        total = len(self.results)

        # Print failures first, then passes
        for r in sorted(self.results, key=lambda x: (x["passed"], x["test"])):
            status = "PASS" if r["passed"] else "FAIL"
            print(f"  [{status}] {r['test']}")
            if not r["passed"] and "error" in r:
                print(f"         Error: {r['error']}")
            if "issues" in r:
                for issue in r["issues"]:
                    print(f"         Issue: {issue}")
            if "details" in r:
                for k, v in r["details"].items():
                    if isinstance(v, list) and len(v) > 5:
                        print(f"         {k}: {len(v)} items")
                    elif not isinstance(v, list):
                        print(f"         {k}: {v}")

        print("\n" + "=" * 60)
        print(f"Total: {total} | Passed: {passed} | Failed: {failed}")
        if failed > 0:
            print(f"Skills with failures: ", end="")
            failed_skills = set()
            for r in self.results:
                if not r["passed"]:
                    skill = r["test"].split(" ")[0]
                    failed_skills.add(skill)
            print(", ".join(sorted(failed_skills)))
        print("=" * 60)

        return failed == 0


if __name__ == "__main__":
    skills_dir = Path(__file__).parent.parent / "skills"
    tester = SkillTester(skills_dir)
    tester.run_all_tests()
    success = tester.print_results()
    sys.exit(0 if success else 1)
