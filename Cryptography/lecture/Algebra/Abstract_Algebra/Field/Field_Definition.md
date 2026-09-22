# Field Definition (體的定義)

+++

## 證明目標:

`Algebra.pdf` p.45。環的最後一塊拼圖 —— 把「乘法反元素」補上去。
補上之後，加減乘除四則運算全部可用，這就是**體**。

* (a) $\mathbf{Q}, \mathbf{R}, \mathbf{C}$ 是體。
* (b) $\mathbf{Z}_p$（$p$ 為質數）是體，亦記作 $\mathbf{F}_p$ 或 $GF(p)$：

$$\mathbf{Z}_p \ \text{為體} \quad \Longleftrightarrow \quad p \ \text{為質數}$$

* (c) $\mathbf{Z}$ **不是**體，因為 $2^{-1} \notin \mathbf{Z}$。
* (d) **體必為整環**（投影片未列，但說明了兩個概念的關係）：

$$F \ \text{為體} \quad \Longrightarrow \quad F \ \text{為整環}$$

* $F$ : 體的底層集合 (The underlying set of the field) $[\text{集合}]$
* $R$ : 環的底層集合 (The underlying set of the ring) $[\text{集合}]$
* $a,\ b$ : 環元素 (Ring elements) $[a, b \in R]$
* $a^{-1}$ : $a$ 的乘法反元素 (The multiplicative inverse of $a$) $[a^{-1} \in F]$
* $p$ : 質數 (A prime) $[p \in \mathbf{P}]$
* $\mathbf{Z}_p$ : 模 $p$ 剩餘類環 (The ring of residues modulo $p$) $[\text{集合}]$
* 註：依投影片 p.30 的約定，「環」一律指**交換的含單位元環**，故體的定義只需補「非零元素可逆」一條。
* 註：(d) 的逆命題**不成立** —— $\mathbf{Z}$ 是整環但不是體（【證明 (c)】）。
  不過**有限**整環必為體（Wedderburn 的一個推論），本章不證。
* 註：投影片 p.45 提到 $GF(2^8)$ 用於 AES。$GF(2^8)$ **不是** $\mathbf{Z}_{256}$
  （$256$ 不是質數，$\mathbf{Z}_{256}$ 不是體），而是
  [模不可約多項式的商環是體](Quotient_by_Irreducible_is_Field.md) 造出來的，見文末。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [環與交換含單位元環 (Rings, commutative rings with identity)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Ring/Ring_with_Identity_and_Commutative_Ring.html#assumptions-preliminaries)：** 已於本章 [環的定義](../Ring/Ring_Definition.md)【定義 1】與 [含單位元環與交換環](../Ring/Ring_with_Identity_and_Commutative_Ring.md)【定義 1】【定義 2】給出，此處直接引用

  * (a) 環公理：

    $$\left(R, +\right) \ \text{阿貝爾群}, \quad ab \in R, \quad a\left(bc\right) = \left(ab\right)c, \quad a\left(b+c\right) = ab+ac$$

  * (b) 含單位元且交換（投影片 p.30 的約定）：

    $$a \times 1 = 1 \times a = a, \qquad ab = ba$$

  * $R$ : 環的底層集合 (The underlying set of the ring) $[\text{集合}]$
  * $a,\ b,\ c$ : 環元素 (Ring elements) $[a, b, c \in R]$
  * $1$ : 乘法單位元素 (The multiplicative identity) $[1 \in R]$

* **【已知 2】 [模逆元存在的充要條件 (Criterion for the existence of a modular inverse)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Number_Sets_and_Notation.html#assumptions-preliminaries)：** 已於本章 [數系與符號約定](../Number_Sets_and_Notation.md)【已知 3】引用，此處再次引用

  $$\exists\, b \in \mathbf{Z}_n \ \text{ such that } \ ab \equiv 1 \pmod{n} \quad \Longleftrightarrow \quad \gcd(a, n) = 1$$

  * $a,\ b$ : 剩餘類代表元 (Residue representatives) $[a, b \in \mathbf{Z}_n]$
  * $n$ : 模數 (Modulus) $[n \in \mathbf{P}]$
  * $\gcd$ : 最大公因數 (Greatest common divisor) $[\mathbf{Z} \times \mathbf{Z} \to \mathbf{N}]$

* **【已知 3】 [模 $n$ 剩餘類環與質數模的可逆性 (The ring of residues and invertibility modulo a prime)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Ring/Ring_Examples.html#c-verify-that-the-residues-modulo-n-form-a-ring)：** 已於本章 [環的例子](../Ring/Ring_Examples.md)【證明 (c)】與 [群的正例與反例](../Group/Group_Examples_and_Counterexamples.md)【證明 (f)】完整證明，此處直接引用不再重證

  * (a) $\mathbf{Z}_n$ 是環：

    $$\mathbf{Z}_n = \left\{0, 1, \dots, n-1\right\} \ \text{ 配 } \oplus, \otimes \ \text{ 是交換含單位元環}$$

  * (b) 質數模下的可逆元素：

    $$\mathbf{Z}_p^* = \left\{1, 2, \dots, p-1\right\} \qquad \left(p \ \text{為質數}\right)$$

  * $\mathbf{Z}_n$ : 模 $n$ 剩餘類環 (The ring of residues modulo $n$) $[\text{集合}]$
  * $\mathbf{Z}_p^*$ : 模 $p$ 可逆剩餘類集合 (The set of units modulo $p$) $[\text{集合}]$
  * $p$ : 質數 (A prime) $[p \in \mathbf{P}]$
  * $n$ : 模數 (Modulus) $[n \in \mathbf{P}]$

* **【已知 4】 [零因子與整環 (Zero divisors and integral domains)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Ring/Zero_Divisor.html#b-proof-of-the-criterion-for-the-existence-of-zero-divisors-modulo-n)：** 已於本章 [零因子](../Ring/Zero_Divisor.md)【定義 1】【證明 (b)】與 [整環](../Ring/Integral_Domain.md)【定義 1】給出並證明，此處直接引用不再重證

  * (a) 零因子的定義與整環：

    $$a, b \ \text{為零因子} \Leftrightarrow a \neq 0,\ b \neq 0,\ ab = 0; \qquad R \ \text{為整環} \Leftrightarrow R \ \text{無零因子}$$

  * (b) $\mathbf{Z}_n$ 有零因子的充要條件：

    $$\mathbf{Z}_n \ \text{有零因子} \quad \Longleftrightarrow \quad n \ \text{為合數}$$

  * $R$ : 環的底層集合 (The underlying set of the ring) $[\text{集合}]$
  * $a,\ b$ : 環元素 (Ring elements) $[a, b \in R]$
  * $n$ : 模數 (Modulus) $[n \in \mathbf{P}]$

* **【定義 1】 體 (Field)：** 每個非零元素都有乘法反元素的環

  $$F \ \text{為體} \quad \overset{\text{def}}{\Longleftrightarrow} \quad F \ \text{為交換含單位元環，且 } \forall\, a \in F \setminus \left\{0\right\},\ \exists\, a^{-1} \in F \ \text{ with } \ a a^{-1} = 1$$

  * $F$ : 體的底層集合 (The underlying set of the field) $[\text{集合}]$
  * $a$ : 非零體元素 (A non-zero field element) $[a \in F \setminus \left\{0\right\}]$
  * $a^{-1}$ : $a$ 的乘法反元素 (The multiplicative inverse of $a$) $[a^{-1} \in F]$
  * $1$ : 乘法單位元素 (The multiplicative identity) $[1 \in F]$
  * 註：**$0$ 被明確排除**。$0$ 不可能有乘法反元素 ——
    由 [環的基本命題](../Ring/Ring_Basic_Propositions.md)【證明 (a)】，
    $0 \times b = 0 \neq 1$（在非零環裡），故 $0^{-1}$ 不存在。
  * 註：等價的說法是「$\left(F \setminus \left\{0\right\}, \times\right)$ 是阿貝爾群」——
    體就是「加法是阿貝爾群、去掉零之後乘法也是阿貝爾群，兩者用分配律連起來」的結構。

* **【定義 2】 有限體與 Galois 體的記號 (Finite fields and Galois field notation)：**

  $$\mathbf{F}_p = GF(p) \overset{\text{def}}{=} \mathbf{Z}_p \qquad \left(p \ \text{為質數}\right)$$

  * $\mathbf{F}_p,\ GF(p)$ : 階為 $p$ 的有限體 (The finite field of order $p$) $[\text{集合}]$
  * $p$ : 質數 (A prime) $[p \in \mathbf{P}]$
  * 註（**dangling 標註**）：本卡片只是換一套記號，不是推導的依據，故證明段**不會**以
    `\overset{\text{定義 2}}` 引用它。
  * 註：$GF$ 取自 **Galois Field**（伽羅瓦體），紀念 Évariste Galois。
    三個記號 $\mathbf{Z}_p$、$\mathbf{F}_p$、$GF(p)$ 指的是同一個東西，本章視上下文混用。
  * 註：$GF(q)$ 在 $q = p^n$（質數冪）時也有定義，但那時**不是** $\mathbf{Z}_q$ ——
    見 [模不可約多項式的商環是體](Quotient_by_Irreducible_is_Field.md)。

* **【假設 1】 反設：$\mathbf{Z}$ 是體 (Proof by contradiction)：** 【證明 (c)】的出發點

  $$\exists\, b \in \mathbf{Z} \ \text{ such that } \ 2b = 1$$

  * $b$ : $2$ 的假定反元素 (The putative inverse of two) $[b \in \mathbf{Z}]$

+++

## 證明:

### (a) verify that the three number systems are fields

三者都是交換含單位元環（[環的例子](../Ring/Ring_Examples.md)【證明 (a)】），
只需補上非零元素可逆這一條。以 $\mathbf{Q}$ 為代表：

$$\begin{gather*}
a = \frac{p}{q} \neq 0 &\Longrightarrow& p \neq 0 \\
\frac{q}{p} &\in& \mathbf{Q} \qquad \text{(因 } p \neq 0\text{)} \\
\frac{p}{q} \times \frac{q}{p} &=& 1 \\
a^{-1} &\overset{\text{定義 1}}{=}& \frac{q}{p} \in \mathbf{Q} \\
\mathbf{Q} &\overset{\text{定義 1}}{=}& \text{體}
\end{gather*}$$

$\mathbf{R}$ 與 $\mathbf{C}$ 同理（$a^{-1} = 1/a$、$\left(a+bi\right)^{-1} = \dfrac{a - bi}{a^2+b^2}$），
與投影片一致。

### (b) proof that the residues modulo a prime form a field

**($\Leftarrow$) $p$ 為質數推出 $\mathbf{Z}_p$ 是體。** 由【已知 3(a)】它是環；
非零元素的可逆性由【已知 3(b)】直接給出：

$$\begin{gather*}
a &\in& \mathbf{Z}_p \setminus \left\{0\right\} \\
a &\overset{\text{已知 3(b)}}{\in}& \mathbf{Z}_p^* \\
\exists\, a^{-1} \in \mathbf{Z}_p \ \text{ with } \ a a^{-1} &\overset{\text{已知 2}}{=}& 1 \\
\mathbf{Z}_p &\overset{\text{定義 1}}{=}& \text{體}
\end{gather*}$$

**($\Rightarrow$) $\mathbf{Z}_n$ 是體推出 $n$ 為質數。** 證逆否 —— $n$ 為合數時 $\mathbf{Z}_n$ 有零因子，
而零因子不可能可逆：

$$\begin{gather*}
n \ \text{為合數} &\overset{\text{已知 4(b)}}{\Longrightarrow}& \exists\, a, b \neq 0 \ \text{ with } \ ab = 0 \\
a \ \text{可逆} &\Longrightarrow& b = a^{-1}\left(ab\right) = a^{-1} \times 0 = 0 \\
b &\neq& 0 \\
a \ &\text{不可逆}& \\
\mathbf{Z}_n &\overset{\text{定義 1}}{\neq}& \text{體}
\end{gather*}$$

兩個方向都證完。依【定義 2】記作：

$$\mathbf{Z}_p = \mathbf{F}_p = GF(p)$$

與投影片一致。

* 註：**$n = 1$ 的邊界情形**：$\mathbf{Z}_1 = \left\{0\right\}$ 是零環，
  它沒有非零元素，形式上「所有非零元素都可逆」空虛成立 ——
  但依 [環的基本命題](../Ring/Ring_Basic_Propositions.md)【證明 (e)】的約定，
  體要求 $1 \neq 0$，故零環不算體。$1$ 既非質數也非合數，不在敘述範圍內。

### (c) disprove that the integers form a field

$\mathbf{Z}$ 是交換含單位元環，但 $2$ 沒有乘法反元素。反設它有（【假設 1】）：

$$\begin{gather*}
2b &\overset{\text{假設 1}}{=}& 1 \\
b &=& \frac{1}{2} \\
b &\notin& \mathbf{Z} \\
\mathbf{Z} &\overset{\text{定義 1}}{\neq}& \text{體}
\end{gather*}$$

與【假設 1】要求 $b \in \mathbf{Z}$ 矛盾，與投影片的「$\mathbf{Z}$ is not a field, since $2^{-1} \notin \mathbf{Z}$」一致。

* 註：$\mathbf{Z}$ 裡**只有 $\pm 1$ 可逆**。這與
  [含單位元環與交換環](../Ring/Ring_with_Identity_and_Commutative_Ring.md) 文末的三階梯一致 ——
  $\mathbf{Z}$ 有 $1$、交換、無零因子，唯獨缺乘法反元素。

### (d) proof that every field is an integral domain

設 $F$ 是體、$ab = 0$ 且 $a \neq 0$。用 $a^{-1}$ 把 $a$ 消掉：

$$\begin{gather*}
ab &=& 0 \\
a^{-1}\left(ab\right) &=& a^{-1} \times 0 \\
\left(a^{-1}a\right)b &\overset{\text{已知 1(a)}}{=}& 0 \\
1 \times b &\overset{\text{定義 1}}{=}& 0 \\
b &\overset{\text{已知 1(b)}}{=}& 0
\end{gather*}$$

兩個因子不可能同時非零，故依【已知 4(a)】$F$ 無零因子，即 $F$ 是整環。

* 註：$a^{-1} \times 0 = 0$ 用的是 [環的基本命題](../Ring/Ring_Basic_Propositions.md)【證明 (a)】。
* 註：**逆命題不成立** —— $\mathbf{Z}$ 是整環但不是體（【證明 (c)】）。
  整環只保證「可以約分」，體保證「可以除」，後者嚴格更強。

+++

## 意義與密碼學關聯 (Interpretation and Relevance to Cryptography)

### 四則運算全開

體是本章的終點。把三個結構並排：

| 結構 | $+$ | $-$ | $\times$ | $\div$ |
|---|---|---|---|---|
| **群**（加法） | 可以 | 可以 | — | — |
| **環** | 可以 | 可以 | 可以 | **不保證** |
| **體** | 可以 | 可以 | 可以 | **可以**（除了除以 $0$） |

「體」這個中文譯名取自「本體、完備」的意思 —— 它是四則運算完備的結構。
英文 field（德文 Körper「身體」）也是同樣的意象。

### $\mathbf{Z}_p$ 是體、$\mathbf{Z}_n$ 不是：密碼學最重要的分界

【證明 (b)】是全章最實用的結論之一：

$$\boxed{\mathbf{Z}_n \ \text{是體} \quad \Longleftrightarrow \quad n \ \text{是質數}}$$

這一行直接決定了密碼學的參數選擇：

| 場合 | 模數 | 是不是體 | 為什麼這樣選 |
|---|---|---|---|
| Diffie–Hellman、DSA、ECC | 質數 $p$ | **是** | 需要除法（求反元素、解方程） |
| RSA | $n = pq$ | **否** | **刻意的** —— 不是體才難分解 |
| Kyber | $q = 3329$（質數） | **是** | 需要 NTT，而 NTT 需要體 |
| AES | $GF(2^8)$ | **是** | S-box 要取乘法反元素 |

**RSA 是唯一刻意不用體的** —— 因為 $\mathbf{Z}_n$ 的「壞」（有零因子、難分解）
正是它的安全基礎，見 [零因子](../Ring/Zero_Divisor.md) 文末。

### $GF(2^8)$ 不是 $\mathbf{Z}_{256}$

這是初學最常見的誤解。AES 的一個位元組有 $256$ 種值，
但 $\mathbf{Z}_{256}$ **不是體**（$256 = 2^8$ 是合數，由【證明 (b)】）。
例如 $2 \times 128 = 256 \equiv 0$，$2$ 是零因子。

AES 用的是：

$$GF(2^8) = \mathbf{Z}_2[x] \big/ \left\langle x^8 + x^4 + x^3 + x + 1 \right\rangle$$

它**也有 $256$ 個元素，但結構完全不同** —— 加法是 XOR（逐位元），
乘法是多項式乘法後對那個不可約多項式取餘。
這樣造出來的才是體，每個非零元素才有反元素，S-box 才能定義。

為什麼這樣造出來是體？見 [不可約多項式](Irreducible_Polynomial.md) 與
[模不可約多項式的商環是體](Quotient_by_Irreducible_is_Field.md)。

### 有限體的階只能是質數冪

一個經典定理（本章不證）：**有限體的元素個數必定是 $p^n$ 的形式**，
而且每個 $p^n$ 恰好對應一個體（同構意義下）。

所以不存在 $6$ 個元素的體、$10$ 個元素的體。
密碼學裡看到的有限體一律是：

$$GF(2), \quad GF(2^8), \quad GF(2^{128}), \quad GF(p) \ (p \ \text{大質數}), \quad GF(p^2)$$

$GF(2^{128})$ 用在 **AES-GCM 的認證標籤**（GHASH），
$GF(p^2)$ 等擴張體用在**配對密碼學 (pairing-based cryptography)**。

### 程式思維

```python
# 體的判斷：每個非零元素都可逆
def is_field_Zn(n):
    return all(math.gcd(a, n) == 1 for a in range(1, n))   # 已知 2

assert is_field_Zn(7)        # 質數 -> 是體
assert not is_field_Zn(8)    # 合數 -> 不是體（2, 4, 6 不可逆）

# 體裡的除法一定成功
def div(a, b, p):
    assert b % p != 0, "除以零"
    return a * pow(b, -1, p) % p     # p 為質數時 pow(b,-1,p) 永不失敗
```

`pow(b, -1, p)` 在 $p$ 為質數且 $b \not\equiv 0$ 時**保證成功** ——
這就是【證明 (b)】的程式版本。換成合數模數就可能丟 `ValueError`，
所以密碼程式碼裡「模數是質數」這個前提必須在參數驗證時就確立。
