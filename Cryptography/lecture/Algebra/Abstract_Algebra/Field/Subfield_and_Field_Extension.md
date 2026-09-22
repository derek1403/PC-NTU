# Subfield and Field Extension (子體與體擴張)

+++

## 證明目標:

`Algebra.pdf` p.48 與 p.50。把體塞進更大的體裡。關鍵的新觀念是：
**大體可以被看成小體上的向量空間**，於是「大多少」這件事有了精確的數字 —— 擴張次數。

* (a) 子體判別法（投影片未列，本檔補上）：

$$K \ \text{是 } F \text{ 的子體} \quad \Longleftrightarrow \quad \left|K\right| \ge 2, \quad a - b \in K, \quad ab^{-1} \in K \ \left(b \neq 0\right)$$

* (b) 投影片的兩個例子：

$$\mathbf{Q} \ \text{是 } \mathbf{R} \text{ 的子體}, \qquad \mathbf{R} \ \text{是 } \mathbf{C} \text{ 的子體}$$

* (c) **體擴張 $L : K$ 中，$L$ 自動是 $K$ 上的向量空間**（投影片 p.50 的核心斷言）。
* (d) 擴張次數的定義與第一個例子：

$$\left[L : K\right] \overset{\text{def}}{=} \dim_K L, \qquad \left[\mathbf{C} : \mathbf{R}\right] = 2 \ \text{（基底 } \left\{1, i\right\}\text{）}$$

* $F,\ L$ : 大體的底層集合 (The underlying sets of the larger fields) $[\text{集合}]$
* $K$ : 子體的底層集合 (The underlying set of the subfield) $[K \subseteq F]$
* $a,\ b$ : 體元素 (Field elements) $[a, b \in F]$
* $\left[L : K\right]$ : 擴張次數 (The degree of the extension) $[\left[L:K\right] \in \mathbf{P} \cup \left\{\infty\right\}]$
* $\dim_K L$ : $L$ 作為 $K$-向量空間的維數 (The dimension of $L$ as a $K$-vector space) $[\dim_K L \in \mathbf{P} \cup \left\{\infty\right\}]$
* 註：記號 $L : K$ 讀作「$L$ 在 $K$ 上的擴張」，**冒號左邊是大的**。
  這與 $\left[L : K\right]$ 的順序一致。
* 註：(c) 是投影片 p.50 的「$L$ has a **natural** structure as a vector space over $K$」——
  「natural」的意思是**不需要額外定義任何東西**，體的加法與乘法直接就是向量加法與純量乘法。
  【證明 (c)】把這件事驗證出來。
* 註：擴張次數可以是無限的（$\left[\mathbf{R} : \mathbf{Q}\right] = \infty$）。
  有限次數的擴張稱為**有限擴張**，是 [塔定理](Tower_Law.md) 與
  [本原元定理](Primitive_Element_Theorem.md) 的舞台。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [體的定義 (Definition of a field)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Field/Field_Definition.html#assumptions-preliminaries)：** 已於本章 [體的定義](Field_Definition.md)【定義 1】【證明 (a)】給出，此處直接引用

  * (a) 體公理：

    $$\left(F, +\right) \ \text{阿貝爾群}, \quad ab = ba, \quad a\left(bc\right) = \left(ab\right)c, \quad a\left(b+c\right) = ab+ac, \quad a \times 1 = a$$

  * (b) 非零元素可逆：

    $$\forall\, a \in F \setminus \left\{0\right\}, \ \exists\, a^{-1} \in F \ \text{ with } \ a a^{-1} = 1$$

  * (c) $\mathbf{Q}, \mathbf{R}, \mathbf{C}$ 都是體：

    $$\mathbf{Q},\ \mathbf{R},\ \mathbf{C} \ \text{皆為體}$$

  * $F$ : 體的底層集合 (The underlying set of the field) $[\text{集合}]$
  * $a,\ b,\ c$ : 體元素 (Field elements) $[a, b, c \in F]$
  * $1$ : 乘法單位元素 (The multiplicative identity) $[1 \in F]$

* **【已知 2】 [子環判別法 (Subring criterion)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Ring/Subring.html#a-proof-of-the-subring-criterion)：** 已於本章 [子環](../Ring/Subring.md)【證明 (a)】完整證明，此處直接引用不再重證

  $$S \le R \quad \Longleftrightarrow \quad S \neq \varnothing, \quad a - b \in S, \quad ab \in S \qquad \text{for all } a, b \in S$$

  * $S$ : $R$ 的子集 (A subset of $R$) $[S \subseteq R]$
  * $R$ : 母環的底層集合 (The underlying set of the ambient ring) $[\text{集合}]$
  * $a,\ b$ : 子集中的元素 (Elements of the subset) $[a, b \in S]$

* **【已知 3】 [向量空間的公理 (Vector space axioms)](https://mathworld.wolfram.com/VectorSpace.html)：** 線性代數的標準定義，本章直接引用不再重證。$V$ 是體 $K$ 上的向量空間，若

  * (a) $\left(V, +\right)$ 是阿貝爾群；
  * (b) 純量乘法對向量加法分配：

    $$\lambda\left(u + v\right) = \lambda u + \lambda v$$

  * (c) 純量乘法對純量加法分配：

    $$\left(\lambda + \mu\right)u = \lambda u + \mu u$$

  * (d) 純量乘法相容於純量乘法：

    $$\left(\lambda \mu\right)u = \lambda\left(\mu u\right)$$

  * (e) 單位純量不動：

    $$1 \cdot u = u$$

  * $V$ : 向量空間 (The vector space) $[\text{集合}]$
  * $K$ : 純量所在的體 (The field of scalars) $[\text{體}]$
  * $u,\ v$ : 向量 (Vectors) $[u, v \in V]$
  * $\lambda,\ \mu$ : 純量 (Scalars) $[\lambda, \mu \in K]$
  * $1$ : $K$ 的乘法單位元素 (The multiplicative identity of $K$) $[1 \in K]$

* **【已知 4】 [維數與基底 (Dimension and basis)](https://mathworld.wolfram.com/Basis.html)：** 線性代數的標準結果，本章直接引用不再重證

  * (a) 基底的定義：

    $$\left\{v_1, \dots, v_m\right\} \ \text{為基底} \quad \Longleftrightarrow \quad \text{線性獨立且生成 } V$$

  * (b) 維數的良定義性（任兩組基底的元素個數相同）：

    $$\dim_K V \overset{\text{def}}{=} \text{任一組基底的元素個數}$$

  * $V$ : 向量空間 (The vector space) $[\text{集合}]$
  * $K$ : 純量所在的體 (The field of scalars) $[\text{體}]$
  * $v_i$ : 基底向量 (Basis vectors) $[v_i \in V]$
  * $m$ : 基底大小 (The size of the basis) $[m \in \mathbf{P}]$

* **【已知 5】 [複數的定義與虛數單位 (Complex numbers and the imaginary unit)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Number_Sets_and_Notation.html#definitions-and-notation)：** 已於本章 [數系與符號約定](../Number_Sets_and_Notation.md)【定義 5(a)】給出，此處直接引用

  $$\mathbf{C} = \left\{a + bi \ \middle|\ a, b \in \mathbf{R}\right\}, \qquad i^2 = -1$$

  * $\mathbf{C}$ : 複數集合 (The set of complex numbers) $[\text{集合}]$
  * $a,\ b$ : 實部與虛部 (Real and imaginary parts) $[a, b \in \mathbf{R}]$
  * $i$ : 虛數單位 (The imaginary unit) $[i \in \mathbf{C}]$

* **【定義 1】 子體與體擴張 (Subfield and field extension)：**

  * (a) 子體：

    $$K \ \text{是 } F \text{ 的子體} \quad \overset{\text{def}}{\Longleftrightarrow} \quad K \subseteq F \ \text{ 且 } \ \left(K, +, \times\right) \ \text{本身是體}$$

  * (b) 體擴張（同一件事換個說法，並記號化）：

    $$L : K \quad \overset{\text{def}}{\Longleftrightarrow} \quad K \ \text{是 } L \text{ 的子體}$$

  * $K$ : 子體的底層集合 (The underlying set of the subfield) $[K \subseteq F]$
  * $F,\ L$ : 大體的底層集合 (The underlying sets of the larger fields) $[\text{集合}]$
  * $+,\ \times$ : 體運算，與大體的**同一組** (The field operations, the same ones as in the larger field) $[F \times F \to F]$
  * 註：投影片 p.48 說「also $F$ is called a **field extension** of $K$」——
    「$K$ 是 $F$ 的子體」與「$F$ 是 $K$ 的擴張」是同一個事實的兩種說法。
  * 註：p.50 把它寫成「a pair of fields $(K, L)$ where $K$ is a subfield of $L$」，
    與 (b) 相同。

* **【定義 2】 擴張次數 (Degree of an extension)：**

  $$\left[L : K\right] \overset{\text{def}}{=} \dim_K L$$

  * $\left[L : K\right]$ : 擴張次數 (The degree of the extension) $[\left[L:K\right] \in \mathbf{P} \cup \left\{\infty\right\}]$
  * $\dim_K L$ : $L$ 作為 $K$-向量空間的維數 (The dimension of $L$ as a $K$-vector space) $[\dim_K L \in \mathbf{P} \cup \left\{\infty\right\}]$
  * $L,\ K$ : 大體與子體 (The larger field and the subfield) $[\text{集合}]$
  * 註：這個定義要合法，必須先確認 $L$ **確實是** $K$ 上的向量空間 —— 那是【證明 (c)】的工作。
  * 註：維數的良定義性（與基底選擇無關）由【已知 4(b)】保證。

* **【假設 1】 子體判別法的三個條件 (The three conditions of the subfield criterion)：** 【證明 (a)】的出發點

  * (a) 至少兩個元素（含 $0$ 與 $1$）：

    $$\left|K\right| \ge 2$$

  * (b) 對減法封閉：

    $$a - b \in K \qquad \text{for all } a, b \in K$$

  * (c) 對除法封閉：

    $$ab^{-1} \in K \qquad \text{for all } a \in K,\ b \in K \setminus \left\{0\right\}$$

  * $K$ : $F$ 的子集 (A subset of $F$) $[K \subseteq F]$
  * $a,\ b$ : 子集中的元素 (Elements of the subset) $[a, b \in K]$
  * 註：(a) 不能只寫「非空」—— 那樣 $K = \left\{0\right\}$ 會通過 (b)(c)，
    但零環不是體（[環的基本命題](../Ring/Ring_Basic_Propositions.md)【證明 (e)】）。
    要求兩個元素才能保證 $1 \in K$。

+++

## 證明:

### (a) proof of the subfield criterion

**($\Rightarrow$)** $K$ 是子體則自己是體，三條都是體公理的直接內容
（$\left|K\right| \ge 2$ 因為 $0 \neq 1$ 都在 $K$ 裡）。

**($\Leftarrow$)** 設【假設 1】三條成立。先造出 $0$ 與 $1$：

$$\begin{gather*}
\exists\, a \in K,\ a &\overset{\text{假設 1(a)}}{\neq}& 0 \qquad \text{(至少兩個元素，故有非零的)} \\
0 = a - a &\overset{\text{假設 1(b)}}{\in}& K \\
1 = a a^{-1} &\overset{\text{假設 1(c)}}{\in}& K
\end{gather*}$$

再逐條檢查體公理。加法群的部分由【已知 2】的子環論證給出：

$$\begin{gather*}
-b = 0 - b &\overset{\text{假設 1(b)}}{\in}& K \\
a + b = a - \left(-b\right) &\overset{\text{假設 1(b)}}{\in}& K \\
\left(K, +\right) &\overset{\text{已知 2}}{\le}& \left(F, +\right)
\end{gather*}$$

乘法與反元素的部分靠【假設 1(c)】：

$$\begin{gather*}
b^{-1} = 1 \cdot b^{-1} &\overset{\text{假設 1(c)}}{\in}& K \qquad \text{for } b \neq 0 \\
ab = a\left(b^{-1}\right)^{-1} &\overset{\text{假設 1(c)}}{\in}& K \qquad \text{(乘法封閉)} \\
a^{-1} &\overset{\text{假設 1(c)}}{\in}& K \qquad \text{(非零元素可逆)}
\end{gather*}$$

其餘公理（結合、交換、分配）是全稱命題，由 $F$ 免費繼承（【已知 1(a)】）。
故：

$$\begin{gather*}
\left(K, +, \times\right) &=& \text{體} \\
K &\overset{\text{定義 1}}{=}& F \ \text{的子體}
\end{gather*}$$

* 註：**「$a - b$」與「$ab^{-1}$」兩條各抵兩條** —— 與
  [子環](../Ring/Subring.md)【證明 (a)】的技巧完全相同，只是多了乘法的版本。
* 註：$ab = a\left(b^{-1}\right)^{-1}$ 這一步用的是
  [反元素的反元素](../Group/Inverse_of_an_Inverse.md)【證明 (a)】的乘法版本。
  $b = 0$ 時 $ab = 0 \in K$ 直接成立，不需要這一步。

### (b) verify the two subfield examples from the slides

**$\mathbf{Q}$ 是 $\mathbf{R}$ 的子體**，依【證明 (a)】三條：

$$\begin{gather*}
0, 1 &\in& \mathbf{Q} \qquad \text{(至少兩個元素)} \\
a - b &\in& \mathbf{Q} \qquad \text{(兩有理數相減仍為有理數)} \\
ab^{-1} = \frac{a}{b} &\in& \mathbf{Q} \qquad \text{(} b \neq 0\text{，兩有理數相除仍為有理數)}
\end{gather*}$$

三條全中，故 $\mathbf{Q}$ 是 $\mathbf{R}$ 的子體，記作 $\mathbf{R} : \mathbf{Q}$。

**$\mathbf{R}$ 是 $\mathbf{C}$ 的子體**，同理：

$$\begin{gather*}
0, 1 &\in& \mathbf{R} \qquad \text{(至少兩個元素)} \\
a - b &\in& \mathbf{R} \qquad \text{(減法封閉)} \\
ab^{-1} &\in& \mathbf{R} \qquad \text{(} b \neq 0\text{，除法封閉)} \\
\mathbf{R} &\overset{\text{已知 5}}{\subseteq}& \mathbf{C} \qquad \text{(取 } b = 0\text{，即 } a + 0i\text{)}
\end{gather*}$$

三條全中，故 $\mathbf{C} : \mathbf{R}$，與投影片一致。

### (c) proof that the larger field is a vector space over the subfield

設 $L : K$。把 $L$ 的元素當**向量**、$K$ 的元素當**純量**，
純量乘法就直接用 $L$ 的乘法（$K \subseteq L$ 故合法）。逐條驗證【已知 3】：

$$\begin{gather*}
\left(L, +\right) &\overset{\text{已知 1(a),已知 3}}{=}& \text{阿貝爾群} \qquad \text{(公理 (a)，因 } L \text{ 是體)} \\
\lambda\left(u + v\right) &\overset{\text{已知 1(a)}}{=}& \lambda u + \lambda v \qquad \text{(公理 (b)，即 } L \text{ 的分配律)} \\
\left(\lambda + \mu\right)u &\overset{\text{已知 1(a)}}{=}& \lambda u + \mu u \qquad \text{(公理 (c)，即 } L \text{ 的分配律)} \\
\left(\lambda\mu\right)u &\overset{\text{已知 1(a)}}{=}& \lambda\left(\mu u\right) \qquad \text{(公理 (d)，即 } L \text{ 的結合律)} \\
1 \cdot u &\overset{\text{已知 1(a)}}{=}& u \qquad \text{(公理 (e)，即 } L \text{ 的單位元素性質)}
\end{gather*}$$

五條全中，故 $L$ 是 $K$ 上的向量空間，與投影片 p.50 一致。

* 註：**五條公理全部是 $L$ 自己的體公理，一條都不必新證** ——
  這就是投影片說「**natural** structure」的意思。
  向量空間的公理其實是體公理的一個子集，只是把元素分成「向量」與「純量」兩種角色來看。
* 註：這裡唯一用到「$K$ 是體」的地方是**純量必須可逆**（才談得上維數與基底）。
  若 $K$ 只是環，$L$ 就只是 $K$-模，沒有良定義的維數。

### (d) verify the degree of the complex numbers over the reals

依【定義 2】要找 $\mathbf{C}$ 作為 $\mathbf{R}$-向量空間的維數。宣稱基底是 $\left\{1, i\right\}$。

**生成**：由【已知 5】，每個複數都是 $1$ 與 $i$ 的實係數組合：

$$\begin{gather*}
z &\overset{\text{已知 5}}{\in}& \mathbf{C} \\
z &\overset{\text{已知 5}}{=}& a + bi \qquad \text{for some } a, b \in \mathbf{R} \\
z &=& a \cdot 1 + b \cdot i
\end{gather*}$$

**線性獨立**：設實係數組合為零：

$$\begin{gather*}
a \cdot 1 + b \cdot i &=& 0 \\
a + bi &=& 0 + 0i \\
a = 0, \quad b &=& 0 \qquad \text{(複數相等即實部虛部各自相等)}
\end{gather*}$$

兩者都成立，故 $\left\{1, i\right\}$ 是基底（【已知 4(a)】），元素個數為 $2$：

$$\begin{gather*}
\dim_{\mathbf{R}} \mathbf{C} &\overset{\text{已知 4(b)}}{=}& 2 \\
\left[\mathbf{C} : \mathbf{R}\right] &\overset{\text{定義 2}}{=}& 2
\end{gather*}$$

與投影片 p.48 的「$\mathbf{C}$ is a field extension of $\mathbf{R}$ with degree $2$」一致。

* 註：**$\left[\mathbf{R} : \mathbf{Q}\right] = \infty$**（本章不證）——
  $\mathbf{R}$ 作為 $\mathbf{Q}$-向量空間沒有有限基底，
  因為 $\mathbf{R}$ 不可數而有限維 $\mathbf{Q}$-空間是可數的
  （見 [群的階](../Group/Group_Order.md)【證明 (d)】的基數討論）。

+++

## 意義與密碼學關聯 (Interpretation and Relevance to Cryptography)

### 「大多少」有了數字

體擴張最重要的觀念是：**大體對小體的「倍數」是一個精確的數字**。

$$\mathbf{C} = \mathbf{R} \oplus \mathbf{R}i \qquad \Longrightarrow \qquad \left[\mathbf{C} : \mathbf{R}\right] = 2$$

每個複數要用**兩個**實數描述。這個「$2$」就是擴張次數。

在有限體上，這個數字直接給出元素個數：

$$\left[L : K\right] = n, \quad \left|K\right| = q \qquad \Longrightarrow \qquad \left|L\right| = q^{n}$$

理由是 $L$ 的每個元素都寫成 $c_1 v_1 + \cdots + c_n v_n$，
每個係數 $c_i$ 有 $q$ 種選擇，共 $q^n$ 種組合（與
[一般線性群的階](../Group/General_Linear_Group_Order.md)【已知 4】的計數相同）。

**這就是為什麼有限體的階一定是質數冪** ——
任何有限體都是 $GF(p)$ 的有限擴張，故 $\left|F\right| = p^n$。

### $GF(2^8)$ 的身分證

AES 的位元組體就是這個公式的實例：

$$GF(2^8) : GF(2), \qquad \left[GF(2^8) : GF(2)\right] = 8, \qquad \left|GF(2^8)\right| = 2^8 = 256$$

**一個位元組 $=$ $GF(2)$ 上的 $8$ 維向量 $=$ $8$ 個位元。**

基底是 $\left\{1, \alpha, \alpha^2, \dots, \alpha^7\right\}$（$\alpha$ 是
$x^8+x^4+x^3+x+1$ 的一個根），所以：

$$b_7 b_6 b_5 b_4 b_3 b_2 b_1 b_0 \quad \longleftrightarrow \quad b_7\alpha^7 + b_6\alpha^6 + \cdots + b_1\alpha + b_0$$

**「位元組」與「$GF(2^8)$ 的元素」之間的對應，就是向量與座標的對應。**
這也解釋了為什麼 $GF(2^8)$ 的加法是 XOR —— 向量加法就是逐座標相加，
而在 $GF(2)$ 裡「相加」就是 XOR。

### 擴張次數決定安全參數

| 體 | 基體 | 次數 | 元素個數 | 用在 |
|---|---|---|---|---|
| $GF(2^8)$ | $GF(2)$ | $8$ | $256$ | AES 的位元組運算 |
| $GF(2^{128})$ | $GF(2)$ | $128$ | $2^{128}$ | AES-GCM 的 GHASH |
| $GF(p^2)$ | $GF(p)$ | $2$ | $p^2$ | 配對密碼學的中間體 |
| $GF(p^{12})$ | $GF(p)$ | $12$ | $p^{12}$ | BN 曲線的配對目標體 |

最後一列的 $12$ 稱為**嵌入次數 (embedding degree)**，
它決定配對密碼學的安全等級 —— 次數太小，離散對數問題會被 MOV 攻擊搬到
$GF(p^k)$ 裡用指數演算法解掉。**選曲線時算的就是這個次數。**

### 為什麼要「擴張」而不是直接用大質數

一個自然的問題：既然要 $256$ 個元素，為什麼不用 $GF(251)$（$251$ 是質數）而要用 $GF(2^8)$？

答案是**位元對齊**：

* $GF(2^8)$ 的元素恰好是一個位元組，加法是 XOR，硬體實作零成本；
* $GF(251)$ 的元素是 $0$–$250$，有 $5$ 個位元組值用不到，
  而且加法要做模 $251$ 約化，需要條件減法。

**擴張體買到的是「元素個數恰好是 $2$ 的冪」這個工程上的便利。**
代價是乘法比較複雜（要做多項式乘法再模約化），
但那可以用查表或 PCLMULQDQ 指令解決。

下一步是弄清楚**怎麼把 $GF(p)$ 擴張成 $GF(p^n)$** ——
那需要 [不可約多項式](Irreducible_Polynomial.md) 與
[模不可約多項式的商環是體](Quotient_by_Irreducible_is_Field.md)。
