#!/usr/bin/env python3
"""Add row 147 (Row 68 → Row 127 ↔ Row 67 part-boundary meta prelude capstone on capstone path)."""
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


def lift_107_to_127(s: str) -> str:
    """Promote opening-hinge row 107 sources index to capstone row 127 wording."""
    p = [
        (
            "Row 68 → Row 87 Row 68 → Row 67 part-boundary meta prelude reunion",
            "Row 68 → Row 107 Row 68 → Row 67 part-boundary meta prelude capstone reunion",
        ),
        (
            "row68-row87-part-boundary-meta-prelude-reunion-index-row-107",
            "row68-row107-part-boundary-meta-prelude-capstone-reunion-index-row-127",
        ),
        (
            "row-107-baby-picture-row68-row87-part-boundary-meta-prelude-reunion",
            "row-127-baby-picture-row68-row107-part-boundary-meta-prelude-capstone-reunion",
        ),
        ("Row 107 names", "Row 127 names"),
        ("Row 107 does not replace", "Row 127 does not replace"),
        ("(row 107)", "(row 127)"),
        ("skill-navigation-row-107", "skill-navigation-row-127"),
        ("preface row 107", "preface row 127"),
        ("Preface row 107", "Preface row 127"),
        ("memory sheet row 107", "memory sheet row 127"),
        ("Row 107 baby picture", "Row 127 baby picture"),
        ("row 106 verified", "row 126 verified"),
        ("row 106's canonical-tree", "row 126's canonical-tree"),
        ("row 106's canonical-tree", "row 126's canonical-tree"),
        ("[row 106]", "__ROW106_REF__"),
        ("row 106", "row 126"),
        ("Row 106", "Row 126"),
        ("__ROW106_REF__", "[row 126]"),
        (
            "part-boundary meta capstone boundary",
            "part-boundary meta prelude capstone boundary inside the coupling gate on the capstone path",
        ),
        (
            "Writings canonical meta capstone / part-boundary opening prelude",
            "Writings canonical meta prelude capstone / part-boundary meta prelude",
        ),
    ]
    return tx(s, p)


def lift_127_to_147(s: str) -> str:
    p = [
        ("Row 128 closing loop", "__ROW128_LOOP__"),
        ("Row 127 closing loop", "Row 147 closing loop"),
        ("row-128-closing-loop", "__ROW128_LOOP_ANCHOR__"),
        ("row-127-closing-loop", "row-147-closing-loop"),
        ("Row 128 closing stitch", "__ROW128_STITCH__"),
        ("Row 127 closing stitch", "Row 147 closing stitch"),
        ("row-128-closing-stitch", "__ROW128_STITCH_ANCHOR__"),
        ("row-127-closing-stitch", "row-147-closing-stitch"),
        ("prologue-preview-row-128", "__ROW128_PREVIEW__"),
        ("prologue-preview-row-127", "prologue-preview-row-147"),
        ("Row 128 preview", "__ROW128_PREVIEW_TEXT__"),
        ("Row 127 preview", "Row 147 preview"),
        ("Row 128 skill checkpoint", "__ROW128_SKILL__"),
        ("Row 127 skill checkpoint", "Row 147 skill checkpoint"),
        ("skill-navigation-row-128", "__ROW128_SKILL_NAV__"),
        ("skill-navigation-row-127", "skill-navigation-row-147"),
        ("memory sheet row 128", "__ROW128_MEM__"),
        ("memory sheet row 127", "memory sheet row 147"),
        ("Row 128 baby picture", "__ROW128_BABY__"),
        ("Row 127 baby picture", "Row 147 baby picture"),
        ("Row 128 three-way audit", "__ROW128_AUDIT__"),
        ("Row 127 three-way audit", "Row 147 three-way audit"),
        (
            "Row 68 → Row 107 Row 68 → Row 67 part-boundary meta prelude capstone",
            "Row 68 → Row 127 Row 68 → Row 67 part-boundary meta prelude capstone",
        ),
        (
            "row68-row107-part-boundary-meta-prelude-capstone-reunion-index-row-127",
            "row68-row127-part-boundary-meta-prelude-capstone-reunion-index-row-147",
        ),
        (
            "row-127-baby-picture-row68-row107-part-boundary-meta-prelude-capstone-reunion",
            "row-147-baby-picture-row68-row127-part-boundary-meta-prelude-capstone-reunion",
        ),
        ("[row 128]", "__ROW128_REF__"),
        ("[row 108]", "[row 128]"),
        ("row 108", "row 128"),
        ("Row 108", "Row 128"),
        ("__ROW128_REF__", "[row 128]"),
        ("[row 127]", "__ROW127_REF__"),
        ("[row 107]", "[row 127]"),
        ("row 107", "row 127"),
        ("Row 107", "Row 127"),
        ("__ROW127_REF__", "[row 127]"),
        ("[row 126]", "__ROW126_REF__"),
        ("__ROW126_REF__", "[row 146]"),
        ("skill-navigation-row-126", "skill-navigation-row-146"),
        (
            "Row 68 → Row 87 part-boundary meta prelude reunion index (row 147)",
            "Row 68 → Row 127 part-boundary meta prelude capstone reunion index (row 147)",
        ),
        (
            "row68-row87-part-boundary-meta-prelude-reunion-index-row-107",
            "row68-row127-part-boundary-meta-prelude-capstone-reunion-index-row-147",
        ),
        ("when sync is clean after row 126 but", "when sync is clean after row 146 but"),
        ("memory sheet row 127 baby picture", "memory sheet row 147 baby picture"),
        ("prologue row 127 closing stitch", "prologue row 147 closing stitch"),
        ("prologue row 127 preview", "prologue row 147 preview"),
        ("Row 127 three-way audit", "Row 147 three-way audit"),
        ("Row 127 closes the", "Row 147 closes the"),
        ("Row 127 does not conflate", "Row 147 does not conflate"),
        ("(row 127)", "(row 147)"),
        ("__ROW128_LOOP__", "Row 128 closing loop"),
        ("__ROW128_LOOP_ANCHOR__", "row-128-closing-loop"),
        ("__ROW128_STITCH__", "Row 128 closing stitch"),
        ("__ROW128_STITCH_ANCHOR__", "row-128-closing-stitch"),
        ("__ROW128_PREVIEW__", "prologue-preview-row-128"),
        ("__ROW128_PREVIEW_TEXT__", "Row 128 preview"),
        ("__ROW128_SKILL__", "Row 128 skill checkpoint"),
        ("__ROW128_SKILL_NAV__", "skill-navigation-row-128"),
        ("__ROW128_MEM__", "memory sheet row 128"),
        ("__ROW128_BABY__", "Row 128 baby picture"),
        ("__ROW128_AUDIT__", "Row 128 three-way audit"),
        (
            "verified Writings canonical meta prelude capstone closure (row 126)",
            "verified Writings canonical meta prelude capstone closure (row 146)",
        ),
        ("When row 126 closed", "When row 146 closed"),
        ("after row 126 alone", "after row 146 alone"),
        ("Recite [preface row 126]", "Recite [preface row 146]"),
        (
            "when row 126 closed but row 67 part-boundary meta still feels like elasticity homework disconnected from verified Writings canonical meta prelude capstone on the capstone path",
            "when row 146 closed but row 67 part-boundary meta still feels like elasticity homework disconnected from verified Writings canonical meta prelude capstone on the capstone path",
        ),
        (
            "when row 126 and row 67 both verify individually",
            "when row 146 and row 67 both verify individually",
        ),
        (
            "rear-view mirror of row 126's canonical-tree → twin-ladder turn",
            "rear-view mirror of row 146's canonical-tree → twin-ladder turn",
        ),
        (
            "read row 68 gate + row 126 or row 107 Writings meta prelude capstone / part-boundary meta prelude gate + V.4 Bridge → VI.0 twin-ladder landing + row 67 meta aloud when canonical tree is clean on the capstone path but writings/fvm → writings/continuum feels like two courses after verified Writings meta prelude capstone",
            "read row 68 gate + row 146 or row 127 Writings meta prelude capstone / part-boundary meta prelude gate + V.4 Bridge → VI.0 twin-ladder landing + row 67 meta aloud when canonical tree is clean on the capstone path after verified Writings meta prelude capstone but writings/fvm → writings/continuum feels like two courses",
        ),
        (
            "Confirm [row 126](preface.md#skill-navigation-row-126) or [Row 68 → Row 87 part-boundary meta prelude reunion index (row 107)](appendix/sources.md#row68-row87-part-boundary-meta-prelude-reunion-index-row-107) recited",
            "Confirm [row 146](preface.md#skill-navigation-row-146) or [Row 68 → Row 127 part-boundary meta prelude capstone reunion index (row 147)](appendix/sources.md#row68-row127-part-boundary-meta-prelude-capstone-reunion-index-row-147) recited",
        ),
        (
            "Row 127 does not replace row 68, row 67, row 126, row 107, row 87, row 66, row 47, or row 30",
            "Row 147 does not replace row 68, row 67, row 146, row 127, row 87, row 66, row 47, or row 30",
        ),
        (
            "[row 126](preface.md#skill-navigation-row-126) or [row 107](preface.md#skill-navigation-row-107)",
            "[row 146](preface.md#skill-navigation-row-146) or [row 127](preface.md#skill-navigation-row-127)",
        ),
        (
            "When row 127 is complete, proceed to [row 128]",
            "When row 147 is complete, proceed to [row 128](preface.md#skill-navigation-row-128) when row 68 closed but midpoint meta prelude capstone still lags after verified part-boundary meta prelude capstone on the capstone path, "
            "to [row 127](preface.md#skill-navigation-row-127) when Writings canonical meta prelude capstone is clean but part-boundary meta prelude still lags on the opening-hinge path, "
            "to [row 107](preface.md#skill-navigation-row-107) for the Row 68 ↔ Row 67 meta audit on the opening-hinge prelude path alone, "
            "to [row 146](preface.md#skill-navigation-row-146) when Writings canonical meta prelude capstone still lags after verified second-pass meta prelude capstone on the capstone path, "
            "to [row 87](preface.md#skill-navigation-row-87) for the Row 68 ↔ Row 67 opening prelude audit alone, "
            "to [row 67](preface.md#skill-navigation-row-67) when only part-boundary prelude meta stalls, "
            "to [row 47](preface.md#skill-navigation-row-47) when only the fvm → continuum boundary stalls, "
            "or extend prose only under `writings/` then sync.\n\nDUPLICATE_WHEN_ROW_127",
        ),
        (
            "Proceed to [row 128](#row-128-closing-loop) when row 68 closed but midpoint meta prelude capstone still lags after row 127 on the capstone path",
            "Proceed to [row 128](#row-128-closing-loop) when row 68 closed but midpoint meta prelude capstone still lags after row 147 on the capstone path, "
            "to [row 127](#row-127-closing-loop) when row 68 closed but midpoint meta prelude capstone still lags after verified part-boundary meta prelude capstone on the opening-hinge path",
        ),
        (
            "when opening [row 128](preface.md#skill-navigation-row-128) before row 48 closes on the capstone path",
            "when opening [row 128](preface.md#skill-navigation-row-128) before row 48 closes on the capstone path",
        ),
        (
            "When row 67 feels like elasticity homework after row 126 alone on the capstone path",
            "When row 67 feels like elasticity homework after row 146 alone on the capstone path",
        ),
        (
            "row 127 (row 68 ↔ row 67 reunion on the capstone path) with row 107",
            "row 147 (row 68 ↔ row 67 reunion on the capstone path) with row 127",
        ),
        (
            "row 127 (row 68 ↔ row 67 reunion on the capstone path) with row 107 (opening-hinge prelude stitch alone)",
            "row 147 (row 68 ↔ row 67 reunion on the capstone path) with row 127 (opening-hinge prelude stitch alone)",
        ),
        (
            "row 127 names **why that reunion must follow verified Writings canonical meta prelude capstone (row 126)",
            "row 147 names **why that reunion must follow verified Writings canonical meta prelude capstone (row 146)",
        ),
    ]
    out = tx(s, p)
    if "DUPLICATE_WHEN_ROW_127" in out:
        out = re.sub(r"\n\nDUPLICATE_WHEN_ROW_127.*", "", out, flags=re.S)
    return out


def add_row_147() -> None:
    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    if "skill-navigation-row-147" in preface and "### Row 147 skill checkpoint" in preface:
        print("preface: row 147 already present")
    else:
        m127 = re.search(
            r"(### Row 127 skill checkpoint.*?)(?=\n### Row 128 skill checkpoint)",
            preface,
            re.S,
        )
        if not m127:
            raise SystemExit("row 127 preface checkpoint missing")
        row147 = lift_127_to_147(m127.group(1))
        anchor = "\n## The copper wire through the book"
        idx = preface.find(anchor)
        if idx < 0:
            raise SystemExit("copper wire anchor missing")
        preface = preface[:idx] + "\n" + row147 + preface[idx:]
        preface_path.write_text(preface)
        print("preface: added row 147")

    ep_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    ep = ep_path.read_text()
    if "row-147-closing-loop" not in ep:
        block127 = extract_between(ep, "### Row 127 closing loop", "### Row 131 closing loop")
        block147 = lift_127_to_147(block127)
        ep = ep.replace("### Row 146 closing loop", block147 + "### Row 146 closing loop", 1)
        ep_path.write_text(ep)
        print("epilogue: added row 147 loop")

    pro_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    pro = pro_path.read_text()
    compass_line = (
        "| Row 68 → Row 127 Row 68 → Row 67 part-boundary meta prelude capstone reunion (row 147) |"
    )
    if compass_line not in pro:
        line146 = (
            "| Row 68 → Row 126 Row 68 → Row 66 Writings canonical meta prelude capstone reunion (row 146) |"
        )
        idx146 = pro.find(line146)
        if idx146 < 0:
            raise SystemExit("prologue compass row 146 not found")
        line_end146 = pro.find("\n", idx146)
        line127 = (
            "| Row 68 → Row 107 Row 68 → Row 67 part-boundary meta prelude capstone reunion (row 127) |"
        )
        idx127 = pro.find(line127)
        if idx127 < 0:
            raise SystemExit("prologue compass row 127 not found")
        line_end127 = pro.find("\n", idx127)
        compass147 = lift_127_to_147(pro[idx127:line_end127]) + "\n"
        pro = pro[: line_end146 + 1] + compass147 + pro[line_end146 + 1 :]
        preview127 = extract_between(
            pro,
            '| <span id="prologue-preview-row-127"></span>',
            '\n| <span id="prologue-preview-row-136"></span>',
        )
        preview147 = lift_127_to_147(preview127)
        pro = pro.replace(
            '| <span id="prologue-preview-row-127"></span>',
            preview147 + '| <span id="prologue-preview-row-127"></span>',
            1,
        )
        if "row-147-closing-stitch" not in pro:
            stitch = (
                "**Row 146 closing stitch (Row 68 → Row 126 Row 68 → Row 66 Writings canonical meta prelude capstone reunion).** {#row-147-closing-stitch} "
                "When row 146 closed — Writings canonical meta prelude capstone verified, row 145 or row 126 recited on the capstone path, and `./scripts/sync-writings.sh --check` green with prose under `writings/` only — "
                "but **row 67 part-boundary meta reunion still opens like standalone elasticity coursework after Navier–Stokes on the capstone path** — "
                "the [preface row 146 When-to-pause opening sentence](../preface.md#skill-navigation-row-147) names the dual reunion before midpoint meta prelude reunion; "
                "read [preface row 146](../preface.md#skill-navigation-row-147), then the "
                "[Row 68 → Row 127 reunion index](../appendix/sources.md#row68-row127-part-boundary-meta-prelude-capstone-reunion-index-row-147), then "
                "[epilogue row 146 closing loop](../epilogue/multiscale.md#row-147-closing-loop) before row 48 midpoint meta prelude opens on the capstone path.\n\n"
            )
            pro = pro.replace("**Row 127 closing stitch", stitch + "**Row 127 closing stitch", 1)
        pro_path.write_text(pro)
        print("prologue: added row 147 compass/preview/stitch")

    src_path = ROOT / "writings/appendix/chapters/sources.md"
    src = src_path.read_text()
    if "row68-row127-part-boundary-meta-prelude-capstone-reunion-index-row-147" not in src:
        block107 = extract_between(
            src,
            "## Row 68 → Row 87 Row 68 → Row 67 part-boundary meta prelude reunion index (row 107)",
            "## Row 68 → Row 88 Row 68 → Row 48 midpoint meta prelude reunion index (row 108)",
        )
        block147 = lift_127_to_147(lift_107_to_127(block107))
        table_row = (
            "| 147 | Row 68 → Row 127 Row 68 → Row 67 part-boundary meta prelude capstone (midpoint prelude gate ↔ Writings meta prelude capstone ↔ row 67 meta) | "
            "[Row 68 → Row 127 part-boundary meta prelude capstone reunion index](#row68-row127-part-boundary-meta-prelude-capstone-reunion-index-row-147) · "
            "[preface row 147](../preface.md#skill-navigation-row-147) · "
            "[prologue row 147 preview](../prologue/00-many-scales.md#prologue-preview-row-147) · "
            "[prologue row 147 closing stitch](../prologue/00-many-scales.md#row-147-closing-stitch) · "
            "[epilogue row 147 closing loop](../epilogue/multiscale.md#row-147-closing-loop) · "
            "[memory sheet row 147 baby picture](memory-sheet.md#row-147-baby-picture-row68-row127-part-boundary-meta-prelude-capstone-reunion) | "
            "Row 68 closed but **row 67 part-boundary meta reunion still feels disconnected from verified Writings canonical meta prelude capstone on the capstone path** — "
            "read row 68 + row 146 or row 127 gate + V.4 Bridge → VI.0 twin-ladder + row 67; "
            "[preface row 67](../preface.md#skill-navigation-row-67) |\n"
        )
        src = src.replace(
            "| 146 | Row 68 → Row 126 Row 68 → Row 66 Writings canonical meta prelude capstone",
            table_row + "| 146 | Row 68 → Row 126 Row 68 → Row 66 Writings canonical meta prelude capstone",
        )
        src = src.replace(
            "## Row 68 → Row 126 Row 68 → Row 66 Writings canonical meta prelude capstone reunion index (row 146)",
            block147 + "## Row 68 → Row 126 Row 68 → Row 66 Writings canonical meta prelude capstone reunion index (row 146)",
        )
        extra = (
            "[row 146](#row68-row127-part-boundary-meta-prelude-capstone-reunion-index-row-147) reunites **Writings canonical meta prelude capstone with the part-boundary meta prelude capstone boundary** "
            "when row 146 closed Writings canonical meta prelude capstone at verified single-manuscript-tree rhythm on the capstone path but twin-ladder Bridge and row 67 still read like separate courses after verified fvm → continuum meta;"
        )
        if extra not in src:
            needle = (
                "[row 145](#row68-row126-writings-meta-prelude-capstone-reunion-index-row-146) reunites **book-loop meta prelude capstone with the second-pass meta prelude capstone boundary** "
            )
            if needle in src:
                src = src.replace(needle, needle + " " + extra)
        src_path.write_text(src)
        print("sources: added row 147 index")

    mem_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    mem = mem_path.read_text()
    if "row-147-baby-picture" not in mem:
        baby127 = extract_between(mem, "### Row 127 baby picture", "### Row 128 baby picture")
        baby147 = lift_127_to_147(baby127)
        mem = mem.replace("### Row 127 baby picture", baby147 + "### Row 127 baby picture", 1)
        mem_table = (
            "| 147 | Meta | Row 68 → Row 127 Row 68 → Row 67 part-boundary meta prelude capstone reunion | "
            "[Row 68 → Row 127 part-boundary meta prelude capstone reunion index](sources.md#row68-row127-part-boundary-meta-prelude-capstone-reunion-index-row-147) · "
            "[preface row 147 skill checkpoint](../preface.md#skill-navigation-row-147) · "
            "[prologue row 147 preview](../prologue/00-many-scales.md#prologue-preview-row-147) · "
            "[prologue row 147 closing stitch](../prologue/00-many-scales.md#row-147-closing-stitch) · "
            "[epilogue row 147 closing loop](../epilogue/multiscale.md#row-147-closing-loop) | "
            "Row 68 closed but row 67 part-boundary meta reunion feels disconnected from verified Writings meta prelude capstone on the capstone path — "
            "read row 68 + row 146 or row 127 gate + twin-ladder Bridge + row 67; "
            "[row 147 baby picture](#row-147-baby-picture-row68-row127-part-boundary-meta-prelude-capstone-reunion) |\n"
        )
        mem = mem.replace(
            "| 127 | Meta | Row 68 → Row 107 Row 68 → Row 67 part-boundary meta prelude capstone reunion |",
            mem_table + "| 127 | Meta | Row 68 → Row 107 Row 68 → Row 67 part-boundary meta prelude capstone reunion |",
        )
        if "When row 146 closed but twin-ladder reunion still lags" not in mem:
            mem = mem.replace(
                "When row 145 closed but canonical tree discipline still lags on the capstone path, switch to [row 146](#row-146-baby-picture-row68-row126-writings-meta-prelude-capstone-reunion).",
                "When row 145 closed but canonical tree discipline still lags on the capstone path, switch to [row 146](#row-146-baby-picture-row68-row126-writings-meta-prelude-capstone-reunion). "
                "When row 146 closed but twin-ladder reunion still lags on the capstone path, switch to [row 147](#row-147-baby-picture-row68-row127-part-boundary-meta-prelude-capstone-reunion).",
            )
        mem_path.write_text(mem)
        print("memory-sheet: added row 147")
    else:
        print("memory-sheet: row 147 baby already present")


def main() -> None:
    add_row_147()


if __name__ == "__main__":
    main()
