# Integral Domain (整環)

+++

## 證明目標:

`Algebra.pdf` p.32。把「無零因子」這個好性質命名，並確認熟悉的環都有它。

* (a) $\mathbf{Z}, \mathbf{Q}, \mathbf{R}, \mathbf{C}$ 是整環。
* (b) $\mathbf{Q}[x]$ 與 $\mathbf{Z}[x, y]$ 是整環（靠【推導 2】的多項式次數論證）。
* (c) $\mathbf{Z}\!\left[\sqrt{2}\right] = \left\{a + b\sqrt{2} \ \middle|\ a, b \in \mathbf{Z}\right\}$ 是整環。
* (d) $\mathbf{Z}_6$ **不是**整環，零因子為 $2, 3, 4$。

* $R$ : 環的底層集合 (The underlying set of the ring) $[\text{集合}]$
* $a,\ b$ : 環元素 (Ring elements) $[a, b \in R]$
* $\mathbf{Z}\!\left[\sqrt{2}\right]$ : 二次整數環 (The quadratic integer ring) $[\text{集合}]$
* $R[x]$ : 多項式環 (The polynomial ring) $[\text{集合}]$
* $\mathbf{Z}_6$ : 模 $6$ 剩餘類環 (The ring of residues modulo 6) $[\text{集合}]$
* 註：依投影片 p.30 的約定，本檔的「環」一律指**交換的含單位元環**，
  見 [含單位元環與交換環](Ring_with_Identity_and_Commutative_Ring.md) 文末。
  標準教科書的整環定義還會明文加上「交換、含 $1$、$1 \neq 0$」三條，
  在本章的約定下它們已經內建，故投影片只寫「無零因子」是一致的。
* 註：整環是「$\mathbf{Z}$ 的抽象化」—— 它抓住了整數最重要的代數性質：
  **可以約分，但不見得能除**。能除的是 [體](../Field/Field_Definition.md)。
* 註：**本檔的兩張【推導】卡片是可重複使用的工具** ——
  【推導 1】說無零因子會被子環繼承、【推導 2】說會被多項式環繼承。
  有了它們，(a)(b)(c) 都只剩一行。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [零因子的定義與消去律 (Zero divisors and the cancellation law)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Ring/Zero_Divisor.html#c-proof-that-the-absence-of-zero-divisors-is-equivalent-to-the-cancellation-law)：** 已於本章 [零因子](Zero_Divisor.md)【定義 1】【證明 (c)】給出並證明，此處直接引用不再重證

  * (a) 零因子的定義：

    $$a, b \ \text{為零因子} \quad \overset{\text{def}}{\Longleftrightarrow} \quad a \neq 0, \quad b \neq 0, \quad ab = 0$$

  * (b) 無零因子等價於消去律：

    $$R \ \text{無零因子} \quad \Longleftrightarrow \quad \left[\, ab = ac,\ a \neq 0 \ \Longrightarrow \ b = c \,\right]$$

  * $R$ : 環的底層集合 (The underlying set of the ring) $[\text{集合}]$
  * $a,\ b,\ c$ : 環元素 (Ring elements) $[a, b, c \in R]$
  * $0$ : 加法單位元素 (The additive identity) $[0 \in R]$

* **【已知 2】 [$\mathbf{Z}_6$ 的零因子 (Zero divisors in the residues modulo six)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Ring/Zero_Divisor.html#a-verify-the-zero-divisors-in-the-residues-modulo-six)：** 已於本章 [零因子](Zero_Divisor.md)【證明 (a)】完整計算，此處直接引用不再重證

  $$2 \otimes 3 = 0, \qquad 3 \otimes 4 = 0 \qquad \text{在 } \mathbf{Z}_6 \text{ 中}$$

  * $\mathbf{Z}_6$ : 模 $6$ 剩餘類環 (The ring of residues modulo 6) $[\text{集合}]$
  * $\otimes$ : 模 $6$ 乘法 (Multiplication modulo 6) $[\mathbf{Z}_6 \times \mathbf{Z}_6 \to \mathbf{Z}_6]$

* **【已知 3】 [子環判別法 (Subring criterion)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Ring/Subring.html#a-proof-of-the-subring-criterion)：** 已於本章 [子環](Subring.md)【證明 (a)】完整證明，此處直接引用不再重證

  $$S \le R \quad \Longleftrightarrow \quad S \neq \varnothing, \quad a - b \in S, \quad ab \in S \qquad \text{for all } a, b \in S$$

  * $S$ : $R$ 的子集 (A subset of $R$) $[S \subseteq R]$
  * $R$ : 母環的底層集合 (The underlying set of the ambient ring) $[\text{集合}]$
  * $a,\ b$ : 子集中的元素 (Elements of the subset) $[a, b \in S]$

* **【已知 4】 [多項式環的構造 (Construction of the polynomial ring)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Ring/Ring_Examples.html#e-verify-that-the-polynomials-form-a-ring)：** 已於本章 [環的例子](Ring_Examples.md)【定義 2】【定義 3】【證明 (e)(f)】給出並證明，此處直接引用不再重證

  * (a) 乘法的摺積公式：

    $$\left(\sum_i a_i x^i\right)\left(\sum_j b_j x^j\right) = \sum_k \left(\sum_{i+j=k} a_i b_j\right)x^k$$

  * (b) 多變元遞迴構造：

    $$R[x, y] = \left(R[x]\right)[y]$$

  * $R[x]$ : 多項式環 (The polynomial ring) $[\text{集合}]$
  * $R$ : 係數所在的環 (The coefficient ring) $[\text{環}]$
  * $a_i,\ b_j$ : 多項式係數 (Polynomial coefficients) $[a_i, b_j \in R]$
  * $x,\ y$ : 未定元 (Indeterminates) $[x, y \notin R]$
  * $i,\ j,\ k$ : 次數指標 (Degree indices) $[i, j, k \in \mathbf{N}]$

* **【已知 5】 [實數無零因子 ($\mathbf{R}$ has no zero divisors)](https://mathworld.wolfram.com/Field.html)：** 標準結果，本章直接引用不再重證

  $$ab = 0, \quad a, b \in \mathbf{R} \quad \Longrightarrow \quad a = 0 \ \text{ 或 } \ b = 0$$

  * $a,\ b$ : 實數 (Real numbers) $[a, b \in \mathbf{R}]$
  * 註：$\mathbf{Z}, \mathbf{Q} \subseteq \mathbf{R}$，故三者都無零因子，這由【推導 1】直接得到。
    $\mathbf{C}$ 的情形同理（$ab = 0$ 時取模長得 $\left|a\right|\left|b\right| = 0$）。

* **【定義 1】 整環 (Integral domain)：** 沒有零因子的環

  $$R \ \text{為整環} \quad \overset{\text{def}}{\Longleftrightarrow} \quad R \ \text{為環且無零因子}$$

  * $R$ : 環的底層集合 (The underlying set of the ring) $[\text{集合}]$
  * 註：依【已知 1(b)】，這等價於「乘法消去律成立」。兩種說法可以互換使用。
  * 註：中文的「整環」取自 integral（整數的）—— 它的原型就是整數環 $\mathbf{Z}$。

* **【定義 2】 二次整數環 (Quadratic integer ring)：**

  $$\mathbf{Z}\!\left[\sqrt{2}\right] \overset{\text{def}}{=} \left\{a + b\sqrt{2} \ \middle|\ a, b \in \mathbf{Z}\right\}$$

  * $\mathbf{Z}\!\left[\sqrt{2}\right]$ : 二次整數環 (The quadratic integer ring) $[\text{集合}]$
  * $a,\ b$ : 整數係數 (Integer coefficients) $[a, b \in \mathbf{Z}]$

* **【推導 1】 無零因子由母環繼承到子環 (Absence of zero divisors passes to subrings)：** 零因子的定義只牽涉「非零」與「乘積為零」，兩者在子環與母環裡是同一回事

  $$\begin{gather*}
  S &\overset{\text{已知 3}}{\le}& R \\
  a, b \in S,\ ab = 0,\ a \neq 0,\ b \neq 0 &\overset{\text{已知 1(a)}}{\Longrightarrow}& a, b \ \text{是 } R \ \text{的零因子} \\
  R \ \text{無零因子} &\overset{\text{定義 1}}{\Longrightarrow}& S \ \text{無零因子}
  \end{gather*}$$

  * $S$ : $R$ 的子環 (A subring of $R$) $[S \le R]$
  * $R$ : 母環的底層集合 (The underlying set of the ambient ring) $[\text{集合}]$
  * $a,\ b$ : 子環中的元素 (Elements of the subring) $[a, b \in S]$
  * 註：第二行的關鍵是 **$S$ 的零元素與 $R$ 的零元素是同一個** ——
    這由 [子環判別法](Subring.md)【證明 (a)】的 $0 = a - a \in S$ 保證。
    否則「$ab = 0$」在兩個環裡會是不同的敘述。

* **【推導 2】 整環上的多項式環仍是整環 (The polynomial ring over an integral domain is an integral domain)：** 靠首項係數相乘不會消失

  * (a) 設 $f, g \neq 0$，首項係數分別為 $a_m \neq 0$、$b_n \neq 0$（$m, n$ 為次數）。
    摺積中 $x^{m+n}$ 的係數只有一項：

    $$\begin{gather*}
    \left[fg\right]_{m+n} &\overset{\text{已知 4(a)}}{=}& \sum_{i+j=m+n} a_i b_j \\
    \left[fg\right]_{m+n} &=& a_m b_n \qquad \text{(其餘項的 } a_i \text{ 或 } b_j \text{ 超出次數而為 } 0\text{)}
    \end{gather*}$$

  * (b) $R$ 無零因子，故這個係數非零，於是 $fg \neq 0$：

    $$\begin{gather*}
    a_m \neq 0, \quad b_n &\neq& 0 \\
    a_m b_n &\overset{\text{定義 1}}{\neq}& 0 \\
    fg &\neq& 0
    \end{gather*}$$

  * $R$ : 係數所在的整環 (The coefficient integral domain) $[\text{環}]$
  * $f,\ g$ : 非零多項式 (Non-zero polynomials) $[f, g \in R[x]]$
  * $a_m,\ b_n$ : 首項係數 (Leading coefficients) $[a_m, b_n \in R]$
  * $m,\ n$ : 兩個多項式的次數 (The degrees of the two polynomials) $[m, n \in \mathbf{N}]$
  * $i,\ j$ : 次數指標 (Degree indices) $[i, j \in \mathbf{N}]$
  * 註：(a) 的括號說明是重點 —— 要湊出 $i + j = m + n$ 且兩個指標都不超界，
    **只有 $i = m,\ j = n$ 這一種拆法**。所以最高次項的係數乾乾淨淨只有一項，
    不會有其他項來抵銷它。
  * 註：這同時證明了 $\deg\left(fg\right) = \deg f + \deg g$ ——
    這個等式在一般環裡**不成立**（首項係數可能相乘為零而降次）。

+++

## 證明:

### (a) verify that the four number systems are integral domains

由【已知 5】，$\mathbf{R}$ 無零因子；$\mathbf{Z}$ 與 $\mathbf{Q}$ 是 $\mathbf{R}$ 的子環
（[子環](Subring.md)【證明 (b)】），故由【推導 1】直接繼承：

$$\begin{gather*}
\mathbf{R} &\overset{\text{已知 5}}{=}& \text{無零因子} \\
\mathbf{Z},\ \mathbf{Q} &\overset{\text{已知 3}}{\le}& \mathbf{R} \\
\mathbf{Z},\ \mathbf{Q} &\overset{\text{推導 1}}{=}& \text{無零因子} \\
\mathbf{Z},\ \mathbf{Q},\ \mathbf{R},\ \mathbf{C} &\overset{\text{定義 1}}{=}& \text{整環}
\end{gather*}$$

$\mathbf{C}$ 的部分由【已知 5】的註直接給出。

### (b) verify that the polynomial rings are integral domains

$\mathbf{Q}$ 是整環（【證明 (a)】），套【推導 2】一次得 $\mathbf{Q}[x]$：

$$\begin{gather*}
\mathbf{Q} &\overset{\text{證明 (a)}}{=}& \text{整環} \\
\mathbf{Q}[x] &\overset{\text{推導 2}}{=}& \text{整環}
\end{gather*}$$

$\mathbf{Z}[x, y]$ 則套兩次 —— 先對 $x$、再對 $y$（【已知 4(b)】的遞迴構造）：

$$\begin{gather*}
\mathbf{Z} &\overset{\text{證明 (a)}}{=}& \text{整環} \\
\mathbf{Z}[x] &\overset{\text{推導 2}}{=}& \text{整環} \\
\mathbf{Z}[x, y] &\overset{\text{已知 4(b),推導 2}}{=}& \text{整環}
\end{gather*}$$

與投影片一致。

* 註：**【推導 2】可以無限次套用**，故任意多個未定元的多項式環仍是整環。
  這與 [環的例子](Ring_Examples.md)【證明 (f)】的遞迴手法完全一樣。

### (c) verify that the quadratic integer ring is an integral domain

先確認 $\mathbf{Z}\!\left[\sqrt{2}\right]$ 是 $\mathbf{R}$ 的子環（【已知 3】三條）：

$$\begin{gather*}
0 = 0 + 0\sqrt{2} &\overset{\text{定義 2}}{\in}& \mathbf{Z}\!\left[\sqrt{2}\right] \qquad \text{(非空)} \\
\left(a + b\sqrt{2}\right) - \left(c + d\sqrt{2}\right) &=& \left(a - c\right) + \left(b - d\right)\sqrt{2} \\
\left(a + b\sqrt{2}\right) - \left(c + d\sqrt{2}\right) &\overset{\text{定義 2}}{\in}& \mathbf{Z}\!\left[\sqrt{2}\right] \qquad \text{(減法封閉)} \\
\left(a + b\sqrt{2}\right)\left(c + d\sqrt{2}\right) &=& \left(ac + 2bd\right) + \left(ad + bc\right)\sqrt{2} \\
\left(a + b\sqrt{2}\right)\left(c + d\sqrt{2}\right) &\overset{\text{定義 2}}{\in}& \mathbf{Z}\!\left[\sqrt{2}\right] \qquad \text{(乘法封閉)} \\
\mathbf{Z}\!\left[\sqrt{2}\right] &\overset{\text{已知 3}}{\le}& \mathbf{R}
\end{gather*}$$

再套【推導 1】：

$$\begin{gather*}
\mathbf{R} &\overset{\text{已知 5}}{=}& \text{無零因子} \\
\mathbf{Z}\!\left[\sqrt{2}\right] &\overset{\text{推導 1}}{=}& \text{無零因子} \\
\mathbf{Z}\!\left[\sqrt{2}\right] &\overset{\text{定義 1}}{=}& \text{整環}
\end{gather*}$$

* 註：乘法封閉那一行的 $\left(\sqrt{2}\right)^2 = 2 \in \mathbf{Z}$ 是關鍵 ——
  **$\sqrt{2}$ 的平方掉回整數裡**，所以不會生出 $\sqrt{2}$ 以外的新東西。
  這正是 $\sqrt{2}$ 滿足整係數方程 $t^2 - 2 = 0$ 的後果，
  也是 [單擴張](../Field/Simple_Extension.md) 要推廣的想法。

### (d) disprove that the residues modulo six form an integral domain

直接引用【已知 2】：

$$\begin{gather*}
2 \otimes 3 &\overset{\text{已知 2}}{=}& 0 \\
2 \neq 0, \quad 3 &\neq& 0 \\
2, 3 &\overset{\text{已知 1(a)}}{=}& \mathbf{Z}_6 \ \text{的零因子} \\
\mathbf{Z}_6 &\overset{\text{定義 1}}{\neq}& \text{整環}
\end{gather*}$$

投影片列出的零因子是 $2, 3, 4$ —— $4$ 的搭檔是 $3$（$3 \otimes 4 = 12 \equiv 0$，【已知 2】）。

* 註：$\mathbf{Z}_n$ 是整環 $\Leftrightarrow$ $n$ 為質數，這由
  [零因子](Zero_Divisor.md)【證明 (b)】直接得到。

+++

## 意義與密碼學關聯 (Interpretation and Relevance to Cryptography)

### 整環 = 「可以約分的環」

整環最實用的刻畫是【已知 1(b)】的消去律版本：

$$ab = ac, \quad a \neq 0 \quad \Longrightarrow \quad b = c$$

這是你從小學會的動作。整環的定義就是「保留這個動作的環」。

$\mathbf{Z}$ 是整環但**不是體** —— 你可以約分，但不能除。
這個微妙的差別正是 [體的定義](../Field/Field_Definition.md) 要處理的事：

$$\text{環} \ \supsetneq \ \text{整環} \ \supsetneq \ \text{體}$$

（最後一個包含對**有限**的情形其實是等號 —— 有限整環必為體，這是 Wedderburn 的一個推論，本章不證。）

### 投影片 p.32 的 Remark：數體篩法

投影片在這一頁提到：

> The *Number Field Sieve* is based on the theory with Dedekind Domains,
> Unique Factorization Domains (UFD), and Principal Ideal Domains (PID)

這三個名詞都是整環的加強版，構成一條階梯：

$$\text{整環} \ \supsetneq \ \text{Dedekind 整環} \ \supsetneq \ \text{PID} \ \supsetneq \ \text{UFD 的一部分} \ \supsetneq \ \text{體}$$

（嚴格的包含關係是 體 $\subsetneq$ PID $\subsetneq$ UFD $\subsetneq$ 整環，Dedekind 整環另成一支。）

**數體篩法 (NFS) 是目前分解 RSA 模數最快的已知演算法**，它的想法是：

1. 在 $\mathbf{Z}$ 裡分解 $n$ 很難；
2. 但把問題搬到一個更大的環 $\mathbf{Z}[\alpha]$（$\alpha$ 是某個代數數）裡，
   那裡的「分解」可以用理想的語言處理，而且有現成的演算法；
3. 把那邊的結果搬回 $\mathbf{Z}$，就得到 $n$ 的因數。

第 2 步需要那個大環的分解性質夠好 —— 這就是為什麼需要 Dedekind 整環與 UFD 的理論。
【證明 (c)】的 $\mathbf{Z}\!\left[\sqrt{2}\right]$ 正是這類環最簡單的例子。

**RSA-2048 之所以還沒被分解，靠的就是 NFS 的複雜度還不夠低** ——
所以這一頁的 Remark 不是離題，它直接關係到 RSA 該用多長的金鑰。

### 為什麼 $\mathbf{Z}_n$（$n$ 合數）不是整環，RSA 卻照用不誤

[零因子](Zero_Divisor.md) 文末已經說過：$\mathbf{Z}_n$（$n = pq$）必有零因子，
所以它**不是整環**，消去律失效。

RSA 能運作的原因是它**不在 $\mathbf{Z}_n$ 整體上工作**，而是在
$\mathbf{Z}_n^*$（可逆元素的群，見 [數系與符號約定](../Number_Sets_and_Notation.md)【定義 4】）裡。
$\mathbf{Z}_n^*$ 是一個群，裡面每個元素都可逆，自然沒有零因子的問題。

**壞元素（零因子）與好元素（可逆元）在 $\mathbf{Z}_n$ 裡涇渭分明**：

$$\mathbf{Z}_n = \underbrace{\left\{0\right\}}_{\text{零}} \ \sqcup \ \underbrace{\mathbf{Z}_n^*}_{\text{可逆}} \ \sqcup \ \underbrace{\left\{\text{其餘}\right\}}_{\text{零因子}}$$

RSA 只用中間那塊。而「其餘那塊裡的元素都是零因子」這件事，正是
[零因子](Zero_Divisor.md) 文末說的「找到零因子等於分解 $n$」。
