# Coset Partition (陪集分割)

+++

## 證明目標:

投影片 p.20 直接丟出 [拉格朗日定理](Lagrange_Theorem.md)，中間跳過了兩條關鍵引理。
本檔把它們補齊 —— **陪集一樣大**，而且**它們把 $G$ 不重不漏地切完**。

* (a) 每個左陪集都與 $H$ 等勢（「一樣大」）：

$$\left|gH\right| = \left|H\right| \qquad \text{for all } g \in G$$

* (b) 兩個左陪集要嘛完全相同、要嘛完全不相交：

$$g_1H \cap g_2H \neq \varnothing \quad \Longrightarrow \quad g_1H = g_2H$$

* (c) 全部左陪集的聯集恰好是 $G$：

$$\bigcup_{g \in G} gH = G$$

* (d) (a)(b)(c) 合起來：**左陪集構成 $G$ 的一個分割 (partition)**，每一塊大小都是 $\left|H\right|$。

* $G$ : 母群的底層集合 (The underlying set of the ambient group) $[\text{集合}]$
* $H$ : $G$ 的子群 (A subgroup of $G$) $[H \le G]$
* $g,\ g_1,\ g_2$ : 群元素（陪集代表元）(Group elements serving as coset representatives) $[g, g_1, g_2 \in G]$
* $gH$ : 左陪集 (A left coset) $[gH \subseteq G]$
* $\left|gH\right|$ : 陪集的基數 (The cardinality of the coset) $[\left|gH\right| \in \mathbf{N} \cup \left\{\infty\right\}]$
* 註：**本檔的內容不在投影片上**，是為了讓 [拉格朗日定理](Lagrange_Theorem.md)
  能有一條乾淨的證明鏈而補的。投影片把這幾步壓縮成一句「then $\left|H\right|$ divides $\left|G\right|$」。
* 註：三條引理在 [特殊線性群的指標](Special_Linear_Subgroup_Index.md) 會被**再用一次** ——
  投影片 p.22 計算 $\left|SL_2(\mathbf{Z}_7)\right|$ 用的正是同一套論證。
  收成獨立檔案就是為了讓兩處共用，不必重證。
* 註：(a) 對**無限群**也成立（雙射即等勢），但 [拉格朗日定理](Lagrange_Theorem.md)
  需要 $G$ 有限才談得上整除。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [群的公理 (Group axioms)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Group/Group_Definition.html#definitions-and-notation)：** 已於本章 [群的定義](Group_Definition.md)【定義 2】給出，此處直接引用

  * (a) 結合律：

    $$a * \left(b * c\right) = \left(a * b\right) * c$$

  * (b) 單位元素與反元素：

    $$a * e = e * a = a, \qquad a * a^{-1} = a^{-1} * a = e$$

  * $G$ : 群的底層集合 (The underlying set of the group) $[\text{集合}]$
  * $a,\ b,\ c$ : 群元素 (Group elements) $[a, b, c \in G]$
  * $e$ : 單位元素 (The identity element) $[e \in G]$

* **【已知 2】 [左消去律 (Left cancellation law)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Group/Unique_Solution_and_Cancellation_Law.html#a-proof-of-the-left-cancellation-law)：** 已於本章 [唯一解與消去律](Unique_Solution_and_Cancellation_Law.md)【證明 (a)】完整證明，此處直接引用不再重證

  $$a * b = a * c \quad \Longrightarrow \quad b = c$$

  * $a,\ b,\ c$ : 群元素 (Group elements) $[a, b, c \in G]$

* **【已知 3】 [子群判別法 (Subgroup criterion)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Group/Subgroup_Criterion.html#b-proof-of-the-backward-direction)：** 已於本章 [子群判別法](Subgroup_Criterion.md) 完整證明，此處直接引用不再重證

  $$H \le G \quad \Longleftrightarrow \quad H \neq \varnothing,\ \ ab \in H,\ \ a^{-1} \in H \quad \text{for all } a, b \in H$$

  * $H$ : $G$ 的子群 (A subgroup of $G$) $[H \le G]$
  * $G$ : 母群的底層集合 (The underlying set of the ambient group) $[\text{集合}]$
  * $a,\ b$ : 子群中的元素 (Elements of the subgroup) $[a, b \in H]$
  * 註：由此可推出 $e \in H$，本檔多處會用到。

* **【已知 4】 [陪集的定義 (Definition of a coset)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Group/Coset.html#assumptions-preliminaries)：** 已於本章 [陪集](Coset.md)【定義 1】給出，此處直接引用

  $$gH = \left\{g * h \ \middle|\ h \in H\right\}$$

  * $H$ : $G$ 的子群 (A subgroup of $G$) $[H \le G]$
  * $g$ : 用來平移的群元素 (The translating group element) $[g \in G]$
  * $h$ : 子群中的元素 (An element of the subgroup) $[h \in H]$
  * $gH$ : 左陪集 (A left coset) $[gH \subseteq G]$

* **【已知 5】 [陪集相等的充要條件 (Coset equality criterion)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Group/Coset_Equality_Criterion.html#b-proof-of-the-backward-direction-for-left-cosets)：** 已於本章 [陪集相等的充要條件](Coset_Equality_Criterion.md)【證明 (a)(b)】完整證明，此處直接引用不再重證

  $$g_1H = g_2H \quad \Longleftrightarrow \quad g_1^{-1} * g_2 \in H$$

  * $g_1,\ g_2$ : 兩個陪集代表元 (Two coset representatives) $[g_1, g_2 \in G]$
  * $H$ : $G$ 的子群 (A subgroup of $G$) $[H \le G]$

* **【定義 1】 平移映射 (Translation map)：** 【證明 (a)】的主角。把 $H$ 的每個元素往左乘上 $g$

  $$L_g : H \to gH, \qquad L_g(h) \overset{\text{def}}{=} g * h$$

  * $L_g$ : 由 $g$ 決定的平移映射 (The translation map determined by $g$) $[H \to gH]$
  * $g$ : 用來平移的群元素 (The translating group element) $[g \in G]$
  * $h$ : 子群中的元素 (An element of the subgroup) $[h \in H]$
  * $H$ : $G$ 的子群 (A subgroup of $G$) $[H \le G]$
  * $gH$ : 左陪集 (A left coset) $[gH \subseteq G]$
  * 註：值域寫成 $gH$ 而不是 $G$ —— 依【已知 4】，$L_g$ 的像**恰好**就是 $gH$，
    這一點在【證明 (a)】的滿射部分會用到。

* **【定義 2】 分割 (Partition)：** 把一個集合拆成若干塊，每個元素恰好屬於一塊

  $$\left\{A_i\right\}_{i \in I} \ \text{為 } G \ \text{的分割} \quad \overset{\text{def}}{\Longleftrightarrow} \quad \bigcup_{i \in I} A_i = G \ \text{ 且 } \ A_i \cap A_j = \varnothing \ \text{ for } i \neq j$$

  * $A_i$ : 分割中的一塊 (A block of the partition) $[A_i \subseteq G]$
  * $I$ : 指標集合 (The index set) $[\text{集合}]$
  * $G$ : 被分割的集合 (The set being partitioned) $[\text{集合}]$
  * $i,\ j$ : 塊的指標 (Block indices) $[i, j \in I]$

+++

## 證明:

### (a) proof that every coset has the same size as the subgroup

證明【定義 1】的 $L_g$ 是雙射即可。

**滿射**：$gH$ 的元素依【已知 4】都長成 $g * h$ 的樣子，而那正是 $L_g(h)$：

$$\begin{gather*}
x &\overset{\text{已知 4}}{\in}& gH \\
x &\overset{\text{已知 4}}{=}& g * h \qquad \text{for some } h \in H \\
x &\overset{\text{定義 1}}{=}& L_g(h)
\end{gather*}$$

**單射**：兩個輸入若給出同一個輸出，左消去律立刻把 $g$ 約掉：

$$\begin{gather*}
L_g\left(h_1\right) &=& L_g\left(h_2\right) \\
g * h_1 &\overset{\text{定義 1}}{=}& g * h_2 \\
h_1 &\overset{\text{已知 2}}{=}& h_2
\end{gather*}$$

$L_g$ 是雙射，故兩集合等勢：

$$\left|gH\right| = \left|H\right|$$

* 註：**單射性完全依賴左消去律**，也就是依賴 $g^{-1}$ 存在。
  這是「陪集一樣大」這件事背後唯一的理由。

### (b) proof that two cosets are either identical or disjoint

設 $g_1H \cap g_2H \neq \varnothing$，取交集中的一個元素 $x$。它同時能用兩種方式寫出來：

$$\begin{gather*}
x &\overset{\text{已知 4}}{=}& g_1 * h_1 \qquad \text{for some } h_1 \in H \\
x &\overset{\text{已知 4}}{=}& g_2 * h_2 \qquad \text{for some } h_2 \in H
\end{gather*}$$

把兩個表示式接起來，解出 $g_1^{-1} * g_2$：

$$\begin{gather*}
g_1 * h_1 &=& g_2 * h_2 \\
g_1^{-1} * \left(g_1 * h_1\right) &=& g_1^{-1} * \left(g_2 * h_2\right) \\
h_1 &\overset{\text{已知 1(a)(b)}}{=}& \left(g_1^{-1} * g_2\right) * h_2 \\
h_1 * h_2^{-1} &\overset{\text{已知 1(a)(b)}}{=}& g_1^{-1} * g_2
\end{gather*}$$

左端是 $H$ 的兩個元素相乘（$h_2^{-1} \in H$ 由【已知 3】保證），故落在 $H$ 裡：

$$\begin{gather*}
h_2^{-1} &\overset{\text{已知 3}}{\in}& H \\
h_1 * h_2^{-1} &\overset{\text{已知 3}}{\in}& H \\
g_1^{-1} * g_2 &\in& H \\
g_1H &\overset{\text{已知 5}}{=}& g_2H
\end{gather*}$$

故兩陪集只要沾到一點，就完全重合。

### (c) proof that the cosets cover the whole group

任取 $g \in G$。它一定落在自己的陪集裡，因為 $H$ 含有單位元素：

$$\begin{gather*}
e &\overset{\text{已知 3}}{\in}& H \\
g &\overset{\text{已知 1(b)}}{=}& g * e \\
g &\overset{\text{已知 4}}{\in}& gH \\
g &\in& \bigcup_{g' \in G} g'H
\end{gather*}$$

反向的包含是顯然的（每個 $gH$ 都是 $G$ 的子集），故：

$$\bigcup_{g \in G} gH = G$$

### (d) proof that the left cosets form a partition

把三條合起來。【證明 (c)】給出覆蓋、【證明 (b)】給出互斥，這正是【定義 2】的兩個條件：

$$\begin{gather*}
\bigcup_{g \in G} gH &\overset{\text{證明 (c)}}{=}& G \qquad \text{(覆蓋)} \\
g_1H \cap g_2H &\overset{\text{證明 (b)}}{=}& \varnothing \quad \text{whenever } g_1H \neq g_2H \qquad \text{(互斥)} \\
\left\{gH\right\}_{g \in G} &\overset{\text{定義 2}}{=}& G \ \text{的一個分割}
\end{gather*}$$

再加上【證明 (a)】，**每一塊的大小都恰好是 $\left|H\right|$**。

* 註：【證明 (b)】的逆否形式才是分割定義要的樣子：「相異的兩塊必不相交」。
  原命題「相交則相同」與它邏輯等價。
* 註：不同的 $g$ 可能給出**同一塊**（由【已知 5】，恰好有 $\left|H\right|$ 個 $g$ 給出同一塊），
  所以 $\left\{gH\right\}_{g \in G}$ 這個族裡有大量重複。作為**集合的集合**，相異的塊數是
  $\left|G\right| / \left|H\right|$ —— 這正是 [拉格朗日定理](Lagrange_Theorem.md) 要說的。

+++

## 意義與密碼學關聯 (Interpretation and Relevance to Cryptography)

### 切蛋糕：三條引理的圖像

把 $G$ 想成一塊蛋糕，$H$ 是其中一片：

* **【證明 (a)】每一片一樣大** —— 平移不會改變大小，因為平移是雙射（有反向操作 $L_{g^{-1}}$）。
* **【證明 (b)】切片之間不重疊** —— 兩片只要沾到一點，就是同一片。
* **【證明 (c)】切片合起來就是整塊蛋糕** —— 沒有任何一塊碎屑被漏掉。

$$G = \underbrace{g_1H}_{\left|H\right|} \ \sqcup \ \underbrace{g_2H}_{\left|H\right|} \ \sqcup \ \cdots \ \sqcup \ \underbrace{g_kH}_{\left|H\right|}$$

**大小相等的 $k$ 片拼成整塊，所以 $\left|G\right| = k\left|H\right|$。**
[拉格朗日定理](Lagrange_Theorem.md) 就只剩下把這句話寫成整除關係而已。

### 為什麼要先證「一樣大」

【證明 (a)】看起來平凡，但它是整條論證鏈裡**唯一用到群結構**的一步。

分割（(b)(c)）對任何**等價關係**都成立，不需要群。
真正讓拉格朗日定理成立的是「每塊一樣大」，而那完全來自左消去律 ——
也就是來自**反元素的存在**。

把群換成只有封閉性與結合律的么半群（如 $\left(2\mathbf{Z}+1, \times\right)$，
見 [群的正例與反例](Group_Examples_and_Counterexamples.md)【證明 (j)】），
$L_g$ 不再是單射，各塊大小就會不同，整個定理立刻垮掉。

**「反元素」這條公理，最終買到的就是拉格朗日定理。**

### 分割就是「等價類」

分割與等價關係是同一件事的兩面。本檔的分割對應到的等價關係是：

$$g_1 \sim g_2 \quad \overset{\text{def}}{\Longleftrightarrow} \quad g_1^{-1} * g_2 \in H$$

由 [陪集相等的充要條件](Coset_Equality_Criterion.md)，這恰好是「$g_1$ 與 $g_2$ 落在同一塊」。

取 $G = \mathbf{Z}$、$H = n\mathbf{Z}$ 時，這個等價關係就是**同餘** $a \equiv b \pmod n$，
而分割的塊就是 $\mathbf{Z}_n$ 的 $n$ 個剩餘類。

**這是本章從「群」通往「環」的橋樑** —— 同樣的分割手法，
在 [模理想的同餘類](../Ring/Congruence_Class_Modulo_Ideal.md) 會用理想取代子群，
在 [商環](../Ring/Quotient_Ring.md) 會把塊本身變成新的代數結構。

### 密碼學上的對應：子群的指標決定安全邊界

密碼協議常在 $\mathbf{Z}_p^*$ 的一個子群 $H$ 裡運算。本檔告訴我們 $G$ 被切成
$\left|G\right| / \left|H\right|$ 塊，每塊 $\left|H\right|$ 個元素。

這個數字有直接的安全意義：

* 攻擊者若能判斷某個元素**落在哪一塊**，就得到了 $\log_2\left(\left|G\right|/\left|H\right|\right)$ 位元的資訊；
* 這正是 **Legendre 符號攻擊**的原理 —— 在 $\mathbf{Z}_p^*$ 裡，
  平方剩餘構成一個指標為 $2$ 的子群，而「是不是平方剩餘」可以在多項式時間內算出來。
  攻擊者因此免費拿到 $1$ 位元。

textbook ElGamal 就有這個問題：密文會洩漏明文的 Legendre 符號。
防禦方法是把運算限制在**質數階子群**裡 —— 質數階的群沒有真子群
（這也是拉格朗日定理的直接推論），也就沒有可以被利用的分割。
