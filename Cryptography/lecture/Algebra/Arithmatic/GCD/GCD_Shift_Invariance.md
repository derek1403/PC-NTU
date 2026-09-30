# GCD Shift Invariance (GCD 的平移不變性)

+++

## 證明目標:

`Arithmetic.pdf` p.8–9。歐幾里得演算法的**唯一數學內容**就是這一條：
把一個數加上另一個數的任意倍數，gcd 不變。

* (a)(b) 兩組數的公因數集合互相包含（投影片的 (i)(ii)）：

$$\mathrm{CD}(a, b) \subseteq \mathrm{CD}(a + kb,\ b), \qquad \mathrm{CD}(a + kb,\ b) \subseteq \mathrm{CD}(a, b)$$

* (c) 定理：設 $a \neq 0$ 或 $b \neq 0$，則對任意 $k \in \mathbf{Z}$：

$$\gcd(a, b) = \gcd(a + kb,\ b)$$

* (d) 系理：設 $b > 0$，則

$$\gcd(a, b) = \gcd\left(b,\ a \bmod b\right)$$

* $a,\ b$ : 不全為零的整數 (Integers, not both zero) $[a, b \in \mathbf{Z}]$
* $k$ : 任意整數倍數 (An arbitrary integer multiplier) $[k \in \mathbf{Z}]$
* $\mathrm{CD}(a, b)$ : $a, b$ 的公因數集合 (The set of common divisors of $a$ and $b$) $[\text{集合}]$
* $a \bmod b$ : $a$ 除以 $b$ 的餘數 (The remainder of $a$ divided by $b$) $[a \bmod b \in \left\{0, \dots, b-1\right\}]$
* 註：(c) 右邊的 $\gcd$ 也需要「不全為零」才有定義。這自動成立：若 $b = 0$ 則 $a \neq 0$，而 $a + kb = a \neq 0$。
* 註：投影片寫「(i) $A \subset B$」「(ii) $B \subset A$」，這裡的 $\subset$ 應讀作 $\subseteq$（不要求真包含）；
  兩個真包含不可能同時成立。本檔依 A4 慣例寫成 $\subseteq$。
* 註：(d) 要求 $b > 0$ 是因為 $a \bmod b$ 只對正模數有定義（[取模函數](../Division/Modular_Function.md)）。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [整除的線性組合性質 (Divisibility of linear combinations)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/GCD/Divisibility_Basics.html#a-proof-that-a-common-divisor-divides-every-linear-combination)：** 已於本章 [整除的基本性質](Divisibility_Basics.md)【證明 (a)】完整證明，此處直接引用不再重證

  $$d \mid a,\ \ d \mid b \quad \Longrightarrow \quad d \mid \left(ax + by\right) \qquad \text{for all } x, y \in \mathbf{Z}$$

  * $a,\ b$ : 任意整數 (Arbitrary integers) $[a, b \in \mathbf{Z}]$
  * $d$ : 公因數 (A common divisor) $[d \in \mathbf{Z}]$
  * $x,\ y$ : 組合係數 (Combination coefficients) $[x, y \in \mathbf{Z}]$

* **【已知 2】 [最大公因數的定義與對稱性 (Definition and symmetry of the gcd)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/GCD/Greatest_Common_Divisor.html#d-proof-that-the-gcd-ignores-signs-and-order)：** 已於本章 [最大公因數](Greatest_Common_Divisor.md)【定義 1】【定義 2】【證明 (d)】給出並證明，此處直接引用不再重證

  * (a) 公因數集合與 gcd：

    $$\mathrm{CD}(a, b) = \left\{d \neq 0 \ \middle|\ d \mid a,\ d \mid b\right\}, \qquad \gcd(a, b) = \max\ \mathrm{CD}(a, b)$$

  * (b) 對稱性：

    $$\gcd(a, b) = \gcd(b, a)$$

  * $\mathrm{CD}(a, b)$ : 公因數集合 (The set of common divisors) $[\text{集合}]$
  * $a,\ b$ : 不全為零的整數 (Integers, not both zero) $[a, b \in \mathbf{Z}]$

* **【已知 3】 [取模函數 (Modular function)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/Division/Modular_Function.html#assumptions-preliminaries)：** 已於本章 [取模函數](../Division/Modular_Function.md)【定義 1】給出，此處直接引用

  $$a \bmod b = a - \left\lfloor \frac{a}{b} \right\rfloor b$$

  * $a$ : 被除數 (The dividend) $[a \in \mathbf{Z}]$
  * $b$ : 模數 (The modulus) $[b \in \mathbf{P}]$

+++

## 證明:

### (a) proof that the common divisor set is preserved in the forward direction

依 A4 慣例，先證 $\mathrm{CD}(a, b) \subseteq \mathrm{CD}(a + kb,\ b)$。任取 $d \in \mathrm{CD}(a,b)$：

$$\begin{gather*}
d \in \mathrm{CD}(a, b) &\overset{\text{已知 2(a)}}{\Longrightarrow}& d \mid a,\ \ d \mid b \\
d &\overset{\text{已知 1}}{\mid}& a \times 1 + b \times k \\
d &\in& \mathrm{CD}(a + kb,\ b) \qquad \text{(} d \mid b \text{ 已有)}
\end{gather*}$$

* 註：投影片的寫法是 $a = xd$、$b = yd$ 代入得 $a + kb = \left(x + ky\right)d$ —— 那正是【已知 1】的證明本身，這裡直接引用。

### (b) proof that the common divisor set is preserved in the backward direction

再證 $\mathrm{CD}(a + kb,\ b) \subseteq \mathrm{CD}(a, b)$。任取 $c \in \mathrm{CD}(a+kb, b)$，把 $a$ 寫成兩者的組合 $a = \left(a+kb\right) \times 1 + b \times \left(-k\right)$：

$$\begin{gather*}
c \in \mathrm{CD}(a + kb, b) &\overset{\text{已知 2(a)}}{\Longrightarrow}& c \mid a + kb,\ \ c \mid b \\
c &\overset{\text{已知 1}}{\mid}& \left(a + kb\right) \times 1 + b \times \left(-k\right) \\
c &\mid& a \\
c &\in& \mathrm{CD}(a, b)
\end{gather*}$$

### (c) proof of the shift invariance theorem

【證明 (a)(b)】給出兩個方向的包含，故公因數集合相等，最大值也相等：

$$\begin{gather*}
\mathrm{CD}(a, b) &\overset{\text{證明 (a)(b)}}{=}& \mathrm{CD}(a + kb,\ b) \\
\gcd(a, b) &\overset{\text{已知 2(a)}}{=}& \gcd(a + kb,\ b)
\end{gather*}$$

與投影片的定理一致。

### (d) proof of the corollary using the remainder

設 $b > 0$。取 $k = -\left\lfloor a/b \right\rfloor$，則 $a + kb$ 恰好就是 $a \bmod b$：

$$\begin{gather*}
\gcd(a, b) &\overset{\text{證明 (c)}}{=}& \gcd\left(a - \left\lfloor \frac{a}{b} \right\rfloor b,\ b\right) \\
&\overset{\text{已知 3}}{=}& \gcd\left(a \bmod b,\ b\right) \\
&\overset{\text{已知 2(b)}}{=}& \gcd\left(b,\ a \bmod b\right)
\end{gather*}$$

三步分別對應投影片標註的 [Theorem]、[Definition]、[Proposition]，與投影片一致。

+++

## 意義與密碼學關聯 (Interpretation and Relevance to Cryptography)

### 為什麼「平移」不改變 gcd

想成**同一把尺量兩根木條**：若 $d$ 能量完 $a$ 和 $b$，那麼把 $a$ 接上 $k$ 段 $b$
（或剪掉 $k$ 段 $b$），$d$ 仍然量得完。反過來也一樣。
所以「能同時量完的尺」這個集合根本沒變，最長的那把自然也沒變。

### 系理把問題變小

$\left(a, b\right) \to \left(b,\ a \bmod b\right)$ 這一步保持 gcd 不變，而且
**第二個數嚴格變小**（$0 \le a \bmod b < b$）。重複下去必定走到 $\left(g, 0\right)$，
而 $\gcd(g, 0) = g$ —— 這就是 [歐幾里得演算法](Euclidean_Algorithm.md)。

### 同一個想法的抽象版本

在 Abstract_Algebra 章的語言裡，本檔說的是**理想的相等**：

$$\left\langle a, b \right\rangle = \left\langle a + kb,\ b \right\rangle$$

因為兩邊的生成元可以互相表示。這也解釋了為什麼
[主理想](../../Abstract_Algebra/Ring/Principal_Ideal.md) 的生成元就是 gcd：
歐幾里得演算法不斷換生成元而不改變理想，最後剩下單一生成元。

### 程式思維

```python
from math import gcd
for a in range(-30, 31):
    for b in range(1, 20):
        for k in range(-5, 6):
            assert gcd(a, b) == gcd(a + k * b, b)      # 證明 (c)
        assert gcd(a, b) == gcd(b, a % b)              # 證明 (d)
```
