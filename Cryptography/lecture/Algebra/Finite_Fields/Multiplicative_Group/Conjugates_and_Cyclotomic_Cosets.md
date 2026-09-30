# Conjugates and Cyclotomic Cosets (共軛元與分圓陪集)

+++

## 證明目標:

`FiniteFields.pdf` p.23（Fact）、p.21（Minimal Polynomial 欄）；補充講義 §7.8.4（Lemma 7.19、7.20、Exercise 14、Theorem 7.21、Example 3 續）。
**極小多項式的根長什麼樣？** 答案出奇地整齊：一個根 $\beta$ 決定了全部 —— 其餘的根是 $\beta^p, \beta^{p^2}, \dots$。

* (a) 投影片 p.23 的 Fact（投影片寫 $p = 2$，本檔對一般 $p$）：

$$f \in GF(p)[x],\ f(u) = 0 \quad \Longrightarrow \quad f\!\left(u^{p^r}\right) = 0 \qquad \text{for all } r \in \mathbf{N}$$

* (b) 補充講義 Exercise 14 與 Lemma 7.20：在特徵 $p$ 的體 $L$ 上，對 $f = \sum f_i x^i \in L[x]$，

$$f(x)^p = \sum_i f_i^{\,p}\,x^{ip}, \qquad f(x)^p = f\!\left(x^p\right) \ \Longleftrightarrow \ \text{所有 } f_i \in GF(p)$$

* (c) 補充講義 Theorem 7.21：$\beta \in GF(p^m)$，令 $k$ 為使 $\beta^{p^k} = \beta$ 的最小正整數，則 $\beta$ 在 $GF(p)$ 上的極小多項式為

$$g(x) = \prod_{i=0}^{k-1}\left(x - \beta^{p^i}\right), \qquad \deg g = k, \qquad k \mid m$$

* (d) 驗證投影片 p.21 的極小多項式欄（$GF(8)$）與補充講義 Example 3 的分圓陪集（$GF(16)$）。

* $p$ : 特徵 (The characteristic) $[p \in \mathbf{P},\ \text{質數}]$
* $f$ : $GF(p)$ 係數的多項式 (A polynomial over $GF(p)$) $[f \in GF(p)[x]]$
* $u,\ \beta$ : 擴張體中的元素 (Elements of an extension) $[u, \beta \in GF(p^m)]$
* $r$ : 自然數 (A natural number) $[r \in \mathbf{N}]$
* $L$ : 特徵 $p$ 的體 (A field of characteristic $p$) $[\text{體}]$
* $k$ : $\beta$ 的共軛元個數 (The number of conjugates of $\beta$) $[k \in \mathbf{P}]$
* $g$ : $\beta$ 的極小多項式 (The minimal polynomial of $\beta$) $[g \in GF(p)[x]]$
* 註：$\left\{\beta, \beta^p, \dots, \beta^{p^{k-1}}\right\}$ 稱為 $\beta$ 的**共軛元 (conjugates)**；
  取 $\beta = \alpha^j$（$\alpha$ 本原元）時，對應的指數集合 $\left\{j, jp, jp^2, \dots\right\} \bmod \left(p^m - 1\right)$ 稱為**分圓陪集 (cyclotomic coset)**。
* 註：投影片 p.23 的推導最後一步寫「$= f(u)^{2^r} = 0$」，其中用到 $c_i^{\,2} = c_i$（係數在 $GF(2)$）——
  投影片沒有明說，本檔 (a) 以【已知 2(b)】補上；**係數不在 $GF(p)$ 時結論不成立**，見 (b)。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [新生之夢 (Freshman's dream)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Field/Freshmans_Dream.html#b-proof-of-the-inductive-step)：** 已於 [新生之夢](../../Abstract_Algebra/Field/Freshmans_Dream.md)【證明 (a)(b)】完整證明，此處直接引用不再重證。
  該證明只用到二項式定理（交換環皆成立）與「$p$ 倍為零」，故對**任何特徵 $p$ 的交換環**（包含 $L$ 與 $L[x]$）都成立

  $$\left(a + b\right)^{p^r} = a^{p^r} + b^{p^r}$$

  * $a,\ b$ : 特徵 $p$ 交換環的元素 (Elements of a commutative ring of characteristic $p$) $[a, b \in L \text{ 或 } L[x]]$
  * $r$ : 自然數 (A natural number) $[r \in \mathbf{N}]$

* **【已知 2】 [$x^q - x$ 的根 (Roots of x^q − x)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Finite_Fields/Structure/Roots_of_x_q_minus_x.html#a-proof-that-every-element-satisfies-the-finite-field-version-of-fermats-theorem)：** 已於本章 [$x^q - x$ 的根](../Structure/Roots_of_x_q_minus_x.md)【證明 (a)(b)】完整證明，此處直接引用不再重證

  * (a) $GF(p^m)$ 的元素滿足：

    $$\beta^{p^m} = \beta$$

  * (b) $GF(p)$ 的元素滿足（取 $q = p$）：

    $$c^p = c \qquad \left(c \in GF(p)\right)$$

  * $c$ : 質子體的元素 (An element of the prime subfield) $[c \in GF(p)]$

* **【已知 3】 [多項式的根 (Roots of polynomials)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Finite_Fields/Polynomial_Arithmetic/Roots_of_Polynomials.html#c-proof-that-n-distinct-roots-determine-the-factorization)：** 已於本章 [多項式的根](../Polynomial_Arithmetic/Roots_of_Polynomials.md)【推導 1】【證明 (b)(c)】完整證明，此處直接引用不再重證

  * (a) $N$ 次非零多項式最多 $N$ 個根：

    $$\deg f = N,\ f \neq 0 \quad \Longrightarrow \quad \left|\left\{f \text{ 的根}\right\}\right| \le N$$

  * (b) 相異根的一次因式之積整除原多項式（【證明 (c)】前 $k$ 步）：

    $$g\!\left(\beta_1\right) = \cdots = g\!\left(\beta_k\right) = 0,\ \beta_i \ \text{相異} \quad \Longrightarrow \quad \prod_{i=1}^{k}\left(x - \beta_i\right) \ \Big|\ g$$

* **【已知 4】 [極小多項式的刻畫 (Characterization of the minimal polynomial)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Finite_Fields/Multiplicative_Group/Minimal_Polynomial.html#c-proof-of-the-divisibility-characterization-of-the-minimal-polynomial)：** 已於本章 [極小多項式](Minimal_Polynomial.md)【證明 (b)(c)】完整證明，此處直接引用不再重證

  * (a) 整除刻畫：

    $$h \in GF(p)[x],\ h(\beta) = 0 \quad \Longleftrightarrow \quad g \mid h$$

  * (b) 首一不可約零化多項式唯一：

    $$h \ \text{首一不可約},\ h(\beta) = 0 \quad \Longrightarrow \quad h = g$$

  * $h$ : 多項式 (A polynomial) $[h \in GF(p)[x]]$

* **【已知 5】 [質子體 (The prime subfield)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Finite_Fields/Structure/Order_of_a_Finite_Field.html#a-proof-that-every-finite-field-contains-a-copy-of-the-prime-field)：** 已於本章 [有限體的階](../Structure/Order_of_a_Finite_Field.md)【證明 (a)】完整證明，此處直接引用不再重證（證明只用到特徵 $p$，對無限體 $L$ 同樣適用）

  $$\mathrm{ch}(L) = p \quad \Longrightarrow \quad GF(p) \cong \left\{0, 1, \dots, \left(p-1\right) \cdot 1_L\right\} \subseteq L$$

* **【已知 6】 [整數除法原理 (Integer division algorithm)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Group/Order_of_Element_and_Cyclic_Subgroup.html#assumptions-preliminaries)：** 已於 [元素的階與循環子群](../../Abstract_Algebra/Group/Order_of_Element_and_Cyclic_Subgroup.md)【已知 6(b)】引用，此處再次引用

  $$m = s\,k + r, \qquad 0 \le r < k$$

  * $m,\ k,\ s,\ r$ : 整數 (Integers) $[\in \mathbf{Z}]$

* **【已知 7】 [GF(8) 與 GF(16) 的冪次表 (Power tables of GF(8) and GF(16))](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Finite_Fields/Construction/Galois_Fields_GF8_and_GF16.html#d-verify-that-every-element-is-a-root-of-x-to-the-eighth-minus-x)：** 已於本章 [伽羅瓦體 GF(8) 與 GF(16)](../Construction/Galois_Fields_GF8_and_GF16.md)【定義 1】【定義 2(a)】【證明 (c)(d)(e)】驗證，此處直接引用

  * (a) $GF(8)$：$\alpha^3 = \alpha + 1$，$o(\alpha) = 7$；$\alpha, \alpha^2, \alpha^4$ 是 $x^3 + x + 1$ 的根，$\alpha^3, \alpha^5, \alpha^6$ 是 $x^3 + x^2 + 1$ 的根：

    $$\alpha^7 = 1$$

  * (b) $GF(16)$：$\gamma^4 = \gamma + 1$，$o(\gamma) = 15$：

    $$\gamma^{15} = 1$$

* **【假設 1】 以 $u$ 為根的 $GF(p)$ 係數多項式 (A polynomial over GF(p) with root u)：** 【證明 (a)】的前提

  $$f = \sum_{i} c_i x^i,\ c_i \in GF(p), \qquad f(u) = 0, \qquad u \in K \supseteq GF(p)$$

  * $K$ : 特徵 $p$ 的擴張體 (An extension of characteristic $p$) $[\text{體}]$

* **【假設 2】 有限體中的元素 (An element of a finite field)：** 【證明 (c)】的前提

  $$\beta \in F = GF(p^m)$$

  * $F$ : $p^m$ 元素的體 (The field with $p^m$ elements) $[\text{體}]$

* **【定義 1】 共軛元的個數 (The number of conjugates)：**

  $$k \overset{\text{def}}{=} \min\left\{j \in \mathbf{P} \ \middle|\ \beta^{p^j} = \beta\right\}$$

  * $k$ : 最小的「回到自己」的步數 (The least return time) $[k \in \mathbf{P}]$
  * 註：由【已知 2(a)】$j = m$ 在集合中，故集合非空，最小值存在。

* **【推導 1】 多項式形式的新生之夢 (The freshman's dream for sums and products)：** 【證明 (a)(b)(c)】共用

  * (a) 多項和：對項數 $s$ 歸納，每次拆成 $a_1 + \left(a_2 + \cdots + a_s\right)$

    $$\left(a_1 + a_2 + \cdots + a_s\right)^{p^r} \overset{\text{已知 1}}{=} a_1^{p^r} + a_2^{p^r} + \cdots + a_s^{p^r}$$

  * (b) 乘積（交換環）：

    $$\left(ab\right)^{p^r} = a^{p^r}\,b^{p^r}$$

  * $a_i,\ a,\ b$ : 特徵 $p$ 交換環的元素 (Ring elements) $[\in L \text{ 或 } L[x]]$
  * $s$ : 項數 (The number of summands) $[s \in \mathbf{P}]$

+++

## 證明:

### (a) proof that the p-th powers of a root are roots

投影片 p.23 的推導，推廣到一般 $p$：

$$\begin{gather*}
f\!\left(u^{p^r}\right) &\overset{\text{假設 1}}{=}& \sum_i c_i \left(u^{i}\right)^{p^r} \\
&\overset{\text{已知 2(b)}}{=}& \sum_i c_i^{\,p^r}\left(u^{i}\right)^{p^r} \qquad \text{(} c^p = c \text{ 反覆套用)} \\
&\overset{\text{推導 1(b)}}{=}& \sum_i \left(c_i u^{i}\right)^{p^r} \\
&\overset{\text{推導 1(a)}}{=}& \left(\sum_i c_i u^{i}\right)^{p^r} \\
&\overset{\text{假設 1}}{=}& 0^{p^r} = 0
\end{gather*}$$

與投影片 p.23「$f\!\left(u^{2^r}\right) = \cdots = f(u)^{2^r} = 0$」一致。

### (b) proof of the prime subfield criterion for polynomials

**第一式**（Exercise 14，$r = 1$）：在交換環 $L[x]$ 中套【推導 1】：

$$\begin{gather*}
f(x)^p &=& \left(\sum_i f_i x^i\right)^p \\
&\overset{\text{推導 1(a)}}{=}& \sum_i \left(f_i x^i\right)^p \\
&\overset{\text{推導 1(b)}}{=}& \sum_i f_i^{\,p}\,x^{ip}
\end{gather*}$$

**等價條件**（Lemma 7.20）：$f\!\left(x^p\right) = \sum_i f_i x^{ip}$，兩式逐項比較係數：

$$\begin{gather*}
f(x)^p = f\!\left(x^p\right) &\Longleftrightarrow& f_i^{\,p} = f_i \quad \forall i \\
\left\{c \in L \ \middle|\ c^p = c\right\} &\overset{\text{已知 2(b),已知 5}}{\supseteq}& GF(p) \qquad \text{(已有 } p \text{ 個根)} \\
\left\{c \in L \ \middle|\ c^p = c\right\} &\overset{\text{已知 3(a)}}{=}& GF(p) \qquad \text{(} x^p - x \text{ 最多 } p \text{ 個根)} \\
f(x)^p = f\!\left(x^p\right) &\Longleftrightarrow& f_i \in GF(p) \quad \forall i
\end{gather*}$$

與補充講義 Lemma 7.20 一致。

* 註：這是「一個多項式的係數是否全在質子體裡」的**代數判準** —— 不必看係數，只要檢查 $f^p$ 與 $f(x^p)$ 是否相同。
  【證明 (c)】正是用它證明 $\prod\left(x - \beta^{p^i}\right)$ 的係數落在 $GF(p)$。

### (c) proof that the minimal polynomial is the product over the conjugates

**共軛元兩兩相異**：設 $0 \le i < j < k$ 且 $\beta^{p^i} = \beta^{p^j}$，兩邊再取 $p^{k-j}$ 次方：

$$\begin{gather*}
\beta^{p^{i + k - j}} &=& \beta^{p^{k}} \\
\beta^{p^{i + k - j}} &\overset{\text{定義 1}}{=}& \beta \\
0 < i + k - j &<& k
\end{gather*}$$

與【定義 1】的最小性矛盾。**$k \mid m$**：由【已知 6】寫 $m = sk + r$，並注意 $\beta^{p^{sk}} = \beta$（【定義 1】反覆套用 $s$ 次）：

$$\begin{gather*}
\beta &\overset{\text{已知 2(a),假設 2}}{=}& \beta^{p^m} \\
\beta &=& \left(\beta^{p^{sk}}\right)^{p^r} \\
\beta &\overset{\text{定義 1}}{=}& \beta^{p^r}, \qquad 0 \le r < k \\
r &\overset{\text{定義 1}}{=}& 0 \qquad \text{(若 } r > 0 \text{ 與最小性矛盾)}
\end{gather*}$$

**$h = \prod_{i=0}^{k-1}\left(x - \beta^{p^i}\right)$ 的係數在 $GF(p)$**：在 $F[x]$ 中取 $p$ 次方，下標平移一格後用 $\beta^{p^k} = \beta$ 繞回：

$$\begin{gather*}
h(x)^p &\overset{\text{推導 1(b)}}{=}& \prod_{i=0}^{k-1}\left(x - \beta^{p^i}\right)^p \\
&\overset{\text{推導 1(a)}}{=}& \prod_{i=0}^{k-1}\left(x^p - \beta^{p^{i+1}}\right) \\
&\overset{\text{定義 1}}{=}& \prod_{i=0}^{k-1}\left(x^p - \beta^{p^{i}}\right) \\
&=& h\!\left(x^p\right)
\end{gather*}$$

**$h = g$**：由【證明 (b)】$h \in GF(p)[x]$；由【證明 (a)】每個 $\beta^{p^i}$ 都是 $g$ 的根，於是兩者互相整除：

$$\begin{gather*}
h &\overset{\text{證明 (b)}}{\in}& GF(p)[x] \\
h(\beta) = 0 &\overset{\text{已知 4(a)}}{\Longrightarrow}& g \mid h \\
g\!\left(\beta^{p^i}\right) &\overset{\text{證明 (a)}}{=}& 0 \qquad \text{for } 0 \le i < k \\
h &\overset{\text{已知 3(b)}}{\mid}& g \\
h &=& g \qquad \text{(互相整除且皆首一)}
\end{gather*}$$

故 $g = \prod_{i=0}^{k-1}\left(x - \beta^{p^i}\right)$，$\deg g = k \mid m$。與補充講義 Theorem 7.21 一致。

### (d) verify the minimal polynomials in GF(8) and the cyclotomic cosets in GF(16)

**$GF(8)$**（$p = 2$、$m = 3$、$\alpha$ 本原元）：指數反覆乘以 $2$（模 $7$），得分圓陪集

$$\begin{gather*}
\left\{0\right\} &\longrightarrow& \alpha^0 = 1 \ \text{的極小多項式} \ x + 1 \\
\left\{1, 2, 4\right\} &\overset{\text{證明 (c),已知 7(a)}}{\longrightarrow}& \left(x - \alpha\right)\left(x - \alpha^2\right)\left(x - \alpha^4\right) = x^3 + x + 1 \\
\left\{3, 6, 12 \equiv 5\right\} &\overset{\text{證明 (c),已知 7(a)}}{\longrightarrow}& \left(x - \alpha^3\right)\left(x - \alpha^6\right)\left(x - \alpha^5\right) = x^3 + x^2 + 1
\end{gather*}$$

加上 $0$ 的極小多項式 $x$，與投影片 p.21 的 Minimal Polynomial 欄**逐列一致**。
（三次式的等號：兩邊都是首一三次、有相同的三個相異根，由【已知 7(a)】與【已知 4(b)】。）

**$GF(16)$**（$p = 2$、$m = 4$、$\gamma$ 本原元）：指數反覆乘以 $2$（模 $15$）：

$$\begin{gather*}
\left\{1, 2, 4, 8\right\} &\longrightarrow& x^4 + x + 1 \\
\left\{3, 6, 12, 9\right\} &\longrightarrow& x^4 + x^3 + x^2 + x + 1 \\
\left\{5, 10\right\} &\longrightarrow& x^2 + x + 1 \\
\left\{7, 14, 13, 11\right\} &\longrightarrow& x^4 + x^3 + 1
\end{gather*}$$

以 $\gamma^7$ 驗證最後一列（由【已知 7(b)】化簡指數，再用 $\gamma^4 = \gamma + 1$ 展開：$\gamma^6 = \gamma^3 + \gamma^2$、$\gamma^{13} = \gamma^3 + \gamma^2 + 1$）：

$$\begin{gather*}
\left(\gamma^7\right)^4 + \left(\gamma^7\right)^3 + 1 &\overset{\text{已知 7(b)}}{=}& \gamma^{13} + \gamma^{6} + 1 \\
&=& \left(\gamma^3 + \gamma^2 + 1\right) + \left(\gamma^3 + \gamma^2\right) + 1 \\
&=& 0
\end{gather*}$$

其餘三列同理（$\gamma^5$ 的階為 $3$，故為 $\frac{x^3 - 1}{x - 1} = x^2 + x + 1$ 的根；$\gamma^3$ 的階為 $5$，故為 $\frac{x^5 - 1}{x - 1}$ 的根）。
**陪集大小 $1, 4, 4, 2, 4$ 都整除 $m = 4$**，與【證明 (c)】一致；也與補充講義 Example 3 的列表一致。

+++

## 意義與密碼學關聯 (Interpretation and Relevance to Cryptography)

### Frobenius 映射在這裡現身

$\sigma(x) = x^p$ 是 [新生之夢](../../Abstract_Algebra/Field/Freshmans_Dream.md) 文末的 Frobenius 自同構。本檔 (c) 說：

$$\beta \text{ 的共軛元} = \beta \text{ 在 } \sigma \text{ 作用下的軌道} = \left\{\beta, \sigma(\beta), \sigma^2(\beta), \dots\right\}$$

**極小多項式 = 軌道上所有元素的一次因式之積**。這是伽羅瓦理論在有限體上最乾淨的樣貌：
伽羅瓦群就是 $\left\langle \sigma \right\rangle \cong \mathbf{Z}_m$。

### 平方是免費的

$p = 2$ 時，(b) 說 $f(x)^2 = f\!\left(x^2\right)$（係數在 $GF(2)$）。在 $GF(2^n)$ 的位元表示中，
**平方就是把位元之間插入 $0$ 再模約化** —— 這是線性運算，不需要乘法器。
二元曲線 ECC（如 Koblitz 曲線）利用 $\sigma$ 取代點倍加，大幅加速純量乘法；
AES S-box 的某些代數描述也利用 $x \mapsto x^{2^i}$ 的線性性。

### 共軛元有相同的「密碼學性質」

共軛元有相同的極小多項式、相同的乘法階（$\gcd\left(p^i, p^m - 1\right) = 1$）。
所以挑選生成元或本原多項式時，**一次排除整個分圓陪集**，搜尋量除以 $m$。
[本原多項式](Primitive_Polynomial.md) 的個數 $\varphi\left(p^m - 1\right)/m$ 正是這樣來的。

### 程式思維

```python
def cyclotomic_cosets(p, m):
    """模 p^m - 1 的分圓陪集：指數反覆乘以 p（證明 (c)）。"""
    N, seen, out = p ** m - 1, set(), []
    for j in range(N):
        if j not in seen:
            c, coset = j, []
            while c not in coset:
                coset.append(c)
                c = c * p % N
            seen.update(coset)
            out.append(coset)
    return out

assert cyclotomic_cosets(2, 3) == [[0], [1, 2, 4], [3, 6, 5]]                       # 證明 (d)：GF(8)
assert cyclotomic_cosets(2, 4) == [[0], [1, 2, 4, 8], [3, 6, 12, 9], [5, 10], [7, 14, 13, 11]]   # GF(16)
```
