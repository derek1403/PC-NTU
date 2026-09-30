# Roots of x^q − x (x^q − x 的根)

+++

## 證明目標:

`FiniteFields.pdf` p.19（下半）、p.32、p.34（中段）；補充講義 §7.7.2（Theorem 7.12、Exercise 11(b)、12）。
有限體最核心的一條恆等式：**$GF(q)$ 的元素恰好是 $x^q - x$ 的全部根。**
它把「一個體」與「一個多項式」綁在一起，是存在性、唯一性、子體定理的共同起點。

* (a) 補充講義 Theorem 7.12 前半（有限體版的費馬小定理）：

$$\beta \in GF(q)^* \ \Longrightarrow \ \beta^{q-1} = 1, \qquad \beta \in GF(q) \ \Longrightarrow \ \beta^{q} = \beta$$

* (b) 補充講義 (7.3)(7.4)：

$$x^{q-1} - 1 = \prod_{\beta \in GF(q)^*}\left(x - \beta\right), \qquad x^{q} - x = \prod_{\beta \in GF(q)}\left(x - \beta\right)$$

* (c) 投影片 p.32 的 Proposition：在任何特徵為 $p$ 的體 $L$ 中，

$$K = \left\{\alpha \in L \ \middle|\ \alpha^{p^n} = \alpha\right\} \ \text{是 } L \text{ 的子體}$$

* (d) 補充講義 Exercise 11(b)（威爾遜定理）：

$$\left(p - 1\right)! \equiv -1 \pmod{p} \qquad \left(p \ \text{為質數}\right)$$

* $GF(q)$ : $q$ 元素的有限體 (The finite field with $q$ elements) $[\text{體}]$
* $GF(q)^*$ : 其非零元素構成的乘法群 (Its multiplicative group) $[\text{群}]$
* $\beta$ : 體元素 (A field element) $[\beta \in GF(q)]$
* $L$ : 特徵 $p$ 的任意體 (Any field of characteristic $p$) $[\text{體}]$
* $K$ : $x^{p^n} - x$ 在 $L$ 中的根集 (The set of roots of $x^{p^n} - x$ in $L$) $[K \subseteq L]$
* $p$ : 質數 (A prime) $[p \in \mathbf{P}]$
* $n$ : 正整數 (A positive integer) $[n \in \mathbf{P}]$
* 註：(a) 取 $q = p$ 就是 [費馬小定理](../../Abstract_Algebra/Group/Order_of_Element_and_Cyclic_Subgroup.md)【證明 (d)】；證明方法相同（拉格朗日）。
* 註：投影片 p.19 的「Each field element is a root of $x^8 - x$」是 (a) 取 $q = 8$ 的特例，
  已於 [伽羅瓦體 GF(8) 與 GF(16)](../Construction/Galois_Fields_GF8_and_GF16.md)【證明 (d)】逐一驗證。
* 註：(c) **不需要事先知道 $K$ 有幾個元素**；「恰有 $p^n$ 個」要配合重根判準，見 [$GF(p^n)$ 的存在性](Existence_of_GF_p_n.md)。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [體的定義 (Definition of a field)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Field/Field_Definition.html#assumptions-preliminaries)：** 已於 [體的定義](../../Abstract_Algebra/Field/Field_Definition.md)【定義 1】給出，此處直接引用

  $$\left(F \setminus \left\{0\right\}, \times\right) \ \text{為阿貝爾群}, \qquad \left|F^*\right| = \left|F\right| - 1$$

  * $F$ : 體 (A field) $[\text{體}]$
  * $F^*$ : 非零元素的乘法群 (The multiplicative group) $[F \setminus \left\{0\right\}]$

* **【已知 2】 [元素的階整除群的階與指數律 (Order divides group order; exponent laws)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Group/Order_of_Element_and_Cyclic_Subgroup.html#b-proof-that-the-order-of-an-element-divides-the-order-of-the-group)：** 已於 [元素的階與循環子群](../../Abstract_Algebra/Group/Order_of_Element_and_Cyclic_Subgroup.md)【已知 1(b)】【定義 1】【證明 (b)】完整證明，此處直接引用不再重證

  * (a) 階整除群的階：

    $$o(\beta) \ \Big|\ \left|G\right|$$

  * (b) 指數律與階的定義：

    $$\beta^{mk} = \left(\beta^{m}\right)^{k}, \qquad \beta^{o(\beta)} = 1$$

  * $G$ : 有限群 (A finite group) $[\text{群}]$
  * $m,\ k$ : 整數 (Integers) $[m, k \in \mathbf{Z}]$

* **【已知 3】 [多項式的根 (Roots of polynomials)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Finite_Fields/Polynomial_Arithmetic/Roots_of_Polynomials.html#c-proof-that-n-distinct-roots-determine-the-factorization)：** 已於本章 [多項式的根](../Polynomial_Arithmetic/Roots_of_Polynomials.md)【證明 (c)】完整證明，此處直接引用不再重證

  $$f \ \text{首一},\ \deg f = N,\ f \ \text{有 } N \text{ 個相異根 } \beta_1, \dots, \beta_N \quad \Longrightarrow \quad f = \prod_{i=1}^{N}\left(x - \beta_i\right)$$

  * $f$ : 首一多項式 (A monic polynomial) $[f \in F[x]]$
  * $N$ : 次數 (The degree) $[N \in \mathbf{P}]$

* **【已知 4】 [新生之夢 (Freshman's dream)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Field/Freshmans_Dream.html#b-proof-of-the-inductive-step)：** 已於 [新生之夢](../../Abstract_Algebra/Field/Freshmans_Dream.md)【證明 (b)】完整證明，此處直接引用不再重證

  $$\mathrm{ch}(L) = p \quad \Longrightarrow \quad \left(a + b\right)^{p^n} = a^{p^n} + b^{p^n}$$

  * $a,\ b$ : 體元素 (Field elements) $[a, b \in L]$

* **【已知 5】 [子體判別法 (Subfield criterion)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Field/Subfield_and_Field_Extension.html#a-proof-of-the-subfield-criterion)：** 已於 [子體與體擴張](../../Abstract_Algebra/Field/Subfield_and_Field_Extension.md)【證明 (a)】完整證明，此處直接引用不再重證

  $$K \ \text{是 } L \text{ 的子體} \quad \Longleftrightarrow \quad \left|K\right| \ge 2, \quad u - v \in K, \quad uv^{-1} \in K \ \left(v \neq 0\right)$$

  * $u,\ v$ : $K$ 的元素 (Elements of $K$) $[u, v \in K]$

* **【假設 1】 $q$ 元素的有限體 (A finite field with q elements)：** 【證明 (a)(b)(d)】的前提

  $$\left|F\right| = q < \infty$$

  * $F$ : 有限體，即 $GF(q)$ (The finite field $GF(q)$) $[\text{體}]$

* **【假設 2】 特徵 $p$ 的體 (A field of characteristic p)：** 【證明 (c)】的前提

  $$\mathrm{ch}(L) = p$$

  * $L$ : 任意特徵 $p$ 的體（有限或無限）(Any field of characteristic $p$) $[\text{體}]$

* **【定義 1】 根集 (The root set)：** 投影片 p.32

  $$K \overset{\text{def}}{=} \left\{\alpha \in L \ \middle|\ \alpha^{p^n} - \alpha = 0\right\}$$

  * $K$ : $x^{p^n} - x$ 在 $L$ 中的根集 (The roots of $x^{p^n} - x$ in $L$) $[K \subseteq L]$

* **【推導 1】 負號穿過 $p^n$ 次方 (The sign passes through the p^n-th power)：** 投影片 p.32 分兩種情形

  * (a) $p$ 為奇質數：$p^n$ 為奇數

    $$\left(-\alpha\right)^{p^n} = \left(-1\right)^{p^n}\alpha^{p^n} = -\alpha^{p^n}$$

  * (b) $p = 2$：特徵 $2$ 中 $-1 = 1$

    $$\left(-\alpha\right)^{2^n} = \alpha^{2^n} = -\alpha^{2^n}$$

  * $\alpha$ : 體元素 (A field element) $[\alpha \in L]$

+++

## 證明:

### (a) proof that every element satisfies the finite field version of Fermat's theorem

設 $\beta \in F^*$。$F^*$ 是 $q - 1$ 階的群，$\beta$ 的階整除 $q - 1$：

$$\begin{gather*}
\left|F^*\right| &\overset{\text{已知 1,假設 1}}{=}& q - 1 \\
o(\beta) &\overset{\text{已知 2(a)}}{\Big|}& q - 1 \\
\beta^{q-1} &\overset{\text{已知 2(b)}}{=}& \left(\beta^{o(\beta)}\right)^{\left(q-1\right)/o(\beta)} \\
\beta^{q-1} &\overset{\text{已知 2(b)}}{=}& 1
\end{gather*}$$

兩邊乘以 $\beta$ 得 $\beta^q = \beta$；對 $\beta = 0$，$0^q = 0$ 也成立。與補充講義 Theorem 7.12 一致。

### (b) proof that the field is exactly the root set of x to the q minus x

由【證明 (a)】，$F^*$ 的 $q - 1$ 個相異元素都是首一 $q - 1$ 次多項式 $x^{q-1} - 1$ 的根；
$F$ 的 $q$ 個相異元素都是首一 $q$ 次多項式 $x^q - x$ 的根：

$$\begin{gather*}
x^{q-1} - 1 &\overset{\text{已知 3,證明 (a)}}{=}& \prod_{\beta \in F^*}\left(x - \beta\right) \\
x^{q} - x &\overset{\text{已知 3,證明 (a)}}{=}& \prod_{\beta \in F}\left(x - \beta\right)
\end{gather*}$$

與補充講義 (7.3)(7.4) 一致。**驗證**（補充講義 Exercise 12(a)，$F = GF(5)$）：

$$\begin{gather*}
\left(x - 1\right)\left(x - 4\right) &=& x^2 - 5x + 4 \equiv x^2 + 4 \\
\left(x - 2\right)\left(x - 3\right) &=& x^2 - 5x + 6 \equiv x^2 + 1 \\
\left(x^2 + 4\right)\left(x^2 + 1\right) &=& x^4 + 5x^2 + 4 \equiv x^4 - 1
\end{gather*}$$

* 註：「多項式 $x^q - x$」與「函數 $\beta \mapsto \beta^q - \beta$」必須分清楚：
  **作為函數它在 $F$ 上恆為零，作為多項式它不是零**（補充講義 §7.5 的腳註）。

### (c) proof that the roots of x to the p to the n minus x form a subfield

由【假設 2】與【定義 1】逐條驗證【已知 5】。**至少兩個元素**：

$$\begin{gather*}
0^{p^n} &=& 0 \\
1^{p^n} &=& 1 \\
0,\ 1 &\overset{\text{定義 1}}{\in}& K
\end{gather*}$$

**減法封閉**：設 $\alpha_1, \alpha_2 \in K$：

$$\begin{gather*}
\left(\alpha_1 - \alpha_2\right)^{p^n} &\overset{\text{已知 4,假設 2}}{=}& \alpha_1^{p^n} + \left(-\alpha_2\right)^{p^n} \\
&\overset{\text{推導 1(a)(b)}}{=}& \alpha_1^{p^n} - \alpha_2^{p^n} \\
&\overset{\text{定義 1}}{=}& \alpha_1 - \alpha_2
\end{gather*}$$

**除法封閉**：設 $\alpha_2 \neq 0$，乘法交換故冪次可以分配，反元素的冪次等於冪次的反元素：

$$\begin{gather*}
\left(\alpha_1 \alpha_2^{-1}\right)^{p^n} &=& \alpha_1^{p^n}\left(\alpha_2^{p^n}\right)^{-1} \\
&\overset{\text{定義 1}}{=}& \alpha_1 \alpha_2^{-1}
\end{gather*}$$

三條全中，$K$ 是 $L$ 的子體：

$$K \overset{\text{已知 5}}{=} L \text{ 的子體}$$

與投影片 p.32 一致（投影片把加法、乘法、負元素、反元素分四條驗，本檔合併為子體判別法的兩條）。

* 註：**加法封閉是整個證明唯一不平凡的地方** —— 它需要新生之夢，也就是需要特徵 $p$。
  在 $\mathbf{C}$ 裡 $x^3 - x$ 的根 $\left\{0, 1, -1\right\}$ 就不對加法封閉（$1 + 1 = 2$ 不是根）。

### (d) proof of Wilson's theorem

取 $F = GF(p)$，比較【證明 (b)】第一式兩邊的常數項：

$$\begin{gather*}
x^{p-1} - 1 &\overset{\text{證明 (b)}}{=}& \prod_{\beta = 1}^{p-1}\left(x - \beta\right) \\
-1 &=& \prod_{\beta = 1}^{p-1}\left(-\beta\right) \qquad \text{(令 } x = 0\text{)} \\
-1 &=& \left(-1\right)^{p-1}\left(p - 1\right)! \\
-1 &\equiv& \left(p - 1\right)! \pmod{p} \qquad \text{(} p \text{ 奇數時 } p - 1 \text{ 偶；} p = 2 \text{ 時 } -1 \equiv 1\text{)}
\end{gather*}$$

**驗證** $p = 3, 5, 7$：

$$\begin{gather*}
2! &=& 2 \equiv -1 \pmod 3 \\
4! &=& 24 \equiv -1 \pmod 5 \\
6! &=& 720 = 7 \cdot 102 + 6 \equiv -1 \pmod 7
\end{gather*}$$

與補充講義 Exercise 11(b) 一致。

+++

## 意義與密碼學關聯 (Interpretation and Relevance to Cryptography)

### 「冪次 $q$ 等於什麼都沒做」

(a) 的 $\beta^q = \beta$ 意味著 $GF(q)$ 裡的指數**只在模 $q - 1$ 下有意義**：

$$\beta^{e} = \beta^{e \bmod \left(q - 1\right)} \qquad \left(\beta \neq 0\right)$$

這是所有離散對數密碼系統的共同骨架：DH 的共享金鑰 $g^{ab}$、ElGamal 的解密、DSA 的簽章，
指數運算全部在 $\mathbf{Z}_{q-1}$（或其子群的階）裡進行。

### 反元素的第二種算法

(a) 立刻給出 $\beta^{-1} = \beta^{q-2}$。在 AES 的 $GF(2^8)$ 中：

$$\beta^{-1} = \beta^{254}$$

它只用平方與乘法（$254 = 11111110_2$），**沒有資料相依的分支**，
因此是 AES S-box 常數時間實作的標準做法之一（相對於 [歐幾里得整環](../Polynomial_Arithmetic/Euclidean_Domain.md) 的擴展歐幾里得）。

### (b) 讓「$GF(q)$ = 多項式的根」成為可計算的事實

(b) 說 $x^q - x$ 在 $GF(q)$ 上**完全分解且無重根**。
Cantor–Zassenhaus 等分解演算法第一步都會計算 $\gcd\left(f,\ x^q - x\right)$，
抽出 $f$ 在 $GF(q)$ 中的全部一次因式（即全部根）—— 這是 Reed–Solomon 解碼與
ECC 點解壓縮（求平方根）中的實際操作。

### 程式思維

```python
p, q = 5, 5
assert all(pow(b, q, p) == b for b in range(p))            # 證明 (a)：b^q = b
from math import factorial
assert all(factorial(p - 1) % p == p - 1 for p in (2, 3, 5, 7, 11, 13))   # 證明 (d)：威爾遜
```
