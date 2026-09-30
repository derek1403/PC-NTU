# Polynomial Ring over a Field (體上的多項式環)

+++

## 證明目標:

`FiniteFields.pdf` p.5–p.6；補充講義 §7.5。有限體 $GF(p^n)$ 的元素全部是「$GF(p)$ 係數的多項式」，
所以第一步是把 $F[x]$ 的次數、首項與乘法規則講清楚。

* (a) 投影片 p.5 的乘法例子（在 $GF(7)[x]$ 中）：

$$\left(2x^3 + 3x^2 + 5x + 1\right)\left(5x^2 + 3x + 2\right) = 3x^5 + 3x^3 + 5x^2 + 6x + 2$$

* (b) 投影片 p.6 的 Proposition：對任意非零 $p(x), q(x) \in F[x]$，

$$\text{(1)} \ \ p(x)\,q(x) \neq 0, \qquad \text{(2)} \ \ \deg\left(p(x)\,q(x)\right) = \deg p(x) + \deg q(x)$$

  並且在約定 $\deg 0 = -\infty$ 之下，(2) 對**零多項式也成立**。

* (c) 投影片 p.6 的 Note：把 $F$ 換成一般的環 $R$，(1)(2) 都可能失敗 —— 以 $\mathbf{Z}_4[x]$ 為反例：

$$\left(2x\right)\left(2x\right) = 0, \qquad \left(2x + 1\right)\left(2x + 1\right) = 1$$

* $F$ : 係數所在的體 (The field of coefficients) $[\text{體}]$
* $F[x]$ : $F$ 上的多項式環 (The polynomial ring over $F$) $[\text{集合}]$
* $p(x),\ q(x)$ : 多項式 (Polynomials) $[p, q \in F[x]]$
* $\deg$ : 次數 (Degree) $[F[x] \to \mathbf{N} \cup \left\{-\infty\right\}]$
* $\mathrm{LT}$ : 首項 (Leading term) $[F[x] \setminus \left\{0\right\} \to F[x]]$
* 註：(b) 對「係數在整環上」已於 [整環](../../Abstract_Algebra/Ring/Integral_Domain.md)【推導 2】證過，
  本檔只把它套到體上並補上零多項式的約定，不重證。
* 註：投影片 p.5 的標題寫 $GF_p[x]$，但定義與命題對**任意體** $F$ 都成立，本檔一律寫 $F[x]$。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [多項式環的定義與摺積乘法 (The polynomial ring and its convolution product)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Ring/Ring_Examples.html#e-verify-that-the-polynomials-form-a-ring)：** 已於 [環的例子](../../Abstract_Algebra/Ring/Ring_Examples.md)【定義 2】【證明 (e)】給出並證明，此處直接引用不再重證

  $$\left(\sum_{i} a_i x^i\right)\left(\sum_{j} b_j x^j\right) = \sum_{k}\left(\sum_{i+j=k} a_i b_j\right)x^k$$

  * $a_i,\ b_j$ : 係數 (Coefficients) $[a_i, b_j \in R]$
  * $k$ : 乘積的次數指標 (The degree index of the product) $[k \in \mathbf{N}]$
  * $R$ : 係數環 (The coefficient ring) $[\text{環}]$

* **【已知 2】 [整環上的多項式環仍是整環 (The polynomial ring over an integral domain is an integral domain)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Ring/Integral_Domain.html#assumptions-preliminaries)：** 已於 [整環](../../Abstract_Algebra/Ring/Integral_Domain.md)【推導 2】完整證明，此處直接引用不再重證

  * (a) 乘積的最高次係數是兩個首項係數的乘積：

    $$\left[fg\right]_{m+n} = a_m b_n$$

  * (b) $R$ 為整環時首項係數乘積非零，故次數相加：

    $$R \ \text{整環},\ f, g \neq 0 \quad \Longrightarrow \quad fg \neq 0, \quad \deg\left(fg\right) = \deg f + \deg g$$

  * $f,\ g$ : 非零多項式 (Non-zero polynomials) $[f, g \in R[x]]$
  * $a_m,\ b_n$ : 首項係數 (Leading coefficients) $[a_m, b_n \in R]$
  * $m,\ n$ : 次數 (Degrees) $[m, n \in \mathbf{N}]$

* **【已知 3】 [體必為整環 (Every field is an integral domain)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Field/Field_Definition.html#d-proof-that-every-field-is-an-integral-domain)：** 已於 [體的定義](../../Abstract_Algebra/Field/Field_Definition.md)【證明 (d)】完整證明，此處直接引用不再重證

  $$F \ \text{為體} \quad \Longrightarrow \quad F \ \text{無零因子}$$

  * $F$ : 體 (A field) $[\text{體}]$

* **【已知 4】 [模 $n$ 剩餘類的運算 (Arithmetic of residues modulo n)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Field/Field_Definition.html#b-proof-that-the-residues-modulo-a-prime-form-a-field)：** 已於 [體的定義](../../Abstract_Algebra/Field/Field_Definition.md) 給出，此處直接引用

  $$a \oplus b = \left(a + b\right) \bmod n, \qquad a \otimes b = \left(ab\right) \bmod n$$

  * $a,\ b$ : 剩餘類代表元 (Residue representatives) $[a, b \in \mathbf{Z}_n]$
  * $n$ : 模數 (Modulus) $[n \in \mathbf{P}]$

* **【定義 1】 次數 (Degree)：** 投影片 p.5 的兩條定義

  $$\deg\left(a_n x^n + \cdots + a_1 x + a_0\right) \overset{\text{def}}{=} \max\left\{m \ \middle|\ a_m \neq 0\right\}, \qquad \deg 0 \overset{\text{def}}{=} -\infty$$

  * $a_i$ : 係數 (Coefficients) $[a_i \in F]$
  * $m$ : 候選次數 (A candidate degree) $[m \in \mathbf{N}]$
  * 註：$-\infty$ 的算術約定：$-\infty + k = k + \left(-\infty\right) = -\infty$，且 $-\infty < k$ 對所有 $k \in \mathbf{N}$。
  * 註：非零常數的次數是 $0$，**零多項式的次數不是 $0$**。這個區分讓「非零常數 $=$ 可逆元素」與「$0$ 不可逆」在次數上看得出來。

* **【定義 2】 首項 (Leading term)：** 投影片 p.6

  $$\mathrm{LT}\!\left(p(x)\right) \overset{\text{def}}{=} a_m x^m, \qquad m = \deg p$$

  * $\mathrm{LT}$ : 首項 (Leading term) $[F[x] \setminus \left\{0\right\} \to F[x]]$
  * $a_m$ : 首項係數 (The leading coefficient) $[a_m \in F \setminus \left\{0\right\}]$
  * 註：首項係數為 $1$ 的多項式稱為**首一 (monic)**。

* **【推導 1】 首項相乘 (The leading term is multiplicative)：** 投影片 p.6 的 Proof 一行，由【已知 2(a)】與【已知 3】組合而成

  $$\begin{gather*}
  \mathrm{LT}\!\left(pq\right) &\overset{\text{已知 2(a)}}{=}& a_m b_n\, x^{m+n} \\
  \mathrm{LT}\!\left(pq\right) &\overset{\text{定義 2}}{=}& \mathrm{LT}(p)\,\mathrm{LT}(q) \\
  a_m b_n &\overset{\text{已知 3}}{\neq}& 0
  \end{gather*}$$

  * $p,\ q$ : 非零多項式 (Non-zero polynomials) $[p, q \in F[x]]$
  * $a_m,\ b_n$ : $p, q$ 的首項係數 (The leading coefficients of $p, q$) $[a_m, b_n \in F \setminus \left\{0\right\}]$

+++

## 證明:

### (a) verify the product example over the field with seven elements

依【已知 1】逐次數收集係數，再依【已知 4】（$n = 7$）化簡：

$$\begin{gather*}
\left[\,\cdot\,\right]_5 &\overset{\text{已知 1}}{=}& 2 \cdot 5 = 10 \equiv 3 \\
\left[\,\cdot\,\right]_4 &\overset{\text{已知 1}}{=}& 2 \cdot 3 + 3 \cdot 5 = 21 \equiv 0 \\
\left[\,\cdot\,\right]_3 &\overset{\text{已知 1}}{=}& 2 \cdot 2 + 3 \cdot 3 + 5 \cdot 5 = 38 \equiv 3 \\
\left[\,\cdot\,\right]_2 &\overset{\text{已知 1}}{=}& 3 \cdot 2 + 5 \cdot 3 + 1 \cdot 5 = 26 \equiv 5 \\
\left[\,\cdot\,\right]_1 &\overset{\text{已知 1}}{=}& 5 \cdot 2 + 1 \cdot 3 = 13 \equiv 6 \\
\left[\,\cdot\,\right]_0 &\overset{\text{已知 4}}{=}& 1 \cdot 2 = 2
\end{gather*}$$

故乘積為 $3x^5 + 0x^4 + 3x^3 + 5x^2 + 6x + 2$，與投影片一致。首項與次數的交叉檢查：

$$\begin{gather*}
\mathrm{LT}\!\left(\left(2x^3 + \cdots\right)\left(5x^2 + \cdots\right)\right) &\overset{\text{推導 1}}{=}& \left(2x^3\right)\left(5x^2\right) \\
&\overset{\text{已知 4}}{=}& 3x^5
\end{gather*}$$

* 註：$x^4$ 的係數**恰好消失**（$21 \equiv 0$）。係數消失只會發生在**中間**的次數；
  最高次項永遠不會消失 —— 這正是 (b) 的內容。

### (b) proof that degrees add in the polynomial ring over a field

**非零情形**：$F$ 是體，由【已知 3】無零因子，即為整環；套【已知 2(b)】：

$$\begin{gather*}
F &\overset{\text{已知 3}}{=}& \text{整環} \\
p(x)\,q(x) &\overset{\text{已知 2(b)}}{\neq}& 0 \\
\deg\left(pq\right) &\overset{\text{已知 2(b)}}{=}& \deg p + \deg q
\end{gather*}$$

這就是投影片的 (1)(2)。**零多項式情形**：設 $p = 0$，則 $pq = 0$：

$$\begin{gather*}
\deg\left(0 \cdot q\right) &=& \deg 0 \\
&\overset{\text{定義 1}}{=}& -\infty \\
&\overset{\text{定義 1}}{=}& -\infty + \deg q \\
&=& \deg 0 + \deg q
\end{gather*}$$

故約定 $\deg 0 = -\infty$ 之下，(2) 對所有 $p, q$ 成立。

* 註：若改約定 $\deg 0 = 0$，則 $\deg\left(0 \cdot x\right) = 0 \neq 0 + 1$，公式就壞了。
  **$-\infty$ 是唯一讓次數加法公式無例外的約定**（補充講義 §7.5 也這樣說明）。

### (c) disprove the proposition over a ring with zero divisors

取 $R = \mathbf{Z}_4$（有零因子 $2 \otimes 2 = 0$）。依【已知 1】、【已知 4】（$n = 4$）：

$$\begin{gather*}
\left(2x\right)\left(2x\right) &\overset{\text{已知 1}}{=}& \left(2 \otimes 2\right)x^2 \\
\left(2x\right)\left(2x\right) &\overset{\text{已知 4}}{=}& 0 \\
\left(2x + 1\right)\left(2x + 1\right) &\overset{\text{已知 1}}{=}& \left(2 \otimes 2\right)x^2 + \left(2 \oplus 2\right)x + 1 \\
\left(2x + 1\right)\left(2x + 1\right) &\overset{\text{已知 4}}{=}& 0 \cdot x^2 + 0 \cdot x + 1 \\
\left(2x + 1\right)\left(2x + 1\right) &=& 1
\end{gather*}$$

第一條：兩個非零多項式相乘得 $0$，(1) 失敗。
第二條：$\deg = 0 \neq 1 + 1$，(2) 失敗。

* 註：第二條還說明 **$2x + 1$ 在 $\mathbf{Z}_4[x]$ 中可逆**（它是自己的反元素）——
  一次多項式居然是單位元素！這在 $F[x]$ 中不可能發生，因為次數相加迫使可逆元素只能是非零常數。
* 註：失敗的唯一原因是【推導 1】裡的 $a_m b_n \neq 0$ 不再成立（$2 \cdot 2 = 0$）。

+++

## 意義與密碼學關聯 (Interpretation and Relevance to Cryptography)

### 次數相加是「模多項式」運算的前提

有限體 $GF(p^n)$ 的元素是次數 $< n$ 的多項式。兩個元素相乘後次數最高到 $2n - 2$，
再除以一個 $n$ 次的模多項式把次數拉回 $< n$。**能「拉回」的前提是除法有唯一的餘式**，
而那正依賴本檔的次數規則 —— 見 [多項式的除法原理](Division_Algorithm_for_Polynomials.md)。

### 為什麼後量子密碼要小心 $\mathbf{Z}_q[x]$

Kyber、Dilithium 等格密碼在 $\mathbf{Z}_q[x]/\left\langle x^{256}+1 \right\rangle$ 上運算，
其中 $q = 3329$ 或 $8380417$ 是**質數** —— 所以係數環是體，(b) 成立。
若誤用合數模數（例如 $q = 2^{16}$），就會像 (c) 一樣出現降次與零因子，
破壞安全性分析裡「乘積的範數不會莫名消失」的假設。
NTRU 恰好是用 $\mathbf{Z}_{2048}[x]$ 的例子，它的設計因此必須另外處理可逆性。

### 程式思維

```python
def poly_mul(a, b, p):
    """F_p[x] 的乘法：係數由低到高存放，摺積後取模 p（已知 1）。"""
    r = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            r[i + j] = (r[i + j] + x * y) % p
    return r

assert poly_mul([1, 5, 3, 2], [2, 3, 5], 7) == [2, 6, 5, 3, 0, 3]   # 證明 (a)
assert poly_mul([0, 2], [0, 2], 4) == [0, 0, 0]                     # 證明 (c)：非零乘非零得零
```
