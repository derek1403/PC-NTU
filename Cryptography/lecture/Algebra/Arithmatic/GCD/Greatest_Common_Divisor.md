# Greatest Common Divisor (最大公因數)

+++

## 證明目標:

`Arithmetic.pdf` p.7。整章的主角之一。先把「公因數」「最大公因數」精確定義，
再證明投影片列出的四條基本性質。

* (a) 只要 $a, b$ 不全為零，$\gcd(a,b)$ **存在**且是正整數：

$$a \neq 0 \ \text{ or } \ b \neq 0 \quad \Longrightarrow \quad \gcd(a, b) \in \mathbf{P}$$

* (b) 驗證投影片的例子：

$$\gcd(20, 16) = 4$$

* (c) 投影片第一組命題（$a \in \mathbf{P}$）：

$$\gcd(a, a) = a, \qquad \gcd(a, 0) = a$$

* (d) 投影片第二組命題（$a \neq 0$ 或 $b \neq 0$）：

$$\gcd(a, b) = \gcd\left(\left|a\right|, \left|b\right|\right), \qquad \gcd(a, b) = \gcd(b, a)$$

* $a,\ b$ : 不全為零的整數 (Integers, not both zero) $[a, b \in \mathbf{Z}]$
* $d$ : 公因數 (A common divisor) $[d \in \mathbf{Z},\ d \neq 0]$
* $\gcd(a, b)$ : 最大公因數 (The greatest common divisor) $[\gcd(a,b) \in \mathbf{P}]$
* 註：**$a = b = 0$ 被排除**。每個非零整數都整除 $0$，公因數沒有上界，「最大」不存在。
  有些教科書約定 $\gcd(0, 0) = 0$，本章不採用。
* 註：Abstract_Algebra 章 [數系與符號約定](../../Abstract_Algebra/Number_Sets_and_Notation.md)【已知 1(b)】
  把 gcd 寫成「正公因數的最大者」，本檔的定義允許負公因數。兩者給出同一個數，
  因為正負公因數成對出現（【已知 1(c)】），最大者必為正。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [整除的基本性質 (Divisibility basics)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/GCD/Divisibility_Basics.html#e-proof-that-a-divisor-of-a-nonzero-integer-is-no-larger-in-absolute-value)：** 已於本章 [整除的基本性質](Divisibility_Basics.md)【證明 (c)(d)(e)】完整證明，此處直接引用不再重證

  * (a) 平凡整除：

    $$d \mid 0 \quad \left(d \neq 0\right), \qquad 1 \mid a$$

  * (b) 大小界：

    $$d \mid a,\ \ a \neq 0 \quad \Longrightarrow \quad \left|d\right| \le \left|a\right|$$

  * (c) 正負號無關：

    $$d \mid a \quad \Longleftrightarrow \quad d \mid -a$$

  * $a$ : 任意整數 (An arbitrary integer) $[a \in \mathbf{Z}]$
  * $d$ : 因數 (A divisor) $[d \in \mathbf{Z}]$

* **【已知 2】 [有上界的整數集合有最大元 (A bounded-above set of integers has a maximum)](https://mathworld.wolfram.com/WellOrderingPrinciple.html)：** 良序原理的等價形式，本章直接引用不再重證

  $$\varnothing \neq S \subseteq \mathbf{Z},\ \ S \ \text{有上界} \quad \Longrightarrow \quad \max S \ \text{存在}$$

  * $S$ : 整數的子集 (A subset of the integers) $[S \subseteq \mathbf{Z}]$

* **【定義 1】 公因數 (Common divisor)：** 非零且同時整除兩數

  $$\mathrm{CD}(a, b) \overset{\text{def}}{=} \left\{d \in \mathbf{Z} \ \middle|\ d \neq 0,\ d \mid a,\ d \mid b\right\}$$

  * $\mathrm{CD}(a, b)$ : $a, b$ 的公因數集合 (The set of common divisors of $a$ and $b$) $[\text{集合}]$
  * $a,\ b$ : 不全為零的整數 (Integers, not both zero) $[a, b \in \mathbf{Z}]$
  * $d$ : 候選公因數 (A candidate common divisor) $[d \in \mathbf{Z}]$
  * 註：$\mathrm{CD}$ 是本章為了推導方便引入的記號，投影片只用文字描述。

* **【定義 2】 最大公因數 (Greatest common divisor)：** 公因數中最大的那一個

  $$\gcd(a, b) \overset{\text{def}}{=} \max\ \mathrm{CD}(a, b)$$

  * $\gcd(a, b)$ : 最大公因數 (The greatest common divisor) $[\gcd(a,b) \in \mathbf{P}]$
  * $\mathrm{CD}(a, b)$ : 公因數集合 (The set of common divisors) $[\text{集合}]$
  * 註：「最大值存在」這件事要證，見【證明 (a)】。
  * 註：**兩組數的公因數集合相等，gcd 就相等** —— 這是整章證 gcd 等式的標準手法
    （先證 $\mathrm{CD}$ 相等，再套本定義）。

+++

## 證明:

### (a) proof that the greatest common divisor exists and is positive

不失一般性設 $a \neq 0$（否則交換 $a, b$ 的角色）。公因數集合含 $1$，且每個公因數都不超過 $\left|a\right|$：

$$\begin{gather*}
1 &\overset{\text{已知 1(a)}}{\in}& \mathrm{CD}(a, b) \\
\mathrm{CD}(a, b) &\neq& \varnothing \\
d &\le& \left|d\right| \qquad \text{for all } d \in \mathrm{CD}(a,b) \\
\left|d\right| &\overset{\text{已知 1(b)}}{\le}& \left|a\right| \qquad \text{(} d \mid a,\ a \neq 0 \text{)} \\
\max \mathrm{CD}(a, b) &\overset{\text{已知 2}}{\in}& \mathrm{CD}(a,b) \qquad \text{(最大元素存在)} \\
\gcd(a, b) &\overset{\text{定義 2}}{\ge}& 1
\end{gather*}$$

最後一行因為 $1$ 本身是一個公因數，最大值不會比它小。故 $\gcd(a,b) \in \mathbf{P}$。

### (b) verify the example of twenty and sixteen

依【已知 1(b)】，$20$ 的因數絕對值不超過 $20$、$16$ 的不超過 $16$，逐一檢查即得（與投影片一致）：

$$\begin{gather*}
\left\{d \ \middle|\ d \mid 20\right\} &=& \left\{\pm 1,\ \pm 2,\ \pm 4,\ \pm 5,\ \pm 10,\ \pm 20\right\} \\
\left\{d \ \middle|\ d \mid 16\right\} &=& \left\{\pm 1,\ \pm 2,\ \pm 4,\ \pm 8,\ \pm 16\right\} \\
\mathrm{CD}(20, 16) &\overset{\text{定義 1}}{=}& \left\{\pm 1,\ \pm 2,\ \pm 4\right\} \\
\gcd(20, 16) &\overset{\text{定義 2}}{=}& 4
\end{gather*}$$

### (c) proof that the gcd of a with itself and with zero is a

設 $a \in \mathbf{P}$。**$\gcd(a, a)$**：$a$ 自己是公因數，且沒有公因數超過 $\left|a\right| = a$：

$$\begin{gather*}
a &\in& \mathrm{CD}(a, a) \qquad \text{(} a = a \times 1 \text{)} \\
d &\overset{\text{已知 1(b)}}{\le}& a \qquad \text{for all } d \in \mathrm{CD}(a, a) \\
\gcd(a, a) &\overset{\text{定義 2}}{=}& a
\end{gather*}$$

**$\gcd(a, 0)$**：每個非零整數都整除 $0$，所以「整除 $0$」這個條件是空的，公因數就是 $a$ 的因數：

$$\begin{gather*}
\mathrm{CD}(a, 0) &\overset{\text{定義 1}}{=}& \left\{d \neq 0 \ \middle|\ d \mid a,\ d \mid 0\right\} \\
\mathrm{CD}(a, 0) &\overset{\text{已知 1(a)}}{=}& \left\{d \neq 0 \ \middle|\ d \mid a\right\} \\
\mathrm{CD}(a, 0) &=& \mathrm{CD}(a, a) \\
\gcd(a, 0) &\overset{\text{定義 2}}{=}& \gcd(a, a) \\
\gcd(a, 0) &=& a
\end{gather*}$$

兩式與投影片一致。

* 註：$a$ 為負時結論變成 $\gcd(a, 0) = \left|a\right|$ —— 由 (d) 的第一式即得。
  [歐幾里得演算法](Euclidean_Algorithm.md) 的終止條件「$b = 0$ 時輸出 $\left|a\right|$」就是這一條。

### (d) proof that the gcd ignores signs and order

**正負號**：由【已知 1(c)】，$d \mid a \Longleftrightarrow d \mid \left|a\right|$（$\left|a\right|$ 不是 $a$ 就是 $-a$），
所以兩組數的公因數集合逐元素相同：

$$\begin{gather*}
\mathrm{CD}(a, b) &\overset{\text{定義 1}}{=}& \left\{d \neq 0 \ \middle|\ d \mid a,\ d \mid b\right\} \\
\mathrm{CD}(a, b) &\overset{\text{已知 1(c)}}{=}& \left\{d \neq 0 \ \middle|\ d \mid \left|a\right|,\ d \mid \left|b\right|\right\} \\
\mathrm{CD}(a, b) &\overset{\text{定義 1}}{=}& \mathrm{CD}\left(\left|a\right|, \left|b\right|\right) \\
\gcd(a, b) &\overset{\text{定義 2}}{=}& \gcd\left(\left|a\right|, \left|b\right|\right)
\end{gather*}$$

**順序**：【定義 1】的兩個條件「$d \mid a$ 且 $d \mid b$」對 $a, b$ 對稱：

$$\begin{gather*}
\mathrm{CD}(a, b) &\overset{\text{定義 1}}{=}& \mathrm{CD}(b, a) \\
\gcd(a, b) &\overset{\text{定義 2}}{=}& \gcd(b, a)
\end{gather*}$$

兩式與投影片一致。

+++

## 意義與密碼學關聯 (Interpretation and Relevance to Cryptography)

### 直覺：同一把尺量兩根木條

想像兩根長 $20$ 與 $16$ 公分的木條。「$d$ 是公因數」就是：有一把長 $d$ 的短尺，
可以把兩根木條**都剛好量完、不留零頭**。最大公因數就是能做到這件事的**最長**的那把尺 —— 這裡是 $4$ 公分。

$\gcd(a, 0) = a$ 的直覺是：長度 $0$ 的木條「什麼尺都量得完」，所以限制只來自另一根。

### 列舉法太慢，要換演算法

【證明 (b)】用的是**列舉**：列出所有因數再取交集。對 $a = 105623$、$b = 39481$ 這種數已經很吃力；
對 RSA 的 $2048$ 位元數字，列舉因數**就等於分解整數**，是公認做不到的事。

所以接下來三檔的目標是：**不分解整數，也能算出 gcd**。

1. [GCD 的平移不變性](GCD_Shift_Invariance.md)：$\gcd(a, b) = \gcd(b,\ a \bmod b)$
2. [歐幾里得演算法](Euclidean_Algorithm.md)：反覆套用上式，對數步內結束
3. [擴展歐幾里得演算法](Extended_Euclidean_Algorithm.md)：順便求出 $ax + by = \gcd(a,b)$ 的係數

**gcd 容易、分解困難** —— 這個不對稱正是 RSA 安全性的根基之一。

### 程式思維

```python
def gcd_by_listing(a, b):
    """定義 2 的直譯：列出所有公因數取最大。只適合很小的數。"""
    assert a != 0 or b != 0
    bound = max(abs(a), abs(b))
    cd = [d for d in range(-bound, bound + 1)
          if d != 0 and a % d == 0 and b % d == 0]
    return max(cd)

assert gcd_by_listing(20, 16) == 4
assert gcd_by_listing(7, 0) == 7 and gcd_by_listing(-20, 16) == 4
```
