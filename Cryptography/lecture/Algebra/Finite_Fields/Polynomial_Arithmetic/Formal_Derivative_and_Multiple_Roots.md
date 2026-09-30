# Formal Derivative and Multiple Roots (形式導數與重根)

+++

## 證明目標:

`FiniteFields.pdf` p.33–p.34（上半）；補充講義 Exercise 16。
有限體上沒有極限、沒有微積分，但「導數」照樣可以**純代數地**定義，而且它能偵測重根。
這是「$GF(p^n)$ 恰有 $p^n$ 個元素」的關鍵一步。

* (a) 投影片 p.33 的 Lemma（$\Rightarrow$）：$f$ 在某個擴張體 $K$ 中完全分解時，

$$f \ \text{有 } n = \deg f \ \text{個相異根} \quad \Longrightarrow \quad \gcd\left(f, f'\right) = 1$$

* (b) 同一 Lemma（$\Leftarrow$）：

$$\gcd\left(f, f'\right) = 1 \quad \Longrightarrow \quad f \ \text{有 } n \ \text{個相異根}$$

* (c) 投影片 p.34 的 Remark：

$$x^{p^n} - x \ \text{在 } GF(p) \text{ 的任何擴張體中都沒有重根}$$

* $F$ : 係數所在的體 (The field of coefficients) $[\text{體}]$
* $K$ : $F$ 的擴張體，$f$ 在其中完全分解 (An extension of $F$ over which $f$ splits) $[F \subseteq K]$
* $f$ : 多項式 (A polynomial) $[f \in F[x],\ \deg f = n \ge 1]$
* $f'$ : $f$ 的形式導數 (The formal derivative of $f$) $[f' \in F[x]]$
* $\alpha_i$ : $f$ 在 $K$ 中的相異根 (The distinct roots of $f$ in $K$) $[\alpha_i \in K]$
* $k_i$ : $\alpha_i$ 的重數 (The multiplicity of $\alpha_i$) $[k_i \in \mathbf{P}]$
* $p$ : 質數 (A prime) $[p \in \mathbf{P}]$
* 註：(a)(b) 的 $\gcd$ 是在 $F[x]$ 中計算的，而根在 $K$ 中。**$\gcd$ 不因擴大係數體而改變**
  —— 這一點投影片默認，本檔在證明中經由貝祖等式處理（係數在 $F$ 的等式 $uf + vf' = 1$ 在 $K[x]$ 中照樣成立）。
* 註：(c) 讓我們**不必事先知道 $GF(p^n)$ 存在**就能數出 $x^{p^n} - x$ 的根有 $p^n$ 個，
  見 [$GF(p^n)$ 的存在性](../Structure/Existence_of_GF_p_n.md)。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [多項式版貝祖等式 (Bézout's identity for polynomials)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Finite_Fields/Polynomial_Arithmetic/Euclidean_Domain.html#e-proof-that-the-extended-euclidean-algorithm-works-for-polynomials)：** 已於本章 [歐幾里得整環](Euclidean_Domain.md)【證明 (e)】完整證明，此處直接引用不再重證

  * (a) 貝祖等式：

    $$\exists\, u, v \in F[x] \ \text{ with } \ u\,f + v\,f' = \gcd\left(f, f'\right)$$

  * (b) $\gcd$ 整除兩者：

    $$\gcd\left(f, f'\right) \mid f, \qquad \gcd\left(f, f'\right) \mid f'$$

  * $u,\ v$ : 貝祖係數 (Bézout coefficients) $[u, v \in F[x]]$

* **【已知 2】 [多項式的唯一分解 (Unique factorization of polynomials)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Finite_Fields/Polynomial_Arithmetic/Unique_Factorization_of_Polynomials.html#c-proof-of-the-uniqueness-of-the-factorization)：** 已於本章 [多項式的唯一分解](Unique_Factorization_of_Polynomials.md)【證明 (c)】完整證明，此處直接引用不再重證。套在 $K[x]$ 上：$f$ 已分解成一次因式之積，則 $f$ 的任一首一因式也是其中某些一次因式之積

  $$d \mid a\prod_{i}\left(x - \alpha_i\right)^{k_i},\ d \ \text{首一} \quad \Longrightarrow \quad d = \prod_{i}\left(x - \alpha_i\right)^{l_i}, \quad 0 \le l_i \le k_i$$

  * $d$ : 首一因式 (A monic divisor) $[d \in K[x]]$
  * $l_i$ : 因式中的重數 (Multiplicities in the divisor) $[l_i \in \mathbf{N}]$

* **【已知 3】 [因式定理與代入同態 (The factor theorem and evaluation)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Finite_Fields/Polynomial_Arithmetic/Roots_of_Polynomials.html#a-proof-of-the-factor-theorem)：** 已於本章 [多項式的根](Roots_of_Polynomials.md)【已知 2】【證明 (a)】給出並證明，此處直接引用不再重證

  * (a) 代入保運算：

    $$\left(g + h\right)(\beta) = g(\beta) + h(\beta), \qquad \left(gh\right)(\beta) = g(\beta)\,h(\beta)$$

  * (b) 因式定理：

    $$\left(x - \beta\right) \mid g \quad \Longleftrightarrow \quad g(\beta) = 0$$

  * $g,\ h$ : 多項式 (Polynomials) $[g, h \in K[x]]$
  * $\beta$ : 代入的值 (The value substituted) $[\beta \in K]$

* **【已知 4】 [體無零因子 (A field has no zero divisors)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Field/Field_Definition.html#d-proof-that-every-field-is-an-integral-domain)：** 已於 [體的定義](../../Abstract_Algebra/Field/Field_Definition.md)【證明 (d)】完整證明，此處直接引用不再重證

  $$a_1, a_2, \dots, a_m \neq 0 \quad \Longrightarrow \quad a_1 a_2 \cdots a_m \neq 0$$

  * $a_i$ : 非零體元素 (Non-zero field elements) $[a_i \in K]$

* **【已知 5】 [特徵 p 讓 p 倍歸零 (Characteristic p annihilates p-fold sums)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Field/Freshmans_Dream.html#assumptions-preliminaries)：** 已於 [新生之夢](../../Abstract_Algebra/Field/Freshmans_Dream.md)【推導 1】完整證明，此處直接引用不再重證

  $$\mathrm{ch}(F) = p, \quad p \mid m \quad \Longrightarrow \quad m \cdot x = 0 \quad \forall x \in F$$

  * $m$ : 整數倍數 (An integer multiple) $[m \in \mathbf{Z}]$
  * $x$ : 體元素 (A field element) $[x \in F]$

* **【已知 6】 [數學歸納法 (Mathematical induction)](https://mathworld.wolfram.com/PrincipleofMathematicalInduction.html)：** 標準結果，直接引用不再重證

  $$P(1) \ \text{且} \ \left[P(k-1) \Rightarrow P(k)\right] \quad \Longrightarrow \quad P(k) \ \forall k \in \mathbf{P}$$

  * $P$ : 待證命題 (The statement to be proved) $[\mathbf{P} \to \left\{\text{真},\text{假}\right\}]$

* **【定義 1】 形式導數 (Formal derivative)：** 補充講義 Exercise 16 —— 照抄微積分的公式，但係數 $j$ 理解為 $j \cdot 1_F$

  $$f(x) = \sum_{j=0}^{n} f_j x^j \quad \Longrightarrow \quad f'(x) \overset{\text{def}}{=} \sum_{j=1}^{n}\left(j \cdot 1_F\right) f_j\, x^{j-1}$$

  * $f_j$ : 係數 (Coefficients) $[f_j \in F]$
  * $j \cdot 1_F$ : $1_F$ 的 $j$ 倍 (The $j$-fold sum of $1_F$) $[j \cdot 1_F \in F]$
  * 註：由定義直接可見 $D : f \mapsto f'$ 是 **$F$-線性**的：$\left(cf + g\right)' = cf' + g'$。
  * 註：特徵 $p$ 時 $\left(x^p\right)' = \left(p \cdot 1_F\right)x^{p-1} = 0$ —— **非常數多項式的導數可以是 $0$**，這與微積分大不相同。

* **【假設 1】 $f$ 在 $K$ 中完全分解 (f splits completely over K)：** 投影片 p.33 的「Write $f(x) = \prod\left(x - \alpha_i\right)^{k_i}$」

  $$f = a\prod_{i=1}^{s}\left(x - \alpha_i\right)^{k_i} \ \text{ in } K[x], \qquad \alpha_i \ \text{兩兩相異}, \qquad \sum_{i} k_i = n$$

  * $a$ : 首項係數 (The leading coefficient) $[a \in F \setminus \left\{0\right\}]$
  * $s$ : 相異根的個數 (The number of distinct roots) $[s \in \mathbf{P}]$
  * 註：「$n$ 個相異根」$\Longleftrightarrow$ $s = n$ $\Longleftrightarrow$ 所有 $k_i = 1$。

* **【推導 1】 乘積法則 (The product rule)：** 補充講義 Exercise 16(a)。先對單項式驗證，再由線性推廣

  * (a) 單項式：

    $$\begin{gather*}
    \left(x^i x^j\right)' &\overset{\text{定義 1}}{=}& \left(\left(i + j\right) \cdot 1_F\right)x^{i+j-1} \\
    \left(x^i x^j\right)' &=& \left(i \cdot 1_F\right)x^{i-1} \cdot x^j + x^i \cdot \left(j \cdot 1_F\right)x^{j-1} \\
    \left(x^i x^j\right)' &\overset{\text{定義 1}}{=}& \left(x^i\right)' x^j + x^i \left(x^j\right)'
    \end{gather*}$$

  * (b) 一般多項式 $g = \sum g_i x^i$、$h = \sum h_j x^j$：

    $$\begin{gather*}
    \left(gh\right)' &\overset{\text{定義 1}}{=}& \sum_{i,j} g_i h_j \left(x^i x^j\right)' \\
    \left(gh\right)' &\overset{\text{推導 1(a)}}{=}& \sum_{i,j} g_i h_j \left[\left(x^i\right)' x^j + x^i \left(x^j\right)'\right] \\
    \left(gh\right)' &=& g'\,h + g\,h'
    \end{gather*}$$

  * $g,\ h$ : 多項式 (Polynomials) $[g, h \in K[x]]$
  * $i,\ j$ : 次數指標 (Degree indices) $[i, j \in \mathbf{N}]$

* **【推導 2】 冪次法則 (The power rule)：** 對 $k$ 歸納

  $$\begin{gather*}
  \left(\left(x - \alpha\right)^1\right)' &\overset{\text{定義 1}}{=}& 1 \\
  \left(\left(x - \alpha\right)^k\right)' &\overset{\text{推導 1(b)}}{=}& \left(\left(x - \alpha\right)^{k-1}\right)'\left(x - \alpha\right) + \left(x - \alpha\right)^{k-1} \cdot 1 \\
  \left(\left(x - \alpha\right)^k\right)' &\overset{\text{已知 6}}{=}& \left(k - 1\right)\left(x - \alpha\right)^{k-2}\left(x - \alpha\right) + \left(x - \alpha\right)^{k-1} \\
  \left(\left(x - \alpha\right)^k\right)' &=& k\left(x - \alpha\right)^{k-1}
  \end{gather*}$$

  * $\alpha$ : 體元素 (A field element) $[\alpha \in K]$
  * $k$ : 冪次 (The exponent) $[k \in \mathbf{P}]$
  * 註：第三行用的是歸納假設 $\left(\left(x - \alpha\right)^{k-1}\right)' = \left(k-1\right)\left(x - \alpha\right)^{k-2}$。

* **【推導 3】 投影片 p.33 的導數公式 (The derivative of the split form)：** 對【假設 1】反覆用乘積法則

  $$f' \overset{\text{推導 1(b),推導 2}}{=} a\sum_{i=1}^{s} k_i\left(x - \alpha_i\right)^{k_i - 1}\prod_{j \neq i}\left(x - \alpha_j\right)^{k_j}$$

  * $f'$ : $f$ 的形式導數 (The formal derivative of $f$) $[f' \in K[x]]$

+++

## 證明:

### (a) proof that distinct roots imply coprimality with the derivative

設所有 $k_i = 1$（$s = n$）。**第一步**：$f'$ 在每個根上都不為零 ——
【推導 3】的和式中只有 $i$ 那一項不含 $\left(x - \alpha_i\right)$：

$$\begin{gather*}
f'\!\left(\alpha_i\right) &\overset{\text{推導 3,已知 3(a)}}{=}& a\prod_{j \neq i}\left(\alpha_i - \alpha_j\right) \\
f'\!\left(\alpha_i\right) &\overset{\text{已知 4}}{\neq}& 0 \qquad \text{(} a \neq 0\text{，} \alpha_i \neq \alpha_j\text{)}
\end{gather*}$$

**第二步**：設 $d = \gcd\left(f, f'\right)$，若 $\deg d \ge 1$，則 $d$ 必含某個 $x - \alpha_i$，於是 $\alpha_i$ 也是 $f'$ 的根：

$$\begin{gather*}
d &\overset{\text{已知 1(b)}}{\mid}& f \\
d &\overset{\text{已知 2,假設 1}}{=}& \prod_{i \in T}\left(x - \alpha_i\right) \qquad \text{(} T \neq \varnothing \text{ 若 } \deg d \ge 1\text{)} \\
d &\overset{\text{已知 1(b)}}{\mid}& f' \\
f'\!\left(\alpha_i\right) &\overset{\text{已知 3(b)}}{=}& 0 \qquad \text{for } i \in T
\end{gather*}$$

與第一步矛盾，故 $\deg d = 0$，即 $\gcd\left(f, f'\right) = 1$。與投影片「$f'(\alpha_i) \neq 0$ for all $i$, so $f(x)$ and $f'(x)$ have no common factor」一致。

### (b) proof that coprimality with the derivative implies distinct roots

證逆否：設某個 $k_i \ge 2$。則 $\left(x - \alpha_i\right)$ 同時整除 $f$ 與 $f'$ ——
【推導 3】的第 $i$ 項含 $\left(x - \alpha_i\right)^{k_i - 1}$（指數 $\ge 1$），其餘項含 $\left(x - \alpha_i\right)^{k_i}$：

$$\begin{gather*}
f\!\left(\alpha_i\right) &\overset{\text{假設 1,已知 3(a)}}{=}& 0 \\
f'\!\left(\alpha_i\right) &\overset{\text{推導 3,已知 3(a)}}{=}& 0 \qquad \text{(每一項都含因式 } x - \alpha_i\text{)}
\end{gather*}$$

若 $\gcd\left(f, f'\right) = 1$，貝祖等式的係數在 $F$、等式在 $K[x]$ 中照樣成立，代入 $\alpha_i$：

$$\begin{gather*}
u\,f + v\,f' &\overset{\text{已知 1(a)}}{=}& 1 \\
u\!\left(\alpha_i\right) f\!\left(\alpha_i\right) + v\!\left(\alpha_i\right) f'\!\left(\alpha_i\right) &\overset{\text{已知 3(a)}}{=}& 1 \\
0 &=& 1
\end{gather*}$$

矛盾。故 $\gcd\left(f, f'\right) \neq 1$。與投影片「$k_i > 1$ for some $i$, then $x - \alpha_i$ is a common factor」一致。

* 註：這裡的論證**不需要**知道 $k_i \cdot 1_F$ 是否為零。
  在特徵 $p$ 中 $k_i = p$ 時第 $i$ 項整個消失，但 $x - \alpha_i$ 仍整除其他每一項，結論不變。

### (c) proof that the polynomial x to the p to the n minus x has no multiple roots

取 $F = GF(p)$、$f = x^{p^n} - x$。$p \mid p^n$，故由【已知 5】首項的導數係數歸零：

$$\begin{gather*}
f' &\overset{\text{定義 1}}{=}& \left(p^n \cdot 1_F\right)x^{p^n - 1} - 1 \\
f' &\overset{\text{已知 5}}{=}& 0 \cdot x^{p^n - 1} - 1 \\
f' &=& -1 \\
\gcd\left(f, -1\right) &=& 1
\end{gather*}$$

由【證明 (b)】，在任何讓 $f$ 完全分解的擴張體中，$f$ 都有 $p^n$ 個**相異**的根。
與投影片 p.34「$f'(x) = p^nx^{p^n-1} - 1 \equiv -1 \pmod p$ relatively prime to $f(x)$」一致。

* 註：這是 [$GF(p^n)$ 的存在性](../Structure/Existence_of_GF_p_n.md) 能數出「恰好 $p^n$ 個元素」的原因。

+++

## 意義與密碼學關聯 (Interpretation and Relevance to Cryptography)

### 不用極限的微積分

形式導數完全是**符號操作**：把 $x^j$ 換成 $j\,x^{j-1}$。它繼承了微積分的乘積法則（【推導 1】），
卻沒有微積分的直覺 —— 例如 $GF(2)$ 上 $\left(x^2\right)' = 2x = 0$。
它唯一的用途（在本章裡）就是**偵測重根**：$f$ 與 $f'$ 共享的根，恰好是重根。

### 分解演算法的第一步：無平方分解

Berlekamp、Cantor–Zassenhaus 等有限體多項式分解演算法都要求輸入**無重因式**。
第一步因此是計算 $\gcd\left(f, f'\right)$ 並除掉它（square-free factorization），
理論依據就是本檔的 (a)(b)。這些演算法用於：

* 產生 $GF(2^n)$ 的不可約多項式（例如為新的 AES 變體或 GCM 的 GHASH 選模數）；
* 橢圓曲線點計數（Schoof 演算法需要分解除法多項式）；
* 解碼 Reed–Solomon 碼（找錯誤定位多項式的根）。

### 程式思維

```python
def formal_derivative(f, p):
    """定義 1：係數由低到高，j*f_j 取模 p。"""
    return [(j * c) % p for j, c in enumerate(f)][1:]

# x^8 - x over GF(2) = x^8 + x：導數 = 8x^7 + 1 = 1（證明 (c)）
f = [0, 1, 0, 0, 0, 0, 0, 0, 1]
assert formal_derivative(f, 2) == [1, 0, 0, 0, 0, 0, 0, 0]
```
