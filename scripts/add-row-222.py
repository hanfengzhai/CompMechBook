#!/usr/bin/env python3
"""Add row 222 meta-stitch (Row 68 → Row 202 ↔ Row 62 Handshake 4b meta prelude capstone reunion, full capstone path)."""
from pathlib import Path
import importlib.util

ROOT = Path(__file__).resolve().parents[1]


def bump202_to_222(text: str) -> str:
    """Transform row-202 capstone-path meta copy to row 222 (182→202 inner, 221 Handshake 4a gate)."""
    out = text.replace("row 223", "TEMP_ROW223")
    out = text.replace("row 222", "TEMP_ROW222")
    out = text.replace("row 221", "TEMP_ROW221")
    repl = [
        ("Row 68 → Row 182 Row 68 → Row 62", "Row 68 → Row 202 Row 68 → Row 62"),
        (
            "row68-row182-handshake4b-meta-prelude-capstone-reunion-index-row-202",
            "TEMP_ROW222_HS4B_INDEX",
        ),
        (
            "row-202-baby-picture-row68-row182-handshake4b-meta-prelude-capstone-reunion",
            "row-222-baby-picture-row68-row202-handshake4b-meta-prelude-capstone-reunion",
        ),
        ("### Row 202 skill checkpoint", "### Row 222 skill checkpoint"),
        ("skill-navigation-row-202", "skill-navigation-row-222"),
        ("prologue-preview-row-202", "prologue-preview-row-222"),
        ("row-202-closing-stitch", "row-222-closing-stitch"),
        ("row-202-closing-loop", "row-222-closing-loop"),
        ("Row 202 three-way audit", "Row 222 three-way audit"),
        (
            "[row 201](preface.md#skill-navigation-row-201) or [row 182](preface.md#skill-navigation-row-182)",
            "[row 221](preface.md#skill-navigation-row-221) or [row 202](preface.md#skill-navigation-row-202)",
        ),
        (
            "[row 181](preface.md#skill-navigation-row-181) or [Row 68 → Row 182 Handshake 4b meta prelude capstone reunion index (row 202)](appendix/sources.md#row68-row182-handshake4b-meta-prelude-capstone-reunion-index-row-202)",
            "[row 221](preface.md#skill-navigation-row-221) or [Row 68 → Row 202 Handshake 4b meta prelude capstone reunion index (row 222)](appendix/sources.md#row68-row202-handshake4b-meta-prelude-capstone-reunion-index-row-222)",
        ),
        (
            "verified Handshake 4a meta prelude capstone closure (row 201)",
            "verified Handshake 4a meta prelude capstone closure (row 221)",
        ),
        (
            "before row 203 orchestration meta prelude capstone reunion opens on the full capstone path",
            "before row 223 orchestration meta prelude capstone reunion opens on the full capstone path",
        ),
    ]
    for old, new in repl:
        out = out.replace(old, new)
    out = out.replace(
        "TEMP_ROW222_HS4B_INDEX",
        "row68-row202-handshake4b-meta-prelude-capstone-reunion-index-row-222",
    )
    out = out.replace("Row 202 does not replace", "Row 222 does not replace")
    out = out.replace("When row 202 is complete", "When row 222 is complete")
    out = out.replace("When row 201 closed", "When row 221 closed")
    out = out.replace("when row 201 closed but row 62", "when row 221 closed but row 62")
    out = out.replace("after row 202 alone", "after row 222 alone")
    out = out.replace("Recite [preface row 201]", "Recite [preface row 221]")
    out = out.replace("row 202 or row 182 recited", "row 222 or row 202 recited")
    out = out.replace("row 201 or row 182 recited", "row 221 or row 202 recited")
    out = out.replace("when row 201 and row 62", "when row 221 and row 62")
    out = out.replace("after row 201 alone", "after row 221 alone")
    out = out.replace("skill-navigation-row-182", "TEMP_SKILL_182")
    out = out.replace("row 182", "row 202")
    out = out.replace("Row 182", "Row 202")
    out = out.replace("TEMP_SKILL_182", "skill-navigation-row-182")
    out = out.replace("[row 202](preface.md#skill-navigation-row-201)", "[row 221](preface.md#skill-navigation-row-221)")
    out = out.replace("[row 202](preface.md#skill-navigation-row-182)", "[row 202](preface.md#skill-navigation-row-202)")
    out = out.replace("row 162", "row 182")
    out = out.replace("Row 162", "Row 182")
    out = out.replace("row 142", "row 162")
    out = out.replace("Row 142", "Row 162")
    out = out.replace(
        "row68-row142-handshake4b-meta-prelude-capstone-reunion-index-row-162",
        "row68-row162-handshake4b-meta-prelude-capstone-reunion-index-row-182",
    )
    out = out.replace(
        "row68-row181-handshake4a-meta-prelude-capstone-reunion-index-row-201",
        "row68-row201-handshake4a-meta-prelude-capstone-reunion-index-row-221",
    )
    out = out.replace("Row 68 → Row 222 Row 68 → Row 62", "Row 68 → Row 202 Row 68 → Row 62")
    out = out.replace("memory sheet row 202 baby picture", "memory sheet row 222 baby picture")
    out = out.replace("prologue row 202 closing stitch", "prologue row 222 closing stitch")
    out = out.replace("prologue row 202 preview", "prologue row 222 preview")
    out = out.replace("epilogue row 202 closing loop", "epilogue row 222 closing loop")
    out = out.replace("opening [row 203]", "opening [row 223]")
    out = out.replace("skill-navigation-row-203", "skill-navigation-row-223")
    out = out.replace(
        "Prologue preview ([row 202](prologue/00-many-scales.md#prologue-preview-row-202))",
        "Prologue preview ([row 222](prologue/00-many-scales.md#prologue-preview-row-222))",
    )
    out = out.replace("preface row 202", "preface row 222")
    out = out.replace(
        "[row 203](preface.md#skill-navigation-row-203)",
        "[row 223](preface.md#skill-navigation-row-223)",
    )
    out = out.replace("TEMP_ROW221", "row 221")
    out = out.replace("TEMP_ROW222", "row 222")
    out = out.replace("TEMP_ROW223", "row 223")
    out = out.replace(
        "proceed to [row 203](preface.md#skill-navigation-row-203)",
        "proceed to [row 223](preface.md#skill-navigation-row-223)",
    )
    out = out.replace(
        "Row 68 → Row 202 reunion index](appendix/sources.md#row68-row182-handshake4b-meta-prelude-capstone-reunion-index-row-202)",
        "Row 68 → Row 202 reunion index](appendix/sources.md#row68-row202-handshake4b-meta-prelude-capstone-reunion-index-row-222)",
    )
    out = out.replace(
        "reunion index (row 202)](appendix/sources.md#row68-row182-handshake4b-meta-prelude-capstone-reunion-index-row-202)",
        "reunion index (row 222)](appendix/sources.md#row68-row202-handshake4b-meta-prelude-capstone-reunion-index-row-222)",
    )
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
    row222_preface = bump202_to_222(preface[start:end]) + "\n\n"

    row182_stitch = next(
        line
        for line in (ROOT / "writings/prologue/chapters/00-many-scales.md").read_text().splitlines()
        if line.startswith("**Row 182 closing stitch (Row 68 → Row 162")
    )
    prologue_stitch = bump202_to_222(
        row182_stitch.replace("{#row-182-closing-stitch}", "{#row-222-closing-stitch}").replace(
            "**Row 182 closing stitch (Row 68 → Row 162 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion).",
            "**Row 222 closing stitch (Row 68 → Row 202 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion).",
        ).replace("row 181 closed", "row 221 closed").replace("row 160 or row 141", "row 220 or row 201")
    ) + "\n\n"

    b202 = add202._build_blocks()
    prologue_compass = bump202_to_222(b202["prologue_compass"])
    prologue_preview = bump202_to_222(b202["prologue_preview"])

    epilogue = (ROOT / "writings/epilogue/chapters/multiscale.md").read_text()
    row182_loop_anchor = (
        "### Row 182 closing loop (Row 68 → Row 162 Row 68 → Row 62 "
        "Handshake 4b meta prelude capstone reunion) {#row-182-closing-loop}"
    )
    row203_loop_end = (
        "### Row 203 closing loop (Row 68 → Row 183 Row 68 → Row 63 "
        "orchestration meta prelude capstone reunion) {#row-203-closing-loop}"
    )
    epilogue_loop = bump202_to_222(
        row182_loop_anchor + epilogue.split(row182_loop_anchor, 1)[1].split(row203_loop_end, 1)[0]
    )
    epilogue_loop = epilogue_loop.replace("{#row-182-closing-loop}", "{#row-222-closing-loop}", 1)
    epilogue_loop = epilogue_loop.replace(
        "### Row 202 closing loop (Row 68 → Row 162 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion)",
        "### Row 222 closing loop (Row 68 → Row 202 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion)",
        1,
    )

    sources = (ROOT / "writings/appendix/chapters/sources.md").read_text()
    src202_header = (
        "## Row 68 → Row 182 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion index (row 202)"
    )
    next203_header = (
        "## Row 68 → Row 183 Row 68 → Row 63 orchestration meta prelude capstone reunion index (row 203)"
    )
    sources_index = bump202_to_222(sources.split(src202_header, 1)[1].split(next203_header, 1)[0])
    sources_index = (
        "## Row 68 → Row 202 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion index (row 222) "
        "{#row68-row202-handshake4b-meta-prelude-capstone-reunion-index-row-222}"
        + sources_index
    )

    sources_table = bump202_to_222(b202["sources_table"])
    sources_table = sources_table.replace("| 202 | Row 68 → Row 182", "| 222 | Row 68 → Row 202", 1)

    memory_table = bump202_to_222(b202["memory_table"])
    memory_table = memory_table.replace("| 202 | Meta |", "| 222 | Meta |", 1)

    memory_baby = bump202_to_222(b202["memory_baby"])
    if "{#row-222-baby-picture-row68-row202" not in memory_baby:
        memory_baby = memory_baby.replace(
            "### Row 222 baby picture (Row 68 → Row 202 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion)",
            "### Row 222 baby picture {#row-222-baby-picture-row68-row202-handshake4b-meta-prelude-capstone-reunion} "
            "(Row 68 → Row 202 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion)",
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


ROW221_TAIL_OLD = (
    "When row 221 is complete, proceed to [row 202](preface.md#skill-navigation-row-202) when bulk hardening matches flow stress but Handshake 4b still feels disconnected from Part VII Step 4 after verified Handshake 4a meta prelude capstone on the full capstone path,"
)
ROW221_TAIL_NEW = (
    "When row 221 is complete, proceed to [row 222](preface.md#skill-navigation-row-222) when bulk hardening matches flow stress but Handshake 4b still feels disconnected from Part VII Step 4 after verified Handshake 4a meta prelude capstone on the full capstone path,"
)

ROW221_EPILOGUE_OLD = (
    "Proceed to [row 202](#row-202-closing-loop) when row 68 closed but Handshake 4b meta still feels disconnected after row 201 on the full capstone path,"
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
        if "### Row 221 skill checkpoint" not in preface:
            raise SystemExit("row 221 must exist before row 222")
        if ROW221_TAIL_OLD not in preface:
            raise SystemExit("row 221 tail proceed string not found")
        preface = preface.replace(ROW221_TAIL_OLD, ROW221_TAIL_NEW, 1)
        preface = preface.replace(
            "when opening [row 182](preface.md#skill-navigation-row-182) before row 62 closes on the full capstone path",
            "when opening [row 222](preface.md#skill-navigation-row-222) before row 62 closes on the full capstone path",
            1,
        )
        if copper not in preface:
            raise SystemExit("copper wire anchor not found")
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
            for anchor in ("**Row 202 closing stitch", "**Row 182 closing stitch (Row 68 → Row 162"):
                if anchor in prologue:
                    prologue = prologue.replace(anchor, b["prologue_stitch"] + anchor, 1)
                    break
            else:
                raise SystemExit("prologue stitch anchor not found")
        preview_anchor = '| <span id="prologue-preview-row-202"></span>Row 202 preview'
        prologue = prologue.replace(preview_anchor, b["prologue_preview"] + preview_anchor)
        if ROW221_EPILOGUE_BEFORE_OLD in prologue:
            prologue = prologue.replace(ROW221_EPILOGUE_BEFORE_OLD, ROW221_EPILOGUE_BEFORE_NEW, 1)
        prologue_path.write_text(prologue)
        print("prologue: added row 222")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if "{#row-222-closing-loop}" not in epilogue:
        if ROW221_EPILOGUE_OLD in epilogue:
            epilogue = epilogue.replace(ROW221_EPILOGUE_OLD, ROW221_EPILOGUE_NEW, 1)
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
        inserted = False
        for baby_anchor in (
            "### Row 202 baby picture (Row 68 → Row 182 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion)",
            "### Row 201 baby picture (Row 68 → Row 181 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion)",
            "### Row 201 baby picture (Row 68 → Row 182 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion) — read",
        ):
            if baby_anchor in memory:
                memory = memory.replace(baby_anchor, b["memory_baby"] + baby_anchor, 1)
                inserted = True
                break
        if not inserted:
            raise SystemExit("memory baby picture anchor not found")
        memory_path.write_text(memory)
        print("memory-sheet: added row 222")


if __name__ == "__main__":
    main()
