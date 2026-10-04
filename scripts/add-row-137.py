#!/usr/bin/env python3
"""Repair row 136 capstone artifacts and add row 137 (Row 68 → Row 117 ↔ Row 57 Kohn–Sham meta capstone)."""
from __future__ import annotations

import re
import subprocess
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
        raise SystemExit(f"start marker not found: {start[:60]}")
    j = text.find(end, i + len(start))
    if j < 0:
        raise SystemExit(f"end marker not found after {start[:40]}")
    return text[i:j]


def lift_116_to_136(s: str) -> str:
    p = [
        ("Row 116 closing loop", "Row 136 closing loop"),
        ("row-116-closing-loop", "row-136-closing-loop"),
        ("Row 116 closing stitch", "Row 136 closing stitch"),
        ("row-116-closing-stitch", "row-136-closing-stitch"),
        ("prologue-preview-row-116", "prologue-preview-row-136"),
        ("Row 116 preview", "Row 136 preview"),
        ("Row 116 skill checkpoint", "Row 136 skill checkpoint"),
        ("skill-navigation-row-116", "skill-navigation-row-136"),
        ("memory sheet row 116", "memory sheet row 136"),
        ("Row 116 baby picture", "Row 136 baby picture"),
        (
            "Row 68 → Row 96 Row 68 → Row 56 Born–Oppenheimer meta capstone",
            "Row 68 → Row 116 Row 68 → Row 56 Born–Oppenheimer meta capstone",
        ),
        (
            "row68-row96-born-oppenheimer-meta-capstone-reunion-index-row-116",
            "row68-row116-born-oppenheimer-meta-capstone-reunion-index-row-136",
        ),
        (
            "row-116-baby-picture-row68-row96-born-oppenheimer-meta-capstone-reunion",
            "row-136-baby-picture-row68-row116-born-oppenheimer-meta-capstone-reunion",
        ),
        ("(row 116)", "(row 136)"),
        ("row 116", "row 136"),
        ("Row 116", "Row 136"),
        ("[row 115]", "[row 135]"),
        ("row 115", "row 135"),
        ("Row 115", "Row 135"),
        ("[row 96]", "[row 116]"),
        ("row 96", "row 116"),
        ("Row 96", "Row 116"),
        ("electronic audit meta capstone", "electronic audit meta prelude capstone"),
        (
            "Born–Oppenheimer meta capstone at the foundation SCF → BO/HK chapter boundary in reading time",
            "Born–Oppenheimer meta capstone at the foundation SCF → BO/HK chapter boundary in reading time on the capstone path",
        ),
        (
            "row 115 closed electronic audit meta capstone",
            "row 135 closed electronic audit meta prelude capstone",
        ),
        (
            "after the foundation SCF Lab act** while",
            "after the foundation SCF Lab act on the capstone path** while",
        ),
        (
            "verified electronic audit meta capstone closure (row 115)",
            "verified electronic audit meta prelude capstone closure (row 135)",
        ),
        (
            "Row 68 → Row 56 meta (row 116)",
            "Row 68 → Row 56 meta (row 136)",
        ),
        (
            "before row 117 Kohn–Sham meta capstone opens in workflow time",
            "before row 57 Kohn–Sham meta prelude opens on the capstone path in workflow time",
        ),
        ("When row 56 feels like quantum chemistry homework after row 115 alone", "When row 56 feels like quantum chemistry homework after row 135 alone on the capstone path"),
        ("Recite [preface row 115]", "Recite [preface row 135]"),
        (
            "Do not conflate row 116 (row 68 ↔ row 56 reunion",
            "Do not conflate row 136 (row 68 ↔ row 56 reunion on the capstone path",
        ),
        (
            "row 116 names **Row 68 → Row 76",
            "row 136 names **why that reunion must follow verified electronic audit meta prelude capstone (row 135) and the outer midpoint prelude gate (row 68)**; row 116 names **Row 68 → Row 76",
        ),
        (
            "Proceed to [row 117](#row-117-closing-loop) when row 68 closed but Kohn–Sham meta capstone still lags after row 116",
            "Proceed to [row 137](#row-137-closing-loop) when row 68 closed but Kohn–Sham meta capstone still lags after row 136 on the capstone path, to [row 117](#row-117-closing-loop) when row 68 closed but Kohn–Sham meta capstone still lags after row 116 on the opening-hinge path, to [row 116](#row-116-closing-loop) when row 68 closed but Born–Oppenheimer meta capstone still lags after row 115 on the opening-hinge path, to [row 135](#row-135-closing-loop) when electronic audit meta prelude capstone still lags after row 134 on the capstone path, to [row 56](#row-56-closing-loop) when only IX.0 → IX.1 stalls",
        ),
        ("Electronic audit meta row 115", "Electronic audit meta prelude capstone row 135"),
        (
            "row 115 when **VIII.3 Bridge",
            "row 135 when **VIII.3 Bridge",
        ),
        (
            "row 116 when **IX.0 Bridge",
            "row 136 when **IX.0 Bridge",
        ),
        (
            "before row 117 Kohn–Sham meta capstone or row 97 prelude opens",
            "before row 137 Kohn–Sham meta capstone or row 57 KS reunion opens on the capstone path",
        ),
        (
            "| Row 68 → Row 96 Row 68 → Row 56 Born–Oppenheimer meta capstone reunion (row 136) |",
            "| Row 68 → Row 116 Row 68 → Row 56 Born–Oppenheimer meta capstone reunion (row 136) |",
        ),
        (
            "when foundation SCF logs are clean but Born–Oppenheimer still feels like standalone quantum chemistry after verified electronic audit meta prelude capstone |",
            "when foundation SCF logs are clean on the capstone path but IX.1 still feels like standalone quantum chemistry after verified electronic audit meta prelude capstone |",
        ),
        (
            "electronic audit meta prelude capstone / Born–Oppenheimer opening gate + IX.0 Bridge",
            "electronic audit meta prelude capstone / Born–Oppenheimer opening gate + IX.0 Bridge",
        ),
        (
            "read row 68 gate + row 135 or row 116 electronic audit meta prelude capstone / Born–Oppenheimer opening gate + IX.0 Bridge → opening hinge → IX.1 BO/HK + row 56 meta aloud when foundation SCF logs are clean on the capstone path but IX.1 still feels like standalone quantum chemistry after verified electronic audit meta prelude capstone",
            "read row 68 gate + row 135 or row 116 electronic audit meta prelude capstone / Born–Oppenheimer opening gate + IX.0 Bridge → opening hinge → IX.1 BO/HK + row 56 meta aloud when foundation SCF logs are clean on the capstone path but Born–Oppenheimer still feels like standalone quantum chemistry after verified electronic audit meta prelude capstone",
        ),
    ]
    return tx(s, p)


def lift_117_to_137(s: str) -> str:
    p = [
        ("Row 117 closing loop", "Row 137 closing loop"),
        ("row-117-closing-loop", "row-137-closing-loop"),
        ("Row 117 closing stitch", "Row 137 closing stitch"),
        ("row-117-closing-stitch", "row-137-closing-stitch"),
        ("prologue-preview-row-117", "prologue-preview-row-137"),
        ("Row 117 preview", "Row 137 preview"),
        ("Row 117 skill checkpoint", "Row 137 skill checkpoint"),
        ("skill-navigation-row-117", "skill-navigation-row-137"),
        ("memory sheet row 117", "memory sheet row 137"),
        ("Row 117 baby picture", "Row 137 baby picture"),
        ("Row 117 three-way audit", "Row 137 three-way audit"),
        (
            "Row 68 → Row 97 Row 68 → Row 57 Kohn–Sham meta capstone",
            "Row 68 → Row 117 Row 68 → Row 57 Kohn–Sham meta capstone",
        ),
        (
            "row68-row97-kohn-sham-meta-capstone-reunion-index-row-117",
            "row68-row117-kohn-sham-meta-capstone-reunion-index-row-137",
        ),
        (
            "row-117-baby-picture-row68-row97-kohn-sham-meta-capstone-reunion",
            "row-137-baby-picture-row68-row117-kohn-sham-meta-capstone-reunion",
        ),
        ("(row 117)", "(row 137)"),
        ("row 117", "row 137"),
        ("Row 117", "Row 137"),
        ("[row 116]", "[row 136]"),
        ("row 116", "row 136"),
        ("Row 116", "Row 136"),
        ("[row 97]", "[row 117]"),
        ("row 97", "row 117"),
        ("Row 97", "Row 117"),
        (
            "Kohn–Sham meta capstone / Kohn–Sham opening prelude hinge",
            "Born–Oppenheimer meta capstone / Kohn–Sham opening prelude hinge on the capstone path",
        ),
        (
            "Born–Oppenheimer meta capstone / Kohn–Sham opening prelude hinge",
            "Born–Oppenheimer meta capstone / Kohn–Sham opening prelude hinge on the capstone path",
        ),
        (
            "after IX.1's Murnaghan Lab act**",
            "after IX.1's Murnaghan Lab act on the capstone path**",
        ),
        (
            "at the Kohn–Sham meta capstone boundary inside Part IX",
            "at the Kohn–Sham meta capstone boundary inside the coupling gate on the capstone path",
        ),
        ("Row 68 ↔ Row 57 reunion |", "Row 68 ↔ Row 57 reunion (capstone path) |"),
        (
            "[Row 68 → Row 77 Kohn–Sham meta prelude reunion index (row 97)]",
            "[Row 68 → Row 97 Kohn–Sham meta capstone reunion index (row 117)]",
        ),
        (
            "row68-row77-kohn-sham-meta-prelude-reunion-index-row-97",
            "row68-row97-kohn-sham-meta-capstone-reunion-index-row-117",
        ),
        (
            "Row 117 does not replace row 68, row 57, row 116, row 97, row 77, row 96, or row 38",
            "Row 137 does not replace row 68, row 57, row 136, row 117, row 97, row 77, or row 38",
        ),
        (
            "before IX.3 opens at \\(T_w\\)",
            "before row 58 DFT workflows meta prelude opens on the capstone path at \\(T_w\\)",
        ),
        (
            "row 116 closed but row 57",
            "row 136 closed but row 57",
        ),
        (
            "when `murnaghan_eos.yaml` exists but the inner SCF loop",
            "when `murnaghan_eos.yaml` exists on the capstone path but the inner SCF loop",
        ),
        ("after row 116.", "after row 136."),
        ("when row 116 and row 57", "when row 136 and row 57"),
        (
            "before row 57 closes",
            "before row 58 closes on the capstone path",
        ),
        (
            "When row 117 is complete, proceed to [row 118]",
            "When row 137 is complete, proceed to [row 138](preface.md#skill-navigation-row-138) when cutoff certificates exist on the capstone path but IX.3 still lags, to [row 118](preface.md#skill-navigation-row-118) when Kohn–Sham meta capstone is clean but DFT workflows meta capstone still lags on the opening-hinge path, to [row 98](preface.md#skill-navigation-row-98) for the Row 68 ↔ Row 58 DFT workflows opening prelude audit alone, to [row 117](preface.md#skill-navigation-row-117) for the Row 68 ↔ Row 57 Kohn–Sham meta audit on the opening-hinge path alone, to [row 136](preface.md#skill-navigation-row-136) when Born–Oppenheimer meta capstone still lags after verified electronic audit meta prelude capstone on the capstone path, to [row 57](preface.md#skill-navigation-row-57) when only IX.1 → IX.2 stalls, or extend prose only under `writings/` then sync.\n\nDUPLICATE_WHEN_ROW_117",
        ),
        (
            "Kohn–Sham meta capstone at the Murnaghan → SCF fixed-point chapter boundary in reading time",
            "Kohn–Sham meta capstone at the Murnaghan → SCF fixed-point chapter boundary in reading time on the capstone path",
        ),
        (
            "row 116 closed Born–Oppenheimer meta capstone",
            "row 136 closed Born–Oppenheimer meta capstone",
        ),
        (
            "verified Born–Oppenheimer meta capstone closure (row 116)",
            "verified Born–Oppenheimer meta capstone closure (row 136)",
        ),
        (
            "Row 68 → Row 57 meta (row 117)",
            "Row 68 → Row 57 meta (row 137)",
        ),
        (
            "before row 118 DFT workflows meta capstone opens in workflow time",
            "before row 58 DFT workflows meta prelude opens on the capstone path in workflow time",
        ),
        ("When row 57 feels like quantum chemistry homework after row 116 alone", "When row 57 feels like quantum chemistry homework after row 136 alone on the capstone path"),
        ("Recite [preface row 116]", "Recite [preface row 136]"),
        (
            "Do not conflate row 117 (row 68 ↔ row 57 reunion",
            "Do not conflate row 137 (row 68 ↔ row 57 reunion on the capstone path",
        ),
        (
            "row 117 names **Row 68 → Row 77",
            "row 137 names **why that reunion must follow verified Born–Oppenheimer meta capstone (row 136) and the outer midpoint prelude gate (row 68)**; row 117 names **Row 68 → Row 77",
        ),
        (
            "Proceed to [row 118](#row-118-closing-loop) when row 68 closed but DFT workflows meta capstone still lags after row 117",
            "Proceed to [row 138](#row-138-closing-loop) when row 68 closed but DFT workflows meta capstone still lags after row 137 on the capstone path, to [row 118](#row-118-closing-loop) when row 68 closed but DFT workflows meta capstone still lags after row 117 on the opening-hinge path, to [row 117](#row-117-closing-loop) for the Row 68 ↔ Row 57 Kohn–Sham meta audit on the opening-hinge path alone, to [row 136](#row-136-closing-loop) when Born–Oppenheimer meta capstone still lags after row 135 on the capstone path, to [row 57](#row-57-closing-loop) when only IX.1 → IX.2 stalls",
        ),
        ("Born–Oppenheimer meta row 116", "Born–Oppenheimer meta capstone row 136"),
        (
            "row 116 when **IX.0 Bridge",
            "row 136 when **IX.0 Bridge",
        ),
        (
            "row 117 when **IX.1 Bridge",
            "row 137 when **IX.1 Bridge",
        ),
        (
            "before row 118 DFT workflows meta capstone or row 98 prelude opens",
            "before row 138 DFT workflows meta capstone or row 58 workflow reunion opens on the capstone path",
        ),
        (
            "when Murnaghan fits are clean but Kohn–Sham SCF still feels like standalone quantum chemistry after verified Born–Oppenheimer meta capstone |",
            "when Murnaghan fits are clean on the capstone path but Kohn–Sham SCF still feels like standalone quantum chemistry after verified Born–Oppenheimer meta capstone |",
        ),
        (
            "read row 68 gate + row 136 or row 117 Born–Oppenheimer meta capstone / Kohn–Sham opening gate + IX.1 Bridge → opening hinge → IX.2 Kohn–Sham SCF + row 57 meta aloud when Murnaghan fits are clean on the capstone path but Kohn–Sham SCF still feels like standalone quantum chemistry after verified Born–Oppenheimer meta capstone",
            "read row 68 gate + row 136 or row 117 Born–Oppenheimer meta capstone / Kohn–Sham opening gate + IX.1 Bridge → opening hinge → IX.2 Kohn–Sham SCF + row 57 meta aloud when Murnaghan fits are clean on the capstone path but Kohn–Sham SCF still feels like standalone quantum chemistry after verified Born–Oppenheimer meta capstone",
        ),
    ]
    out = tx(s, p)
    if "DUPLICATE_WHEN_ROW_117" in out:
        out = re.sub(r"\n\nDUPLICATE_WHEN_ROW_117.*", "", out, flags=re.S)
    return out


def fix_row_136_preface() -> None:
    subprocess.run([sys.executable, str(ROOT / "scripts/fix-row-136-content.py")], check=True)


def fix_row_136_artifacts() -> None:
    ep_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    ep = ep_path.read_text()
    block116 = extract_between(ep, "### Row 116 closing loop", "### Row 117 closing loop")
    block136 = lift_116_to_136(block116)
    if "### Row 136 closing loop" in ep:
        ep = re.sub(
            r"### Row 136 closing loop.*?(?=\n### Row 135 closing loop)",
            block136,
            ep,
            count=1,
            flags=re.S,
        )
    else:
        ep = ep.replace("### Row 135 closing loop", block136 + "### Row 135 closing loop", 1)
    ep_path.write_text(ep)
    print("epilogue: repaired row 136 loop")

    mem_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    mem = mem_path.read_text()
    baby116 = extract_between(mem, "### Row 116 baby picture", "### Row 117 baby picture")
    baby136 = lift_116_to_136(baby116)
    if "### Row 136 baby picture" in mem:
        mem = re.sub(
            r"### Row 136 baby picture.*?(?=\n### Act VI baby picture)",
            baby136,
            mem,
            count=1,
            flags=re.S,
        )
    else:
        mem = mem.replace("### Act VI baby picture", baby136 + "### Act VI baby picture", 1)
    mem_path.write_text(mem)
    print("memory-sheet: repaired row 136 baby picture")

    pro_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    pro = pro_path.read_text()
    compass116 = extract_between(
        pro,
        "| Row 68 → Row 96 Row 68 → Row 56 Born–Oppenheimer meta capstone reunion (row 116) |",
        "\n| Row 68 → Row 97",
    )
    compass136 = lift_116_to_136(compass116)
    bad = re.search(
        r"\| Row 68 → Row 116 Row 68 → Row 56 dynamics meta prelude capstone reunion \(row 136\) \|.*?\n",
        pro,
    )
    if bad:
        pro = pro[: bad.start()] + compass136 + pro[bad.end() :]
    elif "| Row 68 → Row 116 Row 68 → Row 56 Born–Oppenheimer meta capstone reunion (row 136) |" not in pro:
        anchor = "| Row 68 → Row 115 Row 68 → Row 55 electronic audit meta prelude capstone reunion (row 135) |"
        idx = pro.find(anchor)
        line_end = pro.find("\n", idx)
        pro = pro[: line_end + 1] + compass136 + pro[line_end + 1 :]

    preview116 = extract_between(
        pro,
        '| <span id="prologue-preview-row-116"></span>',
        "\n| <span id=\"prologue-preview-row-117\">",
    )
    preview136 = lift_116_to_136(preview116)
    pro = re.sub(
        r'\| <span id="prologue-preview-row-136"></span>.*?\n(?=\| <span id="prologue-preview-row-13)',
        preview136,
        pro,
        count=1,
        flags=re.S,
    )
    if "row-136-closing-stitch" not in pro:
        stitch = (
            "**Row 136 closing stitch (Row 68 → Row 116 Row 68 → Row 56 Born–Oppenheimer meta capstone reunion).** {#row-136-closing-stitch} "
            "When row 135 closed — electronic audit meta prelude capstone verified, row 134 or row 115 recited on the capstone path, and VIII.3 Bridge → IX.0 SCF recited with "
            "[foundation SCF audit Lab act](../part09-dft/00-opening.md#lab-act-foundation-scf-audit-before-born-oppenheimer-act-vi--foundation) archived `cu.relax.out` and `alpha_export.yaml` — but **row 56 IX.0 → IX.1 opening hinge still opens like standalone quantum chemistry homework after the electronic audit Scene on the capstone path** — "
            "the [preface row 136 When-to-pause opening sentence](../preface.md#skill-navigation-row-136) names the dual reunion before Kohn–Sham meta reunion; read [preface row 136](../preface.md#skill-navigation-row-136), then the "
            "[Row 68 → Row 116 reunion index](../appendix/sources.md#row68-row116-born-oppenheimer-meta-capstone-reunion-index-row-136), then "
            "[epilogue row 136 closing loop](../epilogue/multiscale.md#row-136-closing-loop) before row 57 Kohn–Sham meta capstone opens on the capstone path.\n\n"
        )
        pro = pro.replace("**Row 117 closing stitch", stitch + "**Row 117 closing stitch", 1)
    pro_path.write_text(pro)
    print("prologue: repaired row 136 compass/preview/stitch")

    src_path = ROOT / "writings/appendix/chapters/sources.md"
    src = src_path.read_text()
    idx116 = src.find(
        "## Row 68 → Row 96 Row 68 → Row 56 Born–Oppenheimer meta capstone reunion index (row 116)"
    )
    idx117 = src.find(
        "## Row 68 → Row 97 Row 68 → Row 57 Kohn–Sham meta capstone reunion index (row 117)"
    )
    if idx116 >= 0 and idx117 > idx116:
        block = src[idx116:idx117]
        block136 = lift_116_to_136(block)
        block136 = block136.replace(
            "## Row 68 → Row 116 Row 68 → Row 56 Born–Oppenheimer meta capstone reunion index (row 136)",
            "## Row 68 → Row 116 Row 68 → Row 56 Born–Oppenheimer meta capstone reunion index (row 136) {#row68-row116-born-oppenheimer-meta-capstone-reunion-index-row-136}",
            1,
        )
        block136 = re.sub(r"\s*\{#row68-row116-born-oppenheimer-meta-capstone-reunion-index-row-136\}\s*\{#.*?\}", " {#row68-row116-born-oppenheimer-meta-capstone-reunion-index-row-136}", block136, count=1)
        start_pat = "## Row 68 → Row 116 Row 68 → Row 56 Born–Oppenheimer meta capstone reunion index (row 136)"
        s0 = src.find(start_pat)
        if s0 >= 0:
            s1 = src.find("\n## Row 68 → Row 115", s0)
            if s1 < 0:
                s1 = src.find("\n## Row 68 → Row 97", s0)
            if s1 < 0:
                raise SystemExit("row 136 sources block end not found")
            src = src[:s0] + block136 + src[s1:]
        table_row = (
            "| 136 | Row 68 → Row 116 Row 68 → Row 56 Born–Oppenheimer meta capstone (midpoint prelude gate ↔ electronic audit meta prelude capstone ↔ row 56 meta) | "
            "[Row 68 → Row 116 Born–Oppenheimer meta capstone reunion index](#row68-row116-born-oppenheimer-meta-capstone-reunion-index-row-136) · "
            "[preface row 136](../preface.md#skill-navigation-row-136) · "
            "[prologue row 136 preview](../prologue/00-many-scales.md#prologue-preview-row-136) · "
            "[prologue row 136 closing stitch](../prologue/00-many-scales.md#row-136-closing-stitch) · "
            "[epilogue row 136 closing loop](../epilogue/multiscale.md#row-136-closing-loop) · "
            "[memory sheet row 136 baby picture](memory-sheet.md#row-136-baby-picture-row68-row116-born-oppenheimer-meta-capstone-reunion) | "
            "Row 68 closed but **row 56 IX.0 → IX.1 opening hinge still feels disconnected from verified electronic audit meta prelude capstone on the capstone path** — "
            "read row 68 + row 135 or row 116 gate + IX.0 Bridge → opening hinge → IX.1 BO/HK + row 56; "
            "[preface row 56](../preface.md#skill-navigation-row-56) |\n"
        )
        src = re.sub(
            r"\| 136 \| Row 68 → Row 116 Row 68 → Row 56 dynamics meta prelude capstone.*?\n",
            table_row,
            src,
            count=1,
        )
        extra = (
            "[row 137](#row68-row117-kohn-sham-meta-capstone-reunion-index-row-137) reunites **Born–Oppenheimer meta capstone with the Kohn–Sham meta capstone boundary** "
            "when row 136 closed Born–Oppenheimer meta capstone at verified foundation SCF on the capstone path but `murnaghan_eos.yaml` and IX.1 → IX.2 opening hinge still read like separate courses after verified Kohn–Sham meta prelude meta;"
        )
        if extra not in src and "row-136" in extra:
            pass
        if "[row 137](#row68-row117-kohn-sham-meta-capstone-reunion-index-row-137)" not in src:
            src = src.replace(
                "when row 135 closed electronic audit meta prelude capstone at verified foundation SCF on the capstone path but `cu.relax.out` and IX.0 → IX.1 opening hinge still read like separate courses after verified Born–Oppenheimer meta prelude meta;",
                "when row 135 closed electronic audit meta prelude capstone at verified foundation SCF on the capstone path but `cu.relax.out` and IX.0 → IX.1 opening hinge still read like separate courses after verified Born–Oppenheimer meta prelude meta; "
                + extra,
            )
        src_path.write_text(src)
        print("sources: repaired row 136 index")


def add_row_137() -> None:
    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    if "skill-navigation-row-137" in preface:
        print("preface: row 137 already present")
    else:
        m116 = re.search(
            r"(### Row 117 skill checkpoint.*?)(?=\n### Row 118 skill checkpoint)",
            preface,
            re.S,
        )
        if not m116:
            raise SystemExit("row 117 preface checkpoint missing")
        row137 = lift_117_to_137(m116.group(1))
        row136_tail_old = (
            "When row 135 is complete, proceed to [row 136](preface.md#skill-navigation-row-136) when electronic audit meta prelude capstone is clean but Born–Oppenheimer meta capstone still lags after verified foundation SCF archive on the capstone path, to [row 116](preface.md#skill-navigation-row-116) when electronic audit meta capstone is clean but Born–Oppenheimer meta capstone still lags on the opening-hinge path, to [row 96](preface.md#skill-navigation-row-96) for the Row 68 ↔ Row 56 Born–Oppenheimer opening prelude audit alone, to [row 135](preface.md#skill-navigation-row-135) when export meta prelude capstone still lags after verified pedigree checklist on the capstone path, to [row 56](preface.md#skill-navigation-row-56) when only IX.0 → IX.1 stalls, or extend prose only under `writings/` then sync."
        )
        row136_tail_new = (
            "When row 136 is complete, proceed to [row 137](preface.md#skill-navigation-row-137) when Born–Oppenheimer meta capstone is clean but Kohn–Sham meta capstone still lags after verified Murnaghan archive on the capstone path, to [row 117](preface.md#skill-navigation-row-117) when Born–Oppenheimer meta capstone is clean but Kohn–Sham meta capstone still lags on the opening-hinge path, to [row 97](preface.md#skill-navigation-row-97) for the Row 68 ↔ Row 57 Kohn–Sham opening prelude audit alone, to [row 136](preface.md#skill-navigation-row-136) when electronic audit meta prelude capstone still lags after verified foundation SCF on the capstone path, to [row 57](preface.md#skill-navigation-row-57) when only IX.1 → IX.2 stalls, or extend prose only under `writings/` then sync."
        )
        if row136_tail_old in preface:
            preface = preface.replace(row136_tail_old, row136_tail_new)
        anchor = "\n## The copper wire through the book"
        preface = preface.replace(anchor, "\n" + row137 + anchor)
        preface_path.write_text(preface)
        print("preface: added row 137")

    ep_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    ep = ep_path.read_text()
    if "row-137-closing-loop" not in ep:
        block117 = extract_between(ep, "### Row 117 closing loop", "### Row 118 closing loop")
        block137 = lift_117_to_137(block117)
        ep = ep.replace("### Row 118 closing loop", block137 + "### Row 118 closing loop", 1)
        ep = ep.replace(
            "Proceed to [row 136](#row-136-closing-loop) when row 68 closed but Born–Oppenheimer meta capstone still lags after row 135 on the capstone path, to [row 135](#row-135-closing-loop) when row 68 closed but electronic audit meta prelude capstone still lags after row 134 on the capstone path,",
            "Proceed to [row 137](#row-137-closing-loop) when row 68 closed but Kohn–Sham meta capstone still lags after row 136 on the capstone path, to [row 136](#row-136-closing-loop) when row 68 closed but Born–Oppenheimer meta capstone still lags after row 135 on the capstone path, to [row 135](#row-135-closing-loop) when row 68 closed but electronic audit meta prelude capstone still lags after row 134 on the capstone path,",
            1,
        )
        ep_path.write_text(ep)
        print("epilogue: added row 137 loop")

    pro_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    pro = pro_path.read_text()
    if "| Row 68 → Row 117 Row 68 → Row 57 Kohn–Sham meta capstone reunion (row 137) |" not in pro:
        compass117 = extract_between(
            pro,
            "| Row 68 → Row 97 Row 68 → Row 57 Kohn–Sham meta capstone reunion (row 117) |",
            "\n| Row 68 → Row 98",
        )
        compass137 = lift_117_to_137(compass117)
        needle = "| Row 68 → Row 116 Row 68 → Row 56 Born–Oppenheimer meta capstone reunion (row 136) |"
        idx = pro.find(needle)
        line_end = pro.find("\n", idx)
        pro = pro[: line_end + 1] + compass137 + pro[line_end + 1 :]
        preview117 = extract_between(
            pro,
            '| <span id="prologue-preview-row-117"></span>',
            "\n| <span id=\"prologue-preview-row-118\">",
        )
        preview137 = lift_117_to_137(preview117)
        pro = pro.replace(
            '| <span id="prologue-preview-row-117"></span>',
            preview137 + '| <span id="prologue-preview-row-117"></span>',
            1,
        )
        if "row-137-closing-stitch" not in pro:
            stitch = (
                "**Row 137 closing stitch (Row 68 → Row 117 Row 68 → Row 57 Kohn–Sham meta capstone reunion).** {#row-137-closing-stitch} "
                "When row 136 closed — Born–Oppenheimer meta capstone verified, row 135 or row 116 recited on the capstone path, and IX.0 Bridge → IX.1 BO/HK recited with "
                "[Murnaghan Lab act](../part09-dft/01-born-oppenheimer.md#lab-act-murnaghan-fit-on-fcc-cu-act-vi--foundation) archived `murnaghan_eos.yaml` — but **row 57 IX.1 → IX.2 opening hinge still opens like standalone quantum chemistry homework after the BO/HK Scene on the capstone path** — "
                "the [preface row 137 When-to-pause opening sentence](../preface.md#skill-navigation-row-137) names the dual reunion before DFT workflows meta reunion; read [preface row 137](../preface.md#skill-navigation-row-137), then the "
                "[Row 68 → Row 117 reunion index](../appendix/sources.md#row68-row117-kohn-sham-meta-capstone-reunion-index-row-137), then "
                "[epilogue row 137 closing loop](../epilogue/multiscale.md#row-137-closing-loop) before row 58 DFT workflows meta capstone opens on the capstone path.\n\n"
            )
            pro = pro.replace("**Row 118 closing stitch", stitch + "**Row 118 closing stitch", 1)
        pro_path.write_text(pro)
        print("prologue: added row 137 compass/preview/stitch")

    src_path = ROOT / "writings/appendix/chapters/sources.md"
    src = src_path.read_text()
    if "row68-row117-kohn-sham-meta-capstone-reunion-index-row-137" not in src:
        idx117 = src.find(
            "## Row 68 → Row 97 Row 68 → Row 57 Kohn–Sham meta capstone reunion index (row 117)"
        )
        idx118 = src.find(
            "## Row 68 → Row 98 Row 68 → Row 58 DFT workflows meta capstone reunion index (row 118)"
        )
        block = src[idx117:idx118]
        block137 = lift_117_to_137(block)
        table_row = (
            "| 137 | Row 68 → Row 117 Row 68 → Row 57 Kohn–Sham meta capstone (midpoint prelude gate ↔ Born–Oppenheimer meta capstone ↔ row 57 meta) | "
            "[Row 68 → Row 117 Kohn–Sham meta capstone reunion index](#row68-row117-kohn-sham-meta-capstone-reunion-index-row-137) · "
            "[preface row 137](../preface.md#skill-navigation-row-137) · "
            "[prologue row 137 preview](../prologue/00-many-scales.md#prologue-preview-row-137) · "
            "[prologue row 137 closing stitch](../prologue/00-many-scales.md#row-137-closing-stitch) · "
            "[epilogue row 137 closing loop](../epilogue/multiscale.md#row-137-closing-loop) · "
            "[memory sheet row 137 baby picture](memory-sheet.md#row-137-baby-picture-row68-row117-kohn-sham-meta-capstone-reunion) | "
            "Row 68 closed but **row 57 IX.1 → IX.2 opening hinge still feels disconnected from verified Born–Oppenheimer meta capstone on the capstone path** — "
            "read row 68 + row 136 or row 117 gate + IX.1 Bridge → opening hinge → IX.2 Kohn–Sham SCF + row 57; "
            "[preface row 57](../preface.md#skill-navigation-row-57) |\n"
        )
        src = src.replace(
            "| 136 | Row 68 → Row 116 Row 68 → Row 56 Born–Oppenheimer meta capstone",
            table_row + "| 136 | Row 68 → Row 116 Row 68 → Row 56 Born–Oppenheimer meta capstone",
        )
        src = src.replace(
            "## Row 68 → Row 97 Row 68 → Row 57 Kohn–Sham meta capstone reunion index (row 117)",
            block137 + "## Row 68 → Row 97 Row 68 → Row 57 Kohn–Sham meta capstone reunion index (row 117)",
        )
        src_path.write_text(src)
        print("sources: added row 137 index")

    mem_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    mem = mem_path.read_text()
    if "row-137-baby-picture" not in mem:
        baby117 = extract_between(mem, "### Row 117 baby picture", "### Row 118 baby picture")
        baby137 = lift_117_to_137(baby117)
        mem = mem.replace("### Act VI baby picture", baby137 + "### Act VI baby picture", 1)
        mem_table = (
            "| 137 | Meta | Row 68 → Row 117 Row 68 → Row 57 Kohn–Sham meta capstone reunion | "
            "[Row 68 → Row 117 Kohn–Sham meta capstone reunion index](sources.md#row68-row117-kohn-sham-meta-capstone-reunion-index-row-137) · "
            "[preface row 137 skill checkpoint](../preface.md#skill-navigation-row-137) · "
            "[prologue row 137 preview](../prologue/00-many-scales.md#prologue-preview-row-137) · "
            "[prologue row 137 closing stitch](../prologue/00-many-scales.md#row-137-closing-stitch) · "
            "[epilogue row 137 closing loop](../epilogue/multiscale.md#row-137-closing-loop) | "
            "Row 68 closed but row 57 IX.1 → IX.2 opening hinge feels disconnected from verified Born–Oppenheimer meta capstone on the capstone path — "
            "read row 68 + row 136 or row 117 gate + IX.1 Bridge → opening hinge → IX.2 Kohn–Sham SCF + row 57; "
            "[row 137 baby picture](#row-137-baby-picture-row68-row117-kohn-sham-meta-capstone-reunion) |\n"
        )
        mem = mem.replace(
            "[row-136-baby-picture-row68-row116-born-oppenheimer-meta-capstone-reunion) |\n| 93 | Meta |",
            "[row-136-baby-picture-row68-row116-born-oppenheimer-meta-capstone-reunion) |\n" + mem_table + "| 93 | Meta |",
        )
        if "When row 136 closed but Kohn–Sham meta reunion still lags" not in mem:
            mem = mem.replace(
                "When row 135 closed but Born–Oppenheimer meta reunion still lags on the capstone path, switch to [row 136](#row-136-baby-picture-row68-row116-born-oppenheimer-meta-capstone-reunion).",
                "When row 135 closed but Born–Oppenheimer meta reunion still lags on the capstone path, switch to [row 136](#row-136-baby-picture-row68-row116-born-oppenheimer-meta-capstone-reunion). When row 136 closed but Kohn–Sham meta reunion still lags on the capstone path, switch to [row 137](#row-137-baby-picture-row68-row117-kohn-sham-meta-capstone-reunion).",
            )
        mem_path.write_text(mem)
        print("memory-sheet: added row 137")


def main() -> None:
    fix_row_136_preface()
    fix_row_136_artifacts()
    add_row_137()


if __name__ == "__main__":
    main()
