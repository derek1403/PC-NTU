# Subring (子環)

+++

## 證明目標:

`Algebra.pdf` p.30。與 [子群判別法](../Group/Subgroup_Criterion.md) 完全平行的故事：
驗證一個子集是不是子環，不必檢查全部公理。

* (a) 子環判別法（投影片未列，本檔補上）：

$$S \ \text{是 } R \text{ 的子環} \quad \Longleftrightarrow \quad S \neq \varnothing, \quad a - b \in S, \quad ab \in S \qquad \text{for all } a, b \in S$$

* (b)–(e) 投影片的四個例子：

$$\mathbf{Z} \le \mathbf{Q}, \qquad \mathbf{Q}[i] \le \mathbf{C}, \qquad \mathbf{C}[x] \le \mathbf{C}[x, y], \qquad 6\mathbf{Z} \le 2\mathbf{Z}$$

* $R$ : 母環的底層集合 (The underlying set of the ambient ring) $[\text{集合}]$
* $S$ : $R$ 的子集 (A subset of $R$) $[S \subseteq R]$
* $a,\ b$ : 子集中的元素 (Elements of the subset) $[a, b \in S]$
* $\mathbf{Q}[i]$ : 高斯有理數 (The Gaussian rationals) $[\text{集合}]$
* $\le$ : 「是……的子環」（沿用子群的記號）(The subring relation) $[\text{關係}]$
* 註：(a) 的「$a - b \in S$」一條就同時涵蓋了加法封閉與加法反元素 ——
  這是 [子群判別法](../Group/Subgroup_Criterion.md) 兩條件的**合併寫法**，理由見【證明 (a)】。
* 註：**投影片 p.30 的 Note 在這一頁宣告**：往後「環」一律指交換的含單位元環。
  但**子環不必繼承母環的 $1$** —— $2\mathbf{Z} \le \mathbf{Z}$ 就是例子（$\mathbf{Z}$ 有 $1$，$2\mathbf{Z}$ 沒有）。
  本檔採投影片的定義（子環只要自己是環即可），並在文末說明這個歧異。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [環的公理 (Ring axioms)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Ring/Ring_Definition.html#definitions-and-notation)：** 已於本章 [環的定義](Ring_Definition.md)【定義 1】給出，此處直接引用

  $$\left(R, +\right) \ \text{阿貝爾群}, \quad ab \in R, \quad a\left(bc\right) = \left(ab\right)c, \quad a\left(b+c\right) = ab + ac$$

  * $R$ : 環的底層集合 (The underlying set of the ring) $[\text{集合}]$
  * $a,\ b,\ c$ : 環元素 (Ring elements) $[a, b, c \in R]$

* **【已知 2】 [子群判別法 (Subgroup criterion)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Group/Subgroup_Criterion.html#b-proof-of-the-backward-direction)：** 已於本章 [子群判別法](../Group/Subgroup_Criterion.md) 完整證明，此處套在 $\left(R, +\right)$ 上直接引用不再重證

  $$H \le G \quad \Longleftrightarrow \quad H \neq \varnothing, \quad a + b \in H, \quad -a \in H \qquad \text{for all } a, b \in H$$

  * $H$ : $G$ 的子集 (A subset of $G$) $[H \subseteq G]$
  * $G$ : 母群的底層集合 (The underlying set of the ambient group) $[\text{集合}]$
  * $a,\ b$ : 子集中的元素 (Elements of the subset) $[a, b \in H]$
  * 註：這裡已改寫成加法記號（$*$ 換成 $+$、$a^{-1}$ 換成 $-a$），內容不變。

* **【已知 3】 [複數的乘法 (Multiplication of complex numbers)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Group/Group_Homomorphism_and_Isomorphism.html#assumptions-preliminaries)：** 已於本章 [群同態與群同構](../Group/Group_Homomorphism_and_Isomorphism.md)【已知 5(a)】引用，此處再次引用

  $$\left(a + bi\right)\left(c + di\right) = \left(ac - bd\right) + \left(ad + bc\right)i$$

  * $a,\ b,\ c,\ d$ : 實部與虛部 (Real and imaginary parts) $[a, b, c, d \in \mathbf{R}]$
  * $i$ : 虛數單位 (Imaginary unit) $[i \in \mathbf{C}]$，$i^2 = -1$

* **【已知 4】 [多項式環與其構造 (The polynomial ring and its construction)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Ring/Ring_Examples.html#assumptions-preliminaries)：** 已於本章 [環的例子](Ring_Examples.md)【定義 2】【定義 3】給出，此處直接引用

  $$R[x] = \left\{\sum_{i=0}^{m} a_i x^i \ \middle|\ m \in \mathbf{N},\ a_i \in R\right\}, \qquad R[x, y] = \left(R[x]\right)[y]$$

  * $R[x]$ : 一個未定元的多項式環 (The polynomial ring in one indeterminate) $[\text{集合}]$
  * $R[x,y]$ : 兩個未定元的多項式環 (The polynomial ring in two indeterminates) $[\text{集合}]$
  * $R$ : 係數所在的環 (The coefficient ring) $[\text{環}]$
  * $a_i$ : 多項式係數 (Polynomial coefficients) $[a_i \in R]$
  * $x,\ y$ : 未定元 (Indeterminates) $[x, y \notin R]$
  * $m,\ i$ : 次數上界與次數指標 (Degree bound and index) $[m, i \in \mathbf{N}]$

* **【定義 1】 子環 (Subring)：** $R$ 的一個子集，用**同樣的兩個運算**自己也構成環

  $$S \le R \quad \overset{\text{def}}{\Longleftrightarrow} \quad S \subseteq R \ \text{ 且 } \ \left(S, +, \times\right) \ \text{本身是環}$$

  * $S$ : $R$ 的子集 (A subset of $R$) $[S \subseteq R]$
  * $R$ : 母環的底層集合 (The underlying set of the ambient ring) $[\text{集合}]$
  * $+,\ \times$ : 環運算，與 $R$ 的**同一組** (The ring operations, the same ones as in $R$) $[R \times R \to R]$

* **【定義 2】 高斯有理數 (The Gaussian rationals)：**

  $$\mathbf{Q}[i] \overset{\text{def}}{=} \left\{a + bi \ \middle|\ a, b \in \mathbf{Q}\right\}$$

  * $\mathbf{Q}[i]$ : 高斯有理數 (The Gaussian rationals) $[\text{集合}]$
  * $a,\ b$ : 有理數的實部與虛部 (Rational real and imaginary parts) $[a, b \in \mathbf{Q}]$
  * $i$ : 虛數單位 (Imaginary unit) $[i \in \mathbf{C}]$

* **【假設 1】 判別法的三個條件 (The three conditions of the criterion)：** 【證明 (a)】的出發點

  * (a) 非空：

    $$S \neq \varnothing$$

  * (b) 對減法封閉：

    $$a - b \in S \qquad \text{for all } a, b \in S$$

  * (c) 對乘法封閉：

    $$ab \in S \qquad \text{for all } a, b \in S$$

  * $S$ : $R$ 的子集 (A subset of $R$) $[S \subseteq R]$
  * $a,\ b$ : 子集中的元素 (Elements of the subset) $[a, b \in S]$

+++

## 證明:

### (a) proof of the subring criterion

**($\Rightarrow$)** $S$ 是子環，則它自己是環。非空（含 $0$）、加法封閉、有加法反元素、乘法封閉，
全都是環公理的直接內容；而減法封閉由前兩者合成：

$$\begin{gather*}
0 &\overset{\text{已知 1}}{\in}& S \qquad \text{(非空)} \\
-b &\overset{\text{已知 1}}{\in}& S \\
a - b = a + \left(-b\right) &\overset{\text{已知 1}}{\in}& S \qquad \text{(減法封閉)} \\
ab &\overset{\text{已知 1}}{\in}& S \qquad \text{(乘法封閉)}
\end{gather*}$$

**($\Leftarrow$)** 設【假設 1】三條成立。先證加法部分是子群 —— 關鍵是**「減法封閉」一條
同時給出反元素與加法封閉**：

$$\begin{gather*}
\exists\, a &\overset{\text{假設 1(a)}}{\in}& S \\
0 = a - a &\overset{\text{假設 1(b)}}{\in}& S \qquad \text{(取 } b = a\text{)} \\
-b = 0 - b &\overset{\text{假設 1(b)}}{\in}& S \qquad \text{(反元素封閉)} \\
a + b = a - \left(-b\right) &\overset{\text{假設 1(b)}}{\in}& S \qquad \text{(加法封閉)} \\
\left(S, +\right) &\overset{\text{已知 2}}{\le}& \left(R, +\right)
\end{gather*}$$

再檢查環的其餘三條公理：

$$\begin{gather*}
ab &\overset{\text{假設 1(c)}}{\in}& S \qquad \text{(乘法封閉)} \\
a\left(bc\right) &\overset{\text{已知 1}}{=}& \left(ab\right)c \qquad \text{(乘法結合，由 } R \text{ 繼承)} \\
a\left(b + c\right) &\overset{\text{已知 1}}{=}& ab + ac \qquad \text{(分配律，由 } R \text{ 繼承)}
\end{gather*}$$

四條全中（加法阿貝爾群的交換律也由 $R$ 繼承），故：

$$\begin{gather*}
\left(S, +, \times\right) &=& \text{環} \\
S &\overset{\text{定義 1}}{\le}& R
\end{gather*}$$

* 註：**「$a - b \in S$」一條抵兩條**（加法封閉 + 反元素封閉）。
  技巧是先取 $b = a$ 造出 $0$，再用 $0 - b$ 造出 $-b$，最後用 $a - (-b)$ 造出 $a + b$。
  這比 [子群判別法](../Group/Subgroup_Criterion.md) 的寫法更緊湊。
* 註：與子群一樣，**結合律與分配律是全稱命題，從 $R$ 免費繼承**，一次都不用檢查。

### (b) verify that the integers form a subring of the rationals

依【證明 (a)】三條檢查：

$$\begin{gather*}
0 &\in& \mathbf{Z} \qquad \text{(非空)} \\
a - b &\in& \mathbf{Z} \qquad \text{(兩整數相減仍為整數)} \\
ab &\in& \mathbf{Z} \qquad \text{(兩整數相乘仍為整數)}
\end{gather*}$$

三條全中，故 $\mathbf{Z} \le \mathbf{Q}$。同理 $\mathbf{Z} \le \mathbf{R}$。

### (c) verify that the Gaussian rationals form a subring of the complex numbers

依【定義 2】，元素長成 $a + bi$（$a, b \in \mathbf{Q}$）：

$$\begin{gather*}
0 = 0 + 0i &\overset{\text{定義 2}}{\in}& \mathbf{Q}[i] \qquad \text{(非空)} \\
\left(a + bi\right) - \left(c + di\right) &=& \left(a - c\right) + \left(b - d\right)i \\
\left(a + bi\right) - \left(c + di\right) &\overset{\text{定義 2}}{\in}& \mathbf{Q}[i] \qquad \text{(因 } a-c,\ b-d \in \mathbf{Q}\text{)} \\
\left(a + bi\right)\left(c + di\right) &\overset{\text{已知 3}}{=}& \left(ac - bd\right) + \left(ad + bc\right)i \\
\left(a + bi\right)\left(c + di\right) &\overset{\text{定義 2}}{\in}& \mathbf{Q}[i] \qquad \text{(因 } ac-bd,\ ad+bc \in \mathbf{Q}\text{)}
\end{gather*}$$

三條全中，故 $\mathbf{Q}[i] \le \mathbf{C}$。

* 註：**乘法封閉是這裡唯一需要動腦的一條** —— 靠的是 $\mathbf{Q}$ 自己對加減乘封閉，
  讓【已知 3】展開後的實部與虛部都留在 $\mathbf{Q}$ 裡。

### (d) verify that the one-variable polynomials form a subring of the two-variable ones

依【已知 4】，$\mathbf{C}[x, y] = \left(\mathbf{C}[x]\right)[y]$，
故 $\mathbf{C}[x]$ 恰好是「$y$ 的次數為 $0$」的那些元素：

$$\begin{gather*}
\mathbf{C}[x] &\overset{\text{已知 4}}{=}& \left\{f \in \mathbf{C}[x, y] \ \middle|\ f \ \text{不含 } y\right\} \\
0 &\overset{\text{已知 4}}{\in}& \mathbf{C}[x] \qquad \text{(非空)} \\
f - g &\overset{\text{已知 4}}{\in}& \mathbf{C}[x] \qquad \text{(兩個不含 } y \text{ 的多項式相減仍不含 } y\text{)} \\
fg &\overset{\text{已知 4}}{\in}& \mathbf{C}[x] \qquad \text{(乘法只會產生 } x \text{ 的次數，不會憑空生出 } y\text{)}
\end{gather*}$$

三條全中，故 $\mathbf{C}[x] \le \mathbf{C}[x, y]$。

* 註：$\mathbf{C}[x]$ **是**子環，但**不是理想** —— 因為 $y \cdot f$ 會跑出去。
  這個區別正是 [理想](Ideal.md)【證明 (e)】要說的事，投影片 p.35 也特別列出了它。

### (e) verify that the multiples of six form a subring of the even integers

$6\mathbf{Z}$ 的元素長成 $6t$：

$$\begin{gather*}
6\mathbf{Z} &\subseteq& 2\mathbf{Z} \qquad \text{(因 } 6t = 2\left(3t\right)\text{)} \\
0 = 6 \times 0 &\in& 6\mathbf{Z} \qquad \text{(非空)} \\
6s - 6t &=& 6\left(s - t\right) \\
6s - 6t &\in& 6\mathbf{Z} \qquad \text{(減法封閉)} \\
\left(6s\right)\left(6t\right) &=& 6\left(6st\right) \\
\left(6s\right)\left(6t\right) &\in& 6\mathbf{Z} \qquad \text{(乘法封閉)}
\end{gather*}$$

三條全中，故 $6\mathbf{Z} \le 2\mathbf{Z}$。

* 註：**兩者都沒有乘法單位元素**（見 [含單位元環與交換環](Ring_with_Identity_and_Commutative_Ring.md)【證明 (b)】），
  但它們仍然是環與子環。這說明子環關係與「有沒有 $1$」無關。

+++

## 意義與密碼學關聯 (Interpretation and Relevance to Cryptography)

### 子環 vs 子群：省下來的東西一樣

| | 要檢查 | 免費繼承 |
|---|---|---|
| [子群判別法](../Group/Subgroup_Criterion.md) | 非空、$ab \in H$、$a^{-1} \in H$ | 結合律、單位元素 |
| 子環判別法（【證明 (a)】） | 非空、$a - b \in S$、$ab \in S$ | 結合律、分配律、加法交換律、$0$ |

理由完全相同：**全稱形式的公理（結合、分配、交換）會自動被子集繼承**，
而「某個元素存在於 $S$ 裡」型的公理不會。

子環比子群多省一條，是因為「減法封閉」把兩條併成了一條 ——
這只是記號上的便利，不是本質差異。

### 投影片沒說的一個歧異：子環要不要含 $1$

**這是教科書之間真實存在的分歧。** 兩種定義：

* **投影片採的（本章沿用）**：$S$ 自己是環就好。於是 $2\mathbf{Z} \le \mathbf{Z}$ 成立，
  雖然 $\mathbf{Z}$ 有 $1$ 而 $2\mathbf{Z}$ 沒有。
* **另一派（如 Dummit & Foote 的 unital 慣例）**：還要求 $1_R \in S$。
  這一派不承認 $2\mathbf{Z}$ 是 $\mathbf{Z}$ 的子環。

兩種都通行，重點是**用之前先講清楚是哪一種**。
本章採投影片的第一種 —— 這也是為什麼【證明 (e)】的 $6\mathbf{Z} \le 2\mathbf{Z}$ 成立。

**幸運的是這個歧異在密碼學裡不會造成問題**，因為密碼學關心的子結構幾乎都是
[理想](Ideal.md)（一個更強的概念），而理想除了 $R$ 自己以外**本來就不含 $1$**。

### $\mathbf{Q}[i]$ 與 $\mathbf{Z}[i]$：高斯整數在密碼學裡的角色

【證明 (c)】的 $\mathbf{Q}[i]$ 換成整數係數就是**高斯整數** $\mathbf{Z}[i]$，
同樣的論證證明它是 $\mathbf{C}$ 的子環。

高斯整數在整數分解演算法裡有實際用途：它是**二次篩法 (Quadratic Sieve)** 與
**數體篩法 (Number Field Sieve)** 的原型。核心想法是把 $\mathbf{Z}$ 裡難分解的數
搬到更大的環（如 $\mathbf{Z}[i]$）裡，在那裡分解變得容易，再把結果搬回來。

投影片 p.32 的 Remark 提到的「Number Field Sieve 建立在 Dedekind 整環、UFD、PID 的理論上」
說的就是這件事 —— 而 **NFS 是目前分解 RSA 模數最快的已知演算法**。
見 [整環](Integral_Domain.md) 與 [主理想](Principal_Ideal.md)。
