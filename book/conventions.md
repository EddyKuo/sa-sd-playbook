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
