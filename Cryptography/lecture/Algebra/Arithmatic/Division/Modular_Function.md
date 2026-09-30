# Modular Function (取模函數)

+++

## 證明目標:

`Arithmetic.pdf` p.3（下半）–p.4。整章所有運算的起點：**餘數**的精確定義。

* (a) 餘數永遠落在 $0$ 與 $m-1$ 之間：

$$0 \le n \bmod m < m$$

* (b) **除法原理 (Division algorithm)**：$n$ 唯一地寫成「商 $\times$ 除數 $+$ 餘數」，
  而且商與餘數就是地板與取模：

$$n = \left\lfloor \frac{n}{m} \right\rfloor m + \left(n \bmod m\right), \qquad n = q'm + r',\ 0 \le r' < m \ \Longrightarrow \ q' = \left\lfloor \frac{n}{m} \right\rfloor,\ r' = n \bmod m$$

* (c) 整除等價於餘數為零：

$$m \mid n \quad \Longleftrightarrow \quad n \bmod m = 0$$

* (d) 驗證投影片的兩個例子：

$$25 \bmod 7 = 4, \qquad 58 = \left(2011\right)_3$$

* $n$ : 被除數 (The dividend) $[n \in \mathbf{Z}]$
* $m$ : 除數、模數 (The divisor, the modulus) $[m \in \mathbf{P}]$
* $q',\ r'$ : 任一組滿足條件的商與餘數 (Any admissible quotient and remainder) $[q', r' \in \mathbf{Z}]$
* $n \bmod m$ : $n$ 除以 $m$ 的餘數 (The remainder of $n$ divided by $m$) $[\mathbf{Z} \times \mathbf{P} \to \mathbf{Z}]$
* 註：**模數 $m$ 必須是正整數**（投影片寫 $m > 0$）。$m \le 0$ 時本檔的 $n \bmod m$ 無定義 ——
  這一點在 [歐幾里得演算法](../GCD/Euclidean_Algorithm.md) 處理負數輸入時會回頭造成麻煩。
* 註：(b) 的**唯一性**是整章最常被引用的一句話。[同餘關係](../Congruence/Congruence_Relation.md)、
  [擴展歐幾里得演算法](../GCD/Extended_Euclidean_Algorithm.md) 都靠它。
  Abstract_Algebra 章把除法原理當成外部已知引用，本檔把它證出來。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [地板函數的性質 (Properties of the floor function)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/Division/Floor_and_Ceiling.html#b-proof-of-the-characterization-of-the-floor)：** 已於本章 [取整函數](Floor_and_Ceiling.md)【證明 (a)(b)】完整證明，此處直接引用不再重證

  * (a) 夾擠不等式：

    $$\left\lfloor x \right\rfloor \le x < \left\lfloor x \right\rfloor + 1$$

  * (b) 刻畫：

    $$n \in \mathbf{Z},\ \ n \le x < n + 1 \quad \Longrightarrow \quad n = \left\lfloor x \right\rfloor$$

  * $x$ : 任意實數 (An arbitrary real number) $[x \in \mathbf{R}]$
  * $n$ : 整數 (An integer) $[n \in \mathbf{Z}]$
  * $\left\lfloor x \right\rfloor$ : 地板函數值 (The floor of $x$) $[\mathbf{R} \to \mathbf{Z}]$

* **【已知 2】 [整除 (Divisibility)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Number_Sets_and_Notation.html#assumptions-preliminaries)：** 已於 Abstract_Algebra 章 [數系與符號約定](../../Abstract_Algebra/Number_Sets_and_Notation.md)【已知 1(a)】給出，此處直接引用

  $$m \mid k \quad \overset{\text{def}}{\Longleftrightarrow} \quad \exists\, t \in \mathbf{Z} \ \text{ such that } \ k = mt$$

  * $m,\ k$ : 任意整數 (Arbitrary integers) $[m, k \in \mathbf{Z}]$
  * $t$ : 整數倍數 (Integer multiplier) $[t \in \mathbf{Z}]$

* **【定義 1】 取模函數 (Modular function)：**

  $$n \bmod m \overset{\text{def}}{=} n - \left\lfloor \frac{n}{m} \right\rfloor \times m$$

  * $n \bmod m$ : $n$ 除以 $m$ 的餘數 (The remainder of $n$ divided by $m$) $[\mathbf{Z} \times \mathbf{P} \to \mathbf{Z}]$
  * $n$ : 被除數 (The dividend) $[n \in \mathbf{Z}]$
  * $m$ : 模數 (The modulus) $[m \in \mathbf{P}]$
  * 註：$\left\lfloor n/m \right\rfloor$ 稱為**商 (quotient)**。投影片的
    $25 = 3 \times 7 + 4$「$7$: divisor，$3$: quotient，$4$: remainder」就是這三個角色。

* **【定義 2】 $b$ 進位表示 (Base-$b$ representation)：**

  $$\left(a_k a_{k-1} \cdots a_1 a_0\right)_b \overset{\text{def}}{=} \sum_{i=0}^{k} a_i\, b^{i}, \qquad 0 \le a_i < b$$

  * $b$ : 底數 (The base) $[b \in \mathbf{P},\ b \ge 2]$
  * $a_i$ : 第 $i$ 位數字 (The $i$-th digit) $[a_i \in \left\{0, \dots, b-1\right\}]$
  * $k$ : 最高位的位置 (The position of the leading digit) $[k \in \mathbf{N}]$
  * $i$ : 位置指標 (Digit index) $[i \in \left\{0, \dots, k\right\}]$

* **【推導 1】 進位轉換的遞迴 (Recursion for base conversion)：** 【證明 (e)】要用。
  反覆「取餘數當這一位、取商當下一輪」，每一輪都是一次除法原理

  $$\begin{gather*}
  n_0 &\overset{\text{let}}{=}& n \\
  a_i &\overset{\text{let}}{=}& n_i \bmod b \\
  n_{i+1} &\overset{\text{let}}{=}& \left\lfloor \frac{n_i}{b} \right\rfloor \\
  n_i &\overset{\text{定義 1}}{=}& b\, n_{i+1} + a_i
  \end{gather*}$$

  * $n$ : 要轉換的非負整數 (The non-negative integer to convert) $[n \in \mathbf{N}]$
  * $n_i$ : 第 $i$ 輪的商 (The quotient after round $i$) $[n_i \in \mathbf{N}]$
  * $a_i$ : 第 $i$ 位數字 (The $i$-th digit) $[a_i \in \left\{0, \dots, b-1\right\}]$
  * $b$ : 底數 (The base) $[b \in \mathbf{P},\ b \ge 2]$
  * 註：一路代回去就得到 $n = a_0 + b\left(a_1 + b\left(a_2 + \cdots\right)\right) = \sum a_i b^i$，
    即【定義 2】。$n_i$ 嚴格遞減，到 $0$ 時停止。

+++

## 證明:

### (a) proof that the remainder lies between zero and the modulus

把【已知 1(a)】套在 $x = n/m$ 上，兩邊同乘正數 $m$（不等號方向不變），再減掉 $\left\lfloor n/m \right\rfloor m$：

$$\begin{gather*}
\left\lfloor \frac{n}{m} \right\rfloor &\overset{\text{已知 1(a)}}{\le}& \frac{n}{m} \\
\left\lfloor \frac{n}{m} \right\rfloor m &\le& n \qquad \text{(} m > 0 \text{)} \\
0 &\le& n - \left\lfloor \frac{n}{m} \right\rfloor m \\
0 &\overset{\text{定義 1}}{\le}& n \bmod m \\
\frac{n}{m} &\overset{\text{已知 1(a)}}{<}& \left\lfloor \frac{n}{m} \right\rfloor + 1 \\
n &<& \left\lfloor \frac{n}{m} \right\rfloor m + m \\
n - \left\lfloor \frac{n}{m} \right\rfloor m &<& m \\
n \bmod m &\overset{\text{定義 1}}{<}& m
\end{gather*}$$

與投影片「which is $\ge 0$ and $< m$」一致。

### (b) proof of the division algorithm with uniqueness

**存在性**直接由【定義 1】移項：

$$\begin{gather*}
n \bmod m &\overset{\text{定義 1}}{=}& n - \left\lfloor \frac{n}{m} \right\rfloor m \\
n &=& \left\lfloor \frac{n}{m} \right\rfloor m + \left(n \bmod m\right)
\end{gather*}$$

**唯一性**：設另有 $n = q'm + r'$、$0 \le r' < m$。兩邊除以 $m$，由 $0 \le r'/m < 1$ 把 $q'$ 夾在 $n/m$ 下方一格內：

$$\begin{gather*}
n &=& q'm + r' \\
\frac{n}{m} &=& q' + \frac{r'}{m} \\
q' &\le& \frac{n}{m} \qquad \text{(} r' \ge 0 \text{)} \\
\frac{n}{m} &<& q' + 1 \qquad \text{(} r' < m \text{)} \\
q' &\overset{\text{已知 1(b)}}{=}& \left\lfloor \frac{n}{m} \right\rfloor \\
r' &=& n - q'm \\
r' &\overset{\text{定義 1}}{=}& n \bmod m
\end{gather*}$$

商與餘數都被唯一決定。

### (c) proof (⇒) that divisibility forces a zero remainder

設 $m \mid n$，即 $n = tm$。這本身就是一個「餘數為 $0$」的除法式，由唯一性它就是那一個：

$$\begin{gather*}
n &\overset{\text{已知 2}}{=}& t m \\
n &=& t m + 0 \qquad \text{(} 0 \le 0 < m \text{)} \\
n \bmod m &\overset{\text{證明 (b)}}{=}& 0
\end{gather*}$$

### (d) proof (⇐) that a zero remainder gives divisibility

$$\begin{gather*}
n &\overset{\text{證明 (b)}}{=}& \left\lfloor \frac{n}{m} \right\rfloor m + \left(n \bmod m\right) \\
n &=& \left\lfloor \frac{n}{m} \right\rfloor m + 0 \\
m &\overset{\text{已知 2}}{\mid}& n
\end{gather*}$$

(c)(d) 合起來即 $m \mid n \Longleftrightarrow n \bmod m = 0$。

### (e) verify the two examples from the slides

**$25 \bmod 7$。** 先用【已知 1(b)】確認商是 $3$（$21 \le 25 < 28$），再代入【定義 1】：

$$\begin{gather*}
3 &\le& \frac{25}{7} \qquad \text{(} 21 \le 25 \text{)} \\
\frac{25}{7} &<& 3 + 1 \qquad \text{(} 25 < 28 \text{)} \\
\left\lfloor \frac{25}{7} \right\rfloor &\overset{\text{已知 1(b)}}{=}& 3 \\
25 \bmod 7 &\overset{\text{定義 1}}{=}& 25 - 3 \times 7 \\
25 \bmod 7 &=& 4
\end{gather*}$$

與投影片一致。

**$58$ 的三進位。** 依【推導 1】反覆除以 $3$：

$$\begin{gather*}
58 &\overset{\text{推導 1}}{=}& 3 \times 19 + 1 \qquad \left(a_0 = 1,\ n_1 = 19\right) \\
19 &\overset{\text{推導 1}}{=}& 3 \times 6 + 1 \qquad \left(a_1 = 1,\ n_2 = 6\right) \\
6 &\overset{\text{推導 1}}{=}& 3 \times 2 + 0 \qquad \left(a_2 = 0,\ n_3 = 2\right) \\
2 &\overset{\text{推導 1}}{=}& 3 \times 0 + 2 \qquad \left(a_3 = 2,\ n_4 = 0\right)
\end{gather*}$$

$n_4 = 0$ 停止。由高位到低位讀出數字，依【定義 2】驗算：

$$\begin{gather*}
\left(2011\right)_3 &\overset{\text{定義 2}}{=}& 2 \times 3^3 + 0 \times 3^2 + 1 \times 3^1 + 1 \times 3^0 \\
&=& 54 + 0 + 3 + 1 \\
&=& 58
\end{gather*}$$

與投影片一致。

+++

## 意義與密碼學關聯 (Interpretation and Relevance to Cryptography)

### 「餘數」就是有限世界的座標

$n \bmod m$ 把無限多個整數**摺疊**到 $\left\{0, 1, \dots, m-1\right\}$ 這 $m$ 個格子裡。
所有現代公鑰密碼 —— RSA、Diffie–Hellman、ECC —— 都活在這種有限的格子世界裡，
因為**有限才能用固定長度的位元表示**，也才能讓攻擊者無法用「大小」推回原值。

在 Abstract_Algebra 章，這些格子被正式化成同餘類
（[模理想的同餘類](../../Abstract_Algebra/Ring/Congruence_Class_Modulo_Ideal.md)），
而 $\mathbf{Z}_n$ 的運算則由 [商環](../../Abstract_Algebra/Ring/Quotient_Ring.md) 給出嚴格定義。

### 進位轉換就是「重複取模」

【證明 (e)】的三進位轉換，換成二進位就是電腦把整數變成位元串的方式。
**快速冪 (square-and-multiply)** 演算法正是先把指數 $e$ 做一次這樣的二進位展開，
再依每一位決定「平方」或「平方再乘」—— 見 [尤拉定理](../Fermat_Euler/Euler_Theorem.md) 的程式思維。

### 程式思維

```python
def mod(n, m):
    """定義 1：n - floor(n/m)*m，m 必須為正。"""
    assert m > 0
    return n - (n // m) * m           # Python 的 // 就是地板除法

assert mod(25, 7) == 4 == 25 % 7
assert mod(-25, 7) == 3               # 餘數永遠非負（證明 (a)）

def to_base(n, b):
    """推導 1：反覆取餘數。"""
    digits = []
    while n:
        n, a = divmod(n, b)            # divmod 一次給出 (商, 餘數) —— 證明 (b)
        digits.append(a)
    return digits[::-1]

assert to_base(58, 3) == [2, 0, 1, 1]
```
