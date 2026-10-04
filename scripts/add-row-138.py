#!/usr/bin/env python3
"""Add row 138 (Row 68 → Row 118 ↔ Row 58 DFT workflows meta capstone on capstone path)."""
from __future__ import annotations

import re
import sys
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


def lift_118_to_138(s: str) -> str:
    p = [
        ("Row 118 closing loop", "Row 138 closing loop"),
        ("row-118-closing-loop", "row-138-closing-loop"),
        ("Row 118 closing stitch", "Row 138 closing stitch"),
        ("row-118-closing-stitch", "row-138-closing-stitch"),
        ("prologue-preview-row-118", "prologue-preview-row-138"),
        ("Row 118 preview", "Row 138 preview"),
        ("Row 118 skill checkpoint", "Row 138 skill checkpoint"),
        ("skill-navigation-row-118", "skill-navigation-row-138"),
        ("memory sheet row 118", "memory sheet row 138"),
        ("Row 118 baby picture", "Row 138 baby picture"),
        ("Row 118 three-way audit", "Row 138 three-way audit"),
        (
            "Row 68 → Row 98 Row 68 → Row 58 DFT workflows meta capstone",
            "Row 68 → Row 118 Row 68 → Row 58 DFT workflows meta capstone",
        ),
        (
            "row68-row98-dft-workflows-meta-capstone-reunion-index-row-118",
            "row68-row118-dft-workflows-meta-capstone-reunion-index-row-138",
        ),
        (
            "row-118-baby-picture-row68-row98-dft-workflows-meta-capstone-reunion",
            "row-138-baby-picture-row68-row118-dft-workflows-meta-capstone-reunion",
        ),
        ("(row 118)", "(row 138)"),
        ("row 118", "row 138"),
        ("[row 117]", "[row 137]"),
        ("row 117", "row 137"),
        ("Row 117", "Row 137"),
        ("[row 98]", "[row 118]"),
        ("row 98", "row 118"),
        ("Row 98", "Row 118"),
        (
            "Kohn–Sham meta capstone / DFT workflows opening prelude hinge",
            "Kohn–Sham meta capstone / DFT workflows opening prelude hinge on the capstone path",
        ),
        (
            "after IX.2's cutoff-sweep Lab act**",
            "after IX.2's cutoff-sweep Lab act on the capstone path**",
        ),
        (
            "at the DFT workflows meta capstone boundary inside Part IX",
            "at the DFT workflows meta capstone boundary inside the coupling gate on the capstone path",
        ),
        ("Row 68 ↔ Row 58 reunion |", "Row 68 ↔ Row 58 reunion (capstone path) |"),
        (
            "[Row 68 → Row 78 DFT workflows meta prelude reunion index (row 98)]",
            "[Row 68 → Row 98 DFT workflows meta capstone reunion index (row 118)]",
        ),
        (
            "row68-row78-dft-workflows-meta-prelude-reunion-index-row-98",
            "row68-row98-dft-workflows-meta-capstone-reunion-index-row-118",
        ),
        (
            "before row 119 Handshake 3 meta prelude opens at \\(T_w\\)",
            "before row 59 Handshake 3 meta prelude opens on the capstone path at \\(T_w\\)",
        ),
        (
            "row 137 closed but row 58",
            "row 137 closed but row 58",
        ),
        (
            "when `cutoff_convergence.yaml` exists but `cu.foundation/` is missing after row 117",
            "when `cutoff_convergence.yaml` exists on the capstone path but `cu.foundation/` is missing after row 137",
        ),
        ("when row 137 and row 58", "when row 137 and row 58"),
        (
            "before row 58 closes",
            "before row 59 closes on the capstone path",
        ),
        (
            "When row 118 is complete, proceed to [row 119]",
            "When row 138 is complete, proceed to [row 139](preface.md#skill-navigation-row-139) when `foundation_export.yaml` exists on the capstone path but Handshake 3 still lags, to [row 119](preface.md#skill-navigation-row-119) when DFT workflows meta capstone is clean but Handshake 3 meta capstone still lags on the opening-hinge path, to [row 99](preface.md#skill-navigation-row-99) for the Row 68 ↔ Row 59 Handshake 3 opening prelude audit alone, to [row 118](preface.md#skill-navigation-row-118) for the Row 68 ↔ Row 58 DFT workflows meta audit on the opening-hinge path alone, to [row 137](preface.md#skill-navigation-row-137) when Kohn–Sham meta capstone still lags after verified Born–Oppenheimer meta capstone on the capstone path, to [row 58](preface.md#skill-navigation-row-58) when only IX.2 → IX.3 stalls, or extend prose only under `writings/` then sync.\n\nDUPLICATE_WHEN_ROW_118",
        ),
        (
            "DFT workflows meta capstone at the cutoff certificate → foundation archive chapter boundary in reading time",
            "DFT workflows meta capstone at the cutoff certificate → foundation archive chapter boundary in reading time on the capstone path",
        ),
        (
            "row 137 closed Kohn–Sham meta capstone",
            "row 137 closed Kohn–Sham meta capstone",
        ),
        (
            "verified Kohn–Sham meta capstone closure (row 117)",
            "verified Kohn–Sham meta capstone closure (row 137)",
        ),
        (
            "Row 68 → Row 58 meta (row 118)",
            "Row 68 → Row 58 meta (row 138)",
        ),
        (
            "before row 119 Handshake 3 meta capstone opens in workflow time",
            "before row 59 Handshake 3 meta prelude opens on the capstone path in workflow time",
        ),
        (
            "When row 58 feels like DFT coursework after row 117 alone",
            "When row 58 feels like DFT coursework after row 137 alone on the capstone path",
        ),
        ("Recite [preface row 117]", "Recite [preface row 137]"),
        (
            "Do not conflate row 118 (row 68 ↔ row 58 reunion",
            "Do not conflate row 138 (row 68 ↔ row 58 reunion on the capstone path",
        ),
        (
            "row 118 names **Row 68 → Row 78",
            "row 138 names **why that reunion must follow verified Kohn–Sham meta capstone (row 137) and the outer midpoint prelude gate (row 68)**; row 118 names **Row 68 → Row 78",
        ),
        (
            "Proceed to [row 119](#row-119-closing-loop) when row 68 closed but Handshake 3 meta capstone still lags after row 118",
            "Proceed to [row 139](#row-139-closing-loop) when row 68 closed but Handshake 3 meta capstone still lags after row 138 on the capstone path, to [row 119](#row-119-closing-loop) when row 68 closed but Handshake 3 meta capstone still lags after row 118 on the opening-hinge path, to [row 118](#row-118-closing-loop) for the Row 68 ↔ Row 58 DFT workflows meta audit on the opening-hinge path alone, to [row 137](#row-137-closing-loop) when Kohn–Sham meta capstone still lags after row 136 on the capstone path, to [row 58](#row-58-closing-loop) when only IX.2 → IX.3 stalls",
        ),
        ("Kohn–Sham meta row 117", "Kohn–Sham meta row 137"),
        (
            "row 117 when **IX.1 → IX.2 must reunite",
            "row 137 when **IX.1 → IX.2 must reunite",
        ),
        (
            "row 118 when **cutoff export manifest",
            "row 138 when **cutoff export manifest",
        ),
        (
            "before row 119 Handshake 3 meta capstone or row 99 prelude opens",
            "before row 139 Handshake 3 meta capstone or row 59 workflow reunion opens on the capstone path",
        ),
        (
            "when cutoff certificates are clean but DFT workflows still feel like standalone coursework after verified Kohn–Sham meta capstone |",
            "when cutoff certificates are clean on the capstone path but DFT workflows still feel like standalone coursework after verified Kohn–Sham meta capstone |",
        ),
        (
            "read row 68 gate + row 137 or row 118 Kohn–Sham meta capstone / DFT workflows opening gate + IX.2 Bridge → opening hinge → IX.3 calculation ladder + row 58 meta aloud when cutoff certificates are clean but DFT workflows still feel like standalone coursework after verified Kohn–Sham meta capstone",
            "read row 68 gate + row 137 or row 118 Kohn–Sham meta capstone / DFT workflows opening gate + IX.2 Bridge → opening hinge → IX.3 calculation ladder + row 58 meta aloud when cutoff certificates are clean on the capstone path but DFT workflows still feel like standalone coursework after verified Kohn–Sham meta capstone",
        ),
        (
            "when opening [row 119](preface.md#skill-navigation-row-119) before row 58 closes",
            "when opening [row 139](preface.md#skill-navigation-row-139) before row 59 closes on the capstone path",
        ),
    ]
    out = tx(s, p)
    if "DUPLICATE_WHEN_ROW_118" in out:
        out = re.sub(r"\n\nDUPLICATE_WHEN_ROW_118.*", "", out, flags=re.S)
    return out


def fix_row_137_tail(preface: str) -> str:
    old = (
        "When row 137 is complete, proceed to [row 118](preface.md#skill-navigation-row-118) when `cutoff_convergence.yaml` exists but IX.3 still feels disconnected from verified Kohn–Sham meta capstone, to [row 98](preface.md#skill-navigation-row-98) for the Row 68 ↔ Row 58 DFT workflows opening prelude audit alone, to [row 117](preface.md#skill-navigation-row-117) for the Row 68 ↔ Row 57 Kohn–Sham opening prelude audit alone, to [row 77](preface.md#skill-navigation-row-77) for the Row 68 ↔ Row 57 prelude audit alone, to [row 136](preface.md#skill-navigation-row-136) when Born–Oppenheimer meta capstone still lags after verified electronic audit meta capstone, to [row 57](preface.md#skill-navigation-row-57) when only IX.1 → IX.2 stalls, or extend prose only under `writings/` then sync."
    )
    new = (
        "When row 137 is complete, proceed to [row 138](preface.md#skill-navigation-row-138) when cutoff certificates exist on the capstone path but IX.3 still lags, to [row 118](preface.md#skill-navigation-row-118) when Kohn–Sham meta capstone is clean but DFT workflows meta capstone still lags on the opening-hinge path, to [row 98](preface.md#skill-navigation-row-98) for the Row 68 ↔ Row 58 DFT workflows opening prelude audit alone, to [row 117](preface.md#skill-navigation-row-117) for the Row 68 ↔ Row 57 Kohn–Sham meta audit on the opening-hinge path alone, to [row 136](preface.md#skill-navigation-row-136) when Born–Oppenheimer meta capstone still lags after verified electronic audit meta prelude capstone on the capstone path, to [row 57](preface.md#skill-navigation-row-57) when only IX.1 → IX.2 stalls, or extend prose only under `writings/` then sync."
    )
    if old in preface:
        preface = preface.replace(old, new)
    return preface


def fix_row_137_baby(mem: str) -> str:
    """Correct row 116/97 → row 136/117 in row 137 baby picture body."""
    reps = [
        ("row 116 or row 97 closed Born–Oppenheimer", "row 136 or row 117 closed Born–Oppenheimer"),
        ("[preface row 116]", "[preface row 136]"),
        ("[preface row 97]", "[preface row 117]"),
        ("Born–Oppenheimer meta row 116", "Born–Oppenheimer meta row 136"),
        ("When row 137 feels disconnected from row 116", "When row 137 feels disconnected from row 136"),
        ("Row 68 → Row 137 Row 68 → Row 57", "Row 68 → Row 117 Row 68 → Row 57"),
    ]
    for a, b in reps:
        mem = mem.replace(a, b)
    return mem


def add_row_138() -> None:
    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    preface = fix_row_137_tail(preface)
    if "skill-navigation-row-138" in preface and "### Row 138 skill checkpoint" in preface:
        print("preface: row 138 already present")
    else:
        m118 = re.search(
            r"(### Row 118 skill checkpoint.*?)(?=\n### Row 119 skill checkpoint)",
            preface,
            re.S,
        )
        if not m118:
            raise SystemExit("row 118 preface checkpoint missing")
        row138 = lift_118_to_138(m118.group(1))
        anchor = "\n## The copper wire through the book"
        preface = preface.replace(anchor, "\n" + row138 + anchor)
        preface_path.write_text(preface)
        print("preface: added row 138")

    ep_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    ep = ep_path.read_text()
    if "row-138-closing-loop" not in ep:
        block118 = extract_between(ep, "### Row 118 closing loop", "### Row 119 closing loop")
        block138 = lift_118_to_138(block118)
        ep = ep.replace("### Row 119 closing loop", block138 + "### Row 119 closing loop", 1)
        ep = ep.replace(
            "Proceed to [row 137](#row-137-closing-loop) when row 68 closed but Kohn–Sham meta capstone still lags after row 136 on the capstone path, to [row 136](#row-136-closing-loop) when row 68 closed but Born–Oppenheimer meta capstone still lags after row 135 on the capstone path,",
            "Proceed to [row 138](#row-138-closing-loop) when row 68 closed but DFT workflows meta capstone still lags after row 137 on the capstone path, to [row 137](#row-137-closing-loop) when row 68 closed but Kohn–Sham meta capstone still lags after row 136 on the capstone path, to [row 136](#row-136-closing-loop) when row 68 closed but Born–Oppenheimer meta capstone still lags after row 135 on the capstone path,",
            1,
        )
        ep_path.write_text(ep)
        print("epilogue: added row 138 loop")

    pro_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    pro = pro_path.read_text()
    if "| Row 68 → Row 118 Row 68 → Row 58 DFT workflows meta capstone reunion (row 138) |" not in pro:
        line118 = "| Row 68 → Row 98 Row 68 → Row 58 DFT workflows meta capstone reunion (row 118) |"
        idx118 = pro.find(line118)
        if idx118 < 0:
            raise SystemExit("prologue compass row 118 not found")
        line_end118 = pro.find("\n", idx118)
        compass138 = lift_118_to_138(pro[idx118:line_end118]) + "\n"
        line137 = "| Row 68 → Row 117 Row 68 → Row 57 Kohn–Sham meta capstone reunion (row 137) |"
        idx137 = pro.find(line137)
        if idx137 < 0:
            raise SystemExit("prologue compass row 137 not found")
        line_end137 = pro.find("\n", idx137)
        if line_end137 < 0:
            pro = pro + "\n" + compass138
        else:
            pro = pro[: line_end137 + 1] + compass138 + pro[line_end137 + 1 :]
        preview118 = extract_between(
            pro,
            '| <span id="prologue-preview-row-118"></span>',
            "\n| <span id=\"prologue-preview-row-119\">",
        )
        preview138 = lift_118_to_138(preview118)
        pro = pro.replace(
            '| <span id="prologue-preview-row-118"></span>',
            preview138 + '| <span id="prologue-preview-row-118"></span>',
            1,
        )
        if "row-138-closing-stitch" not in pro:
            stitch = (
                "**Row 138 closing stitch (Row 68 → Row 118 Row 68 → Row 58 DFT workflows meta capstone reunion).** {#row-138-closing-stitch} "
                "When row 137 closed — Kohn–Sham meta capstone verified, row 136 or row 117 recited on the capstone path, and IX.1 Bridge → IX.2 SCF recited with "
                "[cutoff-sweep Lab act](../part09-dft/02-kohn-sham.md#lab-act-cutoff-sweep-on-fcc-cu-act-vi--convergence-certificate) archived `cutoff_convergence.yaml` — but **row 58 IX.2 → IX.3 opening hinge still opens like standalone DFT coursework after the SCF implementation Scene on the capstone path** — "
                "the [preface row 138 When-to-pause opening sentence](../preface.md#skill-navigation-row-138) names the dual reunion before Handshake 3 meta reunion; read [preface row 138](../preface.md#skill-navigation-row-138), then the "
                "[Row 68 → Row 118 reunion index](../appendix/sources.md#row68-row118-dft-workflows-meta-capstone-reunion-index-row-138), then "
                "[epilogue row 138 closing loop](../epilogue/multiscale.md#row-138-closing-loop) before row 59 Handshake 3 meta capstone opens on the capstone path.\n\n"
            )
            pro = pro.replace("**Row 119 closing stitch", stitch + "**Row 119 closing stitch", 1)
        pro_path.write_text(pro)
        print("prologue: added row 138 compass/preview/stitch")

    src_path = ROOT / "writings/appendix/chapters/sources.md"
    src = src_path.read_text()
    if "row68-row118-dft-workflows-meta-capstone-reunion-index-row-138" not in src:
        idx118 = src.find(
            "## Row 68 → Row 98 Row 68 → Row 58 DFT workflows meta capstone reunion index (row 118)"
        )
        idx119 = src.find(
            "## Row 68 → Row 99 Row 68 → Row 59 Handshake 3 meta capstone reunion index (row 119)"
        )
        if idx118 < 0 or idx119 < 0:
            raise SystemExit("row 118/119 sources anchors missing")
        block = src[idx118:idx119]
        block138 = lift_118_to_138(block)
        table_row = (
            "| 138 | Row 68 → Row 118 Row 68 → Row 58 DFT workflows meta capstone (midpoint prelude gate ↔ Kohn–Sham meta capstone ↔ row 58 meta) | "
            "[Row 68 → Row 118 DFT workflows meta capstone reunion index](#row68-row118-dft-workflows-meta-capstone-reunion-index-row-138) · "
            "[preface row 138](../preface.md#skill-navigation-row-138) · "
            "[prologue row 138 preview](../prologue/00-many-scales.md#prologue-preview-row-138) · "
            "[prologue row 138 closing stitch](../prologue/00-many-scales.md#row-138-closing-stitch) · "
            "[epilogue row 138 closing loop](../epilogue/multiscale.md#row-138-closing-loop) · "
            "[memory sheet row 138 baby picture](memory-sheet.md#row-138-baby-picture-row68-row118-dft-workflows-meta-capstone-reunion) | "
            "Row 68 closed but **row 58 IX.2 → IX.3 opening hinge still feels disconnected from verified Kohn–Sham meta capstone on the capstone path** — "
            "read row 68 + row 137 or row 118 gate + IX.2 Bridge → opening hinge → IX.3 calculation ladder + row 58; "
            "[preface row 58](../preface.md#skill-navigation-row-58) |\n"
        )
        src = src.replace(
            "| 137 | Row 68 → Row 117 Row 68 → Row 57 Kohn–Sham meta capstone",
            table_row + "| 137 | Row 68 → Row 117 Row 68 → Row 57 Kohn–Sham meta capstone",
        )
        src = src.replace(
            "## Row 68 → Row 98 Row 68 → Row 58 DFT workflows meta capstone reunion index (row 118)",
            block138 + "## Row 68 → Row 98 Row 68 → Row 58 DFT workflows meta capstone reunion index (row 118)",
        )
        extra = (
            "[row 138](#row68-row118-dft-workflows-meta-capstone-reunion-index-row-138) reunites **Kohn–Sham meta capstone with the DFT workflows meta capstone boundary** "
            "when row 137 closed Kohn–Sham meta capstone at verified Murnaghan scan on the capstone path but `cutoff_convergence.yaml` and IX.2 → IX.3 opening hinge still read like separate courses after verified DFT workflows meta prelude meta;"
        )
        if extra not in src:
            src = src.replace(
                "when row 136 closed Born–Oppenheimer meta capstone at verified Murnaghan fits on the capstone path but `murnaghan_eos.yaml` and IX.1 → IX.2 opening hinge still read like separate courses after verified Kohn–Sham meta prelude meta;",
                "when row 136 closed Born–Oppenheimer meta capstone at verified Murnaghan fits on the capstone path but `murnaghan_eos.yaml` and IX.1 → IX.2 opening hinge still read like separate courses after verified Kohn–Sham meta prelude meta; "
                + extra,
            )
        src_path.write_text(src)
        print("sources: added row 138 index")

    mem_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    mem = mem_path.read_text()
    mem = fix_row_137_baby(mem)
    if "row-138-baby-picture" not in mem:
        baby118 = extract_between(mem, "### Row 118 baby picture", "### Row 119 baby picture")
        baby138 = lift_118_to_138(baby118)
        mem = mem.replace("### Act VI baby picture", baby138 + "### Act VI baby picture", 1)
        mem_table = (
            "| 138 | Meta | Row 68 → Row 118 Row 68 → Row 58 DFT workflows meta capstone reunion | "
            "[Row 68 → Row 118 DFT workflows meta capstone reunion index](sources.md#row68-row118-dft-workflows-meta-capstone-reunion-index-row-138) · "
            "[preface row 138 skill checkpoint](../preface.md#skill-navigation-row-138) · "
            "[prologue row 138 preview](../prologue/00-many-scales.md#prologue-preview-row-138) · "
            "[prologue row 138 closing stitch](../prologue/00-many-scales.md#row-138-closing-stitch) · "
            "[epilogue row 138 closing loop](../epilogue/multiscale.md#row-138-closing-loop) | "
            "Row 68 closed but row 58 IX.2 → IX.3 opening hinge feels disconnected from verified Kohn–Sham meta capstone on the capstone path — "
            "read row 68 + row 137 or row 118 gate + IX.2 Bridge → opening hinge → IX.3 calculation ladder + row 58; "
            "[row 138 baby picture](#row-138-baby-picture-row68-row118-dft-workflows-meta-capstone-reunion) |\n"
        )
        mem = mem.replace(
            "[row-137-baby-picture-row68-row117-kohn-sham-meta-capstone-reunion) |\n| 93 | Meta |",
            "[row-137-baby-picture-row68-row117-kohn-sham-meta-capstone-reunion) |\n" + mem_table + "| 93 | Meta |",
        )
        if "When row 137 closed but DFT workflows meta reunion still lags" not in mem:
            mem = mem.replace(
                "When row 136 closed but Kohn–Sham meta reunion still lags on the capstone path, switch to [row 137](#row-137-baby-picture-row68-row117-kohn-sham-meta-capstone-reunion).",
                "When row 136 closed but Kohn–Sham meta reunion still lags on the capstone path, switch to [row 137](#row-137-baby-picture-row68-row117-kohn-sham-meta-capstone-reunion). When row 137 closed but DFT workflows meta reunion still lags on the capstone path, switch to [row 138](#row-138-baby-picture-row68-row118-dft-workflows-meta-capstone-reunion).",
            )
        mem_path.write_text(mem)
        print("memory-sheet: added row 138")
    else:
        mem_path.write_text(mem)
        print("memory-sheet: row 138 baby already present (137 fixes applied)")


def main() -> None:
    add_row_138()


if __name__ == "__main__":
    main()
