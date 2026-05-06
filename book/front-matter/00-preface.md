---
chapter: 0
part: front-matter
title: 序章 — 為什麼還要寫一本 SA/SD 書
slug: preface
agent: Orchestrator
status: published
---

# 序章 ⸺ 為什麼還要寫一本 SA/SD 書

## 這本書不打算解釋什麼是「系統分析」

書架上已經有十幾本經典 SA/SD 教科書。Valacich & George 的《Modern Systems Analysis and Design》到第 10 版了,Tilley 的書到第 13 版了,Eric Evans 的 *Domain-Driven Design* 在 2003 年定義了一個世代,Sam Newman 的《Building Microservices》第二版填了 2021 年的空白。這些書寫得好。

如果這本書要做的事情是「再寫一遍那些書」,那就沒必要動筆。

這本書要做的不一樣。

## 真正的問題:2025–2026 之後,SA/SD 的劇本要重新接

過去三十年,SA/SD 是一門逐漸穩定的學科。教科書的章節幾乎可以預測:訪談、進度研究、需求蒐集、資料流圖、實體關係圖、結構化設計、模組實作、整合與維護。這套章節是建立在「一份規格 → 寫一份程式碼 → 維護一份系統」的線性世界觀上。

到 2025–2026,軟體工程經歷了三十年來最劇烈的結構性轉變:

- **微服務退潮**。CNCF 2026 Q1 報告顯示,42% 採用微服務的組織已將部分服務整併回模組化單體。Shopify 在 2025 年公開以單一模組化單體處理 30TB/min 訊息流量的架構。Neal Ford 與 Sam Newman 在 2026 年公開宣告反思元年。
- **AI 代理進入工程流程**。Vibe Coding 一詞在 2025 上半年流行,被 Context-Driven Engineering(CDE)取代;規格(spec)、ADR、CLAUDE.md / agents.md 成為可被 LLM 讀取的脈絡,從輔助工具變為一級工程產出。
- **架構由 Agent 來設計**。AWS、Databricks、Microsoft 在 2026 年都明確指出:當 AI Agent 成為系統的主要消費者,DDD、Cell-based 架構、可逆操作的價值,從「建議」變成「生存條件」。
- **可觀測性的工程一級能力**。OpenTelemetry 在 2025 達到 12+ 語言穩定,2026 報告顯示 32.8% 的可觀測性團隊將「跨訊號相關」(traces、metrics、logs)取代了過去的監控組合。

在這樣的轉折點上,沿用 1990 年代的 SA/SD 框架教導工程師,就像給拿了無法在現代技術環境下生存的工具。本書的目的,是把古老 SA/SD 的核心知識,與雲原生、資料密集、AI 原生(AI-Native)的架構視角整合成一條完整的學習路徑。

## 三個改寫原則

這本書的設計貫徹三個原則:

### 一、古老不被丟棄,只被重新脈絡化(Recontextualized, Not Replaced)

資料流圖、ERD、UML、用例分析這些古老工具,在 AI 時代的價值沒有變小,反而因為需要產出**機器可讀的清晰邊界**而再次重要。本書不丟棄分析的基礎,而是讓基礎重新獲得當代的意義。

### 二、從「畫圖」轉向「建模」(From Drawing to Modelling)

Simon Brown 多次強調:多張漂亮的圖無法取代一個系統,但一個清楚的模型可以衍生出多張對應不同讀者的圖。本書教讀者建立心智模型,而非畫符號。

### 三、立即實用,而非可考試的

每一章的語言一套配置與一組可帶走的 artifact,讀者完成閱讀後,就會擁有一套可直接帶入工作的工具:System Charter、Cadence Charter、Project Initiation Brief、Requirements Decision Log、Bounded Context Card、API Contract Card、Threat Model Card、Observability Plane Card、SLO Catalog、Fitness Function Card、Workload Cost & Carbon Card、AI-Native System Vision Card⋯⋯ 全書共 45 份。

## 寫給誰

本書適合三層讀者,不同層次有不同的閱讀路徑:

- **新手(0–2 年)**:從第 I 篇到第 III 篇,熟練第 47 章 Capstone 的核心 artifact 即可獨立完成需求分析與設計。
- **進階(3–8 年)**:基礎之上額外閱讀第 IV 篇與第 V 篇,並選讀第 VI 篇。重點掌握分散式系統的架構決策、模組化單體 vs 微服務、可觀測性與 ADR 流程。
- **資深 / 架構師(8+ 年)**:重點通讀,著重第 IV、VI、VII、VIII 篇。關注 AI 原生系統設計、跨團隊架構治理、建立內部開發者平台(IDP)、引入適應度函式。

詳見 [01-reader-guide.md](./01-reader-guide.md)。

## 與其他書籍的關係

本書並非取代下列經典,而是與它們互為層級:

- **Valacich & George《Modern Systems Analysis and Design》第 10 版** ⸺ 流程與方法論的權威,提供瀑布式 SDLC 與需求工程的完整結構。
- **Eric Evans《Domain-Driven Design》與 Vaughn Vernon《Implementing DDD》** ⸺ DDD 戰略與戰術經典,本書將 DDD 與 Event Storming、Cell-based 設計連動。
- **Simon Brown《Software Architecture for Developers》與 C4 Model** ⸺ 架構視覺化的事實標準,本書採用其 4 層解法。
- **Sam Newman《Building Microservices》、Neal Ford《Software Architecture: The Hard Parts》** ⸺ 微服務的反思與權衡,本書以「先做模組化單體」收緊。
- **Chip Huyen《Designing Machine Learning Systems》與 Anthropic / OpenAI 2026 Agent 設計指引** ⸺ 本書第 VII 篇 AI 時代章節的最新依據。

## 一個誠實的承諾

書裡所有公司名、產品名、流水數字都是虛構,但業務邏輯、技術細節、合規條文都來自真實工程現場。寫法是「戰場筆記」⸺ 每一章從一個現場片段開頭,拆解真問題,給可以抄走的決策框架,列出常見地雷,結尾交付一份一頁式 artifact。

每一章後面都應該留下一個能塞進 PR、能釘在白板、能丟給 AI Agent 當 context 的東西。這不是裝飾,是 SA/SD 在 2026 年的工作方式。

---

下一站:[01 三層讀者導引](./01-reader-guide.md)。
