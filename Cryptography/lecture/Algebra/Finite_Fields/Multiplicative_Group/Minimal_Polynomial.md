# Minimal Polynomial (極小多項式)

+++

## 證明目標:

`FiniteFields.pdf` p.20、p.42；補充講義 §7.8.1–§7.8.2（Lemma 7.14、Theorem 7.15）。
大體裡的一個元素 $u$，在小體 $F$ 的眼中是什麼？答案是一個多項式 —— **$u$ 滿足的最簡單的方程式**。
極小多項式是「元素」與「不可約多項式」之間的橋樑，本原多項式、共軛元、唯一性定理都建立在它上面。

設 $F \subseteq K$ 且 $\left[K : F\right] = m < \infty$，$u \in K$。

* (a) 投影片 p.20 的 Definition 良定義：$J = \left\{f \in F[x] \mid f(u) = 0\right\}$ 是非零理想，且有**唯一的首一生成元** $g$，稱為 $u$ 在 $F$ 上的極小多項式。
* (b) 投影片 p.42 的 Lemma：

$$g \ \text{是 } u \text{ 的極小多項式} \quad \Longrightarrow \quad g \ \text{不可約}$$

* (c) 補充講義 Lemma 7.14：

$$f(u) = 0 \ \Longleftrightarrow \ g \mid f; \qquad g \ \text{是使 } g(u) = 0 \text{ 的最低次首一多項式}; \qquad h \ \text{首一不可約},\ h(u) = 0 \ \Longrightarrow \ h = g$$

* (d) 補充講義 Theorem 7.15：

$$F[u] = \left\{f(u) \ \middle|\ f \in F[x]\right\} \cong F[x]\big/\left\langle g \right\rangle, \qquad \left[F[u] : F\right] = \deg g, \qquad \deg g \mid m$$

* (e) 投影片 p.20 的 Example：$\alpha^3 + \alpha + 1 = 0$ 時，$x^3 + x^2 + 1$ 是 $\alpha^2 + 1$ 在 $GF(2)$ 上的極小多項式。

* $F$ : 小體 (The base field) $[\text{體}]$
* $K$ : 大體 (The larger field) $[F \subseteq K]$
* $m$ : 擴張次數 (The degree of the extension) $[m = \left[K : F\right] \in \mathbf{P}]$
* $u$ : 大體中的元素 (An element of the larger field) $[u \in K]$
* $J$ : 以 $u$ 為根的多項式全體 (The polynomials vanishing at $u$) $[J \trianglelefteq F[x]]$
* $g$ : $u$ 的極小多項式 (The minimal polynomial of $u$) $[g \in F[x]]$
* $F[u]$ : $u$ 的多項式值全體 (The polynomial expressions in $u$) $[F \subseteq F[u] \subseteq K]$
* 註：投影片 p.20 的定義要求「uniquely determined monic polynomial generating the ideal $J$」——
  「$J$ 是主理想」「生成元唯一」「$J \neq \left\{0\right\}$」三件事投影片都沒有證，本檔 (a) 補上。
* 註：$\left[K : F\right] < \infty$ 保證 $J \neq \left\{0\right\}$（$u$ 是**代數元**）。有限體的所有元素都滿足此條件。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [F[x] 是主理想整環 (F[x] is a principal ideal domain)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Finite_Fields/Polynomial_Arithmetic/Euclidean_Domain.html#d-proof-that-every-euclidean-domain-is-a-principal-ideal-domain)：** 已於本章 [歐幾里得整環](../Polynomial_Arithmetic/Euclidean_Domain.md)【證明 (b)(d)】完整證明，此處直接引用不再重證

  * (a) 每個理想是主理想：

    $$J \trianglelefteq F[x] \quad \Longrightarrow \quad J = \left\langle g_0 \right\rangle$$

  * (b) 理想的判別（對減法與吸收封閉）：

    $$f, h \in J,\ r \in F[x] \quad \Longrightarrow \quad f - h \in J, \quad rf \in J \qquad \left(J \text{ 為理想}\right)$$

  * $g_0$ : 生成元 (A generator) $[g_0 \in F[x]]$

* **【已知 2】 [代入是環同態 (Evaluation is a ring homomorphism)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Ring/Ring_Examples.html#e-verify-that-the-polynomials-form-a-ring)：** 已於 [環的例子](../../Abstract_Algebra/Ring/Ring_Examples.md) 與 [單擴張](../../Abstract_Algebra/Field/Simple_Extension.md)【已知 2(b)】給出，此處直接引用

  $$\left(f \pm h\right)(u) = f(u) \pm h(u), \qquad \left(fh\right)(u) = f(u)\,h(u)$$

  * $f,\ h$ : 多項式 (Polynomials) $[f, h \in F[x]]$

* **【已知 3】 [體無零因子 (A field has no zero divisors)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Field/Field_Definition.html#d-proof-that-every-field-is-an-integral-domain)：** 已於 [體的定義](../../Abstract_Algebra/Field/Field_Definition.md)【證明 (d)】完整證明，此處直接引用不再重證

  $$ab = 0 \quad \Longrightarrow \quad a = 0 \ \text{或} \ b = 0$$

  * $a,\ b$ : 體元素 (Field elements) $[a, b \in K]$

* **【已知 4】 [維數與線性相依 (Dimension and linear dependence)](https://mathworld.wolfram.com/LinearlyDependentVectors.html)：** 線性代數的標準結果，直接引用不再重證

  $$\dim_F K = m \quad \Longrightarrow \quad \text{任意 } m + 1 \text{ 個向量線性相依}$$

  * $K$ : 視為 $F$-向量空間 (Viewed as an $F$-vector space) $[\dim_F K = m]$

* **【已知 5】 [模不可約多項式的商環是體 (Quotient by an irreducible polynomial is a field)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Field/Quotient_by_Irreducible_is_Field.html#b-proof-of-the-degree-of-the-extension)：** 已於 [模不可約多項式的商環是體](../../Abstract_Algebra/Field/Quotient_by_Irreducible_is_Field.md)【證明 (a)(b)】完整證明，此處直接引用不再重證

  * (a) 商環是體：

    $$g \ \text{不可約} \quad \Longrightarrow \quad F[x]\big/\left\langle g \right\rangle \ \text{為體}$$

  * (b) 次數：

    $$\left[F[x]\big/\left\langle g \right\rangle : F\right] = \deg g$$

* **【已知 6】 [塔定理 (Tower law)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Field/Tower_Law.html#a-proof-of-the-tower-law)：** 已於 [塔定理](../../Abstract_Algebra/Field/Tower_Law.md)【證明 (a)】完整證明，此處直接引用不再重證

  $$F \subseteq E \subseteq K \quad \Longrightarrow \quad \left[K : F\right] = \left[K : E\right]\left[E : F\right]$$

  * $E$ : 中間體 (An intermediate field) $[F \subseteq E \subseteq K]$

* **【已知 7】 [次數相加 (Degrees add)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Finite_Fields/Polynomial_Arithmetic/Polynomial_Ring_over_a_Field.html#b-proof-that-degrees-add-in-the-polynomial-ring-over-a-field)：** 已於本章 [體上的多項式環](../Polynomial_Arithmetic/Polynomial_Ring_over_a_Field.md)【證明 (b)】完整證明，此處直接引用不再重證

  $$\deg\left(ab\right) = \deg a + \deg b$$

  * $a,\ b$ : 多項式 (Polynomials) $[a, b \in F[x]]$

* **【已知 8】 [GF(8) 的冪次表與三次質多項式 (The power table of GF(8) and the cubic primes)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Finite_Fields/Construction/Galois_Fields_GF8_and_GF16.html#assumptions-preliminaries)：** 已於本章 [伽羅瓦體 GF(8) 與 GF(16)](../Construction/Galois_Fields_GF8_and_GF16.md)【已知 2(a)】【推導 1】驗證，此處直接引用

  * (a) $\alpha^3 = \alpha + 1$，故 $\alpha^6 = \left(\alpha + 1\right)^2$：

    $$\alpha^6 = \left(\alpha^3\right)^2 = \left(\alpha + 1\right)^2 = \alpha^2 + 1$$

  * (b) $x^3 + x^2 + 1$ 在 $GF(2)$ 上不可約：

    $$x^3 + x^2 + 1 \ \text{為質多項式}$$

  * $\alpha$ : $x^3 + x + 1$ 的根 (A root of $x^3 + x + 1$) $[\alpha \in GF(8)]$

* **【假設 1】 有限次擴張中的元素 (An element of a finite extension)：**

  $$F \subseteq K, \qquad \left[K : F\right] = m < \infty, \qquad u \in K$$

  * $u$ : 被研究的元素 (The element under study) $[u \in K]$

* **【定義 1】 零化理想 (The vanishing ideal)：**

  $$J \overset{\text{def}}{=} \left\{f \in F[x] \ \middle|\ f(u) = 0\right\}$$

  * $J$ : 以 $u$ 為根的 $F$-係數多項式 (Polynomials over $F$ vanishing at $u$) $[J \subseteq F[x]]$

* **【定義 2】 極小多項式 (Minimal polynomial)：** 投影片 p.20

  $$g \overset{\text{def}}{=} J \ \text{的首一生成元}$$

  * $g$ : $u$ 在 $F$ 上的極小多項式 (The minimal polynomial of $u$ over $F$) $[g \in F[x]]$

* **【定義 3】 多項式值全體 (Polynomial expressions in u)：** 補充講義 §7.8.2 的 $\mathbb{G}_\beta$

  $$F[u] \overset{\text{def}}{=} \left\{f(u) \ \middle|\ f \in F[x]\right\}$$

  * $F[u]$ : $u$ 的 $F$-係數多項式值全體 (All values $f(u)$) $[F[u] \subseteq K]$

+++

## 證明:

### (a) proof that the vanishing ideal has a unique monic generator

**$J$ 是理想**：由【已知 2】，兩個以 $u$ 為根的多項式相減、或乘上任何多項式，仍以 $u$ 為根：

$$\begin{gather*}
\left(f - h\right)(u) &\overset{\text{已知 2}}{=}& f(u) - h(u) = 0 - 0 = 0 \\
\left(rf\right)(u) &\overset{\text{已知 2}}{=}& r(u) \cdot 0 = 0 \\
J &\overset{\text{已知 1(b),定義 1}}{=}& F[x] \text{ 的理想}
\end{gather*}$$

**$J \neq \left\{0\right\}$**：$1, u, \dots, u^m$ 是 $K$ 中 $m + 1$ 個向量，必線性相依：

$$\begin{gather*}
c_0 + c_1 u + \cdots + c_m u^m &\overset{\text{已知 4,假設 1}}{=}& 0 \qquad \text{(} c_i \in F \text{ 不全為 } 0\text{)} \\
f_0 &\overset{\text{let}}{=}& c_0 + c_1 x + \cdots + c_m x^m \neq 0 \\
f_0 &\overset{\text{定義 1}}{\in}& J
\end{gather*}$$

**唯一的首一生成元**：由【已知 1(a)】$J = \left\langle g_0 \right\rangle$，$g_0 \neq 0$；除以首項係數得首一的 $g$。
若 $g, g'$ 都是首一生成元，則互相整除、次數相同（【已知 7】），差一個常數倍，而兩者首一，故 $g = g'$。
又 $1(u) = 1 \neq 0$，$1 \notin J$，故 $\deg g \ge 1$。

### (b) proof that the minimal polynomial is irreducible

設 $g = ab$（投影片 p.42 的 Proof）。代入 $u$，兩個因子之一為零；不妨 $a(u) = 0$：

$$\begin{gather*}
0 = g(u) &\overset{\text{已知 2}}{=}& a(u)\,b(u) \\
a(u) &\overset{\text{已知 3}}{=}& 0 \qquad \text{(或 } b(u) = 0\text{，對稱處理)} \\
a &\overset{\text{定義 1}}{\in}& J = \left\langle g \right\rangle \\
\deg a &\overset{\text{已知 7}}{\ge}& \deg g \\
\deg b &\overset{\text{已知 7}}{=}& \deg g - \deg a \le 0
\end{gather*}$$

故 $b$ 是常數。$g$ 的任何分解都有一個因子是常數，且 $\deg g \ge 1$（【證明 (a)】），故 $g$ 不可約。
與投影片 p.42 一致。

### (c) proof of the divisibility characterization of the minimal polynomial

**整除刻畫**：

$$\begin{gather*}
f(u) = 0 &\overset{\text{定義 1}}{\Longleftrightarrow}& f \in J \\
f \in J &\overset{\text{定義 2}}{\Longleftrightarrow}& f \in \left\langle g \right\rangle \\
f \in \left\langle g \right\rangle &\Longleftrightarrow& g \mid f
\end{gather*}$$

**最低次**：$J$ 中任何非零 $f$ 都是 $g$ 的倍數，由【已知 7】$\deg f \ge \deg g$。

**唯一的首一不可約零化多項式**：設 $h$ 首一不可約且 $h(u) = 0$：

$$\begin{gather*}
g &\mid& h \qquad \text{(上面的整除刻畫)} \\
h &=& c\,g \qquad \text{(} h \text{ 不可約且 } \deg g \ge 1\text{，故餘因式為常數 } c\text{)} \\
h &=& g \qquad \text{(兩者首一，} c = 1\text{)}
\end{gather*}$$

與補充講義 Lemma 7.14 一致。

* 註：最後一條讓我們**用不可約性來辨認極小多項式**：只要找到一個首一不可約多項式以 $u$ 為根，它就是極小多項式，
  不必去驗證「沒有更低次的」。【證明 (e)】就是這樣用的。

### (d) proof that adjoining the element gives a field of degree equal to the degree of the minimal polynomial

定義 $\psi : F[x]/\left\langle g \right\rangle \to F[u]$，$\psi\left(\left[f\right]\right) = f(u)$。
**良定義且單射**：由【證明 (c)】

$$\begin{gather*}
\left[f\right] = \left[h\right] &\Longleftrightarrow& g \mid \left(f - h\right) \\
g \mid \left(f - h\right) &\overset{\text{證明 (c)}}{\Longleftrightarrow}& \left(f - h\right)(u) = 0 \\
\left(f - h\right)(u) = 0 &\overset{\text{已知 2}}{\Longleftrightarrow}& f(u) = h(u)
\end{gather*}$$

**滿射**由【定義 3】；**保運算**由【已知 2】。故 $\psi$ 是同構，$F[u]$ 是體且次數為 $\deg g$：

$$\begin{gather*}
F[u] &\overset{\text{定義 3}}{\cong}& F[x]\big/\left\langle g \right\rangle \\
F[u] &\overset{\text{證明 (b),已知 5(a)}}{=}& \text{體} \\
\left[F[u] : F\right] &\overset{\text{已知 5(b)}}{=}& \deg g \\
m = \left[K : F\right] &\overset{\text{已知 6}}{=}& \left[K : F[u]\right] \cdot \deg g \\
\deg g &\mid& m
\end{gather*}$$

與補充講義 Theorem 7.15 一致。

* 註：$F[u]$ 是體，而 $K$ 中任何含 $F$ 與 $u$ 的子體都含所有 $f(u)$，故
  $F[u]$ 就是 [單擴張](../../Abstract_Algebra/Field/Simple_Extension.md) $F(u)$ —— **代數元的方括號與圓括號相等**。
* 註：取 $F = GF(p)$、$K = GF(p^m)$：**$GF(p^m)$ 中每個元素的極小多項式次數都整除 $m$**。

### (e) verify the minimal polynomial example in GF(8)

依投影片 p.20 直接展開（係數模 $2$），再用【已知 8(a)】化簡：

$$\begin{gather*}
\left(\alpha^2 + 1\right)^3 + \left(\alpha^2 + 1\right)^2 + 1 &=& \left(\alpha^6 + 3\alpha^4 + 3\alpha^2 + 1\right) + \left(\alpha^4 + 2\alpha^2 + 1\right) + 1 \\
\left(\alpha^2 + 1\right)^3 + \left(\alpha^2 + 1\right)^2 + 1 &=& \alpha^6 + 4\alpha^4 + 5\alpha^2 + 3 \\
\left(\alpha^2 + 1\right)^3 + \left(\alpha^2 + 1\right)^2 + 1 &\equiv& \alpha^6 + \alpha^2 + 1 \pmod 2 \\
\left(\alpha^2 + 1\right)^3 + \left(\alpha^2 + 1\right)^2 + 1 &\overset{\text{已知 8(a)}}{=}& \left(\alpha + 1\right)^2 + \alpha^2 + 1 \\
\left(\alpha^2 + 1\right)^3 + \left(\alpha^2 + 1\right)^2 + 1 &=& 0
\end{gather*}$$

$x^3 + x^2 + 1$ 首一、不可約（【已知 8(b)】）且以 $\alpha^2 + 1$ 為根，由【證明 (c)】它就是極小多項式：

$$x^3 + x^2 + 1 \overset{\text{已知 8(b),證明 (c)}}{=} \alpha^2 + 1 \ \text{在 } GF(2) \text{ 上的極小多項式}$$

與投影片 p.20 一致。

+++

## 意義與密碼學關聯 (Interpretation and Relevance to Cryptography)

### 元素的「身分證」

(d) 說：$u$ 生成的子體長什麼樣，完全由它的極小多項式決定。
在 $GF(2^8)$ 裡，每個位元組都有一個極小多項式（次數 $1, 2, 4$ 或 $8$，由 (d) 的 $\deg g \mid 8$），
它是該元素在 $GF(2)$ 上的「身分證」：

* 次數 $1$：$0$ 與 $1$（在 $GF(2)$ 裡）；
* 次數 $2$：落在子體 $GF(4)$；
* 次數 $4$：落在子體 $GF(16)$；
* 次數 $8$：生成整個 $GF(2^8)$。

### 換基底：AES 的另一種模數

(d) 還給了一個實用結論：若 $u \in GF(2^8)$ 的極小多項式 $g$ 是 $8$ 次，則

$$GF(2)[x]\big/\left\langle g \right\rangle \ \xrightarrow{\ \cong\ } \ GF(2^8), \qquad \left[x\right] \mapsto u$$

**任何一個 $8$ 次不可約多項式都能當 AES 的模數**，彼此之間用這個同構換基底（一個 $8 \times 8$ 的 $GF(2)$ 矩陣）。
AES 的緊湊硬體實作正是先把輸入換到「塔式基底」、在那裡求逆、再換回來 —— 換基底矩陣就是由極小多項式算出來的。

### 程式思維

```python
def min_poly_gf2(u, mod, n):
    """GF(2^n) = GF(2)[x]/<mod> 中 u 的極小多項式：乘上 (x - u^{2^i}) 直到共軛循環（見共軛元一檔）。"""
    def mul(a, b):
        r = 0
        while b:
            if b & 1:
                r ^= a
            b >>= 1
            a <<= 1
            if a >> n:
                a ^= mod
        return r
    conj, c = [], u
    while c not in conj:
        conj.append(c)
        c = mul(c, c)
    poly = [1]                               # 係數為 GF(2^n) 元素，由低到高
    for r in conj:                           # poly *= (x + r)
        poly = [0] + poly
        for i in range(len(poly) - 1):
            poly[i] ^= mul(poly[i + 1], r)
    return poly

assert min_poly_gf2(0b101, 0b1011, 3) == [1, 0, 1, 1]   # 證明 (e)：alpha^2 + 1 -> 1 + x^2 + x^3
```
