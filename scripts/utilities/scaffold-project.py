#!/usr/bin/env python3
"""
Scaffold a new project from vibe-centric templates.

Usage:
  python scripts/utilities/scaffold-project.py --type python --name myproj --out ../myproj
  python scripts/utilities/scaffold-project.py --type terraform --name myinfra --out ../myinfra

Notes:
- Minimal, dependency-free script for portability.
- Copies template tree and does placeholder substitution for {{PROJECT_NAME}} and {{PY_PACKAGE}}.
"""
from __future__ import annotations

import argparse
import os
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TEMPLATES = ROOT / "templates" / "projects"

PLACEHOLDERS = {
    "{{PROJECT_NAME}}": None,  # filled from args.name
    "{{PY_PACKAGE}}": None,    # derived from name (safe package)
}


def to_package(name: str) -> str:
    return name.strip().lower().replace("-", "_").replace(" ", "_")


def copy_with_substitution(src: Path, dst: Path, subs: dict[str, str]) -> None:
    if src.is_dir():
        for child in src.iterdir():
            rel = child.relative_to(src)
            target = dst / rel
            if child.is_dir():
                target.mkdir(parents=True, exist_ok=True)
                copy_with_substitution(child, target, subs)
            else:
                target.parent.mkdir(parents=True, exist_ok=True)
                text = child.read_text(encoding="utf-8")
                for k, v in subs.items():
                    text = text.replace(k, v)
                target.write_text(text, encoding="utf-8")
    else:
        dst.parent.mkdir(parents=True, exist_ok=True)
        text = src.read_text(encoding="utf-8")
        for k, v in subs.items():
            text = text.replace(k, v)
        dst.write_text(text, encoding="utf-8")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--type", choices=["python", "terraform"], required=True)
    ap.add_argument("--name", required=True, help="Project name")
    ap.add_argument("--out", required=True, help="Output directory to create")
    args = ap.parse_args()

    template_dir = TEMPLATES / args.type
    if not template_dir.exists():
        raise SystemExit(f"Template not found: {template_dir}")

    out_dir = Path(args.out).resolve()
    if out_dir.exists() and any(out_dir.iterdir()):
        raise SystemExit(f"Output directory exists and is not empty: {out_dir}")
    out_dir.mkdir(parents=True, exist_ok=True)

    subs = dict(PLACEHOLDERS)
    subs["{{PROJECT_NAME}}"] = args.name
    subs["{{PY_PACKAGE}}"] = to_package(args.name)

    copy_with_substitution(template_dir, out_dir, subs)
    print(f"Scaffolded {args.type} project at {out_dir}")


if __name__ == "__main__":
    main()
