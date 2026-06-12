#!/usr/bin/env python
"""
Architecture Skills Test Suite
Validates skill structure, content, and completeness.
"""

import os
import sys
import yaml
from pathlib import Path

# Add skill-creator scripts to path
SKILL_CREATOR_PATH = Path.home() / ".codex" / "skills" / ".system" / "skill-creator" / "scripts"
sys.path.insert(0, str(SKILL_CREATOR_PATH))

class SkillTester:
    def __init__(self, skills_dir):
        self.skills_dir = Path(skills_dir)
        self.results = []
    
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
        """Test that SKILL.md has valid frontmatter."""
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
            # Extract frontmatter
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
            passed = has_name and has_description
            
            self.results.append({
                "test": f"{skill_name} frontmatter",
                "passed": passed,
                "details": {
                    "has_name": has_name,
                    "has_description": has_description,
                    "name": frontmatter.get("name"),
                    "description_length": len(frontmatter.get("description", ""))
                }
            })
            return passed
        except Exception as e:
            self.results.append({
                "test": f"{skill_name} frontmatter",
                "passed": False,
                "error": str(e)
            })
            return False
    
    def test_references_dir(self, skill_name):
        """Test that references directory exists with files."""
        refs_path = self.skills_dir / skill_name / "references"
        if not refs_path.exists():
            self.results.append({
                "test": f"{skill_name} references directory",
                "passed": False,
                "error": "Directory not found"
            })
            return False
        
        files = list(refs_path.glob("*.md"))
        passed = len(files) > 0
        self.results.append({
            "test": f"{skill_name} references directory",
            "passed": passed,
            "details": {
                "file_count": len(files),
                "files": [f.name for f in files]
            }
        })
        return passed
    
    def test_assets_dir(self, skill_name):
        """Test that assets directory exists with files."""
        assets_path = self.skills_dir / skill_name / "assets"
        if not assets_path.exists():
            self.results.append({
                "test": f"{skill_name} assets directory",
                "passed": False,
                "error": "Directory not found"
            })
            return False
        
        files = list(assets_path.rglob("*"))
        files = [f for f in files if f.is_file()]
        passed = len(files) > 0
        self.results.append({
            "test": f"{skill_name} assets directory",
            "passed": passed,
            "details": {
                "file_count": len(files)
            }
        })
        return passed
    
    def test_openai_yaml(self, skill_name):
        """Test that agents/openai.yaml exists."""
        yaml_path = self.skills_dir / skill_name / "agents" / "openai.yaml"
        exists = yaml_path.exists()
        self.results.append({
            "test": f"{skill_name} agents/openai.yaml",
            "passed": exists
        })
        return exists
    
    def test_skill_content_quality(self, skill_name):
        """Test that SKILL.md has substantial content."""
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
        
        # Check for key sections
        has_workflow = any("workflow" in line.lower() for line in lines)
        has_steps = any("step" in line.lower() for line in lines)
        has_references = any("references" in line.lower() for line in lines)
        
        passed = word_count > 500 and has_workflow
        self.results.append({
            "test": f"{skill_name} content quality",
            "passed": passed,
            "details": {
                "word_count": word_count,
                "line_count": len(lines),
                "has_workflow": has_workflow,
                "has_steps": has_steps,
                "has_references": has_references
            }
        })
        return passed
    
    def run_all_tests(self):
        """Run all tests for all skills."""
        skills = ["arch-doc", "arch-review", "arch-fitness", "arch-decision",
                   "arch-security", "arch-perf", "arch-migration", "arch-api",
                   "arch-cloud", "arch-event", "arch-ddd", "arch-metrics",
                   "arch-resilience", "arch-test", "arch-data", "arch-observability",
                   "arch-usability", "arch-accessibility", "arch-compliance", "arch-deployment",
                   "arch-integration", "arch-microservices", "arch-devops", "arch-cost", "arch-governance"]
        
        print("=" * 60)
        print("Architecture Skills Test Suite")
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
        
        return self.results
    
    def print_results(self):
        """Print test results."""
        print("\n" + "=" * 60)
        print("Test Results Summary")
        print("=" * 60)
        
        passed = sum(1 for r in self.results if r["passed"])
        failed = sum(1 for r in self.results if not r["passed"])
        total = len(self.results)
        
        for r in self.results:
            status = "PASS" if r["passed"] else "FAIL"
            print(f"  [{status}] {r['test']}")
            if not r["passed"] and "error" in r:
                print(f"    Error: {r['error']}")
            if "details" in r:
                for k, v in r["details"].items():
                    if isinstance(v, list) and len(v) > 5:
                        print(f"    {k}: {len(v)} items")
                    else:
                        print(f"    {k}: {v}")
        
        print("\n" + "=" * 60)
        print(f"Total: {total} | Passed: {passed} | Failed: {failed}")
        print("=" * 60)
        
        return failed == 0


if __name__ == "__main__":
    skills_dir = Path(__file__).parent.parent / "skills"
    tester = SkillTester(skills_dir)
    tester.run_all_tests()
    success = tester.print_results()
    sys.exit(0 if success else 1)
