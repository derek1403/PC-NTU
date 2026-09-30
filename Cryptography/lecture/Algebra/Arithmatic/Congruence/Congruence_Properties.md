# Congruence Properties (同餘的性質)

+++

## 證明目標:

`Arithmetic.pdf` p.28–29。同餘「像等號一樣好用」的全部理由 —— 可以兩邊同加、同乘、同取冪；
但**不能隨便兩邊同除**，除法需要互質條件。投影片列了八條，只證了 5) 與 7)。本檔全部補齊。

設 $a, b, c \in \mathbf{Z}$、$m, d \in \mathbf{P}$。

* (a) 等價關係（投影片 1) 2) 6)）：

$$a \equiv a, \qquad a \equiv b \Rightarrow b \equiv a, \qquad a \equiv b,\ b \equiv c \Rightarrow a \equiv c \pmod{m}$$

* (b)(c)(d) 若 $a \equiv b \pmod m$，則（投影片 3) 4) 5)）：

$$a + c \equiv b + c, \qquad ac \equiv bc, \qquad a^d \equiv b^d \pmod{m}$$

* (e) 同餘式相乘（投影片未列，本章補；後面算冪次時一直要用）：

$$a \equiv b,\ \ c \equiv e \pmod{m} \quad \Longrightarrow \quad ac \equiv be \pmod{m}$$

* (f) 帶 gcd 的消去律（投影片 7)）：設 $g = \gcd(a, m)$，

$$ab \equiv ac \pmod{m} \quad \Longrightarrow \quad b \equiv c \pmod{m/g}$$

* (g) 互質消去律（投影片 8)）：

$$a \perp m,\ \ ab \equiv ac \pmod{m} \quad \Longrightarrow \quad b \equiv c \pmod{m}$$

* (h) 驗證投影片的例子：

$$6 \times 2 \equiv 6 \times 7 \pmod{15} \quad \Longrightarrow \quad 2 \equiv 7 \pmod{5}, \ \text{ 但 } \ 2 \not\equiv 7 \pmod{15}$$

* $a,\ b,\ c,\ e$ : 任意整數 (Arbitrary integers) $[a, b, c, e \in \mathbf{Z}]$
* $m$ : 模數 (The modulus) $[m \in \mathbf{P}]$
* $d$ : 指數 (An exponent) $[d \in \mathbf{P}]$
* $g$ : $a$ 與 $m$ 的最大公因數 (The gcd of $a$ and $m$) $[g \in \mathbf{P}]$
* 註：投影片 7) 把 gcd 記作 $d$，與 5) 的指數 $d$ **撞名**。本檔把 7) 的 gcd 改記為 $g$，數學內容不變。
* 註：(f) 的結論是**模 $m/g$**，不是模 $m$。除掉 $a$ 的同時，模數也要除掉 $a$ 與 $m$ 的公因數 ——
  這是模運算裡最常見的錯誤來源。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [同餘的整除刻畫 (Congruence as divisibility)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/Congruence/Congruence_Relation.html#b-proof-that-a-difference-divisible-by-the-modulus-gives-equal-remainders)：** 已於本章 [同餘關係](Congruence_Relation.md)【證明 (a)(b)】完整證明，此處直接引用不再重證

  $$a \equiv b \pmod{m} \quad \Longleftrightarrow \quad m \mid \left(a - b\right)$$

  * $a,\ b$ : 任意整數 (Arbitrary integers) $[a, b \in \mathbf{Z}]$
  * $m$ : 模數 (The modulus) $[m \in \mathbf{P}]$

* **【已知 2】 [模理想的同餘是等價關係 (Congruence modulo an ideal is an equivalence relation)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Ring/Congruence_Class_Modulo_Ideal.html#a-proof-that-congruence-modulo-an-ideal-is-an-equivalence-relation)：** 已於 Abstract_Algebra 章 [模理想的同餘類](../../Abstract_Algebra/Ring/Congruence_Class_Modulo_Ideal.md)【證明 (a)(c)】完整證明（取 $R = \mathbf{Z}$、$I = m\mathbf{Z}$），此處直接引用不再重證

  $$m \mid (a - a), \qquad m \mid (a - b) \Rightarrow m \mid (b - a), \qquad m \mid (a - b),\ m \mid (b - c) \Rightarrow m \mid (a - c)$$

  * $a,\ b,\ c$ : 任意整數 (Arbitrary integers) $[a, b, c \in \mathbf{Z}]$
  * $m$ : 模數 (The modulus) $[m \in \mathbf{P}]$

* **【已知 3】 [整除的基本性質 (Divisibility basics)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/GCD/Divisibility_Basics.html#a-proof-that-a-common-divisor-divides-every-linear-combination)：** 已於本章 [整除的基本性質](../GCD/Divisibility_Basics.md)【證明 (a)(e)】完整證明，此處直接引用不再重證

  * (a) 線性組合：

    $$m \mid x,\ \ m \mid y \quad \Longrightarrow \quad m \mid \left(xu + yv\right)$$

  * (b) 大小界：

    $$m \mid x,\ \ x \neq 0 \quad \Longrightarrow \quad \left|m\right| \le \left|x\right|$$

  * $m,\ x,\ y,\ u,\ v$ : 任意整數 (Arbitrary integers) $[\mathbf{Z}]$

* **【已知 4】 [貝祖係數與 gcd 的整除性 (Bézout coefficients and divisibility by the gcd)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/GCD/Extended_Euclidean_Algorithm.html#c-proof-of-the-existence-of-bezout-coefficients)：** 已於本章 [擴展歐幾里得演算法](../GCD/Extended_Euclidean_Algorithm.md)【證明 (c)】與 [最大公因數](../GCD/Greatest_Common_Divisor.md)【定義 2】給出並證明，此處直接引用不再重證

  $$g = \gcd(a, m) = ax + my \ \text{ for some } x, y \in \mathbf{Z}, \qquad g \mid a, \quad g \mid m$$

  * $g$ : 最大公因數 (The gcd) $[g \in \mathbf{P}]$
  * $a$ : 任意整數 (An arbitrary integer) $[a \in \mathbf{Z}]$
  * $m$ : 模數 (The modulus) $[m \in \mathbf{P}]$
  * $x,\ y$ : 貝祖係數 (Bézout coefficients) $[x, y \in \mathbf{Z}]$

* **【推導 1】 冪次差的因式分解 (Factorization of a difference of powers)：** 【證明 (d)】要用。展開後相鄰項兩兩抵消（望遠鏡求和）

  $$\begin{gather*}
  \left(a - b\right)\sum_{j=0}^{d-1} a^{d-1-j} b^{j} &=& \sum_{j=0}^{d-1} a^{d-j} b^{j} - \sum_{j=0}^{d-1} a^{d-1-j} b^{j+1} \\
  \left(a - b\right)\sum_{j=0}^{d-1} a^{d-1-j} b^{j} &=& \sum_{j=0}^{d-1} a^{d-j} b^{j} - \sum_{j=1}^{d} a^{d-j} b^{j} \\
  \left(a - b\right)\sum_{j=0}^{d-1} a^{d-1-j} b^{j} &=& a^{d} - b^{d}
  \end{gather*}$$

  * $a,\ b$ : 任意整數 (Arbitrary integers) $[a, b \in \mathbf{Z}]$
  * $d$ : 指數 (An exponent) $[d \in \mathbf{P}]$
  * $j$ : 求和指標 (Summation index) $[j \in \left\{0, \dots, d-1\right\}]$
  * 註：第二列把第二個和的指標平移 $j \to j - 1$；兩個和只剩第一個的 $j = 0$ 項 $a^d$ 與第二個的 $j = d$ 項 $b^d$。
    這就是投影片 p.29 的 $\left(a - b\right)\left(a^{d-1} + a^{d-2}b + \cdots + b^{d-1}\right) = a^d - b^d$。

+++

## 證明:

### (a) proof that congruence is an equivalence relation

由【已知 1】，模 $m$ 同餘就是 $m \mid$ 差，而【已知 2】已證這三條：

$$\begin{gather*}
m &\overset{\text{已知 2}}{\mid}& a - a \\
a &\overset{\text{已知 1}}{\equiv}& a \pmod{m} \\
a \equiv b \pmod{m} &\overset{\text{已知 1,已知 2}}{\Longrightarrow}& b \equiv a \pmod{m} \\
a \equiv b,\ \ b \equiv c \pmod{m} &\overset{\text{已知 1,已知 2}}{\Longrightarrow}& a \equiv c \pmod{m}
\end{gather*}$$

（本章的同餘定義是「餘數相同」，這三條其實也可以直接從「等號是等價關係」讀出來；兩種看法一致。）

### (b) proof that congruence is preserved by addition

$$\begin{gather*}
\left(a + c\right) - \left(b + c\right) &=& a - b \\
m &\overset{\text{已知 1}}{\mid}& a - b \\
a + c &\overset{\text{已知 1}}{\equiv}& b + c \pmod{m}
\end{gather*}$$

### (c) proof that congruence is preserved by multiplication

$$\begin{gather*}
ac - bc &=& \left(a - b\right) c \\
m &\overset{\text{已知 1}}{\mid}& a - b \\
m &\overset{\text{已知 3(a)}}{\mid}& \left(a - b\right) c \\
ac &\overset{\text{已知 1}}{\equiv}& bc \pmod{m}
\end{gather*}$$

### (d) proof that congruence is preserved by powers

$a^d - b^d$ 有因子 $a - b$，而 $m$ 整除 $a - b$：

$$\begin{gather*}
a^d - b^d &\overset{\text{推導 1}}{=}& \left(a - b\right)\sum_{j=0}^{d-1} a^{d-1-j} b^{j} \\
m &\overset{\text{已知 1}}{\mid}& a - b \\
m &\overset{\text{已知 3(a)}}{\mid}& a^d - b^d \\
a^d &\overset{\text{已知 1}}{\equiv}& b^d \pmod{m}
\end{gather*}$$

與投影片 p.29 的 5) 一致。

### (e) proof that congruences can be multiplied together

先乘 $c$，再乘 $b$，最後用遞移性接起來：

$$\begin{gather*}
ac &\overset{\text{證明 (c)}}{\equiv}& bc \pmod{m} \qquad \text{(} a \equiv b \text{)} \\
bc &\overset{\text{證明 (c)}}{\equiv}& be \pmod{m} \qquad \text{(} c \equiv e \text{)} \\
ac &\overset{\text{證明 (a)}}{\equiv}& be \pmod{m}
\end{gather*}$$

### (f) proof of cancellation with the gcd

依投影片 p.29 的 7)。把 $g = ax + my$ 兩邊除以 $g$，得到一組「湊出 $1$」；乘上 $b - c$ 後兩項都被 $m/g$ 整除：

$$\begin{gather*}
g &\overset{\text{已知 4}}{=}& ax + my \\
1 &=& \frac{a}{g} x + \frac{m}{g} y \qquad \text{(} \tfrac{a}{g}, \tfrac{m}{g} \in \mathbf{Z} \text{)} \\
b - c &=& \frac{a}{g}\left(b - c\right) x + \frac{m}{g}\left(b - c\right) y \\
a\left(b - c\right) &\overset{\text{已知 1}}{=}& m k \qquad \text{for some } k \in \mathbf{Z} \\
\frac{a}{g}\left(b - c\right) &=& \frac{m}{g}\, k \\
\frac{m}{g} &\overset{\text{已知 3(a)}}{\mid}& \frac{a}{g}\left(b - c\right) x + \frac{m}{g}\left(b - c\right) y \\
\frac{m}{g} &\mid& b - c \\
b &\overset{\text{已知 1}}{\equiv}& c \pmod{m/g}
\end{gather*}$$

與投影片一致。

### (g) proof of cancellation for a coprime factor

$a \perp m$ 即 $g = 1$，套 (f)，模數 $m/1 = m$ 不變：

$$\begin{gather*}
b &\overset{\text{證明 (f)}}{\equiv}& c \pmod{m/1} \\
b &\equiv& c \pmod{m}
\end{gather*}$$

### (h) verify the example from the slides

**前提**：$6 \times 2 \equiv 6 \times 7 \pmod{15}$。

$$\begin{gather*}
6 \times 7 - 6 \times 2 &=& 30 \\
30 &=& 15 \times 2 \\
6 \times 2 &\overset{\text{已知 1}}{\equiv}& 6 \times 7 \pmod{15}
\end{gather*}$$

**套 (f)**：$g = \gcd(6, 15) = 3$，$15/3 = 5$：

$$\begin{gather*}
2 &\overset{\text{證明 (f)}}{\equiv}& 7 \pmod{5} \\
7 - 2 &=& 5 \times 1
\end{gather*}$$

**模 $15$ 不成立**：$7 - 2 = 5$ 非零且比 $15$ 小，不可能被 $15$ 整除：

$$\begin{gather*}
15 &\overset{\text{已知 3(b)}}{\nmid}& 5 \qquad \text{(否則 } 15 \le 5 \text{)} \\
2 &\overset{\text{已知 1}}{\not\equiv}& 7 \pmod{15}
\end{gather*}$$

與投影片「$2 \equiv 7 \pmod 5$, not $\pmod{15}$」一致。

+++

## 意義與密碼學關聯 (Interpretation and Relevance to Cryptography)

### 為什麼可以「先取模再算」

(b)(c)(e) 合起來說：**加法與乘法可以在任何時候先取模**。
這讓 $\mathbf{Z}_m$ 上的運算良定義 —— 在 Abstract_Algebra 章，這件事的正式說法是
[商環](../../Abstract_Algebra/Ring/Quotient_Ring.md)【證明 (a)(b)】的「運算與代表元的選取無關」。

(d) 則讓大指數冪可以一步一步縮小：計算 $11^{2006} \bmod 21$ 時可以先把 $11^{12}$ 換成 $1$
（見 [尤拉定理](../Fermat_Euler/Euler_Theorem.md)）。

### 除法是危險的

(f) 是密碼學實作中經典的陷阱：在 $\mathbf{Z}_m$ 裡想「兩邊除以 $a$」，
只有在 $\gcd(a, m) = 1$ 時才安全（(g)）。否則答案只在較小的模數 $m/g$ 下唯一，
在原本的模 $m$ 下有 $g$ 個可能的解。

對 RSA 而言，$\gcd(a, n) > 1$ 的 $a$ 等於找到了 $n$ 的一個因數 ——
**碰到不能除的數，就是分解了 $n$**。這也是 Abstract_Algebra 章 [零因子](../../Abstract_Algebra/Ring/Zero_Divisor.md) 文末那句話的初等版本。

### 程式思維

```python
from math import gcd
m = 15
for a in range(-20, 21):
    for b in range(-20, 21):
        for c in range(-20, 21):
            if (a*b - a*c) % m == 0:                  # ab ≡ ac (mod m)
                g = gcd(a, m) if a else m
                assert (b - c) % (m // g) == 0         # 證明 (f)
assert (6*2 - 6*7) % 15 == 0 and (2 - 7) % 5 == 0 and (2 - 7) % 15 != 0   # 證明 (h)
```
