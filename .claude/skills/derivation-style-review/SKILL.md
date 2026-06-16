---
name: derivation-style-review
description: >-
  使用者（葉品辰）撰寫物理／大氣科學理論推導 .ipynb 的專屬風格標準。當需要 (1) 以此風格審閱／修正
  現有推導 .ipynb，(2) 依此風格新寫一份推導，或 (3) 檢查 knowns/assumptions/definitions
  的編號與 \overset 引用一致性時使用。編輯一律走 Jupytext 草稿紙模式（改配對 .md 再 sync 回 .ipynb，見 §7），
  不直接改 .ipynb JSON。涵蓋 Modern-Physics、Advanced-Atmospheric-Dynamics、
  Typhoon-Dynamics 等課程的推導 notebook。觸發詞：推導風格、審閱推導、已知與假設、overset 引用、
  derivation style、review derivation。
---

# 推導風格審閱 Skill（derivation-style-review）

本 Skill 把使用者獨特的理論推導寫法編成**可執行的規範與檢查清單**。
參考來源：`Modern-Physics/homework/hw9/hw9.ipynb`、`Advanced-Atmospheric-Dynamics/project/project1/project1_1.ipynb`。
可複製的樣板片段見 [reference/templates.md](reference/templates.md)。

風格的靈魂一句話：
> **先把所有 knowns / assumptions / definitions 編號攤開，證明過程只做「引用」；任何一步都能沿 `\overset` 標註回溯到某條卡片或前一子步——可追溯性是這套風格的核心。**

---

## 1. 巨觀文件結構規則（R1）

- **R1.1** 每題分兩個 markdown cell：`## Question N`（原題照錄，英文／LaTeX 原文，**不改寫題目**）→ `## Question N - Answer`。
- **R1.2** Answer 第一個區塊**固定**是前置知識區：標題用 `### 假設與已知 (Assumptions & Preliminaries)`（中英並陳）。先把所有武器擺出來，**之後**才進入實際推導。
- **R1.3** 實際推導小節用動詞性英文標題：`### proof`、`### solve …`、`### (a) proof …`、`### (a) solve …`。
- **R1.4** 大氣類長推導另設獨立 `## 證明` 大段，與前置 preliminaries 分離。**證明段只做引用，不臨時引入新假設**——任何新條件都必須先回到前置區新增一張卡片。

## 2. 前置知識「卡片」格式（R2，核心）

四種粗體標籤，各自獨立流水編號：

| 標籤 | 用途 | 等號寫法 |
|------|------|----------|
| **【已知 N】** | 外部既有定律／公式（大氣檔常附 lecture 超連結） | 一般 `=` |
| **【假設 N】** | 簡化條件（inviscid、isentropic、linear perturbation、hydrostatic、isothermal…） | — |
| **【定義 N】** | 引入新符號（c²、H_s、N²、Γ…） | `\overset{\text{def}}{=}` |
| **【推導 N】** | 供主證明引用的中間結果 | `\overset{依據}{=}` |

每張卡片格式固定（**缺一不可**）：

1. 粗體標籤 + **中文名（English name）** + `：`，可附一句中文說明。
2. display math 公式（`$$ … $$`）。
3. 緊接一條 bullet list，**逐一定義公式中每一個符號**，格式：
   `* $符號$ : 中文名 (English name) $[\text{單位}]$`
   - 無因次寫 `[無單位]`。
   - 物理常數在說明處給近似值，例如 `$k \approx 1.38 \times 10^{-23} \text{ J}\cdot\text{K}^{-1}$`。
4. 子項用 `(a) (b) (c)`，可在標籤後標 `(a)` 並各帶自己的 `gather*`。

完整樣板見 [reference/templates.md](reference/templates.md) §卡片。

## 3. 推導嚴謹度規則（R3 — 逐步、絕不跳步、全程可追溯）

- **R3.1** 多步推導一律用 `$$\begin{gather*} … \end{gather*}$$`，三欄 `&=&`（或 `&\approx&`）對齊。
- **R3.2 （最關鍵）** 每個「有依據」的關鍵等號上方加 `\overset{依據}{=}` 標註，依據文字用 `\text{}` 包裹，格式如：
  `\overset{\text{已知 1(b)}}{=}`、`\overset{\text{假設 3(a)}}{=}`、`\overset{\text{推導 5,6}}{=}`、
  `\overset{\text{定義 4}}{=}`、`\overset{\text{Q4(a)}}{=}`、`\overset{\text{let}}{=}`。
  - 純代數整理（移項、約分）可不標；凡「援用某條卡片或前一子步」就**必須**標。
- **R3.3** 子步驟有層級編號，供後續回引：`Q1.1.3`、`1(a)(b)`、大段證明用 `2a`~`2e`。
- **R3.4** 最終答案用 `\approx` 給數值並**附單位**。代入數值的那一步要把帶單位的量整串寫出（如 `(6.626 \times 10^{-34} \text{ J s})(1.32 \times 10^{14} \text{ s}^{-1})`）。

## 4. 術語 / 符號 / 語言慣例（R4）

- **R4.1 雙語並陳**：中文（English）成對出現，貫穿卡片標籤與符號說明。
- **R4.2** 動詞性小節標題用英文：`proof` / `solve` / `verify`。
- **R4.3** 單位與常數一律 `\text{}` 包裹，單位放 `[ ]`（如 `[\text{m}\cdot\text{s}^{-1}]`）。
- **R4.4** 符號慣例：擾動量加撇號 `p'`、`\rho'`；背景／基本態加 `\bar{}`（`\bar{\rho}`、`\bar{p}`）；向量粗體 `\mathbf{u}`；下標用 `\text{}`（`f_{\text{FD}}`、`\varepsilon_{\text{med}}`）。
- **R4.5 字形一致**：能量態統一用 `\varepsilon`（不混 `\epsilon`）；速率／一般量視題目既有符號而定，但**同一份檔內同一物理量只用一種字形**。

---

## 5. 審閱檢查清單（套用到目標 .ipynb 時逐條打勾）

對每個 `## Question N - Answer`：

- [ ] **C1 結構**：有 `## Question N` + `## Question N - Answer`？Answer 首段是前置知識區？（R1）
- [ ] **C2 前置標題**：是否統一為 `### 假設與已知 (Assumptions & Preliminaries)`（含英文）？（R1.2）
- [ ] **C3 卡片完整**：每張【已知/假設/定義/推導】是否都有「雙語標籤 → 公式 → 逐符號 bullet 清單」三件套？（R2）
- [ ] **C4 符號定義**：公式中**每一個**符號都在 bullet list 出現？含中文名（English）與單位？（R2.3）
- [ ] **C5 標籤分類正確**：外部定律=【已知】、簡化=【假設】、引新符號=【定義】(用 `\overset{def}{=}`)、中間結果=【推導】？（R2）
- [ ] **C6 overset 引用**：每個援引卡片／前步的等號是否都有 `\overset{依據}{=}`？被引用的編號是否真的存在？（R3.2）
- [ ] **C7 不跳步**：相鄰兩列之間是否只做一個可驗證的代數／物理動作？（R3.1）
- [ ] **C8 子步編號**：層級編號是否連續、可被後文回引？（R3.3）
- [ ] **C9 數值與單位**：最終答案 `\approx` + 單位？代入步驟帶單位？（R3.4）
- [ ] **C10 字形/符號一致**：`\varepsilon` vs `\epsilon`、下標、撇號、bar 是否全篇一致？（R4.4–R4.5）
- [ ] **C11 拼字**：英文術語拼字正確？（見 §6 樣式庫）

## 6. 常見不一致樣式庫（要主動抓的 pattern，源自參考檔自身問題）

1. **符號筆誤 `f_{\text{Fb}}` ↔ `f_{\text{FD}}`**：費米–狄拉克分佈，符號清單與公式混用。→ 全篇統一為 `f_{\text{FD}}`。
2. **前置標題不統一**：部分題用「假設與已知 (Assumptions & Preliminaries)」、部分只用「已知與假設」無英文。→ 統一成前者。
3. **epsilon 字形混用**：`\epsilon` 與 `\varepsilon` 並存。→ 統一 `\varepsilon`。
4. **英文拼字**：`kenatic`→`kinetic`；`亞變數`→`啞變數 (dummy variable)`。
5. **期望值符號歧義**：同題混用 `⟨E⟩`／`⟨ε⟩` 又令其相等時，需加一句說明釐清。
6. **定義 vs inline（跨領域）**：大氣用【定義】+ `\overset{def}{=}`，物理常 inline 引常數。標準化時，凡新符號改走【定義】卡片。

## 7. 檔案編輯與同步協議（Jupytext 草稿紙模式 — 強制遵守）

> 本協議**取代**舊版「直接用 NotebookEdit 改 .ipynb」的做法。因為 `.ipynb` 是 JSON，
> 大段落重寫易破壞結構；改為透過配對的 `.md`（MyST）編輯，再雙向同步回 `.ipynb`。
> **絕對禁止直接編輯 `.ipynb` 的 JSON 內容**（不論用 Edit、NotebookEdit 或文字替換）。

執行環境：jupytext 裝在獨立全域 Python `py -3.13`（`C:\Users\PDK\python.exe`），
與使用者的 Anaconda / jupyter-book 1.x **完全隔離**，所有指令一律以 `py -3.13 -m jupytext …` 呼叫。

### 7.1 環境與格式綁定（審閱前第一步）
當使用者指定任一 `.ipynb` 推導檔要審閱／修改時，**先檢查是否已有配對的同名 `.md`**：
- 看 `.ipynb` 是否含 `"jupytext": {"formats": "ipynb,md:myst"}` metadata，或同資料夾是否有同名 `.md`。
- 若**尚未配對**，強制先執行綁定（MyST 格式，避免 cell 合併）：
  ```
  py -3.13 -m jupytext --set-formats ipynb,md:myst "<路徑>\<檔名>.ipynb"
  ```
- 綁定後建議跑一次保真度檢查（比對 `.md` 還原的 cell source 與原 `.ipynb` 是否內容一致，
  僅允許行尾空白／空白尾格差異）。

### 7.2 絕對隔離編輯（草稿紙模式）
- **審閱與計畫階段：只讀取並分析該 `.md` 檔**（不碰 `.ipynb`）。用 Read 讀 `.md`，必要時 Grep 抓
  `【`、`overset`、`gather`、`### ` 等標記定位。
- **先出清單，後改檔**：對使用者輸出
  `位置（Question / 子步 / .md 行）→ 違反哪條規則(C/R 編號) → 現況 → 擬改寫`
  的逐項 diff 清單，**等使用者確認**。
- 獲同意後，**所有增刪改寫只能在 `.md` 上進行**（可用 Edit/Write 自由大篇幅重寫公式與段落）。

### 7.3 雙向同步驗證（改完才同步回 Notebook）
- 在 `.md` 完成全部修改、且使用者確認內容無誤後，**主動執行同步**將變更安全寫回 Notebook：
  ```
  py -3.13 -m jupytext --sync "<路徑>\<檔名>.md"
  ```
  （`--sync` 以較新檔更新另一個；流程恆為「先改 .md → 再 sync」。）
- 同步後確認 `.ipynb` 仍為合法 JSON、cell 數正常，並向使用者回報 diff 範圍。

### 7.4 不改物理／數學內容（不變的底線）
本 Skill 只統一**風格與一致性**。若發現疑似物理或數學「實質錯誤」，**先列出來問使用者**，
不擅自更動推導結論。
