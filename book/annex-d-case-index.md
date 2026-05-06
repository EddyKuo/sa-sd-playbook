---
chapter: 40
part: annex
title: 附錄 D — 案例索引(43 個虛構案例)
slug: case-index
status: published
---

# 附錄 D|案例索引(43 個虛構案例)

> 全書所有案例**純虛構**(公司名、產品名、數字),但業務邏輯與技術細節真實可驗證。完整定義見 [`_refs/case-registry.yaml`](_refs/case-registry.yaml)。本附錄按領域與章節整理。

---

## 領域分布(Domain Mix)

| 領域 | 案例數 | 占比 |
|---|---|---|
| **fintech**(支付 / 銀行 / 風控) | 12 | 28% |
| **ecommerce**(零售 / 訂閱 / 平台) | 9 | 21% |
| **saas**(B2B / 多租戶 / 工具) | 9 | 21% |
| **healthcare**(醫療 / EMR / 合規) | 7 | 16% |
| **energy**(儲能 / 太陽能 / 電網) | 6 | 14% |
| **總計** | **43** | 100% |

## 按章節順序

### Ch 1 — 為什麼 SA/SD
- **CASE-FIN-001 PayLoop**(fintech)— 18 天 MVP / 180 天崩潰,跨境匯款新創因 vibe coding 缺乏脈絡持久化的事故
- **CASE-ECM-001 MeshFirst**(ecommerce)— 47 微服務 → 6 Modular Monolith 反向遷移(亦見 Ch 21)

### Ch 2 — SDLC 演進
- **CASE-ECM-002 ShelfMart vs QuickAisle**(ecommerce)— 半年 release vs 雙週迭代 / 四個 Tempo 對齊

### Ch 3 — 專案啟動
- **CASE-HCR-001 聖恩醫療體系**(healthcare)— 12 個月 EMR PoC 失敗,被夜班護理長帶領的工會擋下

### Ch 4 — 需求工程
- **CASE-SAS-001 FlowDeck**(saas)— 30 訪談 / 218 backlog / Frankenstein 流失率

### Ch 5 — UML 全景
- **CASE-ENR-001 AurumGrid vs VoltKnit**(energy)— 80 頁 11 圖 PDF 沒人讀 vs 三張 Mermaid 全公司懂

### Ch 6 — DFD
- **CASE-FIN-002 NorthBay Pay**(fintech)— 8.40 美元拒付 / 47 Kafka topics 沒人答得出

### Ch 7 — OOA
- **CASE-ECM-003 DripCycle**(ecommerce)— 訂閱快時尚 47 用例 / 18% 出包率

### Ch 8 — 資料模型 / 正規化
- **CASE-HCR-002 MedCanvas Inpatient**(healthcare)— 4 個 patient_id 在四張表上語意不同

### Ch 9 — 流程模型
- **CASE-SAS-002 LedgerPilot**(saas)— $42.13 客訴 / 7-service 流程迷宮

### Ch 10 — 規格文件
- **CASE-ENR-002 VoltMesh Energy**(energy)— PRD「即時告警」三種理解 / SAT 4 分 12 秒

### Ch 11 — SOLID / Clean / 12-Factor
- **CASE-FIN-003 AxisPay FraudGuardCore**(fintech)— 14 檔案改動半徑事故

### Ch 12 — 設計模式
- **CASE-SAS-003 MeshConduit**(saas)— 30 個 GoF 包 100 行業務的 PR 事故

### Ch 13 — 架構風格
- **CASE-HCR-003 CareLattice Health**(healthcare)— 第 9 個 EMR 從分層遷到六角

### Ch 14 — API 設計
- **CASE-ECM-004 HarborGate**(ecommerce)— 三套 schema 對不起來 / 12 萬賠款

### Ch 15 — 資料儲存
- **CASE-ENR-003 SunLedger Energy**(energy)— PG → Cassandra 反向遷移 / 90s → 4m12s

### Ch 16 — UI/UX
- **CASE-FIN-004 NeoLedger Bank**(fintech)— KYC 70% 放棄率 / DACR 設計復原

### Ch 17 — CUX
- **CASE-HCR-004 居家視訊看護**(healthcare)— 跌倒偵測 SDC 五層多模態

### Ch 18 — DDD
- **CASE-HCR-005 聖維禮醫療體系**(healthcare)— 三個 BC 共用 patient 的出院結算事故

### Ch 19 — Event Storming
- **CASE-SAS-004 RenewLane**(saas)— 380 張便利貼 / 兩個月零產出

### Ch 20 — C4 Model
- **CASE-FIN-005 PaySpan**(fintech)— B 輪募資 47 投影片無 Level 1/2 / 估值砍兩位數百分點

### Ch 21 — Modular Monolith
- **CASE-ECM-001 MeshFirst**(ecommerce)— 沿用 Ch 1,深入 2022→2025 演進

### Ch 22 — 微服務
- **CASE-ECM-005 TideCart**(ecommerce)— 黑五 inventory cascade 7 分鐘 6 服務同掛

### Ch 23 — EDA / CQRS / ES
- **CASE-FIN-006 CardPilot Asia**(fintech)— 三件套上線 P99 80→320ms

### Ch 24 — K8s / Cloud-Native
- **CASE-SAS-005 TenantForge**(saas)— 12 人 SaaS 上 K8s SRE 工時 8%→35%

### Ch 25 — Service Mesh / Cell-Based
- **CASE-ENR-004 GridPulse Energy**(energy)— 電網調度 Mesh control plane 12 分鐘卡死

### Ch 26 — 邊緣 / OT-IT
- **CASE-ENR-005 200kW/400kWh 儲能櫃 PoC**(energy)— 雲架構師被嗆「網路斷三十秒會放掉電池嗎」

### Ch 27 — Security by Design
- **CASE-FIN-007 PocketRail**(fintech)— OAuth refresh + 客服社交工程 NT$280 萬被盜

### Ch 28 — Compliance
- **CASE-SAS-007 多租戶 RAG 共用 vector index**(saas)— 跨租戶資料洩漏

### Ch 29 — 可觀測性
- **CASE-ECM-006 HarborPick**(ecommerce)— 黑五 12 dashboard 全綠卻掉 12%

### Ch 30 — SRE / SLO / Chaos
- **CASE-SAS-006 PolicyPilot**(saas)— 99.95% 承諾 / 99.62% 實際 / 168K 美元賠款

### Ch 31 — Data Architecture
- **CASE-HCR-006 MedNexus Health Data Network**(healthcare)— 七家醫院 Lakehouse 三年仍是「更貴 SFTP」

### Ch 32 — Platform Engineering
- **CASE-ECM-007 HarborPick Retail**(ecommerce)— 17 個內部工具 / 採用率 22%

### Ch 33 — ADR
- **CASE-FIN-008 OrbitPay**(fintech)— 盡職調查 8 名工程師 8 種版本

### Ch 34 — Fitness Functions
- **CASE-SAS-008 HelixOps**(saas)— ADR-0007 寫 Hexagonal / 18 月後 73% 反向依賴

### Ch 35 — FinOps / Green
- **CASE-ENR-006 AmpereLoom**(energy)— Q3 雲帳單 84K→230K + 寫不出 SCI 報告

### Ch 36 — AI-Native
- **CASE-HCR-007 NorthVale Health Network**(healthcare)— ER LLM Triage 把胸痛判 ESI 3

### Ch 37 — CDE
- **CASE-ECM-008 AisleNova**(ecommerce)— Cursor + Claude Code 三月 2.2x 第六月歸零

### Ch 38 — RAG / Memory / Tool
- **CASE-FIN-009 HavenAxis Bank ComplianceCopilot**(fintech)— 跨對話失憶事故

### Ch 39 — Multi-Agent
- **CASE-SAS-009 Helmsworth**(saas)— 7 Agent / P95 8s→47s

### Ch 40 — Multi-Agent 共識
- 沿用 CASE-SAS-009

### Ch 43 — Coding Agent
- **CASE-ECM-009 CartMosaic**(ecommerce)— 拆微服務後 Cursor PR 通過率 78%→24%

### Ch 44 — AI Eval / Drift / Red Team
- **CASE-FIN-010 HavenAxis AMLNavigator**(fintech)— 92%→71% 半年崩壞

### Ch 45 — Agentic QA
- 沿用 CASE-FIN-010

### Ch 46 — Brownfield + AI 逆向
- **CASE-FIN-011 7 年前 WebLogic + 5000 行 PL/SQL**(fintech)— 程式碼考古學

### Ch 47 — Capstone
- **CASE-FIN-012 PayLoop 2.0**(fintech)— 全書整合案例,從 Ch 1 PayLoop 1.0 演化(22 人 / USD 4,200 萬月流水 / 跨 5 國)

---

## 按領域檢索

### Fintech(12 個)
CASE-FIN-001 PayLoop · CASE-FIN-002 NorthBay Pay · CASE-FIN-003 AxisPay · CASE-FIN-004 NeoLedger · CASE-FIN-005 PaySpan · CASE-FIN-006 CardPilot · CASE-FIN-007 PocketRail · CASE-FIN-008 OrbitPay · CASE-FIN-009 HavenAxis ComplianceCopilot · CASE-FIN-010 HavenAxis AMLNavigator · CASE-FIN-011 WebLogic 考古 · CASE-FIN-012 PayLoop 2.0

### Ecommerce(9 個)
CASE-ECM-001 MeshFirst · CASE-ECM-002 ShelfMart vs QuickAisle · CASE-ECM-003 DripCycle · CASE-ECM-004 HarborGate · CASE-ECM-005 TideCart · CASE-ECM-006 HarborPick · CASE-ECM-007 HarborPick Retail · CASE-ECM-008 AisleNova · CASE-ECM-009 CartMosaic

### SaaS(9 個)
CASE-SAS-001 FlowDeck · CASE-SAS-002 LedgerPilot · CASE-SAS-003 MeshConduit · CASE-SAS-004 RenewLane · CASE-SAS-005 TenantForge · CASE-SAS-006 PolicyPilot · CASE-SAS-007 多租戶 RAG · CASE-SAS-008 HelixOps · CASE-SAS-009 Helmsworth

### Healthcare(7 個)
CASE-HCR-001 聖恩醫療體系 · CASE-HCR-002 MedCanvas Inpatient · CASE-HCR-003 CareLattice · CASE-HCR-004 居家看護 · CASE-HCR-005 聖維禮 · CASE-HCR-006 MedNexus · CASE-HCR-007 NorthVale Health

### Energy(6 個)
CASE-ENR-001 AurumGrid vs VoltKnit · CASE-ENR-002 VoltMesh Energy · CASE-ENR-003 SunLedger · CASE-ENR-004 GridPulse · CASE-ENR-005 200kW 儲能 PoC · CASE-ENR-006 AmpereLoom

---

## 跨章節案例

部分案例在多章使用,提供連續性:

| 案例 | 跨章節 |
|---|---|
| **CASE-FIN-001 PayLoop** | Ch 1 → Ch 47(演化為 PayLoop 2.0) |
| **CASE-ECM-001 MeshFirst** | Ch 1 → Ch 21(深入演進) |
| **CASE-FIN-010 HavenAxis AMLNavigator** | Ch 44 → Ch 45(沿用) |
| **CASE-SAS-009 Helmsworth** | Ch 39 → Ch 40(沿用) |

---

完整 case 定義(含 summary、技術棧、業務細節)見 [`_refs/case-registry.yaml`](_refs/case-registry.yaml)。
