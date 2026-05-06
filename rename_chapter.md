# 方案 C — 全書連續重編號執行計畫

> 產生日期：2026-05-06
> 目標：將 9 個補章（A–I）整合為連續正式章節，全書由 44 主章 + 9 補章 = **53 章**

---

## Phase 0｜決策確認（執行前必須拍板）

### Part 07 補章插入順序歧異

| 來源 | Part 07 順序 |
|---|---|
| 各補章 frontmatter（**權威**） | 33 → 34 → 35 → 36 → **D → H → I** → 37 → 38 → **B → C** |
| `SUMMARY.md` | 33 → 34 → 35 → 36 → 37 → 38 → **B → C → D → H → I** |
| `book/README.md` | 33 → 34 → 35 → 36 → **D** → 37 → 38 → **B → C** |

**建議採用 frontmatter 版本**（作者逐章標明插入位置，語意連貫）。

### 其他補章插入位置（三方一致，無歧異）

| 補章 | 插入位置 |
|---|---|
| Ch 17 | Ch 16 之後（Part 03 末） |
| Ch 26 | Ch 25 之後（Part 04 末） |
| Ch 28 | Ch 27 之後（Part 05） |
| Ch 53 | Ch 52 之後（Part 09 末） |

### 需要確認的四個問題

1. **Part 07 順序**：採 frontmatter 版（D/H/I 在 36–37 之間，B/C 在 38 之後） ans: 
2. **保留補章標記**：全部變主章不留「延伸閱讀」標記？ ans: 不保留
3. **重定向表**：要不要在 root README 留一份舊號 → 新號對照，給已分享連結的讀者？ ans: 不用
4. **執行時機**：直接在 master？還是開新 branch + PR？ ans: 新開分支, 完成之後再合併

---

## Phase 1｜新舊章節對照表

採 frontmatter 版，共 53 章：

| 舊號 | 新號 | 標題（簡） | 舊檔名 | 新檔名 |
|---|---|---|---|---|
| Ch 1 | Ch 1 | 為什麼 SA/SD | `ch-01-why-sa-sd.md` | 不變 |
| Ch 2 | Ch 2 | SDLC 演進 | `ch-02-sdlc-evolution.md` | 不變 |
| Ch 3 | Ch 3 | 專案啟動 | `ch-03-project-initiation.md` | 不變 |
| Ch 4 | Ch 4 | 需求工程 | `ch-04-requirements-engineering.md` | 不變 |
| Ch 5 | Ch 5 | UML | `ch-05-uml-overview.md` | 不變 |
| Ch 6 | Ch 6 | 結構化分析 | `ch-06-dfd-structured-analysis.md` | 不變 |
| Ch 7 | Ch 7 | 物件導向分析 | `ch-07-object-oriented-analysis.md` | 不變 |
| Ch 8 | Ch 8 | 資料模型 | `ch-08-data-modeling-normalization.md` | 不變 |
| Ch 9 | Ch 9 | 流程模型 | `ch-09-process-modeling.md` | 不變 |
| Ch 10 | Ch 10 | 規格文件 | `ch-10-spec-documents.md` | 不變 |
| Ch 11 | Ch 11 | 架構原則 | `ch-11-architecture-principles.md` | 不變 |
| Ch 12 | Ch 12 | 設計模式 | `ch-12-design-patterns.md` | 不變 |
| Ch 13 | Ch 13 | 架構風格 | `ch-13-architecture-styles.md` | 不變 |
| Ch 14 | Ch 14 | API 設計 | `ch-14-api-design.md` | 不變 |
| Ch 15 | Ch 15 | 資料儲存 | `ch-15-data-storage.md` | 不變 |
| Ch 16 | Ch 16 | UI/UX | `ch-16-uiux-system-view.md` | 不變 |
| **Ch 17** | **Ch 18** | 多模態 / CUX | `ch-17-cux.md` | `ch-18-cux.md` |
| Ch 18 | Ch 19 | DDD | `ch-18-ddd-strategic-tactical.md` | `ch-19-ddd-strategic-tactical.md` |
| Ch 19 | Ch 20 | Event Storming | `ch-19-event-storming-modeling.md` | `ch-20-event-storming-modeling.md` |
| Ch 20 | Ch 21 | C4 Model | `ch-20-c4-model-visualization.md` | `ch-21-c4-model-visualization.md` |
| Ch 21 | Ch 22 | Modular Monolith | `ch-21-modular-monolith.md` | `ch-22-modular-monolith.md` |
| Ch 22 | Ch 23 | 微服務 | `ch-22-microservices.md` | `ch-23-microservices.md` |
| Ch 23 | Ch 24 | EDA/CQRS/ES | `ch-23-event-driven-cqrs-es.md` | `ch-24-event-driven-cqrs-es.md` |
| Ch 24 | Ch 25 | Cloud Native/K8s | `ch-24-cloud-native-kubernetes.md` | `ch-25-cloud-native-kubernetes.md` |
| Ch 25 | Ch 27 | Service Mesh | `ch-25-service-mesh-cell-based.md` | `ch-27-service-mesh-cell-based.md` |
| **Ch 26** | **Ch 29** | 邊緣 / OT-IT | `ch-26-edge-ot-it.md` | `ch-29-edge-ot-it.md` |
| Ch 27 | Ch 30 | Security | `ch-27-security-by-design.md` | `ch-30-security-by-design.md` |
| **Ch 28** | **Ch 31** | Compliance | `ch-28-compliance.md` | `ch-31-compliance.md` |
| Ch 29 | Ch 32 | 可觀測性 | `ch-29-observability-otel.md` | `ch-32-observability-otel.md` |
| Ch 30 | Ch 33 | SRE/SLO/Chaos | `ch-30-sre-slo-chaos.md` | `ch-33-sre-slo-chaos.md` |
| Ch 31 | Ch 34 | 資料架構 | `ch-31-data-architecture.md` | `ch-34-data-architecture.md` |
| Ch 32 | Ch 35 | Platform/IDP | `ch-32-platform-engineering-idp.md` | `ch-35-platform-engineering-idp.md` |
| Ch 33 | Ch 36 | ADR | `ch-33-adr-architecture-knowledge.md` | `ch-36-adr-architecture-knowledge.md` |
| Ch 34 | Ch 37 | Fitness Functions | `ch-34-fitness-functions.md` | `ch-37-fitness-functions.md` |
| Ch 35 | Ch 38 | FinOps | `ch-35-finops-green-software.md` | `ch-38-finops-green-software.md` |
| Ch 36 | Ch 39 | AI-Native | `ch-36-ai-native-architecture.md` | `ch-39-ai-native-architecture.md` |
| Ch 37 | Ch 43 | CDE | `ch-37-context-driven-engineering.md` | `ch-43-context-driven-engineering.md` |
| Ch 38 | Ch 44 | RAG/Memory/Tool | `ch-38-rag-memory-tool.md` | `ch-44-rag-memory-tool.md` |
| Ch 39 | Ch 47 | Multi-Agent | `ch-39-multi-agent.md` | `ch-47-multi-agent.md` |
| **Ch 40** | **Ch 48** | Multi-Agent 共識 | `ch-40-multi-agent.md` | `ch-48-multi-agent-consensus.md` |
| **Ch 41** | **Ch 49** | Agent 設定語言 | `ch-41-agent-spec.md` | `ch-49-agent-spec.md` |
| **Ch 42** | **Ch 50** | Agent Harness | `ch-42-harness-engineering.md` | `ch-50-harness-engineering.md` |
| Ch 43 | Ch 51 | Coding Agent | `ch-43-coding-agent.md` | `ch-51-coding-agent.md` |
| Ch 44 | Ch 52 | Eval/Drift/Red Team | `ch-44-ai-eval-drift-redteam.md` | `ch-52-ai-eval-drift-redteam.md` |
| **Ch 45** | **Ch 45** | Agentic QA | `ch-45-agentic-qa.md` | `ch-45-agentic-qa.md` |
| **Ch 46** | **Ch 46** | Legacy/AI 逆向 | `ch-46-legacy-ai.md` | `ch-46-legacy-ai.md` |
| Ch 47 | **Ch 47** | Capstone | `ch-47-capstone.md` | `ch-47-capstone.md` |
| Ch 48 | Ch 48 | AI 能力地圖 | `ch-48-ai-capability-map.md` | `ch-48-ai-capability-map.md` |
| Ch 49 | Ch 49 | 有效使用 AI | `ch-49-effective-ai-assistance.md` | `ch-49-effective-ai-assistance.md` |
| Ch 50 | Ch 50 | 不能外包的邊界 | `ch-50-human-judgment-boundary.md` | `ch-50-human-judgment-boundary.md` |
| Ch 51 | Ch 51 | AI 弱點研究 | `ch-51-ai-weakness-research.md` | `ch-51-ai-weakness-research.md` |
| Ch 52 | Ch 52 | AI 程式碼審計 | `ch-52-ai-code-audit.md` | `ch-52-ai-code-audit.md` |
| **Ch 53** | **Ch 53** | 工程直覺保護 | `ch-53-engineering-intuition.md` | `ch-53-engineering-intuition.md` |

> ⚠️ 檔名衝突警告：`ch-39-multi-agent.md`（舊 Ch 39）與Ch 40 都含 `multi-agent`。
> Ch 40 新檔名加區分詞 `ch-48-multi-agent-consensus.md` 以避免衝突。

---

## Phase 2｜工具與資產準備

### 2.1 對照表 CSV

建立 `renumber-mapping.csv`（4 欄），作為腳本與稽核共用 source of truth：

```csv
old_chapter,new_chapter,old_filename,new_filename
F,17,ch-17-cux.md,ch-18-cux.md
17,18,ch-18-ddd-strategic-tactical.md,ch-19-ddd-strategic-tactical.md
...
```

### 2.2 替換腳本邏輯（PowerShell）

```powershell
# Pass 1 — 檔名重命名（使用 git mv 保留歷史）
# 依照 renumber-mapping.csv 逐行執行
foreach ($row in $mapping) {
    git mv $row.old_filename $row.new_filename
}

# Pass 2 — 兩階段文字替換（避免連鎖污染）
# 第一階段：所有舊號換成獨特佔位符
# 例：Ch 18 → __CH_OLD017__，Ch 19 → __CH_OLD018__ ...
# （包含「第 18 章」「Ch 18」「ch-18-」等所有變體）

# 第二階段：佔位符換成新號
# __CH_OLD017__ → Ch 19，__CH_OLD018__ → Ch 20 ...

# Pass 3 — 補章引用
# 「補章 X」   → 「Ch NN」
# 「chX-*.md」 → 「ch-NN-*.md」
```

### 2.3 需處理的文字變體

在 Pass 2 需涵蓋以下所有寫法：

| 變體 | 範例 |
|---|---|
| 英文帶空格 | `Ch 18` |
| 英文不帶空格 | `Ch 18` |
| 中文帶空格 | `第 18 章` |
| 中文不帶空格 | `第 18 章` |
| 檔名形式 | `ch-18-` |
| frontmatter | `chapter: 17` |

### 2.4 驗證腳本（執行後應全部為 0）

```bash
# 不應有任何「補章 X」殘留
grep -rE "補章\s*[A-I]" book/

# 不應有任何 chX- 檔名引用
grep -rE "ch[A-I]-[a-z\-]+\.md" book/

# frontmatter chapter: 欄位應全為數字
grep -rE "^chapter:\s*[A-I]" book/

# 不應有任何佔位符殘留
grep -rE "__CH_OLD\d+" book/
```

---

## Phase 3｜執行順序（建議拆 6 個 commit）

| # | Commit 訊息 | 內容 | 預估 diff |
|---|---|---|---|
| 1 | `chore: 加入章節重編號對照表與腳本` | `renumber-mapping.csv` + 腳本 + 本計畫文件 | 新增 2–3 檔 |
| 2 | `refactor(ch): 重命名補章檔案` | 9 個 `git mv`（`chX-*.md` → `ch-NN-*.md`）+ frontmatter `chapter:` 欄位更新 | 9 檔重命名 |
| 3 | `refactor(ch): 主章檔名位移` | Ch 18→18, 18→19 ... Ch 52→52 等約 28 檔 `git mv` + frontmatter | 28 檔重命名 |
| 4 | `refactor(ch): 章節內文字引用更新` | 「補章 X」→「Ch NN」、舊 Ch 號 → 新 Ch 號（腳本批次，跨 53 檔） | ~450 處 |
| 5 | `refactor(ch): 章節內檔名連結更新` | `chX-*.md` 與 `ch-舊NN-*.md` 路徑修正 | ~140 處 |
| 6 | `refactor(ch): 索引文件更新` | `SUMMARY.md` / 兩份 `README.md` / 7 份附錄 / 9 份篇導讀 / 3 份 front-matter | ~17 檔 |

每個 commit 後跑 Phase 2.4 驗證腳本，確認為 0 才進下一步。

---

## Phase 4｜高風險區手工稽核

腳本處理 ~95% 引用，以下區域需人眼複查：

| 區域 | 風險點 | 引用密度 |
|---|---|---|
| **Ch 47 Capstone**（舊 Ch 47） | 全書文件樹整合，47 處補章引用 + 18 處檔名引用 | ⭐⭐⭐ 最高 |
| **附錄 F Glossary** | 32 處補章交叉引用 | ⭐⭐⭐ |
| **附錄 E Standards** | 16 處，圖表編號可能含補章字母 | ⭐⭐ |
| **`part-07-ai-era/00-overview.md`** | 16 處，章節依存圖含Ch 40/H/I 拓樸 | ⭐⭐ |
| **各補章自身 frontmatter 的「插入位置」段** | 重編號後此段意義消失，需改寫或刪除 | ⭐⭐ |
| **Ch 41/I/D 內部相互引用** | 補章間互引需轉成新章號 | ⭐⭐ |
| **`front-matter/02-how-to-read.md`** | mermaid 圖節點 ID 可能用了 chA、chF | ⭐ |

---

## Phase 5｜最終驗證清單

```bash
# 1. 補章字樣清零
grep -rE "補章\s*[A-I]" book/

# 2. 舊檔名引用清零
grep -rE "ch[A-I]-[a-z\-]+\.md" book/

# 3. frontmatter 全為數字
grep -rE "^chapter:\s*[A-I]" book/

# 4. 手動抽樣 5 章，確認章號一致（標題、frontmatter、相對引用）
# 5. 抽樣點開 10 個交叉連結確認檔案存在
# 6. 比對 SUMMARY.md 條目數：應為 53 章 + 7 附錄 + 3 前置
```

---

## 風險矩陣

| 風險 | 機率 | 衝擊 | 緩解方式 |
|---|---|---|---|
| 章號替換連鎖污染（Ch 18→18 把新 Ch 19 又改成 19） | 高 | 高 | 強制使用佔位符兩階段法，絕不直接 `s/Ch 18/Ch 19/` |
| 中文 / 全形空格在 grep 漏抓 | 中 | 高 | Phase 2.3 先盤點所有變體，腳本支援多 pattern |
| 附錄 D 案例索引綁了補章字母 ID（如 `CASE-CHA-*`） | 中 | 中 | Phase 0 加做案例 ID 盤點，有則改為 `CASE-CH26-*` |
| Glossary 詞條「來源章節」過時 | 高 | 低 | Phase 4 手工掃 annex-f |
| 外部已分享連結 / 截圖 / 社群引用失效 | 100% | 中 | Commit message 記錄對照，可選在 README 保留重定向表 |
| 操作期間有未 commit 的草稿 | 中 | 高 | 開始前確認 `git status` 為 clean；或先 `git stash` |

---

## 估時

| Phase | 估時 |
|---|---|
| Phase 0 決策確認 | 5 分鐘 |
| Phase 1 對照表 + 變體盤點 | 30 分鐘 |
| Phase 2 腳本撰寫 + 自測 | 1 小時 |
| Phase 3 Commit 1–6（機械化） | 2 小時 |
| Phase 4 高風險區稽核 | 2 小時 |
| Phase 5 驗證 + 修補 | 30 分鐘 |
| **總計** | **約 6 小時** |

---

## Rollback 策略

每個 commit 均為原子操作，可 `git revert` 單獨回滾。
最壞情況用 `git reset --hard <原始 commit hash>` + `git push --force-with-lease` 一鍵還原。
**腳本失控時務必先 `git diff` 確認，不要直接 `git add -A && commit`。**
