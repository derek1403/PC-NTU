# Two Moduli CRT (兩個模數的中國剩餘定理)

+++

## 證明目標:

`Arithmetic.pdf` p.38–39。回答 [座標表示](CRT_Coordinate_Representation.md) 留下的問題：
**給定座標 $\left(a_1, a_2\right)$，怎麼算回原來的數？** 投影片給了一條明確公式。

投影片的命題：若 $m_1 \perp m_2$，同餘方程組

$$x \equiv a_1 \pmod{m_1}, \qquad x \equiv a_2 \pmod{m_2}$$

有解，且任兩解模 $m_1 m_2$ 同餘。

* (a) **存在性**（構造解）：令 $t = m_1^{-1}\left(a_2 - a_1\right) \bmod m_2$，則

$$x = a_1 + m_1 t$$

  是一個解。

* (b) **唯一性**：任兩解 $x_1, x_2$ 滿足 $x_1 \equiv x_2 \pmod{m_1 m_2}$。
* (c) **反過來**（投影片未列，本章補）：與一個解模 $m_1 m_2$ 同餘的數也都是解 —— 所以解集**恰好**是一個同餘類。
* (d) 驗證投影片 p.38 的例子：

$$x \equiv 4 \pmod{7},\ \ x \equiv 3 \pmod{5} \quad \Longrightarrow \quad x \equiv 18 \pmod{35}$$

* $m_1,\ m_2$ : 互質的模數 (Coprime moduli) $[m_1, m_2 \in \mathbf{P}]$
* $a_1,\ a_2$ : 給定的餘數 (The prescribed residues) $[a_1, a_2 \in \mathbf{Z}]$
* $m_1^{-1}$ : $m_1$ 模 $m_2$ 的反元素 (The inverse of $m_1$ modulo $m_2$) $[m_1^{-1} \in \mathbf{P}]$
* $t$ : 修正量 (The correction term) $[t \in \left\{0, \dots, m_2 - 1\right\}]$
* $x,\ x_1,\ x_2,\ x'$ : 解 (Solutions) $[\mathbf{Z}]$
* 註：公式的想法是「**先滿足第一條，再用 $m_1$ 的倍數去調整第二條**」：$a_1 + m_1 t$ 不論 $t$ 是多少都滿足第一條，
  剩下的只是解一個關於 $t$ 的一次同餘式 $m_1 t \equiv a_2 - a_1 \pmod{m_2}$ —— 由 [模反元素](../Congruence/Modular_Inverse.md)【證明 (c)】直接得解。
* 註：投影片 p.38 的解法（令 $x = 4 + 7u$ 再解 $u$）與本檔 (a) 的公式是同一件事，只是沒有寫成公式。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [模反元素的存在性 (Existence of the modular inverse)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/Congruence/Modular_Inverse.html#b-proof-that-coprimality-gives-an-inverse)：** 已於本章 [模反元素](../Congruence/Modular_Inverse.md)【證明 (b)】完整證明，此處直接引用不再重證

  $$m_1 \perp m_2 \quad \Longrightarrow \quad m_1 \cdot m_1^{-1} \equiv 1 \pmod{m_2}$$

  * $m_1,\ m_2$ : 互質的正整數 (Coprime positive integers) $[m_1, m_2 \in \mathbf{P}]$
  * $m_1^{-1}$ : $m_1 \bmod m_2$ 的反元素 (The inverse of $m_1$ modulo $m_2$) $[m_1^{-1} \in \mathbf{P}]$

* **【已知 2】 [同餘的運算性質 (Arithmetic of congruences)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/Congruence/Congruence_Properties.html#e-proof-that-congruences-can-be-multiplied-together)：** 已於本章 [同餘的性質](../Congruence/Congruence_Properties.md)【證明 (a)(b)(c)】完整證明，此處直接引用不再重證

  * (a) 遞移性：

    $$u \equiv v,\ \ v \equiv w \quad \Longrightarrow \quad u \equiv w \pmod{m}$$

  * (b) 兩邊同加：

    $$u \equiv v \quad \Longrightarrow \quad u + c \equiv v + c \pmod{m}$$

  * (c) 兩邊同乘：

    $$u \equiv v \quad \Longrightarrow \quad uc \equiv vc \pmod{m}$$

  * $u,\ v,\ w,\ c$ : 任意整數 (Arbitrary integers) $[\mathbf{Z}]$
  * $m$ : 模數 (The modulus) $[m \in \mathbf{P}]$

* **【已知 3】 [同餘關係的刻畫 (Characterizations of congruence)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/Congruence/Congruence_Relation.html#c-proof-that-every-integer-is-congruent-to-its-remainder)：** 已於本章 [同餘關係](../Congruence/Congruence_Relation.md)【證明 (a)(b)(c)】完整證明，此處直接引用不再重證

  * (a) 整除刻畫：

    $$u \equiv v \pmod{m} \quad \Longleftrightarrow \quad m \mid \left(u - v\right)$$

  * (b) 與自己的餘數同餘：

    $$u \equiv \left(u \bmod m\right) \pmod{m}$$

  * $u,\ v$ : 任意整數 (Arbitrary integers) $[u, v \in \mathbf{Z}]$
  * $m$ : 模數 (The modulus) $[m \in \mathbf{P}]$

* **【已知 4】 [互質因數相乘仍整除 (Coprime divisors multiply)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/Factorization/Relatively_Prime.html#c-proof-that-coprime-divisors-multiply)：** 已於本章 [互質](../Factorization/Relatively_Prime.md)【證明 (c)】完整證明，此處直接引用不再重證

  $$m_1 \mid y,\ \ m_2 \mid y,\ \ m_1 \perp m_2 \quad \Longrightarrow \quad m_1 m_2 \mid y$$

  * $m_1,\ m_2$ : 互質的正整數 (Coprime positive integers) $[m_1, m_2 \in \mathbf{P}]$
  * $y$ : 被整除的整數 (The integer being divided) $[y \in \mathbf{Z}]$

* **【定義 1】 構造解 (The constructed solution)：** 投影片 p.39 的公式

  $$\begin{gather*}
  t &\overset{\text{def}}{=}& m_1^{-1}\left(a_2 - a_1\right) \bmod m_2 \\
  x &\overset{\text{def}}{=}& a_1 + m_1 t
  \end{gather*}$$

  * $t$ : 修正量 (The correction term) $[t \in \left\{0, \dots, m_2 - 1\right\}]$
  * $x$ : 構造出的解 (The constructed solution) $[x \in \mathbf{Z}]$
  * $a_1,\ a_2$ : 給定的餘數 (The prescribed residues) $[a_1, a_2 \in \mathbf{Z}]$
  * $m_1,\ m_2$ : 互質的模數 (Coprime moduli) $[m_1, m_2 \in \mathbf{P}]$
  * $m_1^{-1}$ : $m_1 \bmod m_2$ 的反元素 (The inverse of $m_1$ modulo $m_2$) $[m_1^{-1} \in \mathbf{P}]$

+++

## 證明:

### (a) proof that the constructed number solves both congruences

**第一條**：$x - a_1 = m_1 t$ 直接被 $m_1$ 整除：

$$\begin{gather*}
x - a_1 &\overset{\text{定義 1}}{=}& m_1 t \\
x &\overset{\text{已知 3(a)}}{\equiv}& a_1 \pmod{m_1}
\end{gather*}$$

**第二條**：在模 $m_2$ 下，$t$ 可以換回 $m_1^{-1}\left(a_2 - a_1\right)$，而 $m_1 m_1^{-1} \equiv 1$ 把 $m_1$ 消掉：

$$\begin{gather*}
t &\overset{\text{定義 1,已知 3(b)}}{\equiv}& m_1^{-1}\left(a_2 - a_1\right) \pmod{m_2} \\
m_1 t &\overset{\text{已知 2(c)}}{\equiv}& m_1 m_1^{-1}\left(a_2 - a_1\right) \pmod{m_2} \\
m_1 m_1^{-1}\left(a_2 - a_1\right) &\overset{\text{已知 1,已知 2(c)}}{\equiv}& a_2 - a_1 \pmod{m_2} \\
m_1 t &\overset{\text{已知 2(a)}}{\equiv}& a_2 - a_1 \pmod{m_2} \\
a_1 + m_1 t &\overset{\text{已知 2(b)}}{\equiv}& a_2 \pmod{m_2} \\
x &\overset{\text{定義 1}}{\equiv}& a_2 \pmod{m_2}
\end{gather*}$$

兩條都滿足，與投影片一致。

### (b) proof that any two solutions agree modulo the product

設 $x_1, x_2$ 都是解。兩者模 $m_1$ 都同餘於 $a_1$、模 $m_2$ 都同餘於 $a_2$：

$$\begin{gather*}
x_1 &\overset{\text{已知 2(a)}}{\equiv}& x_2 \pmod{m_1} \qquad \text{(都} \equiv a_1 \text{)} \\
m_1 &\overset{\text{已知 3(a)}}{\mid}& x_1 - x_2 \\
x_1 &\overset{\text{已知 2(a)}}{\equiv}& x_2 \pmod{m_2} \qquad \text{(都} \equiv a_2 \text{)} \\
m_2 &\overset{\text{已知 3(a)}}{\mid}& x_1 - x_2 \\
m_1 m_2 &\overset{\text{已知 4}}{\mid}& x_1 - x_2 \\
x_1 &\overset{\text{已知 3(a)}}{\equiv}& x_2 \pmod{m_1 m_2}
\end{gather*}$$

與投影片一致（投影片寫「since $m_1 \perp m_2$」，即【已知 4】）。

### (c) proof that the whole congruence class solves the system

設 $x' \equiv x \pmod{m_1 m_2}$，即 $x' - x = k m_1 m_2$。這個差同時是 $m_1$ 與 $m_2$ 的倍數：

$$\begin{gather*}
x' - x &\overset{\text{已知 3(a)}}{=}& k m_1 m_2 \\
x' &\overset{\text{已知 3(a)}}{\equiv}& x \pmod{m_1} \qquad \text{(} m_1 \mid k m_1 m_2 \text{)} \\
x' &\overset{\text{證明 (a),已知 2(a)}}{\equiv}& a_1 \pmod{m_1} \\
x' &\overset{\text{已知 3(a)}}{\equiv}& x \pmod{m_2} \qquad \text{(} m_2 \mid k m_1 m_2 \text{)} \\
x' &\overset{\text{證明 (a),已知 2(a)}}{\equiv}& a_2 \pmod{m_2}
\end{gather*}$$

所以解集恰好是 $x + m_1 m_2\mathbf{Z}$ 這一個同餘類：(b) 說解不會跑出這個類，(c) 說類裡每個數都是解。

### (d) verify the example of four modulo seven and three modulo five

取 $m_1 = 7$、$a_1 = 4$、$m_2 = 5$、$a_2 = 3$。先求 $7^{-1} \bmod 5$：$7 \times 3 = 21 = 4 \times 5 + 1$，故為 $3$。代入【定義 1】：

$$\begin{gather*}
7 \times 3 &\overset{\text{已知 3(a)}}{\equiv}& 1 \pmod{5} \\
t &\overset{\text{定義 1}}{=}& 3 \times \left(3 - 4\right) \bmod 5 \\
t &=& -3 \bmod 5 \\
t &=& 2 \\
x &\overset{\text{定義 1}}{=}& 4 + 7 \times 2 \\
x &=& 18
\end{gather*}$$

驗算與結論：

$$\begin{gather*}
18 - 4 &=& 2 \times 7 \\
18 &\overset{\text{已知 3(a)}}{\equiv}& 4 \pmod{7} \\
18 - 3 &=& 3 \times 5 \\
18 &\overset{\text{已知 3(a)}}{\equiv}& 3 \pmod{5} \\
x &\overset{\text{證明 (b)}}{\equiv}& 18 \pmod{35}
\end{gather*}$$

與投影片一致。

* 註：投影片的算法是令 $x = 4 + 7u$，代入第二條得 $7u \equiv 3 - 4 \pmod 5$，
  因 $7 \equiv 2$ 化為 $2u \equiv 4$，「兩邊除以 $2$」得 $u \equiv 2$。
  最後一步其實是乘以 $2^{-1} \equiv 3 \pmod 5$：$u \equiv 3 \times 4 = 12 \equiv 2$ —— 與本檔的 $t = 2$ 相同。
  「除以 $2$」能做，是因為 $\gcd(2, 5) = 1$（[同餘的性質](../Congruence/Congruence_Properties.md)【證明 (g)】）。
* 註：這也與 Abstract_Algebra 章 [中國剩餘定理](../../Abstract_Algebra/Ring/Chinese_Remainder_Theorem.md)【證明 (d)】
  用另一個公式 $r = a_1 e_2 + a_2 e_1$ 算出的「模 $5$ 餘 $3$、模 $7$ 餘 $4$ 得 $18$」一致。

+++

## 意義與密碼學關聯 (Interpretation and Relevance to Cryptography)

### 兩種重建公式

同一個問題有兩種常見公式：

| 公式 | 形式 | 特點 |
|---|---|---|
| 本檔（Garner 形式） | $x = a_1 + m_1 \cdot \left[m_1^{-1}\left(a_2 - a_1\right) \bmod m_2\right]$ | 只需**一個**反元素；中間量都不超過 $m_1 m_2$ |
| 高斯形式（[中國剩餘定理](Chinese_Remainder_Theorem.md)） | $x = \sum a_i M_i y_i \bmod M$ | 對稱、好推廣，但要 $k$ 個反元素 |

**RSA-CRT 的實作用的是本檔的形式**：私鑰檔裡存的 `iqmp` $= q^{-1} \bmod p$ 就是那一個預先算好的反元素。
解密時算出 $m_p = c^{d_p} \bmod p$、$m_q = c^{d_q} \bmod q$ 後：

$$m = m_q + q \cdot \left[q^{-1}\left(m_p - m_q\right) \bmod p\right]$$

這正是 (a) 取 $\left(m_1, a_1\right) = \left(q, m_q\right)$、$\left(m_2, a_2\right) = \left(p, m_p\right)$。

### 唯一性就是「資訊沒有遺失」

(b)(c) 說：知道 $x \bmod m_1$ 與 $x \bmod m_2$，就知道 $x \bmod m_1 m_2$，**不多也不少**。
兩個小座標攜帶的資訊量（$\log m_1 + \log m_2$ 位元）恰好等於大模數的資訊量（$\log m_1 m_2$ 位元）。

### 程式思維

```python
def crt2(a1, m1, a2, m2):
    """投影片 p.39 的公式（Garner 形式）。"""
    t = (pow(m1, -1, m2) * (a2 - a1)) % m2     # 定義 1
    return (a1 + m1 * t) % (m1 * m2)

x = crt2(4, 7, 3, 5)
assert x == 18 and x % 7 == 4 and x % 5 == 3   # 證明 (d)
assert pow(7, -1, 5) == 3
```
