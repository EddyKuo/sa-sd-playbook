# 《系統分析與系統設計 2026 版》

> 從乾淨白板,到 AI 會寫程式的工程現場。
> 39 章 + 6 補章 = 41 篇,純戰場筆記,非教科書。

---

## 全書地圖(閱讀順序)

主章與補章按**插入順序**呈現,而非主大綱的乾淨順序。

### 前置(Front Matter)

- [00 序章 — 為什麼還要寫一本 SA/SD 書](front-matter/00-preface.md)
- [01 三層讀者導引(新手 / 進階 / 資深)](front-matter/01-reader-guide.md)
- [02 章節依存圖 — 如何讀這本書](front-matter/02-how-to-read.md)

### 第 I 篇 — 認知基礎

- [**篇導讀**](part-01-foundations/00-overview.md) — 詞彙層建立 / 章節依存圖 / 三條讀者路徑
- [Ch 1 為什麼系統分析與系統設計](part-01-foundations/ch-01-why-sa-sd.md) — 在 AI 會寫程式的 2026 年
- [Ch 2 SDLC 與方法論演進](part-01-foundations/ch-02-sdlc-evolution.md) — 從瀑布到 Context-Driven Engineering
- [Ch 3 專案啟動與利害關係人分析](part-01-foundations/ch-03-project-initiation.md) — 摸清誰能讓這事死掉
- [Ch 4 需求工程基礎](part-01-foundations/ch-04-requirements-engineering.md) — 從訪談到拒絕清單
- [Ch 5 UML 模型語言全景](part-01-foundations/ch-05-uml-overview.md) — 14 種圖,你只需要 3 種

### 第 II 篇 — 分析

- [**篇導讀**](part-02-analysis/00-overview.md) — 五種分析工具的問題型別 / 章節依存圖 / 讀者入口
- [Ch 6 結構化分析 — DFD](part-02-analysis/ch-06-dfd-structured-analysis.md)
- [Ch 7 物件導向分析](part-02-analysis/ch-07-object-oriented-analysis.md) — 從用例到狀態,讓四張圖一起活著
- [Ch 8 資料模型與正規化](part-02-analysis/ch-08-data-modeling-normalization.md) — 3NF 通過 ≠ schema 是好的
- [Ch 9 流程模型](part-02-analysis/ch-09-process-modeling.md) — BPMN / 狀態機 / 決策表三層分工
- [Ch 10 規格文件](part-02-analysis/ch-10-spec-documents.md) — PRD / SRS / MVP 壓縮三層歧義

### 第 III 篇 — 設計基礎

- [**篇導讀**](part-03-design/00-overview.md) — 六章 + 補章 F / 改動半徑到 CUX 的設計地基 / 章節依存圖
- [Ch 11 軟體架構原則](part-03-design/ch-11-architecture-principles.md) — SOLID / Clean / 12-Factor 是改動半徑成本估算工具
- [Ch 12 設計模式](part-03-design/ch-12-design-patterns.md) — GoF 與 EIP,為已知問題命名的工具
- [Ch 13 架構風格實戰](part-03-design/ch-13-architecture-styles.md) — 各擋哪一種變動
- [Ch 14 API 設計](part-03-design/ch-14-api-design.md) — 各自定義不同的信任邊界
- [Ch 15 資料儲存設計](part-03-design/ch-15-data-storage.md) — 先看 Workload 再選引擎
- [Ch 16 UI/UX 與人機互動的系統觀](part-03-design/ch-16-uiux-system-view.md) — UX 是錯誤狀態下的決策設計
- **[補章 F 多模態與對話式互動](part-03-design/chF-cux.md)** — Multimodal & CUX

### 第 IV 篇 — 進階架構

- [**篇導讀**](part-04-architecture/00-overview.md) — 八章 + 補章 A / 複雜度增長的架構工具序列 / 章節依存圖
- [Ch 17 領域驅動設計(DDD)](part-04-architecture/ch-17-ddd-strategic-tactical.md) — 戰略 vs 戰術,真正的價值在語言邊界
- [Ch 18 Event Storming 與 Event Modeling](part-04-architecture/ch-18-event-storming-modeling.md)
- [Ch 19 C4 Model 與架構視覺化](part-04-architecture/ch-19-c4-model-visualization.md) — 給多種讀者看的同一份地圖
- [Ch 20 Modular Monolith](part-04-architecture/ch-20-modular-monolith.md) — 2026 微服務反思元年的主場
- [Ch 21 微服務架構](part-04-architecture/ch-21-microservices.md) — 分散式系統的稅金與其抵稅條件
- [Ch 22 EDA / CQRS / Event Sourcing](part-04-architecture/ch-22-event-driven-cqrs-es.md) — 三件不該綁一起的工具
- [Ch 23 雲端原生與 Kubernetes](part-04-architecture/ch-23-cloud-native-kubernetes.md) — 不是用 K8s 就是雲端原生
- [Ch 24 Service Mesh / API Gateway / Cell-Based](part-04-architecture/ch-24-service-mesh-cell-based.md) — 三層流量治理
- **[補章 A 邊緣計算與 OT/IT 融合](part-04-architecture/chA-edge-ot-it.md)**

### 第 V 篇 — 品質屬性

- [**篇導讀**](part-05-quality/00-overview.md) — 四章 + 補章 E / 安全到合規的品質屬性依存順序 / 章節依存圖
- [Ch 25 Security by Design](part-05-quality/ch-25-security-by-design.md) — 不是清單,是預設值
- **[補章 E Compliance by Design](part-05-quality/chE-compliance.md)** — AI 合規架構
- [Ch 26 可觀測性 / OpenTelemetry](part-05-quality/ch-26-observability-otel.md) — 不該只是 Dashboard 牆
- [Ch 27 SRE / SLO / Chaos Engineering](part-05-quality/ch-27-sre-slo-chaos.md) — 用 Error Budget 換來的可靠度
- [Ch 28 資料架構](part-05-quality/ch-28-data-architecture.md) — Data Mesh / Lakehouse / Lakebase 三層問題

### 第 VI 篇 — 現代工程實踐

- [**篇導讀**](part-06-engineering/00-overview.md) — 四章 / 工程文化基礎設施 / IDP → ADR → Fitness → FinOps 依存圖
- [Ch 29 Platform Engineering 與 IDP](part-06-engineering/ch-29-platform-engineering-idp.md) — Platform-as-a-Product
- [Ch 30 架構決策紀錄(ADR)](part-06-engineering/ch-30-adr-architecture-knowledge.md) — 把決策寫成「決定的化石」
- [Ch 31 架構適應度函式](part-06-engineering/ch-31-fitness-functions.md) — 把架構規則寫成可執行的測試
- [Ch 32 FinOps 與綠色軟體](part-06-engineering/ch-32-finops-green-software.md) — 帳單與碳排是同一個 Workload Profile

### 第 VII 篇 — AI 時代的 SA/SD

- [**篇導讀**](part-07-ai-era/00-overview.md) — 六章 + 補章 B/C/D / 複雜度增長的 AI 工具序列 / 各讀者入口
- [Ch 33 AI-Native Architecture](part-07-ai-era/ch-33-ai-native-architecture.md) — 從 AI-Embedded 到 Agent-First
- [Ch 34 Context-Driven Engineering(CDE)](part-07-ai-era/ch-34-context-driven-engineering.md)
- [Ch 35 RAG / Memory / Tool 設計](part-07-ai-era/ch-35-rag-memory-tool.md) — 三組記憶與三種能力
- [Ch 36 Multi-Agent 系統設計](part-07-ai-era/ch-36-multi-agent.md) — 不是更多 Agent,是更窄的 Agent
- **[補章 D Multi-Agent 共識、狀態與衝突解決](part-07-ai-era/chD-multi-agent.md)**
- [Ch 37 AI Coding Agent / Pair Programming](part-07-ai-era/ch-37-coding-agent.md)
- [Ch 38 AI 系統的 Eval / Drift / Red Team](part-07-ai-era/ch-38-ai-eval-drift-redteam.md)
- **[補章 B Agentic QA](part-07-ai-era/chB-agentic-qa.md)** — 非確定性系統的品質保證
- **[補章 C 遺留系統現代化與 AI 逆向工程](part-07-ai-era/chC-legacy-ai.md)**

### 第 VIII 篇 — 綜合 Capstone

- [**篇導讀**](part-08-synthesis/00-overview.md) — PayLoop 2.0 / 45 份 artifact 對應索引 / 你讀完能做的事
- [Ch 39 Capstone — 把 SA/SD 的劇本全部接上](part-08-synthesis/ch-39-capstone.md)

### 附錄

- [附錄 A 未來趨勢(2026 ↔ 2030)](annex-a-future-trends.md)
- [附錄 B 工具速查](annex-b-tooling.md)
- [附錄 C 參考書單](annex-c-bibliography.md)
- [附錄 D 案例索引(43 個虛構案例)](annex-d-case-index.md)
- [附錄 E 標準對照(ISO / IEEE / NIST / EU AI Act)](annex-e-standards.md)
- [附錄 F Glossary 全書術語表(280+ 條)](annex-f-glossary.md)
- [附錄 G Citations 引用登記(316+ 條)](annex-g-citations.md)

### 寫作框架

- [Voice Guide 寫作風格守則](voice-guide.md)
- [Conventions 章節格式規範](conventions.md)

---

## 三層讀者建議路徑

| 讀者 | 建議路徑 | 預期收穫 |
|---|---|---|
| **新手(0–2 年)** | I → II → III(跳過補章 F)→ Ch 39 Capstone | 完整需求拆解、模型語言、設計原則,最小可帶走 artifact 套件 |
| **進階(3–8 年)** | 上面 + IV → V → VI + 補章 A(若有 OT)、E(若有合規) | 進階架構、品質屬性、現代工程實踐;能設計中型系統 |
| **資深 / 架構師(8+)** | 全書 + 重點 IV / VI / VII + 全部補章 | AI 時代 SA/SD 整合視角、可帶領團隊建立 Capstone Pack |

詳見 [front-matter/01-reader-guide.md](front-matter/01-reader-guide.md)。

---

## 寫作原則速覽(Voice Arc)

四段式 × 四種語氣:**冷觀察(TENSE)→ 真問題(STEADY)→ 決策框架(COACHING)→ 踩坑+交付(CONSTRUCTIVE)**。詳見 [voice-guide.md](voice-guide.md)。

---

## 全書統計

- **總篇數**:41 篇(39 主章 + 6 補章 + Ch 39 Capstone)
- **總字元**:約 137 萬(中文約 84 萬字)
- **平均每章**:~28,000 字元
- **可帶走 artifact**:45 份(每章一頁式模板)
- **虛構案例**:43 個(fintech / ecommerce / saas / healthcare / energy 五領域均衡)
- **術語**:280+ 條([附錄 F](annex-f-glossary.md))
- **引用**:316+ 條([附錄 G](annex-g-citations.md))
- **Mermaid 圖**:~115 張
