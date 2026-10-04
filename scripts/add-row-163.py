#!/usr/bin/env python3
"""Add row 163 (Row 68 → Row 143 ↔ Row 63 orchestration meta prelude capstone reunion continuation)."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def tx(s: str, pairs: list[tuple[str, str]]) -> str:
    for a, b in pairs:
        s = s.replace(a, b)
    return s


def lift_143_to_163(s: str) -> str:
    s = s.replace("Row 144 closing loop", "__P144__")
    p = [
        ("Row 143 closing loop", "Row 163 closing loop"),
        ("row-143-closing-loop", "row-163-closing-loop"),
        ("Row 143 closing stitch", "Row 163 closing stitch"),
        ("row-143-closing-stitch", "row-163-closing-stitch"),
        ("prologue-preview-row-143", "prologue-preview-row-163"),
        ("Row 143 preview", "Row 163 preview"),
        ("Row 143 skill checkpoint", "Row 163 skill checkpoint"),
        ("skill-navigation-row-143", "skill-navigation-row-163"),
        ("memory sheet row 143", "memory sheet row 163"),
        ("Row 143 baby picture", "Row 163 baby picture"),
        ("Row 143 three-way audit", "Row 163 three-way audit"),
        (
            "Row 68 → Row 123 Row 68 → Row 63 orchestration meta prelude capstone reunion",
            "Row 68 → Row 143 Row 68 → Row 63 orchestration meta prelude capstone reunion continuation",
        ),
        (
            "row68-row123-orchestration-meta-prelude-capstone-reunion-index-row-143",
            "row68-row143-orchestration-meta-prelude-capstone-reunion-continuation-index-row-163",
        ),
        (
            "row-143-baby-picture-row68-row123-orchestration-meta-prelude-capstone-reunion",
            "row-163-baby-picture-row68-row143-orchestration-meta-prelude-capstone-reunion-continuation",
        ),
        ("[row 144]", "__R144__"),
        ("[row 124]", "[row 144]"),
        ("row 124", "row 144"),
        ("Row 124", "Row 144"),
        ("__R144__", "[row 144]"),
        ("[row 123]", "[row 143]"),
        ("row 123", "row 143"),
        ("Row 123", "Row 143"),
        ("[row 142]", "[row 162]"),
        ("row 142", "row 162"),
        ("Row 142", "Row 162"),
        ("(row 143)", "(row 163)"),
        ("row 143", "row 163"),
        ("Row 143", "Row 163"),
        (
            "orchestration meta prelude capstone reunion audit",
            "orchestration meta prelude capstone reunion continuation audit",
        ),
        (
            "Row 143 does not replace row 68, row 63, row 162, row 143",
            "Row 163 does not replace row 68, row 63, row 162, row 143",
        ),
        (
            "Row 143 does not replace row 68, row 63, row 142, row 123",
            "Row 163 does not replace row 68, row 63, row 162, row 143",
        ),
        (
            "verified Handshake 4b meta prelude capstone closure (row 162)",
            "__VH4B162__",
        ),
        (
            "verified Handshake 4b meta prelude capstone closure (row 142)",
            "verified Handshake 4b meta prelude capstone closure (row 162)",
        ),
        ("__VH4B162__", "verified Handshake 4b meta prelude capstone closure (row 162)"),
        (
            "before row 144 book-loop meta prelude capstone or row 64 workflow reunion opens on the capstone path",
            "before row 164 book-loop meta prelude capstone or row 64 workflow reunion opens on the capstone path",
        ),
    ]
    s = tx(s, p)
    return s.replace("__P144__", "Row 144 closing loop")


def fix_row_163_corruptions() -> None:
    pairs = [
        ("reunion continuation continuation", "reunion continuation"),
        (
            "[row 163](preface.md#skill-navigation-row-143)",
            "[row 163](preface.md#skill-navigation-row-163)",
        ),
        (
            "Row 68 → Row 163 Row 68 → Row 63",
            "Row 68 → Row 143 Row 68 → Row 63",
        ),
        (
            "row68-row163-orchestration",
            "row68-row143-orchestration",
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
    anchor = "### Row 143 baby picture"
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


def add_row_163() -> None:
    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    if "### Row 163 skill checkpoint" in preface:
        print("preface: row 163 already present")
    else:
        m = re.search(
            r"(### Row 143 skill checkpoint.*?)(?=\n### Row 144 skill checkpoint)",
            preface,
            re.S,
        )
        if not m:
            raise SystemExit("row 143 preface checkpoint missing")
        preface = preface.replace(
            "\n## The copper wire through the book",
            "\n" + lift_143_to_163(m.group(1)) + "\n## The copper wire through the book",
        )
        preface_path.write_text(preface)
        print("preface: added row 163")

    ep_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    ep = ep_path.read_text()
    if "row-163-closing-loop" not in ep:
        block = extract_between(
            ep,
            "### Row 143 closing loop (Row 68 → Row 123 Row 68 → Row 63 orchestration meta prelude capstone reunion) {#row-143-closing-loop}",
            "### Row 144 closing loop (Row 68 → Row 124 Row 68 → Row 64 book-loop meta prelude capstone reunion) {#row-144-closing-loop}",
        )
        ep = ep.replace(
            "### Row 144 closing loop (Row 68 → Row 124 Row 68 → Row 64 book-loop meta prelude capstone reunion) {#row-144-closing-loop}",
            lift_143_to_163(block)
            + "### Row 144 closing loop (Row 68 → Row 124 Row 68 → Row 64 book-loop meta prelude capstone reunion) {#row-144-closing-loop}",
            1,
        )
        ep_path.write_text(ep)
        print("epilogue: added row 163 loop")

    pro_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    pro = pro_path.read_text()
    compass = (
        "| Row 68 → Row 143 Row 68 → Row 63 orchestration meta prelude capstone reunion continuation (row 163) |"
    )
    if compass not in pro:
        line143 = (
            "| Row 68 → Row 123 Row 68 → Row 63 orchestration meta prelude capstone reunion (row 143) |"
        )
        idx = pro.find(line143)
        if idx < 0:
            raise SystemExit("prologue compass row 143 not found")
        end = pro.find("\n", idx)
        line162 = (
            "| Row 68 → Row 142 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion continuation (row 162) |"
        )
        idx162 = pro.find(line162)
        end162 = pro.find("\n", idx162)
        pro = pro[: end162 + 1] + lift_143_to_163(pro[idx:end]) + "\n" + pro[end162 + 1 :]
        prev = extract_between(
            pro,
            '| <span id="prologue-preview-row-143"></span>',
            '\n| <span id="prologue-preview-row-144">',
        )
        pro = pro.replace(
            '| <span id="prologue-preview-row-143"></span>',
            lift_143_to_163(prev) + '| <span id="prologue-preview-row-143"></span>',
            1,
        )
        if "row-163-closing-stitch" not in pro:
            stitch = (
                "**Row 163 closing stitch (Row 68 → Row 143 Row 68 → Row 63 orchestration meta prelude capstone reunion continuation).** {#row-163-closing-stitch} "
                "When row 162 closed on the capstone path but row 63 orchestration meta reunion still opens like standalone epilogue coursework — "
                "read [preface row 163](../preface.md#skill-navigation-row-163), "
                "[Row 68 → Row 143 reunion continuation index](../appendix/sources.md#row68-row143-orchestration-meta-prelude-capstone-reunion-continuation-index-row-163), and "
                "[epilogue row 163 closing loop](../epilogue/multiscale.md#row-163-closing-loop) before row 64 opens on the capstone path.\n\n"
            )
            pro = pro.replace("**Row 144 closing stitch", stitch + "**Row 144 closing stitch", 1)
        pro_path.write_text(pro)
        print("prologue: added row 163")

    src_path = ROOT / "writings/appendix/chapters/sources.md"
    src = src_path.read_text()
    idx_key = "row68-row143-orchestration-meta-prelude-capstone-reunion-continuation-index-row-163"
    if idx_key not in src:
        i = src.find(
            "## Row 68 → Row 123 Row 68 → Row 63 orchestration meta prelude capstone reunion index (row 143)"
        )
        j = src.find(
            "## Row 68 → Row 124 Row 68 → Row 64 book-loop meta prelude capstone reunion index (row 144)"
        )
        if i < 0 or j < 0:
            raise SystemExit("row 143/144 sources anchors missing")
        block = lift_143_to_163(src[i:j])
        block = block.replace(
            "## Row 68 → Row 163 Row 68 → Row 63 orchestration meta prelude capstone reunion continuation index (row 163)",
            f"## Row 68 → Row 143 Row 68 → Row 63 orchestration meta prelude capstone reunion continuation index (row 163) {{#{idx_key}}}",
            1,
        )
        tr = (
            "| 163 | Row 68 → Row 143 Row 68 → Row 63 orchestration meta prelude capstone reunion continuation "
            "(midpoint prelude gate ↔ Handshake 4b meta prelude capstone ↔ row 63 meta) | "
            f"[Row 68 → Row 143 orchestration meta prelude capstone reunion continuation index](#{idx_key}) · "
            "[preface row 163](../preface.md#skill-navigation-row-163) · "
            "[prologue row 163 preview](../prologue/00-many-scales.md#prologue-preview-row-163) · "
            "[prologue row 163 closing stitch](../prologue/00-many-scales.md#row-163-closing-stitch) · "
            "[epilogue row 163 closing loop](../epilogue/multiscale.md#row-163-closing-loop) · "
            "[memory sheet row 163 baby picture](memory-sheet.md#row-163-baby-picture-row68-row143-orchestration-meta-prelude-capstone-reunion-continuation) | "
            "Row 68 closed but row 63 orchestration meta reunion still feels disconnected on the capstone path after row 143 — "
            "read row 68 + row 162 or row 143 gate + epilogue orchestration cross-links + row 63; "
            "[preface row 63](../preface.md#skill-navigation-row-63) |\n"
        )
        src = src.replace(
            "| 143 | Row 68 → Row 123 Row 68 → Row 63 orchestration meta prelude capstone",
            tr + "| 143 | Row 68 → Row 123 Row 68 → Row 63 orchestration meta prelude capstone",
        )
        src = src.replace(
            "## Row 68 → Row 123 Row 68 → Row 63 orchestration meta prelude capstone reunion index (row 143)",
            block
            + "## Row 68 → Row 123 Row 68 → Row 63 orchestration meta prelude capstone reunion index (row 143)",
            1,
        )
        src_path.write_text(src)
        print("sources: added row 163")

    mem_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    mem = mem_path.read_text()
    if "row-163-baby-picture" not in mem:
        baby = lift_143_to_163(
            extract_between(mem, "### Row 143 baby picture", "### Row 144 baby picture")
        )
        mem = mem.replace("### Row 144 baby picture", baby + "### Row 144 baby picture", 1)
        mt = (
            "| 163 | Meta | Row 68 → Row 143 Row 68 → Row 63 orchestration meta prelude capstone reunion continuation | "
            f"[Row 68 → Row 143 orchestration meta prelude capstone reunion continuation index](sources.md#{idx_key}) · "
            "[preface row 163 skill checkpoint](../preface.md#skill-navigation-row-163) · "
            "[prologue row 163 preview](../prologue/00-many-scales.md#prologue-preview-row-163) · "
            "[prologue row 163 closing stitch](../prologue/00-many-scales.md#row-163-closing-stitch) · "
            "[epilogue row 163 closing loop](../epilogue/multiscale.md#row-163-closing-loop) | "
            "Row 68 closed but row 63 orchestration meta reunion feels disconnected on the capstone path after row 143 — "
            "read row 68 + row 162 or row 143 gate + epilogue orchestration cross-links + row 63; "
            "[row 163 baby picture](#row-163-baby-picture-row68-row143-orchestration-meta-prelude-capstone-reunion-continuation) |\n"
        )
        mem = mem.replace(
            "| 143 | Meta | Row 68 → Row 123 Row 68 → Row 63 orchestration meta prelude capstone reunion |",
            mt + "| 143 | Meta | Row 68 → Row 123 Row 68 → Row 63 orchestration meta prelude capstone reunion |",
        )
        if "When row 162 closed but orchestration meta prelude reunion still lags" not in mem:
            mem = mem.replace(
                "When row 162 closed but Handshake 4b meta prelude reunion still lags on the capstone path, switch to [row 162](#row-162-baby-picture-row68-row142-handshake4b-meta-prelude-capstone-reunion-continuation).",
                "When row 162 closed but Handshake 4b meta prelude reunion still lags on the capstone path, switch to [row 162](#row-162-baby-picture-row68-row142-handshake4b-meta-prelude-capstone-reunion-continuation). "
                "When row 162 closed but orchestration meta prelude reunion still lags on the capstone path, switch to [row 163](#row-163-baby-picture-row68-row143-orchestration-meta-prelude-capstone-reunion-continuation).",
            )
        mem_path.write_text(mem)
        print("memory-sheet: added row 163")


def main() -> None:
    dedupe_memory_baby_pictures()
    add_row_163()
    fix_row_163_corruptions()


if __name__ == "__main__":
    main()
