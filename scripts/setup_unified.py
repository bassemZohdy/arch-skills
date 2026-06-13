#!/usr/bin/env python3
"""
Unified skill management - single source of truth.
Creates symlinks from each tool's expected location to the central skills/ directory.
"""

import os
import sys
import platform
from pathlib import Path

# Tool skill locations (where each tool expects to find skills)
TOOL_PATHS = {
    "claude-code": Path.home() / ".claude" / "skills",
    "codex": Path.home() / ".codex" / "skills",
    "cursor": Path.cwd() / ".cursor" / "rules",
    "copilot": Path.cwd() / ".github",
    "gemini": Path.home() / ".gemini" / "skills",
    "junie": Path.cwd() / ".agents" / "skills",
    "openhands": Path.cwd() / ".agents" / "skills",
    "opencode": Path.home() / ".config" / "opencode" / "skills",
    "pi": Path.home() / ".pi" / "skills",
    "cline": Path.cwd() / ".cline" / "skills",
    "kilocode": Path.home() / ".kilo" / "skills",
    "mimocode": Path.home() / ".mimocode" / "skills",
}


def create_symlink(source: Path, target: Path, force: bool = False):
    """Create a symlink from target to source."""
    if target.exists() or target.is_symlink():
        if force:
            if target.is_dir() and not target.is_symlink():
                import shutil
                shutil.rmtree(target)
            elif target.is_symlink():
                target.unlink()
        else:
            return True  # Already exists
    
    target.parent.mkdir(parents=True, exist_ok=True)
    
    try:
        if platform.system() == "Windows":
            # Windows: use directory junction for directories
            import subprocess
            subprocess.run(["mklink", "/J", str(target), str(source)], 
                         shell=True, check=True, capture_output=True)
        else:
            # Unix: use symbolic link
            os.symlink(source, target, target_is_directory=True)
        return True
    except Exception as e:
        print(f"  [WARN] Could not create symlink: {e}")
        return False


def setup_unified_skills(skills_dir: Path, force: bool = False):
    """Set up symlinks from tool locations to central skills directory."""
    print("=" * 60)
    print("Setting up unified skills (single source of truth)")
    print("=" * 60)
    print()
    print(f"Source: {skills_dir}")
    print()
    
    for tool_name, tool_path in TOOL_PATHS.items():
        try:
            success = create_symlink(skills_dir, tool_path, force)
            if success:
                print(f"  [OK] {tool_name}: {tool_path}")
            else:
                print(f"  [SKIP] {tool_name}: {tool_path}")
        except Exception as e:
            print(f"  [WARN] {tool_name}: {e}")
    
    print()
    print("=" * 60)
    print("Done! All tools now point to the same skills directory.")
    print("Changes to skills/ are immediately visible to all tools.")
    print("=" * 60)


def main():
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Set up unified skills - single source of truth"
    )
    parser.add_argument(
        "--skills-dir", 
        default=str(Path(__file__).parent.parent / "skills"),
        help="Path to skills directory"
    )
    parser.add_argument(
        "--force", 
        action="store_true",
        help="Overwrite existing symlinks/directories"
    )
    args = parser.parse_args()
    
    setup_unified_skills(Path(args.skills_dir), args.force)


if __name__ == "__main__":
    main()
