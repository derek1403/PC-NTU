# Primitive Polynomial (本原多項式)

+++

## 證明目標:

`FiniteFields.pdf` p.42（Definition）、p.44、p.45。
不可約多項式保證「模它得到一個體」；**本原多項式**更進一步保證「$\left[x\right]$ 本身就是乘法群的生成元」——
於是整個體可以寫成 $\left\{0, 1, \left[x\right], \left[x\right]^2, \dots\right\}$，乘法變成指數加法。

* (a) 投影片 p.42 的 Definition 與其等價刻畫：$n$ 次首一不可約 $f \in GF(p)[x]$，

$$f \ \text{為本原多項式} \quad \Longleftrightarrow \quad \mathrm{ord}(f) = p^n - 1 \quad \Longleftrightarrow \quad \left[x\right] \ \text{生成} \left(GF(p)[x]/\left\langle f \right\rangle\right)^*$$

* (b) 投影片 p.44 的證明實際給出：每個 $n$ 都有 $n$ 次本原多項式，且個數為

$$\frac{\varphi\left(p^n - 1\right)}{n}$$

* (c) 本原元判準（投影片 p.45 的做法的理論依據）：

$$o(\alpha) = N \quad \Longleftrightarrow \quad \alpha^{N/r} \neq 1 \ \text{對 } N \text{ 的每個質因數 } r \qquad \left(N = p^n - 1\right)$$

* (d) 投影片 p.45 的 Example：$g(x) = x^2 + 3$ 在 $GF(5)$ 上不可約，而在 $GF(25) = GF(5)[x]/\left\langle g \right\rangle$ 中 $x + 3$ 是本原元：

$$\left(x + 3\right)^{8} = 2x + 2, \qquad \left(x + 3\right)^{12} = 4, \qquad \left(x + 3\right)^{24} = 1$$

* (e) 投影片 p.45 的問題「Is $g(x)$ a primitive polynomial? If not, how to get one?」：

$$x^2 + 3 \ \text{不是本原多項式}\ \left(\mathrm{ord} = 8\right), \qquad x^2 + 4x + 2 \ \text{是}\ \left(x + 3 \text{ 的極小多項式}\right)$$

* $p$ : 質數 (A prime) $[p \in \mathbf{P}]$
* $n$ : 次數 (The degree) $[n \in \mathbf{P}]$
* $f$ : 首一不可約多項式 (A monic irreducible polynomial) $[f \in GF(p)[x]]$
* $N$ : 乘法群的階 (The order of the multiplicative group) $[N = p^n - 1]$
* $r$ : $N$ 的質因數 (A prime divisor of $N$) $[r \in \mathbf{P}]$
* $\alpha$ : $GF(p^n)$ 的非零元素 (A non-zero element of $GF(p^n)$) $[\alpha \in GF(p^n)^*]$
* 註：投影片 p.45 說「find $q(x)$ such that $\left(q(x)^{24} \bmod x^2 + 3\right) \bmod 5 = 1$ and $\neq 1$ with less power」——
  字面上要檢查**所有**較小的冪次；(c) 證明只需檢查 $24/2 = 12$ 與 $24/3 = 8$ 兩個，投影片實際上也只算了這兩個。
* 註：投影片 p.44 的 Theorem 陳述為「存在不可約多項式」，但它的證明取的是**本原元**的極小多項式，
  所以實際上證出的是更強的「存在本原多項式」—— 本檔 (b) 據此陳述。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [多項式的階等於根的階 (The order of a polynomial equals the order of its roots)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Finite_Fields/Multiplicative_Group/Order_of_a_Polynomial.html#b-proof-that-the-order-of-an-irreducible-polynomial-equals-the-order-of-its-roots)：** 已於本章 [多項式的階](Order_of_a_Polynomial.md)【證明 (b)】完整證明，此處直接引用不再重證

  $$f \ \text{不可約},\ f(0) \neq 0,\ f(\alpha) = 0 \quad \Longrightarrow \quad \mathrm{ord}(f) = o(\alpha)$$

* **【已知 2】 [本原元與其個數 (Primitive elements and their number)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Finite_Fields/Multiplicative_Group/Cyclic_Multiplicative_Group_of_Finite_Field.html#b-proof-that-the-multiplicative-group-of-a-finite-field-is-cyclic)：** 已於本章 [有限體的乘法群是循環群](Cyclic_Multiplicative_Group_of_Finite_Field.md)【定義 1】【證明 (b)】完整證明，此處直接引用不再重證

  $$\alpha \ \text{為本原元} \ \Longleftrightarrow \ o(\alpha) = p^n - 1; \qquad \text{本原元恰有 } \varphi\left(p^n - 1\right) \text{ 個}$$

* **【已知 3】 [極小多項式 (Minimal polynomial)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Finite_Fields/Multiplicative_Group/Minimal_Polynomial.html#c-proof-of-the-divisibility-characterization-of-the-minimal-polynomial)：** 已於本章 [極小多項式](Minimal_Polynomial.md)【證明 (b)(c)】完整證明，此處直接引用不再重證

  * (a) 極小多項式不可約（投影片 p.42 的 Lemma）：

    $$g_\alpha \ \text{為質多項式}$$

  * (b) 首一不可約零化多項式即極小多項式：

    $$h \ \text{首一不可約},\ h(\alpha) = 0 \quad \Longrightarrow \quad h = g_\alpha$$

  * $g_\alpha$ : $\alpha$ 的極小多項式 (The minimal polynomial of $\alpha$) $[g_\alpha \in GF(p)[x]]$

* **【已知 4】 [極小多項式的根是 n 個相異共軛元 (The roots are n distinct conjugates)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Finite_Fields/Multiplicative_Group/Conjugates_and_Cyclotomic_Cosets.html#c-proof-that-the-minimal-polynomial-is-the-product-over-the-conjugates)：** 已於本章 [共軛元與分圓陪集](Conjugates_and_Cyclotomic_Cosets.md)【證明 (c)】完整證明，此處直接引用不再重證

  $$g_\alpha = \prod_{i=0}^{k-1}\left(x - \alpha^{p^i}\right), \qquad \alpha^{p^i} \ \text{兩兩相異}, \qquad k = \deg g_\alpha$$

* **【已知 5】 [本原元的極小多項式是 n 次 (The minimal polynomial of a primitive element has degree n)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Finite_Fields/Multiplicative_Group/Factorization_of_x_p_n_minus_x.html#e-proof-that-prime-polynomials-of-every-degree-exist)：** 已於本章 [$x^{p^n}-x$ 的分解](Factorization_of_x_p_n_minus_x.md)【證明 (e)】完整證明，此處直接引用不再重證

  $$\alpha \ \text{為 } GF(p^n) \text{ 的本原元} \quad \Longrightarrow \quad \deg g_\alpha = n$$

* **【已知 6】 [冪次為 1 的刻畫 (When a power is the identity)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Finite_Fields/Multiplicative_Group/Euler_Phi_and_Cyclic_Group_Orders.html#a-proof-that-a-power-is-the-identity-exactly-when-the-order-divides-the-exponent)：** 已於本章 [尤拉函數與循環群中元素的階](Euler_Phi_and_Cyclic_Group_Orders.md)【證明 (a)】與 [元素的階與循環子群](../../Abstract_Algebra/Group/Order_of_Element_and_Cyclic_Subgroup.md)【證明 (b)】完整證明，此處直接引用不再重證

  $$\alpha^e = 1 \ \Longleftrightarrow \ o(\alpha) \mid e, \qquad o(\alpha) \mid N$$

* **【已知 7】 [二次不可約判別法 (Root criterion for quadratics)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Field/Irreducible_Polynomial.html#a-proof-of-the-root-criterion-for-degrees-two-and-three)：** 已於 [不可約多項式](../../Abstract_Algebra/Field/Irreducible_Polynomial.md)【證明 (a)】完整證明，此處直接引用不再重證

  $$\deg h = 2 \quad \Longrightarrow \quad \left[\, h \ \text{不可約} \Leftrightarrow h \ \text{無根} \,\right]$$

* **【已知 8】 [GF(p^n) 的構造 (Construction of GF(p^n))](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Finite_Fields/Construction/Construction_of_GF_p_n.html#a-proof-that-the-remainder-set-is-a-field-with-p-to-the-n-elements)：** 已於本章 [GF(p^n) 的構造](../Construction/Construction_of_GF_p_n.md)【證明 (a)】完整證明，此處直接引用不再重證

  $$g \ \text{不可約},\ \deg g = n \quad \Longrightarrow \quad GF(p)[x]\big/\left\langle g \right\rangle \ \text{是 } p^n \text{ 元素的體}$$

* **【定義 1】 本原多項式 (Primitive polynomial)：** 投影片 p.42

  $$f \ \text{為本原多項式} \quad \overset{\text{def}}{\Longleftrightarrow} \quad f = g_\alpha \ \text{for some 本原元} \ \alpha \in GF(p^n), \ \deg f = n$$

  * $f$ : 本原多項式 (A primitive polynomial) $[f \in GF(p)[x]]$

* **【假設 1】 一個 $n$ 次質多項式 (A prime polynomial of degree n)：** 【證明 (a)】的前提

  $$f \in GF(p)[x] \ \text{首一不可約}, \qquad \deg f = n, \qquad \alpha = \left[x\right] \in GF(p)[x]/\left\langle f \right\rangle$$

  * 註：$n = 1$ 且 $f = x$ 時 $f(0) = 0$，$\left[x\right] = 0$ 不在乘法群中；以下默認 $f \neq x$，故 $f(0) \neq 0$（不可約且非 $x$ 則 $x \nmid f$）。

+++

## 證明:

### (a) proof of the order criterion for primitive polynomials

由【假設 1】，$\alpha = \left[x\right]$ 是 $f$ 的根，$f$ 是它的極小多項式；再由【已知 1】：

$$\begin{gather*}
f &\overset{\text{已知 3(b),假設 1}}{=}& g_\alpha \\
\mathrm{ord}(f) &\overset{\text{已知 1}}{=}& o(\alpha) \\
\mathrm{ord}(f) = p^n - 1 &\overset{\text{已知 2}}{\Longleftrightarrow}& \alpha = \left[x\right] \ \text{是本原元}
\end{gather*}$$

**與【定義 1】等價**：若 $f$ 為本原多項式，$f = g_\beta$（$\beta$ 本原元），則 $\mathrm{ord}(f) = o(\beta) = p^n - 1$；
反之若 $\mathrm{ord}(f) = p^n - 1$，上式說 $\left[x\right]$ 是本原元且 $f = g_{[x]}$：

$$f \ \text{為本原多項式} \quad \overset{\text{定義 1,已知 1}}{\Longleftrightarrow} \quad \mathrm{ord}(f) = p^n - 1$$

* 註：這就是投影片 p.24 表中「$e = 2^n - 1$」那些列的意思 —— **它們是本原多項式**。

### (b) proof of the existence and the number of primitive polynomials

**存在**：取本原元 $\alpha$（【已知 2】保證 $\varphi\left(p^n - 1\right) \ge 1$ 個），其極小多項式不可約且為 $n$ 次：

$$\begin{gather*}
g_\alpha &\overset{\text{已知 3(a)}}{=}& \text{質多項式} \\
\deg g_\alpha &\overset{\text{已知 5}}{=}& n \\
g_\alpha &\overset{\text{定義 1}}{=}& n \ \text{次本原多項式}
\end{gather*}$$

**計數**：每個本原多項式 $f$ 恰有 $n$ 個相異的根，且全是本原元（它們的階都等於 $\mathrm{ord}(f) = p^n - 1$）；
每個本原元恰屬於一個本原多項式（它自己的極小多項式）。於是「本原元 $\to$ 本原多項式」是 $n$ 對 $1$ 的滿射：

$$\begin{gather*}
\left|\left\{f \text{ 的根}\right\}\right| &\overset{\text{已知 4,已知 5}}{=}& n \\
o(\text{每個根}) &\overset{\text{已知 1}}{=}& \mathrm{ord}(f) = p^n - 1 \\
\left|\left\{\text{本原多項式}\right\}\right| &\overset{\text{已知 2}}{=}& \frac{\varphi\left(p^n - 1\right)}{n}
\end{gather*}$$

**驗證**：$p = 2$、$n = 8$ 時 $\varphi(255) = \varphi(3)\varphi(5)\varphi(17) = 2 \cdot 4 \cdot 16 = 128$，本原多項式有 $128/8 = 16$ 個，
與投影片 p.24 表中 $n = 8$ 標 $e = 255$ 的列數（$16$ 列）一致。

### (c) proof of the prime divisor test for primitive elements

由【已知 6】$o(\alpha) \mid N$。若 $o(\alpha) < N$，則 $N / o(\alpha) > 1$ 有質因數 $r$，於是 $o(\alpha) \mid N / r$：

$$\begin{gather*}
o(\alpha) \mid N,\ o(\alpha) < N &\Longrightarrow& o(\alpha) \mid \tfrac{N}{r} \ \text{ for some prime } r \mid N \\
o(\alpha) \mid \tfrac{N}{r} &\overset{\text{已知 6}}{\Longleftrightarrow}& \alpha^{N/r} = 1
\end{gather*}$$

取逆否：若對每個質因數 $r$ 都有 $\alpha^{N/r} \neq 1$，則 $o(\alpha) = N$。反向顯然（$o(\alpha) = N$ 時 $N/r < N$ 次方不為 $1$）。

### (d) verify the primitive element of GF(25)

**$g$ 不可約**：$g(0), \dots, g(4) = 3, 4, 7, 12, 19 \equiv 3, 4, 2, 2, 4$，都不為 $0$：

$$\begin{gather*}
x^2 + 3 &\overset{\text{已知 7}}{=}& \text{在 } GF(5) \text{ 上不可約} \\
GF(5)[x]\big/\left\langle x^2 + 3 \right\rangle &\overset{\text{已知 8}}{=}& 25 \text{ 元素的體} = GF(25)
\end{gather*}$$

**計算冪次**（$x^2 \equiv -3 \equiv 2$，係數模 $5$）：

$$\begin{gather*}
\left(x + 3\right)^2 &=& x^2 + 6x + 9 \equiv 2 + x + 4 \equiv x + 1 \\
\left(x + 3\right)^4 &=& \left(x + 1\right)^2 = x^2 + 2x + 1 \equiv 2x + 3 \\
\left(x + 3\right)^8 &=& \left(2x + 3\right)^2 = 4x^2 + 12x + 9 \equiv 8 + 2x + 9 \equiv 2x + 2 \\
\left(x + 3\right)^{12} &=& \left(2x + 2\right)\left(2x + 3\right) = 4x^2 + 10x + 6 \equiv 8 + 0 + 6 \equiv 4 \\
\left(x + 3\right)^{24} &=& 4^2 = 16 \equiv 1
\end{gather*}$$

$N = 24 = 2^3 \cdot 3$，質因數 $r = 2, 3$，$N/2 = 12$、$N/3 = 8$，兩者都不給 $1$：

$$o\!\left(x + 3\right) \overset{\text{證明 (c)}}{=} 24$$

故 $x + 3$ 是 $GF(25)$ 的本原元。三個數值與投影片 p.45 一致。

### (e) answer whether x squared plus three is a primitive polynomial

**$x^2 + 3$ 不是本原多項式**：$\left[x\right]$ 的階只有 $8$：

$$\begin{gather*}
\left[x\right]^2 &\equiv& 2 \\
\left[x\right]^4 &\equiv& 4 \\
\left[x\right]^8 &\equiv& 16 \equiv 1 \\
\mathrm{ord}\left(x^2 + 3\right) &\overset{\text{已知 1}}{=}& o\!\left(\left[x\right]\right) \le 8 < 24
\end{gather*}$$

由【證明 (a)】它不是本原多項式。**得到一個本原多項式**：取本原元 $\beta = x + 3$ 的極小多項式。
$\beta - 3 = \left[x\right]$，而 $\left[x\right]^2 = 2$：

$$\begin{gather*}
\left(\beta - 3\right)^2 &=& 2 \\
\beta^2 - 6\beta + 9 - 2 &=& 0 \\
\beta^2 + 4\beta + 2 &=& 0 \qquad \text{(係數模 } 5\text{)}
\end{gather*}$$

$h = x^2 + 4x + 2$ 在 $GF(5)$ 中無根（$h(0), \dots, h(4) \equiv 2, 2, 4, 3, 4$），故不可約；它首一、以本原元 $\beta$ 為根：

$$\begin{gather*}
h &\overset{\text{已知 7}}{=}& \text{質多項式} \\
h &\overset{\text{已知 3(b)}}{=}& g_\beta \\
x^2 + 4x + 2 &\overset{\text{定義 1,證明 (d)}}{=}& \text{本原多項式}
\end{gather*}$$

* 註：換句話說，在 $GF(25) = GF(5)[y]/\left\langle y^2 + 4y + 2 \right\rangle$ 中，$\left[y\right]$ 自己就是生成元 ——
  這正是「how to get one」的答案：**找一個本原元，取它的極小多項式**。

+++

## 意義與密碼學關聯 (Interpretation and Relevance to Cryptography)

### LFSR 與流密碼

以本原多項式為回饋的 $n$ 級 LFSR 產生週期 $2^n - 1$ 的 m-序列，擁有良好的統計性質（平衡、遊程分布、雙值自相關）。
A5/1（GSM）、E0（藍牙）、Trivium、SNOW 3G 的線性部分都建立在本原多項式上。
**但 m-序列本身是線性的**：Berlekamp–Massey 演算法只需 $2n$ 個輸出就能還原整個 LFSR ——
所以流密碼必須再加上非線性組合或濾波函數。

### 本原多項式 vs 不可約多項式：各取所需

| 用途 | 需要 | 例子 |
|---|---|---|
| 體的構造（取反元素） | 不可約即可 | AES 的 $x^8 + x^4 + x^3 + x + 1$（$e = 51$，**非**本原） |
| 對數表 / 冪次表 | $\left[x\right]$ 最好是本原元 | Reed–Solomon 碼常選本原多項式 $x^8 + x^4 + x^3 + x^2 + 1$ |
| LFSR 最大週期 | 必須本原 | CRC、擾碼器、偽隨機序列 |

### 程式思維

```python
def gf_pow(a, e, mod, p):
    """GF(p)[x]/<mod> 中的冪次（係數低到高，mod 首一二次）。"""
    def mul(u, v):
        r = [0] * (len(u) + len(v) - 1)
        for i, x in enumerate(u):
            for j, y in enumerate(v):
                r[i + j] = (r[i + j] + x * y) % p
        while len(r) > 2:                   # 模 x^2 + c1 x + c0
            c = r.pop()
            r[-1] = (r[-1] - c * mod[1]) % p
            r[-2] = (r[-2] - c * mod[0]) % p
        return r + [0] * (2 - len(r))
    out = [1, 0]
    for _ in range(e):
        out = mul(out, a)
    return out

g = [3, 0, 1]                                  # x^2 + 3
beta = [3, 1]                                  # x + 3
assert gf_pow(beta, 8, g, 5) == [2, 2]         # 2x + 2
assert gf_pow(beta, 12, g, 5) == [4, 0]        # 4
assert gf_pow(beta, 24, g, 5) == [1, 0]        # 1   —— 證明 (d)
assert gf_pow([0, 1], 8, g, 5) == [1, 0]       # [x]^8 = 1 —— 證明 (e)：x^2 + 3 非本原
```
