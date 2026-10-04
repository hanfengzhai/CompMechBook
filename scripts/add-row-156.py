#!/usr/bin/env python3
"""Add row 156 (Row 68 → Row 136 ↔ Row 56 Born–Oppenheimer meta prelude capstone on full capstone path)."""
from __future__ import annotations

import re
import runpy
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GOLD_REF = "origin/cursor/computational-mechanics-book-0a8a"


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


def git_show(path: str) -> str:
    r = subprocess.run(
        ["git", "show", f"{GOLD_REF}:{path}"],
        capture_output=True,
        text=True,
        check=False,
    )
    if r.returncode != 0:
        raise SystemExit(f"cannot read {GOLD_REF}:{path}: {r.stderr}")
    return r.stdout


def lift_136_to_156(s: str) -> str:
    """Promote opening-hinge row 136 checkpoint to full-capstone row 156 wording."""
    p = [
        ("skill-navigation-row-136", "skill-navigation-row-156"),
        ("### Row 136 skill checkpoint", "### Row 156 skill checkpoint"),
        ("Row 136 does not replace", "Row 156 does not replace"),
        ("Row 136 three-way audit", "Row 156 three-way audit"),
        ("Row 136 closing loop", "Row 156 closing loop"),
        ("row-136-closing-loop", "row-156-closing-loop"),
        ("Row 136 closing stitch", "Row 156 closing stitch"),
        ("row-136-closing-stitch", "row-156-closing-stitch"),
        ("prologue-preview-row-136", "prologue-preview-row-156"),
        ("Row 136 preview", "Row 156 preview"),
        ("Row 136 skill checkpoint", "Row 156 skill checkpoint"),
        ("memory sheet row 136", "memory sheet row 156"),
        ("Row 136 baby picture", "Row 156 baby picture"),
        (
            "Row 68 → Row 116 Row 68 → Row 56 Born–Oppenheimer meta capstone",
            "Row 68 → Row 136 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone",
        ),
        (
            "row68-row116-born-oppenheimer-meta-capstone-reunion-index-row-136",
            "row68-row136-born-oppenheimer-meta-prelude-capstone-reunion-index-row-156",
        ),
        (
            "row-136-baby-picture-row68-row116-born-oppenheimer-meta-capstone-reunion",
            "row-156-baby-picture-row68-row136-born-oppenheimer-meta-prelude-capstone-reunion",
        ),
        ("[row 137]", "__ROW157__"),
        ("[row 135]", "[row 155]"),
        ("row 135", "row 155"),
        ("Row 135", "Row 155"),
        ("__ROW157__", "[row 157]"),
        (
            "Row 68 → Row 116 Born–Oppenheimer meta capstone reunion index (row 136)",
            "Row 68 → Row 136 Born–Oppenheimer meta prelude capstone reunion index (row 156)",
        ),
        (
            "Born–Oppenheimer meta capstone reunion index (row 136)",
            "Born–Oppenheimer meta prelude capstone reunion index (row 156)",
        ),
        ("Born–Oppenheimer meta capstone reunion", "Born–Oppenheimer meta prelude capstone reunion"),
        ("Born–Oppenheimer meta capstone", "Born–Oppenheimer meta prelude capstone"),
        ("born-oppenheimer-meta-capstone-reunion", "born-oppenheimer-meta-prelude-capstone-reunion"),
        (
            "verified electronic audit meta prelude capstone closure with the full-book IX.0 → IX.1 Born–Oppenheimer meta prelude capstone reunion",
            "verified electronic audit meta prelude capstone closure (row 155) with the full-book IX.0 → IX.1 Born–Oppenheimer meta reunion (row 56)",
        ),
        (
            "or [row 116](preface.md#skill-navigation-row-96) closed",
            "or [row 136](preface.md#skill-navigation-row-136) closed",
        ),
        (
            "Born–Oppenheimer opening prelude hinge on the capstone path (VIII.3 Bridge → IX.0 SCF recited",
            "Born–Oppenheimer opening prelude hinge (IX.0 Bridge → foundation SCF recited on the full capstone path",
        ),
        (
            "one dft arc under `writings/dft` chapters 00–01), but",
            "one dft arc under `writings/dft` chapters 00–01 after verified electronic audit meta prelude capstone), but",
        ),
        (
            "after IX.0's foundation SCF audit Lab act on the capstone path**",
            "after IX.0's foundation SCF audit Lab act on the full capstone path**",
        ),
        (
            "Born–Oppenheimer meta prelude capstone boundary inside the coupling gate on the capstone path",
            "Born–Oppenheimer meta prelude capstone boundary inside the dft subtree on the full capstone path",
        ),
        (
            "Row 156 does not replace row 68, row 56, row 155, row 136, row 116, row 96, row 76, or row 37",
            "Row 156 does not replace row 68, row 56, row 155, row 136, row 116, row 96, row 76, row 115, row 55, row 154, or row 37",
        ),
        (
            "before row 57 Kohn–Sham meta prelude opens on the capstone path at \\(T_w\\)",
            "before IX.2 opens at \\(T_w\\) on the full capstone path",
        ),
        ("Row 68 ↔ Row 56 reunion (capstone path)", "Row 68 ↔ Row 56 reunion (full capstone path)"),
        (
            "[row 135](preface.md#skill-navigation-row-115) or [Row 68 → Row 116 Born–Oppenheimer meta prelude capstone reunion index (row 136)]",
            "[row 155](preface.md#skill-navigation-row-155) or [Row 68 → Row 116 Born–Oppenheimer meta prelude capstone reunion index (row 136)]",
        ),
        ("SCF log + `alpha_export.yaml` at \\(T_w\\) before IX.0 Bridge → BO",
            "SCF log + `alpha_export.yaml` at \\(T_w\\) on full capstone path before IX.0 Bridge → BO",
        ),
        (
            "when opening [row 117](preface.md#skill-navigation-row-117) before row 57 closes on the capstone path",
            "when opening [row 157](preface.md#skill-navigation-row-157) before row 56 closes on the full capstone path",
        ),
        (
            "When row 136 is complete, proceed to [row 137](preface.md#skill-navigation-row-137) when Born–Oppenheimer meta prelude capstone is clean but Kohn–Sham meta capstone still lags after verified Murnaghan archive on the capstone path, to [row 117](preface.md#skill-navigation-row-117) when Born–Oppenheimer meta prelude capstone is clean but Kohn–Sham meta capstone still lags on the opening-hinge path, to [row 97](preface.md#skill-navigation-row-117) for the Row 68 ↔ Row 57 Kohn–Sham opening prelude audit alone, to [row 136](preface.md#skill-navigation-row-136) when electronic audit meta prelude capstone still lags after verified foundation SCF on the capstone path, to [row 57](preface.md#skill-navigation-row-57) when only IX.1 → IX.2 stalls, or extend prose only under `writings/` then sync.",
            "When row 156 is complete, proceed to [row 157](preface.md#skill-navigation-row-157) when `murnaghan_eos.yaml` exists but IX.2 still feels disconnected from verified Born–Oppenheimer meta prelude capstone on the full capstone path, to [row 137](preface.md#skill-navigation-row-137) when `murnaghan_eos.yaml` exists but IX.2 still feels disconnected on the opening-hinge capstone path alone, to [row 116](preface.md#skill-navigation-row-116) for the Row 68 ↔ Row 56 Born–Oppenheimer meta audit on the opening-hinge prelude path alone, to [row 115](preface.md#skill-navigation-row-115) for the Row 68 ↔ Row 55 electronic audit meta audit on the opening-hinge prelude path alone, to [row 154](preface.md#skill-navigation-row-154) when `cu.relax.out` is missing after verified export meta prelude capstone on the full capstone path, to [row 134](preface.md#skill-navigation-row-134) for the Row 68 ↔ Row 54 export meta audit on the opening-hinge capstone path alone, to [row 136](preface.md#skill-navigation-row-136) for the Row 68 ↔ Row 56 Born–Oppenheimer meta audit on the opening-hinge capstone path alone, to [row 155](preface.md#skill-navigation-row-155) when foundation SCF is clean but Born–Oppenheimer still stalls on the full capstone path, to [row 56](preface.md#skill-navigation-row-56) when only IX.0 → IX.1 stalls, or extend prose only under `writings/` then sync.",
        ),
        (
            "when row 155 closed but row 56 IX.0 → IX.1 reunion still feels like quantum chemistry homework disconnected from verified electronic audit meta prelude capstone on the capstone path — it names the dual reunion before the Murnaghan Lab act",
            "when row 155 closed but row 56 IX.0 → IX.1 reunion still feels like quantum chemistry homework disconnected from verified electronic audit meta prelude capstone on the full capstone path — it names the dual reunion before Kohn–Sham meta prelude capstone",
        ),
        (
            "when `cu.relax.out` exists on the capstone path but \\(V_{\\text{BO}}\\) is unnamed after row 155",
            "when `cu.relax.out` exists on the full capstone path but \\(V_{\\text{BO}}\\) is unnamed after row 155",
        ),
        (
            "Row 68 → Row 116 reunion index",
            "Row 68 → Row 136 reunion index",
        ),
        (
            "when opening [row 116](preface.md#skill-navigation-row-136) before row 56 closes on the capstone path",
            "when opening [row 156](preface.md#skill-navigation-row-156) before row 56 closes on the full capstone path",
        ),
        (
            "When row 155 is complete, proceed to [row 156]",
            "When row 155 is complete, proceed to [row 156]",
        ),
        (
            "Proceed to [row 156](#row-155-closing-loop) when row 68 closed but Born–Oppenheimer meta capstone still lags after row 155 on the capstone path",
            "Proceed to [row 156](#row-155-closing-loop) when row 68 closed but Born–Oppenheimer meta prelude capstone still lags after row 155 on the full capstone path",
        ),
        ("Recite [preface row 135]", "Recite [preface row 155]"),
        ("[row 115](preface.md#skill-navigation-row-115)", "[row 135](preface.md#skill-navigation-row-135)"),
        ("on the capstone path", "on the full capstone path"),
    ]
    out = tx(s, p)
    # Fix over-replacement in row 137+ references inside proceed links (row 157 should stay)
    out = out.replace("full full capstone path", "full capstone path")
    return out


def insert_preface_row() -> None:
    path = ROOT / "writings/preface/chapters/preface.md"
    text = path.read_text()
    if "skill-navigation-row-156" in text and "### Row 156 skill checkpoint" in text:
        print("preface: row 156 already present")
        return
    m = re.search(
        r"(### Row 136 skill checkpoint.*?)(?=\n### Row 137 skill checkpoint)",
        text,
        re.S,
    )
    if not m:
        raise SystemExit("preface row 136 checkpoint missing")
    block = lift_136_to_156(m.group(1))
    anchor = "\n## The copper wire through the book"
    idx = text.find(anchor)
    if idx < 0:
        raise SystemExit("copper wire anchor missing")
    text = text[:idx] + "\n" + block + text[idx:]
    path.write_text(text)
    print("preface: added row 156")


def insert_epilogue_loop() -> None:
    path = ROOT / "writings/epilogue/chapters/multiscale.md"
    text = path.read_text()
    if "row-156-closing-loop" in text:
        print("epilogue: row 156 loop already present")
        return
    block = lift_136_to_156(
        extract_between(text, "### Row 136 closing loop", "### Row 135 closing loop")
    )
    text = text.replace("### Row 155 closing loop", block + "### Row 155 closing loop", 1)
    path.write_text(text)
    print("epilogue: added row 156 loop")


def add_prologue_compass() -> None:
    path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    text = path.read_text()
    line155 = "| Row 68 → Row 135 Row 68 → Row 55 electronic audit meta prelude capstone reunion (row 155) |"
    if "| Row 68 → Row 136 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone reunion (row 156) |" in text:
        print("prologue: row 156 compass already present")
        return
    idx = text.find(line155)
    if idx < 0:
        raise SystemExit("prologue row 155 compass line not found")
    line_end = text.find("\n", idx)
    line136 = "| Row 68 → Row 136 Row 68 → Row 56 Born–Oppenheimer meta capstone reunion (row 136) |"
    idx136 = text.find(line136)
    if idx136 < 0:
        raise SystemExit("prologue row 136 compass line not found")
    line_end136 = text.find("\n", idx136)
    new_line = lift_136_to_156(text[idx136:line_end136]) + "\n"
    text = text[: line_end + 1] + new_line + text[line_end + 1 :]

    preview_src = '| <span id="prologue-preview-row-136"></span>'
    if preview_src in text and 'prologue-preview-row-156' not in text:
        i = text.find(preview_src)
        j = text.find("\n|", i + 1)
        preview_block = lift_136_to_156(text[i:j])
        text = text.replace(preview_src, preview_block + preview_src, 1)

    if "row-156-closing-stitch" not in text:
        stitch = (
            "**Row 156 closing stitch (Row 68 → Row 136 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone reunion).** {#row-156-closing-stitch} "
            "When row 155 closed — electronic audit meta prelude capstone verified, row 154 or row 135 recited on the full capstone path, and VIII.3 Bridge → IX.0 SCF recited with "
            "[foundation SCF audit Lab act](../part09-dft/00-opening.md#lab-act-foundation-scf-audit-before-born-oppenheimer-act-vi--foundation) archived `cu.relax.out` — but **row 56 IX.0 → IX.1 opening hinge still opens like standalone quantum chemistry homework after the electronic audit Scene on the full capstone path** — "
            "the [preface row 156 When-to-pause opening sentence](../preface.md#skill-navigation-row-156) names the dual reunion before Kohn–Sham meta prelude capstone; read [preface row 156](../preface.md#skill-navigation-row-156), then the "
            "[Row 68 → Row 136 reunion index](../appendix/sources.md#row68-row136-born-oppenheimer-meta-prelude-capstone-reunion-index-row-156), then "
            "[epilogue row 156 closing loop](../epilogue/multiscale.md#row-156-closing-loop) before row 57 Kohn–Sham meta prelude capstone opens on the full capstone path.\n\n"
        )
        text = text.replace("**Row 155 closing stitch", stitch + "**Row 155 closing stitch", 1)
    path.write_text(text)
    print("prologue: added row 156 compass/preview/stitch")


def add_sources_row() -> None:
    path = ROOT / "writings/appendix/chapters/sources.md"
    text = path.read_text()
    idx_key = "row68-row136-born-oppenheimer-meta-prelude-capstone-reunion-index-row-156"
    if idx_key in text:
        print("sources: row 156 already present")
        return
    ns137 = runpy.run_path(str(ROOT / "scripts/add-row-137.py"))
    lift_116_to_136 = ns137["lift_116_to_136"]
    block = lift_136_to_156(
        lift_116_to_136(
            extract_between(
                text,
                "## Row 68 → Row 96 Row 68 → Row 56 Born–Oppenheimer meta capstone reunion index (row 116)",
                "## Row 68 → Row 97 Row 68 → Row 57 Kohn–Sham meta capstone reunion index (row 117)",
            )
        )
    )
    block = (
        "## Row 68 → Row 136 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone reunion index (row 156) "
        f"{{#{idx_key}}}"
        + block.split("{#row68-row116-born-oppenheimer-meta-capstone-reunion-index-row-136}", 1)[-1]
    )
    table_row = (
        "| 156 | Row 68 → Row 136 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone "
        "(midpoint prelude gate ↔ electronic audit meta prelude capstone ↔ row 56 meta) | "
        f"[Row 68 → Row 136 Born–Oppenheimer meta prelude capstone reunion index](#{idx_key}) · "
        "[preface row 156](../preface.md#skill-navigation-row-156) · "
        "[prologue row 156 preview](../prologue/00-many-scales.md#prologue-preview-row-156) · "
        "[prologue row 156 closing stitch](../prologue/00-many-scales.md#row-156-closing-stitch) · "
        "[epilogue row 156 closing loop](../epilogue/multiscale.md#row-156-closing-loop) · "
        "[memory sheet row 156 baby picture](memory-sheet.md#row-156-baby-picture-row68-row136-born-oppenheimer-meta-prelude-capstone-reunion) | "
        "Row 68 closed but **row 56 IX.0 → IX.1 opening hinge still feels disconnected from verified electronic audit meta prelude capstone on the full capstone path** — "
        "read row 68 + row 155 or row 136 gate + IX.0 Bridge → opening hinge → IX.1 BO/HK + row 56; "
        "[preface row 56](../preface.md#skill-navigation-row-56) |\n"
    )
    text = text.replace(
        "| 155 | Row 68 → Row 135 Row 68 → Row 55 electronic audit meta prelude capstone",
        table_row + "| 155 | Row 68 → Row 135 Row 68 → Row 55 electronic audit meta prelude capstone",
    )
    text = text.replace(
        "## Row 68 → Row 135 Row 68 → Row 55 electronic audit meta prelude capstone reunion index (row 155)",
        block + "## Row 68 → Row 135 Row 68 → Row 55 electronic audit meta prelude capstone reunion index (row 155)",
    )
    path.write_text(text)
    print("sources: added row 156")


def add_memory_row() -> None:
    path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    text = path.read_text()
    if "row-156-baby-picture" in text:
        print("memory-sheet: row 156 already present")
        return
    baby = lift_136_to_156(extract_between(text, "### Row 136 baby picture", "### Row 137 baby picture"))
    text = text.replace("### Row 137 baby picture", baby + "### Row 137 baby picture", 1)
    mem_table = (
        "| 156 | Meta | Row 68 → Row 136 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone reunion | "
        "[Row 68 → Row 136 Born–Oppenheimer meta prelude capstone reunion index](sources.md#row68-row136-born-oppenheimer-meta-prelude-capstone-reunion-index-row-156) · "
        "[preface row 156 skill checkpoint](../preface.md#skill-navigation-row-156) · "
        "[prologue row 156 preview](../prologue/00-many-scales.md#prologue-preview-row-156) · "
        "[prologue row 156 closing stitch](../prologue/00-many-scales.md#row-156-closing-stitch) · "
        "[epilogue row 156 closing loop](../epilogue/multiscale.md#row-156-closing-loop) | "
        "Row 68 closed but row 56 IX.0 → IX.1 opening hinge feels disconnected from verified electronic audit meta prelude capstone on the full capstone path — "
        "read row 68 + row 155 or row 136 gate + IX.0 Bridge → opening hinge → IX.1 BO/HK + row 56; "
        "[row 156 baby picture](#row-156-baby-picture-row68-row136-born-oppenheimer-meta-prelude-capstone-reunion) |\n"
    )
    text = text.replace(
        "| 155 | Meta | Row 68 → Row 135 Row 68 → Row 55 electronic audit meta prelude capstone reunion |",
        mem_table + "| 155 | Meta | Row 68 → Row 135 Row 68 → Row 55 electronic audit meta prelude capstone reunion |",
    )
    if "When row 155 closed but Born–Oppenheimer meta reunion still lags" not in text:
        text = text.replace(
            "When row 154 closed but electronic audit meta reunion still lags on the capstone path, switch to [row 155](#row-155-baby-picture-row68-row135-electronic-audit-meta-prelude-capstone-reunion).",
            "When row 154 closed but electronic audit meta reunion still lags on the capstone path, switch to [row 155](#row-155-baby-picture-row68-row135-electronic-audit-meta-prelude-capstone-reunion). "
            "When row 155 closed but Born–Oppenheimer meta reunion still lags on the full capstone path, switch to [row 156](#row-156-baby-picture-row68-row136-born-oppenheimer-meta-prelude-capstone-reunion).",
        )
    path.write_text(text)
    print("memory-sheet: added row 156")


def patch_row_155_tail() -> None:
    preface = ROOT / "writings/preface/chapters/preface.md"
    text = preface.read_text()
    text = text.replace(
        "when opening [row 156](preface.md#skill-navigation-row-155) before row 56 closes",
        "when opening [row 156](preface.md#skill-navigation-row-156) before row 56 closes on the full capstone path",
    )
    preface.write_text(text)


def main() -> None:
    insert_preface_row()
    insert_epilogue_loop()
    add_prologue_compass()
    add_sources_row()
    add_memory_row()
    patch_row_155_tail()
    subprocess.run([sys.executable, str(ROOT / "scripts/fix-prologue-row-156.py")], check=True)


if __name__ == "__main__":
    main()
