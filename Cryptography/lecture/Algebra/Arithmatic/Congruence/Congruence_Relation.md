# Congruence Relation (同餘關係)

+++

## 證明目標:

`Arithmetic.pdf` p.27。投影片用「**餘數相同**」定義同餘，然後給出「**差被整除**」的等價刻畫，
證明留作習題（「both straightforward — exercise」）。本檔把兩個方向都寫出來。

* (a)(b) 投影片的定理：

$$a \equiv b \pmod{m} \quad \Longleftrightarrow \quad m \mid \left(a - b\right)$$

* (c) 每個整數與自己的餘數同餘：

$$a \equiv \left(a \bmod m\right) \pmod{m}$$

* (d) 驗證：$17 \equiv 2 \pmod 5$、$-25 \equiv 3 \pmod 7$。

* $a,\ b$ : 任意整數 (Arbitrary integers) $[a, b \in \mathbf{Z}]$
* $m$ : 模數 (The modulus) $[m \in \mathbf{P}]$
* $a \equiv b \pmod m$ : $a$ 與 $b$ 模 $m$ 同餘 ($a$ is congruent to $b$ modulo $m$) $[\text{關係}]$
* 註：Abstract_Algebra 章 [數系與符號約定](../../Abstract_Algebra/Number_Sets_and_Notation.md)【已知 2】
  直接把 $m \mid (a - b)$ 當成同餘的**定義**。本檔的 (a)(b) 證明兩種定義等價，
  所以兩章對「同餘」的用法完全一致，可以互相引用。
* 註：(c) 雖然簡單，卻是「**取模可以隨時做**」的根據 —— 計算途中任何時候把中間結果換成它的餘數，同餘關係都不變。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [除法原理 (Division algorithm)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/Division/Modular_Function.html#b-proof-of-the-division-algorithm-with-uniqueness)：** 已於本章 [取模函數](../Division/Modular_Function.md)【證明 (a)(b)】完整證明，此處直接引用不再重證

  * (a) 存在性：

    $$n = \left\lfloor \frac{n}{m} \right\rfloor m + \left(n \bmod m\right), \qquad 0 \le n \bmod m < m$$

  * (b) 唯一性：

    $$n = q'm + r',\ \ 0 \le r' < m \quad \Longrightarrow \quad r' = n \bmod m$$

  * $n$ : 被除數 (The dividend) $[n \in \mathbf{Z}]$
  * $m$ : 模數 (The modulus) $[m \in \mathbf{P}]$
  * $q',\ r'$ : 任一組滿足條件的商與餘數 (Any admissible quotient and remainder) $[q', r' \in \mathbf{Z}]$

* **【已知 2】 [整除 (Divisibility)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Number_Sets_and_Notation.html#assumptions-preliminaries)：** 已於 Abstract_Algebra 章 [數系與符號約定](../../Abstract_Algebra/Number_Sets_and_Notation.md)【已知 1(a)】給出，此處直接引用

  $$m \mid k \quad \overset{\text{def}}{\Longleftrightarrow} \quad \exists\, t \in \mathbf{Z} \ \text{ such that } \ k = mt$$

  * $m,\ k$ : 任意整數 (Arbitrary integers) $[m, k \in \mathbf{Z}]$
  * $t$ : 整數倍數 (Integer multiplier) $[t \in \mathbf{Z}]$

* **【定義 1】 同餘 (Congruence modulo $m$)：** 投影片的定義 —— 除以 $m$ 的餘數相同

  $$a \equiv b \pmod{m} \quad \overset{\text{def}}{\Longleftrightarrow} \quad a \bmod m = b \bmod m$$

  * $a,\ b$ : 任意整數 (Arbitrary integers) $[a, b \in \mathbf{Z}]$
  * $m$ : 模數 (The modulus) $[m \in \mathbf{P}]$

+++

## 證明:

### (a) proof (⇒) that congruent integers differ by a multiple of the modulus

設 $a \bmod m = b \bmod m$，記為 $r$。兩者都寫成「商 $\times\, m + r$」，相減後 $r$ 消掉：

$$\begin{gather*}
a &\overset{\text{已知 1(a)}}{=}& q_1 m + r \qquad \text{(} q_1 = \left\lfloor a/m \right\rfloor \text{)} \\
b &\overset{\text{已知 1(a),定義 1}}{=}& q_2 m + r \qquad \text{(} q_2 = \left\lfloor b/m \right\rfloor \text{，餘數同為 } r \text{)} \\
a - b &=& \left(q_1 - q_2\right) m \\
m &\overset{\text{已知 2}}{\mid}& a - b
\end{gather*}$$

### (b) proof (⇐) that a difference divisible by the modulus gives equal remainders

設 $a - b = tm$。把 $b$ 的除法式搬到 $a$ 身上：$a$ 也是「某個商 $\times\, m$ 加上同一個 $r$」，而 $0 \le r < m$，由唯一性那就是 $a$ 的餘數：

$$\begin{gather*}
a - b &\overset{\text{已知 2}}{=}& t m \\
b &\overset{\text{已知 1(a)}}{=}& q m + r \qquad \text{with } r = b \bmod m,\ 0 \le r < m \\
a &=& b + tm \\
a &=& \left(q + t\right) m + r \\
a \bmod m &\overset{\text{已知 1(b)}}{=}& r \\
a \bmod m &=& b \bmod m \\
a &\overset{\text{定義 1}}{\equiv}& b \pmod{m}
\end{gather*}$$

(a)(b) 合起來即投影片的定理。

### (c) proof that every integer is congruent to its remainder

$r = a \bmod m$ 已經落在 $\left[0, m\right)$ 裡，所以 $r = 0 \cdot m + r$ 就是 $r$ 自己的除法式，$r$ 的餘數就是它自己：

$$\begin{gather*}
r &=& 0 \times m + r \qquad \text{(} 0 \le r < m \text{)} \\
r \bmod m &\overset{\text{已知 1(b)}}{=}& r \\
r \bmod m &=& a \bmod m \\
a &\overset{\text{定義 1}}{\equiv}& \left(a \bmod m\right) \pmod{m}
\end{gather*}$$

### (d) verify two numerical congruences

**$17 \equiv 2 \pmod 5$**，分別用【定義 1】與【證明 (a)(b)】的刻畫：

$$\begin{gather*}
17 \bmod 5 &\overset{\text{已知 1(a)}}{=}& 17 - 3 \times 5 \\
17 \bmod 5 &=& 2 \\
2 \bmod 5 &\overset{\text{已知 1(a)}}{=}& 2 \\
17 - 2 &=& 5 \times 3 \\
5 &\overset{\text{證明 (a)}}{\mid}& 17 - 2
\end{gather*}$$

**$-25 \equiv 3 \pmod 7$**，負數的餘數要用地板除法（$\left\lfloor -25/7 \right\rfloor = -4$）：

$$\begin{gather*}
-25 \bmod 7 &\overset{\text{已知 1(a)}}{=}& -25 - \left(-4\right) \times 7 \\
-25 \bmod 7 &=& 3 \\
-25 &\overset{\text{定義 1}}{\equiv}& 3 \pmod{7}
\end{gather*}$$

用 (b) 的刻畫驗算：$-25 - 3 = -28 = 7 \times \left(-4\right)$，確實被 $7$ 整除。

+++

## 意義與密碼學關聯 (Interpretation and Relevance to Cryptography)

### 兩種定義各有用處

| 定義 | 適合 | 例子 |
|---|---|---|
| 餘數相同（【定義 1】） | **計算**：直接比較兩個 `% m` 的結果 | 程式判斷 `a % m == b % m` |
| 差被整除（【證明 (a)(b)】） | **證明**：可以做代數運算 | 同餘的加減乘冪全靠它（[同餘的性質](Congruence_Properties.md)） |

「差被整除」的版本把同餘變成**關於整除的陳述**，於是 [整除的基本性質](../GCD/Divisibility_Basics.md) 全部可以拿來用。
這也是為什麼 Abstract_Algebra 章直接用它當定義 ——
[模理想的同餘類](../../Abstract_Algebra/Ring/Congruence_Class_Modulo_Ideal.md) 把它進一步推廣成 $a - b \in I$。

### 取模可以隨時做

(c) 保證：**計算途中任何時候把中間結果換成它的餘數，不會改變最終的同餘類。**
這是所有模運算實作的基礎 —— 計算 $a^{65537} \bmod n$ 時，每乘一次就取一次模，
中間結果永遠不超過 $n^2$，否則 $a^{65537}$ 本身有幾十萬位數，記憶體根本裝不下。

### 程式思維

```python
def congruent(a, b, m):
    return a % m == b % m                   # 定義 1

for a in range(-50, 50):
    for b in range(-50, 50):
        for m in range(1, 12):
            assert congruent(a, b, m) == ((a - b) % m == 0)   # 證明 (a)(b)
assert congruent(17, 2, 5) and congruent(-25, 3, 7)            # 證明 (d)
```
