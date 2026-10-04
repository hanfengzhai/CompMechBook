#!/usr/bin/env python3
"""Add row 162 (Row 68 → Row 142 ↔ Row 62 Handshake 4b meta prelude capstone reunion continuation)."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def tx(s: str, pairs: list[tuple[str, str]]) -> str:
    for a, b in pairs:
        s = s.replace(a, b)
    return s


def lift_142_to_162(s: str) -> str:
    s = s.replace("Row 143 closing loop", "__P143__")
    p = [
        ("Row 142 closing loop", "Row 162 closing loop"),
        ("row-142-closing-loop", "row-162-closing-loop"),
        ("Row 142 closing stitch", "Row 162 closing stitch"),
        ("row-142-closing-stitch", "row-162-closing-stitch"),
        ("prologue-preview-row-142", "prologue-preview-row-162"),
        ("Row 142 preview", "Row 162 preview"),
        ("Row 142 skill checkpoint", "Row 162 skill checkpoint"),
        ("skill-navigation-row-142", "skill-navigation-row-162"),
        ("memory sheet row 142", "memory sheet row 162"),
        ("Row 142 baby picture", "Row 162 baby picture"),
        ("Row 142 three-way audit", "Row 162 three-way audit"),
        (
            "Row 68 → Row 122 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion",
            "Row 68 → Row 142 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion continuation",
        ),
        (
            "row68-row122-handshake4b-meta-prelude-capstone-reunion-index-row-142",
            "row68-row142-handshake4b-meta-prelude-capstone-reunion-continuation-index-row-162",
        ),
        (
            "row-142-baby-picture-row68-row122-handshake4b-meta-prelude-capstone-reunion",
            "row-162-baby-picture-row68-row142-handshake4b-meta-prelude-capstone-reunion-continuation",
        ),
        ("[row 143]", "__R143__"),
        ("[row 123]", "[row 143]"),
        ("row 123", "row 143"),
        ("Row 123", "Row 143"),
        ("__R143__", "[row 143]"),
        ("[row 122]", "[row 142]"),
        ("row 122", "row 142"),
        ("Row 122", "Row 142"),
        ("[row 141]", "[row 161]"),
        ("row 141", "row 161"),
        ("Row 141", "Row 161"),
        ("(row 142)", "(row 162)"),
        ("row 142", "row 162"),
        ("Row 142", "Row 162"),
    ]
    s = tx(s, p)
    return s.replace("__P143__", "Row 143 closing loop")


def fix_row_162_corruptions() -> None:
    pairs = [
        ("reunion continuation reunion", "reunion continuation"),
        ("Row 68 → Row 162 Row 68 → Row 62", "Row 68 → Row 142 Row 68 → Row 62"),
        ("Row 68 → Row 162 Handshake", "Row 68 → Row 142 Handshake"),
        (
            "[row 162](preface.md#skill-navigation-row-142)",
            "[row 162](preface.md#skill-navigation-row-162)",
        ),
        (
            "[row 161](preface.md#skill-navigation-row-141)",
            "[row 161](preface.md#skill-navigation-row-161)",
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
    anchor = "### Row 142 baby picture"
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


def add_row_162() -> None:
    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    if "### Row 162 skill checkpoint" in preface:
        print("preface: row 162 already present")
    else:
        m = re.search(
            r"(### Row 142 skill checkpoint.*?)(?=\n### Row 143 skill checkpoint)",
            preface,
            re.S,
        )
        if not m:
            raise SystemExit("row 142 preface checkpoint missing")
        preface = preface.replace(
            "\n## The copper wire through the book",
            "\n" + lift_142_to_162(m.group(1)) + "\n## The copper wire through the book",
        )
        preface_path.write_text(preface)
        print("preface: added row 162")

    ep_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    ep = ep_path.read_text()
    if "row-162-closing-loop" not in ep:
        block = extract_between(
            ep,
            "### Row 142 closing loop (Row 68 → Row 122 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion) {#row-142-closing-loop}",
            "### Row 143 closing loop (Row 68 → Row 123 Row 68 → Row 63 orchestration meta prelude capstone reunion) {#row-143-closing-loop}",
        )
        ep = ep.replace(
            "### Row 143 closing loop",
            lift_142_to_162(block) + "### Row 143 closing loop",
            1,
        )
        ep_path.write_text(ep)
        print("epilogue: added row 162 loop")

    pro_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    pro = pro_path.read_text()
    compass = (
        "| Row 68 → Row 142 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion continuation (row 162) |"
    )
    if compass not in pro:
        line142 = (
            "| Row 68 → Row 122 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion (row 142) |"
        )
        idx = pro.find(line142)
        if idx < 0:
            raise SystemExit("prologue compass row 142 not found")
        end = pro.find("\n", idx)
        line161 = (
            "| Row 68 → Row 141 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion continuation (row 161) |"
        )
        idx161 = pro.find(line161)
        end161 = pro.find("\n", idx161)
        pro = pro[: end161 + 1] + lift_142_to_162(pro[idx:end]) + "\n" + pro[end161 + 1 :]
        prev = extract_between(
            pro,
            '| <span id="prologue-preview-row-142"></span>',
            '\n| <span id="prologue-preview-row-143">',
        )
        pro = pro.replace(
            '| <span id="prologue-preview-row-142"></span>',
            lift_142_to_162(prev) + '| <span id="prologue-preview-row-142"></span>',
            1,
        )
        if "row-162-closing-stitch" not in pro:
            stitch = (
                "**Row 162 closing stitch (Row 68 → Row 142 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion continuation).** {#row-162-closing-stitch} "
                "When row 161 closed on the capstone path but row 62 Handshake 4b meta reunion still opens like standalone epilogue coursework — "
                "read [preface row 162](../preface.md#skill-navigation-row-162), "
                "[Row 68 → Row 142 reunion continuation index](../appendix/sources.md#row68-row142-handshake4b-meta-prelude-capstone-reunion-continuation-index-row-162), and "
                "[epilogue row 162 closing loop](../epilogue/multiscale.md#row-162-closing-loop) before row 63 opens on the capstone path.\n\n"
            )
            pro = pro.replace("**Row 143 closing stitch", stitch + "**Row 143 closing stitch", 1)
        pro_path.write_text(pro)
        print("prologue: added row 162")

    src_path = ROOT / "writings/appendix/chapters/sources.md"
    src = src_path.read_text()
    idx_key = "row68-row142-handshake4b-meta-prelude-capstone-reunion-continuation-index-row-162"
    if idx_key not in src:
        i = src.find(
            "## Row 68 → Row 122 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion index (row 142)"
        )
        j = src.find(
            "## Row 68 → Row 103 Row 68 → Row 63 orchestration meta prelude capstone reunion index (row 123)"
        )
        if i < 0 or j < 0:
            raise SystemExit("row 142/123 sources anchors missing")
        block = lift_142_to_162(src[i:j])
        block = block.replace(
            "## Row 68 → Row 142 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion continuation index (row 162)",
            f"## Row 68 → Row 142 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion continuation index (row 162) {{#{idx_key}}}",
            1,
        )
        tr = (
            "| 162 | Row 68 → Row 142 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion continuation "
            "(midpoint prelude gate ↔ Handshake 4a meta prelude capstone ↔ row 62 meta) | "
            f"[Row 68 → Row 142 Handshake 4b meta prelude capstone reunion continuation index](#{idx_key}) · "
            "[preface row 162](../preface.md#skill-navigation-row-162) · "
            "[prologue row 162 preview](../prologue/00-many-scales.md#prologue-preview-row-162) · "
            "[prologue row 162 closing stitch](../prologue/00-many-scales.md#row-162-closing-stitch) · "
            "[epilogue row 162 closing loop](../epilogue/multiscale.md#row-162-closing-loop) · "
            "[memory sheet row 162 baby picture](memory-sheet.md#row-162-baby-picture-row68-row142-handshake4b-meta-prelude-capstone-reunion-continuation) | "
            "Row 68 closed but row 62 Handshake 4b meta reunion still feels disconnected on the capstone path after row 142 — "
            "read row 68 + row 161 or row 142 gate + epilogue FE² cross-links + row 62; "
            "[preface row 62](../preface.md#skill-navigation-row-62) |\n"
        )
        src = src.replace(
            "| 142 | Row 68 → Row 122 Row 68 → Row 62 Handshake 4b meta prelude capstone",
            tr + "| 142 | Row 68 → Row 122 Row 68 → Row 62 Handshake 4b meta prelude capstone",
        )
        src = src.replace(
            "## Row 68 → Row 122 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion index (row 142)",
            block
            + "## Row 68 → Row 122 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion index (row 142)",
            1,
        )
        src_path.write_text(src)
        print("sources: added row 162")

    mem_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    mem = mem_path.read_text()
    if "row-162-baby-picture" not in mem:
        baby = lift_142_to_162(
            extract_between(mem, "### Row 142 baby picture", "### Row 143 baby picture")
        )
        mem = mem.replace("### Row 143 baby picture", baby + "### Row 143 baby picture", 1)
        mt = (
            "| 162 | Meta | Row 68 → Row 142 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion continuation | "
            f"[Row 68 → Row 142 Handshake 4b meta prelude capstone reunion continuation index](sources.md#{idx_key}) · "
            "[preface row 162 skill checkpoint](../preface.md#skill-navigation-row-162) · "
            "[prologue row 162 preview](../prologue/00-many-scales.md#prologue-preview-row-162) · "
            "[prologue row 162 closing stitch](../prologue/00-many-scales.md#row-162-closing-stitch) · "
            "[epilogue row 162 closing loop](../epilogue/multiscale.md#row-162-closing-loop) | "
            "Row 68 closed but row 62 Handshake 4b meta reunion feels disconnected on the capstone path after row 142 — "
            "read row 68 + row 161 or row 142 gate + epilogue FE² cross-links + row 62; "
            "[row 162 baby picture](#row-162-baby-picture-row68-row142-handshake4b-meta-prelude-capstone-reunion-continuation) |\n"
        )
        mem = mem.replace(
            "| 142 | Meta | Row 68 → Row 122 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion |",
            mt + "| 142 | Meta | Row 68 → Row 122 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion |",
        )
        mem_path.write_text(mem)
        print("memory-sheet: added row 162")


def main() -> None:
    dedupe_memory_baby_pictures()
    add_row_162()
    fix_row_162_corruptions()
    import importlib.util

    spec = importlib.util.spec_from_file_location(
        "fix_row_162", ROOT / "scripts/fix-row-162-corruptions.py"
    )
    fix = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(fix)
    fix.main()


if __name__ == "__main__":
    main()
