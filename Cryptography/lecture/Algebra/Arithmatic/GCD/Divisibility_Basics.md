# Divisibility Basics (整除的基本性質)

+++

## 證明目標:

**投影片未列，本章補上。** `Arithmetic.pdf` 從 p.7 起大量使用「$d \mid a$」的各種推論，
卻從未把它們列出來。本檔把後面每一檔都會用到的六條整除性質一次證完，之後一律引用。

* (a) **線性組合**：整除兩數，就整除它們的任意整係數組合：

$$d \mid a,\ \ d \mid b \quad \Longrightarrow \quad d \mid \left(ax + by\right) \qquad \text{for all } x, y \in \mathbf{Z}$$

* (b) **遞移性**：

$$d \mid a,\ \ a \mid b \quad \Longrightarrow \quad d \mid b$$

* (c) **正負號無關**：

$$d \mid a \quad \Longleftrightarrow \quad -d \mid a \quad \Longleftrightarrow \quad d \mid -a$$

* (d) **兩個平凡的整除**：

$$d \mid 0 \quad \left(d \neq 0\right), \qquad 1 \mid a$$

* (e) **大小界**：非零數的因數不會比它大：

$$d \mid a,\ \ a \neq 0 \quad \Longrightarrow \quad \left|d\right| \le \left|a\right|$$

* (f) **互相整除則絕對值相等**：

$$a \mid b,\ \ b \mid a \quad \Longrightarrow \quad \left|a\right| = \left|b\right|$$

* $a,\ b$ : 任意整數 (Arbitrary integers) $[a, b \in \mathbf{Z}]$
* $d$ : 因數 (A divisor) $[d \in \mathbf{Z}]$
* $x,\ y$ : 組合係數 (Combination coefficients) $[x, y \in \mathbf{Z}]$
* 註：(a) 是整章引用次數最多的一條。[GCD 的平移不變性](GCD_Shift_Invariance.md)、
  [貝祖等式](Bezout_Identity.md)、[互質](../Factorization/Relatively_Prime.md) 全部靠它。
* 註：(e) 保證「公因數有上界」，於是**最大**公因數才存在 —— 見 [最大公因數](Greatest_Common_Divisor.md)。
* 註：(a) 取 $y = 0$ 就得到「$d \mid a \Rightarrow d \mid ax$」（整除倍數），後文常直接這樣用。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [整除 (Divisibility)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Number_Sets_and_Notation.html#assumptions-preliminaries)：** 已於 Abstract_Algebra 章 [數系與符號約定](../../Abstract_Algebra/Number_Sets_and_Notation.md)【已知 1(a)】給出，此處直接引用

  $$m \mid k \quad \overset{\text{def}}{\Longleftrightarrow} \quad \exists\, t \in \mathbf{Z} \ \text{ such that } \ k = mt$$

  * $m,\ k$ : 任意整數 (Arbitrary integers) $[m, k \in \mathbf{Z}]$
  * $t$ : 整數倍數 (Integer multiplier) $[t \in \mathbf{Z}]$

* **【已知 2】 [絕對值的性質 (Properties of the absolute value)](https://mathworld.wolfram.com/AbsoluteValue.html)：** 標準結果，本章直接引用不再重證

  * (a) 乘法性：

    $$\left|xy\right| = \left|x\right|\left|y\right|$$

  * (b) 非零整數的絕對值至少是 $1$：

    $$t \in \mathbf{Z},\ t \neq 0 \quad \Longrightarrow \quad \left|t\right| \ge 1$$

  * $x,\ y$ : 任意整數 (Arbitrary integers) $[x, y \in \mathbf{Z}]$
  * $t$ : 非零整數 (A non-zero integer) $[t \in \mathbf{Z}]$

+++

## 證明:

### (a) proof that a common divisor divides every linear combination

$$\begin{gather*}
a &\overset{\text{已知 1}}{=}& d s \qquad \text{for some } s \in \mathbf{Z} \\
b &\overset{\text{已知 1}}{=}& d t \qquad \text{for some } t \in \mathbf{Z} \\
ax + by &=& \left(ds\right)x + \left(dt\right)y \\
ax + by &=& d\left(sx + ty\right) \\
d &\overset{\text{已知 1}}{\mid}& ax + by \qquad \text{(} sx + ty \in \mathbf{Z} \text{)}
\end{gather*}$$

### (b) proof that divisibility is transitive

$$\begin{gather*}
a &\overset{\text{已知 1}}{=}& d s \\
b &\overset{\text{已知 1}}{=}& a t \\
b &=& d\left(st\right) \\
d &\overset{\text{已知 1}}{\mid}& b
\end{gather*}$$

### (c) proof that divisibility ignores signs

同一個等式 $a = dt$ 換個方式分配負號，就同時是三種整除的見證：

$$\begin{gather*}
d \mid a &\overset{\text{已知 1}}{\Longleftrightarrow}& a = d t \\
&\Longleftrightarrow& a = \left(-d\right)\left(-t\right) \\
&\overset{\text{已知 1}}{\Longleftrightarrow}& -d \mid a
\end{gather*}$$

$$\begin{gather*}
d \mid a &\overset{\text{已知 1}}{\Longleftrightarrow}& a = d t \\
&\Longleftrightarrow& -a = d\left(-t\right) \\
&\overset{\text{已知 1}}{\Longleftrightarrow}& d \mid -a
\end{gather*}$$

* 註：反覆套用兩條等價鏈即得 $d \mid a \Longleftrightarrow \left|d\right| \ \middle|\ \left|a\right|$。

### (d) proof of the two trivial divisibilities

$$\begin{gather*}
0 &=& d \times 0 \\
d &\overset{\text{已知 1}}{\mid}& 0 \\
a &=& 1 \times a \\
1 &\overset{\text{已知 1}}{\mid}& a
\end{gather*}$$

* 註：**$0$ 被每個非零整數整除**。這是 $\gcd(a, 0) = \left|a\right|$ 的根源
  （[最大公因數](Greatest_Common_Divisor.md)【證明 (b)】）。
  $d = 0$ 被排除，是因為「$0 \mid 0$」在 gcd 的定義裡要求公因數非零。

### (e) proof that a divisor of a nonzero integer is no larger in absolute value

$a \neq 0$ 迫使倍數 $t \neq 0$，於是 $\left|t\right| \ge 1$：

$$\begin{gather*}
a &\overset{\text{已知 1}}{=}& d t \\
t &\neq& 0 \qquad \text{(否則 } a = 0 \text{)} \\
\left|a\right| &\overset{\text{已知 2(a)}}{=}& \left|d\right| \left|t\right| \\
\left|a\right| &\overset{\text{已知 2(b)}}{\ge}& \left|d\right| \times 1 \\
\left|a\right| &\ge& \left|d\right|
\end{gather*}$$

### (f) proof that mutual divisibility forces equal absolute values

**情形一：$a = 0$。** 則 $b = a t = 0$，兩者相等。

**情形二：$a \neq 0$。** 則 $b \neq 0$（否則 $a = b s = 0$），兩個方向各用一次【證明 (e)】：

$$\begin{gather*}
\left|a\right| &\overset{\text{證明 (e)}}{\le}& \left|b\right| \qquad \text{(} a \mid b,\ b \neq 0 \text{)} \\
\left|b\right| &\overset{\text{證明 (e)}}{\le}& \left|a\right| \qquad \text{(} b \mid a,\ a \neq 0 \text{)} \\
\left|a\right| &=& \left|b\right|
\end{gather*}$$

+++

## 意義與密碼學關聯 (Interpretation and Relevance to Cryptography)

### 整除就是「落在某個理想裡」

$d \mid a$ 的另一種說法是 $a \in d\mathbf{Z}$。這樣看：

* (a) 線性組合封閉 $\Longleftrightarrow$ $d\mathbf{Z}$ 是 $\mathbf{Z}$ 的**理想**
  （加法封閉 + 吸收乘法）；
* (b) 遞移性 $\Longleftrightarrow$ $a\mathbf{Z} \subseteq d\mathbf{Z}$（小理想包在大理想裡）。

這是 Abstract_Algebra 章 [理想](../../Abstract_Algebra/Ring/Ideal.md) 的具體版本。
本章用初等語言重走一遍，因為**演算法是用初等語言寫的**。

### 線性組合性質是「用 gcd 分解 $n$」攻擊的核心

若攻擊者手上有兩個數 $x, y$ 都是 $p$ 的倍數（例如兩把共用質因數的 RSA 公鑰 $n_1 = pq_1$、$n_2 = pq_2$），
則由 (a)，$p$ 整除 $n_1, n_2$ 的每一個組合 —— 而 [歐幾里得演算法](Euclidean_Algorithm.md) 正是在做這種組合，
最後得到 $\gcd(n_1, n_2) = p$，**兩把金鑰同時被分解**。
2012 年 Lenstra 等人對網路上數百萬把 RSA 公鑰做批次 gcd，真的分解了約 $0.2\%$ 的金鑰，原因就是弱亂數產生器讓不同金鑰共用了質因數。

### 程式思維

```python
def divides(d, a):
    """已知 1：存在整數 t 使 a = d*t。d = 0 時只有 a = 0 符合，這裡直接排除。"""
    return d != 0 and a % d == 0

assert divides(3, 12) and divides(-3, 12) and divides(3, -12)   # 證明 (c)
assert divides(7, 0)                                            # 證明 (d)
d, a, b = 5, 35, 100
assert all(divides(d, a*x + b*y) for x in range(-5, 6) for y in range(-5, 6))  # 證明 (a)
```
