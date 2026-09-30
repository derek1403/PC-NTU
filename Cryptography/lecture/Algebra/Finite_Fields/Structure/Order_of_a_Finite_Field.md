# Order of a Finite Field (有限體的階)

+++

## 證明目標:

**本檔內容只出現在補充講義** `Introduction_to_Finite_Fields.pdf` §7.4.2（Theorem 7.7）與 §7.8（Theorem 7.16 的結論、Exercise 13）；
投影片 p.36 只說「$GF(p^n)$ 有 $p^n$ 個元素」，沒有證明**有限體的元素個數只能是質數冪**。
[Abstract_Algebra 定理索引](../../Abstract_Algebra/theorems_index.md) 將「有限體的階必為質數冪」列為**未證明**，本檔補證。

* (a) 質子體（補充講義 Theorem 7.7）：任何有限體都含一份 $GF(p)$，$p$ 為其特徵：

$$P = \left\{0,\ 1_F,\ 2 \cdot 1_F,\ \dots,\ \left(p-1\right) \cdot 1_F\right\} \ \text{是 } F \text{ 的子體}, \qquad P \cong GF(p)$$

* (b) 有限體的階是質數冪：

$$\left|F\right| < \infty \quad \Longrightarrow \quad \left|F\right| = p^n, \qquad n = \left[F : P\right]$$

* (c) 補充講義 Exercise 13 的「不存在」部分：$1 \le q \le 12$ 中，$q = 1, 6, 10, 12$ 沒有 $q$ 元素的體。

* $F$ : 有限體 (A finite field) $[\text{體}]$
* $p$ : $F$ 的特徵 (The characteristic of $F$) $[p \in \mathbf{P},\ \text{質數}]$
* $P$ : $F$ 的質子體 (The prime subfield of $F$) $[P \subseteq F]$
* $n$ : $F$ 對 $P$ 的擴張次數 (The degree of $F$ over $P$) $[n \in \mathbf{P}]$
* $1_F$ : $F$ 的乘法單位元素 (The multiplicative identity) $[1_F \in F]$
* 註：Exercise 13 的「存在」部分（$q = 2, 3, 4, 5, 7, 8, 9, 11$ 都有體）由
  [$GF(p^n)$ 的存在性](Existence_of_GF_p_n.md) 給出，本檔不涉及以免前向引用。
* 註：補充講義證明 (b) 的路線是「每個有限體都同構於某個 $\mathbb{F}_{g(x)}$」（需要本原元與極小多項式）；
  本檔改走**向量空間計數**，只用到特徵與線性代數，短得多。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [有限體的特徵是質數 (The characteristic of a finite field is prime)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Field/Characteristic_of_a_Field.html#d-proof-that-a-finite-field-has-positive-characteristic)：** 已於 [體的特徵](../../Abstract_Algebra/Field/Characteristic_of_a_Field.md)【定義 1】【證明 (b)(d)】完整證明，此處直接引用不再重證

  * (a) 特徵的定義（即 $1_F$ 的加法階）：

    $$\mathrm{ch}(F) = \min\left\{p \in \mathbf{P} \ \middle|\ p \cdot 1_F = 0\right\}$$

  * (b) 有限體的特徵是質數：

    $$\left|F\right| < \infty \quad \Longrightarrow \quad \mathrm{ch}(F) = p \ \text{為質數}$$

  * $\mathrm{ch}(F)$ : $F$ 的特徵 (The characteristic) $[\mathrm{ch}(F) \in \mathbf{N}]$

* **【已知 2】 [倍數可以化簡到 0 與 p−1 之間 (Reducing multiples modulo the order)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Group/Order_of_Element_and_Cyclic_Subgroup.html#assumptions-preliminaries)：** 已於 [元素的階與循環子群](../../Abstract_Algebra/Group/Order_of_Element_and_Cyclic_Subgroup.md)【推導 2】完整證明，此處直接引用不再重證。以加法記號、$g = 1_F$、$o(1_F) = p$ 寫出

  * (a) 化簡：

    $$m \cdot 1_F = \left(m \bmod p\right) \cdot 1_F$$

  * (b) 最小性：

    $$0 < r < p \quad \Longrightarrow \quad r \cdot 1_F \neq 0$$

  * $m$ : 整數 (An integer) $[m \in \mathbf{Z}]$
  * $r$ : 餘數 (A remainder) $[r \in \mathbf{Z}]$

* **【已知 3】 [整數倍與分配律 (Integer multiples and distributivity)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Ring/Ring_Definition.html#definitions-and-notation)：** 已於 [環的定義](../../Abstract_Algebra/Ring/Ring_Definition.md)【定義 2(c)】給出，此處直接引用

  $$k \cdot 1_F + l \cdot 1_F = \left(k + l\right) \cdot 1_F, \qquad \left(k \cdot 1_F\right)\left(l \cdot 1_F\right) = \left(kl\right) \cdot 1_F$$

  * $k,\ l$ : 整數 (Integers) $[k, l \in \mathbf{Z}]$

* **【已知 4】 [$\mathbf{Z}_p$ 是體 (The residues modulo a prime form a field)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Field/Field_Definition.html#b-proof-that-the-residues-modulo-a-prime-form-a-field)：** 已於 [體的定義](../../Abstract_Algebra/Field/Field_Definition.md)【證明 (b)】完整證明，此處直接引用不再重證

  $$p \ \text{為質數} \quad \Longrightarrow \quad \mathbf{Z}_p = GF(p) \ \text{為體}$$

  * $p$ : 質數 (A prime) $[p \in \mathbf{P}]$

* **【已知 5】 [子體判別法 (Subfield criterion)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Field/Subfield_and_Field_Extension.html#a-proof-of-the-subfield-criterion)：** 已於 [子體與體擴張](../../Abstract_Algebra/Field/Subfield_and_Field_Extension.md)【證明 (a)】完整證明，此處直接引用不再重證

  $$P \ \text{是 } F \text{ 的子體} \quad \Longleftrightarrow \quad \left|P\right| \ge 2, \quad u - v \in P, \quad uv^{-1} \in P \ \left(v \neq 0\right)$$

  * $u,\ v$ : $P$ 的元素 (Elements of $P$) $[u, v \in P]$

* **【已知 6】 [大體是小體上的向量空間 (The larger field is a vector space over the subfield)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Field/Subfield_and_Field_Extension.html#c-proof-that-the-larger-field-is-a-vector-space-over-the-subfield)：** 已於 [子體與體擴張](../../Abstract_Algebra/Field/Subfield_and_Field_Extension.md)【證明 (c)】及其文末完整證明，此處直接引用不再重證

  * (a) 向量空間結構：

    $$P \subseteq F \ \text{子體} \quad \Longrightarrow \quad F \ \text{是 } P \text{ 上的向量空間}$$

  * (b) 有限維時的元素個數（每個向量由 $n$ 個座標唯一決定）：

    $$\dim_P F = n \quad \Longrightarrow \quad \left|F\right| = \left|P\right|^{n}$$

  * $\dim_P F$ : $F$ 作為 $P$-向量空間的維數 (The dimension of $F$ over $P$) $[n \in \mathbf{N}]$

* **【已知 7】 [算術基本定理 (Fundamental theorem of arithmetic)](https://mathworld.wolfram.com/FundamentalTheoremofArithmetic.html)：** 初等數論的標準結果，直接引用不再重證

  $$\text{每個 } m \ge 2 \text{ 唯一地寫成質數冪之積}$$

  * $m$ : 正整數 (A positive integer) $[m \in \mathbf{P}]$

* **【定義 1】 質子體 (Prime subfield)：** 補充講義 §7.4.2「the integers of $\mathbb{F}_q$」

  $$P \overset{\text{def}}{=} \left\{k \cdot 1_F \ \middle|\ k \in \mathbf{Z}\right\}$$

  * $P$ : $1_F$ 的所有整數倍 (All integer multiples of $1_F$) $[P \subseteq F]$

* **【假設 1】 有限體 (A finite field)：**

  $$F \ \text{為體}, \qquad \left|F\right| < \infty$$

  * $F$ : 被研究的體 (The field under study) $[\text{體}]$

* **【推導 1】 $k \mapsto k \cdot 1_F$ 是 $GF(p)$ 到 $F$ 的單射同態 (An injective homomorphism from GF(p))：** 【證明 (a)】的樞紐。設 $p = \mathrm{ch}(F)$

  * (a) 良定義且單射（$0 \le l \le k < p$）：

    $$\begin{gather*}
    \phi(k) &\overset{\text{let}}{=}& k \cdot 1_F \\
    \phi(k) = \phi(l) &\overset{\text{已知 3}}{\Longrightarrow}& \left(k - l\right) \cdot 1_F = 0 \\
    0 \le k - l < p &\overset{\text{已知 2(b)}}{\Longrightarrow}& k - l = 0
    \end{gather*}$$

  * (b) 保加法與乘法（$\oplus, \otimes$ 為模 $p$ 運算）：

    $$\begin{gather*}
    \phi\left(k \oplus l\right) &\overset{\text{已知 2(a)}}{=}& \left(k + l\right) \cdot 1_F \\
    \phi\left(k \oplus l\right) &\overset{\text{已知 3}}{=}& \phi(k) + \phi(l) \\
    \phi\left(k \otimes l\right) &\overset{\text{已知 2(a)}}{=}& \left(kl\right) \cdot 1_F \\
    \phi\left(k \otimes l\right) &\overset{\text{已知 3}}{=}& \phi(k)\,\phi(l)
    \end{gather*}$$

  * $\phi$ : 嵌入映射 (The embedding) $[\mathbf{Z}_p \to F]$
  * $k,\ l$ : $\mathbf{Z}_p$ 的元素 (Elements of $\mathbf{Z}_p$) $[k, l \in \left\{0, \dots, p-1\right\}]$
  * 註：與 [質體 GF(p)](../Polynomial_Arithmetic/Prime_Field_GF_p.md)【證明 (c)】是同一個映射；
    那裡 $\left|F\right| = p$ 使它成為雙射，這裡 $F$ 可能更大，只得到單射。

+++

## 證明:

### (a) proof that every finite field contains a copy of the prime field

由【假設 1】與【已知 1(b)】，$p = \mathrm{ch}(F)$ 是質數。由【已知 2(a)】，每個整數倍都化簡成 $0$ 到 $p-1$ 倍之一：

$$\begin{gather*}
p = \mathrm{ch}(F) &\overset{\text{假設 1,已知 1(a)(b)}}{=}& \text{質數} \\
P &\overset{\text{定義 1}}{=}& \left\{k \cdot 1_F \ \middle|\ k \in \mathbf{Z}\right\} \\
P &\overset{\text{已知 2(a)}}{=}& \left\{0,\ 1_F,\ \dots,\ \left(p-1\right) \cdot 1_F\right\} = \phi\left(\mathbf{Z}_p\right) \\
\left|P\right| &\overset{\text{推導 1(a)}}{=}& p \ge 2
\end{gather*}$$

**$P$ 是子體**：減法與除法都能拉回 $\mathbf{Z}_p$ 中計算。對 $u = \phi(k)$、$v = \phi(l) \neq 0$（故 $l \neq 0$，$l^{-1}$ 在 $\mathbf{Z}_p$ 中存在）：

$$\begin{gather*}
u - v &\overset{\text{推導 1(b)}}{=}& \phi\left(k \ominus l\right) \in P \\
v \cdot \phi\left(l^{-1}\right) &\overset{\text{推導 1(b)}}{=}& \phi\left(l \otimes l^{-1}\right) = \phi(1) = 1_F \\
uv^{-1} = \phi(k)\,\phi\left(l^{-1}\right) &\overset{\text{推導 1(b),已知 4}}{=}& \phi\left(k \otimes l^{-1}\right) \in P \\
P &\overset{\text{已知 5}}{=}& F \text{ 的子體}
\end{gather*}$$

$\phi : \mathbf{Z}_p \to P$ 是保運算的雙射，故 $P \cong \mathbf{Z}_p = GF(p)$。與補充講義 Theorem 7.7 一致。

### (b) proof that the order of a finite field is a prime power

由【證明 (a)】$P$ 是 $F$ 的子體，故 $F$ 是 $P$ 上的向量空間；$F$ 本身是有限的生成集，故維數有限，記為 $n$：

$$\begin{gather*}
F &\overset{\text{已知 6(a)}}{=}& P \text{ 上的向量空間} \\
n &\overset{\text{let}}{=}& \dim_P F = \left[F : P\right] < \infty \\
\left|F\right| &\overset{\text{已知 6(b)}}{=}& \left|P\right|^{n} \\
\left|F\right| &\overset{\text{證明 (a)}}{=}& p^{n}
\end{gather*}$$

* 註：$n \ge 1$，因為 $F \supseteq P \neq \left\{0\right\}$。
* 註：這條定理回答了「為什麼沒有 $6$ 元素的體」—— 不是找不到，是**不可能**：
  任何有限體都是某個 $GF(p)$ 上的向量空間，大小只能是 $p$ 的冪。

### (c) disprove the existence of fields of orders one six ten and twelve

**$q = 1$**：體的定義要求 $0 \neq 1$，故至少兩個元素。**$q = 6, 10, 12$**：由【已知 7】分解，都含兩個相異質因數，不是質數冪：

$$\begin{gather*}
6 &\overset{\text{已知 7}}{=}& 2 \cdot 3 \\
10 &\overset{\text{已知 7}}{=}& 2 \cdot 5 \\
12 &\overset{\text{已知 7}}{=}& 2^2 \cdot 3 \\
q \in \left\{6, 10, 12\right\} &\overset{\text{證明 (b)}}{\neq}& p^n
\end{gather*}$$

故這四個 $q$ 都沒有體。其餘 $q = 2, 3, 4, 5, 7, 8, 9, 11$ 都是質數冪。

+++

## 意義與密碼學關聯 (Interpretation and Relevance to Cryptography)

### 有限體的完整分類，第一步

有限體的分類定理由三塊拼成：

| 定理 | 本章出處 |
|---|---|
| 大小只能是 $p^n$ | **本檔 (b)** |
| 每個 $p^n$ 都有 | [$GF(p^n)$ 的存在性](Existence_of_GF_p_n.md) |
| 同樣大小的都同構 | [$GF(p^n)$ 的唯一性](Uniqueness_of_GF_p_n.md) |

三塊拼完，「有限體」就被 $\left(p, n\right)$ 兩個整數完全刻畫 —— 投影片 p.2 所說的「The finite fields are completely known」。

### 為什麼密碼學只看到 $GF(p)$ 與 $GF(2^n)$

(b) 說每個有限體都長在某個 $GF(p)$ 上。實務上：

* **$GF(p)$，$p$ 很大**：RSA 以外的公鑰系統（DH、ECDSA over P-256、EdDSA）；
* **$GF(2^n)$**：對稱密碼（AES、GCM）、二元曲線 ECC、糾錯碼；
* **$GF(p^n)$，$p$ 很大、$n$ 小**：配對密碼學的 $GF(p^{12})$。

「$256$ 元素的體」、「$2^{128}$ 元素的體」可以有，但「$10^{6}$ 元素的體」就不存在 ——
設計參數時要記得 (b)。

### 質子體就是「整數」

補充講義把 $P$ 稱為「the integers of $\mathbb{F}_q$」：在 $GF(2^8)$ 裡，$P = \left\{0, 1\right\}$；
在 $GF(3^5)$ 裡，$P = \left\{0, 1, 2\right\}$。所有其他元素都是 $P$-係數的「向量」。
AES 的位元組正是 $GF(2)$ 上的 $8$ 維向量 —— **位元**就是質子體的元素。
