# Galois Fields GF(8) and GF(16) (伽羅瓦體 GF(8) 與 GF(16))

+++

## 證明目標:

`FiniteFields.pdf` p.16–p.23。$GF(2^n)$ 的元素天然就是 $n$ 位元的二進位數，
「硬體最好懂」（投影片 p.17）。本檔把 $n = 3, 4$ 兩個小例子算到底，
它們是 AES 的 $GF(2^8)$ 的縮小版。

* (a) 投影片 p.18：$GF(2)$ 上三次不可約多項式恰為 $x^3 + x^2 + 1$ 與 $x^3 + x + 1$，兩個商環都是 $8$ 元素的體：

$$GF(8) \cong GF(2)[x]\big/\left\langle x^3 + x^2 + 1 \right\rangle \cong GF(2)[x]\big/\left\langle x^3 + x + 1 \right\rangle$$

* (b) 投影片 p.18 在 $GF(2)[x]/\left\langle x^3 + x + 1 \right\rangle$ 中的例子：

$$\left[x^2 + 1\right] \oplus \left[x^2 + x\right] = \left[x + 1\right], \qquad \left[x^2 + 1\right] \otimes \left[x^2 + x\right] = \left[x + 1\right]$$

* (c) 投影片 p.19、p.21：設 $\alpha^3 + \alpha + 1 = 0$，則 $\alpha^7 = 1$ 且 $GF(8)^* = \left\langle \alpha \right\rangle$，元素表為

$$\begin{array}{c|c|c|c} \text{冪次} & \text{多項式} & \text{二進位} & \text{十進位} \\ \hline 0 & 0 & 000 & 0 \\ \alpha^0 & 1 & 001 & 1 \\ \alpha^1 & \alpha & 010 & 2 \\ \alpha^2 & \alpha^2 & 100 & 4 \\ \alpha^3 & \alpha + 1 & 011 & 3 \\ \alpha^4 & \alpha^2 + \alpha & 110 & 6 \\ \alpha^5 & \alpha^2 + \alpha + 1 & 111 & 7 \\ \alpha^6 & \alpha^2 + 1 & 101 & 5 \end{array}$$

* (d) 投影片 p.19：$GF(8)$ 的每個元素都是 $x^8 - x$ 的根；並且

$$\alpha,\ \alpha^2,\ \alpha^2 + \alpha \ \text{是} \ x^3 + x + 1 \ \text{的根}, \qquad \alpha + 1,\ \alpha^2 + 1,\ \alpha^2 + \alpha + 1 \ \text{是} \ x^3 + x^2 + 1 \ \text{的根}$$

* (e) 投影片 p.22–p.23：四次不可約多項式恰有三個；設 $\gamma^4 + \gamma + 1 = 0$，則 $GF(16)^* = \left\langle \gamma \right\rangle$。
* (f) 投影片 p.23 的 Note：若 $\beta$ 是 $x^4 + x^3 + x^2 + x + 1$ 的根，則 $\beta^5 = 1$，故 $GF(16)^* \neq \left\langle \beta \right\rangle$。

* $\alpha$ : $x^3 + x + 1$ 的根 (A root of $x^3 + x + 1$) $[\alpha \in GF(8)]$
* $\gamma$ : $x^4 + x + 1$ 的根 (A root of $x^4 + x + 1$) $[\gamma \in GF(16)]$
* $\beta$ : $x^4 + x^3 + x^2 + x + 1$ 的根 (A root of $x^4 + x^3 + x^2 + x + 1$) $[\beta \in GF(16)]$
* $GF(q)^*$ : 非零元素構成的乘法群 (The multiplicative group of non-zero elements) $[\text{群}]$
* 註：**投影片 p.23 把 $x^4 + x + 1$ 的根也記為 $\alpha$**，與 $GF(8)$ 的 $\alpha$ 同名；本檔改記為 $\gamma$ 以免混淆。
* 註：(a) 裡兩個商環**同構**這件事，本檔只驗證「兩者都是 $8$ 元素的體」；
  同構本身由 [$GF(p^n)$ 的唯一性](../Structure/Uniqueness_of_GF_p_n.md) 保證。
* 註：投影片 p.21 的「Minimal Polynomial」欄見 [共軛元與分圓陪集](../Multiplicative_Group/Conjugates_and_Cyclotomic_Cosets.md)【證明 (d)】；
  p.20 的極小多項式例子見 [極小多項式](../Multiplicative_Group/Minimal_Polynomial.md)；p.23 的 Fact 見 [共軛元與分圓陪集](../Multiplicative_Group/Conjugates_and_Cyclotomic_Cosets.md)【證明 (a)】；
  p.22 的 $x^{16} - x$ 分解見 [$x^{p^n}-x$ 的分解](../Multiplicative_Group/Factorization_of_x_p_n_minus_x.md)。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [GF(p^n) 的構造 (Construction of GF(p^n))](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Finite_Fields/Construction/Construction_of_GF_p_n.html#a-proof-that-the-remainder-set-is-a-field-with-p-to-the-n-elements)：** 已於本章 [GF(p^n) 的構造](Construction_of_GF_p_n.md)【證明 (a)】完整證明，此處直接引用不再重證

  $$q \in GF(p)[x] \ \text{不可約},\ \deg q = n \quad \Longrightarrow \quad GF(p)[x]\big/\left\langle q \right\rangle \ \text{是 } p^n \text{ 元素的體，元素為次數} < n \text{ 的餘式}$$

  * $q$ : 不可約多項式 (An irreducible polynomial) $[q \in GF(p)[x]]$

* **【已知 2】 [低次質多項式表 (The table of low-degree prime polynomials)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Finite_Fields/Polynomial_Arithmetic/Unique_Factorization_of_Polynomials.html#d-verify-the-sieve-for-prime-polynomials-of-low-degree-over-the-binary-field)：** 已於本章 [多項式的唯一分解](../Polynomial_Arithmetic/Unique_Factorization_of_Polynomials.md)【證明 (d)】驗證，此處直接引用

  * (a) 三次：

    $$x^3 + x + 1, \qquad x^3 + x^2 + 1$$

  * (b) 四次：

    $$x^4 + x + 1, \qquad x^4 + x^3 + 1, \qquad x^4 + x^3 + x^2 + x + 1$$

* **【已知 3】 [元素的階整除群的階 (The order of an element divides the group order)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Group/Order_of_Element_and_Cyclic_Subgroup.html#b-proof-that-the-order-of-an-element-divides-the-order-of-the-group)：** 已於 [元素的階與循環子群](../../Abstract_Algebra/Group/Order_of_Element_and_Cyclic_Subgroup.md)【證明 (a)(b)】完整證明，此處直接引用不再重證

  * (a) 階整除群的階：

    $$o(g) \ \Big|\ \left|G\right|$$

  * (b) 循環子群的大小等於階：

    $$\left|\left\langle g \right\rangle\right| = o(g)$$

  * $G$ : 有限群 (A finite group) $[\text{群}]$
  * $g$ : 群元素 (A group element) $[g \in G]$

* **【已知 4】 [同餘類與餘式一一對應 (Residue classes correspond to remainders)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Finite_Fields/Polynomial_Arithmetic/Division_Algorithm_for_Polynomials.html#d-proof-that-the-residues-modulo-a-polynomial-are-counted-by-the-remainders)：** 已於本章 [多項式的除法原理](../Polynomial_Arithmetic/Division_Algorithm_for_Polynomials.md)【證明 (d)】完整證明，此處直接引用不再重證

  $$r_1 \neq r_2,\ \deg r_i < \deg m \quad \Longrightarrow \quad \left[r_1\right] \neq \left[r_2\right]$$

  * $r_1,\ r_2$ : 低次餘式 (Low-degree remainders) $[\in F[x]]$
  * 註：用在「$\alpha^3 \neq 1$」這類判斷：兩個次數 $< 3$ 的相異多項式代表相異的元素。

* **【定義 1】 $GF(8)$ 的生成根 (The root generating GF(8))：** 投影片 p.19

  $$\alpha^3 + \alpha + 1 \overset{\text{def}}{=} 0, \qquad \text{即} \qquad \alpha^3 = \alpha + 1$$

  * $\alpha$ : $\left[x\right] \in GF(2)[x]/\left\langle x^3 + x + 1 \right\rangle$ (The class of $x$) $[\alpha \in GF(8)]$

* **【定義 2】 $GF(16)$ 的兩個根 (Two roots in GF(16))：** 投影片 p.23

  * (a) $\gamma$：

    $$\gamma^4 + \gamma + 1 \overset{\text{def}}{=} 0, \qquad \text{即} \qquad \gamma^4 = \gamma + 1$$

  * (b) $\beta$：

    $$\beta^4 + \beta^3 + \beta^2 + \beta + 1 \overset{\text{def}}{=} 0$$

  * $\gamma$ : $\left[x\right] \in GF(2)[x]/\left\langle x^4 + x + 1 \right\rangle$ (The class of $x$) $[\gamma \in GF(16)]$
  * $\beta$ : $\left[x\right] \in GF(2)[x]/\left\langle x^4 + x^3 + x^2 + x + 1 \right\rangle$ (The class of $x$) $[\beta \in GF(16)]$

* **【推導 1】 $\alpha$ 的冪次表 (The power table of alpha)：** 每次乘以 $\alpha$，遇到 $\alpha^3$ 就用【定義 1】換掉

  $$\begin{gather*}
  \alpha^3 &\overset{\text{定義 1}}{=}& \alpha + 1 \\
  \alpha^4 = \alpha \cdot \alpha^3 &\overset{\text{定義 1}}{=}& \alpha^2 + \alpha \\
  \alpha^5 = \alpha \cdot \alpha^4 = \alpha^3 + \alpha^2 &\overset{\text{定義 1}}{=}& \alpha^2 + \alpha + 1 \\
  \alpha^6 = \alpha \cdot \alpha^5 = \alpha^3 + \alpha^2 + \alpha &\overset{\text{定義 1}}{=}& \alpha^2 + 1 \\
  \alpha^7 = \alpha \cdot \alpha^6 = \alpha^3 + \alpha &\overset{\text{定義 1}}{=}& 1
  \end{gather*}$$

  * 註：係數運算在 $GF(2)$ 中，$\alpha + \alpha = 0$。例如第四列 $\alpha^3 + \alpha^2 + \alpha = \left(\alpha + 1\right) + \alpha^2 + \alpha = \alpha^2 + 1$。

+++

## 證明:

### (a) verify that both cubic quotients are fields with eight elements

由【已知 2(a)】兩個三次多項式都不可約，套【已知 1】（$p = 2$、$n = 3$）：

$$\begin{gather*}
GF(2)[x]\big/\left\langle x^3 + x^2 + 1 \right\rangle &\overset{\text{已知 1,已知 2(a)}}{=}& 2^3 = 8 \ \text{元素的體} \\
GF(2)[x]\big/\left\langle x^3 + x + 1 \right\rangle &\overset{\text{已知 1,已知 2(a)}}{=}& 2^3 = 8 \ \text{元素的體}
\end{gather*}$$

投影片 p.18 的「neither $0$ nor $1$ is a root of either polynomial」就是【已知 2(a)】背後的根判別。
而「$x^8 - x \equiv x\left(x+1\right)\left(x^3+x+1\right)\left(x^3+x^2+1\right)$ gives a complete list」
見 [$x^{p^n}-x$ 的分解](../Multiplicative_Group/Factorization_of_x_p_n_minus_x.md)【證明 (d)】。

### (b) verify the sum and product example in GF(8)

加法逐項模 $2$；乘法展開後除以 $x^3 + x + 1$：

$$\begin{gather*}
\left[x^2 + 1\right] \oplus \left[x^2 + x\right] &=& \left[2x^2 + x + 1\right] \\
\left[x^2 + 1\right] \oplus \left[x^2 + x\right] &=& \left[x + 1\right] \\
\left[x^2 + 1\right] \otimes \left[x^2 + x\right] &=& \left[x^4 + x^3 + x^2 + x\right] \\
\left[x^2 + 1\right] \otimes \left[x^2 + x\right] &=& \left[\left(x + 1\right)\left(x^3 + x + 1\right) + \left(x + 1\right)\right] \\
\left[x^2 + 1\right] \otimes \left[x^2 + x\right] &\overset{\text{已知 1}}{=}& \left[x + 1\right]
\end{gather*}$$

第四列的驗算：$\left(x + 1\right)\left(x^3 + x + 1\right) = x^4 + x^3 + x^2 + 2x + 1 \equiv x^4 + x^3 + x^2 + 1$，
加上 $x + 1$ 得 $x^4 + x^3 + x^2 + x$。與投影片 p.18 一致。

* 註：用 (c) 的冪次表更快：$x^2 + 1 = \alpha^6$、$x^2 + x = \alpha^4$，乘積 $\alpha^{10} = \alpha^3 = \alpha + 1$。
  **冪次表把乘法變成指數加法** —— 這是查表實作的原理。

### (c) verify that alpha generates the multiplicative group of GF(8)

由【推導 1】，$\alpha^0, \alpha^1, \dots, \alpha^6$ 化成的七個多項式
$1,\ \alpha,\ \alpha^2,\ \alpha+1,\ \alpha^2+\alpha,\ \alpha^2+\alpha+1,\ \alpha^2+1$
兩兩相異且都次數 $< 3$，由【已知 4】是七個相異元素：

$$\begin{gather*}
\left|\left\{\alpha^0, \alpha^1, \dots, \alpha^6\right\}\right| &\overset{\text{推導 1,已知 4}}{=}& 7 \\
\left|GF(8)^*\right| &=& 8 - 1 = 7 \\
\left\langle \alpha \right\rangle &=& GF(8)^*
\end{gather*}$$

且 $\alpha^7 = 1$（【推導 1】末列），即 $o(\alpha) = 7$。與投影片 p.19「$\alpha^7 = 1$」、「$GF_8^* = \left\langle \alpha \right\rangle$」及 p.21 的表一致。

* 註：$7$ 是質數，故由【已知 3(a)】$GF(8)^*$ 的**每個**非單位元素的階都是 $7$ —— 都是生成元。

### (d) verify that every element is a root of x to the eighth minus x

**$0$ 與 $\alpha^i$**（投影片 p.19 的兩行）：

$$\begin{gather*}
0^8 - 0 &=& 0 \\
\left(\alpha^i\right)^8 - \alpha^i &=& \left(\alpha^7\right)^i \alpha^i - \alpha^i \\
\left(\alpha^i\right)^8 - \alpha^i &\overset{\text{推導 1}}{=}& \alpha^i - \alpha^i = 0
\end{gather*}$$

**根的歸屬**：以【推導 1】的表代入。$\alpha^2 + \alpha = \alpha^4$、$\alpha + 1 = \alpha^3$、$\alpha^2 + 1 = \alpha^6$、$\alpha^2 + \alpha + 1 = \alpha^5$，
指數模 $7$ 化簡：

$$\begin{gather*}
\left(\alpha^2\right)^3 + \alpha^2 + 1 &\overset{\text{推導 1}}{=}& \left(\alpha^2 + 1\right) + \alpha^2 + 1 = 0 \\
\left(\alpha^4\right)^3 + \alpha^4 + 1 = \alpha^5 + \alpha^4 + 1 &\overset{\text{推導 1}}{=}& \left(\alpha^2 + \alpha + 1\right) + \left(\alpha^2 + \alpha\right) + 1 = 0 \\
\left(\alpha^3\right)^3 + \left(\alpha^3\right)^2 + 1 = \alpha^2 + \alpha^6 + 1 &\overset{\text{推導 1}}{=}& \alpha^2 + \left(\alpha^2 + 1\right) + 1 = 0 \\
\left(\alpha^5\right)^3 + \left(\alpha^5\right)^2 + 1 = \alpha + \alpha^3 + 1 &\overset{\text{推導 1}}{=}& \alpha + \left(\alpha + 1\right) + 1 = 0 \\
\left(\alpha^6\right)^3 + \left(\alpha^6\right)^2 + 1 = \alpha^4 + \alpha^5 + 1 &\overset{\text{推導 1}}{=}& \left(\alpha^2 + \alpha\right) + \left(\alpha^2 + \alpha + 1\right) + 1 = 0
\end{gather*}$$

$\alpha$ 本身是 $x^3 + x + 1$ 的根由【定義 1】給出。與投影片 p.19 一致。

* 註：規律是 $\left\{\alpha, \alpha^2, \alpha^4\right\}$ 與 $\left\{\alpha^3, \alpha^6, \alpha^{12} = \alpha^5\right\}$ ——
  **每組都是把指數反覆乘以 $2$**。原因見 [共軛元與分圓陪集](../Multiplicative_Group/Conjugates_and_Cyclotomic_Cosets.md)。

### (e) verify that the root of x to the fourth plus x plus one generates GF(16)

由【已知 2(b)】$x^4 + x + 1$ 不可約，故【已知 1】給出 $16$ 元素的體，$\left|GF(16)^*\right| = 15$。
$o(\gamma)$ 整除 $15$，只可能是 $1, 3, 5, 15$；逐一排除：

$$\begin{gather*}
o(\gamma) &\overset{\text{已知 3(a)}}{\in}& \left\{1, 3, 5, 15\right\} \\
\gamma^1,\ \gamma^3 &\overset{\text{已知 4}}{\neq}& 1 \qquad \text{(次數 } 1, 3 \text{ 的單項式，不是常數)} \\
\gamma^5 = \gamma \cdot \gamma^4 &\overset{\text{定義 2(a)}}{=}& \gamma^2 + \gamma \\
\gamma^2 + \gamma &\overset{\text{已知 4}}{\neq}& 1 \\
o(\gamma) &=& 15 \\
\left|\left\langle \gamma \right\rangle\right| &\overset{\text{已知 3(b)}}{=}& 15 = \left|GF(16)^*\right|
\end{gather*}$$

故 $GF(16)^* = \left\langle \gamma \right\rangle$，與投影片 p.23 一致。

### (f) verify that the root of the all-ones quartic has order five

$x^4 + x^3 + x^2 + x + 1$ 乘以 $x - 1$ 是 $x^5 - 1$（等比級數）：

$$\begin{gather*}
\left(\beta - 1\right)\left(\beta^4 + \beta^3 + \beta^2 + \beta + 1\right) &=& \beta^5 - 1 \\
\left(\beta - 1\right) \cdot 0 &\overset{\text{定義 2(b)}}{=}& \beta^5 - 1 \\
\beta^5 &=& 1 \\
\left|\left\langle \beta \right\rangle\right| &\overset{\text{已知 3(b)}}{\le}& 5 < 15
\end{gather*}$$

故 $\left\langle \beta \right\rangle \neq GF(16)^*$，與投影片 p.23 的 Note 一致。

* 註：**不可約不等於能生成乘法群**。$x^4 + x^3 + x^2 + x + 1$ 不可約（【已知 2(b)】），
  模它得到的 $GF(16)$ 完全合法，只是 $\left[x\right]$ 不是生成元。
  「$\left[x\right]$ 能生成乘法群」的不可約多項式稱為**本原多項式**，見 [本原多項式](../Multiplicative_Group/Primitive_Polynomial.md)。

+++

## 意義與密碼學關聯 (Interpretation and Relevance to Cryptography)

### 為什麼密碼學偏愛 $GF(2^n)$

投影片 p.17 的兩個應用：

* **AES**：$GF(2^8)$，一個元素 $=$ 一個位元組；
* **ECC**：橢圓曲線建在 $GF(2^n)$ 或 $GF(p)$ 上，**不用** $GF(p^n)$（$p > 2$、$n > 1$）——
  前者硬體最快、後者軟體最快，中間型兩頭不討好（配對密碼學是例外）。

$GF(2^n)$ 的加法是 XOR、不需要進位，乘法可以用移位與 XOR 完成 —— 這正是 (b) 的計算方式。

### 冪次表 = 對數表

(c) 的表同時是一張**離散對數表**：$\log_\alpha\left(\alpha^2 + 1\right) = 6$。
小體（如 $GF(2^8)$）的實作常建兩張 $256$ 項的表 `log[]` 與 `exp[]`，
乘法就變成 `exp[(log[a] + log[b]) % 255]`。
**但這種實作有快取時序側通道**，現代 AES 實作已改用位元切片或硬體指令（AES-NI、PCLMULQDQ）。

### 本原多項式的重要性

(e)(f) 的對比是 LFSR（線性回饋移位暫存器）設計的核心：
回饋多項式是本原多項式時，LFSR 的週期達到最大值 $2^n - 1$；
選到 $x^4 + x^3 + x^2 + x + 1$ 這種非本原的不可約多項式，週期只有 $5$。
流密碼與偽亂數產生器因此一律選本原多項式。

### 程式思維

```python
def gf2n_powers(mod, n):
    """列出 [x]^0 .. [x]^(2^n - 2)（位元表示），推導 1 的機械化版本。"""
    out, a = [], 1
    for _ in range(2 ** n - 1):
        out.append(a)
        a <<= 1
        if a >> n:
            a ^= mod
    return out

assert gf2n_powers(0b1011, 3) == [1, 2, 4, 3, 6, 7, 5]        # 證明 (c)：投影片 p.21 的十進位欄
assert len(set(gf2n_powers(0b10011, 4))) == 15                # 證明 (e)：gamma 生成 GF(16)*
assert len(set(gf2n_powers(0b11111, 4))) == 5                 # 證明 (f)：beta 只生成 5 個
```
