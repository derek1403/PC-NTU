# Least Common Multiple (最小公倍數)

+++

## 證明目標:

`Arithmetic.pdf` p.25。gcd 的對偶：**最小公倍數**。投影片用 [算術基本定理](Fundamental_Theorem_of_Arithmetic.md)
把兩者都寫成質數冪的乘積，指數分別取 $\min$ 與 $\max$，於是乘積關係一目了然。

* (a) 因數的指數刻畫（投影片未列、但 gcd 與 lcm 公式都要用）：

$$d \mid n \quad \Longleftrightarrow \quad d = \prod_{i} p_i^{c_i} \ \text{ with } \ 0 \le c_i \le e_i \qquad \left(n = \prod_i p_i^{e_i},\ d \in \mathbf{P}\right)$$

* (b) gcd 的指數公式：

$$\gcd(a, b) = \prod_{i=1}^{k} p_i^{\min\left(e_i, f_i\right)}$$

* (c) lcm 的指數公式：

$$\mathrm{lcm}(a, b) = \prod_{i=1}^{k} p_i^{\max\left(e_i, f_i\right)}$$

* (d) 投影片的定理：

$$a \times b = \gcd(a, b) \times \mathrm{lcm}(a, b) \qquad \left(a, b \in \mathbf{P}\right)$$

* (e) 驗證：$20 \times 16 = 4 \times 80$、$100 \times 35 = 5 \times 700$。

* $a,\ b$ : 正整數 (Positive integers) $[a, b \in \mathbf{P}]$
* $p_1, \dots, p_k$ : 出現在 $a$ 或 $b$ 裡的所有相異質數 (All distinct primes dividing $a$ or $b$) $[p_i \in \mathbf{P}]$
* $e_i,\ f_i$ : $p_i$ 在 $a$、$b$ 中的指數，可以是 $0$ (The exponents of $p_i$ in $a$ and $b$, possibly zero) $[e_i, f_i \in \mathbf{N}]$
* $n,\ d$ : 正整數 (Positive integers) $[n, d \in \mathbf{P}]$
* $c_i$ : $p_i$ 在 $d$ 中的指數 (The exponent of $p_i$ in $d$) $[c_i \in \mathbf{N}]$
* $\mathrm{lcm}(a, b)$ : 最小公倍數 (The least common multiple) $[\mathrm{lcm}(a,b) \in \mathbf{P}]$
* 註：投影片直接寫出 gcd 與 lcm 的指數公式（「On the other hand, …」），**沒有證明**。
  本檔用 (a) 的因數刻畫把 (b)(c) 補證出來。
* 註：共用同一串質數 $p_1, \dots, p_k$ 是關鍵技巧 —— 允許指數為 $0$，兩個數就能「對齊」逐項比較。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [算術基本定理 (Fundamental theorem of arithmetic)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/Factorization/Fundamental_Theorem_of_Arithmetic.html#d-proof-of-the-inductive-step-of-uniqueness)：** 已於本章 [算術基本定理](Fundamental_Theorem_of_Arithmetic.md)【證明 (a)–(d)】完整證明，此處直接引用不再重證

  * (a) 存在性：每個正整數都是質數冪的乘積（$1$ 是空乘積）

    $$n = \prod_i p_i^{e_i}$$

  * (b) 唯一性：兩個質數冪乘積相等，則每個質數的指數相等

    $$\prod_i p_i^{e_i} = \prod_i p_i^{g_i} \quad \Longrightarrow \quad e_i = g_i \ \text{ for all } i$$

  * $n$ : 正整數 (A positive integer) $[n \in \mathbf{P}]$
  * $p_i$ : 相異質數 (Distinct primes) $[p_i \in \mathbf{P}]$
  * $e_i,\ g_i$ : 指數 (Exponents) $[e_i, g_i \in \mathbf{N}]$

* **【已知 2】 [最大公因數的定義 (Definition of the gcd)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/GCD/Greatest_Common_Divisor.html#assumptions-preliminaries)：** 已於本章 [最大公因數](../GCD/Greatest_Common_Divisor.md)【定義 2】【證明 (a)】給出並證明，此處直接引用

  $$\gcd(a, b) = \max\left\{d \ \middle|\ d \mid a,\ d \mid b\right\} \in \mathbf{P}$$

  * $a,\ b$ : 正整數 (Positive integers) $[a, b \in \mathbf{P}]$
  * $d$ : 公因數 (A common divisor) $[d \in \mathbf{Z}]$
  * 註：最大值必為正，所以只需比較**正**公因數。

* **【定義 1】 最小公倍數 (Least common multiple)：**

  $$\mathrm{lcm}(a, b) \overset{\text{def}}{=} \min\left\{m \in \mathbf{P} \ \middle|\ a \mid m,\ b \mid m\right\}$$

  * $\mathrm{lcm}(a, b)$ : 最小公倍數 (The least common multiple) $[\mathrm{lcm}(a,b) \in \mathbf{P}]$
  * $a,\ b$ : 正整數 (Positive integers) $[a, b \in \mathbf{P}]$
  * $m$ : 候選公倍數 (A candidate common multiple) $[m \in \mathbf{P}]$
  * 註：集合非空（$ab$ 就是一個公倍數），由良序原理最小值存在。

* **【定義 2】 對齊的質因數分解 (Aligned prime factorizations)：** 讓 $a, b$ 共用同一串質數，缺的指數補 $0$

  $$a \overset{\text{def}}{=} \prod_{i=1}^{k} p_i^{e_i}, \qquad b \overset{\text{def}}{=} \prod_{i=1}^{k} p_i^{f_i}, \qquad e_i, f_i \ge 0$$

  * $p_1 < \cdots < p_k$ : $a$ 或 $b$ 的所有相異質因數 (All distinct prime factors of $a$ or $b$) $[p_i \in \mathbf{P}]$
  * $e_i,\ f_i$ : 對應指數 (The corresponding exponents) $[e_i, f_i \in \mathbf{N}]$
  * $k$ : 相異質數的個數 (The number of distinct primes) $[k \in \mathbf{N}]$
  * 註：由【已知 1】這兩個寫法存在且唯一，所以 $e_i, f_i$ 是良定義的。

+++

## 證明:

### (a) proof of the exponent characterization of divisors

($\Leftarrow$) 若每個 $c_i \le e_i$，把 $n$ 拆成 $d$ 乘上剩下的部分：

$$\begin{gather*}
n &\overset{\text{已知 1(a)}}{=}& \prod_i p_i^{e_i} \\
n &=& \prod_i p_i^{c_i} \times \prod_i p_i^{e_i - c_i} \qquad \text{(} e_i - c_i \ge 0 \text{)} \\
n &=& d \times \prod_i p_i^{e_i - c_i} \\
d &\mid& n
\end{gather*}$$

($\Rightarrow$) 若 $n = dt$，把 $d$ 與 $t$ 各自分解；接起來是 $n$ 的一個分解，由唯一性逐項比對指數。
（$d$ 或 $t$ 若含 $p_i$ 以外的質數，那個質數也會出現在 $n$ 的分解裡，與唯一性矛盾，所以它們只用得到 $p_i$。）

$$\begin{gather*}
d &\overset{\text{已知 1(a)}}{=}& \prod_i p_i^{c_i} \\
t &\overset{\text{已知 1(a)}}{=}& \prod_i p_i^{t_i} \\
\prod_i p_i^{e_i} &=& \prod_i p_i^{c_i + t_i} \\
e_i &\overset{\text{已知 1(b)}}{=}& c_i + t_i \\
c_i &\le& e_i \qquad \text{(} t_i \ge 0 \text{)}
\end{gather*}$$

### (b) proof of the exponent formula for the gcd

由 (a)，正整數 $d = \prod p_i^{c_i}$ 同時整除 $a, b$ 若且唯若每個 $c_i$ 同時 $\le e_i$ 與 $\le f_i$：

$$\begin{gather*}
d \mid a,\ d \mid b &\overset{\text{證明 (a)}}{\Longleftrightarrow}& c_i \le e_i,\ \ c_i \le f_i \quad \text{for all } i \\
&\Longleftrightarrow& c_i \le \min\left(e_i, f_i\right) \quad \text{for all } i
\end{gather*}$$

每個指數都取到上限時 $d$ 最大（其他任何合格的 $d$ 都整除它，因而不比它大）：

$$\begin{gather*}
\gcd(a, b) &\overset{\text{已知 2}}{=}& \max\left\{\prod_i p_i^{c_i} \ \middle|\ c_i \le \min\left(e_i, f_i\right)\right\} \\
&=& \prod_i p_i^{\min\left(e_i, f_i\right)}
\end{gather*}$$

### (c) proof of the exponent formula for the lcm

設 $m$ 是公倍數。由 (a)（把 $a$ 當因數、$m$ 當被整除者），$m$ 中 $p_i$ 的指數 $g_i$ 必須 $\ge e_i$ 且 $\ge f_i$：

$$\begin{gather*}
a \mid m,\ b \mid m &\overset{\text{證明 (a)}}{\Longrightarrow}& g_i \ge e_i,\ \ g_i \ge f_i \quad \text{for all } i \\
&\Longrightarrow& g_i \ge \max\left(e_i, f_i\right) \quad \text{for all } i \\
&\Longrightarrow& m \ge \prod_i p_i^{\max\left(e_i, f_i\right)}
\end{gather*}$$

而 $L = \prod p_i^{\max(e_i, f_i)}$ 本身就是公倍數（再由 (a) 的 ($\Leftarrow$)），故它是最小的：

$$\begin{gather*}
e_i \le \max\left(e_i, f_i\right),\ \ f_i \le \max\left(e_i, f_i\right) &\overset{\text{證明 (a)}}{\Longrightarrow}& a \mid L,\ \ b \mid L \\
\mathrm{lcm}(a, b) &\overset{\text{定義 1}}{=}& \prod_i p_i^{\max\left(e_i, f_i\right)}
\end{gather*}$$

### (d) proof of the product formula

兩個非負整數的 $\max$ 與 $\min$ 相加，就是兩數相加（一個取大、一個取小，恰好各取一次）：

$$\begin{gather*}
\gcd(a, b) \times \mathrm{lcm}(a, b) &\overset{\text{證明 (b),證明 (c)}}{=}& \prod_i p_i^{\min\left(e_i, f_i\right) + \max\left(e_i, f_i\right)} \\
&=& \prod_i p_i^{e_i + f_i} \\
&=& \prod_i p_i^{e_i} \times \prod_i p_i^{f_i} \\
&\overset{\text{定義 2}}{=}& a \times b
\end{gather*}$$

與投影片「The conclusion follows from $e_i + f_i = g_i + h_i$」一致。

### (e) verify the two numerical examples

**$a = 20 = 2^2 \times 5$、$b = 16 = 2^4$**，對齊成 $p = \left(2, 5\right)$：$e = \left(2, 1\right)$、$f = \left(4, 0\right)$：

$$\begin{gather*}
\gcd(20, 16) &\overset{\text{證明 (b)}}{=}& 2^{\min(2,4)} \times 5^{\min(1,0)} \\
&=& 2^2 \times 5^0 \\
&=& 4
\end{gather*}$$

$$\begin{gather*}
\mathrm{lcm}(20, 16) &\overset{\text{證明 (c)}}{=}& 2^{\max(2,4)} \times 5^{\max(1,0)} \\
&=& 2^4 \times 5 \\
&=& 80
\end{gather*}$$

$$\begin{gather*}
20 \times 16 &\overset{\text{證明 (d)}}{=}& 4 \times 80 \\
&=& 320
\end{gather*}$$

**$a = 100 = 2^2 \times 5^2$、$b = 35 = 5 \times 7$**，對齊成 $p = \left(2, 5, 7\right)$：$e = \left(2, 2, 0\right)$、$f = \left(0, 1, 1\right)$：

$$\begin{gather*}
\gcd(100, 35) &\overset{\text{證明 (b)}}{=}& 2^0 \times 5^1 \times 7^0 \\
&=& 5
\end{gather*}$$

$$\begin{gather*}
\mathrm{lcm}(100, 35) &\overset{\text{證明 (c)}}{=}& 2^2 \times 5^2 \times 7^1 \\
&=& 700
\end{gather*}$$

$$\begin{gather*}
100 \times 35 &\overset{\text{證明 (d)}}{=}& 5 \times 700 \\
&=& 3500
\end{gather*}$$

兩邊一致；$\gcd(100, 35) = 5$ 也與 [擴展歐幾里得演算法](../GCD/Extended_Euclidean_Algorithm.md)【證明 (d)】一致。

+++

## 意義與密碼學關聯 (Interpretation and Relevance to Cryptography)

### 用 gcd 算 lcm，不必分解

指數公式很漂亮，但要先**分解** $a, b$ —— 對大數做不到。(d) 提供了捷徑：

$$\mathrm{lcm}(a, b) = \frac{ab}{\gcd(a, b)}$$

而 gcd 用 [歐幾里得演算法](../GCD/Euclidean_Algorithm.md) 對數時間就算完。**本檔的證明需要分解，本檔的結論卻讓你不必分解。**

### RSA 的 Carmichael 函數

現代 RSA 標準（PKCS #1、FIPS 186）用的不是 $\varphi(n) = (p-1)(q-1)$，而是

$$\lambda(n) = \mathrm{lcm}(p - 1,\ q - 1)$$

來計算私鑰 $d = e^{-1} \bmod \lambda(n)$。$\lambda(n)$ 通常比 $\varphi(n)$ 小好幾倍
（$p - 1$ 與 $q - 1$ 至少共用因數 $2$，故 $\lambda(n) \le \varphi(n)/2$），私鑰因此更短，而解密依然正確。
計算方式正是 (d)：$\lambda(n) = (p-1)(q-1) / \gcd(p-1, q-1)$。

### 與理想的對應

Abstract_Algebra 章 [理想](../../Abstract_Algebra/Ring/Ideal.md) 說：

$$m\mathbf{Z} \cap n\mathbf{Z} = \mathrm{lcm}(m, n)\,\mathbf{Z}, \qquad m\mathbf{Z} + n\mathbf{Z} = \gcd(m, n)\,\mathbf{Z}$$

**交集對應 lcm（取 $\max$）、和對應 gcd（取 $\min$）**。
[中國剩餘定理](../CRT/Chinese_Remainder_Theorem.md) 的「互質時 $\mathbf{Z}_{m_1 m_2} \cong \mathbf{Z}_{m_1} \times \mathbf{Z}_{m_2}$」，
背後就是互質時 $\mathrm{lcm}(m_1, m_2) = m_1 m_2$ —— 由 (d) 取 $\gcd = 1$ 即得。

### 程式思維

```python
from math import gcd, lcm
for a in range(1, 200):
    for b in range(1, 200):
        assert a * b == gcd(a, b) * lcm(a, b)          # 證明 (d)
assert (gcd(20, 16), lcm(20, 16)) == (4, 80)
assert (gcd(100, 35), lcm(100, 35)) == (5, 700)
```
