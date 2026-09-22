# Special Linear Subgroup Index (特殊線性群的指標)

+++

## 證明目標:

`Algebra.pdf` p.22。投影片用陪集的語言解釋 $\left|SL_2(\mathbf{Z}_7)\right| = \left|GL_2(\mathbf{Z}_7)\right|/6$，
但把關鍵一步標成「(why?)」留給讀者。本檔把整條論證補完。

* (a) 用 $D_t$ 平移出來的陪集，恰好就是「行列式等於 $t$」的那些矩陣：

$$H_t = D_t H = \left\{M \in GL_2(\mathbf{Z}_7) \ \middle|\ \det\left(M\right) = t\right\}, \qquad D_t = \begin{bmatrix} 1 & 0 \\ 0 & t \end{bmatrix}$$

* (b) 投影片的「(why?)」：平移映射 $f_t$ 是雙射，故 $\left|H\right| = \left|H_t\right|$。
* (c) 六個陪集不重不漏地蓋滿 $GL_2(\mathbf{Z}_7)$：

$$GL_2(\mathbf{Z}_7) = H \ \sqcup \ H_2 \ \sqcup \ H_3 \ \sqcup \ H_4 \ \sqcup \ H_5 \ \sqcup \ H_6$$

* (d) 因此：

$$\left|SL_2(\mathbf{Z}_7)\right| = \frac{\left|GL_2(\mathbf{Z}_7)\right|}{6} = \frac{2016}{6} = 336$$

* $GL_2(\mathbf{Z}_7)$ : 一般線性群 (The general linear group) $[\text{集合}]$
* $H = SL_2(\mathbf{Z}_7)$ : 特殊線性群 (The special linear group) $[H \le GL_2(\mathbf{Z}_7)]$
* $H_t$ : 由 $D_t$ 平移出的左陪集 (The left coset translated by $D_t$) $[H_t \subseteq GL_2(\mathbf{Z}_7)]$
* $D_t$ : 對角平移矩陣 (The diagonal translating matrix) $[D_t \in GL_2(\mathbf{Z}_7)]$
* $t$ : 行列式的值 (The determinant value) $[t \in \mathbf{Z}_7^*]$
* $M$ : 一個可逆矩陣 (An invertible matrix) $[M \in GL_2(\mathbf{Z}_7)]$
* 註：**投影片的 $H_t$ 只定義到 $t = 2, \dots, 6$**，因為 $t = 1$ 時 $D_1 = I$、$H_1 = H$ 就是 $SL_2$ 自己。
  本檔為了讓公式整齊，把 $t = 1$ 也納入，並在【證明 (c)】說明兩種寫法一致。
* 註：**「(why?)」的答案已經在 [陪集分割](Coset_Partition.md)【證明 (a)】證過了** ——
  平移映射對任何群、任何子群都是雙射，這裡只是套用。這就是把那三條引理獨立成檔的價值。
* 註：本檔同時是 [拉格朗日定理](Lagrange_Theorem.md) 的一個完整實例：
  $\left[GL_2(\mathbf{Z}_7) : SL_2(\mathbf{Z}_7)\right] = 6 = \left|\mathbf{Z}_7^*\right|$。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [線性群的定義與行列式的乘法性 (Linear groups and multiplicativity of the determinant)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Number_Sets_and_Notation.html#definitions-and-notation)：** 已於本章 [數系與符號約定](../Number_Sets_and_Notation.md)【定義 6】【定義 7】【已知 4】給出，此處直接引用

  * (a) 兩個線性群：

    $$GL_n(R) = \left\{A \ \middle|\ \det A \ \text{可逆}\right\}, \qquad SL_n(R) = \left\{A \in GL_n(R) \ \middle|\ \det A = 1\right\}$$

  * (b) 行列式的乘法性：

    $$\det\left(AB\right) = \det\left(A\right)\det\left(B\right)$$

  * $GL_n(R),\ SL_n(R)$ : 一般線性群與特殊線性群 (General and special linear groups) $[\text{集合}]$
  * $A,\ B$ : 方陣 (Square matrices) $[A, B \in M_n(R)]$
  * $\det$ : 行列式 (Determinant) $[M_n(R) \to R]$
  * $R$ : 係數所在的環 (The coefficient ring) $[\text{環}]$
  * $n$ : 矩陣的邊長 (Matrix size) $[n \in \mathbb{Z}^{+}]$

* **【已知 2】 [$SL$ 是 $GL$ 的子群 ($SL$ is a subgroup of $GL$)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Group/Subgroup_Examples.html#e-verify-that-the-special-linear-group-is-a-subgroup-of-the-general-linear-group)：** 已於本章 [子群的例子](Subgroup_Examples.md)【證明 (e)】完整證明，此處直接引用不再重證

  $$SL_2(\mathbf{Z}_7) \le GL_2(\mathbf{Z}_7)$$

  * $GL_2(\mathbf{Z}_7),\ SL_2(\mathbf{Z}_7)$ : 一般線性群與特殊線性群 (General and special linear groups) $[\text{集合}]$

* **【已知 3】 [一般線性群的階 (Order of the general linear group)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Group/General_Linear_Group_Order.html#c-proof-of-the-numerical-orders-in-the-slides)：** 已於本章 [一般線性群的階](General_Linear_Group_Order.md)【證明 (c)】完整證明，此處直接引用不再重證

  $$\left|GL_2(\mathbf{Z}_7)\right| = \left(7^2-1\right)\left(7^2-7\right) = 2016$$

  * $GL_2(\mathbf{Z}_7)$ : 一般線性群 (The general linear group) $[\text{集合}]$

* **【已知 4】 [陪集等勢與陪集分割 (Coset equinumerosity and partition)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Group/Coset_Partition.html#a-proof-that-every-coset-has-the-same-size-as-the-subgroup)：** 已於本章 [陪集分割](Coset_Partition.md) 完整證明，此處直接引用不再重證

  * (a) 平移映射是雙射，故陪集與子群等勢：

    $$L_g : H \to gH,\ L_g(h) = g * h \ \text{ 為雙射}, \qquad \left|gH\right| = \left|H\right|$$

  * (b) 相異陪集互斥：

    $$g_1H \neq g_2H \quad \Longrightarrow \quad g_1H \cap g_2H = \varnothing$$

  * $L_g$ : 平移映射 (The translation map) $[H \to gH]$
  * $H$ : 子群 (A subgroup) $[H \le G]$
  * $G$ : 母群的底層集合 (The underlying set of the ambient group) $[\text{集合}]$
  * $g,\ g_1,\ g_2$ : 陪集代表元 (Coset representatives) $[g, g_1, g_2 \in G]$
  * $h$ : 子群中的元素 (An element of the subgroup) $[h \in H]$

* **【已知 5】 [質數模下非零元素皆可逆 (Every non-zero residue modulo a prime is invertible)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Group/Group_Examples_and_Counterexamples.html#f-proof-the-units-modulo-seven-under-multiplication-form-a-group)：** 已於本章 [群的正例與反例](Group_Examples_and_Counterexamples.md)【證明 (f)】完整證明，此處直接引用不再重證

  $$\mathbf{Z}_7^* = \left\{1, 2, 3, 4, 5, 6\right\}, \qquad \left|\mathbf{Z}_7^*\right| = 6$$

  * $\mathbf{Z}_7^*$ : 模 $7$ 可逆剩餘類集合 (The set of units modulo 7) $[\text{集合}]$

* **【定義 1】 對角平移矩陣與陪集 (The diagonal translating matrix and its coset)：** 投影片 p.22 的構造

  * (a) 平移矩陣：

    $$D_t \overset{\text{def}}{=} \begin{bmatrix} 1 & 0 \\ 0 & t \end{bmatrix} \qquad \left(t \in \mathbf{Z}_7^*\right)$$

  * (b) 對應的左陪集：

    $$H_t \overset{\text{def}}{=} D_t H, \qquad H \overset{\text{def}}{=} SL_2(\mathbf{Z}_7)$$

  * $D_t$ : 對角平移矩陣 (The diagonal translating matrix) $[D_t \in GL_2(\mathbf{Z}_7)]$
  * $H_t$ : 由 $D_t$ 平移出的左陪集 (The left coset translated by $D_t$) $[H_t \subseteq GL_2(\mathbf{Z}_7)]$
  * $H$ : 特殊線性群 (The special linear group) $[H \le GL_2(\mathbf{Z}_7)]$
  * $t$ : 行列式的值 (The determinant value) $[t \in \mathbf{Z}_7^*]$

* **【推導 1】 平移矩陣可逆且行列式為 $t$ (The translating matrix is invertible with determinant $t$)：** 【證明 (a)】要用

  * (a) 行列式：

    $$\det\left(D_t\right) = 1 \times t - 0 \times 0 = t$$

  * (b) 可逆（因 $t \in \mathbf{Z}_7^*$，由【已知 5】$t^{-1}$ 存在）：

    $$D_t^{-1} = \begin{bmatrix} 1 & 0 \\ 0 & t^{-1} \end{bmatrix}, \qquad \det\left(D_t^{-1}\right) = t^{-1}$$

  * $D_t$ : 對角平移矩陣 (The diagonal translating matrix) $[D_t \in GL_2(\mathbf{Z}_7)]$
  * $t$ : 行列式的值 (The determinant value) $[t \in \mathbf{Z}_7^*]$
  * $t^{-1}$ : $t$ 在 $\mathbf{Z}_7^*$ 中的反元素 (The inverse of $t$ in $\mathbf{Z}_7^*$) $[t^{-1} \in \mathbf{Z}_7^*]$
  * $\det$ : 行列式 (Determinant) $[M_2(\mathbf{Z}_7) \to \mathbf{Z}_7]$
  * 註：(b) 直接驗算 $D_t D_t^{-1} = I$ 即可。**$t$ 必須落在 $\mathbf{Z}_7^*$ 裡**，
    否則 $t^{-1}$ 不存在、$D_t$ 不可逆，整個構造無從開始。

+++

## 證明:

### (a) proof that the coset is the set of matrices with a given determinant

用雙向包含。

**($\subseteq$)** 設 $M \in H_t$，則 $M = D_t N$ 且 $\det N = 1$：

$$\begin{gather*}
M &\overset{\text{定義 1(b)}}{=}& D_t N \qquad \text{for some } N \in H \\
\det\left(M\right) &\overset{\text{已知 1(b)}}{=}& \det\left(D_t\right)\det\left(N\right) \\
\det\left(M\right) &\overset{\text{推導 1(a),已知 1(a)}}{=}& t \times 1 \\
\det\left(M\right) &=& t
\end{gather*}$$

**($\supseteq$)** 反過來，設 $\det M = t$。把 $M$ 拆成 $D_t$ 乘上一個行列式為 $1$ 的矩陣：

$$\begin{gather*}
\det\left(D_t^{-1} M\right) &\overset{\text{已知 1(b)}}{=}& \det\left(D_t^{-1}\right)\det\left(M\right) \\
\det\left(D_t^{-1} M\right) &\overset{\text{推導 1(b)}}{=}& t^{-1} \times t \\
\det\left(D_t^{-1} M\right) &=& 1 \\
D_t^{-1} M &\overset{\text{已知 1(a)}}{\in}& H \\
M &=& D_t\left(D_t^{-1} M\right) \\
M &\overset{\text{定義 1(b)}}{\in}& H_t
\end{gather*}$$

兩個包含合起來：

$$H_t = \left\{M \in GL_2(\mathbf{Z}_7) \ \middle|\ \det\left(M\right) = t\right\}$$

與投影片的第一個小項一致。

### (b) proof that the translation map is bijective

這就是投影片的「(why?)」。投影片定義的 $f_t : H \to H_t$、$f_t(M) = D_t M$，
**正是** [陪集分割](Coset_Partition.md)【定義 1】的平移映射 $L_{D_t}$：

$$\begin{gather*}
H &\overset{\text{已知 2}}{\le}& GL_2(\mathbf{Z}_7) \qquad \text{(陪集的語言才適用)} \\
f_t(M) &\overset{\text{定義 1(b)}}{=}& D_t M \\
f_t &=& L_{D_t} \\
f_t &\overset{\text{已知 4(a)}}{=}& \text{雙射} \\
\left|H_t\right| &\overset{\text{已知 4(a)}}{=}& \left|H\right|
\end{gather*}$$

* 註：**為什麼是雙射，一句話**：滿射是因為 $H_t$ 依定義就是 $f_t$ 的像；
  單射是因為 $D_t$ 可逆（【推導 1(b)】），可以從左邊消掉。
  完整論證見 [陪集分割](Coset_Partition.md)【證明 (a)】。
* 註：這一步是本檔**唯一用到群結構**的地方 —— 沒有 $D_t^{-1}$ 就沒有單射，
  各個 $H_t$ 的大小就不會相等，整個計數垮掉。

### (c) proof that the six cosets partition the general linear group

**互斥**由【已知 4(b)】給出；更直接的理由是【證明 (a)】：
$H_t$ 的元素行列式都是 $t$，而一個矩陣只有一個行列式，不可能同時屬於兩個 $H_t$。

**覆蓋**：任取 $M \in GL_2(\mathbf{Z}_7)$。它的行列式依【已知 1(a)】必為可逆元素：

$$\begin{gather*}
\det\left(M\right) &\overset{\text{已知 1(a)}}{\in}& \mathbf{Z}_7^* \\
\det\left(M\right) &\overset{\text{已知 5}}{\in}& \left\{1, 2, 3, 4, 5, 6\right\} \\
M &\overset{\text{證明 (a)}}{\in}& H_{\det\left(M\right)}
\end{gather*}$$

故每個 $M$ 恰好落在一個 $H_t$ 裡：

$$GL_2(\mathbf{Z}_7) = H_1 \ \sqcup \ H_2 \ \sqcup \ H_3 \ \sqcup \ H_4 \ \sqcup \ H_5 \ \sqcup \ H_6$$

* 註：$t = 1$ 時 $D_1 = I$，故 $H_1 = I \cdot H = H = SL_2(\mathbf{Z}_7)$。
  投影片寫成 $GL_2(\mathbf{Z}_7) = H \cup H_2 \cup \dots \cup H_6$，與本式**完全相同**，
  只是把第一項直接寫成 $H$。
* 註：這裡的 $\sqcup$ 表示**不交聯集**（disjoint union），
  比投影片的 $\cup$ 多帶了「互斥」這個資訊。

### (d) proof of the order of the special linear group

把【證明 (b)】的等勢與【證明 (c)】的分割合起來：

$$\begin{gather*}
\left|GL_2(\mathbf{Z}_7)\right| &\overset{\text{證明 (c)}}{=}& \sum_{t=1}^{6}\left|H_t\right| \\
&\overset{\text{證明 (b)}}{=}& \sum_{t=1}^{6}\left|H\right| \\
&=& 6\left|H\right| \\
&=& 6\left|SL_2(\mathbf{Z}_7)\right|
\end{gather*}$$

代入【已知 3】的數值：

$$\begin{gather*}
\left|SL_2(\mathbf{Z}_7)\right| &=& \frac{\left|GL_2(\mathbf{Z}_7)\right|}{6} \\
&\overset{\text{已知 3}}{=}& \frac{2016}{6} \\
&=& 336
\end{gather*}$$

與投影片的 $\left|SL_2(\mathbf{Z}_7)\right| = \left|GL_2(\mathbf{Z}_7)\right|/6$ 一致。

* 註：那個 $6$ 不是巧合，它就是 $\left|\mathbf{Z}_7^*\right|$ ——
  **行列式有幾種可能的值，就切成幾塊**。
* 註：一般地，同樣的論證給出

  $$\left|SL_n(\mathbf{Z}_q)\right| = \frac{\left|GL_n(\mathbf{Z}_q)\right|}{q - 1} \qquad \left(q \ \text{為質數}\right)$$

  這也解釋了 [一般線性群的階](General_Linear_Group_Order.md)【證明 (b)】的結果 ——
  $q = 2$ 時 $q - 1 = 1$，兩個群當然重合。

+++

## 意義與密碼學關聯 (Interpretation and Relevance to Cryptography)

### 這就是拉格朗日定理的一個完整實例

把本檔的結果對照 [拉格朗日定理](Lagrange_Theorem.md)：

$$\left[GL_2(\mathbf{Z}_7) : SL_2(\mathbf{Z}_7)\right] \overset{\text{證明 (d)}}{=} 6 = \left|\mathbf{Z}_7^*\right|, \qquad 336 \ \Big|\ 2016$$

**投影片 p.22 其實就是在做拉格朗日定理的證明**，只是限定在這個具體例子上：
它逐條列出了「陪集等勢」「陪集互斥」「陪集覆蓋」三件事，
恰好就是 [陪集分割](Coset_Partition.md) 的三條引理。

這也回頭印證了為什麼要把那三條獨立成檔 —— 本檔一行都不必重證，全部引用。

### 行列式是一個群同態

【證明 (a)】揭露了一個更深的結構。考慮映射

$$\det : GL_2(\mathbf{Z}_7) \to \mathbf{Z}_7^*$$

由【已知 1(b)】它滿足 $\det(AB) = \det(A)\det(B)$ —— 這正是
[群同態與群同構](Group_Homomorphism_and_Isomorphism.md) 的定義。

而 $SL_2(\mathbf{Z}_7) = \left\{M \ \middle|\ \det M = 1\right\}$ 是它的**核 (kernel)**，
六個陪集 $H_t$ 則是六條**纖維**（同一個行列式值的原像）。

$$\left|GL_2\right| = \left|\ker\right| \times \left|\mathrm{im}\right| = 336 \times 6 = 2016$$

這是**第一同構定理**的一個實例。本章不正式證明它，但
[環同態與核](../Ring/Ring_Homomorphism_and_Kernel.md) 會在環的版本裡再遇到同樣的模式。

### 密碼學上的對應：為什麼要限制行列式

在有限體上構造密碼零件時，經常需要「隨機挑一個可逆矩陣」。
本檔的計數給出兩種做法：

| 做法 | 從哪裡挑 | 大小 |
|---|---|---|
| 挑任意可逆矩陣 | $GL_2(\mathbf{Z}_7)$ | $2016$ |
| 挑行列式為 $1$ 的 | $SL_2(\mathbf{Z}_7)$ | $336$ |

**限制行列式會把空間縮小 $q-1$ 倍。** 對 $8 \times 8$ 的 $\mathbf{Z}_2$ 矩陣（AES 的情形）
$q - 1 = 1$，兩者一樣大，所以 AES 的設計不必操心這件事
（見 [一般線性群的階](General_Linear_Group_Order.md)【證明 (b)】）。

但在 $GF(2^8)$ 上構造 MixColumns 矩陣時 $q - 1 = 255$，
限制行列式會讓可選空間少掉兩個數量級 —— 這時就要衡量值不值得。

### Hill 密碼：直接用 $GL_n$ 當金鑰空間

歷史上的 Hill 密碼直接把金鑰取成 $GL_n(\mathbf{Z}_{26})$ 的一個矩陣，
加密就是矩陣乘法 $c = Km$，解密是 $m = K^{-1}c$。

金鑰空間的大小正是本檔在算的東西。但 Hill 密碼早已被破解 ——
因為它是**線性的**，攻擊者拿到 $n$ 組明密文對就能解聯立方程式還原 $K$。

這也說明了 [一般線性群的階](General_Linear_Group_Order.md) 文末的那句話：
**現代密碼絕不會把 $GL_n$ 的元素當祕密**，
$GL_n$ 只用來提供擴散，非線性必須另外由 S-box 提供。
