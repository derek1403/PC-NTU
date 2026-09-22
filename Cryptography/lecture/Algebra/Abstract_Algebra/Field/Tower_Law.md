# Tower Law (塔定理)

+++

## 證明目標:

`Algebra.pdf` p.51（上半）。擴張可以疊羅漢，而**次數會相乘**。
這條定理讓複雜的擴張可以拆成幾層簡單的來算。

* (a) 擴張的遞移性與次數相乘：

$$K \subseteq L \subseteq M \quad \Longrightarrow \quad M : K \ \text{是體擴張，且} \ \left[M : K\right] = \left[M : L\right]\left[L : K\right]$$

* (b) 驗證投影片的例子：

$$\left[\mathbf{Q}\!\left(\sqrt{2}, \sqrt{3}\right) : \mathbf{Q}\right] = \left[\mathbf{Q}\!\left(\sqrt{2}, \sqrt{3}\right) : \mathbf{Q}\!\left(\sqrt{2}\right)\right]\left[\mathbf{Q}\!\left(\sqrt{2}\right) : \mathbf{Q}\right] = 2 \times 2 = 4$$

* $K,\ L,\ M$ : 三層體，由小到大 (Three nested fields, from smallest to largest) $[K \subseteq L \subseteq M]$
* $\left[M : K\right]$ : 擴張次數 (The degree of the extension) $[\left[M:K\right] \in \mathbf{P} \cup \left\{\infty\right\}]$
* $u_i$ : $L$ 在 $K$ 上的基底 (A basis of $L$ over $K$) $[u_i \in L]$
* $v_j$ : $M$ 在 $L$ 上的基底 (A basis of $M$ over $L$) $[v_j \in M]$
* $m,\ n$ : 兩層的次數 (The two degrees) $[m, n \in \mathbf{P}]$
* 註：證明的核心是一句話 —— **把兩層的基底「相乘」，得到的 $mn$ 個元素就是整體的基底**。
  【推導 1】【推導 2】分別驗證它生成與線性獨立。
* 註：本檔只處理**有限**次數的情形。任一層無限時等式仍成立（兩側都是 $\infty$），
  但需要基數的語言，本章不涉入。
* 註：(b) 用到 $\mathbf{Q}\!\left(\sqrt{2}\right)$ 這個記號，
  嚴格的定義見 [單擴張](Simple_Extension.md)；本檔在【定義 2】給出所需的具體形式。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [體擴張與擴張次數 (Field extensions and degree)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Field/Subfield_and_Field_Extension.html#c-proof-that-the-larger-field-is-a-vector-space-over-the-subfield)：** 已於本章 [子體與體擴張](Subfield_and_Field_Extension.md)【定義 1】【定義 2】【證明 (a)(c)(d)】給出並證明，此處直接引用不再重證

  * (a) 大體是小體上的向量空間：

    $$L : K \quad \Longrightarrow \quad L \ \text{是 } K \text{ 上的向量空間}$$

  * (b) 擴張次數即維數：

    $$\left[L : K\right] = \dim_K L$$

  * (c) 子體判別法：

    $$K \ \text{是 } F \text{ 的子體} \Longleftrightarrow \left|K\right| \ge 2,\ a - b \in K,\ ab^{-1} \in K \ \left(b \neq 0\right)$$

  * $K,\ L$ : 子體與大體 (The subfield and the larger field) $[K \subseteq L]$
  * $a,\ b$ : 體元素 (Field elements) $[a, b \in K]$
  * $\dim_K L$ : $L$ 作為 $K$-向量空間的維數 (The dimension of $L$ over $K$) $[\dim_K L \in \mathbf{P} \cup \left\{\infty\right\}]$

* **【已知 2】 [基底與維數 (Basis and dimension)](https://mathworld.wolfram.com/Basis.html)：** 線性代數的標準結果，本章直接引用不再重證

  * (a) 基底：線性獨立且生成整個空間。

    $$\left\{v_1, \dots, v_n\right\} \ \text{為基底} \quad \Longleftrightarrow \quad \text{線性獨立且生成 } V$$

  * (b) 維數是任一組基底的元素個數（與選擇無關）：

    $$\dim_K V = \left|\text{任一組基底}\right|$$

  * $V$ : 向量空間 (The vector space) $[\text{集合}]$
  * $K$ : 純量所在的體 (The field of scalars) $[\text{體}]$
  * $v_j$ : 基底向量 (Basis vectors) $[v_j \in V]$
  * $n$ : 基底大小 (The size of the basis) $[n \in \mathbf{P}]$

* **【已知 3】 [$\sqrt{2}$ 與 $\sqrt{3}$ 是無理數 (Irrationality of the square roots of two and three)](https://mathworld.wolfram.com/IrrationalNumber.html)：** 初等數論的標準結果，本章直接引用不再重證

  * (a) 兩個平方根皆非有理數：

    $$\sqrt{2} \notin \mathbf{Q}, \qquad \sqrt{3} \notin \mathbf{Q}$$

  * (b) 更一般地，非完全平方的正整數的平方根為無理數：

    $$n \in \mathbf{P},\ n \ \text{非完全平方} \quad \Longrightarrow \quad \sqrt{n} \notin \mathbf{Q}$$

  * (c) 非完全平方的有理數的平方根亦為無理數：

    $$q \in \mathbf{Q}^+,\ \sqrt{q} \notin \mathbf{Q} \quad \text{例如 } q = \tfrac{3}{2}$$

  * $n$ : 正整數 (A positive integer) $[n \in \mathbf{P}]$
  * $q$ : 正有理數 (A positive rational) $[q \in \mathbf{Q}^+]$

* **【定義 1】 基底乘積集合 (The product of two bases)：** 【證明 (a)】的主角

  $$B \overset{\text{def}}{=} \left\{u_i v_j \ \middle|\ 1 \le i \le m,\ 1 \le j \le n\right\}$$

  * $B$ : 基底乘積集合 (The product set) $[B \subseteq M]$
  * $u_i$ : $L$ 在 $K$ 上的基底 (A basis of $L$ over $K$) $[u_i \in L]$
  * $v_j$ : $M$ 在 $L$ 上的基底 (A basis of $M$ over $L$) $[v_j \in M]$
  * $m,\ n$ : 兩層的次數 (The two degrees) $[m, n \in \mathbf{P}]$
  * $i,\ j$ : 基底指標 (Basis indices) $[i \in \left\{1,\dots,m\right\},\ j \in \left\{1,\dots,n\right\}]$
  * 註：$u_i v_j$ 是 **$M$ 裡的乘法**（$u_i \in L \subseteq M$、$v_j \in M$，兩者相乘仍在 $M$ 裡）。
  * 註：$\left|B\right| \le mn$，等號成立是【推導 2】的線性獨立性保證的
    （相異的 $(i,j)$ 給出相異的乘積）。

* **【定義 2】 兩層二次擴張 (The two quadratic extensions)：** 【證明 (b)】要用的具體體

  * (a) 第一層：

    $$\mathbf{Q}\!\left(\sqrt{2}\right) \overset{\text{def}}{=} \left\{a + b\sqrt{2} \ \middle|\ a, b \in \mathbf{Q}\right\}$$

  * (b) 第二層：

    $$\mathbf{Q}\!\left(\sqrt{2}, \sqrt{3}\right) \overset{\text{def}}{=} \left\{p + q\sqrt{3} \ \middle|\ p, q \in \mathbf{Q}\!\left(\sqrt{2}\right)\right\}$$

  * $\mathbf{Q}\!\left(\sqrt{2}\right)$ : 添進 $\sqrt{2}$ 的體 (The field obtained by adjoining the square root of two) $[\text{集合}]$
  * $\mathbf{Q}\!\left(\sqrt{2}, \sqrt{3}\right)$ : 再添進 $\sqrt{3}$ 的體 (The field obtained by further adjoining the square root of three) $[\text{集合}]$
  * $a,\ b$ : 有理係數 (Rational coefficients) $[a, b \in \mathbf{Q}]$
  * $p,\ q$ : $\mathbf{Q}\!\left(\sqrt{2}\right)$ 中的係數 (Coefficients in the first extension) $[p, q \in \mathbf{Q}\!\left(\sqrt{2}\right)]$
  * 註：(b) 刻意寫成「在 $\mathbf{Q}\!\left(\sqrt{2}\right)$ 上再添一層」的形式，
    這樣才直接對應到塔定理的三層結構
    $\mathbf{Q} \subseteq \mathbf{Q}\!\left(\sqrt{2}\right) \subseteq \mathbf{Q}\!\left(\sqrt{2},\sqrt{3}\right)$。
  * 註：兩者都是體，驗證方法與 [整環](../Ring/Integral_Domain.md)【證明 (c)】的
    $\mathbf{Z}\!\left[\sqrt{2}\right]$ 相同，再加上除法封閉（分母有理化）。

* **【假設 1】 反設：$\sqrt{3}$ 落在第一層裡 (Proof by contradiction)：** 【推導 3】的出發點

  $$\sqrt{3} = a + b\sqrt{2} \qquad \text{for some } a, b \in \mathbf{Q}$$

  * $a,\ b$ : 有理係數 (Rational coefficients) $[a, b \in \mathbf{Q}]$

* **【推導 1】 基底乘積生成整個大體 (The product set spans the largest field)：** 【證明 (a)】的一半。
  把 $M$ 的元素先用 $v_j$ 展開（係數在 $L$），再把每個係數用 $u_i$ 展開（係數在 $K$）

  $$\begin{gather*}
  w &\overset{\text{已知 2(a)}}{=}& \sum_{j=1}^{n} b_j v_j \qquad \text{for some } b_j \in L \\
  b_j &\overset{\text{已知 2(a)}}{=}& \sum_{i=1}^{m} a_{ij} u_i \qquad \text{for some } a_{ij} \in K \\
  w &=& \sum_{j=1}^{n}\left(\sum_{i=1}^{m} a_{ij} u_i\right)v_j \\
  w &\overset{\text{已知 1(a)}}{=}& \sum_{i=1}^{m}\sum_{j=1}^{n} a_{ij}\left(u_i v_j\right)
  \end{gather*}$$

  * $w$ : $M$ 中的任意元素 (An arbitrary element of $M$) $[w \in M]$
  * $b_j$ : $L$ 中的係數 (Coefficients in $L$) $[b_j \in L]$
  * $a_{ij}$ : $K$ 中的係數 (Coefficients in $K$) $[a_{ij} \in K]$
  * $u_i,\ v_j$ : 兩組基底 (The two bases) $[u_i \in L,\ v_j \in M]$
  * 註：最後一行只是把和式重排並套用 $M$ 的結合律與分配律 ——
    三層都在同一個體 $M$ 裡運算，故合法。
  * 註：結論是每個 $w \in M$ 都是 $B$（【定義 1】）的 $K$-線性組合，即 $B$ 生成 $M$。

* **【推導 2】 基底乘積線性獨立 (The product set is linearly independent)：** 【證明 (a)】的另一半。
  分兩階段剝開 —— 先用 $v_j$ 的獨立性、再用 $u_i$ 的獨立性

  $$\begin{gather*}
  \sum_{i=1}^{m}\sum_{j=1}^{n} a_{ij}\left(u_i v_j\right) &=& 0 \qquad \text{with } a_{ij} \in K \\
  \sum_{j=1}^{n}\left(\sum_{i=1}^{m} a_{ij} u_i\right)v_j &\overset{\text{已知 1(a)}}{=}& 0 \\
  \sum_{i=1}^{m} a_{ij} u_i &\overset{\text{已知 2(a)}}{=}& 0 \qquad \text{for every } j \ \text{(因 } v_j \ \text{在 } L \ \text{上獨立)} \\
  a_{ij} &\overset{\text{已知 2(a)}}{=}& 0 \qquad \text{for every } i, j \ \text{(因 } u_i \ \text{在 } K \ \text{上獨立)}
  \end{gather*}$$

  * $a_{ij}$ : $K$ 中的係數 (Coefficients in $K$) $[a_{ij} \in K]$
  * $u_i,\ v_j$ : 兩組基底 (The two bases) $[u_i \in L,\ v_j \in M]$
  * $m,\ n$ : 兩層的次數 (The two degrees) $[m, n \in \mathbf{P}]$
  * 註：**第三行是樞紐** —— 括號裡的 $\sum_i a_{ij}u_i$ 是 $L$ 的元素，
    所以整條式子是「$M$ 中的元素用 $L$-係數對 $v_j$ 的線性組合」，
    $v_j$ 在 $L$ 上獨立就逼得每個括號都是 $0$。
  * 註：**兩次獨立性用在不同的層次上**，順序不可對調 ——
    必須先剝外層（$v_j$ 在 $L$ 上）再剝內層（$u_i$ 在 $K$ 上）。

* **【推導 3】 $\sqrt{3}$ 不在第一層裡 ($\sqrt{3}$ does not lie in the first extension)：** 【證明 (b)】要用。
  反設它在（【假設 1】），兩邊平方看會發生什麼

  * (a) 平方後整理：

    $$\begin{gather*}
    3 &\overset{\text{假設 1}}{=}& \left(a + b\sqrt{2}\right)^2 \\
    3 &=& a^2 + 2b^2 + 2ab\sqrt{2}
    \end{gather*}$$

  * (b) 若 $ab \neq 0$，可解出 $\sqrt{2}$ 是有理數：

    $$\begin{gather*}
    \sqrt{2} &=& \frac{3 - a^2 - 2b^2}{2ab} \\
    \sqrt{2} &\in& \mathbf{Q} \\
    \sqrt{2} &\overset{\text{已知 3(a)}}{\notin}& \mathbf{Q}
    \end{gather*}$$

  * (c) 故 $ab = 0$，兩種情形各自也矛盾：

    $$\begin{gather*}
    a = 0 &\Longrightarrow& 3 = 2b^2 \\
    b &=& \sqrt{\tfrac{3}{2}} \\
    b &\overset{\text{已知 3(c)}}{\notin}& \mathbf{Q} \\
    b = 0 &\Longrightarrow& \sqrt{3} = a \in \mathbf{Q} \\
    \sqrt{3} &\overset{\text{已知 3(a)}}{\notin}& \mathbf{Q}
    \end{gather*}$$

  * $a,\ b$ : 有理係數 (Rational coefficients) $[a, b \in \mathbf{Q}]$
  * 註：三種情形全部矛盾，故【假設 1】不成立：$\sqrt{3} \notin \mathbf{Q}\!\left(\sqrt{2}\right)$。
  * 註：(b) 的分母 $2ab \neq 0$ 是該情形的前提，故除法合法。

+++

## 證明:

### (a) proof of the tower law

**先確認 $M : K$ 確實是體擴張。** $K \subseteq L \subseteq M$ 故 $K \subseteq M$；
$K$ 自己是體，且與 $M$ 用同一組運算，故依【已知 1(c)】$K$ 是 $M$ 的子體：

$$\begin{gather*}
K &\subseteq& L \subseteq M \\
K &\overset{\text{已知 1(c)}}{=}& M \ \text{的子體} \\
M : K &\overset{\text{已知 1(a)}}{=}& \text{體擴張}
\end{gather*}$$

**再算次數。** 設 $\left\{u_1, \dots, u_m\right\}$ 是 $L$ 在 $K$ 上的基底、
$\left\{v_1, \dots, v_n\right\}$ 是 $M$ 在 $L$ 上的基底（【已知 2(b)】保證存在）：

$$\begin{gather*}
m &\overset{\text{已知 1(b)}}{=}& \left[L : K\right] \\
n &\overset{\text{已知 1(b)}}{=}& \left[M : L\right]
\end{gather*}$$

由【推導 1】，$B = \left\{u_iv_j\right\}$ 生成 $M$；由【推導 2】，它線性獨立。
故它是 $M$ 在 $K$ 上的基底：

$$\begin{gather*}
B &\overset{\text{推導 1,推導 2,已知 2(a)}}{=}& M \ \text{在 } K \ \text{上的基底} \\
\left|B\right| &\overset{\text{定義 1,推導 2}}{=}& mn \\
\left[M : K\right] &\overset{\text{已知 1(b),已知 2(b)}}{=}& mn \\
\left[M : K\right] &=& \left[M : L\right]\left[L : K\right]
\end{gather*}$$

與投影片一致。

* 註：$\left|B\right| = mn$（而非更少）由【推導 2】保證 ——
  若某兩個 $u_iv_j$ 重合，就會存在一組非零係數使線性組合為零，與獨立性矛盾。

### (b) verify the degree of the biquadratic field

依【定義 2】的三層結構 $\mathbf{Q} \subseteq \mathbf{Q}\!\left(\sqrt{2}\right) \subseteq \mathbf{Q}\!\left(\sqrt{2},\sqrt{3}\right)$，
分別算兩層的次數。

**第一層 $\left[\mathbf{Q}\!\left(\sqrt{2}\right) : \mathbf{Q}\right] = 2$。** 宣稱基底是 $\left\{1, \sqrt{2}\right\}$。
生成性由【定義 2(a)】直接給出；線性獨立性：

$$\begin{gather*}
a \cdot 1 + b\sqrt{2} &\overset{\text{定義 2(a)}}{=}& 0 \qquad \text{with } a, b \in \mathbf{Q} \\
b \neq 0 &\Longrightarrow& \sqrt{2} = -\frac{a}{b} \in \mathbf{Q} \\
\sqrt{2} &\overset{\text{已知 3(a)}}{\notin}& \mathbf{Q} \\
b &=& 0 \\
a &=& 0
\end{gather*}$$

故 $\left\{1, \sqrt{2}\right\}$ 是基底：

$$\left[\mathbf{Q}\!\left(\sqrt{2}\right) : \mathbf{Q}\right] \overset{\text{已知 1(b),已知 2(b)}}{=} 2$$

**第二層 $\left[\mathbf{Q}\!\left(\sqrt{2},\sqrt{3}\right) : \mathbf{Q}\!\left(\sqrt{2}\right)\right] = 2$。**
宣稱基底是 $\left\{1, \sqrt{3}\right\}$。生成性由【定義 2(b)】直接給出；線性獨立性：

$$\begin{gather*}
p \cdot 1 + q\sqrt{3} &\overset{\text{定義 2(b)}}{=}& 0 \qquad \text{with } p, q \in \mathbf{Q}\!\left(\sqrt{2}\right) \\
q \neq 0 &\Longrightarrow& \sqrt{3} = -\frac{p}{q} \in \mathbf{Q}\!\left(\sqrt{2}\right) \\
\sqrt{3} &\overset{\text{推導 3}}{\notin}& \mathbf{Q}\!\left(\sqrt{2}\right) \\
q &=& 0 \\
p &=& 0
\end{gather*}$$

故：

$$\left[\mathbf{Q}\!\left(\sqrt{2},\sqrt{3}\right) : \mathbf{Q}\!\left(\sqrt{2}\right)\right] \overset{\text{已知 1(b),已知 2(b)}}{=} 2$$

**套塔定理**：

$$\begin{gather*}
\left[\mathbf{Q}\!\left(\sqrt{2},\sqrt{3}\right) : \mathbf{Q}\right] &\overset{\text{證明 (a)}}{=}& \left[\mathbf{Q}\!\left(\sqrt{2},\sqrt{3}\right) : \mathbf{Q}\!\left(\sqrt{2}\right)\right]\left[\mathbf{Q}\!\left(\sqrt{2}\right) : \mathbf{Q}\right] \\
&=& 2 \times 2 \\
&=& 4
\end{gather*}$$

與投影片一致。由【證明 (a)】，基底是兩層基底的乘積：

$$B = \left\{1 \times 1,\ 1 \times \sqrt{3},\ \sqrt{2} \times 1,\ \sqrt{2} \times \sqrt{3}\right\} = \left\{1,\ \sqrt{3},\ \sqrt{2},\ \sqrt{6}\right\}$$

也就是說每個元素都能唯一寫成：

$$a + b\sqrt{2} + c\sqrt{3} + d\sqrt{6} \qquad \left(a, b, c, d \in \mathbf{Q}\right)$$

* 註：**$\sqrt{6} = \sqrt{2}\sqrt{3}$ 自動出現在基底裡** ——
  這正是【定義 1】說的「把兩層基底相乘」，不是額外添加的東西。

+++

## 意義與密碼學關聯 (Interpretation and Relevance to Cryptography)

### 次數相乘的直覺：座標的座標

塔定理的圖像是**巢狀座標系統**：

* $M$ 的元素要用 $n$ 個 $L$-座標描述；
* 每個 $L$-座標又要用 $m$ 個 $K$-座標描述；
* 所以 $M$ 的元素總共要用 $mn$ 個 $K$-座標。

$$\underbrace{\left(\underbrace{a_{11}, \dots, a_{m1}}_{b_1 \text{ 的座標}},\ \dots,\ \underbrace{a_{1n}, \dots, a_{mn}}_{b_n \text{ 的座標}}\right)}_{mn \ \text{個 } K\text{-座標}}$$

這與「一個 $m \times n$ 矩陣有 $mn$ 個元素」是同一件事。

### 有限體的階為什麼是質數冪

塔定理給了 [子體與體擴張](Subfield_and_Field_Extension.md) 文末那條結論的證明骨架：

$$GF(p) \subseteq F \quad \Longrightarrow \quad \left|F\right| = p^{\left[F : GF(p)\right]}$$

任何有限體 $F$ 都含有一個**質體** $GF(p)$（$p = \mathrm{ch}(F)$，
由 [體的特徵](Characteristic_of_a_Field.md)【證明 (b)(d)】），
而 $F$ 是它的有限擴張，故階必為 $p^n$。

更進一步，塔定理還給出**子體的結構**：

$$GF(p^d) \subseteq GF(p^n) \quad \Longleftrightarrow \quad d \mid n$$

因為 $\left[GF(p^n) : GF(p)\right] = n = \left[GF(p^n) : GF(p^d)\right] \times d$，
右側要是整數就必須 $d \mid n$。**這是拉格朗日定理在體論裡的對應版本。**

### 密碼學上的對應：嵌入次數與塔式實作

**1. 配對密碼學的塔式擴張**

BN 曲線的配對目標體是 $GF(p^{12})$。直接實作十二次擴張的乘法很慢，
實務上用**塔式構造**：

$$GF(p) \subseteq GF(p^2) \subseteq GF(p^6) \subseteq GF(p^{12})$$

每層都是低次擴張（$2, 3, 2$），乘法用 Karatsuba 或 Toom–Cook 遞迴加速。
由塔定理 $2 \times 3 \times 2 = 12$，層層相乘剛好對上。

**這個「塔」正是本檔定理的名字的由來**，而且它在 pairing 函式庫（如 blst、mcl）
裡是字面意義上的實作結構 —— 每層一個型別。

**2. 嵌入次數決定安全性**

橢圓曲線的**嵌入次數** $k$ 定義為使 $GF(p^k)$ 含有 $r$ 次單位根的最小 $k$。
MOV 攻擊可以把曲線上的離散對數問題搬到 $GF(p^k)^*$ 裡，
而後者可以用指數演算法（index calculus）求解，複雜度是次指數的。

* $k$ **太小**（如超奇異曲線的 $k \le 6$）$\Rightarrow$ 搬過去之後容易解 $\Rightarrow$ **不安全**；
* $k$ **太大** $\Rightarrow$ 配對運算太慢 $\Rightarrow$ 不實用。

BN 曲線選 $k = 12$ 是兩者的平衡點。**這個數字直接來自本檔的次數計算。**

**3. $GF(2^{128})$ 可以看成 $GF(2^8)$ 的擴張嗎？**

$128 = 8 \times 16$，由塔定理可以：

$$GF(2) \subseteq GF(2^8) \subseteq GF(2^{128})$$

有些 AES-GCM 的實作確實利用這個分層，把 GHASH 的 $GF(2^{128})$ 乘法
拆成 $GF(2^8)$ 上的運算再組合，以便重用 AES 的查表。
**但現代 CPU 有 PCLMULQDQ 指令直接做 $GF(2)$ 上的無進位乘法**，
所以實務上通常不分層，直接算。

### 一個常見的誤用

塔定理說 $\left[M:K\right] = \left[M:L\right]\left[L:K\right]$，**但反過來不能亂拆**。

給定 $\left[M:K\right] = 4$，**不保證**存在中間體 $L$ 使兩層各為 $2$ ——
雖然這個例子（$\mathbf{Q}\!\left(\sqrt{2},\sqrt{3}\right)$）恰好有。
$\mathbf{Q}\!\left(\sqrt[4]{2}\right)$ 的次數也是 $4$，
它有中間體 $\mathbf{Q}\!\left(\sqrt{2}\right)$；但一般的四次擴張未必。

**「次數的因數分解」與「中間體的存在」之間的精確關係是伽羅瓦理論的主題**，
超出本章範圍。這裡只要記住：塔定理是**單向**的計算工具。
