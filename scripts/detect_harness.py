#!/usr/bin/env python3
"""
Detect which AI agent harness is available and configure skill paths.
Supports: Claude Code, OpenAI Codex, Cursor, Gemini CLI, Copilot, Junie,
OpenHands, OpenCode, Pi, Cline, Kilo Code, MiMoCode (12 harnesses total)
"""

import os
import sys
import platform
from pathlib import Path

# Supported harnesses and their skill paths
HARNESSES = {
    "claude-code": {
        "name": "Claude Code",
        "paths": [
            Path.home() / ".claude" / "skills",
            Path.cwd() / ".claude" / "skills",
        ],
        "command": "claude",
    },
    "codex": {
        "name": "OpenAI Codex",
        "paths": [
            Path.home() / ".codex" / "skills",
            Path.cwd() / ".codex" / "skills",
        ],
        "command": "codex",
    },
    "cursor": {
        "name": "Cursor",
        "paths": [
            Path.cwd() / ".cursor" / "rules",
            Path.home() / ".cursor" / "rules",
        ],
        "command": "cursor",
    },
    "copilot": {
        "name": "GitHub Copilot",
        "paths": [
            Path.cwd() / ".github" / "copilot-instructions.md",
            Path.home() / ".github" / "copilot-instructions.md",
        ],
        "command": "copilot",
    },
    "gemini": {
        "name": "Gemini CLI",
        "paths": [
            Path.cwd() / ".gemini" / "skills",
            Path.home() / ".gemini" / "skills",
        ],
        "command": "gemini",
    },
    "junie": {
        "name": "JetBrains Junie",
        "paths": [
            Path.cwd() / ".agents" / "skills",
        ],
        "command": "junie",
    },
    "openhands": {
        "name": "OpenHands",
        "paths": [
            Path.cwd() / ".agents" / "skills",
        ],
        "command": "openhands",
    },
    "opencode": {
        "name": "OpenCode",
        "paths": [
            Path.home() / ".config" / "opencode" / "skills",
            Path.cwd() / ".opencode" / "skills",
            Path.cwd() / ".agents" / "skills",
        ],
        "command": "opencode",
    },
    "pi": {
        "name": "Pi (badlogic)",
        "paths": [
            Path.cwd() / ".pi" / "skills",
            Path.home() / ".pi" / "skills",
        ],
        "command": "pi",
    },
    "cline": {
        "name": "Cline",
        "paths": [
            Path.cwd() / ".cline" / "skills",
            Path.cwd() / ".clinerules",
        ],
        "command": "cline",
    },
    "kilocode": {
        "name": "Kilo Code",
        "paths": [
            Path.cwd() / ".kilo" / "skills",
            Path.cwd() / ".kilocode" / "skills",
        ],
        "command": "kilo",
    },
    "mimocode": {
        "name": "MiMoCode",
        "paths": [
            Path.home() / ".mimocode" / "skills",
            Path.cwd() / ".mimocode" / "skills",
            Path.cwd() / ".agents" / "skills",
        ],
        "command": "mimocode",
    },
}


def detect_harnesses():
    """Detect available harnesses on the system."""
    available = []
    for harness_id, config in HARNESSES.items():
        # Check if command exists
        import shutil
        if shutil.which(config["command"]):
            available.append(harness_id)
    return available


def get_skill_paths(harness_id=None):
    """Get skill installation paths for a harness or all harnesses."""
    if harness_id and harness_id in HARNESSES:
        return HARNESSES[harness_id]["paths"]
    
    paths = []
    for config in HARNESSES.values():
        paths.extend(config["paths"])
    return list(set(paths))  # Remove duplicates


def print_detection_results():
    """Print detection results."""
    print("=" * 60)
    print("AI Agent Harness Detection")
    print("=" * 60)
    print()
    
    available = detect_harnesses()
    
    if available:
        print("Detected harnesses:")
        for harness_id in available:
            config = HARNESSES[harness_id]
            print(f"  [OK] {config['name']} ({harness_id})")
    else:
        print("No harnesses detected.")
    
    print()
    print("Supported harnesses:")
    for harness_id, config in HARNESSES.items():
        status = "[OK]" if harness_id in available else "[--]"
        print(f"  {status} {config['name']} ({harness_id})")
    
    print()
    print("Skill installation paths:")
    for harness_id in HARNESSES:
        config = HARNESSES[harness_id]
        for path in config["paths"]:
            exists = "[OK]" if path.exists() else "[--]"
            print(f"  {exists} {path}")
    
    print()
    print("=" * 60)


if __name__ == "__main__":
    print_detection_results()
