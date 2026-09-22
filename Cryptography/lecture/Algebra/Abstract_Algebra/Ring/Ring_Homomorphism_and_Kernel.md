# Ring Homomorphism and Kernel (環同態與核)

+++

## 證明目標:

`Algebra.pdf` p.41–42。與 [群同態與群同構](../Group/Group_Homomorphism_and_Isomorphism.md) 完全平行，
但因為環有兩個運算，同態要**同時保住兩個**。多出來的新東西是**核**。

* (a) 同態的兩條基本性質：

$$f(0) = 0, \qquad f(-a) = -f(a)$$

* (b) 投影片斷言的「$\ker f$ 是理想」：

$$\ker f = \left\{r \in R \ \middle|\ f(r) = 0\right\} \trianglelefteq R$$

* (c) 核完全決定單射性：

$$f \ \text{單射} \quad \Longleftrightarrow \quad \ker f = \left\{0\right\}$$

* (d)–(f) 投影片 p.42 的三個例子：複數共軛是**自同構**、
  零映射 $\mathbf{Z} \to \mathbf{Z}$ 是同態但非同構、
  $\mathbf{Z} \to \mathbf{Z}_n$ 是滿射非單射、$\mathbf{Q}[\omega] \to \mathbf{C}$ 是單射非滿射。

* $R,\ S$ : 兩個環的底層集合 (The underlying sets of two rings) $[\text{集合}]$
* $f$ : 兩環之間的映射 (A map between the two rings) $[R \to S]$
* $+,\ \times$ : $R$ 的兩個運算 (The two operations of $R$) $[R \times R \to R]$
* $\oplus,\ \otimes$ : $S$ 的兩個運算 (The two operations of $S$) $[S \times S \to S]$
* $a,\ b$ : 環元素 (Ring elements) $[a, b \in R]$
* $\ker f$ : $f$ 的核 (The kernel of $f$) $[\ker f \trianglelefteq R]$
* $\omega$ : $x^2 + x + 1 = 0$ 的一個根 (A root of $x^2+x+1=0$) $[\omega \in \mathbf{C}]$
* 註：(c) 不在投影片上，但它是**核最重要的性質** ——
  它把「$f$ 單不單射」這個關於全體元素的問題，壓縮成「$\ker f$ 有幾個元素」這一個檢查。
* 註：**核是理想、不是子環**（它通常不含 $1$）。這與 [理想](Ideal.md) 文末說的一致。
* 註：本檔的 (b) 與 [特殊線性群的指標](../Group/Special_Linear_Subgroup_Index.md) 文末提到的
  $\det : GL_2 \to \mathbf{Z}_7^*$ 是同一個模式的兩個版本 ——
  群同態的核是**正規子群**，環同態的核是**理想**。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [環的公理與基本命題 (Ring axioms and basic propositions)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Ring/Ring_Basic_Propositions.html#a-proof-that-multiplication-by-zero-gives-zero)：** 已於本章 [環的定義](Ring_Definition.md)【定義 1】與 [環的基本命題](Ring_Basic_Propositions.md)【證明 (a)】給出，此處直接引用

  * (a) 加法群結構：

    $$a + 0 = a, \qquad a + \left(-a\right) = 0$$

  * (b) 乘以零得零：

    $$a \times 0 = 0 \times a = 0$$

  * $R$ : 環的底層集合 (The underlying set of the ring) $[\text{集合}]$
  * $a$ : 環元素 (A ring element) $[a \in R]$
  * $0$ : 加法單位元素 (The additive identity) $[0 \in R]$

* **【已知 2】 [加法群的消去律與反元素唯一 (Cancellation and uniqueness of the additive inverse)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Group/Unique_Solution_and_Cancellation_Law.html#a-proof-of-the-left-cancellation-law)：** 已於本章 [唯一解與消去律](../Group/Unique_Solution_and_Cancellation_Law.md)【證明 (a)】與 [反元素唯一](../Group/Uniqueness_of_Inverse.md)【證明 (a)】完整證明，此處套在加法群上直接引用不再重證

  * (a) 消去律：

    $$x + y = x + z \quad \Longrightarrow \quad y = z$$

  * (b) 反元素唯一：

    $$x + y = 0 \quad \Longrightarrow \quad y = -x$$

  * $x,\ y,\ z$ : 環元素 (Ring elements) $[x, y, z \in R]$

* **【已知 3】 [理想判別法 (Ideal criterion)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Ring/Ideal.html#assumptions-preliminaries)：** 已於本章 [理想](Ideal.md)【推導 1】完整證明，此處直接引用不再重證

  $$I \trianglelefteq R \quad \Longleftrightarrow \quad I \neq \varnothing, \quad a - b \in I, \quad ar \in I \qquad \text{for all } a, b \in I,\ r \in R$$

  * $I$ : $R$ 的子集 (A subset of $R$) $[I \subseteq R]$
  * $R$ : 環的底層集合 (The underlying set of the ring) $[\text{集合}]$
  * $a,\ b$ : 理想中的元素 (Elements of the ideal) $[a, b \in I]$
  * $r$ : 母環中的元素 (An element of the ambient ring) $[r \in R]$

* **【已知 4】 [單射、滿射與雙射 (Injectivity, surjectivity, bijectivity)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Group/Permutation.html#assumptions-preliminaries)：** 已於本章 [排列](../Group/Permutation.md)【定義 1】【定義 2】【定義 3】給出，此處直接引用

  $$f \ \text{單射} \Leftrightarrow \left[f(x)=f(y) \Rightarrow x=y\right], \qquad f \ \text{滿射} \Leftrightarrow f(R) = S$$

  * $f$ : 兩環之間的映射 (A map between the two rings) $[R \to S]$
  * $x,\ y$ : 定義域中的元素 (Elements of the domain) $[x, y \in R]$
  * $R,\ S$ : 定義域與值域 (The domain and codomain) $[\text{集合}]$

* **【已知 5】 [複數共軛是雙射且保乘法 (Complex conjugation is a multiplicative bijection)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Group/Group_Homomorphism_and_Isomorphism.html#d-verify-that-complex-conjugation-is-an-isomorphism)：** 已於本章 [群同態與群同構](../Group/Group_Homomorphism_and_Isomorphism.md)【證明 (d)】完整證明，此處直接引用不再重證

  $$\overline{zw} = \bar{z}\,\bar{w}, \qquad \overline{\overline{z}} = z$$

  * $z,\ w$ : 複數 (Complex numbers) $[z, w \in \mathbf{C}]$
  * $\bar{z}$ : $z$ 的共軛 (The conjugate of $z$) $[\bar{z} \in \mathbf{C}]$
  * 註：該處證的是乘法群 $\left(\mathbf{C}^*, \times\right)$ 上的同構。
    本檔還需要加法的部分 $\overline{z+w} = \bar{z} + \bar{w}$，見【證明 (d)】。

* **【已知 6】 [商環與模運算 (Quotient ring and modular arithmetic)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Ring/Quotient_Ring.html#e-proof-that-the-integers-modulo-the-multiples-of-n-form-the-ring-of-residues)：** 已於本章 [商環](Quotient_Ring.md)【證明 (e)】完整證明，此處直接引用不再重證

  $$\mathbf{Z}/n\mathbf{Z} \cong \mathbf{Z}_n, \qquad \left(a+b\right) \bmod n = \left(a \bmod n\right) \oplus \left(b \bmod n\right), \qquad \left(ab\right) \bmod n = \left(a \bmod n\right) \otimes \left(b \bmod n\right)$$

  * $\mathbf{Z}_n$ : 模 $n$ 剩餘類環 (The ring of residues modulo $n$) $[\text{集合}]$
  * $n\mathbf{Z}$ : $n$ 的倍數理想 (The ideal of multiples of $n$) $[n\mathbf{Z} \trianglelefteq \mathbf{Z}]$
  * $a,\ b$ : 整數 (Integers) $[a, b \in \mathbf{Z}]$
  * $n$ : 模數 (Modulus) $[n \in \mathbf{P}]$

* **【定義 1】 環同態 (Ring homomorphism)：** **同時**保住兩個運算

  $$f : \left(R, +, \times\right) \to \left(S, \oplus, \otimes\right) \ \text{為同態} \quad \overset{\text{def}}{\Longleftrightarrow} \quad f\left(a + b\right) = f(a) \oplus f(b), \quad f\left(a \times b\right) = f(a) \otimes f(b)$$

  * $f$ : 兩環之間的映射 (A map between the two rings) $[R \to S]$
  * $R,\ S$ : 兩個環的底層集合 (The underlying sets of two rings) $[\text{集合}]$
  * $a,\ b$ : 環元素 (Ring elements) $[a, b \in R]$
  * 註：**兩條缺一不可**。只保加法的是群同態，不算環同態。
  * 註：本定義**不要求** $f(1_R) = 1_S$。某些教科書會加上這一條（unital homomorphism），
    投影片沒有，本章沿用投影片的寫法。這個差異在【證明 (e)】的零映射上會看得出來。

* **【定義 2】 核 (Kernel)：** 被送到零的元素全體

  $$\ker f \overset{\text{def}}{=} \left\{r \in R \ \middle|\ f(r) = 0_S\right\}$$

  * $\ker f$ : $f$ 的核 (The kernel of $f$) $[\ker f \subseteq R]$
  * $f$ : 環同態 (A ring homomorphism) $[R \to S]$
  * $r$ : 環元素 (A ring element) $[r \in R]$
  * $0_S$ : $S$ 的加法單位元素 (The additive identity of $S$) $[0_S \in S]$
  * 註：投影片 p.41 直接寫「The **ideal** $\ker(f)$」—— 把「是理想」寫進了句子裡。
    【證明 (b)】把這件事證出來。

* **【定義 3】 環同構與自同構 (Ring isomorphism and automorphism)：**

  * (a) 同構：

    $$f \ \text{為同構} \quad \overset{\text{def}}{\Longleftrightarrow} \quad f \ \text{為同態且雙射}$$

  * (b) 自同構：定義域與值域是同一個環的同構：

    $$f \ \text{為自同構} \quad \overset{\text{def}}{\Longleftrightarrow} \quad f : R \to R \ \text{為同構}$$

  * $f$ : 兩環之間的映射 (A map between the two rings) $[R \to S]$
  * $R,\ S$ : 兩個環的底層集合 (The underlying sets of two rings) $[\text{集合}]$

* **【定義 4】 由 $\omega$ 生成的有理數環 (The ring generated by a cube root of unity)：** 【證明 (f)】要用

  $$\mathbf{Q}[\omega] \overset{\text{def}}{=} \left\{a + b\omega \ \middle|\ a, b \in \mathbf{Q}\right\}, \qquad \omega^2 + \omega + 1 = 0$$

  * $\mathbf{Q}[\omega]$ : 由 $\omega$ 生成的環 (The ring generated by $\omega$) $[\text{集合}]$
  * $\omega$ : $x^2+x+1=0$ 的一個根 (A root of $x^2+x+1=0$) $[\omega \in \mathbf{C}]$
  * $a,\ b$ : 有理係數 (Rational coefficients) $[a, b \in \mathbf{Q}]$
  * 註：$\omega = \dfrac{-1 + \sqrt{3}\,i}{2}$ 是一個**三次單位根**（$\omega^3 = 1$ 但 $\omega \neq 1$）。
    關係式 $\omega^2 = -\omega - 1$ 保證乘法封閉 —— 與
    [整環](Integral_Domain.md)【證明 (c)】的 $\left(\sqrt{2}\right)^2 = 2$ 是同一個手法。

+++

## 證明:

### (a) proof of the basic properties of a ring homomorphism

**零對到零。** 起手式取 $f(0)$，利用 $0 + 0 = 0$：

$$\begin{gather*}
f(0) &\overset{\text{已知 1(a)}}{=}& f\left(0 + 0\right) \\
f(0) &\overset{\text{定義 1}}{=}& f(0) \oplus f(0) \\
0_S \oplus f(0) &\overset{\text{已知 1(a)}}{=}& f(0) \oplus f(0) \\
0_S &\overset{\text{已知 2(a)}}{=}& f(0)
\end{gather*}$$

**負號對到負號。** 把 $a + \left(-a\right) = 0$ 整條翻譯過去：

$$\begin{gather*}
f(a) \oplus f\left(-a\right) &\overset{\text{定義 1}}{=}& f\left(a + \left(-a\right)\right) \\
f(a) \oplus f\left(-a\right) &\overset{\text{已知 1(a)}}{=}& f(0) \\
f(a) \oplus f\left(-a\right) &\overset{\text{證明 (a)}}{=}& 0_S \\
f\left(-a\right) &\overset{\text{已知 2(b)}}{=}& -f(a)
\end{gather*}$$

* 註：**這一段只用到【定義 1】的加法那一條** —— 環同態的加法部分就是群同態，
  故論證與 [群同態與群同構](../Group/Group_Homomorphism_and_Isomorphism.md)【證明 (a)】逐字相同。

### (b) proof that the kernel is an ideal

依【已知 3】三條檢查 $\ker f$。

**非空**：

$$\begin{gather*}
f(0) &\overset{\text{證明 (a)}}{=}& 0_S \\
0 &\overset{\text{定義 2}}{\in}& \ker f
\end{gather*}$$

**對減法封閉**：設 $a, b \in \ker f$：

$$\begin{gather*}
f\left(a - b\right) &\overset{\text{定義 1}}{=}& f(a) \oplus f\left(-b\right) \\
f\left(a - b\right) &\overset{\text{證明 (a)}}{=}& f(a) \oplus \left(-f(b)\right) \\
f\left(a - b\right) &\overset{\text{定義 2}}{=}& 0_S \oplus \left(-0_S\right) \\
f\left(a - b\right) &=& 0_S \\
a - b &\overset{\text{定義 2}}{\in}& \ker f
\end{gather*}$$

**吸收性**：設 $a \in \ker f$、$r \in R$ 任意：

$$\begin{gather*}
f\left(ar\right) &\overset{\text{定義 1}}{=}& f(a) \otimes f(r) \\
f\left(ar\right) &\overset{\text{定義 2}}{=}& 0_S \otimes f(r) \\
f\left(ar\right) &\overset{\text{已知 1(b)}}{=}& 0_S \\
ar &\overset{\text{定義 2}}{\in}& \ker f
\end{gather*}$$

三條全中：

$$\begin{gather*}
\ker f &\overset{\text{已知 3}}{\trianglelefteq}& R
\end{gather*}$$

與投影片 p.41 的斷言一致。

* 註：**吸收性那一段是全檔最關鍵的三行。** 它成立的理由是
  [環的基本命題](Ring_Basic_Propositions.md)【證明 (a)】的「$0$ 是乘法的吸收元」——
  $f(a)$ 一旦是 $0_S$，乘上什麼都還是 $0_S$，無論 $r$ 是誰。
  **這正是核比一般子環強、強到成為理想的原因。**

### (c) proof that injectivity is equivalent to a trivial kernel

**($\Rightarrow$)** 設 $f$ 單射。任取 $r \in \ker f$：

$$\begin{gather*}
f(r) &\overset{\text{定義 2}}{=}& 0_S \\
f(0) &\overset{\text{證明 (a)}}{=}& 0_S \\
f(r) &=& f(0) \\
r &\overset{\text{已知 4}}{=}& 0 \\
\ker f &=& \left\{0\right\}
\end{gather*}$$

**($\Leftarrow$)** 設 $\ker f = \left\{0\right\}$。任取 $a, b$ 使 $f(a) = f(b)$：

$$\begin{gather*}
f(a) &=& f(b) \\
f(a) \oplus \left(-f(b)\right) &=& 0_S \\
f\left(a - b\right) &\overset{\text{證明 (a),定義 1}}{=}& 0_S \\
a - b &\overset{\text{定義 2}}{\in}& \ker f \\
a - b &=& 0 \\
a &=& b \\
f &\overset{\text{已知 4}}{=}& \text{單射}
\end{gather*}$$

兩個方向都證完。

* 註：**這條命題把「檢查全體元素對」降成「檢查一個集合」。**
  要驗證 $f$ 單射，樸素做法要掃過所有 $(a,b)$ 對；
  有了本命題只需算出 $\ker f$ 並看它是不是只有 $0$。

### (d) verify that complex conjugation is an automorphism

$f(a + bi) = a - bi$，即 $f(z) = \bar{z}$。

**保加法**：

$$\begin{gather*}
\overline{\left(a+bi\right) + \left(c+di\right)} &=& \overline{\left(a+c\right) + \left(b+d\right)i} \\
&=& \left(a+c\right) - \left(b+d\right)i \\
&=& \left(a - bi\right) + \left(c - di\right) \\
&=& \overline{a+bi} + \overline{c+di}
\end{gather*}$$

**保乘法**由【已知 5】直接給出。**雙射**也由【已知 5】的 $\overline{\bar{z}} = z$ 給出
（$f$ 是自己的反函數）：

$$\begin{gather*}
\overline{zw} &\overset{\text{已知 5}}{=}& \bar{z}\,\bar{w} \\
f \circ f &\overset{\text{已知 5}}{=}& \mathrm{id} \\
f &\overset{\text{定義 3(a)}}{=}& \text{同構} \\
f &\overset{\text{定義 3(b)}}{=}& \text{自同構} \qquad \text{(定義域與值域都是 } \mathbf{C}\text{)}
\end{gather*}$$

與投影片一致。核是：

$$\begin{gather*}
\ker f &\overset{\text{定義 2}}{=}& \left\{z \in \mathbf{C} \ \middle|\ \bar{z} = 0\right\} \\
\ker f &=& \left\{0\right\} \\
f &\overset{\text{證明 (c)}}{=}& \text{單射}
\end{gather*}$$

與雙射的結論一致。

### (e) verify that the zero map is a homomorphism but not an isomorphism

$f : \mathbf{Z} \to \mathbf{Z}$，$f(a) = 0$ 對所有 $a$。

**是同態**（兩條都退化成 $0 = 0 + 0$ 與 $0 = 0 \times 0$）：

$$\begin{gather*}
f\left(a + b\right) &=& 0 \\
f(a) + f(b) &=& 0 + 0 = 0 \\
f\left(a + b\right) &\overset{\text{定義 1}}{=}& f(a) + f(b) \\
f\left(ab\right) &=& 0 \\
f(a) \times f(b) &=& 0 \times 0 = 0 \\
f\left(ab\right) &\overset{\text{定義 1}}{=}& f(a) \times f(b)
\end{gather*}$$

**不是同構**（核太大）：

$$\begin{gather*}
\ker f &\overset{\text{定義 2}}{=}& \mathbf{Z} \\
\ker f &\neq& \left\{0\right\} \\
f &\overset{\text{證明 (c)}}{\neq}& \text{單射} \\
f &\overset{\text{定義 3(a)}}{\neq}& \text{同構}
\end{gather*}$$

與投影片一致。

* 註：零映射**不保乘法單位元素**（$f(1) = 0 \neq 1$）。這正是【定義 1】的第二個註說的差異 ——
  若採 unital 慣例，零映射就不算環同態。投影片採的是不要求的那一版。

### (f) verify the reduction map and the inclusion map

**$f : \mathbf{Z} \to \mathbf{Z}_n$，$f(x) = x \bmod n$。** 保運算由【已知 6】直接給出：

$$\begin{gather*}
f\left(a + b\right) &=& \left(a+b\right) \bmod n \\
f\left(a + b\right) &\overset{\text{已知 6}}{=}& f(a) \oplus f(b) \\
f\left(ab\right) &=& \left(ab\right) \bmod n \\
f\left(ab\right) &\overset{\text{已知 6}}{=}& f(a) \otimes f(b)
\end{gather*}$$

**滿射**（每個 $r \in \left\{0,\dots,n-1\right\}$ 都是 $f(r)$）、**非單射**：

$$\begin{gather*}
\ker f &\overset{\text{定義 2}}{=}& \left\{x \in \mathbf{Z} \ \middle|\ x \bmod n = 0\right\} \\
\ker f &=& n\mathbf{Z} \\
\ker f &\neq& \left\{0\right\} \qquad \text{(} n \ge 2 \text{ 時)} \\
f &\overset{\text{證明 (c)}}{\neq}& \text{單射}
\end{gather*}$$

與投影片的「surjective, but not injective」一致。

**$f : \mathbf{Q}[\omega] \to \mathbf{C}$，$f(x) = x$（嵌入映射）。** 保運算是顯然的（什麼都沒改）：

$$\begin{gather*}
f\left(x + y\right) &=& x + y \\
f\left(x + y\right) &\overset{\text{定義 1}}{=}& f(x) + f(y) \\
f\left(xy\right) &\overset{\text{定義 1}}{=}& f(x)f(y)
\end{gather*}$$

**單射**（核平凡）、**非滿射**：

$$\begin{gather*}
\ker f &\overset{\text{定義 2}}{=}& \left\{x \in \mathbf{Q}[\omega] \ \middle|\ x = 0\right\} = \left\{0\right\} \\
f &\overset{\text{證明 (c)}}{=}& \text{單射} \\
\sqrt{2} &\in& \mathbf{C} \\
\sqrt{2} &\overset{\text{定義 4}}{\notin}& \mathbf{Q}[\omega] \\
f &\overset{\text{已知 4}}{\neq}& \text{滿射}
\end{gather*}$$

與投影片的「injective, but not surjective」一致。

* 註：$\sqrt{2} \notin \mathbf{Q}[\omega]$ 的理由是 $\mathbf{Q}[\omega]$ 是 $\mathbf{Q}$ 上的
  二維向量空間、基底為 $\left\{1, \omega\right\}$，而 $\sqrt{2}$ 無法寫成 $a + b\omega$（$a,b \in \mathbf{Q}$）——
  $\omega$ 的虛部非零而 $\sqrt{2}$ 是實數，故 $b = 0$，但 $\sqrt{2} \notin \mathbf{Q}$。
* 註：**$\ker f = n\mathbf{Z}$ 這件事很重要** ——
  它說明 [商環](Quotient_Ring.md)【證明 (e)】的 $\mathbf{Z}/n\mathbf{Z} \cong \mathbf{Z}_n$
  其實是「$\mathbf{Z}$ 除以 $f$ 的核，同構於 $f$ 的像」的特例。見文末。

+++

## 意義與密碼學關聯 (Interpretation and Relevance to Cryptography)

### 核度量「壓扁了多少」

同態可以把大環壓成小環，而**壓掉的東西恰好就是核**：

| 同態 | 核 | 像 | 壓扁程度 |
|---|---|---|---|
| $z \mapsto \bar{z}$（【證明 (d)】） | $\left\{0\right\}$ | $\mathbf{C}$ | 完全沒壓（同構） |
| $x \mapsto x \bmod n$（【證明 (f)】） | $n\mathbf{Z}$ | $\mathbf{Z}_n$ | 壓成 $n$ 個點 |
| $a \mapsto 0$（【證明 (e)】） | $\mathbf{Z}$ | $\left\{0\right\}$ | 全壓成一點 |

三列的模式很清楚：**核越大，像越小**。這與 [商環](Quotient_Ring.md)【證明 (d)】的
「$I$ 越大、$R/I$ 越小」是同一件事，因為：

$$R/\ker f \ \cong \ \mathrm{im}\, f$$

這是**第一同構定理**（本章不正式證明，但三個例子都符合）。
$\mathbf{Z}/n\mathbf{Z} \cong \mathbf{Z}_n$ 正是它取 $f = \left(\cdot \bmod n\right)$ 的特例。

### 核與理想是同一件事的兩面

【證明 (b)】說「每個核都是理想」。反過來也對：**每個理想都是某個同態的核** ——
取商映射 $\pi : R \to R/I$，$\pi(a) = a + I$，則 $\ker \pi = I$。

$$\left\{\text{理想}\right\} \ = \ \left\{\text{同態的核}\right\}$$

所以 [理想](Ideal.md) 那一整檔可以換個說法：**理想就是「可以被壓掉的部分」**。
吸收性之所以是理想的定義條件，是因為【證明 (b)】的吸收性那三行 ——
$0$ 乘任何東西都是 $0$，這個性質必須被拉回到 $R$ 裡。

### 密碼學上的對應：RSA 就是一連串同態

RSA 的每一步都是環同態：

$$\mathbf{Z} \ \xrightarrow{\ \bmod n\ } \ \mathbf{Z}_n \ \xrightarrow{\ \text{CRT}\ } \ \mathbf{Z}_p \times \mathbf{Z}_q$$

* 第一箭頭是【證明 (f)】的化簡映射，核是 $n\mathbf{Z}$；
* 第二箭頭是 [中國剩餘定理](Chinese_Remainder_Theorem.md) 的同構。

**第二個箭頭在實作上是 RSA 解密加速的關鍵**：在 $\mathbf{Z}_p \times \mathbf{Z}_q$ 裡算
比在 $\mathbf{Z}_n$ 裡快約四倍，因為模數只有一半長。
OpenSSL 的 RSA 私鑰結構裡存的 `p`、`q`、`dp`、`dq`、`qinv` 就是為了走這條路。

**但這也是 fault attack 的入口**：若 CRT 的兩個分支之一算錯，
攻擊者比對正確與錯誤的簽章就能用 $\gcd$ 分解 $n$
（見 [零因子](Zero_Divisor.md) 文末）。這就是著名的 **Bellcore attack**。

### 同態加密：讓核變成零

「同態加密 (Homomorphic Encryption)」這個名詞裡的「同態」就是【定義 1】。
它要求加密函數 $E$ 滿足：

$$E(a) \oplus E(b) = E(a + b), \qquad E(a) \otimes E(b) = E(a \times b)$$

**這樣就能在密文上直接運算，不必解密。** 雲端可以幫你算，卻看不到內容。

* RSA 本身只保乘法（$E(a)E(b) = (ab)^e = E(ab)$）—— 稱為**乘法同態**；
* Paillier 只保加法 —— **加法同態**；
* 兩個都保的是 **全同態加密 (FHE)**，2009 年才由 Gentry 首次構造出來，
  而它用的環正是 [環的例子](Ring_Examples.md) 文末那個
  $\mathbf{Z}_q[x]/\left\langle x^N + 1 \right\rangle$。

**textbook RSA 的乘法同態性其實是個弱點** ——
攻擊者可以把密文 $c$ 乘上 $r^e$ 得到 $E(rm)$，誘騙持有私鑰者解密，再除以 $r$ 還原 $m$。
這是 **chosen-ciphertext attack**，也是為什麼實務上一定要加 OAEP 填充打破同態性。

**同態性在 FHE 裡是功能，在 RSA 裡是漏洞** —— 同一條數學性質，兩種相反的評價。
