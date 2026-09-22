# Inverse of a Product (乘積的反元素)

+++

## 證明目標:

* (a) 乘積的反元素等於「反元素**倒過來**相乘」：

$$\left(a * b\right)^{-1} = b^{-1} * a^{-1} \qquad \text{for all } a, b \in G$$

* $G$ : 群的底層集合 (The underlying set of the group) $[\text{集合}]$
* $*$ : 群運算 (Group operation) $[G \times G \to G]$
* $a,\ b$ : 群元素 (Group elements) $[a, b \in G]$
* $a^{-1},\ b^{-1}$ : 對應的反元素 (The corresponding inverses) $[a^{-1}, b^{-1} \in G]$
* 註：**順序一定要顛倒**。$\left(a * b\right)^{-1} = a^{-1} * b^{-1}$ 一般是**錯的** ——
  只有在群可交換時兩者才碰巧相等（見 [阿貝爾群與非阿貝爾群](Abelian_and_Non_Abelian_Group.md)）。
* 註：證明策略是「**驗證資格 + 引用唯一性**」：先算出 $b^{-1} * a^{-1}$ 與 $a * b$ 相乘（左右都要）
  確實得到 $e$，說明它**符合反元素的定義**；再由 [反元素唯一](Uniqueness_of_Inverse.md) 斷定它**就是**那個反元素。
  兩個方向的驗算冗長，依減壓閥原則提前放進【推導 1】【推導 2】。
* 註：同一結論亦見 [Theory_Playground](https://derek1403.github.io/Theory_Playground/_build/html/02_Concepts/Abstract_Algebra/proof_group_fundamental_theory.html)，
  本章依統一風格重新證明一次，以維持引用鏈自洽。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [群的公理 (Group axioms)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Group/Group_Definition.html#definitions-and-notation)：** 已於本章 [群的定義](Group_Definition.md)【定義 2】給出，此處引用其中三條

  * (a) 封閉性：

    $$a * b \in G \qquad \text{for all } a, b \in G$$

  * (b) 結合律：

    $$a * \left(b * c\right) = \left(a * b\right) * c \qquad \text{for all } a, b, c \in G$$

  * (c) 單位元素：

    $$a * e = e * a = a \qquad \text{for all } a \in G$$

  * $G$ : 群的底層集合 (The underlying set of the group) $[\text{集合}]$
  * $*$ : 群運算 (Group operation) $[G \times G \to G]$
  * $a,\ b,\ c$ : 群元素 (Group elements) $[a, b, c \in G]$
  * $e$ : 單位元素 (The identity element) $[e \in G]$
  * 註：(a) 在本檔用來保證 $a * b$ 與 $b^{-1} * a^{-1}$ 都確實落在 $G$ 裡，
    否則談論它們的反元素沒有意義。

* **【已知 2】 [反元素唯一 (Uniqueness of the inverse)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Group/Uniqueness_of_Inverse.html#a-proof-uniqueness-of-the-inverse-element)：** 已於本章 [反元素唯一](Uniqueness_of_Inverse.md)【證明 (a)】完整證明，此處直接引用不再重證

  * (a) 反元素的定義式：

    $$a * a^{-1} = a^{-1} * a = e$$

  * (b) 唯一性（本檔的關鍵）：若某個 $x \in G$ 滿足 $g * x = x * g = e$，則 $x$ **必為** $g^{-1}$：

    $$g * x = x * g = e \quad \Longrightarrow \quad x = g^{-1}$$

  * $a,\ g,\ x$ : 群元素 (Group elements) $[a, g, x \in G]$
  * $a^{-1},\ g^{-1}$ : 對應的反元素 (The corresponding inverses) $[a^{-1}, g^{-1} \in G]$
  * $e$ : 單位元素 (The identity element) $[e \in G]$

* **【推導 1】 右側驗算 (Right-hand verification)：** 把 $a * b$ 擺左邊、$b^{-1} * a^{-1}$ 擺右邊相乘。
  括號一路往右挪，中間的 $b * b^{-1}$ 先消掉，$a * a^{-1}$ 接著消掉

  $$\begin{gather*}
  \left(a * b\right) * \left(b^{-1} * a^{-1}\right) &\overset{\text{已知 1(b)}}{=}& a * \left(b * \left(b^{-1} * a^{-1}\right)\right) \\
  &\overset{\text{已知 1(b)}}{=}& a * \left(\left(b * b^{-1}\right) * a^{-1}\right) \\
  &\overset{\text{已知 2(a)}}{=}& a * \left(e * a^{-1}\right) \\
  &\overset{\text{已知 1(c)}}{=}& a * a^{-1} \\
  &\overset{\text{已知 2(a)}}{=}& e
  \end{gather*}$$

  * $a,\ b$ : 群元素 (Group elements) $[a, b \in G]$
  * $a^{-1},\ b^{-1}$ : 對應的反元素 (The corresponding inverses) $[a^{-1}, b^{-1} \in G]$
  * $e$ : 單位元素 (The identity element) $[e \in G]$
  * 註：**順序顛倒的理由就在第二行** —— 只有把 $b^{-1}$ 寫在最靠近 $b$ 的位置，
    括號挪過去時才會湊成 $b * b^{-1}$。若寫成 $a^{-1} * b^{-1}$，
    中間卡住的是 $b * a^{-1}$，在非交換群裡什麼都消不掉。

* **【推導 2】 左側驗算 (Left-hand verification)：** 把 $b^{-1} * a^{-1}$ 擺左邊、$a * b$ 擺右邊相乘。
  與【推導 1】完全對稱，這次先消掉 $a^{-1} * a$

  $$\begin{gather*}
  \left(b^{-1} * a^{-1}\right) * \left(a * b\right) &\overset{\text{已知 1(b)}}{=}& b^{-1} * \left(a^{-1} * \left(a * b\right)\right) \\
  &\overset{\text{已知 1(b)}}{=}& b^{-1} * \left(\left(a^{-1} * a\right) * b\right) \\
  &\overset{\text{已知 2(a)}}{=}& b^{-1} * \left(e * b\right) \\
  &\overset{\text{已知 1(c)}}{=}& b^{-1} * b \\
  &\overset{\text{已知 2(a)}}{=}& e
  \end{gather*}$$

  * $a,\ b$ : 群元素 (Group elements) $[a, b \in G]$
  * $a^{-1},\ b^{-1}$ : 對應的反元素 (The corresponding inverses) $[a^{-1}, b^{-1} \in G]$
  * $e$ : 單位元素 (The identity element) $[e \in G]$
  * 註：兩個方向都要驗，因為 [群的定義](Group_Definition.md)【定義 2(d)】要求的是**雙邊**反元素。
    在非交換群裡，$xy = e$ 不自動保證 $yx = e$。

+++

## 證明:

### (a) proof of the inverse of a product

兩張【推導】卡片已經證明 $b^{-1} * a^{-1}$ 與 $a * b$ 左右相乘都得到 $e$，
也就是它**符合 $a * b$ 的反元素的定義**。再引用唯一性收尾：

$$\begin{gather*}
\left(a * b\right) * \left(b^{-1} * a^{-1}\right) &\overset{\text{推導 1}}{=}& e \\
\left(b^{-1} * a^{-1}\right) * \left(a * b\right) &\overset{\text{推導 2}}{=}& e \\
\left(a * b\right)^{-1} &\overset{\text{已知 2(b)}}{=}& b^{-1} * a^{-1}
\end{gather*}$$

故 $\left(a * b\right)^{-1} = b^{-1} * a^{-1}$。

+++

## 意義與密碼學關聯 (Interpretation and Relevance to Cryptography)

### 為什麼順序要顛倒：穿衣服與脫衣服

最好記的直覺是穿脫衣服：

$$\text{先穿襪子，再穿鞋子} \quad \Longrightarrow \quad \text{先脫鞋子，再脫襪子}$$

$$\left(\text{鞋} * \text{襪}\right)^{-1} = \text{襪}^{-1} * \text{鞋}^{-1}$$

**撤銷一連串操作時，必須從最後做的那一步開始倒著撤銷。** 這在任何有順序的系統裡都成立，
群論只是把它寫成了公式。

代數上的理由見【推導 1】的註：括號往中間收攏時，
**必須讓互為反元素的那一對站在相鄰的位置**，$b$ 才遇得到 $b^{-1}$。

### 推廣到任意長度

同樣的論證可以反覆套用，得到：

$$\left(a_1 * a_2 * \cdots * a_n\right)^{-1} = a_n^{-1} * \cdots * a_2^{-1} * a_1^{-1}$$

整串**完全反序**。這在分析多輪加密時是基本工具。

### 密碼學上的對應：多輪密碼的解密順序

AES 有 $10$ 到 $14$ 輪，DES 有 $16$ 輪，每一輪都是一個可逆變換。整體加密是：

$$\text{AES} = R_{10} \circ R_9 \circ \cdots \circ R_1$$

解密時必須：

$$\text{AES}^{-1} = R_1^{-1} \circ R_2^{-1} \circ \cdots \circ R_{10}^{-1}$$

**輪金鑰要倒著用**。這不是實作上的小技巧，而是本命題的直接後果。
任何把輪金鑰順著用的解密實作一定是錯的。

同樣地，加密後再簽章（$\text{Sign} \circ \text{Encrypt}$）的訊息，
驗證方必須**先驗簽章、再解密**，順序不能對調。

### 什麼時候順序可以不顛倒

若群是交換的（$xy = yx$），則：

$$b^{-1} * a^{-1} = a^{-1} * b^{-1}$$

此時寫成哪一個都對。$\left(\mathbf{Z}_n, \oplus\right)$、$\left(\mathbf{Z}_n^*, \otimes\right)$
都是交換群，所以在 RSA 裡順序無所謂。

但 $S_n$（[對稱群](Symmetric_Group.md)）與 $GL_n$
（[一般線性群的階](General_Linear_Group_Order.md)）**不是**交換群 ——
AES 的 S-box 與矩陣運算都活在這裡，順序寫錯結果就是錯的。
