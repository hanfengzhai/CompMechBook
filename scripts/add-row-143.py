#!/usr/bin/env python3
"""Add row 143 (Row 68 → Row 123 ↔ Row 63 orchestration meta prelude capstone on capstone path)."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def tx(s: str, pairs: list[tuple[str, str]]) -> str:
    for a, b in pairs:
        s = s.replace(a, b)
    return s


def extract_between(text: str, start: str, end: str) -> str:
    i = text.find(start)
    if i < 0:
        raise SystemExit(f"start marker not found: {start[:80]}")
    j = text.find(end, i + len(start))
    if j < 0:
        raise SystemExit(f"end marker not found after {start[:40]}")
    return text[i:j]


def lift_123_to_143(s: str) -> str:
    p = [
        ("Row 124 closing loop", "__ROW124_LOOP__"),
        ("Row 123 closing loop", "Row 143 closing loop"),
        ("row-124-closing-loop", "__ROW124_LOOP_ANCHOR__"),
        ("row-123-closing-loop", "row-143-closing-loop"),
        ("Row 124 closing stitch", "__ROW124_STITCH__"),
        ("Row 123 closing stitch", "Row 143 closing stitch"),
        ("row-124-closing-stitch", "__ROW124_STITCH_ANCHOR__"),
        ("row-123-closing-stitch", "row-143-closing-stitch"),
        ("prologue-preview-row-124", "__ROW124_PREVIEW__"),
        ("prologue-preview-row-123", "prologue-preview-row-143"),
        ("Row 124 preview", "__ROW124_PREVIEW_TEXT__"),
        ("Row 123 preview", "Row 143 preview"),
        ("Row 124 skill checkpoint", "__ROW124_SKILL__"),
        ("Row 123 skill checkpoint", "Row 143 skill checkpoint"),
        ("skill-navigation-row-124", "__ROW124_SKILL_NAV__"),
        ("skill-navigation-row-123", "skill-navigation-row-143"),
        ("memory sheet row 124", "__ROW124_MEM__"),
        ("memory sheet row 123", "memory sheet row 143"),
        ("Row 124 baby picture", "__ROW124_BABY__"),
        ("Row 123 baby picture", "Row 143 baby picture"),
        ("Row 124 three-way audit", "__ROW124_AUDIT__"),
        ("Row 123 three-way audit", "Row 143 three-way audit"),
        (
            "Row 68 → Row 103 Row 68 → Row 63 orchestration meta prelude capstone",
            "Row 68 → Row 123 Row 68 → Row 63 orchestration meta prelude capstone",
        ),
        (
            "row68-row103-orchestration-meta-prelude-capstone-reunion-index-row-123",
            "row68-row123-orchestration-meta-prelude-capstone-reunion-index-row-143",
        ),
        (
            "row-123-baby-picture-row68-row103-orchestration-meta-prelude-capstone-reunion",
            "row-143-baby-picture-row68-row123-orchestration-meta-prelude-capstone-reunion",
        ),
        ("[row 124]", "__ROW124_REF__"),
        ("[row 104]", "[row 124]"),
        ("row 104", "row 124"),
        ("Row 104", "Row 124"),
        ("__ROW124_REF__", "[row 124]"),
        ("[row 123]", "__ROW123_REF__"),
        ("[row 103]", "[row 123]"),
        ("row 103", "row 123"),
        ("Row 103", "Row 123"),
        ("__ROW123_REF__", "[row 123]"),
        ("[row 122]", "[row 142]"),
        ("row 122", "row 142"),
        ("Row 122", "Row 142"),
        ("(row 123)", "(row 143)"),
        ("__ROW124_LOOP__", "Row 124 closing loop"),
        ("__ROW124_LOOP_ANCHOR__", "row-124-closing-loop"),
        ("__ROW124_STITCH__", "Row 124 closing stitch"),
        ("__ROW124_STITCH_ANCHOR__", "row-124-closing-stitch"),
        ("__ROW124_PREVIEW__", "prologue-preview-row-124"),
        ("__ROW124_PREVIEW_TEXT__", "Row 124 preview"),
        ("__ROW124_SKILL__", "Row 124 skill checkpoint"),
        ("__ROW124_SKILL_NAV__", "skill-navigation-row-124"),
        ("__ROW124_MEM__", "memory sheet row 124"),
        ("__ROW124_BABY__", "Row 124 baby picture"),
        ("__ROW124_AUDIT__", "Row 124 three-way audit"),
        (
            "Handshake 4b meta prelude capstone / orchestration meta prelude hinge",
            "Handshake 4b meta prelude capstone / orchestration meta prelude hinge on the capstone path",
        ),
        (
            "at the orchestration meta prelude capstone boundary inside the coupling gate",
            "at the orchestration meta prelude capstone boundary inside the coupling gate on the capstone path",
        ),
        ("Row 68 ↔ Row 63 reunion |", "Row 68 ↔ Row 63 reunion (capstone path) |"),
        (
            "[Row 68 → Row 83 orchestration meta prelude reunion index (row 103)]",
            "[Row 68 → Row 123 orchestration meta prelude capstone reunion index (row 143)]",
        ),
        (
            "row68-row83-orchestration-meta-prelude-reunion-index-row-103",
            "row68-row123-orchestration-meta-prelude-capstone-reunion-index-row-143",
        ),
        (
            "verified Handshake 4b meta prelude capstone closure (row 122)",
            "verified Handshake 4b meta prelude capstone closure (row 142)",
        ),
        (
            "Row 68 → Row 63 meta (row 123)",
            "Row 68 → Row 63 meta (row 143)",
        ),
        (
            "before row 44 book loop opens in workflow time",
            "before row 44 book loop opens on the capstone path in workflow time",
        ),
        (
            "When row 123 is complete, proceed to [row 124]",
            "When row 143 is complete, proceed to [row 144](preface.md#skill-navigation-row-144) when row 68 closed but book-loop meta prelude still lags on the capstone path, "
            "to [row 124](preface.md#skill-navigation-row-124) when orchestration meta prelude capstone is clean but book-loop meta prelude still lags on the opening-hinge path, "
            "to [row 104](preface.md#skill-navigation-row-104) for the Row 68 ↔ Row 64 book-loop meta prelude audit alone, "
            "to [row 103](preface.md#skill-navigation-row-103) for the Row 68 ↔ Row 63 orchestration meta prelude audit on the opening-hinge path alone, "
            "to [row 142](preface.md#skill-navigation-row-142) when Handshake 4b meta prelude capstone still lags after verified Handshake 4a meta prelude capstone on the capstone path, "
            "to [row 83](preface.md#skill-navigation-row-83) for the Row 68 ↔ Row 63 opening prelude audit alone, "
            "to [row 63](preface.md#skill-navigation-row-63) when only orchestration meta stalls, "
            "or extend prose only under `writings/` then sync.\n\nDUPLICATE_WHEN_ROW_123",
        ),
        (
            "orchestration meta prelude capstone at the H1→OUT boundary in reading time",
            "orchestration meta prelude capstone at the H1→OUT boundary in reading time on the capstone path",
        ),
        (
            "When row 63 feels like epilogue homework after row 122 alone",
            "When row 63 feels like epilogue homework after row 142 alone on the capstone path",
        ),
        (
            "When row 63 feels like epilogue homework after row 142 alone",
            "When row 63 feels like epilogue homework after row 142 alone on the capstone path",
        ),
        ("Recite [preface row 122]", "Recite [preface row 142]"),
        (
            "Proceed to [row 124](#row-124-closing-loop) when row 68 closed but book-loop meta still feels disconnected after row 123",
            "Proceed to [row 144](#row-144-closing-loop) when row 68 closed but book-loop meta prelude still lags after row 143 on the capstone path, "
            "to [row 124](#row-124-closing-loop) when row 68 closed but book-loop meta still feels disconnected after row 123 on the opening-hinge path",
        ),
        (
            "when opening [row 124](preface.md#skill-navigation-row-124) before row 63 closes",
            "when opening [row 144](preface.md#skill-navigation-row-144) before row 64 closes on the capstone path",
        ),
        (
            "when individual export yamls are verified after row 122 but no orchestrated pedigree links them",
            "when individual export yamls are verified on the capstone path after row 142 but no orchestrated pedigree links them",
        ),
        (
            "when row 122 closed but row 63 orchestration meta still feels like epilogue homework",
            "when row 142 closed but row 63 orchestration meta still feels like epilogue homework",
        ),
        (
            "when row 122 and row 63 both verify individually",
            "when row 142 and row 63 both verify individually",
        ),
        (
            "rear-view mirror of row 122's Handshake 4b meta → notch",
            "rear-view mirror of row 142's Handshake 4b meta → notch",
        ),
        (
            "read row 68 gate + row 122 or row 103 Handshake 4b meta prelude capstone / orchestration meta prelude gate + epilogue orchestration cross-links + row 63 meta aloud when Handshakes 1–4b verify individually after Handshake 4b meta prelude capstone but Act V notch and Act VI foundation still feel like separate afternoons without orchestrated `multiscale_export.yaml`",
            "read row 68 gate + row 142 or row 123 Handshake 4b meta prelude capstone / orchestration meta prelude gate + epilogue orchestration cross-links + row 63 meta aloud when Handshakes 1–4b verify individually on the capstone path after Handshake 4b meta prelude capstone but Act V notch and Act VI foundation still feel like separate afternoons without orchestrated `multiscale_export.yaml`",
        ),
        (
            "before row 143 orchestration meta prelude capstone or row 63 workflow reunion opens on the capstone path",
            "before row 144 book-loop meta prelude capstone or row 64 workflow reunion opens on the capstone path",
        ),
        (
            "before row 124 book-loop meta prelude capstone opens",
            "before row 64 book-loop meta prelude opens on the capstone path",
        ),
    ]
    out = tx(s, p)
    if "DUPLICATE_WHEN_ROW_123" in out:
        out = re.sub(r"\n\nDUPLICATE_WHEN_ROW_123.*", "", out, flags=re.S)
    return out


def fix_row_142_tail(preface: str) -> str:
    old = (
        "When row 142 is complete, proceed to [row 143](preface.md#skill-navigation-row-143) when row 68 closed but orchestration meta prelude still lags on the capstone path, "
        "to [row 123](preface.md#skill-navigation-row-123) when Handshake 4b meta prelude capstone is clean but orchestration meta prelude still lags on the opening-hinge path, "
        "to [row 103](preface.md#skill-navigation-row-103) for the Row 68 ↔ Row 63 orchestration meta prelude audit alone, "
        "to [row 102](preface.md#skill-navigation-row-102) for the Row 68 ↔ Row 62 Handshake 4b meta prelude audit on the opening-hinge path alone, "
        "to [row 141](preface.md#skill-navigation-row-141) when Handshake 4a meta prelude capstone still lags after verified Handshake 4a meta capstone on the capstone path, "
        "to [row 62](preface.md#skill-navigation-row-62) when only Handshake 4b meta stalls, "
    )
    if old not in preface:
        return preface
    return preface.replace(old, old)  # already correct


def add_row_143() -> None:
    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    if "skill-navigation-row-143" in preface and "### Row 143 skill checkpoint" in preface:
        print("preface: row 143 already present")
    else:
        m123 = re.search(
            r"(### Row 123 skill checkpoint.*?)(?=\n### Row 124 skill checkpoint)",
            preface,
            re.S,
        )
        if not m123:
            raise SystemExit("row 123 preface checkpoint missing")
        row143 = lift_123_to_143(m123.group(1))
        anchor = "\n## The copper wire through the book"
        if "### Row 142 skill checkpoint" in preface:
            # Insert after row 142 block (before copper wire)
            idx = preface.find(anchor)
            if idx < 0:
                raise SystemExit("copper wire anchor missing")
            preface = preface[:idx] + "\n" + row143 + preface[idx:]
        else:
            preface = preface.replace(anchor, "\n" + row143 + anchor)
        preface_path.write_text(preface)
        print("preface: added row 143")

    ep_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    ep = ep_path.read_text()
    if "row-143-closing-loop" not in ep:
        block123 = extract_between(ep, "### Row 123 closing loop", "### Row 124 closing loop")
        block143 = lift_123_to_143(block123)
        ep = ep.replace("### Row 124 closing loop", block143 + "### Row 124 closing loop", 1)
        ep_path.write_text(ep)
        print("epilogue: added row 143 loop")

    pro_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    pro = pro_path.read_text()
    compass_line = (
        "| Row 68 → Row 123 Row 68 → Row 63 orchestration meta prelude capstone reunion (row 143) |"
    )
    if compass_line not in pro:
        line142 = (
            "| Row 68 → Row 122 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion (row 142) |"
        )
        idx142 = pro.find(line142)
        if idx142 < 0:
            raise SystemExit("prologue compass row 142 not found")
        line_end142 = pro.find("\n", idx142)
        line123 = (
            "| Row 68 → Row 103 Row 68 → Row 63 orchestration meta prelude capstone reunion (row 123) |"
        )
        idx123 = pro.find(line123)
        if idx123 < 0:
            raise SystemExit("prologue compass row 123 not found")
        line_end123 = pro.find("\n", idx123)
        compass143 = lift_123_to_143(pro[idx123:line_end123]) + "\n"
        pro = pro[: line_end142 + 1] + compass143 + pro[line_end142 + 1 :]
        preview123 = extract_between(
            pro,
            '| <span id="prologue-preview-row-123"></span>',
            '\n| <span id="prologue-preview-row-124">',
        )
        preview143 = lift_123_to_143(preview123)
        pro = pro.replace(
            '| <span id="prologue-preview-row-123"></span>',
            preview143 + '| <span id="prologue-preview-row-123"></span>',
            1,
        )
        if "row-143-closing-stitch" not in pro:
            stitch = (
                "**Row 143 closing stitch (Row 68 → Row 123 Row 68 → Row 63 orchestration meta prelude capstone reunion).** {#row-143-closing-stitch} "
                "When row 142 closed — Handshake 4b meta prelude capstone verified, row 141 or row 122 recited on the capstone path, and "
                "[`parse_fe2.sh`](../../scripts/parse_fe2.sh) archived `fe2_export.yaml` with enrichment when uplift exceeds 10% after verified Handshake 4b meta prelude capstone — "
                "but **row 63 orchestration meta reunion still opens like standalone epilogue coursework after the orchestration opening prelude chapter hinge on the capstone path** — "
                "the [preface row 143 When-to-pause opening sentence](../preface.md#skill-navigation-row-143) names the dual reunion before book-loop meta prelude reunion; "
                "read [preface row 143](../preface.md#skill-navigation-row-143), then the "
                "[Row 68 → Row 123 reunion index](../appendix/sources.md#row68-row123-orchestration-meta-prelude-capstone-reunion-index-row-143), then "
                "[epilogue row 143 closing loop](../epilogue/multiscale.md#row-143-closing-loop) before row 64 book-loop meta prelude opens on the capstone path.\n\n"
            )
            pro = pro.replace("**Row 124 closing stitch", stitch + "**Row 124 closing stitch", 1)
        pro_path.write_text(pro)
        print("prologue: added row 143 compass/preview/stitch")

    src_path = ROOT / "writings/appendix/chapters/sources.md"
    src = src_path.read_text()
    if "row68-row123-orchestration-meta-prelude-capstone-reunion-index-row-143" not in src:
        idx123 = src.find(
            "## Row 68 → Row 103 Row 68 → Row 63 orchestration meta prelude capstone reunion index (row 123)"
        )
        idx124 = src.find(
            "## Row 68 → Row 104 Row 68 → Row 64 book-loop meta prelude capstone reunion index (row 124)"
        )
        if idx123 < 0 or idx124 < 0:
            raise SystemExit("row 123/124 sources anchors missing")
        block = src[idx123:idx124]
        block143 = lift_123_to_143(block)
        table_row = (
            "| 143 | Row 68 → Row 123 Row 68 → Row 63 orchestration meta prelude capstone (midpoint prelude gate ↔ Handshake 4b meta prelude capstone ↔ row 63 meta) | "
            "[Row 68 → Row 123 orchestration meta prelude capstone reunion index](#row68-row123-orchestration-meta-prelude-capstone-reunion-index-row-143) · "
            "[preface row 143](../preface.md#skill-navigation-row-143) · "
            "[prologue row 143 preview](../prologue/00-many-scales.md#prologue-preview-row-143) · "
            "[prologue row 143 closing stitch](../prologue/00-many-scales.md#row-143-closing-stitch) · "
            "[epilogue row 143 closing loop](../epilogue/multiscale.md#row-143-closing-loop) · "
            "[memory sheet row 143 baby picture](memory-sheet.md#row-143-baby-picture-row68-row123-orchestration-meta-prelude-capstone-reunion) | "
            "Row 68 closed but **row 63 orchestration meta reunion still feels disconnected from verified Handshake 4b meta prelude capstone on the capstone path** — "
            "read row 68 + row 142 or row 123 gate + epilogue orchestration cross-links + row 63; "
            "[preface row 63](../preface.md#skill-navigation-row-63) |\n"
        )
        src = src.replace(
            "| 142 | Row 68 → Row 122 Row 68 → Row 62 Handshake 4b meta prelude capstone",
            table_row + "| 142 | Row 68 → Row 122 Row 68 → Row 62 Handshake 4b meta prelude capstone",
        )
        src = src.replace(
            "## Row 68 → Row 103 Row 68 → Row 63 orchestration meta prelude capstone reunion index (row 123)",
            block143
            + "## Row 68 → Row 103 Row 68 → Row 63 orchestration meta prelude capstone reunion index (row 123)",
        )
        extra = (
            "[row 143](#row68-row123-orchestration-meta-prelude-capstone-reunion-index-row-143) reunites **Handshake 4b meta prelude capstone with the orchestration meta prelude capstone boundary** "
            "when row 142 closed Handshake 4b meta prelude capstone at verified notch-root stress on the capstone path but epilogue orchestration cross-links and row 16 still read like separate courses after verified orchestration meta prelude meta;"
        )
        if extra not in src:
            needle = (
                "[row 142](#row68-row122-handshake4b-meta-prelude-capstone-reunion-index-row-142) reunites **Handshake 4a meta prelude capstone with the Handshake 4b meta prelude capstone boundary** "
                "when row 141 closed Handshake 4a meta prelude capstone at verified bulk hardening on the capstone path but epilogue FE² cross-links and Part VII Step 4 still read like separate courses after verified Handshake 4b meta prelude meta;"
            )
            if needle in src:
                src = src.replace(needle, needle + " " + extra)
        src_path.write_text(src)
        print("sources: added row 143 index")

    mem_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    mem = mem_path.read_text()
    if "row-143-baby-picture" not in mem:
        baby123 = extract_between(mem, "### Row 123 baby picture", "### Row 124 baby picture")
        baby143 = lift_123_to_143(baby123)
        mem = mem.replace("### Row 124 baby picture", baby143 + "### Row 124 baby picture", 1)
        mem_table = (
            "| 143 | Meta | Row 68 → Row 123 Row 68 → Row 63 orchestration meta prelude capstone reunion | "
            "[Row 68 → Row 123 orchestration meta prelude capstone reunion index](sources.md#row68-row123-orchestration-meta-prelude-capstone-reunion-index-row-143) · "
            "[preface row 143 skill checkpoint](../preface.md#skill-navigation-row-143) · "
            "[prologue row 143 preview](../prologue/00-many-scales.md#prologue-preview-row-143) · "
            "[prologue row 143 closing stitch](../prologue/00-many-scales.md#row-143-closing-stitch) · "
            "[epilogue row 143 closing loop](../epilogue/multiscale.md#row-143-closing-loop) | "
            "Row 68 closed but row 63 orchestration meta reunion feels disconnected from verified Handshake 4b meta prelude capstone on the capstone path — "
            "read row 68 + row 142 or row 123 gate + epilogue orchestration cross-links + row 63; "
            "[row 143 baby picture](#row-143-baby-picture-row68-row123-orchestration-meta-prelude-capstone-reunion) |\n"
        )
        mem = mem.replace(
            "[row-142-baby-picture-row68-row122-handshake4b-meta-prelude-capstone-reunion) |\n| 93 | Meta |",
            "[row-142-baby-picture-row68-row122-handshake4b-meta-prelude-capstone-reunion) |\n" + mem_table + "| 93 | Meta |",
        )
        if "When row 142 closed but orchestration meta prelude reunion still lags" not in mem:
            mem = mem.replace(
                "When row 141 closed but Handshake 4b meta prelude reunion still lags on the capstone path, switch to [row 142](#row-142-baby-picture-row68-row122-handshake4b-meta-prelude-capstone-reunion).",
                "When row 141 closed but Handshake 4b meta prelude reunion still lags on the capstone path, switch to [row 142](#row-142-baby-picture-row68-row122-handshake4b-meta-prelude-capstone-reunion). "
                "When row 142 closed but orchestration meta prelude reunion still lags on the capstone path, switch to [row 143](#row-143-baby-picture-row68-row123-orchestration-meta-prelude-capstone-reunion).",
            )
        mem_path.write_text(mem)
        print("memory-sheet: added row 143")
    else:
        print("memory-sheet: row 143 baby already present")


def main() -> None:
    add_row_143()


if __name__ == "__main__":
    main()
