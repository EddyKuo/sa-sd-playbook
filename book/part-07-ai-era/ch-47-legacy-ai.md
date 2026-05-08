---
chapter: 47
part: VII
title: Ch 47｜遺留系統現代化與 AI 逆向工程
slug: legacy-ai
agent: SA
skills_used:
  - sa/arch-monolith
  - sa/arch-microservice
  - shared/meta-skill-factory
  - shared/domain-fintech
domain_case: CASE-FIN-011
reviewers: [PM, QA, Orchestrator]
status: migrated
word_count_target: 6500
---

# Ch 47｜遺留系統現代化與 AI 逆向工程
## ⸺ Brownfield Modernization with Agent-Assisted Reverse Engineering

> **前置閱讀**:[Ch 18 DDD](../part-04-architecture/ch-18-ddd-strategic-tactical.md)、[Ch 21 Modular Monolith](../part-04-architecture/ch-21-modular-monolith.md)、[Ch 37 CDE](./ch-38-context-driven-engineering.md)、[Ch 43 Coding Agent](./ch-44-coding-agent.md)
> **下游章節**:[Ch 47 Capstone](../part-08-synthesis/ch-48-capstone.md)
> **延伸補章**:[Ch 45 Agentic QA](./ch-46-agentic-qa.md)

---

## 47.1 冷觀察 ⸺ 主大綱默認在 Greenfield,但你大概率不在

打開主大綱重讀:[Ch 18](../part-04-architecture/ch-18-ddd-strategic-tactical.md) 談 DDD 從 Bounded Context 開始畫,[Ch 20](../part-04-architecture/ch-20-c4-model-visualization.md) C4 從 System Context 圖開始畫,[Ch 23](../part-04-architecture/ch-23-event-driven-cqrs-es.md) Event Sourcing 假設能重新設計事件流。

**這些都是 Greenfield 視角**。

但任何在現場待過 5 年以上的工程師都知道:接手的系統,大概率是一個 7 年前由某個離職資深工程師寫的 Java EE 應用,跑在 WebLogic 上,跟一個 PL/SQL 資料庫深度耦合,沒有單元測試,沒有文件,業務規則散落在 5,000 行的 stored procedure 裡(`CASE-FIN-011`)。

[Ch 21](../part-04-architecture/ch-21-modular-monolith.md) 提到 Strangler Fig 模式 ⸺ 這是現代化的「目標形狀」,但不是「行動方案」。Strangler Fig 假設已經知道**舊系統做了什麼**。**現實是:不知道**。原作者離職了,文件不存在,使用者只知道「按這個鈕會觸發那個流程」。

這一章談的是:**在這種狀態下,如何用 AI Agent 逆向找回知識,然後設計現代化路徑**。

```mermaid
flowchart LR
    subgraph Old[傳統 SA]
      A1[訪談人類]
      A2[業務需求往下推]
      A3[假設原作者意圖明確]
      A4[產出 To-Be]
    end
    subgraph Arch[程式碼考古學 Code Archaeology]
      B1[訪談人類 + 程式碼 + DB + 日誌]
      B2[從現有行為往上推 + 對校]
      B3[假設意圖部分丟失 需重建]
      B4[產出 As-Is + To-Be + Migration Path]
    end

    classDef cold fill:#eef,stroke:#36c
    classDef goal fill:#efe,stroke:#3a3
    class A1,A2,A3,A4 cold
    class B1,B2,B3,B4 goal
```

## 47.2 真問題 ⸺ 用 Agent 做逆向工程的四個層次

不要把 Agent 當成「貼進去問問題」的工具。它能做的事分四個層次,要分階段使用。

| Level | 名稱 | 內容 | 適用工具 | Agent 角色 |
|---|---|---|---|---|
| **L1** | Lexical(詞彙層) | 抽取所有類別、函式、表名、欄名;統計呼叫頻率、依賴關係;找出明顯死碼 | SonarQube、Understand、CodeQL | 價值不大 |
| **L2** | Structural(結構層) | 重建模組依賴圖、類別繼承樹、ER 圖;找出循環依賴、上帝物件、跨層耦合 | CodeQL + Agent 摘要 | Agent 把工具輸出翻譯成人話與圖示 |
| **L3** | Behavioral(行為層) | 給定入口追蹤執行路徑;從 stored procedure 提取業務規則;識別「看似相同但暗藏差異」程式碼;把日誌反推回程式碼路徑 | Claude Code、Cursor、Antigravity、Codex CLI | **Agent 真正開始發光的地方**,需要長上下文與工具呼叫 |
| **L4** | Domain(領域層) | 從程式碼推回 Ubiquitous Language;為每一個 Bounded Context 寫考古報告;對照訪談標記矛盾點(程式碼這樣寫、使用者描述不一樣 → 一定有故事) | Claude Code + 領域專家 | **必須人類主導,Agent 輔助**。Agent 可提案,人類必須驗證 |

## 47.3 決策框架 ⸺ IDE / Agent 工具取捨與三段式遷移

### 47.3.1 IDE / Agent 工具取捨(2026 現實)

[Ch 37 CDE](./ch-38-context-driven-engineering.md) 與 [Ch 43 Coding Agent](./ch-44-coding-agent.md) 提到了 Context-Driven Engineering 與工具,但沒針對「逆向工程」場景做選型。這裡補上:

| 工具 | 上下文視窗 | Brownfield 適合度 | 取捨 |
|---|---|---|---|
| **Google Antigravity**(Gemini 3.1 Pro) | 200 萬 token | ★★★★★ 大型 codebase 整體理解 | 可一口氣吃下整個中型 monorepo,但 production 穩定性仍差。**用它做分析,不用它做生產修改**。 |
| **Cursor**(Claude Sonnet 4.6 / GPT-5.1) | ~200K | ★★★★ 精準局部修改 | SOC 2 + GDPR 合規通過,適合在嚴肅環境做小範圍修改。Shadow workspace 是 Brownfield 救命特性。 |
| **Claude Code**(Claude Opus / Sonnet) | ~200K(可分段) | ★★★★★ 終端原生 + 80.8% SWE-Bench | 主力。Skills + Subagent 機制能把考古經驗模組化。 |
| **Aider**(多模型) | 隨模型 | ★★★ 輕量、git-native | 適合 git history 重建、commit-by-commit 重構。 |
| **GitHub Copilot Workspace** | 隨模型 | ★★★ 與 PR 流程整合好 | 適合「已知道要改什麼」的場景,Brownfield 探索性差。 |

**一個務實的工具組合**:實務上會用兩到三套疊加 ⸺ Antigravity / Gemini 3.1 Pro 跑一次「全景考古」,生成宏觀報告後就停(**不寫回任何檔案**);Claude Code 主力編碼,跑深度逆向工程,提取業務規則,寫進文件,Skills 設計成「逆向某個 stored procedure 並產出 PRD」這類;Cursor 進入修改階段做精準 refactor,Shadow workspace 確保不污染主分支。

### 47.3.2 從 As-Is 到 To-Be 的安全平滑遷移

這是最容易翻車的環節。一旦提取出 As-Is 領域模型,開始畫 To-Be,**80% 的失敗在這裡發生**:To-Be 畫得太理想、跟 As-Is 不接、導致遷移路徑根本走不通。

**三條黃金規則**:

| 規則 | 內容 |
|---|---|
| **規則一:To-Be 必須能用 As-Is 的語言被解釋** | 如果 To-Be 引入了 As-Is 完全沒有的概念(如新的 Bounded Context),必須能在現有業務語言中為它找到對應。否則使用者訓練成本會殺死整個專案。 |
| **規則二:任何 To-Be 模組必須有「並行運轉一個月」的計畫** | 新模組接管舊模組之前,讓兩者並行跑、輸出比對。Stripe、GitLab、Shopify 在大型遷移上都用這套。 |
| **規則三:Strangler Fig 必須有「中途停下來」的設計** | 做到一半發現方向錯了,要能停在中間狀態繼續運轉,而不是「全有或全無」。舊新模組之間必須維持雙向相容。 |

### 47.3.3 一個典型的遷移迭代

```mermaid
flowchart TD
    Start([迭代 N 開始]) --> S1[Step 1: 用 As-Is 領域模型挑邊界明確的舊模組]
    S1 --> S2[Step 2: 寫契約測試 以舊模組行為為基準]
    S2 --> S3[Step 3: 用 Agent 生成 To-Be 模組骨架]
    S3 --> S4[Step 4: 並行運轉 舊模組仍是 source of truth]
    S4 --> S5{Step 5: 比對輸出 差異分類}
    S5 -->|舊模組 bug| F1[為 To-Be 寫對的版本 留 ADR]
    S5 -->|To-Be bug| F2[修]
    S5 -->|業務歧義 沒人記得當初為什麼| F3[召集利害關係人決議]
    F1 --> S6[Step 6: 切換流量 從 1% canary 起逐週加碼]
    F2 --> S6
    F3 --> S6
    S6 --> S7[Step 7: 退役舊模組]

    classDef cold fill:#eef,stroke:#36c
    classDef goal fill:#efe,stroke:#3a3
    classDef hot fill:#fee,stroke:#c33
    class S1,S2,S3,S4 cold
    class S5,F3 hot
    class F1,F2,S6,S7 goal
```

每一個迭代產出一份 ADR + 一份「考古報告」,慢慢累積整個系統的知識資產。

---

## 47.4 踩坑清單

### 反模式 1:相信 Agent 的初次摘要

給它一個 2 萬行的 service,它會自信地告訴你業務邏輯。但常常半對半錯。

> ✅ **修正方向**:重要環節人工驗證至少 3 次。Agent 摘要寫進「考古報告草稿」,不直接寫進 ADR。每條業務規則記載出處(檔名 + 行號)、推導理由、置信度(High / Medium / Low)。

### 反模式 2:相信 Agent「幻覺出來的 API」

Agent 有時會發明不存在的函式呼叫,看起來合理但實際 codebase 沒有這個 method。

> ✅ **修正方向**:寫程式碼前必須驗證真實存在(grep / IDE go-to-definition)。在 Agent 工作流中加一條「rule:任何 API 呼叫必須附上 file path + line number 的證據」,沒附證據的 API 視為幻覺。

### 反模式 3:讓 Agent 自己決定刪除程式碼

Agent 看了一段沒被呼叫的程式碼說「這是 dead code 可以刪」⸺ 但 Agent 看不到 cron job、爬蟲、外部整合等隱性觸發路徑。

> ✅ **修正方向**:死碼分析永遠假設「可能漏看了某條觸發路徑」。要刪,必須有人簽字。先 deprecation period(加 log 警告 + 監控 30 天無觸發)再刪。

### 反模式 4:忽略隱性權限與資料庫 trigger

舊系統的權限模型常常是隱含的(「這個欄位只有特定 role 看得到,但檢查邏輯散在 5 個地方」)、資料庫 trigger 與 stored procedure 一樣是業務規則藏身處,Agent 容易漏掉。

> ✅ **修正方向**:在考古 Skill 中加固定 checklist:(1) trigger 列表 + 每個 trigger 的觸發條件 + 副作用;(2) 散落在多處的權限檢查(grep `if user.role` 類);(3) 跨系統整合(cron / 爬蟲 / 共享 DB)需訪談 + 日誌分析。Agent 看不到的,人類補上。

---

## 47.5 交付清單

完成本章後,讀者應產出:

````markdown
# Brownfield Modernization Pack — {專案名稱}

## 1. As-Is Bounded Context Map
- [ ] 從程式碼考古推回的領域模型
- [ ] 每個 Context 的 Ubiquitous Language Top 10
- [ ] 與訪談的矛盾點清單

## 2. Business Rules Catalog
- [ ] 每條規則:出處(檔名 + 行號)/ 推導理由 / 置信度(High/Medium/Low)
- [ ] 規則之間的依賴 / 互斥關係

## 3. Migration Dependency Graph
- [ ] 模組之間的拆解順序與依賴
- [ ] 並行運轉時的 source of truth 標註

## 4. Migration ADR Set
- [ ] 每一個重要決策有理由
- [ ] 每個 ADR 連結到對應「考古報告」

## 5. Parallel Run Comparison Report
- [ ] 舊新差異分類:舊 bug / To-Be bug / 業務歧義
- [ ] 處置紀錄與簽核

## 6. 工具組合配置
- [ ] L1/L2(SonarQube / CodeQL)
- [ ] L3(Claude Code Skills 設計)
- [ ] L4(人類主導 + Agent 提案的工作流)
````

放在 `docs/brownfield/`,與程式碼同 repo。

---

## 47.6 Recap

讀完本章,應該已經能做到:

- [ ] 認得出主大綱章節哪些是 Greenfield 視角、在 Brownfield 必須補做考古
- [ ] 把 AI Agent 逆向工程分四層使用(L1 Lexical / L2 Structural / L3 Behavioral / L4 Domain)
- [ ] 用 Antigravity + Claude Code + Cursor 三套工具的組合策略
- [ ] 遵守 As-Is → To-Be 三條黃金規則(語言可解釋 / 並行運轉 / 中途可停)
- [ ] 在每個遷移迭代產出 ADR + 考古報告,累積系統知識資產

如果先挑一項做,建議是 L4 領域層的「考古報告」⸺ 它是把程式碼知識翻譯回業務語言的橋樑,有了它,後面所有的遷移決策才有共同語言。

---

## Cross-References

- **前置**:[Ch 18 DDD](../part-04-architecture/ch-18-ddd-strategic-tactical.md)、[Ch 21 Modular Monolith](../part-04-architecture/ch-21-modular-monolith.md)、[Ch 37 CDE](./ch-38-context-driven-engineering.md)、[Ch 43 Coding Agent](./ch-44-coding-agent.md)
- **下游**:[Ch 47 Capstone](../part-08-synthesis/ch-48-capstone.md)
- **延伸補章**:[Ch 45 Agentic QA](./ch-46-agentic-qa.md)

## 引用

本章無外部文獻引用。
