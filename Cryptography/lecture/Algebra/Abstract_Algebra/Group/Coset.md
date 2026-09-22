# Coset (陪集)

+++

## 證明目標:

`Algebra.pdf` p.18（下半）與 p.19（上半）。把子群 $H$ 用群元素 $g$「平移」一下，
得到的東西叫陪集。這是通往 [拉格朗日定理](Lagrange_Theorem.md) 的第一步。

* (a) 左陪集與右陪集**一般不相等**（投影片 p.19 第一組例子）：

$$\left(123\right)\left\{e, \left(12\right)\right\} = \left\{\left(123\right), \left(13\right)\right\} \ \neq \ \left\{\left(123\right), \left(23\right)\right\} = \left\{e, \left(12\right)\right\}\left(123\right)$$

* (b) 但兩者**也可能相等**（投影片 p.19 第二組例子，逐個乘積不同、集合卻相同）：

$$\left(12\right)\left\{e, \left(123\right), \left(132\right)\right\} = \left\{e, \left(123\right), \left(132\right)\right\}\left(12\right) = \left\{\left(12\right), \left(13\right), \left(23\right)\right\}$$

* (c) 陪集自己是不是子群？只有一種情形是：

$$gH \le G \quad \Longleftrightarrow \quad g \in H \quad \Longleftrightarrow \quad gH = H$$

* $G$ : 母群的底層集合 (The underlying set of the ambient group) $[\text{集合}]$
* $H$ : $G$ 的子群 (A subgroup of $G$) $[H \le G]$
* $g$ : 用來平移的群元素 (The translating group element) $[g \in G]$
* $gH,\ Hg$ : 左陪集與右陪集 (Left and right cosets) $[gH, Hg \subseteq G]$
* $S_3$ : $3$ 次對稱群 (The symmetric group on three letters) $[\text{集合}]$
* 註：投影片把兩組例子並列在 **Remark: In general, Left coset $\neq$ Right coset** 底下，
  但**第二組其實是兩者相等的例子** —— 兩邊的元素逐個算出來雖然配對方式不同，
  收集成集合後完全一樣。本檔【證明 (b)】把這件事算清楚。
* 註：(c) 說明陪集**通常不是群**。這一點很重要 —— 陪集是「$G$ 被切開後的一塊」，
  塊本身沒有結構，只有塊的**大小**與**數量**有意義（見 [陪集分割](Coset_Partition.md)）。
* 註：兩者永遠相等的子群稱為**正規子群 (normal subgroup)**，是商群理論的起點。
  本章不深入，但 [商環](../Ring/Quotient_Ring.md) 會在環的版本裡再遇到同樣的問題。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [群的公理 (Group axioms)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Group/Group_Definition.html#definitions-and-notation)：** 已於本章 [群的定義](Group_Definition.md)【定義 2】給出，此處直接引用

  * (a) 結合律：

    $$a * \left(b * c\right) = \left(a * b\right) * c$$

  * (b) 單位元素與反元素：

    $$a * e = e * a = a, \qquad a * a^{-1} = a^{-1} * a = e$$

  * $G$ : 群的底層集合 (The underlying set of the group) $[\text{集合}]$
  * $a,\ b,\ c$ : 群元素 (Group elements) $[a, b, c \in G]$
  * $e$ : 單位元素 (The identity element) $[e \in G]$

* **【已知 2】 [子群判別法 (Subgroup criterion)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Group/Subgroup_Criterion.html#b-proof-of-the-backward-direction)：** 已於本章 [子群判別法](Subgroup_Criterion.md)【證明 (a)(b)】完整證明，此處直接引用不再重證

  $$H \le G \quad \Longleftrightarrow \quad H \neq \varnothing,\ \ ab \in H \ \text{ for all } a,b \in H,\ \ a^{-1} \in H \ \text{ for all } a \in H$$

  * $H$ : $G$ 的子集 (A subset of $G$) $[H \subseteq G]$
  * $G$ : 母群的底層集合 (The underlying set of the ambient group) $[\text{集合}]$
  * $a,\ b$ : 子集中的元素 (Elements of the subset) $[a, b \in H]$

* **【已知 3】 [$S_3$ 的元素與其子群 (Elements and subgroups of $S_3$)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Group/Subgroup_Examples.html#c-verify-that-the-three-cycles-together-with-the-identity-form-a-subgroup-of-the-symmetric-group)：** 已於本章 [對稱群](Symmetric_Group.md) 與 [子群的例子](Subgroup_Examples.md)【證明 (c)】給出，此處直接引用

  * (a) 六個元素：

    $$S_3 = \left\{e,\ \left(12\right),\ \left(13\right),\ \left(23\right),\ \left(123\right),\ \left(132\right)\right\}$$

  * (b) 一個三階子群：

    $$\left\{e,\ \left(123\right),\ \left(132\right)\right\} \le S_3$$

  * (c) 合成由右往左作用：

    $$\left(f \circ g\right)(x) = f\left(g(x)\right)$$

  * $S_3$ : $3$ 次對稱群 (The symmetric group on three letters) $[\text{集合}]$
  * $f,\ g$ : 排列 (Permutations) $[f, g \in S_3]$
  * $x$ : 被排列的元素 (An element being permuted) $[x \in \left\{1,2,3\right\}]$

* **【推導 1】 $\left\{e, \left(12\right)\right\}$ 是 $S_3$ 的子群 (The pair identity-and-transposition is a subgroup)：** 【證明 (a)】要用。依【已知 2】三條檢查

  $$\begin{gather*}
  e &\overset{\text{已知 2}}{\in}& \left\{e, \left(12\right)\right\} \qquad \text{(非空)} \\
  \left(12\right) \circ \left(12\right) &=& e \qquad \text{(封閉)} \\
  \left(12\right)^{-1} &=& \left(12\right) \qquad \text{(取反元素封閉)}
  \end{gather*}$$

  * $S_3$ : $3$ 次對稱群 (The symmetric group on three letters) $[\text{集合}]$
  * $e$ : 恆等排列 (The identity permutation) $[e \in S_3]$
  * 註：$\left(12\right) \circ \left(12\right) = e$ 是因為交換兩次回到原狀；
    所有**對換 (transposition)** 都有這個性質，故都是自己的反元素。

* **【定義 1】 左陪集與右陪集 (Left and right cosets)：** 把子群 $H$ 整個從左邊（或右邊）乘上一個 $g$

  * (a) 左陪集：

    $$gH \overset{\text{def}}{=} \left\{g * h \ \middle|\ h \in H\right\}$$

  * (b) 右陪集：

    $$Hg \overset{\text{def}}{=} \left\{h * g \ \middle|\ h \in H\right\}$$

  * $H$ : $G$ 的子群 (A subgroup of $G$) $[H \le G]$
  * $G$ : 母群的底層集合 (The underlying set of the ambient group) $[\text{集合}]$
  * $g$ : 用來平移的群元素 (The translating group element) $[g \in G]$
  * $h$ : 子群中的元素 (An element of the subgroup) $[h \in H]$
  * $gH,\ Hg$ : 左陪集與右陪集 (Left and right cosets) $[gH, Hg \subseteq G]$
  * 註：$g$ 取遍 $G$ 而**不限於 $H$**。$g \in H$ 時會發生什麼，見【證明 (c)】。

* **【定義 2】 加法記號下的陪集 (Cosets in additive notation)：** 群運算寫成加法時（必為阿貝爾群），陪集記作

  $$g + H \overset{\text{def}}{=} \left\{g + h \ \middle|\ h \in H\right\} = H + g$$

  * $g$ : 用來平移的群元素 (The translating group element) $[g \in G]$
  * $H$ : $G$ 的子群 (A subgroup of $G$) $[H \le G]$
  * $h$ : 子群中的元素 (An element of the subgroup) $[h \in H]$
  * 註：加法記號預設交換，故左右陪集**永遠相等**，$g + H = H + g$，不必區分。
    投影片 p.18 的最後一行說的就是這件事。
  * 註（**dangling 標註**）：本卡片只是換一套記號，不是推導的依據，故本檔的證明段**不會**以
    `\overset{\text{定義 2}}` 引用它。
  * 註：最熟悉的例子是 $\mathbf{Z}$ 對 $4\mathbf{Z}$ 的四個陪集
    $\left\{4\mathbf{Z},\ 1+4\mathbf{Z},\ 2+4\mathbf{Z},\ 3+4\mathbf{Z}\right\}$，
    也就是「除以 $4$ 的四種餘數」。詳見 [模理想的同餘類](../Ring/Congruence_Class_Modulo_Ideal.md)。

+++

## 證明:

### (a) verify that left and right cosets differ in general

取 $H = \left\{e, \left(12\right)\right\}$（【推導 1】已證它是子群）、$g = \left(123\right)$。

**先算左陪集 $gH$。** 依【定義 1(a)】，把 $g$ 乘在左邊：

$$\begin{gather*}
\left(123\right) \circ e &=& \left(123\right) \\
\left[\left(123\right) \circ \left(12\right)\right](1) &\overset{\text{已知 3(c)}}{=}& \left(123\right)(2) = 3 \\
\left[\left(123\right) \circ \left(12\right)\right](2) &\overset{\text{已知 3(c)}}{=}& \left(123\right)(1) = 2 \\
\left[\left(123\right) \circ \left(12\right)\right](3) &\overset{\text{已知 3(c)}}{=}& \left(123\right)(3) = 1 \\
\left(123\right) \circ \left(12\right) &=& \left(13\right) \\
\left(123\right)H &\overset{\text{定義 1(a),推導 1}}{=}& \left\{\left(123\right),\ \left(13\right)\right\}
\end{gather*}$$

**再算右陪集 $Hg$。** 依【定義 1(b)】，把 $g$ 乘在右邊：

$$\begin{gather*}
e \circ \left(123\right) &=& \left(123\right) \\
\left[\left(12\right) \circ \left(123\right)\right](1) &\overset{\text{已知 3(c)}}{=}& \left(12\right)(2) = 1 \\
\left[\left(12\right) \circ \left(123\right)\right](2) &\overset{\text{已知 3(c)}}{=}& \left(12\right)(3) = 3 \\
\left[\left(12\right) \circ \left(123\right)\right](3) &\overset{\text{已知 3(c)}}{=}& \left(12\right)(1) = 2 \\
\left(12\right) \circ \left(123\right) &=& \left(23\right) \\
H\left(123\right) &\overset{\text{定義 1(b)}}{=}& \left\{\left(123\right),\ \left(23\right)\right\}
\end{gather*}$$

兩者相比：

$$\begin{gather*}
\left\{\left(123\right),\ \left(13\right)\right\} &\neq& \left\{\left(123\right),\ \left(23\right)\right\} \\
\left(123\right)H &\neq& H\left(123\right)
\end{gather*}$$

與投影片一致，左陪集確實一般不等於右陪集。

### (b) verify that left and right cosets can nonetheless coincide

取 $H = \left\{e, \left(123\right), \left(132\right)\right\}$（【已知 3(b)】）、$g = \left(12\right)$。

**左陪集 $gH$：**

$$\begin{gather*}
\left(12\right) \circ e &=& \left(12\right) \\
\left[\left(12\right) \circ \left(123\right)\right](1) &\overset{\text{已知 3(c)}}{=}& \left(12\right)(2) = 1 \\
\left[\left(12\right) \circ \left(123\right)\right](2) &\overset{\text{已知 3(c)}}{=}& \left(12\right)(3) = 3 \\
\left[\left(12\right) \circ \left(123\right)\right](3) &\overset{\text{已知 3(c)}}{=}& \left(12\right)(1) = 2 \\
\left(12\right) \circ \left(123\right) &=& \left(23\right) \\
\left[\left(12\right) \circ \left(132\right)\right](1) &\overset{\text{已知 3(c)}}{=}& \left(12\right)(3) = 3 \\
\left[\left(12\right) \circ \left(132\right)\right](2) &\overset{\text{已知 3(c)}}{=}& \left(12\right)(1) = 2 \\
\left[\left(12\right) \circ \left(132\right)\right](3) &\overset{\text{已知 3(c)}}{=}& \left(12\right)(2) = 1 \\
\left(12\right) \circ \left(132\right) &=& \left(13\right) \\
\left(12\right)H &\overset{\text{定義 1(a)}}{=}& \left\{\left(12\right),\ \left(23\right),\ \left(13\right)\right\}
\end{gather*}$$

**右陪集 $Hg$：**

$$\begin{gather*}
e \circ \left(12\right) &=& \left(12\right) \\
\left[\left(123\right) \circ \left(12\right)\right](1) &\overset{\text{已知 3(c)}}{=}& \left(123\right)(2) = 3 \\
\left[\left(123\right) \circ \left(12\right)\right](2) &\overset{\text{已知 3(c)}}{=}& \left(123\right)(1) = 2 \\
\left[\left(123\right) \circ \left(12\right)\right](3) &\overset{\text{已知 3(c)}}{=}& \left(123\right)(3) = 1 \\
\left(123\right) \circ \left(12\right) &=& \left(13\right) \\
\left[\left(132\right) \circ \left(12\right)\right](1) &\overset{\text{已知 3(c)}}{=}& \left(132\right)(2) = 1 \\
\left[\left(132\right) \circ \left(12\right)\right](2) &\overset{\text{已知 3(c)}}{=}& \left(132\right)(1) = 3 \\
\left[\left(132\right) \circ \left(12\right)\right](3) &\overset{\text{已知 3(c)}}{=}& \left(132\right)(3) = 2 \\
\left(132\right) \circ \left(12\right) &=& \left(23\right) \\
H\left(12\right) &\overset{\text{定義 1(b)}}{=}& \left\{\left(12\right),\ \left(13\right),\ \left(23\right)\right\}
\end{gather*}$$

兩者相比：

$$\begin{gather*}
\left\{\left(12\right),\ \left(23\right),\ \left(13\right)\right\} &=& \left\{\left(12\right),\ \left(13\right),\ \left(23\right)\right\} \\
\left(12\right)H &=& H\left(12\right)
\end{gather*}$$

**兩者相等。**

* 註：**這一組不是「左 $\neq$ 右」的反例，恰恰相反。** 投影片把它列在
  「In general, Left coset $\neq$ Right coset」底下，容易讓人誤以為它也是反例；
  實際上兩個集合完全一樣，只是**元素配對的方式不同**
  （左邊 $\left(12\right)\left(123\right) = \left(23\right)$，右邊 $\left(123\right)\left(12\right) = \left(13\right)$）。
* 註：這裡兩者相等的原因是 $\left\{e,\left(123\right),\left(132\right)\right\}$ 在 $S_3$ 裡的**指標為 $2$**
  （$6/3 = 2$），而指標 $2$ 的子群必為正規子群，左右陪集永遠相同。
  **真正的分辨標準是子群本身正不正規，不是選了哪個 $g$。**

### (c) proof that a coset is a subgroup if and only if it is the subgroup itself

**($\Rightarrow$) 陪集是子群推出 $g \in H$。** 子群必含單位元素（【已知 2】的非空 + 另兩條推出 $e \in H$）：

$$\begin{gather*}
gH \ \text{為子群} &\overset{\text{已知 2}}{\Longrightarrow}& e \in gH \\
e &\overset{\text{定義 1(a)}}{=}& g * h \qquad \text{for some } h \in H \\
g^{-1} &\overset{\text{已知 1(b)}}{=}& h \\
g^{-1} &\in& H \\
g &\overset{\text{已知 2}}{\in}& H \qquad \text{(} H \text{ 對取反元素封閉)}
\end{gather*}$$

**($\Leftarrow$) $g \in H$ 推出 $gH = H$。** 用雙向包含。

先證 $gH \subseteq H$，這只是 $H$ 的封閉性：

$$\begin{gather*}
g \in H, \quad h &\in& H \\
g * h &\overset{\text{已知 2}}{\in}& H \\
gH &\overset{\text{定義 1(a)}}{\subseteq}& H
\end{gather*}$$

再證 $H \subseteq gH$。任取 $h \in H$，把它寫成 $g$ 乘上某個 $H$ 的元素：

$$\begin{gather*}
h &\overset{\text{已知 1(b)}}{=}& g * \left(g^{-1} * h\right) \\
g^{-1} &\overset{\text{已知 2}}{\in}& H \qquad \text{(因 } g \in H\text{)} \\
g^{-1} * h &\overset{\text{已知 2}}{\in}& H \qquad \text{(封閉性)} \\
h &\overset{\text{定義 1(a)}}{\in}& gH \\
H &\subseteq& gH
\end{gather*}$$

兩個包含合起來得 $gH = H$，而 $H$ 本來就是子群。

兩個方向都證完，三個敘述等價。

+++

## 意義與密碼學關聯 (Interpretation and Relevance to Cryptography)

### 陪集是「平移」，不是「子群」

【證明 (c)】說得很清楚：**除了 $H$ 自己，沒有任何陪集是子群。**

幾何上的圖像是：$H$ 是一條**通過原點**的直線，$gH$ 是把它平移到別處的平行線。
平行線不通過原點（不含單位元素），所以不是子群。

$$H \ \text{(通過原點)} \quad \xrightarrow{\ \text{平移 } g\ } \quad gH \ \text{(不通過原點)}$$

這也是為什麼陪集**沒有內部結構可談**。它們有價值的地方只有兩點：

1. **大小** —— 每個陪集都跟 $H$ 一樣大；
2. **數量** —— 它們把 $G$ 不重不漏地切完。

兩點合起來就是 [拉格朗日定理](Lagrange_Theorem.md)。這兩件事會在
[陪集分割](Coset_Partition.md) 證明。

### 最熟悉的陪集：除法的餘數

在 $\left(\mathbf{Z}, +\right)$ 裡取 $H = 4\mathbf{Z}$（[子群的例子](Subgroup_Examples.md)【證明 (a)】的 $n=4$ 版本），
四個陪集是：

$$\begin{aligned}
0 + 4\mathbf{Z} &= \left\{\dots, -8, -4, 0, 4, 8, \dots\right\} \\
1 + 4\mathbf{Z} &= \left\{\dots, -7, -3, 1, 5, 9, \dots\right\} \\
2 + 4\mathbf{Z} &= \left\{\dots, -6, -2, 2, 6, 10, \dots\right\} \\
3 + 4\mathbf{Z} &= \left\{\dots, -5, -1, 3, 7, 11, \dots\right\}
\end{aligned}$$

**這就是「除以 $4$ 餘 $0$、$1$、$2$、$3$」四組數。** 每個整數恰好落在一組裡，四組合起來就是 $\mathbf{Z}$。

換句話說：**你從小學就在用陪集，只是那時候它叫「餘數」。**
$\mathbf{Z}_4$ 這個集合的正式身分，就是 $\mathbf{Z}$ 的所有陪集所成的集合。
這條線索在 [模理想的同餘類](../Ring/Congruence_Class_Modulo_Ideal.md) 與
[商環](../Ring/Quotient_Ring.md) 會被完整展開。

### 左右之分為什麼在密碼學裡通常不用煩惱

【定義 2】的註指出：阿貝爾群裡左右陪集永遠相同。
而公鑰密碼用的群（$\mathbf{Z}_n^*$、橢圓曲線點群）**全部都是阿貝爾群**
（見 [阿貝爾群與非阿貝爾群](Abelian_and_Non_Abelian_Group.md)）。

所以在 RSA、Diffie–Hellman、ECC 的分析裡，**根本不需要區分左右陪集**，
所有子群自動正規，商群自動存在。

左右之分只在對稱密碼涉及 $S_n$、$GL_n$ 這類非阿貝爾群時才浮現，
而那些場合通常不需要商結構。**這是公鑰密碼的數學比對稱密碼乾淨的另一個原因。**
