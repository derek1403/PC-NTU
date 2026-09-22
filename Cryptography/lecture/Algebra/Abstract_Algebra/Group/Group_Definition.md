# Group Definition (群的定義)

+++

## 本檔目標:

把 `Algebra.pdf` p.4 的群公理攤開成可被全章引用的**【定義】卡片**。本章往後每一次寫
`\overset{\text{已知 N}}{=}` 而依據是「封閉性」「結合律」「單位元素」「反元素」時，都回溯到本檔。

* (a) 群的四條公理：

$$\text{封閉性 (Closure)}, \quad \text{結合律 (Associativity)}, \quad \text{單位元素 (Identity)}, \quad \text{反元素 (Inverse)}$$

* (b) 一個群記作 $\left(G, *\right)$ —— **集合 $G$ 與運算 $*$ 兩者合起來**才是群，
  單講集合 $G$ 而不指定運算是沒有意義的。

* 註：本檔**只有定義，沒有證明**。四條公理各自在具體集合上成立與否的逐條檢查，
  見 [群的正例與反例](Group_Examples_and_Counterexamples.md)。
* 註：群的公理**不包含交換律**。滿足交換律的群另有專名，見
  [阿貝爾群與非阿貝爾群](Abelian_and_Non_Abelian_Group.md)。
* 註：公理只保證單位元素與反元素**存在**，沒有說它們**唯一**。唯一性要另外證，
  見 [單位元素唯一](Uniqueness_of_Identity.md) 與 [反元素唯一](Uniqueness_of_Inverse.md)。
  在那兩件事證完之前，記號 $a^{-1}$ 嚴格來說是不合法的（因為不知道該指哪一個）。

+++

## 定義與符號 (Definitions and Notation)

* **【定義 1】 二元運算 (Binary operation)：** 群的前提。一個把 $G$ 中兩個元素配成一個元素的規則

  $$* : G \times G \to G, \qquad \left(a, b\right) \mapsto a * b$$

  * $G$ : 一個集合 (A set) $[\text{集合}]$
  * $*$ : 二元運算 (Binary operation) $[G \times G \to G]$
  * $a,\ b$ : 集合的兩個元素 (Two elements of the set) $[a, b \in G]$
  * 註：寫成 $G \times G \to G$ 的箭頭時，**值域已經寫死是 $G$** —— 這其實就把封閉性
    藏在記號裡了。投影片仍把封閉性單獨列為一條公理，本章沿用投影片的寫法（【定義 2(a)】），
    因為實際驗證一個集合是不是群時，封閉性往往是最先壞掉的那一條。

* **【定義 2】 群 (Group)：** 一個集合 $G$ 配上一個二元運算 $*$，滿足以下四條公理

  * (a) 封閉性 (Closure)：

    $$a * b \in G \qquad \text{for all } a, b \in G$$

  * (b) 結合律 (Associativity)：

    $$a * \left(b * c\right) = \left(a * b\right) * c \qquad \text{for all } a, b, c \in G$$

  * (c) 單位元素 (Identity)：存在 $e \in G$ 使得

    $$a * e = e * a = a \qquad \text{for all } a \in G$$

  * (d) 反元素 (Inverse)：對每個 $a \in G$，存在 $b \in G$ 使得

    $$a * b = b * a = e$$

  * $G$ : 群的底層集合 (The underlying set of the group) $[\text{集合}]$
  * $*$ : 群運算 (Group operation) $[G \times G \to G]$
  * $a,\ b,\ c$ : 群元素 (Group elements) $[a, b, c \in G]$
  * $e$ : 單位元素 (Identity element) $[e \in G]$
  * 註：(c) 與 (d) 都要求**左右兩側都成立**（$a * e = e * a$、$a * b = b * a$）。
    只滿足單側的結構稱為「左單位元素／右反元素」等，本章不討論。
  * 註：(d) 的 $e$ 引用的是 (c) 的那個 $e$ —— 所以**必須先有單位元素才談得上反元素**，
    四條公理的順序不能任意對調。

* **【定義 3】 乘法記號與冪次 (Multiplicative notation and powers)：** 運算符號 $*$ 寫久了很煩，本章沿用標準簡寫

  * (a) 省略運算符號：

    $$ab \overset{\text{def}}{=} a * b$$

  * (b) 正冪次：

    $$g^n \overset{\text{def}}{=} \underbrace{g * g * \cdots * g}_{n \ \text{個}} \qquad \left(n \in \mathbf{P}\right)$$

  * (c) 零次冪與負冪次：

    $$g^0 \overset{\text{def}}{=} e, \qquad g^{-n} \overset{\text{def}}{=} \underbrace{g^{-1} * g^{-1} * \cdots * g^{-1}}_{n \ \text{個}} \qquad \left(n \in \mathbf{P}\right)$$

  * $g$ : 群元素 (A group element) $[g \in G]$
  * $a,\ b$ : 群元素 (Group elements) $[a, b \in G]$
  * $n$ : 冪次 (Exponent) $[n \in \mathbf{P}]$
  * $e$ : 單位元素 (Identity element) $[e \in G]$
  * $g^{-1}$ : $g$ 的反元素 (The inverse of $g$) $[g^{-1} \in G]$
  * $\mathbf{P}$ : 正整數集合 (The set of positive integers) $[\text{集合}]$，見
    [數系與符號約定](../Number_Sets_and_Notation.md)【定義 2(b)】
  * 註：(b) 的寫法不必加括號，因為【定義 2(b)】的結合律保證**怎麼加括號結果都一樣**。
    沒有結合律的話 $g * g * g$ 是有歧義的。
  * 註：群運算寫成加法時（如 $\left(\mathbf{Z}, +\right)$），對應的記號改成
    $na$ 而非 $a^n$、$-a$ 而非 $a^{-1}$、$0$ 而非 $e$。這只是記號差異，不是不同的結構。
  * 註：(c) 的 $g^{-1}$ 引用了【定義 2(d)】保證存在的反元素。此處的合法性依賴
    [反元素唯一](Uniqueness_of_Inverse.md)，該檔證完後 $g^{-1}$ 才是良定義的記號。

+++

## 意義與密碼學關聯 (Interpretation and Relevance to Cryptography)

### 四條公理各自在擋掉什麼

四條公理不是隨便湊的，每一條都恰好擋掉一種「算到一半卡住」的情形：

| 公理 | 沒有它會怎樣 | 本章的反例 |
|---|---|---|
| **封閉性** | 算出來的東西跑出集合外，後面的運算無法繼續 | $\mathbf{Z}_7$ 配不取模的 $+$ |
| **結合律** | $a * b * c$ 沒有唯一意義，冪次 $g^n$ 無法定義 | $\mathbf{Z}$ 配減法 $-$ |
| **單位元素** | 沒有「不動點」，無法定義反元素 | $\mathbf{P}$ 配 $+$ |
| **反元素** | 方程式 $a * x = b$ 解不出來，加密後無法解密 | $2\mathbf{Z}+1$ 配 $\times$ |

逐條的驗證見 [群的正例與反例](Group_Examples_and_Counterexamples.md)。

### 為什麼密碼學非要是群不可

密碼學的核心需求是「**加密後一定要能解密**」。用群論的話講就是：

$$\text{加密} \ c = a * m \quad \xrightarrow{\ \text{解密}\ } \quad m = a^{-1} * c$$

這一步要成立，$a^{-1}$ 必須**存在**（反元素公理）、$a^{-1} * \left(a * m\right)$ 必須等於
$\left(a^{-1} * a\right) * m$（結合律）、$a^{-1} * a$ 必須是 $e$ 且 $e * m = m$（單位元素公理），
而中間每一步的結果都必須還在明文空間裡（封閉性）。

**四條公理全部用上，一條都不能少。** 這就是為什麼幾乎所有密碼系統的第一句話都是
「令 $G$ 為一個群」。

### 程式思維

封閉性在程式裡就是**型別保證**：若你定義一個類別 `GroupElement` 並實作 `__mul__`，
封閉性要求 `return` 的型別必須仍是 `GroupElement`，不能突然變成 `int` 或 `list`。

結合律則決定了你能不能安全地寫 `functools.reduce(op, elements)` —— 沒有結合律，
`reduce` 的左折疊與右折疊會給出不同答案。

$\left(G, *\right)$ 這個記號本身也值得注意：**群是「集合 + 運算」的配對**，
不是集合本身。同一個集合配不同運算可能一個是群、一個不是
（$\mathbf{Z}$ 配 $+$ 是群，配 $-$ 不是；配 $\times$ 也不是）。
在程式裡對應的就是「資料結構 + 操作」必須一起傳。
