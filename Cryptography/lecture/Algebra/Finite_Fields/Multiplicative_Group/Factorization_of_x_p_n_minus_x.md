# Factorization of x^(p^n) − x (x^(p^n) − x 的分解)

+++

## 證明目標:

`FiniteFields.pdf` p.18、p.22、p.43、p.44；補充講義 §7.8.3–§7.9（Lemma 7.17、Theorem 7.22、式 (7.8)、Theorem 7.23、Exercise 17、18）。
$x^{p^n} - x$ 是有限體理論的「萬用多項式」：它在 $GF(p)$ 上的分解，**一次列出所有次數整除 $n$ 的不可約多項式**。

* (a) 補充講義 Lemma 7.17（推廣）：$g$ 為 $GF(p)[x]$ 中的 $d$ 次質多項式、$d \mid n$，則

$$g(x) \ \Big|\ x^{p^n} - x$$

* (b) 反過來：$x^{p^n} - x$ 的每個質因式的次數都整除 $n$。

* (c) 投影片 p.43 的 Proposition 與補充講義 Theorem 7.22：

$$x^{p^n} - x = \prod_{d \mid n}\ \prod_{\substack{g \ \text{質多項式} \\ \deg g = d}} g(x) \qquad \text{（無重複因式）}$$

* (d) 補充講義式 (7.8) 與投影片 p.43 的問題：記 $N_p(d)$ 為 $d$ 次質多項式的個數，則

$$p^n = \sum_{d \mid n} d\,N_p(d), \qquad N_2(7) = 18, \qquad N_2(8) = 30$$

  並驗證投影片 p.18、p.22、p.43 與補充講義 Exercise 17 的分解。

* (e) 投影片 p.44 的 Theorem：對每個質數 $p$ 與 $n \in \mathbf{P}$，**存在 $n$ 次首一不可約多項式**。

* $p$ : 質數 (A prime) $[p \in \mathbf{P}]$
* $n,\ d$ : 正整數，$d \mid n$ (Positive integers) $[n, d \in \mathbf{P}]$
* $g$ : 質多項式（首一不可約）(A prime polynomial) $[g \in GF(p)[x]]$
* $N_p(d)$ : $GF(p)[x]$ 中 $d$ 次質多項式的個數 (The number of prime polynomials of degree $d$) $[N_p(d) \in \mathbf{N}]$
* 註：投影片 p.44 的 Proof (Sketch) 只寫「We obtain $m = n$ by showing $m \ge n$ and $m \le n$」，本檔 (e) 補齊兩個不等式的理由。
* 註：補充講義證 (e) 的方式是計數（Theorem 7.23：$n N(n) \ge p^n - \tfrac{n}{2}p^{n/2} > 0$）；
  本檔走投影片的路線（本原元的極小多項式），兩者皆可，(d) 的計數公式另外給出個數。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [GF(p^n) 的構造與 Kronecker 根 (Construction of GF(p^n) and the Kronecker root)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Finite_Fields/Construction/Splitting_Field.html#a-proof-that-every-polynomial-has-a-root-in-some-extension)：** 已於本章 [GF(p^n) 的構造](../Construction/Construction_of_GF_p_n.md)【證明 (a)】與 [分裂體](../Construction/Splitting_Field.md)【推導 1】完整證明，此處直接引用不再重證

  $$g \ \text{不可約},\ \deg g = d \quad \Longrightarrow \quad K = GF(p)[x]\big/\left\langle g \right\rangle \ \text{是 } p^d \text{ 元素的體}, \quad g\!\left(\left[x\right]\right) = 0$$

  * $K$ : 商環體 (The quotient field) $[\left|K\right| = p^d]$
  * $\left[x\right]$ : $x$ 的同餘類 (The class of $x$) $[\left[x\right] \in K]$

* **【已知 2】 [有限體版費馬 (Fermat's theorem in a finite field)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Finite_Fields/Structure/Roots_of_x_q_minus_x.html#a-proof-that-every-element-satisfies-the-finite-field-version-of-fermats-theorem)：** 已於本章 [$x^q - x$ 的根](../Structure/Roots_of_x_q_minus_x.md)【證明 (a)】完整證明，此處直接引用不再重證

  $$\left|K\right| = q \quad \Longrightarrow \quad y^q = y \quad \forall y \in K$$

* **【已知 3】 [極小多項式 (Minimal polynomial)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Finite_Fields/Multiplicative_Group/Minimal_Polynomial.html#d-proof-that-adjoining-the-element-gives-a-field-of-degree-equal-to-the-degree-of-the-minimal-polynomial)：** 已於本章 [極小多項式](Minimal_Polynomial.md)【證明 (b)(c)(d)】完整證明，此處直接引用不再重證

  * (a) 首一不可約零化多項式就是極小多項式，且它整除所有零化多項式：

    $$h \ \text{首一不可約},\ h(u) = 0 \ \Longrightarrow \ h = g_u; \qquad f(u) = 0 \ \Longleftrightarrow \ g_u \mid f$$

  * (b) 極小多項式不可約，且生成的子體：

    $$g_u \ \text{不可約}, \qquad \left|GF(p)[u]\right| = p^{\deg g_u}, \qquad \deg g_u \le \left[K : GF(p)\right]$$

  * $u$ : 有限擴張中的元素 (An element of a finite extension) $[u \in K]$
  * $g_u$ : $u$ 的極小多項式 (The minimal polynomial of $u$) $[g_u \in GF(p)[x]]$

* **【已知 4】 [係數在質子體的多項式與 $p$ 次方交換 (Polynomials over GF(p) commute with p-th powers)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Finite_Fields/Multiplicative_Group/Conjugates_and_Cyclotomic_Cosets.html#a-proof-that-the-p-th-powers-of-a-root-are-roots)：** 已於本章 [共軛元與分圓陪集](Conjugates_and_Cyclotomic_Cosets.md)【證明 (a)】的推導鏈給出，此處直接引用

  $$h \in GF(p)[x] \quad \Longrightarrow \quad h(u)^{p^r} = h\!\left(u^{p^r}\right)$$

  * $h$ : $GF(p)$ 係數的多項式 (A polynomial over $GF(p)$) $[h \in GF(p)[x]]$
  * $r$ : 自然數 (A natural number) $[r \in \mathbf{N}]$

* **【已知 5】 [n 次多項式最多 n 個根 (At most n roots)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Finite_Fields/Polynomial_Arithmetic/Roots_of_Polynomials.html#b-proof-that-a-non-zero-polynomial-of-degree-n-has-at-most-n-roots)：** 已於本章 [多項式的根](../Polynomial_Arithmetic/Roots_of_Polynomials.md)【證明 (b)】完整證明，此處直接引用不再重證

  $$f \neq 0,\ \deg f = N \quad \Longrightarrow \quad f \ \text{最多 } N \text{ 個根}$$

* **【已知 6】 [乘積法則與 $x^{p^n}-x$ 的導數 (Product rule and the derivative of x^{p^n} − x)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Finite_Fields/Polynomial_Arithmetic/Formal_Derivative_and_Multiple_Roots.html#c-proof-that-the-polynomial-x-to-the-p-to-the-n-minus-x-has-no-multiple-roots)：** 已於本章 [形式導數與重根](../Polynomial_Arithmetic/Formal_Derivative_and_Multiple_Roots.md)【推導 1】【證明 (c)】完整證明，此處直接引用不再重證

  * (a) 乘積法則：

    $$\left(ab\right)' = a'b + ab'$$

  * (b) 導數為常數：

    $$\left(x^{p^n} - x\right)' = -1$$

* **【已知 7】 [多項式的唯一分解 (Unique factorization of polynomials)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Finite_Fields/Polynomial_Arithmetic/Unique_Factorization_of_Polynomials.html#c-proof-of-the-uniqueness-of-the-factorization)：** 已於本章 [多項式的唯一分解](../Polynomial_Arithmetic/Unique_Factorization_of_Polynomials.md)【證明 (b)(c)(d)】完整證明，此處直接引用不再重證

  * (a) 唯一分解：

    $$f = \prod_{g} g^{e_g} \quad \text{（質多項式，不計順序唯一）}$$

  * (b) $GF(2)[x]$ 中次數 $1, 2, 3, 4$ 的質多項式：

    $$x,\ x+1; \quad x^2+x+1; \quad x^3+x+1,\ x^3+x^2+1; \quad x^4+x+1,\ x^4+x^3+1,\ x^4+x^3+x^2+x+1$$

  * $e_g$ : 重數 (Multiplicities) $[e_g \in \mathbf{N}]$

* **【已知 8】 [GF(p^n) 的存在性與乘法群的循環性 (Existence of GF(p^n) and cyclicity)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Finite_Fields/Multiplicative_Group/Cyclic_Multiplicative_Group_of_Finite_Field.html#b-proof-that-the-multiplicative-group-of-a-finite-field-is-cyclic)：** 已於本章 [$GF(p^n)$ 的存在性](../Structure/Existence_of_GF_p_n.md)【證明 (a)(c)】與 [有限體的乘法群是循環群](Cyclic_Multiplicative_Group_of_Finite_Field.md)【證明 (b)】完整證明，此處直接引用不再重證

  * (a) 存在 $p^n$ 元素的體 $E$，且 $\left[E : GF(p)\right] = n$：

    $$\left|E\right| = p^n, \qquad \left[E : GF(p)\right] = n$$

  * (b) $E^*$ 有生成元：

    $$E^* = \left\langle \omega \right\rangle$$

  * $E$ : $p^n$ 元素的體 (A field with $p^n$ elements) $[\text{體}]$
  * $\omega$ : 本原元 (A primitive element) $[\omega \in E^*]$

* **【已知 9】 [整數除法原理 (Integer division algorithm)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Group/Order_of_Element_and_Cyclic_Subgroup.html#assumptions-preliminaries)：** 已於 [元素的階與循環子群](../../Abstract_Algebra/Group/Order_of_Element_and_Cyclic_Subgroup.md)【已知 6(b)】引用，此處再次引用

  $$n = s\,d + r, \qquad 0 \le r < d$$

* **【假設 1】 一個質多項式 (A prime polynomial)：** 【證明 (a)(b)】的出發點

  $$g \in GF(p)[x] \ \text{首一不可約}, \qquad \deg g = d$$

  * $g$ : 質多項式 (A prime polynomial) $[g \in GF(p)[x]]$

* **【定義 1】 質多項式的個數 (The number of prime polynomials)：** 補充講義 §7.9

  $$N_p(d) \overset{\text{def}}{=} \left|\left\{g \in GF(p)[x] \ \middle|\ g \ \text{首一不可約},\ \deg g = d\right\}\right|$$

  * $N_p(d)$ : 個數 (The count) $[N_p(d) \in \mathbf{N}]$

* **【推導 1】 反覆取 $p^d$ 次方不動 (Iterating the p^d-th power)：** 若 $y^{p^d} = y$，則對 $s$ 歸納

  $$\begin{gather*}
  y^{p^{sd}} &=& \left(y^{p^{(s-1)d}}\right)^{p^d} \\
  y^{p^{sd}} &=& y^{p^d} \qquad \text{(歸納假設 } y^{p^{(s-1)d}} = y\text{)} \\
  y^{p^{sd}} &=& y
  \end{gather*}$$

  * $y$ : 滿足 $y^{p^d} = y$ 的元素 (An element with $y^{p^d} = y$) $[y \in K]$
  * $s$ : 自然數 (A natural number) $[s \in \mathbf{N}]$

* **【推導 2】 $x^{p^n} - x$ 沒有重複的質因式 (x^{p^n} − x is square-free)：** 反設 $g^2 \mid f$，$f = x^{p^n} - x$

  $$\begin{gather*}
  f &=& g^2 h \\
  f' &\overset{\text{已知 6(a)}}{=}& 2g\,g'\,h + g^2 h' = g\left(2g'h + g\,h'\right) \\
  g &\mid& f' \\
  f' &\overset{\text{已知 6(b)}}{=}& -1 \\
  g &\mid& -1 \qquad \text{(與 } \deg g \ge 1 \text{ 矛盾)}
  \end{gather*}$$

  * $h$ : 餘因式 (The cofactor) $[h \in GF(p)[x]]$

+++

## 證明:

### (a) proof that every prime polynomial of degree dividing n divides x to the p to the n minus x

由【假設 1】造 $K = GF(p)[x]/\left\langle g \right\rangle$，$\beta = \left[x\right]$ 是 $g$ 的根；$\left|K\right| = p^d$，故 $\beta^{p^d} = \beta$，再反覆取次方：

$$\begin{gather*}
\left|K\right| &\overset{\text{已知 1,假設 1}}{=}& p^d \\
\beta^{p^d} &\overset{\text{已知 2}}{=}& \beta \\
\beta^{p^n} = \beta^{p^{sd}} &\overset{\text{推導 1}}{=}& \beta \qquad \text{(} n = sd\text{)} \\
g &\overset{\text{已知 3(a),已知 1}}{=}& \beta \ \text{的極小多項式} \\
g &\overset{\text{已知 3(a)}}{\mid}& x^{p^n} - x
\end{gather*}$$

與補充講義 Lemma 7.17（$d = n$ 的情形）一致。

### (b) proof that every prime factor has degree dividing n

設 $g$ 為【假設 1】且 $g \mid x^{p^n} - x$。仍取 $K$、$\beta = \left[x\right]$，則 $\beta^{p^n} = \beta$。
$K$ 的每個元素都是 $\beta$ 的 $GF(p)$-係數多項式 $y = h(\beta)$，故也滿足 $y^{p^n} = y$：

$$\begin{gather*}
\beta^{p^n} - \beta &\overset{\text{已知 1,已知 3(a)}}{=}& 0 \qquad \text{(} g = \beta \text{ 的極小多項式整除 } x^{p^n} - x\text{)} \\
y^{p^n} = h(\beta)^{p^n} &\overset{\text{已知 4}}{=}& h\!\left(\beta^{p^n}\right) = h(\beta) = y
\end{gather*}$$

寫 $n = sd + r$（【已知 9】）。由【已知 2】每個 $y$ 也滿足 $y^{p^d} = y$，於是

$$\begin{gather*}
y &=& y^{p^n} \\
y &=& \left(y^{p^{sd}}\right)^{p^r} \\
y &\overset{\text{推導 1,已知 2}}{=}& y^{p^r} \qquad \text{for all } p^d \text{ 個 } y \in K
\end{gather*}$$

若 $0 < r < d$，則 $p^r$ 次多項式 $x^{p^r} - x$ 有 $p^d > p^r$ 個根，違反【已知 5】。故 $r = 0$：

$$d \ \Big|\ n$$

* 註：補充講義 Theorem 7.21 之後的文字用「根是 $\left\{\beta, \beta^p, \dots\right\}$、循環長度整除 $m$」得到同一結論；本檔的論證不需要共軛元的個數。

### (c) proof of the factorization of x to the p to the n minus x

$f = x^{p^n} - x$ 首一，由【已知 7(a)】唯一分解成質多項式之積；由【推導 2】每個指數都是 $1$；
由【證明 (a)(b)】出現的質多項式恰好是「次數整除 $n$ 的全部」：

$$\begin{gather*}
x^{p^n} - x &\overset{\text{已知 7(a)}}{=}& \prod_{g \mid f} g^{e_g} \\
e_g &\overset{\text{推導 2}}{=}& 1 \\
\left\{g \ \middle|\ g \mid f\right\} &\overset{\text{證明 (a)(b)}}{=}& \left\{g \ \text{質多項式} \ \middle|\ \deg g \mid n\right\} \\
x^{p^n} - x &=& \prod_{d \mid n}\ \prod_{\deg g = d} g
\end{gather*}$$

與投影片 p.43 及補充講義 Theorem 7.22 一致。

### (d) verify the factorizations and count the prime polynomials

**計數公式**：比較【證明 (c)】兩邊的次數：

$$p^n \overset{\text{證明 (c),定義 1}}{=} \sum_{d \mid n} d\,N_p(d)$$

**$n = 3$、$n = 4$**（$p = 2$）：由【已知 7(b)】列出次數整除 $n$ 的質多項式，得投影片 p.18、p.22、p.43 的分解：

$$\begin{gather*}
x^8 - x &\overset{\text{證明 (c),已知 7(b)}}{=}& x\left(x + 1\right)\left(x^3 + x + 1\right)\left(x^3 + x^2 + 1\right) \\
x^{16} - x &\overset{\text{證明 (c),已知 7(b)}}{=}& x\left(x + 1\right)\left(x^2 + x + 1\right)\left(x^4 + x + 1\right)\left(x^4 + x^3 + 1\right)\left(x^4 + x^3 + x^2 + x + 1\right)
\end{gather*}$$

次數核對：$1 + 1 + 3 + 3 = 8$、$1 + 1 + 2 + 4 + 4 + 4 = 16$。

**投影片 p.43 的問題**（$GF(2)$ 上有幾個 $7$ 次質多項式）：$7$ 是質數，因數只有 $1, 7$：

$$\begin{gather*}
2^7 &\overset{\text{證明 (c),定義 1}}{=}& 1 \cdot N_2(1) + 7 \cdot N_2(7) \\
128 &=& 2 + 7\,N_2(7) \\
N_2(7) &=& 18
\end{gather*}$$

與投影片 p.24 的 $n = 7$ 表恰有 $18$ 列一致。同理 $n = 8$（因數 $1, 2, 4, 8$）：

$$\begin{gather*}
2^8 &=& 1 \cdot 2 + 2 \cdot 1 + 4 \cdot 3 + 8\,N_2(8) \\
N_2(8) &=& \left(256 - 16\right)/8 = 30
\end{gather*}$$

與投影片 p.24 的 $n = 8$ 表恰有 $30$ 列一致（也是 [不可約多項式](../../Abstract_Algebra/Field/Irreducible_Polynomial.md) 文末「恰好 $30$ 個」的證明）。

**補充講義 Exercise 17**（$p = 3$、$n = 2$）：$GF(3)$ 上次數 $1$ 的三個與次數 $2$ 的三個質多項式之積：

$$x^9 - x \overset{\text{證明 (c)}}{=} x\left(x + 1\right)\left(x + 2\right)\left(x^2 + 1\right)\left(x^2 + x + 2\right)\left(x^2 + 2x + 2\right)$$

次數核對 $3 \cdot 1 + 3 \cdot 2 = 9$。「with reference to $GF(9)$」：這九個一次因式的根，恰是 $GF(9)$ 的九個元素。

* 註：補充講義 Exercise 18 的數列 $N_2(m) = 2, 1, 2, 3, 6, 9, 18, 30, 56, 99$（$m = 1, \dots, 10$）由計數公式遞迴算出，以 Python 驗算（見文末）。

### (e) proof that prime polynomials of every degree exist

由【已知 8】取 $p^n$ 元素的體 $E$ 與本原元 $\omega$，設其極小多項式 $f$ 的次數為 $m$。**$m \le n$**：

$$m \overset{\text{已知 3(b),已知 8(a)}}{\le} \left[E : GF(p)\right] = n$$

**$m \ge n$**：$GF(p)[\omega]$ 含 $\omega$ 的所有冪次，即含整個 $E^*$ 與 $0$：

$$\begin{gather*}
GF(p)[\omega] &\overset{\text{已知 8(b)}}{\supseteq}& \left\{0\right\} \cup \left\{\omega^k\right\} = E \\
p^m &\overset{\text{已知 3(b)}}{=}& \left|GF(p)[\omega]\right| \ge \left|E\right| = p^n \\
m &\ge& n
\end{gather*}$$

故 $m = n$，而 $f$ 首一不可約（【已知 3(b)】）：

$$f \ \text{是 } n \text{ 次質多項式}$$

與投影片 p.44 的 Theorem 一致（投影片的「$f(x)$ is irreducible by Lemma」即【已知 3(b)】）。

+++

## 意義與密碼學關聯 (Interpretation and Relevance to Cryptography)

### 不可約多項式有多少？

由 (d) 用莫比烏斯反演得到精確公式：

$$N_p(n) = \frac{1}{n}\sum_{d \mid n}\mu(d)\,p^{n/d} \approx \frac{p^n}{n}$$

**隨機挑一個 $n$ 次首一多項式，約有 $1/n$ 的機率不可約**（多項式版的質數定理）。
所以產生 $GF(2^{128})$ 的模數時，隨機試 $\sim 128$ 次（配合快速的 Rabin 或 Ben-Or 不可約檢驗）就能找到一個。

### Rabin 不可約檢驗的原理

(a)(b)(c) 直接給出檢驗法：$n$ 次多項式 $f$ 不可約，當且僅當

$$f \ \Big|\ x^{p^n} - x \quad \text{且} \quad \gcd\!\left(f,\ x^{p^{n/r}} - x\right) = 1 \ \text{對 } n \text{ 的每個質因數 } r$$

第一條保證所有質因式的次數整除 $n$；第二條排除次數是 $n$ 的真因數的質因式。
[不可約多項式](../../Abstract_Algebra/Field/Irreducible_Polynomial.md) 文末提到的 Rabin 測試，本檔給出了完整理由。

### AES 為什麼能「挑」模數

(d) 說八次質多項式有 $30$ 個，而 [$GF(p^n)$ 的唯一性](../Structure/Uniqueness_of_GF_p_n.md) 說它們給出的體全部同構。
AES 設計者因此可以純粹依**實作效率**挑選：$x^8 + x^4 + x^3 + x + 1$ 是 $30$ 個中項數最少的之一（五項），
模約化只需幾個 XOR。

### 程式思維

```python
def mobius(n):
    r, m, q = 1, n, 2
    while q * q <= m:
        if m % q == 0:
            m //= q
            if m % q == 0:
                return 0
            r = -r
        q += 1
    return -r if m > 1 else r

def N(n, p):
    """n 次質多項式個數：證明 (d) 的計數公式經莫比烏斯反演。"""
    return sum(mobius(d) * p ** (n // d) for d in range(1, n + 1) if n % d == 0) // n

assert [N(m, 2) for m in range(1, 11)] == [2, 1, 2, 3, 6, 9, 18, 30, 56, 99]   # 補充講義 Exercise 18
assert N(7, 2) == 18 and N(8, 2) == 30                                          # 投影片 p.43 的問題、p.24 的表
```
