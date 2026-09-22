# Chinese Remainder Theorem (中國剩餘定理)

+++

## 證明目標:

`Algebra.pdf` p.43。環論篇的壓軸 —— 把一個大商環**拆成幾個小商環的直積**。
這是 RSA 解密加速、Kyber 的 NTT、秘密分享全部共用的一條定理。

* (a) 投影片的映射是環同態：

$$\varphi : R \to R/I_1 \times \cdots \times R/I_k, \qquad \varphi(r) = \left(r + I_1,\ \dots,\ r + I_k\right)$$

* (b) 它的核恰好是所有理想的交集：

$$\ker \varphi = I_1 \cap I_2 \cap \cdots \cap I_k$$

* (c) 若理想**兩兩互質**（$I_i + I_j = R$ for $i \neq j$），則 $\varphi$ 滿射，於是：

$$R \big/ \left(I_1 \cap \cdots \cap I_k\right) \ \cong \ R/I_1 \times \cdots \times R/I_k$$

* (d) 驗證投影片的例子：

$$\mathbf{Z}/35\mathbf{Z} \ \cong \ \mathbf{Z}/5\mathbf{Z} \times \mathbf{Z}/7\mathbf{Z}$$

* $R$ : 環的底層集合 (The underlying set of the ring) $[\text{集合}]$
* $I_1, \dots, I_k$ : $R$ 的 $k$ 個理想 ($k$ ideals of $R$) $[I_i \trianglelefteq R]$
* $R/I_i$ : 商環 (The quotient rings) $[\text{集合}]$
* $\varphi$ : 投影片定義的映射 (The map defined in the slide) $[R \to \prod_i R/I_i]$
* $r$ : 環元素 (A ring element) $[r \in R]$
* $k$ : 理想的個數 (The number of ideals) $[k \in \mathbf{P}]$
* 註：「兩兩互質」的條件 $I_i + I_j = R$ 翻譯成整數的語言就是 $\gcd(m_i, m_j) = 1$ ——
  由 [理想](Ideal.md)【已知 5(b)】的貝祖等式，$m_i\mathbf{Z} + m_j\mathbf{Z} = \gcd\!\left(m_i,m_j\right)\mathbf{Z}$，
  而它等於 $\mathbf{Z}$ 若且唯若 gcd 為 $1$。
* 註：**條件是「兩兩」互質，不是「全部一起」互質**。
  $\left\{6, 10, 15\right\}$ 三個數的 gcd 是 $1$，但兩兩都不互質，定理不適用。
* 註：(c) 的滿射性是全檔唯一困難的部分，靠【推導 1】【推導 2】兩張卡片支撐。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [商環的定義與運算 (Definition and operations of the quotient ring)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Ring/Quotient_Ring.html#c-proof-that-the-quotient-is-a-ring)：** 已於本章 [商環](Quotient_Ring.md)【定義 1】【證明 (a)(b)(c)】給出並證明，此處直接引用不再重證

  * (a) 運算：

    $$\left(a + I\right) + \left(b + I\right) = \left(a+b\right) + I, \qquad \left(a + I\right)\left(b + I\right) = ab + I$$

  * (b) 同餘類相等的判別式：

    $$a + I = b + I \quad \Longleftrightarrow \quad a - b \in I$$

  * $R$ : 母環的底層集合 (The underlying set of the ambient ring) $[\text{集合}]$
  * $I$ : $R$ 的理想 (An ideal of $R$) $[I \trianglelefteq R]$
  * $a,\ b$ : 環元素 (Ring elements) $[a, b \in R]$

* **【已知 2】 [環同態與核 (Ring homomorphism and kernel)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Ring/Ring_Homomorphism_and_Kernel.html#c-proof-that-injectivity-is-equivalent-to-a-trivial-kernel)：** 已於本章 [環同態與核](Ring_Homomorphism_and_Kernel.md)【定義 1】【定義 2】【定義 3】【證明 (c)】給出並證明，此處直接引用不再重證

  * (a) 同態的定義：

    $$f\left(a+b\right) = f(a) \oplus f(b), \qquad f\left(ab\right) = f(a) \otimes f(b)$$

  * (b) 核的定義與單射判準：

    $$\ker f = \left\{r \ \middle|\ f(r) = 0\right\}, \qquad f \ \text{單射} \Leftrightarrow \ker f = \left\{0\right\}$$

  * (c) 同構：同態且雙射。

    $$f \ \text{為同構} \quad \Longleftrightarrow \quad f \ \text{同態且雙射}$$

  * $f$ : 兩環之間的映射 (A map between two rings) $[R \to S]$
  * $a,\ b,\ r$ : 環元素 (Ring elements) $[a, b, r \in R]$
  * $R,\ S$ : 兩個環 (Two rings) $[\text{集合}]$

* **【已知 3】 [理想的性質 (Properties of ideals)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Ring/Ideal.html#e-proof-that-the-intersection-and-the-sum-of-two-ideals-are-ideals)：** 已於本章 [理想](Ideal.md)【定義 1】【定義 2】【證明 (e)】與文末給出並證明，此處直接引用不再重證

  * (a) 吸收性：

    $$cr \in I \qquad \text{for all } c \in I,\ r \in R$$

  * (b) 交集與和都是理想：

    $$I_1 \cap I_2 \trianglelefteq R, \qquad I_1 + I_2 = \left\{a_1 + a_2 \ \middle|\ a_i \in I_i\right\} \trianglelefteq R$$

  * (c) 含 $1$ 的理想就是整個環：

    $$1 \in I \quad \Longrightarrow \quad I = R$$

  * $I,\ I_1,\ I_2$ : $R$ 的理想 (Ideals of $R$) $[I \trianglelefteq R]$
  * $R$ : 母環的底層集合 (The underlying set of the ambient ring) $[\text{集合}]$
  * $c,\ a_1,\ a_2$ : 理想中的元素 (Elements of the ideals) $[c \in I,\ a_i \in I_i]$
  * $r$ : 母環中的元素 (An element of the ambient ring) $[r \in R]$

* **【已知 4】 [理想的交與和對應 lcm 與 gcd (Intersection and sum correspond to lcm and gcd)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Ring/Ideal.html#f-verify-the-numerical-examples-of-intersections-and-sums)：** 已於本章 [理想](Ideal.md)【已知 5】【證明 (f)】引用並驗證，此處再次引用

  $$m\mathbf{Z} \cap n\mathbf{Z} = \mathrm{lcm}(m,n)\,\mathbf{Z}, \qquad m\mathbf{Z} + n\mathbf{Z} = \gcd(m,n)\,\mathbf{Z}$$

  * $m,\ n$ : 兩個正整數 (Two positive integers) $[m, n \in \mathbf{P}]$
  * $\mathrm{lcm},\ \gcd$ : 最小公倍數與最大公因數 (Least common multiple and greatest common divisor) $[\mathbf{P} \times \mathbf{P} \to \mathbf{P}]$

* **【定義 1】 環的直積 (Direct product of rings)：** 逐分量做運算

  $$R_1 \times \cdots \times R_k \overset{\text{def}}{=} \left\{\left(x_1, \dots, x_k\right) \ \middle|\ x_i \in R_i\right\}$$

  配上逐分量的加法與乘法：

  $$\left(x_1, \dots, x_k\right) + \left(y_1, \dots, y_k\right) \overset{\text{def}}{=} \left(x_1 + y_1,\ \dots,\ x_k + y_k\right), \qquad \left(x_1, \dots, x_k\right)\left(y_1, \dots, y_k\right) \overset{\text{def}}{=} \left(x_1 y_1,\ \dots,\ x_k y_k\right)$$

  * $R_i$ : 第 $i$ 個環 (The $i$-th ring) $[\text{集合}]$
  * $x_i,\ y_i$ : 各分量的元素 (Components) $[x_i, y_i \in R_i]$
  * $k$ : 分量個數 (The number of components) $[k \in \mathbf{P}]$
  * 註：直積的零元素是 $\left(0, \dots, 0\right)$、單位元素是 $\left(1, \dots, 1\right)$。
    環公理逐分量驗證即得，本檔不另證。
  * 註：**直積通常有零因子** —— $\left(1, 0\right)\left(0, 1\right) = \left(0,0\right)$。
    所以即使每個 $R_i$ 都是整環，直積也不是。這一點在
    [模不可約多項式的商環是體](../Field/Quotient_by_Irreducible_is_Field.md) 會用來區分 $\mathbf{C}$ 與 $\mathbf{R} \times \mathbf{R}$。

* **【定義 2】 兩兩互質的理想 (Pairwise comaximal ideals)：**

  $$I_i + I_j = R \qquad \text{for all } i \neq j$$

  * $I_i,\ I_j$ : $R$ 的兩個理想 (Two ideals of $R$) $[I_i, I_j \trianglelefteq R]$
  * $R$ : 母環的底層集合 (The underlying set of the ambient ring) $[\text{集合}]$
  * $i,\ j$ : 理想的指標 (Ideal indices) $[i, j \in \left\{1, \dots, k\right\}]$
  * 註：由【已知 3(c)】，$I_i + I_j = R$ 等價於 $1 \in I_i + I_j$，
    也就是**存在 $e_i \in I_i$、$e_j \in I_j$ 使 $e_i + e_j = 1$**。
    這個拆法是【推導 2】的起點，也是整條證明的引擎。

* **【假設 1】 歸納假設 (Induction hypothesis)：** 【證明 (c)】對理想個數 $k$ 做歸納時的假設。
  設結論對 $k-1$ 個兩兩互質的理想已經成立

  $$R \big/ \left(I_2 \cap \cdots \cap I_k\right) \ \cong \ R/I_2 \times \cdots \times R/I_k$$

  * $R$ : 母環的底層集合 (The underlying set of the ambient ring) $[\text{集合}]$
  * $I_2, \dots, I_k$ : $k-1$ 個兩兩互質的理想 ($k-1$ pairwise comaximal ideals) $[I_i \trianglelefteq R]$
  * $k$ : 理想的個數 (The number of ideals) $[k \in \mathbf{P}]$
  * 註：歸納的基底情形是 $k = 2$，由【推導 2】直接給出，不需要本假設。

* **【推導 1】 互質性傳遞到交集 (Comaximality passes to intersections)：** 【證明 (c)】的歸納步驟要用。
  若 $I_1$ 與 $I_2, \dots, I_k$ 各自互質，則 $I_1$ 與它們的交集也互質

  * (a) $k = 3$ 的情形。把兩個「$1$ 的拆法」相乘：

    $$\begin{gather*}
    1 &\overset{\text{定義 2}}{=}& a_2 + b_2 \qquad \text{with } a_2 \in I_1,\ b_2 \in I_2 \\
    1 &\overset{\text{定義 2}}{=}& a_3 + b_3 \qquad \text{with } a_3 \in I_1,\ b_3 \in I_3 \\
    1 &=& \left(a_2 + b_2\right)\left(a_3 + b_3\right) \\
    1 &=& \underbrace{a_2 a_3 + a_2 b_3 + b_2 a_3}_{\in\, I_1} + \underbrace{b_2 b_3}_{\in\, I_2 \cap I_3}
    \end{gather*}$$

  * (b) 前三項由吸收性落在 $I_1$、第四項同時落在 $I_2$ 與 $I_3$：

    $$\begin{gather*}
    a_2 a_3,\ a_2 b_3,\ b_2 a_3 &\overset{\text{已知 3(a)}}{\in}& I_1 \qquad \text{(每一項都含一個 } I_1 \text{ 的因子)} \\
    b_2 b_3 &\overset{\text{已知 3(a)}}{\in}& I_2 \qquad \text{(} b_2 \in I_2\text{)} \\
    b_2 b_3 &\overset{\text{已知 3(a)}}{\in}& I_3 \qquad \text{(} b_3 \in I_3\text{)} \\
    1 &\overset{\text{已知 3(b)}}{\in}& I_1 + \left(I_2 \cap I_3\right) \\
    I_1 + \left(I_2 \cap I_3\right) &\overset{\text{已知 3(c)}}{=}& R
    \end{gather*}$$

  * $I_1,\ I_2,\ I_3$ : $R$ 的三個理想 (Three ideals of $R$) $[I_i \trianglelefteq R]$
  * $a_2,\ a_3$ : $I_1$ 中的元素 (Elements of $I_1$) $[a_2, a_3 \in I_1]$
  * $b_2,\ b_3$ : $I_2, I_3$ 中的元素 (Elements of $I_2, I_3$) $[b_2 \in I_2,\ b_3 \in I_3]$
  * $R$ : 母環的底層集合 (The underlying set of the ambient ring) $[\text{集合}]$
  * 註：一般的 $k$ 把 $k-1$ 個拆法全部相乘，展開後**唯一不含 $I_1$ 因子的項**是
    $b_2 b_3 \cdots b_k$，而它落在 $I_2 \cap \cdots \cap I_k$ 裡。論證逐字相同。
  * 註：**這張卡片是整條證明裡唯一「有技巧」的一步** ——
    把兩個等於 $1$ 的式子**相乘**（而不是相加），展開後自動分成兩堆。

* **【推導 2】 兩個互質理想的情形可以解 (Solving the two-ideal case)：** 【證明 (c)】的基底情形。
  給定任意目標 $\left(a_1 + I_1,\ a_2 + I_2\right)$，構造出一個 $r$ 同時滿足兩個條件

  * (a) 取 $1$ 的拆法並構造候選解：

    $$\begin{gather*}
    1 &\overset{\text{定義 2}}{=}& e_1 + e_2 \qquad \text{with } e_1 \in I_1,\ e_2 \in I_2 \\
    r &\overset{\text{let}}{=}& a_1 e_2 + a_2 e_1
    \end{gather*}$$

  * (b) 驗證第一個條件 $r \equiv a_1 \pmod{I_1}$：

    $$\begin{gather*}
    r - a_1 &=& a_1 e_2 + a_2 e_1 - a_1 \\
    r - a_1 &=& a_1 e_2 + a_2 e_1 - a_1\left(e_1 + e_2\right) \\
    r - a_1 &=& a_2 e_1 - a_1 e_1 \\
    r - a_1 &=& \left(a_2 - a_1\right)e_1 \\
    r - a_1 &\overset{\text{已知 3(a)}}{\in}& I_1 \qquad \text{(因 } e_1 \in I_1\text{)}
    \end{gather*}$$

  * (c) 驗證第二個條件 $r \equiv a_2 \pmod{I_2}$（與 (b) 完全對稱）：

    $$\begin{gather*}
    r - a_2 &=& a_1 e_2 + a_2 e_1 - a_2\left(e_1 + e_2\right) \\
    r - a_2 &=& a_1 e_2 - a_2 e_2 \\
    r - a_2 &=& \left(a_1 - a_2\right)e_2 \\
    r - a_2 &\overset{\text{已知 3(a)}}{\in}& I_2 \qquad \text{(因 } e_2 \in I_2\text{)}
    \end{gather*}$$

  * $I_1,\ I_2$ : $R$ 的兩個互質理想 (Two comaximal ideals of $R$) $[I_1, I_2 \trianglelefteq R]$
  * $e_1,\ e_2$ : $1$ 的一組拆法 (A decomposition of one) $[e_1 \in I_1,\ e_2 \in I_2]$
  * $a_1,\ a_2$ : 目標的兩個代表元 (The two target representatives) $[a_1, a_2 \in R]$
  * $r$ : 構造出的解 (The constructed solution) $[r \in R]$
  * 註：(b) 第二行的關鍵是**把 $a_1$ 寫成 $a_1 \times 1 = a_1\left(e_1+e_2\right)$** ——
    這樣 $a_1 e_2$ 就被抵銷，只剩下帶 $e_1$ 的項。(c) 同理。
  * 註：構造式 $r = a_1 e_2 + a_2 e_1$ 的**交叉配對**是刻意的：
    $e_2 \in I_2$ 在模 $I_1$ 時等於 $1$（因 $e_2 = 1 - e_1$），所以 $a_1 e_2 \equiv a_1$；
    而 $e_1 \in I_1$ 在模 $I_1$ 時等於 $0$，所以 $a_2 e_1 \equiv 0$。兩者相加恰好是 $a_1$。

+++

## 證明:

### (a) proof that the map is a ring homomorphism

依【已知 2(a)】檢查兩條。兩者都是把【已知 1(a)】的商環運算逐分量套用：

$$\begin{gather*}
\varphi\left(r + s\right) &=& \left(\left(r+s\right) + I_1,\ \dots,\ \left(r+s\right) + I_k\right) \\
\varphi\left(r + s\right) &\overset{\text{已知 1(a)}}{=}& \left(\left(r + I_1\right) + \left(s + I_1\right),\ \dots,\ \left(r + I_k\right) + \left(s + I_k\right)\right) \\
\varphi\left(r + s\right) &\overset{\text{定義 1}}{=}& \varphi(r) + \varphi(s) \\
\varphi\left(rs\right) &=& \left(rs + I_1,\ \dots,\ rs + I_k\right) \\
\varphi\left(rs\right) &\overset{\text{已知 1(a)}}{=}& \left(\left(r + I_1\right)\left(s + I_1\right),\ \dots,\ \left(r + I_k\right)\left(s + I_k\right)\right) \\
\varphi\left(rs\right) &\overset{\text{定義 1}}{=}& \varphi(r)\,\varphi(s)
\end{gather*}$$

兩條全中，故 $\varphi$ 是環同態，與投影片一致。

### (b) proof that the kernel is the intersection of the ideals

直積的零元素是 $\left(0 + I_1, \dots, 0 + I_k\right)$（【定義 1】的註）。依【已知 2(b)】：

$$\begin{gather*}
r \in \ker \varphi &\overset{\text{已知 2(b)}}{\Longleftrightarrow}& \varphi(r) = \left(0 + I_1,\ \dots,\ 0 + I_k\right) \\
&\Longleftrightarrow& r + I_i = 0 + I_i \quad \text{for all } i \\
&\overset{\text{已知 1(b)}}{\Longleftrightarrow}& r - 0 \in I_i \quad \text{for all } i \\
&\Longleftrightarrow& r \in I_1 \cap I_2 \cap \cdots \cap I_k
\end{gather*}$$

故 $\ker \varphi = I_1 \cap \cdots \cap I_k$，與投影片一致。

### (c) proof of surjectivity and the isomorphism

**先證 $k = 2$ 的滿射性。** 任取目標 $\left(a_1 + I_1,\ a_2 + I_2\right)$，
【推導 2】已經構造出 $r = a_1 e_2 + a_2 e_1$ 並驗證兩個條件：

$$\begin{gather*}
r - a_1 &\overset{\text{推導 2(b)}}{\in}& I_1 \\
r + I_1 &\overset{\text{已知 1(b)}}{=}& a_1 + I_1 \\
r - a_2 &\overset{\text{推導 2(c)}}{\in}& I_2 \\
r + I_2 &\overset{\text{已知 1(b)}}{=}& a_2 + I_2 \\
\varphi(r) &=& \left(a_1 + I_1,\ a_2 + I_2\right)
\end{gather*}$$

任意目標都有原像，故 $\varphi$ 滿射。

**再用歸納推到一般的 $k$。** 設 $k \ge 3$ 且結論對 $k-1$ 成立。
由【推導 1】，$I_1$ 與 $J = I_2 \cap \cdots \cap I_k$ 互質：

$$\begin{gather*}
I_1 + J &\overset{\text{推導 1}}{=}& R \\
R \big/ \left(I_1 \cap J\right) &\overset{\text{推導 2}}{\cong}& R/I_1 \times R/J \qquad \text{(} k=2 \text{ 的情形)} \\
R/J &=& R \big/ \left(I_2 \cap \cdots \cap I_k\right) \\
R/J &\overset{\text{假設 1}}{\cong}& R/I_2 \times \cdots \times R/I_k \\
R \big/ \left(I_1 \cap \cdots \cap I_k\right) &\cong& R/I_1 \times R/I_2 \times \cdots \times R/I_k
\end{gather*}$$

**最後把滿射與核合起來。** $\varphi$ 是滿射同態、核為 $I_1 \cap \cdots \cap I_k$，
故誘導出的映射

$$\bar{\varphi} : R \big/ \left(I_1 \cap \cdots \cap I_k\right) \to R/I_1 \times \cdots \times R/I_k, \qquad \bar{\varphi}\left(r + \bigcap_i I_i\right) = \varphi(r)$$

良定義（由【證明 (b)】，$\ker\varphi$ 裡的元素送到零）、單射（核已被除掉）、滿射（剛證）、保運算（【證明 (a)】），
故依【已知 2(c)】是同構：

$$R \big/ \left(I_1 \cap \cdots \cap I_k\right) \ \cong \ R/I_1 \times \cdots \times R/I_k$$

與投影片一致。

* 註：**兩兩互質的條件不可省。** 少了它 $\varphi$ 不滿射 ——
  例如 $R = \mathbf{Z}$、$I_1 = I_2 = 2\mathbf{Z}$ 時 $\varphi$ 的像只有對角線
  $\left\{(x,x)\right\}$，打不到 $(0+2\mathbf{Z},\ 1+2\mathbf{Z})$。
* 註：【推導 1】正是為了讓歸納跑得動 —— 歸納時要把 $I_2, \dots, I_k$ 收成一個 $J$，
  而必須先確認 $I_1$ 與 $J$ 仍然互質。

### (d) verify the example from the slides

取 $R = \mathbf{Z}$、$I_1 = 5\mathbf{Z}$、$I_2 = 7\mathbf{Z}$。

**先檢查互質**（【定義 2】）：

$$\begin{gather*}
5\mathbf{Z} + 7\mathbf{Z} &\overset{\text{已知 4}}{=}& \gcd(5, 7)\,\mathbf{Z} \\
&=& 1\mathbf{Z} \\
&=& \mathbf{Z}
\end{gather*}$$

**再算交集**（【已知 4】）：

$$\begin{gather*}
5\mathbf{Z} \cap 7\mathbf{Z} &\overset{\text{已知 4}}{=}& \mathrm{lcm}(5, 7)\,\mathbf{Z} \\
&=& 35\mathbf{Z}
\end{gather*}$$

代入【證明 (c)】：

$$\mathbf{Z}/35\mathbf{Z} \ \cong \ \mathbf{Z}/5\mathbf{Z} \times \mathbf{Z}/7\mathbf{Z}$$

與投影片一致。具體的 $1$ 的拆法（【推導 2(a)】的 $e_1, e_2$）：

$$\begin{gather*}
1 &=& 5 \times 3 + 7 \times \left(-2\right) \\
1 &=& 15 + \left(-14\right) \\
e_1 = 15 &\in& 5\mathbf{Z} \\
e_2 = -14 &\in& 7\mathbf{Z}
\end{gather*}$$

於是給定餘數 $\left(a_1, a_2\right)$，解是 $r = a_1 \times \left(-14\right) + a_2 \times 15 \pmod{35}$。
例如求「模 $5$ 餘 $3$、模 $7$ 餘 $4$」的數：

$$\begin{gather*}
r &\overset{\text{推導 2(a)}}{=}& 3 \times \left(-14\right) + 4 \times 15 \\
r &=& -42 + 60 \\
r &=& 18 \\
18 \bmod 5 &=& 3 \\
18 \bmod 7 &=& 4
\end{gather*}$$

兩個條件都滿足，構造正確。

+++

## 意義與密碼學關聯 (Interpretation and Relevance to Cryptography)

### 定理在說什麼：一個大問題拆成幾個小問題

$$\mathbf{Z}/35\mathbf{Z} \ \cong \ \mathbf{Z}/5\mathbf{Z} \times \mathbf{Z}/7\mathbf{Z}$$

左邊有 $35$ 個元素、右邊有 $5 \times 7 = 35$ 個 —— 個數對得上不是巧合，
是同構的必然。而且對應是**可計算的兩個方向**：

* **正向**（容易）：給 $r$，算 $\left(r \bmod 5,\ r \bmod 7\right)$。
* **逆向**（也容易）：給 $\left(a_1, a_2\right)$，用【推導 2(a)】的公式算回 $r$。

**在 $\mathbf{Z}_{35}$ 裡算一次乘法，等於在 $\mathbf{Z}_5$ 與 $\mathbf{Z}_7$ 裡各算一次。**
數字小了，運算快了。

### RSA-CRT：解密加速四倍

這是本檔最直接的應用。RSA 的 $n = pq$，由【證明 (c)】：

$$\mathbf{Z}_n \ \cong \ \mathbf{Z}_p \times \mathbf{Z}_q$$

解密要算 $m = c^d \bmod n$，其中 $d$ 與 $n$ 都是 $2048$ 位元。改走 CRT：

$$\begin{aligned}
m_p &= c^{d \bmod (p-1)} \bmod p \\
m_q &= c^{d \bmod (q-1)} \bmod q \\
m &= \text{CRT 合併}\left(m_p, m_q\right)
\end{aligned}$$

模冪運算的成本大約是模數位元長度的三次方。位元長度減半 $\Rightarrow$ 成本變成 $1/8$，
兩次加起來是 $1/4$。**RSA-CRT 讓解密快約四倍**，所以幾乎所有實作都用它 ——
OpenSSL 的私鑰格式裡存的 `p`、`q`、`dmp1`、`dmq1`、`iqmp` 五個欄位就是為此。

其中 `dmp1` $= d \bmod (p-1)$ 這個化簡，理由是
[元素的階與循環子群](../Group/Order_of_Element_and_Cyclic_Subgroup.md)【證明 (d)】的費馬小定理。

### 同一條定理也是最著名的攻擊入口

**Bellcore attack（1997）**：若 RSA-CRT 的兩個分支之一因硬體故障算錯，
得到 $m_p$ 正確、$m_q'$ 錯誤，則合併出的簽章 $s'$ 滿足：

$$s'^{\,e} \equiv m \pmod p, \qquad s'^{\,e} \not\equiv m \pmod q$$

於是 $\gcd\!\left(s'^{\,e} - m,\ n\right) = p$ —— **一次錯誤的簽章就分解了 $n$。**

這與 [零因子](Zero_Divisor.md) 文末說的「找到零因子等於分解 $n$」是同一件事：
$s'^{\,e} - m$ 是 $\mathbf{Z}_n$ 的一個零因子。

防禦方法是**驗證後再輸出**（算完簽章先用公鑰驗一次），這已是所有正規實作的標配。

### Kyber 的 NTT：同一條定理的多項式版本

後量子標準 Kyber 用的環是 $R_q = \mathbf{Z}_q[x]/\left\langle x^{256}+1 \right\rangle$。
當 $q$ 選得好時，$x^{256}+1$ 在 $\mathbf{Z}_q$ 上可以分解成 $128$ 個二次因式，
於是由【證明 (c)】：

$$\mathbf{Z}_q[x] \big/ \left\langle x^{256}+1 \right\rangle \ \cong \ \prod_{i=1}^{128} \mathbf{Z}_q[x] \big/ \left\langle f_i(x) \right\rangle$$

右邊每個分量的乘法都是小運算。這個同構的快速實作就是 **NTT（數論變換）**，
它把多項式乘法從 $O(N^2)$ 降到 $O(N \log N)$。

**Kyber 的 $q = 3329$ 不是隨便選的** —— 它要讓 $x^{256}+1$ 有足夠多的因式，
CRT 才拆得夠細。這是本定理直接決定密碼參數的一個實例。

### 秘密分享：把祕密藏在互質性裡

**Asmuth–Bloom 秘密分享**：選兩兩互質的 $m_1 < m_2 < \dots < m_k$，
把祕密 $s$ 的份額設為 $s \bmod m_i$。

* 拿到 $t$ 份以上 $\Rightarrow$ $\prod$ 夠大 $\Rightarrow$ 由 CRT 唯一還原 $s$；
* 拿到 $t-1$ 份 $\Rightarrow$ $\prod$ 太小 $\Rightarrow$ 有多個 $s$ 都說得通，**什麼都推不出來**。

**兩兩互質的條件在這裡直接翻譯成安全性** —— 若 $m_i$ 們不互質，
份額之間會有重疊資訊，門檻就守不住。

### 程式思維

```python
def crt(residues, moduli):
    """中國剩餘定理：推導 2(a) 的構造，推廣到 k 個模數。"""
    from math import prod
    N = prod(moduli)
    total = 0
    for a_i, m_i in zip(residues, moduli):
        N_i = N // m_i                    # N_i ∈ 其他所有理想的交集
        total += a_i * N_i * pow(N_i, -1, m_i)
    return total % N

assert crt([3, 4], [5, 7]) == 18          # 證明 (d) 的例子
```

`pow(N_i, -1, m_i)` 能成功的前提正是 $\gcd\!\left(N_i, m_i\right) = 1$ ——
也就是**兩兩互質的條件**。模數若不互質，這一行會丟出 `ValueError`，
忠實反映了【定義 2】的必要性。
