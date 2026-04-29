---
chapter: 0
part: front-matter
title: 章節依存圖
slug: how-to-read
status: published
---

# 02 章節依存圖 ⸺ 如何讀這本書

## 全書八篇地圖

```mermaid
flowchart LR
    subgraph I[第 I 篇 認知基礎]
      C1[Ch 1 為什麼 SA SD]
      C2[Ch 2 SDLC 演進]
      C3[Ch 3 啟動與利害關係人]
      C4[Ch 4 需求工程]
      C5[Ch 5 UML 全景]
    end
    subgraph II[第 II 篇 分析]
      C6[Ch 6 DFD]
      C7[Ch 7 OOA]
      C8[Ch 8 資料模型]
      C9[Ch 9 流程模型]
      C10[Ch 10 規格文件]
    end
    subgraph III[第 III 篇 設計基礎]
      C11[Ch 11 架構原則]
      C12[Ch 12 設計模式]
      C13[Ch 13 架構風格]
      C14[Ch 14 API 設計]
      C15[Ch 15 資料儲存]
      C16[Ch 16 UI UX]
      F[補 F CUX]
    end
    subgraph IV[第 IV 篇 進階架構]
      C17[Ch 17 DDD]
      C18[Ch 18 Event Storming]
      C19[Ch 19 C4]
      C20[Ch 20 Modular Monolith]
      C21[Ch 21 微服務]
      C22[Ch 22 EDA CQRS ES]
      C23[Ch 23 K8s]
      C24[Ch 24 Mesh Cell]
      A[補 A 邊緣 OT-IT]
    end
    subgraph V[第 V 篇 品質屬性]
      C25[Ch 25 Security]
      E[補 E Compliance]
      C26[Ch 26 Observability]
      C27[Ch 27 SRE Chaos]
      C28[Ch 28 Data Architecture]
    end
    subgraph VI[第 VI 篇 現代工程]
      C29[Ch 29 Platform IDP]
      C30[Ch 30 ADR]
      C31[Ch 31 Fitness Function]
      C32[Ch 32 FinOps Green]
    end
    subgraph VII[第 VII 篇 AI 時代]
      C33[Ch 33 AI-Native]
      C34[Ch 34 CDE]
      C35[Ch 35 RAG Memory Tool]
      C36[Ch 36 Multi-Agent]
      D[補 D 共識衝突]
      C37[Ch 37 Coding Agent]
      C38[Ch 38 Eval Drift]
      B[補 B Agentic QA]
      Cs[補 C Brownfield + AI 逆向]
    end
    subgraph VIII[第 VIII 篇 綜合]
      C39[Ch 39 Capstone]
    end

    I --> II --> III --> IV --> V --> VI --> VII --> VIII

    classDef cold fill:#eef,stroke:#36c
    classDef goal fill:#efe,stroke:#3a3
    classDef hot fill:#fee,stroke:#c33
    class C1,C2,C3,C4,C5 cold
    class C6,C7,C8,C9,C10 cold
    class C11,C12,C13,C14,C15,C16 cold
    class C17,C18,C19,C20,C21,C22,C23,C24 goal
    class C25,C26,C27,C28 goal
    class C29,C30,C31,C32 goal
    class C33,C34,C35,C36,C37,C38 goal
    class A,B,Cs,D,E,F hot
    class C39 hot
```

## 跨章關鍵依賴

```mermaid
flowchart LR
    Ch1[Ch 1<br/>System Charter] --> Ch30[Ch 30 ADR]
    Ch1 --> Ch34[Ch 34 CDE]

    Ch4[Ch 4 需求工程] --> Ch10[Ch 10 PRD/SRS/MVP]
    Ch4 --> Ch17[Ch 17 DDD]

    Ch5[Ch 5 UML] --> Ch7[Ch 7 OOA]
    Ch5 --> Ch19[Ch 19 C4]

    Ch7[Ch 7 OOA] --> Ch9[Ch 9 流程模型]
    Ch7 --> Ch17[Ch 17 DDD]

    Ch11[Ch 11 SOLID] --> Ch13[Ch 13 架構風格]
    Ch11 --> Ch31[Ch 31 Fitness Function]

    Ch17[Ch 17 DDD] --> Ch18[Ch 18 Event Storming]
    Ch17 --> Ch20[Ch 20 Modular Monolith]
    Ch17 --> Ch22[Ch 22 EDA/ES]

    Ch20 --> Ch21[Ch 21 微服務]
    Ch21 --> Ch24[Ch 24 Mesh/Cell]
    Ch24 --> ChA[補 A 邊緣]

    Ch25[Ch 25 Security] --> ChE[補 E Compliance]
    ChE --> Ch33[Ch 33 AI-Native]

    Ch26[Ch 26 OTel] --> Ch27[Ch 27 SRE]
    Ch27 --> Ch31[Ch 31 Fitness Function]
    Ch27 --> Ch38[Ch 38 AI Eval]

    Ch30[Ch 30 ADR] --> Ch31
    Ch30 --> Ch34[Ch 34 CDE]

    Ch33[Ch 33 AI-Native] --> Ch34
    Ch33 --> Ch35[Ch 35 RAG/Memory/Tool]
    Ch33 --> Ch36[Ch 36 Multi-Agent]
    Ch36 --> ChD[補 D 共識]

    Ch34 --> Ch37[Ch 37 Coding Agent]
    Ch37 --> ChCs[補 C Brownfield AI]

    Ch38[Ch 38 AI Eval] --> ChB[補 B Agentic QA]

    Ch39[Ch 39 Capstone] -.整合全書.-> Ch1

    classDef cold fill:#eef,stroke:#36c
    classDef hot fill:#fee,stroke:#c33
    classDef goal fill:#efe,stroke:#3a3
    class Ch1,Ch4,Ch5,Ch7,Ch11,Ch17,Ch20,Ch25,Ch26,Ch30,Ch33 cold
    class ChA,ChB,ChCs,ChD,ChE goal
    class Ch39 hot
```

## 解讀

- **左到右是預設閱讀順序**(I → VIII)。
- **跨章箭頭代表觀念依賴**(後章用到前章的工具或語彙)。
- **6 個補章(A、B、C、D、E、F)**穿插在主章流程中,點出主大綱的 6 個盲點。
- **Ch 39 Capstone** 不是新內容,是把全書 38 章 + 6 補章串成一個 PayLoop 2.0 故事。

## 跳章策略

| 你的需求 | 建議跳到 |
|---|---|
| 馬上要寫 PRD | Ch 4 → Ch 10 |
| 要決定拆不拆微服務 | Ch 1 → Ch 17 → **Ch 20** → Ch 21 |
| 接手遺留系統 | Ch 1 → **補章 C** → Ch 17 → Ch 20 |
| 要引入 AI Agent 工具 | Ch 30 → Ch 34 → Ch 37 → **補章 B** |
| 要做 Compliance 評估 | Ch 25 → **補章 E** → Ch 33 |
| 想看一個整合案例 | **Ch 39 Capstone**(可從這裡開始倒讀) |

## 章節長度概覽

| 篇 | 章數 | 平均字元數 | 特點 |
|---|---|---|---|
| I 認知基礎 | 5 | 25K | 短而緊湊 |
| II 分析 | 5 | 25K | 工具與技法 |
| III 設計基礎 | 6 + 1 補 | 28K | 設計詞彙 |
| IV 進階架構 | 8 + 1 補 | 32K | 密度最高的一段 |
| V 品質屬性 | 4 + 1 補 | 32K | 多 cross-cut |
| VI 現代工程 | 4 | 31K | 工程實踐 |
| VII AI 時代 | 6 + 3 補 | 35K | 篇幅最長 |
| VIII 綜合 | 1 | 47K | 整合章 |

---

下一站:[Ch 1 為什麼系統分析與系統設計](../part-01-foundations/ch-01-why-sa-sd.md)。
