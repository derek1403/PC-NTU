# Bezout Identity (貝祖等式)

+++

## 證明目標:

`Arithmetic.pdf` p.22 第一條定理。[擴展歐幾里得演算法](Extended_Euclidean_Algorithm.md) 證明了 gcd **是**一個組合；
本檔證明它還是**最小的**正組合 —— 於是 gcd 有了一個完全不提「因數」的刻畫。

* (a) **定理**：設 $a, b$ 不全為零，則 $\gcd(a, b)$ 是所有形如 $ax + by$ 的**正**整數中最小的：

$$\gcd(a, b) = \min\left\{ax + by \ \middle|\ x, y \in \mathbf{Z},\ ax + by > 0\right\}$$

* (b) 系理一：**每個公因數都整除 gcd**：

$$c \mid a,\ \ c \mid b \quad \Longrightarrow \quad c \mid \gcd(a, b)$$

* (c)(d) 系理二：**互質的組合刻畫**（(⇒) 與 (⇐) 兩向）：

$$\gcd(a, b) = 1 \quad \Longleftrightarrow \quad \exists\, x, y \in \mathbf{Z} \ \text{ such that } \ ax + by = 1$$

* (e) 驗證：$\gcd(15, 21) = 3 = 15 \times 3 + 21 \times \left(-2\right)$，且沒有更小的正組合。

* $a,\ b$ : 不全為零的整數 (Integers, not both zero) $[a, b \in \mathbf{Z}]$
* $x,\ y$ : 組合係數 (Combination coefficients) $[x, y \in \mathbf{Z}]$
* $c$ : 任一公因數 (Any common divisor) $[c \in \mathbf{Z},\ c \neq 0]$
* $S$ : 正的整係數組合全體 (The set of positive integer combinations) $[S \subseteq \mathbf{P}]$
* 註：(c) 的 (⇐) 方向是整章最常用的「互質證明法」：**只要湊出一組係數讓組合等於 $1$，就證完互質**。
  [互質](../Factorization/Relatively_Prime.md)、[模反元素](../Congruence/Modular_Inverse.md) 都靠它。
* 註：(b) 說明 gcd 不只是「最大的」公因數，還是**被所有公因數整除**的那個 ——
  這是比「最大」更強、也更代數的性質，可以推廣到沒有大小順序的環（如多項式環）。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [貝祖係數存在 (Existence of Bézout coefficients)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/GCD/Extended_Euclidean_Algorithm.html#c-proof-of-the-existence-of-bezout-coefficients)：** 已於本章 [擴展歐幾里得演算法](Extended_Euclidean_Algorithm.md)【證明 (c)】完整證明，此處直接引用不再重證

  $$\exists\, x_0, y_0 \in \mathbf{Z} \ \text{ such that } \ a x_0 + b y_0 = \gcd(a, b)$$

  * $a,\ b$ : 不全為零的整數 (Integers, not both zero) $[a, b \in \mathbf{Z}]$
  * $x_0,\ y_0$ : 一組貝祖係數 (A pair of Bézout coefficients) $[x_0, y_0 \in \mathbf{Z}]$

* **【已知 2】 [整除的基本性質 (Divisibility basics)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/GCD/Divisibility_Basics.html#a-proof-that-a-common-divisor-divides-every-linear-combination)：** 已於本章 [整除的基本性質](Divisibility_Basics.md)【證明 (a)(e)】完整證明，此處直接引用不再重證

  * (a) 線性組合：

    $$d \mid a,\ \ d \mid b \quad \Longrightarrow \quad d \mid \left(ax + by\right)$$

  * (b) 大小界：

    $$d \mid n,\ \ n \neq 0 \quad \Longrightarrow \quad \left|d\right| \le \left|n\right|$$

  * $a,\ b,\ n$ : 任意整數 (Arbitrary integers) $[a, b, n \in \mathbf{Z}]$
  * $d$ : 因數 (A divisor) $[d \in \mathbf{Z}]$

* **【已知 3】 [最大公因數是公因數 (The gcd is a common divisor)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/GCD/Greatest_Common_Divisor.html#a-proof-that-the-greatest-common-divisor-exists-and-is-positive)：** 已於本章 [最大公因數](Greatest_Common_Divisor.md)【定義 2】【證明 (a)】給出並證明，此處直接引用不再重證

  $$\gcd(a, b) \mid a, \qquad \gcd(a, b) \mid b, \qquad \gcd(a, b) \ge 1$$

  * $a,\ b$ : 不全為零的整數 (Integers, not both zero) $[a, b \in \mathbf{Z}]$

* **【定義 1】 正組合集合 (The set of positive combinations)：**

  $$S \overset{\text{def}}{=} \left\{ax + by \ \middle|\ x, y \in \mathbf{Z},\ ax + by > 0\right\}$$

  * $S$ : 正的整係數組合全體 (The set of positive integer combinations) $[S \subseteq \mathbf{P}]$
  * $a,\ b$ : 不全為零的整數 (Integers, not both zero) $[a, b \in \mathbf{Z}]$
  * $x,\ y$ : 組合係數 (Combination coefficients) $[x, y \in \mathbf{Z}]$

+++

## 證明:

### (a) proof that the gcd is the smallest positive combination

**$\gcd(a,b)$ 在 $S$ 裡**：由【已知 1】它是一個組合，由【已知 3】它是正的。

**$S$ 裡每個元素都 $\ge \gcd(a,b)$**：gcd 整除 $a$ 與 $b$，故整除它們的每個組合；而正整數的正因數不超過它自己：

$$\begin{gather*}
\gcd(a, b) &\overset{\text{已知 1}}{=}& a x_0 + b y_0 \\
\gcd(a, b) &\overset{\text{已知 3}}{>}& 0 \\
\gcd(a, b) &\overset{\text{定義 1}}{\in}& S \\
\gcd(a, b) &\overset{\text{已知 2(a),已知 3}}{\mid}& ax + by \qquad \text{for every } ax + by \in S \\
\gcd(a, b) &\overset{\text{已知 2(b)}}{\le}& ax + by \qquad \text{(} ax + by > 0 \text{)} \\
\gcd(a, b) &=& \min S
\end{gather*}$$

與投影片一致。

### (b) proof that every common divisor divides the gcd

把 gcd 寫成組合，公因數就整除它：

$$\begin{gather*}
\gcd(a, b) &\overset{\text{已知 1}}{=}& a x_0 + b y_0 \\
c &\overset{\text{已知 2(a)}}{\mid}& a x_0 + b y_0 \qquad \text{(} c \mid a,\ c \mid b \text{)} \\
c &\mid& \gcd(a, b)
\end{gather*}$$

### (c) proof (⇒) that coprime integers combine to one

$$\begin{gather*}
a x_0 + b y_0 &\overset{\text{已知 1}}{=}& \gcd(a, b) \\
a x_0 + b y_0 &=& 1
\end{gather*}$$

### (d) proof (⇐) that a combination equal to one forces coprimality

$1$ 是正的組合，所以在 $S$ 裡；而 $S$ 的最小元素就是 gcd，且 gcd 至少是 $1$：

$$\begin{gather*}
1 &\overset{\text{定義 1}}{\in}& S \\
\gcd(a, b) &\overset{\text{證明 (a)}}{\le}& 1 \\
\gcd(a, b) &\overset{\text{已知 3}}{\ge}& 1 \\
\gcd(a, b) &=& 1
\end{gather*}$$

(c)(d) 合起來即系理二。

### (e) verify the example of fifteen and twenty-one

由【證明 (a)】，只要找到一個等於 $3$ 的組合、並說明 $1, 2$ 不是組合即可。
$15, 21$ 都是 $3$ 的倍數，所以每個組合都是 $3$ 的倍數，$1$ 與 $2$ 不可能出現：

$$\begin{gather*}
15 \times 3 + 21 \times \left(-2\right) &=& 45 - 42 \\
15 \times 3 + 21 \times \left(-2\right) &=& 3 \\
3 &\overset{\text{已知 2(a)}}{\mid}& 15x + 21y \qquad \text{for all } x, y \\
\min S &=& 3 \\
\gcd(15, 21) &\overset{\text{證明 (a)}}{=}& 3
\end{gather*}$$

與 Abstract_Algebra 章 [主理想](../../Abstract_Algebra/Ring/Principal_Ideal.md)【證明 (d)】的
$\left\langle 15, 21 \right\rangle = \left\langle 3 \right\rangle$ 一致。

+++

## 意義與密碼學關聯 (Interpretation and Relevance to Cryptography)

### gcd 的三種面貌

到這裡，同一個數 $\gcd(a,b)$ 有了三個等價的刻畫：

| 觀點 | 刻畫 | 出處 |
|---|---|---|
| 因數 | 最大的公因數 | [最大公因數](Greatest_Common_Divisor.md)【定義 2】 |
| 組合 | 最小的正組合 | 本檔【證明 (a)】 |
| 理想 | $\left\langle a, b \right\rangle$ 的生成元 | [主理想](../../Abstract_Algebra/Ring/Principal_Ideal.md)【證明 (c)(d)】 |

第二種與第三種其實是同一件事：$\left\{ax + by\right\} = \left\langle a, b \right\rangle$，而
Abstract_Algebra 證明了 $\mathbf{Z}$ 的每個理想都由它**最小的正元素**生成。

### 互質就是「湊得出 $1$」

系理二把「沒有共同因數」（一個關於**不存在**的陳述，難以直接驗證）
換成「存在 $x, y$ 使 $ax + by = 1$」（一個**可以出示證據**的陳述）。
擴展歐幾里得演算法會直接把這組 $x, y$ 算出來，所以互質性是**可以被驗證的**。

這在密碼學裡有具體意義：證明者可以出示 $\left(x, y\right)$ 讓驗證者用兩次乘法、一次加法確認 $\gcd = 1$，
不必讓對方重跑整個演算法。

### 程式思維

```python
from math import gcd
def smallest_positive_combination(a, b, bound=50):
    return min(a*x + b*y for x in range(-bound, bound+1)
                         for y in range(-bound, bound+1) if a*x + b*y > 0)

assert smallest_positive_combination(15, 21) == gcd(15, 21) == 3     # 證明 (e)
assert smallest_positive_combination(100, 35) == gcd(100, 35) == 5
```
