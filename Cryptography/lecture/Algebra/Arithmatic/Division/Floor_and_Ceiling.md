# Floor and Ceiling (取整函數：地板與天花板)

+++

## 證明目標:

`Arithmetic.pdf` p.3（上半）。整章第一塊積木 —— 取模運算 $n \bmod m$ 就是用地板函數定義的。

* (a) 地板與天花板**存在**，並滿足基本夾擠不等式：

$$\left\lfloor x \right\rfloor \le x < \left\lfloor x \right\rfloor + 1, \qquad \left\lceil x \right\rceil - 1 < x \le \left\lceil x \right\rceil$$

* (b) 地板的刻畫：夾在 $x$ 下方一格之內的整數**只有一個**：

$$n \in \mathbf{Z},\ \ n \le x < n + 1 \quad \Longrightarrow \quad n = \left\lfloor x \right\rfloor$$

* (c) 驗證投影片的四個例子：

$$\left\lfloor e \right\rfloor = 2, \qquad \left\lceil e \right\rceil = 3, \qquad \left\lfloor -3.1416 \right\rfloor = -4, \qquad \left\lceil -3.1416 \right\rceil = -3$$

* $x$ : 任意實數 (An arbitrary real number) $[x \in \mathbf{R}]$
* $n$ : 整數 (An integer) $[n \in \mathbf{Z}]$
* $\left\lfloor x \right\rfloor$ : 地板函數值 (The floor of $x$) $[\mathbf{R} \to \mathbf{Z}]$
* $\left\lceil x \right\rceil$ : 天花板函數值 (The ceiling of $x$) $[\mathbf{R} \to \mathbf{Z}]$
* $e$ : 自然對數的底 (Euler's number) $[e \in \mathbf{R}]$，$e \approx 2.71828$
* 註：**負數要特別小心**。$\left\lfloor -3.1416 \right\rfloor = -4$ 不是 $-3$ ——
  地板是「往 $-\infty$ 方向取整」，不是「把小數點後砍掉」。
  Python 的 `int(-3.1416)` 得 `-3`（砍掉），`math.floor(-3.1416)` 才得 `-4`。
* 註：(b) 是後續所有「取模」證明的引擎 —— 要證某個整數等於 $\left\lfloor x \right\rfloor$，
  只需驗證它落在 $\left[x-1,\ x\right]$ 那個半開區間裡。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [阿基米德性與整數的完備性 (Archimedean property and the completeness of the integers)](https://mathworld.wolfram.com/ArchimedeanProperty.html)：** 實數系的標準結果，本章直接引用不再重證

  * (a) 阿基米德性：任何實數都被兩個整數夾住

    $$\forall\, x \in \mathbf{R}, \ \exists\, n_1, n_2 \in \mathbf{Z} \ \text{ such that } \ n_1 \le x \le n_2$$

  * (b) 整數的非空子集若有上界則有最大元素，若有下界則有最小元素：

    $$\varnothing \neq S \subseteq \mathbf{Z},\ S \ \text{有上界} \quad \Longrightarrow \quad \max S \ \text{存在}$$

  * $x$ : 任意實數 (An arbitrary real number) $[x \in \mathbf{R}]$
  * $n_1,\ n_2$ : 夾住 $x$ 的兩個整數 (Two integers bracketing $x$) $[n_1, n_2 \in \mathbf{Z}]$
  * $S$ : 整數的子集 (A subset of the integers) $[S \subseteq \mathbf{Z}]$
  * 註：(b) 的「有下界則有最小元素」是 (b) 對 $-S$ 的版本，也是良序原理的推廣。

* **【已知 2】 [兩個常數的數值 (Numerical values of two constants)](https://mathworld.wolfram.com/e.html)：** 標準數值，本章直接引用

  $$2 < e < 3, \qquad e \approx 2.71828$$

  * $e$ : 自然對數的底 (Euler's number) $[e \in \mathbf{R}]$

* **【定義 1】 地板與天花板 (Floor and ceiling)：**

  * (a) 地板：不超過 $x$ 的最大整數

    $$\left\lfloor x \right\rfloor \overset{\text{def}}{=} \max\left\{n \in \mathbf{Z} \ \middle|\ n \le x\right\}$$

  * (b) 天花板：不小於 $x$ 的最小整數

    $$\left\lceil x \right\rceil \overset{\text{def}}{=} \min\left\{n \in \mathbf{Z} \ \middle|\ n \ge x\right\}$$

  * $\left\lfloor x \right\rfloor$ : 地板函數值 (The floor of $x$) $[\mathbf{R} \to \mathbf{Z}]$
  * $\left\lceil x \right\rceil$ : 天花板函數值 (The ceiling of $x$) $[\mathbf{R} \to \mathbf{Z}]$
  * $x$ : 任意實數 (An arbitrary real number) $[x \in \mathbf{R}]$
  * $n$ : 候選整數 (A candidate integer) $[n \in \mathbf{Z}]$
  * 註：「$\max$、$\min$ 存在」這件事**不是**定義的一部分，而是要證的 —— 見【證明 (a)】。

+++

## 證明:

### (a) proof of existence and the sandwich inequality

**先證地板存在。** 令 $S = \left\{n \in \mathbf{Z} \mid n \le x\right\}$。由阿基米德性它非空，且以 $x$ 為上界：

$$\begin{gather*}
n_1 &\overset{\text{已知 1(a)}}{\le}& x \qquad \text{for some } n_1 \in \mathbf{Z} \\
n_1 &\in& S \\
S &\neq& \varnothing \\
n &\le& x \qquad \text{for all } n \in S \\
\max S &\overset{\text{已知 1(b)}}{\in}& S \qquad \text{(最大元素存在)} \\
\left\lfloor x \right\rfloor &\overset{\text{定義 1(a)}}{=}& \max S
\end{gather*}$$

**再證夾擠不等式。** $\left\lfloor x \right\rfloor \in S$ 給出左半；$\left\lfloor x \right\rfloor + 1$ 比最大元素還大，
故不在 $S$ 裡，給出右半：

$$\begin{gather*}
\left\lfloor x \right\rfloor &\overset{\text{定義 1(a)}}{\le}& x \\
\left\lfloor x \right\rfloor + 1 &>& \max S \\
\left\lfloor x \right\rfloor + 1 &\notin& S \\
\left\lfloor x \right\rfloor + 1 &\overset{\text{定義 1(a)}}{>}& x
\end{gather*}$$

**天花板完全對稱。** $T = \left\{n \in \mathbf{Z} \mid n \ge x\right\}$ 由【已知 1(a)】的 $n_2$ 知非空、以 $x$ 為下界，
由【已知 1(b)】（下界版本）最小元素存在；$\left\lceil x \right\rceil - 1$ 比最小元素還小故不在 $T$ 裡：

$$\begin{gather*}
\left\lceil x \right\rceil &\overset{\text{定義 1(b)}}{\ge}& x \\
\left\lceil x \right\rceil - 1 &<& \min T \\
\left\lceil x \right\rceil - 1 &\overset{\text{定義 1(b)}}{<}& x
\end{gather*}$$

兩條夾擠不等式都成立。

### (b) proof of the characterization of the floor

設整數 $n$ 滿足 $n \le x < n+1$。一方面 $n \in S$，故不超過最大元素；
另一方面 $\left\lfloor x \right\rfloor \le x < n + 1$，而兩者都是整數：

$$\begin{gather*}
n &\overset{\text{定義 1(a)}}{\le}& \left\lfloor x \right\rfloor \\
\left\lfloor x \right\rfloor &\overset{\text{證明 (a)}}{\le}& x \\
\left\lfloor x \right\rfloor &<& n + 1 \\
\left\lfloor x \right\rfloor &\le& n \qquad \text{(兩邊都是整數)} \\
\left\lfloor x \right\rfloor &=& n
\end{gather*}$$

* 註：同理可得天花板的刻畫：$n - 1 < x \le n \Rightarrow n = \left\lceil x \right\rceil$。

### (c) verify the four examples from the slides

每個例子都只要找出**夾住它的那個整數**，再套【證明 (b)】（天花板用 (b) 的對稱版本）：

$$\begin{gather*}
2 &\overset{\text{已知 2}}{<}& e \\
e &\overset{\text{已知 2}}{<}& 2 + 1 \\
\left\lfloor e \right\rfloor &\overset{\text{證明 (b)}}{=}& 2 \\
\left\lceil e \right\rceil &\overset{\text{證明 (b)}}{=}& 3 \qquad \text{(因 } 3 - 1 < e \le 3 \text{)} \\
-4 &\le& -3.1416 \\
-3.1416 &<& -4 + 1 \\
\left\lfloor -3.1416 \right\rfloor &\overset{\text{證明 (b)}}{=}& -4 \\
\left\lceil -3.1416 \right\rceil &\overset{\text{證明 (b)}}{=}& -3 \qquad \text{(因 } -3 - 1 < -3.1416 \le -3 \text{)}
\end{gather*}$$

四個值都與投影片一致。

+++

## 意義與密碼學關聯 (Interpretation and Relevance to Cryptography)

### 地板函數是「除法」的整數版

整數除法 $n / m$ 通常不是整數。地板函數把它**壓回整數**，而且壓的方向是固定的（往 $-\infty$）：

$$\left\lfloor \frac{25}{7} \right\rfloor = 3, \qquad \left\lfloor \frac{-25}{7} \right\rfloor = -4$$

這個「固定往下」的選擇，正是下一檔 [取模函數](Modular_Function.md) 能保證餘數**永遠非負**的原因。

### 程式語言的陷阱

| 語言 | `-25 / 7` 的整數除法 | `-25 % 7` |
|---|---|---|
| Python `//`、`%` | `-4`（地板） | `3`（非負） |
| C / Java `/`、`%` | `-3`（往零截斷） | `-4`（可能為負） |

密碼學實作若在 C 裡直接用 `%` 處理可能為負的中間值（例如 $a - b \bmod p$），
會得到**負的餘數**，後續查表或比較就會出錯。標準修法是 `((a - b) % p + p) % p`，
其本質就是把「往零截斷」修正成本檔的「往下取整」。

### 程式思維

```python
import math
assert math.floor(math.e) == 2 and math.ceil(math.e) == 3
assert math.floor(-3.1416) == -4 and math.ceil(-3.1416) == -3
assert int(-3.1416) == -3          # int() 是截斷，不是地板！
assert -25 // 7 == -4 and -25 % 7 == 3
```
