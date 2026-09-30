# Relatively Prime (互質)

+++

## 證明目標:

`Arithmetic.pdf` p.22。「互質」是整章後半的通行證 —— 模反元素、中國剩餘定理、尤拉函數都以它為前提。
本檔先證投影片的定理，再補兩條投影片在後面**默默使用卻沒有證明**的引理。

* (a) 投影片的定理（**廣義歐幾里得引理**）：

$$a \mid bc,\ \ a \perp b \quad \Longrightarrow \quad a \mid c$$

* (b) 互質對乘法封閉（**投影片未列，本章補**；[中國剩餘定理](../CRT/Chinese_Remainder_Theorem.md)、[尤拉函數的乘法性](../Fermat_Euler/Euler_Phi_Multiplicativity.md) 要用）：

$$a \perp m,\ \ b \perp m \quad \Longrightarrow \quad ab \perp m$$

* (c) 互質的兩個因數同時整除，則乘積整除（**投影片未列，本章補**；p.39 寫「since $m_1 \perp m_2$」直接使用）：

$$m_1 \mid x,\ \ m_2 \mid x,\ \ m_1 \perp m_2 \quad \Longrightarrow \quad m_1 m_2 \mid x$$

* (d) 驗證：$9 \perp 20$；以及「$a \perp b$」這個條件在 (a) 中不可省（反例 $6 \mid 4 \times 9$ 但 $6 \nmid 4$、$6 \nmid 9$）。

* $a,\ b,\ c$ : 整數 (Integers) $[a, b, c \in \mathbf{Z}]$
* $m,\ m_1,\ m_2$ : 模數或因數 (Moduli or divisors) $[m, m_1, m_2 \in \mathbf{Z}]$
* $x$ : 被整除的整數 (The integer being divided) $[x \in \mathbf{Z}]$
* $a \perp b$ : $a$ 與 $b$ 互質 ($a$ and $b$ are relatively prime) $[\text{關係}]$
* 註：投影片 p.22 的第一條定理（gcd 是最小正組合）已獨立成 [貝祖等式](../GCD/Bezout_Identity.md)，本檔直接引用其系理。
* 註：(c) 的條件 $m_1 \perp m_2$ 不可省：$4 \mid 12$、$6 \mid 12$，但 $24 \nmid 12$。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [互質的組合刻畫 (Coprimality via combinations)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/GCD/Bezout_Identity.html#d-proof-that-a-combination-equal-to-one-forces-coprimality)：** 已於本章 [貝祖等式](../GCD/Bezout_Identity.md)【證明 (c)(d)】完整證明，此處直接引用不再重證

  $$\gcd(a, b) = 1 \quad \Longleftrightarrow \quad \exists\, x, y \in \mathbf{Z} \ \text{ such that } \ ax + by = 1$$

  * $a,\ b$ : 不全為零的整數 (Integers, not both zero) $[a, b \in \mathbf{Z}]$
  * $x,\ y$ : 組合係數 (Combination coefficients) $[x, y \in \mathbf{Z}]$

* **【已知 2】 [整除的基本性質 (Divisibility basics)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/GCD/Divisibility_Basics.html#a-proof-that-a-common-divisor-divides-every-linear-combination)：** 已於本章 [整除的基本性質](../GCD/Divisibility_Basics.md)【證明 (a)】完整證明，此處直接引用不再重證

  $$d \mid a,\ \ d \mid b \quad \Longrightarrow \quad d \mid \left(ax + by\right) \qquad \text{for all } x, y \in \mathbf{Z}$$

  * $a,\ b$ : 任意整數 (Arbitrary integers) $[a, b \in \mathbf{Z}]$
  * $d$ : 公因數 (A common divisor) $[d \in \mathbf{Z}]$
  * $x,\ y$ : 組合係數 (Combination coefficients) $[x, y \in \mathbf{Z}]$

* **【定義 1】 互質 (Relatively prime)：**

  $$a \perp b \quad \overset{\text{def}}{\Longleftrightarrow} \quad \gcd(a, b) = 1$$

  * $a,\ b$ : 不全為零的整數 (Integers, not both zero) $[a, b \in \mathbf{Z}]$
  * $a \perp b$ : 互質 (Relatively prime, coprime) $[\text{關係}]$
  * 註：$\perp$ 是投影片採用的記號（Knuth 的寫法），取「垂直」之意 —— 兩數「沒有共同方向」。
  * 註：由 gcd 的對稱性，$a \perp b \Longleftrightarrow b \perp a$。

+++

## 證明:

### (a) proof of the generalized Euclid lemma

把 $a \perp b$ 寫成組合，兩邊乘 $c$，右邊恰好剩下 $c$；左邊兩項都被 $a$ 整除：

$$\begin{gather*}
a x + b y &\overset{\text{定義 1,已知 1}}{=}& 1 \\
a c x + b c y &=& c \\
a &\mid& a \qquad \text{(自明)} \\
a &\mid& bc \qquad \text{(前提)} \\
a &\overset{\text{已知 2}}{\mid}& a \left(cx\right) + \left(bc\right) y \\
a &\mid& c
\end{gather*}$$

與投影片一致。

### (b) proof that coprimality to a modulus is closed under products

把兩個「湊出 $1$」相乘，展開後所有含 $m$ 的項歸成一堆：

$$\begin{gather*}
a x + m y &\overset{\text{定義 1,已知 1}}{=}& 1 \\
b u + m v &\overset{\text{定義 1,已知 1}}{=}& 1 \\
\left(ax\right)\left(bu\right) &=& \left(1 - my\right)\left(1 - mv\right) \\
ab\left(xu\right) &=& 1 - m\left(y + v - myv\right) \\
ab\left(xu\right) + m\left(y + v - myv\right) &=& 1 \\
\gcd(ab, m) &\overset{\text{已知 1}}{=}& 1 \\
ab &\overset{\text{定義 1}}{\perp}& m
\end{gather*}$$

* 註：把兩個等於 $1$ 的式子**相乘**，與 Abstract_Algebra 章 [中國剩餘定理](../../Abstract_Algebra/Ring/Chinese_Remainder_Theorem.md)【推導 1】
  的技巧完全相同 —— 那裡是理想版本，這裡是整數版本。
* 註：反覆套用得 $a_1, \dots, a_k$ 都與 $m$ 互質 $\Longrightarrow$ $a_1 a_2 \cdots a_k \perp m$。

### (c) proof that coprime divisors multiply

寫 $x = m_1 k$；$m_2$ 整除 $m_1 k$ 而與 $m_1$ 互質，由 (a) 它整除 $k$：

$$\begin{gather*}
x &=& m_1 k \qquad \text{(} m_1 \mid x \text{)} \\
m_2 &\mid& m_1 k \qquad \text{(} m_2 \mid x \text{)} \\
m_2 &\overset{\text{證明 (a)}}{\mid}& k \qquad \text{(} m_2 \perp m_1 \text{)} \\
k &=& m_2 l \qquad \text{for some } l \in \mathbf{Z} \\
x &=& m_1 m_2 l \\
m_1 m_2 &\mid& x
\end{gather*}$$

### (d) verify the coprime example and the counterexample

**$9 \perp 20$**：湊出 $1$ 即可，由【已知 1】直接判定：

$$\begin{gather*}
9 \times 9 + 20 \times \left(-4\right) &=& 81 - 80 \\
9 \times 9 + 20 \times \left(-4\right) &=& 1 \\
\gcd(9, 20) &\overset{\text{已知 1}}{=}& 1
\end{gather*}$$

**(a) 的互質條件不可省**：取 $a = 6$、$b = 4$、$c = 9$，$\gcd(6, 4) = 2 \neq 1$：

$$\begin{gather*}
4 \times 9 &=& 36 \\
36 &=& 6 \times 6 \\
6 &\mid& 4 \times 9 \\
6 &\nmid& 4 \\
6 &\nmid& 9
\end{gather*}$$

$6$ 的兩個質因數 $2, 3$ 分別躲在 $4$ 與 $9$ 裡，所以 $6$ 整除乘積卻不整除任何一個因子。

+++

## 意義與密碼學關聯 (Interpretation and Relevance to Cryptography)

### 「互質」就是「沒有共同的質因數」

等[算術基本定理](Fundamental_Theorem_of_Arithmetic.md) 證完後，$a \perp b$ 可以讀成「兩者的質因數分解沒有交集」。
(a) 的直覺就是：$a$ 的質因數全部要在 $bc$ 裡找到，但一個都不在 $b$ 裡，只好全在 $c$ 裡。

### 整章的依賴關係

| 用到本檔的地方 | 用哪一條 |
|---|---|
| [歐幾里得引理](Euclid_Lemma.md)（質數版） | (a) |
| [同餘的性質](../Congruence/Congruence_Properties.md) 的消去律 | (a) 的變形 |
| [兩個模數的中國剩餘定理](../CRT/Two_Moduli_CRT.md) 的唯一性 | (c) |
| [中國剩餘定理](../CRT/Chinese_Remainder_Theorem.md) 的構造 | (b) |
| [尤拉函數的乘法性](../Fermat_Euler/Euler_Phi_Multiplicativity.md) | (b) |

### 密碼學：RSA 的兩個互質條件

RSA 金鑰產生時要確認兩件互質：

1. $\gcd\left(e, \varphi(n)\right) = 1$ —— 保證私鑰 $d = e^{-1} \bmod \varphi(n)$ 存在；
2. $\gcd(p, q) = 1$ —— 兩個相異質數自動成立，保證 $\mathbf{Z}_n \cong \mathbf{Z}_p \times \mathbf{Z}_q$（CRT）。

(c) 在 RSA-CRT 解密中扮演關鍵角色：若 $m \equiv m' \pmod p$ 且 $m \equiv m' \pmod q$，
由 (c) 得 $pq \mid m - m'$，即 $m \equiv m' \pmod n$ —— **兩個小模數的答案拼起來是唯一的**。

### 程式思維

```python
from math import gcd
coprime = lambda a, b: gcd(a, b) == 1
assert 9 * 9 + 20 * (-4) == 1 and coprime(9, 20)            # 證明 (d)
# (b)：互質對乘法封閉
assert all(coprime(a * b, 20) for a in range(1, 50) for b in range(1, 50)
           if coprime(a, 20) and coprime(b, 20))
# (c)：互質因數相乘仍整除
assert all(x % 35 == 0 for x in range(0, 2000) if x % 5 == 0 and x % 7 == 0)
```
