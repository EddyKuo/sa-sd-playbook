---
chapter: 48
part: VIII
title: Capstone — 把 SA/SD 的劇本全部接上
slug: capstone
agent: Orchestrator
skills_used:
  - sa/arch-microservice
  - sa/arch-event-driven
  - sa/security-architecture
  - sa/observability
  - shared/domain-fintech
  - shared/compliance-pci-dss
domain_case: CASE-FIN-012
reviewers: [PM, SA, RD, DBA, QA, UI/UX, Orchestrator]
status: draft
word_count_target: 7500
---

# 第 48 章|Capstone
## ⸺ 把 SA/SD 的劇本全部接上

> **前置閱讀**:全書 38 主章 + Ch 26–I(本章是收束章,不重講細節,只接劇本)
> **下游章節**:附錄 1 全書術語 / 附錄 2 全書案例 / 附錄 3 全書引用 / 附錄 4 一頁式 artifact 速查 / 附錄 5 全書 ADR 範例庫
> **延伸補章**:[Ch 26 雲原生選擇](../part-04-architecture/ch-26-edge-ot-it.md)、[Ch 45 Agentic QA](../part-07-ai-era/ch-46-agentic-qa.md)、[Ch 46 遺留系統 AI 現代化](../part-07-ai-era/ch-47-legacy-ai.md)、[Ch 40 Multi-Agent Consensus](../part-07-ai-era/ch-41-multi-agent-consensus.md)、[Ch 28 Compliance by Design](../part-05-quality/ch-28-compliance.md)、[Ch 17 CUX 對話式體驗](../part-03-design/ch-17-cux.md)、[Ch 53 工程直覺保護手冊](../part-09-human-engineer/ch-54-engineering-intuition.md)、[Ch 41 Agent 設定語言](../part-07-ai-era/ch-42-agent-spec.md)、[Ch 42 Agent Harness 工程](../part-07-ai-era/ch-43-harness-engineering.md)

---

## 48.1 冷觀察 ⸺ 兩年後,同一個 CTO,被問同一句話

我在 2027 年第一季再次看到 PayLoop 的名字。

[Ch 1](../part-01-foundations/ch-01-why-sa-sd.md) 那家虛構新創,在第一場事故(`CASE-FIN-001`)之後,沒有解散,也沒有被收購。三名工程師擴成 22 人,跨境匯款業務從新加坡-越南一條走廊,加到香港、菲律賓、日本與印尼,月流水從一百萬美元成長到 4,200 萬美元(`CASE-FIN-012`,以下稱 PayLoop 2.0)。技術棧也換了:Next.js 15 退到只負責 banker 工作站的前端;後端換成 Spring Boot 3.3 + PostgreSQL 17 + pgvector + Kafka 3.7;AI 那條線,換上 Anthropic Claude Opus 4.7(1M context)+ LangGraph 0.2 跑多 Agent 風控;部署從 Vercel + Supabase,換到自管 Kubernetes 1.31 cell-based 架構,同時保留邊緣節點處理新加坡端的合規隔離。

兩年後的某一個下午,新加坡金管局(MAS)再次來敲門。這次不是事故覆盤,是例行的 thematic review,但問題依然挑釁:

> 「兩年前你們有過一次 8,400 美元差額對不上的事故。MAS 想確認,如果今天再來一次,你們六小時內能不能回答『這筆交易在你們系統裡走了哪幾步、寫了哪張表、誰是 source of truth』?」

這次 CTO 沒有沉默。她打開 IDE,在 monorepo 的根目錄敲下 `tree docs/`,投影到牆上的不是 PRD、不是 80 頁 SRS,而是這樣一棵樹:

```
docs/
├── charter.md                 # System Charter v3.2(Ch 1)
├── cadence.md                 # Cadence Charter(Ch 2)
├── stakeholders/telop.md      # 利害關係人 TELOP(Ch 3)
├── requirements/log.md        # Requirements Decision Log(Ch 4)
├── architecture/
│   ├── c4/                    # C4 四層 .dsl(Ch 20)
│   ├── adr/                   # 84 份 ADR(Ch 33)
│   └── fitness/               # 23 條 Fitness Function(Ch 34)
├── domain/
│   ├── bounded-contexts.md    # DDD BC 圖(Ch 18)
│   └── event-storming.md      # ES 結論(Ch 19)
├── api/
│   └── contracts/             # OpenAPI 3.1 + AsyncAPI 2.6(Ch 14)
├── data/
│   ├── lineage.md             # transaction_id 同名異義表(Ch 8)
│   └── storage-decisions.md   # Workload Profile(Ch 15)
├── agents/
│   ├── claude.md              # 給 Claude Code 看的 root(Ch 37)
│   ├── system-card.md         # Agent System Card(Ch 38)
│   ├── multi-agent-card.md    # Multi-Agent System Card(Ch 39)
│   ├── quality-card.md        # AI Quality Card(Ch 44)
│   ├── agent-spec.md          # Agent Spec Card(Ch 41)
│   └── harness-config.md      # Harness Engineering Card(Ch 42)
└── compliance/
    └── design-pack.md         # Compliance by Design Pack(Ch 28)
```

她沒有講話,只把游標停在 `data/lineage.md`,Ctrl+F 輸入「reconciliation」,跳出三筆 ADR 連結、一張 sequence diagram、四個 source-of-truth 標記。整個過程花了不到三分鐘。MAS 的稽核人員看了一眼,問:「這個目錄是兩年慢慢長出來的,還是一次補的?」

CTO 回了一句話,我把它原樣記下來:

> 「**它是跟著 commit 一起長的。每一次架構變動,我們都先改這裡,再改 code。當初我們只擁有一個會跑的東西;現在我們擁有它的形狀。**」

把這兩年的時間軸壓成一張圖,大概長這樣:

```mermaid
timeline
    title PayLoop 1.0 → 2.0 兩年 SA/SD 旅程
    section 月 0(事故覆盤)
      重寫 System Charter   : Ch 1 / Ch 4
      建 Requirements Decision Log : Ch 4
      畫 Bounded Context 圖 : Ch 18
    section 月 1–3(補課)
      Cadence Charter 把四個 Tempo 對上 : Ch 2
      TELOP 評估 + 找出隱性否決者 : Ch 3
      Class/Sequence/State 三張圖補上 : Ch 5
    section 月 4–9(架構重構)
      DDD 重劃 BC + Event Storming : Ch 18 / 18
      C4 四層 + Module Boundary Card : Ch 20 / 20
      Coarse-grained API + Storage 重選 : Ch 14 / 15
    section 月 10–14(品質與工程)
      SLO + Threat Model + Data Architecture : Ch 27–28
      Platform / ADR / Fitness Function / FinOps : Ch 32–32
    section 月 15–22(AI 起手)
      AI-Native L1–L7 + CDE + RAG : Ch 36–35
      Multi-Agent + Coding Agent + Eval : Ch 39–38
      Agentic QA + Compliance Pack : Ch 45 / E
    section 月 23(MAS 抽查)
      六小時答得出來的 PayLoop 2.0
```

兩年前的 PayLoop 之所以崩潰,不是因為他們沒做 SA/SD,而是因為他們**做的 SA/SD 沒留下「可被傳遞的理解」**。兩年後的 PayLoop 2.0 之所以能站住,不是因為他們做了「最佳實踐」,而是因為他們把這本書 38 主章 + 9 補章每一章交付的那張 Card,都老老實實寫成了現場的 artifact。

接下來這一章,要做的不是再講 38 章的內容,而是把這 22 個月走過的劇本接成同一張地圖 ⸺ 證明一件事:**這本書不是 39+6 章獨立內容,是同一張系統設計地圖的不同 zoom level**。

---

## 48.2 真問題 ⸺ 全書其實只在講六件事

把全書 38 主章 + 9 補章拉開來看,內容像是覆蓋了所有 SA/SD 的領域:從 UML 到 DDD、從 SOLID 到 K8s、從 Threat Model 到 LLM Eval。但若把每一章交付的那張 Card 攤開、把每一章開頭的「真問題」段落攤開,會發現全書反覆在講的,其實只有六件事。這六件事是同一張地圖的六個「定錨點」⸺ 任何一個 SA/SD 問題,最後都會落回其中一個。

把它拆開來看會比較清楚:

| 全書定錨點 | 一句話 | 對應章節 / 補章 | 對應 artifact |
|---|---|---|---|
| **① SA/SD = 製造可被傳遞的理解** | 不是儀式、不是文件,而是讓三年後的人(和 AI)能接手 | Ch 1 / 4 / 10 / 30 / 34 / Ch 46 | System Charter、Requirements Decision Log、ADR、CLAUDE.md |
| **② System Charter 是入口** | 比 PRD 更早、比 ADR 更總,是專案的「定錨」 | Ch 1 / 2 / 3 / 11 | Charter、Cadence Charter、TELOP |
| **③ Cadence 讓四個 Tempo 對上** | Business / Product / Engineering / Compliance 不是同一個鼓點 | Ch 2 / 27 / 32 / Ch 28 | Cadence Charter、SLO Catalog、FinOps Card |
| **④ Bounded Context 是抗變動的核心** | 從 DDD 到 Modular Monolith 到 Cell-based,都在處理同一件事:邊界 | Ch 18 / 18 / 19 / 20 / 21 / 24 | BC Card、ES Outcome、C4、Module Boundary Card |
| **⑤ AI 時代的 SA/SD = 脈絡工程** | LLM 沒失憶,是脈絡沒持久化;CLAUDE.md / Skill / RAG / Memory / Harness 都在補這件事 | Ch 36 / 34 / 35 / 36 / 37 / 38 / Ch 45 / D / G / H / I | CDE Setup、Agent System Card、AI Quality Card、Agent Spec Card、Harness Engineering Card |
| **⑥ Workload-Aware 是治理基礎** | 從儲存到雲端到 LLM 成本,先看 workload profile 再選工具 | Ch 13 / 15 / 23 / 32 / 37 | Storage Card、Architecture Style Card、Workload Cost & Carbon |

這六件事彼此並非平行。它們有層次:① 是哲學前提,②③ 是專案啟動的雙引擎,④ 是技術層的核心,⑤ 是 2026 年新增的補丁,⑥ 是貫穿所有層的判準。把它們疊在一起,就是全書的骨架。

換句話說,讀者讀完這本書之後,**如果只能記住六句話**,就是這六句。其餘 38 章都是這六句話在不同 zoom level 的展開:Ch 5 的 UML 是「製造可被傳遞的理解」在「給工程師看」這個 zoom 的展開;Ch 38 的 RAG 是「製造可被傳遞的理解」在「給 LLM 看」這個 zoom 的展開 ⸺ 同一件事,不同形狀。

PayLoop 2.0 之所以能在 22 個月內把劇本接起來,就是因為他們在事故覆盤時(月 0)沒有問「我們缺哪份文件」,而是問「我們在這六件事上各自在哪一格」。表格填完之後,38 章對他們來說就不是 38 章,是一張一張可以按需取用的卡。

---

## 48.3 決策框架 ⸺ PayLoop 2.0 的 22 個月,逐章對應

這一節是全書最長的一節,也是最後一次的「白板示範」。把 PayLoop 2.0 的 22 個月切成五個階段,每個階段對應 1–N 章,並列出當時實際產出的 artifact ⸺ 讓讀者能對著自己的專案說:「我在第幾個月、缺哪張 Card。」

### 48.3.1 月 0–1:重新定錨(對應 Ch 1 / 2 / 3 / 4)

事故覆盤後第一週,PayLoop 沒有去寫 PRD、沒有去重寫 code。CTO 把白板擦乾淨,寫上四個字:**Charter 重寫**。

這個階段交付了四份 artifact:

| Artifact | 章節溯源 | 內容(節錄) |
|---|---|---|
| **System Charter v3.0** | Ch 1 | 一頁。Problem:「跨境匯款 banker 在事故 6 小時內無法回答 source of truth。」Constraints:MAS / 央行 / 卡組織三條紅線。Out of Scope:不做 retail-facing 錢包。 |
| **Cadence Charter** | Ch 2 | 把四個 Tempo 對齊:Business(月)/ Product(雙週)/ Engineering(週)/ Compliance(季)。每個 Tempo 的決策點與升級條件寫死。 |
| **TELOP 利害關係人圖** | Ch 3 | 找出三個隱性否決者:**MAS 合規官、Visa/Mastercard 卡組織風控、新加坡央行外匯司**。三人從未出現在 PRD,但一句話可以讓上線推遲六個月。 |
| **Requirements Decision Log** | Ch 4 | 30 場 banker / compliance / ops 訪談,輸出 47 條需求,每條附三欄:What / Why / Decision-Owner。 |

這四份東西加起來不到 12 頁,但它們做的事是 [Ch 1.2](../part-01-foundations/ch-01-why-sa-sd.md) 反覆強調的:**把模糊業務問題,轉換成可被傳遞的決定與限制**。沒有這層,後面所有架構動作都沒有可以對齊的座標。

### 48.3.2 月 1–3:把上一版的「會跑的東西」拆解(對應 Ch 5 / 6 / 7 / 8 / 9 / 10)

這個階段的目標不是設計新系統,是先**看懂舊系統**。PayLoop 1.0 那 70% AI 寫的 code 還在跑,真實流量也還在進來,所以 SA 團隊必須在「不停機 / 不 break 任何 banker 工作流」的前提下,把舊系統的形狀逆向出來。

不畫 14 張 UML 圖,只畫三張([Ch 5](../part-01-foundations/ch-05-uml-overview.md) 反覆強調的劑量):

- **Class Diagram**:只畫核心領域物件(Transaction、Wallet、Counterparty、ComplianceCase),共 14 個 class。
- **Sequence Diagram**:只畫「跨境匯款一筆走到底」這條黃金路徑,共 11 個 step。
- **State Diagram**:只畫 Transaction 的 8 個狀態(initiated / screened / settled / disputed ...),把 PayLoop 1.0 那次 8,400 美元差額對應到「screened ↔ settled」這條邊。

DFD 與 OOA([Ch 6 / 7](../part-02-analysis/ch-06-dfd-structured-analysis.md))在這個階段做了**資料拓樸圖**(Use Case Atom),清楚標註:每個 use case 只能改 1–2 個 entity,跨 entity 的操作必須走 saga 而不是 transaction。

[Ch 8](../part-02-analysis/ch-08-data-modeling-normalization.md) 那課關於 `Patient_id`「同名異義」的教訓,在 PayLoop 2.0 對應的就是 `transaction_id`。事故覆盤揭露:PayLoop 1.0 裡至少有三張表叫 `transaction_id`,但意思不一樣 ⸺ payment 表的 `transaction_id` 是內部 UUID;ledger 表的 `transaction_id` 是合作銀行給的編號;reconciliation 表的 `transaction_id` 是兩者拼接後的 hash。當初 8,400 美元差額對不上,根因之一就是這個。新版立刻引入 Data Lineage Card:

> **transaction_id 同名異義表(Data Lineage Card 節錄)**
>
> | 出現位置 | 真實語意 | 重新命名 |
> |---|---|---|
> | `payment.transaction_id` | 內部 UUIDv7 | `payment_internal_id` |
> | `ledger.transaction_id` | 合作銀行編號 | `bank_external_ref` |
> | `reconciliation.transaction_id` | 對帳鍵 | `reconciliation_key` |

[Ch 9](../part-02-analysis/ch-09-process-modeling.md) 的「BPMN / 狀態機 / 決策表三層分工」直接套用:BPMN 描繪業務人員看到的端到端流程;狀態機描繪 Transaction 的內部生命周期;決策表描繪 AML 規則(共 38 條)。三層各自負責不同抽象層,不互相壓縮。

[Ch 10](../part-02-analysis/ch-10-spec-documents.md) 的「PRD / SRS / MVP 壓縮三層歧義」也在這個月底交付:不是寫一份 80 頁 SRS,而是三份各 6–10 頁的 Spec Triage One-Pager,每份對應不同讀者(business / engineering / compliance)。

### 48.3.3 月 4–9:架構級重構(對應 Ch 11–24,本書最長的一段)

這六個月是真正的工程主戰場。PayLoop 2.0 的架構重構分成「原則 → 模式 → 風格 → 邊界 → 合約 → 拓樸」六層,每一層都有對應的 Card。

#### 架構原則層([Ch 11 / 12 / 13](../part-03-design/ch-11-architecture-principles.md))

- **SOLID 改動半徑**:每個變更前先問「這次改動的半徑跨幾個 module」,跨越 2 個就要寫 ADR。
- **GoF 命名統一**:Strategy / Adapter / Repository 在 codebase 統一命名(`*Strategy`, `*Adapter`, `*Repository`),禁止 `*Helper`、`*Util` 這類無資訊命名。
- **Hexagonal 抗邊界變動**:核心 domain 與外部 adapter(MAS API、Visa API、Stripe Connect API)之間放 port,讓三家銀行 API 換廠商時,domain code 不動。

對應的 Coupling Audit Card 與 Pattern Adoption Card 寫進 `docs/architecture/`,每季一次審計。

#### API 設計([Ch 14](../part-03-design/ch-14-api-design.md))

PayLoop 1.0 同時有 REST、GraphQL、gRPC 三套協定散落各處,banker 工作站靠 REST,合作銀行靠 SOAP(歷史包袱),內部風控靠 gRPC。重構策略:**保留三套協定,但統一 API Contract Card**。每個 endpoint 都有一張卡,寫:Coarse-grained Intent(這個 API 在業務上做的事,用一句話)、SLA、idempotency key 規則、retry 策略。

關鍵決策是 Coarse-grained API:不再有 `POST /transactions/{id}/screen`、`POST /transactions/{id}/settle`、`POST /transactions/{id}/notify` 這三個細粒度,而是 `POST /transactions/{id}/advance`,讓內部狀態機決定下一步。這個改動把 banker 端的呼叫次數降了 60%。

#### 資料儲存([Ch 15](../part-03-design/ch-15-data-storage.md))

[Ch 15](../part-03-design/ch-15-data-storage.md) 的 Workload Profile 在這個月做了一份完整的:

| Workload 類型 | 量級 | 訪問模式 | 選擇 |
|---|---|---|---|
| Transaction OLTP | 4,200 萬美元 / 月、~80 萬筆 | 寫多讀少、強一致 | PostgreSQL 17 主庫 |
| Reconciliation | 每日 80 萬筆對帳 | 批次讀、分析 | PostgreSQL 17 read replica + Citus 分片 |
| AML Rule Vector Search | 38 條規則 + 客戶歷史 embedding | 相似度檢索 | pgvector 0.8(同一個 PG 17 實例) |
| Banker Session State | ~200 並發 | 短 TTL、低延遲 | Redis 7.4 |
| Audit Log | 寫入即不可變 | append-only、合規 7 年 | S3 + Iceberg(via Ch 28) |

關鍵決策是「**不引入 MongoDB / Cassandra**」⸺ Workload Profile 表明所有需求 PG 17 + pgvector + Citus 都能處理,引入 NoSQL 只會增加運維成本。這條 ADR 編號 `ADR-0023`,後面 §48.5 會展示完整內容。

#### UI/UX([Ch 16](../part-03-design/ch-16-uiux-system-view.md) + Ch 17)

banker 工作站的錯誤訊息在 PayLoop 1.0 是「Transaction failed.」這種等於沒講的話。重構引入 [Ch 16](../part-03-design/ch-16-uiux-system-view.md) 的 **DACR 錯誤訊息框架**(Diagnose / Action / Context / Recovery),把每個錯誤改寫成四欄。同時為將要上線的 AI banker 助手預備 [Ch 17](../part-03-design/ch-17-cux.md) 的 **CUX(Conversational UX)Card**,定義 AI 何時主動發言、何時等待、何時 handoff 給真人。

#### DDD / Event Storming / C4([Ch 18 / 18 / 19](../part-04-architecture/ch-18-ddd-strategic-tactical.md))

這是整個重構的脊椎。PayLoop 1.0 沒有明確的 Bounded Context,所有業務概念混在一個 namespace 裡。月 4–6 跑了三場 Event Storming workshop,各 4 小時,輸出:

- **6 個 Bounded Context**:Onboarding、Compliance、Transaction、Settlement、Reconciliation、Reporting。
- **每個 BC 一張 Bounded Context Card**(`docs/domain/bc-*.md`),定義:Ubiquitous Language(該 BC 內的詞彙表)、上游 / 下游 BC、Anti-Corruption Layer 的位置。
- **Event Storming Outcome Card**:38 個 domain event、12 個 command、6 個 policy,輸出成一張 PDF 釘在會議室牆上。

[Ch 20](../part-04-architecture/ch-20-c4-model-visualization.md) 的 C4 四層在月 7 用 Structurizr DSL 寫出來,放 `docs/architecture/c4/*.dsl`。CI 加入一條 Fitness Function:每次 PR 自動 parse C4 .dsl 與真實 Maven 依賴,如果發現「C4 圖上沒寫的依賴在 code 裡」就阻擋 merge ⸺ 這就是 [Ch 1.4 反模式 3](../part-01-foundations/ch-01-why-sa-sd.md) 講的 C4 圖過期問題的根治法。

#### Modular Monolith / 微服務 / EDA / Mesh / Cell([Ch 21 / 21 / 22 / 23 / 24](../part-04-architecture/ch-21-modular-monolith.md))

最關鍵的拓樸決策是:**走 Modular Monolith,不走微服務**。理由就是 [Ch 1.2.1](../part-01-foundations/ch-01-why-sa-sd.md) 的「防早期分解」⸺ 6 個 BC 中,只有 Compliance 因為合規隔離需求(MAS 要求合規資料留在新加坡境內)拆出獨立 service。其餘 5 個 BC 在同一個 Spring Boot 3.3 模組化單體內,各自獨立 maven module、獨立 schema、獨立 owner。

這條決策對應 Module Boundary Card 與 Microservice Tax Card([Ch 21 / 21](../part-04-architecture/ch-21-modular-monolith.md))。Microservice Tax Card 列出「如果現在拆成 6 個 service 要付的稅」:6 個 K8s deployment、6 條 CI pipeline、6 份 observability stack、跨 service transaction 改成 saga 的 4 週改動成本 ⸺ 加總後團隊的反應是「不值得」。

EDA / CQRS / ES([Ch 23](../part-04-architecture/ch-23-event-driven-cqrs-es.md))**三件不套餐**:只引入 EDA(Kafka 3.7 處理 BC 之間的 domain event),CQRS 與 ES 暫時不做。理由是 ES 對 audit / replay 雖好,但 PayLoop 2.0 的合規要求用 append-only audit log 已經滿足,不需要 ES 的全套機械成本。這個「只挑一件」的決策,對應 EDA Layer Card。

K8s / Mesh / Cell([Ch 24 / 24](../part-04-architecture/ch-24-cloud-native-kubernetes.md) + [Ch 26](../part-04-architecture/ch-26-edge-ot-it.md))在月 8 引入。Cell-based 的關鍵切割是「按地理 + 合規邊界」:新加坡 cell、香港 cell、菲律賓 cell 各自獨立,符合 MAS 的資料境內要求。Mesh 用 Istio 1.22 處理 cell 之間的流量(主要是 Reporting 跨 cell 聚合)。Edge 處理 banker 工作站本地端的合規預檢(避免每次按鈕都飛到 cloud)。

對應交付:Cloud-Native Choice Card、Traffic Governance Card、OT/IT Edge Design Pack(Ch 26)。

### 48.3.4 月 10–14:四層品質與工程實踐(對應 Ch 27–32 + Ch 28)

#### Security / Observability / SRE / Data([Ch 27 / 26 / 27 / 28](../part-05-quality/ch-27-security-by-design.md))

四層品質一次補齊,各自一張 Card:

| 層 | Card | 關鍵決策 |
|---|---|---|
| **Security** | Threat Model Card | STRIDE 跑全部 6 個 BC,輸出 24 個 threat,12 個進 mitigation backlog |
| **Observability** | Observability Plane Card | OpenTelemetry 1.x、三平面分離(metrics / traces / logs)、Tempo + Loki + Mimir |
| **SRE** | SLO Catalog + EB Card | 18 條 SLO,每條對應一個 Error Budget,burn rate alert 兩段(2% / 10%) |
| **Data** | Data Architecture Decision Card | Bronze / Silver / Gold 三層 lakehouse,合規資料另走 vault path |

合規這一條走 [Ch 28 Compliance by Design](../part-05-quality/ch-28-compliance.md) 的 **Compliance Design Pack**:把 MAS / FATF / EU AI Act Annex III 的條文逐條對應到系統元件,輸出 Compliance Trace Matrix。月 12 MAS 來做小範圍 pre-audit,這份 matrix 直接拿去用,過。

#### Platform / ADR / Fitness / FinOps([Ch 32 / 30 / 31 / 32](../part-06-engineering/ch-32-platform-engineering-idp.md))

- **Platform Product Card**:把 internal platform 視為產品。Backstage(Spotify)做開發者入口,提供 4 個 Golden Path(new-service / new-data-pipeline / new-fitness-function / new-adr)。
- **ADR Template + Index Card**:84 份 ADR,索引在 `docs/architecture/adr/INDEX.md`,自動依關鍵字搜尋。每份 ADR < 500 字。
- **Fitness Function Card**:23 條 Fitness Function 跑 nightly CI,涵蓋從架構合規(C4 圖一致)到性能(P95 latency)到合規(audit log 完整性)。
- **Workload Cost & Carbon Card**:每月跑一次 cost-per-transaction 分析,目前 USD 0.012 / 筆;碳排放走 GreenSoftware patterns 跟著一起報告。

### 48.3.5 月 15–22:AI 起手(對應 Ch 36–38 + Ch 45 / C / D)

到這個階段,前面 14 個月的 SA/SD 基礎做穩了,PayLoop 才開始把 AI 放進系統。**順序很重要** ⸺ 把 AI 放在沒做好 SA/SD 的系統上,等於把第二個 PayLoop 1.0 蓋在第一個之上。

#### AI-Native L1–L7([Ch 36](../part-07-ai-era/ch-37-ai-native-architecture.md))

引入 AI-Native 七層架構:L1 Foundation Model(Claude Opus 4.7)、L2 Inference Gateway、L3 Memory、L4 Tool、L5 Orchestration、L6 Observability、L7 Governance。對應 AI-Native System Vision Card。

#### CDE 脈絡工程([Ch 37](../part-07-ai-era/ch-38-context-driven-engineering.md))

CLAUDE.md root 寫在 monorepo 根目錄,SKILL.md 散落在每個 BC 之下。Skill 的設計原則是「每個 Skill 對應一條業務能力,且必須註冊到至少一份 ADR」⸺ 這是 [Ch 33 / 34](../part-06-engineering/ch-33-adr-architecture-knowledge.md) 強調的「Skill 與 ADR 連動」,避免 Skill 漂移。

對應交付:CDE Setup Card + SKILL.md(每個 BC 一份)。

#### RAG / Memory / Tool([Ch 38](../part-07-ai-era/ch-39-rag-memory-tool.md))

合規 AI 助手 ComplianceCopilot 在月 17 上線。RAG 接 38 條 AML 規則 + 過去 90 天 transaction 摘要;Memory 分三層(short-term session、long-term per-banker preference、shared institutional knowledge);Tool 遵循 Least Privilege 與 dry-run + HITL,寫操作預設不自動執行。

對應交付:Agent System Card。

#### Multi-Agent / Coding Agent / Eval([Ch 39 / 37 / 38](../part-07-ai-era/ch-40-multi-agent.md) + [Ch 45](../part-07-ai-era/ch-46-agentic-qa.md))

風控做成 Multi-Agent(LangGraph 0.2):Screener Agent 負責規則匹配、Investigator Agent 負責拉相關歷史交易、Reporter Agent 負責出 STR 草稿。三個 Agent 透過 [Ch 40 Multi-Agent Consensus](../part-07-ai-era/ch-41-multi-agent-consensus.md) 的 consensus pattern 達成共識,任一 Agent 不同意時走 HITL。對應 Multi-Agent System Card。

Coding Agent([Ch 43](../part-07-ai-era/ch-44-coding-agent.md))在 22 人團隊中作為 pair programmer,但寫死兩條規則:(1)所有 commit 必須由人類 approve;(2)涉及 ADR 變動的 PR 必須先寫 / 改 ADR 再改 code。對應 Agent-Friendly Codebase Card。

[Ch 44](../part-07-ai-era/ch-45-ai-eval-drift-redteam.md) 的 Eval / Drift / Red Team **三軸並行**全做。Eval set 480 題、Drift PSI 接 PagerDuty、Red Team CI 攻擊集 240 題。對應 AI Quality Card,並走 [Ch 45 Agentic QA](../part-07-ai-era/ch-46-agentic-qa.md) 的雙 Agent 對抗評估補強 Judge 校準。

### 48.3.6 全書 artifact ↔ 章節對應索引(可帶走)

下表是這 22 個月實際產出的全書級 artifact 索引,讀者可以對照自己的專案逐項檢核。**這張表本身就是一份 capstone 交付物**:

| # | Artifact | 章節 | PayLoop 2.0 路徑 |
|---|---|---|---|
| 1 | System Charter | Ch 1 | `docs/charter.md` |
| 2 | Cadence Charter | Ch 2 | `docs/cadence.md` |
| 3 | Project Initiation Brief | Ch 2 | `docs/cadence.md#brief` |
| 4 | TELOP 利害關係人圖 | Ch 3 | `docs/stakeholders/telop.md` |
| 5 | Requirements Decision Log | Ch 4 | `docs/requirements/log.md` |
| 6 | Diagram Decision Card | Ch 5 | `docs/diagrams/decision.md` |
| 7 | Use Case Atom | Ch 6 / 7 | `docs/usecase/atoms.md` |
| 8 | Data Lineage Card | Ch 8 | `docs/data/lineage.md` |
| 9 | Schema Decision Card | Ch 8 | `docs/data/schema.md` |
| 10 | Process Model Triage Card | Ch 9 | `docs/process/triage.md` |
| 11 | Spec Triage One-Pager | Ch 10 | `docs/spec/triage-{audience}.md` |
| 12 | Coupling Audit Card | Ch 11 | `docs/architecture/coupling.md` |
| 13 | Pattern Adoption Card | Ch 12 | `docs/architecture/patterns.md` |
| 14 | Architecture Style Selection Card | Ch 13 | `docs/architecture/style.md` |
| 15 | API Contract Card | Ch 14 | `docs/api/contracts/*.md` |
| 16 | Storage Selection Card | Ch 15 | `docs/data/storage-decisions.md` |
| 17 | Interaction State Card | Ch 16 | `docs/ui/state.md` |
| 18 | Bounded Context Card | Ch 18 | `docs/domain/bc-*.md` |
| 19 | Event Storming Outcome Card | Ch 19 | `docs/domain/event-storming.md` |
| 20 | C4 Diagram Card | Ch 20 | `docs/architecture/c4/*.dsl` |
| 21 | Module Boundary Card | Ch 21 | `docs/architecture/modules.md` |
| 22 | Microservice Tax Card | Ch 22 | `docs/architecture/microservice-tax.md` |
| 23 | EDA Layer Card | Ch 23 | `docs/architecture/eda.md` |
| 24 | Cloud-Native Choice Card | Ch 24 | `docs/cloud/choice.md` |
| 25 | Traffic Governance Card | Ch 25 | `docs/cloud/traffic.md` |
| 26 | Threat Model Card | Ch 27 | `docs/security/threat-model.md` |
| 27 | Observability Plane Card | Ch 29 | `docs/ops/observability.md` |
| 28 | SLO Catalog + EB Card | Ch 30 | `docs/ops/slo.md` |
| 29 | Data Architecture Decision Card | Ch 31 | `docs/data/architecture.md` |
| 30 | Platform Product Card | Ch 32 | `docs/platform/product.md` |
| 31 | ADR Template + Index Card | Ch 33 | `docs/architecture/adr/INDEX.md` |
| 32 | Fitness Function Card | Ch 34 | `docs/architecture/fitness/*.yaml` |
| 33 | Workload Cost & Carbon Card | Ch 35 | `docs/finops/cost-carbon.md` |
| 34 | AI-Native System Vision Card | Ch 36 | `docs/agents/vision.md` |
| 35 | CDE Setup Card + SKILL.md | Ch 37 | `CLAUDE.md` + `**/SKILL.md` |
| 36 | Agent System Card | Ch 38 | `docs/agents/system-card.md` |
| 37 | Multi-Agent System Card | Ch 39 | `docs/agents/multi-agent-card.md` |
| 38 | Agent-Friendly Codebase Card | Ch 43 | `docs/agents/codebase-card.md` |
| 39 | AI Quality Card | Ch 44 | `docs/agents/quality-card.md` |
| 40 | OT/IT Edge Design Pack | Ch 26 | `docs/edge/design-pack.md` |
| 41 | Agentic QA Pack | Ch 45 | `docs/agents/qa-pack.md` |
| 42 | Brownfield Modernization Pack | Ch 46 | `docs/legacy/modernization.md` |
| 43 | Multi-Agent Consensus Pack | Ch 40 | `docs/agents/consensus-pack.md` |
| 44 | Compliance Design Pack | Ch 28 | `docs/compliance/design-pack.md` |
| 45 | CUX Design Pack | Ch 17 | `docs/ui/cux-pack.md` |
| 46 | Engineering Intuition Card | Ch 53 | `docs/human/intuition-card.md` |
| 47 | Agent Spec Card | Ch 41 | `docs/agents/agent-spec.md` |
| 48 | Harness Engineering Card | Ch 42 | `docs/agents/harness-config.md` |

48 份 artifact,每份一頁,加總約 65–85 頁 ⸺ **這就是 PayLoop 2.0 在 MAS 抽查當天投影到牆上的那棵 `docs/` 樹**。

把 48 份 artifact 跟對應章節畫成一張結構圖,可以更清楚看到「同一張地圖的不同 zoom level」這句話的形狀:

```mermaid
flowchart LR
    subgraph Anchor [錨定層 · 月 0]
      Charter["Charter / Cadence / TELOP / Req Log<br/>Ch 1-4"]:::goal
    end
    subgraph Analysis [分析層 · 月 1-3]
      A["UML 三張 / DFD / Data Lineage<br/>Process Triage / Spec Triage<br/>Ch 5-10"]:::cold
    end
    subgraph Design [設計層 · 月 4-6]
      D["Principles / Patterns / Style<br/>API Contract / Storage / UI+CUX<br/>Ch 11-16 + 補 F"]:::cold
    end
    subgraph Architecture [架構層 · 月 7-9]
      AR["BC / ES / C4 / Module / Micro Tax<br/>EDA / Cloud / Mesh / Cell + Edge<br/>Ch 18-24 + 補 A"]:::cold
    end
    subgraph Quality [品質層 · 月 10-12]
      Q["Threat / Obs / SLO / Data Arch<br/>Compliance Pack<br/>Ch 27-28 + 補 E"]:::cold
    end
    subgraph Engineering [工程層 · 月 13-14]
      E["Platform / ADR / Fitness / FinOps<br/>Ch 32-32"]:::cold
    end
    subgraph AI [AI 層 · 月 15-22]
      AIL["L1-L7 / CDE / RAG / Multi-Agent<br/>Coding Agent / Eval-Drift-RT<br/>+ Agentic QA / Brownfield / Consensus<br/>Ch 36-38 + 補 B/C/D"]:::hot
    end

    Anchor --> Analysis --> Design --> Architecture --> Quality --> Engineering --> AI
    Anchor -. 約束 .-> Architecture
    Anchor -. 約束 .-> AI
    Architecture -. BC 邊界 .-> AI

    classDef hot fill:#fee,stroke:#c33
    classDef cold fill:#eef,stroke:#36c
    classDef goal fill:#efe,stroke:#3a3
```

這張圖的關鍵不是六個盒子的順序,是**那三條虛線**:Charter 一直在約束底層架構與 AI 層、BC 邊界一直延伸到 AI Agent 的職責劃分。少了這三條虛線,48 份 artifact 就會退化成 48 份各自獨立的文件 ⸺ 這就是 §48.4 反模式 1 要避免的事。

### 48.3.7 全書整合的 ADR 範例

這 22 個月最有教育意義的一份 ADR 是 `ADR-0023`,它一份文件把多章決策連動。這份 ADR 也是讀者可以直接套用的「全書整合範例」:

```markdown
# ADR-0023: 不引入 MongoDB,用 PostgreSQL 17 + pgvector + Citus 處理全部 workload

Status: Accepted (2026-09-12) | Owners: SA + DBA + Platform Lead
Linked: System Charter v3.2 §2 (Constraints),
        Storage Selection Card (Ch 15),
        Architecture Style Selection Card (Ch 13),
        Module Boundary Card (Ch 21),
        Workload Cost & Carbon Card (Ch 35),
        Compliance Design Pack §4.2 (Ch 28)

## Context
Workload Profile (Ch 15) 顯示我們需要支援:OLTP、批次對帳、向量檢索、
session state、append-only audit。團隊內有人提議引入 MongoDB(文件型)
與 Cassandra(寬列)以「現代化資料層」。

## Decision
不引入 MongoDB / Cassandra。全部 workload 走:
- PostgreSQL 17 主庫 + read replica(OLTP / 對帳)
- pgvector 0.8 共用同一個 PG 17 實例(向量檢索)
- Citus 12 水平分片(對帳批次)
- Redis 7.4(session state,獨立)
- S3 + Iceberg(audit log,獨立)

## Consequences
+ 運維面:1 個 RDBMS 比 3 個 RDBMS 少 60% 運維成本(對應 Ch 35 FinOps)
+ 合規面:單一 source of truth 對 MAS audit trail 友善(對應Ch 28)
+ 邊界面:Module Boundary Card 限定每個 BC 一個 schema,單庫多 schema
  即可滿足(對應 Ch 21)
- 規模面:若未來月流水 > USD 5 億且 OLTP 寫入 > 5,000 TPS,需重評估
  (觸發條件寫入 Fitness Function FF-0014,對應 Ch 34)

## Reversal Cost
若 12 個月內反悔,改 schema + 資料遷移工時 ~6 週(可逆)。
若 36 個月後反悔,因 Citus 分片與 partition 已成熟,不可逆。

## Trigger to Re-evaluate
1. 月寫入 TPS > 5,000(FF-0014 自動觸發)
2. pgvector 在 1 億+ embedding 規模 P95 latency > 500ms
3. PG 17 LTS 終止支援(預計 2032)
```

這份 ADR 一頁,連動了 6 章 + 1 補章。**這就是「同一張地圖的不同 zoom level」的具體含義**:單一決策不是孤立的,它必須說得出來自己跟哪些章節的觀念連動,以及在什麼條件下應該被推翻。

---

## 48.4 踩坑清單 ⸺ 全書級反模式

PayLoop 2.0 的 22 個月不只是成功故事。覆盤時也記下了四個曾經差點重蹈覆轍的全書級反模式,每一個都串多章。

### 反模式 1:把書當清單,而不是當地圖

最常見的讀者反應是「我把每章的 Card 都寫一遍就行了」,然後在月底交出 48 份各 1 頁、彼此互不相干的 Card。Charter 寫了一份、ADR 寫了 84 份,但 ADR 沒回頭引 Charter,Charter 沒有約束 ADR。結果是有 artifact、沒有理解。

> ✅ **修正方向**:每份 Card 強制標註「上游(我從哪來)」與「下游(我影響誰)」兩欄,跟 git commit 一樣建立 DAG。本章 §48.3.7 那份 ADR-0023 就是示範:它在 Linked 區塊明確列出 6 章 + 1 補章的連動。把全書當「彼此引用的圖」而不是「依序讀完的書」⸺ 這也是 [Ch 1.2](../part-01-foundations/ch-01-why-sa-sd.md) 一開始強調的「製造可被傳遞的理解」最具體的形狀。

### 反模式 2:只做 Greenfield,不做 Brownfield(承接Ch 46)

PayLoop 1.0 → 2.0 是 brownfield,不是 greenfield。團隊一開始有過一陣子的衝動,想「砍掉重寫」,因為 1.0 的 70% AI 寫的 code 看起來像個爛攤子。如果走 greenfield,根據 [Ch 46](../part-07-ai-era/ch-47-legacy-ai.md) 的經驗,大概率會在月 6 出現「新版做不完、舊版沒人改 bug」的雙線崩潰。

> ✅ **修正方向**:走 [Ch 46](../part-07-ai-era/ch-47-legacy-ai.md) 的 Brownfield Modernization Pack。先做 **Strangler Fig** ⸺ 新功能寫在新模組,舊功能逐步從舊系統剝離,中間 6–9 個月雙線並存。AI 幫忙的地方不是「寫新程式」,是「讀舊 code 寫 ADR、補測試、生 type stubs」。PayLoop 2.0 month 4–9 的架構重構,就是 Strangler Fig 在跑。

### 反模式 3:只做 Eval,不做 Drift / Red Team(承接Ch 45)

[Ch 44](../part-07-ai-era/ch-45-ai-eval-drift-redteam.md) 的 AMLNavigator 教訓在 PayLoop 2.0 內部被當作經典案例反覆複述。但實際做的時候,還是有人想偷懶,理由是「我們先做 Eval,Drift / Red Team 等 Q4 再做」。這個拖延一旦發生,通常第三季就會吃到事故,因為輸入分布飄移與 prompt injection 攻擊不會等你做好準備才來。

> ✅ **修正方向**:Eval / Drift / Red Team **三軸並行,同月上線**。任何一軸晚兩個月做,等於三軸都白做。具體做法去 [Ch 45 Agentic QA](../part-07-ai-era/ch-46-agentic-qa.md):用雙 Agent 對抗評估自動產生 Drift 警報、用自動 Red Team Agent 持續產生新攻擊向量。PayLoop 2.0 ComplianceCopilot 上線當月,三軸都接好 PagerDuty。

### 反模式 4:Skill 沒接 ADR(承接 Ch 33 / 34)

[Ch 37](../part-07-ai-era/ch-38-context-driven-engineering.md) 的 SKILL.md 設計初期容易出現一種偏差:工程師寫 Skill 是為了「讓 Claude 寫 code 更順」,而不是「讓決策被持久化」。結果是 Skill 變成個人偏好的集合,半年後跟 ADR 互相打架,Claude 拿到衝突的脈絡時會幻覺,人類開 PR 時會踩雷。

> ✅ **修正方向**:每份 SKILL.md 必須在 frontmatter 列出 `linked_adrs: [ADR-0023, ADR-0041]`,且每次 Skill 改動都要在 commit message 引用 ADR 編號。CI 加一條 Fitness Function:Skill 引用的 ADR 不存在或已 deprecated 時阻擋 merge。這就是 [Ch 33](../part-06-engineering/ch-33-adr-architecture-knowledge.md) 與 [Ch 37](../part-07-ai-era/ch-38-context-driven-engineering.md) 的連動 ⸺ Skill 是 ADR 在 AI 協作層的可執行延伸,不是另起爐灶。

---

## 48.5 交付清單 ⸺ 全書 SA/SD 整合 Pack

讀完這 39 章 + 9 補章,你可以帶走的不是 39 份心得,而是**一整個整合 Pack**。它的形狀就是 PayLoop 2.0 那棵 `docs/` 樹,規模 48 份 artifact,加總 65–85 頁。

### 48.5.1 全書地圖 Mermaid

```mermaid
flowchart LR
    subgraph P1 [Part I 起手 · Ch 1-3]
      C1[Charter]:::goal
      C2[Cadence]:::goal
      C3[TELOP]:::goal
    end
    subgraph P2 [Part II 分析 · Ch 4-10]
      A1["Req Log / UML / DFD"]:::cold
      A2["Data Lineage / Process / Spec"]:::cold
    end
    subgraph P3 [Part III 設計 · Ch 11-16 + 補 F]
      D1["Principles / Patterns / Style"]:::cold
      D2["API / Storage / UI/UX + CUX"]:::cold
    end
    subgraph P4 [Part IV 架構 · Ch 18-24 + 補 A]
      AR1["DDD / ES / C4"]:::cold
      AR2["Modular Mono / Micro / EDA / Cloud / Edge"]:::cold
    end
    subgraph P5 [Part V 品質 · Ch 27-28 + 補 E]
      Q1["Security / Obs / SRE / Data"]:::cold
      Q2[Compliance Pack]:::cold
    end
    subgraph P6 [Part VI 工程 · Ch 32-32]
      E1["Platform / ADR / Fitness / FinOps"]:::cold
    end
    subgraph P7 [Part VII AI · Ch 36-38 + 補 B/C/D]
      AI1["L1-L7 / CDE / RAG"]:::hot
      AI2["Multi-Agent / Coding / Eval"]:::hot
      AI3["Agentic QA / Brownfield / Consensus"]:::hot
    end
    subgraph P8 [Part VIII Capstone · Ch 47]
      CS[同一張地圖]:::goal
    end

    P1 --> P2 --> P3 --> P4 --> P5 --> P6 --> P7 --> P8
    P1 -. Charter 約束所有層 .-> P8
    P4 -. BC 是技術層核心 .-> P8
    P7 -. CDE 是 2026 補丁 .-> P8

    classDef hot fill:#fee,stroke:#c33
    classDef cold fill:#eef,stroke:#36c
    classDef goal fill:#efe,stroke:#3a3
```

這張圖的關鍵不是「八個 Part」,是**那三條虛線**:Charter 一直在約束最底層的 capstone、BC 是中段的脊椎、CDE 是 2026 才補的最後一塊。讀者把這三條虛線記住,本書 38 章 + 9 補章就有了座標。

### 48.5.2 AI 時代與 SA/SD 整合表(可貼上會議室白板)

| SA/SD 經典工具 | 1990 年代角色 | 2026 年新角色 | 整合 artifact |
|---|---|---|---|
| **SRS** | 上線前驗收文件 | spec.md(給人 + 給 AI) | Spec Triage One-Pager(Ch 10) |
| **UML / ERD** | 全套 14 圖 | 三張(Class / Sequence / State) | Diagram Decision Card(Ch 5) |
| **PRD** | 80 頁規格 | 一頁 Charter + 訪談 log | Charter + Req Log(Ch 1 / 4) |
| **DDD BC** | 學術概念 | Modular Monolith 切割線 | BC Card + Module Card(Ch 18 / 20) |
| **Code Review** | 人對人 | 人 + AI + Fitness Function | ADR + FF Card(Ch 33 / 31) |
| **Test** | unit / integration / e2e | + Eval / Drift / Red Team | AI Quality Card(Ch 44) |
| **Documentation** | Word / Confluence | git-tracked Markdown + CLAUDE.md | CDE Setup Card(Ch 37) |

### 48.5.3 全書交付物速查表

| 啟動階段 | 必交付(無論 S/M/L) | M 模式加做 | L 模式加做 |
|---|---|---|---|
| 月 0 | Charter + Cadence + TELOP | + Req Log | + Compliance Pack |
| 月 1–3 | UML 三張 + Data Lineage | + Process Triage + Spec Triage | + Threat Model 初版 |
| 月 4–9 | API Contract + Storage Card | + BC Card + C4 + Module Card | + Microservice Tax + EDA + Cloud Choice |
| 月 10–14 | SLO + Observability | + ADR Index + Fitness | + FinOps + 全套品質四 Card |
| 月 15+ | CLAUDE.md + System Card | + Multi-Agent Card + AI Quality | + Agentic QA Pack + Consensus Pack |

S 模式適合「丟掉重寫不會痛」的內部工具;L 模式留給「弄錯會被監理罰款 / 上新聞」的場景;**預設值是 M**。這跟 [Ch 1.3.1](../part-01-foundations/ch-01-why-sa-sd.md) 的三維 Triage 表一致 ⸺ 全書從 Ch 1 到 Ch 47,預設值始終沒變。

---

## 48.6 Recap ⸺ 全書六大核心觀念與一封給讀者的短信

讀完這 39 章 + 9 補章,如果只能帶走六句話,就是這六句:

1. **SA/SD = 製造可被傳遞的理解**。不是儀式、不是文件,是讓三年後的人(和 AI)能接手。([Ch 1](../part-01-foundations/ch-01-why-sa-sd.md))
2. **System Charter 是入口**。一頁、寫不滿就是寫得不對、會逼出取捨。([Ch 1](../part-01-foundations/ch-01-why-sa-sd.md))
3. **Cadence 讓四個 Tempo 對上**。Business / Product / Engineering / Compliance 不是同一個鼓點,寫死它們各自的決策點。([Ch 2](../part-01-foundations/ch-02-sdlc-evolution.md))
4. **Bounded Context 是抗變動的核心**。從 DDD 到 Modular Monolith 到 Cell-based,本質上都在處理同一件事:邊界。([Ch 18 / 20 / 24](../part-04-architecture/ch-18-ddd-strategic-tactical.md))
5. **AI 時代的 SA/SD = 脈絡工程**。LLM 沒失憶,是脈絡沒持久化。CLAUDE.md / Skill / RAG / Memory / Multi-Agent / Eval-Drift-RedTeam / Harness 都在處理這件事。([Ch 36–38](../part-07-ai-era/ch-37-ai-native-architecture.md) + [Ch 41](../part-07-ai-era/ch-42-agent-spec.md) / [Ch 42](../part-07-ai-era/ch-43-harness-engineering.md))
6. **Workload-Aware 是治理基礎**。從儲存到雲端到 LLM 成本,先看 workload profile 再選工具,不要反過來。([Ch 13 / 15 / 32](../part-03-design/ch-13-architecture-styles.md))

把這六句話釘在會議室白板上,任何一個 SA/SD 的爭論最後都會回到其中一句。

---

### 一封給讀者的短信

寫到這裡,這本書 39 章 + 9 補章的旅程要收束了。

我看著 PayLoop 從 18 天上線、180 天崩潰,走到 22 個月後在 MAS 稽核員面前打開 `docs/` 那棵樹。中間沒有奇蹟,沒有銀彈,只有一張一張被認真寫出來的 Card。每一張 Card 一頁,寫不滿就是寫得不對 ⸺ 這句話從 Ch 1 講到 Ch 47,沒變過。

如果你是剛接手新專案的工程師,請從 Charter 開始,一頁。如果你是接到 brownfield 任務的架構師,請從Ch 46 開始,Strangler Fig。如果你是把 AI 放進系統的 PM / RD,請從 Ch 44 + Ch 36 開始,三軸並行。如果你是要寫 Agent 設定規格的 SA/RD,請從Ch 41 的 SKILL.md 語言開始。如果你是要讓 Agent 穩定跑在生產環境的平台工程師,請從Ch 42 的 Harness Engineering 五元件開始。如果你擔心自己的工程直覺在 AI 輔助下逐漸退化,請從Ch 53 的「不可外包的五種判斷」開始。其餘 38 章是地圖,等你需要某個 zoom level 的時候再回來查。

Karpathy 在 2024 講 Software 3.0 [^CIT-390] 時,把「prompt 是新的程式語言、context 是新的記憶體、Agent 是新的執行單元」這個三段式講得很乾淨;Anthropic 2024–2026 的 Building Effective Agents [^CIT-391] 系列把 workflow 與 agent 的差別講得很實。這兩條線的共同結論是:**AI 系統的能力上限,取決於我們能餵給它多乾淨的脈絡**。而 SA/SD 做的事,從 1990 年代的 Eric Evans DDD [^CIT-392] 到 2026 年的 CLAUDE.md,本質上都是製造這個脈絡。

工具會換,Cursor 換 Claude Code 換下一個還沒命名的東西;模型會換,Sonnet 換 Opus 換 Haiku 4 換 Opus 5;雲會換,K8s 換 cell-based 換下一個還沒命名的拓樸。但「**製造可被傳遞的理解**」這件事不會換。它從 1968 年 NATO Software Engineering 會議開始,到你手上現在這個 commit,一直是同一件事。

這本書留給你的最後一個 artifact,不是一頁 Card,是一個位置:**請你也成為下一位老師傅**。把你接下來踩的坑寫成 ADR、把你做出的取捨寫成 Charter、把你訓出的 Skill 接到 ADR、把你教 AI 寫 code 的方式寫成 SKILL.md。下一個讀這本書的工程師,以及下一個接手你 repo 的 Claude / Cursor 後繼者,都會謝謝你。

我們有什麼?除了一個會跑的東西之外,我們現在擁有它的形狀。

把那個形狀傳下去。

---

## Cross-References

- **本書起點**:[Ch 1 為什麼系統分析與系統設計](../part-01-foundations/ch-01-why-sa-sd.md) ⸺ 同一個 PayLoop,18 天上線、180 天崩潰
- **節奏對齊**:[Ch 2 SDLC 與方法學演進](../part-01-foundations/ch-02-sdlc-evolution.md)
- **資料同名異義**:[Ch 8 資料模型](../part-02-analysis/ch-08-data-modeling-normalization.md)
- **Bounded Context 三章組**:[Ch 18 DDD](../part-04-architecture/ch-18-ddd-strategic-tactical.md) / [Ch 19 Event Storming](../part-04-architecture/ch-19-event-storming-modeling.md) / [Ch 20 C4](../part-04-architecture/ch-20-c4-model-visualization.md)
- **Modular Monolith 路線**:[Ch 21](../part-04-architecture/ch-21-modular-monolith.md) / [Ch 22 微服務稅](../part-04-architecture/ch-22-microservices.md)
- **AI 系統工程紀律**:[Ch 36–38](../part-07-ai-era/ch-37-ai-native-architecture.md) + [Ch 45](../part-07-ai-era/ch-46-agentic-qa.md) / [Ch 40](../part-07-ai-era/ch-41-multi-agent-consensus.md)
- **Brownfield 路徑**:[Ch 46 遺留系統 AI 現代化](../part-07-ai-era/ch-47-legacy-ai.md)
- **合規對齊**:[Ch 28 Compliance by Design](../part-05-quality/ch-28-compliance.md)
- **CUX 預備**:[Ch 17 對話式體驗](../part-03-design/ch-17-cux.md)
- **工程直覺保護**:[Ch 53 工程直覺保護手冊](../part-09-human-engineer/ch-54-engineering-intuition.md)
- **Agent 設定語言**:[Ch 41 Agent 設定語言](../part-07-ai-era/ch-42-agent-spec.md)
- **Agent Harness 工程**:[Ch 42 Agent Harness 工程](../part-07-ai-era/ch-43-harness-engineering.md)

## 引用

[^CIT-390]: Andrej Karpathy, "Software 3.0 / Software Is Changing (Again)", AI Engineer Summit / Sequoia 2024–2025。「prompt is the new programming language; context is the new memory; agents are the new execution unit」三段式的源頭。
[^CIT-391]: Anthropic, "Building Effective Agents" (2024) + "Effective Context Engineering for Agents" (2025–2026)。anthropic.com/research。Workflow 與 Agent 的區分、context engineering 的工程紀律。
[^CIT-392]: Eric Evans, *Domain-Driven Design: Tackling Complexity in the Heart of Software* (Addison-Wesley, 2003)。Bounded Context、Ubiquitous Language、Anti-Corruption Layer 的奠基。本書 Ch 18 / 20 / 39 三章共同的概念源頭。
[^CIT-393]: Sam Newman, *Monolith to Microservices* (O'Reilly, 2019) + GOTO 2020 / 2024 重訪。Strangler Fig 在 brownfield 的應用,對應 Ch 22 / Ch 46 / 本章 §48.4。
[^CIT-394]: ThoughtWorks Technology Radar Vol. 30 (2024)。Modular Monolith → Adopt;Microservices Envy → Hold。對應 Ch 1 / 20 / 21 / 本章 §48.3.3。
[^CIT-395]: Michael Nygard, "Documenting Architecture Decisions" (2011)。ADR 概念奠基。本章 §48.3.7 的 ADR-0023 範例直接套用 Nygard template。
[^CIT-396]: Neal Ford, Rebecca Parsons, Patrick Kua, *Building Evolutionary Architectures* (O'Reilly, 2nd ed. 2023)。Fitness Function 的奠基。對應 Ch 34 / 本章 §48.3.4。
[^CIT-397]: CNCF 2026 Q1 Microservices Regression Report。對應 Ch 1 / 本章 §48.3.3 微服務反思的數據來源。
[^CIT-398]: Shopify Engineering Blog, "How we scale our modular monolith to 30TB/min" (2025)。對應 Ch 1 / 20 / 本章 §48.3.3。
[^CIT-399]: EU AI Act, Annex III "High-Risk AI Systems" (2024 通過,2026 起分階段生效)。對應 Ch 44 / Ch 28 / 本章 §48.3.4 的高風險分類。

---
