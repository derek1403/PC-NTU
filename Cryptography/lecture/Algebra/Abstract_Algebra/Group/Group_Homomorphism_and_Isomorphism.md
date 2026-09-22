# Group Homomorphism and Isomorphism (群同態與群同構)

+++

## 證明目標:

`Algebra.pdf` p.23–24。前面的檔案都在研究**單一個群**；本檔開始研究**群與群之間的關係** ——
哪些群其實是「同一個群穿了不同衣服」。

* (a) 同態的兩條基本性質（投影片未列，但每個後續證明都會用）：

$$f\left(e_G\right) = e_H, \qquad f\left(a^{-1}\right) = f(a)^{-1}$$

* (b) $f : \left(\mathbf{Z}, +\right) \to \left(\mathbf{Z}, +\right)$、$f(1) = 2$ 是同態，**單射但非滿射**。
* (c) $f : \left(\mathbf{Z}, +\right) \to \left(\mathbf{Z}_7^*, \otimes\right)$、$f(1) = 3$ 是同態，**滿射但非單射**。
* (d) $f : \left(\mathbf{C}^*, \times\right) \to \left(\mathbf{C}^*, \times\right)$、$f(a+bi) = a - bi$ 是**同構**。
* (e) $f : \left(\mathbf{Z}_6, \oplus\right) \to \left(\mathbf{Z}_7^*, \otimes\right)$、$f(1) = 3$ 是**同構**：

$$f(0) = 1,\quad f(1) = 3,\quad f(2) = 2,\quad f(3) = 6,\quad f(4) = 4,\quad f(5) = 5$$

* (f) 回答投影片 p.24 最後的兩個問句：$f(1) = 5$ 與 $f(1) = 2$ 各會如何。

* $G,\ H$ : 兩個群的底層集合 (The underlying sets of two groups) $[\text{集合}]$
* $*,\ \bullet$ : $G$ 與 $H$ 的群運算 (The group operations of $G$ and $H$) $[G \times G \to G,\ H \times H \to H]$
* $f$ : 兩群之間的映射 (A map between the two groups) $[G \to H]$
* $a,\ b$ : 群元素 (Group elements) $[a, b \in G]$
* $e_G,\ e_H$ : 兩群各自的單位元素 (The identity elements of the two groups) $[e_G \in G,\ e_H \in H]$
* 註：**同態保運算、同構保一切**。同構的兩個群在群論上是**完全一樣**的東西，
  只是元素的名字不同。(e) 說 $\mathbf{Z}_6$ 與 $\mathbf{Z}_7^*$ 就是這種關係 ——
  一個是加法群、一個是乘法群，卻是同一個群。
* 註：(b)(c) 刻意各缺一半（一個單射不滿射、一個滿射不單射），說明**同態不必是同構**。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [群的公理與冪次記號 (Group axioms and power notation)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Group/Group_Definition.html#definitions-and-notation)：** 已於本章 [群的定義](Group_Definition.md)【定義 2】【定義 3】給出，此處直接引用

  * (a) 單位元素與反元素：

    $$a * e = e * a = a, \qquad a * a^{-1} = a^{-1} * a = e$$

  * (b) 指數律：

    $$g^m * g^n = g^{m+n}, \qquad \left(g^m\right)^n = g^{mn}$$

  * $G$ : 群的底層集合 (The underlying set of the group) $[\text{集合}]$
  * $a$ : 群元素 (A group element) $[a \in G]$
  * $g$ : 群元素 (A group element) $[g \in G]$
  * $m,\ n$ : 冪次 (Exponents) $[m, n \in \mathbf{Z}]$
  * $e$ : 單位元素 (The identity element) $[e \in G]$

* **【已知 2】 [左消去律與反元素唯一 (Left cancellation and uniqueness of the inverse)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Group/Unique_Solution_and_Cancellation_Law.html#a-proof-of-the-left-cancellation-law)：** 已於本章 [唯一解與消去律](Unique_Solution_and_Cancellation_Law.md)【證明 (a)】與 [反元素唯一](Uniqueness_of_Inverse.md)【證明 (a)】完整證明，此處直接引用不再重證

  * (a) 左消去律：

    $$a * b = a * c \quad \Longrightarrow \quad b = c$$

  * (b) 反元素唯一：

    $$g * x = x * g = e \quad \Longrightarrow \quad x = g^{-1}$$

  * $a,\ b,\ c,\ g,\ x$ : 群元素 (Group elements) $[a, b, c, g, x \in G]$
  * $e$ : 單位元素 (The identity element) $[e \in G]$

* **【已知 3】 [單射與滿射的定義 (Definitions of injectivity and surjectivity)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Group/Permutation.html#assumptions-preliminaries)：** 已於本章 [排列](Permutation.md)【定義 1】【定義 2】【定義 3】給出，此處直接引用

  * (a) 單射：

    $$f(x) = f(y) \quad \Longrightarrow \quad x = y$$

  * (b) 滿射：

    $$\forall\, z \in H, \ \exists\, x \in G \ \text{ such that } \ f(x) = z$$

  * (c) 雙射：同時單射與滿射。

    $$f \ \text{雙射} \quad \overset{\text{def}}{\Longleftrightarrow} \quad f \ \text{單射且滿射}$$

  * $f$ : 兩群之間的映射 (A map between the two groups) $[G \to H]$
  * $x,\ y$ : 定義域中的元素 (Elements of the domain) $[x, y \in G]$
  * $z$ : 值域中的元素 (An element of the codomain) $[z \in H]$

* **【已知 4】 [$3$ 是 $\mathbf{Z}_7^*$ 的生成元 (Three generates the units modulo seven)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Group/Cyclic_Group.html#b-proof-that-the-units-modulo-seven-form-a-cyclic-group)：** 已於本章 [循環群](Cyclic_Group.md)【證明 (b)】完整計算並證明，此處直接引用不再重證

  $$3^1 = 3,\quad 3^2 = 2,\quad 3^3 = 6,\quad 3^4 = 4,\quad 3^5 = 5,\quad 3^6 = 1 \qquad \left(\bmod\ 7\right)$$

  * $\mathbf{Z}_7^*$ : 模 $7$ 可逆剩餘類集合 (The set of units modulo 7) $[\text{集合}]$
  * 註：六個值兩兩相異且恰好填滿 $\mathbf{Z}_7^* = \left\{1,2,3,4,5,6\right\}$。

* **【已知 5】 [複數的乘法與共軛 (Multiplication and conjugation of complex numbers)](https://mathworld.wolfram.com/ComplexConjugate.html)：** 標準結果，本章直接引用不再重證

  * (a) 乘法：

    $$\left(a + bi\right)\left(c + di\right) = \left(ac - bd\right) + \left(ad + bc\right)i$$

  * (b) 共軛：

    $$\overline{a + bi} \overset{\text{def}}{=} a - bi$$

  * $a,\ b,\ c,\ d$ : 實部與虛部 (Real and imaginary parts) $[a, b, c, d \in \mathbf{R}]$
  * $i$ : 虛數單位 (Imaginary unit) $[i \in \mathbf{C}]$，$i^2 = -1$

* **【定義 1】 群同態 (Group homomorphism)：** 把 $G$ 的運算「翻譯」成 $H$ 的運算，且翻譯前後結果一致

  $$f : \left(G, *\right) \to \left(H, \bullet\right) \ \text{為同態} \quad \overset{\text{def}}{\Longleftrightarrow} \quad f\left(a * b\right) = f(a) \bullet f(b) \qquad \text{for all } a, b \in G$$

  * $f$ : 兩群之間的映射 (A map between the two groups) $[G \to H]$
  * $G,\ H$ : 兩個群的底層集合 (The underlying sets of two groups) $[\text{集合}]$
  * $*,\ \bullet$ : $G$ 與 $H$ 的群運算 (The group operations of $G$ and $H$) $[G \times G \to G,\ H \times H \to H]$
  * $a,\ b$ : 群元素 (Group elements) $[a, b \in G]$
  * 註：等號**左邊先算 $G$ 的運算再翻譯，右邊先翻譯再算 $H$ 的運算**。
    同態說的就是「這兩條路殊途同歸」。

* **【定義 2】 群同構與同構關係 (Group isomorphism)：** 同態再加上雙射

  * (a) 同構：

    $$f \ \text{為同構} \quad \overset{\text{def}}{\Longleftrightarrow} \quad f \ \text{為同態且 } f \ \text{為雙射}$$

  * (b) 同構關係：

    $$G \cong H \quad \overset{\text{def}}{\Longleftrightarrow} \quad \exists\, f : G \to H \ \text{ 為同構}$$

  * $f$ : 兩群之間的映射 (A map between the two groups) $[G \to H]$
  * $G,\ H$ : 兩個群的底層集合 (The underlying sets of two groups) $[\text{集合}]$
  * $\cong$ : 同構關係 (The isomorphism relation) $[\text{關係}]$
  * 註：同構的兩個群在群論上**完全無法區分** —— 任何用群公理能表述的性質，
    一個有另一個就有（交換性、階、子群結構…）。

* **【定義 3】 由生成元決定的映射 (A map determined by the image of a generator)：** $\left(\mathbf{Z}, +\right)$ 與 $\left(\mathbf{Z}_6, \oplus\right)$ 都由 $1$ 生成（見 [循環群](Cyclic_Group.md)），故指定 $f(1)$ 就決定了整個映射

  $$f(1) = c \quad \Longrightarrow \quad f(x) = c^{x} \ \text{（} H \text{ 為乘法群時）}, \qquad f(x) = xc \ \text{（} H \text{ 為加法群時）}$$

  * $f$ : 兩群之間的映射 (A map between the two groups) $[G \to H]$
  * $c$ : 生成元的像 (The image of the generator) $[c \in H]$
  * $x$ : 定義域中的元素 (An element of the domain) $[x \in G]$
  * 註：投影片全部用「$f(1) = \cdots$」來指定映射，靠的就是這一點。
  * 註：$G = \mathbf{Z}_6$ 時**還需要檢查良定義性** —— $0$ 與 $6$ 在 $\mathbf{Z}_6$ 裡是同一個元素，
    故必須有 $c^0 = c^6$。見【證明 (e)】。

+++

## 證明:

### (a) proof of the basic properties of a homomorphism

**單位元素對到單位元素。** 起手式取 $f\left(e_G\right)$，利用 $e_G * e_G = e_G$：

$$\begin{gather*}
f\left(e_G\right) &\overset{\text{已知 1(a)}}{=}& f\left(e_G * e_G\right) \\
f\left(e_G\right) &\overset{\text{定義 1}}{=}& f\left(e_G\right) \bullet f\left(e_G\right) \\
e_H \bullet f\left(e_G\right) &\overset{\text{已知 1(a)}}{=}& f\left(e_G\right) \bullet f\left(e_G\right) \\
e_H &\overset{\text{已知 2(a)}}{=}& f\left(e_G\right)
\end{gather*}$$

**反元素對到反元素。** 把 $a * a^{-1} = e_G$ 整條翻譯過去：

$$\begin{gather*}
f(a) \bullet f\left(a^{-1}\right) &\overset{\text{定義 1}}{=}& f\left(a * a^{-1}\right) \\
&\overset{\text{已知 1(a)}}{=}& f\left(e_G\right) \\
&\overset{\text{證明 (a)}}{=}& e_H
\end{gather*}$$

同理 $f\left(a^{-1}\right) \bullet f(a) = e_H$，故由反元素唯一：

$$f\left(a^{-1}\right) \overset{\text{已知 2(b)}}{=} f(a)^{-1}$$

* 註：第一段第三行是**刻意把左端寫成 $e_H \bullet f(e_G)$**，
  這樣兩邊才有共同的右因子可以消去。這是消去律的標準用法。

### (b) verify the doubling map on the integers

依【定義 3】，$f(1) = 2$ 在加法群上給出 $f(x) = 2x$。

**同態**：

$$\begin{gather*}
f\left(x + y\right) &\overset{\text{定義 3}}{=}& 2\left(x + y\right) \\
&=& 2x + 2y \\
&\overset{\text{定義 3}}{=}& f(x) + f(y)
\end{gather*}$$

**單射**：

$$\begin{gather*}
f(x) &=& f(y) \\
2x &\overset{\text{定義 3}}{=}& 2y \\
x &=& y
\end{gather*}$$

**非滿射**：$1 \in \mathbf{Z}$ 沒有原像：

$$\begin{gather*}
2x &=& 1 \\
x &=& \frac{1}{2} \\
x &\notin& \mathbf{Z} \\
f &\overset{\text{已知 3(b)}}{\neq}& \text{滿射}
\end{gather*}$$

與投影片的「injective, not surjective」一致。

* 註：像集是 $2\mathbf{Z}$，只佔 $\mathbf{Z}$ 的一半。**無限群才可能發生這種事** ——
  由 [排列](Permutation.md)【證明 (a)】，有限集合上單射必定滿射。

### (c) verify the exponential map from the integers to the units modulo seven

依【定義 3】，$f(1) = 3$ 在乘法群上給出 $f(x) = 3^x \bmod 7$。

**同態**：

$$\begin{gather*}
f\left(x + y\right) &\overset{\text{定義 3}}{=}& 3^{x+y} \\
&\overset{\text{已知 1(b)}}{=}& 3^x \otimes 3^y \\
&\overset{\text{定義 3}}{=}& f(x) \otimes f(y)
\end{gather*}$$

**滿射**：由【已知 4】，$x = 1, \dots, 6$ 的像已經跑遍 $\mathbf{Z}_7^*$ 全部六個元素：

$$\begin{gather*}
\left\{f(1), f(2), f(3), f(4), f(5), f(6)\right\} &\overset{\text{已知 4}}{=}& \left\{3, 2, 6, 4, 5, 1\right\} \\
\left\{f(1), f(2), f(3), f(4), f(5), f(6)\right\} &=& \mathbf{Z}_7^* \\
f &\overset{\text{已知 3(b)}}{=}& \text{滿射}
\end{gather*}$$

**非單射**：$0$ 與 $6$ 這兩個相異的整數有相同的像：

$$\begin{gather*}
f(0) &\overset{\text{定義 3}}{=}& 3^0 = 1 \\
f(6) &\overset{\text{已知 4}}{=}& 3^6 = 1 \\
f(0) = f(6), \quad 0 &\neq& 6 \\
f &\overset{\text{已知 3(a)}}{\neq}& \text{單射}
\end{gather*}$$

與投影片的「surjective, not injective」一致。

### (d) verify that complex conjugation is an isomorphism

$f(a+bi) = a - bi$，即 $f(z) = \bar{z}$。

**同態**（兩邊分別展開，比對實部與虛部）：

$$\begin{gather*}
f\left(\left(a+bi\right)\left(c+di\right)\right) &\overset{\text{已知 5(a)}}{=}& f\left(\left(ac - bd\right) + \left(ad + bc\right)i\right) \\
f\left(\left(a+bi\right)\left(c+di\right)\right) &\overset{\text{已知 5(b)}}{=}& \left(ac - bd\right) - \left(ad + bc\right)i \\
f\left(a+bi\right) \times f\left(c+di\right) &\overset{\text{已知 5(b)}}{=}& \left(a - bi\right)\left(c - di\right) \\
f\left(a+bi\right) \times f\left(c+di\right) &\overset{\text{已知 5(a)}}{=}& \left(ac - bd\right) + \left(-ad - bc\right)i \\
f\left(a+bi\right) \times f\left(c+di\right) &=& \left(ac - bd\right) - \left(ad + bc\right)i
\end{gather*}$$

兩者相同，故 $f$ 是同態。

**雙射**：$f$ 是自己的反函數，故必為雙射：

$$\begin{gather*}
f\left(f\left(a+bi\right)\right) &\overset{\text{已知 5(b)}}{=}& f\left(a - bi\right) \\
f\left(f\left(a+bi\right)\right) &\overset{\text{已知 5(b)}}{=}& a + bi \\
f \circ f &=& \mathrm{id} \\
f &\overset{\text{定義 2}}{=}& \text{同構}
\end{gather*}$$

同態 + 雙射，故 $f$ 是同構。

* 註：定義域與值域是**同一個群**，這種同構稱為**自同構 (automorphism)**（投影片 p.42 的用語）。
* 註：$f \circ f = \mathrm{id}$ 這件事與 [反元素的反元素](Inverse_of_an_Inverse.md) 的對合結構是同一個模式。

### (e) verify the isomorphism from the residues modulo six to the units modulo seven

$f : \mathbf{Z}_6 \to \mathbf{Z}_7^*$、$f(1) = 3$，依【定義 3】即 $f(x) = 3^x \bmod 7$。

**先檢查良定義性**（【定義 3】的註）。$\mathbf{Z}_6$ 裡 $x$ 與 $x + 6$ 是同一個元素，故需要：

$$\begin{gather*}
3^{6} &\overset{\text{已知 4}}{=}& 1 \\
3^{x+6} &\overset{\text{已知 1(b)}}{=}& 3^x \otimes 3^6 \\
3^{x+6} &=& 3^x
\end{gather*}$$

良定義。**列出六個值**（【已知 4】）：

$$\begin{gather*}
f(0) &=& 3^0 = 1 \\
f(1) &\overset{\text{已知 4}}{=}& 3 \\
f(2) &\overset{\text{已知 4}}{=}& 2 \\
f(3) &\overset{\text{已知 4}}{=}& 6 \\
f(4) &\overset{\text{已知 4}}{=}& 4 \\
f(5) &\overset{\text{已知 4}}{=}& 5
\end{gather*}$$

與投影片列出的 $f(2)=2$、$f(3)=6$、$f(4)=4$、$f(5)=5$、$f(0)=1$ 完全一致。

**同態**（與【證明 (c)】同一條鏈，只是指數在 $\mathbf{Z}_6$ 裡運算）：

$$\begin{gather*}
f\left(x \oplus y\right) &\overset{\text{定義 3}}{=}& 3^{\left(x+y\right) \bmod 6} \\
&=& 3^{x+y} \qquad \text{(由良定義性，指數取模不影響值)} \\
&\overset{\text{已知 1(b)}}{=}& 3^x \otimes 3^y \\
&\overset{\text{定義 3}}{=}& f(x) \otimes f(y)
\end{gather*}$$

**雙射**：上面六個值兩兩相異且填滿 $\mathbf{Z}_7^*$：

$$\begin{gather*}
\left\{f(0), \dots, f(5)\right\} &=& \left\{1, 3, 2, 6, 4, 5\right\} \\
\left\{f(0), \dots, f(5)\right\} &=& \mathbf{Z}_7^* \\
\left|\mathbf{Z}_6\right| = \left|\mathbf{Z}_7^*\right| &=& 6
\end{gather*}$$

同態 + 雙射，故 $\left(\mathbf{Z}_6, \oplus\right) \cong \left(\mathbf{Z}_7^*, \otimes\right)$。

* 註：投影片對 $f(0) = 1$ 的解釋是 $f(0) = f(0+0) = f(0) \times f(0)$，
  這正是【證明 (a)】第一段的特例。

### (f) answer the two questions posed in the slides

投影片 p.24 最後問：改成 $f(1) = 5$ 或 $f(1) = 2$ 會如何？兩者的差別**完全取決於該元素的階**
（見 [元素的階與循環子群](Order_of_Element_and_Cyclic_Subgroup.md)）。

**$f(1) = 5$ 的情形。** 先算 $5$ 的冪次：

$$\begin{gather*}
5^1 &=& 5 \\
5^2 &=& 25 \bmod 7 = 4 \\
5^3 &=& 4 \times 5 = 20 \bmod 7 = 6 \\
5^4 &=& 6 \times 5 = 30 \bmod 7 = 2 \\
5^5 &=& 2 \times 5 = 10 \bmod 7 = 3 \\
5^6 &=& 3 \times 5 = 15 \bmod 7 = 1
\end{gather*}$$

六個值 $\left\{5,4,6,2,3,1\right\}$ 兩兩相異、填滿 $\mathbf{Z}_7^*$，且 $5^6 = 1$ 保證良定義。
論證與【證明 (e)】逐字相同：

$$\left(\mathbf{Z}_6, \oplus\right) \cong \left(\mathbf{Z}_7^*, \otimes\right) \qquad \text{（仍是同構）}$$

**$f(1) = 2$ 的情形。** 先算 $2$ 的冪次：

$$\begin{gather*}
2^1 &=& 2 \\
2^2 &=& 4 \\
2^3 &=& 8 \bmod 7 = 1 \\
2^4 &=& 2 \\
2^5 &=& 4 \\
2^6 &=& 1
\end{gather*}$$

$2^6 = 1$，故仍**良定義**、仍是**同態**。但像集只有三個元素：

$$\begin{gather*}
\left\{f(0), \dots, f(5)\right\} &=& \left\{1, 2, 4, 1, 2, 4\right\} \\
\left\{f(0), \dots, f(5)\right\} &=& \left\{1, 2, 4\right\} \\
\left|\left\{1,2,4\right\}\right| = 3 &<& 6 = \left|\mathbf{Z}_7^*\right| \\
f &\overset{\text{已知 3(b)}}{\neq}& \text{滿射} \\
f(0) = f(3) = 1, \quad 0 &\neq& 3 \\
f &\overset{\text{已知 3(a)}}{\neq}& \text{單射}
\end{gather*}$$

**是同態，但不是同構。** 像集 $\left\{1, 2, 4\right\}$ 恰好是 $\langle 2 \rangle$，
$\mathbf{Z}_7^*$ 的一個三階子群（$3 \mid 6$，符合 [拉格朗日定理](Lagrange_Theorem.md)）。

* 註：**判準只有一句話** —— $f(1) = c$ 給出同構，若且唯若 $c$ 是 $\mathbf{Z}_7^*$ 的生成元
  （即 $o(c) = 6$）。$3$ 與 $5$ 是生成元，$2$ 不是（$o(2) = 3$）。
  $\mathbf{Z}_7^*$ 共有 $\varphi(6) = 2$ 個生成元，恰好就是 $3$ 與 $5$。

+++

## 意義與密碼學關聯 (Interpretation and Relevance to Cryptography)

### 同構＝「同一個群，換了名字」

【證明 (e)】說 $\mathbf{Z}_6$ 與 $\mathbf{Z}_7^*$ 同構。這件事很反直覺 ——
一個是**加法**群、一個是**乘法**群，元素也完全不同。但群論看不出差別：

| $\mathbf{Z}_6$（加法） | $\mathbf{Z}_7^*$（乘法） |
|---|---|
| $0$ | $1$ |
| $1$ | $3$ |
| $2$ | $2$ |
| $3$ | $6$ |
| $4$ | $4$ |
| $5$ | $5$ |
| $x \oplus y$ | $f(x) \otimes f(y)$ |

**這張對照表就是一本字典。** 左邊做一次加法，右邊就做一次乘法，結果永遠對得上。

這也解釋了為什麼 [循環群](Cyclic_Group.md) 那麼重要：
**所有 $n$ 階的循環群彼此同構**，全部都是 $\mathbf{Z}_n$ 換了名字。

### 離散對數就是「查這本字典」

上表由左往右查（給 $x$ 求 $3^x$）是**快速冪**，$O(\log x)$。
由右往左查（給 $3^x$ 求 $x$）就是**離散對數問題**。

$$x \ \xrightarrow[\ \text{容易}\ ]{\ f\ } \ 3^x \bmod 7, \qquad 3^x \bmod 7 \ \xrightarrow[\ \text{困難}\ ]{\ f^{-1}\ } \ x$$

同構保證 $f^{-1}$ **存在**（雙射），但**不保證它好算**。
這個「存在卻難算」的落差，就是 Diffie–Hellman 與 ElGamal 的全部安全性來源。

**群論說兩個群一樣，計算複雜度說它們天差地遠** —— 密碼學正是活在這道縫隙裡。

### 【證明 (f)】就是「為什麼要檢查生成元」

投影片那兩個問句的答案，在密碼學裡是一條硬性規定。

$f(1) = 2$ 的情形：像集只有 $\left\{1,2,4\right\}$，**金鑰空間從 $6$ 掉到 $3$**。
在真實的參數規模下，這相當於把 $2048$ 位元的安全性砍到只剩幾位元。

所以 Diffie–Hellman 的參數產生必須驗證 $g$ 的階：

```python
# g 必須是階為 q 的元素（q 為大質數，q | p-1）
assert pow(g, q, p) == 1        # g 的階整除 q
assert g != 1                    # 排除平凡元素
# q 是質數，故 o(g) | q 且 o(g) != 1 ⟹ o(g) == q
```

最後那一行的推理用的正是 [拉格朗日定理](Lagrange_Theorem.md) 與
[元素的階與循環子群](Order_of_Element_and_Cyclic_Subgroup.md)【證明 (b)】。

### 同態的「不完美」也有用

【證明 (b)(c)】的兩個同態都不是同構，但它們並非沒有價值：

* **單射非滿射**（如 $x \mapsto 2x$）—— 這是**嵌入 (embedding)**，
  把一個小群塞進大群裡。橢圓曲線配對 (pairing) 就是把曲線群嵌入有限體的乘法群。
* **滿射非單射**（如 $x \mapsto 3^x \bmod 7$）—— 這是**投影**，
  把大群壓縮成小群，壓縮掉的部分就是**核 (kernel)**。
  雜湊函數的設計精神與此類似。

核的概念在環的版本會正式登場，見 [環同態與核](../Ring/Ring_Homomorphism_and_Kernel.md)。
而 [特殊線性群的指標](Special_Linear_Subgroup_Index.md) 文末提到的
$\det : GL_2 \to \mathbf{Z}_7^*$，正是一個滿射非單射的群同態，核是 $SL_2$。
