# Ring with Identity and Commutative Ring (含單位元環與交換環)

+++

## 證明目標:

`Algebra.pdf` p.28。[環的定義](Ring_Definition.md) 對乘法只要求封閉與結合。
把「有單位元素」與「交換」各自補回去，就得到兩個更強的名稱。

* (a) $M_n(\mathbf{R})$（$n \ge 2$）**不是**交換環：

$$\begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}\begin{bmatrix} 1 & 0 \\ 1 & 1 \end{bmatrix} \neq \begin{bmatrix} 1 & 0 \\ 1 & 1 \end{bmatrix}\begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}$$

* (b) $2\mathbf{Z}$ **沒有**乘法單位元素。
* (c) 乘法單位元素若存在則**唯一**（故記號 $1$ 合法）。

* $R$ : 環的底層集合 (The underlying set of the ring) $[\text{集合}]$
* $1$ : 乘法單位元素 (The multiplicative identity) $[1 \in R]$
* $a,\ b$ : 環元素 (Ring elements) $[a, b \in R]$
* $M_n(\mathbf{R})$ : 實係數 $n \times n$ 方陣全體 (All real $n \times n$ matrices) $[\text{集合}]$
* $2\mathbf{Z}$ : 偶數集合 (The set of even integers) $[\text{集合}]$
* 註：(a) 與 (b) 是**兩種不同的缺陷**：$M_n(\mathbf{R})$ 有 $1$（單位矩陣）但不交換；
  $2\mathbf{Z}$ 交換但沒有 $1$。**兩個性質互相獨立**，可以各缺各的。
* 註：投影片 p.30 的 Note 宣告「往後的投影片裡，『環』一律指**交換的含單位元環**」。
  本章沿用這個約定，見文末。
* 註：(c) 不在投影片上，但它是記號 $1$ 合法的前提，與
  [單位元素唯一](../Group/Uniqueness_of_Identity.md) 是同一件事的乘法版本。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [環的公理 (Ring axioms)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Ring/Ring_Definition.html#definitions-and-notation)：** 已於本章 [環的定義](Ring_Definition.md)【定義 1】給出，此處直接引用

  $$\left(R, +\right) \ \text{阿貝爾群}, \quad a \times b \in R, \quad a \times \left(b \times c\right) = \left(a \times b\right) \times c, \quad \text{分配律}$$

  * $R$ : 環的底層集合 (The underlying set of the ring) $[\text{集合}]$
  * $a,\ b,\ c$ : 環元素 (Ring elements) $[a, b, c \in R]$
  * 註：公理裡**沒有**乘法單位元素、沒有乘法反元素、沒有乘法交換律 —— 這正是本檔要補的三件事中的兩件。

* **【已知 2】 [單位元素唯一 (Uniqueness of the identity)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Group/Uniqueness_of_Identity.html#a-proof-uniqueness-of-the-identity-element)：** 已於本章 [單位元素唯一](../Group/Uniqueness_of_Identity.md)【證明 (a)】完整證明，此處直接引用不再重證。該證明**只用到單位元素公理一條**，故對任何帶單位元素的運算都適用，不限於群

  $$e_1 = e_2 \qquad \text{for any two identities } e_1, e_2$$

  * $e_1,\ e_2$ : 兩個單位元素 (Two identity elements) $[e_1, e_2 \in R]$
  * $R$ : 底層集合 (The underlying set) $[\text{集合}]$

* **【已知 3】 [矩陣乘法不交換 (Non-commutativity of matrix multiplication)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Group/Abelian_and_Non_Abelian_Group.html#c-disprove-commutativity-of-the-general-and-special-linear-groups)：** 已於本章 [阿貝爾群與非阿貝爾群](../Group/Abelian_and_Non_Abelian_Group.md)【證明 (c)】逐格計算並證明，此處直接引用不再重證

  $$\begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}\begin{bmatrix} 1 & 0 \\ 1 & 1 \end{bmatrix} = \begin{bmatrix} 2 & 1 \\ 1 & 1 \end{bmatrix}, \qquad \begin{bmatrix} 1 & 0 \\ 1 & 1 \end{bmatrix}\begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix} = \begin{bmatrix} 1 & 1 \\ 1 & 2 \end{bmatrix}$$

  * $M_n(\mathbf{R})$ : 實係數 $n \times n$ 方陣全體 (All real $n \times n$ matrices) $[\text{集合}]$
  * 註：該處證的是 $GL_2(\mathbf{Q}) \subseteq M_2(\mathbf{Q})$ 裡的反例。
    同一組矩陣的元素都是整數，故同時落在 $M_2(\mathbf{R})$ 裡，反例照樣有效。

* **【已知 4】 [偶數集合是環 (The even integers form a ring)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Ring/Ring_Examples.html#b-verify-that-the-multiples-of-a-fixed-integer-form-a-ring)：** 已於本章 [環的例子](Ring_Examples.md)【證明 (b)】完整證明（取 $n = 2$），此處直接引用不再重證

  $$2\mathbf{Z} = \left\{2t \ \middle|\ t \in \mathbf{Z}\right\} \ \text{ 是環}$$

  * $2\mathbf{Z}$ : 偶數集合 (The set of even integers) $[\text{集合}]$
  * $t$ : 整數係數 (Integer coefficient) $[t \in \mathbf{Z}]$

* **【定義 1】 含單位元環 (Ring with identity)：** 乘法也有單位元素

  $$\left(R, +, \times\right) \ \text{為含單位元環} \quad \overset{\text{def}}{\Longleftrightarrow} \quad \exists\, 1 \in R \ \text{ such that } \ a \times 1 = 1 \times a = a \quad \text{for all } a \in R$$

  * $R$ : 環的底層集合 (The underlying set of the ring) $[\text{集合}]$
  * $1$ : 乘法單位元素 (The multiplicative identity) $[1 \in R]$
  * $a$ : 環元素 (A ring element) $[a \in R]$
  * 註：加法單位元素 $0$ 由 [環的定義](Ring_Definition.md)【定義 1(a)】**保證存在**；
    乘法單位元素 $1$ **不保證**，要另外要求，這就是本定義的全部內容。

* **【定義 2】 交換環 (Commutative ring)：** 乘法也交換

  $$\left(R, +, \times\right) \ \text{為交換環} \quad \overset{\text{def}}{\Longleftrightarrow} \quad a \times b = b \times a \quad \text{for all } a, b \in R$$

  * $R$ : 環的底層集合 (The underlying set of the ring) $[\text{集合}]$
  * $a,\ b$ : 環元素 (Ring elements) $[a, b \in R]$
  * 註：加法的交換律由 [環的定義](Ring_Definition.md)【定義 1(a)】保證（阿貝爾群）；
    **本定義說的是乘法**。
  * 註：交換環裡 [環的定義](Ring_Definition.md)【定義 1(d)】的兩條分配律退化成一條 ——
    左分配律加上交換律即得右分配律。

* **【假設 1】 反設：$2\mathbf{Z}$ 有乘法單位元素 (Proof by contradiction)：** 【證明 (b)】的出發點

  $$\exists\, u \in 2\mathbf{Z} \ \text{ such that } \ a \times u = a \quad \text{for all } a \in 2\mathbf{Z}$$

  * $u$ : 假定的乘法單位元素 (The putative multiplicative identity) $[u \in 2\mathbf{Z}]$
  * $a$ : 偶數 (An even integer) $[a \in 2\mathbf{Z}]$
  * $2\mathbf{Z}$ : 偶數集合 (The set of even integers) $[\text{集合}]$

+++

## 證明:

### (a) disprove commutativity of the matrix ring

$M_2(\mathbf{R})$ 是環（依【已知 1】，加法逐格相加構成阿貝爾群、乘法封閉結合、分配律成立）：

$$\begin{gather*}
M_2(\mathbf{R}) &\overset{\text{已知 1}}{=}& \text{環}
\end{gather*}$$

再直接引用【已知 3】的兩個乘積：

$$\begin{gather*}
\begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}\begin{bmatrix} 1 & 0 \\ 1 & 1 \end{bmatrix} &\overset{\text{已知 3}}{=}& \begin{bmatrix} 2 & 1 \\ 1 & 1 \end{bmatrix} \\
\begin{bmatrix} 1 & 0 \\ 1 & 1 \end{bmatrix}\begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix} &\overset{\text{已知 3}}{=}& \begin{bmatrix} 1 & 1 \\ 1 & 2 \end{bmatrix} \\
\begin{bmatrix} 2 & 1 \\ 1 & 1 \end{bmatrix} &\neq& \begin{bmatrix} 1 & 1 \\ 1 & 2 \end{bmatrix} \\
M_2(\mathbf{R}) &\overset{\text{定義 2}}{\neq}& \text{交換環}
\end{gather*}$$

把這兩個矩陣嵌進 $n \times n$ 的左上角、其餘補單位矩陣，同樣的反例對所有 $n \ge 2$ 皆成立。

* 註：$M_n(\mathbf{R})$ **有**乘法單位元素（單位矩陣 $I$），只是不交換 ——
  它是「含單位元環但非交換環」的標準例子。

### (b) disprove the existence of a multiplicative identity in the even integers

反設 $2\mathbf{Z}$ 有乘法單位元素 $u$（【假設 1】），取 $a = 2 \in 2\mathbf{Z}$ 代入：

$$\begin{gather*}
2\mathbf{Z} &\overset{\text{已知 4}}{=}& \text{環} \\
2 \times u &\overset{\text{假設 1}}{=}& 2 \\
u &=& 1 \\
1 &=& 2 \times \frac{1}{2} \\
\frac{1}{2} &\notin& \mathbf{Z} \\
u = 1 &\notin& 2\mathbf{Z}
\end{gather*}$$

與【假設 1】要求 $u \in 2\mathbf{Z}$ 矛盾。故 $2\mathbf{Z}$ 沒有乘法單位元素：

$$2\mathbf{Z} \overset{\text{定義 1}}{\neq} \text{含單位元環}$$

* 註：$2\mathbf{Z}$ **是**交換環（乘法交換律由 $\mathbf{Z}$ 繼承），只是沒有 $1$ ——
  它是「交換環但非含單位元環」的標準例子，與【證明 (a)】恰好互補。
* 註：同樣的論證對任意 $n \ge 2$ 都成立：$n\mathbf{Z}$ 都沒有乘法單位元素。

### (c) proof of the uniqueness of the multiplicative identity

設 $1_1$ 與 $1_2$ 都是 $R$ 的乘法單位元素（【定義 1】）。
[單位元素唯一](../Group/Uniqueness_of_Identity.md)【證明 (a)】的論證**只用到單位元素性質一條**，
與運算是加法還是乘法無關，故可直接套用：

$$\begin{gather*}
1_1 &\overset{\text{定義 1}}{=}& 1_1 \times 1_2 \qquad \text{(把 } 1_2 \text{ 當單位元素看)} \\
1_1 &\overset{\text{定義 1}}{=}& 1_2 \qquad \text{(把 } 1_1 \text{ 當單位元素看)} \\
1_1 &\overset{\text{已知 2}}{=}& 1_2
\end{gather*}$$

故乘法單位元素唯一，記號 $1$ 合法。

* 註：同樣的論證也保證加法單位元素 $0$ 唯一，故記號 $0$ 也合法。
  這在 [環的基本命題](Ring_Basic_Propositions.md) 每一條都會用到。

+++

## 意義與密碼學關聯 (Interpretation and Relevance to Cryptography)

### 三個性質互相獨立

環的乘法可以缺三樣東西，缺法互不相干：

| 缺什麼 | 補上之後叫 | 本章的例子（**只缺這一樣**） |
|---|---|---|
| 乘法單位元素 $1$ | 含單位元環 | $2\mathbf{Z}$（【證明 (b)】） |
| 乘法交換律 | 交換環 | $M_2(\mathbf{R})$（【證明 (a)】） |
| 乘法反元素 | 除環／體 | $\mathbf{Z}$（見 [體的定義](../Field/Field_Definition.md)） |

三樣**全部補上**就是**體**。這就是 [體的定義](../Field/Field_Definition.md) 要做的事，
也是 `Algebra.pdf` 第 3 大段的主題。

### 投影片 p.30 的那個約定

投影片在 [子環](Subring.md) 那一頁宣告：

> **Note** In the remaining slides, "ring" means a **commutative ring with identity**

這個約定在本章之後一律沿用。理由是：接下來的 [理想](Ideal.md)、[商環](Quotient_Ring.md)、
[中國剩餘定理](Chinese_Remainder_Theorem.md) 全部需要交換性
（否則要區分左理想、右理想、雙邊理想，複雜度暴增），
而密碼學用到的環（$\mathbf{Z}_n$、$\mathbf{Z}_q[x]/(f)$）也全都是交換的含單位元環。

**本檔之後，看到「環」就預設它交換且有 $1$。** 需要一般環時會明確說明。

### 為什麼 $1 \neq 0$ 值得單獨拿出來講

[環的基本命題](Ring_Basic_Propositions.md) 會提到 $1 \neq 0$。
乍看廢話，但它排除的是**零環** $R = \left\{0\right\}$ —— 在那個環裡 $1 = 0$，
所有元素都相等，一切命題都空虛成立。

密碼學上這不是學術潔癖：$\mathbf{Z}_1 = \left\{0\right\}$ 就是零環。
若某個實作不小心讓模數 $n = 1$，整個系統的明文空間會塌陷成一個點，
加密變成常數函數。**參數驗證要擋掉 $n = 1$，數學上的理由就在這裡。**

### 程式思維

「有沒有 $1$」在程式裡是一個很實際的問題：

```python
# 含單位元環才有「乘法單位元素」可以當 reduce 的初值
functools.reduce(mul, elements, ONE)   # 需要 ONE 存在

# 2Z 沒有 1，所以空乘積沒有自然的值
functools.reduce(mul, [], ???)         # 無解
```

這也影響冪次：[環的定義](Ring_Definition.md)【定義 2(c)】的 $a^n$ 只對 $n \ge 1$ 有定義，
因為 $a^0 = 1$ 需要 $1$ 存在。在 $2\mathbf{Z}$ 裡寫 `pow(a, 0)` 是沒有意義的。
