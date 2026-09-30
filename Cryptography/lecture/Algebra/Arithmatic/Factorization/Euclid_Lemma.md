# Euclid Lemma (歐幾里得引理)

+++

## 證明目標:

`Arithmetic.pdf` p.23。質數最重要的性質：**質數整除乘積，就整除其中一個因子**。
這是 [算術基本定理](Fundamental_Theorem_of_Arithmetic.md) 唯一性的全部依據。

* (a) 質數與不被它整除的數互質：

$$p \ \text{為質數},\ \ p \nmid a \quad \Longrightarrow \quad \gcd(p, a) = 1$$

* (b) 投影片的第一個系理（**歐幾里得引理**）：

$$p \mid ab \quad \Longrightarrow \quad p \mid a \ \text{ or } \ p \mid b$$

* (c)(d) 投影片的第二個系理（推廣到 $k$ 個因子，用歸納法）：

$$p \mid a_1 a_2 \cdots a_k \quad \Longrightarrow \quad p \mid a_i \ \text{ for some } i$$

* (e) 驗證：$7 \mid 4 \times 21$ 故 $7 \mid 21$；而合數 $6$ 不具此性質。

* $p$ : 質數 (A prime) $[p \in \mathbf{P}]$
* $a,\ b,\ a_1, \dots, a_k$ : 整數 (Integers) $[a, b, a_i \in \mathbf{Z}]$
* $k$ : 因子個數 (The number of factors) $[k \in \mathbf{P}]$
* $i$ : 因子指標 (Factor index) $[i \in \left\{1, \dots, k\right\}]$
* 註：投影片 p.23 的第二個系理寫「repeat the argument, eventually we must get $p \mid a_i$」，
  這是一個非正式的歸納。本檔依 A5 寫成正式的基底 + 歸納步驟。
* 註：**「$p$ 是質數」不可省**：$6 \mid 4 \times 9$，但 $6 \nmid 4$ 且 $6 \nmid 9$（見 [互質](Relatively_Prime.md)【證明 (d)】）。
  事實上「整除乘積必整除某因子」可以反過來當成質數的**定義** —— 在一般的環裡這叫「質元素 (prime element)」。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [廣義歐幾里得引理 (Generalized Euclid lemma)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/Factorization/Relatively_Prime.html#a-proof-of-the-generalized-euclid-lemma)：** 已於本章 [互質](Relatively_Prime.md)【證明 (a)】完整證明，此處直接引用不再重證

  $$p \mid bc,\ \ \gcd(p, b) = 1 \quad \Longrightarrow \quad p \mid c$$

  * $p,\ b,\ c$ : 整數 (Integers) $[p, b, c \in \mathbf{Z}]$

* **【已知 2】 [gcd 是正的公因數 (The gcd is a positive common divisor)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/GCD/Greatest_Common_Divisor.html#a-proof-that-the-greatest-common-divisor-exists-and-is-positive)：** 已於本章 [最大公因數](../GCD/Greatest_Common_Divisor.md)【定義 2】【證明 (a)】給出並證明，此處直接引用不再重證

  $$\gcd(p, a) \mid p, \qquad \gcd(p, a) \mid a, \qquad \gcd(p, a) \in \mathbf{P}$$

  * $p,\ a$ : 不全為零的整數 (Integers, not both zero) $[p, a \in \mathbf{Z}]$

* **【定義 1】 質數 (Prime number)：** 大於 $1$，且正因數只有 $1$ 與自己

  $$p \ \text{為質數} \quad \overset{\text{def}}{\Longleftrightarrow} \quad p > 1 \ \text{ and } \ \left\{d \in \mathbf{P} \ \middle|\ d \mid p\right\} = \left\{1, p\right\}$$

  * $p$ : 被判定的正整數 (The positive integer under test) $[p \in \mathbf{P}]$
  * $d$ : 正因數 (A positive divisor) $[d \in \mathbf{P}]$
  * 註：大於 $1$ 而不是質數的正整數稱為**合數 (composite)**：它有一個真因數 $d$，$1 < d < p$。
  * 註：$1$ **不是**質數。這不是任意的約定 —— 若允許 $1$ 為質數，
    [算術基本定理](Fundamental_Theorem_of_Arithmetic.md) 的唯一性就壞了（$6 = 2 \times 3 = 1 \times 2 \times 3$）。

* **【假設 1】 歸納假設 (Induction hypothesis)：** 【證明 (d)】對因子個數 $k$ 做歸納時的假設。
  設結論對 $k - 1$ 個因子成立

  $$p \mid a_1 a_2 \cdots a_{k-1} \quad \Longrightarrow \quad p \mid a_i \ \text{ for some } i \le k-1$$

  * $p$ : 質數 (A prime) $[p \in \mathbf{P}]$
  * $a_1, \dots, a_{k-1}$ : 前 $k-1$ 個因子 (The first $k-1$ factors) $[a_i \in \mathbf{Z}]$
  * $k$ : 因子個數 (The number of factors) $[k \in \mathbf{P},\ k \ge 2]$

+++

## 證明:

### (a) proof that a prime is coprime to every integer it does not divide

$g = \gcd(p, a)$ 是 $p$ 的正因數，所以只有兩種可能；$g = p$ 會讓 $p \mid a$，與前提矛盾：

$$\begin{gather*}
g &\overset{\text{已知 2}}{\mid}& p \\
g &\overset{\text{定義 1}}{\in}& \left\{1, p\right\} \qquad \text{(} g \in \mathbf{P} \text{)} \\
g = p &\overset{\text{已知 2}}{\Longrightarrow}& p \mid a \qquad \text{(與 } p \nmid a \text{ 矛盾)} \\
\gcd(p, a) &=& 1
\end{gather*}$$

與投影片「$p \nmid a \Rightarrow \gcd(p, a) = 1$」一致。

### (b) proof of Euclid's lemma for two factors

**情形一：$p \mid a$。** 已完成。

**情形二：$p \nmid a$。** 由 (a) 得互質，再用廣義歐幾里得引理：

$$\begin{gather*}
\gcd(p, a) &\overset{\text{證明 (a)}}{=}& 1 \\
p &\overset{\text{已知 1}}{\mid}& b \qquad \text{(} p \mid ab \text{)}
\end{gather*}$$

兩種情形合起來即 $p \mid a$ 或 $p \mid b$，與投影片一致。

### (c) proof of the base case for one factor

$k = 1$ 時結論就是前提本身：

$$\begin{gather*}
p &\mid& a_1
\end{gather*}$$

### (d) proof of the inductive step for k factors

把 $k$ 個因子的乘積看成「前 $k-1$ 個的乘積」乘「$a_k$」兩個因子，套 (b)：

$$\begin{gather*}
p &\mid& \left(a_1 \cdots a_{k-1}\right) a_k \\
p \mid \left(a_1 \cdots a_{k-1}\right) a_k &\overset{\text{證明 (b)}}{\Longrightarrow}& p \mid a_1 \cdots a_{k-1} \ \text{ or } \ p \mid a_k
\end{gather*}$$

* 若 $p \mid a_k$：完成（$i = k$）。
* 若 $p \mid a_1 \cdots a_{k-1}$：

$$\begin{gather*}
p \mid a_1 \cdots a_{k-1} &\overset{\text{假設 1}}{\Longrightarrow}& p \mid a_i \ \text{ for some } i \le k-1
\end{gather*}$$

兩種情形都找到某個 $a_i$。由 (c)(d) 與歸納法，對所有 $k$ 成立，與投影片一致。

### (e) verify the prime example and the composite counterexample

**質數 $7$**：$7 \mid 84 = 4 \times 21$，而 $7 \nmid 4$，故必整除另一個因子：

$$\begin{gather*}
4 \times 21 &=& 84 \\
84 &=& 7 \times 12 \\
7 &\nmid& 4 \\
7 &\overset{\text{證明 (b)}}{\mid}& 21
\end{gather*}$$

確實 $21 = 7 \times 3$。

**合數 $6$**：$6 \mid 4 \times 9 = 36$，但 $6 \nmid 4$ 且 $6 \nmid 9$ —— $6$ 不是質數，(b) 不適用；
失敗的原因是 (a) 在 $6$ 身上不成立：$6 \nmid 4$ 但 $\gcd(6, 4) = 2 \neq 1$。

+++

## 意義與密碼學關聯 (Interpretation and Relevance to Cryptography)

### 質數是「不可拆的原子」，而且拆法是乾淨的

歐幾里得引理保證：**質數不會「分散」在兩個因子之間**。$6$ 可以一半躲在 $4$ 裡（因子 $2$）、
一半躲在 $9$ 裡（因子 $3$），質數做不到 —— 它沒有「一半」。
這個性質直接推出 [算術基本定理](Fundamental_Theorem_of_Arithmetic.md) 的唯一性：
一個質數出現在一邊的分解裡，就必須出現在另一邊。

### $\mathbf{Z}_p$ 沒有零因子的真正原因

在 $\mathbf{Z}_p$ 裡 $ab \equiv 0$ 就是 $p \mid ab$，由 (b) 得 $p \mid a$ 或 $p \mid b$，
即 $a \equiv 0$ 或 $b \equiv 0$ —— **$\mathbf{Z}_p$ 沒有零因子**。
這正是 Abstract_Algebra 章 [零因子](../../Abstract_Algebra/Ring/Zero_Divisor.md)【證明 (b)】所引用的外部結果，本檔把它證出來了。
對比 [凱萊表](../Division/Cayley_Tables_of_Z6.md) 裡 $\mathbf{Z}_6$ 的 $2 \otimes 3 = 0$。

### 程式思維

```python
def is_prime(n):
    return n > 1 and all(n % d for d in range(2, int(n**0.5) + 1))

# 歐幾里得引理：只對質數成立
for p in range(2, 40):
    holds = all((a*b) % p != 0 or a % p == 0 or b % p == 0
                for a in range(1, 60) for b in range(1, 60))
    assert holds == is_prime(p)
```
