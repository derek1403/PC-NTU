# General Linear Group Order (一般線性群的階)

+++

## 證明目標:

`Algebra.pdf` p.16 問「$8 \times 8$ 的 $\mathbf{Z}_2$ 可逆矩陣有幾個？」，p.21 用到
$\left|GL_2(\mathbf{Z}_7)\right| = \left(7^2-1\right)\left(7^2-7\right)$。本檔把這個計數一次做完。

* (a) 質數模的一般線性群的階：

$$\left|GL_n(\mathbf{Z}_q)\right| = \prod_{k=0}^{n-1}\left(q^n - q^k\right) \qquad \left(q \ \text{為質數}\right)$$

* (b) 在 $\mathbf{Z}_2$ 上兩個線性群重合：

$$GL_n(\mathbf{Z}_2) = SL_n(\mathbf{Z}_2)$$

* (c) 代入投影片的兩組數值：

$$\left|GL_2(\mathbf{Z}_7)\right| = 2016, \qquad \left|GL_8(\mathbf{Z}_2)\right| = 5\,348\,063\,769\,211\,699\,200$$

* $GL_n(\mathbf{Z}_q)$ : 一般線性群 (General linear group) $[\text{集合}]$
* $SL_n(\mathbf{Z}_q)$ : 特殊線性群 (Special linear group) $[\text{集合}]$
* $n$ : 矩陣的邊長 (Matrix size) $[n \in \mathbb{Z}^{+}]$
* $q$ : 係數所在的質數模 (The prime modulus of the coefficients) $[q \in \mathbf{P}]$
* $k$ : 已選定的列數 (The number of rows already chosen) $[k \in \left\{0, 1, \dots, n-1\right\}]$
* 註：**$q$ 必須是質數**。這一步靠的是「$\mathbf{Z}_q$ 的非零元素全部可逆」，
  已於 [群的正例與反例](Group_Examples_and_Counterexamples.md)【證明 (f)】對 $q=7$ 證明、
  該處的註說明論證對任意質數逐字相同。$q$ 為合數時 $\mathbf{Z}_q$ 有不可逆的非零元素，
  線性代數的整套語言（線性獨立、生成空間）就不適用，本檔的計數失效。
* 註：(a) 的乘積**從 $k=0$ 開始**，第一項是 $q^n - q^0 = q^n - 1$，對應「第一列不可為零向量」。
* 註：$\left|SL_n(\mathbf{Z}_q)\right|$ 的計算需要陪集的語言，留到
  [特殊線性群的指標](Special_Linear_Subgroup_Index.md)。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [一般線性群與特殊線性群的定義 (Definitions of the general and special linear groups)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Number_Sets_and_Notation.html#definitions-and-notation)：** 已於本章 [數系與符號約定](../Number_Sets_and_Notation.md)【定義 6】【定義 7】給出，此處直接引用

  * (a) 一般線性群：

    $$GL_n(R) = \left\{A \in M_n(R) \ \middle|\ \det\left(A\right) \ \text{在} \ R \ \text{中可逆}\right\}$$

  * (b) 特殊線性群：

    $$SL_n(R) = \left\{A \in GL_n(R) \ \middle|\ \det\left(A\right) = 1\right\}$$

  * $GL_n(R),\ SL_n(R)$ : 一般線性群與特殊線性群 (General and special linear groups) $[\text{集合}]$
  * $M_n(R)$ : 係數取自 $R$ 的 $n \times n$ 方陣全體 (All $n \times n$ matrices over $R$) $[\text{集合}]$
  * $A$ : 一個方陣 (A square matrix) $[A \in M_n(R)]$
  * $R$ : 係數所在的環 (The coefficient ring) $[\text{環}]$
  * $n$ : 矩陣的邊長 (Matrix size) $[n \in \mathbb{Z}^{+}]$
  * $\det$ : 行列式 (Determinant) $[M_n(R) \to R]$

* **【已知 2】 [質數模下非零元素皆可逆 (Every non-zero residue modulo a prime is invertible)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Group/Group_Examples_and_Counterexamples.html#f-proof-the-units-modulo-seven-under-multiplication-form-a-group)：** 已於本章 [群的正例與反例](Group_Examples_and_Counterexamples.md)【證明 (f)】完整證明（該處對 $q=7$，註中說明對任意質數逐字相同），此處直接引用不再重證

  $$\mathbf{Z}_q^* = \left\{1, 2, \dots, q-1\right\} \qquad \left(q \ \text{為質數}\right)$$

  * $\mathbf{Z}_q^*$ : 模 $q$ 可逆剩餘類集合 (The set of units modulo $q$) $[\text{集合}]$
  * $q$ : 質數 (A prime) $[q \in \mathbf{P}]$
  * 註：這一條讓 $\mathbf{Z}_q$ 成為一個**體**，線性代數的整套工具（線性獨立、生成空間、
    可逆 $\Leftrightarrow$ 列滿秩）才能原封不動搬過來使用。

* **【已知 3】 [可逆與列線性獨立等價 (Invertibility is equivalent to row independence)](https://mathworld.wolfram.com/MatrixRank.html)：** 體上的線性代數標準結果，本章直接引用不再重證

  $$A \in GL_n(F) \quad \Longleftrightarrow \quad A \ \text{的 } n \ \text{個列向量在 } F^n \ \text{中線性獨立}$$

  * $A$ : 一個方陣 (A square matrix) $[A \in M_n(F)]$
  * $F$ : 一個體 (A field) $[\text{體}]$
  * $F^n$ : $F$ 上的 $n$ 維向量空間 (The $n$-dimensional vector space over $F$) $[\text{集合}]$
  * $n$ : 矩陣的邊長 (Matrix size) $[n \in \mathbb{Z}^{+}]$

* **【已知 4】 [有限體上子空間的大小 (Size of a subspace over a finite field)](https://mathworld.wolfram.com/VectorSpace.html)：** 線性代數的標準結果，本章直接引用不再重證。$k$ 個線性獨立向量張出的子空間，恰由所有係數組合構成

  $$\left|\mathrm{span}\left(v_1, \dots, v_k\right)\right| = q^k \qquad \left(v_1, \dots, v_k \ \text{線性獨立}\right)$$

  * $v_1, \dots, v_k$ : 線性獨立的向量 (Linearly independent vectors) $[v_i \in \mathbf{Z}_q^n]$
  * $\mathrm{span}$ : 生成空間 (The span) $[\text{集合}]$
  * $q$ : 係數所在的質數模 (The prime modulus of the coefficients) $[q \in \mathbf{P}]$
  * $k$ : 向量個數 (The number of vectors) $[k \in \mathbf{N}]$
  * 註：理由是每個係數 $c_i$ 有 $q$ 種選擇、共 $k$ 個係數，且線性獨立保證不同的係數組合給出不同的向量。
    $k = 0$ 時 $\mathrm{span}\left(\ \right) = \left\{\mathbf{0}\right\}$，大小 $q^0 = 1$。

* **【已知 5】 [乘法原理 (Multiplication principle)](https://mathworld.wolfram.com/MultiplicationPrinciple.html)：** 組合計數的標準結果，本章直接引用不再重證

  $$\text{若第 } i \text{ 步有 } m_i \text{ 種選法且各步獨立，則總方法數} = \prod_{i} m_i$$

  * $m_i$ : 第 $i$ 步的選法數 (The number of choices at step $i$) $[m_i \in \mathbf{N}]$
  * $i$ : 步驟編號 (Step index) $[i \in \mathbf{P}]$

+++

## 證明:

### (a) proof of the order of the general linear group over a prime field

依【已知 3】，數 $GL_n(\mathbf{Z}_q)$ 的元素等於數「$n$ 個線性獨立的列向量」有幾種排法。
**一列一列地選**，並注意每一步的限制：

**第 1 列**（$k = 0$）。唯一的限制是不可為零向量。$\mathbf{Z}_q^n$ 共有 $q^n$ 個向量，扣掉零向量：

$$\begin{gather*}
\left|\mathbf{Z}_q^n\right| &=& q^n \\
\left|\mathrm{span}\left(\ \right)\right| &\overset{\text{已知 4}}{=}& q^0 = 1 \\
\text{第 1 列的選法數} &=& q^n - q^0
\end{gather*}$$

**第 $k+1$ 列**（已選好 $k$ 個線性獨立的列）。新的列必須**不落在前 $k$ 列張出的子空間裡** ——
否則它會是前面那些列的線性組合，線性獨立性就壞了：

$$\begin{gather*}
\left|\mathrm{span}\left(v_1, \dots, v_k\right)\right| &\overset{\text{已知 4}}{=}& q^k \\
\text{第 } k+1 \text{ 列的選法數} &=& q^n - q^k
\end{gather*}$$

**把 $k = 0, 1, \dots, n-1$ 各步相乘**（【已知 5】）：

$$\begin{gather*}
\left|GL_n(\mathbf{Z}_q)\right| &\overset{\text{已知 3}}{=}& \text{線性獨立的列向量組數} \\
&\overset{\text{已知 5}}{=}& \prod_{k=0}^{n-1}\left(q^n - q^k\right) \\
&=& \left(q^n - 1\right)\left(q^n - q\right)\left(q^n - q^2\right)\cdots\left(q^n - q^{n-1}\right)
\end{gather*}$$

* 註：**「不落在前面的生成空間裡」這個條件，恰好等於「線性獨立」**，這是本證明的樞紐。
  如果只要求「與前面每一列都不同」，數出來會太多（一個向量可以與前面每一列都不同，
  卻仍是它們的線性組合）。

### (b) proof that the general and special linear groups coincide over the binary field

由【已知 2】，$q = 2$ 時可逆的剩餘類只有一個：

$$\begin{gather*}
\mathbf{Z}_2^* &\overset{\text{已知 2}}{=}& \left\{1\right\}
\end{gather*}$$

於是任何 $A \in GL_n(\mathbf{Z}_2)$ 的行列式**別無選擇**：

$$\begin{gather*}
\det\left(A\right) &\overset{\text{已知 1(a)}}{\in}& \mathbf{Z}_2^* \\
\det\left(A\right) &\overset{\text{已知 2}}{=}& 1 \\
A &\overset{\text{已知 1(b)}}{\in}& SL_n(\mathbf{Z}_2)
\end{gather*}$$

反向的包含由【已知 1(b)】直接給出（$SL_n$ 依定義是 $GL_n$ 的子集）。兩個方向合起來：

$$GL_n(\mathbf{Z}_2) = SL_n(\mathbf{Z}_2)$$

* 註：投影片 p.16 寫的 $GL_8(\mathbf{Z}_2) \left(= SL_8(\mathbf{Z}_2)\right)$ 就是本小節的 $n = 8$ 特例。
* 註：**只有 $q = 2$ 時成立**。$q = 7$ 時 $\mathbf{Z}_7^*$ 有六個元素，
  行列式可以是 $1$ 到 $6$ 任一個，$SL_2(\mathbf{Z}_7)$ 只佔 $GL_2(\mathbf{Z}_7)$ 的六分之一 ——
  這正是 [特殊線性群的指標](Special_Linear_Subgroup_Index.md) 要算的東西。

### (c) proof of the numerical orders in the slides

**投影片 p.21 的 $\left|GL_2(\mathbf{Z}_7)\right|$**，代入【證明 (a)】取 $n = 2$、$q = 7$：

$$\begin{gather*}
\left|GL_2(\mathbf{Z}_7)\right| &\overset{\text{證明 (a)}}{=}& \left(7^2 - 7^0\right)\left(7^2 - 7^1\right) \\
&=& \left(49 - 1\right)\left(49 - 7\right) \\
&=& 48 \times 42 \\
&=& 2016
\end{gather*}$$

與投影片的 $\left(7^2-1\right)\left(7^2-7\right)$ 一致。

**投影片 p.16 的 $\left|GL_8(\mathbf{Z}_2)\right|$**，代入【證明 (a)】取 $n = 8$、$q = 2$：

$$\begin{gather*}
\left|GL_8(\mathbf{Z}_2)\right| &\overset{\text{證明 (a)}}{=}& \prod_{k=0}^{7}\left(2^8 - 2^k\right) \\
&=& \left(256-1\right)\left(256-2\right)\left(256-4\right)\left(256-8\right)\left(256-16\right)\left(256-32\right)\left(256-64\right)\left(256-128\right) \\
&=& 255 \times 254 \times 252 \times 248 \times 240 \times 224 \times 192 \times 128 \\
&=& 5\,348\,063\,769\,211\,699\,200 \\
&\approx& 5.35 \times 10^{18}
\end{gather*}$$

這就是投影片 p.16 那個問號的答案。

+++

## 意義與密碼學關聯 (Interpretation and Relevance to Cryptography)

### AES S-box 的那個矩陣

投影片 p.16 展示的矩陣

$$M = \begin{bmatrix}
1 & 0 & 0 & 0 & 1 & 1 & 1 & 1 \\
1 & 1 & 0 & 0 & 0 & 1 & 1 & 1 \\
1 & 1 & 1 & 0 & 0 & 0 & 1 & 1 \\
1 & 1 & 1 & 1 & 0 & 0 & 0 & 1 \\
1 & 1 & 1 & 1 & 1 & 0 & 0 & 0 \\
0 & 1 & 1 & 1 & 1 & 1 & 0 & 0 \\
0 & 0 & 1 & 1 & 1 & 1 & 1 & 0 \\
0 & 0 & 0 & 1 & 1 & 1 & 1 & 1
\end{bmatrix} \in GL_8(\mathbf{Z}_2)$$

是 AES S-box 的**仿射變換**部分。完整的 S-box 是兩步：

1. 在 $GF(2^8)$ 裡取乘法反元素（$0$ 映到 $0$）—— 見 [體的定義](../Field/Field_Definition.md)；
2. 套用仿射變換 $x \mapsto Mx + c$，其中 $c = \left(1,1,0,0,0,1,1,0\right)^{\mathsf{T}}$。

第 1 步提供**非線性**（這是抵抗線性密碼分析的關鍵），
第 2 步的 $M$ 則負責把位元攪散，並確保 S-box 沒有不動點。

$M$ 必須落在 $GL_8(\mathbf{Z}_2)$ 裡 —— **可逆是硬性要求**，
否則 S-box 不是 [排列](Permutation.md)，AES 就無法解密。

### $5.35 \times 10^{18}$ 這個數字說明了什麼

AES 的設計者從 $5.35 \times 10^{18}$ 個可逆矩陣裡挑了上面那一個。這個數字看起來很大，但請對照：

| 集合 | 大小 |
|---|---|
| $GL_8(\mathbf{Z}_2)$（可能的仿射矩陣） | $5.35 \times 10^{18}$ |
| $S_{256}$（可能的 S-box） | $256! \approx 10^{507}$ |
| AES-128 金鑰空間 | $2^{128} \approx 3.4 \times 10^{38}$ |

$GL_8(\mathbf{Z}_2)$ **比金鑰空間還小得多**。這不是漏洞 ——
$M$ 是公開的設計參數，不是祕密。但它說明了一件事：
**S-box 的安全性不來自「猜不到 $M$」，而來自 $M$ 的代數性質**
（分支數、差分均勻性、不動點數量）。

$M$ 的選法是有跡可循的：它是一個**循環矩陣 (circulant)**，
每一列都是上一列右移一格。這讓硬體實作可以用移位暫存器完成，省下大量電路。

### 為什麼機率上「幾乎所有矩陣都可逆」

把【證明 (a)】除以全部矩陣的個數 $q^{n^2}$：

$$\frac{\left|GL_n(\mathbf{Z}_q)\right|}{q^{n^2}} = \prod_{k=0}^{n-1}\left(1 - q^{k-n}\right) = \left(1 - \frac{1}{q^n}\right)\left(1 - \frac{1}{q^{n-1}}\right)\cdots\left(1 - \frac{1}{q}\right)$$

$q = 2$、$n = 8$ 時這個比例約為 $0.290$ —— **隨機挑一個 $8\times8$ 的二元矩陣，
約有 $29\%$ 的機率可逆**。比例主要被最後一項 $\left(1 - 1/q\right) = 1/2$ 壓住，
$q$ 越大比例越接近 $1$（$q = 7$、$n = 2$ 時是 $2016/2401 \approx 0.84$）。

實務上這代表：**要隨機生成一個可逆矩陣，直接隨機生成再檢查行列式就好**，
期望只需試三、四次，不必設計特殊的演算法。
