# Quotient by an Irreducible Polynomial is a Field (模不可約多項式的商環是體)

+++

## 證明目標:

`Algebra.pdf` p.51（中段）與 p.52。整章的技術高峰 ——
**這是有限體 $GF(p^n)$ 唯一的造法**，也是 AES 的 $GF(2^8)$ 從哪裡來的答案。

* (a) 主定理：

$$p(x) \in F[x] \ \text{不可約} \quad \Longrightarrow \quad F[x] \big/ \left\langle p(x) \right\rangle \ \text{是 } F \text{ 的體擴張}$$

* (b) 擴張次數恰為多項式的次數：

$$\left[\, F[x] \big/ \left\langle p(x) \right\rangle \ : \ F \,\right] = \deg p, \qquad \text{基底} = \left\{1,\ \bar{x},\ \bar{x}^2,\ \dots,\ \bar{x}^{\deg p - 1}\right\}$$

* (c) 投影片 p.52 的三個同構：

$$\mathbf{R}[x] \big/ \left\langle x+1 \right\rangle \cong \mathbf{R} \cong \mathbf{R}[x] \big/ \left\langle x-1 \right\rangle, \qquad \mathbf{R}[x] \big/ \left\langle x^2+1 \right\rangle \cong \mathbf{C}$$

* (d) 投影片 p.52 的 CRT 分解與最後的**不**同構：

$$\mathbf{R}[x] \big/ \left\langle x^2-1 \right\rangle \cong \mathbf{R} \times \mathbf{R}, \qquad \mathbf{C} \ncong \mathbf{R} \times \mathbf{R}$$

* $F$ : 係數所在的體 (The field of coefficients) $[\text{體}]$
* $F[x]$ : 多項式環 (The polynomial ring) $[\text{集合}]$
* $p(x)$ : 不可約多項式 (An irreducible polynomial) $[p(x) \in F[x]]$
* $f,\ g$ : 多項式 (Polynomials) $[f, g \in F[x]]$
* $\bar{x}$ : $x$ 在商環中的同餘類 (The class of $x$ in the quotient) $[\bar{x} \in F[x]/\left\langle p \right\rangle]$
* $\deg p$ : $p$ 的次數 (The degree of $p$) $[\deg p \in \mathbf{P}]$
* 註：**「不可約」在 (a) 裡的地位，完全對應 $\mathbf{Z}_p$ 裡「$p$ 是質數」** ——
  對照 [體的定義](Field_Definition.md)【證明 (b)】，兩條定理的證明骨架逐字平行。
* 註：(d) 的 $x^2 - 1 = \left(x+1\right)\left(x-1\right)$ **可約**，故 (a) 不適用 ——
  商環不是體，而是兩個體的直積（有零因子）。**這個對照是投影片 p.52 的全部重點。**
* 註：(b) 的基底結果是 $GF(2^8)$ 的位元組表示的來源，見文末。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [商環的定義與運算 (Definition and operations of the quotient ring)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Ring/Quotient_Ring.html#c-proof-that-the-quotient-is-a-ring)：** 已於本章 [商環](../Ring/Quotient_Ring.md)【定義 1】【證明 (a)(b)(c)】給出並證明，此處直接引用不再重證

  * (a) 運算：

    $$\left(f + I\right) + \left(g + I\right) = \left(f+g\right) + I, \qquad \left(f + I\right)\left(g + I\right) = fg + I$$

  * (b) 同餘類相等的判別式：

    $$f + I = g + I \quad \Longleftrightarrow \quad f - g \in I$$

  * (c) 商環是交換含單位元環（$F[x]$ 交換含 $1$，逐代表元繼承）：

    $$F[x]/I \ \text{為交換含單位元環}$$

  * $F[x]$ : 多項式環 (The polynomial ring) $[\text{集合}]$
  * $I$ : $F[x]$ 的理想 (An ideal of $F[x]$) $[I \trianglelefteq F[x]]$
  * $f,\ g$ : 多項式 (Polynomials) $[f, g \in F[x]]$

* **【已知 2】 [多項式環是主理想整環 (The polynomial ring over a field is a PID)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Ring/Principal_Ideal.html#c-proof-that-every-ideal-of-the-integers-is-principal)：** 與 [主理想](../Ring/Principal_Ideal.md)【證明 (c)】對 $\mathbf{Z}$ 的論證逐字平行（把「最小正元素」換成「次數最小的非零元素」、「除法原理」換成「多項式除法」），本章直接引用不再重證

  * (a) $F[x]$ 是 PID：

    $$I \trianglelefteq F[x] \quad \Longrightarrow \quad I = \left\langle d(x) \right\rangle \ \text{ for some } d(x) \in F[x]$$

  * (b) 多項式版的貝祖等式：

    $$\left\langle f, g \right\rangle = \left\langle \gcd(f, g) \right\rangle, \qquad \exists\, u, v \in F[x] \ \text{ with } \ uf + vg = \gcd(f, g)$$

  * (c) 多項式除法：

    $$\forall\, f, d \in F[x],\ d \neq 0, \ \exists\, q, r \ \text{ with } \ f = qd + r,\ \deg r < \deg d \ \text{（或 } r = 0\text{）}$$

  * $F[x]$ : 多項式環 (The polynomial ring) $[\text{集合}]$
  * $I$ : $F[x]$ 的理想 (An ideal) $[I \trianglelefteq F[x]]$
  * $f,\ g,\ d,\ u,\ v,\ q,\ r$ : 多項式 (Polynomials) $[\in F[x]]$
  * $\gcd$ : 最大公因式 (The greatest common divisor) $[F[x] \times F[x] \to F[x]]$
  * 註：(c) 成立的**唯一前提是 $F$ 為體** —— 除法要把除數的首項係數約掉，需要它可逆。
    這就是 [$\mathbf{Z}[x]$ 中的非主理想](../Ring/Non_Principal_Ideal_in_Z_x.md) 文末說的分水嶺。

* **【已知 3】 [不可約多項式的定義 (Definition of an irreducible polynomial)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Field/Irreducible_Polynomial.html#assumptions-preliminaries)：** 已於本章 [不可約多項式](Irreducible_Polynomial.md)【定義 1】給出，此處直接引用

  $$p \ \text{不可約} \quad \Longleftrightarrow \quad \deg p \ge 1 \ \text{ 且 } \ \left[\, p = gh \Longrightarrow \deg g = 0 \ \text{或} \ \deg h = 0 \,\right]$$

  * $p$ : 被檢查的多項式 (The polynomial under test) $[p \in F[x]]$
  * $g,\ h$ : 因式 (Factors) $[g, h \in F[x]]$
  * $F$ : 係數所在的體 (The field of coefficients) $[\text{體}]$

* **【已知 4】 [體的定義與體擴張 (Field definition and field extension)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Field/Subfield_and_Field_Extension.html#assumptions-preliminaries)：** 已於本章 [體的定義](Field_Definition.md)【定義 1】與 [子體與體擴張](Subfield_and_Field_Extension.md)【定義 1】【定義 2】給出，此處直接引用

  * (a) 體：

    $$F \ \text{為體} \Leftrightarrow F \ \text{為交換含單位元環且每個非零元素可逆}$$

  * (b) 體擴張與次數：

    $$L : K \Leftrightarrow K \ \text{是 } L \text{ 的子體}, \qquad \left[L : K\right] = \dim_K L$$

  * $F,\ K,\ L$ : 體 (Fields) $[\text{集合}]$

* **【已知 5】 [環同態、核與中國剩餘定理 (Ring homomorphisms, kernels, and the CRT)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Ring/Chinese_Remainder_Theorem.html#c-proof-of-surjectivity-and-the-isomorphism)：** 已於本章 [環同態與核](../Ring/Ring_Homomorphism_and_Kernel.md) 與 [中國剩餘定理](../Ring/Chinese_Remainder_Theorem.md)【證明 (c)】給出並證明，此處直接引用不再重證

  * (a) 第一同構定理（滿射同態誘導的同構）：

    $$f : R \to S \ \text{滿射同態} \quad \Longrightarrow \quad R/\ker f \cong S$$

  * (b) 中國剩餘定理：

    $$I_1 + I_2 = R \quad \Longrightarrow \quad R\big/\left(I_1 \cap I_2\right) \cong R/I_1 \times R/I_2$$

  * (c) 直積有零因子：

    $$\left(1, 0\right)\left(0, 1\right) = \left(0, 0\right)$$

  * $R,\ S$ : 環 (Rings) $[\text{集合}]$
  * $f$ : 環同態 (A ring homomorphism) $[R \to S]$
  * $I_1,\ I_2$ : 互質的理想 (Comaximal ideals) $[I_1, I_2 \trianglelefteq R]$
  * 註：(a) 在 [環同態與核](../Ring/Ring_Homomorphism_and_Kernel.md) 文末以三個例子說明，
    本章不正式證明，但它的內容就是「把核壓掉之後，剩下的與像同構」，
    與 [中國剩餘定理](../Ring/Chinese_Remainder_Theorem.md)【證明 (c)】最後一段的手法相同。

* **【已知 6】 [體必為整環 (Every field is an integral domain)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Field/Field_Definition.html#d-proof-that-every-field-is-an-integral-domain)：** 已於本章 [體的定義](Field_Definition.md)【證明 (d)】完整證明，此處直接引用不再重證

  $$F \ \text{為體} \quad \Longrightarrow \quad F \ \text{無零因子}$$

  * $F$ : 體的底層集合 (The underlying set of the field) $[\text{集合}]$

* **【定義 1】 商環中的元素記號 (Notation for elements of the quotient)：**

  $$\bar{f} \overset{\text{def}}{=} f + \left\langle p(x) \right\rangle, \qquad \bar{x} \overset{\text{def}}{=} x + \left\langle p(x) \right\rangle$$

  * $\bar{f}$ : $f$ 的同餘類 (The class of $f$) $[\bar{f} \in F[x]/\left\langle p \right\rangle]$
  * $\bar{x}$ : $x$ 的同餘類 (The class of $x$) $[\bar{x} \in F[x]/\left\langle p \right\rangle]$
  * $p(x)$ : 不可約多項式 (An irreducible polynomial) $[p(x) \in F[x]]$
  * 註：$\bar{x}$ 是商環裡的一個**具體元素**，而且它滿足 $p\!\left(\bar{x}\right) = \bar{0}$ ——
    換句話說，**商環裡自動長出了 $p$ 的一個根**。這是整個構造的精神。

* **【假設 1】 非零同餘類 (A non-zero class)：** 【證明 (a)】的出發點

  $$\bar{f} \neq \bar{0}, \qquad \text{即} \qquad p \nmid f$$

  * $\bar{f}$ : 一個非零同餘類 (A non-zero class) $[\bar{f} \in F[x]/\left\langle p \right\rangle]$
  * $f,\ p$ : 多項式 (Polynomials) $[f, p \in F[x]]$
  * 註：「$\bar{f} = \bar{0}$」依【已知 1(b)】等價於 $f - 0 = f \in \left\langle p \right\rangle$，
    即 $p \mid f$。取否定即得本假設的第二個寫法。

* **【推導 1】 不可約多項式與不整除它的多項式互質 (An irreducible polynomial is coprime to anything it does not divide)：** 【證明 (a)】要用

  $$\begin{gather*}
  d &\overset{\text{已知 2(b)}}{=}& \gcd(p, f) \\
  d &\mid& p \\
  \deg d = 0 \ \text{ 或 } \ d = cp &\overset{\text{已知 3}}{\ } & \text{（} c \ \text{為非零常數，因 } p \ \text{不可約）} \\
  d = cp &\Longrightarrow& p \mid f \\
  p &\overset{\text{假設 1}}{\nmid}& f \\
  \deg d &=& 0 \\
  \gcd(p, f) &=& 1 \qquad \text{（可取首一，即常數 } 1\text{）}
  \end{gather*}$$

  * $p$ : 不可約多項式 (An irreducible polynomial) $[p \in F[x]]$
  * $f$ : 不被 $p$ 整除的多項式 (A polynomial not divisible by $p$) $[f \in F[x]]$
  * $d$ : 最大公因式 (The greatest common divisor) $[d \in F[x]]$
  * $c$ : 非零常數 (A non-zero constant) $[c \in F \setminus \left\{0\right\}]$
  * 註：第三行是不可約性的直接內容 —— $p$ 的因式只有常數與 $p$ 的常數倍兩種。
  * 註：這完全對應到整數的情形：**質數 $p$ 與任何不被它整除的數互質**。

* **【推導 2】 每個同餘類有唯一的低次代表元 (Each class has a unique low-degree representative)：** 【證明 (b)】要用

  $$\begin{gather*}
  f &\overset{\text{已知 2(c)}}{=}& q\,p + r \qquad \text{with } \deg r < \deg p \ \text{或} \ r = 0 \\
  f - r &=& q\,p \in \left\langle p \right\rangle \\
  \bar{f} &\overset{\text{已知 1(b)}}{=}& \bar{r} \\
  \bar{r_1} = \bar{r_2},\ \deg r_i < \deg p &\overset{\text{已知 1(b)}}{\Longrightarrow}& p \mid \left(r_1 - r_2\right) \\
  \deg\left(r_1 - r_2\right) &<& \deg p \\
  r_1 - r_2 &=& 0
  \end{gather*}$$

  * $f$ : 任意多項式 (An arbitrary polynomial) $[f \in F[x]]$
  * $q,\ r,\ r_1,\ r_2$ : 商與餘式 (Quotients and remainders) $[\in F[x]]$
  * $p$ : 不可約多項式 (An irreducible polynomial) $[p \in F[x]]$
  * 註：前三行是**存在性**（每個類都有次數 $< \deg p$ 的代表元），
    後三行是**唯一性**（次數比 $\deg p$ 小又被 $p$ 整除，只能是零多項式）。
  * 註：這與 $\mathbf{Z}/n\mathbf{Z}$ 的「每個類唯一對應 $0$ 到 $n-1$ 的餘數」逐字平行
    （[商環](../Ring/Quotient_Ring.md)【證明 (e)】）。

+++

## 證明:

### (a) proof that the quotient by an irreducible polynomial is a field

由【已知 1(c)】，$F[x]/\left\langle p \right\rangle$ 已經是交換含單位元環。
依【已知 4(a)】只需補上「非零元素可逆」。

取任意 $\bar{f} \neq \bar{0}$（【假設 1】）。由【推導 1】，$\gcd(p, f) = 1$，
套多項式版的貝祖等式：

$$\begin{gather*}
\gcd(p, f) &\overset{\text{推導 1}}{=}& 1 \\
\exists\, u, v \in F[x] \ \text{ with } \ uf + vp &\overset{\text{已知 2(b)}}{=}& 1
\end{gather*}$$

把這條等式整個取同餘類，$vp$ 那一項落在理想裡故歸零：

$$\begin{gather*}
\overline{uf + vp} &=& \bar{1} \\
\bar{u}\,\bar{f} + \bar{v}\,\bar{p} &\overset{\text{已知 1(a)}}{=}& \bar{1} \\
\bar{p} &\overset{\text{已知 1(b)}}{=}& \bar{0} \qquad \text{(因 } p \in \left\langle p \right\rangle\text{)} \\
\bar{u}\,\bar{f} &=& \bar{1} \\
\bar{f}^{-1} &\overset{\text{已知 4(a)}}{=}& \bar{u}
\end{gather*}$$

每個非零類都可逆，故商環是體：

$$F[x] \big/ \left\langle p(x) \right\rangle \overset{\text{已知 4(a)}}{=} \text{體}$$

**再確認它是 $F$ 的擴張。** 常數多項式的同餘類構成一份 $F$ 的複本：

$$\begin{gather*}
\iota : F \to F[x]/\left\langle p \right\rangle, \qquad \iota(c) &\overset{\text{定義 1}}{=}& \bar{c} \\
\bar{c_1} = \bar{c_2} &\overset{\text{已知 1(b)}}{\Longrightarrow}& p \mid \left(c_1 - c_2\right) \\
\deg\left(c_1 - c_2\right) \le 0 < \deg p &\Longrightarrow& c_1 - c_2 = 0 \\
\iota &\overset{\text{已知 5(a)}}{=}& \text{單射同態}
\end{gather*}$$

故 $F$ 嵌入商環成為子體，依【已知 4(b)】：

$$F[x] \big/ \left\langle p(x) \right\rangle \ : \ F \quad \text{是體擴張}$$

與投影片 p.51 的「then $F[x]/\left\langle p(x) \right\rangle$ is a field extension of $F$」一致。

* 註：**本證明與 [體的定義](Field_Definition.md)【證明 (b)】（$\mathbf{Z}_p$ 是體）逐字平行**：
  那裡用整數的貝祖等式、這裡用多項式的；那裡靠 $p$ 是質數、這裡靠 $p$ 不可約。
  **兩條定理其實是同一條定理在兩個 PID 上的實例。**
* 註：$p$ 不可約這個前提用在**唯一的一個地方** ——【推導 1】的 $\gcd(p,f) = 1$。
  $p$ 可約時會有 $f$ 使 $\gcd(p,f) \neq 1$（取 $p$ 的一個真因式），那個 $\bar{f}$ 就不可逆，
  而且它會是零因子，見【證明 (d)】。

### (b) proof of the degree of the extension

由【推導 2】，每個同餘類恰好對應一個次數 $< \deg p$ 的多項式。
設 $n = \deg p$，宣稱 $\left\{\bar{1}, \bar{x}, \dots, \bar{x}^{\,n-1}\right\}$ 是基底。

**生成**：任取 $\bar{f}$，取其低次代表元 $r = c_0 + c_1x + \cdots + c_{n-1}x^{n-1}$：

$$\begin{gather*}
\bar{f} &\overset{\text{推導 2}}{=}& \bar{r} \\
\bar{f} &\overset{\text{已知 1(a)}}{=}& \bar{c_0} + \bar{c_1}\bar{x} + \cdots + \bar{c_{n-1}}\bar{x}^{\,n-1}
\end{gather*}$$

**線性獨立**：設 $F$-係數組合為零：

$$\begin{gather*}
\bar{c_0} + \bar{c_1}\bar{x} + \cdots + \bar{c_{n-1}}\bar{x}^{\,n-1} &=& \bar{0} \\
\overline{c_0 + c_1 x + \cdots + c_{n-1}x^{n-1}} &\overset{\text{已知 1(a)}}{=}& \bar{0} \\
c_0 + c_1 x + \cdots + c_{n-1}x^{n-1} &\overset{\text{推導 2}}{=}& 0 \qquad \text{(唯一性)} \\
c_0 = c_1 = \cdots = c_{n-1} &=& 0
\end{gather*}$$

故它是基底，元素個數為 $n$：

$$\left[\, F[x] \big/ \left\langle p \right\rangle \ : \ F \,\right] \overset{\text{已知 4(b)}}{=} n = \deg p$$

* 註：由 [子體與體擴張](Subfield_and_Field_Extension.md) 文末的計數，
  $F$ 有限時商環的元素個數是 $\left|F\right|^{\deg p}$ ——
  **取 $F = \mathbf{Z}_2$、$\deg p = 8$ 就得到 $2^8 = 256$ 個元素的 $GF(2^8)$。**

### (c) verify the three isomorphisms from the slides

**$\mathbf{R}[x]/\left\langle x+1 \right\rangle \cong \mathbf{R}$。** 用「代入 $x = -1$」的求值映射：

$$\begin{gather*}
\varepsilon_{-1} : \mathbf{R}[x] \to \mathbf{R}, \qquad \varepsilon_{-1}(f) &\overset{\text{let}}{=}& f(-1) \\
\varepsilon_{-1}\left(f + g\right) = f(-1) + g(-1) &=& \varepsilon_{-1}(f) + \varepsilon_{-1}(g) \\
\varepsilon_{-1}\left(fg\right) = f(-1)g(-1) &=& \varepsilon_{-1}(f)\,\varepsilon_{-1}(g) \\
\varepsilon_{-1} &=& \text{滿射同態（常數多項式打到每個實數）} \\
\ker \varepsilon_{-1} &=& \left\{f \ \middle|\ f(-1) = 0\right\} = \left\langle x+1 \right\rangle \qquad \text{(因式定理)} \\
\mathbf{R}[x]\big/\left\langle x+1 \right\rangle &\overset{\text{已知 5(a)}}{\cong}& \mathbf{R}
\end{gather*}$$

$\mathbf{R}[x]/\left\langle x-1 \right\rangle \cong \mathbf{R}$ 同理（改用 $\varepsilon_{1}$）。
與投影片一致。

**$\mathbf{R}[x]/\left\langle x^2+1 \right\rangle \cong \mathbf{C}$。** 用「代入 $x = i$」：

$$\begin{gather*}
\varepsilon_{i} : \mathbf{R}[x] \to \mathbf{C}, \qquad \varepsilon_{i}(f) &\overset{\text{let}}{=}& f(i) \\
\varepsilon_{i}\left(a + bx\right) &=& a + bi \\
\varepsilon_{i} &=& \text{滿射（一次多項式已打到全部複數）} \\
\ker \varepsilon_{i} &=& \left\{f \ \middle|\ f(i) = 0\right\} = \left\langle x^2+1 \right\rangle \\
\mathbf{R}[x]\big/\left\langle x^2+1 \right\rangle &\overset{\text{已知 5(a)}}{\cong}& \mathbf{C}
\end{gather*}$$

與投影片一致。另外由【證明 (a)(b)】直接印證：
$x^2+1$ 在 $\mathbf{R}[x]$ 中不可約（[不可約多項式](Irreducible_Polynomial.md)【證明 (b)】的註），
故商環是體，次數為 $2$ —— 恰好是 $\left[\mathbf{C} : \mathbf{R}\right] = 2$
（[子體與體擴張](Subfield_and_Field_Extension.md)【證明 (d)】）。

* 註：$\ker \varepsilon_i = \left\langle x^2+1 \right\rangle$ 的理由：
  $f$ 是實係數多項式且 $f(i) = 0$，則共軛也給出 $f(-i) = 0$，
  故 $\left(x-i\right)\left(x+i\right) = x^2+1$ 整除 $f$。
* 註：**$\bar{x}$ 扮演的角色就是 $i$** —— 由【定義 1】的註，
  商環裡 $\bar{x}^2 + \bar{1} = \bar{0}$，即 $\bar{x}^2 = -\bar{1}$。
  **「虛數單位」不是憑空發明的，它是 $x^2+1$ 在商環裡長出來的根。**

### (d) proof of the product decomposition and the non-isomorphism

**先用中國剩餘定理拆開。** $x^2 - 1 = \left(x+1\right)\left(x-1\right)$，兩個因式互質：

$$\begin{gather*}
\gcd\left(x+1,\ x-1\right) &=& 1 \qquad \text{(因 } \tfrac{1}{2}\left[\left(x+1\right) - \left(x-1\right)\right] = 1\text{)} \\
\left\langle x+1 \right\rangle + \left\langle x-1 \right\rangle &\overset{\text{已知 2(b)}}{=}& \mathbf{R}[x] \\
\left\langle x+1 \right\rangle \cap \left\langle x-1 \right\rangle &=& \left\langle x^2-1 \right\rangle \\
\mathbf{R}[x]\big/\left\langle x^2-1 \right\rangle &\overset{\text{已知 5(b)}}{\cong}& \mathbf{R}[x]\big/\left\langle x+1 \right\rangle \times \mathbf{R}[x]\big/\left\langle x-1 \right\rangle \\
\mathbf{R}[x]\big/\left\langle x^2-1 \right\rangle &\overset{\text{證明 (c)}}{\cong}& \mathbf{R} \times \mathbf{R}
\end{gather*}$$

與投影片一致。

**再證 $\mathbf{C} \ncong \mathbf{R} \times \mathbf{R}$。** 兩者作為 $\mathbf{R}$-向量空間都是二維，
但代數結構天差地別 —— 直積有零因子、體沒有：

$$\begin{gather*}
\left(1, 0\right)\left(0, 1\right) &\overset{\text{已知 5(c)}}{=}& \left(0, 0\right) \\
\left(1,0\right) \neq \left(0,0\right), \quad \left(0,1\right) &\neq& \left(0,0\right) \\
\mathbf{R} \times \mathbf{R} &=& \text{有零因子} \\
\mathbf{C} &\overset{\text{已知 6}}{=}& \text{無零因子} \\
\mathbf{C} &\ncong& \mathbf{R} \times \mathbf{R}
\end{gather*}$$

與投影片的「$\mathbf{C} \ncong \mathbf{R} \times \mathbf{R}$ since $\mathbf{R} \times \mathbf{R}$ has zero divisors」一致。

* 註：**這組對照是整頁投影片的重點**。同樣是「$\mathbf{R}[x]$ 模一個二次多項式」：
  * $x^2 + 1$ **不可約** $\Rightarrow$ 商環是**體** $\mathbf{C}$；
  * $x^2 - 1$ **可約** $\Rightarrow$ 商環不是體，而是直積 $\mathbf{R} \times \mathbf{R}$（有零因子）。

  **可約性直接決定了商環是不是體。**
* 註：同構會保持「有沒有零因子」這個性質（同構是雙射同態，零因子會被對應到零因子），
  所以兩者不可能同構 —— 儘管它們的**加法群**結構完全相同（都是 $\mathbf{R}^2$）。

+++

## 意義與密碼學關聯 (Interpretation and Relevance to Cryptography)

### 整數與多項式的完整對照表

本檔完成了貫穿環論與體論的那張對照表：

| 整數 $\mathbf{Z}$ | 多項式 $F[x]$ |
|---|---|
| 質數 $p$ | 不可約多項式 $p(x)$ |
| $p$ 為質數 $\Rightarrow$ $\mathbf{Z}/\left\langle p \right\rangle$ 是體 | $p(x)$ 不可約 $\Rightarrow$ $F[x]/\left\langle p(x) \right\rangle$ 是體 |
| $n$ 為合數 $\Rightarrow$ $\mathbf{Z}_n$ 有零因子 | $p(x)$ 可約 $\Rightarrow$ 商環有零因子 |
| $\left\|\mathbf{Z}_p\right\| = p$ | $\left\|F[x]/\left\langle p \right\rangle\right\| = \left\|F\right\|^{\deg p}$ |
| CRT：$n = ab$、$\gcd(a,b)=1$ | CRT：$p = gh$、$\gcd(g,h)=1$ |

**左右兩欄的每一條定理都有相同的證明**，因為 $\mathbf{Z}$ 與 $F[x]$ 都是 PID。
這是抽象代數「一次證明、處處適用」的最佳示範。

### $GF(2^8)$ 終於造出來了

AES 的位元組體：

$$GF(2^8) = \mathbf{Z}_2[x] \big/ \left\langle x^8 + x^4 + x^3 + x + 1 \right\rangle$$

由本檔的三條結論：

1. **【證明 (a)】** 生成多項式不可約（[不可約多項式](Irreducible_Polynomial.md) 文末）$\Rightarrow$ 商環是**體**，
   每個非零元素可逆 $\Rightarrow$ **S-box 的「取反元素」有定義**；
2. **【證明 (b)】** 基底是 $\left\{1, \bar{x}, \dots, \bar{x}^7\right\}$，共 $8$ 維 $\Rightarrow$
   每個元素是 $8$ 個 $GF(2)$ 座標 $\Rightarrow$ **恰好一個位元組**；
3. **【推導 2】** 每個元素有唯一的低次代表元 $\Rightarrow$ **位元組與元素一一對應**，
   運算是「多項式乘法後模 $\texttt{0x11B}$」。

**三條加起來，就是 AES 規格書裡那幾行「$GF(2^8)$ 算術」的全部數學內容。**

### 求乘法反元素：S-box 第一步的演算法

【證明 (a)】不只證明反元素存在，**它還給了演算法** ——
貝祖等式 $uf + vp = 1$ 裡的 $u$ 就是 $\bar{f}^{-1}$。
求 $u$ 的方法是**擴展歐幾里得演算法**，與求整數模逆元完全相同：

```python
def gf256_inverse(a, modulus=0x11B):
    """GF(2^8) 中求乘法反元素：證明 (a) 的貝祖等式。"""
    if a == 0:
        return 0                       # 0 沒有反元素，S-box 約定映到 0
    r0, r1 = modulus, a
    u0, u1 = 0, 1
    while r1 != 1:
        q = gf_divmod(r0, r1)[0]       # 二元多項式除法
        r0, r1 = r1, r0 ^ gf_mul(q, r1)
        u0, u1 = u1, u0 ^ gf_mul(q, u1)
    return u1
```

這就是 AES S-box 的第一步（第二步是
[一般線性群的階](../Group/General_Linear_Group_Order.md) 文末那個仿射變換）。
實務上會預先算好 $256$ 個值存成查表，但**表的內容就是這段程式算出來的**。

### 可約多項式的陷阱

【證明 (d)】的對照有一個真實的工程後果。若有人不小心選了**可約**的多項式當模數：

$$\mathbf{Z}_2[x] \big/ \left\langle x^8 + x^4 + x^3 + x + 1 \right\rangle \quad \text{vs} \quad \mathbf{Z}_2[x] \big/ \left\langle x^8 + x^7 + x^6 + x^4 + x^2 + x + 1 \right\rangle$$

後者若可約，商環就有零因子 —— **某些位元組會沒有反元素，S-box 就建不起來**，
而且會有一整批輸入被映到同一個輸出，加密不可逆。

這不是假想的風險：設計新的分組密碼時，生成多項式的不可約性**必須驗證**，
不能憑感覺挑。驗證方法見 [不可約多項式](Irreducible_Polynomial.md) 文末的 Rabin 測試。

### Kyber 為什麼刻意選可約的多項式

有趣的反轉：後量子標準 **Kyber 用的 $x^{256}+1$ 在 $\mathbf{Z}_{3329}$ 上是可約的** ——
它刻意選擇這樣，好讓【證明 (d)】的 CRT 分解成立：

$$\mathbf{Z}_q[x]\big/\left\langle x^{256}+1 \right\rangle \cong \prod_{i=1}^{128}\mathbf{Z}_q[x]\big/\left\langle f_i \right\rangle$$

拆得越細，NTT 越快。**Kyber 要的是速度不是體結構** ——
它的安全性來自格問題，不需要每個元素都可逆。

$$\text{AES：要體} \ \Rightarrow \ \text{選不可約}, \qquad \text{Kyber：要速度} \ \Rightarrow \ \text{選可約}$$

**同一條定理，兩個相反的設計選擇。** 這大概是本章最能說明「懂數學才知道怎麼選參數」的例子。
