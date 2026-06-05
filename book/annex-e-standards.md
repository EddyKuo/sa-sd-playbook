---
chapter: 28
part: annex
title: 附錄 E — 標準對照
slug: standards
status: published
---

# 附錄 E|標準對照(ISO / IEEE / NIST / EU AI Act / 業界標準)

> 本附錄整理全書出現的標準、規格、與法規,提供讀者在實際合約 / 稽核 / 合規評估中查照。**不是法律意見**,實際適用以官方文本為準。

---

## 1. 軟體工程標準

| 標準 | 範疇 | 出現章節 |
|---|---|---|
| **ISO/IEC/IEEE 29148:2018** | Requirements engineering | [Ch 4](part-01-foundations/ch-04-requirements-engineering.md)、[Ch 10](part-02-analysis/ch-10-spec-documents.md) |
| **IEEE Std 830-1998** | SRS(已被 29148 取代,但仍流通) | Ch 4、Ch 10 |
| **ISO/IEC 25010** | 軟體品質模型 | [Ch 27–28](part-05-quality/) |
| **ISO 9241-210:2019** | Human-centred design for interactive systems | [Ch 16](part-03-design/ch-16-uiux-system-view.md) |
| **W3C WCAG 2.2** | Web Content Accessibility Guidelines | Ch 16 |

## 2. 模型語言 / 圖表標準

| 標準 | 範疇 | 出現章節 |
|---|---|---|
| **OMG UML 2.5.1** | Unified Modeling Language | [Ch 5](part-01-foundations/ch-05-uml-overview.md) |
| **OMG BPMN 2.0.2** | Business Process Model and Notation | [Ch 9](part-02-analysis/ch-09-process-modeling.md) |
| **OMG DMN 1.4** | Decision Model and Notation | Ch 9 |
| **C4 Model** | 架構視覺化(社群事實標準) | [Ch 20](part-04-architecture/ch-20-c4-model-visualization.md) |
| **The Open Group ArchiMate 3.2** | 企業架構建模 | Ch 5 |

## 3. API / 訊息標準

| 標準 | 範疇 | 出現章節 |
|---|---|---|
| **OpenAPI 3.1** | REST API 規範 | [Ch 14](part-03-design/ch-14-api-design.md)、[Ch 34](part-06-engineering/ch-34-fitness-functions.md) |
| **AsyncAPI 3.0** | 訊息式 API 規範 | Ch 14、[Ch 19](part-04-architecture/ch-19-event-storming-modeling.md)、[Ch 23](part-04-architecture/ch-23-event-driven-cqrs-es.md) |
| **GraphQL Specification** | Query language(Linux Foundation) | Ch 14 |
| **gRPC + Protocol Buffers** | RPC 框架(CNCF) | Ch 14 |
| **W3C Trace Context** | 分散式追蹤標頭 | [Ch 29](part-05-quality/ch-29-observability-otel.md) |
| **CNCF OpenTelemetry Specification 1.x** | 三大支柱 | Ch 29 |
| **OpenLineage Specification** | 資料血緣機讀格式 | [Ch 6](part-02-analysis/ch-06-dfd-structured-analysis.md) |

## 4. 資料 / 識別碼標準

| 標準 | 範疇 | 出現章節 |
|---|---|---|
| **IETF RFC 9562**(2024)| UUIDv6 / v7 / v8 | [Ch 8](part-02-analysis/ch-08-data-modeling-normalization.md) |
| **ISO 8583:2003** | 卡組織交易訊息(fintech) | [Ch 6](part-02-analysis/ch-06-dfd-structured-analysis.md)、[Ch 11](part-03-design/ch-11-architecture-principles.md)、Ch 23 |
| **EMVCo EMV 3-D Secure v2.2.0** | 支付認證(fintech) | Ch 6 |
| **HL7 v2.5.1 ADT + FHIR R4** | 醫療資訊整合 | [Ch 8](part-02-analysis/ch-08-data-modeling-normalization.md)、[Ch 13](part-03-design/ch-13-architecture-styles.md)、[Ch 37](part-07-ai-era/ch-37-ai-native-architecture.md) |
| **WHO ICD-10-CM**(2025–2026)| 疾病分類 | Ch 8 |

## 5. 安全 / 隱私 / 合規

### 安全標準
| 標準 | 範疇 | 出現章節 |
|---|---|---|
| **NIST SP 800-207** | Zero Trust Architecture | [Ch 27](part-05-quality/ch-27-security-by-design.md) |
| **NIST FIPS 203 / 204 / 205**(2024)| Post-Quantum Cryptography | Ch 27 |
| **OWASP Top 10**(Web 2021、API 2023、LLM 2024 / 2025)| Web / API / LLM 安全 | Ch 27、[Ch 45](part-07-ai-era/ch-45-ai-eval-drift-redteam.md) |
| **SLSA Framework** | Supply Chain Security | Ch 27 |
| **Sigstore** | 軟體簽名 | Ch 27 |
| **SPIFFE / SPIRE** | Workload Identity | Ch 27 |

### 隱私 / 合規法規
| 法規 | 範疇 | 出現章節 |
|---|---|---|
| **EU GDPR**(2018)| 個資保護 / DPIA Art. 35 | [Ch 28](part-05-quality/ch-28-compliance.md) |
| **EU AI Act**(2024,Annex III 高風險系統 2026/8/2 全面執行)| AI 系統合規 | [Ch 37](part-07-ai-era/ch-37-ai-native-architecture.md)、Ch 28 |
| **HIPAA** | 醫療資訊隱私(美國) | Ch 28 |
| **PCI DSS v4.0**(March 2022)| 卡資料安全(fintech) | [Ch 6](part-02-analysis/ch-06-dfd-structured-analysis.md)、Ch 27 |
| **SOC 2 Type I / II** | 服務組織控制 | Ch 28、[Ch 33](part-06-engineering/ch-33-adr-architecture-knowledge.md) |
| **個資法 / 個人資料保護法**(台灣)| 本國個資 | Ch 28 |
| **新加坡 PDPA / MAS Notices** | 金融與個資 | Ch 44、Ch 28 |

### AI 治理
| 標準 | 範疇 | 出現章節 |
|---|---|---|
| **ISO/IEC 42001:2023** | AI Management System(AIMS) | Ch 28 |
| **NIST AI Risk Management Framework**(2023+) | AI 風險管理 | Ch 28 |
| **EU AI Act Annex IV** | 高風險系統技術文件(9 大類) | Ch 28 |

## 6. 工業 / 控制系統 / 能源

| 標準 | 範疇 | 出現章節 |
|---|---|---|
| **IEC 62443** | 工業自動化與控制系統(IACS)資安 | [Ch 26](part-04-architecture/ch-26-edge-ot-it.md)、Ch 28 |
| **IEC 61850** | 變電站自動化通訊 | Ch 26、[Ch 25](part-04-architecture/ch-25-service-mesh-cell-based.md) |
| **IEC 60870-5-104** | 遠端控制系統通訊 | Ch 25 |
| **Modbus / Modbus-over-TCP** | 工業協定 | Ch 26、[Ch 15](part-03-design/ch-15-data-storage.md) |
| **SunSpec Alliance Specs** | 太陽能逆變器標準 | Ch 15 |
| **Eclipse Sparkplug B** | OT/IT 邊界狀態協定 | Ch 26 |

## 7. ESG / 永續

| 標準 | 範疇 | 出現章節 |
|---|---|---|
| **ISO/IEC 21031:2024** | Software Carbon Intensity (SCI) | [Ch 35](part-06-engineering/ch-35-finops-green-software.md) |
| **Green Software Foundation Principles** | 三原則(Carbon Awareness / Efficiency / Hardware Efficiency) | Ch 35 |
| **EU CSRD**(2024 起) | 企業永續報告指令 | Ch 35 |
| **ISSB IFRS S2** | 氣候相關財務揭露 | Ch 35 |

## 8. 可逆性 / Migration

| 標準 / 模式 | 範疇 | 出現章節 |
|---|---|---|
| **Strangler Fig Pattern**(Martin Fowler 2004)| 漸進遷移策略 | [Ch 21](part-04-architecture/ch-21-modular-monolith.md)、[Ch 47](part-07-ai-era/ch-47-legacy-ai.md) |
| **Expand-Contract Migration** | Schema 演進不停機 | Ch 8 |

---

## 主要法規時程一覽(2024–2030)

| 日期 | 事件 | 影響 |
|---|---|---|
| 2024-08-01 | EU AI Act 部分生效(禁用 AI 行為) | Ch 28 |
| 2024-Q4 | NIST FIPS 203/204/205 PQC 標準化 | Ch 27 |
| **2026-08-02** | **EU AI Act Annex III 高風險系統全面執行** | Ch 36、Ch 28 |
| 2027(預估) | 大型企業合約開始要求 SCI 報告 | Ch 35 |
| 2030(預估) | 美國聯邦強制 PQC 過渡完成 | Ch 27 |

---

法規條文的最新版本以官方公告為準(EU AI Act 見 europa.eu;NIST 見 nist.gov;OWASP 見 owasp.org)。
