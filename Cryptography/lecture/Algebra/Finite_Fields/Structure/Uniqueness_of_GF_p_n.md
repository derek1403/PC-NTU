# Uniqueness of GF(p^n) (GF(p^n) 的唯一性)

+++

## 證明目標:

`FiniteFields.pdf` p.36；補充講義 §7.8.3（Theorem 7.16、7.18）。
**同樣大小的有限體只有一個**（同構意義下）。這是記號 $GF(p^n)$ 合法的理由，
也是 AES 可以任選一個八次不可約多項式而不改變數學結構的理由。

* (a) 補充講義 Theorem 7.16：任何 $p^n$ 元素的體 $F$ 都同構於某個「模 $n$ 次不可約多項式」的商環：

$$F \cong GF(p)[x]\big/\left\langle f \right\rangle, \qquad f \ \text{為 } n \text{ 次質多項式}$$

* (b) 投影片 p.36 的 Theorem 與補充講義 Theorem 7.18：

$$\left|F\right| = \left|F'\right| = p^n \quad \Longrightarrow \quad F \cong F'$$

* (c) 投影片 p.36 的 Remark：$GF(p^n)$ 是 $GF(p)$ 上的向量空間，基底為 $\left\{x^{n-1}, x^{n-2}, \dots, x, 1\right\}$。

* (d) 推論：投影片 p.18、p.22 的同構

$$\tfrac{GF(2)[x]}{\left\langle x^3 + x^2 + 1 \right\rangle} \cong \tfrac{GF(2)[x]}{\left\langle x^3 + x + 1 \right\rangle}, \qquad \tfrac{GF(2)[x]}{\left\langle x^4 + x + 1 \right\rangle} \cong \tfrac{GF(2)[x]}{\left\langle x^4 + x^3 + 1 \right\rangle} \cong \tfrac{GF(2)[x]}{\left\langle x^4 + x^3 + x^2 + x + 1 \right\rangle}$$

* $F,\ F'$ : 兩個 $p^n$ 元素的體 (Two fields with $p^n$ elements) $[\text{體}]$
* $f$ : $n$ 次質多項式 (A prime polynomial of degree $n$) $[f \in GF(p)[x]]$
* $\omega$ : $F$ 的本原元 (A primitive element of $F$) $[\omega \in F^*]$
* $\beta$ : $f$ 在 $F'$ 中的一個根 (A root of $f$ in $F'$) $[\beta \in F']$
* 註：同構時兩個體的質子體 $GF(p)$ 彼此對應（$1 \mapsto 1$ 迫使 $k \cdot 1 \mapsto k \cdot 1$），
  故「$f$ 的係數在 $F'$ 中」有意義：係數看成 $F'$ 的質子體元素（[有限體的階](Order_of_a_Finite_Field.md)【證明 (a)】）。
* 註：投影片 p.36 同時說「which is the splitting field of $x^{p^n} - x$ over $GF_p$」—— 那是存在性的構造，見 [$GF(p^n)$ 的存在性](Existence_of_GF_p_n.md)【證明 (b)】。
  本檔證明**任何** $p^n$ 元素的體都同構於它。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [有限體的階與質子體 (Order of a finite field and the prime subfield)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Finite_Fields/Structure/Order_of_a_Finite_Field.html#b-proof-that-the-order-of-a-finite-field-is-a-prime-power)：** 已於本章 [有限體的階](Order_of_a_Finite_Field.md)【證明 (a)(b)】完整證明，此處直接引用不再重證

  $$\left|F\right| = p^n \quad \Longrightarrow \quad GF(p) \cong P \subseteq F, \qquad \left[F : P\right] = n$$

  * $P$ : $F$ 的質子體 (The prime subfield of $F$) $[P \subseteq F]$

* **【已知 2】 [有限體的乘法群是循環群 (The multiplicative group of a finite field is cyclic)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Finite_Fields/Multiplicative_Group/Cyclic_Multiplicative_Group_of_Finite_Field.html#b-proof-that-the-multiplicative-group-of-a-finite-field-is-cyclic)：** 已於本章 [有限體的乘法群是循環群](../Multiplicative_Group/Cyclic_Multiplicative_Group_of_Finite_Field.md)【證明 (b)】完整證明，此處直接引用不再重證

  $$F^* = \left\langle \omega \right\rangle = \left\{\omega^0, \omega^1, \dots, \omega^{p^n - 2}\right\}$$

* **【已知 3】 [極小多項式 (Minimal polynomial)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Finite_Fields/Multiplicative_Group/Minimal_Polynomial.html#d-proof-that-adjoining-the-element-gives-a-field-of-degree-equal-to-the-degree-of-the-minimal-polynomial)：** 已於本章 [極小多項式](../Multiplicative_Group/Minimal_Polynomial.md)【證明 (b)(c)(d)】完整證明，此處直接引用不再重證

  * (a) 首一不可約的零化多項式就是極小多項式：

    $$h \ \text{首一不可約},\ h(u) = 0 \quad \Longrightarrow \quad h = g_u$$

  * (b) 生成的子體與商環同構，且次數受控：

    $$GF(p)[u] \cong GF(p)[x]\big/\left\langle g_u \right\rangle, \qquad \left|GF(p)[u]\right| = p^{\deg g_u}, \qquad \deg g_u \le \left[K : GF(p)\right]$$

  * (c) 極小多項式不可約：

    $$g_u \ \text{為質多項式}$$

  * $u$ : 有限體 $K$ 中的元素 (An element of a finite field $K$) $[u \in K]$
  * $g_u$ : $u$ 的極小多項式 (The minimal polynomial of $u$) $[g_u \in GF(p)[x]]$

* **【已知 4】 [次數整除 n 的質多項式整除 x^{p^n} − x (Prime polynomials of degree dividing n divide x^{p^n} − x)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Finite_Fields/Multiplicative_Group/Factorization_of_x_p_n_minus_x.html#a-proof-that-every-prime-polynomial-of-degree-dividing-n-divides-x-to-the-p-to-the-n-minus-x)：** 已於本章 [$x^{p^n}-x$ 的分解](../Multiplicative_Group/Factorization_of_x_p_n_minus_x.md)【證明 (a)】完整證明，此處直接引用不再重證

  $$f \ \text{質多項式},\ \deg f \mid n \quad \Longrightarrow \quad f \ \Big|\ x^{p^n} - x$$

* **【已知 5】 [x^q − x 在 GF(q) 上完全分解 (x^q − x splits over GF(q))](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Finite_Fields/Structure/Roots_of_x_q_minus_x.html#b-proof-that-the-field-is-exactly-the-root-set-of-x-to-the-q-minus-x)：** 已於本章 [$x^q - x$ 的根](Roots_of_x_q_minus_x.md)【證明 (b)】完整證明，此處直接引用不再重證

  $$x^{p^n} - x = \prod_{b \in F'}\left(x - b\right) \qquad \left(\left|F'\right| = p^n\right)$$

  * $b$ : $F'$ 的元素 (Elements of $F'$) $[b \in F']$

* **【已知 6】 [多項式的唯一分解 (Unique factorization of polynomials)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Finite_Fields/Polynomial_Arithmetic/Unique_Factorization_of_Polynomials.html#c-proof-of-the-uniqueness-of-the-factorization)：** 已於本章 [多項式的唯一分解](../Polynomial_Arithmetic/Unique_Factorization_of_Polynomials.md)【證明 (c)】完整證明，此處直接引用不再重證。套在 $F'[x]$ 上

  $$f \ \Big|\ \prod_{b \in F'}\left(x - b\right),\ \deg f \ge 1 \quad \Longrightarrow \quad \left(x - \beta\right) \mid f \ \text{ for some } \beta \in F'$$

* **【已知 7】 [商環的基底 (The basis of the quotient)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Field/Quotient_by_Irreducible_is_Field.html#b-proof-of-the-degree-of-the-extension)：** 已於 [模不可約多項式的商環是體](../../Abstract_Algebra/Field/Quotient_by_Irreducible_is_Field.md)【證明 (b)】完整證明，此處直接引用不再重證

  $$\left\{1,\ \left[x\right],\ \dots,\ \left[x\right]^{n-1}\right\} \ \text{是 } GF(p)[x]/\left\langle f \right\rangle \text{ 在 } GF(p) \text{ 上的基底}$$

* **【已知 8】 [GF(8) 與 GF(16) 的商環都是體 (The cubic and quartic quotients are fields)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Finite_Fields/Construction/Galois_Fields_GF8_and_GF16.html#a-verify-that-both-cubic-quotients-are-fields-with-eight-elements)：** 已於本章 [伽羅瓦體 GF(8) 與 GF(16)](../Construction/Galois_Fields_GF8_and_GF16.md)【已知 2】【證明 (a)(e)】驗證，此處直接引用

  $$\left|\tfrac{GF(2)[x]}{\left\langle \text{三次質多項式} \right\rangle}\right| = 8, \qquad \left|\tfrac{GF(2)[x]}{\left\langle \text{四次質多項式} \right\rangle}\right| = 16$$

* **【假設 1】 兩個同樣大小的有限體 (Two finite fields of the same size)：**

  $$\left|F\right| = \left|F'\right| = p^n$$

  * $F,\ F'$ : 有限體 (Finite fields) $[\text{體}]$

* **【推導 1】 本原元的極小多項式是 $n$ 次 (The minimal polynomial of a primitive element has degree n)：** 取 $F^* = \left\langle \omega \right\rangle$、$f = g_\omega$

  $$\begin{gather*}
  \deg f &\overset{\text{已知 3(b),已知 1}}{\le}& \left[F : GF(p)\right] = n \\
  GF(p)[\omega] &\overset{\text{已知 2}}{\supseteq}& \left\{0\right\} \cup \left\{\omega^k\right\} = F \\
  p^{\deg f} = \left|GF(p)[\omega]\right| &\ge& \left|F\right| = p^n \\
  \deg f &=& n \\
  GF(p)[\omega] &=& F
  \end{gather*}$$

  * $f$ : $\omega$ 的極小多項式 (The minimal polynomial of $\omega$) $[f \in GF(p)[x]]$
  * 註：與 [$x^{p^n}-x$ 的分解](../Multiplicative_Group/Factorization_of_x_p_n_minus_x.md)【證明 (e)】的論證相同，這裡對**任意** $p^n$ 元素的體 $F$ 使用。

+++

## 證明:

### (a) proof that every finite field is a quotient by a prime polynomial

由【假設 1】取 $F$ 的本原元 $\omega$ 與其極小多項式 $f$：

$$\begin{gather*}
F &\overset{\text{推導 1}}{=}& GF(p)[\omega] \\
F &\overset{\text{已知 3(b)}}{\cong}& GF(p)[x]\big/\left\langle f \right\rangle \\
f &\overset{\text{已知 3(c),推導 1}}{=}& n \ \text{次質多項式}
\end{gather*}$$

與補充講義 Theorem 7.16 一致。**特別地，這給出第二個「有限體的階必為質數冪」的證明**（補充講義的路線）。

### (b) proof that two fields of the same order are isomorphic

取 (a) 的 $f$。它是 $n$ 次質多項式，故整除 $x^{p^n} - x$，而後者在 $F'$ 中完全分解，所以 $f$ 在 $F'$ 中有根 $\beta$：

$$\begin{gather*}
f &\overset{\text{已知 4}}{\mid}& x^{p^n} - x \\
x^{p^n} - x &\overset{\text{已知 5,假設 1}}{=}& \prod_{b \in F'}\left(x - b\right) \\
f(\beta) &\overset{\text{已知 6}}{=}& 0 \qquad \text{for some } \beta \in F'
\end{gather*}$$

$f$ 首一不可約且以 $\beta$ 為根，故它也是 $\beta$ 的極小多項式；$\beta$ 生成的子體與 $F'$ 一樣大，故就是 $F'$：

$$\begin{gather*}
f &\overset{\text{已知 3(a)}}{=}& g_\beta \\
GF(p)[\beta] &\overset{\text{已知 3(b)}}{\cong}& GF(p)[x]\big/\left\langle f \right\rangle \\
\left|GF(p)[\beta]\right| &\overset{\text{已知 3(b)}}{=}& p^n = \left|F'\right| \\
GF(p)[\beta] &=& F' \qquad \text{(子集且等大)}
\end{gather*}$$

把兩條同構接起來：

$$F \overset{\text{證明 (a)}}{\cong} GF(p)[x]\big/\left\langle f \right\rangle \overset{\text{已知 3(b)}}{\cong} F'$$

與投影片 p.36「any two fields with $p^n$ elements are isomorphic」一致。

* 註：同構映射很具體：$\omega^k \mapsto \beta^k$（把 $F$ 的本原元送到 $f$ 在 $F'$ 中的一個根）。
  $f$ 在 $F'$ 中有 $n$ 個根（共軛元），選哪一個都行 —— 所以同構**不唯一**，共有 $n$ 個（伽羅瓦群的大小）。

### (c) proof that the powers of x form a basis

由 (a)，$GF(p^n) \cong GF(p)[x]/\left\langle f \right\rangle$，套【已知 7】：

$$\left\{x^{n-1}, x^{n-2}, \dots, x, 1\right\} \overset{\text{已知 7}}{=} GF(p^n) \ \text{在 } GF(p) \text{ 上的基底}$$

與投影片 p.36 的 Remark 一致（投影片把 $\left[x\right]^i$ 簡寫成 $x^i$）。

### (d) proof of the isomorphisms among the quotients of the same degree

由【已知 8】，兩個三次商環都是 $8$ 元素的體、三個四次商環都是 $16$ 元素的體；套【證明 (b)】：

$$\begin{gather*}
\tfrac{GF(2)[x]}{\left\langle x^3 + x^2 + 1 \right\rangle} &\overset{\text{已知 8,證明 (b)}}{\cong}& \tfrac{GF(2)[x]}{\left\langle x^3 + x + 1 \right\rangle} \\
\tfrac{GF(2)[x]}{\left\langle x^4 + x + 1 \right\rangle} \cong \tfrac{GF(2)[x]}{\left\langle x^4 + x^3 + 1 \right\rangle} &\overset{\text{已知 8,證明 (b)}}{\cong}& \tfrac{GF(2)[x]}{\left\langle x^4 + x^3 + x^2 + x + 1 \right\rangle}
\end{gather*}$$

與投影片 p.18、p.22 的「$\cong$」一致。

* 註：具體的同構：在 $GF(2)[x]/\left\langle x^3 + x + 1 \right\rangle$ 中，$x^3 + x^2 + 1$ 的根是 $\alpha^3 = \alpha + 1$
  （[伽羅瓦體 GF(8) 與 GF(16)](../Construction/Galois_Fields_GF8_and_GF16.md)【證明 (d)】），
  故 $\left[x\right] \mapsto \alpha + 1$ 給出 $GF(2)[x]/\left\langle x^3 + x^2 + 1 \right\rangle \to GF(2)[x]/\left\langle x^3 + x + 1 \right\rangle$ 的同構。

+++

## 意義與密碼學關聯 (Interpretation and Relevance to Cryptography)

### 「$GF(2^8)$」只有一個，「AES 的 $GF(2^8)$」是一種座標

(b) 說：所有 $256$ 元素的體都同構。AES 選 $x^8 + x^4 + x^3 + x + 1$，只是選了一組**座標**（基底 $\left\{1, x, \dots, x^7\right\}$ 配上這個模數）。
換一個八次質多項式，就是換一組座標 —— 數學結構完全相同，但**位元組的數值會變**。

因此：

* AES 的標準向量（test vectors）綁定在這組座標上，實作者**不能**任意換模數；
* 但實作**內部**可以換到方便的座標（例如塔式基底 $GF\!\left(\left(2^4\right)^2\right)$）計算，最後再換回來 —— 同構保證結果一致。
  這就是 Canright、Boyar–Peralta 等最小面積 AES S-box 電路的原理。

### 同構 $\ne$ 可以忽視的安全性差異

數學上同構，不代表所有表示在**實作安全性**上等價：

* 某些模數讓約化步驟更少、更容易做成常數時間；
* 橢圓曲線的 $GF(2^n)$ 表示若選到「特殊」的模數，某些攻擊（如 Weil descent）的適用性可能不同。

但這些差異都在**計算與實作**層面，不在代數結構層面。

### 有限體分類完成

| 問題 | 答案 | 出處 |
|---|---|---|
| 有限體可以有幾個元素？ | 恰好是質數冪 $p^n$ | [有限體的階](Order_of_a_Finite_Field.md) |
| 每個 $p^n$ 都有嗎？ | 有 | [$GF(p^n)$ 的存在性](Existence_of_GF_p_n.md) |
| 同樣大小的有幾個？ | 同構意義下一個 | **本檔** |
| 怎麼具體造出來？ | 模一個 $n$ 次質多項式 | [GF(p^n) 的構造](../Construction/Construction_of_GF_p_n.md) |

投影片 p.2「The finite fields are completely known」至此完整證明。
