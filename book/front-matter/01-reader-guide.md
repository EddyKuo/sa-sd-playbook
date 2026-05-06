---
chapter: 0
part: front-matter
title: 三層讀者導引
slug: reader-guide
status: published
---

# 01 三層讀者導引 ⸺ 你可以這樣讀這本書

## 三條建議路徑

| 讀者輪廓 | 建議路徑 | 預期完成時間 | 預期收穫 |
|---|---|---|---|
| **新手(0–2 年)** | I → II → III(可跳Ch 17)→ Ch 47 Capstone | 4–6 週 | 完整需求拆解能力、UML 三圖、設計原則、最小 artifact 套件 |
| **進階(3–8 年)** | 上述 + IV → V → VI + Ch 26(若有 OT)、E(若有合規) | 6–10 週 | 進階架構、品質屬性、現代工程實踐;能設計中型系統 |
| **資深 / 架構師(8+)** | 全書 + 重點 IV / VI / VII + 全部補章 | 8–12 週 | AI 時代 SA/SD 整合視角、能帶領團隊建立 Capstone Pack |

## 路徑詳解

### 路徑 A:新手(0–2 年工程經驗)

**目標**:能獨立完成一個中等規模系統的 SA/SD 工作。

**章節地圖**:
1. **Ch 1 → Ch 5(認知基礎)**:理解 SA/SD 在 2026 年的定位、需求工程基本功。
2. **Ch 6 → Ch 10(分析)**:DFD、OOA、ERD、流程模型、規格文件五件事。
3. **Ch 11 → Ch 16(設計基礎)**:SOLID、設計模式、架構風格、API、儲存、UX 系統觀。
4. **Ch 47 Capstone**:把上述工具串起的整合練習。

**可選跳過**:Ch 16 Ch 17(多模態 / CUX),除非工作直接涉及。

**最小 artifact 帶走清單**:System Charter、Project Initiation Brief、Requirements Decision Log、Use Case Atom、Schema Decision Card、API Contract Card、Coupling Audit Card。

### 路徑 B:進階(3–8 年工程經驗)

**目標**:能設計分散式系統、做出有品質屬性保障的架構決策、引入 AI 工具進團隊。

**章節地圖**:
1. **路徑 A 的全部章節**(已熟練可快速複習)。
2. **Ch 18 → Ch 25(進階架構)**:DDD、Event Storming、C4、Modular Monolith、微服務、EDA、K8s、Mesh / Cell + Ch 26(邊緣 / OT-IT)。
3. **Ch 27 → Ch 31(品質屬性)**:Security、Observability、SRE、Data Architecture + Ch 28(Compliance)。
4. **Ch 32 → Ch 35(現代工程實踐)**:Platform Engineering、ADR、Fitness Function、FinOps。

**選讀**:Ch 36 → Ch 38(AI 時代起手三章),理解 AI-Native、CDE、RAG / Memory / Tool 設計。

**新增 artifact**:Bounded Context Card、Event Storming Outcome Card、Microservice Tax Card、EDA Layer Card、Observability Plane Card、SLO Catalog、ADR Template、Fitness Function Card、Platform Product Card。

### 路徑 C:資深 / 架構師(8+ 年)

**目標**:在 AI 時代帶領團隊重建 SA/SD 整套劇本,建立組織級的 Capstone Pack。

**章節地圖**:
1. **路徑 A + B 的全部章節**(已熟,作為共同語言)。
2. **Ch 36 → Ch 44(AI 時代)**:AI-Native、CDE、RAG / Memory / Tool、Multi-Agent、Coding Agent、Eval / Drift / Red Team。
3. **6 個補章全部讀**:A(邊緣)、B(Agentic QA)、C(Brownfield 現代化)、D(Multi-Agent 共識)、E(合規)、F(CUX)。
4. **Ch 47 Capstone**:把 PayLoop 2.0 案例當作組織內可複製的整合範本。

**新增 artifact**:AI-Native System Vision Card、CDE Setup Card、Agent System Card、Multi-Agent System Card、Agent-Friendly Codebase Card、AI Quality Card、OT/IT Edge Design Pack、Compliance Design Pack、Agentic QA Pack、Brownfield Modernization Pack、Multi-Agent Consensus Pack。

## 跨路徑使用建議

### 工作對應路徑

| 工作場景 | 重點章節 |
|---|---|
| 新建一個 SaaS 產品 | Ch 1, 2, 3, 4, 10, 11, 13, 14, 15, 17, 20, 23, 25, 27 |
| 重構遺留系統 | Ch 1, 17, 20, 30, 31 + **Ch 46** + **Ch 47 Capstone** |
| 引入 AI Agent 進工程流程 | Ch 33, 33, 34, 37 + **Ch 45** + **Ch 47** |
| 建立 Platform Engineering | Ch 24, 24, 26, 27, **29**, 30, 31, 32 |
| 處理工業 / OT 系統 | Ch 13, 23, 24 + **Ch 26** + Ch 31 + **Ch 28** |
| 醫療 / 金融受監管系統 | Ch 27, 28 + **Ch 28** + Ch 36, 38 + **Ch 45** |
| 從 monolith 拆微服務 | Ch 18, 18, **20**, 21, 22 + **Ch 46** |
| 設計 RAG / Agent 應用 | Ch 14, 15, 25, **33**, **34**, **35**, 36, 38 + **Ch 45**, **E** |

## 章節依存關係

詳見 [02-how-to-read.md](./02-how-to-read.md) 的 Mermaid 章節依存圖。

## 三條原則,給每位讀者

1. **跳章節是被允許的**。本書按閱讀順序編排,但各章獨立可讀。需要時跳到對應章節,然後再回來。
2. **每章末尾的 artifact 是核心**。讀完一章只記得概念是不夠的;把那一頁帶到工作中、塞進 PR、釘在白板,才是這本書希望發生的事。
3. **PayLoop 2.0(Ch 47)是全書的縮影**。如果讀完任一篇覺得「這些怎麼整合?」,直接跳到 Ch 47 看 PayLoop 2.0 怎麼用該篇章節的工具。

---

下一站:[02 章節依存圖 — 如何讀這本書](./02-how-to-read.md)。
