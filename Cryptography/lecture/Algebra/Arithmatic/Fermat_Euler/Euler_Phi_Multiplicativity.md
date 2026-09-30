# Euler Phi Multiplicativity (尤拉函數的乘法性)

+++

## 證明目標:

`Arithmetic.pdf` p.51–52。尤拉函數最有用的性質：**互質時可以拆開算**。
配合 [質數冪的公式](Euler_Phi_Function.md)，任何 $n$ 的 $\varphi(n)$ 都能從質因數分解直接讀出。

* (a) 投影片的 Note (i)：

$$a \perp mn \quad \Longleftrightarrow \quad a \perp m \ \text{ and } \ a \perp n$$

* (b) 投影片的 Note (ii)：$\left[1, mn\right]$ 裡的每個 $a$ 都唯一寫成

$$a = i \times n + j, \qquad 0 \le i < m,\ \ 1 \le j \le n$$

* (c) 投影片的 ① ②：$a = in + j$ 與 $n$ 互質，若且唯若 $j$ 與 $n$ 互質。
* (d) 投影片的 ③：$j \perp n$ 時，那一行 $C_j = \left\{j,\ n + j,\ \dots,\ (m-1)n + j\right\}$ 是模 $m$ 的完全剩餘系，其中恰有 $\varphi(m)$ 個與 $m$ 互質。
* (e) **乘法性**：

$$\varphi(mn) = \varphi(m)\,\varphi(n) \qquad \left(m \perp n\right)$$

* (f) **乘積公式**：

$$n = \prod_{i=1}^{r} p_i^{e_i} \quad \Longrightarrow \quad \varphi(n) = \prod_{i=1}^{r} p_i^{e_i - 1}\left(p_i - 1\right)$$

* (g) 驗證投影片 p.52 的兩個例子：$\varphi(360) = 96$、$\left|\mathbf{Z}_{208}^*\right| = \varphi(208) = 96$。

* $m,\ n$ : 互質的正整數 (Coprime positive integers) $[m, n \in \mathbf{P}]$
* $a$ : $\left[1, mn\right]$ 中的整數 (An integer in $\left[1, mn\right]$) $[a \in \mathbf{P}]$
* $i,\ j$ : 行列座標 (Row and column coordinates) $[i \in \left\{0, \dots, m-1\right\},\ j \in \left\{1, \dots, n\right\}]$
* $C_j$ : 第 $j$ 行 (The $j$-th column) $[C_j \subseteq \mathbf{P}]$
* $p_i,\ e_i$ : 相異質數與指數 (Distinct primes and exponents) $[p_i \in \mathbf{P},\ e_i \in \mathbf{P}]$
* 註：想像把 $1, 2, \dots, mn$ 排成 $m$ 列 $n$ 行的方陣（第 $i$ 列是 $in + 1, \dots, in + n$）。
  (c) 說「與 $n$ 互質」只看**行**；(d) 說每個好行裡「與 $m$ 互質」的恰有 $\varphi(m)$ 個。於是總數 $= \varphi(n) \times \varphi(m)$。
* 註：乘法性的**結構性**解釋是 $\mathbf{Z}_{mn}^* \cong \mathbf{Z}_m^* \times \mathbf{Z}_n^*$（CRT 限制在可逆元上），
  見 Abstract_Algebra 章 [群的階](../../Abstract_Algebra/Group/Group_Order.md)【證明 (c)】的註。本檔走投影片的**計數**路線。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [互質對乘法封閉 (Coprimality is closed under products)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/Factorization/Relatively_Prime.html#b-proof-that-coprimality-to-a-modulus-is-closed-under-products)：** 已於本章 [互質](../Factorization/Relatively_Prime.md)【證明 (b)】完整證明，此處直接引用不再重證

  $$u \perp w,\ \ v \perp w \quad \Longrightarrow \quad uv \perp w$$

  * $u,\ v,\ w$ : 整數 (Integers) $[u, v, w \in \mathbf{Z}]$

* **【已知 2】 [gcd 的基本性質 (Basic properties of the gcd)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/GCD/GCD_Shift_Invariance.html#c-proof-of-the-shift-invariance-theorem)：** 已於本章 [GCD 的平移不變性](../GCD/GCD_Shift_Invariance.md)【證明 (c)】、[最大公因數](../GCD/Greatest_Common_Divisor.md)【定義 2】與 [整除的基本性質](../GCD/Divisibility_Basics.md)【證明 (b)】給出並證明，此處直接引用不再重證

  * (a) 平移不變：

    $$\gcd(u + kv,\ v) = \gcd(u, v)$$

  * (b) 公因數不超過 gcd；整除可遞移：

    $$d \mid u,\ d \mid v \ \Longrightarrow \ d \le \gcd(u, v); \qquad d \mid v,\ v \mid w \ \Longrightarrow \ d \mid w$$

  * $u,\ v,\ w$ : 整數 (Integers) $[u, v, w \in \mathbf{Z}]$
  * $k$ : 任意整數 (An arbitrary integer) $[k \in \mathbf{Z}]$
  * $d$ : 公因數 (A common divisor) $[d \in \mathbf{P}]$

* **【已知 3】 [除法原理 (Division algorithm)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/Division/Modular_Function.html#b-proof-of-the-division-algorithm-with-uniqueness)：** 已於本章 [取模函數](../Division/Modular_Function.md)【證明 (a)(b)】完整證明，此處直接引用不再重證

  $$u = q n + s,\ \ 0 \le s < n \qquad \text{（} q, s \text{ 存在且唯一）}$$

  * $u$ : 被除數 (The dividend) $[u \in \mathbf{Z}]$
  * $n$ : 除數 (The divisor) $[n \in \mathbf{P}]$
  * $q,\ s$ : 商與餘數 (The quotient and remainder) $[q, s \in \mathbf{Z}]$

* **【已知 4】 [完全剩餘系 (Complete residue systems)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/Fermat_Euler/Complete_Residue_System.html#c-proof-that-m-pairwise-incongruent-integers-form-a-complete-residue-system)：** 已於本章 [完全剩餘系](Complete_Residue_System.md)【證明 (a)(c)】完整證明，此處直接引用不再重證

  * (a) 判別法：

    $$\left|C\right| = m,\ \ C \ \text{中兩兩不同餘} \quad \Longrightarrow \quad C \ \text{為模 } m \text{ 的完全剩餘系}$$

  * (b) 完全剩餘系上的「取餘數」是到 $\left\{0, \dots, m-1\right\}$ 的雙射：

    $$\rho : C \to \left\{0, \dots, m-1\right\},\ \ \rho(c) = c \bmod m \ \ \text{為雙射}$$

  * $C$ : 整數集合 (A set of integers) $[C \subseteq \mathbf{Z}]$
  * $m$ : 模數 (The modulus) $[m \in \mathbf{P}]$

* **【已知 5】 [互質消去律 (Cancellation of a coprime factor)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/Congruence/Congruence_Properties.html#g-proof-of-cancellation-for-a-coprime-factor)：** 已於本章 [同餘的性質](../Congruence/Congruence_Properties.md)【證明 (b)(g)】完整證明，此處直接引用不再重證

  * (a) 兩邊同加：

    $$u \equiv v \quad \Longrightarrow \quad u - j \equiv v - j \pmod{m}$$

  * (b) 互質消去：

    $$n \perp m,\ \ un \equiv vn \pmod{m} \quad \Longrightarrow \quad u \equiv v \pmod{m}$$

  * $u,\ v,\ j$ : 整數 (Integers) $[u, v, j \in \mathbf{Z}]$
  * $m,\ n$ : 互質的正整數 (Coprime positive integers) $[m, n \in \mathbf{P}]$

* **【已知 6】 [尤拉函數的已知值 (Known values of the totient)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/Fermat_Euler/Euler_Phi_Function.html#d-proof-of-the-formula-for-a-prime-power)：** 已於本章 [尤拉函數](Euler_Phi_Function.md)【已知 1】【證明 (a)(d)】與 Abstract_Algebra 章 [群的階](../../Abstract_Algebra/Group/Group_Order.md)【定義 3】給出並證明，此處直接引用不再重證

  * (a) 定義：

    $$\varphi(n) = \left|\left\{a \ \middle|\ 1 \le a \le n,\ a \perp n\right\}\right|$$

  * (b) 等於 $\left\{0, \dots, m-1\right\}$ 中與 $m$ 互質者的個數：

    $$\varphi(m) = \left|\mathbf{Z}_m^*\right| = \left|\left\{r \ \middle|\ 0 \le r < m,\ r \perp m\right\}\right|$$

  * (c) 質數冪：

    $$\varphi\left(p^{e}\right) = p^{e-1}\left(p - 1\right)$$

  * $n,\ m$ : 正整數 (Positive integers) $[n, m \in \mathbf{P}]$
  * $a,\ r$ : 被計數的整數 (The integers being counted) $[a, r \in \mathbf{Z}]$
  * $p$ : 質數 (A prime) $[p \in \mathbf{P}]$
  * $e$ : 指數 (An exponent) $[e \in \mathbf{P}]$

* **【已知 7】 [相異質數互質 (Distinct primes are coprime)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/Factorization/Euclid_Lemma.html#a-proof-that-a-prime-is-coprime-to-every-integer-it-does-not-divide)：** 已於本章 [歐幾里得引理](../Factorization/Euclid_Lemma.md)【證明 (a)】完整證明（$p \nmid q$），此處直接引用不再重證

  $$p \neq q \ \text{為質數} \quad \Longrightarrow \quad p \perp q$$

  * $p,\ q$ : 相異質數 (Distinct primes) $[p, q \in \mathbf{P}]$

+++

## 證明:

### (a) proof that coprimality to a product splits into the two factors

($\Leftarrow$) 直接由【已知 1】（$m \perp a$、$n \perp a$ 推出 $mn \perp a$）：

$$\begin{gather*}
a \perp m,\ \ a \perp n &\overset{\text{已知 1}}{\Longrightarrow}& a \perp mn
\end{gather*}$$

($\Rightarrow$) $a$ 與 $m$ 的任一正公因數 $d$ 也整除 $mn$，所以也是 $a$ 與 $mn$ 的公因數，不超過 $\gcd(a, mn) = 1$：

$$\begin{gather*}
d \mid a,\ \ d \mid m &\overset{\text{已知 2(b)}}{\Longrightarrow}& d \mid mn \\
d &\overset{\text{已知 2(b)}}{\le}& \gcd(a, mn) \\
d &\le& 1 \\
\gcd(a, m) &=& 1
\end{gather*}$$

$n$ 的情形完全相同。

### (b) proof that every integer up to mn has unique row and column coordinates

對 $a - 1$ 做除以 $n$ 的除法，把餘數往上移一格：

$$\begin{gather*}
a - 1 &\overset{\text{已知 3}}{=}& i n + s \qquad \text{with } 0 \le s < n \\
a &=& i n + j \qquad \text{with } j = s + 1,\ \ 1 \le j \le n \\
0 &\le& i \qquad \text{(} a - 1 \ge 0 \text{)} \\
i &<& m \qquad \text{(} a - 1 < mn \text{)}
\end{gather*}$$

$\left(i, s\right)$ 由除法原理唯一決定，故 $\left(i, j\right)$ 也唯一。反之每一對 $\left(i, j\right)$ 給出 $\left[1, mn\right]$ 裡的一個 $a$，對應是雙射。

### (c) proof that coprimality to n depends only on the column

$$\begin{gather*}
\gcd(a, n) &=& \gcd(j + in,\ n) \\
&\overset{\text{已知 2(a)}}{=}& \gcd(j, n)
\end{gather*}$$

所以 $a \perp n \Longleftrightarrow j \perp n$：與 $n$ 不互質的行整行淘汰（投影片 ①），
與 $n$ 互質的行整行保留，共 $\varphi(n)$ 行（投影片 ②，【已知 6(a)】）。

### (d) proof that each good column is a complete residue system with phi of m coprime entries

固定 $j \perp n$。$C_j$ 有 $m$ 個元素；若其中兩個模 $m$ 同餘，減掉 $j$ 再消去與 $m$ 互質的 $n$，得 $i_1 \equiv i_2 \pmod m$，而 $0 \le i_1, i_2 < m$ 只能相等：

$$\begin{gather*}
i_1 n + j &\equiv& i_2 n + j \pmod{m} \\
i_1 n &\overset{\text{已知 5(a)}}{\equiv}& i_2 n \pmod{m} \\
i_1 &\overset{\text{已知 5(b)}}{\equiv}& i_2 \pmod{m} \qquad \text{(} m \perp n \text{)} \\
i_1 &=& i_2 \qquad \text{(} \left|i_1 - i_2\right| < m \text{)} \\
\left|C_j\right| = m,\ \text{兩兩不同餘} &\overset{\text{已知 4(a)}}{\Longrightarrow}& C_j \ \text{為模 } m \text{ 的完全剩餘系}
\end{gather*}$$

再數 $C_j$ 裡與 $m$ 互質的元素。$\gcd(c, m) = \gcd(c \bmod m,\ m)$（平移不變），而 $c \mapsto c \bmod m$ 是雙射，
所以個數等於 $\left\{0, \dots, m-1\right\}$ 裡與 $m$ 互質的個數：

$$\begin{gather*}
\gcd(c, m) &\overset{\text{已知 2(a)}}{=}& \gcd\left(c \bmod m,\ m\right) \\
\left|\left\{c \in C_j \ \middle|\ c \perp m\right\}\right| &\overset{\text{已知 4(b)}}{=}& \left|\left\{r \ \middle|\ 0 \le r < m,\ r \perp m\right\}\right| \\
\left|\left\{c \in C_j \ \middle|\ c \perp m\right\}\right| &\overset{\text{已知 6(b)}}{=}& \varphi(m)
\end{gather*}$$

與投影片 ③ 一致。

### (e) proof of multiplicativity

把 $\left[1, mn\right]$ 按行 $j$ 分組計數，依序套用 (a)(b)(c)(d)：

$$\begin{gather*}
\varphi(mn) &\overset{\text{已知 6(a)}}{=}& \left|\left\{a \in \left[1, mn\right] \ \middle|\ a \perp mn\right\}\right| \\
&\overset{\text{證明 (a)}}{=}& \left|\left\{a \in \left[1, mn\right] \ \middle|\ a \perp m,\ a \perp n\right\}\right| \\
&\overset{\text{證明 (b)(c)}}{=}& \sum_{1 \le j \le n,\ j \perp n} \left|\left\{c \in C_j \ \middle|\ c \perp m\right\}\right| \\
&\overset{\text{證明 (d)}}{=}& \sum_{1 \le j \le n,\ j \perp n} \varphi(m) \\
&\overset{\text{已知 6(a)}}{=}& \varphi(n)\,\varphi(m)
\end{gather*}$$

與投影片一致。

### (f) proof of the product formula

相異質數的冪兩兩互質（【已知 7】加上【已知 1】反覆套用），於是 (e) 可以一個質因數一個質因數地拆開；每個質數冪再用公式：

$$\begin{gather*}
p_i &\overset{\text{已知 7}}{\perp}& p_j \qquad \left(i \neq j\right) \\
p_1^{e_1} \cdots p_{r-1}^{e_{r-1}} &\overset{\text{已知 1}}{\perp}& p_r^{e_r} \\
\varphi(n) &\overset{\text{證明 (e)}}{=}& \varphi\left(p_1^{e_1} \cdots p_{r-1}^{e_{r-1}}\right) \varphi\left(p_r^{e_r}\right) \\
\varphi(n) &=& \prod_{i=1}^{r} \varphi\left(p_i^{e_i}\right) \qquad \text{(對 } r \text{ 歸納)} \\
\varphi(n) &\overset{\text{已知 6(c)}}{=}& \prod_{i=1}^{r} p_i^{e_i - 1}\left(p_i - 1\right)
\end{gather*}$$

與投影片 p.52 的命題一致。

### (g) verify the two examples from the slides

**$360 = 2^3 \times 3^2 \times 5$**：

$$\begin{gather*}
\varphi(360) &\overset{\text{證明 (f)}}{=}& 2^{2}\left(2 - 1\right) \times 3^{1}\left(3 - 1\right) \times 5^{0}\left(5 - 1\right) \\
&=& 4 \times 6 \times 4 \\
&=& 96
\end{gather*}$$

**$208 = 2^4 \times 13$**：

$$\begin{gather*}
\varphi(208) &\overset{\text{證明 (f)}}{=}& 2^{3}\left(2 - 1\right) \times 13^{0}\left(13 - 1\right) \\
&=& 8 \times 12 \\
&=& 96
\end{gather*}$$

兩者都與投影片一致（$\left|\mathbf{Z}_{208}^*\right| = \varphi(208)$ 由 [尤拉函數](Euler_Phi_Function.md)【證明 (a)】）。
兩個不同的模數有相同的 $\varphi$ 值，並不稀奇。

+++

## 意義與密碼學關聯 (Interpretation and Relevance to Cryptography)

### RSA 的 $\varphi(n) = (p-1)(q-1)$

$n = pq$（$p \neq q$ 質數）時，$p \perp q$，由 (e) 與 $\varphi(p) = p - 1$：

$$\varphi(pq) = \varphi(p)\varphi(q) = \left(p - 1\right)\left(q - 1\right)$$

這就是 RSA 金鑰產生時算私鑰要用的數。**只有知道 $p, q$ 的人才能用 (f) 算出 $\varphi(n)$** ——
不知道分解，就只能照定義一個一個數，對 $2048$ 位元的 $n$ 完全不可行。
**乘積公式需要分解，這個不對稱就是 RSA 的陷門。**

### 為什麼互質條件不可省

$\varphi(4) = 2$，但 $\varphi(2)\varphi(2) = 1$。$2 \not\perp 2$，(d) 的「消去 $n$」那一步壞掉 ——
方陣的一行裡會有重複的模 $m$ 餘數。所以乘積公式一定要先把 $n$ 拆成**相異**質數的冪。

### 程式思維

```python
from math import gcd
def phi(n):
    return sum(1 for a in range(1, n + 1) if gcd(a, n) == 1)

for m in range(1, 40):
    for n in range(1, 40):
        if gcd(m, n) == 1:
            assert phi(m * n) == phi(m) * phi(n)                  # 證明 (e)
assert phi(360) == 2**2 * 1 * 3 * 2 * 4 == 96                      # 證明 (g)
assert phi(208) == 2**3 * 1 * 12 == 96
assert phi(4) != phi(2) * phi(2)                                   # 互質條件不可省
```
