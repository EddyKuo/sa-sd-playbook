---
chapter: F
part: annex
title: 附錄 F — Glossary 全書術語表
slug: glossary
status: published
---

# 附錄 F|Glossary 全書術語表(280+ 條)

> 本附錄為全書術語的權威定義。章節內可用 `[term](../annex-f-glossary.md#term-anchor)` 連結。
> 排序:英文字母,同字母內按英文名。中英並陳。

---

## A

### ADR (Architecture Decision Record) {#adr}
架構決策紀錄。一份輕量文件(通常 < 1 頁),記錄一個架構決策的脈絡、選項、結論、後果。Michael Nygard 2011 年提出。詳見 Ch 30。

### ADR Index Card {#adr-index-card}
Ch 30 提出的 repo 級別 artifact:Active / Superseded / Deprecated / Proposed 四區塊清單。

### ADR Write Criteria {#adr-write-criteria}
Ch 30 提出的三條判準:改回來成本高(> 1 週工程時間)+ 影響至少一個外部介面 + 不可逆。三者擇二即寫。

### ADT (Admission, Discharge, Transfer) {#adt}
HL7 v2.x 中的住院事件訊息族,描述病人在住院期間的入院、轉床、出院、轉院等狀態變化。詳見 Ch 8。

### Agent Communication Protocol {#agent-communication-protocol}
Multi-Agent 之間訊息傳遞方式,常見三種:Direct Call / Message Queue / Shared State。詳見 Ch 36。

### Agent-Friendly Codebase {#agent-friendly-codebase}
為 AI Coding Agent 提供足夠脈絡密度的工程屬性集合。六維量測:CLAUDE.md / agents.md 完整度、Skill ↔ ADR 連動、模組邊界、Test 覆蓋、命名一致性、Context Size 可控。詳見 Ch 37。

### Agent-Friendly Codebase Card {#agent-friendly-codebase-card}
Ch 37 提出的一頁式 artifact:CLAUDE.md / Skill↔ADR / 模組邊界 / Test / 命名 / Context Size / Owner 六維 + Owner。

### Agent Memory (三層) {#agent-memory}
Agent 系統的記憶子系統。三層:Short-term(context window)/ Long-term(vector DB / KG)/ Episodic(對話歷史)。詳見 Ch 35。

### Agent Pattern Language {#agent-pattern-language}
Anthropic 2024《Building Effective Agents》提出的 Agent 系統設計模式語言:Augmented LLM / Prompt Chaining / Routing / Parallelization / Orchestrator-Workers / Evaluator-Optimizer。詳見 Ch 12、Ch 36。

### Agent System Card {#agent-system-card}
Ch 35 提出的一頁式 artifact:RAG Stack / Memory 三層 / Tool 清單 + 顆粒度 / Eval Set / Owner。

### Agentic QA {#agentic-qa}
針對非確定性 AI 系統(LLM、Agent)的品質保證實踐。包含 Eval Set、LLM-as-Judge、紅隊、Drift 監測。詳見補章 B。

### Agentic QA Pack {#agentic-qa-pack}
補章 B 提出的一頁式 artifact:Eval Set v1 / Judge Rubric / Red Team Playbook 三層 / Drift Dashboard 三類指標 / CI/CD 整合 / 失敗 Runbook。

### Aggregate (聚合) {#aggregate}
DDD 戰術設計的一致性邊界,事件發生在其上。Event Storming 黃色便利貼。詳見 Ch 17、Ch 18。

### Aggregate (Transactional Consistency Boundary) {#aggregate-consistency-boundary}
DDD 戰術設計核心。一個 Aggregate 內所有 entity 必須在同一個交易內保持一致。跨 Aggregate 用 ID reference,不直接持有對象。詳見 Ch 17。

### Aggregator (EIP) {#aggregator}
EIP Routing 模式。多個訊息彙整成一個輸出(N → 1)。詳見 Ch 12。

### AI-Augmented {#ai-augmented}
系統設計上預設「人 + AI」雙線決策,任一條斷掉旅程仍可降級閉環的定位。詳見 Ch 33。

### AI-Embedded {#ai-embedded}
在既有系統某個節點塞進 LLM 呼叫的系統定位。Litmus Test:把 LLM 拿掉,系統旅程仍可成立。詳見 Ch 33。

### AI-Native {#ai-native}
系統的核心旅程由 Agent 推理 / 規劃 / 工具調用所構成的定位。Litmus Test:把 LLM 拿掉,系統旅程整段崩潰。詳見 Ch 33。

### AI-Native 七層架構 {#ai-native-seven-layers}
Foundation Model / Inference / Memory / Tool / Agent Orchestration / Experience / Governance 七層。L1、L5 為非確定性層,L7 為確定性治理層。詳見 Ch 33。

### AI-Native System Vision Card {#ai-native-vision-card}
Ch 33 提出的一頁式 artifact:定位選擇 / Litmus Test / 業務風險分級 / 七層元件 / 確定性邊界 / HITL 觸發點 / Circuit Breaker / Audit Trail / Owner。

### AI Quality Card {#ai-quality-card}
Ch 38 提出的一頁式 artifact:Eval Set 結構 / Drift 監測指標 / Red Team Cadence / LLM-Judge 校準 / 警報門檻 / Owner。

### AI 逆向工程四層 {#ai-reverse-engineering-four-levels}
補章 C 提出:L1 Lexical(SonarQube / CodeQL)/ L2 Structural(CodeQL + Agent 摘要)/ L3 Behavioral(Claude Code 真正發光)/ L4 Domain(人類主導 Agent 輔助)。

### Ant Design 5 {#antd-5}
Ant Group 維護的 React 設計系統第五代,2022 起。CSS-in-JS、Token 化、多主題支援。詳見 Ch 16。

### Anticorruption Layer / ACL (防腐層) {#anticorruption-layer}
Context Map 八種模式之一。下游 context 建一層翻譯,把上游(常為 legacy 或不可控系統)的語言、DTO、事件全部隔離在外。必須覆蓋 DTO in / DTO out / Event in / Event out 四個方向。詳見 Ch 17。

### API Contract Card {#api-contract-card}
Ch 14 提出的一頁式 artifact:Trust Boundary / Granularity / Protocol / Auth / Retry / Deprecation Cadence / Observability / Owner。

### API Gateway {#api-gateway}
位於外部 ↔ 內部邊界的反向代理,處理 routing / rate limit / auth / TLS termination。Kong / APISIX / Gloo / AWS API Gateway 為 2026 主流。詳見 Ch 24。

### Apache Iceberg / Delta Lake / Apache Hudi {#lakehouse-formats}
三大開源 Lakehouse 表格格式。Iceberg 中立、Delta 與 Databricks 緊密、Hudi 偏 streaming。詳見 Ch 28。

### ArchiMate {#archimate}
The Open Group 維護的企業架構建模語言,當前 3.2。涵蓋業務 / 應用 / 技術 / 動機四層,與 UML 分層共存。詳見 Ch 5。

### Architecture Knowledge Graph {#architecture-knowledge-graph}
把 ADR、C4、Fitness Function、Code、Stakeholder 之間關係建模成圖,讓 AI Agent 可推理。詳見 Ch 30。

### Architecture Style Selection Card {#architecture-style-selection-card}
Ch 13 提出的一頁式 artifact:這次要擋哪種變動 / 選擇 / 入場成本 / 半年後驗證指標。

### AsyncAPI {#asyncapi}
訊息式 API 規範(Kafka / AMQP / MQTT / WebSocket / SSE),3.0 在 2024 年發布。詳見 Ch 14。

### Atomic / Holistic Fitness Function {#atomic-holistic-ff}
Ford et al. 三維分類之一。Atomic 檢查單一屬性、Holistic 檢查多屬性互動。詳見 Ch 31。

### Audit Trail (AI-Native) {#audit-trail-ai-native}
完整重現一次 AI 決策的輸入、prompt、tool call、輸出的不可變紀錄。對齊 EU AI Act Art. 12。詳見 Ch 33。

---

## B

### Behavior Drift {#behavior-drift}
沒人改 prompt 但 Agent 行為變了。四個來源:底層模型悄悄更新、檢索資料庫加了矛盾文件、使用者提問模式變、工具回傳格式微調。詳見補章 B。

### BFF (Backend for Frontend) {#bff-pattern}
為單一前端類型(web / mobile / desktop)聚合多個後端 API 的中介層。容易越界變成業務邏輯堆積處,需嚴格限制職責。詳見 Ch 24。

### Big Picture Event Storming {#big-picture-event-storming}
Event Storming 三層工作坊的第一層,跨部門以橘色 Domain Event 與紅色 Hotspot 攤開整個領域。詳見 Ch 18。

### Blameless Postmortem {#blameless-postmortem}
SRE 文化核心。事故覆盤聚焦於系統與流程,不找戰犯。詳見 Ch 27。

### Bounded Context (限界上下文) {#bounded-context}
DDD 概念,標示同一業務詞彙語意一致的語言邊界。OOA 是單一 Bounded Context 內的工作方法,DDD 處理跨 context 的整合。詳見 Ch 17。

### Bounded Context Card {#bounded-context-card}
Ch 17 提出的一頁式 artifact:Context Name / Subdomain Type / Ubiquitous Language Top 10 / Upstream / Downstream / Integration Pattern / Owner Team / Out of Scope。

### Bounded Negotiation {#bounded-negotiation}
補章 D 提出的 Multi-Agent 協商協議:Position → Question → Update。最大 3 輪,不收斂強制升級到 Arbiter。

### BPMN (Business Process Model and Notation) {#bpmn}
OMG 維護的業務流程建模語言,當前 2.0.2。可執行子集可由 Camunda 8 / Zeebe 等 workflow engine 直接執行。詳見 Ch 9。

### Brownfield Modernization Pack {#brownfield-modernization-pack}
補章 C 提出的一頁式 artifact:As-Is BC Map / Business Rules Catalog / Migration Dependency Graph / Migration ADR Set / Parallel Run Comparison / 工具組合配置。

### Budget Circuit Breaker {#budget-circuit-breaker}
Multi-Agent 系統在呼叫次數 / wall-clock / token 三維度設置硬上限,超過即停損降級。詳見 Ch 36。

### Build-Measure-Learn {#build-measure-learn}
Eric Ries 提出的精實循環。已過 RAT、要找 PMF 階段使用。詳見 Ch 10。

### Business Tempo (業務節奏) {#business-tempo}
市場、客戶行為或競爭環境改變的觀測週期。衡量單位通常是日/週/月/季。Cadence Charter 的第一欄。詳見 Ch 2。

---

## C

### C4 Diagram Card {#c4-diagram-card}
Ch 19 提出的一頁式 artifact:Level / Audience / Question Answered / Last Update / Owner / Verification / Linked ADRs / Out of Scope。

### C4 Dynamic Diagram {#c4-dynamic-diagram}
C4 補充圖之一,在 Container 圖上以編號箭頭表達某 use case 的時序。詳見 Ch 19。

### C4 Filtered View {#c4-filtered-view}
Structurizr DSL 原生支援的視圖機制。同一份 workspace.dsl 套不同 include / exclude 規則產出的子集。詳見 Ch 19。

### C4 Model {#c4-model}
Simon Brown 2018 年提出的架構視覺化模型。四層:System Context、Container、Component、Code。在 2026 年逐漸成為事實標準。詳見 Ch 19。

### Cadence Charter (節奏對齊章程) {#cadence-charter}
Ch 2 提出的一頁式 artifact:Business / Decision / Release / Feedback Tempo + 對齊紅旗 + 本季校準動作。

### Capstone Pack {#capstone-pack}
Ch 39 提出。全書 39 章 + 6 補章交付的 45 份一頁式 artifact 整合成一棵 docs/ 樹的概念。

### Carbon-Aware Computing {#carbon-aware-computing}
依據電網即時碳強度(g CO2eq / kWh)動態調度 workload(時間 / 區域)。詳見 Ch 32。

### Cell-Based Architecture {#cell-based-architecture}
把系統切成多個獨立 Cell,每個 Cell 是完整自足的故障域單元,透過 Cell Router 路由。AWS 2026 列為超大規模預設模式。詳見 Ch 24。

### Chaos Engineering {#chaos-engineering}
Netflix 倡議的可靠度工程實踐:在受控範圍內注入故障,驗證恢復能力。詳見 Ch 27。

### Chen Notation (Chen 標記) {#chen-notation}
Peter Chen 1976 提出的 ERD 標記法,以矩形 (entity)、菱形 (relationship)、橢圓 (attribute) 為元件。詳見 Ch 8。

### Choreography (Saga) {#choreography}
Saga 的一種實作:服務之間透過事件互相觸發,沒有中央協調者。詳見 Ch 21。

### Circuit Breaker (AI-Native) {#circuit-breaker-ai-native}
當 Agent / LLM 行為異常(drift / hallucination / cost spike)時自動降級或停機的治理機制。詳見 Ch 33。

### CLAUDE.md {#claude-md}
專案級 AI 工程脈絡檔。記錄專案技術棧、複雜度、角色配置。本書框架使用此檔作為多 Agent 協作的 Source of Truth。

### Clean Architecture (整潔架構) {#clean-architecture}
Robert C. Martin 2017 年提出的架構分層方法,四個同心圓(Entities / Use Cases / Interface Adapters / Frameworks & Drivers)。詳見 Ch 11、Ch 13。

### Cloud Native (雲端原生) {#cloud-native}
CNCF 定義的應用設計方法。**不等於 Kubernetes**。詳見 Ch 23。

### Cloud-Native Choice Card {#cloud-native-choice-card}
Ch 23 提出的一頁式 artifact:團隊規模 / 部署平台選擇 / SRE 能力評估 / 平台稅金 / 12-Factor 對齊狀態 / 退場策略 / Owner。

### Coarse-grained Intent {#coarse-grained-intent}
API 顆粒度設計原則,給 AI Agent / partner 的 endpoint 對應業務意圖(create order)而非業務步驟。Wijesekare 2026 提出。詳見 Ch 14。

### Code Archaeology (程式碼考古學) {#code-archaeology}
補章 C 提出的概念:傳統 SA 訪談人類、從業務需求往下推;考古學訪談人類 + 程式碼 + DB + 日誌、從現有行為往上推。

### Cohesion & Coupling (內聚與耦合) {#cohesion-coupling}
Constantine / Myers / Stevens 1974 提出的模組設計度量。詳見 Ch 11。

### Compliance Design Pack {#compliance-design-pack}
補章 E 提出的一頁式 artifact:合規分類 / DPIA × FRIA / Model Card / System Card / Datasheet / 存取控制設計 / 多租戶隔離 / 事件回報 SOP / ISO 42001 / Annex IV。

### Concept Drift {#concept-drift}
輸入–輸出關係 P(Y|X) 隨時間變化。詳見 Ch 38。

### Conceptual Class Diagram {#conceptual-class-diagram}
Larman *Applying UML and Patterns* 區分的 OOA 階段類別圖,記錄業務概念與其關係,而非資料表結構。詳見 Ch 7。

### Concierge MVP {#concierge-mvp}
MVP 工具之一。完全人工服務早期客戶,記下流程後再決定是否寫成軟體。詳見 Ch 10。

### Constitution Layer {#constitution-layer}
CDE 三層之首,對應 CLAUDE.md / agents.md。寫整個 repo / 組織不可動的紅線。建議 ≤ 800 字。詳見 Ch 34。

### Constitutional Classifiers {#constitutional-classifiers}
Anthropic 2026 提出的 prompt injection 自動防護分類器。詳見 Ch 38。

### Context-Driven Engineering (CDE) {#cde}
脈絡驅動工程。2026 年取代 Vibe Coding 的工程典範:用 spec、ADR、CLAUDE.md、agents.md 提供 AI 可讀脈絡。詳見 Ch 34。

### Context Map (上下文映射) {#context-map}
DDD 戰略設計工具,描述 Bounded Context 之間的權力結構與整合模式。Evans 列八種:Partnership / Customer-Supplier / Conformist / Anticorruption Layer / Open-Host Service / Published Language / Shared Kernel / Separate Ways。詳見 Ch 17。

### Continuous Aggregate {#continuous-aggregate}
TimescaleDB 提供的增量物化視圖,自動隨新資料寫入更新聚合結果。詳見 Ch 15。

### Conversation Path Pack {#conversation-path-pack}
補章 F 提出的對話流分析方法:Happy Path / Slot Filling / Disambiguation / Correction / Bailout 五條典型路徑 + 邊角案例集。

### Conversational UX (CUX) {#cux}
對話式 UX。把與系統的互動主介面從 GUI 換成自然語言對話 / 多模態的設計典範。詳見補章 F。

### Coupling Audit Card {#coupling-audit-card}
Ch 11 提出的一頁式 artifact:模組職責 / 對外依賴 / 被依賴情況 / 改動半徑估算 / 抽象等級聲明 / Out of Scope。

### CQRS (Command Query Responsibility Segregation) {#cqrs}
命令查詢責任分離。把寫入路徑(Command)與讀取路徑(Query)分開設計。詳見 Ch 8、Ch 22。

### Crow's Foot Notation (Crow's Foot 標記) {#crows-foot-notation}
ERD 標記法之一,以「魚尾」線端表達 1:1 / 1:N / N:M 基數。Mermaid `erDiagram` 預設語法。詳見 Ch 8。

---

## D

### DACR (Diagnosis / Action / Cause / Recoverability) {#dacr}
Ch 16 提出的錯誤訊息四維設計法。每個錯誤訊息至少需有 D 與 A;C 視合規可選;R 大幅降低放棄率。

### Data Architecture Decision Card {#data-architecture-decision-card}
Ch 28 提出的一頁式 artifact:組織問題 / 儲存問題 / 存取問題 / 三層各自決定 / Data Contract 治理機制 / Owner。

### Data Contract {#data-contract}
資料生產者與消費者的契約,定義 schema、SLA、語意。應進 CI 自動驗證(類比 Pact)。詳見 Ch 28。

### Data Dictionary (資料字典) {#data-dictionary}
DFD 配套產出物。為每個資料流與資料儲存定義欄位、型別、業務規則、來源、流向。詳見 Ch 6。

### Data Drift {#data-drift}
輸入分布 P(X) 隨時間變化,監測手段:KS Test / PSI / embedding centroid。詳見 Ch 38。

### Data Lineage (資料血緣) {#data-lineage}
一筆資料的來源、轉換、流向追蹤。GDPR、PCI DSS v4.0、個資新法的合規要求基礎。詳見 Ch 6、Ch 22。

### Data Lineage Card {#data-lineage-card}
Ch 6 提出的一頁式 artifact:Source / Transformation / Sink / Owner / Update Trigger。

### Data Mesh {#data-mesh}
Zhamak Dehghani 2019/2022 提出的資料架構範式。四原則:Domain Ownership / Data as Product / Self-Serve Platform / Federated Governance。**組織問題**。詳見 Ch 28。

### Data Product {#data-product}
Data Mesh 中的核心單元:有 owner、有 SLA、有版本、有可發現性的資料資產。詳見 Ch 28。

### Datasheet for Datasets {#datasheet-for-datasets}
資料集說明卡,Gebru et al. 2018 提出。記錄資料來源、收集方法、偏誤、用途限制。EU AI Act Art. 10 資料治理要求。詳見補章 E。

### Decision Table (決策表) {#decision-table}
條件 × 動作的二維矩陣,規則層的精準語言。詳見 Ch 9。

### Decision Tempo (決策節奏) {#decision-tempo}
一個產品/技術決定從「提出」到「拍板」並落地為 ADR 的週期。詳見 Ch 2。

### Denormalization (反正規化) {#denormalization}
在已正規化的 schema 上,有意識地引入冗餘以換取讀取性能、簡化查詢、或對齊邊界上下文。詳見 Ch 8。

### DFD (Data Flow Diagram) {#dfd}
資料流程圖。Tom DeMarco 1979 提出。Yourdon-Coad 與 Gane-Sarson 兩套標記法。詳見 Ch 6。

### Diagrams-as-Code (DaC) {#diagrams-as-code}
以純文字格式描述圖形,放進版本控制系統。代表工具:Mermaid、PlantUML、Structurizr DSL、D2。詳見 Ch 5。

### Digital Twin (數位孿生) {#digital-twin}
不是 3D 模型,是設備的資料合約:現在狀態(Telemetry)/ 應該狀態(Setpoint)/ 經歷歷程(Event Log)/ 行為模型(Behavioral Model)。詳見補章 A。

### Distributed Monolith (分散式單體) {#distributed-monolith}
拆成多個服務但同步耦合嚴重,任一服務抖動會 cascade 到所有依賴它的服務。詳見 Ch 21。

### Distributed State Machine (Agent) {#distributed-state-machine-agent}
補章 D 強調的反模式對立面:LLM 決定 action,不決定 state。

### DMN (Decision Model and Notation) {#dmn}
OMG 2014 發佈的決策建模標準,當前 1.4。詳見 Ch 9。

### Domain Event {#domain-event}
領域裡發生過的事實,以過去式動詞命名。Event Sourcing 的 source of truth。詳見 Ch 18、Ch 22。

### DORA Four Keys {#dora-four-keys}
Deployment Frequency / Lead Time for Changes / Change Failure Rate / Time to Restore Service。Forsgren et al. 2018 *Accelerate* 提出。詳見 Ch 29。

### DPIA (Data Protection Impact Assessment) {#dpia}
GDPR Art. 35 要求的資料保護影響評估,高風險處理活動必做。詳見補章 E。

### DRG (Diagnosis-Related Group) {#drg}
診斷關聯群組。住院案件分類系統。詳見 Ch 8。

---

## E

### EDA Layer Card {#eda-layer-card}
Ch 22 提出的一頁式 artifact:EDA 層次選擇 / CQRS 是否必要 / ES 是否必要 / 訊息傳輸選型 / Schema 治理 / Idempotency / Owner。

### EIP (Enterprise Integration Patterns) {#eip}
Gregor Hohpe 與 Bobby Woolf 2003 提出的整合模式語言。入場券是「系統真的是訊息驅動」。詳見 Ch 12。

### Encounter (Clinical BC) {#encounter-clinical-bc}
Clinical Bounded Context 內的就診事件主體。詳見 Ch 17。

### EU AI Act {#eu-ai-act}
歐盟 2024 年通過、2026/8/2 高風險系統全面執行的 AI 法規。罰則上限 3,500 萬歐元或全球年營收 7%。詳見補章 E。

### Eval Set {#eval-set}
AI 系統 QA 的核心資料集,涵蓋 Diversity / Edge / Adversarial / Slice 四維。詳見 Ch 38。

### Eval Set vs Test Set {#eval-vs-test}
傳統 Test 是 Pass/Fail、100% 通過才能 merge。Agent Eval 是統計性的、0–100 分多維度向量、Eval Regression > 3% 才阻擋。詳見補章 B。

### Evaluator-Optimizer Pattern {#evaluator-optimizer}
Generator 產出後由 Evaluator 給 feedback,循環直到達標的 Workflow 模式。詳見 Ch 36。

### Event-Carried State Transfer {#event-carried-state-transfer}
EDA L2 模式。事件酬載攜帶完整或部分業務狀態。詳見 Ch 22。

### Event Log as Truth {#event-log-as-truth}
補章 D 提出的 Multi-Agent 共識基礎模式。所有 Agent 重要動作寫進 append-only event log。

### Event Modeling {#event-modeling}
Adam Dymitruk 2018+ 推廣的事件流建模方法。詳見 Ch 18。

### Event Notification {#event-notification}
EDA L1 模式。事件酬載僅含 ID 與 type,消費者收到後反向呼叫 source。Martin Fowler (2017) 分類。詳見 Ch 22。

### Event Sourcing {#event-sourcing}
事件溯源。狀態 = 事件 fold 的結果;事件本身是 source of truth。詳見 Ch 22。

### Event Storming {#event-storming}
Alberto Brandolini 2013 提出的領域探索工作坊方法。詳見 Ch 9、Ch 18。

### Event Storming Outcome Card {#event-storming-outcome-card}
Ch 18 提出的一頁式 artifact:Big Picture 範圍 / Bounded Context / Aggregate / Hotspot follow-up 清單 / 進入 Event Modeling 的時機 / Owner。

### Expand-Contract Migration {#expand-contract-migration}
Schema 演進模式。先擴展(新增欄位、雙寫、雙讀),確認穩定後再收縮(下線舊欄位)。詳見 Ch 8。

---

## F

### Feedback Tempo (回饋節奏) {#feedback-tempo}
從功能上線到團隊收到可行動訊號的延遲。判準:Feedback Tempo ≤ Release Tempo × 2。詳見 Ch 2。

### FinOps {#finops}
FinOps Foundation 提出的雲端財務治理框架。三階段:Inform / Optimize / Operate。詳見 Ch 32。

### Fitness Function (架構適應度函式) {#fitness-function}
Neal Ford 等人在 *Building Evolutionary Architectures* 中提出:把架構規則寫成可執行的測試,放進 CI 自動驗證,違反者擋 PR。詳見 Ch 11、Ch 20、Ch 31。

### Fitness Function Card {#fitness-function-card}
Ch 31 提出的一頁式 artifact:對應 ADR / 五層分類 / 三維分類 / 工具 / CI 強制度 / Baseline / 量測週期 / Sunset Plan / Owner。

### Fitness Function 五層 {#fitness-function-layers}
Ch 31 整理:Code(ArchUnit / Konsist)/ API(Spectral / Pact / Buf)/ Data(Schema Registry)/ Deploy(OPA / Trivy)/ Observe(Prometheus multi-burn-rate)。

### Four Golden Signals {#golden-signals}
Google SRE Book 提出:Latency / Traffic / Errors / Saturation。詳見 Ch 26。

### 4+1 View Model {#four-plus-one-view}
Kruchten 1995 提出的架構視圖框架:Logical / Process / Development / Physical + Scenarios。詳見 Ch 7。

### FRIA (Fundamental Rights Impact Assessment) {#fria}
EU AI Act Art. 27 要求的基本權利影響評估,高風險 AI 部署前必做。詳見補章 E。

### Functional Dependency (函數依賴) {#functional-dependency}
若已知 A 的值,B 的值就唯一確定,則記為 A → B。正規化的數學基礎。詳見 Ch 8。

---

## G

### Gane-Sarson Notation (Gane-Sarson 標記) {#gane-sarson-notation}
DFD 標記法之一:圓角矩形代表程序、開口矩形代表資料儲存。Chris Gane 與 Trish Sarson 1979 提出。詳見 Ch 6。

### GitOps {#gitops}
以 Git 為 Source of Truth、宣告式管理基礎設施與部署狀態的實踐。Weaveworks 2017 提出。詳見 Ch 23。

### GoF (Gang of Four) {#gof}
Gamma / Helm / Johnson / Vlissides 四人合稱,1994 合著《Design Patterns》。23 模式分創建型 5、結構型 7、行為型 11 三類。詳見 Ch 12。

### Golden Path / Paved Road {#golden-path}
Platform team 提供的「鋪好的路」⸺ 預設選擇 + 內建最佳實踐。詳見 Ch 29。

### GraphQL {#graphql}
Facebook 2015 公開的 query language + runtime,client 描述需要的資料形狀,server 一次回傳。詳見 Ch 14。

### Green Software Foundation Principles {#gsf-principles}
三原則:Carbon Awareness / Carbon Efficiency / Carbon Hardware Efficiency。詳見 Ch 32。

### gRPC {#grpc}
Google 2015 開源的 RPC 框架,基於 HTTP/2 + Protocol Buffers。CNCF 畢業專案。詳見 Ch 14。

---

## H

### HATEOAS {#hateoas}
Hypermedia as the Engine of Application State。REST 的第六項約束。Richardson Maturity Model 第 3 級。詳見 Ch 14。

### Hexagonal Architecture (六角架構) {#hexagonal-architecture}
Alistair Cockburn 2005 提出,又名 Ports & Adapters。所有外部依賴透過 Port 與 Adapter 進入。對抗邊界系統變動。詳見 Ch 13。

### Hidden Vetoer (隱性否決者) {#hidden-vetoer}
組織圖上不顯眼但具有否決權的角色,典型如法遵、稽核、資安、感染管制、職業安全衛生、工會代表。詳見 Ch 3。

### HITL (Human-In-The-Loop) {#hitl}
在不可逆 / 高風險 step 強制要求人類確認的治理機制。詳見 Ch 33。

### Hotspot (Event Storming) {#hotspot-event-storming}
Event Storming 中的紅色便利貼,代表矛盾、不確定、卡住的點。詳見 Ch 18。

### Hybrid Retrieval {#hybrid-retrieval}
混合檢索。同時使用語意檢索(dense / vector)、字面檢索(sparse / BM25)、結構化檢索(KG)三軌,以 RRF 合併排名。詳見 Ch 35。

### Hypertable {#hypertable}
TimescaleDB 的核心抽象,把一張時序表自動依時間維度切成 chunk。詳見 Ch 15。

---

## I

### ICD-10-CM {#icd-10-cm}
WHO 維護的疾病分類第十版。詳見 Ch 8。

### IEC 62443 {#iec-62443}
工業自動化與控制系統(IACS)資訊安全國際標準系列。詳見補章 A、補章 E。

### Idempotency Key {#idempotency-key}
client 在寫操作 header 帶 UUID,server 在 24h 內為同一 key 返回相同結果。詳見 Ch 14、Ch 22。

### Idempotent Receiver (EDA) {#idempotent-receiver-eda}
消費者預設同一事件可能收到多次,以 idempotency-key + 去重機制確保重複處理不產生副作用。詳見 Ch 12、Ch 22。

### IDP (Internal Developer Platform) {#idp}
組成:Service Catalog / CI/CD / Provisioning / Observability / Developer Portal。Backstage / Port / Cortex 為 2026 主流。詳見 Ch 29。

### Information Hiding (資訊隱藏) {#information-hiding}
David Parnas 1972 論文提出的核心概念:模組邊界應劃在「會獨立變化的決定」周圍。詳見 Ch 11。

### Intent Graph (意圖網絡) {#intent-graph}
對話式介面的結構化模型,三層:Intent(意圖)/ Slots(槽位)/ Confirmation(確認)。詳見補章 F。

### Inter-Agent Message Schema {#inter-agent-message-schema}
跨 Agent 訊息的 schema 化結構,production 必要,反 free-form 對話。詳見 Ch 36。

### Interaction State Card {#interaction-state-card}
Ch 16 提出的一頁式 artifact:系統狀態 ↔ UI 對應、DACR 錯誤訊息、資訊不足狀態、復原路徑、a11y 檢核、量化驗收。

---

## J

### Job Story {#job-story}
Intercom 提出的需求敘事格式。模板:When {situation}, I want to {motivation}, so I can {expected outcome}。詳見 Ch 4。

---

## K

### Kano Model {#kano-model}
Noriaki Kano 1984 提出的需求分類模型。Must-Be / Performance / Attractive / Indifferent / Reverse 五類。詳見 Ch 4。

---

## L

### Lakebase {#lakebase}
Databricks 2026 提出的 unified storage layer,整合 OLTP Postgres、analytical Delta 與 vector index。詳見 Ch 15。

### Lakehouse {#lakehouse}
Databricks 2020 倡議。在資料湖儲存格式上加 ACID 與 schema 治理。詳見 Ch 28。

### Late Chunking {#late-chunking}
Jina AI 2024 提出。整篇文檔先以 long-context embedder 計算 token 級 embedding,再 pool 成 chunk embedding。詳見 Ch 35。

### Layered Architecture {#layered-architecture}
N-Tier Architecture 別稱。最常見的企業系統架構風格,典型三層為 Presentation / Business / Data。詳見 Ch 13。

### LLM-as-Judge {#llm-as-judge}
用較強 LLM 評估另一 LLM 輸出的方法,有 position / verbosity / self-preference / domain 四種偏誤。詳見 Ch 38、補章 B。

### LLM-as-Judge Bias 四種 {#llm-judge-bias}
Position Bias / Verbosity Bias / Self-preference / Sycophancy。詳見補章 B。

---

## M

### MADR (Markdown ADR) {#madr}
Markdown Architectural Decision Records 標準格式。詳見 Ch 30。

### Material 3 {#material-3}
Google 2021 發布、2023 起穩定的設計系統第三代。詳見 Ch 16。

### Materialized View (物化視圖) {#materialized-view}
把查詢結果具體化為儲存實體,以換取讀取性能。詳見 Ch 8。

### Mealy Machine {#mealy-machine}
輸出來自當前狀態 + 輸入(transition 上)的有限狀態機。業務系統(訂閱、工單、退款)的常用形式。詳見 Ch 9。

### Microservice Tax Card {#microservice-tax-card}
Ch 21 提出的一頁式 artifact:六項稅金(平台 / 觀測 / 一致性 / 部署 / 認知 / 網路)+ 抵稅條件 + Owner + 退場條件。

### Model Card {#model-card}
AI 模型透明度文件,Mitchell et al. 2018 提出。詳見補章 E。

### Modular Monolith {#modular-monolith}
模組化單體。在單一部署單元內以強模組邊界(編譯期、命名空間、ArchUnit)維持解耦。詳見 Ch 20。

### Module Boundary Card {#module-boundary-card}
Ch 20 提出的一頁式 artifact:Module Identity / Public API / Events Published / Events Consumed / Allowed Dependencies / Boundary Enforcement / Persistence Boundary / Out of Scope / Splittability Score 九節。

### Moore Machine {#moore-machine}
輸出純由當前狀態決定的有限狀態機。較適合硬體、協定握手。詳見 Ch 9。

### MoSCoW {#moscow}
範圍切割優先級方法。Must / Should / Could / Won't 四類。詳見 Ch 4。

### MRN (Medical Record Number) {#mrn}
醫療紀錄號碼。一個病人在某機構內的終身識別碼。詳見 Ch 8。

### Multi-Agent Consensus Pack {#multi-agent-consensus-pack}
補章 D 提出的一頁式 artifact:共識需求分類表 / Event Log Schema / Negotiation Protocol / Distributed State Machine 圖 / 失敗 Runbook。

### Multi-Agent System {#multi-agent-system}
多個獨立 Agent(各有 context window / tools / memory)透過通訊協定協作完成任務的系統。詳見 Ch 36。

### Multi-Agent System Card {#multi-agent-system-card}
Ch 36 提出的一頁式 artifact:模式選擇 / Agent 分工表 / 通訊協定 / 失敗隔離 / Budget Circuit Breaker / Owner。

### Multi-window Multi-burn-rate Alert {#multi-burn-rate}
Google SRE Workbook 提出的告警設計:同時用多個時間窗 + 多個 burn rate 閾值。詳見 Ch 27。

### MVP (Minimum Viable Product) {#mvp}
最小可行產品。Eric Ries (2011) 提出。壓縮市場層歧義(有沒有人要)的最小學習單元。詳見 Ch 10。

---

## N

### Normalization 1NF–5NF {#normalization-forms}
正規化形式。1NF(原子性)→ 2NF → 3NF → BCNF → 4NF → 5NF。詳見 Ch 8。

---

## O

### Observability Plane Card {#observability-plane-card}
Ch 26 提出的一頁式 artifact:系統邊界 / 三大支柱投資配比 / Sampling 策略 / Cardinality 預算 / SLI 列表 / 警報原則 / Owner。

### Offline Autonomy Maturity (離線自治成熟度) {#offline-autonomy}
邊緣節點獨立運轉能力分五級:L0 純採集 / L1 暫存重傳 / L2 本地策略執行 / L3 完整本地閉環 / L4 邊緣協作網。詳見補章 A。

### Onion Architecture (洋蔥架構) {#onion-architecture}
Jeffrey Palermo 2008 提出。以同心圓表示依賴方向。詳見 Ch 13。

### OpenAPI 3.1 {#openapi-3-1}
OpenAPI Initiative 維護的 REST API 規範,3.1(2021)與 JSON Schema 2020-12 對齊。詳見 Ch 14。

### OpenLineage {#openlineage}
Linux Foundation / LF AI & Data 託管的資料血緣機讀規範。詳見 Ch 6。

### Operator Pattern {#operator-pattern}
用 K8s CRD + 控制迴圈封裝特定應用的運維知識的設計模式。詳見 Ch 23。

### Orchestration (Saga) {#orchestration}
Saga 的一種實作:有 Process Manager / Orchestrator 統籌每一步。詳見 Ch 21。

### Orchestrator-Workers Pattern {#orchestrator-workers}
Anthropic Building Effective Agents 五種模式之一,主 Agent 在 runtime 動態拆解任務交給 Worker Agent。詳見 Ch 36。

### Outbox Pattern {#outbox-pattern}
把 DB 寫入與訊息發布綁在同一個本地交易裡的模式,透過獨立 relay 把 outbox 紀錄轉發到 broker。詳見 Ch 21、Ch 22。

---

## P

### PACELC {#pacelc}
Daniel Abadi 2012 提出的分散式資料庫取捨模型。Partition 時 A vs C,Else(平時)Latency vs Consistency。詳見 Ch 15。

### Pact {#pact}
Consumer-driven contract testing 框架。Pact Broker 為交換中樞。詳見 Ch 14。

### Parallelization (Agentic) {#parallelization-agentic}
Workflow 模式之一,同任務並行多次執行後投票 / 聚合,用於多角度檢視。詳見 Ch 36。

### Partitioning (分割) {#partitioning}
在單一資料庫實例內把大表切成多個物理區段(範圍 / 列表 / Hash)。與跨主機 Sharding 不同。詳見 Ch 8。

### Pattern Adoption Card {#pattern-adoption-card}
Ch 12 提出的一頁式 artifact:Pattern Name / Problem / Cost of Adoption / Cost of NOT Adopting / Alternatives / Exit Strategy / Acceptance Signal。

### pgvector {#pgvector}
PostgreSQL 向量相似搜尋 extension,支援 IVFFlat 與 HNSW 索引,2024–2026 為 PG 生態 RAG 主流選擇。詳見 Ch 15。

### Plan-Execute (Coding Agent) {#plan-execute}
Terminal Agent 成熟工作模式。Agent 接到任務後先寫 plan.md,經人類 review 後再執行。詳見 Ch 37。

### Platform-as-a-Product {#platform-as-a-product}
把內部開發者當客戶經營的 platform engineering 思維。需有 PM、roadmap、NPS、retention KPI。詳見 Ch 29。

### Platform Product Card {#platform-product-card}
Ch 29 提出的一頁式 artifact:目標客戶 / Top 3 Golden Path / DORA + SPACE 指標 / 平台 NPS / Roadmap / Owner / Retention 機制。

### Pod Security Standards (PSS) {#pod-security-standards}
K8s 1.25 起取代 PodSecurityPolicy 的三檔安全規範:privileged / baseline / restricted。詳見 Ch 23。

### Policy (Event Storming) {#policy-event-storming}
Event Storming 紫色便利貼,描述「當 X 事件發生時,自動觸發 Y command」的反應式規則。詳見 Ch 18、Ch 22。

### Ports & Adapters {#ports-and-adapters}
Hexagonal Architecture 另一個名字。Driving Adapter 在左、Driven Adapter 在右。詳見 Ch 13。

### Power-Interest Grid {#power-interest-grid}
Mendelow 1981 提出的二維利害關係人分類矩陣。詳見 Ch 3。

### PR Review Bot {#pr-review-bot}
PR 流程中自動 review 的 Coding Agent 子類。CodeRabbit / Greptile / Sweep。詳見 Ch 37。

### PRD (Product Requirements Document) {#prd}
產品需求文件。壓縮商業層歧義(為什麼做、給誰、解什麼痛)的規格文件。詳見 Ch 10。

### Pretotyping {#pretotyping}
Alberto Savoia 提出的方法論(*The Right It*, 2019)。在做產品之前,用最低成本驗證「有沒有人要」。詳見 Ch 10。

### Process Modelling Event Storming {#process-modelling-event-storming}
Event Storming 三層工作坊第二層,聚焦單一關鍵流程,補入 Command / Aggregate / Policy / Read Model / External System。詳見 Ch 18。

### Process Model Triage Card {#process-model-triage-card}
Ch 9 提出的一頁式 artifact:這個流程屬於哪一層 / 該畫哪張 / 圖的版本控制位置 / 由誰更新。

### Project Initiation Brief {#project-initiation-brief}
啟動階段第一份要產出的一頁式文件,先於 Project Charter。內容:Why Now、TELOP 五維初判、利害關係人初步盤點、Top 5 風險、下一個 Gate、Out of Scope。詳見 Ch 3。

### Prompt Caching (Anthropic) {#prompt-caching}
Anthropic 2024 推出的 LLM 成本控制機制:重複的 system prompt + tools 定義 cache 5 分鐘,命中時 input token 折扣 90%。詳見 Ch 32。

### Prompt Chaining {#prompt-chaining}
任務拆成固定線性步驟,前一步輸出餵下一步的最簡 Workflow 模式。詳見 Ch 36。

### Prompt Drift {#prompt-drift}
Prompt / RAG / tool 改動未經完整 regression eval 即上線。詳見 Ch 38。

### Prompt Injection {#prompt-injection}
OWASP LLM Top 10 (2024) 排首位的 AI 系統威脅。攻擊者透過輸入操縱 LLM 行為。詳見 Ch 25、Ch 38。

### PSI (Population Stability Index) {#psi}
fintech 風控業界 drift 量測指標,經驗閾值 < 0.1 / 0.1–0.25 / > 0.25。詳見 Ch 38。

### Public API (Module) {#public-api-module}
一個模組對外暴露的契約集合。模組外部只准 import Public API,其餘類別屬於私有。詳見 Ch 20。

---

## Q

### Quality Scenario {#quality-scenario}
SEI 提出的 NFR 描述格式:Source / Stimulus / Environment / Response / Response Measure 五欄式。詳見 Ch 4 與 Ch 25。

---

## R

### RAG (Retrieval-Augmented Generation) {#rag}
檢索增強生成。三段式 pipeline:Retriever / Reranker / Generator。詳見 Ch 35。

### RAT (Riskiest Assumption Test) {#rat}
最高風險假設測試。MVP 的核心提問:這個產品最可能死掉的假設是哪一個?先驗那個。詳見 Ch 10。

### Read Model {#read-model}
為了某個查詢 / 報表 / UI 而生的資料視圖,在 CQRS 中與 Write Model 分離。詳見 Ch 18、Ch 22。

### Reciprocal Rank Fusion (RRF) {#rrf}
多軌檢索結果合併演算法。score = sum(1 / (k + rank_i)),經典 k=60(Cormack et al. 2009)。詳見 Ch 35。

### Release Tempo (發布節奏) {#release-tempo}
生產環境部署頻率。詳見 Ch 2。

### Requirements Traceability Matrix (RTM) {#rtm}
需求追蹤矩陣。把每個需求對應到設計、實作、測試的對照表。詳見 Ch 4。

### REST (Representational State Transfer) {#rest}
Roy Fielding 2000 博士論文提出的架構風格,六項約束。詳見 Ch 14。

### Reverse ETL {#reverse-etl}
從 warehouse / lakehouse 把分析結果反向同步回 SaaS 工具(Salesforce / HubSpot / Iterable)的模式。詳見 Ch 28。

### RICE {#rice}
Reach × Impact × Confidence ÷ Effort。Intercom 採用的量化排序方法。詳見 Ch 4。

### Richardson Maturity Model {#richardson-maturity-model}
Leonard Richardson 2008 提出的 REST 成熟度模型,0–3 級。詳見 Ch 14。

### Routing (Agentic) {#routing-agentic}
Workflow 模式之一,先用 Router LLM 分類輸入,再導向預定義子流程。詳見 Ch 36。

---

## S

### SA/SD {#sa-sd}
Systems Analysis / Systems Design。系統分析與系統設計。本書主題。

### Saga Pattern {#saga-pattern}
把長交易拆成一連串本地交易 + 對應補償交易的模式,1987 Garcia-Molina & Salem 提出。詳見 Ch 21、Ch 22。

### Salience Model {#salience-model}
Mitchell, Agle & Wood 1997 三維利害關係人模型:Power + Legitimacy + Urgency。詳見 Ch 3。

### SBOM (Software Bill of Materials) {#sbom}
軟體物料清單。SPDX / CycloneDX 為主要格式。詳見 Ch 25。

### Schema Decision Card {#schema-decision-card}
Ch 8 提出的一頁式 artifact:欄位 / 型別 / 來源 / 索引策略 / 演進策略 / 不可變性聲明。

### SCI (Software Carbon Intensity) {#sci}
ISO/IEC 21031:2024 標準。SCI = ((E × I) + M) / R。詳見 Ch 32。

### Scrum-but {#scrum-but}
Ron Jeffries 點名的反模式句型:「我們做 Scrum,但是…」。詳見 Ch 2。

### Service Blueprint {#service-blueprint}
服務藍圖。Lynn Shostack 1984 提出。詳見 Ch 16。

### Service Mesh {#service-mesh}
基礎設施層,透過 sidecar(或 sidecar-less data plane)為服務間流量提供 mTLS、observability、traffic policy。詳見 Ch 24。

### Sharding (分片) {#sharding}
跨主機把資料切成獨立子集,每個 shard 在不同實例。詳見 Ch 8。

### Signal-Decision-Confidence (SDC) Model {#sdc-model}
補章 F 採用的多模態 / CUX 分析框架,五層:Continuous Signals → Feature Extraction → Multi-Modal Fusion → Decision with Confidence → Action with Reversibility。

### Skill (Claude Code) {#skill-claude-code}
Anthropic Claude Code 中的可調用能力單元。三要素契約:Description(何時觸發)/ Allowed Tools(工具白名單)/ Knowledge Sources(脈絡來源)。詳見 Ch 34。

### SLI / SLO / SLA / Error Budget {#sli-slo-sla-eb}
SLI(指標)→ SLO(內部紀律目標)→ SLA(對外合約承諾,通常 < SLO)→ Error Budget(SLO 容許的「不可靠時數預算」)。詳見 Ch 27。

### SLO Catalog + Error Budget Card {#slo-catalog-card}
Ch 27 提出的一頁式 artifact:SLI 定義 / SLO 目標 / 量測方式 / 季度 Error Budget / 已用比例 / 補預算機制 / Owner。

### Software Design Event Storming {#software-design-event-storming}
Event Storming 三層工作坊第三層,聚焦單一 Aggregate,寫出 invariant 與 Command/Event 配對。詳見 Ch 18。

### SOLID Principles {#solid-principles}
Robert C. Martin 整理的五條物件導向設計原則:SRP / OCP / LSP / ISP / DIP。詳見 Ch 11。

### SPACE Framework {#space-framework}
Forsgren et al. 2021 提出:Satisfaction / Performance / Activity / Communication / Efficiency。補足 DORA 偏重產出量的盲點。詳見 Ch 29。

### Sparkplug B {#sparkplug-b}
Eclipse 基金會規範,把 MQTT 從「訊息協定」升級為「狀態協定」。詳見補章 A。

### Spec-as-Prompt-Context {#spec-as-prompt-context}
2026 視角的需求文件設計原則:讓需求文件同時是人類規格與 AI Agent 的脈絡輸入。詳見 Ch 4 與 Ch 10。

### Spec Triage One-Pager {#spec-triage}
Ch 10 提出的一頁式 artifact:這次該寫哪份(PRD/SRS/MVP)/ 待壓縮的歧義是什麼 / 由誰簽收 / 如何驗收。

### Spectral {#spectral}
Stoplight 開源的 OpenAPI / AsyncAPI linter。詳見 Ch 14。

### SRS (Software Requirements Specification) {#srs}
系統需求規格。壓縮工程層歧義(怎麼算做完、NFR 門檻、邊界)的規格文件。詳見 Ch 10。

### Stakeholder Analysis (利害關係人分析) {#stakeholder-analysis}
識別、分類、追蹤所有能影響專案或被專案影響的個人或群體的系統性方法。詳見 Ch 3。

### State Machine / Statechart (狀態機) {#state-machine}
描述單一實體生命週期的形式化模型。Mealy 機與 Moore 機為兩種主流。詳見 Ch 9。

### State Machine Diagram {#state-machine-diagram}
UML 行為圖之一。表達某個實體在生命週期中的狀態與轉移。詳見 Ch 5、Ch 9。

### Static / Dynamic Fitness Function {#static-dynamic-ff}
Static 不需執行(靜態分析)、Dynamic 需執行(integration / chaos test)。詳見 Ch 31。

### Storage Selection Card {#storage-selection-card}
Ch 15 提出的一頁式 artifact:Workload Profile / 候選引擎(含維持現狀)/ 決策(PACELC 對齊)/ 入場成本 / 半年後 reassessment trigger / Out of Scope。

### Strangler Fig (Brownfield) {#strangler-fig}
Martin Fowler 2004 推廣的漸進遷移策略:在舊系統外圍包一層 ACL,逐步攔截、替換、量化、收掉舊邏輯。詳見 Ch 20、補章 C。

### Strangler Fig 三條黃金規則 {#strangler-fig-three-rules}
補章 C 提出:(1) To-Be 必須能用 As-Is 語言被解釋 / (2) 任何 To-Be 模組必須有並行運轉一個月計畫 / (3) Strangler Fig 必須有「中途停下來」的設計。

### STRIDE Threat Modeling {#stride}
Microsoft 提出的威脅分類:Spoofing / Tampering / Repudiation / Information Disclosure / Denial of Service / Elevation of Privilege。詳見 Ch 25。

### Structurizr DSL {#structurizr-dsl}
Simon Brown 設計的 C4 專用 DSL。Ch 19 主示範工具。

### Structured Analysis (結構化分析) {#structured-analysis}
1970s 末由 DeMarco / Yourdon / Constantine / Gane-Sarson 提出的系統分析方法,核心工具為 DFD + 資料字典 + 程序規格。詳見 Ch 6。

### Subagent {#subagent}
Claude Code 的協作模式,主 Agent 把特定任務委派給專責子 Agent。詳見 Ch 34。

### Subdomain Classification (子域分類) {#subdomain-classification}
DDD 戰略設計第一步,把業務域分成 Core / Supporting / Generic 三類。詳見 Ch 17。

### SWE-Bench {#swe-bench}
Princeton NLP 2023+ 的 LLM coding benchmark。詳見 Ch 37。

### System Charter {#system-charter}
系統章程。Ch 1 提出的一頁式 artifact:Problem / Constraints / Decisions / Open Questions / Owners。

### System Card {#system-card}
AI 系統(模型 + 資料 + 部署上下文)透明度文件。詳見補章 E。

### System Landscape Diagram {#system-landscape-diagram}
C4 補充圖之一,集團 / 多產品線等級的 Level 0。詳見 Ch 19。

---

## T

### Tail-based Sampling {#tail-based-sampling}
基於 trace 完成後的觀察決定保留與否。確保事故 trace 不被丟掉。詳見 Ch 26。

### Team Topologies (團隊拓撲) {#team-topologies}
Skelton & Pais 2019 提出的四種團隊類型:Stream-aligned / Platform / Enabling / Complicated-Subsystem。詳見 Ch 29。

### TELOP 五維可行性 {#telop}
本書對傳統 TELOS 框架的修訂版本:把 S(Schedule)歸還專案管理,把 P(Political,政治可行性)補進來。詳見 Ch 3。

### Tenant Isolation (多租戶隔離) {#tenant-isolation}
SaaS / RAG 系統的合規核心:儲存 / 計算 / 模型 / 遙測四層皆需隔離。詳見補章 E。

### Test-Driven Generation (TDG) {#tdg}
人類先寫失敗測試,Agent 拿測試 + 相關脈絡迭代產出實作直到測試全綠。詳見 Ch 37。

### Threat Model Card {#threat-model-card}
Ch 25 提出的一頁式 artifact:系統邊界 / 信任邊界 / STRIDE 六項威脅 / 緩解措施 / 殘餘風險 / Owner。

### Three Pillars of Observability {#three-pillars}
Logs / Metrics / Traces 三大支柱。2025–2026 收斂為以 trace_id 相關的單一資料平面。詳見 Ch 26。

### Tool Use (LLM) {#tool-use}
LLM 透過 structured output 呼叫外部函式 / API 的能力。設計四原則:Selection / Composition / Failure Handling / Least Privilege。詳見 Ch 35。

### Traffic Governance Card {#traffic-governance-card}
Ch 24 提出的一頁式 artifact:三層治理選型(Gateway / Mesh / Cell)/ 規模門檻 / Mesh data plane vs control plane 分離 / Cell 邊界定義 / Owner。

### Triggered / Continuous Fitness Function {#triggered-continuous-ff}
Triggered 在 PR / release 觸發、Continuous 持續監測(SLO burn rate)。詳見 Ch 31。

### 12-Factor App (十二因子應用) {#twelve-factor-app}
Heroku 2011 發表(Adam Wiggins 主筆)的雲端原生應用 12 條原則。詳見 Ch 11。

### 三類共識需求 {#three-types-of-consensus}
補章 D 提出:資料共識(誰的數值對)/ 權威共識(誰說了算)/ 意義共識(這代表什麼)。

---

## U

### Ubiquitous Language (通用語言) {#ubiquitous-language}
DDD 戰略設計概念。在單一 Bounded Context 內,所有人用同一個詞時理解一致的契約。詳見 Ch 17。

### UML (Unified Modeling Language) {#uml}
統一塑模語言。OMG 維護,最新 2.5.1(2017)。14 種圖。2026 工程現場常用三種:Class / Sequence / State。詳見 Ch 5。

### Upcasting {#upcasting}
消費者讀取舊版事件時,在進入領域邏輯前升級到當前版本的機制。詳見 Ch 22。

### USE Method {#use-method}
Brendan Gregg 提出的資源監控指標:Utilization(使用率)/ Saturation(飽和度)/ Errors(錯誤)。詳見 Ch 26。

### Use Case Altitude (用例海拔) {#use-case-altitude}
Cockburn *Writing Effective Use Cases* 提出的用例顆粒度隱喻:雲端(摘要)/ 海面(用戶目標)/ 海底(子功能)。詳見 Ch 7。

### Use Case Atom {#use-case-atom}
Ch 7 提出的一頁式 artifact:Trigger / Actor / Pre-state / Post-state / Linked Class / Linked State Diagram / Linked Sequence / Variants / Out of Scope。

### User Journey Map {#user-journey-map}
使用者旅程地圖。從使用者視角描繪「跨時間、跨觸點完成某項目標」的階段、行動、感受、痛點。詳見 Ch 16。

### UUIDv7 / ULID {#uuidv7-ulid}
時間有序的 128-bit 唯一識別碼。UUIDv7 由 IETF RFC 9562 (May 2024) 規範。詳見 Ch 8。

---

## V

### Vibe Coding {#vibe-coding}
2024–2025 興起的 AI 協作風格:大量倚賴 LLM 對話直接寫程式,脈絡與決定主要存在於會話內。詳見 Ch 1、Ch 34。

---

## W

### WCAG 2.2 {#wcag-2-2}
Web Content Accessibility Guidelines 2.2,W3C 2023 年 10 月發布。詳見 Ch 16。

### Webhook {#webhook}
server 主動 HTTP POST 推送事件給 partner 預先註冊的 URL。需配套 HMAC 簽章 / Idempotency-Key / 重試策略 / 棄用通知。詳見 Ch 14。

### Wizard-of-Oz MVP {#wizard-of-oz-mvp}
MVP 工具之一。前台看起來自動化,後台由人工執行。詳見 Ch 10。

### Workload-Aware Engineering {#workload-aware-engineering}
Ch 32 提出的整合視角:把 FinOps、Green Software、Performance 視為同一份 Workload Profile 的三個視角。

### Workload Cost & Carbon Card {#workload-cost-carbon-card}
Ch 32 提出的一頁式 artifact:Workload Profile / 月成本基線 / 月碳排基線 / Top 3 最佳化動作 / SCI 數值 / Owner。

### Workload Profile {#workload-profile}
系統被讀寫的量化描述,五維:讀寫比、查詢模式、規模、一致性需求、延遲 SLO。資料儲存選型的前置產出。詳見 Ch 15。

### WSJF (Weighted Shortest Job First) {#wsjf}
加權最短作業優先。Cost of Delay ÷ Job Size,源自 Donald Reinertsen,後被 SAFe 採用。詳見 Ch 4。

---

## Y

### Y-Statement {#y-statement}
Olaf Zimmermann 提出的單句 ADR 格式:In the context of {use case}, facing {concern}, we decided for {option}, to achieve {quality}, accepting {downside}。詳見 Ch 30。

### Yourdon-Coad Notation (Yourdon-Coad 標記) {#yourdon-coad-notation}
DFD 標記法之一:圓圈代表程序、雙線代表資料儲存、矩形代表外部實體、箭頭代表資料流。詳見 Ch 6。

---

## Z

### Zero Trust Architecture {#zero-trust}
NIST SP 800-207 定義的安全架構:Never trust, always verify。詳見 Ch 25。
