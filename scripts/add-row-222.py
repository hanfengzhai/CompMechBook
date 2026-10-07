#!/usr/bin/env python3
"""Add row 222 meta-stitch (Row 68 → Row 202 ↔ Row 62 Handshake 4b meta prelude capstone reunion, full capstone path)."""
from pathlib import Path
import importlib.util

ROOT = Path(__file__).resolve().parents[1]


def lift202_to_222(text: str) -> str:
    """Lift row-202 capstone meta copy to row 222 (+20 capstone path: 182→202 index, 202→222 checkpoint)."""
    out = text.replace("row 223", "__R223__")
    out = out.replace("row 222", "__R222__")
    out = out.replace("row 203", "__R203__")
    out = out.replace("row 202", "__R202__")
    repl = [
        ("Row 68 → Row 182 Row 68 → Row 62", "Row 68 → Row 202 Row 68 → Row 62"),
        (
            "row68-row182-handshake4b-meta-prelude-capstone-reunion-index-row-202",
            "row68-row202-handshake4b-meta-prelude-capstone-reunion-index-row-222",
        ),
        (
            "row-202-baby-picture-row68-row182-handshake4b-meta-prelude-capstone-reunion",
            "row-222-baby-picture-row68-row202-handshake4b-meta-prelude-capstone-reunion",
        ),
        ("prologue-preview-row-202", "prologue-preview-row-222"),
        ("row-202-closing-stitch", "row-222-closing-stitch"),
        ("row-202-closing-loop", "row-222-closing-loop"),
        ("Row 202 three-way audit", "Row 222 three-way audit"),
        (
            "verified Handshake 4a meta prelude capstone closure (row 201)",
            "verified Handshake 4a meta prelude capstone closure (row 221)",
        ),
        (
            "before row 203 orchestration meta prelude capstone opens on the full capstone path",
            "before row 223 orchestration meta prelude capstone opens on the full capstone path",
        ),
        (
            "before row 203 orchestration meta prelude capstone reunion on the full capstone path",
            "before row 223 orchestration meta prelude capstone reunion on the full capstone path",
        ),
    ]
    for old, new in repl:
        out = out.replace(old, new)
    out = out.replace("skill-navigation-row-202", "skill-navigation-row-222")
    out = out.replace("row 201](preface.md#skill-navigation-row-201)", "row 221](preface.md#skill-navigation-row-221)")
    out = out.replace(
        "[row 201](preface.md#skill-navigation-row-201) or [row 202](preface.md#skill-navigation-row-182)",
        "[row 221](preface.md#skill-navigation-row-221) or [row 202](preface.md#skill-navigation-row-202)",
    )
    out = out.replace("row 182](preface.md#skill-navigation-row-182)", "row 202](preface.md#skill-navigation-row-202)")
    out = out.replace("row 182's epilogue FE²", "row 202's epilogue FE²")
    out = out.replace("| 202 |", "| 222 |")
    out = out.replace("memory sheet row 202", "memory sheet row 222")
    out = out.replace("prologue row 202", "prologue row 222")
    out = out.replace("epilogue row 202", "epilogue row 222")
    out = out.replace("When row 202 is complete", "When row 222 is complete")
    out = out.replace("proceed to [row 203](preface.md#skill-navigation-row-203)", "proceed to [row 223](preface.md#skill-navigation-row-223)")
    out = out.replace("row 202 closed but row 62", "row 221 closed but row 62")
    out = out.replace("when row 201 closed but row 62", "when row 221 closed but row 62")
    out = out.replace("after row 201 on the full capstone path", "after row 221 on the full capstone path")
    out = out.replace("when row 201 and row 62", "when row 221 and row 62")
    out = out.replace("row 201's Handshake 4a meta", "row 221's Handshake 4a meta")
    out = out.replace("Row 202 does not replace", "Row 222 does not replace")
    out = out.replace("Row 202 three-way", "Row 222 three-way")
    out = out.replace("Row 182 Handshake 4b meta prelude capstone reunion index (row 202)", "Row 202 Handshake 4b meta prelude capstone reunion index (row 222)")
    out = out.replace("Row 68 → Row 182 Handshake 4b meta prelude capstone reunion index (row 202)", "Row 68 → Row 202 Handshake 4b meta prelude capstone reunion index (row 222)")
    out = out.replace("Row 68 → Row 202 reunion index", "Row 68 → Row 202 reunion index")
    out = out.replace("__R202__", "row 222")
    out = out.replace("__R203__", "row 223")
    out = out.replace("__R222__", "row 222")
    out = out.replace("__R223__", "row 223")
    return out


def _load_add202():
    spec = importlib.util.spec_from_file_location("add202", ROOT / "scripts/add-row-202.py")
    add202 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(add202)
    return add202


def _build_blocks() -> dict[str, str]:
    add202 = _load_add202()
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    start = preface.index("### Row 202 skill checkpoint")
    end = preface.index("\n\n### Row 203 skill checkpoint", start)
    row222_preface = lift202_to_222(preface[start:end]) + "\n\n"
    row222_preface = row222_preface.replace(
        "### Row 202 skill checkpoint",
        "### Row 222 skill checkpoint",
        1,
    ).replace("{#skill-navigation-row-202}", "{#skill-navigation-row-222}", 1)

    b202 = add202._build_blocks()
    prologue_stitch = lift202_to_222(
        b202["prologue_stitch"].replace("{#row-202-closing-stitch}", "{#row-222-closing-stitch}").replace(
            "**Row 202 closing stitch (Row 68 → Row 182",
            "**Row 222 closing stitch (Row 68 → Row 202",
        )
    )
    prologue_compass = lift202_to_222(b202["prologue_compass"])
    prologue_preview = lift202_to_222(b202["prologue_preview"])

    epilogue_loop = lift202_to_222(b202["epilogue_loop"])
    epilogue_loop = epilogue_loop.replace("{#row-202-closing-loop}", "{#row-222-closing-loop}", 1)
    epilogue_loop = epilogue_loop.replace("{#row-182-closing-loop}", "{#row-222-closing-loop}", 1)

    sources = (ROOT / "writings/appendix/chapters/sources.md").read_text()
    src202_header = (
        "## Row 68 → Row 182 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion index (row 202)"
    )
    next203_header = (
        "## Row 68 → Row 183 Row 68 → Row 63 orchestration meta prelude capstone reunion index (row 203)"
    )
    sources_index = lift202_to_222(sources.split(src202_header, 1)[1].split(next203_header, 1)[0])
    sources_index = (
        "## Row 68 → Row 202 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion index (row 222) "
        "{#row68-row202-handshake4b-meta-prelude-capstone-reunion-index-row-222}"
        + sources_index
    )

    sources_table = lift202_to_222(b202["sources_table"])
    sources_table = sources_table.replace("| 222 | Row 68 → Row 202", "| 222 | Row 68 → Row 202", 1)

    memory_table = lift202_to_222(b202["memory_table"])
    memory_table = memory_table.replace("| 202 | Meta |", "| 222 | Meta |", 1)

    memory_baby = lift202_to_222(b202["memory_baby"])
    if "{#row-222-baby-picture-row68-row202" not in memory_baby:
        memory_baby = memory_baby.replace(
            "### Row 202 baby picture (Row 68 → Row 182 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion)",
            "### Row 222 baby picture {#row-222-baby-picture-row68-row202-handshake4b-meta-prelude-capstone-reunion} (Row 68 → Row 202 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion)",
            1,
        )
        memory_baby = memory_baby.replace(
            "### Row 202 baby picture (Row 68 → Row 182 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion)",
            "### Row 222 baby picture {#row-222-baby-picture-row68-row202-handshake4b-meta-prelude-capstone-reunion} (Row 68 → Row 202 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion)",
            1,
        )

    return {
        "row222_preface": row222_preface,
        "prologue_compass": prologue_compass,
        "prologue_stitch": prologue_stitch,
        "prologue_preview": prologue_preview,
        "epilogue_loop": epilogue_loop,
        "sources_table": sources_table,
        "sources_index": sources_index,
        "memory_baby": memory_baby,
        "memory_table": memory_table,
    }


ROW221_TAIL_MARKER = (
    "When row 221 is complete, proceed to [row 202](preface.md#skill-navigation-row-202)"
)

ROW221_EPILOGUE_OLD = (
    "Proceed to [row 201](#row-201-closing-loop) when row 68 closed but Handshake 4b meta still feels disconnected after row 200 on the full capstone path,"
)
ROW221_EPILOGUE_NEW = (
    "Proceed to [row 222](#row-222-closing-loop) when row 68 closed but Handshake 4b meta still feels disconnected after row 221 on the full capstone path,"
)

ROW221_EPILOGUE_BEFORE_OLD = (
    "before row 222 Handshake 4b meta prelude capstone reunion on the full capstone path (then row 202 Handshake 4b on the full capstone path)."
)
ROW221_EPILOGUE_BEFORE_NEW = (
    "before row 223 orchestration meta prelude capstone reunion on the full capstone path (then row 203 orchestration on the full capstone path)."
)


def main() -> None:
    b = _build_blocks()
    copper = "\n## The copper wire through the book"

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    if "### Row 222 skill checkpoint" in preface:
        print("preface: row 222 already present")
    else:
        if ROW221_TAIL_MARKER not in preface:
            raise SystemExit("row 221 tail proceed marker not found")
        preface = preface.replace(
            ROW221_TAIL_MARKER,
            "When row 221 is complete, proceed to [row 222](preface.md#skill-navigation-row-222)",
            1,
        )
        preface = preface.replace(copper, "\n" + b["row222_preface"] + copper, 1)
        preface_path.write_text(preface)
        print("preface: added row 222")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "prologue-preview-row-222" not in prologue:
        needle = "| Row 68 → Row 182 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion (row 202) |"
        if needle not in prologue:
            raise SystemExit("prologue compass row 202 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + b["prologue_compass"] + prologue[line_end + 1 :]
        if "**Row 222 closing stitch" not in prologue:
            prologue = prologue.replace(
                "**Row 202 closing stitch",
                b["prologue_stitch"] + "**Row 202 closing stitch",
                1,
            )
        preview_anchor = '| <span id="prologue-preview-row-202"></span>Row 202 preview'
        prologue = prologue.replace(preview_anchor, b["prologue_preview"] + preview_anchor)
        prologue_path.write_text(prologue)
        print("prologue: added row 222")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if "{#row-222-closing-loop}" not in epilogue:
        if ROW221_EPILOGUE_OLD in epilogue:
            epilogue = epilogue.replace(ROW221_EPILOGUE_OLD, ROW221_EPILOGUE_NEW, 1)
        if ROW221_EPILOGUE_BEFORE_OLD in epilogue:
            epilogue = epilogue.replace(ROW221_EPILOGUE_BEFORE_OLD, ROW221_EPILOGUE_BEFORE_NEW, 1)
        marker = (
            "### Row 186 closing loop (Row 68 → Row 166 Row 68 → Row 66 Writings canonical meta prelude capstone reunion)"
        )
        if marker not in epilogue:
            raise SystemExit("epilogue row 186 insert anchor not found")
        epilogue = epilogue.replace(marker, b["epilogue_loop"] + "\n\n" + marker, 1)
        epilogue_path.write_text(epilogue)
        print("epilogue: added row 222")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row202-handshake4b-meta-prelude-capstone-reunion-index-row-222" not in sources:
        sources = sources.replace(
            "| 202 | Row 68 → Row 182 Row 68 → Row 62 Handshake 4b meta prelude capstone",
            b["sources_table"] + "| 202 | Row 68 → Row 182 Row 68 → Row 62 Handshake 4b meta prelude capstone",
            1,
        )
        src202_header = (
            "## Row 68 → Row 182 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion index (row 202)"
        )
        sources = sources.replace(src202_header, b["sources_index"] + src202_header, 1)
        sources_path.write_text(sources)
        print("sources: added row 222")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-222-baby-picture-row68-row202" not in memory:
        memory = memory.replace(
            "| 202 | Meta | [Row 68 → Row 182 Handshake 4b meta prelude capstone reunion index]",
            b["memory_table"] + "| 202 | Meta | [Row 68 → Row 182 Handshake 4b meta prelude capstone reunion index]",
            1,
        )
        baby_anchor = (
            "### Row 202 baby picture (Row 68 → Row 202 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion) — read"
        )
        if baby_anchor not in memory:
            baby_anchor = (
                "### Row 202 baby picture (Row 68 → Row 182 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion)"
            )
        if baby_anchor not in memory:
            raise SystemExit("memory baby picture anchor not found")
        memory = memory.replace(baby_anchor, b["memory_baby"] + baby_anchor, 1)
        memory_path.write_text(memory)
        print("memory-sheet: added row 222")


if __name__ == "__main__":
    main()
