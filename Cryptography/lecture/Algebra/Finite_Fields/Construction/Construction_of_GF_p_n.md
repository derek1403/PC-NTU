# Construction of GF(p^n) (GF(p^n) 的構造)

+++

## 證明目標:

`FiniteFields.pdf` p.28–p.30；補充講義 §7.6（Theorem 7.9）。
把 $GF(4)$ 的構造一般化：**只要有一個 $n$ 次不可約多項式，就能造出 $p^n$ 個元素的體**，
而且它的元素就是「次數 $< n$ 的多項式」—— 電腦可以直接存成係數陣列。

* (a) 投影片 p.28 的 Theorem：設 $p$ 為質數、$q(x) \in GF(p)[x]$ 不可約且 $\deg q = n$，令

$$S = \left\{a_{n-1}x^{n-1} + \cdots + a_1 x + a_0 \ \middle|\ a_i \in GF(p)\right\}$$

  配上 $f \oplus g = f + g \bmod p$、$f \otimes g = \left(fg \bmod q\right) \bmod p$，則

$$\left(S, \oplus, \otimes\right) \ \text{是一個含 } p^n \text{ 個元素的體} \ = GF(p^n)$$

* (b) 投影片 p.30 的 Example：下列四個商環哪一個同構於 $GF(64)$？

$$A: \tfrac{GF(2)[x]}{\left\langle x^6 + x^2 + 1 \right\rangle}, \quad B: \tfrac{GF(2)[x]}{\left\langle x^6 + x^5 + \cdots + x + 1 \right\rangle}, \quad C: \tfrac{GF(2)[x]}{\left\langle x^6 + x^3 + 1 \right\rangle}, \quad D: \tfrac{GF(2)[x]}{\left\langle x^6 + x^4 + x^3 + x^2 + 1 \right\rangle}$$

  答案為 **C**。

* $p$ : 質數 (A prime) $[p \in \mathbf{P}]$
* $q(x)$ : $n$ 次不可約多項式 (An irreducible polynomial of degree $n$) $[q \in GF(p)[x]]$
* $n$ : 擴張次數 (The degree) $[n \in \mathbf{P}]$
* $S$ : 次數 $< n$ 的多項式集合 (The set of polynomials of degree $< n$) $[\text{集合}]$
* $\oplus,\ \otimes$ : $S$ 上的運算 (Operations on $S$) $[S \times S \to S]$
* 註：投影片 p.28 的條件 ② 寫 $\deg q = n > 1$；**$n = 1$ 時定理同樣成立**（$S = GF(p)$ 本身），
  $> 1$ 只是為了強調「新的」體。
* 註：本定理的數學核心 ——「模不可約多項式的商環是體」—— 已於
  [模不可約多項式的商環是體](../../Abstract_Algebra/Field/Quotient_by_Irreducible_is_Field.md)【證明 (a)(b)】證明。
  本檔的工作是證明投影片的「餘式集合 $S$」**就是**那個商環（同構），不重證體公理。
* 註：投影片 p.29 的 Proof (Sketch) 兩步（① 恰 $p^n$ 個餘式、② 非零元素有反元素「since $q(x)$ is irreducible」）
  分別對應【已知 2】與【已知 1(a)】。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [模不可約多項式的商環是體 (Quotient by an irreducible polynomial is a field)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Field/Quotient_by_Irreducible_is_Field.html#a-proof-that-the-quotient-by-an-irreducible-polynomial-is-a-field)：** 已於 [模不可約多項式的商環是體](../../Abstract_Algebra/Field/Quotient_by_Irreducible_is_Field.md)【證明 (a)(b)】完整證明，此處直接引用不再重證

  * (a) 商環是體：

    $$q \ \text{不可約} \quad \Longrightarrow \quad F[x]\big/\left\langle q \right\rangle \ \text{為體}$$

  * (b) 擴張次數等於 $\deg q$：

    $$\left[F[x]\big/\left\langle q \right\rangle : F\right] = \deg q$$

  * $F$ : 係數體 (The coefficient field) $[\text{體}]$
  * $q$ : 不可約多項式 (An irreducible polynomial) $[q \in F[x]]$

* **【已知 2】 [同餘類與餘式一一對應 (Residue classes correspond to remainders)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Finite_Fields/Polynomial_Arithmetic/Division_Algorithm_for_Polynomials.html#d-proof-that-the-residues-modulo-a-polynomial-are-counted-by-the-remainders)：** 已於本章 [多項式的除法原理](../Polynomial_Arithmetic/Division_Algorithm_for_Polynomials.md)【證明 (d)】完整證明，此處直接引用不再重證

  * (a) 每個同餘類恰含一個次數 $< \deg m$ 的餘式：

    $$\left[g\right] = \left[g \bmod m\right], \qquad \left[r_1\right] = \left[r_2\right],\ \deg r_i < \deg m \ \Longrightarrow \ r_1 = r_2$$

  * (b) 計數：

    $$\left|F[x]\big/\left\langle m \right\rangle\right| = \left|F\right|^{\deg m}$$

  * $m$ : 模多項式 (The modulus) $[m \in F[x]]$
  * $g,\ r_1,\ r_2$ : 多項式 (Polynomials) $[\in F[x]]$

* **【已知 3】 [商環的運算 (Operations in the quotient ring)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Ring/Quotient_Ring.html#c-proof-that-the-quotient-is-a-ring)：** 已於 [商環](../../Abstract_Algebra/Ring/Quotient_Ring.md)【證明 (a)(b)(c)】完整證明，此處直接引用不再重證

  $$\left[g\right] + \left[h\right] = \left[g + h\right], \qquad \left[g\right]\left[h\right] = \left[gh\right]$$

  * $g,\ h$ : 多項式 (Polynomials) $[g, h \in F[x]]$

* **【已知 4】 [多項式的唯一分解與低次質多項式表 (Unique factorization and the table of low-degree primes)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Finite_Fields/Polynomial_Arithmetic/Unique_Factorization_of_Polynomials.html#d-verify-the-sieve-for-prime-polynomials-of-low-degree-over-the-binary-field)：** 已於本章 [多項式的唯一分解](../Polynomial_Arithmetic/Unique_Factorization_of_Polynomials.md)【證明 (b)(c)(d)】完整證明，此處直接引用不再重證

  * (a) 每個次數 $\ge 1$ 的多項式都有質多項式因式：

    $$\deg g \ge 1 \quad \Longrightarrow \quad \exists \ \text{質多項式} \ a \mid g, \ \deg a \le \deg g$$

  * (b) $GF(2)[x]$ 中次數 $\le 3$ 的質多項式恰為：

    $$x, \quad x + 1, \quad x^2 + x + 1, \quad x^3 + x + 1, \quad x^3 + x^2 + 1$$

  * $g$ : 多項式 (A polynomial) $[g \in F[x]]$
  * $a$ : 質多項式 (A prime polynomial) $[a \in F[x]]$

* **【已知 5】 [新生之夢 (Freshman's dream)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Field/Freshmans_Dream.html#a-proof-of-the-base-case)：** 已於 [新生之夢](../../Abstract_Algebra/Field/Freshmans_Dream.md)【證明 (a)】完整證明，此處直接引用不再重證（對交換環 $GF(2)[x]$ 同樣成立，證明只用到二項式定理與特徵）

  $$\left(a + b\right)^2 = a^2 + b^2 \qquad \left(\text{特徵 } 2\right)$$

  * $a,\ b$ : 特徵 $2$ 交換環的元素 (Elements of a commutative ring of characteristic $2$) $[a, b \in GF(2)[x]]$

* **【已知 6】 [體無零因子 (A field has no zero divisors)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Field/Field_Definition.html#d-proof-that-every-field-is-an-integral-domain)：** 已於 [體的定義](../../Abstract_Algebra/Field/Field_Definition.md)【證明 (d)】完整證明，此處直接引用不再重證

  $$F \ \text{為體} \quad \Longrightarrow \quad F \ \text{無零因子}$$

  * $F$ : 體 (A field) $[\text{體}]$

* **【假設 1】 投影片 p.28 的前提 ①② (Hypotheses ① and ②)：**

  $$p \ \text{為質數}, \qquad q(x) \in GF(p)[x] \ \text{不可約}, \qquad \deg q = n$$

  * $p$ : 質數 (A prime) $[p \in \mathbf{P}]$
  * $q(x)$ : 不可約多項式 (An irreducible polynomial) $[q \in GF(p)[x]]$

* **【定義 1】 投影片 p.28 的 ③④⑤ (Definitions ③–⑤)：** 餘式集合與其運算

  $$S \overset{\text{def}}{=} \left\{r \in GF(p)[x] \ \middle|\ r = 0 \ \text{或} \ \deg r < n\right\}, \qquad f \oplus g \overset{\text{def}}{=} f + g, \qquad f \otimes g \overset{\text{def}}{=} fg \bmod q$$

  * $f,\ g$ : $S$ 的元素 (Elements of $S$) $[f, g \in S]$
  * 註：投影片寫的「$\bmod p$」只是提醒係數在 $GF(p)$ 中運算，已含在「$GF(p)[x]$」的意思裡。
  * 註：兩個次數 $< n$ 的多項式相加，次數仍 $< n$，故 $\oplus$ 不需要再模 $q$。

* **【推導 1】 可約多項式必有低次質因式 (A reducible polynomial has a low-degree prime factor)：** 【證明 (b)】的判準

  $$\begin{gather*}
  f &=& g\,h \qquad \text{with } 1 \le \deg g \le \deg h \\
  \deg g &\le& \tfrac{1}{2}\deg f \\
  a &\overset{\text{已知 4(a)}}{\mid}& g \qquad \text{(} a \text{ 質多項式}, \ \deg a \le \deg g\text{)} \\
  a &\mid& f, \qquad \deg a \le \tfrac{1}{2}\deg f
  \end{gather*}$$

  * $f$ : 可約多項式 (A reducible polynomial) $[f \in F[x]]$
  * $g,\ h$ : 非常數因式 (Non-constant factors) $[g, h \in F[x]]$
  * 註：逆否形式：**若 $f$ 不被任何次數 $\le \tfrac{1}{2}\deg f$ 的質多項式整除，$f$ 就不可約**。這就是試除法。

* **【推導 2】 可約模數產生零因子 (A reducible modulus produces zero divisors)：** 【證明 (b)】排除 A、B、D 用

  $$\begin{gather*}
  m &=& g\,h \qquad \text{with } 1 \le \deg g,\ \deg h < \deg m \\
  \left[g\right],\ \left[h\right] &\overset{\text{已知 2(a)}}{\neq}& \left[0\right] \qquad \text{(次數 } < \deg m \text{ 的非零餘式)} \\
  \left[g\right]\left[h\right] &\overset{\text{已知 3}}{=}& \left[m\right] = \left[0\right] \\
  F[x]\big/\left\langle m \right\rangle &\overset{\text{已知 6}}{\neq}& \text{體}
  \end{gather*}$$

  * $m$ : 可約的模多項式 (A reducible modulus) $[m \in F[x]]$
  * $g,\ h$ : 其非常數因式 (Its non-constant factors) $[g, h \in F[x]]$

+++

## 證明:

### (a) proof that the remainder set is a field with p to the n elements

定義 $\psi : S \to GF(p)[x]\big/\left\langle q \right\rangle$，$\psi(r) = \left[r\right]$。**雙射**：

$$\begin{gather*}
\psi(r_1) = \psi(r_2) &\overset{\text{已知 2(a)}}{\Longrightarrow}& r_1 = r_2 \qquad \text{(單射)} \\
\left[g\right] = \left[g \bmod q\right] &\overset{\text{已知 2(a)}}{=}& \psi\left(g \bmod q\right) \qquad \text{(滿射)}
\end{gather*}$$

**保加法與乘法**：

$$\begin{gather*}
\psi\left(f \oplus g\right) &\overset{\text{定義 1}}{=}& \left[f + g\right] \\
\psi\left(f \oplus g\right) &\overset{\text{已知 3}}{=}& \left[f\right] + \left[g\right] \\
\psi\left(f \otimes g\right) &\overset{\text{定義 1}}{=}& \left[fg \bmod q\right] \\
\psi\left(f \otimes g\right) &\overset{\text{已知 2(a)}}{=}& \left[fg\right] \\
\psi\left(f \otimes g\right) &\overset{\text{已知 3}}{=}& \left[f\right]\left[g\right]
\end{gather*}$$

故 $S \cong GF(p)[x]/\left\langle q \right\rangle$，而後者是體、元素個數為 $p^n$：

$$\begin{gather*}
GF(p)[x]\big/\left\langle q \right\rangle &\overset{\text{已知 1(a),假設 1}}{=}& \text{體} \\
\left|S\right| = \left|GF(p)[x]\big/\left\langle q \right\rangle\right| &\overset{\text{已知 2(b)}}{=}& p^n \\
\left[S : GF(p)\right] &\overset{\text{已知 1(b)}}{=}& n
\end{gather*}$$

與投影片 p.28 的 Conclusion 一致，也與補充講義 Theorem 7.9 一致。

* 註：補充講義的證法是**直接**驗證 $S$ 的體公理（Exercise 10：分配律、消去律、「乘以非零 $r$ 是 $S^*$ 的排列」）。
  本檔改用「$S$ 同構於一個已知是體的商環」，省去重驗公理 —— 這正是同構的用處。

### (b) verify which quotient ring is isomorphic to the field with sixty-four elements

**A**：由【已知 5】，特徵 $2$ 中平方可以逐項進行：

$$\begin{gather*}
\left(x^3 + x + 1\right)^2 &\overset{\text{已知 5}}{=}& x^6 + x^2 + 1 \\
A &\overset{\text{推導 2}}{\neq}& \text{體}
\end{gather*}$$

**B**：展開後 $x^3$ 出現三次、$3 \equiv 1$：

$$\begin{gather*}
\left(x^3 + x^2 + 1\right)\left(x^3 + x + 1\right) &=& x^6 + x^5 + x^4 + 3x^3 + x^2 + x + 1 \\
\left(x^3 + x^2 + 1\right)\left(x^3 + x + 1\right) &=& x^6 + x^5 + x^4 + x^3 + x^2 + x + 1 \\
B &\overset{\text{推導 2}}{\neq}& \text{體}
\end{gather*}$$

**D**：

$$\begin{gather*}
\left(x^2 + x + 1\right)\left(x^4 + x^3 + x^2 + x + 1\right) &=& x^6 + 2x^5 + 3x^4 + 3x^3 + 3x^2 + 2x + 1 \\
\left(x^2 + x + 1\right)\left(x^4 + x^3 + x^2 + x + 1\right) &=& x^6 + x^4 + x^3 + x^2 + 1 \\
D &\overset{\text{推導 2}}{\neq}& \text{體}
\end{gather*}$$

**C**：由【推導 1】只需試除次數 $\le 3$ 的五個質多項式（【已知 4(b)】）。
用 $x^3 \equiv$ 各模數的餘式反覆降次，五個餘式全不為零：

$$\begin{gather*}
\left(x^6 + x^3 + 1\right) \bmod x &=& 1 \\
\left(x^6 + x^3 + 1\right) \bmod \left(x + 1\right) &=& 1 + 1 + 1 \equiv 1 \\
\left(x^6 + x^3 + 1\right) \bmod \left(x^2 + x + 1\right) &=& 1 + 1 + 1 \equiv 1 \qquad \text{(} x^3 \equiv 1\text{)} \\
\left(x^6 + x^3 + 1\right) \bmod \left(x^3 + x + 1\right) &=& \left(x^2 + 1\right) + \left(x + 1\right) + 1 \equiv x^2 + x + 1 \qquad \text{(} x^3 \equiv x + 1\text{)} \\
\left(x^6 + x^3 + 1\right) \bmod \left(x^3 + x^2 + 1\right) &=& \left(x^2 + x\right) + \left(x^2 + 1\right) + 1 \equiv x \qquad \text{(} x^3 \equiv x^2 + 1\text{)} \\
x^6 + x^3 + 1 &\overset{\text{推導 1,已知 4(b)}}{=}& \text{不可約}
\end{gather*}$$

由【證明 (a)】（$p = 2$、$n = 6$），C 是含 $2^6 = 64$ 個元素的體。與投影片 p.30 一致。

* 註：第四、五列的 $x^6$ 降次：模 $x^3 + x + 1$ 時 $x^6 = \left(x^3\right)^2 \equiv \left(x + 1\right)^2 = x^2 + 1$；
  模 $x^3 + x^2 + 1$ 時 $x^6 \equiv \left(x^2 + 1\right)^2 = x^4 + 1$，而 $x^4 = x \cdot x^3 \equiv x^3 + x \equiv x^2 + x + 1$，故 $x^6 \equiv x^2 + x$。
* 註：D 的模數**沒有根**（$f(0) = f(1) = 1$）卻可約 —— 又一個「次數 $\ge 4$ 不能只檢查根」的例子
  （[不可約多項式](../../Abstract_Algebra/Field/Irreducible_Polynomial.md)【證明 (c)】）。

+++

## 意義與密碼學關聯 (Interpretation and Relevance to Cryptography)

### 從定理到資料結構

(a) 把抽象的商環變成具體的資料結構：

| 數學 | 程式 |
|---|---|
| $S$ 的元素 $a_{n-1}x^{n-1} + \cdots + a_0$ | 長度 $n$ 的陣列（$p = 2$ 時就是 $n$ 位元整數） |
| $\oplus$ | 逐項模 $p$ 相加（$p = 2$ 時是 XOR） |
| $\otimes$ | 多項式乘法 + 模 $q$ 約化 |
| 反元素 | 擴展歐幾里得（[歐幾里得整環](../Polynomial_Arithmetic/Euclidean_Domain.md)） |

AES 取 $p = 2$、$n = 8$、$q = x^8 + x^4 + x^3 + x + 1$；AES-GCM 的 GHASH 取 $n = 128$、
$q = x^{128} + x^7 + x^2 + x + 1$。**兩者都只是 (a) 的特例。**

### 選錯模數的後果

(b) 的 A、B、D 看起來都是「六次多項式」，但模它們得到的環有零因子（【推導 2】）：
某些非零元素相乘得零、沒有反元素。若用在 S-box 這類需要「取反元素」的構件，
部分輸入會無法定義或碰撞，**加密變得不可逆**。這就是規格書必須寫明模多項式、
且實作者必須驗證其不可約性的原因。

### 程式思維

```python
def gf2_mod(a, m):
    """GF(2)[x] 取模（位元表示）：推導 1 的試除法會用到。"""
    while a and a.bit_length() >= m.bit_length():
        a ^= m << (a.bit_length() - m.bit_length())
    return a

C = 0b1001001                                    # x^6 + x^3 + 1
low_primes = [0b10, 0b11, 0b111, 0b1011, 0b1101]  # 已知 4(b)
assert [gf2_mod(C, g) for g in low_primes] == [1, 1, 1, 0b111, 0b10]   # 證明 (b)：全不為 0
```
