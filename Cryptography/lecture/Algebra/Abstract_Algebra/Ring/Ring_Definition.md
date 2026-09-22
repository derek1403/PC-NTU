# Ring Definition (環的定義)

+++

## 本檔目標:

`Algebra.pdf` p.26。群只有**一個**運算；環有**兩個**。多出來的那個乘法不像加法那麼講究 ——
它不要求有反元素、甚至不要求交換。

* (a) 環的四條公理：

$$\left(R, +\right) \ \text{為阿貝爾群}, \quad \times \ \text{封閉}, \quad \times \ \text{結合}, \quad \text{分配律}$$

* (b) 一個環記作 $\left(R, +, \times\right)$ —— **一個集合配上兩個運算**。

* $R$ : 環的底層集合 (The underlying set of the ring) $[\text{集合}]$
* $+,\ \times$ : 環的加法與乘法 (The addition and multiplication of the ring) $[R \times R \to R]$
* $a,\ b,\ c$ : 環元素 (Ring elements) $[a, b, c \in R]$
* 註：本檔**只有定義，沒有證明**。具體例子見 [環的例子](Ring_Examples.md)。
* 註：**加法與乘法的地位極不對稱**：
  加法要求構成阿貝爾群（有單位元素 $0$、有反元素 $-a$、交換），
  乘法只要求封閉與結合 —— **不要求有單位元素 $1$、不要求有反元素、不要求交換**。
  這三項各自補上會得到更強的結構，見 [含單位元環與交換環](Ring_with_Identity_and_Commutative_Ring.md)
  與 [體的定義](../Field/Field_Definition.md)。
* 註：分配律是**唯一**把兩個運算綁在一起的公理。沒有它，$\left(R,+\right)$ 與 $\left(R,\times\right)$
  只是兩個各自獨立的結構，湊在一起沒有意義。

+++

## 定義與符號 (Definitions and Notation)

* **【定義 1】 環 (Ring)：** 一個集合 $R$ 配上兩個二元運算 $+$ 與 $\times$，滿足以下四條公理

  * (a) $\left(R, +\right)$ 是阿貝爾群：

    $$a + b \in R, \quad a + \left(b + c\right) = \left(a + b\right) + c, \quad a + 0 = a, \quad a + \left(-a\right) = 0, \quad a + b = b + a$$

  * (b) 乘法封閉：

    $$a \times b \in R \qquad \text{for all } a, b \in R$$

  * (c) 乘法結合：

    $$a \times \left(b \times c\right) = \left(a \times b\right) \times c \qquad \text{for all } a, b, c \in R$$

  * (d) 分配律（**左右各一條**）：

    $$a \times \left(b + c\right) = a \times b + a \times c, \qquad \left(a + b\right) \times c = a \times c + b \times c$$

  * $R$ : 環的底層集合 (The underlying set of the ring) $[\text{集合}]$
  * $+,\ \times$ : 環的加法與乘法 (The addition and multiplication of the ring) $[R \times R \to R]$
  * $a,\ b,\ c$ : 環元素 (Ring elements) $[a, b, c \in R]$
  * $0$ : 加法單位元素（**零元素**）(The additive identity, the zero element) $[0 \in R]$
  * $-a$ : $a$ 的加法反元素 (The additive inverse of $a$) $[-a \in R]$
  * 註：(a) 的五個條件就是 [群的定義](../Group/Group_Definition.md)【定義 2】的四條公理
    加上 [阿貝爾群與非阿貝爾群](../Group/Abelian_and_Non_Abelian_Group.md)【定義 1】的交換律，
    只是換成加法記號。本檔不重複展開。
  * 註：(d) 的**兩條分配律缺一不可**。乘法不交換時，
    $a \times \left(b+c\right)$ 與 $\left(b+c\right) \times a$ 是兩件不同的事。
  * 註：$0$ 與 $-a$ 的**唯一性**已由 [單位元素唯一](../Group/Uniqueness_of_Identity.md) 與
    [反元素唯一](../Group/Uniqueness_of_Inverse.md) 保證（把那兩個結論套在 $\left(R,+\right)$ 上），
    故記號 $0$ 與 $-a$ 是合法的。

* **【定義 2】 減法與乘法記號 (Subtraction and multiplicative notation)：** 環裡的減法由加法反元素定義

  * (a) 減法：

    $$a - b \overset{\text{def}}{=} a + \left(-b\right)$$

  * (b) 乘法簡寫：

    $$ab \overset{\text{def}}{=} a \times b$$

  * (c) 整數倍與冪次：

    $$na \overset{\text{def}}{=} \underbrace{a + \cdots + a}_{n \ \text{個}}, \qquad a^n \overset{\text{def}}{=} \underbrace{a \times \cdots \times a}_{n \ \text{個}} \qquad \left(n \in \mathbf{P}\right)$$

  * $a,\ b$ : 環元素 (Ring elements) $[a, b \in R]$
  * $-b$ : $b$ 的加法反元素 (The additive inverse of $b$) $[-b \in R]$
  * $n$ : 正整數 (A positive integer) $[n \in \mathbf{P}]$
  * 註：(c) 的 $na$ **不是**環的乘法（$n$ 未必是 $R$ 的元素），而是「加 $n$ 次」的簡寫。
    這個區別在 [體的特徵](../Field/Characteristic_of_a_Field.md) 會變得關鍵。
  * 註：$a^n$ 只對 $n \in \mathbf{P}$ 有定義。$a^0$ 需要乘法單位元素、$a^{-n}$ 需要乘法反元素，
    兩者環都不保證有。

+++

## 意義與密碼學關聯 (Interpretation and Relevance to Cryptography)

### 環＝「可以加減乘，但不保證能除」

一句話記住環是什麼：

$$\text{環} = \text{可以} + - \times \text{，但不保證可以} \div$$

熟悉的例子恰好說明了這件事：

| 結構 | 加減乘 | 除 |
|---|---|---|
| $\mathbf{Z}$ | 都可以 | **不行**（$1/2 \notin \mathbf{Z}$）$\to$ 是環，不是體 |
| $\mathbf{Q}$ | 都可以 | 可以（除了除以 $0$）$\to$ 是體 |
| $\mathbf{Z}_6$ | 都可以 | **不行**（$2$ 沒有反元素）$\to$ 是環，不是體 |
| $\mathbf{Z}_7$ | 都可以 | 可以 $\to$ 是體 |

**「能不能除」就是環與體唯一的分界線**，見 [體的定義](../Field/Field_Definition.md)。

### 為什麼加法要求比乘法嚴格

這個不對稱看起來很怪，但它忠實反映了**整數的實情**：

* 整數的加法確實構成阿貝爾群 —— 每個數都有相反數；
* 整數的乘法確實只有封閉與結合 —— 除了 $\pm 1$ 沒人有倒數。

環的公理是從 $\mathbf{Z}$ 抽象出來的，所以照抄了 $\mathbf{Z}$ 的性質。
**環論就是「整數算術」的一般化**，這也是為什麼它在密碼學裡無所不在 ——
密碼學的底層幾乎全是整數運算。

### 密碼學裡的環

| 環 | 出現在 |
|---|---|
| $\mathbf{Z}_n$（$n = pq$） | RSA 的明文與密文空間 |
| $\mathbf{Z}_2[x]$ | CRC 校驗、LFSR、AES 的 $GF(2^8)$ 建構 |
| $\mathbf{Z}_q[x]/\left(x^N - 1\right)$ | NTRU、Kyber 等後量子格密碼 |
| $\mathbf{Z}[i]$（高斯整數） | 某些整數分解演算法 |

**格密碼（後量子密碼的主流）整個建立在多項式環上**，
所以 [環的例子](Ring_Examples.md) 裡的 $R[x]$ 與
[商環](Quotient_Ring.md) 的 $R/I$ 不是純理論 —— 它們是 NIST 標準演算法的骨架。

### 程式思維

環在程式裡對應到「支援 `+ - *` 但不支援 `/` 的型別」：

```python
# Python 的 int 就是環 Z 的實作
7 + 3, 7 - 3, 7 * 3      # 都留在 int 裡（封閉）
7 / 3                     # 跑出 int 變成 float —— 除法不封閉

# Z_n 的實作
(a + b) % n, (a - b) % n, (a * b) % n   # 封閉
# 除法要先問「有沒有反元素」：pow(b, -1, n) 可能丟 ValueError
```

`7 / 3` 會變成 `float` 這件事，就是「$\mathbf{Z}$ 對除法不封閉」的程式版本。
Python 另外提供 `//` 是因為整數除法**不是環運算**，而是帶餘除法 ——
那屬於 [Arithmetic](../../Arithmatic/Arithmetic.ipynb) 的範圍。
