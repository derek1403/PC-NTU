# Ring Examples (環的例子)

+++

## 證明目標:

`Algebra.pdf` p.27。把五組例子逐一對照 [環的定義](Ring_Definition.md) 的四條公理驗證。

* (a) $\mathbf{Z}, \mathbf{Q}, \mathbf{R}, \mathbf{C}$ 配一般加法與乘法。
* (b) $n\mathbf{Z} = \left\{nt \ \middle|\ t \in \mathbf{Z}\right\}$ 配一般加法與乘法。
* (c) $\mathbf{Z}_n$ 配模 $n$ 加法與模 $n$ 乘法。
* (d) $C(\mathbf{R})$：$\mathbf{R}$ 上的連續函數，配逐點加法與逐點乘法。
* (e) $R[x]$：係數取自環 $R$ 的多項式，配一般多項式加法與乘法。
* (f) $R[x, y] = R[x][y]$：兩個未定元的多項式環。

* $R$ : 係數所在的環 (The coefficient ring) $[\text{環}]$
* $n$ : 模數或倍數 (The modulus or the multiplier) $[n \in \mathbf{P}]$
* $\mathbf{Z}_n$ : 模 $n$ 剩餘類集合 (The set of residues modulo $n$) $[\text{集合}]$
* $C(\mathbf{R})$ : $\mathbf{R}$ 上的連續函數全體 (All continuous functions on $\mathbf{R}$) $[\text{集合}]$
* $R[x]$ : 係數取自 $R$ 的多項式環 (The polynomial ring over $R$) $[\text{集合}]$
* $x,\ y$ : 未定元 (Indeterminates) $[x, y \notin R]$
* 註：(a) 的加法部分已於 [群的正例與反例](../Group/Group_Examples_and_Counterexamples.md)【證明 (a)】
  完整驗證，本檔直接引用不再重證，只補乘法與分配律那三條。
* 註：**投影片 p.27 的 $R[x]$ 定義寫得略窄** —— 它寫成
  $\left\{a_0 + a_1x + \dots + a_nx^n \ \middle|\ a_i \in R,\ a_n \neq 0,\ n \in \mathbf{Z}^+\right\}$，
  這樣會把**零多項式**與**非零常數**排除在外（$n$ 必須是正整數、首項係數必須非零），
  但零多項式是加法單位元素，不能不在環裡。本檔【定義 2】採標準寫法並在該處說明。
* 註：(b) 的 $n\mathbf{Z}$ 在 $n \ge 2$ 時**沒有乘法單位元素**，見
  [含單位元環與交換環](Ring_with_Identity_and_Commutative_Ring.md)。它仍然是環 ——
  環不要求有 $1$。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [環的公理 (Ring axioms)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Ring/Ring_Definition.html#definitions-and-notation)：** 已於本章 [環的定義](Ring_Definition.md)【定義 1】給出，此處直接引用

  * (a) $\left(R, +\right)$ 是阿貝爾群：

    $$a + b \in R, \quad a + \left(b + c\right) = \left(a + b\right) + c, \quad a + 0 = a, \quad a + \left(-a\right) = 0, \quad a + b = b + a$$

  * (b) 乘法封閉：

    $$a \times b \in R$$

  * (c) 乘法結合：

    $$a \times \left(b \times c\right) = \left(a \times b\right) \times c$$

  * (d) 分配律：

    $$a \times \left(b + c\right) = a \times b + a \times c, \qquad \left(a + b\right) \times c = a \times c + b \times c$$

  * $R$ : 環的底層集合 (The underlying set of the ring) $[\text{集合}]$
  * $a,\ b,\ c$ : 環元素 (Ring elements) $[a, b, c \in R]$
  * $0$ : 加法單位元素 (The additive identity) $[0 \in R]$
  * $-a$ : $a$ 的加法反元素 (The additive inverse of $a$) $[-a \in R]$

* **【已知 2】 [數系配加法構成阿貝爾群 (The number systems form abelian groups under addition)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Group/Group_Examples_and_Counterexamples.html#a-proof-the-integers-under-addition-form-a-group)：** 已於本章 [群的正例與反例](../Group/Group_Examples_and_Counterexamples.md)【證明 (a)(c)(e)】與 [阿貝爾群與非阿貝爾群](../Group/Abelian_and_Non_Abelian_Group.md)【證明 (b)】完整證明，此處直接引用不再重證

  $$\left(\mathbf{Z}, +\right), \quad \left(\mathbf{Q}, +\right), \quad \left(\mathbf{R}, +\right), \quad \left(\mathbf{C}, +\right), \quad \left(n\mathbf{Z}, +\right), \quad \left(\mathbf{Z}_n, \oplus\right) \qquad \text{皆為阿貝爾群}$$

  * $\mathbf{Z},\ \mathbf{Q},\ \mathbf{R},\ \mathbf{C}$ : 四個數系 (The four number systems) $[\text{集合}]$
  * $n\mathbf{Z}$ : $n$ 的倍數集合 (The set of multiples of $n$) $[\text{集合}]$
  * $\mathbf{Z}_n$ : 模 $n$ 剩餘類集合 (The set of residues modulo $n$) $[\text{集合}]$
  * $\oplus$ : 模 $n$ 加法 (Addition modulo $n$) $[\mathbf{Z}_n \times \mathbf{Z}_n \to \mathbf{Z}_n]$
  * 註：[群的正例與反例](../Group/Group_Examples_and_Counterexamples.md)【證明 (c)】證的是 $5\mathbf{Z}$、
    【證明 (e)】證的是 $\mathbf{Z}_6$，兩處的註都說明論證對任意 $n$ 逐字相同。

* **【已知 3】 [整數算術與模運算的基本性質 (Basic arithmetic and modular arithmetic)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Group/Group_Examples_and_Counterexamples.html#assumptions-preliminaries)：** 已於本章 [群的正例與反例](../Group/Group_Examples_and_Counterexamples.md)【已知 3】【已知 4】引用，此處再次引用

  * (a) 乘法結合與交換：

    $$a \times \left(b \times c\right) = \left(a \times b\right) \times c, \qquad a \times b = b \times a$$

  * (b) 分配律：

    $$a \times \left(b + c\right) = a \times b + a \times c$$

  * (c) 模運算與整數運算相容：

    $$\left(a \times b\right) \bmod n = \left(\left(a \bmod n\right) \times \left(b \bmod n\right)\right) \bmod n$$

  * $a,\ b,\ c$ : 任意整數（或有理數、實數、複數）(Arbitrary integers, or rationals, reals, complex numbers) $[a, b, c \in \mathbf{Z}]$
  * $n$ : 模數 (Modulus) $[n \in \mathbf{P}]$

* **【已知 4】 [連續函數的四則封閉性 (Closure of continuous functions under arithmetic)](https://mathworld.wolfram.com/ContinuousFunction.html)：** 微積分的標準結果，本章直接引用不再重證

  $$f, g \ \text{連續} \quad \Longrightarrow \quad f + g \ \text{連續}, \quad fg \ \text{連續}, \quad -f \ \text{連續}$$

  * $f,\ g$ : $\mathbf{R}$ 上的連續函數 (Continuous functions on $\mathbf{R}$) $[f, g \in C(\mathbf{R})]$

* **【定義 1】 $n$ 的倍數集合 (The set of multiples of $n$)：**

  $$n\mathbf{Z} \overset{\text{def}}{=} \left\{nt \ \middle|\ t \in \mathbf{Z}\right\}$$

  * $n\mathbf{Z}$ : $n$ 的倍數集合 (The set of multiples of $n$) $[\text{集合}]$
  * $n$ : 倍數 (The multiplier) $[n \in \mathbf{Z}]$
  * $t$ : 整數係數 (Integer coefficient) $[t \in \mathbf{Z}]$

* **【定義 2】 多項式環 (Polynomial ring)：** 係數取自環 $R$、未定元為 $x$ 的多項式全體

  * (a) 集合：

    $$R[x] \overset{\text{def}}{=} \left\{\sum_{i=0}^{m} a_i x^i \ \middle|\ m \in \mathbf{N},\ a_i \in R\right\}$$

  * (b) 加法（逐項相加）：

    $$\sum_i a_i x^i + \sum_i b_i x^i \overset{\text{def}}{=} \sum_i \left(a_i + b_i\right)x^i$$

  * (c) 乘法（摺積）：

    $$\left(\sum_i a_i x^i\right)\left(\sum_j b_j x^j\right) \overset{\text{def}}{=} \sum_k \left(\sum_{i+j=k} a_i b_j\right)x^k$$

  * $R[x]$ : 多項式環 (The polynomial ring) $[\text{集合}]$
  * $R$ : 係數所在的環 (The coefficient ring) $[\text{環}]$
  * $a_i,\ b_j$ : 多項式係數 (Polynomial coefficients) $[a_i, b_j \in R]$
  * $x$ : 未定元 (The indeterminate) $[x \notin R]$
  * $m$ : 多項式的項數上界 (An upper bound on the number of terms) $[m \in \mathbf{N}]$
  * $i,\ j,\ k$ : 次數指標 (Degree indices) $[i, j, k \in \mathbf{N}]$
  * 註：**本定義與投影片 p.27 的寫法有別**。投影片要求 $a_n \neq 0$ 且 $n \in \mathbf{Z}^+$，
    那會把零多項式與非零常數排除在外；但零多項式是加法單位元素、常數 $1$ 是乘法單位元素，
    兩者都必須在環裡。投影片的寫法其實是在描述「次數恰為 $n$ 的多項式長什麼樣」，
    而不是在界定整個集合。本檔採標準寫法。
  * 註：兩個多項式相等的定義是**逐項係數相等**，未定元 $x$ 只是形式符號，不是變數。
    這一點在 [不可約多項式](../Field/Irreducible_Polynomial.md) 會很重要 ——
    $x^2 + x \in \mathbf{Z}_2[x]$ 在每個 $\mathbf{Z}_2$ 的值上都取 $0$，但它**不是**零多項式。

* **【定義 3】 多變元多項式環 (Polynomial ring in several indeterminates)：** 遞迴地套用【定義 2】

  $$R[x, y] \overset{\text{def}}{=} \left(R[x]\right)[y]$$

  * $R[x, y]$ : 兩個未定元的多項式環 (The polynomial ring in two indeterminates) $[\text{集合}]$
  * $R[x]$ : 一個未定元的多項式環 (The polynomial ring in one indeterminate) $[\text{集合}]$
  * $R$ : 係數所在的環 (The coefficient ring) $[\text{環}]$
  * $x,\ y$ : 兩個未定元 (Two indeterminates) $[x, y \notin R]$
  * 註：「把 $R[x]$ 當成新的係數環，再對 $y$ 做一次【定義 2】」。
    這個遞迴可以推廣到任意多個未定元，即投影片的
    「Can be generalized to any number of indeterminates」。

+++

## 證明:

### (a) verify that the four number systems are rings

以 $\mathbf{Z}$ 為代表（$\mathbf{Q}, \mathbf{R}, \mathbf{C}$ 逐字相同）。加法部分直接引用，
乘法與分配律三條逐一檢查：

$$\begin{gather*}
\left(\mathbf{Z}, +\right) &\overset{\text{已知 2}}{=}& \text{阿貝爾群} \qquad \text{(公理 (a))} \\
a \times b &\in& \mathbf{Z} \qquad \text{(公理 (b)，整數相乘仍為整數)} \\
a \times \left(b \times c\right) &\overset{\text{已知 3(a)}}{=}& \left(a \times b\right) \times c \qquad \text{(公理 (c))} \\
a \times \left(b + c\right) &\overset{\text{已知 3(b)}}{=}& a \times b + a \times c \qquad \text{(公理 (d) 左)} \\
\left(a + b\right) \times c &\overset{\text{已知 3(a)(b)}}{=}& a \times c + b \times c \qquad \text{(公理 (d) 右)}
\end{gather*}$$

四條全中，故 $\left(\mathbf{Z}, +, \times\right)$ 是環。

* 註：右分配律由左分配律加上乘法交換律（【已知 3(a)】）直接得到 ——
  這是**交換環**才有的便利，一般環兩條要分別驗。

### (b) verify that the multiples of a fixed integer form a ring

$n\mathbf{Z}$ 的元素都長成 $nt$（【定義 1】）：

$$\begin{gather*}
\left(n\mathbf{Z}, +\right) &\overset{\text{已知 2}}{=}& \text{阿貝爾群} \qquad \text{(公理 (a))} \\
\left(ns\right)\left(nt\right) &\overset{\text{已知 3(a)}}{=}& n\left(nst\right) \\
\left(ns\right)\left(nt\right) &\overset{\text{定義 1}}{\in}& n\mathbf{Z} \qquad \text{(公理 (b)，因 } nst \in \mathbf{Z}\text{)} \\
a \times \left(b \times c\right) &\overset{\text{已知 3(a)}}{=}& \left(a \times b\right) \times c \qquad \text{(公理 (c)，由 } \mathbf{Z} \text{ 繼承)} \\
a \times \left(b + c\right) &\overset{\text{已知 3(b)}}{=}& a \times b + a \times c \qquad \text{(公理 (d)，由 } \mathbf{Z} \text{ 繼承)}
\end{gather*}$$

四條全中，故 $\left(n\mathbf{Z}, +, \times\right)$ 是環。

* 註：結合律與分配律是**全稱命題**，$n\mathbf{Z} \subseteq \mathbf{Z}$ 故自動繼承 ——
  與 [子群判別法](../Group/Subgroup_Criterion.md) 文末說的是同一個道理。
* 註：$n \ge 2$ 時 $1 \notin n\mathbf{Z}$，故**沒有乘法單位元素**。它仍是環。

### (c) verify that the residues modulo n form a ring

$\mathbf{Z}_n$ 配模 $n$ 加法 $\oplus$ 與模 $n$ 乘法 $\otimes$：

$$\begin{gather*}
\left(\mathbf{Z}_n, \oplus\right) &\overset{\text{已知 2}}{=}& \text{阿貝爾群} \qquad \text{(公理 (a))} \\
a \otimes b &\overset{\text{已知 3(c)}}{=}& \left(a \times b\right) \bmod n \\
a \otimes b &\in& \left\{0, 1, \dots, n-1\right\} = \mathbf{Z}_n \qquad \text{(公理 (b))} \\
a \otimes \left(b \otimes c\right) &\overset{\text{已知 3(a)(c)}}{=}& \left(a \otimes b\right) \otimes c \qquad \text{(公理 (c))} \\
a \otimes \left(b \oplus c\right) &\overset{\text{已知 3(b)(c)}}{=}& \left(a \otimes b\right) \oplus \left(a \otimes c\right) \qquad \text{(公理 (d))}
\end{gather*}$$

四條全中，故 $\left(\mathbf{Z}_n, \oplus, \otimes\right)$ 是環。

* 註：結合律與分配律都靠【已知 3(c)】把運算搬回 $\mathbf{Z}$ 裡做，
  在 $\mathbf{Z}$ 裡用【已知 3(a)(b)】，再取模搬回來。**取模不會破壞這些等式**，
  這就是【已知 3(c)】的全部作用。
* 註：$n$ 是不是質數在這裡**完全無關** —— $\mathbf{Z}_n$ 對任意 $n$ 都是環。
  質數性要到 [體的定義](../Field/Field_Definition.md) 才變得關鍵。

### (d) verify that the continuous functions form a ring

運算是**逐點**定義的：$\left(f+g\right)(x) = f(x) + g(x)$、$\left(fg\right)(x) = f(x)g(x)$。

$$\begin{gather*}
f + g &\overset{\text{已知 4}}{\in}& C(\mathbf{R}) \qquad \text{(加法封閉)} \\
-f &\overset{\text{已知 4}}{\in}& C(\mathbf{R}) \qquad \text{(加法反元素)} \\
\left(C(\mathbf{R}), +\right) &=& \text{阿貝爾群} \qquad \text{(公理 (a)，零元素為常數函數 } 0\text{)} \\
fg &\overset{\text{已知 4}}{\in}& C(\mathbf{R}) \qquad \text{(公理 (b))} \\
\left[f\left(gh\right)\right](x) &\overset{\text{已知 3(a)}}{=}& \left[\left(fg\right)h\right](x) \qquad \text{(公理 (c)，逐點套 } \mathbf{R} \text{ 的結合律)} \\
\left[f\left(g+h\right)\right](x) &\overset{\text{已知 3(b)}}{=}& \left[fg + fh\right](x) \qquad \text{(公理 (d)，逐點套 } \mathbf{R} \text{ 的分配律)}
\end{gather*}$$

四條全中，故 $\left(C(\mathbf{R}), +, \times\right)$ 是環。

* 註：**所有環公理都是逐點驗證的** —— 兩個函數相等的定義是「在每一點取值相同」，
  所以只要 $\mathbf{R}$ 本身滿足某條公理，函數環就自動滿足。
  唯一需要外部輸入的是【已知 4】的封閉性（連續性會不會被破壞）。
* 註：$C(\mathbf{R})$ 有零因子 —— 兩個非零的連續函數可以乘出零函數
  （各自在互補的區間上為零）。詳見 [零因子](Zero_Divisor.md)。

### (e) verify that the polynomials form a ring

依【定義 2】逐條檢查。加法部分逐項套用 $R$ 的加法群結構：

$$\begin{gather*}
\sum_i a_i x^i + \sum_i b_i x^i &\overset{\text{定義 2(b)}}{=}& \sum_i \left(a_i + b_i\right)x^i \\
a_i + b_i &\overset{\text{已知 1(a)}}{\in}& R \qquad \text{(逐項封閉)} \\
\left(R[x], +\right) &\overset{\text{已知 1(a)}}{=}& \text{阿貝爾群} \qquad \text{(公理 (a)，零元素為零多項式)}
\end{gather*}$$

乘法部分，摺積的每個係數都是 $R$ 中有限多個乘積之和：

$$\begin{gather*}
\sum_{i+j=k} a_i b_j &\overset{\text{已知 1(b)(a)}}{\in}& R \qquad \text{(每項在 } R \text{ 內，有限和仍在 } R \text{ 內)} \\
\left(\sum_i a_i x^i\right)\left(\sum_j b_j x^j\right) &\overset{\text{定義 2(c)}}{\in}& R[x] \qquad \text{(公理 (b))}
\end{gather*}$$

結合律與分配律逐係數比對，兩邊在 $x^k$ 的係數都等於同一個三重和：

$$\begin{gather*}
\left[\left(fg\right)h\right]_k &\overset{\text{定義 2(c)}}{=}& \sum_{i+j+l=k} a_i b_j c_l \\
\left[f\left(gh\right)\right]_k &\overset{\text{定義 2(c)}}{=}& \sum_{i+j+l=k} a_i b_j c_l \qquad \text{(公理 (c))} \\
\left[f\left(g+h\right)\right]_k &\overset{\text{已知 1(d)}}{=}& \sum_{i+j=k} a_i\left(b_j + c_j\right) \\
\left[f\left(g+h\right)\right]_k &\overset{\text{已知 1(d)}}{=}& \left[fg + fh\right]_k \qquad \text{(公理 (d))}
\end{gather*}$$

四條全中，故 $\left(R[x], +, \times\right)$ 是環。

* 註：結合律的兩個三重和之所以相同，是因為 $R$ 自己的乘法結合（【已知 1(c)】）
  讓 $\left(a_ib_j\right)c_l = a_i\left(b_jc_l\right)$，於是求和的**項完全一樣**，只是括號位置不同。

### (f) verify that the two-variable polynomials form a ring

依【定義 3】，$R[x,y]$ 就是把 $R[x]$ 當係數環再做一次【定義 2】。
而【證明 (e)】的論證**對任意係數環 $R$ 都成立**，故可直接套用：

$$\begin{gather*}
R[x] &\overset{\text{證明 (e)}}{=}& \text{環} \\
\left(R[x]\right)[y] &\overset{\text{證明 (e)}}{=}& \text{環} \qquad \text{(把 } R[x] \text{ 當係數環再套一次)} \\
R[x, y] &\overset{\text{定義 3}}{=}& \text{環}
\end{gather*}$$

* 註：**這是本檔最省力的一步** —— 因為【證明 (e)】沒有用到 $R$ 的任何特殊性質
  （不需要 $R$ 交換、不需要 $R$ 有 $1$），所以可以無限次遞迴套用，
  得到任意多個未定元的多項式環。

+++

## 意義與密碼學關聯 (Interpretation and Relevance to Cryptography)

### 六個例子的分類

| 環 | 有 $1$？ | 交換？ | 有零因子？ | 是體？ |
|---|---|---|---|---|
| $\mathbf{Z}$ | 有 | 是 | 無 | **否**（沒有除法） |
| $\mathbf{Q}, \mathbf{R}, \mathbf{C}$ | 有 | 是 | 無 | **是** |
| $n\mathbf{Z}$（$n \ge 2$） | **無** | 是 | 無 | 否 |
| $\mathbf{Z}_n$（$n$ 合數） | 有 | 是 | **有** | 否 |
| $\mathbf{Z}_p$（$p$ 質數） | 有 | 是 | 無 | **是** |
| $C(\mathbf{R})$ | 有 | 是 | **有** | 否 |
| $R[x]$ | 隨 $R$ | 隨 $R$ | 隨 $R$ | **否**（$x$ 沒有倒數） |

後面三檔會逐一處理這張表的三個欄位：
[含單位元環與交換環](Ring_with_Identity_and_Commutative_Ring.md)、
[零因子](Zero_Divisor.md)、[體的定義](../Field/Field_Definition.md)。

### $R[x]$ 是密碼學最重要的環

多項式環是後量子密碼的地基：

| 演算法 | 用到的環 |
|---|---|
| AES 的 $GF(2^8)$ | $\mathbf{Z}_2[x] / \left(x^8 + x^4 + x^3 + x + 1\right)$ |
| CRC 校驗、LFSR | $\mathbf{Z}_2[x]$ |
| NTRU | $\mathbf{Z}_q[x] / \left(x^N - 1\right)$ |
| Kyber、Dilithium（NIST 後量子標準） | $\mathbf{Z}_q[x] / \left(x^{256} + 1\right)$ |

**注意表格右欄全都是「$R[x]$ 除以某個東西」** —— 那個「除以」就是
[商環](Quotient_Ring.md) 的運算，而被除的東西是 [主理想](Principal_Ideal.md)。
本檔的 $R[x]$ 只是原料，真正在用的是加工過的商環。

### 為什麼 $x$ 是「形式符號」而不是變數

【定義 2】的第二個註提到一個容易忽略的陷阱：在 $\mathbf{Z}_2[x]$ 裡，

$$f(x) = x^2 + x$$

把 $x = 0$ 與 $x = 1$ 代進去都得到 $0$（$1 + 1 = 0$ 在 $\mathbf{Z}_2$ 裡），
但 $f$ **不是**零多項式 —— 它的係數不全為零。

在有限體上，**「多項式」與「多項式定義的函數」不是同一件事**。
$\mathbf{Z}_2$ 上只有 $4$ 個相異的函數 $\mathbf{Z}_2 \to \mathbf{Z}_2$，
但 $\mathbf{Z}_2[x]$ 有無限多個多項式。

這在實作上是真實的區別：AES 的 $GF(2^8)$ 運算操作的是**係數陣列**（一個位元組的 $8$ 個位元），
不是函數值。搞混兩者會寫出完全錯誤的實作。

### 程式思維

```python
# R[x] 的實作：係數列表，index = 次數
def poly_add(f, g):
    n = max(len(f), len(g))
    return [(f[i] if i < len(f) else 0) + (g[i] if i < len(g) else 0) for i in range(n)]

def poly_mul(f, g):                      # 定義 2(c) 的摺積
    out = [0] * (len(f) + len(g) - 1)
    for i, a in enumerate(f):
        for j, b in enumerate(g):
            out[i + j] += a * b
    return out
```

`poly_mul` 的雙重迴圈就是【定義 2(c)】的 $\sum_{i+j=k} a_ib_j$。
實務上 Kyber 等演算法用 **NTT（數論變換）** 把這個 $O(N^2)$ 的摺積降到 $O(N\log N)$ ——
而 NTT 能成立的原因，正是 [中國剩餘定理](Chinese_Remainder_Theorem.md)。
