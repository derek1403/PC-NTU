# Roots of Polynomials (多項式的根)

+++

## 證明目標:

`FiniteFields.pdf` p.34（下半）–p.35；補充講義 §7.7.1（Theorem 7.10、7.11）。
「$n$ 次多項式最多 $n$ 個根」看似中學常識，但它**只在體（整環）上成立** ——
而它正是「$GF(q)^*$ 是循環群」的證明支柱。

* (a) 因式定理（[不可約多項式](../../Abstract_Algebra/Field/Irreducible_Polynomial.md)【已知 2】當時引用未證，本檔補證）：

$$f(\alpha) = 0 \quad \Longleftrightarrow \quad \left(x - \alpha\right) \mid f(x)$$

* (b) 投影片 p.34 的 Proposition 與 p.35 的 Remark：

$$f \in F[x],\ f \neq 0,\ \deg f = n \quad \Longrightarrow \quad f \ \text{在 } F \text{ 中最多有 } n \text{ 個相異根}$$

* (c) 補充講義 Theorem 7.10 的後半：首一 $n$ 次多項式若有 $n$ 個相異根 $\beta_1, \dots, \beta_n$，則

$$f(x) = \left(x - \beta_1\right)\left(x - \beta_2\right)\cdots\left(x - \beta_n\right)$$

* (d) 投影片 p.35 的 Example：**係數環不是體時 (b) 失敗** ——

$$\text{在 } \mathbf{Z}_8 \text{ 中}, \quad x^2 - 1 \ \text{有四個根} \ 1, 3, 5, 7$$

* (e) 補充講義 Theorem 7.11：體的乘法群 $F^*$ 對每個 $n$ **最多只有一個** $n$ 階循環子群；
  若 $S = \left\{1, \beta, \dots, \beta^{n-1}\right\}$ 是一個，則

$$x^n - 1 = \prod_{s \in S}\left(x - s\right)$$

* $F$ : 體 (A field) $[\text{體}]$
* $f$ : 多項式 (A polynomial) $[f \in F[x]]$
* $\alpha,\ \beta,\ \beta_i$ : 體元素 (Field elements) $[\in F]$
* $n$ : 次數或子群的階 (The degree, or the order of the subgroup) $[n \in \mathbf{N}]$
* $S$ : $F^*$ 的 $n$ 階循環子群 (A cyclic subgroup of order $n$ in $F^*$) $[S \le F^*]$
* 註：**投影片 p.35 的 Remark「any polynomial $f(x) \in F[x]$ has at most $n$ roots」漏寫了「$f \neq 0$、$\deg f = n$」**
  （零多項式以體的每個元素為根）。本檔 (b) 補上。
* 註：補充講義把 (b)(c) 稱為「Fundamental theorem of algebra」，這是講義的用語；
  它與一般所說「$\mathbf{C}$ 代數封閉」的代數基本定理**不是**同一條定理。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [多項式的除法原理 (Division algorithm for polynomials)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Finite_Fields/Polynomial_Arithmetic/Division_Algorithm_for_Polynomials.html#a-proof-of-the-existence-of-the-quotient-and-remainder)：** 已於本章 [多項式的除法原理](Division_Algorithm_for_Polynomials.md)【證明 (a)】完整證明，此處直接引用不再重證

  $$f = \left(x - \alpha\right)q + r, \qquad r = 0 \ \text{或} \ \deg r < 1 \ \ \text{（即 } r \in F\text{）}$$

  * $q$ : 商式 (The quotient) $[q \in F[x]]$
  * $r$ : 餘式，為常數 (The remainder, a constant) $[r \in F]$

* **【已知 2】 [代入是環同態 (Evaluation is a ring homomorphism)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Ring/Ring_Examples.html#e-verify-that-the-polynomials-form-a-ring)：** 已於 [環的例子](../../Abstract_Algebra/Ring/Ring_Examples.md) 與 [單擴張](../../Abstract_Algebra/Field/Simple_Extension.md)【已知 2(b)】給出，此處直接引用

  $$\left(f + g\right)(\beta) = f(\beta) + g(\beta), \qquad \left(fg\right)(\beta) = f(\beta)\,g(\beta)$$

  * $f,\ g$ : 多項式 (Polynomials) $[f, g \in R[x]]$
  * $\beta$ : 代入的值 (The value substituted) $[\beta \in R]$
  * $R$ : 交換環 (A commutative ring) $[\text{環}]$

* **【已知 3】 [次數相加 (Degrees add)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Finite_Fields/Polynomial_Arithmetic/Polynomial_Ring_over_a_Field.html#b-proof-that-degrees-add-in-the-polynomial-ring-over-a-field)：** 已於本章 [體上的多項式環](Polynomial_Ring_over_a_Field.md)【證明 (b)】完整證明，此處直接引用不再重證

  $$\deg\left(gh\right) = \deg g + \deg h$$

  * $g,\ h$ : 多項式 (Polynomials) $[g, h \in F[x]]$

* **【已知 4】 [體無零因子 (A field has no zero divisors)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Field/Field_Definition.html#d-proof-that-every-field-is-an-integral-domain)：** 已於 [體的定義](../../Abstract_Algebra/Field/Field_Definition.md)【證明 (d)】完整證明，此處直接引用不再重證

  $$ab = 0 \quad \Longrightarrow \quad a = 0 \ \text{或} \ b = 0$$

  * $a,\ b$ : 體元素 (Field elements) $[a, b \in F]$

* **【已知 5】 [數學歸納法 (Mathematical induction)](https://mathworld.wolfram.com/PrincipleofMathematicalInduction.html)：** 標準結果，直接引用不再重證

  $$P(0) \ \text{且} \ \left[P(n-1) \Rightarrow P(n)\right] \quad \Longrightarrow \quad P(n) \ \forall n \in \mathbf{N}$$

  * $P$ : 待證命題 (The statement to be proved) $[\mathbf{N} \to \left\{\text{真},\text{假}\right\}]$

* **【已知 6】 [循環子群的大小與指數律 (Size of a cyclic subgroup and exponent laws)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Group/Order_of_Element_and_Cyclic_Subgroup.html#a-proof-that-the-powers-of-an-element-form-a-subgroup-of-size-equal-to-the-order)：** 已於 [元素的階與循環子群](../../Abstract_Algebra/Group/Order_of_Element_and_Cyclic_Subgroup.md)【已知 1(b)】【證明 (a)】完整證明，此處直接引用不再重證

  * (a) 循環子群的大小等於生成元的階：

    $$\left|\left\langle \gamma \right\rangle\right| = o(\gamma)$$

  * (b) 指數律：

    $$\left(\beta^k\right)^n = \left(\beta^n\right)^k$$

  * $\gamma,\ \beta$ : 群元素 (Group elements) $[\gamma, \beta \in F^*]$
  * $k,\ n$ : 指數 (Exponents) $[k, n \in \mathbf{Z}]$

* **【定義 1】 根 (Root)：** 補充講義 §7.7.1

  $$\alpha \ \text{為 } f \text{ 的根} \quad \overset{\text{def}}{\Longleftrightarrow} \quad f(\alpha) = 0$$

  * $\alpha$ : 候選的根 (A candidate root) $[\alpha \in F]$
  * $f$ : 多項式 (A polynomial) $[f \in F[x]]$

* **【假設 1】 (b) 的歸納假設 (Induction hypothesis for (b))：**

  $$g \neq 0,\ \deg g = n - 1 \quad \Longrightarrow \quad g \ \text{最多有 } n - 1 \text{ 個根}$$

  * $g$ : 次數較低的非零多項式 (A non-zero polynomial of lower degree) $[g \in F[x]]$

* **【假設 2】 有 $n$ 個相異根的首一多項式 (A monic polynomial with n distinct roots)：** 【證明 (c)】的出發點

  $$f \ \text{首一}, \quad \deg f = n, \quad f(\beta_1) = \cdots = f(\beta_n) = 0, \quad \beta_i \ \text{兩兩相異}$$

  * $\beta_1, \dots, \beta_n$ : 相異的根 (Distinct roots) $[\beta_i \in F]$

* **【假設 3】 一個 $n$ 階循環子群 (A cyclic subgroup of order n)：** 【證明 (e)】的出發點

  $$S = \left\langle \beta \right\rangle = \left\{1, \beta, \beta^2, \dots, \beta^{n-1}\right\} \le F^*, \qquad \left|S\right| = n$$

  * $\beta$ : 生成元 (The generator) $[\beta \in F^*,\ o(\beta) = n]$
  * $S$ : $n$ 階循環子群 (The cyclic subgroup of order $n$) $[S \le F^*]$

* **【推導 1】 剝掉一個根後，其他根仍是商式的根 (Other roots survive in the quotient)：** 【證明 (b)(c)】共用

  $$\begin{gather*}
  f &=& \left(x - \alpha\right)q \\
  0 = f(\beta) &\overset{\text{已知 2}}{=}& \left(\beta - \alpha\right)q(\beta) \\
  \beta - \alpha &\neq& 0 \qquad \text{(} \beta \neq \alpha\text{)} \\
  q(\beta) &\overset{\text{已知 4}}{=}& 0
  \end{gather*}$$

  * $\alpha$ : 已剝掉的根 (The root already factored out) $[\alpha \in F]$
  * $\beta$ : 另一個根 (Another root) $[\beta \in F,\ \beta \neq \alpha]$
  * $q$ : 商式 (The quotient) $[q \in F[x]]$
  * 註：**整個檔案唯一需要「體」的地方就是這裡的【已知 4】**。【證明 (d)】會看到它在 $\mathbf{Z}_8$ 裡壞掉。

+++

## 證明:

### (a) proof of the factor theorem

對 $x - \alpha$ 做除法，餘式是常數；把 $x = \alpha$ 代進去：

$$\begin{gather*}
f &\overset{\text{已知 1}}{=}& \left(x - \alpha\right)q + r \\
f(\alpha) &\overset{\text{已知 2}}{=}& \left(\alpha - \alpha\right)q(\alpha) + r \\
f(\alpha) &=& r
\end{gather*}$$

故

$$\begin{gather*}
\alpha \ \text{為 } f \text{ 的根} &\overset{\text{定義 1}}{\Longleftrightarrow}& f(\alpha) = 0 \\
f(\alpha) = 0 &\Longleftrightarrow& r = 0 \\
r = 0 &\overset{\text{已知 1}}{\Longleftrightarrow}& \left(x - \alpha\right) \mid f
\end{gather*}$$

* 註：除式 $x - \alpha$ 是首一的，所以【已知 1】在這裡**對任意交換含單位元環都成立**，
  (a) 在 $\mathbf{Z}_8$ 裡照樣成立 —— 壞掉的是 (b)。

### (b) proof that a non-zero polynomial of degree n has at most n roots

對 $n$ 歸納（【已知 5】）。**基底** $n = 0$：$f$ 是非零常數，沒有根。
**歸納步驟**：若 $f$ 沒有根則已成立；否則取一根 $\alpha$：

$$\begin{gather*}
f &\overset{\text{證明 (a)}}{=}& \left(x - \alpha\right)q \\
\deg q &\overset{\text{已知 3}}{=}& n - 1 \\
\left\{f \text{ 的根}\right\} &\overset{\text{推導 1}}{\subseteq}& \left\{\alpha\right\} \cup \left\{q \text{ 的根}\right\} \\
\left|\left\{f \text{ 的根}\right\}\right| &\overset{\text{假設 1}}{\le}& 1 + \left(n - 1\right) \\
\left|\left\{f \text{ 的根}\right\}\right| &\le& n
\end{gather*}$$

$$\text{(b) 對所有 } n \in \mathbf{N} \ \text{成立} \quad \overset{\text{已知 5}}{\Longleftarrow} \quad \text{基底} + \text{歸納步驟}$$

與投影片「Use the Division Algorithm」的提示一致。

### (c) proof that n distinct roots determine the factorization

由【假設 2】，依序剝掉 $\beta_1, \beta_2, \dots$。第 $k$ 步後，由【推導 1】剩下的 $\beta_{k+1}, \dots, \beta_n$ 仍是商式的根：

$$\begin{gather*}
f &\overset{\text{證明 (a),假設 2}}{=}& \left(x - \beta_1\right)q_1 \\
q_1\!\left(\beta_2\right) &\overset{\text{推導 1}}{=}& 0 \\
f &\overset{\text{證明 (a)}}{=}& \left(x - \beta_1\right)\left(x - \beta_2\right)q_2 \\
f &=& \left(x - \beta_1\right)\cdots\left(x - \beta_n\right)q_n \\
\deg q_n &\overset{\text{已知 3}}{=}& n - n = 0 \\
q_n &=& 1 \qquad \text{(比較首項係數：} f \text{ 首一)}
\end{gather*}$$

故 $f = \prod_{i=1}^{n}\left(x - \beta_i\right)$，與補充講義 Theorem 7.10 一致。

### (d) disprove the root bound over the residues modulo eight

逐一代入 $\mathbf{Z}_8$ 的奇數：

$$\begin{gather*}
1^2 - 1 &=& 0 \\
3^2 - 1 &=& 8 \equiv 0 \\
5^2 - 1 &=& 24 \equiv 0 \\
7^2 - 1 &=& 48 \equiv 0
\end{gather*}$$

二次多項式有**四個**根，(b) 失敗。失敗點正是【推導 1】的最後一步 —— 取 $\alpha = 1$、$\beta = 3$：

$$\begin{gather*}
x^2 - 1 &=& \left(x - 1\right)\left(x + 1\right) \\
\left(3 - 1\right)\left(3 + 1\right) &=& 2 \cdot 4 = 8 \equiv 0 \\
3 - 1 = 2 \neq 0, \quad 3 + 1 &=& 4 \neq 0
\end{gather*}$$

$2 \cdot 4 = 0$ 但兩者皆非零 —— $\mathbf{Z}_8$ 有零因子（[零因子](../../Abstract_Algebra/Ring/Zero_Divisor.md)【證明 (b)】，$8$ 為合數），
所以不能從乘積為零推出某個因子為零。與投影片的「Note that $\mathbf{Z}_8$ is not a field」一致。

### (e) proof that a field has at most one cyclic subgroup of each order

由【假設 3】，$S$ 的每個元素都是 $x^n - 1$ 的根：

$$\begin{gather*}
\left(\beta^k\right)^n &\overset{\text{已知 6(b)}}{=}& \left(\beta^n\right)^k \\
\left(\beta^k\right)^n &\overset{\text{假設 3}}{=}& 1^k = 1
\end{gather*}$$

這是 $n$ 個相異的根，而 $x^n - 1$ 的次數為 $n$，由【證明 (b)】**它們就是全部的根**，且由【證明 (c)】：

$$x^n - 1 \overset{\text{證明 (c)}}{=} \prod_{s \in S}\left(x - s\right)$$

設 $T = \left\langle \gamma \right\rangle$ 是另一個 $n$ 階循環子群。同理 $T$ 的元素全是 $x^n - 1$ 的根，故落在 $S$ 裡：

$$\begin{gather*}
\left|T\right| = o(\gamma) &\overset{\text{已知 6(a)}}{=}& n \\
T &\overset{\text{證明 (b)}}{\subseteq}& \left\{x^n - 1 \text{ 的根}\right\} = S \\
\left|T\right| = \left|S\right| &\Longrightarrow& T = S
\end{gather*}$$

與補充講義 Theorem 7.11 一致。

* 註：**對比 $\mathbf{Z}_8^*$**：它的三個 $2$ 階子群 $\left\{1,3\right\}$、$\left\{1,5\right\}$、$\left\{1,7\right\}$ 彼此不同，
  正對應 (d) 中 $x^2 - 1$ 的根太多。這也是 $\mathbf{Z}_8^*$ 不循環的原因
  （[循環群](../../Abstract_Algebra/Group/Cyclic_Group.md)【證明 (e)】）。

+++

## 意義與密碼學關聯 (Interpretation and Relevance to Cryptography)

### (e) 是「$GF(q)^*$ 是循環群」的一半

[有限體的乘法群是循環群](../Multiplicative_Group/Cyclic_Multiplicative_Group_of_Finite_Field.md) 的證明分兩半：

1. **上界**：每個 $d$ 階元素都落在唯一的 $d$ 階循環子群裡，故 $d$ 階元素最多 $\varphi(d)$ 個 —— 本檔 (e)；
2. **計數**：$\sum_{d \mid q-1}\varphi(d) = q - 1$ 迫使每個上界都取等號。

沒有「最多 $n$ 個根」，第一半就不成立 —— $\mathbf{Z}_8^*$ 就是反例。

### 秘密分享的正確性也靠 (b)

Shamir $(t, n)$ 門檻秘密分享的安全性說：少於 $t$ 個分享**完全不洩漏**秘密。
證明的核心是「$t-1$ 次多項式由 $t$ 個點唯一決定」——
兩個 $t-1$ 次多項式若在 $t$ 個點相等，差是次數 $\le t-1$ 卻有 $t$ 個根的多項式，由 (b) 必為零。
**若在 $\mathbf{Z}_n$（$n$ 合數）上做，(b) 失敗，唯一性就沒了。**

### 程式思維

```python
roots = lambda coeffs, n: [a for a in range(n)
                            if sum(c * pow(a, i, n) for i, c in enumerate(coeffs)) % n == 0]
assert roots([-1, 0, 1], 8) == [1, 3, 5, 7]   # 證明 (d)：Z_8 中 4 個根
assert roots([-1, 0, 1], 7) == [1, 6]         # 體 Z_7 中最多 2 個
```
