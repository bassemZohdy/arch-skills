#!/usr/bin/env python3
"""
Sync skills to all detected harness locations.
"""

import os
import sys
import shutil
from pathlib import Path

# Import harness detection
sys.path.insert(0, str(Path(__file__).parent))
from detect_harness import HARNESSES, get_skill_paths


def sync_skills(source_dir, target_paths):
    """Sync skills from source to target paths."""
    source = Path(source_dir)
    if not source.exists():
        print(f"Error: Source directory {source} does not exist")
        return False
    
    success = True
    for target in target_paths:
        target = Path(target)
        try:
            target.mkdir(parents=True, exist_ok=True)
            
            for skill_dir in source.iterdir():
                if skill_dir.is_dir() and skill_dir.name.startswith("arch-"):
                    dest = target / skill_dir.name
                    if dest.exists():
                        shutil.rmtree(dest)
                    shutil.copytree(skill_dir, dest)
                    print(f"  Synced: {skill_dir.name} → {target}")
            
            print(f"  ✓ Synced to {target}")
        except Exception as e:
            print(f"  ✗ Error syncing to {target}: {e}")
            success = False
    
    return success


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="Sync skills to harness locations")
    parser.add_argument("--source", default=str(Path(__file__).parent.parent / "skills"),
                       help="Source directory containing skills")
    parser.add_argument("--harness", help="Specific harness to sync to (e.g., claude-code)")
    parser.add_argument("--all", action="store_true", help="Sync to all detected harnesses")
    args = parser.parse_args()
    
    print("Syncing skills...")
    print()
    
    if args.harness:
        paths = get_skill_paths(args.harness)
        success = sync_skills(args.source, paths)
    elif args.all:
        paths = get_skill_paths()
        success = sync_skills(args.source, paths)
    else:
        # Default: sync to all detected harnesses
        paths = get_skill_paths()
        success = sync_skills(args.source, paths)
    
    print()
    if success:
        print("Done! All skills synced successfully.")
    else:
        print("Warning: Some sync operations failed.")
        sys.exit(1)


if __name__ == "__main__":
    main()
