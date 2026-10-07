#!/usr/bin/env python3
"""Add row 202 meta-stitch (Row 68 → Row 182 ↔ Row 62 Handshake 4b meta prelude capstone, full capstone path)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Reuse the proven row-181 → row-201 lift, composed with 4b ↔ 4a row renumbering.
from importlib.util import module_from_spec, spec_from_file_location

_spec = spec_from_file_location("row201", ROOT / "scripts/add-row-201.py")
_row201 = module_from_spec(_spec)
assert _spec.loader is not None
_spec.loader.exec_module(_row201)
t181_to_201 = _row201.t181_to_201


def _downgrade_182_to_181(text: str) -> str:
    """Map row-182 (Handshake 4b) prose to row-181 (Handshake 4a) template numbers."""
    out = text.replace("row 203", "__R203__")
    out = out.replace("row 202", "__R202__")
    out = out.replace("row 201", "__R201__")
    repl = [
        ("Row 68 → Row 182 Row 68 → Row 62", "Row 68 → Row 161 Row 68 → Row 61"),
        (
            "row68-row182-handshake4b-meta-prelude-capstone-reunion-index-row-202",
            "row68-row161-handshake4a-meta-prelude-capstone-reunion-index-row-181",
        ),
        (
            "row-202-baby-picture-row68-row182-handshake4b-meta-prelude-capstone-reunion",
            "row-181-baby-picture-row68-row161-handshake4a-meta-prelude-capstone-reunion",
        ),
        ("skill-navigation-row-202", "skill-navigation-row-181"),
        ("prologue-preview-row-202", "prologue-preview-row-181"),
        ("row-202-closing-stitch", "row-181-closing-stitch"),
        ("row-202-closing-loop", "row-181-closing-loop"),
        ("handshake4b", "handshake4a"),
        ("Handshake 4b", "Handshake 4a"),
        ("FE² cross-links", "rate cross-links"),
        ("FE² notch-localization", "rate extrapolation"),
        ("fe2_export.yaml", "rate_export.yaml"),
        ("parse_fe2.sh", "parse_rate.sh"),
        ("opening-hinge-vii3-handshake4b", "opening-hinge-vii3-handshake4a"),
        ("notch-root", "power-law"),
    ]
    for a, b in repl:
        out = out.replace(a, b)
    out = out.replace("row 182", "row 181")
    out = out.replace("Row 182", "Row 181")
    out = out.replace("row 162", "row 161")
    out = out.replace("row 62", "row 61")
    out = out.replace("__R201__", "row 200")
    out = out.replace("__R202__", "row 181")
    out = out.replace("__R203__", "row 182")
    return out


def _upgrade_201_to_202(text: str) -> str:
    """Map row-201 lift output back to row-202 Handshake 4b capstone path."""
    out = text.replace("row 203", "__R203__")
    out = out.replace("row 202", "__R202__")
    out = out.replace("row 201", "__R201__")
    repl = [
        ("Row 68 → Row 181 Row 68 → Row 61", "Row 68 → Row 182 Row 68 → Row 62"),
        (
            "row68-row181-handshake4a-meta-prelude-capstone-reunion-index-row-201",
            "row68-row182-handshake4b-meta-prelude-capstone-reunion-index-row-202",
        ),
        (
            "row-201-baby-picture-row68-row181-handshake4a-meta-prelude-capstone-reunion",
            "row-202-baby-picture-row68-row182-handshake4b-meta-prelude-capstone-reunion",
        ),
        ("skill-navigation-row-201", "skill-navigation-row-202"),
        ("prologue-preview-row-201", "prologue-preview-row-202"),
        ("row-201-closing-stitch", "row-202-closing-stitch"),
        ("row-201-closing-loop", "row-202-closing-loop"),
        ("handshake4a", "handshake4b"),
        ("Handshake 4a", "Handshake 4b"),
        ("rate cross-links", "FE² cross-links"),
        ("rate extrapolation", "FE² notch-localization"),
        ("rate_export.yaml", "fe2_export.yaml"),
        ("parse_rate.sh", "parse_fe2.sh"),
        ("opening-hinge-vii3-handshake4a", "opening-hinge-vii3-handshake4b"),
        ("power-law", "notch-root"),
    ]
    for a, b in repl:
        out = out.replace(a, b)
    out = out.replace("row 181", "row 182")
    out = out.replace("Row 181", "Row 182")
    out = out.replace("row 161", "row 162")
    out = out.replace("row 61", "row 62")
    out = out.replace("__R201__", "row 202")
    out = out.replace("__R202__", "row 203")
    out = out.replace("__R203__", "row 203")
    out = out.replace("row 200", "row 201")
    out = out.replace("Row 200", "Row 201")
    return out


def t182_to_202(text: str) -> str:
    return _upgrade_201_to_202(t181_to_201(_downgrade_182_to_181(text)))


def _build_blocks() -> dict[str, str]:
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    prologue = (ROOT / "writings/prologue/chapters/00-many-scales.md").read_text()
    epilogue = (ROOT / "writings/epilogue/chapters/multiscale.md").read_text()
    sources = (ROOT / "writings/appendix/chapters/sources.md").read_text()
    memory = (ROOT / "writings/appendix/chapters/memory-sheet.md").read_text()

    start = preface.index("### Row 182 skill checkpoint")
    end = preface.index("\n\n### Row 183 skill checkpoint", start)
    row202_preface = t182_to_202(preface[start:end]) + "\n\n"

    row182_stitch = next(line for line in prologue.splitlines() if line.startswith("**Row 182 closing stitch"))

    prologue_compass = (
        "| Row 68 → Row 182 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion (row 202) | "
        "[Preface: row 202 skill checkpoint](../preface.md#skill-navigation-row-202) · "
        "[Row 68 → Row 182 Handshake 4b meta prelude capstone reunion index](../appendix/sources.md#row68-row182-handshake4b-meta-prelude-capstone-reunion-index-row-202) · "
        "[memory sheet row 202 baby picture](../appendix/memory-sheet.md#row-202-baby-picture-row68-row182-handshake4b-meta-prelude-capstone-reunion) · "
        "[prologue row 202 preview row](#prologue-preview-row-202); [prologue row 202 closing stitch](#row-202-closing-stitch); "
        "[epilogue row 202 closing loop](../epilogue/multiscale.md#row-202-closing-loop) — "
        "read row 68 gate + row 201 or row 182 Handshake 4b meta prelude capstone / Handshake 4b meta capstone gate + epilogue FE² cross-links + row 62 meta aloud "
        "when bulk hardening matches flow stress after verified Handshake 4b meta prelude capstone on the full capstone path but Handshake 4b still feels disconnected from Part VII Step 4 |\n"
    )

    prologue_preview = (
        '| <span id="prologue-preview-row-202"></span>Row 202 preview (Row 68 → Row 182 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion) | '
        "Explain why midpoint closure (row 68) and Handshake 4b meta (row 62) must be read together with the epilogue FE² cross-links and discretization chain after verified Handshake 4b meta prelude capstone on the full capstone path before Act IV hardening and Act V notch localization feel like separate courses | "
        'One sentence: "read row 68 gate + row 201 or row 182 Handshake 4b meta prelude capstone / Handshake 4b meta capstone gate + epilogue FE² cross-links + row 62 meta aloud when bulk hardening matches flow stress after verified Handshake 4b meta prelude capstone on the full capstone path but FE² exports feed the orchestration deck without notch-root extrapolation" — '
        "[preface row 202 skill checkpoint](../preface.md#skill-navigation-row-202); [prologue row 202 closing stitch](#row-202-closing-stitch); "
        "[Row 68 → Row 182 reunion index](../appendix/sources.md#row68-row182-handshake4b-meta-prelude-capstone-reunion-index-row-202); "
        "[memory sheet row 202 baby picture](../appendix/memory-sheet.md#row-202-baby-picture-row68-row182-handshake4b-meta-prelude-capstone-reunion); "
        "[preface row 201 skill checkpoint](../preface.md#skill-navigation-row-201); "
        "[epilogue row 202 closing loop](../epilogue/multiscale.md#row-202-closing-loop) |\n"
    )

    row182_loop_anchor = (
        "### Row 182 closing loop (Row 68 → Row 162 Row 68 → Row 62 "
        "Handshake 4b meta prelude capstone reunion) {#row-182-closing-loop}"
    )
    row181_loop_end = (
        "### Row 181 closing loop (Row 68 → Row 161 Row 68 → Row 61 "
        "Handshake 4a meta prelude capstone reunion) {#row-181-closing-loop}"
    )
    epilogue_loop = t182_to_202(
        row182_loop_anchor
        + epilogue.split(row182_loop_anchor, 1)[1].split(row181_loop_end, 1)[0]
    )

    src182_header = "## Row 68 → Row 162 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion index (row 182)"
    next183_header = "## Row 68 → Row 163 Row 68 → Row 63 orchestration meta prelude capstone reunion index (row 183)"
    sources_index = t182_to_202(sources.split(src182_header, 1)[1].split(next183_header, 1)[0])
    sources_index = (
        "## Row 68 → Row 182 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion index (row 202)"
        + sources_index
    )

    sources_table = next(
        line for line in sources.splitlines() if line.startswith("| 162 | Row 68 → Row 162")
    )
    sources_table = t182_to_202(sources_table).replace("| 162 | Row 68 → Row 162", "| 202 | Row 68 → Row 182", 1) + "\n"

    memory_table = next(
        line for line in memory.splitlines() if line.startswith("| 201 | Meta |")
    )
    memory_table = t182_to_202(memory_table).replace("| 201 | Meta |", "| 202 | Meta |", 1) + "\n"

    baby_anchor = (
        "### Row 201 baby picture (Row 68 → Row 181 Row 68 → Row 61 "
        "Handshake 4a meta prelude capstone reunion)"
    )
    baby_end = "### Row 190 baby picture"
    memory_baby = t182_to_202(
        baby_anchor + memory.split(baby_anchor, 1)[1].split(baby_end, 1)[0]
    )

    return {
        "row202_preface": row202_preface,
        "prologue_compass": prologue_compass,
        "prologue_stitch": t182_to_202(row182_stitch) + "\n\n",
        "prologue_preview": prologue_preview,
        "epilogue_loop": epilogue_loop,
        "sources_table": sources_table,
        "sources_index": sources_index,
        "memory_table": memory_table,
        "memory_baby": memory_baby,
    }


ROW201_TAIL_MARKER = "When row 201 is complete, proceed to [row 182](preface.md#skill-navigation-row-182)"

ROW201_EPILOGUE_OLD = (
    "Proceed to [row 182](#row-182-closing-loop) when row 68 closed but Handshake 4b meta still feels disconnected after row 201 on the full capstone path,"
)
ROW201_EPILOGUE_NEW = (
    "Proceed to [row 202](#row-202-closing-loop) when row 68 closed but Handshake 4b meta still feels disconnected after row 201 on the full capstone path,"
)

ROW201_EPILOGUE_BEFORE_OLD = (
    "before row 203 orchestration meta prelude capstone reunion on the full capstone path (then row 183 orchestration on the full capstone path)."
)
ROW201_EPILOGUE_BEFORE_NEW = (
    "before row 203 orchestration meta prelude capstone reunion on the full capstone path (then row 183 orchestration on the full capstone path)."
)


def main() -> None:
    b = _build_blocks()

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    copper = "\n## The copper wire through the book"
    if "### Row 202 skill checkpoint" in preface:
        print("preface: row 202 already present")
    else:
        if ROW201_TAIL_MARKER not in preface:
            raise SystemExit("row 201 tail proceed marker not found")
        preface = preface.replace(
            ROW201_TAIL_MARKER,
            "When row 201 is complete, proceed to [row 202](preface.md#skill-navigation-row-202)",
            1,
        )
        preface = preface.replace(copper, "\n" + b["row202_preface"] + copper)
        preface_path.write_text(preface)
        print("preface: added row 202")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "**Row 202 closing stitch" not in prologue:
        needle = "| Row 68 → Row 181 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion (row 201) |"
        if needle not in prologue:
            raise SystemExit("prologue compass row 201 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + b["prologue_compass"] + prologue[line_end + 1 :]
        prologue = prologue.replace(
            "**Row 201 closing stitch",
            b["prologue_stitch"] + "**Row 201 closing stitch",
            1,
        )
        preview_anchor = '| <span id="prologue-preview-row-201"></span>Row 201 preview'
        prologue = prologue.replace(preview_anchor, b["prologue_preview"] + preview_anchor)
        prologue_path.write_text(prologue)
        print("prologue: added row 202")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if "### Row 202 closing loop" not in epilogue:
        if ROW201_EPILOGUE_OLD in epilogue:
            epilogue = epilogue.replace(ROW201_EPILOGUE_OLD, ROW201_EPILOGUE_NEW, 1)
        marker = "### Row 186 closing loop (Row 68 → Row 166 Row 68 → Row 66 Writings canonical meta prelude capstone reunion)"
        if marker not in epilogue:
            raise SystemExit("epilogue row 186 insert anchor not found")
        epilogue = epilogue.replace(marker, b["epilogue_loop"] + "\n\n" + marker, 1)
        epilogue_path.write_text(epilogue)
        print("epilogue: added row 202")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row182-handshake4b-meta-prelude-capstone-reunion-index-row-202" not in sources:
        sources = sources.replace(
            "| 201 | Row 68 → Row 181 Row 68 → Row 61 Handshake 4a meta prelude capstone",
            b["sources_table"] + "| 201 | Row 68 → Row 181 Row 68 → Row 61 Handshake 4a meta prelude capstone",
            1,
        )
        sources = sources.replace(
            src182_header := "## Row 68 → Row 162 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion index (row 182)",
            b["sources_index"] + src182_header,
            1,
        )
        sources_path.write_text(sources)
        print("sources: added row 202")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-202-baby-picture-row68-row182" not in memory:
        memory = memory.replace(
            "| 201 | Meta | [Row 68 → Row 181 Handshake 4a meta prelude capstone reunion index]",
            b["memory_table"] + "| 201 | Meta | [Row 68 → Row 181 Handshake 4a meta prelude capstone reunion index]",
            1,
        )
        memory = memory.replace(
            "### Row 201 baby picture (Row 68 → Row 181 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion)",
            b["memory_baby"]
            + "### Row 201 baby picture (Row 68 → Row 181 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion)",
            1,
        )
        memory_path.write_text(memory)
        print("memory-sheet: added row 202")


if __name__ == "__main__":
    main()
