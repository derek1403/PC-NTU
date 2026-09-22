# Group Order (群的階)

+++

## 證明目標:

`Algebra.pdf` p.14–15。群的「大小」。這個量是 [拉格朗日定理](Lagrange_Theorem.md) 的主角，
也是密碼學衡量金鑰空間的唯一尺規。

* (a) 對稱群的階：

$$\left|S_3\right| = 6, \qquad \left|S_4\right| = 24, \qquad \left|S_n\right| = n!$$

* (b) 質數模的兩個階：

$$\left|\mathbf{Z}_p\right| = p, \qquad \left|\mathbf{Z}_p^*\right| = p - 1 \qquad \left(p \ \text{為質數}\right)$$

* (c) 一般模數的階：

$$\left|\mathbf{Z}_n^*\right| = \varphi(n), \qquad \left|\mathbf{Z}_9^*\right| = 6$$

* (d) 無限群的基數分層：$\left|\mathbf{Z}\right|$ 與 $\left|\mathbf{Q}\right|$ **可數**，
  $\left|\mathbf{R}\right|$ 與 $\left|\mathbf{C}\right|$ **不可數**：

$$\left|\mathbf{Z}\right| = \left|\mathbf{Q}\right| = \aleph_0 \ < \ \left|\mathbf{R}\right| = \left|\mathbf{C}\right|$$

* $G$ : 群的底層集合 (The underlying set of the group) $[\text{集合}]$
* $\left|G\right|$ : 群的階 (The order of the group) $[\left|G\right| \in \mathbf{N} \cup \left\{\infty\right\}]$
* $S_n$ : $n$ 次對稱群 (The symmetric group on $n$ letters) $[\text{集合}]$
* $\mathbf{Z}_n,\ \mathbf{Z}_n^*$ : 模 $n$ 剩餘類與可逆剩餘類集合 (Residues and units modulo $n$) $[\text{集合}]$
* $\varphi$ : 尤拉函數 (Euler's totient function) $[\mathbb{Z}^{+} \to \mathbb{Z}^{+}]$
* $p$ : 質數 (A prime) $[p \in \mathbf{P}]$
* $n$ : 模數 (Modulus) $[n \in \mathbf{P}]$
* $\aleph_0$ : 可數無限的基數 (The cardinality of a countably infinite set) $[\text{基數}]$
* 註：「階」這個字在本章有**兩個**意思 —— 群的階 $\left|G\right|$（本檔）與
  元素的階 $o(g)$（見 [元素的階與循環子群](Order_of_Element_and_Cyclic_Subgroup.md)）。
  兩者由 [拉格朗日定理](Lagrange_Theorem.md) 的系理連在一起（$o(g)$ 整除 $\left|G\right|$），
  但**不是同一個東西**。
* 註：(d) 屬於集合論，與群結構無關 —— 這裡談的是底層集合的基數。
  本檔只把 Cantor 的結果引用進來，不重證對角線論證。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [對稱群的階 (Order of the symmetric group)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Group/Symmetric_Group.html#b-proof-of-the-order-of-the-symmetric-group)：** 已於本章 [對稱群](Symmetric_Group.md)【證明 (b)】完整證明，此處直接引用不再重證

  $$\left|S_n\right| = n!$$

  * $S_n$ : $n$ 次對稱群 (The symmetric group on $n$ letters) $[\text{集合}]$
  * $n$ : 被排列的元素個數 (The number of letters) $[n \in \mathbf{P}]$

* **【已知 2】 [模 $n$ 剩餘類與可逆剩餘類 (Residues and units modulo $n$)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Number_Sets_and_Notation.html#definitions-and-notation)：** 已於本章 [數系與符號約定](../Number_Sets_and_Notation.md)【定義 3】【定義 4】給出，此處直接引用

  $$\mathbf{Z}_n = \left\{0, 1, \dots, n-1\right\}, \qquad \mathbf{Z}_n^* = \left\{a \in \mathbf{Z}_n \ \middle|\ \gcd(a, n) = 1\right\}$$

  * $\mathbf{Z}_n$ : 模 $n$ 剩餘類集合 (The set of residues modulo $n$) $[\text{集合}]$
  * $\mathbf{Z}_n^*$ : 模 $n$ 可逆剩餘類集合 (The set of units modulo $n$) $[\text{集合}]$
  * $a$ : 剩餘類代表元 (Residue representative) $[a \in \mathbf{Z}_n]$
  * $n$ : 模數 (Modulus) $[n \in \mathbf{P}]$
  * $\gcd$ : 最大公因數 (Greatest common divisor) $[\mathbf{Z} \times \mathbf{Z} \to \mathbf{N}]$

* **【已知 3】 [Cantor 的基數結果 (Cantor's cardinality results)](https://mathworld.wolfram.com/CountablyInfinite.html)：** 集合論的標準結果，本章直接引用不再重證

  * (a) 有理數可數：

    $$\left|\mathbf{Q}\right| = \aleph_0$$

  * (b) 實數不可數（對角線論證）：

    $$\left|\mathbf{R}\right| > \aleph_0$$

  * (c) 複數與實數等勢：

    $$\left|\mathbf{C}\right| = \left|\mathbf{R}\right|$$

  * $\mathbf{Q},\ \mathbf{R},\ \mathbf{C}$ : 有理數、實數、複數集合 (The sets of rationals, reals, and complex numbers) $[\text{集合}]$
  * $\aleph_0$ : 可數無限的基數 (The cardinality of a countably infinite set) $[\text{基數}]$

* **【定義 1】 群的階 (Order of a group)：** 群裡元素的個數，也就是底層集合的基數

  $$\left|G\right| \overset{\text{def}}{=} \text{the cardinality of } G$$

  * $G$ : 群的底層集合 (The underlying set of the group) $[\text{集合}]$
  * $\left|G\right|$ : 群的階 (The order of the group) $[\left|G\right| \in \mathbf{N} \cup \left\{\infty\right\}]$

* **【定義 2】 有限群與無限群 (Finite and infinite group)：**

  * (a) 有限群：

    $$\left(G, *\right) \ \text{為有限群} \quad \overset{\text{def}}{\Longleftrightarrow} \quad \left|G\right| < \infty$$

  * (b) 無限群：

    $$\left(G, *\right) \ \text{為無限群} \quad \overset{\text{def}}{\Longleftrightarrow} \quad \left|G\right| = \infty$$

  * $G$ : 群的底層集合 (The underlying set of the group) $[\text{集合}]$
  * $\left|G\right|$ : 群的階 (The order of the group) $[\left|G\right| \in \mathbf{N} \cup \left\{\infty\right\}]$
  * 註：**密碼學只用有限群。** 理由見文末。

* **【定義 3】 尤拉函數 (Euler's totient function)：** 小於 $n$ 且與 $n$ 互質的正整數個數

  $$\varphi(n) \overset{\text{def}}{=} \left|\left\{a \in \mathbf{Z} \ \middle|\ 1 \le a \le n,\ \gcd(a, n) = 1\right\}\right|$$

  * $\varphi$ : 尤拉函數 (Euler's totient function) $[\mathbb{Z}^{+} \to \mathbb{Z}^{+}]$
  * $n$ : 模數 (Modulus) $[n \in \mathbf{P}]$
  * $a$ : 被計數的整數 (The integers being counted) $[a \in \mathbf{Z}]$
  * $\gcd$ : 最大公因數 (Greatest common divisor) $[\mathbf{Z} \times \mathbf{Z} \to \mathbf{N}]$
  * 註：投影片寫成 $\phi$，本章統一用 $\varphi$（字形一致性）。
  * 註：計數範圍 $1 \le a \le n$ 與【已知 2】的 $0 \le a \le n-1$ **差在頭尾兩端**：
    前者含 $n$ 不含 $0$、後者含 $0$ 不含 $n$。兩者計數結果相同，理由見【證明 (c)】的註。

+++

## 證明:

### (a) proof of the order of the symmetric group

直接引用【已知 1】並代入具體數值：

$$\begin{gather*}
\left|S_n\right| &\overset{\text{已知 1}}{=}& n! \\
\left|S_3\right| &\overset{\text{已知 1}}{=}& 3! = 6 \\
\left|S_4\right| &\overset{\text{已知 1}}{=}& 4! = 24
\end{gather*}$$

與投影片一致。

### (b) proof of the orders of the residues and units modulo a prime

**$\mathbf{Z}_p$ 的階**直接由【已知 2】數出來：

$$\begin{gather*}
\mathbf{Z}_p &\overset{\text{已知 2}}{=}& \left\{0, 1, \dots, p-1\right\} \\
\left|\mathbf{Z}_p\right| &\overset{\text{定義 1}}{=}& p
\end{gather*}$$

**$\mathbf{Z}_p^*$ 的階**要用到 $p$ 是質數。質數的因數只有 $1$ 與 $p$ 自己，
所以 $\left\{1, \dots, p-1\right\}$ 每個元素都與 $p$ 互質，只有 $0$ 被排除：

$$\begin{gather*}
\gcd(a, p) &=& 1 \qquad \text{for all } a \in \left\{1, 2, \dots, p-1\right\} \\
\gcd(0, p) &=& p \neq 1 \\
\mathbf{Z}_p^* &\overset{\text{已知 2}}{=}& \left\{1, 2, \dots, p-1\right\} \\
\left|\mathbf{Z}_p^*\right| &\overset{\text{定義 1}}{=}& p - 1
\end{gather*}$$

* 註：**質數性在第一行被用到**。$n$ 為合數時 $\left\{1,\dots,n-1\right\}$ 裡會有與 $n$ 有公因數的元素，
  $\mathbf{Z}_n^*$ 就會比 $n-1$ 小 —— 這正是【證明 (c)】的內容。

### (c) proof of the order of the units modulo a general number

$\mathbf{Z}_n^*$ 的定義（【已知 2】）與尤拉函數的定義（【定義 3】）數的是**同一批元素**：

$$\begin{gather*}
\left|\mathbf{Z}_n^*\right| &\overset{\text{已知 2}}{=}& \left|\left\{a \in \mathbf{Z}_n \ \middle|\ \gcd(a, n) = 1\right\}\right| \\
&\overset{\text{定義 3}}{=}& \varphi(n)
\end{gather*}$$

代入 $n = 9$，由 [循環群](Cyclic_Group.md)【已知 3】已列出
$\mathbf{Z}_9^* = \left\{1, 2, 4, 5, 7, 8\right\}$：

$$\begin{gather*}
\left|\mathbf{Z}_9^*\right| &\overset{\text{定義 1}}{=}& 6 \\
\varphi(9) &=& 6
\end{gather*}$$

與投影片一致。

* 註：兩個定義的計數範圍差在頭尾（【定義 3】的註）。實際上**兩端都不影響計數** ——
  $n > 1$ 時 $\gcd(0, n) = n \neq 1$ 且 $\gcd(n, n) = n \neq 1$，
  $0$ 與 $n$ 兩者都**不會**被算進去，所以兩個範圍數出來的是同一個數。
* 註：$\varphi$ 的具體算法（$\varphi(p) = p-1$、$\varphi\!\left(p^k\right) = p^k - p^{k-1}$、
  互質時 $\varphi(mn) = \varphi(m)\varphi(n)$）屬於 [Arithmetic](../Arithmatic/Arithmetic.ipynb) 的範圍，
  本章只用其值。乘法性的群論解釋見 [中國剩餘定理](../Ring/Chinese_Remainder_Theorem.md)。

### (d) proof that the integers are countable and comparison of infinite cardinalities

$\left|\mathbf{Z}\right| = \left|\mathbf{Q}\right|$ 的證明只需給出 $\mathbf{Z}$ 與 $\mathbf{N}$ 之間的一個雙射
（把整數「之字形」排成一列），其餘引用【已知 3】。定義

$$h : \mathbf{N} \to \mathbf{Z}, \qquad h(k) = \begin{cases} \dfrac{k}{2}, & k \ \text{為偶數} \\[2mm] -\dfrac{k+1}{2}, & k \ \text{為奇數} \end{cases}$$

逐項列出即可看出它踩遍所有整數且不重複：

$$\begin{gather*}
h(0) &=& 0 \\
h(1) &=& -1 \\
h(2) &=& 1 \\
h(3) &=& -2 \\
h(4) &=& 2 \\
\vdots &\ \vdots\ & \vdots
\end{gather*}$$

偶數位給出 $0, 1, 2, \dots$、奇數位給出 $-1, -2, -3, \dots$，兩者合起來恰為 $\mathbf{Z}$ 且互不重疊，
故 $h$ 是雙射：

$$\begin{gather*}
\left|\mathbf{Z}\right| &=& \left|\mathbf{N}\right| = \aleph_0 \\
\left|\mathbf{Q}\right| &\overset{\text{已知 3(a)}}{=}& \aleph_0 \\
\left|\mathbf{Z}\right| &=& \left|\mathbf{Q}\right|
\end{gather*}$$

實數與複數則落在更高的層級：

$$\begin{gather*}
\left|\mathbf{R}\right| &\overset{\text{已知 3(b)}}{>}& \aleph_0 \\
\left|\mathbf{C}\right| &\overset{\text{已知 3(c)}}{=}& \left|\mathbf{R}\right| \\
\left|\mathbf{Z}\right| = \left|\mathbf{Q}\right| &<& \left|\mathbf{R}\right| = \left|\mathbf{C}\right| \\
\mathbf{Z},\ \mathbf{Q},\ \mathbf{R},\ \mathbf{C} \ \text{配加法} &\overset{\text{定義 2(b)}}{=}& \text{無限群}
\end{gather*}$$

與投影片一致。

* 註：$\mathbf{Q} \supsetneq \mathbf{Z}$（$\mathbf{Q}$ 真包含 $\mathbf{Z}$）卻**基數相同** ——
  這是無限集合特有的現象，有限集合絕不可能（【排列】【已知 1(b)】）。

+++

## 意義與密碼學關聯 (Interpretation and Relevance to Cryptography)

### $\left|G\right|$ 就是金鑰空間的大小

密碼學裡，群的階直接翻譯成一個安全性數字：

$$\text{窮舉攻擊需要嘗試的次數} \ \approx \ \left|G\right|$$

| 群 | 階 | 安全性意義 |
|---|---|---|
| $S_{256}$ | $256! \approx 10^{507}$ | 可能的 S-box 數量 |
| $\left\{0,1\right\}^{128}$ 配 XOR | $2^{128}$ | AES-128 的金鑰空間 |
| $\mathbf{Z}_p^*$（$p$ 為 $2048$ 位元） | $p - 1 \approx 2^{2048}$ | Diffie–Hellman 的群大小 |
| $\mathbf{Z}_n^*$（RSA-$2048$） | $\varphi(n)$ | RSA 的指數空間 |

**這就是「密碼學只用有限群」的第一個理由** —— 無限群沒有 $\left|G\right|$ 這個數字，
安全性無從量化。

### 為什麼 $\varphi(n)$ 是 RSA 的心臟

RSA 的模數是 $n = pq$（兩個大質數），而

$$\varphi(n) = \varphi(p)\varphi(q) \overset{\text{證明 (b)}}{=} \left(p-1\right)\left(q-1\right)$$

* **知道 $p, q$** $\to$ 一秒算出 $\varphi(n)$ $\to$ 解出私鑰 $d$；
* **只知道 $n$** $\to$ 想算 $\varphi(n)$ 就得先分解 $n$，而分解大合數是困難問題。

**$\varphi(n)$ 就是 RSA 的私密資訊本身。** 整個 RSA 的安全性可以濃縮成一句話：
「$\left|\mathbf{Z}_n^*\right|$ 這個數字必須算不出來。」

這跟 [循環群](Cyclic_Group.md) 的離散對數問題是**兩個不同的困難問題**：
RSA 靠分解困難，Diffie–Hellman 靠離散對數困難。

### 為什麼密碼學只用有限群（第二個理由）

【證明 (d)】給了第二個、也更根本的理由：**無限群的元素無法用有限位元表示**。

$\mathbf{R}$ 不可數意味著幾乎所有實數都**沒有有限的描述**，電腦存不下、也傳不出去。
即使是可數的 $\mathbf{Q}$，分子分母也會在運算中無限膨脹。

有限群則保證每個元素都能塞進固定長度的位元串（$\left\lceil \log_2 \left|G\right| \right\rceil$ 個位元），
運算結果的大小有上界。**「取模」這個動作存在的唯一理由，就是把無限群壓成有限群。**

### 階是拉格朗日定理的主角

$\left|G\right|$ 真正的威力還沒展開。[拉格朗日定理](Lagrange_Theorem.md) 會說：

$$H \ \text{是 } G \text{ 的子群} \quad \Longrightarrow \quad \left|H\right| \ \text{整除} \ \left|G\right|$$

這條定理把「大小」變成一個**強力的結構限制** ——
它會直接導出尤拉定理 $a^{\varphi(n)} \equiv 1 \pmod n$，
而那正是 RSA 解密之所以成立的那一行。
