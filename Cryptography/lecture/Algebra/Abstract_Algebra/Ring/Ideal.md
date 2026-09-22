# Ideal (理想)

+++

## 證明目標:

`Algebra.pdf` p.33（上半）、p.34、p.35。子環只要求「自己是環」；理想**額外**要求
「被母環的任何元素乘到還是跑不出去」。這個吸收性質是 [商環](Quotient_Ring.md) 能存在的唯一原因。

* (a) 理想判別法（投影片未列，本檔補上）：

$$I \ \text{是 } R \text{ 的理想} \quad \Longleftrightarrow \quad I \neq \varnothing, \quad a - b \in I, \quad ar \in I \qquad \text{for all } a, b \in I,\ r \in R$$

* (b) 每個環至少有兩個理想：$\left\{0\right\}$ 與 $R$。
* (c) $aR = \left\{ar \ \middle|\ r \in R\right\}$ 對每個 $a \in R$ 都是理想。
* (d) 投影片的三個具體例子：$n\mathbf{Z} \trianglelefteq \mathbf{Z}$、
  $\left\{h(x)\left(x^2-2\right)\right\} \trianglelefteq \mathbf{Q}[x]$、
  $\mathbf{Z}[x]$ 中常數項為偶數的多項式 $\trianglelefteq \mathbf{Z}[x]$。
* (e) 理想對交集與和封閉：

$$I_1 \cap I_2 \ \text{是理想}, \qquad I_1 + I_2 = \left\{a_1 + a_2 \ \middle|\ a_1 \in I_1,\ a_2 \in I_2\right\} \ \text{是理想}$$

* (f) 投影片 p.35 的數值例子：

$$4\mathbf{Z} \cap 3\mathbf{Z} = 12\mathbf{Z}, \quad 4\mathbf{Z} \cap 6\mathbf{Z} = 12\mathbf{Z}, \quad 4\mathbf{Z} + 3\mathbf{Z} = \mathbf{Z}, \quad 4\mathbf{Z} + 6\mathbf{Z} = 2\mathbf{Z}$$

* (g) 投影片 p.35 的三個**反**例：$\mathbf{Z}$ 不是 $\mathbf{Q}$ 的理想、
  $\mathbf{Q}$ 不是 $\mathbf{R}$ 的理想、$\mathbf{C}[x]$ 是 $\mathbf{C}[x,y]$ 的子環但**不是**理想。

* $R$ : 環的底層集合 (The underlying set of the ring) $[\text{集合}]$
* $I,\ I_1,\ I_2$ : $R$ 的理想 (Ideals of $R$) $[I \trianglelefteq R]$
* $a,\ b$ : 理想中的元素 (Elements of the ideal) $[a, b \in I]$
* $r$ : 母環中的元素 (An element of the ambient ring) $[r \in R]$
* $\trianglelefteq$ : 「是……的理想」 (The ideal relation) $[\text{關係}]$
* 註：依投影片 p.30 的約定，本檔的環一律**交換且含 $1$**，
  故不必區分左理想、右理想與雙邊理想 —— $ar = ra$ 自動成立。
* 註：**理想比子環強**。(g) 的三個反例都是子環卻不是理想，這正是差別所在。
  反過來，含 $1$ 的環裡理想不一定是子環（理想通常不含 $1$，見文末）。
* 註：理想的記號在本章用 $I \trianglelefteq R$，子環用 $S \le R$，兩者不要混。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [環的公理與基本命題 (Ring axioms and basic propositions)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Ring/Ring_Basic_Propositions.html#a-proof-that-multiplication-by-zero-gives-zero)：** 已於本章 [環的定義](Ring_Definition.md)【定義 1】與 [環的基本命題](Ring_Basic_Propositions.md)【證明 (a)】給出，此處直接引用

  * (a) 分配律與結合律：

    $$a\left(b + c\right) = ab + ac, \qquad \left(a + b\right)c = ac + bc, \qquad a\left(bc\right) = \left(ab\right)c$$

  * (b) 乘以零得零：

    $$a \times 0 = 0 \times a = 0$$

  * (c) 交換性（投影片 p.30 的約定）：

    $$ab = ba$$

  * $R$ : 環的底層集合 (The underlying set of the ring) $[\text{集合}]$
  * $a,\ b,\ c$ : 環元素 (Ring elements) $[a, b, c \in R]$
  * $0$ : 加法單位元素 (The additive identity) $[0 \in R]$

* **【已知 2】 [子群判別法 (Subgroup criterion)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Group/Subgroup_Criterion.html#b-proof-of-the-backward-direction)：** 已於本章 [子群判別法](../Group/Subgroup_Criterion.md) 完整證明，此處套在 $\left(R, +\right)$ 上直接引用不再重證

  $$H \le G \quad \Longleftrightarrow \quad H \neq \varnothing, \quad a + b \in H, \quad -a \in H$$

  * $H$ : $G$ 的子集 (A subset of $G$) $[H \subseteq G]$
  * $G$ : 母群的底層集合 (The underlying set of the ambient group) $[\text{集合}]$
  * $a,\ b$ : 子集中的元素 (Elements of the subset) $[a, b \in H]$

* **【已知 3】 [減法封閉一條抵兩條 (Closure under subtraction implies additive subgroup)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Ring/Subring.html#a-proof-of-the-subring-criterion)：** 已於本章 [子環](Subring.md)【證明 (a)】完整證明，此處直接引用不再重證

  $$S \neq \varnothing, \ a - b \in S \ \text{ for all } a, b \in S \quad \Longrightarrow \quad \left(S, +\right) \le \left(R, +\right)$$

  * $S$ : $R$ 的子集 (A subset of $R$) $[S \subseteq R]$
  * $R$ : 母環的底層集合 (The underlying set of the ambient ring) $[\text{集合}]$
  * $a,\ b$ : 子集中的元素 (Elements of the subset) $[a, b \in S]$
  * 註：技巧是先取 $b = a$ 造出 $0$，再用 $0 - b$ 造出 $-b$，最後用 $a - \left(-b\right)$ 造出 $a + b$。

* **【已知 4】 [$n\mathbf{Z}$ 與多項式環 ($n\mathbf{Z}$ and polynomial rings)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Ring/Ring_Examples.html#b-verify-that-the-multiples-of-a-fixed-integer-form-a-ring)：** 已於本章 [環的例子](Ring_Examples.md)【定義 1】【定義 2】【定義 3】給出，此處直接引用

  $$n\mathbf{Z} = \left\{nt \ \middle|\ t \in \mathbf{Z}\right\}, \qquad R[x] = \left\{\sum_i a_i x^i\right\}, \qquad R[x,y] = \left(R[x]\right)[y]$$

  * $n\mathbf{Z}$ : $n$ 的倍數集合 (The set of multiples of $n$) $[\text{集合}]$
  * $R[x]$ : 多項式環 (The polynomial ring) $[\text{集合}]$
  * $R$ : 係數所在的環 (The coefficient ring) $[\text{環}]$
  * $n$ : 倍數 (The multiplier) $[n \in \mathbf{Z}]$
  * $a_i$ : 多項式係數 (Polynomial coefficients) $[a_i \in R]$
  * $x,\ y$ : 未定元 (Indeterminates) $[x, y \notin R]$

* **【已知 5】 [最小公倍數與貝祖等式 (Least common multiple and Bézout's identity)](https://mathworld.wolfram.com/BezoutsIdentity.html)：** 初等數論的標準結果，本章直接引用不再重證。【證明 (f)】要用

  * (a) 公倍數的刻畫：

    $$m\mathbf{Z} \cap n\mathbf{Z} = \mathrm{lcm}(m, n)\,\mathbf{Z}$$

  * (b) 貝祖等式：

    $$m\mathbf{Z} + n\mathbf{Z} = \gcd(m, n)\,\mathbf{Z}$$

  * $m,\ n$ : 兩個正整數 (Two positive integers) $[m, n \in \mathbf{P}]$
  * $\mathrm{lcm}$ : 最小公倍數 (Least common multiple) $[\mathbf{P} \times \mathbf{P} \to \mathbf{P}]$
  * $\gcd$ : 最大公因數 (Greatest common divisor) $[\mathbf{P} \times \mathbf{P} \to \mathbf{P}]$

* **【定義 1】 理想 (Ideal)：** 加法上是子群，乘法上被整個母環「吸收」

  * (a) 加法子群：

    $$\left(I, +\right) \le \left(R, +\right)$$

  * (b) 吸收性：

    $$ar \in I \qquad \text{for all } a \in I,\ r \in R$$

  * $I$ : $R$ 的子集 (A subset of $R$) $[I \subseteq R]$
  * $R$ : 母環的底層集合 (The underlying set of the ambient ring) $[\text{集合}]$
  * $a$ : 理想中的元素 (An element of the ideal) $[a \in I]$
  * $r$ : 母環中的元素 (An element of the ambient ring) $[r \in R]$
  * 註：**(b) 的 $r$ 取遍整個 $R$，不限於 $I$**。這是理想與子環的唯一差別 ——
    子環只要求 $I$ 內部的乘法封閉（$a, b \in I \Rightarrow ab \in I$），
    理想要求**連外面的元素乘進來都跑不掉**。
  * 註：交換環裡 $ar = ra$（【已知 1(c)】），故左右吸收性等價，不必分開寫。

* **【定義 2】 理想的交集與和 (Intersection and sum of ideals)：**

  * (a) 交集：

    $$I_1 \cap I_2 = \left\{a \ \middle|\ a \in I_1 \ \text{ and } \ a \in I_2\right\}$$

  * (b) 和：

    $$I_1 + I_2 \overset{\text{def}}{=} \left\{a_1 + a_2 \ \middle|\ a_1 \in I_1,\ a_2 \in I_2\right\}$$

  * $I_1,\ I_2$ : $R$ 的兩個理想 (Two ideals of $R$) $[I_1, I_2 \trianglelefteq R]$
  * $a,\ a_1,\ a_2$ : 理想中的元素 (Elements of the ideals) $[a \in I_1 \cap I_2,\ a_1 \in I_1,\ a_2 \in I_2]$
  * 註：(b) **不是**聯集。$I_1 \cup I_2$ 一般**不是**理想（兩邊各取一個元素相加可能兩邊都不屬於），
    $I_1 + I_2$ 是把所有這種和都補進來得到的最小理想。

* **【定義 3】 偶常數項多項式集合 (Polynomials with even constant term)：** 【證明 (d)】要用

  $$E \overset{\text{def}}{=} \left\{f \in \mathbf{Z}[x] \ \middle|\ f(0) \ \text{為偶數}\right\}$$

  * $E$ : 常數項為偶數的整係數多項式全體 (Integer polynomials with even constant term) $[E \subseteq \mathbf{Z}[x]]$
  * $f$ : 一個整係數多項式 (An integer polynomial) $[f \in \mathbf{Z}[x]]$
  * 註：$f(0)$ 就是 $f$ 的常數項 $a_0$，因為代入 $x = 0$ 後其餘各項都消失。

* **【推導 1】 理想判別法 (Ideal criterion)：** 把【定義 1】的兩條改寫成三條可直接檢查的條件

  $$\begin{gather*}
  I \neq \varnothing,\ a - b \in I &\overset{\text{已知 3}}{\Longrightarrow}& \left(I, +\right) \le \left(R, +\right) \qquad \text{(即【定義 1(a)】)} \\
  ar \in I \ \text{ for all } r \in R &\overset{\text{定義 1}}{\Longrightarrow}& \text{吸收性（即【定義 1(b)】）}
  \end{gather*}$$

  * $I$ : $R$ 的子集 (A subset of $R$) $[I \subseteq R]$
  * $R$ : 母環的底層集合 (The underlying set of the ambient ring) $[\text{集合}]$
  * $a,\ b$ : 理想中的元素 (Elements of the ideal) $[a, b \in I]$
  * $r$ : 母環中的元素 (An element of the ambient ring) $[r \in R]$
  * 註：反方向（理想 $\Rightarrow$ 三條件）是【定義 1】的直接內容。故三條件與理想**等價**。
  * 註：**注意這三條裡沒有「$I$ 內部乘法封閉」** —— 它是吸收性的特例
    （取 $r = b \in I \subseteq R$），不必另外檢查。

+++

## 證明:

### (a) verify the ideal criterion on the two trivial ideals

**$\left\{0\right\}$ 是理想**，依【推導 1】三條：

$$\begin{gather*}
0 &\overset{\text{推導 1}}{\in}& \left\{0\right\} \qquad \text{(非空)} \\
0 - 0 &=& 0 \in \left\{0\right\} \qquad \text{(減法封閉)} \\
0 \times r &\overset{\text{已知 1(b)}}{=}& 0 \in \left\{0\right\} \qquad \text{(吸收性)}
\end{gather*}$$

**$R$ 自己是理想**：

$$\begin{gather*}
0 &\in& R \qquad \text{(非空)} \\
a - b &\overset{\text{已知 1(a)}}{\in}& R \qquad \text{(減法封閉，環對減法封閉)} \\
ar &\overset{\text{已知 1(a)}}{\in}& R \qquad \text{(吸收性，環對乘法封閉)}
\end{gather*}$$

故每個環至少有這兩個理想，與投影片一致。

* 註：$\left\{0\right\}$ 稱為**零理想**、$R$ 稱為**平凡理想**。
  只有這兩個理想的環稱為**單環 (simple ring)** —— 體就是這種
  （見 [模不可約多項式的商環是體](../Field/Quotient_by_Irreducible_is_Field.md)）。

### (b) proof that the set of multiples of an element is an ideal

$aR = \left\{ar \ \middle|\ r \in R\right\}$，依【推導 1】三條：

$$\begin{gather*}
0 = a \times 0 &\overset{\text{已知 1(b),推導 1}}{\in}& aR \qquad \text{(非空)} \\
ar_1 - ar_2 &\overset{\text{已知 1(a)}}{=}& a\left(r_1 - r_2\right) \\
ar_1 - ar_2 &\in& aR \qquad \text{(減法封閉，因 } r_1 - r_2 \in R\text{)} \\
\left(ar_1\right)s &\overset{\text{已知 1(a)}}{=}& a\left(r_1 s\right) \\
\left(ar_1\right)s &\in& aR \qquad \text{(吸收性，因 } r_1 s \in R\text{)}
\end{gather*}$$

三條全中，故 $aR \trianglelefteq R$，與投影片一致。

* 註：**這是最重要的一類理想** —— 它有專名叫**主理想**，記作 $\langle a \rangle$，
  見 [主理想](Principal_Ideal.md)。
* 註：吸收性的證明**只用到乘法結合律** —— 這說明 $aR$ 的吸收性是「自動」的，
  不需要 $R$ 的任何特殊性質。

### (c) verify that the multiples of an integer form an ideal of the integers

$n\mathbf{Z}$（【已知 4】）恰好是【證明 (b)】取 $R = \mathbf{Z}$、$a = n$ 的情形：

$$\begin{gather*}
n\mathbf{Z} &\overset{\text{已知 4}}{=}& \left\{nt \ \middle|\ t \in \mathbf{Z}\right\} \\
n\mathbf{Z} &=& n\mathbf{Z} \qquad \text{(即 } aR \text{ 的形式)} \\
n\mathbf{Z} &\overset{\text{證明 (b)}}{\trianglelefteq}& \mathbf{Z}
\end{gather*}$$

與投影片一致。

### (d) verify the two polynomial examples

**第一個例子**：$I = \left\{h(x)\left(x^2 - 2\right) \ \middle|\ h(x) \in \mathbf{Q}[x]\right\}$。
這同樣是【證明 (b)】的形式，取 $R = \mathbf{Q}[x]$、$a = x^2 - 2$：

$$\begin{gather*}
I &=& \left(x^2 - 2\right)\mathbf{Q}[x] \\
I &\overset{\text{證明 (b)}}{\trianglelefteq}& \mathbf{Q}[x]
\end{gather*}$$

**第二個例子**：$E$（【定義 3】），常數項為偶數的整係數多項式。這個**不是** $aR$ 的形式
（見 [$\mathbf{Z}[x]$ 中的非主理想](Non_Principal_Ideal_in_Z_x.md)），必須直接驗證三條：

$$\begin{gather*}
0 &\overset{\text{定義 3}}{\in}& E \qquad \text{(非空，常數項 } 0 \text{ 是偶數)} \\
\left(f - g\right)(0) &=& f(0) - g(0) \\
\left(f - g\right)(0) &\overset{\text{定義 3}}{=}& \text{偶數} - \text{偶數} = \text{偶數} \qquad \text{(減法封閉)} \\
\left(fh\right)(0) &\overset{\text{已知 4}}{=}& f(0)\,h(0) \\
\left(fh\right)(0) &\overset{\text{定義 3}}{=}& \text{偶數} \times \text{整數} = \text{偶數} \qquad \text{(吸收性)}
\end{gather*}$$

三條全中，故 $E \trianglelefteq \mathbf{Z}[x]$，與投影片一致。

* 註：吸收性那一步是關鍵 —— **偶數乘以任何整數都還是偶數**，
  所以無論 $h$ 的常數項是什麼，乘積的常數項一定是偶數。這正是理想的「吸收」精神。

### (e) proof that the intersection and the sum of two ideals are ideals

**交集** $I_1 \cap I_2$，依【推導 1】三條：

$$\begin{gather*}
0 &\overset{\text{證明 (a)}}{\in}& I_1 \cap I_2 \qquad \text{(非空，兩個理想都含 } 0\text{)} \\
a - b &\overset{\text{定義 1(a),已知 2}}{\in}& I_1 \qquad \text{(因 } a, b \in I_1\text{)} \\
a - b &\overset{\text{定義 1(a)}}{\in}& I_2 \qquad \text{(因 } a, b \in I_2\text{)} \\
a - b &\overset{\text{定義 2(a)}}{\in}& I_1 \cap I_2 \qquad \text{(減法封閉)} \\
ar &\overset{\text{定義 1(b)}}{\in}& I_1 \ \text{ 且 } \ ar \in I_2 \\
ar &\overset{\text{定義 2(a)}}{\in}& I_1 \cap I_2 \qquad \text{(吸收性)}
\end{gather*}$$

**和** $I_1 + I_2$，同樣三條：

$$\begin{gather*}
0 = 0 + 0 &\overset{\text{定義 2(b)}}{\in}& I_1 + I_2 \qquad \text{(非空)} \\
\left(a_1 + a_2\right) - \left(b_1 + b_2\right) &=& \left(a_1 - b_1\right) + \left(a_2 - b_2\right) \\
a_1 - b_1 \in I_1, \quad a_2 - b_2 &\overset{\text{定義 1(a)}}{\in}& I_2 \\
\left(a_1 + a_2\right) - \left(b_1 + b_2\right) &\overset{\text{定義 2(b)}}{\in}& I_1 + I_2 \qquad \text{(減法封閉)} \\
\left(a_1 + a_2\right)r &\overset{\text{已知 1(a)}}{=}& a_1 r + a_2 r \\
a_1 r \in I_1, \quad a_2 r &\overset{\text{定義 1(b)}}{\in}& I_2 \\
\left(a_1 + a_2\right)r &\overset{\text{定義 2(b)}}{\in}& I_1 + I_2 \qquad \text{(吸收性)}
\end{gather*}$$

兩者都是理想，與投影片一致。

* 註：**$I_1 \cup I_2$ 一般不是理想**。例如 $2\mathbf{Z} \cup 3\mathbf{Z}$ 裡有 $2$ 與 $3$，
  但 $2 + 3 = 5$ 既不是 $2$ 的倍數也不是 $3$ 的倍數，加法不封閉。
  這就是為什麼【定義 2(b)】要用「和」而不是「聯集」。

### (f) verify the numerical examples of intersections and sums

投影片 p.35 取 $R = \mathbf{Z}$、$I_1 = 4\mathbf{Z}$、$I_2 = 3\mathbf{Z}$、$I_3 = 6\mathbf{Z}$。
**交集**由最小公倍數給出（【已知 5(a)】）：

$$\begin{gather*}
4\mathbf{Z} \cap 3\mathbf{Z} &\overset{\text{已知 5(a)}}{=}& \mathrm{lcm}(4, 3)\,\mathbf{Z} \\
4\mathbf{Z} \cap 3\mathbf{Z} &=& 12\mathbf{Z} \\
4\mathbf{Z} \cap 6\mathbf{Z} &\overset{\text{已知 5(a)}}{=}& \mathrm{lcm}(4, 6)\,\mathbf{Z} \\
4\mathbf{Z} \cap 6\mathbf{Z} &=& 12\mathbf{Z}
\end{gather*}$$

**和**由最大公因數給出（【已知 5(b)】）：

$$\begin{gather*}
4\mathbf{Z} + 3\mathbf{Z} &\overset{\text{已知 5(b)}}{=}& \gcd(4, 3)\,\mathbf{Z} \\
4\mathbf{Z} + 3\mathbf{Z} &=& 1\mathbf{Z} = \mathbf{Z} \\
4\mathbf{Z} + 6\mathbf{Z} &\overset{\text{已知 5(b)}}{=}& \gcd(4, 6)\,\mathbf{Z} \\
4\mathbf{Z} + 6\mathbf{Z} &=& 2\mathbf{Z}
\end{gather*}$$

四式都與投影片一致。

* 註：**交集對應 lcm、和對應 gcd** —— 這個對應關係很值得記住。
  直覺是「理想越大，對應的生成元越小」：$\mathbf{Z} = 1\mathbf{Z}$ 最大、$\gcd$ 最小。
  $4\mathbf{Z} + 3\mathbf{Z} = \mathbf{Z}$ 正是貝祖等式 $\gcd(4,3) = 1$ 的理想版本。
* 註：這個對應在 [中國剩餘定理](Chinese_Remainder_Theorem.md) 會直接用到 ——
  那裡的條件「$I_i + I_j = R$」翻譯成整數的語言就是「$\gcd(m_i, m_j) = 1$」。

### (g) disprove that the three subrings are ideals

**$\mathbf{Z}$ 不是 $\mathbf{Q}$ 的理想。** 取 $a = 2 \in \mathbf{Z}$、$r = \frac{1}{3} \in \mathbf{Q}$：

$$\begin{gather*}
2 \times \frac{1}{3} &=& \frac{2}{3} \\
\frac{2}{3} &\notin& \mathbf{Z} \\
\mathbf{Z} &\overset{\text{定義 1(b)}}{\ntrianglelefteq}& \mathbf{Q} \qquad \text{(吸收性失敗)}
\end{gather*}$$

**$\mathbf{Q}$ 不是 $\mathbf{R}$ 的理想。** 取 $a = 1 \in \mathbf{Q}$、$r = \sqrt{2} \in \mathbf{R}$：

$$\begin{gather*}
1 \times \sqrt{2} &=& \sqrt{2} \\
\sqrt{2} &\notin& \mathbf{Q} \\
\mathbf{Q} &\overset{\text{定義 1(b)}}{\ntrianglelefteq}& \mathbf{R} \qquad \text{(吸收性失敗)}
\end{gather*}$$

**$\mathbf{C}[x]$ 不是 $\mathbf{C}[x,y]$ 的理想**（但**是**子環，已於 [子環](Subring.md)【證明 (d)】證明）。
取 $a = x \in \mathbf{C}[x]$、$r = y \in \mathbf{C}[x,y]$：

$$\begin{gather*}
x \times y &=& xy \\
xy &\overset{\text{已知 4}}{\notin}& \mathbf{C}[x] \qquad \text{(含 } y\text{)} \\
\mathbf{C}[x] &\overset{\text{定義 1(b)}}{\ntrianglelefteq}& \mathbf{C}[x, y] \qquad \text{(吸收性失敗)}
\end{gather*}$$

三個反例都與投影片一致，且**壞的都是同一條 —— 吸收性**。

* 註：三者的加法子群條件全部成立，乘法內部封閉也成立（它們都是子環）。
  **唯一失敗的是「被外面的元素乘進來」**，這正是理想比子環強的地方。
* 註：$\mathbf{Z} \trianglelefteq \mathbf{Q}$ 失敗的深層原因是 **$\mathbf{Q}$ 是體** ——
  體只有 $\left\{0\right\}$ 與自己兩個理想，見文末。

+++

## 意義與密碼學關聯 (Interpretation and Relevance to Cryptography)

### 子環 vs 理想：一張表看懂

| | 加法子群 | 內部乘法封閉 | **被外面乘進來也封閉** |
|---|---|---|---|
| **子環** $S \le R$ | 要 | 要 | **不要求** |
| **理想** $I \trianglelefteq R$ | 要 | 自動（吸收性的特例） | **要** |

【證明 (g)】的三個例子全部卡在最後一欄。

**為什麼要多這一條？** 因為 [商環](Quotient_Ring.md) $R/I$ 要能定義乘法，
需要「$\left(a + I\right)\left(b + I\right) = ab + I$」是良定義的 ——
而那恰好需要吸收性。**沒有吸收性就沒有商環**，理想的全部價值在此。

### 理想通常不含 $1$

如果 $1 \in I$，那麼對任何 $r \in R$：

$$r = 1 \times r \overset{\text{定義 1(b)}}{\in} I \quad \Longrightarrow \quad I = R$$

**含 $1$ 的理想只有 $R$ 自己。** 所以除了平凡理想外，理想都不含 $1$，
因此（在要求子環含 $1$ 的那個慣例下）不算子環。

這也解釋了為什麼**體只有兩個理想**：體裡每個非零元素都可逆，
所以任何非零理想都含有某個 $a \neq 0$ 與它的 $a^{-1}$，於是含 $1$，於是等於整個體。
$\mathbf{Q}$ 與 $\mathbf{R}$ 都是體，這就是【證明 (g)】前兩個反例的根本原因。

### $n\mathbf{Z}$ 與「取模」

【證明 (c)】的 $n\mathbf{Z} \trianglelefteq \mathbf{Z}$ 是整章最重要的一個理想。
它的吸收性就是一句小學算術：

$$\text{$n$ 的倍數} \times \text{任何整數} = \text{$n$ 的倍數}$$

有了它，[商環](Quotient_Ring.md) 才能給出 $\mathbf{Z}/n\mathbf{Z} \cong \mathbf{Z}_n$ ——
也就是說，**「模 $n$ 運算」的正式定義就是「對理想 $n\mathbf{Z}$ 取商」**。

RSA 活在 $\mathbf{Z}_n$ 裡，而 $\mathbf{Z}_n$ 的正式身分是 $\mathbf{Z}/n\mathbf{Z}$，
所以 RSA 從頭到尾都在跟這個理想打交道。

### 密碼學裡的理想：格密碼的地基

後量子密碼（NIST 標準的 Kyber、Dilithium）用的環是

$$R_q = \mathbf{Z}_q[x] / \left\langle x^{256} + 1 \right\rangle$$

那個 $\left\langle x^{256} + 1 \right\rangle$ 就是【證明 (b)】的 $aR$ 形式的理想
（取 $a = x^{256}+1$）。整個 **Ring-LWE 問題**建立在這種商環上，
所以本檔的理想理論不是裝飾品，是後量子密碼的直接地基。

**「理想格 (ideal lattice)」這個名詞裡的「理想」就是本檔的理想** ——
把理想 $I \trianglelefteq \mathbf{Z}[x]/\langle f \rangle$ 的元素看成整數向量，
它們構成的集合是一個格，而格上的最短向量問題被相信是量子電腦也難解的。

### 程式思維

```python
# 理想的吸收性 = 「取模之後再乘，還是可以先乘再取模」
(a * r) % n == ((a % n) * (r % n)) % n     # 恆真

# 這正是 n*Z 是理想的程式版本：
#   a ∈ nZ  <=>  a % n == 0
#   吸收性： a % n == 0  =>  (a * r) % n == 0
assert all((a * r) % n == 0 for r in range(n)) if a % n == 0 else True
```

`%` 運算子能夠「穿過」乘法這件事，就是 $n\mathbf{Z}$ 的吸收性。
沒有它，所有模算術的最佳化（先取模再運算以避免數字爆炸）都不合法。
