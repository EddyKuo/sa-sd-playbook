# Conventions — 章節格式與 cross-ref 規範

> 補充 `voice-guide.md` 的格式細節。所有章節 / 附錄 / 補章一律遵守。

---

## 1. 檔案命名

- **主章**:`part-{NN}-{slug}/ch-{NN}-{kebab-slug}.md`(如 `part-04-architecture/ch-18-ddd-strategic-tactical.md`)
- **補章**:對應篇下 `ch{A-F}-{kebab-slug}.md`(如 `part-04-architecture/ch-26-edge-ot-it.md`)
- **附錄**:`annex-{a-g}-{kebab-slug}.md`(如 `annex-f-glossary.md`)
- **Front Matter**:`front-matter/{NN}-{kebab-slug}.md`

## 2. Frontmatter(YAML,章節必填)

```yaml
---
chapter: 1                  # 數字章 / "A"–"F"(補章)/ "F"/"G"(附錄)
part: I                     # I–VIII / annex / front-matter
title: 章節完整標題
slug: kebab-case-slug
agent: SA                   # 主筆角色:PM / SA / RD / DBA / QA / UI/UX / Orchestrator
skills_used:                # 載入的 skills
  - sa/arch-monolith
  - shared/domain-fintech
domain_case: CASE-XXX-NNN   # 主案例 ID(必須在 case-registry.yaml 已註冊)
reviewers: [PM, QA, Orchestrator]
status: draft               # draft / review / approved / migrated
word_count_target: 5500
---
```

## 3. 章首 Cross-Ref Block

緊接 H1 / 副標之後,以 blockquote 形式呈現:

```markdown
> **前置閱讀**:[Ch X 標題](./ch-XX-slug.md)
> **下游章節**:[Ch Y 標題](../part-NN-XXX/ch-YY-slug.md)
> **延伸補章**:[補章 X 標題](./chX-slug.md)
```

## 4. 章末 Cross-References Section

每章末尾必有完整 Cross-References 與引用註腳:

```markdown
## Cross-References

- **下一章**:[Ch X 標題](./ch-XX-slug.md) ⸺ 一句話描述
- **強連結**:[Ch Y 標題](../part-NN-XXX/ch-YY-slug.md)
- **延伸補章**:[補章 X](./chX-slug.md)

## 引用

[^CIT-NNN]: 完整引用條目。詳見 `annex-g-citations.md#cit-nnn`。
```

## 5. 術語連結

章節內第一次出現的關鍵術語,連結到 glossary:

```markdown
[Event Sourcing](../annex-f-glossary.md#event-sourcing) 是…
```

第二次以後不必重複連結。

## 6. Mermaid 樣式

統一三色 classDef:

```
classDef hot fill:#fee,stroke:#c33     # 危險 / 反模式 / 現況的痛點
classDef cold fill:#eef,stroke:#36c    # 中性 / 起始狀態
classDef goal fill:#efe,stroke:#3a3    # 目標 / 推薦做法
```

C4 圖(Ch 20)專用 Structurizr DSL,其他章節一律用 Mermaid。

## 7. 章節內標題層級

- `H1` 章節大標(只出現一次,加 `## ⸺ {副標}` 作為 H2 副標)
- `H2`(`## X.Y 段落`)章節主段(冷觀察 / 真問題 / 決策框架 / 踩坑 / 交付 / Recap)
- `H3`(`### X.Y.Z 子段`)子段
- `H4` 偶用於極細分

## 8. 引用與案例 ID 配置

| 類型 | 命名 | 起始 | 範圍 |
|---|---|---|---|
| Citations | `CIT-NNN` | 001 | Ch X 預留 (X×10)~(X×10+9) |
| Cases | `CASE-{DOMAIN}-NNN` | 001 | DOMAIN 為 FIN/ECM/HCR/SAS/ENR |
| Glossary | `{kebab-anchor}` | — | 章節以 `[term](../annex-f-glossary.md#term-anchor)` 連結 |

## 9. PROPOSED-REFS(章節寫作時用)

新章節在寫作時若引入新 glossary / citations / cases,**不直接編輯共用檔**,在章末附 HTML comment:

```html
<!-- PROPOSED-REFS
glossary:
  - anchor: foo
    name: Foo (中文)
    body: |
      定義...
citations:
  - id: CIT-NNN
    body: "..."
cases:
  - id: CASE-XXX-NNN
    title: "..."
    domain: ...
    chapters: [ch-NN]
    summary: |
      ...
-->
```

由 Orchestrator 在 QA 通過後合併到 `annex-f-glossary.md` / `annex-g-citations.md` / `_refs/case-registry.yaml`,然後刪除 PROPOSED-REFS 區塊。

## 10. 路徑相對規則速查

| 從 | 到 | 路徑 |
|---|---|---|
| `part-NN/ch-XX.md` | 同篇章節 | `./ch-YY-slug.md` |
| `part-NN/ch-XX.md` | 跨篇章節 | `../part-MM-slug/ch-YY-slug.md` |
| `part-NN/ch-XX.md` | 附錄 | `../annex-X-slug.md` |
| `part-NN/ch-XX.md` | front-matter | `../front-matter/NN-slug.md` |
| `book/README.md` | 任何位置 | `front-matter/...`、`part-NN/...`、`annex-X-slug.md`(直接,不加 `./`) |

## 11. 章末 Recap Checklist 格式

```markdown
## X.6 本章交付清單 Recap

讀完本章,你應該已經能做到:

- [ ] {動作 1}
- [ ] {動作 2}
- [ ] {動作 3}
- [ ] {動作 4}

如果先挑一項做,建議是 ⸺{動作 X},理由是 {為什麼這個最值得先做}。
```

## 12. §X.5 交付清單格式 — 模板 + 填好範例 + 欄位註解

每章 §X.5 必須是「**空白模板 + 填好範例**」雙段結構,缺一不可。
只給空白模板會讓讀者第一次接觸時不知道實際長什麼樣;只給填好範例
會讓讀者誤以為是案例分析、不是可重複使用的格式。

### 12.1 結構

```text
## X.5 交付清單 ⸺ 一頁式 {Artifact 名稱} 模板
   ↓
   既有的空白模板 code block(用 `{placeholder}` 形式)
   ↓
   既有的「為什麼是一頁 / 為什麼有 X 欄位」prose 段
   ↓
### X.5.1 範例:{案例名} {動作敘述}
   ↓
   1–2 句 intro,扣回該章故事(故事代價 / 衝突)
   ↓
   填好的範例 code block(以 `<!-- 為什麼這欄:... -->` 標註關鍵欄位)
   ↓
   1–2 句 punchline 收尾(CONSTRUCTIVE 語氣)
```

若該章交付物有多個 artifact(例如 Ch 33 的 ADR 模板 + Index Card),
每個 artifact 後面跟一個自己的範例子段,編號 §X.5.1 / §X.5.3 / ...
中間夾的 §X.5.2 為第二份模板。

### 12.2 範例案例來源

範例必須使用 frontmatter `domain_case:` 欄位指定的案例(該案例已在
`_refs/case-registry.yaml` 註冊,並在章內冷觀察 / 真問題段已鋪陳故事)。
**禁止為了範例新建一個沒在 case-registry 註冊的虛構公司** ⸺ 會讓讀者
記憶負擔暴增、跨章對不起來。

若該章 case 不適合做完整範例(過大或過抽象),可從同 domain 的其他
case 取代,但需在章末 PROPOSED-REFS(見本文件 §9)補註。

### 12.3 欄位註解格式

註解寫在範例 code block 內,以 HTML 註解形式 inline 標註:

```markdown
## 1. Problem(我們在解決什麼)
<!-- 為什麼這欄:逼作者用「誰、做不到什麼、代價多少」三件套寫一句業務問題;
     沒這一句,後面架構決策都會在「我們大概是要做 X 吧」的霧裡。 -->
- 一句話業務問題:...
```

HTML 註解放在 fenced code block 內**視覺可見**(因為 code block 不解析
HTML),讀者複製模板去用時可以選擇保留(當 onboarding 教材)或刪除
(當 production artifact)。

#### 12.3.1 何時加註解

不是每個欄位都加。**只挑「沒寫會吃虧」的關鍵欄位**(通常是模板既有
prose 段已經提到「為什麼有這欄」的那幾個)。一張卡 6–10 個欄位中,
加註解的通常是 3–5 個。

#### 12.3.2 註解語氣(硬規)

| 規則 | 允許 | 禁止 |
|------|------|------|
| 句子長度 | 1–2 句,每句 ≤ 50 字 | 三句以上、長段落 |
| 語氣 | **CONSTRUCTIVE**:後果、設計意圖 | 命令式(「**必須**」「絕對不可」) |
| 抽象度 | 具體後果(「會在霧裡」「會被 partner 重複出貨」) | 抽象大道理(「業界普遍」「眾所周知」) |
| 結尾 | 句號 / 結束於後果 | 警告 / 威脅 |

✅ 範例:
- `<!-- 為什麼這欄:對方是誰、要做什麼,直接決定了 schema 顆粒度與 SLA;寫不出這一欄代表這條 API 還沒準備好對外。 -->`
- `<!-- 為什麼這欄:三年後的人能不能還原當時的氣候,全靠這一欄;寫得太籠統(「當時人手不夠」)等於沒寫。 -->`

❌ 反例:
- `<!-- 此欄為必填,所有 ADR 都必須包含 Context。 -->`(命令式)
- `<!-- 業界普遍認為 Context 很重要。 -->`(抽象大道理)

### 12.4 Intro / Punchline 規則

範例 code block 的前後各一段,把範例扣回章內故事:

- **Intro(1–2 句)**:點出範例與該章衝突的關係。
  例:「HarborGate 第三週開始補卡,第一條補的是 12 萬賠款事故的元凶 ⸺ orders.create」
- **Punchline(1–2 句)**:從範例延伸出可帶走的洞察,語氣 CONSTRUCTIVE。
  例:「寫不出 contract card 的 API,通常是不需要存在的 API。」

兩段都不可以是「最佳實踐」「總結重點」式的教科書腔。

### 12.5 篇幅約束

- 範例 code block 主體控制在 **60 行內**(含註解)
- 加上 intro + punchline,整個 §X.5.1 約 **70–90 行**
- 過長(> 100 行)需拆成 §X.5.1(主範例)+ §X.5.2(次範例)

### 12.6 已通過 pilot 的範本章節

撰寫新章 §X.5 範例時,可參考以下 pilot:

| 章 | Artifact | 案例 |
|---|---|---|
| Ch 1 §1.5.1 | System Charter | PayLoop(`CASE-FIN-001`) |
| Ch 14 §14.5.1 | API Contract Card | HarborGate(`CASE-ECM-004`) |
| Ch 33 §33.5.1 + §33.5.3 | ADR + Index Card | OrbitPay(`CASE-FIN-008`) |
