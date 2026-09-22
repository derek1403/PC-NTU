# Abelian and Non-Abelian Group (阿貝爾群與非阿貝爾群)

+++

## 證明目標:

`Algebra.pdf` p.11–12。[群的定義](Group_Definition.md) **不包含交換律** ——
額外滿足交換律的群另有專名，不滿足的則是本章許多「順序不能寫反」的規則的來源。

* (a) $S_n$ 在 $n \ge 3$ 時**非交換**：

$$\left(12\right) \circ \left(123\right) = \left(23\right) \neq \left(13\right) = \left(123\right) \circ \left(12\right)$$

* (b) $\left(\mathbf{Z}_n^*, \otimes\right)$ 對任意 $n$ 都是**交換**群，並以 $n = 9$ 的凱萊表驗證：

$$a \otimes b = b \otimes a \qquad \text{for all } a, b \in \mathbf{Z}_n^*$$

* (c) $GL_n(R)$ 與 $SL_n(R)$ 在 $n \ge 2$ 時**非交換**：

$$\begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}\begin{bmatrix} 1 & 0 \\ 1 & 1 \end{bmatrix} = \begin{bmatrix} 2 & 1 \\ 1 & 1 \end{bmatrix} \neq \begin{bmatrix} 1 & 1 \\ 1 & 2 \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 1 & 1 \end{bmatrix}\begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}$$

* $G$ : 群的底層集合 (The underlying set of the group) $[\text{集合}]$
* $*$ : 群運算 (Group operation) $[G \times G \to G]$
* $a,\ b$ : 群元素 (Group elements) $[a, b \in G]$
* $S_n$ : $n$ 次對稱群 (The symmetric group on $n$ letters) $[\text{集合}]$
* $\mathbf{Z}_n^*$ : 模 $n$ 可逆剩餘類集合 (The set of units modulo $n$) $[\text{集合}]$
* $GL_n(R),\ SL_n(R)$ : 一般線性群與特殊線性群 (General and special linear groups) $[\text{集合}]$
* 註：證明「非交換」**只需要一個反例**；證明「交換」則必須對所有元素成立。
  這造成 (a)(c) 很短、(b) 需要論證的不對稱。
* 註：本檔的三個結論解釋了本章許多地方為什麼要強調順序：
  [乘積的反元素](Inverse_of_a_Product.md) 的顛倒、
  [唯一解與消去律](Unique_Solution_and_Cancellation_Law.md) 的左右之分、
  [陪集](Coset.md) 的左右陪集不相等。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [對稱群 (Symmetric group)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Group/Symmetric_Group.html#a-proof-that-the-symmetric-group-is-a-group)：** 已於本章 [對稱群](Symmetric_Group.md) 完整證明，此處直接引用不再重證

  * (a) $\left(S_n, \circ\right)$ 是群，元素為 $\left\{1, \dots, n\right\}$ 上的排列：

    $$S_n = \left\{f \ \middle|\ f : \left\{1, \dots, n\right\} \to \left\{1, \dots, n\right\} \ \text{為雙射}\right\}$$

  * (b) 合成由右往左作用：

    $$\left(f \circ g\right)(x) = f\left(g(x)\right)$$

  * (c) 循環記號：$\left(a_1 a_2 \cdots a_k\right)$ 表示 $a_1 \to a_2 \to \cdots \to a_k \to a_1$，其餘不動

    $$\left(12\right) = \begin{pmatrix} 1 & 2 & 3 \\ 2 & 1 & 3 \end{pmatrix}, \qquad \left(123\right) = \begin{pmatrix} 1 & 2 & 3 \\ 2 & 3 & 1 \end{pmatrix}$$

  * $S_n$ : $n$ 次對稱群 (The symmetric group on $n$ letters) $[\text{集合}]$
  * $f,\ g$ : 排列 (Permutations) $[f, g \in S_n]$
  * $x$ : 被排列的元素 (An element being permuted) $[x \in \left\{1, \dots, n\right\}]$
  * $n$ : 被排列的元素個數 (The number of letters) $[n \in \mathbf{P}]$

* **【已知 2】 [整數乘法交換律與模運算相容性 (Commutativity of integer multiplication and compatibility with modular reduction)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Group/Group_Examples_and_Counterexamples.html#assumptions-preliminaries)：** 已於本章 [群的正例與反例](Group_Examples_and_Counterexamples.md)【已知 3(d)】【已知 4(a)】引用，此處再次引用

  * (a) 整數乘法交換：

    $$a \times b = b \times a \qquad \text{for all } a, b \in \mathbf{Z}$$

  * (b) 乘法與取模可交換次序：

    $$\left(a \times b\right) \bmod n = \left(\left(a \bmod n\right) \times \left(b \bmod n\right)\right) \bmod n$$

  * $a,\ b$ : 任意整數 (Arbitrary integers) $[a, b \in \mathbf{Z}]$
  * $n$ : 模數 (Modulus) $[n \in \mathbf{P}]$

* **【已知 3】 [矩陣乘法的定義 (Definition of matrix multiplication)](https://mathworld.wolfram.com/MatrixMultiplication.html)：** 線性代數的標準定義，本章直接引用不再重證

  $$\left(AB\right)_{ij} = \sum_{k} A_{ik} B_{kj}$$

  * $A,\ B$ : 方陣 (Square matrices) $[A, B \in M_n(R)]$
  * $\left(AB\right)_{ij}$ : 乘積的第 $i$ 列第 $j$ 行元素 (The $(i,j)$ entry of the product) $[\left(AB\right)_{ij} \in R]$
  * $i,\ j,\ k$ : 列、行與求和指標 (Row, column, and summation indices) $[i, j, k \in \left\{1, \dots, n\right\}]$
  * $R$ : 係數所在的環 (The coefficient ring) $[\text{環}]$

* **【定義 1】 交換群／阿貝爾群 (Commutative group / Abelian group)：** 群的四條公理之外，**額外**滿足交換律

  $$\left(G, *\right) \ \text{為阿貝爾群} \quad \overset{\text{def}}{\Longleftrightarrow} \quad a * b = b * a \qquad \text{for all } a, b \in G$$

  * $G$ : 群的底層集合 (The underlying set of the group) $[\text{集合}]$
  * $*$ : 群運算 (Group operation) $[G \times G \to G]$
  * $a,\ b$ : 群元素 (Group elements) $[a, b \in G]$
  * 註：「阿貝爾」來自挪威數學家 Niels Henrik Abel。不滿足交換律的群稱為**非阿貝爾群**。
  * 註：交換律是**第五條**公理，不在 [群的定義](Group_Definition.md)【定義 2】的四條之內。
    一個結構可以是群而不是阿貝爾群 —— 【證明 (a)】【證明 (c)】就是這樣的例子。

* **【定義 2】 凱萊表 (Cayley table)：** 有限群的完整乘法表。第 $a$ 列第 $b$ 行填入 $a * b$

  $$\left[\text{Cayley table}\right]_{ab} \overset{\text{def}}{=} a * b$$

  * $a,\ b$ : 群元素 (Group elements) $[a, b \in G]$
  * $*$ : 群運算 (Group operation) $[G \times G \to G]$
  * 註：由【定義 1】，**群是阿貝爾群，若且唯若它的凱萊表對主對角線對稱**。
    這給了有限群一個一眼可判的檢查法。

+++

## 證明:

### (a) disprove commutativity of the symmetric group on three or more letters

取 $f = \left(12\right)$、$g = \left(123\right)$，依【已知 1(b)】兩個方向各算一次。

**先算 $f \circ g$**（先做 $g$，再做 $f$）：

$$\begin{gather*}
\left(f \circ g\right)(1) &\overset{\text{已知 1(b)(c)}}{=}& f(2) = 1 \\
\left(f \circ g\right)(2) &\overset{\text{已知 1(b)(c)}}{=}& f(3) = 3 \\
\left(f \circ g\right)(3) &\overset{\text{已知 1(b)(c)}}{=}& f(1) = 2 \\
f \circ g &=& \begin{pmatrix} 1 & 2 & 3 \\ 1 & 3 & 2 \end{pmatrix} = \left(23\right)
\end{gather*}$$

**再算 $g \circ f$**（先做 $f$，再做 $g$）：

$$\begin{gather*}
\left(g \circ f\right)(1) &\overset{\text{已知 1(b)(c)}}{=}& g(2) = 3 \\
\left(g \circ f\right)(2) &\overset{\text{已知 1(b)(c)}}{=}& g(1) = 2 \\
\left(g \circ f\right)(3) &\overset{\text{已知 1(b)(c)}}{=}& g(3) = 1 \\
g \circ f &=& \begin{pmatrix} 1 & 2 & 3 \\ 3 & 2 & 1 \end{pmatrix} = \left(13\right)
\end{gather*}$$

兩者相比：

$$\begin{gather*}
\left(23\right) &\neq& \left(13\right) \\
f \circ g &\overset{\text{定義 1}}{\neq}& g \circ f
\end{gather*}$$

故 $S_3$ 非交換。對 $n > 3$，把上述 $f, g$ 原封不動放進 $S_n$（讓 $4, \dots, n$ 都不動）即得同樣的反例，
故 $S_n$ 對所有 $n \ge 3$ 皆非交換。

* 註：$S_1$ 只有一個元素、$S_2$ 只有兩個元素，兩者都是交換群 —— **$n \ge 3$ 這個條件是必要的**。

### (b) proof of commutativity of the units modulo n

$\mathbf{Z}_n^*$ 的運算是模 $n$ 乘法，而模 $n$ 乘法的交換律直接從整數乘法繼承：

$$\begin{gather*}
a \otimes b &\overset{\text{已知 2(b)}}{=}& \left(a \times b\right) \bmod n \\
&\overset{\text{已知 2(a)}}{=}& \left(b \times a\right) \bmod n \\
&\overset{\text{已知 2(b)}}{=}& b \otimes a
\end{gather*}$$

故 $\left(\mathbf{Z}_n^*, \otimes\right)$ 對**任意** $n$ 都是阿貝爾群。

**以 $n = 9$ 驗證。** 先由 [數系與符號約定](../Number_Sets_and_Notation.md)【定義 4】列出
$\mathbf{Z}_9^* = \left\{1, 2, 4, 5, 7, 8\right\}$，再算出完整的凱萊表（【定義 2】）：

| $\otimes$ | 1 | 2 | 4 | 5 | 7 | 8 |
|---|---|---|---|---|---|---|
| **1** | 1 | 2 | 4 | 5 | 7 | 8 |
| **2** | 2 | 4 | 8 | 1 | 5 | 7 |
| **4** | 4 | 8 | 7 | 2 | 1 | 5 |
| **5** | 5 | 1 | 2 | 7 | 8 | 4 |
| **7** | 7 | 5 | 1 | 8 | 4 | 2 |
| **8** | 8 | 7 | 5 | 4 | 2 | 1 |

抽查表中幾格的計算：

$$\begin{gather*}
2 \otimes 5 &=& 10 \bmod 9 = 1 \\
4 \otimes 7 &=& 28 \bmod 9 = 1 \\
5 \otimes 8 &=& 40 \bmod 9 = 4 \\
7 \otimes 7 &=& 49 \bmod 9 = 4 \\
8 \otimes 8 &=& 64 \bmod 9 = 1
\end{gather*}$$

表對主對角線**完全對稱**：

$$\begin{gather*}
\left[\text{Cayley table}\right]_{ab} &\overset{\text{定義 2}}{=}& \left[\text{Cayley table}\right]_{ba}
\end{gather*}$$

與【定義 2】的註一致，交換性確認。

* 註：$p$ 為質數時 $\mathbf{Z}_p^* = \left\{1, 2, \dots, p-1\right\}$，是本結論的特例，
  即投影片 p.11 的最後一條。**質數性在這裡沒有被用到** —— 交換律對任意 $n$ 都成立。
* 註：表中每一列、每一行都是 $\left\{1,2,4,5,7,8\right\}$ 的一個重排。
  這不是巧合，是 [唯一解與消去律](Unique_Solution_and_Cancellation_Law.md)【證明 (c)】的直接後果。
* 註：$\left(\mathbf{Z}, +\right)$、$\left(\mathbf{Q}, +\right)$、$\left(\mathbf{R}, +\right)$、
  $\left(\mathbf{C}, +\right)$ 也都是阿貝爾群，理由與本小節相同（加法交換律由【已知 2(a)】的加法版本繼承），
  故不另立小節。

### (c) disprove commutativity of the general and special linear groups

取投影片 p.12 的兩個矩陣，兩者行列式都是 $1$，故都落在 $SL_2(\mathbf{Q}) \subset GL_2(\mathbf{Q})$ 內：

$$A = \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}, \qquad B = \begin{bmatrix} 1 & 0 \\ 1 & 1 \end{bmatrix}, \qquad \det A = \det B = 1$$

**先算 $AB$**，依【已知 3】逐格計算：

$$\begin{gather*}
\left(AB\right)_{11} &\overset{\text{已知 3}}{=}& 1 \times 1 + 1 \times 1 = 2 \\
\left(AB\right)_{12} &\overset{\text{已知 3}}{=}& 1 \times 0 + 1 \times 1 = 1 \\
\left(AB\right)_{21} &\overset{\text{已知 3}}{=}& 0 \times 1 + 1 \times 1 = 1 \\
\left(AB\right)_{22} &\overset{\text{已知 3}}{=}& 0 \times 0 + 1 \times 1 = 1 \\
AB &=& \begin{bmatrix} 2 & 1 \\ 1 & 1 \end{bmatrix}
\end{gather*}$$

**再算 $BA$**：

$$\begin{gather*}
\left(BA\right)_{11} &\overset{\text{已知 3}}{=}& 1 \times 1 + 0 \times 0 = 1 \\
\left(BA\right)_{12} &\overset{\text{已知 3}}{=}& 1 \times 1 + 0 \times 1 = 1 \\
\left(BA\right)_{21} &\overset{\text{已知 3}}{=}& 1 \times 1 + 1 \times 0 = 1 \\
\left(BA\right)_{22} &\overset{\text{已知 3}}{=}& 1 \times 1 + 1 \times 1 = 2 \\
BA &=& \begin{bmatrix} 1 & 1 \\ 1 & 2 \end{bmatrix}
\end{gather*}$$

兩者相比：

$$\begin{gather*}
\begin{bmatrix} 2 & 1 \\ 1 & 1 \end{bmatrix} &\neq& \begin{bmatrix} 1 & 1 \\ 1 & 2 \end{bmatrix} \\
AB &\overset{\text{定義 1}}{\neq}& BA
\end{gather*}$$

故 $SL_2(\mathbf{Q})$ 與 $GL_2(\mathbf{Q})$ 皆非交換。
把 $A, B$ 嵌進 $n \times n$ 的左上角、其餘補上單位矩陣，同樣的反例對所有 $n \ge 2$ 皆成立。

* 註：$A, B$ 都在 $SL_2$ 裡，所以這個反例**同時**否證了 $SL_n$ 與 $GL_n$ 的交換性 ——
  一個反例做兩件事。

+++

## 意義與密碼學關聯 (Interpretation and Relevance to Cryptography)

### 交換與否，決定了「順序」要不要管

本章所有「順序不能寫反」的規則，追根究柢都來自非交換性：

| 規則 | 出處 | 交換群裡會怎樣 |
|---|---|---|
| $\left(ab\right)^{-1} = b^{-1}a^{-1}$ | [乘積的反元素](Inverse_of_a_Product.md) | 退化成 $a^{-1}b^{-1}$，順序無所謂 |
| $ax = b$ 的解是 $a^{-1}b$，$ya = b$ 的解是 $ba^{-1}$ | [唯一解與消去律](Unique_Solution_and_Cancellation_Law.md) | 兩個解相等 |
| 左消去律與右消去律要分開證 | 同上 | 一條就夠 |
| 左陪集 $\neq$ 右陪集 | [陪集](Coset.md) | 兩者永遠相等 |

**在阿貝爾群裡，上面整欄的區分全部消失。** 這就是為什麼 RSA
（活在阿貝爾群 $\mathbf{Z}_n^*$ 裡）的推導比 AES（涉及 $S_{256}$ 與 $GL_8$）乾淨得多。

### 密碼學為什麼兩種都要

**公鑰密碼幾乎都建立在阿貝爾群上**：

* RSA $\to \left(\mathbf{Z}_n^*, \otimes\right)$；
* Diffie–Hellman、ElGamal $\to \left(\mathbf{Z}_p^*, \otimes\right)$ 的循環子群；
* 橢圓曲線密碼 $\to$ 曲線上的點群（也是阿貝爾群）。

理由是**交換律讓「雙方用不同順序做同樣的事，卻得到同一個結果」成為可能**。
Diffie–Hellman 的核心就是一行交換律：

$$\left(g^a\right)^b = g^{ab} = g^{ba} = \left(g^b\right)^a$$

Alice 先做 $a$ 再做 $b$、Bob 先做 $b$ 再做 $a$，兩人算出同一把共享金鑰。
**沒有交換律，Diffie–Hellman 不可能成立。**

**對稱密碼則大量使用非阿貝爾結構**：

* S-box $\to S_{256}$；
* MixColumns、S-box 的仿射部分 $\to GL_n$。

理由恰好相反：**非交換性製造混淆 (confusion) 與擴散 (diffusion)**。
若加密的每個零件都可交換，攻擊者就能任意重排運算順序來化簡，
整個密碼的複雜度會塌陷。

**一句話：公鑰要交換律來建立協議，對稱密碼要非交換性來抵抗分析。**

### 凱萊表是最快的判斷法

【定義 2】的註給了有限群一個一眼判斷的方法：**看表對不對稱**。

實作上：

```python
def is_abelian(elements, op):
    return all(op(a, b) == op(b, a) for a in elements for b in elements)
```

$\left|G\right|^2$ 次比較。而要證明**非**交換，只需找到一組反例就停 ——
這正是【證明 (a)】【證明 (c)】各自只用一組元素的原因。
