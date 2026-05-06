#!/usr/bin/env python3
"""
修正前補章的殘留問題：
1. 小節標題 ## X.N / ### X.N.N 改為 ## NN.N / ### NN.N.N
2. ch-40-multi-agent.md 連結修正為 ch-40-multi-agent-consensus.md
3. 移除前補章檔案頭部的「插入位置」元資料 blockquote
4. 清理 Cross-References 中「作為 Part VII 最後一個補章」等殘留說明
"""
import re
from pathlib import Path

BOOK_DIR = Path("book")

# 補章字母 → 新章號 對照
LETTER_TO_NUM = {
    "F": "17", "A": "26", "E": "28",
    "D": "40", "H": "41", "I": "42",
    "B": "45", "C": "46", "G": "53",
}

# 前補章檔案列表 (字母 → 檔案)
FORMER_SUPP_FILES = {
    "F": BOOK_DIR / "part-03-design/ch-17-cux.md",
    "A": BOOK_DIR / "part-04-architecture/ch-26-edge-ot-it.md",
    "E": BOOK_DIR / "part-05-quality/ch-28-compliance.md",
    "D": BOOK_DIR / "part-07-ai-era/ch-40-multi-agent-consensus.md",
    "H": BOOK_DIR / "part-07-ai-era/ch-41-agent-spec.md",
    "I": BOOK_DIR / "part-07-ai-era/ch-42-harness-engineering.md",
    "B": BOOK_DIR / "part-07-ai-era/ch-45-agentic-qa.md",
    "C": BOOK_DIR / "part-07-ai-era/ch-46-legacy-ai.md",
    "G": BOOK_DIR / "part-09-human-engineer/ch-53-engineering-intuition.md",
}


def fix_section_headers(text: str, letter: str, num: str) -> str:
    """## X.N ... → ## NN.N ..., 同理 ###, ####"""
    for hashes in ["####", "###", "##"]:
        # 匹配 "## X." 開頭的小節標題
        text = re.sub(
            rf"^({hashes}\s+){letter}\.(\d)",
            rf"\g<1>{num}.\2",
            text,
            flags=re.MULTILINE,
        )
    return text


def fix_former_supp_file(letter: str, path: Path) -> int:
    """修正單一前補章檔案的小節標題與插入位置元資料"""
    if not path.exists():
        print(f"  SKIP (not found): {path}")
        return 0
    text = path.read_text(encoding="utf-8")
    original = text
    num = LETTER_TO_NUM[letter]

    # 1. 小節標題
    text = fix_section_headers(text, letter, num)

    # 2. 移除「插入位置」blockquote 行（整行含換行）
    text = re.sub(r"^> \*\*插入位置\*\*[^\n]*\n", "", text, flags=re.MULTILINE)

    # 3. 移除 Cross-References 裡的「插入位置」bullet
    text = re.sub(r"^- \*\*插入位置\*\*[^\n]*\n", "", text, flags=re.MULTILINE)

    # 4. 清理「作為 Part VII 最後一個補章」/ 「作為 Part VII 收束補章」殘留說明
    text = re.sub(r"[，,]\s*作為 Part VII [^\n。」]*", "", text)

    # 5. ch-40-multi-agent.md → ch-40-multi-agent-consensus.md（限本檔案）
    text = text.replace("ch-40-multi-agent.md", "ch-40-multi-agent-consensus.md")

    if text != original:
        path.write_text(text, encoding="utf-8")
        print(f"  fixed (former supp): {path.name}")
        return 1
    return 0


def fix_all_ch40_links():
    """全書修正 ch-40-multi-agent.md → ch-40-multi-agent-consensus.md"""
    count = 0
    for md in sorted(BOOK_DIR.rglob("*.md")):
        text = md.read_text(encoding="utf-8")
        if "ch-40-multi-agent.md" in text:
            new_text = text.replace("ch-40-multi-agent.md", "ch-40-multi-agent-consensus.md")
            md.write_text(new_text, encoding="utf-8")
            print(f"  fixed (ch-40 link): {md.name}")
            count += 1
    return count


if __name__ == "__main__":
    print("=== 1. 修正前補章小節標題與元資料 ===")
    for letter, path in FORMER_SUPP_FILES.items():
        fix_former_supp_file(letter, path)

    print("\n=== 2. 全書修正 ch-40 連結 ===")
    fix_all_ch40_links()

    print("\n=== 3. 驗證 ===")
    import subprocess

    checks = [
        ("## X.N 小節標題殘留", r"^## [A-I]\.", "--include=*.md"),
        ("### X.N.N 小節標題殘留", r"^### [A-I]\.", "--include=*.md"),
        ("插入位置 殘留", r"\*\*插入位置\*\*", "--include=*.md"),
        ("ch-40 錯誤連結", r"ch-40-multi-agent\.md[^-]", "--include=*.md"),
    ]
    for label, pat, inc in checks:
        r = subprocess.run(
            f'grep -rnE "{pat}" book/ {inc}',
            capture_output=True, text=True, encoding="utf-8",
            errors="replace", shell=True
        )
        hits = [l for l in r.stdout.splitlines() if l.strip()]
        status = "PASS" if not hits else f"FAIL ({len(hits)} hits)"
        print(f"  {status}: {label}")
        for h in hits[:5]:
            print(f"    {h}")
