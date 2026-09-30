# Galois Field GF(4) (四元素伽羅瓦體 GF(4))

+++

## 證明目標:

`FiniteFields.pdf` p.10–p.15；補充講義 §7.6 Example 1。
第一個「元素個數不是質數」的有限體。投影片用**三種看似不同的方式**造出它，
本檔逐一驗證，並證明三者其實是同一個體。

* (a) 投影片 p.11 的 Note：$\mathbf{Z}_4$ **不是**體（$2$ 沒有乘法反元素）。
* (b) 投影片 p.12：$f(x) = x^2 + x + 1$ 在 $GF(2)$ 上不可約；但

$$f(x) = \left(x + 2\right)^2 \ \text{ over } GF(3), \qquad f(x) = \left(x - \omega\right)\left(x - \omega^2\right) \ \text{ over } \mathbf{C}, \quad \omega = \tfrac{-1 + \sqrt{3}\,i}{2}$$

* (c) 構造一：一次多項式集合 $\left\{a_1 x + a_2 \mid a_i \in GF(2)\right\}$ 配上「模 $2$、模 $x^2 + x + 1$」的運算（投影片 p.13）：

$$\begin{array}{c|cccc} \otimes & 0 & 1 & x & x+1 \\ \hline 0 & 0 & 0 & 0 & 0 \\ 1 & 0 & 1 & x & x+1 \\ x & 0 & x & x+1 & 1 \\ x+1 & 0 & x+1 & 1 & x \end{array}$$

* (d) 構造二：同餘類 $GF(4) \cong GF(2)[x]\big/\left\langle x^2 + x + 1 \right\rangle$（投影片 p.14）。
* (e) 構造三：固定根 $\alpha$ 的線性組合 $\left\{0, 1, \alpha, \alpha + 1\right\}$，關係式 $\alpha^2 = \alpha + 1$（投影片 p.15）：

$$\left(\alpha + 1\right)\left(\alpha + 1\right) = \alpha$$

* (f) 三種構造同構（投影片 p.11「They look different, but essentially the same」）。
* (g) 投影片 p.12 的問題：$x^2 + x + 1$ 在 $GF(11)$ 上不可約嗎？$p(x) \bmod f(x)$ 有哪些？

* $GF(4)$ : 四元素伽羅瓦體 (The Galois field with four elements) $[\text{體}]$
* $f(x)$ : 生成多項式 (The generating polynomial) $[x^2 + x + 1]$
* $a_1,\ a_2$ : 係數 (Coefficients) $[a_i \in GF(2)]$
* $\alpha$ : $f$ 的一個根 (A root of $f$) $[\alpha \in GF(4)]$
* $\omega$ : 複數三次單位根 (A primitive complex cube root of unity) $[\omega \in \mathbf{C}]$
* 註：投影片 p.12 寫 $\omega = \left(-1 \pm \sqrt{3}\,i\right)/2$，這是**兩個**根的合寫；
  取「$+$」的那個為 $\omega$，另一個恰為 $\omega^2$，本檔 (b) 驗證。
* 註：投影片 p.13 的三張表只是同一張表的三種編碼：多項式 $a_1x + a_2$ $\leftrightarrow$ 二進位 $\left(a_1a_2\right)_2$ $\leftrightarrow$ 十進位 $2a_1 + a_2$。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [$\mathbf{Z}_n$ 是體的充要條件 (Residues modulo n form a field iff n is prime)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Field/Field_Definition.html#b-proof-that-the-residues-modulo-a-prime-form-a-field)：** 已於 [體的定義](../../Abstract_Algebra/Field/Field_Definition.md)【證明 (b)】完整證明，此處直接引用不再重證

  * (a) 判準：

    $$\mathbf{Z}_n \ \text{為體} \quad \Longleftrightarrow \quad n \ \text{為質數}$$

  * (b) 運算：

    $$a \oplus b = \left(a + b\right) \bmod n, \qquad a \otimes b = \left(ab\right) \bmod n$$

  * $n$ : 模數 (Modulus) $[n \in \mathbf{P}]$
  * $a,\ b$ : 剩餘類代表元 (Residue representatives) $[a, b \in \mathbf{Z}_n]$

* **【已知 2】 [二三次不可約判別法 (Root criterion for degrees two and three)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Field/Irreducible_Polynomial.html#a-proof-of-the-root-criterion-for-degrees-two-and-three)：** 已於 [不可約多項式](../../Abstract_Algebra/Field/Irreducible_Polynomial.md)【證明 (a)】完整證明，此處直接引用不再重證

  $$\deg f \in \left\{2, 3\right\} \quad \Longrightarrow \quad \left[\, f \ \text{不可約} \Leftrightarrow f \ \text{在 } F \text{ 中無根} \,\right]$$

  * $f$ : 多項式 (A polynomial) $[f \in F[x]]$
  * $F$ : 體 (A field) $[\text{體}]$

* **【已知 3】 [模不可約多項式的商環是體 (Quotient by an irreducible polynomial is a field)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Field/Quotient_by_Irreducible_is_Field.html#a-proof-that-the-quotient-by-an-irreducible-polynomial-is-a-field)：** 已於 [模不可約多項式的商環是體](../../Abstract_Algebra/Field/Quotient_by_Irreducible_is_Field.md)【證明 (a)】完整證明，此處直接引用不再重證

  $$p(x) \in F[x] \ \text{不可約} \quad \Longrightarrow \quad F[x]\big/\left\langle p(x) \right\rangle \ \text{為體}$$

  * $p(x)$ : 不可約多項式 (An irreducible polynomial) $[p \in F[x]]$

* **【已知 4】 [同餘類與餘式一一對應 (Residue classes correspond to remainders)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Finite_Fields/Polynomial_Arithmetic/Division_Algorithm_for_Polynomials.html#d-proof-that-the-residues-modulo-a-polynomial-are-counted-by-the-remainders)：** 已於本章 [多項式的除法原理](../Polynomial_Arithmetic/Division_Algorithm_for_Polynomials.md)【證明 (d)】完整證明，此處直接引用不再重證

  $$\left[g\right] = \left[g \bmod m\right], \qquad \left|F[x]\big/\left\langle m \right\rangle\right| = \left|F\right|^{\deg m}$$

  * $g$ : 多項式 (A polynomial) $[g \in F[x]]$
  * $m$ : 模多項式 (The modulus) $[m \in F[x]]$
  * $\left[g\right]$ : $g$ 的同餘類 (The class of $g$) $[F[x]/\left\langle m \right\rangle]$

* **【已知 5】 [商環的運算 (Operations in the quotient ring)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Ring/Quotient_Ring.html#c-proof-that-the-quotient-is-a-ring)：** 已於 [商環](../../Abstract_Algebra/Ring/Quotient_Ring.md)【證明 (a)(b)(c)】完整證明，此處直接引用不再重證

  $$\left[g\right] \oplus \left[h\right] = \left[g + h\right], \qquad \left[g\right] \otimes \left[h\right] = \left[gh\right]$$

  * $g,\ h$ : 多項式 (Polynomials) $[g, h \in F[x]]$

* **【定義 1】 構造一的運算 (Operations of construction one)：** 投影片 p.13

  $$\left(a_1x + a_2\right) \oplus \left(b_1x + b_2\right) \overset{\text{def}}{=} \left(a_1x + a_2\right) + \left(b_1x + b_2\right) \bmod 2$$

  $$\left(a_1x + a_2\right) \otimes \left(b_1x + b_2\right) \overset{\text{def}}{=} \left(\left(a_1x + a_2\right)\left(b_1x + b_2\right) \bmod x^2 + x + 1\right) \bmod 2$$

  * $a_i,\ b_i$ : 係數 (Coefficients) $[a_i, b_i \in GF(2)]$

* **【定義 2】 構造三的固定根 (The fixed root of construction three)：** 投影片 p.15

  $$\alpha^2 + \alpha + 1 \overset{\text{def}}{=} 0, \qquad \text{即} \qquad \alpha^2 = \alpha + 1 \quad \left(\bmod 2\right)$$

  * $\alpha$ : 抽象的根 (An abstract root) $[\alpha \in GF(4)]$
  * 註：在 $GF(2)$ 中 $-1 = 1$，故 $-\alpha - 1 = \alpha + 1$。
  * 註：「$\alpha$ 在哪裡？」—— 在構造二裡，$\alpha$ 就是同餘類 $\left[x\right]$
    （[模不可約多項式的商環是體](../../Abstract_Algebra/Field/Quotient_by_Irreducible_is_Field.md)【定義 1】的註：商環裡自動長出 $p$ 的根）。

* **【推導 1】 化簡規則 $x^2 \equiv x + 1$ (The reduction rule)：** 三種構造共用的唯一規則

  $$\begin{gather*}
  x^2 &=& 1 \cdot \left(x^2 + x + 1\right) + \left(-x - 1\right) \\
  x^2 &\overset{\text{已知 1(b)}}{=}& 1 \cdot \left(x^2 + x + 1\right) + \left(x + 1\right) \qquad \text{(} -1 \equiv 1 \pmod 2\text{)} \\
  x^2 \bmod \left(x^2 + x + 1\right) &=& x + 1
  \end{gather*}$$

  * 註：任何次數 $\ge 2$ 的項都可以反覆用這條規則降次。

+++

## 證明:

### (a) disprove that the residues modulo four form a field

$2$ 乘以 $\mathbf{Z}_4$ 的每個元素：

$$\begin{gather*}
2 \otimes 0 &\overset{\text{已知 1(b)}}{=}& 0 \\
2 \otimes 1 &\overset{\text{已知 1(b)}}{=}& 2 \\
2 \otimes 2 &\overset{\text{已知 1(b)}}{=}& 4 \bmod 4 = 0 \\
2 \otimes 3 &\overset{\text{已知 1(b)}}{=}& 6 \bmod 4 = 2
\end{gather*}$$

結果只有 $0, 2$，從未得到 $1$ —— $2$ 沒有反元素，故 $\mathbf{Z}_4$ 不是體，與【已知 1(a)】（$4$ 是合數）一致。

* 註：**$GF(4) \neq \mathbf{Z}_4$。** 四個元素的體存在，但它的運算**不是**模 $4$ 的整數運算。
  這是初學者最常見的誤解，同理 $GF(2^8) \neq \mathbf{Z}_{256}$。

### (b) verify the irreducibility and the two factorizations of the quadratic

**$GF(2)$ 上不可約**：代入兩個元素都不是 $0$，由【已知 2】（次數 $2$）不可約：

$$\begin{gather*}
f(0) &=& 0 + 0 + 1 = 1 \\
f(1) &\overset{\text{已知 1(b)}}{=}& 1 + 1 + 1 = 3 \bmod 2 = 1 \\
f &\overset{\text{已知 2}}{=}& \text{在 } GF(2) \text{ 上不可約}
\end{gather*}$$

**$GF(3)$ 上可約**：

$$\begin{gather*}
\left(x + 2\right)^2 &=& x^2 + 4x + 4 \\
\left(x + 2\right)^2 &\overset{\text{已知 1(b)}}{=}& x^2 + x + 1 \qquad \text{(} 4 \bmod 3 = 1\text{)}
\end{gather*}$$

**$\mathbf{C}$ 上可約**：先驗證 $\omega^2$ 就是另一個根 $\bar{\omega}$，再用根與係數：

$$\begin{gather*}
\omega^2 &=& \tfrac{1 - 2\sqrt{3}\,i - 3}{4} = \tfrac{-1 - \sqrt{3}\,i}{2} = \bar{\omega} \\
\omega + \omega^2 &=& -1 \\
\omega \cdot \omega^2 &=& \tfrac{1}{4} + \tfrac{3}{4} = 1 \\
\left(x - \omega\right)\left(x - \omega^2\right) &=& x^2 - \left(\omega + \omega^2\right)x + \omega^3 \\
\left(x - \omega\right)\left(x - \omega^2\right) &=& x^2 + x + 1
\end{gather*}$$

與投影片一致。又 $f(0) = f(1) = 1 \neq 0$ 正是投影片寫的「It is confirmed by $f(0) = f(1) = 1 \neq 0$」。

### (c) verify the multiplication table of the linear polynomials

依【定義 1】展開後用【推導 1】降次。三個非平凡的格子：

$$\begin{gather*}
x \otimes x &\overset{\text{定義 1}}{=}& x^2 \bmod \left(x^2 + x + 1\right) \\
x \otimes x &\overset{\text{推導 1}}{=}& x + 1 \\
x \otimes \left(x + 1\right) &\overset{\text{定義 1}}{=}& \left(x^2 + x\right) \bmod \left(x^2 + x + 1\right) \\
x \otimes \left(x + 1\right) &\overset{\text{推導 1}}{=}& \left(x + 1\right) + x = 2x + 1 \equiv 1 \\
\left(x + 1\right) \otimes \left(x + 1\right) &\overset{\text{定義 1}}{=}& \left(x^2 + 2x + 1\right) \bmod 2 \bmod \left(x^2 + x + 1\right) \\
\left(x + 1\right) \otimes \left(x + 1\right) &\overset{\text{推導 1}}{=}& \left(x + 1\right) + 1 \equiv x
\end{gather*}$$

其餘格子只涉及 $0$ 與 $1$，直接由乘以 $0$ 得 $0$、乘以 $1$ 不變。
表與投影片 p.13 一致。從表中讀出反元素：

$$1^{-1} = 1, \qquad x^{-1} = x + 1, \qquad \left(x + 1\right)^{-1} = x$$

**每個非零元素都有乘法反元素**，與投影片 p.13 的 Note 一致。

### (d) proof that the congruence classes form a field with four elements

由【證明 (b)】$x^2 + x + 1$ 在 $GF(2)$ 上不可約：

$$\begin{gather*}
GF(2)[x]\big/\left\langle x^2 + x + 1 \right\rangle &\overset{\text{已知 3}}{=}& \text{體} \\
\left|GF(2)[x]\big/\left\langle x^2 + x + 1 \right\rangle\right| &\overset{\text{已知 4}}{=}& 2^2 = 4 \\
\left\{\text{同餘類}\right\} &\overset{\text{已知 4}}{=}& \left\{\left[0\right], \left[1\right], \left[x\right], \left[x+1\right]\right\}
\end{gather*}$$

與投影片 p.12「$p(x) \bmod f(x) = 0, 1, x$, or $x + 1$」、p.14「the congruence classes are $[0], [1], [x], [x+1]$」一致。

### (e) verify the arithmetic of the fixed root

依【定義 2】把 $\alpha^2$ 換掉：

$$\begin{gather*}
\left(\alpha + 1\right)\left(\alpha + 1\right) &=& \alpha^2 + 2\alpha + 1 \\
&\overset{\text{已知 1(b)}}{=}& \alpha^2 + 1 \\
&\overset{\text{定義 2}}{=}& \left(\alpha + 1\right) + 1 \\
&\overset{\text{已知 1(b)}}{=}& \alpha
\end{gather*}$$

與投影片 p.15 的「e.g. $\left(\alpha+1\right)\left(\alpha+1\right) = \alpha^2 + 2\alpha + 1 = \left(\alpha + 1\right) + 1 = \alpha$」一致。

### (f) proof that the three constructions are isomorphic

定義三者之間的對應（係數相同者互相對應）：

$$a_1 x + a_2 \ \longleftrightarrow \ \left[a_1 x + a_2\right] \ \longleftrightarrow \ a_1 \alpha + a_2$$

**加法**：三者都是係數逐項模 $2$ 相加（【定義 1】、【已知 5】、【定義 2】的「$+$ modulo 2」），對應保持。
**乘法**：三者都是「展開後，把 $x^2$（或 $\left[x\right]^2$、$\alpha^2$）換成 $x + 1$（或 $\left[x+1\right]$、$\alpha + 1$）」：

$$\begin{gather*}
\left(a_1x + a_2\right) \otimes \left(b_1x + b_2\right) &\overset{\text{定義 1,推導 1}}{=}& a_1b_1\left(x + 1\right) + \left(a_1b_2 + a_2b_1\right)x + a_2b_2 \\
\left[a_1x + a_2\right] \otimes \left[b_1x + b_2\right] &\overset{\text{已知 5,已知 4,推導 1}}{=}& \left[a_1b_1\left(x + 1\right) + \left(a_1b_2 + a_2b_1\right)x + a_2b_2\right] \\
\left(a_1\alpha + a_2\right)\left(b_1\alpha + b_2\right) &\overset{\text{定義 2}}{=}& a_1b_1\left(\alpha + 1\right) + \left(a_1b_2 + a_2b_1\right)\alpha + a_2b_2
\end{gather*}$$

三條右式的係數完全相同，故對應保持乘法。三者同構。

* 註：這就是「同構」的精確意思 —— **換個名字，運算表一模一樣**。
  之後 [$GF(p^n)$ 的唯一性](../Structure/Uniqueness_of_GF_p_n.md) 會證明：所有 $4$ 元素的體都長這樣。

### (g) answer the two questions posed in the slides

**(1)** 在 $GF(11)$ 中代入全部 $11$ 個元素（由【已知 1(b)】取模 $11$）：

$$\begin{gather*}
f(0), f(1), f(2), f(3), f(4), f(5) &\overset{\text{已知 1(b)}}{=}& 1,\ 3,\ 7,\ 2,\ 10,\ 9 \\
f(6), f(7), f(8), f(9), f(10) &\overset{\text{已知 1(b)}}{=}& 10,\ 2,\ 7,\ 3,\ 1 \\
f &\overset{\text{已知 2}}{=}& \text{在 } GF(11) \text{ 上不可約}
\end{gather*}$$

**(2)** 由【已知 4】，$p(x) \bmod f(x)$ 恰為所有次數 $< 2$ 的多項式：

$$\left\{a x + b \ \middle|\ a, b \in GF(11)\right\}, \qquad \text{共 } 11^2 = 121 \ \text{個}$$

再由【已知 3】，它們構成 $GF(121)$。

* 註：(1) 的另一種看法：$f$ 的根是三次單位根 $\omega \neq 1$，它在 $GF(p)$ 中存在 $\Leftrightarrow$ $GF(p)^*$ 有 $3$ 階元素
  $\Leftrightarrow$ $3 \mid p - 1$（[有限體的乘法群是循環群](../Multiplicative_Group/Cyclic_Multiplicative_Group_of_Finite_Field.md)）。
  $11 - 1 = 10$ 不被 $3$ 整除，故無根；對照 $GF(7)$：$3 \mid 6$，$f(2) = 7 \equiv 0$，可約。

+++

## 意義與密碼學關聯 (Interpretation and Relevance to Cryptography)

### 三種構造，三種實作

| 構造 | 實作觀點 | 適合 |
|---|---|---|
| 一：一次多項式 + 取模 | 位元運算 + 條件 XOR | 硬體、位元切片 |
| 二：同餘類 | 數學證明（商環是體） | 證明正確性 |
| 三：固定根 $\alpha$ | 冪次表 $\alpha^i$ | 查表乘法（log/antilog） |

AES 規格書同時使用了三種觀點：位元組是構造一、正確性由構造二保證、
而某些實作用構造三的 $\log$ 表加速乘法。

### $GF(4)$ 在密碼學裡的蹤跡

$GF(4)$ 本身太小，但它是**塔式構造**的積木：
$GF(2^8) \cong GF\!\left(\left(\left(2^2\right)^2\right)^2\right)$，
AES S-box 的緊湊硬體實作（Canright 2005）正是把 $GF(2^8)$ 的求逆一路拆到 $GF(4)$ 與 $GF(2)$，
每一層都用 [塔定理](../../Abstract_Algebra/Field/Tower_Law.md) 保證正確。

### 程式思維

```python
# GF(4) 的元素用 2 位元整數表示：bit1 = a1（x 的係數），bit0 = a2
def gf4_mul(a, b):
    r = 0
    for i in range(2):                  # 無進位乘法
        if (b >> i) & 1:
            r ^= a << i
    if r & 0b100:                       # 推導 1：x^2 -> x + 1
        r ^= 0b111
    return r

table = [[gf4_mul(a, b) for b in range(4)] for a in range(4)]
assert table == [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 3, 1], [0, 3, 1, 2]]   # 投影片 p.13 最右表
```
