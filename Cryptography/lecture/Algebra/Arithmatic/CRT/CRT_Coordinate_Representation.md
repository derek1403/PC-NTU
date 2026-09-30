# CRT Coordinate Representation (中國剩餘定理的座標表示)

+++

## 證明目標:

`Arithmetic.pdf` p.35–37。用兩個小模數的餘數當「座標」來表示一個大模數的元素。
兩個對照例子說明：**模數互質時座標是一對一的，不互質時會撞號**。

* (a) $N = 15 = 3 \times 5$：$a \mapsto \left(a \bmod 3,\ a \bmod 5\right)$ 是 $\mathbf{Z}_{15}$ 到 $\mathbf{Z}_3 \times \mathbf{Z}_5$ 的**雙射**，並驗證投影片的座標表。
* (b) $N = 24 = 4 \times 6$：$a$ 與 $a + 12$ 的座標**相同**，無法唯一還原。
* (c)(d) 投影片的 Remark（兩個方向）：

$$\mathbf{Z}_{m_1 m_2} \cong \mathbf{Z}_{m_1} \times \mathbf{Z}_{m_2} \quad \Longleftrightarrow \quad \gcd\left(m_1, m_2\right) = 1$$

* $N$ : 大模數 (The large modulus) $[N \in \mathbf{P}]$
* $m_1,\ m_2$ : 兩個小模數 (The two small moduli) $[m_1, m_2 \in \mathbf{P}]$
* $a$ : $\mathbf{Z}_N$ 的元素 (An element of $\mathbf{Z}_N$) $[a \in \left\{0, \dots, N-1\right\}]$
* $\left(a_1, a_2\right)$ : $a$ 的座標 (The coordinates of $a$) $[a_i \in \mathbf{Z}_{m_i}]$
* $\cong$ : 環同構 (Ring isomorphism) $[\text{關係}]$
* 註：投影片的 Remark 寫「$\mathbf{Z}_N \cong \mathbf{Z}_{m_1} \times \mathbf{Z}_{m_2}$ iff $\gcd(m_1, m_2) = 1$」，但**沒有證明**。
  (⇐) 方向就是 Abstract_Algebra 章已證的 [中國剩餘定理](../../Abstract_Algebra/Ring/Chinese_Remainder_Theorem.md)，本檔直接引用；
  (⇒) 方向（不互質就不同構，不只是「這個映射」不行，而是**任何**映射都不行）本檔補證。
* 註：投影片 p.37 最後問「給定座標 $\left(a_1, a_2\right)$，如何算回 $a$？」答案見下一檔 [兩個模數的中國剩餘定理](Two_Moduli_CRT.md)。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [互質因數相乘仍整除 (Coprime divisors multiply)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/Factorization/Relatively_Prime.html#c-proof-that-coprime-divisors-multiply)：** 已於本章 [互質](../Factorization/Relatively_Prime.md)【證明 (c)】完整證明，此處直接引用不再重證

  $$m_1 \mid x,\ \ m_2 \mid x,\ \ m_1 \perp m_2 \quad \Longrightarrow \quad m_1 m_2 \mid x$$

  * $m_1,\ m_2$ : 互質的因數 (Coprime divisors) $[m_1, m_2 \in \mathbf{P}]$
  * $x$ : 被整除的整數 (The integer being divided) $[x \in \mathbf{Z}]$

* **【已知 2】 [同餘與整除 (Congruence and divisibility)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/Congruence/Congruence_Relation.html#b-proof-that-a-difference-divisible-by-the-modulus-gives-equal-remainders)：** 已於本章 [同餘關係](../Congruence/Congruence_Relation.md)【定義 1】【證明 (a)(b)】給出並證明，此處直接引用不再重證

  $$u \bmod m = v \bmod m \quad \Longleftrightarrow \quad m \mid \left(u - v\right)$$

  * $u,\ v$ : 任意整數 (Arbitrary integers) $[u, v \in \mathbf{Z}]$
  * $m$ : 模數 (The modulus) $[m \in \mathbf{P}]$

* **【已知 3】 [整除的大小界 (Size bound for divisors)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/GCD/Divisibility_Basics.html#e-proof-that-a-divisor-of-a-nonzero-integer-is-no-larger-in-absolute-value)：** 已於本章 [整除的基本性質](../GCD/Divisibility_Basics.md)【證明 (a)(e)】完整證明，此處直接引用不再重證

  * (a) 大小界：

    $$d \mid x,\ \ x \neq 0 \quad \Longrightarrow \quad \left|d\right| \le \left|x\right|$$

  * (b) 整除倍數：

    $$d \mid x \quad \Longrightarrow \quad d \mid xy$$

  * $d,\ x,\ y$ : 任意整數 (Arbitrary integers) $[d, x, y \in \mathbf{Z}]$

* **【已知 4】 [中國剩餘定理（環論版） (Chinese remainder theorem, ring version)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Ring/Chinese_Remainder_Theorem.html#c-proof-of-surjectivity-and-the-isomorphism)：** 已於 Abstract_Algebra 章 [中國剩餘定理](../../Abstract_Algebra/Ring/Chinese_Remainder_Theorem.md)【證明 (c)】完整證明，此處取 $R = \mathbf{Z}$ 直接引用不再重證

  $$m_1\mathbf{Z} + m_2\mathbf{Z} = \mathbf{Z} \quad \Longrightarrow \quad \mathbf{Z} \big/ \left(m_1\mathbf{Z} \cap m_2\mathbf{Z}\right) \cong \mathbf{Z}/m_1\mathbf{Z} \times \mathbf{Z}/m_2\mathbf{Z}$$

  * $m_1\mathbf{Z},\ m_2\mathbf{Z}$ : 兩個主理想 (Two principal ideals) $[m_i\mathbf{Z} \trianglelefteq \mathbf{Z}]$

* **【已知 5】 [理想的交與和 (Intersection and sum of ideals in the integers)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Ring/Ideal.html#f-verify-the-numerical-examples-of-intersections-and-sums)：** 已於 Abstract_Algebra 章 [理想](../../Abstract_Algebra/Ring/Ideal.md)【已知 5】【證明 (f)】引用並驗證，此處再次引用

  $$m_1\mathbf{Z} \cap m_2\mathbf{Z} = \mathrm{lcm}\left(m_1, m_2\right)\mathbf{Z}, \qquad m_1\mathbf{Z} + m_2\mathbf{Z} = \gcd\left(m_1, m_2\right)\mathbf{Z}$$

  * $m_1,\ m_2$ : 正整數 (Positive integers) $[m_1, m_2 \in \mathbf{P}]$

* **【已知 6】 [gcd 與 lcm 的乘積公式 (Product formula of gcd and lcm)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/Factorization/Least_Common_Multiple.html#d-proof-of-the-product-formula)：** 已於本章 [最小公倍數](../Factorization/Least_Common_Multiple.md)【證明 (d)】完整證明，此處直接引用不再重證

  $$m_1 m_2 = \gcd\left(m_1, m_2\right) \times \mathrm{lcm}\left(m_1, m_2\right)$$

  * $m_1,\ m_2$ : 正整數 (Positive integers) $[m_1, m_2 \in \mathbf{P}]$

* **【已知 7】 [$\mathbf{Z}/n\mathbf{Z} \cong \mathbf{Z}_n$ 與環同構 (Residue rings and ring isomorphisms)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Ring/Quotient_Ring.html#e-proof-that-the-integers-modulo-the-multiples-of-n-form-the-ring-of-residues)：** 已於 Abstract_Algebra 章 [商環](../../Abstract_Algebra/Ring/Quotient_Ring.md)【證明 (e)】與 [環同態與核](../../Abstract_Algebra/Ring/Ring_Homomorphism_and_Kernel.md)【定義 1】【定義 3】給出並證明，此處直接引用不再重證

  * (a) 商環就是剩餘類環：

    $$\mathbf{Z}/n\mathbf{Z} \cong \mathbf{Z}_n$$

  * (b) 環同構是保持加法與乘法的雙射：

    $$f \ \text{為同構} \quad \Longleftrightarrow \quad f \ \text{雙射},\ \ f(u + v) = f(u) + f(v),\ \ f(uv) = f(u) f(v)$$

  * $n$ : 模數 (The modulus) $[n \in \mathbf{P}]$
  * $f$ : 兩環之間的映射 (A map between two rings) $[R \to S]$
  * $u,\ v$ : 環元素 (Ring elements) $[u, v \in R]$

* **【推導 1】 保持加法的映射與整數倍交換 (An additive map commutes with integer multiples)：** 【證明 (d)】要用。
  把 $L \cdot u = u + u + \cdots + u$（$L$ 項）逐項拆開

  $$\begin{gather*}
  f\left(L \cdot u\right) &=& f\left(u + u + \cdots + u\right) \\
  f\left(L \cdot u\right) &\overset{\text{已知 7(b)}}{=}& f(u) + f(u) + \cdots + f(u) \\
  f\left(L \cdot u\right) &=& L \cdot f(u)
  \end{gather*}$$

  * $f$ : 保持加法的映射 (An additive map) $[R \to S]$
  * $u$ : 環元素 (A ring element) $[u \in R]$
  * $L$ : 正整數 (A positive integer) $[L \in \mathbf{P}]$
  * $L \cdot u$ : $u$ 自加 $L$ 次 ($u$ added to itself $L$ times) $[L \cdot u \in R]$

+++

## 證明:

### (a) verify the bijective coordinates modulo fifteen

**單射**：設 $a, a' \in \left\{0, \dots, 14\right\}$ 座標相同。則 $3$ 與 $5$ 都整除差，而 $3 \perp 5$，故 $15$ 整除差；差的絕對值小於 $15$，只能是 $0$：

$$\begin{gather*}
a \bmod 3 = a' \bmod 3 &\overset{\text{已知 2}}{\Longrightarrow}& 3 \mid a - a' \\
a \bmod 5 = a' \bmod 5 &\overset{\text{已知 2}}{\Longrightarrow}& 5 \mid a - a' \\
15 &\overset{\text{已知 1}}{\mid}& a - a' \qquad \text{(} \gcd(3, 5) = 1 \text{)} \\
\left|a - a'\right| &<& 15 \\
a - a' &\overset{\text{已知 3(a)}}{=}& 0 \qquad \text{(否則 } 15 \le \left|a - a'\right| \text{)}
\end{gather*}$$

**滿射**：$15$ 個相異的元素對應到 $15$ 個相異的座標，而座標總共只有 $3 \times 5 = 15$ 種，所以每一種都被用到。
這就是投影片的「All elements in $\mathbf{Z}_N$ have different coordinates」。

**座標表**（列 $= a \bmod 3$、行 $= a \bmod 5$，格內 $= a$），與投影片 p.35 一致（全部 $15$ 格已用文末程式核對）：

| | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| **0** | 0 | 6 | 12 | 3 | 9 |
| **1** | 10 | 1 | 7 | 13 | 4 |
| **2** | 5 | 11 | 2 | 8 | 14 |

例如 $13$：$13 = 4 \times 3 + 1$、$13 = 2 \times 5 + 3$，座標 $\left(1, 3\right)$，落在第 $1$ 列第 $3$ 行。

### (b) verify the colliding coordinates modulo twenty-four

$12$ 同時是 $4$ 與 $6$ 的倍數，所以加上 $12$ 不改變任何一個餘數：

$$\begin{gather*}
4 &\mid& 12 \\
\left(a + 12\right) \bmod 4 &\overset{\text{已知 2}}{=}& a \bmod 4 \\
6 &\mid& 12 \\
\left(a + 12\right) \bmod 6 &\overset{\text{已知 2}}{=}& a \bmod 6
\end{gather*}$$

$\mathbf{Z}_{24}$ 的 $24$ 個元素兩兩撞在一起，只用到 $4 \times 6 = 24$ 種座標中的 $12$ 種（兩個座標奇偶相同的那些）。
投影片的表格裡每格寫著兩個數（如 $0/12$、$1/13$），另一半的格子是空的，與此一致。

### (c) proof (⇐) that coprime moduli give an isomorphism

設 $\gcd(m_1, m_2) = 1$。先確認兩個理想互質、交集是 $m_1 m_2\mathbf{Z}$，再代入環論版的 CRT：

$$\begin{gather*}
m_1\mathbf{Z} + m_2\mathbf{Z} &\overset{\text{已知 5}}{=}& \gcd\left(m_1, m_2\right)\mathbf{Z} \\
m_1\mathbf{Z} + m_2\mathbf{Z} &=& \mathbf{Z} \\
\mathrm{lcm}\left(m_1, m_2\right) &\overset{\text{已知 6}}{=}& m_1 m_2 \qquad \text{(} \gcd = 1 \text{)} \\
m_1\mathbf{Z} \cap m_2\mathbf{Z} &\overset{\text{已知 5}}{=}& m_1 m_2 \mathbf{Z} \\
\mathbf{Z}/m_1 m_2\mathbf{Z} &\overset{\text{已知 4}}{\cong}& \mathbf{Z}/m_1\mathbf{Z} \times \mathbf{Z}/m_2\mathbf{Z} \\
\mathbf{Z}_{m_1 m_2} &\overset{\text{已知 7(a)}}{\cong}& \mathbf{Z}_{m_1} \times \mathbf{Z}_{m_2}
\end{gather*}$$

### (d) proof (⇒) that non-coprime moduli give no isomorphism

證逆否命題：設 $g = \gcd(m_1, m_2) > 1$，證明**不存在任何**同構 $f : \mathbf{Z}_{m_1 m_2} \to \mathbf{Z}_{m_1} \times \mathbf{Z}_{m_2}$。

取 $L = m_1 m_2 / g$。它是 $m_1$ 與 $m_2$ 的公倍數，又嚴格小於 $N = m_1 m_2$：

$$\begin{gather*}
L &\overset{\text{let}}{=}& \frac{m_1 m_2}{g} \\
L &=& m_1 \cdot \frac{m_2}{g} \qquad \text{(故 } m_1 \mid L \text{)} \\
L &=& m_2 \cdot \frac{m_1}{g} \qquad \text{(故 } m_2 \mid L \text{)} \\
0 &<& L \\
L &<& m_1 m_2 \qquad \text{(} g > 1 \text{)}
\end{gather*}$$

**右邊每個元素乘 $L$ 都變 $0$**，**左邊的 $1$ 乘 $L$ 卻不是 $0$**：

$$\begin{gather*}
L \cdot \left(x, y\right) &=& \left(Lx \bmod m_1,\ Ly \bmod m_2\right) \\
L \cdot \left(x, y\right) &\overset{\text{已知 3(b)}}{=}& \left(0, 0\right) \qquad \text{(} m_1 \mid Lx,\ m_2 \mid Ly \text{)} \\
L \cdot 1 &=& L \bmod m_1 m_2 \qquad \text{(於 } \mathbf{Z}_{m_1 m_2} \text{)} \\
L \cdot 1 &=& L \qquad \text{(} 0 < L < m_1 m_2 \text{)} \\
L &\neq& 0
\end{gather*}$$

若 $f$ 是同構，則 $f(L \cdot 1)$ 與 $f(0)$ 都等於 $\left(0,0\right)$，與單射矛盾：

$$\begin{gather*}
f\left(L \cdot 1\right) &\overset{\text{推導 1}}{=}& L \cdot f(1) \\
f\left(L \cdot 1\right) &=& \left(0, 0\right) \\
f(0) &=& \left(0, 0\right) \qquad \text{(同態把 } 0 \text{ 送到 } 0 \text{)} \\
L \cdot 1 &\overset{\text{已知 7(b)}}{=}& 0 \qquad \text{(單射)}
\end{gather*}$$

最後一行與 $L \cdot 1 \neq 0$ 矛盾。故 $\gcd(m_1, m_2) > 1$ 時不同構。(c)(d) 合起來即投影片的 Remark。

* 註：以 $N = 24 = 4 \times 6$ 為例，$g = 2$、$L = 12$：右邊每個元素乘 $12$ 都是 $\left(0,0\right)$，
  但 $\mathbf{Z}_{24}$ 的 $1$ 乘 $12$ 是 $12 \neq 0$。這正是 (b) 的「$a$ 與 $a + 12$ 撞號」的抽象版本。

+++

## 意義與密碼學關聯 (Interpretation and Relevance to Cryptography)

### 座標化 = 把一個大問題拆成兩個小問題

$\mathbf{Z}_{15}$ 的每個元素都可以寫成 $\left(a \bmod 3,\ a \bmod 5\right)$ 這組座標，而且：

* **正向**（求座標）很容易：兩次取模；
* **加法、乘法可以逐座標做**：$\left(a+b\right) \bmod 3$ 只依賴 $a \bmod 3$ 與 $b \bmod 3$（[同餘的性質](../Congruence/Congruence_Properties.md)）。

所以在 $\mathbf{Z}_{15}$ 裡算，等於在 $\mathbf{Z}_3$ 與 $\mathbf{Z}_5$ 裡**平行地**各算一次。
投影片 p.37 的「computation modulo $N$ can be replaced by modulo $m_1$ and modulo $m_2$」就是這個意思。

### RSA-CRT 與互質條件

RSA 的 $n = pq$ 中 $p \neq q$ 是相異質數，自動互質，所以 $\mathbf{Z}_n \cong \mathbf{Z}_p \times \mathbf{Z}_q$，
解密可以拆成模 $p$ 與模 $q$ 兩半做，快約四倍（見 Abstract_Algebra 章 [中國剩餘定理](../../Abstract_Algebra/Ring/Chinese_Remainder_Theorem.md) 文末）。

若有人誤用 $p = q$（$n = p^2$），(d) 告訴我們座標化會壞掉，而且 $\varphi(n) = p(p-1)$ 的公式也不同 —— 實作會直接算錯。

### 程式思維

```python
coords15 = {a: (a % 3, a % 5) for a in range(15)}
assert len(set(coords15.values())) == 15                   # 證明 (a)：雙射
assert coords15[13] == (1, 3) and coords15[6] == (0, 1)
coords24 = {a: (a % 4, a % 6) for a in range(24)}
assert all(coords24[a] == coords24[a + 12] for a in range(12))   # 證明 (b)
assert len(set(coords24.values())) == 12                   # 只用到一半的座標
```
