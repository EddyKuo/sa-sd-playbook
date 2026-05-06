---
part: VII
title: 第 VII 篇導讀 — AI 時代的 SA/SD
type: overview
chapters: [33, 34, 35, 36, 37, 38, "B", "C", "D", "H", "I"]
---

# 第 VII 篇|AI 時代的 SA/SD

> **NorthVale 那位病安長看著 LangSmith trace 問:「我們明明寫『AI 輔助分流』,為什麼 LLM 一旦答了,系統就直接把答案送進去,沒有人再看一眼?」這篇六章加三個補章,就是在回答這個問題。**

---

AI 工具讓工程師寫得更快了。但沒有人告訴你,**AI 寫出來的程式需要一個更清楚的「為什麼」才能被信任**。

第 VII 篇是全書密度最高的一篇。它不假設你反對 AI,也不假設你相信 AI 能解決所有問題。它假設你已經在用 AI 工具,而且開始遇到它帶來的新問題:LLM 怎麼和現有架構接線?Agent 的邊界怎麼劃?多個 Agent 衝突怎麼解?AI 寫的程式怎麼測?舊系統怎麼在 AI 的幫助下現代化?

六章依**系統複雜度增長**的順序排列:單一 LLM 接入(Ch 36)→ Context 設計(Ch 37)→ Memory 與 Tool(Ch 38)→ Multi-Agent(Ch 39)→ AI 寫程式(Ch 43)→ 評估與紅隊(Ch 44)。五個補章在旁邊等著回答五個更深的問題:非確定性系統的 QA(Ch 45)、用 AI 逆向現有系統(Ch 46)、Multi-Agent 的共識與衝突(Ch 40)、Agent 設定語言作為 SA 的新交付物(Ch 41)、Agent Harness 工程把模型變成可用代理(Ch 42)。

---

## 篇內章節依存圖

```mermaid
flowchart LR
    VI["第 VI 篇<br/>現代工程實踐"] --> CH33

    CH33["Ch 36<br/>AI-Native 架構"] --> CH34["Ch 37<br/>CDE"]
    CH34 --> CH35["Ch 38<br/>RAG/Memory/Tool"]
    CH35 --> CH36["Ch 39<br/>Multi-Agent"]
    CH36 --> CHD["Ch 40<br/>Multi-Agent 共識"]
    CH33 --> CH37["Ch 43<br/>AI Coding Agent"]
    CH36 --> CH38["Ch 44<br/>AI Eval/Drift/Red Team"]
    CH38 --> CHB["Ch 45<br/>Agentic QA"]
    CH37 --> CHC["Ch 46<br/>遺留現代化/AI 逆向"]
    CH36 --> CHH["Ch 41<br/>Agent 設定語言"]
    CHH --> CHI["Ch 42<br/>Agent Harness 工程"]
    CH38 -.串接.-> CHI

    CHB -.解鎖.-> VIII["第 VIII 篇<br/>Capstone"]
    CHD -.解鎖.-> VIII
    CH38 -.解鎖.-> VIII
    CHH -.解鎖.-> VIII
    CHI -.解鎖.-> VIII

    classDef cold fill:#eef,stroke:#36c
    classDef goal fill:#efe,stroke:#3a3
    class CH33,CH34,CH35,CH36,CH37,CH38,CHB,CHC,CHD,CHH,CHI cold
    class VIII goal
    class VI goal
```

---

## 各章核心問句

| 章 | 標題簡稱 | 這章回答的真正問題 |
|---|---|---|
| Ch 36 | AI-Native 架構 | AI-Embedded / Augmented / Native 三個層次,差別在哪裡? |
| Ch 37 | CDE | CLAUDE.md 和 agents.md 是文件還是架構的一部分? |
| Ch 38 | RAG / Memory / Tool | 三種記憶(Semantic / Episodic / Procedural)各自解決什麼問題? |
| Ch 39 | Multi-Agent | 更多 Agent ≠ 更好——什麼時候該拆,什麼時候該合? |
| Ch 43 | AI Coding Agent | 讓 AI 寫程式和讓 AI 審程式,信任模型一樣嗎? |
| Ch 44 | AI Eval / Drift / Red Team | LLM 的「通過率」和傳統軟體的「通過率」,是同一種概念嗎? |
| Ch 45 | Agentic QA | 當系統的輸出不確定時,測試的定義要怎麼改? |
| Ch 46 | 遺留現代化 / AI 逆向 | 用 AI 讀懂一個沒有文件的遺留系統——從哪裡開始? |
| Ch 40 | Multi-Agent 共識 | 兩個 Agent 給出相反結論時,誰說了算? |
| Ch 41 | Agent 設定語言 | Agent 的職責邊界是 SA 規格還是工程師的字串?跨廠商的通用框架長什麼樣? |
| Ch 42 | Agent Harness 工程 | 模型升級分數漲、merge 率不漲——SA 該規格的是哪一層? |

---

## 不同讀者的建議入口

- **剛開始接觸 LLM 應用開發**:Ch 36 → Ch 37 → Ch 38。三章讀完你能設計一個有 Context 管理和 Memory 機制的 AI 功能。
- **正在做 Multi-Agent 系統**:Ch 39 → Ch 40。兩章對應「拆 Agent 的標準」和「Agent 衝突的仲裁機制」。
- **AI 工具的重度使用者(Cursor / Claude Code)**:Ch 43 是你的主章——AI Coding Agent 的委託模型、PR 審查標準、回歸測試策略。
- **QA 工程師**:Ch 45 是你在 AI 時代的新工作定義。比主章更值得先讀。
- **正在做遺留系統評估**:Ch 46 從「AI 逆向工程現有 codebase」的技術開始,到「選擇現代化策略」的決策框架結束。
- **SA / 系統架構師接到 Multi-Agent 系統設計**:Ch 41 → Ch 42。前者把 Agent 規格從工程師腦袋裡提出來,後者把跑 Agent 的執行層做成可審查的 SA 交付物。兩章配對,是 chH「寫什麼」與 chI「怎麼跑」的對位。

---

## 前後篇連結

- **前置**:[第 VI 篇 現代工程實踐](../part-06-engineering/00-overview.md)（ADR 和 Fitness Functions 是 AI 時代工程實踐的地基）
- **這篇解鎖**:[第 VIII 篇 Capstone](../part-08-synthesis/00-overview.md) — 全部工具接上之後,Ch 47 用一個完整案例走一遍
- **長距離影響**:這篇是全書所有前置知識的集大成。Ch 18 DDD 的 Bounded Context 在 Ch 39 重出現為 Agent 邊界;Ch 27 的安全設計在 Ch 44 重出現為 AI 的 Red Team;Ch 34 的 Fitness Functions 在Ch 45 重出現為 Agentic QA 的自動化驗證點
