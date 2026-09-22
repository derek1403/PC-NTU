# Subgroup Criterion (子群判別法)

+++

## 證明目標:

`Algebra.pdf` p.17。驗證一個子集是不是子群，本來要檢查四條公理；
本檔證明**只需檢查兩條**就夠了。

* (a)（$\Rightarrow$）$H$ 是 $G$ 的子群，則兩條件成立：

$$a * b \in H \ \text{ for all } a, b \in H, \qquad a^{-1} \in H \ \text{ for all } a \in H$$

* (b)（$\Leftarrow$）$H$ 非空且兩條件成立，則 $H$ 是 $G$ 的子群。

* $G$ : 母群的底層集合 (The underlying set of the ambient group) $[\text{集合}]$
* $H$ : $G$ 的子集 (A subset of $G$) $[H \subseteq G]$
* $*$ : 群運算 (Group operation) $[G \times G \to G]$
* $a,\ b$ : 子集中的元素 (Elements of the subset) $[a, b \in H]$
* $a^{-1}$ : $a$ 在 $G$ 中的反元素 (The inverse of $a$ in $G$) $[a^{-1} \in G]$
* 註：**投影片漏了「$H$ 非空」這個條件。** 空集合 $\varnothing$ 對兩個條件都「空虛地成立」
  （沒有元素可以違反它們），但 $\varnothing$ 沒有單位元素，不是群。
  本檔在【假設 1(a)】把這個條件補上，並在文末說明。
* 註：省下來的兩條是**結合律**（從 $G$ 免費繼承）與**單位元素**（可由另外兩條推導出來）。
  這是本檔的全部內容。
* 註：($\Rightarrow$) 方向看似顯然，其實有個細節：$H$ 作為群，它自己的單位元素與反元素
  **先驗上不保證**與 $G$ 的相同。【推導 1】【推導 2】處理這件事。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [群的公理 (Group axioms)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Group/Group_Definition.html#definitions-and-notation)：** 已於本章 [群的定義](Group_Definition.md)【定義 2】給出，此處直接引用

  * (a) 封閉性：

    $$a * b \in G \qquad \text{for all } a, b \in G$$

  * (b) 結合律：

    $$a * \left(b * c\right) = \left(a * b\right) * c \qquad \text{for all } a, b, c \in G$$

  * (c) 單位元素：

    $$a * e = e * a = a \qquad \text{for all } a \in G$$

  * (d) 反元素：

    $$a * a^{-1} = a^{-1} * a = e$$

  * $G$ : 母群的底層集合 (The underlying set of the ambient group) $[\text{集合}]$
  * $*$ : 群運算 (Group operation) $[G \times G \to G]$
  * $a,\ b,\ c$ : 群元素 (Group elements) $[a, b, c \in G]$
  * $e$ : $G$ 的單位元素 (The identity element of $G$) $[e \in G]$

* **【已知 2】 [唯一解與消去律 (Unique solution and cancellation law)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Group/Unique_Solution_and_Cancellation_Law.html#a-proof-of-the-left-cancellation-law)：** 已於本章 [唯一解與消去律](Unique_Solution_and_Cancellation_Law.md)【證明 (a)】完整證明，此處直接引用不再重證

  $$a * b = a * c \quad \Longrightarrow \quad b = c$$

  * $a,\ b,\ c$ : 群元素 (Group elements) $[a, b, c \in G]$

* **【已知 3】 [反元素唯一 (Uniqueness of the inverse)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Group/Uniqueness_of_Inverse.html#a-proof-uniqueness-of-the-inverse-element)：** 已於本章 [反元素唯一](Uniqueness_of_Inverse.md)【證明 (a)】完整證明，此處直接引用不再重證

  $$g * x = x * g = e \quad \Longrightarrow \quad x = g^{-1}$$

  * $g,\ x$ : 群元素 (Group elements) $[g, x \in G]$
  * $e$ : $G$ 的單位元素 (The identity element of $G$) $[e \in G]$

* **【定義 1】 子群 (Subgroup)：** $G$ 的一個子集，用**同一個運算**自己也構成群

  $$H \le G \quad \overset{\text{def}}{\Longleftrightarrow} \quad H \subseteq G \ \text{ 且 } \ \left(H, *\right) \ \text{本身是群}$$

  * $H$ : $G$ 的子集 (A subset of $G$) $[H \subseteq G]$
  * $G$ : 母群的底層集合 (The underlying set of the ambient group) $[\text{集合}]$
  * $*$ : 群運算，與 $G$ 的**同一個** (The group operation, the same one as in $G$) $[G \times G \to G]$
  * $\le$ : 「是……的子群」 (The subgroup relation) $[\text{關係}]$
  * 註：「**同一個運算**」是關鍵。$\left(\mathbf{Q}^*, \times\right)$ 是 $\left(\mathbf{R}^*, \times\right)$ 的子群，
    但 $\left(\mathbf{Q}^*, \times\right)$ 不是 $\left(\mathbf{R}, +\right)$ 的子群 —— 運算不同，無從談起。

* **【假設 1】 判別法的兩個條件 (The two conditions of the criterion)：** 【證明 (b)】的出發點

  * (a) 非空（**投影片未列，本檔補上**）：

    $$H \neq \varnothing$$

  * (b) 對運算封閉：

    $$a * b \in H \qquad \text{for all } a, b \in H$$

  * (c) 對取反元素封閉：

    $$a^{-1} \in H \qquad \text{for all } a \in H$$

  * $H$ : $G$ 的子集 (A subset of $G$) $[H \subseteq G]$
  * $a,\ b$ : 子集中的元素 (Elements of the subset) $[a, b \in H]$
  * $a^{-1}$ : $a$ 在 $G$ 中的反元素 (The inverse of $a$ in $G$) $[a^{-1} \in G]$
  * 註：(c) 裡的 $a^{-1}$ 指的是 **$a$ 在 $G$ 中的反元素**（$G$ 是群，所以它存在）。
    條件說的是「這個元素也剛好落在 $H$ 裡」。

* **【推導 1】 子群的單位元素與母群相同 (The identity of a subgroup coincides with that of the ambient group)：** 【證明 (a)】要用。設 $H \le G$，$H$ 自己的單位元素記作 $e_H$

  $$\begin{gather*}
  e_H * e_H &\overset{\text{已知 1(c)}}{=}& e_H \qquad \text{(在 } H \text{ 內，取 } a = e_H\text{)} \\
  e_H * e_H &\overset{\text{已知 1(c)}}{=}& e_H * e \qquad \text{(在 } G \text{ 內化簡右端)} \\
  e_H &\overset{\text{已知 2}}{=}& e
  \end{gather*}$$

  * $H$ : $G$ 的子群 (A subgroup of $G$) $[H \le G]$
  * $e_H$ : $H$ 自己的單位元素 (The identity element of $H$ itself) $[e_H \in H]$
  * $e$ : $G$ 的單位元素 (The identity element of $G$) $[e \in G]$
  * 註：第一行在 $H$ 裡成立、第二行在 $G$ 裡成立，第三行用 $G$ 的消去律把 $e_H$ 約掉。
    **兩個世界必須靠消去律接起來** —— 這就是這張卡片存在的理由。

* **【推導 2】 子群中的反元素與母群中的相同 (The inverse in a subgroup coincides with that in the ambient group)：** 【證明 (a)】要用。設 $H \le G$、$a \in H$，$a$ 在 $H$ 中的反元素記作 $b$

  $$\begin{gather*}
  a * b &\overset{\text{已知 1(d)}}{=}& e_H \qquad \text{(在 } H \text{ 內)} \\
  a * b &\overset{\text{推導 1}}{=}& e \\
  b &\overset{\text{已知 3}}{=}& a^{-1}
  \end{gather*}$$

  * $H$ : $G$ 的子群 (A subgroup of $G$) $[H \le G]$
  * $a$ : 子群中的元素 (An element of the subgroup) $[a \in H]$
  * $b$ : $a$ 在 $H$ 中的反元素 (The inverse of $a$ within $H$) $[b \in H]$
  * $a^{-1}$ : $a$ 在 $G$ 中的反元素 (The inverse of $a$ in $G$) $[a^{-1} \in G]$
  * $e,\ e_H$ : $G$ 與 $H$ 的單位元素 (The identities of $G$ and $H$) $[e \in G,\ e_H \in H]$
  * 註：同理可得 $b * a = e$，故 $b$ 雙邊都是 $a$ 在 $G$ 中的反元素，【已知 3】才適用。

+++

## 證明:

### (a) proof of the forward direction

設 $H \le G$，即 $\left(H, *\right)$ 本身是群（【定義 1】）。

**條件 (b) 封閉性**直接就是 $H$ 作為群的封閉性公理：

$$\begin{gather*}
a * b &\overset{\text{已知 1(a)}}{\in}& H \qquad \text{for all } a, b \in H
\end{gather*}$$

**條件 (c) 反元素封閉**需要多一步 —— $H$ 作為群保證每個 $a \in H$ 在 $H$ 裡有反元素 $b$，
但要說它就是 $G$ 裡的那個 $a^{-1}$，得靠【推導 2】：

$$\begin{gather*}
\exists\, b \in H \ \text{ with } \ a * b = b * a &\overset{\text{已知 1(d)}}{=}& e_H \\
b &\overset{\text{推導 2}}{=}& a^{-1} \\
a^{-1} &\in& H
\end{gather*}$$

兩個條件都成立。

* 註：這個方向**不需要**【假設 1(a)】的非空條件 —— $H$ 既然是群，它至少含有 $e_H$，自動非空。

### (b) proof of the backward direction

設 $H \subseteq G$ 滿足【假設 1】的三個條件。逐條檢查 $\left(H, *\right)$ 的四條群公理。

**封閉性**：這就是【假設 1(b)】，不必再證：

$$\begin{gather*}
a * b &\overset{\text{假設 1(b)}}{\in}& H \qquad \text{for all } a, b \in H
\end{gather*}$$

**結合律**：$H$ 的元素都是 $G$ 的元素，而結合律對 $G$ 的**所有**元素成立，故自動繼承：

$$\begin{gather*}
a, b, c &\in& H \subseteq G \\
a * \left(b * c\right) &\overset{\text{已知 1(b)}}{=}& \left(a * b\right) * c
\end{gather*}$$

**單位元素**：這是唯一需要動腦的一條。用非空條件取出一個元素，
再用另外兩個條件把 $e$ 製造出來：

$$\begin{gather*}
\exists\, a &\overset{\text{假設 1(a)}}{\in}& H \\
a^{-1} &\overset{\text{假設 1(c)}}{\in}& H \\
a * a^{-1} &\overset{\text{假設 1(b)}}{\in}& H \\
a * a^{-1} &\overset{\text{已知 1(d)}}{=}& e \\
e &\in& H
\end{gather*}$$

**反元素**：這就是【假設 1(c)】。由【推導 1】的結論（$H$ 的單位元素就是 $e$），
$a^{-1} \in H$ 確實是 $a$ 在 $H$ 中的反元素：

$$\begin{gather*}
a^{-1} &\overset{\text{假設 1(c)}}{\in}& H \\
a * a^{-1} = a^{-1} * a &\overset{\text{已知 1(d)}}{=}& e
\end{gather*}$$

四條公理全中，故 $\left(H, *\right)$ 是群：

$$\begin{gather*}
\left(H, *\right) &\overset{\text{已知 1}}{=}& \text{群} \\
H &\overset{\text{定義 1}}{\le}& G
\end{gather*}$$

兩個方向都證完，判別法成立。

+++

## 意義與密碼學關聯 (Interpretation and Relevance to Cryptography)

### 投影片漏掉的那一行

投影片 p.17 的 Proposition 寫成：

> A subset $H$ of a group $(G, *)$ is a subgroup of $G$ **iff**
> 1. $a * b \in H$ for all $a, b \in H$
> 2. $a^{-1} \in H$ for all $a \in H$

**這個敘述對 $H = \varnothing$ 是錯的。** 空集合裡沒有任何元素，所以「對所有 $a, b \in H$……」
這兩句話都空虛地為真；但 $\varnothing$ 沒有單位元素，依 [群的定義](Group_Definition.md)【定義 2(c)】
它不是群。

$\Leftarrow$ 方向真正用到非空的地方，在【證明 (b)】的「單位元素」那一段 ——
第一行就是 $\exists\, a \in H$。沒有這一行，整段論證無從開始。

本檔在【假設 1(a)】補上 $H \neq \varnothing$。
標準教科書的寫法也都含這個條件，投影片是省略了。

* **實務上的等價寫法**：與其寫「$H \neq \varnothing$」，更常見的是直接寫「$e \in H$」。
  由【證明 (b)】兩者在有另外兩條件時等價，但「$e \in H$」檢查起來更直接。

### 判別法省下了什麼

| 公理 | 要不要檢查 | 理由 |
|---|---|---|
| 封閉性 | **要** | 條件 (b) |
| 結合律 | **不用** | 從 $G$ 免費繼承（【證明 (b)】第二段） |
| 單位元素 | **不用** | 可由非空 + 另兩條件推出（【證明 (b)】第三段） |
| 反元素 | **要** | 條件 (c) |

四條變兩條（加一個非空），驗證成本大約砍半。
這在 [子群的例子](Subgroup_Examples.md) 會反覆用到。

### 結合律為什麼能白拿

這一點值得停下來想。結合律是一條**全稱命題**：「對所有 $a,b,c$ 都成立」。
$H$ 的元素是 $G$ 的元素的一部分，所以「對 $G$ 的所有元素成立」自動蘊涵「對 $H$ 的所有元素成立」。

**凡是全稱形式的性質，都會自動被子集繼承。** 交換律也是這樣 ——
阿貝爾群的任何子群都是阿貝爾群，不必另外檢查。

而封閉性與反元素**不是**單純的全稱命題，它們斷言「某個東西存在於 $H$ 裡」，
這是關於 $H$ 本身的斷言，$G$ 幫不上忙。**這就是為什麼恰好是這兩條要檢查。**

### 密碼學上的對應：子群攻擊

子群在密碼學裡是雙面刃。

**好的一面**：Diffie–Hellman 常刻意在 $\mathbf{Z}_p^*$ 的一個**大質數階子群**裡運算
（例如 DSA 用階為 $q$ 的子群，$q \mid p-1$）。這樣可以用較短的指數達到同樣的安全性，
運算快得多。

**壞的一面**：若協議收到對方的公鑰時**沒有檢查它是否落在正確的子群裡**，
攻擊者可以送一個階很小的元素（小子群裡的元素），
把共享金鑰壓縮到只有幾種可能，然後窮舉 —— 這就是 **small subgroup confinement attack**。

防禦方法正是本檔的判別法反過來用：**驗證收到的元素 $y$ 滿足 $y^q = e$**，
確認它確實落在那個階為 $q$ 的子群裡。這一行檢查在 TLS、Signal 等協議的實作裡都是必要的。
