---
chapter: 26
part: annex
title: 附錄 A — 未來趨勢(2026 ↔ 2030)
slug: future-trends
status: published
---

# 附錄 A|未來趨勢 — 2026 至 2030 的 SA/SD 看點

> 本書定錨於 2026 年。本附錄列出未來 4 年內可能影響 SA/SD 實踐的方向。**不是預測,是提醒**:當這些事情發生,本書的哪些章節需要重新評估。

---

## 1. AI 系統側

### 1.1 1M / 10M 長上下文常態化(2025–2027)

- Anthropic Claude 的 1M context、Google Gemini 2.5 Pro 的 2M context 已上線(2025)
- 2027 預期 10M context 規模、價格降至 1/10
- **影響章節**:[Ch 38](part-07-ai-era/ch-38-rag-memory-tool.md) RAG vs long context 的角色重劃;[Ch 45](part-07-ai-era/ch-45-agentic-qa.md) Eval Set 規模需擴大

### 1.2 Agent 操作系統(Agent OS)成為部署單位(2026–2028)

- LangGraph、Anthropic Sub-agents、OpenAI Agents SDK、Microsoft Magentic-One 都朝「Agent 操作系統」演化
- 預期 2027–2028 出現「Agent OS as a Platform」(類比 K8s 之於容器)
- **影響章節**:[Ch 24](part-04-architecture/ch-24-cloud-native-kubernetes.md)、[Ch 32](part-06-engineering/ch-32-platform-engineering-idp.md)、[Ch 39](part-07-ai-era/ch-39-multi-agent.md)

### 1.3 Constitutional Classifiers / Self-checking Agent 主流化(2026+)

- Anthropic 2026 提出的 Constitutional Classifiers 將推動「Agent 自帶安全護欄」
- 預期成為合規基準(EU AI Act 高風險系統的 Art. 15 量化指標)
- **影響章節**:[Ch 27](part-05-quality/ch-27-security-by-design.md)、[Ch 44](part-07-ai-era/ch-44-ai-eval-drift-redteam.md)、[Ch 45](part-07-ai-era/ch-45-agentic-qa.md)、[Ch 28](part-05-quality/ch-28-compliance.md)

## 2. 架構側

### 2.1 Modular Monolith 成為新建系統預設(2026 已成立)

- CNCF 2026 Q1、Sam Newman 2026 公開立場、Shopify 30TB/min monolith 案例已是現況
- 預期 2027–2028 微服務從 Adopt 降到 Trial,Modular Monolith 成為主流
- **影響章節**:[Ch 21](part-04-architecture/ch-21-modular-monolith.md)、[Ch 22](part-04-architecture/ch-22-microservices.md)

### 2.2 Cell-Based 取代 Service Mesh 成為大規模預設(2027+)

- AWS 2026 Well-Architected Framework 已把 Cell-Based 列為超大規模預設
- Slack / Stripe / Cloudflare 都在 2024–2026 完成或進行中遷移
- **影響章節**:[Ch 25](part-04-architecture/ch-25-service-mesh-cell-based.md)、[Ch 26](part-04-architecture/ch-26-edge-ot-it.md)

### 2.3 Lakebase / 統一儲存層(2026–2028)

- Databricks 2026 Lakebase 整合 OLTP / OLAP / Vector
- 預期 2027–2028 出現多家 Lakebase 競爭者(Snowflake、Microsoft Fabric)
- **影響章節**:[Ch 15](part-03-design/ch-15-data-storage.md)、[Ch 31](part-05-quality/ch-31-data-architecture.md)

## 3. 工程實踐側

### 3.1 Platform Engineering 與 IDP 標準化(2025–2027)

- Backstage、Port、Cortex 在 2026 已成熟
- 預期 2027 出現「Open IDP Spec」(類比 OCI 之於容器)
- **影響章節**:[Ch 32](part-06-engineering/ch-32-platform-engineering-idp.md)

### 3.2 ADR 與 Skill 連動成為 CI 標準(2026–2027)

- ManoMano、Brevo 等公司在 2026 已把 ADR 變成 AI Pair-Programmer 的 Skill 知識來源
- 預期 2027 出現主流工具支援(Backstage Skill plugin、Cursor / Claude Code 原生整合)
- **影響章節**:[Ch 33](part-06-engineering/ch-33-adr-architecture-knowledge.md)、[Ch 37](part-07-ai-era/ch-37-context-driven-engineering.md)

### 3.3 Carbon-Aware Computing 進合規(2026–2028)

- EU CSRD 2024 起、ISSB IFRS S2 2024 起、ISO/IEC 21031 SCI 2024 已生效
- 預期 2027–2028 大型企業合約要求 SCI 報告(類似 SOC 2)
- **影響章節**:[Ch 35](part-06-engineering/ch-35-finops-green-software.md)

## 4. 合規 / 治理側

### 4.1 EU AI Act 全面執行(2026/8/2)

- 高風險 AI 系統 Annex III 全面執行
- 預期 2027 出現第一波罰則案例(估計 35M 歐元 / 全球 7%)
- **影響章節**:[Ch 27](part-05-quality/ch-27-security-by-design.md)、[Ch 36](part-07-ai-era/ch-36-ai-native-architecture.md)、[Ch 28](part-05-quality/ch-28-compliance.md)

### 4.2 Post-Quantum Cryptography 強制過渡(2026–2030)

- NIST FIPS 203/204/205 2024 標準化
- 預期 2026–2030 出現「強制 PQC 過渡期」(美國聯邦 2030、金融業 2027–2029)
- **影響章節**:[Ch 27](part-05-quality/ch-27-security-by-design.md)、[Ch 28](part-05-quality/ch-28-compliance.md)

## 5. 觀察建議

下一輪本書改版時(預估 2028 / 2030),最可能需要重寫的章節:

1. **[Ch 38 RAG / Memory / Tool](part-07-ai-era/ch-38-rag-memory-tool.md)** ⸺ long context vs RAG 的角色可能再次反轉
2. **[Ch 22 微服務](part-04-architecture/ch-22-microservices.md)** ⸺ 可能從「Adopt」降到「Hold」
3. **[Ch 25 Service Mesh / Cell](part-04-architecture/ch-25-service-mesh-cell-based.md)** ⸺ Mesh 在小規模可能完全消失
4. **[Ch 36 AI-Native](part-07-ai-era/ch-36-ai-native-architecture.md)** ⸺ 七層架構可能重新整理

---

讀者可在 Ch 1 提到的「6 個月後再看」原則上,把這份附錄當作每半年的回頭檢驗清單。
