# Order of a Polynomial (多項式的階)

+++

## 證明目標:

`FiniteFields.pdf` p.24–p.25。投影片 p.24 的大表列出 $GF(2)$ 上次數 $1$ 到 $8$ 的全部不可約多項式及其「$e$」值，
p.25 定義這個 $e$ 並陳述一條定理，但**證明只寫「See Lidl & Niederreiter」**。本檔完整證明它。

* (a) 投影片 p.25 的 Definition 良定義：$f \in GF(q)[x]$，$f(0) \neq 0$，則存在正整數 $e$ 使 $f(x) \mid x^e - 1$；最小者記為 $\mathrm{ord}(f)$。

* (b) 投影片 p.25 的 Theorem：$f$ 在 $GF(q)$ 上不可約、$\deg f = m$、$f(0) \neq 0$，則

$$\mathrm{ord}(f) = f \ \text{的任一根在 } GF(q^m)^* \text{ 中的階}$$

* (c) 推論：

$$\mathrm{ord}(f) \ \Big|\ q^m - 1$$

* (d) 驗證投影片 p.24 大表中的代表性數值（全表 $71$ 列以 Python 驗算）：

$$\mathrm{ord}\left(x^4 + x^3 + x^2 + x + 1\right) = 5, \qquad \mathrm{ord}\left(x^6 + x^3 + 1\right) = 9, \qquad n = 5, 7 \ \text{時每列} \ e = 2^n - 1$$

* $q$ : 係數體的元素個數 (The order of the coefficient field) $[q = p^k]$
* $f$ : 多項式 (A polynomial) $[f \in GF(q)[x],\ f(0) \neq 0]$
* $e$ : 正整數 (A positive integer) $[e \in \mathbf{P}]$
* $\mathrm{ord}(f)$ : $f$ 的階 (The order of $f$) $[\mathrm{ord}(f) \in \mathbf{P}]$
* $m$ : $f$ 的次數 (The degree of $f$) $[m \in \mathbf{P}]$
* $\alpha$ : $f$ 的一個根 (A root of $f$) $[\alpha \in GF(q^m)]$
* 註：**投影片 p.25 的 Theorem 沒有證明**（只引用 Lidl–Niederreiter《Finite Fields》），本檔 (b) 補證。
* 註：**投影片 p.24 表中 $n = 1$ 的第一列「$10$」（即 $f = x$）標 $e = 1$，但 $x$ 不滿足 p.25 定義要求的 $f(0) \neq 0$**。
  這是沿用 Lidl–Niederreiter 的約定：$f(0) = 0$ 時寫 $f = x^h g$、$g(0) \neq 0$，定義 $\mathrm{ord}(f) = \mathrm{ord}(g)$，故 $\mathrm{ord}(x) = \mathrm{ord}(1) = 1$。本檔 (a)(b) 只處理 $f(0) \neq 0$。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [同餘類的個數 (The number of residue classes)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Finite_Fields/Polynomial_Arithmetic/Division_Algorithm_for_Polynomials.html#d-proof-that-the-residues-modulo-a-polynomial-are-counted-by-the-remainders)：** 已於本章 [多項式的除法原理](../Polynomial_Arithmetic/Division_Algorithm_for_Polynomials.md)【證明 (d)】完整證明，此處直接引用不再重證

  $$\left|GF(q)[x]\big/\left\langle f \right\rangle\right| = q^{\deg f} < \infty$$

* **【已知 2】 [多項式版貝祖等式 (Bézout's identity for polynomials)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Finite_Fields/Polynomial_Arithmetic/Euclidean_Domain.html#e-proof-that-the-extended-euclidean-algorithm-works-for-polynomials)：** 已於本章 [歐幾里得整環](../Polynomial_Arithmetic/Euclidean_Domain.md)【證明 (e)】完整證明，此處直接引用不再重證

  $$\gcd(f, a) = 1 \quad \Longrightarrow \quad \exists\, u, v \ \text{ with } \ uf + va = 1$$

  * $a,\ u,\ v$ : 多項式 (Polynomials) $[\in GF(q)[x]]$

* **【已知 3】 [極小多項式的整除刻畫 (Divisibility characterization of the minimal polynomial)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Finite_Fields/Multiplicative_Group/Minimal_Polynomial.html#c-proof-of-the-divisibility-characterization-of-the-minimal-polynomial)：** 已於本章 [極小多項式](Minimal_Polynomial.md)【證明 (c)】完整證明，此處直接引用不再重證

  $$g \ \text{首一不可約},\ g(\alpha) = 0 \quad \Longrightarrow \quad \left[\, h(\alpha) = 0 \Longleftrightarrow g \mid h \,\right]$$

  * $g$ : 首一不可約多項式 (A monic irreducible polynomial) $[g \in GF(q)[x]]$
  * $h$ : 任意多項式 (Any polynomial) $[h \in GF(q)[x]]$

* **【已知 4】 [Kronecker 構造 (The Kronecker construction)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Finite_Fields/Construction/Splitting_Field.html#a-proof-that-every-polynomial-has-a-root-in-some-extension)：** 已於本章 [分裂體](../Construction/Splitting_Field.md)【推導 1】【證明 (a)】完整證明，此處直接引用不再重證

  $$f \ \text{不可約},\ \deg f = m \quad \Longrightarrow \quad GF(q)[x]\big/\left\langle f \right\rangle \ \text{是 } q^m \text{ 元素的體}, \quad \left[x\right] \ \text{是 } f \text{ 的根}$$

* **【已知 5】 [冪次為單位元素的條件與階整除群階 (When a power is the identity; order divides group order)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Finite_Fields/Multiplicative_Group/Euler_Phi_and_Cyclic_Group_Orders.html#a-proof-that-a-power-is-the-identity-exactly-when-the-order-divides-the-exponent)：** 已於本章 [尤拉函數與循環群中元素的階](Euler_Phi_and_Cyclic_Group_Orders.md)【證明 (a)】與 [元素的階與循環子群](../../Abstract_Algebra/Group/Order_of_Element_and_Cyclic_Subgroup.md)【定義 1】【證明 (b)】完整證明，此處直接引用不再重證

  * (a) 階的定義：

    $$o(\alpha) = \min\left\{e \in \mathbf{P} \ \middle|\ \alpha^e = 1\right\}$$

  * (b) 冪次為 $1$ 的刻畫：

    $$\alpha^e = 1 \quad \Longleftrightarrow \quad o(\alpha) \mid e$$

  * (c) 階整除群階：

    $$o(\alpha) \ \Big|\ \left|GF(q^m)^*\right| = q^m - 1$$

* **【已知 6】 [GF(16) 中兩個根的階 (Orders of two roots in GF(16))](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Finite_Fields/Construction/Galois_Fields_GF8_and_GF16.html#f-verify-that-the-root-of-the-all-ones-quartic-has-order-five)：** 已於本章 [伽羅瓦體 GF(8) 與 GF(16)](../Construction/Galois_Fields_GF8_and_GF16.md)【證明 (e)(f)】驗證，此處直接引用

  $$\beta^4 + \beta^3 + \beta^2 + \beta + 1 = 0 \ \Longrightarrow \ \beta^5 = 1,\ \beta \neq 1; \qquad \gamma^4 + \gamma + 1 = 0 \ \Longrightarrow \ o(\gamma) = 15$$

* **【已知 7】 [鴿籠原理 (Pigeonhole principle)](https://mathworld.wolfram.com/DirichletsBoxPrinciple.html)：** 標準結果，直接引用不再重證

  $$N + 1 \ \text{個物件放進 } N \text{ 個盒子} \quad \Longrightarrow \quad \text{某盒至少兩個}$$

* **【定義 1】 多項式的階 (Order of a polynomial)：** 投影片 p.25

  $$\mathrm{ord}(f) \overset{\text{def}}{=} \min\left\{e \in \mathbf{P} \ \middle|\ f(x) \mid x^e - 1\right\}$$

  * $\mathrm{ord}(f)$ : $f$ 的階 (The order of $f$) $[\mathrm{ord}(f) \in \mathbf{P}]$

* **【假設 1】 常數項非零 (Non-zero constant term)：** 【證明 (a)】的前提

  $$f \in GF(q)[x], \qquad f \neq 0, \qquad f(0) \neq 0$$

* **【假設 2】 不可約且常數項非零 (Irreducible with non-zero constant term)：** 【證明 (b)(c)】的前提

  $$f \ \text{在 } GF(q) \text{ 上不可約}, \qquad \deg f = m, \qquad f(0) \neq 0, \qquad f = c\,g,\ g \ \text{首一},\ c \in GF(q)^*$$

  * $c$ : 首項係數 (The leading coefficient) $[c \in GF(q)^*]$
  * $g$ : $f$ 的首一化 (The monic normalization of $f$) $[g \in GF(q)[x]]$

* **【推導 1】 與 $x$ 互質者可消去 $x^i$ (Cancelling a power of x)：** 【證明 (a)】要用。$f(0) \neq 0$ 表示 $x \nmid f$，故 $\gcd\left(f, x^i\right) = 1$

  $$\begin{gather*}
  f &\mid& x^i\,b \\
  u f + v x^i &\overset{\text{已知 2}}{=}& 1 \\
  u f b + v x^i b &=& b \\
  f &\mid& b
  \end{gather*}$$

  * $b$ : 多項式 (A polynomial) $[b \in GF(q)[x]]$
  * $i$ : 自然數 (A natural number) $[i \in \mathbf{N}]$
  * 註：$\gcd\left(f, x^i\right) = 1$：$x^i$ 的首一因式只有 $x^j$，而 $x \nmid f$（因 $f(0) \neq 0$）。

+++

## 證明:

### (a) proof that the order of a polynomial exists

考慮 $x^0, x^1, \dots, x^{N}$ 模 $f$ 的同餘類，$N = q^{\deg f}$。同餘類只有 $N$ 個，必有兩個相同：

$$\begin{gather*}
\left[x^i\right] &\overset{\text{已知 1,已知 7}}{=}& \left[x^j\right] \qquad \text{for some } 0 \le i < j \le N \\
f &\mid& x^j - x^i = x^i\left(x^{j-i} - 1\right) \\
f &\overset{\text{推導 1,假設 1}}{\mid}& x^{j-i} - 1
\end{gather*}$$

$j - i \in \mathbf{P}$ 使 $f \mid x^{j-i} - 1$，集合非空，故【定義 1】的最小值存在。

* 註：$f(0) \neq 0$ **不可省**：$f = x$ 永遠不整除 $x^e - 1$（常數項 $-1 \neq 0$）。

### (b) proof that the order of an irreducible polynomial equals the order of its roots

設 $\alpha$ 是 $f$ 的根（例如 $\left[x\right] \in GF(q^m)$，【已知 4】）。$f(0) \neq 0$ 故 $\alpha \neq 0$。
$g$ 首一不可約且以 $\alpha$ 為根，由【已知 3】「$g$ 整除某式」等價於「$\alpha$ 是它的根」：

$$\begin{gather*}
f \mid x^e - 1 &\overset{\text{假設 2}}{\Longleftrightarrow}& g \mid x^e - 1 \\
g \mid x^e - 1 &\overset{\text{已知 3}}{\Longleftrightarrow}& \alpha^e - 1 = 0 \\
\alpha^e - 1 = 0 &\Longleftrightarrow& \alpha^e = 1
\end{gather*}$$

兩邊取「使之成立的最小正整數 $e$」：

$$\mathrm{ord}(f) \overset{\text{定義 1,已知 5(a)}}{=} o(\alpha)$$

上式對 $f$ 的**任一**根都成立（論證沒有用到 $\alpha$ 是哪一個根），與投影片 p.25 的 Theorem 一致。

* 註：這也順帶說明 $f$ 的所有根有**相同的階** —— 與 [共軛元與分圓陪集](Conjugates_and_Cyclotomic_Cosets.md) 的觀點一致：
  根是 $\alpha, \alpha^q, \alpha^{q^2}, \dots$，而 $\gcd\left(q, q^m - 1\right) = 1$ 使取 $q$ 次方不改變階。

### (c) proof that the order divides q to the m minus one

由【已知 4】$\alpha \in GF(q^m)^*$，其階整除群的階：

$$\mathrm{ord}(f) \overset{\text{證明 (b)}}{=} o(\alpha) \overset{\text{已知 5(c)}}{\Big|} q^m - 1$$

* 註：等號成立（$\mathrm{ord}(f) = q^m - 1$）當且僅當 $\alpha$ 是本原元 —— 這就是 [本原多項式](Primitive_Polynomial.md) 的判準。

### (d) verify entries of the table of irreducible polynomials over the binary field

**$x^4 + x^3 + x^2 + x + 1$（表中 $11111$，$e = 5$）**：

$$\begin{gather*}
\mathrm{ord}\left(x^4 + x^3 + x^2 + x + 1\right) &\overset{\text{證明 (b)}}{=}& o(\beta) \\
o(\beta) &\overset{\text{已知 6,已知 5(b)}}{\in}& \left\{1, 5\right\} \setminus \left\{1\right\} = \left\{5\right\}
\end{gather*}$$

**$x^4 + x + 1$（表中 $10011$，$e = 15$）**：

$$\mathrm{ord}\left(x^4 + x + 1\right) \overset{\text{證明 (b),已知 6}}{=} o(\gamma) = 15$$

**$x^6 + x^3 + 1$（表中 $1001001$，$e = 9$）**：$x^9 - 1 = \left(x^3 - 1\right)\left(x^6 + x^3 + 1\right)$，故 $\mathrm{ord} \mid 9$；
又 $\mathrm{ord} = 1$ 或 $3$ 會使六次式整除一次或三次式，不可能：

$$\begin{gather*}
x^6 + x^3 + 1 &\mid& x^9 - 1 \\
\mathrm{ord}\left(x^6 + x^3 + 1\right) &\overset{\text{證明 (b),已知 5(b)}}{\in}& \left\{1, 3, 9\right\} \\
\mathrm{ord}\left(x^6 + x^3 + 1\right) &\overset{\text{定義 1}}{\neq}& 1, 3 \qquad \text{(次數 } 6 > 3\text{)} \\
\mathrm{ord}\left(x^6 + x^3 + 1\right) &=& 9
\end{gather*}$$

**$n = 5$ 與 $n = 7$ 的整欄**：$2^5 - 1 = 31$、$2^7 - 1 = 127$ 都是質數，由【證明 (c)】$\mathrm{ord} \in \left\{1, 2^n - 1\right\}$，
而 $\mathrm{ord} = 1$ 表示 $f \mid x - 1$，對 $n \ge 2$ 不可能：

$$\mathrm{ord}(f) \overset{\text{證明 (c)}}{=} 2^n - 1 \qquad \left(n = 5, 7\right)$$

與投影片 p.24 表中 $n = 5$ 全為 $31$、$n = 7$ 全為 $127$ 一致。**其餘各列**（特別是 $n = 8$ 的 $30$ 列，
含 AES 的 $100011011$ 其 $e = 51$）以 Python 逐列驗算：**全表 $71$ 列（扣除 $f = x$）的 $e$ 值與「表列即全部不可約多項式」兩項皆正確**。

+++

## 意義與密碼學關聯 (Interpretation and Relevance to Cryptography)

### 階 = 週期

$\mathrm{ord}(f)$ 就是以 $f$ 為回饋多項式的 LFSR 的**週期**（初始狀態非零時）。表中的 $e$ 值因此直接告訴設計者：

* $e = 2^n - 1$（本原多項式）：週期最大，輸出是 m-序列（最大長度序列）；
* $e < 2^n - 1$：週期縮短，例如 $x^4 + x^3 + x^2 + x + 1$ 只有 $5$。

### AES 的模數**不是**本原多項式

表中 AES 的 $x^8 + x^4 + x^3 + x + 1$（$100011011$）**$e = 51$，不是 $255$**。
所以在 AES 的 $GF(2^8)$ 裡，$\left\{02\right\} = \left[x\right]$ 的乘法階只有 $51$，**不是**生成元；
常用的生成元是 $\left\{03\right\} = \left[x + 1\right]$（階 $255$）。
這不影響 AES 的安全性 —— AES 只需要 $GF(2^8)$ 是體（有反元素），不需要 $\left[x\right]$ 是本原元 ——
但它影響查表實作：$\log$ 表必須以 $\left\{03\right\}$ 為底。見 [AES 的 $GF(2^8)$ 算術](../AES/AES_GF_2_8_Arithmetic.md)。

### 程式思維

```python
def poly_order_gf2(f):
    """ord(f)：最小的 e 使 f | x^e - 1（f 以整數位元表示，f(0) = 1）。定義 1。"""
    n, a, e = f.bit_length() - 1, 0b10, 1
    while a != 1:
        a <<= 1
        if a >> n:
            a ^= f
        e += 1
    return e

assert poly_order_gf2(0b11111) == 5 and poly_order_gf2(0b10011) == 15     # 證明 (d)
assert poly_order_gf2(0b1001001) == 9                                      # x^6 + x^3 + 1
assert poly_order_gf2(0b100011011) == 51                                   # AES 的模數
```
