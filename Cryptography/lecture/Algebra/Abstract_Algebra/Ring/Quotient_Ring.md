# Quotient Ring (商環)

+++

## 證明目標:

`Algebra.pdf` p.40。[模理想的同餘類](Congruence_Class_Modulo_Ideal.md) 把 $R$ 切成一堆同餘類，
本檔證明**這些類自己也構成一個環** —— 而這一步需要理想的吸收性，子環辦不到。

* (a) 加法良定義：

$$\left(a + I\right) + \left(b + I\right) = \left(a + b\right) + I$$

* (b) 乘法良定義（**吸收性在這裡是必要的**）：

$$\left(a + I\right) \times \left(b + I\right) = \left(ab\right) + I$$

* (c) $R/I$ 配上這兩個運算構成環。
* (d) 兩個極端情形：

$$R/R \cong \left\{0\right\}, \qquad R/\left\{0\right\} \cong R$$

* (e) 整數的情形：

$$\mathbf{Z}/n\mathbf{Z} \cong \mathbf{Z}_n$$

* $R$ : 環的底層集合 (The underlying set of the ring) $[\text{集合}]$
* $I$ : $R$ 的理想 (An ideal of $R$) $[I \trianglelefteq R]$
* $R/I$ : 商環 (The quotient ring) $[\text{集合}]$
* $a,\ b$ : 環元素 (Ring elements) $[a, b \in R]$
* $a + I$ : $a$ 模 $I$ 的同餘類 (The congruence class of $a$ modulo $I$) $[a + I \in R/I]$
* $n$ : 整數模數 (An integer modulus) $[n \in \mathbf{P}]$
* 註：**「良定義」是本檔的全部難點。** 同餘類有很多代表元
  （$1 + 4\mathbf{Z}$ 也可以寫成 $5 + 4\mathbf{Z}$），
  所以「用代表元定義運算」必須先證明**換代表元不影響結果**，否則定義根本不成立。
* 註：投影片 p.39 說這樣定義「seems natural」。【證明 (a)(b)】就是把那個 "seems" 拿掉。
* 註：投影片 p.40 另列 $\mathbf{R}[x]/\left\langle x^2+1 \right\rangle \cong \mathbf{C}$，
  本檔不證，留到 [模不可約多項式的商環是體](../Field/Quotient_by_Irreducible_is_Field.md) ——
  那裡會證明更一般的定理（模不可約多項式的商環是**體**），這個同構是它的特例。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [理想的定義 (Definition of an ideal)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Ring/Ideal.html#assumptions-preliminaries)：** 已於本章 [理想](Ideal.md)【定義 1】給出，此處直接引用

  * (a) 加法子群：

    $$0 \in I, \qquad c_1 + c_2 \in I, \qquad c_1 - c_2 \in I \qquad \text{for all } c_1, c_2 \in I$$

  * (b) 吸收性：

    $$cr \in I \qquad \text{for all } c \in I,\ r \in R$$

  * $I$ : $R$ 的理想 (An ideal of $R$) $[I \trianglelefteq R]$
  * $R$ : 母環的底層集合 (The underlying set of the ambient ring) $[\text{集合}]$
  * $c,\ c_1,\ c_2$ : 理想中的元素 (Elements of the ideal) $[c, c_1, c_2 \in I]$
  * $r$ : 母環中的元素 (An element of the ambient ring) $[r \in R]$

* **【已知 2】 [同餘類與陪集 (Congruence classes and cosets)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Ring/Congruence_Class_Modulo_Ideal.html#b-proof-that-a-congruence-class-is-a-coset)：** 已於本章 [模理想的同餘類](Congruence_Class_Modulo_Ideal.md)【定義 1】【定義 2】【證明 (a)(b)】給出並證明，此處直接引用不再重證

  * (a) 同餘的定義：

    $$a \equiv b \pmod{I} \quad \Longleftrightarrow \quad a - b \in I$$

  * (b) 同餘類就是陪集：

    $$a + I = \left\{a + c \ \middle|\ c \in I\right\}$$

  * (c) 兩個同餘類相等的判別式：

    $$a + I = a' + I \quad \Longleftrightarrow \quad a - a' \in I$$

  * $a,\ a',\ b$ : 環元素 (Ring elements) $[a, a', b \in R]$
  * $I$ : $R$ 的理想 (An ideal of $R$) $[I \trianglelefteq R]$
  * $c$ : 理想中的元素 (An element of the ideal) $[c \in I]$
  * 註：(c) 是本檔驗證良定義時反覆使用的工具 —— **「兩個類相等」就是「代表元的差在 $I$ 裡」**。

* **【已知 3】 [環的公理 (Ring axioms)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Ring/Ring_Definition.html#definitions-and-notation)：** 已於本章 [環的定義](Ring_Definition.md)【定義 1】給出，此處直接引用

  $$\left(R, +\right) \ \text{阿貝爾群}, \quad ab \in R, \quad a\left(bc\right) = \left(ab\right)c, \quad a\left(b+c\right) = ab + ac$$

  * $R$ : 環的底層集合 (The underlying set of the ring) $[\text{集合}]$
  * $a,\ b,\ c$ : 環元素 (Ring elements) $[a, b, c \in R]$

* **【已知 4】 [環同構的定義 (Definition of a ring isomorphism)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Group/Group_Homomorphism_and_Isomorphism.html#assumptions-preliminaries)：** 與 [群同態與群同構](../Group/Group_Homomorphism_and_Isomorphism.md)【定義 1】【定義 2】平行，環的版本另見 [環同態與核](Ring_Homomorphism_and_Kernel.md)

  $$f \ \text{為環同構} \quad \overset{\text{def}}{\Longleftrightarrow} \quad f(a+b) = f(a) \oplus f(b), \quad f(ab) = f(a) \otimes f(b), \quad f \ \text{雙射}$$

  * $f$ : 兩環之間的映射 (A map between two rings) $[R \to S]$
  * $a,\ b$ : 環元素 (Ring elements) $[a, b \in R]$
  * $\oplus,\ \otimes$ : 目標環的兩個運算 (The two operations of the target ring) $[S \times S \to S]$
  * $R,\ S$ : 兩個環 (Two rings) $[\text{集合}]$

* **【已知 5】 [除法原理與模運算 (Division algorithm and modular arithmetic)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Ring/Ring_Examples.html#c-verify-that-the-residues-modulo-n-form-a-ring)：** 已於本章 [環的例子](Ring_Examples.md)【證明 (c)】與 [主理想](Principal_Ideal.md)【已知 2(b)】給出，此處直接引用

  * (a) 除法原理：

    $$\forall\, a \in \mathbf{Z}, \ \exists!\ q, r \ \text{ with } \ a = qn + r,\ 0 \le r < n$$

  * (b) $\mathbf{Z}_n$ 是環：

    $$\mathbf{Z}_n = \left\{0, 1, \dots, n-1\right\} \ \text{ 配 } \oplus, \otimes$$

  * $a$ : 整數 (An integer) $[a \in \mathbf{Z}]$
  * $q,\ r$ : 商與餘數 (The quotient and the remainder) $[q, r \in \mathbf{Z}]$
  * $n$ : 模數 (Modulus) $[n \in \mathbf{P}]$
  * $\mathbf{Z}_n$ : 模 $n$ 剩餘類環 (The ring of residues modulo $n$) $[\text{集合}]$

* **【定義 1】 商環 (Quotient ring)：** 同餘類全體，配上由代表元誘導的兩個運算

  * (a) 底層集合：

    $$R/I \overset{\text{def}}{=} \left\{a + I \ \middle|\ a \in R\right\}$$

  * (b) 加法：

    $$\left(a + I\right) + \left(b + I\right) \overset{\text{def}}{=} \left(a + b\right) + I$$

  * (c) 乘法：

    $$\left(a + I\right) \times \left(b + I\right) \overset{\text{def}}{=} \left(ab\right) + I$$

  * $R/I$ : 商環 (The quotient ring) $[\text{集合}]$
  * $R$ : 母環的底層集合 (The underlying set of the ambient ring) $[\text{集合}]$
  * $I$ : $R$ 的理想 (An ideal of $R$) $[I \trianglelefteq R]$
  * $a,\ b$ : 代表元 (Representatives) $[a, b \in R]$
  * 註：(b)(c) 是**用代表元下的定義**，所以必須先證良定義（【證明 (a)(b)】），
    否則這兩行只是符號遊戲。
  * 註：投影片 p.40 的寫法完全相同。

* **【假設 1】 換代表元 (Changing representatives)：** 【證明 (a)(b)】的出發點。設兩組代表元描述同一對同餘類

  $$a + I = a' + I, \qquad b + I = b' + I$$

  * $a,\ a',\ b,\ b'$ : 兩組代表元 (Two sets of representatives) $[a, a', b, b' \in R]$
  * $I$ : $R$ 的理想 (An ideal of $R$) $[I \trianglelefteq R]$
  * 註：依【已知 2(c)】，這等價於 $a - a' \in I$ 且 $b - b' \in I$。
    良定義要證的是「換成 $a', b'$ 算出來的結果與用 $a, b$ 算出來的**是同一個同餘類**」。

+++

## 證明:

### (a) proof that addition is well defined

由【假設 1】與【已知 2(c)】，兩個差都落在 $I$ 裡。把兩個和相減：

$$\begin{gather*}
a - a' &\overset{\text{假設 1,已知 2(c)}}{\in}& I \\
b - b' &\overset{\text{假設 1,已知 2(c)}}{\in}& I \\
\left(a + b\right) - \left(a' + b'\right) &\overset{\text{已知 3}}{=}& \left(a - a'\right) + \left(b - b'\right) \\
\left(a + b\right) - \left(a' + b'\right) &\overset{\text{已知 1(a)}}{\in}& I \qquad \text{(理想對加法封閉)} \\
\left(a + b\right) + I &\overset{\text{已知 2(c)}}{=}& \left(a' + b'\right) + I
\end{gather*}$$

換代表元得到同一個類，故【定義 1(b)】的加法良定義。

* 註：**這一段只用到【已知 1(a)】（加法子群）**，沒用到吸收性 ——
  所以任何加法子群都能定義商的加法。這就是群論裡商群的情形。

### (b) proof that multiplication is well defined

同樣把兩個乘積相減。關鍵技巧是**加減同一項把差拆成兩段**：

$$\begin{gather*}
ab - a'b' &=& ab - a'b + a'b - a'b' \\
ab - a'b' &\overset{\text{已知 3}}{=}& \left(a - a'\right)b + a'\left(b - b'\right)
\end{gather*}$$

兩段各自由吸收性落在 $I$ 裡：

$$\begin{gather*}
a - a' &\overset{\text{已知 2(c)}}{\in}& I \\
\left(a - a'\right)b &\overset{\text{已知 1(b)}}{\in}& I \qquad \text{(吸收性，} b \in R\text{)} \\
b - b' &\overset{\text{已知 2(c)}}{\in}& I \\
a'\left(b - b'\right) &\overset{\text{已知 1(b)}}{\in}& I \qquad \text{(吸收性，} a' \in R\text{)} \\
ab - a'b' &\overset{\text{已知 1(a)}}{\in}& I \qquad \text{(兩段相加仍在 } I \text{ 內)} \\
\left(ab\right) + I &\overset{\text{已知 2(c)}}{=}& \left(a'b'\right) + I
\end{gather*}$$

故【定義 1(c)】的乘法良定義。

* 註：**這就是理想必須有吸收性的唯一理由。** 注意兩次使用吸收性時，
  $b$ 與 $a'$ 都是**母環 $R$ 的任意元素**，不保證落在 $I$ 裡 ——
  子環只保證「$I$ 內部相乘還在 $I$」，救不了這裡。
* 註：拆項的技巧（$ab - a'b' = (a-a')b + a'(b-b')$）在分析裡叫「加減同一項」，
  在代數裡則是驗證良定義的標準手法。

### (c) proof that the quotient is a ring

環的四條公理逐條從 $R$ 繼承 —— 每一條都是「把代表元的等式套上 $+I$」：

$$\begin{gather*}
\left(a+I\right) + \left(b+I\right) &\overset{\text{定義 1(b)}}{=}& \left(a+b\right)+I = \left(b+a\right)+I = \left(b+I\right)+\left(a+I\right) \qquad \text{(加法交換)} \\
0 + I &\overset{\text{定義 1(b)}}{=}& \text{加法單位元素} \qquad \text{(因 } \left(a+I\right)+\left(0+I\right) = a+I\text{)} \\
\left(-a\right) + I &\overset{\text{定義 1(b)}}{=}& \text{加法反元素} \qquad \text{(因 } \left(a+I\right)+\left(\left(-a\right)+I\right) = 0+I\text{)} \\
\left[\left(a+I\right)\left(b+I\right)\right]\left(c+I\right) &\overset{\text{定義 1(c),已知 3}}{=}& \left(a+I\right)\left[\left(b+I\right)\left(c+I\right)\right] \qquad \text{(乘法結合)} \\
\left(a+I\right)\left[\left(b+I\right)+\left(c+I\right)\right] &\overset{\text{定義 1(b)(c),已知 3}}{=}& \left(a+I\right)\left(b+I\right) + \left(a+I\right)\left(c+I\right) \qquad \text{(分配律)}
\end{gather*}$$

四條全中（加法結合律同理），故 $R/I$ 是環。

* 註：每一條的證明都是同一個模式 —— **把括號裡的運算換成代表元的運算，
  套用 $R$ 的對應公理，再包回 $+I$**。良定義（【證明 (a)(b)】）保證這個過程合法。
* 註：$R$ 若交換、含 $1$，則 $R/I$ 也交換、含 $1 + I$ —— 同樣由代表元繼承。

### (d) verify the two extreme quotients

**$R/R \cong \left\{0\right\}$。** 取 $I = R$，任何 $a$ 的同餘類都是整個 $R$：

$$\begin{gather*}
a - 0 = a &\in& R \\
a + R &\overset{\text{已知 2(c)}}{=}& 0 + R \qquad \text{for all } a \in R \\
R/R &\overset{\text{定義 1(a)}}{=}& \left\{R\right\} \\
\left|R/R\right| &=& 1
\end{gather*}$$

只有一個元素的環就是零環，故 $R/R \cong \left\{0\right\}$。

**$R/\left\{0\right\} \cong R$。** 取 $I = \left\{0\right\}$，每個同餘類只含一個元素：

$$\begin{gather*}
a + \left\{0\right\} &\overset{\text{已知 2(b)}}{=}& \left\{a\right\} \\
a + \left\{0\right\} = b + \left\{0\right\} &\overset{\text{已知 2(c)}}{\Longleftrightarrow}& a - b \in \left\{0\right\} \\
a + \left\{0\right\} = b + \left\{0\right\} &\Longleftrightarrow& a = b
\end{gather*}$$

映射 $a \mapsto a + \left\{0\right\}$ 是雙射，且由【定義 1(b)(c)】保運算：

$$\begin{gather*}
a \mapsto a + \left\{0\right\} &\overset{\text{已知 4}}{=}& \text{環同構} \\
R/\left\{0\right\} &\cong& R
\end{gather*}$$

兩者都與投影片一致。

* 註：這兩個極端說明了商環的意義 —— **$I$ 越大，$R/I$ 越小**。
  $I = R$ 時把一切壓成一點，$I = \left\{0\right\}$ 時什麼都不壓。

### (e) proof that the integers modulo the multiples of n form the ring of residues

定義映射把同餘類送到它的標準代表元：

$$\psi : \mathbf{Z}/n\mathbf{Z} \to \mathbf{Z}_n, \qquad \psi\left(a + n\mathbf{Z}\right) = a \bmod n$$

**良定義且單射**：由【已知 2(c)】與【已知 5(a)】，兩個類相等等價於餘數相同：

$$\begin{gather*}
a + n\mathbf{Z} = b + n\mathbf{Z} &\overset{\text{已知 2(c)}}{\Longleftrightarrow}& a - b \in n\mathbf{Z} \\
a - b \in n\mathbf{Z} &\Longleftrightarrow& n \mid \left(a - b\right) \\
n \mid \left(a - b\right) &\overset{\text{已知 5(a)}}{\Longleftrightarrow}& a \bmod n = b \bmod n
\end{gather*}$$

由左往右讀是良定義（相等的類送到相同的值），由右往左讀是單射。

**滿射**：每個 $r \in \left\{0, \dots, n-1\right\}$ 都是 $\psi\left(r + n\mathbf{Z}\right)$。

**保運算**：由【定義 1(b)(c)】與【已知 5(b)】：

$$\begin{gather*}
\psi\left(\left(a + n\mathbf{Z}\right) + \left(b + n\mathbf{Z}\right)\right) &\overset{\text{定義 1(b)}}{=}& \psi\left(\left(a+b\right) + n\mathbf{Z}\right) \\
\psi\left(\left(a + n\mathbf{Z}\right) + \left(b + n\mathbf{Z}\right)\right) &=& \left(a + b\right) \bmod n \\
\psi\left(\left(a + n\mathbf{Z}\right) + \left(b + n\mathbf{Z}\right)\right) &\overset{\text{已知 5(b)}}{=}& \left(a \bmod n\right) \oplus \left(b \bmod n\right) \\
\psi\left(\left(a + n\mathbf{Z}\right)\left(b + n\mathbf{Z}\right)\right) &\overset{\text{定義 1(c)}}{=}& \psi\left(ab + n\mathbf{Z}\right) \\
\psi\left(\left(a + n\mathbf{Z}\right)\left(b + n\mathbf{Z}\right)\right) &=& \left(ab\right) \bmod n \\
\psi\left(\left(a + n\mathbf{Z}\right)\left(b + n\mathbf{Z}\right)\right) &\overset{\text{已知 5(b)}}{=}& \left(a \bmod n\right) \otimes \left(b \bmod n\right)
\end{gather*}$$

雙射 + 保兩個運算，故依【已知 4】：

$$\mathbf{Z}/n\mathbf{Z} \cong \mathbf{Z}_n$$

與投影片一致。

* 註：**這條同構是整章最重要的一個**。它說明 [數系與符號約定](../Number_Sets_and_Notation.md)【定義 3】
  那個「$\mathbf{Z}_n = \left\{0,1,\dots,n-1\right\}$」的樸素寫法，
  正式身分就是「$\mathbf{Z}$ 對理想 $n\mathbf{Z}$ 的商環」。
  兩種看法在本檔正式接軌。

+++

## 意義與密碼學關聯 (Interpretation and Relevance to Cryptography)

### 「取模」的正式定義

本檔把貫穿全章的線索封口了：

$$\underbrace{x \bmod n}_{\text{程式}} \ = \ \underbrace{x + n\mathbf{Z}}_{\text{同餘類}} \ = \ \underbrace{\text{$\mathbf{Z}/n\mathbf{Z}$ 的一個元素}}_{\text{商環}}$$

**`%` 運算子在做的事，就是取商環的標準代表元。**

而 $\mathbf{Z}_n$ 之所以是環（可以加減乘），不是因為「取模剛好有這些性質」，
而是因為 $n\mathbf{Z}$ 是理想，由【證明 (c)】商環必定是環。**性質是被證出來的，不是碰巧的。**

### 吸收性買到了什麼

【證明 (b)】是全章最能說明「為什麼要發明理想」的一段。

若 $I$ 只是子環（內部乘法封閉），$\left(a-a'\right)b$ 這一項就失控了 ——
$b$ 是母環的任意元素，可能把結果甩出 $I$ 外。
於是「換代表元會得到不同答案」，乘法根本無法定義。

$$\text{子環} \ \Rightarrow \ \text{商的加法可定義，乘法不行}$$
$$\text{理想} \ \Rightarrow \ \text{兩個都可以}$$

**這就是為什麼 [理想](Ideal.md)【證明 (g)】的三個反例（$\mathbf{Z} \subseteq \mathbf{Q}$ 等）重要** ——
$\mathbf{Q}/\mathbf{Z}$ 作為**環**是沒有意義的（雖然作為群有意義）。

### 密碼學裡的每一個商環

| 演算法 | 商環 | 理想 |
|---|---|---|
| RSA | $\mathbf{Z}/n\mathbf{Z}$（$n = pq$） | $n\mathbf{Z}$ |
| Diffie–Hellman | $\mathbf{Z}/p\mathbf{Z}$ | $p\mathbf{Z}$ |
| AES | $\mathbf{Z}_2[x] / \left\langle x^8+x^4+x^3+x+1 \right\rangle$ | $\left\langle x^8+x^4+x^3+x+1 \right\rangle$ |
| Kyber / Dilithium | $\mathbf{Z}_q[x] / \left\langle x^{256}+1 \right\rangle$ | $\left\langle x^{256}+1 \right\rangle$ |
| NTRU | $\mathbf{Z}_q[x] / \left\langle x^N-1 \right\rangle$ | $\left\langle x^N-1 \right\rangle$ |

**整個現代密碼學都活在商環裡。** 每一列的右欄都是 [主理想](Principal_Ideal.md)，
所以【證明 (c)】保證左欄全部是環，可以放心加減乘。

### $I$ 越大、$R/I$ 越小：安全性的權衡

【證明 (d)】的兩個極端說明了一個實際的權衡：

* $n$ 太小 $\Rightarrow$ $\mathbf{Z}/n\mathbf{Z}$ 太小 $\Rightarrow$ 金鑰空間不夠，可窮舉；
* $n$ 太大 $\Rightarrow$ 運算太慢。

RSA-2048 的 $n$ 是 $2048$ 位元，$\left|\mathbf{Z}/n\mathbf{Z}\right| = n \approx 2^{2048}$ ——
這個數字就是【模理想的同餘類】文末說的指標 $\left[\mathbf{Z} : n\mathbf{Z}\right]$。

**「金鑰長度」這個參數，數學上就是在選理想的大小。**

### 程式思維：商環就是「帶標準化的型別」

```python
class ZmodN:
    """Z/nZ 的實作。每個實例存標準代表元。"""
    def __init__(self, a, n):
        self.n = n
        self.a = a % n                       # 正規化：挑標準代表元
    def __add__(self, o):                    # 定義 1(b)
        return ZmodN(self.a + o.a, self.n)
    def __mul__(self, o):                    # 定義 1(c)
        return ZmodN(self.a * o.a, self.n)
    def __eq__(self, o):                     # 已知 2(c)
        return (self.a - o.a) % self.n == 0
```

`__init__` 裡的 `a % n` 就是**選代表元**；
`__add__`、`__mul__` 直接用代表元運算再正規化 —— 而這樣做合法的理由，
正是【證明 (a)(b)】的良定義。

若 $n\mathbf{Z}$ 不是理想，上面 `__mul__` 的結果會依賴 `self.a` 挑了哪個代表元，
整個類別就壞了。
