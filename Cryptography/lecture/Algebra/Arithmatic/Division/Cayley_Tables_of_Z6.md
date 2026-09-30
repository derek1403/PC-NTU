# Cayley Tables of Z6 (Z6 的凱萊表)

+++

## 證明目標:

`Arithmetic.pdf` p.5。用取模函數在 $\mathbf{Z}_6 = \left\{0,1,2,3,4,5\right\}$ 上定義加法與乘法，
把兩張運算表完整畫出來，然後回答投影片的問題：**$\mathbf{Z}_6$ 是體嗎？**

* (a) 驗證投影片的兩張凱萊表（加法表 $\oplus$、乘法表 $\otimes$）。
* (b) **$\mathbf{Z}_6$ 不是體**：$2$ 在 $\otimes$ 下沒有反元素，而且 $2 \otimes 3 = 0$ 是零因子：

$$2 \otimes b \neq 1 \quad \text{for all } b \in \mathbf{Z}_6, \qquad 2 \otimes 3 = 0$$

* (c) 對照組：$\mathbf{Z}_7$ 的每個非零元素都有乘法反元素：

$$1 \otimes 1 = 2 \otimes 4 = 3 \otimes 5 = 6 \otimes 6 = 1 \qquad \left(\text{於 } \mathbf{Z}_7\right)$$

* $\mathbf{Z}_n$ : 模 $n$ 剩餘類集合 (The set of residues modulo $n$) $[\text{集合}]$
* $\oplus,\ \otimes$ : 模 $n$ 加法與乘法 (Addition and multiplication modulo $n$) $[\mathbf{Z}_n \times \mathbf{Z}_n \to \mathbf{Z}_n]$
* $a,\ b$ : 剩餘類代表元 (Residue representatives) $[a, b \in \mathbf{Z}_n]$
* 註：「$\mathbf{Z}_p$ 是體 $\Longleftrightarrow$ $p$ 是質數」已在 Abstract_Algebra 章
  [體的定義](../../Abstract_Algebra/Field/Field_Definition.md) 完整證明。本檔只做
  $n = 6$ 與 $n = 7$ 兩個**具體實例**的逐條驗證，讓那條定理「看得見」。
* 註：投影片問「Is $\mathbf{Z}_6$ a field?」但沒有給答案。本檔的答案是**不是**，理由有兩個互相獨立的證據（(b) 的兩式）。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [取模函數 (Modular function)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/Division/Modular_Function.html#a-proof-that-the-remainder-lies-between-zero-and-the-modulus)：** 已於本章 [取模函數](Modular_Function.md)【定義 1】【證明 (a)】給出並證明，此處直接引用不再重證

  * (a) 定義：

    $$n \bmod m = n - \left\lfloor \frac{n}{m} \right\rfloor m$$

  * (b) 值域：

    $$0 \le n \bmod m < m$$

  * $n$ : 被除數 (The dividend) $[n \in \mathbf{Z}]$
  * $m$ : 模數 (The modulus) $[m \in \mathbf{P}]$

* **【已知 2】 [體的定義 (Definition of a field)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Field/Field_Definition.html#assumptions-preliminaries)：** 已於 Abstract_Algebra 章 [體的定義](../../Abstract_Algebra/Field/Field_Definition.md)【定義 1】給出，此處直接引用。體是交換含單位元環，且每個非零元素都有乘法反元素

  $$F \ \text{為體} \quad \Longrightarrow \quad \forall\, a \in F \setminus \left\{0\right\},\ \exists\, b \in F \ \text{ such that } \ a b = 1$$

  * $F$ : 體的底層集合 (The underlying set of the field) $[\text{集合}]$
  * $a,\ b$ : 體的元素 (Field elements) $[a, b \in F]$

* **【已知 3】 [$\mathbf{Z}_p$ 是體的充要條件 (Residues modulo p form a field)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Field/Field_Definition.html#b-proof-that-the-residues-modulo-a-prime-form-a-field)：** 已於 Abstract_Algebra 章 [體的定義](../../Abstract_Algebra/Field/Field_Definition.md)【證明 (b)】完整證明，此處直接引用不再重證

  $$\mathbf{Z}_n \ \text{為體} \quad \Longleftrightarrow \quad n \ \text{為質數}$$

  * $\mathbf{Z}_n$ : 配模 $n$ 加法與乘法的剩餘類環 (The ring of residues modulo $n$) $[\text{環}]$
  * $n$ : 模數 (The modulus) $[n \in \mathbf{P},\ n \ge 2]$

* **【已知 4】 [零因子 (Zero divisor)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Ring/Zero_Divisor.html#assumptions-preliminaries)：** 已於 Abstract_Algebra 章 [零因子](../../Abstract_Algebra/Ring/Zero_Divisor.md)【定義 1】給出，此處直接引用

  $$a \neq 0,\ b \neq 0,\ ab = 0 \quad \Longrightarrow \quad a,\ b \ \text{為零因子}$$

  * $a,\ b$ : 環元素 (Ring elements) $[a, b \in R]$
  * $R$ : 環的底層集合 (The underlying set of the ring) $[\text{集合}]$
  * 註：體沒有零因子（[體的定義](../../Abstract_Algebra/Field/Field_Definition.md)【證明 (d)】）。
    所以找到一對零因子就足以判定「不是體」。

* **【定義 1】 模 $n$ 加法與乘法 (Addition and multiplication modulo $n$)：**

  $$a \oplus b \overset{\text{def}}{=} \left(a + b\right) \bmod n, \qquad a \otimes b \overset{\text{def}}{=} \left(a \times b\right) \bmod n$$

  * $\oplus,\ \otimes$ : 模 $n$ 加法與乘法 (Addition and multiplication modulo $n$) $[\mathbf{Z}_n \times \mathbf{Z}_n \to \mathbf{Z}_n]$
  * $a,\ b$ : 剩餘類代表元 (Residue representatives) $[a, b \in \mathbf{Z}_n]$
  * $n$ : 模數 (The modulus) $[n \in \mathbf{P}]$
  * 註：由【已知 1(b)】，結果一定落回 $\left\{0, \dots, n-1\right\}$，所以兩個運算都是**封閉**的。

+++

## 證明:

### (a) verify the two Cayley tables of the residues modulo six

依【定義 1】逐格計算。整張表的規律：**加法表每一列是上一列往左循環位移一格**，
因為 $\left(a+1\right) + b = a + \left(b+1\right)$。代表性的格子（含「繞回」的格子）：

$$\begin{gather*}
3 \oplus 2 &\overset{\text{定義 1}}{=}& 5 \bmod 6 \\
3 \oplus 2 &\overset{\text{已知 1(a)}}{=}& 5 \\
1 \oplus 5 &\overset{\text{定義 1}}{=}& 6 \bmod 6 \\
1 \oplus 5 &\overset{\text{已知 1(a)}}{=}& 0 \\
5 \oplus 5 &\overset{\text{定義 1}}{=}& 10 \bmod 6 \\
5 \oplus 5 &\overset{\text{已知 1(a)}}{=}& 4 \\
4 \otimes 5 &\overset{\text{定義 1}}{=}& 20 \bmod 6 \\
4 \otimes 5 &\overset{\text{已知 1(a)}}{=}& 2 \\
5 \otimes 5 &\overset{\text{定義 1}}{=}& 25 \bmod 6 \\
5 \otimes 5 &\overset{\text{已知 1(a)}}{=}& 1 \\
3 \otimes 4 &\overset{\text{定義 1}}{=}& 12 \bmod 6 \\
3 \otimes 4 &\overset{\text{已知 1(a)}}{=}& 0
\end{gather*}$$

完整的兩張表（全部 $72$ 格已用文末程式逐格核對，與投影片一致）：

| $\oplus$ | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| **0** | 0 | 1 | 2 | 3 | 4 | 5 |
| **1** | 1 | 2 | 3 | 4 | 5 | 0 |
| **2** | 2 | 3 | 4 | 5 | 0 | 1 |
| **3** | 3 | 4 | 5 | 0 | 1 | 2 |
| **4** | 4 | 5 | 0 | 1 | 2 | 3 |
| **5** | 5 | 0 | 1 | 2 | 3 | 4 |

| $\otimes$ | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| **0** | 0 | 0 | 0 | 0 | 0 | 0 |
| **1** | 0 | 1 | 2 | 3 | 4 | 5 |
| **2** | 0 | 2 | 4 | 0 | 2 | 4 |
| **3** | 0 | 3 | 0 | 3 | 0 | 3 |
| **4** | 0 | 4 | 2 | 0 | 4 | 2 |
| **5** | 0 | 5 | 4 | 3 | 2 | 1 |

### (b) disprove that the residues modulo six form a field

**證據一：$2$ 沒有乘法反元素。** 不只是查表看到第 $2$ 列沒有 $1$ —— 對**任意** $b$，
$2 \otimes b$ 都是偶數，因為「偶數減掉 $6$ 的倍數」仍是偶數：

$$\begin{gather*}
2 \otimes b &\overset{\text{定義 1}}{=}& 2b \bmod 6 \\
2 \otimes b &\overset{\text{已知 1(a)}}{=}& 2b - 6\left\lfloor \frac{2b}{6} \right\rfloor \\
2 \otimes b &=& 2\left(b - 3\left\lfloor \frac{2b}{6} \right\rfloor\right) \\
2 \otimes b &\neq& 1 \qquad \text{(偶數不等於奇數 } 1 \text{)} \\
2 \ne 0 \ \text{且對所有 } b \text{ 都有 } 2 \otimes b \neq 1 &\overset{\text{已知 2}}{\Longrightarrow}& \mathbf{Z}_6 \ \text{不是體}
\end{gather*}$$

故 $2 \in \mathbf{Z}_6 \setminus \left\{0\right\}$ 不可逆，違反【已知 2】的要求。

**證據二：零因子。** 兩個非零元素乘出 $0$：

$$\begin{gather*}
2 \otimes 3 &\overset{\text{定義 1}}{=}& 6 \bmod 6 \\
2 \otimes 3 &\overset{\text{已知 1(a)}}{=}& 0 \\
2 \neq 0,\ 3 \neq 0,\ 2 \otimes 3 = 0 &\overset{\text{已知 4}}{\Longrightarrow}& 2,\ 3 \ \text{為零因子}
\end{gather*}$$

體沒有零因子，再次確認 $\mathbf{Z}_6$ 不是體。這與一般定理的預測一致：

$$\begin{gather*}
6 = 2 \times 3 \ \text{不是質數} &\overset{\text{已知 3}}{\Longrightarrow}& \mathbf{Z}_6 \ \text{不是體}
\end{gather*}$$

* 註：兩個證據其實是同一件事的兩面 —— 若 $2$ 有反元素 $c$，則
  $3 = 3 \otimes \left(2 \otimes c\right) = \left(3 \otimes 2\right) \otimes c = 0 \otimes c = 0$，矛盾。
  **零因子必不可逆。**

### (c) verify that every nonzero residue modulo seven is invertible

依【定義 1】取 $n = 7$，把六個非零元素的反元素逐一找出：

$$\begin{gather*}
1 \otimes 1 &\overset{\text{定義 1}}{=}& 1 \bmod 7 \\
1 \otimes 1 &\overset{\text{已知 1(a)}}{=}& 1 \\
2 \otimes 4 &\overset{\text{定義 1}}{=}& 8 \bmod 7 \\
2 \otimes 4 &\overset{\text{已知 1(a)}}{=}& 1 \\
3 \otimes 5 &\overset{\text{定義 1}}{=}& 15 \bmod 7 \\
3 \otimes 5 &\overset{\text{已知 1(a)}}{=}& 1 \\
6 \otimes 6 &\overset{\text{定義 1}}{=}& 36 \bmod 7 \\
6 \otimes 6 &\overset{\text{已知 1(a)}}{=}& 1
\end{gather*}$$

乘法可交換，所以 $4 \otimes 2 = 2 \otimes 4 = 1$、$5 \otimes 3 = 3 \otimes 5 = 1$ 也同時得到。

每個非零元素都有反元素，符合【已知 2】的要求。這與一般定理的預測一致：

$$\begin{gather*}
7 \ \text{是質數} &\overset{\text{已知 3}}{\Longrightarrow}& \mathbf{Z}_7 \ \text{是體}
\end{gather*}$$

+++

## 意義與密碼學關聯 (Interpretation and Relevance to Cryptography)

### 凱萊表的讀法：找 $1$

一個有限集合配一個運算，凱萊表就是它的**完整說明書**。判斷「每個元素都可逆」只要一個動作：
**看每一列有沒有出現 $1$**（乘法單位元素）。

* $\mathbf{Z}_6$ 的乘法表：第 $2, 3, 4$ 列都沒有 $1$ —— 這三個數與 $6$ 有公因數。
* $\mathbf{Z}_7$ 的乘法表：除了第 $0$ 列，**每一列都恰好出現一次 $1$**。

哪些元素會「找不到 $1$」有精確答案：恰好是與模數不互質的那些。
這條判準在 [模反元素](../Congruence/Modular_Inverse.md) 證明。

### 體就是「四則運算封閉的數字世界」

在 $\mathbf{Z}_7$ 裡你可以自由加、減、乘，以及**除以任何非零數**，結果永遠留在 $\mathbf{Z}_7$ 裡。
在 $\mathbf{Z}_6$ 裡「除以 $2$」根本沒有意義。

這就是為什麼 Diffie–Hellman、ElGamal、DSA 都選**質數**模數：
解密或簽章驗證時需要做除法（乘以反元素），模數一旦是合數，某些元素就除不了。
RSA 雖然用合數 $n = pq$，但它只在 $\mathbf{Z}_n^*$（可逆元素）裡運作，刻意避開了零因子。

### 程式思維

```python
n = 6
add = [[(a + b) % n for b in range(n)] for a in range(n)]
mul = [[(a * b) % n for b in range(n)] for a in range(n)]
assert mul[2] == [0, 2, 4, 0, 2, 4]            # 第 2 列沒有 1
assert mul[2][3] == 0                           # 零因子
inv7 = {a: pow(a, -1, 7) for a in range(1, 7)}
assert inv7 == {1: 1, 2: 4, 3: 5, 4: 2, 5: 3, 6: 6}
```
