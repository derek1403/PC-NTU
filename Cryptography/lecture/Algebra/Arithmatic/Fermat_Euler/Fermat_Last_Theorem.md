# Fermat Last Theorem (費馬最後定理)

+++

## 本檔目標:

`Arithmetic.pdf` p.55–56，整份投影片的最後兩頁。費馬在 1637 年寫在書頁空白處、
卻花了人類 $357$ 年才證明的定理。它的證明遠超本章，但其中有一小步是本章工具就能完成的。

* (a) 定理的敘述（**投影片未附證明，本檔亦不證**，理由見下）：

$$n \ge 3 \quad \Longrightarrow \quad a^n + b^n = c^n \ \text{ 沒有正整數解 } \ a, b, c$$

* (b) **化約引理**（本檔完整證明）：若 $n$ 有反例，則 $n$ 的每個 $\ge 3$ 的因數 $e$ 也有反例：

$$a^n + b^n = c^n,\ \ e \mid n \quad \Longrightarrow \quad \left(a^{n/e}\right)^e + \left(b^{n/e}\right)^e = \left(c^{n/e}\right)^e$$

* (c) 每個 $n \ge 3$ 都有一個因數是 $4$ 或奇質數 —— 所以**只需對 $n = 4$ 與奇質數 $n = p$ 證明**。
* (d) $n = 2$ 有解，定理從 $3$ 開始不是任意的：$3^2 + 4^2 = 5^2$。

* $n$ : 指數 (The exponent) $[n \in \mathbf{P}]$
* $a,\ b,\ c$ : 正整數 (Positive integers) $[a, b, c \in \mathbf{P}]$
* $e$ : $n$ 的因數 (A divisor of $n$) $[e \in \mathbf{P},\ e \ge 3]$
* $p$ : 奇質數 (An odd prime) $[p \in \mathbf{P}]$
* 註：**本檔不證明 (a)。** Wiles 的證明（1995，與 Taylor 合作修補）用到橢圓曲線的模性 (modularity)，
  橫跨代數幾何、表示論與 Galois 表示，篇幅超過一百頁，遠超本章。本檔誠實標示這一點，只做 (b)(c)(d)。
* 註：(c) 是歷史上實際的攻略路線：費馬自己用無窮遞降法證了 $n = 4$，Euler 證了 $n = 3$，
  之後的數學家逐個攻克奇質數指數，直到 Kummer 一次處理「正則質數」—— 而那正是 [算術基本定理](../Factorization/Fundamental_Theorem_of_Arithmetic.md)
  文末提到的「唯一分解失敗」問題的發源地。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [算術基本定理（存在性） (Existence of prime factorization)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/Factorization/Fundamental_Theorem_of_Arithmetic.html#b-proof-of-the-inductive-step-of-existence)：** 已於本章 [算術基本定理](../Factorization/Fundamental_Theorem_of_Arithmetic.md)【證明 (a)(b)】完整證明，此處直接引用不再重證

  $$n \ge 2 \quad \Longrightarrow \quad n = p_1 p_2 \cdots p_r, \qquad p_i \ \text{為質數}$$

  * $n$ : 大於 $1$ 的整數 (An integer greater than one) $[n \in \mathbf{P}]$
  * $p_i$ : 質數 (Primes) $[p_i \in \mathbf{P}]$
  * $r$ : 質因數個數 (The number of prime factors) $[r \in \mathbf{P}]$

* **【已知 2】 [整除 (Divisibility)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Number_Sets_and_Notation.html#assumptions-preliminaries)：** 已於 Abstract_Algebra 章 [數系與符號約定](../../Abstract_Algebra/Number_Sets_and_Notation.md)【已知 1(a)】給出，此處直接引用

  $$e \mid n \quad \Longleftrightarrow \quad n = e k \ \text{ for some } k \in \mathbf{Z}$$

  * $e,\ n$ : 正整數 (Positive integers) $[e, n \in \mathbf{P}]$
  * $k$ : 商 (The quotient) $[k \in \mathbf{P}]$

* **【假設 1】 反例存在 (A counterexample exists)：** 【證明 (b)】的出發點。設對某個 $n \ge 3$ 有正整數解

  $$a^n + b^n = c^n$$

  * $a,\ b,\ c$ : 反例中的正整數 (The positive integers in the counterexample) $[a, b, c \in \mathbf{P}]$
  * $n$ : 指數 (The exponent) $[n \in \mathbf{P},\ n \ge 3]$
  * 註：這不是反證法的反設 —— 定理 (a) 本檔不證，(b) 是一個「若有反例則……」的條件命題。

+++

## 定理陳述與證明:

### (a) statement of Fermat's last theorem without proof

**費馬最後定理（投影片 p.55–56，本章不證）：**

$$n \ge 3,\ \ a, b, c \in \mathbf{P} \quad \Longrightarrow \quad a^n + b^n \neq c^n$$

**證明的大致路線（本章沒有建立這些工具）：**

1. **Frey 曲線**（投影片 p.56）：若 $a^n + b^n = c^n$ 是反例，構造橢圓曲線 $y^2 = x\left(x - a^n\right)\left(x + b^n\right)$；
2. **Ribet 定理**（1986）：這條曲線不可能是「模的 (modular)」；
3. **Wiles–Taylor**（1995）：所有（半穩定的）橢圓曲線都是模的（Taniyama–Shimura 猜想的特例）。

2 與 3 矛盾，故反例不存在。**本檔不假裝證明它**，僅陳述並完成下面可以用初等方法處理的部分。

### (b) proof that a counterexample descends to every divisor

寫 $n = ek$，把 $a^n$ 看成 $\left(a^k\right)^e$：

$$\begin{gather*}
n &\overset{\text{已知 2}}{=}& e k \\
a^n + b^n &\overset{\text{假設 1}}{=}& c^n \\
\left(a^k\right)^e + \left(b^k\right)^e &=& \left(c^k\right)^e
\end{gather*}$$

$a^k, b^k, c^k$ 仍是正整數，所以這是指數 $e$ 的反例。換句話說：**對 $e$ 證明了定理，就同時證明了 $e$ 的所有倍數。**

### (c) proof that every exponent from three has a divisor equal to four or an odd prime

由【已知 1】分解 $n$。

**情形一：有奇質因數 $p$。** 則 $p \mid n$，$p \ge 3$。

**情形二：沒有奇質因數。** 則所有質因數都是 $2$，$n = 2^s$；而 $n \ge 3$ 迫使 $s \ge 2$：

$$\begin{gather*}
n &\overset{\text{已知 1}}{=}& 2^{s} \\
s &\ge& 2 \qquad \text{(} 2^0 = 1,\ 2^1 = 2 \text{ 都} < 3 \text{)} \\
n &=& 4 \times 2^{s-2} \\
4 &\overset{\text{已知 2}}{\mid}& n
\end{gather*}$$

兩種情形都找到因數 $4$ 或奇質數。配合 (b)：**若定理對 $4$ 與所有奇質數成立，則對所有 $n \ge 3$ 成立。**

### (d) verify that the exponent two has solutions

$$\begin{gather*}
3^2 + 4^2 &=& 9 + 16 \\
3^2 + 4^2 &=& 25 \\
3^2 + 4^2 &=& 5^2
\end{gather*}$$

$n = 2$ 的解就是畢氏三元數，有無窮多組（如 $\left(5, 12, 13\right)$、$\left(8, 15, 17\right)$）。
注意 (c) 的論證對 $n = 2$ 失效：$2$ 的因數只有 $1, 2$，沒有 $4$ 也沒有奇質數 —— 這正是定理必須從 $3$ 開始的原因。

+++

## 意義與密碼學關聯 (Interpretation and Relevance to Cryptography)

### 「頁邊太窄」的故事

投影片 p.55：Pierre de Fermat（1601–1665）是法國律師與業餘數學家。1637 年他在 Diophantus《算術》的頁邊寫下：
「我已找到一個真正奇妙的證明，可惜頁邊太窄寫不下。」
（Cuius rei demonstrationem mirabilem sane detexi. Hanc marginis exiguitas non caperet.）

$357$ 年後，Andrew Wiles（1953–）在 1993 年宣布證明，隨後發現漏洞，與學生 Richard Taylor 在一年內修補，1995 年發表於 *Annals of Mathematics*。
今天普遍相信費馬當年**並沒有**一個正確的證明 —— 他很可能以為自己的 $n = 4$ 方法可以推廣。

### 與密碼學的連結：橢圓曲線

證明費馬最後定理的關鍵物件 —— **橢圓曲線** —— 正是現代密碼學的主力之一。
投影片 p.56 的 Frey 曲線 $y^2 = x\left(x - a^n\right)\left(x + b^n\right)$ 與 ECC 用的曲線
（如 secp256k1 的 $y^2 = x^3 + 7$）是同一類物件。Wiles 的工作大幅推進了對橢圓曲線算術的理解，
而 ECC 的安全性正建立在「橢圓曲線上的離散對數問題困難」之上。

**一條三百年的純數學難題，與今天保護網路連線的演算法，研究的是同一種曲線。**

### 程式思維

```python
# 證明 (d)：畢氏三元數存在
assert 3**2 + 4**2 == 5**2 and 5**2 + 12**2 == 13**2
# 證明 (b)：n = 6 的反例會給出 n = 3 的反例 —— 以「不存在」的形式在小範圍內檢查
N = 60
cubes = {c**3 for c in range(1, 2 * N)}
assert not any(a**3 + b**3 in cubes for a in range(1, N) for b in range(1, N))
```
