# Unique Factorization of Polynomials (多項式的唯一分解)

+++

## 證明目標:

**本檔內容只出現在補充講義** `Introduction_to_Finite_Fields.pdf` §7.5.1、§7.5.3、§7.5.4（Theorem 7.8、Exercise 9），
投影片未列。它是「$x^{p^n} - x$ 等於所有某些次數的不可約多項式之積」（[$x^{p^n}-x$ 的分解](../Multiplicative_Group/Factorization_of_x_p_n_minus_x.md)）
能成立的根據 —— 沒有唯一分解，「乘積」就可能有好幾種寫法。

* (a) 歐幾里得引理（多項式版）：

$$p \ \text{不可約}, \quad p \mid ab \quad \Longrightarrow \quad p \mid a \ \text{或} \ p \mid b$$

* (b) 存在性：每個次數 $\ge 1$ 的首一多項式都能寫成首一不可約多項式（質多項式）的乘積：

$$f(x) = \prod_{i=1}^{k} a_i(x)$$

* (c) 唯一性（補充講義 Theorem 7.8）：上式的因式**在不計順序下唯一**。

* (d) 補充講義 §7.5.4 的「篩法」：$GF(2)[x]$ 中次數 $\le 3$ 的質多項式恰為

$$x, \quad x + 1, \quad x^2 + x + 1, \quad x^3 + x + 1, \quad x^3 + x^2 + 1$$

* $F$ : 係數所在的體 (The field of coefficients) $[\text{體}]$
* $f$ : 被分解的首一多項式 (The monic polynomial being factored) $[f \in F[x],\ \deg f \ge 1]$
* $a_i,\ b_j$ : 質多項式（首一不可約） (Prime polynomials) $[a_i, b_j \in F[x]]$
* $p$ : 不可約多項式 (An irreducible polynomial) $[p \in F[x]]$
* $a,\ b$ : 任意多項式 (Arbitrary polynomials) $[a, b \in F[x]]$
* 註：補充講義證明唯一性的方式是「取最小反例、用除法造出更小的反例」；
  本檔改走**歐幾里得引理 + 歸納法**的路線（與整數算術基本定理的標準證法平行）。結論相同。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [多項式版貝祖等式 (Bézout's identity for polynomials)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Finite_Fields/Polynomial_Arithmetic/Euclidean_Domain.html#e-proof-that-the-extended-euclidean-algorithm-works-for-polynomials)：** 已於本章 [歐幾里得整環](Euclidean_Domain.md)【證明 (e)】完整證明，此處直接引用不再重證

  $$\exists\, u, v \in F[x] \ \text{ with } \ a\,u + b\,v = \gcd\left(a, b\right)$$

  * $a,\ b,\ u,\ v$ : 多項式 (Polynomials) $[\in F[x]]$

* **【已知 2】 [不可約多項式與不整除它的多項式互質 (An irreducible polynomial is coprime to anything it does not divide)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Field/Quotient_by_Irreducible_is_Field.html#assumptions-preliminaries)：** 已於 [模不可約多項式的商環是體](../../Abstract_Algebra/Field/Quotient_by_Irreducible_is_Field.md)【推導 1】完整證明，此處直接引用不再重證

  $$p \ \text{不可約}, \quad p \nmid f \quad \Longrightarrow \quad \gcd\left(p, f\right) = 1$$

  * $p$ : 不可約多項式 (An irreducible polynomial) $[p \in F[x]]$
  * $f$ : 不被 $p$ 整除的多項式 (A polynomial not divisible by $p$) $[f \in F[x]]$

* **【已知 3】 [不可約多項式的定義 (Definition of an irreducible polynomial)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Field/Irreducible_Polynomial.html#assumptions-preliminaries)：** 已於 [不可約多項式](../../Abstract_Algebra/Field/Irreducible_Polynomial.md)【定義 1】給出，此處直接引用

  $$p \ \text{不可約} \quad \Longleftrightarrow \quad \deg p \ge 1 \ \text{ 且 } \ \left[\, p = gh \Longrightarrow \deg g = 0 \ \text{或} \ \deg h = 0 \,\right]$$

  * $g,\ h$ : 因式 (Factors) $[g, h \in F[x]]$

* **【已知 4】 [次數相加與二三次不可約判別法 (Degree additivity and the root criterion)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Field/Irreducible_Polynomial.html#a-proof-of-the-root-criterion-for-degrees-two-and-three)：** 已於本章 [體上的多項式環](Polynomial_Ring_over_a_Field.md)【證明 (b)】與 [不可約多項式](../../Abstract_Algebra/Field/Irreducible_Polynomial.md)【證明 (a)】完整證明，此處直接引用不再重證

  * (a) 次數相加：

    $$\deg\left(gh\right) = \deg g + \deg h$$

  * (b) 次數 $2, 3$ 時「不可約 $\Leftrightarrow$ 無根」：

    $$\deg f \in \left\{2, 3\right\} \quad \Longrightarrow \quad \left[\, f \ \text{不可約} \Leftrightarrow f \ \text{在 } F \text{ 中無根} \,\right]$$

  * $f,\ g,\ h$ : 多項式 (Polynomials) $[\in F[x]]$

* **【已知 5】 [強歸納法 (Strong induction)](https://mathworld.wolfram.com/PrincipleofStrongInduction.html)：** 標準結果，直接引用不再重證

  $$\left[\,\forall N:\ \left(P(k) \ \forall k < N\right) \Longrightarrow P(N)\,\right] \quad \Longrightarrow \quad P(N) \ \forall N$$

  * $P$ : 待證命題 (The statement to be proved) $[\mathbf{N} \to \left\{\text{真},\text{假}\right\}]$

* **【定義 1】 首一多項式與質多項式 (Monic and prime polynomials)：** 補充講義 §7.5.1

  $$f \ \text{首一} \ \overset{\text{def}}{\Longleftrightarrow} \ \mathrm{LT}(f) = x^{\deg f}, \qquad f \ \text{為質多項式} \ \overset{\text{def}}{\Longleftrightarrow} \ f \ \text{首一且不可約}$$

  * $f$ : 多項式 (A polynomial) $[f \in F[x]]$
  * $\mathrm{LT}$ : 首項 (Leading term) $[F[x] \setminus \left\{0\right\} \to F[x]]$
  * 註：每個非零多項式都唯一地寫成「非零常數 $\times$ 首一多項式」，故只需討論首一的分解。

* **【假設 1】 歐幾里得引理的前提 (Hypotheses of Euclid's lemma)：** 【證明 (a)】的出發點

  $$p \ \text{不可約}, \qquad p \mid ab, \qquad p \nmid a$$

  * $p$ : 不可約多項式 (An irreducible polynomial) $[p \in F[x]]$
  * $a,\ b$ : 多項式 (Polynomials) $[a, b \in F[x]]$

* **【假設 2】 存在性的歸納假設 (Induction hypothesis for existence)：** 【證明 (b)】用

  $$\deg g < N, \ g \ \text{首一} \quad \Longrightarrow \quad g \ \text{是質多項式之積}$$

  * $g$ : 次數較低的首一多項式 (A monic polynomial of lower degree) $[g \in F[x]]$
  * $N$ : 當前歸納的次數 (The current degree) $[N \in \mathbf{P}]$

* **【假設 3】 唯一性的歸納假設 (Induction hypothesis for uniqueness)：** 【證明 (c)】用

  $$\deg g < N \quad \Longrightarrow \quad g \ \text{的質多項式分解在不計順序下唯一}$$

  * $g$ : 次數較低的首一多項式 (A monic polynomial of lower degree) $[g \in F[x]]$

* **【推導 1】 首一不可約整除首一不可約必相等 (A prime polynomial dividing another prime polynomial equals it)：** 【證明 (c)】要用

  $$\begin{gather*}
  b &=& a\,c \qquad \text{(} a \mid b\text{；} a, b \text{ 皆為質多項式)} \\
  \deg a &\overset{\text{定義 1,已知 3}}{\ge}& 1 \\
  \deg c &\overset{\text{已知 3}}{=}& 0 \qquad \text{(} b \text{ 不可約且 } \deg a \ge 1\text{)} \\
  c &=& 1 \qquad \text{(比較首項係數：} a, b \text{ 首一)} \\
  a &=& b
  \end{gather*}$$

  * $a,\ b$ : 質多項式 (Prime polynomials) $[a, b \in F[x]]$
  * $c$ : 商 (The quotient) $[c \in F[x]]$

+++

## 證明:

### (a) proof of Euclid's lemma for polynomials

由【假設 1】$p \nmid a$，套【已知 2】得互質，再套貝祖等式：

$$\begin{gather*}
\gcd\left(p, a\right) &\overset{\text{已知 2,假設 1}}{=}& 1 \\
p\,u + a\,v &\overset{\text{已知 1}}{=}& 1 \\
p\,u\,b + a\,b\,v &=& b \\
p \mid p\,u\,b, \quad p &\overset{\text{假設 1}}{\mid}& a\,b\,v \\
p &\mid& b
\end{gather*}$$

* 註：與整數的歐幾里得引理（質數 $p \mid ab \Rightarrow p \mid a$ 或 $p \mid b$）逐字相同。
  「不可約」在這裡的作用與「質數」完全一樣 —— 讓 $\gcd$ 只有 $1$ 與 $p$ 兩種可能。
* 註：反覆套用得推廣形式：$p \mid b_1 b_2 \cdots b_j \Rightarrow p \mid b_i$（某個 $i$）——
  對 $j$ 歸納，每次把乘積拆成 $b_1 \cdot \left(b_2 \cdots b_j\right)$。

### (b) proof of the existence of a factorization into prime polynomials

對 $N = \deg f$ 做強歸納。**若 $f$ 不可約**，它自己就是一個質多項式（$k = 1$）。
**若 $f$ 可約**，拆成兩個次數較低的因式，各自化為首一後套【假設 2】：

$$\begin{gather*}
f &\overset{\text{已知 3}}{=}& g\,h \qquad \text{with } \deg g,\ \deg h \ge 1 \\
\deg g + \deg h &\overset{\text{已知 4(a)}}{=}& N \\
\deg g,\ \deg h &<& N \\
f &=& \left(c^{-1}g\right)\left(c\,h\right) \qquad \text{(} c = g \text{ 的首項係數；兩者皆首一)} \\
c^{-1}g,\ c\,h &\overset{\text{假設 2}}{=}& \text{質多項式之積} \\
f &=& \text{質多項式之積}
\end{gather*}$$

$$\text{存在性對所有 } N \ge 1 \ \text{成立} \quad \overset{\text{已知 5}}{\Longleftarrow} \quad \text{上述歸納步驟（} N = 1 \text{ 時 } f \text{ 必不可約）}$$

* 註：「$c\,h$ 首一」是因為 $f$ 首一：$1 = \left(g \text{ 的首項係數}\right)\left(h \text{ 的首項係數}\right) = c \cdot \left(h \text{ 的首項係數}\right)$。

### (c) proof of the uniqueness of the factorization

設同一個 $f$（次數 $N$）有兩種分解，並設【假設 3】對更低的次數成立：

$$\begin{gather*}
a_1 a_2 \cdots a_k &=& b_1 b_2 \cdots b_j \\
a_1 &\mid& b_1 b_2 \cdots b_j \\
a_1 &\overset{\text{證明 (a)}}{\mid}& b_i \qquad \text{for some } i \\
a_1 &\overset{\text{推導 1}}{=}& b_i \\
a_2 \cdots a_k &=& \prod_{l \neq i} b_l \qquad \text{(兩邊消去 } a_1\text{；} F[x] \text{ 為整環)} \\
\deg\left(a_2 \cdots a_k\right) &\overset{\text{已知 4(a)}}{=}& N - \deg a_1 < N \\
\left\{a_2, \dots, a_k\right\} &\overset{\text{假設 3}}{=}& \left\{b_l \ \middle|\ l \neq i\right\} \qquad \text{(作為可重複集合)}
\end{gather*}$$

再把 $a_1 = b_i$ 放回，兩組因式完全相同。由【已知 5】，對所有次數成立。

* 註：基底情形是 $\deg f = 1$：$f$ 本身不可約，只有「自己」一種分解。
* 註：**唯一性的關鍵是 (a)**。在沒有歐幾里得引理的環裡（例如 $\mathbf{Z}\!\left[\sqrt{-5}\right]$），
  $6 = 2 \cdot 3 = \left(1 + \sqrt{-5}\right)\left(1 - \sqrt{-5}\right)$ 有兩種不同的「不可約分解」。

### (d) verify the sieve for prime polynomials of low degree over the binary field

**次數 1**：$x$、$x + 1$ 沒有更低次的非常數因式，都是質多項式。

**次數 2**：四個首一多項式中，三個是次數 1 質多項式的乘積：

$$\begin{gather*}
x^2 &=& x \cdot x \\
x^2 + x &=& x\left(x + 1\right) \\
x^2 + 1 &=& \left(x + 1\right)^2 \qquad \text{(} 2x = 0\text{)} \\
x^2 + x + 1 &\overset{\text{已知 4(b)}}{=}& \text{不可約} \qquad \text{(} 0 \mapsto 1,\ 1 \mapsto 1\text{，無根)}
\end{gather*}$$

**次數 3**：八個首一多項式中，六個是低次質多項式的乘積：

$$\begin{gather*}
x^3 &=& x \cdot x \cdot x \\
x^3 + x^2 &=& \left(x + 1\right) x \cdot x \\
x^3 + x &=& \left(x + 1\right)^2 x \\
x^3 + x^2 + x &=& x\left(x^2 + x + 1\right) \\
x^3 + 1 &=& \left(x + 1\right)\left(x^2 + x + 1\right) \\
x^3 + x^2 + x + 1 &=& \left(x + 1\right)^3
\end{gather*}$$

剩下兩個都沒有根，由【已知 4(b)】不可約：

$$\begin{gather*}
x^3 + x + 1 &\overset{\text{已知 4(b)}}{=}& \text{不可約} \qquad \text{(} 0 \mapsto 1,\ 1 \mapsto 1\text{)} \\
x^3 + x^2 + 1 &\overset{\text{已知 4(b)}}{=}& \text{不可約} \qquad \text{(} 0 \mapsto 1,\ 1 \mapsto 1\text{)}
\end{gather*}$$

與補充講義 §7.5.4 一致。以程式繼續篩（見文末），次數 4 有 3 個、次數 5 有 6 個（補充講義 Exercise 9 的提示）：

$$x^4 + x + 1,\ \ x^4 + x^3 + 1,\ \ x^4 + x^3 + x^2 + x + 1; \qquad x^5 + x^2 + 1,\ \ x^5 + x^3 + 1,\ \ x^5 + x^3 + x^2 + x + 1,\ \ x^5 + x^4 + x^2 + x + 1,\ \ x^5 + x^4 + x^3 + x + 1,\ \ x^5 + x^4 + x^3 + x^2 + 1$$

* 註：次數 4、5 **不能**只檢查根（見 [不可約多項式](../../Abstract_Algebra/Field/Irreducible_Polynomial.md)【證明 (c)】），
  篩法之所以可靠，正是因為 (b)(c)：可約的多項式**一定**是某些低次質多項式的乘積，會被篩掉。

+++

## 意義與密碼學關聯 (Interpretation and Relevance to Cryptography)

### 整數與多項式的最後一塊對照

| $\mathbf{Z}$ | $F[x]$ |
|---|---|
| 質數 | 質多項式（首一不可約） |
| 歐幾里得引理 | 【證明 (a)】 |
| 算術基本定理 | 【證明 (b)(c)】 |
| 埃拉托斯特尼篩法 | 【證明 (d)】的篩法 |
| 質數有無限多個 | 每個次數都有質多項式（[$x^{p^n}-x$ 的分解](../Multiplicative_Group/Factorization_of_x_p_n_minus_x.md)） |

### 分解多項式是容易的（與分解整數相反）

**整數分解是困難問題**（RSA 的安全性基礎），但**有限體上的多項式分解有多項式時間演算法**
（Berlekamp、Cantor–Zassenhaus）。這個不對稱是密碼學家必須知道的：
不能把「多項式分解很難」當作安全性假設。反過來，這也是為什麼
挑選 $GF(2^n)$ 的不可約多項式、驗證 CRC 生成多項式的結構都能**快速完成**。

### 程式思維

```python
def sieve_prime_polys_gf2(max_deg):
    """GF(2)[x] 的篩法：多項式以整數位元表示（bit i = x^i 的係數）。證明 (d)。"""
    def mod(a, b):
        while a and a.bit_length() >= b.bit_length():
            a ^= b << (a.bit_length() - b.bit_length())
        return a
    primes = []
    for f in range(2, 1 << (max_deg + 1)):          # 依次數由低到高列出（GF(2) 上非零多項式必為首一）
        d = f.bit_length() - 1
        # 由 (b)(c)：可約 <=> 被某個次數 <= d/2 的質多項式整除（篩掉倍數）
        if all(mod(f, p) for p in primes if 2 * (p.bit_length() - 1) <= d):
            primes.append(f)
    return primes

ps = sieve_prime_polys_gf2(5)
counts = [sum(1 for f in ps if f.bit_length() - 1 == d) for d in range(1, 6)]
assert counts == [2, 1, 2, 3, 6]      # 補充講義 N(m) = 2, 1, 2, 3, 6, ...
```
