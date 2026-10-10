#!/usr/bin/env python3
"""Remove misplaced DFT capstone closing loops (row 255–258) from the dynamics band."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
EPILOGUE = ROOT / "writings/epilogue/chapters/multiscale.md"


def main() -> None:
    text = EPILOGUE.read_text()
    # Orphan band: after row-253 proceed paragraph, before row-254 capstone export loop
    anchor = "Proceed to [row 254](#row-254-closing-loop) when row 68 closed but export meta prelude capstone still lags after row 253"
    if anchor not in text:
        print("anchor not found; skip")
        return
    idx = text.index(anchor)
    end_para = text.find("\n\n\n\n", idx)
    if end_para == -1:
        print("end not found")
        return
    tail = text[end_para:]
    # Drop consecutive capstone loops wrongly inserted before row-254 section
    pattern = (
        r"\n\n### Row 238 closing loop \(Row 68 → Row 238 Row 68 → Row 58 DFT workflows meta prelude capstone reunion\) \{#row-258-closing-loop\}.*?"
        r"(?=\n\n### Row 234 closing loop \(Row 68 → Row 234 Row 68 → Row 54 export meta prelude capstone reunion\) \{#row-254-closing-loop\})"
    )
    new_tail, n = re.subn(pattern, "\n\n", tail, count=1, flags=re.DOTALL)
    if n:
        EPILOGUE.write_text(text[:end_para] + new_tail)
        print(f"removed orphan DFT capstone block ({n})")
    else:
        # Also try removing 258-255 stack before row-255 misplaced block
        pattern2 = (
            r"\n\n### Row 238 closing loop \(Row 68 → Row 238 Row 68 → Row 58 DFT workflows meta prelude capstone reunion\) \{#row-258-closing-loop\}.*?"
            r"(?=\n\n### Row 255 closing loop)"
        )
        new_tail, n2 = re.subn(pattern2, "\n\n", tail, count=1, flags=re.DOTALL)
        if n2:
            EPILOGUE.write_text(text[:end_para] + new_tail)
            print(f"removed orphan stack ({n2})")
        else:
            print("no orphan block matched")


if __name__ == "__main__":
    main()
