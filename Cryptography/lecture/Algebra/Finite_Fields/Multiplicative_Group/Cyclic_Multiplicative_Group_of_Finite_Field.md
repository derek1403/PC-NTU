# Cyclic Multiplicative Group of a Finite Field (有限體的乘法群是循環群)

+++

## 證明目標:

`FiniteFields.pdf` p.38–p.41；補充講義 §7.7.3（Theorem 7.13、Example 2、3）。
**本章最重要的定理之一**：任何有限體的非零元素，都是**單一個元素**的冪次。
[Abstract_Algebra 定理索引](../../Abstract_Algebra/theorems_index.md) 將「$GF(q)^*$ 為循環群」列為**未證明**，本檔補證。

* (a) 上界：對每個 $d \mid q - 1$，$GF(q)^*$ 中階為 $d$ 的元素個數

$$N(d) \in \left\{0,\ \varphi(d)\right\}$$

* (b) 投影片 p.39 的 Theorem：$N(d) = \varphi(d)$ 對所有 $d \mid q - 1$ 成立；特別地

$$GF(q)^* = \left\langle g \right\rangle \ \text{for some } g, \qquad \text{恰有 } \varphi(q - 1) \text{ 個生成元（本原元）}$$

* (c) 補充講義 Example 2、3：$GF(5)$ 與 $GF(16)$ 中各階元素的分布。

* (d) 投影片 p.41 的 Example：$P(x) = x^5 + 2x + 1$ 在 $GF(3)$ 上不可約，$K = GF(3)[x]/\left\langle P \right\rangle$，$Q(x) = x^2 + 2x + 1$，則

$$\left|K\right| = 243, \qquad Q^{1213} = Q^{3} = 2x^3 + x^2 + 2x + 1, \qquad Q^{-1} = x^4 + x^3 + 2x + 1$$

* $q$ : 有限體的元素個數 (The order of the finite field) $[q = p^n]$
* $GF(q)^*$ : 乘法群 (The multiplicative group) $[\text{群},\ \left|GF(q)^*\right| = q - 1]$
* $d$ : $q - 1$ 的正因數 (A positive divisor of $q - 1$) $[d \in \mathbf{P}]$
* $N(d)$ : 階為 $d$ 的元素個數 (The number of elements of order $d$) $[N(d) \in \mathbf{N}]$
* $\varphi$ : 尤拉函數 (Euler's totient) $[\mathbf{P} \to \mathbf{P}]$
* $g$ : 本原元（乘法群的生成元）(A primitive element) $[g \in GF(q)^*]$
* 註：**投影片 p.40 的 Proof (Sketch) 走的是另一條路**（先算 $n(\text{質數}) = q - 1$、$n(q^m) = q^{m-1}(q-1)$，再用乘法性 $n(ab) = n(a)n(b)$），
  其中每一步都需要額外論證（例如「$x^d - 1$ 在 $GF(p^n)$ 中恰有 $d$ 個根」），投影片未寫出。
  本檔改走補充講義 §7.7.3 的「上界 $+$ 計數」路線，每一步都完整。
* 註：投影片 p.39 用 $n(d)$、本檔用 $N(d)$（避免與擴張次數 $n$ 撞名）。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [體的乘法群與元素的階 (The multiplicative group and element orders)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Group/Order_of_Element_and_Cyclic_Subgroup.html#b-proof-that-the-order-of-an-element-divides-the-order-of-the-group)：** 已於 [體的定義](../../Abstract_Algebra/Field/Field_Definition.md)【定義 1】與 [元素的階與循環子群](../../Abstract_Algebra/Group/Order_of_Element_and_Cyclic_Subgroup.md)【證明 (a)(b)】給出並證明，此處直接引用不再重證

  * (a) $F^*$ 是 $q - 1$ 階的群：

    $$\left|F\right| = q \quad \Longrightarrow \quad \left|F^*\right| = q - 1$$

  * (b) 階整除群階、循環子群大小等於階：

    $$o(\beta) \ \Big|\ q - 1, \qquad \left|\left\langle \beta \right\rangle\right| = o(\beta)$$

  * $\beta$ : 非零元素 (A non-zero element) $[\beta \in F^*]$

* **【已知 2】 [體的乘法群對每個階至多一個循環子群 (At most one cyclic subgroup of each order)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Finite_Fields/Polynomial_Arithmetic/Roots_of_Polynomials.html#e-proof-that-a-field-has-at-most-one-cyclic-subgroup-of-each-order)：** 已於本章 [多項式的根](../Polynomial_Arithmetic/Roots_of_Polynomials.md)【證明 (e)】完整證明，此處直接引用不再重證

  $$\left\langle \beta \right\rangle,\ \left\langle \gamma \right\rangle \le F^*, \quad o(\beta) = o(\gamma) \quad \Longrightarrow \quad \left\langle \beta \right\rangle = \left\langle \gamma \right\rangle$$

  * $\beta,\ \gamma$ : 同階的兩個元素 (Two elements of the same order) $[\beta, \gamma \in F^*]$

* **【已知 3】 [循環群中各階元素的個數 (Element counts in a cyclic group)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Finite_Fields/Multiplicative_Group/Euler_Phi_and_Cyclic_Group_Orders.html#c-proof-that-a-cyclic-group-has-exactly-phi-of-d-elements-of-each-order-d)：** 已於本章 [尤拉函數與循環群中元素的階](Euler_Phi_and_Cyclic_Group_Orders.md)【證明 (b)(c)(d)】完整證明，此處直接引用不再重證

  * (a) 冪次的階：

    $$o\!\left(g^k\right) = \frac{o(g)}{\gcd\left(o(g), k\right)}$$

  * (b) $d$ 階循環群恰有 $\varphi(d)$ 個 $d$ 階元素：

    $$\left|\left\{x \in \left\langle \beta \right\rangle \ \middle|\ o(x) = d\right\}\right| = \varphi(d) \qquad \left(o(\beta) = d\right)$$

  * (c) 高斯恆等式：

    $$\sum_{d \mid m}\varphi(d) = m$$

  * $m$ : 正整數 (A positive integer) $[m \in \mathbf{P}]$

* **【已知 4】 [$\gamma$ 生成 $GF(16)^*$ (γ generates GF(16)*)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Finite_Fields/Construction/Galois_Fields_GF8_and_GF16.html#e-verify-that-the-root-of-x-to-the-fourth-plus-x-plus-one-generates-gf16)：** 已於本章 [伽羅瓦體 GF(8) 與 GF(16)](../Construction/Galois_Fields_GF8_and_GF16.md)【證明 (e)】驗證，此處直接引用

  $$\gamma^4 + \gamma + 1 = 0 \quad \Longrightarrow \quad o(\gamma) = 15$$

  * $\gamma$ : $x^4 + x + 1$ 的根 (A root of $x^4 + x + 1$) $[\gamma \in GF(16)]$

* **【已知 5】 [GF(p^n) 的構造與試除判準 (Construction of GF(p^n) and the trial-division test)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Finite_Fields/Construction/Construction_of_GF_p_n.html#a-proof-that-the-remainder-set-is-a-field-with-p-to-the-n-elements)：** 已於本章 [GF(p^n) 的構造](../Construction/Construction_of_GF_p_n.md)【推導 1】【證明 (a)】完整證明，此處直接引用不再重證

  * (a) 試除判準：

    $$f \ \text{不被任何次數} \le \tfrac{1}{2}\deg f \text{ 的質多項式整除} \quad \Longrightarrow \quad f \ \text{不可約}$$

  * (b) 構造：

    $$P \ \text{不可約},\ \deg P = n \quad \Longrightarrow \quad GF(p)[x]\big/\left\langle P \right\rangle \ \text{為 } p^n \text{ 元素的體}$$

  * $f,\ P$ : 多項式 (Polynomials) $[\in GF(p)[x]]$

* **【已知 6】 [二次不可約判別法 (Root criterion for quadratics)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Field/Irreducible_Polynomial.html#a-proof-of-the-root-criterion-for-degrees-two-and-three)：** 已於 [不可約多項式](../../Abstract_Algebra/Field/Irreducible_Polynomial.md)【證明 (a)】完整證明，此處直接引用不再重證

  $$\deg f \in \left\{2, 3\right\} \quad \Longrightarrow \quad \left[\, f \ \text{不可約} \Leftrightarrow f \ \text{無根} \,\right]$$

* **【已知 7】 [有限體版的費馬小定理與新生之夢 (Fermat's theorem in GF(q) and the freshman's dream)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Finite_Fields/Structure/Roots_of_x_q_minus_x.html#a-proof-that-every-element-satisfies-the-finite-field-version-of-fermats-theorem)：** 已於本章 [$x^q - x$ 的根](../Structure/Roots_of_x_q_minus_x.md)【證明 (a)】與 [新生之夢](../../Abstract_Algebra/Field/Freshmans_Dream.md)【證明 (a)】完整證明，此處直接引用不再重證

  * (a) 費馬：

    $$\beta \in GF(q)^* \quad \Longrightarrow \quad \beta^{q-1} = 1$$

  * (b) 新生之夢（特徵 $3$ 的交換環 $GF(3)[x]$ 中）：

    $$\left(a + b\right)^3 = a^3 + b^3$$

  * $a,\ b$ : 環元素 (Ring elements) $[a, b \in GF(3)[x]]$

* **【定義 1】 本原元 (Primitive element)：** 補充講義 §7.7.3；投影片 p.42 稱「a generator of $GF_{p^n}$」

  $$g \ \text{為 } GF(q) \text{ 的本原元} \quad \overset{\text{def}}{\Longleftrightarrow} \quad o(g) = q - 1$$

  * $g$ : 本原元 (A primitive element) $[g \in GF(q)^*]$

* **【定義 2】 階為 $d$ 的元素個數 (The number of elements of order d)：** 投影片 p.40 的 $n(d)$

  $$N(d) \overset{\text{def}}{=} \left|\left\{\beta \in GF(q)^* \ \middle|\ o(\beta) = d\right\}\right|$$

  * $N(d)$ : 階為 $d$ 的元素個數 (The count) $[N(d) \in \mathbf{N}]$

* **【假設 1】 $q$ 元素的有限體 (A finite field with q elements)：**

  $$F = GF(q), \qquad \left|F\right| = q$$

  * $F$ : 有限體 (A finite field) $[\text{體}]$

+++

## 證明:

### (a) proof that the number of elements of each order is zero or phi of d

設 $d \mid q - 1$ 且 $N(d) \neq 0$，取一個 $d$ 階元素 $\beta$。任何其他 $d$ 階元素 $\gamma$ 生成的循環子群與 $\left\langle \beta \right\rangle$ 同階，由【已知 2】兩者相同，故 $\gamma \in \left\langle \beta \right\rangle$：

$$\begin{gather*}
\left\{\gamma \in F^* \ \middle|\ o(\gamma) = d\right\} &\overset{\text{已知 2}}{=}& \left\{\gamma \in \left\langle \beta \right\rangle \ \middle|\ o(\gamma) = d\right\} \\
N(d) &\overset{\text{定義 2,已知 3(b)}}{=}& \varphi(d)
\end{gather*}$$

故 $N(d)$ 只能是 $0$ 或 $\varphi(d)$。

### (b) proof that the multiplicative group of a finite field is cyclic

每個元素的階都整除 $q - 1$（【已知 1(b)】），按階分類計數，再與高斯恆等式比較：

$$\begin{gather*}
\sum_{d \mid q-1} N(d) &\overset{\text{已知 1(a)(b),假設 1}}{=}& q - 1 \\
\sum_{d \mid q-1} N(d) &\overset{\text{已知 3(c)}}{=}& \sum_{d \mid q-1}\varphi(d) \\
N(d) &\overset{\text{證明 (a)}}{\le}& \varphi(d) \qquad \text{for each } d \\
N(d) &=& \varphi(d) \qquad \text{for each } d \qquad \text{(逐項} \le \text{而總和相等)}
\end{gather*}$$

取 $d = q - 1$：

$$\begin{gather*}
N(q - 1) &=& \varphi(q - 1) \ge 1 \\
\exists\, g \ \text{ with } \ o(g) &\overset{\text{定義 1}}{=}& q - 1 \\
\left|\left\langle g \right\rangle\right| &\overset{\text{已知 1(b)}}{=}& q - 1 = \left|F^*\right| \\
\left\langle g \right\rangle &=& F^*
\end{gather*}$$

$F^*$ 是循環群，恰有 $\varphi(q - 1)$ 個本原元。與投影片 p.39 的 Theorem 及補充講義 Theorem 7.13 一致。

* 註：「$\varphi(q-1) \ge 1$」見 [尤拉函數與循環群中元素的階](Euler_Phi_and_Cyclic_Group_Orders.md)【證明 (e)】（Exercise 3）。
* 註：**整個證明的關鍵是 (a) 的上界**，它來自「$x^d - 1$ 最多 $d$ 個根」——這一步需要 $F$ 是**體**。
  $\mathbf{Z}_8^*$（不是體的乘法群）就沒有這個上界，也就不循環。

### (c) verify the distribution of orders in GF(5) and GF(16)

**$GF(5)$**（補充講義 Example 2）：$2$ 的冪次跑遍 $GF(5)^*$，各階個數與 $\varphi$ 相符：

$$\begin{gather*}
2^1, 2^2, 2^3, 2^4 &=& 2,\ 4,\ 3,\ 1 \\
o(1) = 1, \quad o(4) &\overset{\text{已知 3(a)}}{=}& 4/\gcd(4, 2) = 2 \\
o(2) = o(3) &\overset{\text{已知 3(a)}}{=}& 4/\gcd(4, 1) = 4/\gcd(4, 3) = 4 \\
N(1), N(2), N(4) &=& 1,\ 1,\ 2 = \varphi(1), \varphi(2), \varphi(4)
\end{gather*}$$

**$GF(16)$**（補充講義 Example 3）：由【已知 4】$\gamma$ 是本原元，$o\!\left(\gamma^k\right) = 15/\gcd(15, k)$：

$$\begin{gather*}
\left\{k \ \middle|\ o\!\left(\gamma^k\right) = 3\right\} &\overset{\text{已知 3(a),已知 4}}{=}& \left\{5, 10\right\} \\
\left\{k \ \middle|\ o\!\left(\gamma^k\right) = 5\right\} &\overset{\text{已知 3(a),已知 4}}{=}& \left\{3, 6, 9, 12\right\} \\
\left\{k \ \middle|\ o\!\left(\gamma^k\right) = 15\right\} &\overset{\text{已知 3(a),已知 4}}{=}& \left\{1, 2, 4, 7, 8, 11, 13, 14\right\} \\
N(1), N(3), N(5), N(15) &=& 1,\ 2,\ 4,\ 8 = \varphi(1), \varphi(3), \varphi(5), \varphi(15)
\end{gather*}$$

與補充講義 Example 3 的列表一致。

### (d) verify the example in the field with two hundred forty-three elements

**$P$ 不可約**：$\deg P = 5$，由【已知 5(a)】只需試除次數 $1, 2$ 的質多項式。無根（即無一次因式）：

$$\begin{gather*}
P(0) &=& 1 \\
P(1) &=& 1 + 2 + 1 = 4 \equiv 1 \\
P(2) &=& 32 + 4 + 1 = 37 \equiv 1
\end{gather*}$$

$GF(3)$ 上首一二次質多項式恰為沒有根的那三個（【已知 6】）：$x^2 + 1$、$x^2 + x + 2$、$x^2 + 2x + 2$。$P$ 除以它們的餘式：

$$\begin{gather*}
\left\{x^2 + 1,\ x^2 + x + 2,\ x^2 + 2x + 2\right\} &\overset{\text{已知 6}}{=}& \left\{GF(3) \text{ 上的首一二次質多項式}\right\} \\
P \bmod \left(x^2 + 1\right) &=& 1 \qquad \text{(} x^2 \equiv -1\text{，} x^5 \equiv x\text{)} \\
P \bmod \left(x^2 + x + 2\right) &=& x + 1 \\
P \bmod \left(x^2 + 2x + 2\right) &=& x + 1 \\
P &\overset{\text{已知 5(a)}}{=}& \text{不可約}
\end{gather*}$$

**$\left|K\right|$ 與循環性**：

$$\begin{gather*}
\left|K\right| &\overset{\text{已知 5(b)}}{=}& 3^5 = 243 \\
K^* &\overset{\text{證明 (b)}}{=}& \text{242 階循環群}
\end{gather*}$$

**$Q^{1213}$**：$1213 = 242 \cdot 5 + 3$，且 $Q^{242} = 1$：

$$\begin{gather*}
Q^{1213} &=& \left(Q^{242}\right)^{5} Q^{3} \\
Q^{1213} &\overset{\text{已知 7(a)}}{=}& Q^{3} \\
Q^{3} &=& \left(x + 1\right)^{6} = \left[\left(x + 1\right)^3\right]^2 \qquad \text{(} Q = x^2 + 2x + 1 = \left(x + 1\right)^2\text{)} \\
Q^{3} &\overset{\text{已知 7(b)}}{=}& \left(x^3 + 1\right)^2 = x^6 + 2x^3 + 1 \\
Q^{3} &=& \left(x^2 + 2x\right) + 2x^3 + 1 \qquad \text{(} x^5 \equiv -2x - 1 = x + 2\text{，} x^6 \equiv x^2 + 2x\text{)} \\
Q^{3} &=& 2x^3 + x^2 + 2x + 1
\end{gather*}$$

**$Q^{-1}$**：驗證投影片給的貝祖等式（係數模 $3$）：

$$\begin{gather*}
Q\left(x^4 + x^3 + 2x + 1\right) &=& x^6 + 3x^5 + 3x^4 + 3x^3 + 5x^2 + 4x + 1 \\
Q\left(x^4 + x^3 + 2x + 1\right) &=& x^6 + 2x^2 + x + 1 \\
P \cdot x &=& x^6 + 2x^2 + x \\
Q\left(x^4 + x^3 + 2x + 1\right) - P \cdot x &=& 1
\end{gather*}$$

模 $P$ 後 $Q \cdot \left(x^4 + x^3 + 2x + 1\right) \equiv 1$，故 $Q^{-1} = x^4 + x^3 + 2x + 1$。三條結論都與投影片 p.41 一致。

* 註：$Q = \left(x + 1\right)^2$ 是平方元，它的階是 $121$（不是 $242$）—— $Q$ **不是**本原元。
  $Q^{1213} = Q^3$ 只用到 $Q^{242} = 1$，與 $Q$ 是否為本原元無關。
* 註：第二與第三列的餘式由長除法得出，並以 Python 驗算（見文末）。

+++

## 意義與密碼學關聯 (Interpretation and Relevance to Cryptography)

### 離散對數問題的舞台是有保證的

(b) 保證**每個**有限體的乘法群都是循環群。於是對任何 $GF(q)$：

$$GF(q)^* = \left\{g^0, g^1, \dots, g^{q-2}\right\} \cong \left(\mathbf{Z}_{q-1}, +\right)$$

每個非零元素都有唯一的離散對數 $\log_g \beta \in \mathbf{Z}_{q-1}$。
Diffie–Hellman、ElGamal、DSA 能在**任何**有限體上定義，靠的就是這條定理；
沒有它，「找一個生成元」這一步就沒有保證。

### 同構 ≠ 容易計算

$GF(q)^* \cong \mathbf{Z}_{q-1}$ 是**群同構**，但同構映射 $\beta \mapsto \log_g \beta$ 就是離散對數 —— **計算上是困難的**。
這是密碼學的核心張力：**結構上兩個群一模一樣，計算上卻一個容易一個困難**。
（在 $\mathbf{Z}_{q-1}$ 裡「求 $x$ 使 $x \cdot 1 = y$」是 trivial 的；在 $GF(q)^*$ 裡「求 $x$ 使 $g^x = \beta$」是 DLP。）

### Pohlig–Hellman：階的分解決定安全性

(a)(b) 的另一面：$GF(q)^*$ 對 $q - 1$ 的每個因數 $d$ 都有唯一的 $d$ 階子群。
Pohlig–Hellman 演算法把 DLP 拆到各個質因數冪的子群分別解，再用 CRT 拼回，
複雜度由 $q - 1$ 的**最大質因數**決定。所以：

* $GF(p)^*$ 的 DH：選 $p$ 使 $p - 1$ 有大質因數（安全質數 $p = 2r + 1$）；
* $GF(2^n)^*$：$2^n - 1$ 的分解是固定的（例如 $2^8 - 1 = 3 \cdot 5 \cdot 17$），**太小的 $n$ 完全不安全**。

### 程式思維

```python
def polymulmod(a, b, m, p):
    """GF(p)[x]/<m> 的乘法（係數由低到高）。"""
    r = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            r[i + j] = (r[i + j] + x * y) % p
    while len(r) >= len(m):                     # 模 m（m 首一）
        c, d = r[-1], len(r) - len(m)
        for i, y in enumerate(m):
            r[i + d] = (r[i + d] - c * y) % p
        r.pop()
    return r

P, Q = [1, 2, 0, 0, 0, 1], [1, 2, 1]            # x^5 + 2x + 1、x^2 + 2x + 1
def power(a, e):
    r = [1, 0, 0, 0, 0]
    for _ in range(e):
        r = polymulmod(r, a, P, 3)
    return r
assert power(Q, 3) == [1, 2, 1, 2, 0]           # 證明 (d)：2x^3 + x^2 + 2x + 1
assert polymulmod(Q, [1, 2, 0, 1, 1], P, 3) == [1, 0, 0, 0, 0]   # Q^{-1} = x^4 + x^3 + 2x + 1
```
