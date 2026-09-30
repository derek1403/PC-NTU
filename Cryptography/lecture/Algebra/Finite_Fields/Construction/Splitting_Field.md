# Splitting Field (分裂體)

+++

## 證明目標:

`FiniteFields.pdf` p.27、p.31。要證明 $GF(p^n)$ 存在，得先有一個地方讓 $x^{p^n} - x$ 的根「住進去」。
本檔證明：**任何多項式都能在某個擴張體裡完全分解**，而且係數體有限時，那個擴張體也有限。

* (a) 投影片 p.31 的 Corollary（Kronecker 構造）：

$$f \in F[x],\ \deg f \ge 1 \quad \Longrightarrow \quad \exists \ \text{擴張體 } K \supseteq F \ \text{使 } f \text{ 在 } K \text{ 中有根}$$

  特別地，$F = GF(p)$ 時可取 $K = GF(p^n)$，$n$ 為 $f$ 的某個不可約因式的次數。

* (b) $f$ 能在某個擴張體 $L$ 中完全分解，且 $F$ 有限時 $L$ 也有限：

$$f = a\left(x - \alpha_1\right)\left(x - \alpha_2\right)\cdots\left(x - \alpha_n\right), \qquad \alpha_i \in L, \qquad \left[L : F\right] < \infty$$

* (c) 投影片 p.27 的 Definition 所說「包含 $f$ 所有根的最小體」存在（在 (b) 的 $L$ 之內）。

* $F$ : 基體 (The base field) $[\text{體}]$
* $f$ : 非常數多項式 (A non-constant polynomial) $[f \in F[x]]$
* $K,\ L$ : 擴張體 (Extension fields) $[F \subseteq K,\ F \subseteq L]$
* $\alpha_i$ : $f$ 的根 (The roots of $f$) $[\alpha_i \in L]$
* $a$ : $f$ 的首項係數 (The leading coefficient of $f$) $[a \in F \setminus \left\{0\right\}]$
* 註：**投影片 p.31 的證明寫「For $x \in GF_{p^n}$, $\left(f(x) \bmod q(x)\right) \bmod p = 0$」**，
  字面上像是說 $GF(p^n)$ 的**每個**元素都是根，這不對；正確的意思是**那個特定元素** $\left[x\right]$（$x$ 的同餘類）是根。本檔 (a) 照正確意思寫。
* 註：本檔的「分裂體」是相對於某個已知的大體 $L$ 定義的；
  分裂體在同構意義下唯一，本章只對 $x^{p^n} - x$ 證明（[$GF(p^n)$ 的唯一性](../Structure/Uniqueness_of_GF_p_n.md)），一般情形陳述不證。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [質多項式分解的存在性 (Existence of a prime factorization)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Finite_Fields/Polynomial_Arithmetic/Unique_Factorization_of_Polynomials.html#b-proof-of-the-existence-of-a-factorization-into-prime-polynomials)：** 已於本章 [多項式的唯一分解](../Polynomial_Arithmetic/Unique_Factorization_of_Polynomials.md)【證明 (b)】完整證明，此處直接引用不再重證

  $$\deg f \ge 1 \quad \Longrightarrow \quad \exists \ \text{不可約} \ q \mid f$$

  * $q$ : $f$ 的不可約因式 (An irreducible factor of $f$) $[q \in F[x]]$

* **【已知 2】 [模不可約多項式的商環是體 (Quotient by an irreducible polynomial is a field)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Field/Quotient_by_Irreducible_is_Field.html#b-proof-of-the-degree-of-the-extension)：** 已於 [模不可約多項式的商環是體](../../Abstract_Algebra/Field/Quotient_by_Irreducible_is_Field.md)【證明 (a)(b)】與 [商環](../../Abstract_Algebra/Ring/Quotient_Ring.md) 完整證明，此處直接引用不再重證

  * (a) 商環是 $F$ 的擴張體：

    $$q \ \text{不可約} \quad \Longrightarrow \quad K = F[x]\big/\left\langle q \right\rangle \ \text{是 } F \text{ 的擴張體}$$

  * (b) 擴張次數：

    $$\left[K : F\right] = \deg q$$

  * (c) 同餘類的運算（係數 $c \in F$ 等同於 $\left[c\right]$）：

    $$\left[g\right] + \left[h\right] = \left[g + h\right], \qquad \left[g\right]\left[h\right] = \left[gh\right]$$

  * $K$ : 商環（擴張體）(The quotient field) $[\text{體}]$
  * $g,\ h$ : 多項式 (Polynomials) $[g, h \in F[x]]$

* **【已知 3】 [因式定理與代入同態 (The factor theorem and evaluation)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Finite_Fields/Polynomial_Arithmetic/Roots_of_Polynomials.html#a-proof-of-the-factor-theorem)：** 已於本章 [多項式的根](../Polynomial_Arithmetic/Roots_of_Polynomials.md)【已知 2】【證明 (a)】給出並證明，此處直接引用不再重證

  * (a) 代入保乘法：

    $$\left(gh\right)(\beta) = g(\beta)\,h(\beta)$$

  * (b) 因式定理：

    $$g(\beta) = 0 \quad \Longleftrightarrow \quad \left(x - \beta\right) \mid g$$

  * $\beta$ : 代入的值 (The value substituted) $[\beta \in K]$

* **【已知 4】 [塔定理 (Tower law)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Field/Tower_Law.html#a-proof-of-the-tower-law)：** 已於 [塔定理](../../Abstract_Algebra/Field/Tower_Law.md)【證明 (a)】完整證明，此處直接引用不再重證

  $$F \subseteq K \subseteq L \quad \Longrightarrow \quad \left[L : F\right] = \left[L : K\right]\left[K : F\right]$$

  * $F,\ K,\ L$ : 三層體 (Three nested fields) $[F \subseteq K \subseteq L]$

* **【已知 5】 [有限次擴張的元素個數 (Counting elements of a finite extension)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Field/Subfield_and_Field_Extension.html#c-proof-that-the-larger-field-is-a-vector-space-over-the-subfield)：** 已於 [子體與體擴張](../../Abstract_Algebra/Field/Subfield_and_Field_Extension.md)【證明 (c)】及其文末給出，此處直接引用

  $$\left[L : F\right] = n,\ \left|F\right| < \infty \quad \Longrightarrow \quad \left|L\right| = \left|F\right|^{n}$$

  * $n$ : 擴張次數 (The degree) $[n \in \mathbf{P}]$
  * 註：$L$ 是 $F$ 上的 $n$ 維向量空間，每個元素由 $n$ 個 $F$-座標唯一決定。

* **【已知 6】 [子體判別法 (Subfield criterion)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Field/Subfield_and_Field_Extension.html#a-proof-of-the-subfield-criterion)：** 已於 [子體與體擴張](../../Abstract_Algebra/Field/Subfield_and_Field_Extension.md)【證明 (a)】完整證明，此處直接引用不再重證

  $$E \ \text{是 } L \text{ 的子體} \quad \Longleftrightarrow \quad \left|E\right| \ge 2, \quad u - v \in E, \quad uv^{-1} \in E \ \left(v \neq 0\right)$$

  * $E$ : $L$ 的子集 (A subset of $L$) $[E \subseteq L]$
  * $u,\ v$ : $E$ 的元素 (Elements of $E$) $[u, v \in E]$

* **【已知 7】 [數學歸納法 (Mathematical induction)](https://mathworld.wolfram.com/PrincipleofMathematicalInduction.html)：** 標準結果，直接引用不再重證

  $$P(1) \ \text{且} \ \left[P(n-1) \Rightarrow P(n)\right] \quad \Longrightarrow \quad P(n) \ \forall n \in \mathbf{P}$$

  * $P$ : 待證命題 (The statement to be proved) $[\mathbf{P} \to \left\{\text{真},\text{假}\right\}]$

* **【定義 1】 分裂體 (Splitting field)：** 投影片 p.27

  $$E \ \text{為 } f \text{ 的分裂體} \quad \overset{\text{def}}{\Longleftrightarrow} \quad f = a\prod_{i=1}^{n}\left(x - \alpha_i\right),\ \alpha_i \in E, \ \text{且 } E \text{ 是含 } F \text{ 與所有 } \alpha_i \text{ 的最小體}$$

  * $E$ : 分裂體 (The splitting field) $[F \subseteq E]$
  * $n$ : $f$ 的次數 (The degree of $f$) $[n = \deg f]$

* **【假設 1】 非常數多項式 (A non-constant polynomial)：** 【證明 (a)】的出發點

  $$f \in F[x], \qquad \deg f = n \ge 1$$

  * $f$ : 待分解的多項式 (The polynomial to be split) $[f \in F[x]]$

* **【假設 2】 歸納假設 (Induction hypothesis)：** 【證明 (b)】對次數歸納時的假設 —— 對**任意**體都成立

  $$\deg g = n - 1 \quad \Longrightarrow \quad g \ \text{在某個有限次擴張中完全分解}$$

  * $g$ : 任意體上的 $n-1$ 次多項式 (A polynomial of degree $n-1$ over any field) $[g \in K[x]]$

* **【推導 1】 $\left[x\right]$ 是 $q$ 的根 (The class of x is a root of q)：** Kronecker 構造的核心 —— 把「$x$」本身當成根

  $$\begin{gather*}
  q\!\left(\left[x\right]\right) &=& \sum_{j} c_j \left[x\right]^j \qquad \text{(} q = \textstyle\sum_j c_j x^j\text{)} \\
  q\!\left(\left[x\right]\right) &\overset{\text{已知 2(c)}}{=}& \left[\sum_{j} c_j x^j\right] \\
  q\!\left(\left[x\right]\right) &=& \left[q\right] \\
  q\!\left(\left[x\right]\right) &=& \left[0\right] \qquad \text{(} q \in \left\langle q \right\rangle\text{)}
  \end{gather*}$$

  * $\left[x\right]$ : $x$ 的同餘類 (The class of $x$) $[\left[x\right] \in K]$
  * $c_j$ : $q$ 的係數 (The coefficients of $q$) $[c_j \in F]$

+++

## 證明:

### (a) proof that every polynomial has a root in some extension

由【假設 1】與【已知 1】取 $f$ 的一個不可約因式 $q$，造 $K = F[x]/\left\langle q \right\rangle$：

$$\begin{gather*}
f &\overset{\text{假設 1,已知 1}}{=}& q\,h \qquad \text{with } q \ \text{不可約} \\
K &\overset{\text{已知 2(a)}}{=}& F \text{ 的擴張體} \\
f\!\left(\left[x\right]\right) &\overset{\text{已知 3(a)}}{=}& q\!\left(\left[x\right]\right) h\!\left(\left[x\right]\right) \\
f\!\left(\left[x\right]\right) &\overset{\text{推導 1}}{=}& 0 \cdot h\!\left(\left[x\right]\right) = 0
\end{gather*}$$

故 $\left[x\right] \in K$ 是 $f$ 的根。取 $F = GF(p)$、$n = \deg q$，由【已知 2(b)】與【已知 5】：

$$\left|K\right| \overset{\text{已知 2(b),已知 5}}{=} p^{n}$$

即 $K$ 是 $p^n$ 元素的體，與投影片 p.31「Use $q(x)$ to construct $GF_{p^n}$ where $n = \deg\left(q(x)\right)$」一致。

### (b) proof that every polynomial splits in some finite extension

對 $n = \deg f$ 歸納。**$n = 1$**：$f = a\left(x - \alpha_1\right)$ 已在 $F$ 中分解（$\alpha_1 = -a^{-1}\cdot$ 常數項）。
**歸納步驟**：由【證明 (a)】得擴張 $K_1$ 與根 $\alpha_1$，剝掉一個一次因式後套【假設 2】：

$$\begin{gather*}
f\!\left(\alpha_1\right) &\overset{\text{證明 (a)}}{=}& 0, \qquad \alpha_1 \in K_1,\ \left[K_1 : F\right] = \deg q \\
f &\overset{\text{已知 3(b)}}{=}& \left(x - \alpha_1\right)g \qquad \text{in } K_1[x],\ \deg g = n - 1 \\
g &\overset{\text{假設 2}}{=}& a\left(x - \alpha_2\right)\cdots\left(x - \alpha_n\right) \qquad \text{in } L[x],\ \left[L : K_1\right] < \infty \\
f &=& a\left(x - \alpha_1\right)\left(x - \alpha_2\right)\cdots\left(x - \alpha_n\right) \qquad \text{in } L[x] \\
\left[L : F\right] &\overset{\text{已知 4}}{=}& \left[L : K_1\right]\left[K_1 : F\right] < \infty
\end{gather*}$$

$$\text{(b) 對所有 } n \ge 1 \ \text{成立} \quad \overset{\text{已知 7}}{\Longleftarrow} \quad n = 1 \ \text{與歸納步驟}$$

若 $F$ 有限，則由【已知 5】$\left|L\right| = \left|F\right|^{\left[L : F\right]} < \infty$。

* 註：【假設 2】必須對**任意**體成立（這裡套在 $K_1$ 上，不是原本的 $F$），
  所以歸納的命題是「對所有體 $F$ 與所有 $n-1$ 次多項式」。

### (c) proof that the smallest field containing all roots exists

在 (b) 的 $L$ 中，令 $E$ 為所有「含 $F$ 與全部 $\alpha_i$」的子體之交集：

$$E \overset{\text{let}}{=} \bigcap\left\{M \ \middle|\ M \ \text{是 } L \text{ 的子體},\ F \cup \left\{\alpha_1, \dots, \alpha_n\right\} \subseteq M\right\}$$

**$E$ 是子體**：集合族非空（$L$ 自己在內）；每個 $M$ 都滿足子體判別法的三條，交集也滿足：

$$\begin{gather*}
0, 1 \in M \ \forall M &\Longrightarrow& \left|E\right| \ge 2 \\
u, v \in E &\Longrightarrow& u - v,\ uv^{-1} \in M \ \forall M \\
u - v,\ uv^{-1} &\in& E \\
E &\overset{\text{已知 6}}{=}& L \text{ 的子體}
\end{gather*}$$

**$E$ 是最小的**：它含 $F$ 與所有 $\alpha_i$，又包含於每一個這樣的 $M$。$f$ 的分解式的每個因式都在 $E[x]$ 中，故

$$E \overset{\text{定義 1}}{=} f \text{ 的分裂體}$$

與投影片 p.27 的定義一致。

* 註：更具體地，$E = F\left(\alpha_1, \dots, \alpha_n\right)$ —— 反覆做 [單擴張](../../Abstract_Algebra/Field/Simple_Extension.md)。
  對 $f = x^{p^n} - x$ 還有更漂亮的描述：**$E$ 就是根的集合本身**，見 [$GF(p^n)$ 的存在性](../Structure/Existence_of_GF_p_n.md)。

+++

## 意義與密碼學關聯 (Interpretation and Relevance to Cryptography)

### 「根不夠，就造一個」

Kronecker 構造的哲學是：**要一個根，就把 $x$ 本身當成根**，然後模掉它該滿足的方程式。
虛數單位 $i$ 就是這樣來的（$\mathbf{R}[x]/\left\langle x^2 + 1 \right\rangle$），
AES 的 $\left\{02\right\}$（即 $\left[x\right] \in GF(2^8)$）也是這樣來的 ——
它是 $x^8 + x^4 + x^3 + x + 1$ 在 $GF(2^8)$ 裡長出來的根。

### 擴張塔與配對密碼學

(b) 的證明是一層一層往上蓋：$F \subseteq K_1 \subseteq K_2 \subseteq \cdots \subseteq L$。
配對密碼學（BLS 簽章、zk-SNARK 的 BN254、BLS12-381 曲線）正是在這種塔上運算：

$$GF(p) \subseteq GF(p^2) \subseteq GF(p^6) \subseteq GF(p^{12})$$

每一層都是模一個不可約多項式的 Kronecker 構造，配對的值落在最上層 $GF(p^{12})$。
層層構造而非一步到位，是因為每層的模多項式可以選得很稀疏（如 $u^2 + 1$、$v^3 - \xi$），乘法更快。

### 程式思維

```python
# Kronecker 構造：在 GF(2)[x]/<x^3+x+1> 裡，[x] = 0b010 就是 x^3+x+1 的根（推導 1）
def gf2_mulmod(a, b, m):
    r = 0
    while b:
        if b & 1:
            r ^= a
        b >>= 1
        a <<= 1
        if a.bit_length() == m.bit_length():
            a ^= m
    return r

X, M = 0b010, 0b1011
x3 = gf2_mulmod(gf2_mulmod(X, X, M), X, M)
assert x3 ^ X ^ 1 == 0          # [x]^3 + [x] + 1 = 0
```
