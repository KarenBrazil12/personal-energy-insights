#!/usr/bin/env python3
"""Check that local Markdown links resolve inside the repository."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
INLINE_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
REFERENCE_TARGET = re.compile(r"^\s*\[[^\]]+\]:\s*(\S+)", re.MULTILINE)
EXTERNAL_SCHEMES = ("http://", "https://", "mailto:", "tel:")


def normalise_target(raw: str) -> str | None:
    target = raw.strip()
    if target.startswith("<") and ">" in target:
        target = target[1 : target.index(">")]
    else:
        target = target.split()[0]

    target = unquote(target)
    if not target or target.startswith("#") or target.startswith(EXTERNAL_SCHEMES):
        return None

    return target.split("#", 1)[0].split("?", 1)[0]


def resolve(source: Path, target: str) -> Path:
    if target.startswith("/"):
        return ROOT / target.lstrip("/")
    return source.parent / target


def main() -> int:
    failures: list[tuple[Path, str, Path]] = []
    checked = 0

    for source in sorted(ROOT.rglob("*.md")):
        text = source.read_text(encoding="utf-8")
        raw_targets = INLINE_LINK.findall(text) + REFERENCE_TARGET.findall(text)

        for raw in raw_targets:
            target = normalise_target(raw)
            if target is None:
                continue

            checked += 1
            resolved = resolve(source, target)
            if not resolved.exists():
                failures.append((source.relative_to(ROOT), raw, resolved))

    if failures:
        print("Repository integrity check failed: broken internal Markdown links found.\n")
        for source, raw, resolved in failures:
            try:
                expected = resolved.resolve().relative_to(ROOT.resolve())
            except ValueError:
                expected = resolved.resolve()
            print(f"- {source}: {raw}")
            print(f"  Target not found: {expected}")
        print(f"\nChecked {checked} internal Markdown link target(s); {len(failures)} broken.")
        return 1

    print(f"Repository integrity check passed: {checked} internal Markdown link target(s) resolved.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
