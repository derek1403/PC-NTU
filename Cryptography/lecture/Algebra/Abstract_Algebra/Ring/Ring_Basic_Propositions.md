# Ring Basic Propositions (環的基本命題)

+++

## 證明目標:

`Algebra.pdf` p.29。五條「看起來理所當然」的算術規則。它們在 $\mathbf{Z}$ 裡是常識，
但在抽象環裡**必須從公理推出來** —— 而唯一能把加法與乘法連起來的工具只有分配律。

* (a) 任何元素乘以零都是零：

$$a \times 0 = 0 \times a = 0$$

* (b) 負號可以從任一因子提出來：

$$\left(-a\right)b = a\left(-b\right) = -\left(ab\right)$$

* (c) 減法的分配律：

$$a\left(b - c\right) = ab - ac, \qquad \left(a - b\right)c = ac - bc$$

* (d) 含單位元環中，乘以 $-1$ 就是取負：

$$\left(-1\right)a = -a$$

* (e) $1 \neq 0$（**這是約定，不是定理**，見【證明 (e)】）。

* $R$ : 環的底層集合 (The underlying set of the ring) $[\text{集合}]$
* $a,\ b,\ c$ : 環元素 (Ring elements) $[a, b, c \in R]$
* $0$ : 加法單位元素 (The additive identity) $[0 \in R]$
* $1$ : 乘法單位元素 (The multiplicative identity) $[1 \in R]$
* $-a$ : $a$ 的加法反元素 (The additive inverse of $a$) $[-a \in R]$
* 註：五條高度平行，依平行邏輯收束原則全部收在同一檔用 `(a)`–`(e)` 次級編號，
  不拆成五個獨立檔案。
* 註：(a) 是其餘四條的基石 —— (b) 用 (a)、(c) 用 (b)、(d) 用 (b)、(e) 用 (a)。
  **順序不可對調。**
* 註：整條鏈只用到 [環的定義](Ring_Definition.md) 的公理，
  **不需要交換性、不需要 $1$**（除了 (d)(e)）。結論對一般環都成立。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [環的公理 (Ring axioms)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Ring/Ring_Definition.html#definitions-and-notation)：** 已於本章 [環的定義](Ring_Definition.md)【定義 1】給出，此處直接引用

  * (a) $\left(R, +\right)$ 是阿貝爾群，特別是有 $0$ 與 $-a$：

    $$a + 0 = 0 + a = a, \qquad a + \left(-a\right) = 0$$

  * (b) 分配律：

    $$a\left(b + c\right) = ab + ac, \qquad \left(a + b\right)c = ac + bc$$

  * $R$ : 環的底層集合 (The underlying set of the ring) $[\text{集合}]$
  * $a,\ b,\ c$ : 環元素 (Ring elements) $[a, b, c \in R]$
  * $0$ : 加法單位元素 (The additive identity) $[0 \in R]$
  * $-a$ : $a$ 的加法反元素 (The additive inverse of $a$) $[-a \in R]$
  * 註：**(b) 是本檔唯一的工具**。所有五條命題的證明都靠它把乘法的問題轉成加法的問題。

* **【已知 2】 [加法群的消去律 (Cancellation law in the additive group)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Group/Unique_Solution_and_Cancellation_Law.html#a-proof-of-the-left-cancellation-law)：** 已於本章 [唯一解與消去律](../Group/Unique_Solution_and_Cancellation_Law.md)【證明 (a)】對一般群完整證明，此處套在 $\left(R, +\right)$ 上直接引用不再重證

  $$x + y = x + z \quad \Longrightarrow \quad y = z$$

  * $x,\ y,\ z$ : 環元素 (Ring elements) $[x, y, z \in R]$
  * $R$ : 環的底層集合 (The underlying set of the ring) $[\text{集合}]$
  * 註：$\left(R, +\right)$ 依 [環的定義](Ring_Definition.md)【定義 1(a)】是群，故消去律適用。
    **注意這是加法的消去律** —— 乘法的消去律在一般環裡**不成立**，見 [零因子](Zero_Divisor.md)。

* **【已知 3】 [加法反元素唯一 (Uniqueness of the additive inverse)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Group/Uniqueness_of_Inverse.html#a-proof-uniqueness-of-the-inverse-element)：** 已於本章 [反元素唯一](../Group/Uniqueness_of_Inverse.md)【證明 (a)】對一般群完整證明，此處套在 $\left(R, +\right)$ 上直接引用不再重證

  $$x + y = 0 \quad \Longrightarrow \quad y = -x$$

  * $x,\ y$ : 環元素 (Ring elements) $[x, y \in R]$
  * $-x$ : $x$ 的加法反元素 (The additive inverse of $x$) $[-x \in R]$
  * 註：【證明 (b)】的收尾靠這一條 —— 證出某個東西加上 $ab$ 等於 $0$，就能斷定它**是** $-(ab)$。

* **【已知 4】 [乘法單位元素與減法記號 (Multiplicative identity and subtraction notation)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Ring/Ring_with_Identity_and_Commutative_Ring.html#assumptions-preliminaries)：** 已於本章 [含單位元環與交換環](Ring_with_Identity_and_Commutative_Ring.md)【定義 1】與 [環的定義](Ring_Definition.md)【定義 2(a)】給出，此處直接引用

  * (a) 乘法單位元素：

    $$a \times 1 = 1 \times a = a$$

  * (b) 減法：

    $$a - b \overset{\text{def}}{=} a + \left(-b\right)$$

  * $a,\ b$ : 環元素 (Ring elements) $[a, b \in R]$
  * $1$ : 乘法單位元素 (The multiplicative identity) $[1 \in R]$
  * $-b$ : $b$ 的加法反元素 (The additive inverse of $b$) $[-b \in R]$
  * 註：(a) 只在**含單位元環**裡可用，故【證明 (d)(e)】需要這個額外前提，(a)–(c) 不需要。

+++

## 證明:

### (a) proof that multiplication by zero gives zero

起手式是把 $0$ 拆成 $0 + 0$ 塞進分配律 —— 這是**唯一**能讓分配律作用在 $0$ 上的辦法：

$$\begin{gather*}
a \times 0 &\overset{\text{已知 1(a)}}{=}& a\left(0 + 0\right) \\
a \times 0 &\overset{\text{已知 1(b)}}{=}& a \times 0 + a \times 0 \\
a \times 0 + 0 &\overset{\text{已知 1(a)}}{=}& a \times 0 + a \times 0 \\
0 &\overset{\text{已知 2}}{=}& a \times 0
\end{gather*}$$

同理由右分配律得 $0 \times a = 0$：

$$\begin{gather*}
0 \times a &\overset{\text{已知 1(a)}}{=}& \left(0 + 0\right)a \\
0 \times a &\overset{\text{已知 1(b)}}{=}& 0 \times a + 0 \times a \\
0 \times a + 0 &\overset{\text{已知 1(a)}}{=}& 0 \times a + 0 \times a \\
0 &\overset{\text{已知 2}}{=}& 0 \times a
\end{gather*}$$

* 註：**消去律是關鍵一步**。$x = x + x$ 在加法群裡只有 $x = 0$ 這個解，
  這正是【已知 2】在做的事。
* 註：兩個方向都要證，因為一般環的乘法不交換。交換環裡證一個就夠。

### (b) proof that a negative factor pulls the sign out

證明 $\left(-a\right)b$ **是** $ab$ 的加法反元素 —— 也就是兩者相加得 $0$：

$$\begin{gather*}
\left(-a\right)b + ab &\overset{\text{已知 1(b)}}{=}& \left(\left(-a\right) + a\right)b \\
\left(-a\right)b + ab &\overset{\text{已知 1(a)}}{=}& 0 \times b \\
\left(-a\right)b + ab &\overset{\text{證明 (a)}}{=}& 0 \\
\left(-a\right)b &\overset{\text{已知 3}}{=}& -\left(ab\right)
\end{gather*}$$

$a\left(-b\right)$ 完全對稱（改用左分配律）：

$$\begin{gather*}
a\left(-b\right) + ab &\overset{\text{已知 1(b)}}{=}& a\left(\left(-b\right) + b\right) \\
a\left(-b\right) + ab &\overset{\text{已知 1(a)}}{=}& a \times 0 \\
a\left(-b\right) + ab &\overset{\text{證明 (a)}}{=}& 0 \\
a\left(-b\right) &\overset{\text{已知 3}}{=}& -\left(ab\right)
\end{gather*}$$

兩者都等於 $-\left(ab\right)$，故三式相等。

* 註：這是「**驗證資格 + 引用唯一性**」的手法，與
  [乘積的反元素](../Group/Inverse_of_a_Product.md)【證明 (a)】用的是同一個骨架。

### (c) proof of the distributive law over subtraction

把減法展開成「加上反元素」（【已知 4(b)】），套分配律，再用【證明 (b)】把負號收回去：

$$\begin{gather*}
a\left(b - c\right) &\overset{\text{已知 4(b)}}{=}& a\left(b + \left(-c\right)\right) \\
a\left(b - c\right) &\overset{\text{已知 1(b)}}{=}& ab + a\left(-c\right) \\
a\left(b - c\right) &\overset{\text{證明 (b)}}{=}& ab + \left(-\left(ac\right)\right) \\
a\left(b - c\right) &\overset{\text{已知 4(b)}}{=}& ab - ac
\end{gather*}$$

右側版本對稱：

$$\begin{gather*}
\left(a - b\right)c &\overset{\text{已知 4(b)}}{=}& \left(a + \left(-b\right)\right)c \\
\left(a - b\right)c &\overset{\text{已知 1(b)}}{=}& ac + \left(-b\right)c \\
\left(a - b\right)c &\overset{\text{證明 (b)}}{=}& ac + \left(-\left(bc\right)\right) \\
\left(a - b\right)c &\overset{\text{已知 4(b)}}{=}& ac - bc
\end{gather*}$$

* 註：**減法不是環的基本運算**，它是【已知 4(b)】定義出來的簡寫。
  所以「減法的分配律」不是公理，必須像上面這樣推出來。

### (d) proof that multiplying by minus one negates

本小節需要 $R$ 有乘法單位元素。把【證明 (b)】取 $a = 1$、$b = a$：

$$\begin{gather*}
\left(-1\right)a &\overset{\text{證明 (b)}}{=}& -\left(1 \times a\right) \\
\left(-1\right)a &\overset{\text{已知 4(a)}}{=}& -a
\end{gather*}$$

* 註：**$-1$ 指的是 $1$ 的加法反元素**，不是「負一這個整數」。
  在 $\mathbf{Z}_7$ 裡 $-1 = 6$，而 $6 \times a = -a$ 確實成立（例如 $6 \times 3 = 18 = 4 = -3$）。

### (e) discussion of the condition that one differs from zero

**這一條不是定理，是約定。** 投影片把它列在 Proposition 底下，但它無法從環的公理推出來 ——
事實上存在一個環使 $1 = 0$。本小節說明它的真正地位。

設 $R$ 是含單位元環且 $1 = 0$。任取 $a \in R$：

$$\begin{gather*}
a &\overset{\text{已知 4(a)}}{=}& a \times 1 \\
a &=& a \times 0 \qquad \text{(代入 } 1 = 0\text{)} \\
a &\overset{\text{證明 (a)}}{=}& 0 \\
R &=& \left\{0\right\}
\end{gather*}$$

反之，零環 $R = \left\{0\right\}$ 裡 $1 = 0 = 0$ 確實成立。故：

$$1 = 0 \quad \Longleftrightarrow \quad R = \left\{0\right\}$$

換句話說，「$1 \neq 0$」這個條件的**唯一作用是排除零環**。
本章往後（如投影片 p.30 的約定）一律假設 $R \neq \left\{0\right\}$，
因此可以放心地寫 $1 \neq 0$。

* 註：**這是本檔與投影片的一個差異**。投影片把 $1 \neq 0$ 與前四條並列為 Proposition，
  但前四條是可證的定理、這一條是不可證的約定。本檔把它改列為「約定 + 等價刻畫」，
  結論本身沒有改變。

+++

## 意義與密碼學關聯 (Interpretation and Relevance to Cryptography)

### 分配律是唯一的橋

本檔五條命題的證明**沒有一條用到乘法的特殊性質** —— 不需要交換、不需要結合、
（除了 (d)(e)）不需要單位元素。全部只靠一樣東西：

$$a\left(b + c\right) = ab + ac$$

這值得停下來想。環有兩個運算，它們本來毫無關係；分配律是唯一把兩者綁在一起的公理。
於是**任何「同時牽涉加法與乘法」的性質，追根究柢都必須經過分配律**。

【證明 (a)】最能說明這件事：要證 $a \times 0 = 0$，$0$ 是加法的概念、$\times$ 是乘法的運算，
兩者要碰面只能靠分配律。所以起手式必須是把 $0$ 寫成 $0 + 0$ —— 沒有別的路。

### 為什麼 $\mathbf{Z}_7$ 裡 $-1 = 6$

【證明 (d)】的註是實作上最常踩的坑。在 $\mathbf{Z}_n$ 裡：

$$-a = n - a \qquad \left(a \neq 0\right)$$

因為 $a + \left(n - a\right) = n \equiv 0 \pmod n$。所以：

| $n$ | $-1$ | 驗證 |
|---|---|---|
| $7$ | $6$ | $1 + 6 = 7 \equiv 0$ |
| $256$ | $255$ | $1 + 255 = 256 \equiv 0$ |
| $2$ | $1$ | $1 + 1 = 2 \equiv 0$ |

最後一列說明了一件重要的事：**在特徵為 $2$ 的環裡 $-1 = 1$**，
於是加法與減法是同一個運算。這就是為什麼 $GF(2^8)$ 的加法可以直接用 XOR 實作 ——
不必區分加與減。AES 的所有「加法」都是 XOR，理由就在這裡。

### 密碼學上的對應：$a \times 0 = 0$ 是一個安全陷阱

【證明 (a)】說任何元素乘以 $0$ 都得到 $0$。這在密碼學裡是個真實的問題：

**Textbook RSA 的 $0$ 與 $1$**：$0^e \equiv 0$、$1^e \equiv 1$，
所以明文 $0$ 與 $1$ 加密後原封不動。攻擊者一眼就看得出來。

**橢圓曲線的無窮遠點**：若協議沒有檢查對方送來的點是不是 $\mathcal{O}$（群的零元素），
攻擊者可以送 $\mathcal{O}$，讓共享金鑰固定變成 $\mathcal{O}$ ——
雙方會「成功」協商出一把攻擊者已知的金鑰。

**防禦方法都是一樣的：輸入驗證要擋掉零元素。**
這不是實作瑕疵，而是【證明 (a)】這條定理的必然後果 ——
零元素是乘法的吸收元，任何以它為輸入的運算都會塌陷。

### 為什麼要在乎零環

【證明 (e)】說 $1 = 0$ 等價於 $R = \left\{0\right\}$。這看似無聊，但
$\mathbf{Z}_1 = \left\{0\right\}$ 正是零環。

實作上這意味著：**RSA 的模數 $n$ 若被設成 $1$，整個明文空間塌陷成一個點**，
加密函數變成常數。參數驗證必須擋掉 $n \le 1$，數學上的理由就是本小節。
