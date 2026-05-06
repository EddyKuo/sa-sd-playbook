#!/usr/bin/env python3
"""
全書章節重編號腳本
用法: python renumber-chapters.py [phase]
  phase: rename_files | replace_text | verify
"""
import csv, os, re, subprocess, sys
from pathlib import Path

BOOK_DIR = Path("book")
MAPPING_CSV = Path("renumber-mapping.csv")

# ── 讀取對照表 ──────────────────────────────────────────────
def load_mapping():
    rows = []
    with open(MAPPING_CSV, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            rows.append(row)
    return rows

# ── Phase 1: 檔案重命名 (git mv) ──────────────────────────
def rename_files():
    mapping = load_mapping()

    # 先處理補章 (old_id 為字母)，再以「舊號由大到小」處理主章，避免連鎖污染
    letters = [r for r in mapping if r["old_id"].isalpha()]
    numbers = [r for r in mapping if r["old_id"].isdigit()]
    numbers_desc = sorted(numbers, key=lambda r: int(r["old_id"]), reverse=True)
    ordered = letters + numbers_desc

    for row in ordered:
        old_path = BOOK_DIR / row["part_dir"] / row["old_filename"]
        new_path = BOOK_DIR / row["part_dir"] / row["new_filename"]
        if not old_path.exists():
            print(f"  SKIP (not found): {old_path}")
            continue
        result = subprocess.run(
            ["git", "mv", str(old_path), str(new_path)],
            capture_output=True, text=True
        )
        if result.returncode == 0:
            print(f"  mv: {row['old_filename']} → {row['new_filename']}")
        else:
            print(f"  ERROR: {result.stderr.strip()}")

# ── Phase 2: 文字替換 ─────────────────────────────────────
#
# 策略：兩階段佔位符法
#   Stage A: 所有「舊值」→ 唯一佔位符 __CHXXX__
#   Stage B: 佔位符     → 新值
#
# 涵蓋的文字變體：
#   - 英文: "Ch 17" / "Ch17" / "chapter: 17"
#   - 中文: "第 17 章" / "第17章"
#   - 檔名: "ch-17-" (內文中的相對路徑)
#   - 補章: "補章 F" / "chF-" / "chapter: F"

LETTER_MAP = {
    # 補章字母 → 新章號
    "F": "17", "A": "26", "E": "28",
    "D": "40", "H": "41", "I": "42",
    "B": "45", "C": "46", "G": "53",
}

NUMBER_MAP = {
    # 舊章號 → 新章號 (字串形式)
    "17": "18", "18": "19", "19": "20", "20": "21",
    "21": "22", "22": "23", "23": "24", "24": "25",
    "25": "27", "26": "29", "27": "30", "28": "31",
    "29": "32", "30": "33", "31": "34", "32": "35",
    "33": "36", "34": "37", "35": "38", "36": "39",
    "37": "43", "38": "44", "39": "47",
    "40": "48", "41": "49", "42": "50", "43": "51", "44": "52",
}

def placeholder(key: str) -> str:
    """產生唯一佔位符，避免與正文碰撞"""
    return f"__RENUMCH{key}__"

def replace_text_in_file(path: Path):
    try:
        text = path.read_text(encoding="utf-8")
    except Exception as e:
        print(f"  READ ERROR {path}: {e}")
        return

    original = text

    # ── Stage A: 原值 → 佔位符 ─────────────────────────────

    # A1. 補章字母變體
    for letter, _ in LETTER_MAP.items():
        ph = placeholder(f"SUPP{letter}")
        # "補章 F" / "補章F"
        text = re.sub(rf"補章\s*{letter}(?=[^A-Z\da-z]|$)", ph, text)
        # "chF-" (filename in text)
        text = text.replace(f"ch{letter}-", placeholder(f"FN{letter}"))
        # frontmatter "chapter: F"
        text = re.sub(rf"(^chapter:\s*){letter}(\s*$)", rf"\g<1>{placeholder(f'FM{letter}')}\2", text, flags=re.MULTILINE)

    # A2. 數字章節變體 (由大到小處理，避免 "17" 先被替換後影響 "170" 之類)
    for old_num in sorted(NUMBER_MAP.keys(), key=lambda x: -int(x)):
        ph = placeholder(f"NUM{old_num}")
        # "Ch 17" / "Ch17"
        text = re.sub(rf"\bCh\s*{old_num}\b", placeholder(f"CHEN{old_num}"), text)
        # "第 17 章" / "第17章"
        text = re.sub(rf"第\s*{old_num}\s*章", placeholder(f"CHZH{old_num}"), text)
        # "ch-17-" (filename in text, 確保前後有邊界)
        text = re.sub(rf"(?<![0-9])ch-{old_num}-", placeholder(f"FNNUM{old_num}"), text)
        # frontmatter "chapter: 17"
        text = re.sub(rf"(^chapter:\s*){old_num}(\s*$)", rf"\g<1>{placeholder(f'FMNUM{old_num}')}\2", text, flags=re.MULTILINE)

    # ── Stage B: 佔位符 → 新值 ────────────────────────────

    # B1. 補章佔位符
    for letter, new_num in LETTER_MAP.items():
        new_num_zp = new_num.zfill(2)  # 零補位，用於檔名
        text = text.replace(placeholder(f"SUPPF" if letter=="F" else f"SUPP{letter}"), f"Ch {new_num}")
        # 處理 f"SUPP{letter}" 正確
        text = text.replace(placeholder(f"SUPP{letter}"), f"Ch {new_num}")
        text = text.replace(placeholder(f"FN{letter}"), f"ch-{new_num_zp}-")
        text = text.replace(placeholder(f"FM{letter}"), new_num)

    # B2. 數字章節佔位符
    for old_num, new_num in NUMBER_MAP.items():
        new_num_zp = new_num.zfill(2)
        old_zp = old_num.zfill(2)
        text = text.replace(placeholder(f"CHEN{old_num}"), f"Ch {new_num}")
        text = re.sub(re.escape(placeholder(f"CHZH{old_num}")), f"第 {new_num} 章", text)
        text = text.replace(placeholder(f"FNNUM{old_num}"), f"ch-{new_num_zp}-")
        text = text.replace(placeholder(f"FMNUM{old_num}"), new_num)

    if text != original:
        path.write_text(text, encoding="utf-8")
        print(f"  updated: {path}")

def replace_text_all():
    """對 book/ 下所有 .md 及根目錄相關 .md 執行替換"""
    targets = list(BOOK_DIR.rglob("*.md"))
    # 加上根層文件
    for name in ["README.md", "rename_chapter.md"]:
        p = Path(name)
        if p.exists():
            targets.append(p)

    for p in sorted(targets):
        replace_text_in_file(p)

# ── Phase 3: 驗證 ─────────────────────────────────────────
def verify():
    errors = 0

    # 1. 不應有「補章 X」殘留 (X 為大寫字母)
    result = subprocess.run(
        ["grep", "-rnE", r"補章\s*[A-I]", "book/"],
        capture_output=True, text=True
    )
    if result.stdout.strip():
        print("❌ 殘留「補章 X」：")
        print(result.stdout[:2000])
        errors += 1
    else:
        print("✅ 補章字母引用：清零")

    # 2. 不應有 chX- 檔名引用
    result = subprocess.run(
        ["grep", "-rnE", r"ch[A-I]-[a-z\-]+\.md", "book/"],
        capture_output=True, text=True
    )
    if result.stdout.strip():
        print("❌ 殘留 chX- 檔名引用：")
        print(result.stdout[:2000])
        errors += 1
    else:
        print("✅ chX- 檔名引用：清零")

    # 3. frontmatter chapter: 不應為字母
    result = subprocess.run(
        ["grep", "-rnE", r"^chapter:\s*[A-I]", "book/"],
        capture_output=True, text=True
    )
    if result.stdout.strip():
        print("❌ frontmatter chapter 仍為字母：")
        print(result.stdout[:1000])
        errors += 1
    else:
        print("✅ frontmatter chapter 欄位：全為數字")

    # 4. 不應有佔位符殘留
    result = subprocess.run(
        ["grep", "-rnE", r"__RENUMCH", "book/"],
        capture_output=True, text=True
    )
    if result.stdout.strip():
        print("❌ 殘留佔位符：")
        print(result.stdout[:1000])
        errors += 1
    else:
        print("✅ 佔位符：清零")

    print(f"\n{'✅ 驗證通過' if errors == 0 else f'❌ {errors} 項未通過，請手動修正'}")

# ── Entry point ───────────────────────────────────────────
if __name__ == "__main__":
    phase = sys.argv[1] if len(sys.argv) > 1 else "help"
    if phase == "rename_files":
        print("=== Phase 1: 檔案重命名 ===")
        rename_files()
    elif phase == "replace_text":
        print("=== Phase 2: 文字替換 ===")
        replace_text_all()
    elif phase == "verify":
        print("=== Phase 3: 驗證 ===")
        verify()
    else:
        print("用法: python renumber-chapters.py [rename_files | replace_text | verify]")
