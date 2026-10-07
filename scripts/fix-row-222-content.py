#!/usr/bin/env python3
"""Regenerate row 222 capstone meta-stitch blocks from row 202 template (+20 lift)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def t202_to_222(text: str) -> str:
    out = text.replace("Row 68 → Row 182", "__CAP_REUNION__")
    out = out.replace("row 203", "__ROW203__")
    out = out.replace("row 202", "row 222")
    out = out.replace("Row 202", "Row 222")
    out = out.replace("row 201", "row 221")
    out = out.replace("Row 201", "Row 221")
    out = out.replace("row 182", "row 202")
    out = out.replace("Row 182", "Row 202")
    repl = [
        (
            "row68-row182-handshake4b-meta-prelude-capstone-reunion-index-row-202",
            "row68-row202-handshake4b-meta-prelude-capstone-reunion-index-row-222",
        ),
        (
            "row-202-baby-picture-row68-row182-handshake4b-meta-prelude-capstone-reunion",
            "row-222-baby-picture-row68-row202-handshake4b-meta-prelude-capstone-reunion",
        ),
        ("skill-navigation-row-202", "skill-navigation-row-222"),
        ("skill-navigation-row-201", "skill-navigation-row-221"),
        ("skill-navigation-row-182", "skill-navigation-row-202"),
        ("prologue-preview-row-202", "prologue-preview-row-222"),
        ("row-202-closing-stitch", "row-222-closing-stitch"),
        ("row-202-closing-loop", "row-222-closing-loop"),
        ("Row 202 three-way audit", "Row 222 three-way audit"),
        (
            "verified Handshake 4a meta prelude capstone closure (row 201)",
            "verified Handshake 4a meta prelude capstone closure (row 221)",
        ),
        (
            "before row 203 orchestration meta prelude capstone reunion",
            "before row 223 orchestration meta prelude capstone reunion",
        ),
    ]
    for a, b in repl:
        out = out.replace(a, b)
    out = out.replace("__CAP_REUNION__", "Row 68 → Row 202")
    out = out.replace("__ROW203__", "row 223")
    return out


def main() -> None:
    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    start = preface.index("### Row 202 skill checkpoint")
    end = preface.index("\n\n### Row 203 skill checkpoint", start)
    row222 = t202_to_222(preface[start:end]) + "\n\n"
    r222_start = preface.index("### Row 222 skill checkpoint")
    r222_end = preface.index("\n\n## The copper wire through the book", r222_start)
    preface = preface[:r222_start] + row222 + preface[r222_end:]
    preface_path.write_text(preface)
    print("preface: fixed row 222")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    bad = "### Row 221 closing loop (Row 68 → Row 182 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion) {#row-222-closing-loop}"
    if bad in epilogue:
        idx = epilogue.index(bad)
        end_idx = epilogue.find("\n\n\n\n### Row 201 closing loop", idx)
        if end_idx == -1:
            end_idx = epilogue.find("\n\n\n\n", idx + len(bad))
        epilogue = epilogue[:idx] + epilogue[end_idx:]
        print("epilogue: removed misplaced row 222 loop")

    src_start = epilogue.index("### Row 202 closing loop (Row 68 → Row 162 Row 68 → Row 62")
    src_end = epilogue.index("\n\n\n\n### Row 181 closing loop", src_start)
    row222_loop = t202_to_222(epilogue[src_start:src_end]).replace(
        "{#row-182-closing-loop}", "{#row-222-closing-loop}", 1
    )
    anchor = "### Row 221 closing loop (Row 68 → Row 221 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion) {#row-221-closing-loop}"
    if anchor in epilogue and "{#row-222-closing-loop}" not in epilogue.split(anchor)[0][-5000:]:
        epilogue = epilogue.replace(anchor, row222_loop + "\n\n" + anchor, 1)
        print("epilogue: inserted row 222 loop before row 221")

    old221 = (
        "Proceed to [row 202](#row-202-closing-loop) when row 68 closed but Handshake 4b meta still feels disconnected after row 201 on the full capstone path,"
    )
    new221 = (
        "Proceed to [row 222](#row-222-closing-loop) when row 68 closed but Handshake 4b meta still feels disconnected after row 221 on the full capstone path,"
    )
    if old221 in epilogue:
        epilogue = epilogue.replace(old221, new221, 1)
    epilogue_path.write_text(epilogue)

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    prologue = prologue.replace(
        "Row 68 → Row 222 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion (row 222)",
        "Row 68 → Row 202 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion (row 222)",
    )
    needle = "| Row 68 → Row 182 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion (row 202) |"
    if needle in prologue:
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        compass = (
            "| Row 68 → Row 202 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion (row 222) | "
            "[Preface: row 222 skill checkpoint](../preface.md#skill-navigation-row-222) · "
            "[Row 68 → Row 202 Handshake 4b meta prelude capstone reunion index](../appendix/sources.md#row68-row202-handshake4b-meta-prelude-capstone-reunion-index-row-222) · "
            "[memory sheet row 222 baby picture](../appendix/memory-sheet.md#row-222-baby-picture-row68-row202-handshake4b-meta-prelude-capstone-reunion) · "
            "[prologue row 222 preview row](#prologue-preview-row-222); [prologue row 222 closing stitch](#row-222-closing-stitch); "
            "[epilogue row 222 closing loop](../epilogue/multiscale.md#row-222-closing-loop) — "
            "read row 68 gate + row 221 or row 202 Handshake 4b meta prelude capstone / Handshake 4b meta capstone gate + epilogue FE² cross-links + row 62 meta aloud "
            "when bulk hardening matches flow stress after verified Handshake 4b meta prelude capstone on the full capstone path but Handshake 4b still feels disconnected from Part VII Step 4 |\n"
        )
        if "prologue-preview-row-222" not in prologue:
            prologue = prologue[: line_end + 1] + compass + prologue[line_end + 1 :]
    prologue_path.write_text(prologue)
    print("prologue: fixed compass")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    sources = sources.replace(
        "{#row68-row202-handshake4b-meta-prelude-capstone-reunion-index-row-222} {#row68-row162-handshake4b-meta-prelude-capstone-reunion-index-row-182}",
        "{#row68-row202-handshake4b-meta-prelude-capstone-reunion-index-row-222}",
    )
    sources_path.write_text(sources)

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-222-baby-picture-row68-row202" not in memory:
        baby_src = "### Row 202 baby picture (Row 68 → Row 202 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion) — read"
        if baby_src not in memory:
            baby_src = "### Row 202 baby picture (Row 68 → Row 182 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion) — read"
        idx = memory.index(baby_src)
        end = memory.find("\n\n### Row ", idx + 1)
        baby = t202_to_222(memory[idx:end])
        baby = baby.replace(
            "### Row 222 baby picture (Row 68 → Row 202",
            "### Row 222 baby picture {#row-222-baby-picture-row68-row202-handshake4b-meta-prelude-capstone-reunion} (Row 68 → Row 202",
            1,
        )
        table_line = "| 202 | Meta | [Row 68 → Row 182 Handshake 4b meta prelude capstone reunion index]"
        if table_line in memory:
            new_table = (
                "| 222 | Meta | [Row 68 → Row 202 Handshake 4b meta prelude capstone reunion index]"
                "(sources.md#row68-row202-handshake4b-meta-prelude-capstone-reunion-index-row-222) · "
                "[preface row 222 skill checkpoint](../preface.md#skill-navigation-row-222) · "
                "[prologue row 222 preview](../prologue/00-many-scales.md#prologue-preview-row-222) · "
                "[prologue row 222 closing stitch](../prologue/00-many-scales.md#row-222-closing-stitch) · "
                "[epilogue row 222 closing loop](../epilogue/multiscale.md#row-222-closing-loop) | "
                "Row 68 closed but row 62 Handshake 4b meta reunion feels disconnected from verified Handshake 4b meta prelude capstone on the full capstone path — "
                "read row 68 + row 221 or row 222 gate + epilogue FE² cross-links + row 62; "
                "[row 222 baby picture](#row-222-baby-picture-row68-row202-handshake4b-meta-prelude-capstone-reunion) |\n"
            )
            memory = memory.replace(table_line, new_table + table_line, 1)
        memory = memory.replace(baby_src + memory[idx + len(baby_src) : end], baby, 1)
        memory_path.write_text(memory)
        print("memory-sheet: added row 222")


if __name__ == "__main__":
    main()
