#!/usr/bin/env python3
"""Rebuild row 145 sections and restore uncorrupted row 125 epilogue/sources blocks."""
from __future__ import annotations

import importlib.util
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

spec = importlib.util.spec_from_file_location("add_row_145", ROOT / "scripts/add-row-145.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

spec2 = importlib.util.spec_from_file_location("fix_row_145", ROOT / "scripts/fix-row-145-corruptions.py")
fix = importlib.util.module_from_spec(spec2)
spec2.loader.exec_module(fix)


def origin_text(path: str) -> str:
    return subprocess.check_output(
        ["git", "show", f"origin/cursor/computational-mechanics-book-ecc8:{path}"],
        cwd=ROOT,
        text=True,
    )


def extract_between(text: str, start: str, end: str) -> str:
    i = text.find(start)
    j = text.find(end, i + len(start))
    if i < 0 or j < 0:
        raise SystemExit(f"missing anchors: {start[:40]} .. {end[:40]}")
    return text[i:j]


def polish_row_145_index(s: str) -> str:
    extra = [
        ("Row 125 names **Row 68 → Row 125", "Row 145 names **Row 68 → Row 125"),
        ("Row 125 does not replace", "Row 145 does not replace"),
        ("when row 124 verified", "when row 144 verified"),
        ("row 124 or row 125 closed", "row 144 or row 125 closed"),
        ("row 124 names **Row 68 → Row 124", "row 144 names **Row 68 → Row 124"),
        ("Row 125 names **Row 68 → Row 85", "Row 105 names **Row 68 → Row 85"),
        (
            "[row 124](#row68-row104-book-loop-meta-prelude-capstone-reunion-index-row-124) or [row 125](#row68-row125-second-pass-meta-prelude-capstone-reunion-index-row-145)",
            "[row 144](#row68-row124-book-loop-meta-prelude-capstone-reunion-index-row-144) or [row 125](#row68-row105-second-pass-meta-prelude-capstone-reunion-index-row-125)",
        ),
        (
            "[Row 124 reunion (book-loop meta prelude capstone)](#row68-row104-book-loop-meta-prelude-capstone-reunion-index-row-124)",
            "[Row 144 reunion (book-loop meta prelude capstone)](#row68-row124-book-loop-meta-prelude-capstone-reunion-index-row-144)",
        ),
        (
            "[Row 125 reunion (meta prelude)](#row68-row85-second-pass-meta-prelude-reunion-index-row-105)",
            "[Row 125 reunion (opening-hinge meta prelude)](#row68-row85-second-pass-meta-prelude-reunion-index-row-105)",
        ),
        ("Row 124 or row 105 gate", "Row 144 or row 125 gate"),
        ("**Baby picture:** row 124 tells", "**Baby picture:** row 144 tells"),
        ("| [Preface row 125]", "| [Preface row 125]"),
    ]
    s = fix.polish_row_145_text(mod.lift_125_to_145(s))
    for a, b in extra:
        s = s.replace(a, b)
    return s


def rebuild_epilogue() -> None:
    ep_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    ep = ep_path.read_text()
    orig = origin_text("writings/epilogue/chapters/multiscale.md")
    row125_orig = extract_between(orig, "### Row 125 closing loop", "### Row 126 closing loop")
    row145 = extract_between(ep, "### Row 145 closing loop", "### Row 125 closing loop")
    row145 = fix.polish_row_145_text(row145)
    row145_fixes = [
        ("when row 124 closed book-loop", "when row 144 closed book-loop"),
        ("on the capstone path on the capstone path", "on the capstone path"),
        (
            "matches the same novel-rhythm contract per [row 125](../preface.md#skill-navigation-row-145)",
            "matches the same novel-rhythm contract per [row 125](../preface.md#skill-navigation-row-125)",
        ),
        (
            "Do not conflate row 125 (row 68 ↔ row 65 reunion on the capstone path) with row 125 (opening-hinge prelude stitch alone) — row 125 names **Row 68 → Row 85 Row 68 → Row 65 second-pass meta prelude reunion**; row 125 names **why that reunion must follow verified book-loop meta prelude capstone (row 124)",
            "Do not conflate row 145 (row 68 ↔ row 65 reunion on the capstone path) with row 105 (opening-hinge prelude stitch alone) — row 105 names **Row 68 → Row 85 Row 68 → Row 65 second-pass meta prelude reunion**; row 145 names **why that reunion must follow verified book-loop meta prelude capstone (row 144)",
        ),
        (
            "Proceed to [row 126](#row-126-closing-loop) when row 68 closed but Writings canonical meta prelude capstone still lags after row 125, to [row 126](#row-106-closing-loop)",
            "Proceed to [row 146](#row-146-closing-loop) when row 68 closed but Writings canonical meta prelude capstone still lags after row 145 on the capstone path, to [row 126](#row-126-closing-loop)",
        ),
        (
            "verified book-loop meta prelude capstone closure (row 124) and Row 68 → Row 65 meta (row 105)",
            "verified book-loop meta prelude capstone closure (row 144) and Row 68 → Row 65 meta (row 125)",
        ),
    ]
    for a, b in row145_fixes:
        row145 = row145.replace(a, b)
    if "Row 145 closes the **second-pass" not in row145:
        row145 = row145.replace(
            "Row 125 closes the **second-pass meta prelude capstone",
            "Row 145 closes the **second-pass meta prelude capstone",
        )
    marker = "### Row 145 closing loop"
    end = "### Row 126 closing loop"
    i = ep.find(marker)
    j = ep.find(end, i)
    if i < 0 or j < 0:
        raise SystemExit("epilogue row 145/126 anchors missing")
    ep = ep[:i] + row145 + row125_orig + ep[j:]
    ep_path.write_text(ep)
    print("epilogue: rebuilt row 145 + restored row 125")


def rebuild_sources_index() -> None:
    src_path = ROOT / "writings/appendix/chapters/sources.md"
    src = src_path.read_text()
    orig = origin_text("writings/appendix/chapters/sources.md")
    block125 = extract_between(
        orig,
        "## Row 68 → Row 105 Row 68 → Row 65 second-pass meta prelude capstone reunion index (row 125)",
        "## Row 68 → Row 106 Row 68 → Row 66 Writings canonical meta prelude capstone reunion index (row 126)",
    )
    block145 = polish_row_145_index(block125)
    header145 = "## Row 68 → Row 125 Row 68 → Row 65 second-pass meta prelude capstone reunion index (row 145) {#row68-row125-second-pass-meta-prelude-capstone-reunion-index-row-145}"
    header125 = "## Row 68 → Row 105 Row 68 → Row 65 second-pass meta prelude capstone reunion index (row 125)"
    i = src.find(header145)
    j = src.find(header125, i)
    if i < 0 or j < 0:
        raise SystemExit("sources row 145/125 headers missing")
    src = src[:i] + header145 + "\n\n" + block145.lstrip("# ...").lstrip() + header125 + src[j + len(header125) :]
    # block145 still has old header line at start - fix
    if block145.startswith("## Row 68"):
        body = block145.split("\n", 2)[2] if block145.count("\n") >= 2 else ""
    else:
        body = block145
    src = src[:i] + header145 + "\n\n" + body
    k = src.find(header125, i)
    l = src.find(
        "## Row 68 → Row 106 Row 68 → Row 66 Writings canonical meta prelude capstone reunion index (row 126)",
        k,
    )
    src = src[:k] + header125 + "\n\n" + block125.split("\n", 2)[2] + src[l:]
    src_path.write_text(src)
    print("sources: rebuilt row 145 index + restored row 125")


def patch_misc() -> None:
    for rel, pairs in [
        (
            "writings/preface/chapters/preface.md",
            [
                (
                    "[prologue row 125 closing stitch](prologue/00-many-scales.md#row-145-closing-stitch)",
                    "[prologue row 145 closing stitch](prologue/00-many-scales.md#row-145-closing-stitch)",
                ),
                (
                    "[prologue row 125 preview](prologue/00-many-scales.md#prologue-preview-row-145)",
                    "[prologue row 145 preview](prologue/00-many-scales.md#prologue-preview-row-145)",
                ),
            ],
        ),
        (
            "writings/prologue/chapters/00-many-scales.md",
            [
                ("row 124 or row 125 book-loop", "row 144 or row 125 book-loop"),
            ],
        ),
        (
            "writings/appendix/chapters/memory-sheet.md",
            [
                (
                    "row 124 or row 125 closed book-loop meta prelude capstone / second-pass meta prelude",
                    "row 144 or row 125 closed book-loop meta prelude capstone / second-pass meta prelude",
                ),
                (
                    "[preface row 124](../preface.md#skill-navigation-row-124) or [preface row 125](../preface.md#skill-navigation-row-105)",
                    "[preface row 144](../preface.md#skill-navigation-row-144) or [preface row 125](../preface.md#skill-navigation-row-125)",
                ),
                ("Book-loop meta prelude capstone row 124", "Book-loop meta prelude capstone row 144"),
            ],
        ),
    ]:
        path = ROOT / rel
        text = path.read_text()
        for a, b in pairs:
            text = text.replace(a, b)
        path.write_text(text)
        print(f"patched: {rel}")


def main() -> None:
    rebuild_epilogue()
    rebuild_sources_index()
    patch_misc()


if __name__ == "__main__":
    main()
