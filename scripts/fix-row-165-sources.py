#!/usr/bin/env python3
from pathlib import Path


def tx(s, pairs):
    for a, b in pairs:
        s = s.replace(a, b)
    return s


def lift_145_to_165(s: str) -> str:
    s = s.replace("[row 145](preface.md#skill-navigation-row-145)", "__ROW145_HINGE__")
    s = s.replace("skill-navigation-row-145", "__ROW165_NAV__")
    s = s.replace(
        "Row 68 → Row 125 Row 68 → Row 65 second-pass meta prelude capstone",
        "__ROW165TITLE__",
    )
    p = [
        ("row68-row125-second-pass-meta-prelude-capstone-reunion-index-row-145", "row68-row145-second-pass-meta-prelude-capstone-reunion-index-row-165"),
        ("row-145-baby-picture-row68-row125-second-pass-meta-prelude-capstone-reunion", "row-165-baby-picture-row68-row145-second-pass-meta-prelude-capstone-reunion"),
        ("[row 146]", "__R166__"),
        ("[row 126]", "[row 146]"),
        ("row 126", "row 146"),
        ("Row 126", "Row 146"),
        ("__R166__", "[row 166]"),
        ("[row 145]", "__R145__"),
        ("[row 125]", "[row 145]"),
        ("row 125", "row 145"),
        ("Row 125", "Row 145"),
        ("__R145__", "[row 145]"),
        ("[row 144](preface.md#skill-navigation-row-144)", "[row 164](preface.md#skill-navigation-row-164)"),
        ("skill-navigation-row-144", "skill-navigation-row-164"),
        ("row 144", "row 164"),
        ("Row 144", "Row 164"),
        ("(row 145)", "(row 165)"),
        ("Row 145 names", "Row 165 names"),
        ("Row 145 does not replace", "Row 165 does not replace"),
        ("Preface row 145", "Preface row 165"),
        ("memory sheet row 145", "memory sheet row 165"),
        ("Row 145 skill checkpoint", "Row 165 skill checkpoint"),
        ("skill-navigation-row-145", "skill-navigation-row-165"),
    ]
    out = tx(s, p)
    out = out.replace("__ROW165TITLE__", "Row 68 → Row 145 Row 68 → Row 65 second-pass meta prelude capstone")
    out = out.replace("__ROW165_NAV__", "skill-navigation-row-165")
    out = out.replace("__ROW145_HINGE__", "[row 145](preface.md#skill-navigation-row-145)")
    return out


def main() -> None:
    path = Path(__file__).resolve().parents[1] / "writings/appendix/chapters/sources.md"
    text = path.read_text()
    key = "row68-row145-second-pass-meta-prelude-capstone-reunion-index-row-165"
    if f"{{#{key}}}" in text:
        print("sources: row 165 index already present")
        return
    start = text.find(
        "## Row 68 → Row 125 Row 68 → Row 65 second-pass meta prelude capstone reunion index (row 145)"
    )
    end = text.find(
        "## Row 68 → Row 105 Row 68 → Row 65 second-pass meta prelude capstone reunion index (row 125)",
        start,
    )
    if start < 0 or end < 0:
        raise SystemExit("row 145 sources anchors missing")
    block = lift_145_to_165(text[start:end])
    block = block.replace(
        "## Row 68 → Row 145 Row 68 → Row 65 second-pass meta prelude capstone reunion index (row 165)",
        f"## Row 68 → Row 145 Row 68 → Row 65 second-pass meta prelude capstone reunion index (row 165) {{#{key}}}",
        1,
    )
    text = text[:start] + block + text[start:]
    path.write_text(text)
    print("sources: inserted row 165 index section")


if __name__ == "__main__":
    main()
