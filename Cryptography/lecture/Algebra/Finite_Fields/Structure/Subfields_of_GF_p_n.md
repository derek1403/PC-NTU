# Subfields of GF(p^n) (GF(p^n) 的子體)

+++

## 證明目標:

`FiniteFields.pdf` p.37；補充講義 §7.9（Theorem 7.25）與 Example 3（續）。
$GF(p^n)$ 的子體結構**完全由 $n$ 的因數決定**：每個因數 $d$ 恰好對應一個子體 $GF(p^d)$，
包含關係就是整除關係。

* (a) 投影片 p.37 的 Proposition：

$$K \ \text{是 } GF(p^n) \text{ 的子體} \quad \Longrightarrow \quad \left|K\right| = p^d, \ d \mid n$$

* (b) 補充講義 Theorem 7.25（加強為唯一）：對每個 $d \mid n$，$GF(p^n)$ **恰有一個** $p^d$ 元素的子體，即

$$R_d = \left\{y \in GF(p^n) \ \middle|\ y^{p^d} = y\right\}$$

* (c) 投影片 p.37 的 Example：$GF(2^{24})$ 的子體格（Hasse 圖）。
* (d) 補充講義 Example 3：$GF(16)$ 的子體為 $GF(2) = \left\{0, 1\right\}$ 與 $GF(4) = \left\{0, 1, \gamma^5, \gamma^{10}\right\}$。

* $F$ : $p^n$ 元素的體 (The field with $p^n$ elements) $[F = GF(p^n)]$
* $K$ : $F$ 的子體 (A subfield of $F$) $[K \subseteq F]$
* $d$ : $n$ 的正因數 (A positive divisor of $n$) $[d \in \mathbf{P},\ d \mid n]$
* $R_d$ : $x^{p^d} - x$ 在 $F$ 中的根集 (The roots of $x^{p^d} - x$ in $F$) $[R_d \subseteq F]$
* $\gamma$ : $GF(16)$ 的本原元，$\gamma^4 = \gamma + 1$ (A primitive element of $GF(16)$) $[\gamma \in GF(16)]$
* 註：投影片 p.37 只寫「Any subfield of $GF_{p^n}$ is of the form $GF_{p^d}$, $d \mid n$」（必要條件）；
  補充講義 Theorem 7.25 寫「has a subfield … for each $n$ that divides $m$」（存在性）；本檔兩者皆證並補上**唯一性**。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [有限體的階與質子體 (Order of a finite field and the prime subfield)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Finite_Fields/Structure/Order_of_a_Finite_Field.html#b-proof-that-the-order-of-a-finite-field-is-a-prime-power)：** 已於本章 [有限體的階](Order_of_a_Finite_Field.md)【證明 (a)(b)】完整證明，此處直接引用不再重證

  $$\left|K\right| < \infty \quad \Longrightarrow \quad \left|K\right| = p^{\left[K : P\right]}, \quad P \cong GF(p)$$

  * 註：子體 $K$ 與 $F$ 共用 $1$，故兩者的質子體是同一個 $P$、特徵同為 $p$。

* **【已知 2】 [塔定理 (Tower law)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Field/Tower_Law.html#a-proof-of-the-tower-law)：** 已於 [塔定理](../../Abstract_Algebra/Field/Tower_Law.md)【證明 (a)】完整證明，此處直接引用不再重證

  $$P \subseteq K \subseteq F \quad \Longrightarrow \quad \left[F : P\right] = \left[F : K\right]\left[K : P\right]$$

* **【已知 3】 [x^q − x 的根 (Roots of x^q − x)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Finite_Fields/Structure/Roots_of_x_q_minus_x.html#c-proof-that-the-roots-of-x-to-the-p-to-the-n-minus-x-form-a-subfield)：** 已於本章 [$x^q - x$ 的根](Roots_of_x_q_minus_x.md)【證明 (a)(c)】完整證明，此處直接引用不再重證

  * (a) 有限體的元素滿足 $y^{\left|K\right|} = y$：

    $$\left|K\right| = q \quad \Longrightarrow \quad y^q = y \quad \forall y \in K$$

  * (b) 根集是子體：

    $$\left\{y \in F \ \middle|\ y^{p^d} = y\right\} \ \text{是 } F \text{ 的子體}$$

* **【已知 4】 [有限體的乘法群是循環群 (The multiplicative group is cyclic)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Finite_Fields/Multiplicative_Group/Cyclic_Multiplicative_Group_of_Finite_Field.html#b-proof-that-the-multiplicative-group-of-a-finite-field-is-cyclic)：** 已於本章 [有限體的乘法群是循環群](../Multiplicative_Group/Cyclic_Multiplicative_Group_of_Finite_Field.md)【證明 (b)】完整證明，此處直接引用不再重證

  $$F^* = \left\langle \omega \right\rangle, \qquad o(\omega) = p^n - 1$$

  * $\omega$ : 本原元 (A primitive element) $[\omega \in F^*]$

* **【已知 5】 [冪次為單位元素的條件 (When a power is the identity)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Finite_Fields/Multiplicative_Group/Euler_Phi_and_Cyclic_Group_Orders.html#a-proof-that-a-power-is-the-identity-exactly-when-the-order-divides-the-exponent)：** 已於本章 [尤拉函數與循環群中元素的階](../Multiplicative_Group/Euler_Phi_and_Cyclic_Group_Orders.md)【證明 (a)】完整證明，此處直接引用不再重證

  $$\omega^k = 1 \quad \Longleftrightarrow \quad o(\omega) \mid k$$

  * $k$ : 整數 (An integer) $[k \in \mathbf{Z}]$

* **【假設 1】 $p^n$ 元素的體 (The field with p^n elements)：**

  $$F = GF(p^n), \qquad \left[F : P\right] = n$$

* **【假設 2】 $F$ 的一個子體 (A subfield of F)：** 【證明 (a)】的出發點

  $$K \subseteq F \ \text{為子體}$$

* **【定義 1】 根集 (The root set)：**

  $$R_d \overset{\text{def}}{=} \left\{y \in F \ \middle|\ y^{p^d} = y\right\}$$

  * $R_d$ : $x^{p^d} - x$ 在 $F$ 中的根集 (The roots of $x^{p^d} - x$ in $F$) $[R_d \subseteq F]$

* **【推導 1】 $d \mid n$ 時 $p^d - 1$ 整除 $p^n - 1$ (p^d − 1 divides p^n − 1)：** 設 $n = dt$，等比級數

  $$\begin{gather*}
  p^n - 1 &=& \left(p^d\right)^t - 1 \\
  p^n - 1 &=& \left(p^d - 1\right)\left(p^{d(t-1)} + p^{d(t-2)} + \cdots + p^d + 1\right) \\
  M &\overset{\text{let}}{=}& \frac{p^n - 1}{p^d - 1} \in \mathbf{P}
  \end{gather*}$$

  * $t$ : $n / d$ (The quotient $n/d$) $[t \in \mathbf{P}]$
  * $M$ : 商 (The quotient) $[M \in \mathbf{P}]$

+++

## 證明:

### (a) proof that every subfield has p to the d elements with d dividing n

$K$ 是有限體，由【已知 1】$\left|K\right| = p^d$，$d = \left[K : P\right]$；再由塔定理：

$$\begin{gather*}
\left|K\right| &\overset{\text{假設 2,已知 1}}{=}& p^{d}, \qquad d = \left[K : P\right] \\
n &\overset{\text{假設 1}}{=}& \left[F : P\right] \\
n &\overset{\text{已知 2}}{=}& \left[F : K\right] \cdot d \\
d &\mid& n
\end{gather*}$$

與投影片 p.37 的 Proposition 一致。

### (b) proof that each divisor gives exactly one subfield

**存在**：$R_d$ 是子體（【已知 3(b)】）。數它的元素：非零元素寫成 $\omega^k$（$0 \le k < p^n - 1$），用【推導 1】的 $M$：

$$\begin{gather*}
\omega^k \in R_d &\overset{\text{定義 1}}{\Longleftrightarrow}& \omega^{k\left(p^d - 1\right)} = 1 \\
\omega^{k\left(p^d - 1\right)} = 1 &\overset{\text{已知 4,已知 5}}{\Longleftrightarrow}& \left(p^n - 1\right) \mid k\left(p^d - 1\right) \\
\left(p^n - 1\right) \mid k\left(p^d - 1\right) &\overset{\text{推導 1}}{\Longleftrightarrow}& M \mid k \\
\left|R_d \setminus \left\{0\right\}\right| &=& \frac{p^n - 1}{M} = p^d - 1 \\
\left|R_d\right| &=& p^d
\end{gather*}$$

**唯一**：若 $K$ 是任一 $p^d$ 元素的子體，其元素都滿足 $y^{p^d} = y$，故 $K \subseteq R_d$，兩者等大：

$$\begin{gather*}
y^{p^d} &\overset{\text{已知 3(a)}}{=}& y \qquad \forall y \in K \\
K &\overset{\text{定義 1}}{\subseteq}& R_d \\
K &=& R_d \qquad \text{(} \left|K\right| = \left|R_d\right| = p^d\text{)}
\end{gather*}$$

與補充講義 Theorem 7.25 一致。

### (c) verify the lattice of subfields of GF(2 to the 24)

$24$ 的因數為 $1, 2, 3, 4, 6, 8, 12, 24$，由【證明 (b)】對應八個子體 $GF(2^d)$。
**包含關係等於整除關係**：若 $GF(2^d) \subseteq GF(2^e)$，對 $GF(2^e)$ 套【證明 (a)】得 $d \mid e$；
反之若 $d \mid e$，$GF(2^e)$ 內的 $2^d$ 元素子體也是 $GF(2^{24})$ 的 $2^d$ 元素子體，由【證明 (b)】的唯一性它就是 $GF(2^d)$：

$$\begin{gather*}
GF(2^d) \subseteq GF(2^e) &\overset{\text{證明 (a)}}{\Longrightarrow}& d \mid e \\
d \mid e &\overset{\text{證明 (b)}}{\Longrightarrow}& GF(2^d) \subseteq GF(2^e)
\end{gather*}$$

Hasse 圖的邊是「$d \mid e$ 且中間沒有其他因數」的配對：

$$\left(1,2\right),\ \left(1,3\right),\ \left(2,4\right),\ \left(2,6\right),\ \left(3,6\right),\ \left(4,8\right),\ \left(4,12\right),\ \left(6,12\right),\ \left(8,24\right),\ \left(12,24\right)$$

與投影片 p.37 的圖**逐條一致**（以 Python 驗算，見文末）。

* 註：**$GF(2^8)$ 與 $GF(2^{12})$ 互不包含**（$8 \nmid 12$、$12 \nmid 8$），它們的交集是 $GF(2^4)$（$\gcd(8, 12) = 4$）。
  一般地 $GF(p^d) \cap GF(p^e) = GF\!\left(p^{\gcd(d,e)}\right)$。

### (d) verify the subfields of the field with sixteen elements

$n = 4$，因數 $d = 1, 2, 4$。以本原元 $\gamma$（$o(\gamma) = 15$）套【證明 (b)】：

$$\begin{gather*}
R_1 &\overset{\text{證明 (b)}}{=}& \left\{0\right\} \cup \left\{\gamma^k \ \middle|\ 15 \mid k\right\} = \left\{0, 1\right\} \\
R_2 &\overset{\text{證明 (b)}}{=}& \left\{0\right\} \cup \left\{\gamma^k \ \middle|\ 5 \mid k\right\} = \left\{0, 1, \gamma^5, \gamma^{10}\right\} \\
R_4 &\overset{\text{證明 (b)}}{=}& GF(16)
\end{gather*}$$

（$d = 1$：$M = 15/1 = 15$；$d = 2$：$M = 15/3 = 5$。）與補充講義 Example 3 一致：
$GF(4)^* = \left\{1, \gamma^5, \gamma^{10}\right\}$ 恰是 $GF(16)^*$ 中階整除 $3$ 的元素。

+++

## 意義與密碼學關聯 (Interpretation and Relevance to Cryptography)

### AES 的 $GF(2^8)$ 裡藏著 $GF(16)$、$GF(4)$、$GF(2)$

$8$ 的因數是 $1, 2, 4, 8$，所以 $GF(2^8) \supset GF(2^4) \supset GF(2^2) \supset GF(2)$ —— 一條**鏈**。
這條鏈正是 AES S-box 緊湊實作的塔：

$$GF(2^8) \cong GF\!\left(\left(2^4\right)^2\right), \quad GF(2^4) \cong GF\!\left(\left(2^2\right)^2\right)$$

每一層都是二次擴張，求逆公式簡單（二次擴張裡 $\left(a + b\theta\right)^{-1}$ 有封閉形式），
整個 $GF(2^8)$ 求逆就降到幾次 $GF(4)$ 的運算。

### 子體攻擊：為什麼 $n$ 最好是質數

若 $GF(2^n)$ 的 $n$ 有小因數，就有對應的子體，某些橢圓曲線或 DLP 攻擊能「下降」到較小的子體
（Weil descent、GHS 攻擊）。NIST 的二元曲線因此選 $n = 163, 233, 283, 409, 571$ —— **全是質數**，
使 $GF(2^n)$ 除了 $GF(2)$ 之外沒有任何真子體。

### 程式思維

```python
n = 24
divs = [d for d in range(1, n + 1) if n % d == 0]
edges = sorted((d, e) for d in divs for e in divs
               if d < e and e % d == 0
               and not any(d < k < e and k % d == 0 and e % k == 0 for k in divs))
assert edges == [(1, 2), (1, 3), (2, 4), (2, 6), (3, 6), (4, 8), (4, 12), (6, 12), (8, 24), (12, 24)]   # 投影片 p.37
```
