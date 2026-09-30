# Stein Binary GCD (Stein 二進位 GCD 演算法)

+++

## 證明目標:

`Arithmetic.pdf` p.19–20。歐幾里得演算法每一步要做一次**除法**；Stein 演算法只用**減法與除以 $2$**。
在二進位電腦上，除以 $2$ 就是右移一位，幾乎不花時間。它的正確性建立在三條「看最低位元」的性質上。

* (a) $a, b$ 皆偶（不全為零）：

$$\gcd(a, b) = 2 \gcd\left(\frac{a}{2}, \frac{b}{2}\right)$$

* (b) $a$ 偶、$b$ 奇：

$$\gcd(a, b) = \gcd\left(\frac{a}{2}, b\right)$$

* (c) $a, b$ 皆奇（Stein 遞迴）：

$$\gcd(a, b) = \gcd\left(\frac{a - b}{2}, b\right)$$

* (d) 驗證投影片 p.20 的例子：

$$\gcd(325, 234) = 13$$

* $a,\ b$ : 不全為零的整數 (Integers, not both zero) $[a, b \in \mathbf{Z}]$
* 註：投影片**只證了 (c)**（而且是引用 (b)），(a)(b) 沒有證明。本檔補上：
  (a) 用 [貝祖等式](Bezout_Identity.md) 的「最小正組合」刻畫最乾淨；
  (b) 用公因數集合相等 + 一個奇偶性引理（【推導 1】）。
* 註：(a) 需要 $a, b$ **不全為零**（$\gcd(0,0)$ 無定義）。(b)(c) 因為 $b$ 是奇數，自動不全為零。
* 註：(c) 裡的 $\left(a - b\right)/2$ 可能是負數或零，這不影響結論（gcd 對正負號不敏感）。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [貝祖等式：gcd 是最小正組合 (The gcd is the smallest positive combination)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/GCD/Bezout_Identity.html#a-proof-that-the-gcd-is-the-smallest-positive-combination)：** 已於本章 [貝祖等式](Bezout_Identity.md)【證明 (a)】完整證明，此處直接引用不再重證

  $$\gcd(a, b) = \min\left\{ax + by \ \middle|\ x, y \in \mathbf{Z},\ ax + by > 0\right\}$$

  * $a,\ b$ : 不全為零的整數 (Integers, not both zero) $[a, b \in \mathbf{Z}]$
  * $x,\ y$ : 組合係數 (Combination coefficients) $[x, y \in \mathbf{Z}]$

* **【已知 2】 [GCD 的平移不變性 (Shift invariance of the gcd)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/GCD/GCD_Shift_Invariance.html#c-proof-of-the-shift-invariance-theorem)：** 已於本章 [GCD 的平移不變性](GCD_Shift_Invariance.md)【證明 (c)】完整證明，此處直接引用不再重證

  $$\gcd(a, b) = \gcd(a + kb,\ b) \qquad \text{for all } k \in \mathbf{Z}$$

  * $a,\ b$ : 不全為零的整數 (Integers, not both zero) $[a, b \in \mathbf{Z}]$
  * $k$ : 任意整數 (An arbitrary integer) $[k \in \mathbf{Z}]$

* **【已知 3】 [最大公因數的定義與基本命題 (Definition and basic propositions of the gcd)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/GCD/Greatest_Common_Divisor.html#d-proof-that-the-gcd-ignores-signs-and-order)：** 已於本章 [最大公因數](Greatest_Common_Divisor.md)【定義 1】【定義 2】【證明 (c)(d)】給出並證明，此處直接引用不再重證

  * (a) 公因數集合決定 gcd：

    $$\mathrm{CD}(a, b) = \left\{d \neq 0 \ \middle|\ d \mid a,\ d \mid b\right\}, \qquad \gcd(a, b) = \max\ \mathrm{CD}(a, b)$$

  * (b) 對稱性：

    $$\gcd(a, b) = \gcd(b, a)$$

  * (c) 與零的 gcd：

    $$\gcd(0, b) = b \qquad \left(b \in \mathbf{P}\right)$$

  * $a,\ b$ : 不全為零的整數 (Integers, not both zero) $[a, b \in \mathbf{Z}]$
  * $\mathrm{CD}(a, b)$ : 公因數集合 (The set of common divisors) $[\text{集合}]$

* **【已知 4】 [奇偶性 (Parity)](https://mathworld.wolfram.com/OddNumber.html)：** 初等算術，本章直接引用不再重證

  * (a) 奇數乘奇數仍是奇數：

    $$\left(2s+1\right)\left(2t+1\right) = 2\left(2st + s + t\right) + 1$$

  * (b) 偶數的倍數仍是偶數（故奇數的因數必為奇數）：

    $$d = 2u \quad \Longrightarrow \quad d t = 2\left(ut\right)$$

  * $s,\ t,\ u$ : 任意整數 (Arbitrary integers) $[s, t, u \in \mathbf{Z}]$
  * $d$ : 偶數 (An even integer) $[d \in 2\mathbf{Z}]$

* **【已知 5】 [整除倍數 (Divisibility of multiples)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/GCD/Divisibility_Basics.html#a-proof-that-a-common-divisor-divides-every-linear-combination)：** 已於本章 [整除的基本性質](Divisibility_Basics.md)【證明 (a)】取 $y = 0$ 的特例，此處直接引用不再重證

  $$d \mid n \quad \Longrightarrow \quad d \mid nx \qquad \text{for all } x \in \mathbf{Z}$$

  * $d,\ n$ : 任意整數 (Arbitrary integers) $[d, n \in \mathbf{Z}]$
  * $x$ : 任意整數倍數 (An arbitrary multiplier) $[x \in \mathbf{Z}]$

* **【推導 1】 奇因數可以穿過因子 $2$ (An odd divisor passes through a factor of two)：** 【證明 (b)】要用。
  設 $d$ 為奇數、$d \mid a$、$a$ 為偶數，則 $d \mid a/2$。寫 $a = dt$；若 $t$ 是奇數，$a$ 就是奇 $\times$ 奇 $=$ 奇，矛盾，故 $t$ 為偶數

  $$\begin{gather*}
  a &=& d t \\
  t \ \text{奇} &\overset{\text{已知 4(a)}}{\Longrightarrow}& a \ \text{奇（與 } a \text{ 為偶矛盾）} \\
  t &=& 2 s \qquad \text{for some } s \in \mathbf{Z} \\
  \frac{a}{2} &=& d s \\
  d &\mid& \frac{a}{2}
  \end{gather*}$$

  * $d$ : 奇因數 (An odd divisor) $[d \in \mathbf{Z},\ d \ \text{奇}]$
  * $a$ : 偶數 (An even integer) $[a \in 2\mathbf{Z}]$
  * $t,\ s$ : 倍數 (Multipliers) $[t, s \in \mathbf{Z}]$
  * 註：這是 [歐幾里得引理](../Factorization/Euclid_Lemma.md)「$\gcd(d, 2) = 1$ 且 $d \mid 2 \cdot \frac{a}{2}$ 則 $d \mid \frac{a}{2}$」的特例，
    但這裡只用奇偶性就能證，不必等到那一檔。

+++

## 證明:

### (a) proof of the both-even property

$a, b$ 皆偶，把每個組合的因子 $2$ 提出來。正組合的集合整個放大兩倍，最小值也放大兩倍：

$$\begin{gather*}
\gcd(a, b) &\overset{\text{已知 1}}{=}& \min\left\{ax + by > 0\right\} \\
&=& \min\left\{2\left(\frac{a}{2}x + \frac{b}{2}y\right) > 0\right\} \\
&=& 2 \min\left\{\frac{a}{2}x + \frac{b}{2}y > 0\right\} \\
&\overset{\text{已知 1}}{=}& 2 \gcd\left(\frac{a}{2}, \frac{b}{2}\right)
\end{gather*}$$

最後一步合法，因為 $a/2, b/2$ 仍不全為零。

### (b) proof of the even-odd property

依 A4 證明兩組數的公因數集合相等。

($\supseteq$) 整除 $a/2$ 就整除 $a = 2 \cdot \frac{a}{2}$：

$$\begin{gather*}
d &\mid& \frac{a}{2} \\
d &\overset{\text{已知 5}}{\mid}& 2 \times \frac{a}{2} \\
d &\mid& a \\
\mathrm{CD}\left(\frac{a}{2}, b\right) &\subseteq& \mathrm{CD}(a, b)
\end{gather*}$$

($\subseteq$) $d$ 整除奇數 $b$，所以 $d$ 是奇數（若 $d$ 偶，$b = dt$ 就偶）；再用【推導 1】：

$$\begin{gather*}
d &\mid& b \\
d \ \text{偶} &\overset{\text{已知 4(b)}}{\Longrightarrow}& b \ \text{偶（矛盾）} \\
d &\mid& a \qquad \text{(} d \text{ 奇、} a \text{ 偶)} \\
d &\overset{\text{推導 1}}{\mid}& \frac{a}{2} \\
\mathrm{CD}(a, b) &\subseteq& \mathrm{CD}\left(\frac{a}{2}, b\right)
\end{gather*}$$

兩集合相等，最大值相等：

$$\begin{gather*}
\gcd(a, b) &\overset{\text{已知 3(a)}}{=}& \gcd\left(\frac{a}{2}, b\right)
\end{gather*}$$

### (c) proof of the both-odd property

先平移（$k = -1$），$a - b$ 是偶數、$b$ 仍是奇數，於是套用 (b)：

$$\begin{gather*}
\gcd(a, b) &\overset{\text{已知 2}}{=}& \gcd(a - b,\ b) \\
&\overset{\text{證明 (b)}}{=}& \gcd\left(\frac{a - b}{2},\ b\right)
\end{gather*}$$

與投影片的證明一致（投影片寫「by 2)」即本檔的 (b)）。

### (d) verify the example of three hundred twenty-five and two hundred thirty-four

每一步標出用的是哪一條性質；需要交換順序時用【已知 3(b)】：

$$\begin{gather*}
\gcd(325, 234) &\overset{\text{證明 (b),已知 3(b)}}{=}& \gcd(325, 117) \qquad \text{(} 234 \text{ 偶、} 325 \text{ 奇)} \\
&\overset{\text{證明 (c)}}{=}& \gcd\left(\frac{325 - 117}{2}, 117\right) \\
&=& \gcd(104, 117) \\
&\overset{\text{證明 (b)}}{=}& \gcd(52, 117) \\
&\overset{\text{證明 (b)}}{=}& \gcd(26, 117) \\
&\overset{\text{證明 (b)}}{=}& \gcd(13, 117) \\
&\overset{\text{證明 (c),已知 3(b)}}{=}& \gcd\left(13, \frac{117 - 13}{2}\right) \\
&=& \gcd(13, 52) \\
&\overset{\text{證明 (b),已知 3(b)}}{=}& \gcd(13, 26) \\
&\overset{\text{證明 (b),已知 3(b)}}{=}& \gcd(13, 13) \\
&\overset{\text{證明 (c)}}{=}& \gcd\left(\frac{13 - 13}{2}, 13\right) \\
&=& \gcd(0, 13) \\
&\overset{\text{已知 3(c)}}{=}& 13
\end{gather*}$$

與投影片 p.20 一致，也與 [歐幾里得演算法](Euclidean_Algorithm.md)【證明 (e)】的結果相同。

+++

## 意義與密碼學關聯 (Interpretation and Relevance to Cryptography)

### 為什麼只看最低位元

三條性質的前提都只問「奇還是偶」—— 也就是**最低位元是 $0$ 還是 $1$**。
而每一步的動作只有三種：右移（除以 $2$）、相減、比較大小。沒有任何除法。

| 性質 | 最低位元 | 動作 |
|---|---|---|
| (a) | $a_0 = b_0 = 0$ | 兩個都右移，答案記一個因子 $2$ |
| (b) | $a_0 = 0,\ b_0 = 1$ | $a$ 右移 |
| (c) | $a_0 = b_0 = 1$ | 大減小，再右移 |

投影片引用 Knuth《The Art of Computer Programming》Vol. 2，稱它為 **Algorithm B**（B for Binary）。

### 常數時間實作與旁通道

密碼學在意的不只是「快」，還有**執行時間不能洩漏秘密**。
歐幾里得演算法的除法次數與商的大小都依輸入而變，是典型的時間旁通道來源。
Stein 型的二進位演算法因為每一步都是固定的位元操作，**更容易改寫成常數時間版本**
（每一步都做完所有分支，再用位元遮罩選結果）。
現代的常數時間模反元素演算法（如 Bernstein–Yang 2019，被用在 libsecp256k1 等函式庫）就是這個方向的延伸。

### 程式思維

```python
def stein(a, b):
    """三條性質直接遞迴。a, b ≥ 0，不全為零。"""
    if a == 0: return b
    if b == 0: return a
    if a % 2 == 0 and b % 2 == 0: return 2 * stein(a >> 1, b >> 1)   # (a)
    if a % 2 == 0: return stein(a >> 1, b)                           # (b)
    if b % 2 == 0: return stein(a, b >> 1)                           # (b) + 對稱
    if a >= b: return stein((a - b) >> 1, b)                         # (c)
    return stein(a, (b - a) >> 1)                                    # (c) + 對稱

assert stein(325, 234) == 13
```
