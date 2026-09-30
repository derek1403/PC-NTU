# Existence of GF(p^n) (GF(p^n) 的存在性)

+++

## 證明目標:

`FiniteFields.pdf` p.27（下半）、p.34（Remark 2）、p.36（Theorem 的存在部分）；補充講義 Theorem 7.24。
**對每個質數 $p$ 與正整數 $n$，都存在恰有 $p^n$ 個元素的體。**
投影片 p.27 預告的路線：$GF(p^n)$ 就是 $x^{p^n} - x$ 的分裂體，而它「恰好由 $p^n$ 個相異根組成」。

* (a) 在任一讓 $x^{p^n} - x$ 完全分解的擴張體 $L \supseteq GF(p)$ 中，其根集

$$K = \left\{\alpha \in L \ \middle|\ \alpha^{p^n} = \alpha\right\} \ \text{是恰有 } p^n \text{ 個元素的體}$$

* (b) 投影片 p.34 的 Remark：$K$ 就是 $x^{p^n} - x$ 在 $GF(p)$ 上的分裂體 —— **分裂體恰由它的 $p^n$ 個根組成**。

* (c) $K$ 對 $GF(p)$ 的擴張次數是 $n$：

$$\left[K : GF(p)\right] = n$$

* $p$ : 質數 (A prime) $[p \in \mathbf{P}]$
* $n$ : 正整數 (A positive integer) $[n \in \mathbf{P}]$
* $L$ : 讓 $x^{p^n} - x$ 完全分解的有限擴張 (A finite extension over which $x^{p^n} - x$ splits) $[GF(p) \subseteq L]$
* $K$ : $x^{p^n} - x$ 的根集 (The set of roots of $x^{p^n} - x$) $[K \subseteq L]$
* 註：補充講義的路線不同：它先用計數論證（Theorem 7.23）證明**每個次數都有不可約多項式**，
  再套 [GF(p^n) 的構造](../Construction/Construction_of_GF_p_n.md)。
  本檔走投影片的路線（分裂體 + 無重根），不需要先知道不可約多項式存在；
  反過來，「每個次數都有不可約多項式」會在 [$x^{p^n}-x$ 的分解](../Multiplicative_Group/Factorization_of_x_p_n_minus_x.md) 中由本檔推出。
* 註：投影片 p.36 的 Theorem 還有「exactly one ... up to isomorphism」，那是唯一性，見 [$GF(p^n)$ 的唯一性](Uniqueness_of_GF_p_n.md)。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [多項式在有限擴張中完全分解 (Every polynomial splits in a finite extension)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Finite_Fields/Construction/Splitting_Field.html#b-proof-that-every-polynomial-splits-in-some-finite-extension)：** 已於本章 [分裂體](../Construction/Splitting_Field.md)【定義 1】【證明 (b)】給出並證明，此處直接引用不再重證

  * (a) 存在有限擴張 $L$ 使 $f$ 完全分解：

    $$f = a\prod_{i}\left(x - \alpha_i\right) \ \text{ in } L[x], \qquad \left[L : F\right] < \infty$$

  * (b) 分裂體的定義：

    $$E \ \text{為 } f \text{ 的分裂體} \ \Longleftrightarrow \ E \ \text{是含 } F \text{ 與 } f \text{ 所有根的最小體}$$

  * $f$ : 多項式 (A polynomial) $[f \in F[x]]$
  * $\alpha_i$ : 根 (Roots) $[\alpha_i \in L]$

* **【已知 2】 [$x^{p^n}-x$ 的根集是子體 (The roots of x^{p^n} − x form a subfield)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Finite_Fields/Structure/Roots_of_x_q_minus_x.html#c-proof-that-the-roots-of-x-to-the-p-to-the-n-minus-x-form-a-subfield)：** 已於本章 [$x^q - x$ 的根](Roots_of_x_q_minus_x.md)【證明 (a)(c)】完整證明，此處直接引用不再重證

  * (a) 根集是子體：

    $$\mathrm{ch}(L) = p \quad \Longrightarrow \quad \left\{\alpha \in L \ \middle|\ \alpha^{p^n} = \alpha\right\} \ \text{是 } L \text{ 的子體}$$

  * (b) $GF(p)$ 的元素滿足 $a^p = a$：

    $$a \in GF(p) \quad \Longrightarrow \quad a^p = a$$

  * $a$ : $GF(p)$ 的元素 (An element of $GF(p)$) $[a \in GF(p)]$

* **【已知 3】 [$x^{p^n}-x$ 沒有重根 (x^{p^n} − x has no multiple roots)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Finite_Fields/Polynomial_Arithmetic/Formal_Derivative_and_Multiple_Roots.html#c-proof-that-the-polynomial-x-to-the-p-to-the-n-minus-x-has-no-multiple-roots)：** 已於本章 [形式導數與重根](../Polynomial_Arithmetic/Formal_Derivative_and_Multiple_Roots.md)【證明 (c)】完整證明，此處直接引用不再重證

  $$x^{p^n} - x \ \text{在任何讓它完全分解的擴張中有 } p^n \text{ 個相異根}$$

* **【已知 4】 [有限體的階 (Order of a finite field)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Finite_Fields/Structure/Order_of_a_Finite_Field.html#b-proof-that-the-order-of-a-finite-field-is-a-prime-power)：** 已於本章 [有限體的階](Order_of_a_Finite_Field.md)【證明 (a)(b)】完整證明，此處直接引用不再重證

  $$\left|K\right| = p^{\left[K : P\right]}, \qquad P = \left\{k \cdot 1_K\right\} \cong GF(p)$$

  * $P$ : 質子體 (The prime subfield) $[P \subseteq K]$

* **【已知 5】 [體的特徵 (Characteristic of a field)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Field/Characteristic_of_a_Field.html#b-proof-that-a-positive-characteristic-must-be-prime)：** 已於 [體的特徵](../../Abstract_Algebra/Field/Characteristic_of_a_Field.md)【定義 1】給出，此處直接引用

  $$\mathrm{ch}(L) = \min\left\{m \in \mathbf{P} \ \middle|\ m \cdot 1_L = 0\right\}$$

  * $1_L$ : $L$ 的乘法單位元素 (The multiplicative identity of $L$) $[1_L \in L]$

* **【假設 1】 分裂 $x^{p^n} - x$ 的擴張 (An extension splitting x^{p^n} − x)：** 由【已知 1(a)】取定

  $$GF(p) \subseteq L, \qquad x^{p^n} - x = \prod_{i=1}^{p^n}\left(x - \alpha_i\right) \ \text{ in } L[x], \qquad \left[L : GF(p)\right] < \infty$$

  * $\alpha_i$ : $x^{p^n} - x$ 在 $L$ 中的根 (The roots in $L$) $[\alpha_i \in L]$

* **【定義 1】 根集 (The root set)：**

  $$K \overset{\text{def}}{=} \left\{\alpha \in L \ \middle|\ \alpha^{p^n} = \alpha\right\} = \left\{\alpha_1, \dots, \alpha_{p^n}\right\}$$

  * $K$ : 根集 (The root set) $[K \subseteq L]$

* **【推導 1】 擴張體的特徵仍是 $p$ (The extension still has characteristic p)：** $L$ 與子體 $GF(p)$ 共用同一個 $1$

  $$\begin{gather*}
  1_L &=& 1_{GF(p)} \\
  m \cdot 1_L = 0 &\Longleftrightarrow& m \cdot 1_{GF(p)} = 0 \\
  \mathrm{ch}(L) &\overset{\text{已知 5}}{=}& \mathrm{ch}\left(GF(p)\right) = p
  \end{gather*}$$

  * $m$ : 正整數 (A positive integer) $[m \in \mathbf{P}]$

* **【推導 2】 $GF(p) \subseteq K$ (The prime field lies in K)：** 反覆套 $a^p = a$

  $$\begin{gather*}
  a^{p} &\overset{\text{已知 2(b)}}{=}& a \\
  a^{p^2} = \left(a^p\right)^p &=& a^p = a \\
  a^{p^n} &=& a \qquad \text{(對 } n \text{ 歸納)} \\
  a &\overset{\text{定義 1}}{\in}& K
  \end{gather*}$$

  * $a$ : $GF(p)$ 的元素 (An element of $GF(p)$) $[a \in GF(p)]$

+++

## 證明:

### (a) proof that the root set is a field with exactly p to the n elements

**$K$ 是體**：由【推導 1】$L$ 的特徵是 $p$，套【已知 2(a)】。**$K$ 恰有 $p^n$ 個元素**：由【已知 3】根兩兩相異：

$$\begin{gather*}
K &\overset{\text{推導 1,已知 2(a)}}{=}& L \text{ 的子體} \\
K &\overset{\text{定義 1,假設 1}}{=}& \left\{\alpha_1, \dots, \alpha_{p^n}\right\} \\
\left|K\right| &\overset{\text{已知 3}}{=}& p^n
\end{gather*}$$

故恰有 $p^n$ 個元素的體存在。與補充講義 Theorem 7.24 一致。

### (b) proof that the root set is the splitting field

$K$ 含 $GF(p)$（【推導 2】）與 $x^{p^n} - x$ 的全部根（【定義 1】），而任何含這些根的體都含 $K$（$K$ 就是根的集合）：

$$\begin{gather*}
GF(p) &\overset{\text{推導 2}}{\subseteq}& K \\
\left\{\alpha_1, \dots, \alpha_{p^n}\right\} &\overset{\text{定義 1}}{=}& K \\
M \supseteq \left\{\alpha_1, \dots, \alpha_{p^n}\right\} &\Longrightarrow& M \supseteq K \\
K &\overset{\text{已知 1(b)}}{=}& x^{p^n} - x \ \text{在 } GF(p) \text{ 上的分裂體}
\end{gather*}$$

與投影片 p.34「The splitting field of $x^{p^n} - x$ over $GF_p$ consists precisely of its $p^n$ distinct roots」一致。

* 註：一般的分裂體比根集大（要加上根的和、積、商），但 $x^{p^n} - x$ 的根集**自己就對四則運算封閉**（【已知 2(a)】），
  所以不必再加任何東西 —— 這是這個多項式最特別的地方。

### (c) proof of the degree over the prime field

$K$ 是有限體，由【已知 4】其階為 $p^{\left[K : P\right]}$，而 $P = GF(p)$：

$$\begin{gather*}
p^n &\overset{\text{證明 (a)}}{=}& \left|K\right| \\
\left|K\right| &\overset{\text{已知 4}}{=}& p^{\left[K : GF(p)\right]} \\
\left[K : GF(p)\right] &=& n
\end{gather*}$$

* 註：這說明 $K$ 作為 $GF(p)$ 上的向量空間是 $n$ 維的 —— 與 [GF(p^n) 的構造](../Construction/Construction_of_GF_p_n.md) 用 $n$ 次不可約多項式造出來的體**維數相同**。
  兩者同構這件事見 [$GF(p^n)$ 的唯一性](Uniqueness_of_GF_p_n.md)。

+++

## 意義與密碼學關聯 (Interpretation and Relevance to Cryptography)

### 存在性證明的三塊積木

$$\underbrace{\text{分裂體存在}}_{\text{Kronecker}} \ + \ \underbrace{\text{根集是子體}}_{\text{新生之夢}} \ + \ \underbrace{\text{根兩兩相異}}_{\text{形式導數} = -1} \ \Longrightarrow \ \left|K\right| = p^n$$

三塊缺一不可：沒有新生之夢，根集不對加法封閉；沒有形式導數，可能有重根而少於 $p^n$ 個元素。

### 「任意大小的二元體」

本檔保證 $GF(2^n)$ 對**每個** $n$ 都存在。密碼學用到的：

| $n$ | 用途 |
|---|---|
| $8$ | AES 的位元組運算 |
| $128$ | AES-GCM 的 GHASH 認證 |
| $163, 233, 283, 409, 571$ | NIST 二元橢圓曲線 B-163 … B-571 |
| $2^{k}$ 形式的塔 | 零知識證明系統（Binius）的二元塔體 |

但「存在」只是理論保證；實作還需要一個**具體的** $n$ 次不可約多項式當模數 ——
那由 [$x^{p^n}-x$ 的分解](../Multiplicative_Group/Factorization_of_x_p_n_minus_x.md) 保證存在，由標準（NIST、IEEE 1363）指定。
