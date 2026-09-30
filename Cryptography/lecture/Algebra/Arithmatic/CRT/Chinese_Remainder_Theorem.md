# Chinese Remainder Theorem (中國剩餘定理)

+++

## 證明目標:

`Arithmetic.pdf` p.34、p.40–41。把 [兩個模數的版本](Two_Moduli_CRT.md) 推廣到 $r$ 個兩兩互質的模數，
並用投影片的「Proof 2」—— **高斯公式** —— 一次寫出解。最後回到一千五百年前的《孫子算經》。

**中國剩餘定理**：若 $m_1, \dots, m_r$ 兩兩互質，則方程組 $x \equiv a_i \pmod{m_i}$（$1 \le i \le r$）
在模 $M = m_1 m_2 \cdots m_r$ 下有唯一解。

* (a) **存在性**（投影片的 Proof 2）：

$$x = \sum_{i=1}^{r} a_i\, M_i\, y_i, \qquad M_i = \frac{M}{m_i}, \qquad y_i \equiv M_i^{-1} \pmod{m_i}$$

  是一個解。

* (b) **唯一性**：任兩解模 $M$ 同餘。
* (c) 與一個解模 $M$ 同餘的數也都是解（解集恰為一個同餘類）。
* (d) 驗證《孫子算經》的例子：

$$x \equiv 2 \pmod 3,\ \ x \equiv 3 \pmod 5,\ \ x \equiv 2 \pmod 7 \quad \Longrightarrow \quad x \equiv 23 \pmod{105}$$

* $r$ : 方程式個數 (The number of congruences) $[r \in \mathbf{P}]$
* $m_i$ : 兩兩互質的模數 (Pairwise coprime moduli) $[m_i \in \mathbf{P}]$
* $a_i$ : 給定的餘數 (The prescribed residues) $[a_i \in \mathbf{Z}]$
* $M$ : 所有模數的乘積 (The product of all moduli) $[M \in \mathbf{P}]$
* $M_i$ : 去掉 $m_i$ 的乘積 (The product omitting $m_i$) $[M_i \in \mathbf{P}]$
* $y_i$ : $M_i$ 模 $m_i$ 的反元素 (The inverse of $M_i$ modulo $m_i$) $[y_i \in \mathbf{Z}]$
* 註：投影片的「Proof 1: Induction on $r$」就是 [中國剩餘演算法](Chinese_Remainder_Algorithm.md) 的遞迴，在那一檔證明。
* 註：投影片 p.40 的「Note」—— $M_i \equiv 0 \pmod{m_j}$（$j \neq i$）且 $M_i y_i \equiv 1 \pmod{m_i}$ —— 正是 (a) 的兩個關鍵，本檔寫成【推導 2】。
* 註：結構上的版本 $\mathbf{Z}_M \cong \mathbf{Z}_{m_1} \times \cdots \times \mathbf{Z}_{m_r}$ 已在 Abstract_Algebra 章
  [中國剩餘定理](../../Abstract_Algebra/Ring/Chinese_Remainder_Theorem.md) 以理想的語言證完。本檔證的是**初等、可計算**的版本：
  不只說解存在，還給出公式。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [互質的兩條引理 (Two lemmas on coprimality)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/Factorization/Relatively_Prime.html#b-proof-that-coprimality-to-a-modulus-is-closed-under-products)：** 已於本章 [互質](../Factorization/Relatively_Prime.md)【證明 (b)(c)】完整證明，此處直接引用不再重證

  * (a) 互質對乘法封閉（可反覆套用到多個因子）：

    $$b_1 \perp m,\ \dots,\ b_k \perp m \quad \Longrightarrow \quad b_1 b_2 \cdots b_k \perp m$$

  * (b) 互質因數相乘仍整除：

    $$n_1 \mid y,\ \ n_2 \mid y,\ \ n_1 \perp n_2 \quad \Longrightarrow \quad n_1 n_2 \mid y$$

  * $b_i,\ m,\ n_1,\ n_2$ : 正整數 (Positive integers) $[\mathbf{P}]$
  * $y$ : 被整除的整數 (The integer being divided) $[y \in \mathbf{Z}]$

* **【已知 2】 [模反元素的存在性 (Existence of the modular inverse)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/Congruence/Modular_Inverse.html#b-proof-that-coprimality-gives-an-inverse)：** 已於本章 [模反元素](../Congruence/Modular_Inverse.md)【證明 (b)】完整證明，此處直接引用不再重證

  $$n \perp m \quad \Longrightarrow \quad \exists\, y \in \mathbf{P} \ \text{ such that } \ n y \equiv 1 \pmod{m}$$

  * $n,\ m$ : 互質的正整數 (Coprime positive integers) $[n, m \in \mathbf{P}]$
  * $y$ : 反元素 (The inverse) $[y \in \mathbf{P}]$

* **【已知 3】 [同餘的整除刻畫 (Congruence as divisibility)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/Congruence/Congruence_Relation.html#b-proof-that-a-difference-divisible-by-the-modulus-gives-equal-remainders)：** 已於本章 [同餘關係](../Congruence/Congruence_Relation.md)【證明 (a)(b)】完整證明，此處直接引用不再重證

  $$u \equiv v \pmod{m} \quad \Longleftrightarrow \quad m \mid \left(u - v\right)$$

  * $u,\ v$ : 任意整數 (Arbitrary integers) $[u, v \in \mathbf{Z}]$
  * $m$ : 模數 (The modulus) $[m \in \mathbf{P}]$

* **【已知 4】 [整除的線性組合性質 (Divisibility of linear combinations)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/GCD/Divisibility_Basics.html#a-proof-that-a-common-divisor-divides-every-linear-combination)：** 已於本章 [整除的基本性質](../GCD/Divisibility_Basics.md)【證明 (a)】完整證明（反覆套用即推廣到任意多項），此處直接引用不再重證

  $$d \mid u_1,\ \dots,\ d \mid u_k \quad \Longrightarrow \quad d \mid \left(c_1 u_1 + \cdots + c_k u_k\right)$$

  * $d$ : 公因數 (A common divisor) $[d \in \mathbf{Z}]$
  * $u_j,\ c_j$ : 任意整數 (Arbitrary integers) $[u_j, c_j \in \mathbf{Z}]$

* **【定義 1】 高斯公式的各個量 (The ingredients of Gauss's formula)：**

  $$\begin{gather*}
  M &\overset{\text{def}}{=}& m_1 m_2 \cdots m_r \\
  M_i &\overset{\text{def}}{=}& \frac{M}{m_i} = \prod_{j \neq i} m_j \\
  y_i &\overset{\text{def}}{=}& M_i^{-1} \bmod m_i \\
  x &\overset{\text{def}}{=}& \sum_{i=1}^{r} a_i M_i y_i
  \end{gather*}$$

  * $M,\ M_i,\ y_i,\ x$ : 見證明目標的符號清單 (See the symbol list above) $[\mathbf{Z}]$
  * $m_i$ : 兩兩互質的模數 (Pairwise coprime moduli) $[m_i \in \mathbf{P}]$
  * $a_i$ : 給定的餘數 (The prescribed residues) $[a_i \in \mathbf{Z}]$
  * $i,\ j$ : 指標 (Indices) $[i, j \in \left\{1, \dots, r\right\}]$
  * 註：$y_i$ 的存在性要證，見【推導 1】。

* **【假設 1】 兩兩互質 (Pairwise coprime moduli)：** 定理的前提

  $$m_i \perp m_j \qquad \text{for all } i \neq j$$

  * $m_i,\ m_j$ : 模數 (Moduli) $[m_i, m_j \in \mathbf{P}]$
  * 註：**是「兩兩」互質，不是「全體 gcd 為 $1$」**。$\left\{6, 10, 15\right\}$ 的全體 gcd 是 $1$，但兩兩都不互質，定理不適用。

* **【推導 1】 $M_i$ 與 $m_i$ 互質，故 $y_i$ 存在 ($M_i$ is coprime to $m_i$)：** $M_i$ 的每個因子 $m_j$（$j \neq i$）都與 $m_i$ 互質

  $$\begin{gather*}
  m_j &\overset{\text{假設 1}}{\perp}& m_i \qquad \text{for all } j \neq i \\
  M_i = \prod_{j \neq i} m_j &\overset{\text{已知 1(a)}}{\perp}& m_i \\
  M_i \perp m_i &\overset{\text{已知 2}}{\Longrightarrow}& \exists\, y_i \ \text{ such that } \ M_i y_i \equiv 1 \pmod{m_i}
  \end{gather*}$$

  * $M_i$ : 去掉 $m_i$ 的乘積 (The product omitting $m_i$) $[M_i \in \mathbf{P}]$
  * $m_i,\ m_j$ : 模數 (Moduli) $[m_i, m_j \in \mathbf{P}]$
  * $y_i$ : 反元素 (The inverse) $[y_i \in \mathbf{P}]$

* **【推導 2】 投影片 p.40 的 Note (The note on slide 40)：** 【證明 (a)】要用

  * (a) $j \neq i$ 時 $M_j$ 含有因子 $m_i$：

    $$m_i \mid M_j \qquad \left(j \neq i\right)$$

  * (b) $M_i y_i$ 模 $m_i$ 等於 $1$：

    $$\begin{gather*}
    M_i y_i &\overset{\text{推導 1}}{\equiv}& 1 \pmod{m_i} \\
    m_i &\overset{\text{已知 3}}{\mid}& M_i y_i - 1
    \end{gather*}$$

  * $m_i$ : 模數 (A modulus) $[m_i \in \mathbf{P}]$
  * $M_i,\ M_j$ : 去掉某個模數的乘積 (Products omitting one modulus) $[\mathbf{P}]$
  * 註：於是 $M_i y_i$ 是「**模 $m_i$ 為 $1$、模其他 $m_j$ 為 $0$**」的數 —— 第 $i$ 個座標的「單位向量」。
    $x = \sum a_i \left(M_i y_i\right)$ 就是把單位向量乘上想要的座標再加起來。

* **【推導 3】 兩兩互質的因數全體相乘仍整除 (Pairwise coprime divisors multiply)：** 【證明 (b)】要用。
  設每個 $m_i \mid y$，對 $k$ 歸納證明 $P_k = m_1 \cdots m_k \mid y$：$k = 1$ 即前提；若 $P_k \mid y$，則

  $$\begin{gather*}
  P_k &\overset{\text{假設 1,已知 1(a)}}{\perp}& m_{k+1} \\
  P_k\, m_{k+1} &\overset{\text{已知 1(b)}}{\mid}& y \qquad \text{(即 } P_{k+1} \mid y \text{)}
  \end{gather*}$$

  歸納到 $k = r$ 即 $M \mid y$。

  * $P_k$ : 前 $k$ 個模數的乘積 (The product of the first $k$ moduli) $[P_k \in \mathbf{P}]$
  * $y$ : 被整除的整數 (The integer being divided) $[y \in \mathbf{Z}]$
  * $k$ : 歸納變數 (Induction variable) $[k \in \left\{1, \dots, r\right\}]$

+++

## 證明:

### (a) proof that Gauss's formula gives a solution

固定一個 $i$。把 $x - a_i$ 拆成「第 $i$ 項的誤差」加上「其他項」，每一塊都被 $m_i$ 整除：

$$\begin{gather*}
x - a_i &\overset{\text{定義 1}}{=}& a_i M_i y_i - a_i + \sum_{j \neq i} a_j M_j y_j \\
x - a_i &=& a_i\left(M_i y_i - 1\right) + \sum_{j \neq i} a_j y_j M_j \\
m_i &\overset{\text{推導 2(a)(b),已知 4}}{\mid}& a_i\left(M_i y_i - 1\right) + \sum_{j \neq i} a_j y_j M_j \\
x &\overset{\text{已知 3}}{\equiv}& a_i \pmod{m_i}
\end{gather*}$$

$i$ 是任意的，故 $x$ 同時滿足全部 $r$ 條，與投影片一致。

### (b) proof that the solution is unique modulo the product

設 $x, x'$ 都是解。每個 $m_i$ 都整除 $x - x'$，由【推導 3】它們的乘積也整除：

$$\begin{gather*}
x &\equiv& x' \pmod{m_i} \qquad \text{(都} \equiv a_i \text{，遞移性)} \\
m_i &\overset{\text{已知 3}}{\mid}& x - x' \qquad \text{for all } i \\
M &\overset{\text{推導 3}}{\mid}& x - x' \\
x &\overset{\text{已知 3}}{\equiv}& x' \pmod{M}
\end{gather*}$$

### (c) proof that the whole congruence class solves the system

設 $x' = x + kM$。每個 $m_i$ 整除 $M$，故 $x' \equiv x \equiv a_i \pmod{m_i}$：

$$\begin{gather*}
x' - x &=& kM \\
m_i &\overset{\text{定義 1,已知 4}}{\mid}& kM \\
x' &\overset{\text{已知 3}}{\equiv}& x \pmod{m_i} \\
x' &\overset{\text{證明 (a)}}{\equiv}& a_i \pmod{m_i}
\end{gather*}$$

(b)(c) 合起來：解集恰為 $x + M\mathbf{Z}$，「模 $M$ 唯一」。

### (d) verify the example from the Sunzi Suanjing

$m = \left(3, 5, 7\right)$ 兩兩互質、$a = \left(2, 3, 2\right)$、$M = 105$。先算三個 $M_i$ 與反元素：

$$\begin{gather*}
M_1 &\overset{\text{定義 1}}{=}& 35 \\
35 \times 2 &=& 23 \times 3 + 1 \\
y_1 &\overset{\text{定義 1}}{=}& 2 \\
M_2 &\overset{\text{定義 1}}{=}& 21 \\
21 \times 1 &=& 4 \times 5 + 1 \\
y_2 &\overset{\text{定義 1}}{=}& 1 \\
M_3 &\overset{\text{定義 1}}{=}& 15 \\
15 \times 1 &=& 2 \times 7 + 1 \\
y_3 &\overset{\text{定義 1}}{=}& 1
\end{gather*}$$

代入高斯公式：

$$\begin{gather*}
x &\overset{\text{定義 1}}{=}& 2 \times 35 \times 2 + 3 \times 21 \times 1 + 2 \times 15 \times 1 \\
&=& 140 + 63 + 30 \\
&=& 233 \\
&=& 2 \times 105 + 23 \\
&\overset{\text{已知 3}}{\equiv}& 23 \pmod{105}
\end{gather*}$$

與投影片 p.41 一致。驗算：$23 = 7 \times 3 + 2$、$23 = 4 \times 5 + 3$、$23 = 3 \times 7 + 2$，三條都滿足。由【證明 (b)(c)】，所有解恰為 $23 + 105\mathbf{Z}$。

+++

## 意義與密碼學關聯 (Interpretation and Relevance to Cryptography)

### 《孫子算經》原文逐句對照

投影片 p.34 引用的原文，其實**就是高斯公式**，比高斯早了一千三百年：

| 原文 | 本檔 |
|---|---|
| 今有物，不知其數，三三數之剩二，五五數之剩三，七七數之剩二 | $x \equiv 2, 3, 2 \pmod{3, 5, 7}$ |
| 三三數之剩二，置一百四十 | $a_1 M_1 y_1 = 2 \times 70 = 140$ |
| 五五數之剩三，置六十三 | $a_2 M_2 y_2 = 3 \times 21 = 63$ |
| 七七數之剩二，置三十 | $a_3 M_3 y_3 = 2 \times 15 = 30$ |
| 併之，得二百三十三 | $\sum = 233$ |
| 以二百一十減之，即得 | 減去 $2M = 210$，得 $23$ |
| 凡三三數之剩一，則置七十；五五數之剩一，則置二十一；七七數之剩一，則置十五 | **$M_i y_i = 70, 21, 15$**：【推導 2】的「單位向量」 |

最後一句是全段的精華：$70$ 是「除以 $3$ 餘 $1$、被 $5, 7$ 整除」的數。有了三個單位向量，任何餘數組合都能線性組合出來。

### 韓信點兵：唯一性的界線

投影片 p.34 的故事裡，韓信說兵數「三三數之剩二，五五數之剩三，七七數之剩二」，張良說「兵數無法算，不可數！」
張良是對的 —— 由 (b)(c)，答案只確定到**模 $105$**：兵數可以是 $23, 128, 233, \dots, 10523, \dots$ 中任何一個。
**CRT 給的是同餘類，不是數字本身**。要唯一確定，需要事先知道 $0 \le x < M$。

這在密碼學裡是實際的限制：用 CRT 從 $\left(m \bmod p,\ m \bmod q\right)$ 還原明文 $m$，前提是 $m < n = pq$ —— RSA 的明文空間正是 $\mathbf{Z}_n$。

### 秘密分享與 RNS

* **Asmuth–Bloom 秘密分享**：把秘密 $s$ 的份額設為 $s \bmod m_i$，湊到足夠多份額（乘積夠大）才能由 CRT 唯一還原。
* **剩餘數系統 (RNS)**：把大整數拆成許多小模數的餘數，加法與乘法可以在各分量上**平行**計算、沒有進位傳遞。
  同態加密（如 CKKS、BFV）的實作大量使用 RNS 來加速大模數運算。

### 程式思維

```python
from math import prod
def crt_gauss(a, m):
    """投影片 p.40 的 Proof 2（高斯公式）。m 必須兩兩互質。"""
    M = prod(m)
    x = 0
    for a_i, m_i in zip(a, m):
        M_i = M // m_i
        y_i = pow(M_i, -1, m_i)            # 推導 1 保證存在
        x += a_i * M_i * y_i
    return x % M

assert crt_gauss([2, 3, 2], [3, 5, 7]) == 23                   # 證明 (d)
assert [pow(M_i, -1, m_i) * M_i for M_i, m_i in [(35, 3), (21, 5), (15, 7)]] == [70, 21, 15]
```
