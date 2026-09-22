# Subgroup Examples (子群的例子)

+++

## 證明目標:

`Algebra.pdf` p.18（上半）與 p.21。把 [子群判別法](Subgroup_Criterion.md) 實際操作六次，
每次只檢查三個條件（非空、乘法封閉、取反元素封閉）。

* (a) $5\mathbf{Z} \le \left(\mathbf{Z}, +\right)$
* (b) $\mathbf{Q}^* \le \left(\mathbf{R}^*, \times\right)$
* (c) $\left\{e, \left(123\right), \left(132\right)\right\} \le S_3$，且 $3 \mid 6$
* (d) $\left\{1, 8\right\} \le \left(\mathbf{Z}_9^*, \otimes\right)$，且 $2 \mid 6$
* (e) $SL_2(\mathbf{Z}_7) \le GL_2(\mathbf{Z}_7)$
* (f) $T_2(\mathbf{Z}_7) \le GL_2(\mathbf{Z}_7)$，且

$$\left|T_2(\mathbf{Z}_7)\right| = 6 \times 6 \times 7 = 252$$

* $G$ : 母群的底層集合 (The underlying set of the ambient group) $[\text{集合}]$
* $H$ : $G$ 的子集 (A subset of $G$) $[H \subseteq G]$
* $S_3$ : $3$ 次對稱群 (The symmetric group on three letters) $[\text{集合}]$
* $\mathbf{Z}_9^*$ : 模 $9$ 可逆剩餘類集合 (The set of units modulo 9) $[\text{集合}]$
* $GL_2(\mathbf{Z}_7),\ SL_2(\mathbf{Z}_7)$ : 一般線性群與特殊線性群 (General and special linear groups) $[\text{集合}]$
* $T_2(\mathbf{Z}_7)$ : 可逆上三角矩陣群 (The group of invertible upper-triangular matrices) $[\text{集合}]$
* 註：(c)(d) 特別標出了整除關係 $3 \mid 6$、$2 \mid 6$ —— 這不是巧合，
  而是 [拉格朗日定理](Lagrange_Theorem.md) 的預告。本檔**先觀察現象，不證明它**。
* 註：(e)(f) 的 $\left|SL_2(\mathbf{Z}_7)\right|$ 要用陪集才算得出來，留到
  [特殊線性群的指標](Special_Linear_Subgroup_Index.md)。(f) 的階則可以直接數，見【證明 (f)】。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [子群判別法 (Subgroup criterion)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Group/Subgroup_Criterion.html#b-proof-of-the-backward-direction)：** 已於本章 [子群判別法](Subgroup_Criterion.md)【證明 (b)】完整證明，此處直接引用不再重證

  * (a) 非空：

    $$H \neq \varnothing$$

  * (b) 對運算封閉：

    $$a * b \in H \qquad \text{for all } a, b \in H$$

  * (c) 對取反元素封閉：

    $$a^{-1} \in H \qquad \text{for all } a \in H$$

  * $H$ : $G$ 的子集 (A subset of $G$) $[H \subseteq G]$
  * $G$ : 母群的底層集合 (The underlying set of the ambient group) $[\text{集合}]$
  * $a,\ b$ : 子集中的元素 (Elements of the subset) $[a, b \in H]$
  * 註：三條同時成立 $\Leftrightarrow$ $H \le G$。本檔每個例子都照這三條依序檢查。

* **【已知 2】 [行列式的乘法性 (Multiplicativity of the determinant)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Number_Sets_and_Notation.html#assumptions-preliminaries)：** 已於本章 [數系與符號約定](../Number_Sets_and_Notation.md)【已知 4】引用，此處再次引用

  $$\det\left(AB\right) = \det\left(A\right)\det\left(B\right)$$

  * $A,\ B$ : 方陣 (Square matrices) $[A, B \in M_n(R)]$
  * $\det$ : 行列式 (Determinant) $[M_n(R) \to R]$
  * $R$ : 係數所在的環 (The coefficient ring) $[\text{環}]$

* **【已知 3】 [線性群的定義 (Definitions of the linear groups)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Number_Sets_and_Notation.html#definitions-and-notation)：** 已於本章 [數系與符號約定](../Number_Sets_and_Notation.md)【定義 6】【定義 7】給出，此處直接引用

  $$GL_n(R) = \left\{A \ \middle|\ \det A \ \text{可逆}\right\}, \qquad SL_n(R) = \left\{A \in GL_n(R) \ \middle|\ \det A = 1\right\}$$

  * $GL_n(R),\ SL_n(R)$ : 一般線性群與特殊線性群 (General and special linear groups) $[\text{集合}]$
  * $A$ : 一個方陣 (A square matrix) $[A \in M_n(R)]$
  * $R$ : 係數所在的環 (The coefficient ring) $[\text{環}]$
  * $\det$ : 行列式 (Determinant) $[M_n(R) \to R]$

* **【已知 4】 [對稱群 $S_3$ 的元素與循環記號 (Elements of $S_3$ in cycle notation)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Group/Symmetric_Group.html#c-verify-the-composition-and-the-inverse-in-the-symmetric-group-on-three-letters)：** 已於本章 [對稱群](Symmetric_Group.md)【證明 (c)】列出並驗證，此處直接引用不再重證

  * (a) 六個元素與階：

    $$S_3 = \left\{e,\ \left(12\right),\ \left(13\right),\ \left(23\right),\ \left(123\right),\ \left(132\right)\right\}, \qquad \left|S_3\right| = 6$$

  * (b) 已驗證的兩個計算：

    $$\left(123\right) \circ \left(123\right) = \left(132\right), \qquad \left(123\right)^{-1} = \left(132\right)$$

  * $S_3$ : $3$ 次對稱群 (The symmetric group on three letters) $[\text{集合}]$
  * $e$ : 恆等排列 (The identity permutation) $[e \in S_3]$
  * $\circ$ : 函數合成 (Function composition) $[S_3 \times S_3 \to S_3]$

* **【已知 5】 [模 $9$ 可逆剩餘類集合與其階 (The units modulo 9 and their order)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Group/Group_Order.html#c-proof-of-the-order-of-the-units-modulo-a-general-number)：** 已於本章 [群的階](Group_Order.md)【證明 (c)】給出，此處直接引用

  $$\mathbf{Z}_9^* = \left\{1, 2, 4, 5, 7, 8\right\}, \qquad \left|\mathbf{Z}_9^*\right| = \varphi(9) = 6$$

  * $\mathbf{Z}_9^*$ : 模 $9$ 可逆剩餘類集合 (The set of units modulo 9) $[\text{集合}]$
  * $\varphi$ : 尤拉函數 (Euler's totient function) $[\mathbb{Z}^{+} \to \mathbb{Z}^{+}]$

* **【已知 6】 [質數模下非零元素皆可逆 (Every non-zero residue modulo a prime is invertible)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Group/General_Linear_Group_Order.html#assumptions-preliminaries)：** 已於本章 [群的正例與反例](Group_Examples_and_Counterexamples.md)【證明 (f)】完整證明，此處直接引用不再重證

  $$\mathbf{Z}_7^* = \left\{1, 2, 3, 4, 5, 6\right\}, \qquad \left|\mathbf{Z}_7^*\right| = 6$$

  * $\mathbf{Z}_7^*$ : 模 $7$ 可逆剩餘類集合 (The set of units modulo 7) $[\text{集合}]$

* **【定義 1】 五的倍數集合與可逆上三角矩陣群 (Multiples of five and invertible upper-triangular matrices)：**

  * (a) 五的倍數：

    $$5\mathbf{Z} \overset{\text{def}}{=} \left\{5a \ \middle|\ a \in \mathbf{Z}\right\}$$

  * (b) 可逆上三角矩陣：

    $$T_2(\mathbf{Z}_7) \overset{\text{def}}{=} \left\{M \in GL_2(\mathbf{Z}_7) \ \middle|\ M \ \text{為上三角矩陣}\right\} = \left\{\begin{bmatrix} a & b \\ 0 & d \end{bmatrix} \ \middle|\ a, b, d \in \mathbf{Z}_7,\ ad \neq 0\right\}$$

  * $5\mathbf{Z}$ : 五的倍數集合 (The set of multiples of five) $[\text{集合}]$
  * $T_2(\mathbf{Z}_7)$ : 可逆上三角矩陣群 (The group of invertible upper-triangular matrices) $[\text{集合}]$
  * $a,\ b,\ d$ : 矩陣元素 (Matrix entries) $[a, b, d \in \mathbf{Z}_7]$
  * $M$ : 一個上三角矩陣 (An upper-triangular matrix) $[M \in GL_2(\mathbf{Z}_7)]$
  * 註：(b) 的條件 $ad \neq 0$ 來自「上三角矩陣的行列式等於對角線乘積」與
    $M$ 可逆（即 $\det M \in \mathbf{Z}_7^*$，由【已知 6】等價於 $\det M \neq 0$）。

+++

## 證明:

### (a) verify that the multiples of five form a subgroup of the integers

依【已知 1】三條依序檢查（運算是加法，故「反元素」指的是 $-a$）：

$$\begin{gather*}
0 = 5 \times 0 &\overset{\text{定義 1(a),已知 1(a)}}{\in}& 5\mathbf{Z} \qquad \text{(非空)} \\
5a + 5b &=& 5\left(a + b\right) \\
5a + 5b &\overset{\text{定義 1(a)}}{\in}& 5\mathbf{Z} \qquad \text{(封閉，因 } a+b \in \mathbf{Z}\text{)} \\
-\left(5a\right) &=& 5\left(-a\right) \\
-\left(5a\right) &\overset{\text{定義 1(a)}}{\in}& 5\mathbf{Z} \qquad \text{(取反元素封閉，因 } -a \in \mathbf{Z}\text{)}
\end{gather*}$$

三條全中，故 $5\mathbf{Z} \le \left(\mathbf{Z}, +\right)$。

* 註：對照 [群的正例與反例](Group_Examples_and_Counterexamples.md)【證明 (c)】——
  那裡檢查了**四**條公理，這裡只檢查**三**條。省下的就是結合律。

### (b) verify that the non-zero rationals form a subgroup of the non-zero reals

運算是乘法：

$$\begin{gather*}
1 &\in& \mathbf{Q}^* \qquad \text{(非空)} \\
a \times b &\in& \mathbf{Q}^* \qquad \text{(封閉，兩個非零有理數的積仍是非零有理數)} \\
\frac{1}{a} &\in& \mathbf{Q}^* \qquad \text{(取反元素封閉，因 } a \neq 0\text{)}
\end{gather*}$$

三條全中，且 $\mathbf{Q}^* \subseteq \mathbf{R}^*$，故 $\mathbf{Q}^* \le \left(\mathbf{R}^*, \times\right)$。

### (c) verify that the three-cycles together with the identity form a subgroup of the symmetric group

令 $H = \left\{e, \left(123\right), \left(132\right)\right\} \subseteq S_3$。先把封閉性所需的乘法表算完
（記 $f = \left(123\right)$、$g = \left(132\right)$）：

$$\begin{gather*}
f \circ f &\overset{\text{已知 4(b)}}{=}& g \\
f \circ g &\overset{\text{已知 4(b)}}{=}& e \\
g \circ f &\overset{\text{已知 4(b)}}{=}& e \\
g \circ g(1) &=& g(3) = 2 \\
g \circ g(2) &=& g(1) = 3 \\
g \circ g(3) &=& g(2) = 1 \\
g \circ g &=& f
\end{gather*}$$

依【已知 1】三條檢查：

$$\begin{gather*}
e &\in& H \qquad \text{(非空)} \\
\left\{f \circ f,\ f \circ g,\ g \circ f,\ g \circ g\right\} &=& \left\{g,\ e,\ e,\ f\right\} \subseteq H \qquad \text{(封閉)} \\
f^{-1} &\overset{\text{已知 4(b)}}{=}& g \in H \\
g^{-1} &=& f \in H \qquad \text{(取反元素封閉)}
\end{gather*}$$

三條全中，故 $H \le S_3$。階的關係：

$$\begin{gather*}
\left|H\right| &=& 3 \\
\left|S_3\right| &\overset{\text{已知 4(a)}}{=}& 6 \\
3 &\mid& 6
\end{gather*}$$

* 註：與 $e$ 相乘的情形（$e \circ f = f$ 等）由 [對稱群](Symmetric_Group.md)【證明 (a)】的
  單位元素性質直接給出，不必列進乘法表。
* 註：$g^{-1} = f$ 由 $f \circ g = g \circ f = e$ 直接讀出，這正是
  [反元素的反元素](Inverse_of_an_Inverse.md) 的內容。

### (d) verify that the pair one and eight forms a subgroup of the units modulo nine

令 $H = \left\{1, 8\right\} \subseteq \mathbf{Z}_9^*$（由【已知 5】，$8 \in \mathbf{Z}_9^*$）：

$$\begin{gather*}
1 &\in& H \qquad \text{(非空)} \\
8 \otimes 8 &=& 64 \bmod 9 \\
8 \otimes 8 &=& 1 \in H \qquad \text{(封閉；與 } 1 \text{ 相乘的情形顯然落在 } H\text{)} \\
8^{-1} &=& 8 \in H \qquad \text{(取反元素封閉，因 } 8 \otimes 8 = 1\text{)} \\
1^{-1} &=& 1 \in H
\end{gather*}$$

三條全中，故 $H \le \left(\mathbf{Z}_9^*, \otimes\right)$。階的關係：

$$\begin{gather*}
\left|H\right| &=& 2 \\
\left|\mathbf{Z}_9^*\right| &\overset{\text{已知 5}}{=}& 6 \\
2 &\mid& 6
\end{gather*}$$

### (e) verify that the special linear group is a subgroup of the general linear group

依【已知 1】三條檢查（運算是矩陣乘法）：

$$\begin{gather*}
\det\left(I\right) &=& 1 \\
I &\overset{\text{已知 3}}{\in}& SL_2(\mathbf{Z}_7) \qquad \text{(非空)} \\
\det\left(AB\right) &\overset{\text{已知 2}}{=}& \det\left(A\right)\det\left(B\right) \\
\det\left(AB\right) &\overset{\text{已知 3}}{=}& 1 \times 1 = 1 \qquad \text{(封閉)} \\
\det\left(A\right)\det\left(A^{-1}\right) &\overset{\text{已知 2}}{=}& \det\left(A A^{-1}\right) = \det\left(I\right) = 1 \\
\det\left(A^{-1}\right) &\overset{\text{已知 3}}{=}& 1 \qquad \text{(取反元素封閉)}
\end{gather*}$$

三條全中，故 $SL_2(\mathbf{Z}_7) \le GL_2(\mathbf{Z}_7)$。

* 註：整個論證只用到行列式的乘法性，**與矩陣的尺寸 $n$ 和係數環 $R$ 都無關**，
  故 $SL_n(R) \le GL_n(R)$ 一般成立。

### (f) verify that the invertible upper-triangular matrices form a subgroup, and count them

**先檢查子群性質。** 兩個上三角矩陣相乘仍是上三角（左下角保持為 $0$）：

$$\begin{gather*}
\begin{bmatrix} a & b \\ 0 & d \end{bmatrix}\begin{bmatrix} a' & b' \\ 0 & d' \end{bmatrix} &=& \begin{bmatrix} aa' & ab' + bd' \\ 0 & dd' \end{bmatrix}
\end{gather*}$$

依【已知 1】三條檢查：

$$\begin{gather*}
I = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} &\overset{\text{定義 1(b)}}{\in}& T_2(\mathbf{Z}_7) \qquad \text{(非空)} \\
aa' \neq 0, \quad dd' &\neq& 0 \qquad \text{(因 } \mathbf{Z}_7 \text{ 無零因子，【已知 6】)} \\
\begin{bmatrix} a & b \\ 0 & d \end{bmatrix}\begin{bmatrix} a' & b' \\ 0 & d' \end{bmatrix} &\overset{\text{定義 1(b)}}{\in}& T_2(\mathbf{Z}_7) \qquad \text{(封閉)} \\
\begin{bmatrix} a & b \\ 0 & d \end{bmatrix}^{-1} &=& \begin{bmatrix} a^{-1} & -a^{-1}bd^{-1} \\ 0 & d^{-1} \end{bmatrix} \\
\begin{bmatrix} a & b \\ 0 & d \end{bmatrix}^{-1} &\overset{\text{定義 1(b)}}{\in}& T_2(\mathbf{Z}_7) \qquad \text{(取反元素封閉，仍為上三角且對角線非零)}
\end{gather*}$$

三條全中，故 $T_2(\mathbf{Z}_7) \le GL_2(\mathbf{Z}_7)$。

**再數它的階。** 三個自由的位置各自獨立（依 [一般線性群的階](General_Linear_Group_Order.md)【已知 5】的乘法原理）：

$$\begin{gather*}
a \ \text{的選法} &\overset{\text{已知 6}}{=}& \left|\mathbf{Z}_7^*\right| = 6 \qquad \text{(對角線元素不可為 } 0\text{)} \\
d \ \text{的選法} &\overset{\text{已知 6}}{=}& \left|\mathbf{Z}_7^*\right| = 6 \\
b \ \text{的選法} &=& \left|\mathbf{Z}_7\right| = 7 \qquad \text{(右上角無限制)} \\
\left|T_2(\mathbf{Z}_7)\right| &=& 6 \times 6 \times 7 \\
\left|T_2(\mathbf{Z}_7)\right| &=& 252
\end{gather*}$$

與投影片 p.21 的 $6 \times 6 \times 7$ 一致。整除關係：

$$\begin{gather*}
\left|GL_2(\mathbf{Z}_7)\right| &=& 2016 \\
\frac{2016}{252} &=& 8 \\
252 &\mid& 2016
\end{gather*}$$

* 註：$\left|GL_2(\mathbf{Z}_7)\right| = 2016$ 已於
  [一般線性群的階](General_Linear_Group_Order.md)【證明 (c)】算出。
* 註：$252 \mid 2016$ 再一次符合 [拉格朗日定理](Lagrange_Theorem.md) 的模式。

+++

## 意義與密碼學關聯 (Interpretation and Relevance to Cryptography)

### 六個例子裡浮出來的模式

把六個例子的階整理成一張表：

| 子群 $H$ | $\left\|H\right\|$ | 母群 $G$ | $\left\|G\right\|$ | $\left\|G\right\| / \left\|H\right\|$ |
|---|---|---|---|---|
| $\left\{e,\left(123\right),\left(132\right)\right\}$ | $3$ | $S_3$ | $6$ | $2$ |
| $\left\{1, 8\right\}$ | $2$ | $\mathbf{Z}_9^*$ | $6$ | $3$ |
| $T_2(\mathbf{Z}_7)$ | $252$ | $GL_2(\mathbf{Z}_7)$ | $2016$ | $8$ |

**每一次商數都是整數。** $5\mathbf{Z} \le \mathbf{Z}$ 與 $\mathbf{Q}^* \le \mathbf{R}^*$ 是無限群，
不在這張表裡，但有限的三個例子無一例外。

這不是巧合。[拉格朗日定理](Lagrange_Theorem.md) 會證明**任何有限群的任何子群都如此**。
在那之前，先記住這個現象 —— 它是本章接下來三個檔案（[陪集](Coset.md)、
[陪集相等的充要條件](Coset_Equality_Criterion.md)、[陪集分割](Coset_Partition.md)）
存在的唯一理由。

### $5\mathbf{Z}$ 這個例子為什麼重要

$5\mathbf{Z} \le \mathbf{Z}$ 看起來平凡，但它是整個 [環](../Ring/Ring_Definition.md) 與
[理想](../Ring/Ideal.md) 理論的原型：

* 把 $\mathbf{Z}$ 對 $5\mathbf{Z}$ 分組，得到的就是 $\mathbf{Z}_5$；
* 一般地，$\mathbf{Z} / n\mathbf{Z} \cong \mathbf{Z}_n$（見 [商環](../Ring/Quotient_Ring.md)）。

**「取模」這個從小用到大的動作，在群論裡的正式身分就是「對子群 $n\mathbf{Z}$ 取商」。**
這條線索會一路延伸到 [中國剩餘定理](../Ring/Chinese_Remainder_Theorem.md)。

### $T_2$ 這種子群在密碼學裡做什麼

上三角矩陣群 $T_2$ 在密碼學與編碼理論裡有個實際用途：**高斯消去法的結構**。
任何可逆矩陣都能分解成下三角 $\times$ 上三角（LU 分解），
這在有限體上一樣成立，是許多線性碼與 MDS 矩陣構造的基礎。

更直接的關聯是：AES 的 MixColumns 用的是一個 $GL_4(GF(2^8))$ 裡的矩陣，
它必須可逆（解密要用 $M^{-1}$），而且被刻意選成**分支數最大**的 MDS 矩陣。
挑選這種矩陣的過程，就是在 $GL_n$ 這個大群裡尋找具有特定性質的元素。

### 判別法省下的成本有多少

以 (f) 為例。若不用 [子群判別法](Subgroup_Criterion.md)，
要驗證 $T_2(\mathbf{Z}_7)$ 是群就得檢查結合律 —— 對 $252$ 個元素的三元組，
共 $252^3 \approx 1.6 \times 10^{7}$ 次比較。

用了判別法，結合律**一次都不用檢查**（從 $GL_2(\mathbf{Z}_7)$ 免費繼承），
只需驗證「上三角乘上三角還是上三角」這一行代數。

**這就是為什麼實務上幾乎不會有人直接驗四條公理** ——
總是先找一個已知的大群，再證明目標集合是它的子群。
