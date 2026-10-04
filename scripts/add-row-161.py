#!/usr/bin/env python3
"""Add row 161 (Row 68 → Row 141 ↔ Row 61 Handshake 4a meta prelude capstone reunion continuation)."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def tx(s: str, pairs: list[tuple[str, str]]) -> str:
    for a, b in pairs:
        s = s.replace(a, b)
    return s


def lift_141_to_161(s: str) -> str:
    s = s.replace("Row 142 closing loop", "__P142__")
    p = [
        ("Row 141 closing loop", "Row 161 closing loop"),
        ("row-141-closing-loop", "row-161-closing-loop"),
        ("Row 141 closing stitch", "Row 161 closing stitch"),
        ("row-141-closing-stitch", "row-161-closing-stitch"),
        ("prologue-preview-row-141", "prologue-preview-row-161"),
        ("Row 141 preview", "Row 161 preview"),
        ("Row 141 skill checkpoint", "Row 161 skill checkpoint"),
        ("skill-navigation-row-141", "skill-navigation-row-161"),
        ("memory sheet row 141", "memory sheet row 161"),
        ("Row 141 baby picture", "Row 161 baby picture"),
        ("Row 141 three-way audit", "Row 161 three-way audit"),
        (
            "Row 68 → Row 121 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion",
            "Row 68 → Row 141 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion continuation",
        ),
        (
            "row68-row121-handshake4a-meta-prelude-capstone-reunion-index-row-141",
            "row68-row141-handshake4a-meta-prelude-capstone-reunion-continuation-index-row-161",
        ),
        (
            "row-141-baby-picture-row68-row121-handshake4a-meta-prelude-capstone-reunion",
            "row-161-baby-picture-row68-row141-handshake4a-meta-prelude-capstone-reunion-continuation",
        ),
        ("[row 142]", "__R142__"),
        ("[row 122]", "[row 142]"),
        ("row 122", "row 142"),
        ("Row 122", "Row 142"),
        ("__R142__", "[row 142]"),
        ("[row 121]", "[row 141]"),
        ("row 121", "row 141"),
        ("Row 121", "Row 141"),
        ("[row 140]", "[row 160]"),
        ("row 140", "row 160"),
        ("Row 140", "Row 160"),
        ("(row 141)", "(row 161)"),
        ("row 141", "row 161"),
        ("Row 141", "Row 161"),
    ]
    s = tx(s, p)
    return s.replace("__P142__", "Row 142 closing loop")


def fix_row_161_corruptions() -> None:
    pairs = [
        ("reunion continuation reunion", "reunion continuation"),
        ("Row 68 → Row 161 Row 68 → Row 61", "Row 68 → Row 141 Row 68 → Row 61"),
        ("Row 68 → Row 161 Handshake", "Row 68 → Row 141 Handshake"),
        (
            "[row 161](preface.md#skill-navigation-row-141)",
            "[row 161](preface.md#skill-navigation-row-161)",
        ),
        (
            "[row 160](preface.md#skill-navigation-row-140)",
            "[row 160](preface.md#skill-navigation-row-160)",
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
    anchor = "### Row 141 baby picture"
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


def add_row_161() -> None:
    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    if "### Row 161 skill checkpoint" in preface:
        print("preface: row 161 already present")
    else:
        m = re.search(
            r"(### Row 141 skill checkpoint.*?)(?=\n### Row 142 skill checkpoint)",
            preface,
            re.S,
        )
        if not m:
            raise SystemExit("row 141 preface checkpoint missing")
        preface = preface.replace(
            "\n## The copper wire through the book",
            "\n" + lift_141_to_161(m.group(1)) + "\n## The copper wire through the book",
        )
        preface_path.write_text(preface)
        print("preface: added row 161")

    ep_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    ep = ep_path.read_text()
    if "row-161-closing-loop" not in ep:
        block = extract_between(ep, "### Row 141 closing loop", "### Row 142 closing loop")
        ep = ep.replace(
            "### Row 142 closing loop",
            lift_141_to_161(block) + "### Row 142 closing loop",
            1,
        )
        ep_path.write_text(ep)
        print("epilogue: added row 161 loop")

    pro_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    pro = pro_path.read_text()
    compass = (
        "| Row 68 → Row 141 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion continuation (row 161) |"
    )
    if compass not in pro:
        line141 = (
            "| Row 68 → Row 121 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion (row 141) |"
        )
        idx = pro.find(line141)
        if idx < 0:
            raise SystemExit("prologue compass row 141 not found")
        end = pro.find("\n", idx)
        line160 = (
            "| Row 68 → Row 140 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion continuation (row 160) |"
        )
        idx160 = pro.find(line160)
        end160 = pro.find("\n", idx160)
        pro = pro[: end160 + 1] + lift_141_to_161(pro[idx:end]) + "\n" + pro[end160 + 1 :]
        prev = extract_between(
            pro,
            '| <span id="prologue-preview-row-141"></span>',
            '\n| <span id="prologue-preview-row-142">',
        )
        pro = pro.replace(
            '| <span id="prologue-preview-row-141"></span>',
            lift_141_to_161(prev) + '| <span id="prologue-preview-row-141"></span>',
            1,
        )
        if "row-161-closing-stitch" not in pro:
            stitch = (
                "**Row 161 closing stitch (Row 68 → Row 141 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion continuation).** {#row-161-closing-stitch} "
                "When row 160 closed on the capstone path but row 61 Handshake 4a meta reunion still opens like standalone epilogue coursework — "
                "read [preface row 161](../preface.md#skill-navigation-row-161), "
                "[Row 68 → Row 141 reunion continuation index](../appendix/sources.md#row68-row141-handshake4a-meta-prelude-capstone-reunion-continuation-index-row-161), and "
                "[epilogue row 161 closing loop](../epilogue/multiscale.md#row-161-closing-loop) before row 62 opens on the capstone path.\n\n"
            )
            pro = pro.replace("**Row 142 closing stitch", stitch + "**Row 142 closing stitch", 1)
        pro_path.write_text(pro)
        print("prologue: added row 161")

    src_path = ROOT / "writings/appendix/chapters/sources.md"
    src = src_path.read_text()
    idx_key = "row68-row141-handshake4a-meta-prelude-capstone-reunion-continuation-index-row-161"
    if idx_key not in src:
        i = src.find(
            "## Row 68 → Row 121 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion index (row 141)"
        )
        j = src.find(
            "## Row 68 → Row 102 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion index (row 122)"
        )
        if i < 0 or j < 0:
            raise SystemExit("row 141/122 sources anchors missing")
        block = lift_141_to_161(src[i:j])
        block = block.replace(
            "## Row 68 → Row 141 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion continuation index (row 161)",
            f"## Row 68 → Row 141 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion continuation index (row 161) {{#{idx_key}}}",
            1,
        )
        tr = (
            "| 161 | Row 68 → Row 141 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion continuation "
            "(midpoint prelude gate ↔ Handshake 3 meta prelude capstone ↔ row 61 meta) | "
            f"[Row 68 → Row 141 Handshake 4a meta prelude capstone reunion continuation index](#{idx_key}) · "
            "[preface row 161](../preface.md#skill-navigation-row-161) · "
            "[prologue row 161 preview](../prologue/00-many-scales.md#prologue-preview-row-161) · "
            "[prologue row 161 closing stitch](../prologue/00-many-scales.md#row-161-closing-stitch) · "
            "[epilogue row 161 closing loop](../epilogue/multiscale.md#row-161-closing-loop) · "
            "[memory sheet row 161 baby picture](memory-sheet.md#row-161-baby-picture-row68-row141-handshake4a-meta-prelude-capstone-reunion-continuation) | "
            "Row 68 closed but row 61 Handshake 4a meta reunion still feels disconnected on the capstone path after row 141 — "
            "read row 68 + row 160 or row 141 gate + epilogue rate cross-links + row 61; "
            "[preface row 61](../preface.md#skill-navigation-row-61) |\n"
        )
        src = src.replace(
            "| 141 | Row 68 → Row 121 Row 68 → Row 61 Handshake 4a meta prelude capstone",
            tr + "| 141 | Row 68 → Row 121 Row 68 → Row 61 Handshake 4a meta prelude capstone",
        )
        src = src.replace(
            "## Row 68 → Row 121 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion index (row 141)",
            block
            + "## Row 68 → Row 121 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion index (row 141)",
            1,
        )
        src_path.write_text(src)
        print("sources: added row 161")

    mem_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    mem = mem_path.read_text()
    if "row-161-baby-picture" not in mem:
        baby = lift_141_to_161(
            extract_between(mem, "### Row 141 baby picture", "### Row 142 baby picture")
        )
        mem = mem.replace("### Row 142 baby picture", baby + "### Row 142 baby picture", 1)
        mt = (
            "| 161 | Meta | Row 68 → Row 141 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion continuation | "
            f"[Row 68 → Row 141 Handshake 4a meta prelude capstone reunion continuation index](sources.md#{idx_key}) · "
            "[preface row 161 skill checkpoint](../preface.md#skill-navigation-row-161) · "
            "[prologue row 161 preview](../prologue/00-many-scales.md#prologue-preview-row-161) · "
            "[prologue row 161 closing stitch](../prologue/00-many-scales.md#row-161-closing-stitch) · "
            "[epilogue row 161 closing loop](../epilogue/multiscale.md#row-161-closing-loop) | "
            "Row 68 closed but row 61 Handshake 4a meta reunion feels disconnected on the capstone path after row 141 — "
            "read row 68 + row 160 or row 141 gate + epilogue rate cross-links + row 61; "
            "[row 161 baby picture](#row-161-baby-picture-row68-row141-handshake4a-meta-prelude-capstone-reunion-continuation) |\n"
        )
        mem = mem.replace(
            "| 141 | Meta | Row 68 → Row 121 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion |",
            mt + "| 141 | Meta | Row 68 → Row 121 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion |",
        )
        mem_path.write_text(mem)
        print("memory-sheet: added row 161")


def main() -> None:
    dedupe_memory_baby_pictures()
    add_row_161()
    fix_row_161_corruptions()


if __name__ == "__main__":
    main()
