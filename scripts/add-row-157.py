#!/usr/bin/env python3
"""Add row 157 (Row 68 → Row 137 ↔ Row 57 Kohn–Sham meta prelude capstone on full capstone path)."""
from __future__ import annotations

import re
import runpy
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
        raise SystemExit(f"start marker not found: {start[:80]}")
    j = text.find(end, i + len(start))
    if j < 0:
        raise SystemExit(f"end marker not found after {start[:40]}")
    return text[i:j]


def lift_137_to_157(s: str) -> str:
    """Promote capstone-path row 137 checkpoint to full-capstone row 157 wording."""
    p = [
        ("skill-navigation-row-137", "skill-navigation-row-157"),
        ("### Row 137 skill checkpoint", "### Row 157 skill checkpoint"),
        ("Row 137 does not replace", "Row 157 does not replace"),
        ("Row 137 three-way audit", "Row 157 three-way audit"),
        ("Row 137 closing loop", "Row 157 closing loop"),
        ("row-137-closing-loop", "row-157-closing-loop"),
        ("Row 137 closing stitch", "Row 157 closing stitch"),
        ("row-137-closing-stitch", "row-157-closing-stitch"),
        ("prologue-preview-row-137", "prologue-preview-row-157"),
        ("Row 137 preview", "Row 157 preview"),
        ("Row 137 skill checkpoint", "Row 157 skill checkpoint"),
        ("memory sheet row 137", "memory sheet row 157"),
        ("Row 137 baby picture", "Row 157 baby picture"),
        (
            "Row 68 → Row 117 Row 68 → Row 57 Kohn–Sham meta capstone",
            "Row 68 → Row 137 Row 68 → Row 57 Kohn–Sham meta prelude capstone",
        ),
        (
            "row68-row117-kohn-sham-meta-capstone-reunion-index-row-137",
            "row68-row137-kohn-sham-meta-prelude-capstone-reunion-index-row-157",
        ),
        (
            "row-137-baby-picture-row68-row117-kohn-sham-meta-capstone-reunion",
            "row-157-baby-picture-row68-row137-kohn-sham-meta-prelude-capstone-reunion",
        ),
        ("[row 138]", "__ROW158__"),
        ("[row 136]", "[row 156]"),
        ("row 136", "row 156"),
        ("Row 136", "Row 156"),
        ("__ROW158__", "[row 158]"),
        (
            "Row 68 → Row 117 Kohn–Sham meta capstone reunion index (row 137)",
            "Row 68 → Row 137 Kohn–Sham meta prelude capstone reunion index (row 157)",
        ),
        (
            "Kohn–Sham meta capstone reunion index (row 137)",
            "Kohn–Sham meta prelude capstone reunion index (row 157)",
        ),
        ("Kohn–Sham meta capstone reunion", "Kohn–Sham meta prelude capstone reunion"),
        ("Kohn–Sham meta capstone", "Kohn–Sham meta prelude capstone"),
        ("kohn-sham-meta-capstone-reunion", "kohn-sham-meta-prelude-capstone-reunion"),
        (
            "Born–Oppenheimer meta capstone / Kohn–Sham opening gate",
            "Born–Oppenheimer meta prelude capstone / Kohn–Sham opening gate",
        ),
        ("Born–Oppenheimer meta capstone", "Born–Oppenheimer meta prelude capstone"),
        (
            "verified Born–Oppenheimer meta capstone closure with the full-book IX.1 → IX.2 Kohn–Sham meta capstone reunion",
            "verified Born–Oppenheimer meta prelude capstone closure (row 156) with the full-book IX.1 → IX.2 Kohn–Sham meta reunion (row 57)",
        ),
        (
            "or [row 117](preface.md#skill-navigation-row-117) closed",
            "or [row 137](preface.md#skill-navigation-row-137) closed",
        ),
        (
            "Kohn–Sham opening prelude hinge on the capstone path (IX.0 Bridge → IX.1 BO/HK recited",
            "Kohn–Sham opening prelude hinge (IX.1 Bridge → Murnaghan archive recited on the full capstone path",
        ),
        (
            "one dft arc under `writings/dft` chapters 01–02), but",
            "one dft arc under `writings/dft` chapters 01–02 after verified Born–Oppenheimer meta prelude capstone), but",
        ),
        (
            "after IX.1's Murnaghan Lab act on the capstone path**",
            "after IX.1's Murnaghan Lab act on the full capstone path**",
        ),
        (
            "Kohn–Sham meta prelude capstone boundary inside the coupling gate on the capstone path",
            "Kohn–Sham meta prelude capstone boundary inside the dft subtree on the full capstone path",
        ),
        (
            "Row 157 does not replace row 68, row 57, row 156, row 137, row 117, row 97, row 77, or row 38",
            "Row 157 does not replace row 68, row 57, row 156, row 137, row 117, row 97, row 77, row 116, row 56, row 155, or row 38",
        ),
        (
            "before row 58 DFT workflows meta prelude opens on the capstone path at \\(T_w\\)",
            "before IX.3 opens at \\(T_w\\) on the full capstone path",
        ),
        ("Row 68 ↔ Row 57 reunion (capstone path)", "Row 68 ↔ Row 57 reunion (full capstone path)"),
        (
            "[row 156](preface.md#skill-navigation-row-136) or [Row 68 → Row 117 Kohn–Sham meta prelude capstone reunion index (row 137)]",
            "[row 156](preface.md#skill-navigation-row-156) or [Row 68 → Row 117 Kohn–Sham meta prelude capstone reunion index (row 137)]",
        ),
        (
            "Murnaghan yaml + converged `scf_*.out` at \\(T_w\\) before IX.1 Bridge → SCF",
            "Murnaghan yaml + converged `scf_*.out` at \\(T_w\\) on full capstone path before IX.1 Bridge → SCF",
        ),
        (
            "when opening [row 138](preface.md#skill-navigation-row-138) before row 58 closes on the capstone path",
            "when opening [row 158](preface.md#skill-navigation-row-158) before row 57 closes on the full capstone path",
        ),
        (
            "When row 137 is complete, proceed to [row 138](preface.md#skill-navigation-row-138) when cutoff certificates exist on the capstone path but IX.3 still lags, to [row 118](preface.md#skill-navigation-row-118) when Kohn–Sham meta capstone is clean but DFT workflows meta capstone still lags on the opening-hinge path, to [row 98](preface.md#skill-navigation-row-98) for the Row 68 ↔ Row 58 DFT workflows opening prelude audit alone, to [row 117](preface.md#skill-navigation-row-117) for the Row 68 ↔ Row 57 Kohn–Sham meta audit on the opening-hinge path alone, to [row 136](preface.md#skill-navigation-row-136) when Born–Oppenheimer meta capstone still lags after verified electronic audit meta prelude capstone on the capstone path, to [row 57](preface.md#skill-navigation-row-57) when only IX.1 → IX.2 stalls, or extend prose only under `writings/` then sync.",
            "When row 157 is complete, proceed to [row 158](preface.md#skill-navigation-row-158) when `cutoff_convergence.yaml` exists but IX.3 still feels disconnected from verified Kohn–Sham meta prelude capstone on the full capstone path, to [row 138](preface.md#skill-navigation-row-138) when `cutoff_convergence.yaml` exists but IX.3 still feels disconnected on the opening-hinge capstone path alone, to [row 117](preface.md#skill-navigation-row-117) for the Row 68 ↔ Row 57 Kohn–Sham meta audit on the opening-hinge prelude path alone, to [row 116](preface.md#skill-navigation-row-116) for the Row 68 ↔ Row 56 Born–Oppenheimer meta audit on the opening-hinge prelude path alone, to [row 156](preface.md#skill-navigation-row-156) when `murnaghan_eos.yaml` is missing after verified Born–Oppenheimer meta prelude capstone on the full capstone path, to [row 137](preface.md#skill-navigation-row-137) for the Row 68 ↔ Row 57 Kohn–Sham meta audit on the opening-hinge capstone path alone, to [row 136](preface.md#skill-navigation-row-136) for the Row 68 ↔ Row 56 Born–Oppenheimer meta audit on the opening-hinge capstone path alone, to [row 155](preface.md#skill-navigation-row-155) when Born–Oppenheimer still stalls on the full capstone path, to [row 57](preface.md#skill-navigation-row-57) when only IX.1 → IX.2 stalls, or extend prose only under `writings/` then sync.",
        ),
        (
            "when row 156 closed but row 57 IX.1 → IX.2 reunion still feels like quantum chemistry homework disconnected from verified Born–Oppenheimer meta capstone on the capstone path — it names the dual reunion before the cutoff-sweep Lab act",
            "when row 156 closed but row 57 IX.1 → IX.2 reunion still feels like quantum chemistry homework disconnected from verified Born–Oppenheimer meta prelude capstone on the full capstone path — it names the dual reunion before DFT workflows meta prelude capstone",
        ),
        (
            "when `murnaghan_eos.yaml` exists on the capstone path but the inner SCF loop",
            "when `murnaghan_eos.yaml` exists on the full capstone path but the inner SCF loop",
        ),
        (
            "Row 68 → Row 117 reunion index",
            "Row 68 → Row 137 reunion index",
        ),
        (
            "when opening [row 137](preface.md#skill-navigation-row-137) before row 57 closes on the capstone path",
            "when opening [row 157](preface.md#skill-navigation-row-157) before row 57 closes on the full capstone path",
        ),
        ("Recite [preface row 136]", "Recite [preface row 156]"),
        ("on the capstone path", "on the full capstone path"),
    ]
    out = tx(s, p)
    out = out.replace("full full capstone path", "full capstone path")
    return out


def ensure_row_137_preface() -> None:
    path = ROOT / "writings/preface/chapters/preface.md"
    text = path.read_text()
    if "skill-navigation-row-137" in text and "### Row 137 skill checkpoint" in text:
        return
    ns = runpy.run_path(str(ROOT / "scripts/add-row-137.py"))
    m117 = re.search(
        r"(### Row 117 skill checkpoint.*?)(?=\n### Row 118 skill checkpoint)",
        text,
        re.S,
    )
    if not m117:
        raise SystemExit("row 117 preface checkpoint missing for row 137 lift")
    row137 = ns["lift_117_to_137"](m117.group(1))
    anchor = "\n## The copper wire through the book"
    if anchor not in text:
        raise SystemExit("copper wire anchor missing")
    text = text.replace(anchor, "\n" + row137 + anchor)
    path.write_text(text)
    print("preface: added row 137 (prerequisite for row 157)")


def fix_row_156_preface() -> None:
    path = ROOT / "writings/preface/chapters/preface.md"
    text = path.read_text()
    if "### Row 156 skill checkpoint" in text:
        return
    ns156 = runpy.run_path(str(ROOT / "scripts/add-row-156.py"))
    m136 = re.search(
        r"(### Row 136 skill checkpoint.*?)(\*\*When to pause\.\*\*.*?)(?=\n## The copper wire through the book)",
        text,
        re.S,
    )
    if not m136:
        raise SystemExit("row 136 preface block missing for row 156 repair")
    body136 = m136.group(1)
    # Restore row 136 when-to-pause (capstone path, not row 156 wording)
    when136 = (
        "**When to pause.** Read the [prologue row 136 closing stitch](prologue/00-many-scales.md#row-136-closing-stitch) first when row 135 closed but row 56 IX.0 → IX.1 reunion still feels like quantum chemistry homework disconnected from verified electronic audit meta prelude capstone on the capstone path — it names the dual reunion before Kohn–Sham meta reunion. Then read the [prologue row 136 preview](prologue/00-many-scales.md#prologue-preview-row-136) when `cu.relax.out` exists on the capstone path but \\(V_{\\text{BO}}\\) is unnamed after row 135. Return to the [Row 68 → Row 116 reunion index](appendix/sources.md#row68-row116-born-oppenheimer-meta-capstone-reunion-index-row-136) when row 135 and row 56 both verify individually but **electronic audit meta prelude capstone and IX.0 → IX.1 opening hinge still feel like separate stories** — the break is usually skipping [IX.0's Bridge](part09-dft/00-opening.md#bridge), not missing Murnaghan algebra. Read the [memory sheet row 136 baby picture](appendix/memory-sheet.md#row-136-baby-picture-row68-row116-born-oppenheimer-meta-capstone-reunion) when opening [row 137](preface.md#skill-navigation-row-137) before row 56 closes on the capstone path; read the [epilogue row 136 closing loop](epilogue/multiscale.md#row-136-closing-loop) when the competence loop closes. When row 136 is complete, proceed to [row 137](preface.md#skill-navigation-row-137) when Born–Oppenheimer meta capstone is clean but Kohn–Sham meta capstone still lags after verified Murnaghan archive on the capstone path, to [row 117](preface.md#skill-navigation-row-117) when Born–Oppenheimer meta capstone is clean but Kohn–Sham meta capstone still lags on the opening-hinge path, to [row 97](preface.md#skill-navigation-row-97) for the Row 68 ↔ Row 57 Kohn–Sham opening prelude audit alone, to [row 135](preface.md#skill-navigation-row-135) when electronic audit meta prelude capstone still lags after verified foundation SCF on the capstone path, to [row 56](preface.md#skill-navigation-row-56) when only IX.0 → IX.1 stalls, or extend prose only under `writings/` then sync.\n"
    )
    block156 = ns156["lift_136_to_156"](body136 + when136)
    text = re.sub(
        r"### Row 136 skill checkpoint.*?(?=\n## The copper wire through the book)",
        body136 + when136 + "\n" + block156,
        text,
        count=1,
        flags=re.S,
    )
    path.write_text(text)
    print("preface: repaired row 136 when-to-pause and inserted row 156")


def insert_preface_row() -> None:
    path = ROOT / "writings/preface/chapters/preface.md"
    text = path.read_text()
    if "skill-navigation-row-157" in text and "### Row 157 skill checkpoint" in text:
        print("preface: row 157 already present")
        return
    m = re.search(
        r"(### Row 137 skill checkpoint.*?)(?=\n### Row 138 skill checkpoint|\n## The copper wire through the book)",
        text,
        re.S,
    )
    if not m:
        raise SystemExit("preface row 137 checkpoint missing")
    block = lift_137_to_157(m.group(1))
    anchor = "\n## The copper wire through the book"
    idx = text.find(anchor)
    if idx < 0:
        raise SystemExit("copper wire anchor missing")
    text = text[:idx] + "\n" + block + text[idx:]
    # Update row 156 tail to point at row 157
    text = text.replace(
        "When row 156 is complete, proceed to [row 157](preface.md#skill-navigation-row-157) when `murnaghan_eos.yaml` exists but IX.2 still feels disconnected from verified Born–Oppenheimer meta prelude capstone on the full capstone path",
        "When row 156 is complete, proceed to [row 157](preface.md#skill-navigation-row-157) when `murnaghan_eos.yaml` exists but IX.2 still feels disconnected from verified Born–Oppenheimer meta prelude capstone on the full capstone path",
    )
    path.write_text(text)
    print("preface: added row 157")


def insert_epilogue_loop() -> None:
    path = ROOT / "writings/epilogue/chapters/multiscale.md"
    text = path.read_text()
    if "row-157-closing-loop" in text:
        print("epilogue: row 157 loop already present")
        return
    block = lift_137_to_157(
        extract_between(text, "### Row 137 closing loop", "### Row 118 closing loop")
    )
    text = text.replace("### Row 156 closing loop", block + "### Row 156 closing loop", 1)
    path.write_text(text)
    print("epilogue: added row 157 loop")


def add_prologue_compass() -> None:
    path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    text = path.read_text()
    line156 = "| Row 68 → Row 136 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone reunion (row 156) |"
    if "| Row 68 → Row 137 Row 68 → Row 57 Kohn–Sham meta prelude capstone reunion (row 157) |" in text:
        print("prologue: row 157 compass already present")
        return
    idx = text.find(line156)
    if idx < 0:
        raise SystemExit("prologue row 156 compass line not found")
    line_end = text.find("\n", idx)
    line137 = "| Row 68 → Row 117 Row 68 → Row 57 Kohn–Sham meta capstone reunion (row 137) |"
    idx137 = text.find(line137)
    if idx137 < 0:
        raise SystemExit("prologue row 137 compass line not found")
    line_end137 = text.find("\n", idx137)
    new_line = lift_137_to_157(text[idx137:line_end137]) + "\n"
    text = text[: line_end + 1] + new_line + text[line_end + 1 :]

    preview_src = '| <span id="prologue-preview-row-137"></span>'
    if preview_src in text and "prologue-preview-row-157" not in text:
        i = text.find(preview_src)
        j = text.find("\n|", i + 1)
        preview_block = lift_137_to_157(text[i:j])
        text = text.replace(preview_src, preview_block + preview_src, 1)

    if "row-157-closing-stitch" not in text:
        stitch = (
            "**Row 157 closing stitch (Row 68 → Row 137 Row 68 → Row 57 Kohn–Sham meta prelude capstone reunion).** {#row-157-closing-stitch} "
            "When row 156 closed — Born–Oppenheimer meta prelude capstone verified, row 155 or row 136 recited on the full capstone path, and IX.1 Bridge → IX.2 Kohn–Sham SCF recited with "
            "[Murnaghan Lab act](../part09-dft/01-born-oppenheimer.md#lab-act-murnaghan-fit-on-fcc-cu-act-vi--foundation) archived `murnaghan_eos.yaml` — but **row 57 IX.1 → IX.2 opening hinge still opens like standalone quantum chemistry homework after the BO/HK Scene on the full capstone path** — "
            "the [preface row 157 When-to-pause opening sentence](../preface.md#skill-navigation-row-157) names the dual reunion before DFT workflows meta prelude capstone; read [preface row 157](../preface.md#skill-navigation-row-157), then the "
            "[Row 68 → Row 137 reunion index](../appendix/sources.md#row68-row137-kohn-sham-meta-prelude-capstone-reunion-index-row-157), then "
            "[epilogue row 157 closing loop](../epilogue/multiscale.md#row-157-closing-loop) before row 58 DFT workflows meta prelude capstone opens on the full capstone path.\n\n"
        )
        text = text.replace("**Row 156 closing stitch", stitch + "**Row 156 closing stitch", 1)
    path.write_text(text)
    print("prologue: added row 157 compass/preview/stitch")


def add_sources_row() -> None:
    path = ROOT / "writings/appendix/chapters/sources.md"
    text = path.read_text()
    idx_key = "row68-row137-kohn-sham-meta-prelude-capstone-reunion-index-row-157"
    if idx_key in text:
        print("sources: row 157 already present")
        return
    ns137 = runpy.run_path(str(ROOT / "scripts/add-row-137.py"))
    block = lift_137_to_157(
        ns137["lift_117_to_137"](
            extract_between(
                text,
                "## Row 68 → Row 97 Row 68 → Row 57 Kohn–Sham meta capstone reunion index (row 117)",
                "## Row 68 → Row 98 Row 68 → Row 58 DFT workflows meta capstone reunion index (row 118)",
            )
        )
    )
    block = (
        "## Row 68 → Row 137 Row 68 → Row 57 Kohn–Sham meta prelude capstone reunion index (row 157) "
        f"{{#{idx_key}}}"
        + block.split("{#row68-row117-kohn-sham-meta-capstone-reunion-index-row-137}", 1)[-1]
    )
    table_row = (
        "| 157 | Row 68 → Row 137 Row 68 → Row 57 Kohn–Sham meta prelude capstone "
        "(midpoint prelude gate ↔ Born–Oppenheimer meta prelude capstone ↔ row 57 meta) | "
        f"[Row 68 → Row 137 Kohn–Sham meta prelude capstone reunion index](#{idx_key}) · "
        "[preface row 157](../preface.md#skill-navigation-row-157) · "
        "[prologue row 157 preview](../prologue/00-many-scales.md#prologue-preview-row-157) · "
        "[prologue row 157 closing stitch](../prologue/00-many-scales.md#row-157-closing-stitch) · "
        "[epilogue row 157 closing loop](../epilogue/multiscale.md#row-157-closing-loop) · "
        "[memory sheet row 157 baby picture](memory-sheet.md#row-157-baby-picture-row68-row137-kohn-sham-meta-prelude-capstone-reunion) | "
        "Row 68 closed but **row 57 IX.1 → IX.2 opening hinge still feels disconnected from verified Born–Oppenheimer meta prelude capstone on the full capstone path** — "
        "read row 68 + row 156 or row 137 gate + IX.1 Bridge → opening hinge → IX.2 Kohn–Sham SCF + row 57; "
        "[preface row 57](../preface.md#skill-navigation-row-57) |\n"
    )
    text = text.replace(
        "| 156 | Row 68 → Row 136 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone",
        table_row + "| 156 | Row 68 → Row 136 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone",
    )
    text = text.replace(
        "## Row 68 → Row 136 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone reunion index (row 156)",
        block + "## Row 68 → Row 136 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone reunion index (row 156)",
    )
    path.write_text(text)
    print("sources: added row 157")


def add_memory_row() -> None:
    path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    text = path.read_text()
    if "row-157-baby-picture" in text:
        print("memory-sheet: row 157 already present")
        return
    baby = lift_137_to_157(extract_between(text, "### Row 137 baby picture", "### Row 138 baby picture"))
    text = text.replace("### Row 138 baby picture", baby + "### Row 138 baby picture", 1)
    mem_table = (
        "| 157 | Meta | Row 68 → Row 137 Row 68 → Row 57 Kohn–Sham meta prelude capstone reunion | "
        "[Row 68 → Row 137 Kohn–Sham meta prelude capstone reunion index](sources.md#row68-row137-kohn-sham-meta-prelude-capstone-reunion-index-row-157) · "
        "[preface row 157 skill checkpoint](../preface.md#skill-navigation-row-157) · "
        "[prologue row 157 preview](../prologue/00-many-scales.md#prologue-preview-row-157) · "
        "[prologue row 157 closing stitch](../prologue/00-many-scales.md#row-157-closing-stitch) · "
        "[epilogue row 157 closing loop](../epilogue/multiscale.md#row-157-closing-loop) | "
        "Row 68 closed but row 57 IX.1 → IX.2 opening hinge feels disconnected from verified Born–Oppenheimer meta prelude capstone on the full capstone path — "
        "read row 68 + row 156 or row 137 gate + IX.1 Bridge → opening hinge → IX.2 Kohn–Sham SCF + row 57; "
        "[row 157 baby picture](#row-157-baby-picture-row68-row137-kohn-sham-meta-prelude-capstone-reunion) |\n"
    )
    text = text.replace(
        "| 156 | Meta | Row 68 → Row 136 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone reunion |",
        mem_table + "| 156 | Meta | Row 68 → Row 136 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone reunion |",
    )
    if "When row 156 closed but Kohn–Sham meta reunion still lags" not in text:
        text = text.replace(
            "When row 155 closed but Born–Oppenheimer meta reunion still lags on the full capstone path, switch to [row 156](#row-156-baby-picture-row68-row136-born-oppenheimer-meta-prelude-capstone-reunion).",
            "When row 155 closed but Born–Oppenheimer meta reunion still lags on the full capstone path, switch to [row 156](#row-156-baby-picture-row68-row136-born-oppenheimer-meta-prelude-capstone-reunion). "
            "When row 156 closed but Kohn–Sham meta reunion still lags on the full capstone path, switch to [row 157](#row-157-baby-picture-row68-row137-kohn-sham-meta-prelude-capstone-reunion).",
        )
    path.write_text(text)
    print("memory-sheet: added row 157")


def patch_row_156_tail() -> None:
    preface = ROOT / "writings/preface/chapters/preface.md"
    text = preface.read_text()
    old = "when opening [row 157](preface.md#skill-navigation-row-156)"
    if old in text:
        text = text.replace(
            old,
            "when opening [row 157](preface.md#skill-navigation-row-157) before row 57 closes on the full capstone path",
        )
    preface.write_text(text)


def main() -> None:
    fix_row_156_preface()
    ensure_row_137_preface()
    insert_preface_row()
    insert_epilogue_loop()
    add_prologue_compass()
    add_sources_row()
    add_memory_row()
    patch_row_156_tail()
    subprocess.run([sys.executable, str(ROOT / "scripts/fix-prologue-row-157.py")], check=True)


if __name__ == "__main__":
    main()
