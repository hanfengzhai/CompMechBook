#!/usr/bin/env python3
"""Add row 158 meta-stitch (Row 68 → Row 138 ↔ Row 58 DFT workflows meta prelude capstone, full capstone path)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def t138_to_158(text: str) -> str:
    """Transform row-138 full-capstone meta copy to row 158 (138→158, 118→138 inner, 137→157 gate)."""
    repl = [
        ("Row 68 → Row 118 Row 68 → Row 58", "Row 68 → Row 138 Row 68 → Row 58"),
        ("row68-row118-dft-workflows-meta-prelude-capstone-reunion-index-row-138",
         "row68-row138-dft-workflows-meta-prelude-capstone-reunion-index-row-158"),
        ("row-138-baby-picture-row68-row118-dft-workflows-meta-prelude-capstone-reunion",
         "row-158-baby-picture-row68-row138-dft-workflows-meta-prelude-capstone-reunion"),
        ("skill-navigation-row-138", "skill-navigation-row-158"),
        ("prologue-preview-row-138", "prologue-preview-row-158"),
        ("row-138-closing-stitch", "row-158-closing-stitch"),
        ("row-138-closing-loop", "row-158-closing-loop"),
        ("Row 118 three-way audit", "Row 158 three-way audit"),
        ("[row 137](preface.md#skill-navigation-row-137) or [row 118](preface.md#skill-navigation-row-118)",
         "[row 157](preface.md#skill-navigation-row-157) or [row 138](preface.md#skill-navigation-row-138)"),
        ("[row 137](preface.md#skill-navigation-row-137) or [Row 68 → Row 98",
         "[row 157](preface.md#skill-navigation-row-157) or [Row 68 → Row 118"),
        ("row 137", "row 157"),
        ("row 118", "row 138"),
        ("on the capstone path", "on the full capstone path"),
        ("(capstone path)", "(full capstone path)"),
        ("Row 68 ↔ Row 58 reunion", "Row 68 ↔ Row 58 reunion (full capstone path)"),
        ("row 138", "row 158"),
        ("Row 138", "Row 158"),
        ("row 157", "row 157"),  # no-op safeguard after above — fix over-replace below
    ]
    out = text
    for old, new in repl:
        out = out.replace(old, new)
    # Restore gate row numbers accidentally replaced
    out = out.replace("[row 158](preface.md#skill-navigation-row-157)", "[row 157](preface.md#skill-navigation-row-157)")
    out = out.replace("row 1587", "row 157")
    out = out.replace("row 1586", "row 156")
    out = out.replace("row 158 or row 158", "row 157 or row 138")
    out = out.replace("When row 158 closed — Kohn–Sham", "When row 157 closed — Kohn–Sham")
    out = out.replace("row 158 closed Kohn–Sham", "row 157 closed Kohn–Sham")
    out = out.replace("after row 158 alone", "after row 157 alone")
    out = out.replace("Recite [preface row 158]", "Recite [preface row 157]")
    out = out.replace("row 158 or row 138 recited", "row 157 or row 138 recited")
    out = out.replace("from row 158's", "from row 157's")
    out = out.replace("row 158 when `cutoff", "row 157 when `cutoff")
    out = out.replace("row 158 DFT workflows meta prelude capstone reunion index (row 158)",
                       "row 158 DFT workflows meta prelude capstone reunion index (row 158)")
    out = out.replace(
        "before row 159 Handshake 3 meta prelude capstone opens on the full capstone path",
        "before row 139 Handshake 3 meta prelude capstone opens on the full capstone path",
    )
    out = out.replace(
        "Do not conflate row 158 (row 68 ↔ row 58 reunion on the full capstone path) with row 138 (opening-hinge capstone stitch alone) — row 138 names **Row 68 → Row 98",
        "Do not conflate row 158 (row 68 ↔ row 58 reunion on the full capstone path) with row 138 (opening-hinge capstone stitch alone) — row 138 names **Row 68 → Row 118",
    )
    out = out.replace(
        "why that reunion must follow verified Kohn–Sham meta prelude capstone (row 157) and the outer midpoint prelude gate (row 68)**",
        "why that reunion must follow verified Kohn–Sham meta prelude capstone (row 157) and the outer midpoint prelude gate (row 68)**",
    )
    out = out.replace(
        "Proceed to [row 139](#row-139-closing-loop) when row 68 closed but Handshake 3 meta prelude capstone still lags after row 158 on the full capstone path",
        "Proceed to [row 139](#row-139-closing-loop) when row 68 closed but Handshake 3 meta prelude capstone still lags after row 158 on the full capstone path",
    )
    return out


def extract_preface_row138(preface: str) -> str:
    start = preface.index("### Row 138 skill checkpoint")
    end = preface.index("\n\n\n### Row 139 skill checkpoint")
    return preface[start:end]


ROW158_PREFACE = t138_to_158(extract_preface_row138(
    (ROOT / "writings/preface/chapters/preface.md").read_text()
)) + "\n\n"

PROLOGUE_COMPASS = (
    "| Row 68 → Row 138 Row 68 → Row 58 DFT workflows meta prelude capstone reunion (row 158) | "
    "[Preface: row 158 skill checkpoint](../preface.md#skill-navigation-row-158) · "
    "[Row 68 → Row 138 DFT workflows meta prelude capstone reunion index](../appendix/sources.md#row68-row138-dft-workflows-meta-prelude-capstone-reunion-index-row-158) · "
    "[memory sheet row 158 baby picture](../appendix/memory-sheet.md#row-158-baby-picture-row68-row138-dft-workflows-meta-prelude-capstone-reunion) · "
    "[prologue row 158 preview row](#prologue-preview-row-158); [prologue row 158 closing stitch](#row-158-closing-stitch); "
    "[epilogue row 158 closing loop](../epilogue/multiscale.md#row-158-closing-loop) — "
    "read row 68 gate + row 157 or row 138 Kohn–Sham meta prelude capstone / DFT workflows opening gate + IX.2 Bridge → opening hinge → IX.3 calculation ladder + row 58 meta aloud "
    "when cutoff certificates are clean on the full capstone path but DFT workflows still feel like standalone coursework after verified Kohn–Sham meta prelude capstone |\n"
)

PROLOGUE_STITCH = t138_to_158(
    "**Row 138 closing stitch (Row 68 → Row 118 Row 68 → Row 58 DFT workflows meta prelude capstone reunion).** {#row-138-closing-stitch} "
    "When row 137 closed — Kohn–Sham meta prelude capstone verified, row 136 or row 117 recited on the capstone path, and IX.1 Bridge → IX.2 SCF recited with "
    "[cutoff-sweep Lab act](../part09-dft/02-kohn-sham.md#lab-act-cutoff-sweep-on-fcc-cu-act-vi--convergence-certificate) archived `cutoff_convergence.yaml` and converged `scf_ecut*.out` — "
    "but **row 58 IX.2 → IX.3 opening hinge still opens like standalone DFT coursework after the SCF implementation Scene on the capstone path** — "
    "`writings/dft` chapters 02 and 03 build as separate reading acts, Quantum ESPRESSO workflows and `cu.foundation/` feel disconnected from "
    "[cutoff export manifest](../part09-dft/02-kohn-sham.md#cutoff-export-manifest-handoff-to-ix3) and the Bridge line that named missing input decks, "
    "or row 58's Bridge → workflow archive gate feels disconnected from row 137's fixed-point → calculation ladder turn on the capstone path while the unified HTML reads smoothly — "
    "the [preface row 138 When-to-pause opening sentence](../preface.md#skill-navigation-row-138) names the dual reunion before Handshake 3 meta prelude capstone on the capstone path; "
    "read [preface row 138](../preface.md#skill-navigation-row-138), then the "
    "[Row 68 → Row 118 reunion index](../appendix/sources.md#row68-row118-dft-workflows-meta-prelude-capstone-reunion-index-row-138), then "
    "[epilogue row 138 closing loop](../epilogue/multiscale.md#row-138-closing-loop) before row 139 Handshake 3 meta prelude capstone opens on the capstone path.\n\n"
)

PROLOGUE_PREVIEW = (
    "| <span id=\"prologue-preview-row-158\"></span>Row 158 preview (Row 68 → Row 138 Row 68 → Row 58 DFT workflows meta prelude capstone reunion) | "
    "Explain why midpoint closure (row 68) and IX.2 → IX.3 meta (row 58) must be read together with the Bridge → calculation ladder chain "
    "after verified Kohn–Sham meta prelude capstone on the full capstone path before cutoff certificates and `cu.foundation/` feel like separate courses | "
    "One sentence: \"read row 68 gate + row 157 or row 138 Kohn–Sham meta prelude capstone / DFT workflows opening gate + IX.2 Bridge → opening hinge → IX.3 calculation ladder + row 58 meta aloud "
    "when cutoff certificates are clean on the full capstone path but DFT workflows still feel like standalone coursework after verified Kohn–Sham meta prelude capstone\" — "
    "[preface row 158 skill checkpoint](../preface.md#skill-navigation-row-158); [prologue row 158 closing stitch](#row-158-closing-stitch); "
    "[Row 68 → Row 138 reunion index](../appendix/sources.md#row68-row138-dft-workflows-meta-prelude-capstone-reunion-index-row-158); "
    "[memory sheet row 158 baby picture](../appendix/memory-sheet.md#row-158-baby-picture-row68-row138-dft-workflows-meta-prelude-capstone-reunion); "
    "[IX.2 Bridge](../part09-dft/02-kohn-sham.md#bridge); "
    "[IX.3 opening hinge from IX.2](../part09-dft/03-dft-workflows.md#opening-hinge-ix2-to-ix3); "
    "[preface row 58 skill checkpoint](../preface.md#skill-navigation-row-58); "
    "[preface row 157 skill checkpoint](../preface.md#skill-navigation-row-157); "
    "[epilogue row 158 closing loop](../epilogue/multiscale.md#row-158-closing-loop) |\n"
)

EPILOGUE_LOOP = t138_to_158(
    (ROOT / "writings/epilogue/chapters/multiscale.md").read_text().split("### Row 138 closing loop")[1].split("### Row 139 closing loop")[0]
)
EPILOGUE_LOOP = "### Row 158 closing loop" + EPILOGUE_LOOP.split("}", 1)[1]
EPILOGUE_LOOP = EPILOGUE_LOOP.replace(
    "Row 118 closes the **DFT workflows meta prelude capstone",
    "Row 158 closes the **DFT workflows meta prelude capstone",
)
EPILOGUE_LOOP = t138_to_158("### Row 138 closing loop" + EPILOGUE_LOOP[len("### Row 158 closing loop"):])
# Fix header after t138_to_158
EPILOGUE_LOOP = EPILOGUE_LOOP.replace("### Row 158 closing loop (Row 68 → Row 138", "### Row 158 closing loop (Row 68 → Row 138", 1)

SOURCES_TABLE = (
    "| 158 | Row 68 → Row 138 Row 68 → Row 58 DFT workflows meta prelude capstone (midpoint prelude gate ↔ Kohn–Sham meta prelude capstone on full capstone path ↔ row 58 meta) | "
    "[Row 68 → Row 138 DFT workflows meta prelude capstone reunion index](#row68-row138-dft-workflows-meta-prelude-capstone-reunion-index-row-158) · "
    "[preface row 158](../preface.md#skill-navigation-row-158) · "
    "[prologue row 158 preview](../prologue/00-many-scales.md#prologue-preview-row-158) · "
    "[prologue row 158 closing stitch](../prologue/00-many-scales.md#row-158-closing-stitch) · "
    "[epilogue row 158 closing loop](../epilogue/multiscale.md#row-158-closing-loop) · "
    "[memory sheet row 158 baby picture](memory-sheet.md#row-158-baby-picture-row68-row138-dft-workflows-meta-prelude-capstone-reunion) | "
    "Row 68 closed but **row 58 IX.2 → IX.3 opening hinge still feels disconnected from verified Kohn–Sham meta prelude capstone on the full capstone path** — "
    "read row 68 + row 157 or row 138 gate + IX.2 Bridge → opening hinge → IX.3 calculation ladder + row 58; "
    "[preface row 58](../preface.md#skill-navigation-row-58) |\n"
)

SOURCES_INDEX = t138_to_158(
    (ROOT / "writings/appendix/chapters/sources.md").read_text().split(
        "## Row 68 → Row 118 Row 68 → Row 58 DFT workflows meta prelude capstone reunion index (row 138)"
    )[1].split("## Continuous read-through guide")[0]
)
SOURCES_INDEX = "## Row 68 → Row 138 Row 68 → Row 58 DFT workflows meta prelude capstone reunion index (row 158)" + SOURCES_INDEX
# Table layer fixes for 158 index
SOURCES_INDEX = SOURCES_INDEX.replace(
    "| [Row 137 reunion (Kohn–Sham meta prelude capstone)](#row68-row117-kohn-sham-meta-prelude-capstone-reunion-index-row-137) | Kohn–Sham meta prelude capstone | \"Row 137 or row 118 gate before IX.2 Bridge\" | Cutoff yaml clean but IX.3 opens early on capstone path |",
    "| [Row 157 reunion (Kohn–Sham meta prelude capstone)](#row68-row137-kohn-sham-meta-prelude-capstone-reunion-index-row-157) | Kohn–Sham meta prelude capstone | \"Row 157 or row 138 gate before IX.2 Bridge\" | Cutoff yaml clean but IX.3 opens early on full capstone path |",
)
SOURCES_INDEX = SOURCES_INDEX.replace(
    "| [Row 118 reunion (meta capstone)](#row68-row98-dft-workflows-meta-capstone-reunion-index-row-118) | DFT workflows meta capstone | \"Row 68 gate + capstone before row 58\" | Row 137 only; IX.2 Bridge chain skipped |",
    "| [Row 158 reunion (meta prelude capstone)](#row68-row138-dft-workflows-meta-prelude-capstone-reunion-index-row-158) | DFT workflows meta prelude capstone | \"Row 68 gate + capstone before row 58\" | Row 157 only; IX.2 Bridge chain skipped |",
)
SOURCES_INDEX = SOURCES_INDEX.replace(
    "| [Row 58 reunion (meta)](#ix2-ix3-opening-hinge-reunion-index-row-58) | DFT workflows prelude meta | \"Row 138 gate + Bridge before IX.3 foundation archive\" | Row 118 only; row 58 meta skipped |",
    "| [Row 58 reunion (meta)](#ix2-ix3-opening-hinge-reunion-index-row-58) | DFT workflows prelude meta | \"Row 158 gate + Bridge before IX.3 foundation archive\" | Row 138 only; row 58 meta skipped |",
)
SOURCES_INDEX = SOURCES_INDEX.replace(
    "Row 118 names **Row 68 → Row 98 Row 68 → Row 58 DFT workflows meta capstone reunion** at opening-hinge capstone depth",
    "Row 138 names **Row 68 → Row 118 Row 68 → Row 58 DFT workflows meta prelude capstone reunion** at opening-hinge capstone depth",
)
SOURCES_INDEX = SOURCES_INDEX.replace(
    "row 137 names **Row 68 → Row 117 Row 68 → Row 57 Kohn–Sham meta prelude capstone reunion** when Born–Oppenheimer meta prelude capstone and IX.1 → IX.2 meta must read as one afternoon on the capstone path. Row 138 names **Row 68 → Row 118",
    "row 157 names **Row 68 → Row 137 Row 68 → Row 57 Kohn–Sham meta prelude capstone reunion** when Born–Oppenheimer meta prelude capstone and IX.1 → IX.2 meta must read as one afternoon on the full capstone path. Row 158 names **Row 68 → Row 138",
)

MEMORY_TABLE = (
    "| 158 | Meta | [Row 68 → Row 138 DFT workflows meta prelude capstone reunion index](sources.md#row68-row138-dft-workflows-meta-prelude-capstone-reunion-index-row-158) · "
    "[preface row 158 skill checkpoint](../preface.md#skill-navigation-row-158) · "
    "[prologue row 158 preview](../prologue/00-many-scales.md#prologue-preview-row-158) · "
    "[prologue row 158 closing stitch](../prologue/00-many-scales.md#row-158-closing-stitch) · "
    "[epilogue row 158 closing loop](../epilogue/multiscale.md#row-158-closing-loop) | "
    "Row 68 closed but row 58 IX.2 → IX.3 opening hinge feels disconnected from verified Kohn–Sham meta prelude capstone on the full capstone path — "
    "read row 68 + row 157 or row 138 gate + IX.2 Bridge → opening hinge → IX.3 calculation ladder + row 58; "
    "[row 158 baby picture](#row-158-baby-picture-row68-row138-dft-workflows-meta-prelude-capstone-reunion) |\n"
)

MEMORY_BABY = t138_to_158(
    """### Row 138 baby picture (Row 68 → Row 118 Row 68 → Row 58 DFT workflows meta prelude capstone reunion) {#row-138-baby-picture-row68-row118-dft-workflows-meta-prelude-capstone-reunion}

**Row 138 baby picture:** when row 68 closed the midpoint prelude and row 137 or row 118 closed Kohn–Sham meta prelude capstone / DFT workflows opening prelude but **row 58's IX.2 → IX.3 audit or the Bridge → calculation ladder chain still feel like separate checklists on the capstone path**, open the [Row 68 → Row 118 DFT workflows meta prelude capstone reunion index](sources.md#row68-row118-dft-workflows-meta-prelude-capstone-reunion-index-row-138) — read [preface row 68](../preface.md#skill-navigation-row-68) gate → [preface row 137](../preface.md#skill-navigation-row-137) or [preface row 118](../preface.md#skill-navigation-row-118) Kohn–Sham meta prelude capstone / DFT workflows opening gate → [IX.2 Bridge](../part09-dft/02-kohn-sham.md#bridge) through [IX.3 opening hinge from IX.2](../part09-dft/03-dft-workflows.md#opening-hinge-ix2-to-ix3) aloud → [preface row 58](../preface.md#skill-navigation-row-58) five-step audit → confirm [cutoff-sweep Lab act steps 1–5](../part09-dft/02-kohn-sham.md#lab-act-cutoff-sweep-on-fcc-cu-act-vi--convergence-certificate) and [cutoff export manifest](../part09-dft/02-kohn-sham.md#cutoff-export-manifest-handoff-to-ix3) at \\(T_w\\) on the capstone path.

```mermaid
flowchart LR
  MP[Midpoint row 68]
  KS[Kohn–Sham meta prelude capstone row 137]
  BR[IX.2 Bridge to IX.3]
  R58[row 58 meta gate]
  MP --> KS --> BR --> R58
```

When row 138 feels disconnected from row 137, read them as **Kohn–Sham meta prelude capstone vs DFT workflows meta prelude capstones on the capstone path**: row 137 when **IX.1 Bridge and Row 68 → Row 57 meta must read on the same wire before any IX.2 → IX.3 audit on the capstone path**; row 138 when **IX.2 Bridge and Row 68 → Row 58 meta must read on the same wire before row 139 Handshake 3 meta prelude capstone opens on the capstone path** — same copper wire, same Functional Analysis Notes layout, one continuous cutoff certificate → `cu.foundation/` afternoon after verified Kohn–Sham meta prelude capstone.


"""
).replace("row 137", "row 157").replace("row 118", "row 138").replace("row 138", "row 158", 1)
MEMORY_BABY = MEMORY_BABY.replace("Kohn–Sham meta prelude capstone row 137", "Kohn–Sham meta prelude capstone row 157")
MEMORY_BABY = t138_to_158(MEMORY_BABY)


ROW157_TAIL_OLD = (
    "Read the [memory sheet row 157 baby picture](appendix/memory-sheet.md#row-157-baby-picture-row68-row137-kohn-sham-meta-prelude-capstone-reunion) when opening [row 138](preface.md#skill-navigation-row-138) before row 57 closes on the full capstone path; read the [epilogue row 157 closing loop](epilogue/multiscale.md#row-157-closing-loop) when the competence loop closes. When row 157 is complete, proceed to [row 138](preface.md#skill-navigation-row-138) when `cutoff_convergence.yaml` exists but IX.3 still feels disconnected from verified Kohn–Sham meta prelude capstone on the full capstone path, to [row 118](preface.md#skill-navigation-row-118) for the Row 68 ↔ Row 58 DFT workflows meta audit on the opening-hinge prelude path alone, to [row 117](preface.md#skill-navigation-row-117) for the Row 68 ↔ Row 57 Kohn–Sham meta audit on the opening-hinge capstone path alone, to [row 137](preface.md#skill-navigation-row-137) for the Row 68 ↔ Row 57 Kohn–Sham meta audit on the opening-hinge capstone path alone,"
)
ROW157_TAIL_NEW = (
    "Read the [memory sheet row 157 baby picture](appendix/memory-sheet.md#row-157-baby-picture-row68-row137-kohn-sham-meta-prelude-capstone-reunion) when opening [row 158](preface.md#skill-navigation-row-158) before row 58 closes on the full capstone path; read the [epilogue row 157 closing loop](epilogue/multiscale.md#row-157-closing-loop) when the competence loop closes. When row 157 is complete, proceed to [row 158](preface.md#skill-navigation-row-158) when `cutoff_convergence.yaml` exists but IX.3 still feels disconnected from verified Kohn–Sham meta prelude capstone on the full capstone path, to [row 138](preface.md#skill-navigation-row-138) for the Row 68 ↔ Row 58 DFT workflows meta audit on the opening-hinge capstone path alone, to [row 118](preface.md#skill-navigation-row-118) for the Row 68 ↔ Row 58 DFT workflows meta audit on the opening-hinge prelude path alone, to [row 117](preface.md#skill-navigation-row-117) for the Row 68 ↔ Row 57 Kohn–Sham meta audit on the opening-hinge capstone path alone, to [row 137](preface.md#skill-navigation-row-137) for the Row 68 ↔ Row 57 Kohn–Sham meta audit on the opening-hinge capstone path alone,"
)


def main():
    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    anchor = "\n## The copper wire through the book"
    if "skill-navigation-row-158" in preface:
        print("preface: row 158 already present")
    else:
        if ROW157_TAIL_OLD not in preface:
            raise SystemExit("preface row 157 tail not found")
        preface = preface.replace(ROW157_TAIL_OLD, ROW157_TAIL_NEW)
        preface = preface.replace(
            "before row 138 DFT workflows meta prelude capstone reunion opens on the full capstone path",
            "before row 158 DFT workflows meta prelude capstone reunion opens on the full capstone path",
        )
        preface = preface.replace(anchor, ROW158_PREFACE + anchor)
        preface_path.write_text(preface)
        print("preface: added row 158")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "prologue-preview-row-158" not in prologue:
        needle = "| Row 68 → Row 137 Row 68 → Row 57 Kohn–Sham meta prelude capstone reunion (row 157) |"
        if needle not in prologue:
            raise SystemExit("prologue compass row 157 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + PROLOGUE_COMPASS + prologue[line_end + 1 :]
        prologue = prologue.replace(
            "**Row 157 closing stitch",
            PROLOGUE_STITCH + "**Row 157 closing stitch",
        )
        prologue = prologue.replace(
            '| <span id="prologue-preview-row-157"></span>Row 157 preview',
            PROLOGUE_PREVIEW + '| <span id="prologue-preview-row-157"></span>Row 157 preview',
        )
        prologue_path.write_text(prologue)
        print("prologue: added row 158")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if "row-158-closing-loop" not in epilogue:
        epilogue = epilogue.replace(
            "Proceed to [row 138](#row-138-closing-loop) when row 68 closed but DFT workflows meta prelude capstone still lags after row 157 on the full capstone path",
            "Proceed to [row 158](#row-158-closing-loop) when row 68 closed but DFT workflows meta prelude capstone still lags after row 157 on the full capstone path, to [row 138](#row-138-closing-loop) when row 68 closed but DFT workflows meta prelude capstone still lags after row 137 on the opening-hinge capstone path alone",
        )
        epilogue = epilogue.replace(
            "before row 138 DFT workflows meta prelude capstone opens in workflow time on the full capstone path.",
            "before row 158 DFT workflows meta prelude capstone opens in workflow time on the full capstone path.",
        )
        epilogue = epilogue.replace(
            "### Row 135 closing loop (Row 68 → Row 115",
            EPILOGUE_LOOP + "\n\n### Row 135 closing loop (Row 68 → Row 115",
        )
        epilogue_path.write_text(epilogue)
        print("epilogue: added row 158")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row138-dft-workflows-meta-prelude-capstone-reunion-index-row-158" not in sources:
        sources = sources.replace(
            "| 157 | Row 68 → Row 137 Row 68 → Row 57 Kohn–Sham meta prelude capstone",
            SOURCES_TABLE + "| 157 | Row 68 → Row 137 Row 68 → Row 57 Kohn–Sham meta prelude capstone",
        )
        sources = sources.replace(
            "before row 138 DFT workflows meta prelude capstone opens in workflow time on the full capstone path.",
            "before row 158 DFT workflows meta prelude capstone opens in workflow time on the full capstone path.",
        )
        sources = sources.replace(
            "## Continuous read-through guide {#continuous-read-through-guide}",
            SOURCES_INDEX + "\n## Continuous read-through guide {#continuous-read-through-guide}",
        )
        sources = sources.replace(
            "[row 138](#row68-row118-dft-workflows-meta-prelude-capstone-reunion-index-row-138) reunites **Kohn–Sham meta prelude capstone with the DFT workflows meta boundary on the capstone path** when row 137 closed Kohn–Sham meta prelude capstone at verified `cutoff_convergence.yaml` but IX.2 → IX.3 opening hinge still reads like separate courses on the capstone path;",
            "[row 138](#row68-row118-dft-workflows-meta-prelude-capstone-reunion-index-row-138) reunites **Kohn–Sham meta prelude capstone with the DFT workflows meta boundary on the capstone path** when row 137 closed Kohn–Sham meta prelude capstone at verified `cutoff_convergence.yaml` but IX.2 → IX.3 opening hinge still reads like separate courses on the capstone path; [row 158](#row68-row138-dft-workflows-meta-prelude-capstone-reunion-index-row-158) reunites **Kohn–Sham meta prelude capstone with the DFT workflows meta boundary on the full capstone path** when row 157 closed Kohn–Sham meta prelude capstone at verified `cutoff_convergence.yaml` but IX.2 → IX.3 opening hinge still reads like separate courses on the full capstone path;",
        )
        sources_path.write_text(sources)
        print("sources: added row 158")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-158-baby-picture-row68-row138" not in memory:
        memory = memory.replace(
            "| 157 | Meta | [Row 68 → Row 137 Kohn–Sham meta prelude capstone reunion index]",
            MEMORY_TABLE + "| 157 | Meta | [Row 68 → Row 137 Kohn–Sham meta prelude capstone reunion index]",
        )
        memory = memory.replace(
            "before row 138 DFT workflows meta prelude capstone opens on the full capstone path**",
            "before row 158 DFT workflows meta prelude capstone opens on the full capstone path**",
        )
        memory = memory.replace(
            "### Row 131 baby picture (Row 68 → Row 111 Row 68 → Row 51 homogenization meta prelude capstone reunion)",
            MEMORY_BABY + "### Row 131 baby picture (Row 68 → Row 111 Row 68 → Row 51 homogenization meta prelude capstone reunion)",
        )
        memory_path.write_text(memory)
        print("memory-sheet: added row 158")


if __name__ == "__main__":
    main()
