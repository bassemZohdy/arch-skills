#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib
from pathlib import Path
def main():
    p=argparse.ArgumentParser(description="Check canonical and mirrored evaluator skill files")
    p.add_argument("--root",type=Path,default=Path(__file__).resolve().parents[1])
    a=p.parse_args()
    canonical=a.root/"skills/arch-evaluate/SKILL.md"
    mirror=a.root/".github/arch-evaluate/SKILL.md"
    if not mirror.exists():
        print("missing mirror:",mirror); return 1
    if hashlib.sha256(canonical.read_bytes()).digest()!=hashlib.sha256(mirror.read_bytes()).digest():
        print("mirror drift:",mirror); return 1
    print("mirrors: ok"); return 0
if __name__=="__main__": raise SystemExit(main())

