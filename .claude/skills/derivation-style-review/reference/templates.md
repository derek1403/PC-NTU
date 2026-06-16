# 可複製樣板片段（templates）

供依 [derivation-style-review](../SKILL.md) 風格新寫或改寫推導時直接複製。
所有 `〈…〉` 為待填欄位。

---

## 卡片 — 【已知】

```markdown
* **【已知 N】 〈中文名〉（〈English name〉） ：**

  $$〈display 公式〉$$

  * $〈符號〉$ : 〈中文名〉 (〈English name〉) $[\text{〈單位〉}]$
  * $〈符號〉$ : 〈中文名〉 (〈English name〉) [無單位]
```

含 lecture 超連結的版本（大氣常用）：

```markdown
* **【已知 N】 [〈定律中文名〉 (〈English name〉)](〈lecture 連結〉)  ：**

  $$〈display 公式〉$$
```

## 卡片 — 【假設】

```markdown
* **【假設 N】〈中文名〉（〈English assumption〉）：** 〈一句中文說明此假設的物理意義／適用範圍〉

  $$〈簡化後的式子，可用 \overset{\text{假設 N}}{=} 標出被歸零或取常數的項〉$$
```

## 卡片 — 【定義】（引入新符號，用 \overset{def}{=}）

```markdown
* **【定義 N】〈新符號中文名〉（〈English name〉）：**

  $$\begin{gather*}
  〈符號〉 &\overset{\text{def}}{=}& 〈定義式〉 \\
  &\overset{\text{假設 k}}{=}& 〈代入假設後的形式〉
  \end{gather*}$$

  * $〈符號〉$ : 〈中文名〉 (〈English name〉) $[\text{〈單位〉}]$
```

## 卡片 — 【推導】（供主證明引用的中間結果）

```markdown
* **【推導 N】〈中文名〉（〈English name〉）：** 〈一句中文說明這步在做什麼〉

  * (a) 〈子步說明〉

  $$\begin{gather*}
  〈LHS〉 &\overset{\text{let}}{=}& 〈RHS〉 \\
  〈…〉 &=& 〈…〉
  \end{gather*}$$

  * (b) 〈子步說明〉

  $$\begin{gather*}
  〈LHS〉 &\overset{\text{推導 N(a)}}{=}& 〈RHS〉 \\
  \end{gather*}$$
```

---

## 主推導 — gather* 骨架（三欄對齊 + overset 引用）

```markdown
### (a) proof 〈要證明的結論〉

$$\begin{gather*}
〈起手式〉 &\overset{\text{已知 2}}{=}& 〈…〉 \\
            &\overset{\text{已知 1}}{=}& 〈…〉 \\
            &=& 〈純代數整理，不必標〉 \\
            &\overset{\text{推導 1}}{=}& 〈…〉 \\
            &\approx& 〈數值〉 \text{ 〈單位〉}
\end{gather*}$$
```

## 主推導 — 逐值代入（solve，子步層級編號）

```markdown
### solve 〈問句〉

1. $v = 0$

$$\begin{gather*}
\frac{N_v}{N_0} &\overset{\text{推導 1}}{=}& e^{-v \cdot 1.2675} \\
                &\overset{\text{Q1.1.1}}{=}& e^{-0 \times 1.2675} \\
                &=& 1
\end{gather*}$$

2. $v = 1$

$$\begin{gather*}
\frac{N_v}{N_0} &\overset{\text{推導 1}}{=}& e^{-v \cdot 1.2675} \\
                &\overset{\text{Q1.1.2}}{=}& e^{-1 \times 1.2675} \\
                &\approx& 0.2815
\end{gather*}$$
```

---

## 一題的整體骨架

```markdown
## Question N

〈原題照錄，英文／LaTeX 原文，不改寫〉

## Question N - Answer

### 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 … ：** …
* **【假設 1】 … ：** …
* **【定義 1】 … ：** …
* **【推導 1】 … ：** …

### (a) proof / solve …

$$\begin{gather*} … \end{gather*}$$
```

---

## 引用字串速查（放進 `\overset{\text{…}}{=}`）

| 來源 | 寫法 |
|------|------|
| 援用某條已知 | `已知 1`、`已知 1(b)`、`已知 2,3` |
| 援用某條假設 | `假設 3(a)` |
| 援用某條定義 | `定義 4`、`定義 1(b),定義 2` |
| 援用某條推導 | `推導 1`、`推導 5,6` |
| 援用本題前一子步 | `Q4(a)`、`Q1.1.3` |
| 自行設定義 | `def`、`let` |
