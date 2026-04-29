---
chapter: B
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
| Structurizr DSL | C4 Model 主示範工具 | [Ch 19](part-04-architecture/ch-19-c4-model-visualization.md) |
| PlantUML | 傳統 UML 圖 | [Ch 5](part-01-foundations/ch-05-uml-overview.md) |
| IcePanel | 互動式 C4 | Ch 19 |
| Eraser / Lucid / Excalidraw | 共筆白板 | Ch 5、Ch 19 |
| Miro / FigJam | Event Storming 工作坊 | [Ch 18](part-04-architecture/ch-18-event-storming-modeling.md) |
| EventCatalog | 事件文件化 | Ch 18 |

## 2. 訊息 / 事件

| 工具 | 角色 | 出現章節 |
|---|---|---|
| Apache Kafka | 主流 broker、partition + log 模型 | [Ch 22](part-04-architecture/ch-22-event-driven-cqrs-es.md) |
| Redpanda | Kafka API 相容、單 binary 易運維 | Ch 22 |
| NATS JetStream | 觀測性 / replay 強 | Ch 22、[補章 A](part-04-architecture/chA-edge-ot-it.md) |
| Apache Pulsar | 多租戶優勢 | Ch 22 |
| RabbitMQ | classic queue 場景 | Ch 22 |
| Sparkplug B | OT/IT 邊界狀態協定 | 補章 A |
| AsyncAPI 3.0 | 訊息式 API 規範 | [Ch 14](part-03-design/ch-14-api-design.md) |
| Confluent Schema Registry | 事件 schema 演進 | Ch 18、Ch 22 |
| OpenLineage | 資料血緣機讀格式 | [Ch 6](part-02-analysis/ch-06-dfd-structured-analysis.md) |

## 3. 資料庫 / 儲存

| 工具 | 角色 | 出現章節 |
|---|---|---|
| PostgreSQL 17 | 預設 RDBMS,本書多次倡議 | [Ch 8](part-02-analysis/ch-08-data-modeling-normalization.md)、[Ch 15](part-03-design/ch-15-data-storage.md) |
| pgvector | PG 向量 extension,RAG 推薦 | Ch 15、[Ch 35](part-07-ai-era/ch-35-rag-memory-tool.md)、[補章 E](part-05-quality/chE-compliance.md) |
| TimescaleDB | 時序 hypertable + continuous aggregate | Ch 15 |
| CockroachDB / TiDB | NewSQL | Ch 15 |
| Cassandra | 寫密集 wide column | Ch 15 |
| Neo4j | Graph | Ch 15 |
| Qdrant / Weaviate / Milvus / ChromaDB | 向量 DB | Ch 15、Ch 35 |
| Apache Iceberg / Delta Lake / Apache Hudi | Lakehouse 三大格式 | [Ch 28](part-05-quality/ch-28-data-architecture.md) |
| Databricks Lakebase | 統一儲存層(2026) | Ch 15、Ch 28 |

## 4. 容器 / 編排

| 工具 | 角色 | 出現章節 |
|---|---|---|
| Docker / containerd | OCI 容器 | [Ch 23](part-04-architecture/ch-23-cloud-native-kubernetes.md) |
| Kubernetes 1.30 / 1.31 | 編排 | Ch 23 |
| Helm / Kustomize | 部署 | Ch 23、[Ch 29](part-06-engineering/ch-29-platform-engineering-idp.md) |
| ArgoCD / Flux | GitOps | Ch 23、Ch 29 |
| Knative | Serverless on K8s | Ch 23 |
| wasmCloud / SpinKube | WebAssembly + K8s | Ch 23 |
| Render / Fly.io / Railway | PaaS 復興 | Ch 23 |

## 5. Service Mesh / API Gateway

| 工具 | 角色 | 出現章節 |
|---|---|---|
| Istio Ambient | sidecar-less,2026 主流 | [Ch 24](part-04-architecture/ch-24-service-mesh-cell-based.md) |
| Linkerd 2.16 | Rust micro-proxy | Ch 24 |
| Cilium Service Mesh | eBPF | Ch 24 |
| Consul Connect | HashiCorp 整合 | Ch 24 |
| Kong / APISIX / Gloo | API Gateway | Ch 24 |

## 6. 觀測性

| 工具 | 角色 | 出現章節 |
|---|---|---|
| OpenTelemetry 1.x | 三大支柱事實標準 | [Ch 26](part-05-quality/ch-26-observability-otel.md) |
| Grafana LGTM Stack | Loki / Grafana / Tempo / Mimir | Ch 26 |
| SigNoz / Honeycomb / Dash0 | APM | Ch 26 |
| LangSmith / Langfuse / Phoenix | AI Agent observability | Ch 26、[Ch 33](part-07-ai-era/ch-33-ai-native-architecture.md)、[Ch 38](part-07-ai-era/ch-38-ai-eval-drift-redteam.md) |
| Prometheus 2.55 + Sloth | SLO recording rule | [Ch 27](part-05-quality/ch-27-sre-slo-chaos.md) |

## 7. 架構治理 / Fitness Function

| 工具 | 角色 | 出現章節 |
|---|---|---|
| ArchUnit | Java 架構規則 | [Ch 11](part-03-design/ch-11-architecture-principles.md)、[Ch 20](part-04-architecture/ch-20-modular-monolith.md)、[Ch 31](part-06-engineering/ch-31-fitness-functions.md) |
| NetArchTest | .NET 架構規則 | [Ch 13](part-03-design/ch-13-architecture-styles.md)、Ch 31 |
| Konsist | Kotlin 架構規則 | Ch 31 |
| Spring Modulith 1.4 | Java Modular Monolith | Ch 20、Ch 31 |
| Shopify Packwerk | Ruby Modular Monolith | Ch 20、Ch 31 |
| jMolecules | DDD 註解 | Ch 20 |
| Spectral | OpenAPI / AsyncAPI linter | Ch 14、Ch 31 |
| Pact | 契約測試 | Ch 14、[Ch 21](part-04-architecture/ch-21-microservices.md)、Ch 31 |
| Buf | Protobuf 治理 | Ch 31 |
| OPA + Conftest | Policy as code | Ch 31 |
| Trivy / Grype | SBOM / vuln scan | [Ch 25](part-05-quality/ch-25-security-by-design.md)、Ch 31 |

## 8. AI / Agent

| 工具 | 角色 | 出現章節 |
|---|---|---|
| Claude Sonnet / Opus 4.x | LLM(本書多處用) | 全書 VII 篇 |
| Anthropic Skills + Subagents | CDE 三層 | [Ch 34](part-07-ai-era/ch-34-context-driven-engineering.md)、[Ch 36](part-07-ai-era/ch-36-multi-agent.md) |
| LangGraph | Stateful agent 編排 | Ch 33、Ch 36 |
| Microsoft AutoGen | 對話式 Multi-Agent | Ch 36 |
| CrewAI | Role-based Multi-Agent | Ch 36 |
| OpenAI Agents SDK | Agent + Handoff + Guardrail | Ch 36 |
| Microsoft Magentic-One | 預訓練 Specialized Agents | Ch 36 |
| Cohere Rerank v3 | RAG reranking | [Ch 35](part-07-ai-era/ch-35-rag-memory-tool.md) |
| RAGAS / TruLens / DeepEval | RAG / LLM eval | Ch 38、[補章 B](part-07-ai-era/chB-agentic-qa.md) |
| PyRIT / garak / Promptfoo / Lakera | Red Team | Ch 38、補章 B |
| Constitutional Classifiers (Anthropic) | Prompt injection 防護 | Ch 38 |

## 9. AI Coding Agent

| 工具 | 角色 | 出現章節 |
|---|---|---|
| Cursor | IDE-based Agent | [Ch 34](part-07-ai-era/ch-34-context-driven-engineering.md)、[Ch 37](part-07-ai-era/ch-37-coding-agent.md) |
| Anthropic Claude Code | Terminal Agent + Skills + Subagents | Ch 34、Ch 37、[補章 C](part-07-ai-era/chC-legacy-ai.md) |
| Google Antigravity | 200 萬 token 全景考古 | 補章 C |
| GitHub Copilot Workspace | PR 流程整合 | Ch 37 |
| Aider | git-native | 補章 C |
| CodeRabbit / Greptile / Sweep | PR Review Bot | Ch 37 |

## 10. FinOps / Green / 治理

| 工具 | 角色 | 出現章節 |
|---|---|---|
| Kubecost | K8s cost | [Ch 32](part-06-engineering/ch-32-finops-green-software.md) |
| Vantage / Holori | 雲成本平台 | Ch 32 |
| AWS Customer Carbon Footprint Tool | 雲端碳排 | Ch 32 |
| Electricity Maps / WattTime | Carbon-aware API | Ch 32 |
| Anthropic Prompt Caching | LLM 成本控制 | Ch 32 |
| Backstage / Port / Cortex | IDP 平台 | [Ch 29](part-06-engineering/ch-29-platform-engineering-idp.md) |

## 11. 安全 / 合規

| 工具 | 角色 | 出現章節 |
|---|---|---|
| HashiCorp Vault / AWS KMS / SOPS / Sealed Secrets | Secrets 管理 | Ch 25 |
| SLSA / Sigstore | 供應鏈安全 | Ch 25 |
| SPIFFE / SPIRE | Workload Identity | Ch 25 |
| OWASP LLM Top 10(2024 / 2025) | AI 安全分類 | Ch 25、Ch 38 |

---

每章末尾的 ✅ 修正方向都會具體點出工具選擇,本附錄只做總覽與快速回查。
