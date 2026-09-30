# Euclidean Domain (歐幾里得整環)

+++

## 證明目標:

`FiniteFields.pdf` p.8（下半）–p.9。把「有除法原理」這件事抽象成一個定義，
一次證完 $\mathbf{Z}$ 與 $F[x]$ 共同的 gcd 理論。
[模不可約多項式的商環是體](../../Abstract_Algebra/Field/Quotient_by_Irreducible_is_Field.md)【已知 2(a)(b)】
（$F[x]$ 是 PID、多項式版貝祖等式）當時是**引用未證**的，本檔把它們完整證出。

* (a)(b)(c) 投影片 p.9 的三個例子都是歐幾里得整環：

$$\left(\mathbf{Z},\ \left|a\right|\right), \qquad \left(F[x],\ \deg a\right), \qquad \left(\mathbf{Z}[i],\ \left|a+bi\right|^2 = a^2 + b^2\right)$$

* (d) 歐幾里得整環必為主理想整環（投影片未列，但 (e) 需要它）：

$$D \ \text{為歐幾里得整環} \quad \Longrightarrow \quad \text{每個理想 } I \trianglelefteq D \ \text{都是主理想}$$

* (e) 投影片 p.8 的 Proposition：（擴展）歐幾里得演算法在 $F[x]$ 中可行，即

$$\forall\, a(x), b(x) \in F[x] \ \left(\text{不全為 } 0\right), \ \exists\, u(x), v(x) \ \text{ with } \ a\,u + b\,v = \gcd\left(a, b\right)$$

* $D$ : 整環 (An integral domain) $[\text{環}]$
* $d$ : 歐幾里得函數 (The Euclidean function) $[D \setminus \left\{0\right\} \to \mathbf{N}]$
* $I$ : 理想 (An ideal) $[I \trianglelefteq D]$
* $F$ : 體 (A field) $[\text{體}]$
* $a,\ b,\ u,\ v$ : 多項式 (Polynomials) $[a, b, u, v \in F[x]]$
* $\mathbf{Z}[i]$ : 高斯整數環 (The ring of Gaussian integers) $[\left\{a + bi \mid a, b \in \mathbf{Z}\right\}]$
* 註：**投影片 p.8 的 Proposition 省略了證明**，本檔以 (d)(e) 補上。
* 註：(e) 在 $GF(2^8)$ 中求反元素時直接使用 —— 見 [AES 的 $GF(2^8)$ 算術](../AES/AES_GF_2_8_Arithmetic.md)。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [良序原理與整數除法原理 (Well-ordering and the integer division algorithm)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Group/Order_of_Element_and_Cyclic_Subgroup.html#assumptions-preliminaries)：** 已於 [元素的階與循環子群](../../Abstract_Algebra/Group/Order_of_Element_and_Cyclic_Subgroup.md)【已知 6】引用，此處再次引用

  * (a) 良序原理：

    $$S \subseteq \mathbf{N},\ S \neq \varnothing \quad \Longrightarrow \quad S \ \text{有最小元素}$$

  * (b) 整數除法原理：

    $$\forall\, m \in \mathbf{Z},\ n \in \mathbf{P}, \ \exists\, q, r \in \mathbf{Z} \ \text{ with } \ m = qn + r,\ 0 \le r < n$$

  * $S$ : 自然數的非空子集 (A non-empty subset of the naturals) $[S \subseteq \mathbf{N}]$
  * $m,\ n,\ q,\ r$ : 整數 (Integers) $[\in \mathbf{Z}]$

* **【已知 2】 [多項式的除法原理 (Division algorithm for polynomials)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Finite_Fields/Polynomial_Arithmetic/Division_Algorithm_for_Polynomials.html#a-proof-of-the-existence-of-the-quotient-and-remainder)：** 已於本章 [多項式的除法原理](Division_Algorithm_for_Polynomials.md)【證明 (a)】完整證明，此處直接引用不再重證

  $$b \neq 0 \quad \Longrightarrow \quad a = bq + r, \quad r = 0 \ \text{或} \ \deg r < \deg b$$

  * $a,\ b,\ q,\ r$ : 多項式 (Polynomials) $[\in F[x]]$

* **【已知 3】 [體上多項式的次數相加 (Degrees add over a field)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Finite_Fields/Polynomial_Arithmetic/Polynomial_Ring_over_a_Field.html#b-proof-that-degrees-add-in-the-polynomial-ring-over-a-field)：** 已於本章 [體上的多項式環](Polynomial_Ring_over_a_Field.md)【證明 (b)】完整證明，此處直接引用不再重證

  $$\deg\left(ab\right) = \deg a + \deg b$$

  * $a,\ b$ : 多項式 (Polynomials) $[a, b \in F[x]]$

* **【已知 4】 [整環的例子與子環繼承 (Examples of integral domains and inheritance by subrings)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Ring/Integral_Domain.html#assumptions-preliminaries)：** 已於 [整環](../../Abstract_Algebra/Ring/Integral_Domain.md)【推導 1】【推導 2】【證明 (a)】完整證明，此處直接引用不再重證

  * (a) $\mathbf{Z}$ 與 $F[x]$ 是整環：

    $$\mathbf{Z},\ F[x] \ \text{為整環}$$

  * (b) 體的子環是整環（$\mathbf{Z}[i] \subseteq \mathbf{C}$）：

    $$S \le \mathbf{C} \quad \Longrightarrow \quad S \ \text{為整環}$$

  * $S$ : $\mathbf{C}$ 的子環 (A subring of $\mathbf{C}$) $[S \le \mathbf{C}]$

* **【已知 5】 [理想的和與主理想 (Sum of ideals and principal ideals)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Ring/Ideal.html#e-proof-that-the-intersection-and-the-sum-of-two-ideals-are-ideals)：** 已於 [理想](../../Abstract_Algebra/Ring/Ideal.md)【證明 (b)(e)】與 [主理想](../../Abstract_Algebra/Ring/Principal_Ideal.md) 完整證明，此處直接引用不再重證

  * (a) 理想對減法與吸收封閉：

    $$a, b \in I,\ r \in D \quad \Longrightarrow \quad a - b \in I, \quad ra \in I$$

  * (b) 兩個元素生成的理想：

    $$\left\langle a, b \right\rangle = \left\langle a \right\rangle + \left\langle b \right\rangle = \left\{au + bv \ \middle|\ u, v \in D\right\} \trianglelefteq D$$

  * (c) 主理想：

    $$\left\langle d \right\rangle = \left\{dr \ \middle|\ r \in D\right\}$$

  * $I$ : 理想 (An ideal) $[I \trianglelefteq D]$
  * $a,\ b,\ d,\ r,\ u,\ v$ : 環元素 (Ring elements) $[\in D]$

* **【已知 6】 [複數模長的乘法性 (Multiplicativity of the complex modulus)](https://mathworld.wolfram.com/ComplexModulus.html)：** 複數的標準性質，直接引用不再重證

  $$\left|zw\right|^2 = \left|z\right|^2\left|w\right|^2$$

  * $z,\ w$ : 複數 (Complex numbers) $[z, w \in \mathbf{C}]$

* **【定義 1】 歐幾里得整環 (Euclidean domain)：** 投影片 p.9

  $$D \ \text{為歐幾里得整環} \ \overset{\text{def}}{\Longleftrightarrow} \ \exists\, d : D \setminus \left\{0\right\} \to \mathbf{N} \ \text{ with } \begin{cases} \text{(1)} \ d(a) \le d(ab) & a, b \neq 0 \\ \text{(2)} \ a = bq + r,\ r = 0 \ \text{或} \ d(r) < d(b) & b \neq 0 \end{cases}$$

  * $D$ : 整環 (An integral domain) $[\text{環}]$
  * $d$ : 歐幾里得函數 (The Euclidean function) $[D \setminus \left\{0\right\} \to \mathbf{N}]$
  * $a,\ b,\ q,\ r$ : 環元素 (Ring elements) $[\in D]$

* **【定義 2】 最大公因式 (Greatest common divisor in F[x])：** 用 (d) 保證存在的生成元來定義

  $$\gcd\left(a, b\right) \overset{\text{def}}{=} \left\langle a, b \right\rangle \ \text{的首一生成元}$$

  * $\gcd$ : 最大公因式 (The greatest common divisor) $[F[x] \times F[x] \to F[x]]$
  * $a,\ b$ : 不全為零的多項式 (Polynomials, not both zero) $[a, b \in F[x]]$
  * 註：生成元只差一個非零常數倍（$\left\langle d \right\rangle = \left\langle cd \right\rangle$），除以首項係數即得首一的那一個，故良定義。
  * 註：【證明 (e)】會驗證它確實是「公因式中最大的」——整除所有公因式。

* **【推導 1】 四捨五入 (Rounding to the nearest integer)：** 【證明 (c)】要用

  $$\begin{gather*}
  t &\in& \mathbf{R} \\
  n &\overset{\text{let}}{=}& \left\lfloor t + \tfrac{1}{2} \right\rfloor \in \mathbf{Z} \\
  \left|t - n\right| &\le& \tfrac{1}{2}
  \end{gather*}$$

  * $t$ : 任意實數 (A real number) $[t \in \mathbf{R}]$
  * $n$ : 最接近的整數 (The nearest integer) $[n \in \mathbf{Z}]$

+++

## 證明:

### (a) verify that the integers form a Euclidean domain

取 $d(a) = \left|a\right|$。**條件 (1)**：$b \neq 0$ 故 $\left|b\right| \ge 1$：

$$\begin{gather*}
d\left(ab\right) &=& \left|a\right|\left|b\right| \\
d\left(ab\right) &\ge& \left|a\right| \cdot 1 \\
d\left(ab\right) &\overset{\text{定義 1}}{\ge}& d(a)
\end{gather*}$$

**條件 (2)**：對 $n = \left|b\right|$ 套整數除法原理，再把正負號吸收進商：

$$\begin{gather*}
a &\overset{\text{已知 1(b)}}{=}& q\left|b\right| + r, \qquad 0 \le r < \left|b\right| \\
a &=& b\left(\pm q\right) + r \qquad \text{(} b < 0 \text{ 時取負號)} \\
r = 0 \ \text{或} \ d(r) &<& d(b)
\end{gather*}$$

又 $\mathbf{Z}$ 是整環，故

$$\mathbf{Z} \overset{\text{已知 4(a),定義 1}}{=} \text{歐幾里得整環}$$

### (b) verify that the polynomials over a field form a Euclidean domain

取 $d(a) = \deg a$（非零多項式的次數 $\ge 0$）。**條件 (1)**：

$$\begin{gather*}
d\left(ab\right) &\overset{\text{已知 3}}{=}& \deg a + \deg b \\
d\left(ab\right) &\ge& \deg a + 0 \\
d\left(ab\right) &\overset{\text{定義 1}}{\ge}& d(a)
\end{gather*}$$

**條件 (2)** 就是【已知 2】。又 $F[x]$ 是整環，故

$$F[x] \overset{\text{已知 2,已知 4(a),定義 1}}{=} \text{歐幾里得整環}$$

### (c) verify that the Gaussian integers form a Euclidean domain

取 $d(a + bi) = a^2 + b^2 = \left|a + bi\right|^2$。$\mathbf{Z}[i]$ 是 $\mathbf{C}$ 的子環，由【已知 4(b)】為整環。

**條件 (1)**：非零高斯整數的模長平方是正整數，故 $\ge 1$：

$$\begin{gather*}
d\left(\alpha\beta\right) &\overset{\text{已知 6}}{=}& d(\alpha)\,d(\beta) \\
d\left(\alpha\beta\right) &\ge& d(\alpha) \cdot 1
\end{gather*}$$

**條件 (2)**：在 $\mathbf{C}$ 裡先做真正的除法 $\alpha/\beta = s + ti$，再把 $s, t$ 各自四捨五入：

$$\begin{gather*}
\frac{\alpha}{\beta} &=& s + ti, \qquad s, t \in \mathbf{Q} \\
\left|s - m\right|,\ \left|t - n\right| &\overset{\text{推導 1}}{\le}& \tfrac{1}{2} \qquad \text{for some } m, n \in \mathbf{Z} \\
q &\overset{\text{let}}{=}& m + ni \in \mathbf{Z}[i] \\
r &\overset{\text{let}}{=}& \alpha - \beta q = \beta\left[\left(s - m\right) + \left(t - n\right)i\right] \in \mathbf{Z}[i] \\
d(r) &\overset{\text{已知 6}}{=}& d(\beta)\left[\left(s-m\right)^2 + \left(t-n\right)^2\right] \\
d(r) &\le& d(\beta)\left[\tfrac{1}{4} + \tfrac{1}{4}\right] \\
d(r) &<& d(\beta)
\end{gather*}$$

故

$$\mathbf{Z}[i] \overset{\text{已知 4(b),定義 1}}{=} \text{歐幾里得整環}$$

**具體例子**：$\alpha = 7 + 2i$、$\beta = 2 + i$：

$$\begin{gather*}
\frac{7 + 2i}{2 + i} &=& \frac{\left(7 + 2i\right)\left(2 - i\right)}{5} = \frac{16 - 3i}{5} = 3.2 - 0.6i \\
q &\overset{\text{推導 1}}{=}& 3 - i \\
r &=& \left(7 + 2i\right) - \left(2 + i\right)\left(3 - i\right) = \left(7 + 2i\right) - \left(7 + i\right) = i \\
d(r) = 1 &<& 5 = d(\beta)
\end{gather*}$$

* 註：與 $\mathbf{Z}$、$F[x]$ 不同，**高斯整數的商與餘數不唯一**（$s$ 或 $t$ 恰為 $\tfrac{1}{2}$ 時兩邊都可取）。
  定義 1 只要求存在，不要求唯一。

### (d) proof that every Euclidean domain is a principal ideal domain

設 $I \trianglelefteq D$。若 $I = \left\{0\right\}$，則 $I = \left\langle 0 \right\rangle$。否則取 $I$ 中 $d$ 值最小的非零元素 $b$：

$$\begin{gather*}
\left\{d(x) \ \middle|\ x \in I \setminus \left\{0\right\}\right\} &\neq& \varnothing \\
b &\overset{\text{已知 1(a)}}{\in}& I, \qquad d(b) \ \text{最小}
\end{gather*}$$

任取 $a \in I$ 對 $b$ 做除法，餘數仍在 $I$ 裡：

$$\begin{gather*}
a &\overset{\text{定義 1}}{=}& bq + r, \qquad r = 0 \ \text{或} \ d(r) < d(b) \\
r &=& a - bq \\
r &\overset{\text{已知 5(a)}}{\in}& I \\
r &=& 0 \qquad \text{(否則 } d(r) < d(b) \text{ 與最小性矛盾)} \\
a &\overset{\text{已知 5(c)}}{\in}& \left\langle b \right\rangle
\end{gather*}$$

故 $I \subseteq \left\langle b \right\rangle$；反向由吸收性 $br \in I$（【已知 5(a)】）得 $\left\langle b \right\rangle \subseteq I$：

$$I = \left\langle b \right\rangle$$

* 註：與 [主理想](../../Abstract_Algebra/Ring/Principal_Ideal.md)【證明 (c)】（$\mathbf{Z}$ 是 PID）逐字相同 ——
  那裡的「最小正元素」就是這裡的「$d$ 值最小的非零元素」。**本證明一次涵蓋了 $\mathbf{Z}$、$F[x]$、$\mathbf{Z}[i]$。**
* 註：條件 (1) 在本證明中**沒有用到**；它只是讓 $d$ 與「整除」相容（$a \mid b \Rightarrow d(a) \le d(b)$），
  在討論單位元素時才需要。

### (e) proof that the extended Euclidean algorithm works for polynomials

**貝祖等式**：由【證明 (b)(d)】，$F[x]$ 的理想 $\left\langle a, b \right\rangle$ 是主理想：

$$\begin{gather*}
\left\langle a, b \right\rangle &\overset{\text{證明 (d)}}{=}& \left\langle g \right\rangle \\
g &\overset{\text{定義 2}}{=}& \gcd\left(a, b\right) \qquad \text{(取首一生成元)} \\
g \in \left\langle a, b \right\rangle &\overset{\text{已知 5(b)}}{\Longrightarrow}& g = a\,u + b\,v \ \text{ for some } u, v \in F[x]
\end{gather*}$$

**它確實是「最大」公因式**：$a, b \in \left\langle g \right\rangle$ 故 $g$ 整除兩者；任何公因式 $c$ 都整除 $au + bv = g$：

$$\begin{gather*}
a,\ b &\overset{\text{已知 5(c)}}{\in}& \left\langle g \right\rangle \qquad \text{(即 } g \mid a,\ g \mid b\text{)} \\
c \mid a,\ c \mid b &\Longrightarrow& c \mid \left(au + bv\right) = g
\end{gather*}$$

**歐幾里得演算法**：由【已知 2】寫 $a = bq + r$，則兩組生成元生成同一個理想：

$$\begin{gather*}
r = a - bq \in \left\langle a, b \right\rangle, \quad a = bq + r &\in& \left\langle b, r \right\rangle \\
\left\langle a, b \right\rangle &\overset{\text{已知 5(b)}}{=}& \left\langle b, r \right\rangle \\
\gcd\left(a, b\right) &\overset{\text{定義 2}}{=}& \gcd\left(b,\ a \bmod b\right)
\end{gather*}$$

每一步餘式的次數嚴格下降，故有限步後餘式為 $0$，最後一個非零餘式（化為首一）即 $\gcd$；
把每一步的 $r = a - bq$ 往回代，就得到 $u, v$ —— 這就是**擴展**歐幾里得演算法。

**例子**（在 $GF(2)[x]$ 中，$a = x^3 + x + 1$、$b = x^2 + 1$）：

$$\begin{gather*}
x^3 + x + 1 &\overset{\text{已知 2}}{=}& x\left(x^2 + 1\right) + 1 \\
1 &=& \left(x^3 + x + 1\right) - x\left(x^2 + 1\right) \\
1 &=& \left(x^3 + x + 1\right) \cdot 1 + \left(x^2 + 1\right) \cdot x \qquad \text{(} GF(2) \text{ 中 } -1 = 1\text{)}
\end{gather*}$$

故 $\gcd = 1$、$u = 1$、$v = x$。模 $x^3 + x + 1$ 看，$\left(x^2 + 1\right) \cdot x \equiv 1$ ——
**$x$ 就是 $x^2 + 1$ 在 $GF(2)[x]/\left\langle x^3 + x + 1 \right\rangle$ 中的乘法反元素**。

* 註：這正是 [模不可約多項式的商環是體](../../Abstract_Algebra/Field/Quotient_by_Irreducible_is_Field.md)【證明 (a)】
  求反元素的機制；該檔當時引用的「多項式版貝祖等式」由本證明補齊。

+++

## 意義與密碼學關聯 (Interpretation and Relevance to Cryptography)

### 一個定義，三個世界

| 歐幾里得整環 | $d$ | 密碼學用途 |
|---|---|---|
| $\mathbf{Z}$ | $\left|a\right|$ | RSA 私鑰 $d = e^{-1} \bmod \varphi(n)$ |
| $GF(2)[x]$ | $\deg a$ | AES S-box 的 $GF(2^8)$ 反元素 |
| $\mathbf{Z}[i]$ | $a^2 + b^2$ | 費馬二平方定理、某些格密碼的代數結構 |

三者的擴展歐幾里得演算法**是同一份程式碼**，只把「除法」換掉。

### 常數時間的反元素

擴展歐幾里得演算法的迴圈次數與輸入有關，會洩漏時間資訊。
AES 的軟體實作因此常改用費馬小定理的類比 $a^{-1} = a^{2^8 - 2} = a^{254}$
（見 [$x^q - x$ 的根](../Structure/Roots_of_x_q_minus_x.md)），
或直接查表；硬體則用 [塔定理](../../Abstract_Algebra/Field/Tower_Law.md) 把 $GF(2^8)$ 拆成 $GF\left(\left(2^4\right)^2\right)$ 再求逆。

### 程式思維

```python
def ext_euclid_gf2(a, b):
    """GF(2)[x] 的擴展歐幾里得（多項式以整數位元表示）。回傳 (g, u, v) with a*u + b*v = g。"""
    def divmod2(x, y):
        q = 0
        while x and x.bit_length() >= y.bit_length():
            s = x.bit_length() - y.bit_length()
            q ^= 1 << s
            x ^= y << s
        return q, x
    def mul2(x, y):
        r = 0
        while y:
            if y & 1:
                r ^= x
            x <<= 1; y >>= 1
        return r
    u0, v0, u1, v1 = 1, 0, 0, 1
    while b:
        q, r = divmod2(a, b)
        a, b = b, r
        u0, u1 = u1, u0 ^ mul2(q, u1)
        v0, v1 = v1, v0 ^ mul2(q, v1)
    return a, u0, v0

assert ext_euclid_gf2(0b1011, 0b101) == (1, 1, 0b10)   # 證明 (e) 的例子：u = 1, v = x
```
