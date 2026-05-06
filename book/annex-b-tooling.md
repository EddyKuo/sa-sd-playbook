---
chapter: 45
part: annex
title: 附錄 B — 工具速查(2026)
slug: tooling
status: published
---

# 附錄 B|工具速查(2026)

> 全書出現過的工具,按章節整理。**不是推薦清單,是出現過的清單**。版本與態度以 2026 年現場為準。

---

## 1. 圖表 / 視覺化

| 工具 | 用途 | 出現章節 |
|---|---|---|
| Mermaid | Diagrams as Code(本書預設) | 全書 |
| Structurizr DSL | C4 Model 主示範工具 | [Ch 20](part-04-architecture/ch-20-c4-model-visualization.md) |
| PlantUML | 傳統 UML 圖 | [Ch 5](part-01-foundations/ch-05-uml-overview.md) |
| IcePanel | 互動式 C4 | Ch 20 |
| Eraser / Lucid / Excalidraw | 共筆白板 | Ch 5、Ch 20 |
| Miro / FigJam | Event Storming 工作坊 | [Ch 19](part-04-architecture/ch-19-event-storming-modeling.md) |
| EventCatalog | 事件文件化 | Ch 19 |

## 2. 訊息 / 事件

| 工具 | 角色 | 出現章節 |
|---|---|---|
| Apache Kafka | 主流 broker、partition + log 模型 | [Ch 23](part-04-architecture/ch-23-event-driven-cqrs-es.md) |
| Redpanda | Kafka API 相容、單 binary 易運維 | Ch 23 |
| NATS JetStream | 觀測性 / replay 強 | Ch 23、[Ch 26](part-04-architecture/ch-26-edge-ot-it.md) |
| Apache Pulsar | 多租戶優勢 | Ch 23 |
| RabbitMQ | classic queue 場景 | Ch 23 |
| Sparkplug B | OT/IT 邊界狀態協定 | Ch 26 |
| AsyncAPI 3.0 | 訊息式 API 規範 | [Ch 14](part-03-design/ch-14-api-design.md) |
| Confluent Schema Registry | 事件 schema 演進 | Ch 19、Ch 23 |
| OpenLineage | 資料血緣機讀格式 | [Ch 6](part-02-analysis/ch-06-dfd-structured-analysis.md) |

## 3. 資料庫 / 儲存

| 工具 | 角色 | 出現章節 |
|---|---|---|
| PostgreSQL 17 | 預設 RDBMS,本書多次倡議 | [Ch 8](part-02-analysis/ch-08-data-modeling-normalization.md)、[Ch 15](part-03-design/ch-15-data-storage.md) |
| pgvector | PG 向量 extension,RAG 推薦 | Ch 15、[Ch 38](part-07-ai-era/ch-38-rag-memory-tool.md)、[Ch 28](part-05-quality/ch-28-compliance.md) |
| TimescaleDB | 時序 hypertable + continuous aggregate | Ch 15 |
| CockroachDB / TiDB | NewSQL | Ch 15 |
| Cassandra | 寫密集 wide column | Ch 15 |
| Neo4j | Graph | Ch 15 |
| Qdrant / Weaviate / Milvus / ChromaDB | 向量 DB | Ch 15、Ch 38 |
| Apache Iceberg / Delta Lake / Apache Hudi | Lakehouse 三大格式 | [Ch 31](part-05-quality/ch-31-data-architecture.md) |
| Databricks Lakebase | 統一儲存層(2026) | Ch 15、Ch 31 |

## 4. 容器 / 編排

| 工具 | 角色 | 出現章節 |
|---|---|---|
| Docker / containerd | OCI 容器 | [Ch 24](part-04-architecture/ch-24-cloud-native-kubernetes.md) |
| Kubernetes 1.30 / 1.31 | 編排 | Ch 24 |
| Helm / Kustomize | 部署 | Ch 24、[Ch 32](part-06-engineering/ch-32-platform-engineering-idp.md) |
| ArgoCD / Flux | GitOps | Ch 24、Ch 32 |
| Knative | Serverless on K8s | Ch 24 |
| wasmCloud / SpinKube | WebAssembly + K8s | Ch 24 |
| Render / Fly.io / Railway | PaaS 復興 | Ch 24 |

## 5. Service Mesh / API Gateway

| 工具 | 角色 | 出現章節 |
|---|---|---|
| Istio Ambient | sidecar-less,2026 主流 | [Ch 25](part-04-architecture/ch-25-service-mesh-cell-based.md) |
| Linkerd 2.16 | Rust micro-proxy | Ch 25 |
| Cilium Service Mesh | eBPF | Ch 25 |
| Consul Connect | HashiCorp 整合 | Ch 25 |
| Kong / APISIX / Gloo | API Gateway | Ch 25 |

## 6. 觀測性

| 工具 | 角色 | 出現章節 |
|---|---|---|
| OpenTelemetry 1.x | 三大支柱事實標準 | [Ch 29](part-05-quality/ch-29-observability-otel.md) |
| Grafana LGTM Stack | Loki / Grafana / Tempo / Mimir | Ch 29 |
| SigNoz / Honeycomb / Dash0 | APM | Ch 29 |
| LangSmith / Langfuse / Phoenix | AI Agent observability | Ch 29、[Ch 36](part-07-ai-era/ch-36-ai-native-architecture.md)、[Ch 44](part-07-ai-era/ch-44-ai-eval-drift-redteam.md) |
| Prometheus 2.55 + Sloth | SLO recording rule | [Ch 30](part-05-quality/ch-30-sre-slo-chaos.md) |

## 7. 架構治理 / Fitness Function

| 工具 | 角色 | 出現章節 |
|---|---|---|
| ArchUnit | Java 架構規則 | [Ch 11](part-03-design/ch-11-architecture-principles.md)、[Ch 21](part-04-architecture/ch-21-modular-monolith.md)、[Ch 34](part-06-engineering/ch-34-fitness-functions.md) |
| NetArchTest | .NET 架構規則 | [Ch 13](part-03-design/ch-13-architecture-styles.md)、Ch 34 |
| Konsist | Kotlin 架構規則 | Ch 34 |
| Spring Modulith 1.4 | Java Modular Monolith | Ch 21、Ch 34 |
| Shopify Packwerk | Ruby Modular Monolith | Ch 21、Ch 34 |
| jMolecules | DDD 註解 | Ch 21 |
| Spectral | OpenAPI / AsyncAPI linter | Ch 14、Ch 34 |
| Pact | 契約測試 | Ch 14、[Ch 22](part-04-architecture/ch-22-microservices.md)、Ch 34 |
| Buf | Protobuf 治理 | Ch 34 |
| OPA + Conftest | Policy as code | Ch 34 |
| Trivy / Grype | SBOM / vuln scan | [Ch 27](part-05-quality/ch-27-security-by-design.md)、Ch 34 |

## 8. AI / Agent

| 工具 | 角色 | 出現章節 |
|---|---|---|
| Claude Sonnet / Opus 4.x | LLM(本書多處用) | 全書 VII 篇 |
| Anthropic Skills + Subagents | CDE 三層 | [Ch 37](part-07-ai-era/ch-37-context-driven-engineering.md)、[Ch 39](part-07-ai-era/ch-39-multi-agent.md) |
| LangGraph | Stateful agent 編排 | Ch 36、Ch 39 |
| Microsoft AutoGen | 對話式 Multi-Agent | Ch 39 |
| CrewAI | Role-based Multi-Agent | Ch 39 |
| OpenAI Agents SDK | Agent + Handoff + Guardrail | Ch 39 |
| Microsoft Magentic-One | 預訓練 Specialized Agents | Ch 39 |
| Cohere Rerank v3 | RAG reranking | [Ch 38](part-07-ai-era/ch-38-rag-memory-tool.md) |
| RAGAS / TruLens / DeepEval | RAG / LLM eval | Ch 44、[Ch 45](part-07-ai-era/ch-45-agentic-qa.md) |
| PyRIT / garak / Promptfoo / Lakera | Red Team | Ch 44、Ch 45 |
| Constitutional Classifiers (Anthropic) | Prompt injection 防護 | Ch 44 |

## 9. AI Coding Agent

| 工具 | 角色 | 出現章節 |
|---|---|---|
| Cursor | IDE-based Agent | [Ch 37](part-07-ai-era/ch-37-context-driven-engineering.md)、[Ch 43](part-07-ai-era/ch-43-coding-agent.md) |
| Anthropic Claude Code | Terminal Agent + Skills + Subagents | Ch 37、Ch 43、[Ch 46](part-07-ai-era/ch-46-legacy-ai.md) |
| Google Antigravity | 200 萬 token 全景考古 | Ch 46 |
| GitHub Copilot Workspace | PR 流程整合 | Ch 43 |
| Aider | git-native | Ch 46 |
| CodeRabbit / Greptile / Sweep | PR Review Bot | Ch 43 |

## 10. FinOps / Green / 治理

| 工具 | 角色 | 出現章節 |
|---|---|---|
| Kubecost | K8s cost | [Ch 35](part-06-engineering/ch-35-finops-green-software.md) |
| Vantage / Holori | 雲成本平台 | Ch 35 |
| AWS Customer Carbon Footprint Tool | 雲端碳排 | Ch 35 |
| Electricity Maps / WattTime | Carbon-aware API | Ch 35 |
| Anthropic Prompt Caching | LLM 成本控制 | Ch 35 |
| Backstage / Port / Cortex | IDP 平台 | [Ch 32](part-06-engineering/ch-32-platform-engineering-idp.md) |

## 11. 安全 / 合規

| 工具 | 角色 | 出現章節 |
|---|---|---|
| HashiCorp Vault / AWS KMS / SOPS / Sealed Secrets | Secrets 管理 | Ch 27 |
| SLSA / Sigstore | 供應鏈安全 | Ch 27 |
| SPIFFE / SPIRE | Workload Identity | Ch 27 |
| OWASP LLM Top 10(2024 / 2025) | AI 安全分類 | Ch 27、Ch 44 |

---

每章末尾的 ✅ 修正方向都會具體點出工具選擇,本附錄只做總覽與快速回查。
