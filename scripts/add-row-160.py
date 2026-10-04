#!/usr/bin/env python3
"""Add row 160 (Row 68 → Row 140 ↔ Row 60 Handshake 3 meta prelude capstone reunion continuation)."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def tx(s: str, pairs: list[tuple[str, str]]) -> str:
    for a, b in pairs:
        s = s.replace(a, b)
    return s


def lift_140_to_160(s: str) -> str:
    s = s.replace("Row 141 closing loop", "__P141__")
    p = [
        ("Row 140 closing loop", "Row 160 closing loop"),
        ("row-140-closing-loop", "row-160-closing-loop"),
        ("Row 140 closing stitch", "Row 160 closing stitch"),
        ("row-140-closing-stitch", "row-160-closing-stitch"),
        ("prologue-preview-row-140", "prologue-preview-row-160"),
        ("Row 140 preview", "Row 160 preview"),
        ("Row 140 skill checkpoint", "Row 160 skill checkpoint"),
        ("skill-navigation-row-140", "skill-navigation-row-160"),
        ("memory sheet row 140", "memory sheet row 160"),
        ("Row 140 baby picture", "Row 160 baby picture"),
        ("Row 140 three-way audit", "Row 160 three-way audit"),
        (
            "Row 68 → Row 120 Row 68 → Row 60 Handshake 3 meta prelude capstone",
            "Row 68 → Row 140 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion continuation",
        ),
        (
            "row68-row120-handshake3-meta-prelude-capstone-reunion-index-row-140",
            "row68-row140-handshake3-meta-prelude-capstone-reunion-continuation-index-row-160",
        ),
        (
            "row-140-baby-picture-row68-row120-handshake3-meta-prelude-capstone-reunion",
            "row-160-baby-picture-row68-row140-handshake3-meta-prelude-capstone-reunion-continuation",
        ),
        ("[row 159]", "__R159__"),
        ("[row 139]", "[row 159]"),
        ("row 139", "row 159"),
        ("Row 139", "Row 159"),
        ("__R159__", "[row 159]"),
        ("[row 120]", "[row 140]"),
        ("row 120", "row 140"),
        ("Row 120", "Row 140"),
        ("(row 140)", "(row 160)"),
        ("row 140", "row 160"),
        ("Row 140", "Row 160"),
    ]
    s = tx(s, p)
    return s.replace("__P141__", "Row 141 closing loop")


def fix_row_160_corruptions() -> None:
    pairs = [
        ("reunion continuation reunion", "reunion continuation"),
        ("Row 68 → Row 160 Row 68 → Row 60", "Row 68 → Row 140 Row 68 → Row 60"),
        ("Row 68 → Row 160 Handshake", "Row 68 → Row 140 Handshake"),
        (
            "### Row 159 skill checkpoint — Row 68 → Row 139 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion audit {#skill-navigation-row-139}",
            "### Row 159 skill checkpoint — Row 68 → Row 139 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion audit {#skill-navigation-row-159}",
        ),
        (
            "[row 159](preface.md#skill-navigation-row-139)",
            "[row 159](preface.md#skill-navigation-row-159)",
        ),
        (
            "[row 160](preface.md#skill-navigation-row-120)",
            "[row 140](preface.md#skill-navigation-row-140)",
        ),
        (
            "[preface row 159](../preface.md#skill-navigation-row-139)",
            "[preface row 159](../preface.md#skill-navigation-row-159)",
        ),
    ]
    for rel in ROOT.glob("writings/**/*.md"):
        text = rel.read_text()
        orig = text
        for a, b in pairs:
            text = text.replace(a, b)
        if text != orig:
            rel.write_text(text)
            print(f"fixed corruptions: {rel.relative_to(ROOT)}")


def dedupe_memory_baby_pictures() -> None:
    path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    text = path.read_text()
    anchor = "### Row 140 baby picture"
    while True:
        first = text.find(anchor)
        second = text.find(anchor, first + 1)
        if second < 0:
            break
        end = text.find("\n### ", second + 1)
        if end < 0:
            end = len(text)
        text = text[:second] + text[end:]
    path.write_text(text)


def extract_between(text: str, start: str, end: str) -> str:
    i = text.find(start)
    if i < 0:
        raise SystemExit(f"start marker not found: {start[:80]}")
    j = text.find(end, i + len(start))
    if j < 0:
        raise SystemExit(f"end marker not found after {start[:40]}")
    return text[i:j]


def add_row_160() -> None:
    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    if "### Row 160 skill checkpoint" in preface:
        print("preface: row 160 already present")
    else:
        m = re.search(
            r"(### Row 140 skill checkpoint.*?)(?=\n### Row 141 skill checkpoint)",
            preface,
            re.S,
        )
        if not m:
            raise SystemExit("row 140 preface checkpoint missing")
        preface = preface.replace(
            "\n## The copper wire through the book",
            "\n" + lift_140_to_160(m.group(1)) + "\n## The copper wire through the book",
        )
        preface_path.write_text(preface)
        print("preface: added row 160")

    ep_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    ep = ep_path.read_text()
    if "row-160-closing-loop" not in ep:
        block = extract_between(ep, "### Row 140 closing loop", "### Row 141 closing loop")
        ep = ep.replace(
            "### Row 141 closing loop",
            lift_140_to_160(block) + "### Row 141 closing loop",
            1,
        )
        ep_path.write_text(ep)
        print("epilogue: added row 160 loop")

    pro_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    pro = pro_path.read_text()
    compass = (
        "| Row 68 → Row 140 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion continuation (row 160) |"
    )
    if compass not in pro:
        line140 = (
            "| Row 68 → Row 120 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion (row 140) |"
        )
        idx = pro.find(line140)
        if idx < 0:
            raise SystemExit("prologue compass row 140 not found")
        end = pro.find("\n", idx)
        line159 = (
            "| Row 68 → Row 139 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion (row 159) |"
        )
        idx159 = pro.find(line159)
        end159 = pro.find("\n", idx159)
        pro = pro[: end159 + 1] + lift_140_to_160(pro[idx:end]) + "\n" + pro[end159 + 1 :]
        prev = extract_between(
            pro,
            '| <span id="prologue-preview-row-140"></span>',
            '\n| <span id="prologue-preview-row-141">',
        )
        pro = pro.replace(
            '| <span id="prologue-preview-row-140"></span>',
            lift_140_to_160(prev) + '| <span id="prologue-preview-row-140"></span>',
            1,
        )
        if "row-160-closing-stitch" not in pro:
            stitch = (
                "**Row 160 closing stitch (Row 68 → Row 140 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion continuation).** {#row-160-closing-stitch} "
                "When row 159 closed on the capstone path but row 60 Handshake 3 meta reunion still opens like standalone epilogue coursework — "
                "read [preface row 160](../preface.md#skill-navigation-row-160), "
                "[Row 68 → Row 140 reunion continuation index](../appendix/sources.md#row68-row140-handshake3-meta-prelude-capstone-reunion-continuation-index-row-160), and "
                "[epilogue row 160 closing loop](../epilogue/multiscale.md#row-160-closing-loop) before row 61 opens on the capstone path.\n\n"
            )
            pro = pro.replace("**Row 141 closing stitch", stitch + "**Row 141 closing stitch", 1)
        pro_path.write_text(pro)
        print("prologue: added row 160")

    src_path = ROOT / "writings/appendix/chapters/sources.md"
    src = src_path.read_text()
    idx_key = "row68-row140-handshake3-meta-prelude-capstone-reunion-continuation-index-row-160"
    if idx_key not in src:
        i = src.find(
            "## Row 68 → Row 120 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion index (row 140)"
        )
        j = src.find(
            "## Row 68 → Row 101 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion index (row 121)"
        )
        block = lift_140_to_160(src[i:j])
        block = block.replace(
            "## Row 68 → Row 140 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion continuation index (row 160)",
            f"## Row 68 → Row 140 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion continuation index (row 160) {{#{idx_key}}}",
            1,
        )
        tr = (
            "| 160 | Row 68 → Row 140 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion continuation "
            "(midpoint prelude gate ↔ Handshake 3 meta prelude capstone ↔ row 60 meta) | "
            f"[Row 68 → Row 140 Handshake 3 meta prelude capstone reunion continuation index](#{idx_key}) · "
            "[preface row 160](../preface.md#skill-navigation-row-160) · "
            "[prologue row 160 preview](../prologue/00-many-scales.md#prologue-preview-row-160) · "
            "[prologue row 160 closing stitch](../prologue/00-many-scales.md#row-160-closing-stitch) · "
            "[epilogue row 160 closing loop](../epilogue/multiscale.md#row-160-closing-loop) · "
            "[memory sheet row 160 baby picture](memory-sheet.md#row-160-baby-picture-row68-row140-handshake3-meta-prelude-capstone-reunion-continuation) | "
            "Row 68 closed but row 60 Handshake 3 meta reunion still feels disconnected on the capstone path after row 140 — "
            "read row 68 + row 159 or row 140 gate + epilogue α cross-links + row 60; "
            "[preface row 60](../preface.md#skill-navigation-row-60) |\n"
        )
        src = src.replace(
            "| 159 | Row 68 → Row 139 Row 68 → Row 59 Handshake 3 meta prelude capstone",
            tr + "| 159 | Row 68 → Row 139 Row 68 → Row 59 Handshake 3 meta prelude capstone",
        )
        src = src.replace(
            "## Row 68 → Row 120 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion index (row 140)",
            block + "## Row 68 → Row 120 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion index (row 140)",
        )
        src_path.write_text(src)
        print("sources: added row 160")

    mem_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    mem = mem_path.read_text()
    if "row-160-baby-picture" not in mem:
        baby = lift_140_to_160(
            extract_between(mem, "### Row 140 baby picture", "### Row 141 baby picture")
        )
        mem = mem.replace("### Row 141 baby picture", baby + "### Row 141 baby picture", 1)
        mt = (
            "| 160 | Meta | Row 68 → Row 140 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion continuation | "
            f"[Row 68 → Row 140 Handshake 3 meta prelude capstone reunion continuation index](sources.md#{idx_key}) · "
            "[preface row 160 skill checkpoint](../preface.md#skill-navigation-row-160) · "
            "[prologue row 160 preview](../prologue/00-many-scales.md#prologue-preview-row-160) · "
            "[prologue row 160 closing stitch](../prologue/00-many-scales.md#row-160-closing-stitch) · "
            "[epilogue row 160 closing loop](../epilogue/multiscale.md#row-160-closing-loop) | "
            "Row 68 closed but row 60 Handshake 3 meta reunion feels disconnected on the capstone path after row 140 — "
            "read row 68 + row 159 or row 140 gate + epilogue α cross-links + row 60; "
            "[row 160 baby picture](#row-160-baby-picture-row68-row140-handshake3-meta-prelude-capstone-reunion-continuation) |\n"
        )
        mem = mem.replace(
            "| 159 | Meta | Row 68 → Row 139 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion |",
            mt + "| 159 | Meta | Row 68 → Row 139 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion |",
        )
        mem_path.write_text(mem)
        print("memory-sheet: added row 160")


def main() -> None:
    dedupe_memory_baby_pictures()
    add_row_160()
    fix_row_160_corruptions()


if __name__ == "__main__":
    main()
