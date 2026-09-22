# Cyclic Group (循環群)

+++

## 證明目標:

`Algebra.pdf` p.13。有些群整個可以由**單一個元素**的冪次生出來 ——
這類群結構最簡單，也是 Diffie–Hellman 與 ElGamal 的舞台。

* (a) $\left(\mathbf{Z}, +\right)$ 是循環群，生成元為 $1$ 與 $-1$。
* (b) $\left(\mathbf{Z}_7^*, \otimes\right)$ 是循環群，$3$ 是一個生成元：

$$\mathbf{Z}_7^* = \left\{3^1, 3^2, 3^3, 3^4, 3^5, 3^6\right\} = \left\{3, 2, 6, 4, 5, 1\right\}$$

* (c) $\left(\mathbf{Z}_9^*, \otimes\right)$ 是循環群，生成元為 $2$ 與 $5$。
* (d) $\left(\mathbf{Q}, +\right)$ **不是**循環群。
* (e) $\left(\mathbf{Z}_8^*, \otimes\right)$ **不是**循環群（Klein 四元群）。
* (f) **循環群必為阿貝爾群**（投影片未列，但後續多處會用到）：

$$\left(G, *\right) \ \text{循環} \quad \Longrightarrow \quad \left(G, *\right) \ \text{阿貝爾}$$

* $G$ : 群的底層集合 (The underlying set of the group) $[\text{集合}]$
* $*$ : 群運算 (Group operation) $[G \times G \to G]$
* $g$ : 生成元 (A generator) $[g \in G]$
* $a$ : 任意群元素 (An arbitrary group element) $[a \in G]$
* $n$ : 冪次 (Exponent) $[n \in \mathbf{Z}]$
* 註：(f) 的逆命題**不成立** —— 阿貝爾群未必循環，(e) 的 $\mathbf{Z}_8^*$ 就是反例
  （它交換，但不循環）。
* 註：生成元**不唯一**。(a) 有兩個、(c) 有兩個，一般而言 $\mathbf{Z}_n^*$ 循環時有
  $\varphi\left(\varphi(n)\right)$ 個生成元。
* 註：本檔的「循環」是對整個群而言。由單一元素生成的**子群** $\langle g \rangle$（未必等於 $G$）
  見 [元素的階與循環子群](Order_of_Element_and_Cyclic_Subgroup.md)。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [群的公理與冪次記號 (Group axioms and power notation)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Group/Group_Definition.html#definitions-and-notation)：** 已於本章 [群的定義](Group_Definition.md)【定義 2】【定義 3】給出，此處直接引用

  * (a) 結合律：

    $$a * \left(b * c\right) = \left(a * b\right) * c$$

  * (b) 冪次：

    $$g^n \overset{\text{def}}{=} \underbrace{g * \cdots * g}_{n \ \text{個}}, \qquad g^0 \overset{\text{def}}{=} e, \qquad g^{-n} \overset{\text{def}}{=} \underbrace{g^{-1} * \cdots * g^{-1}}_{n \ \text{個}}$$

  * (c) 指數律（由 (a)(b) 直接展開即得，本章直接引用）：

    $$g^m * g^n = g^{m+n} \qquad \text{for all } m, n \in \mathbf{Z}$$

  * $G$ : 群的底層集合 (The underlying set of the group) $[\text{集合}]$
  * $g$ : 群元素 (A group element) $[g \in G]$
  * $a,\ b,\ c$ : 群元素 (Group elements) $[a, b, c \in G]$
  * $m,\ n$ : 冪次 (Exponents) $[m, n \in \mathbf{Z}]$
  * $e$ : 單位元素 (The identity element) $[e \in G]$

* **【已知 2】 [阿貝爾群的定義 (Definition of an abelian group)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Group/Abelian_and_Non_Abelian_Group.html#assumptions-preliminaries)：** 已於本章 [阿貝爾群與非阿貝爾群](Abelian_and_Non_Abelian_Group.md)【定義 1】給出，此處直接引用

  $$\left(G, *\right) \ \text{為阿貝爾群} \quad \overset{\text{def}}{\Longleftrightarrow} \quad a * b = b * a \qquad \text{for all } a, b \in G$$

  * $G$ : 群的底層集合 (The underlying set of the group) $[\text{集合}]$
  * $a,\ b$ : 群元素 (Group elements) $[a, b \in G]$

* **【已知 3】 [模 $n$ 可逆剩餘類集合 (The set of units modulo $n$)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Number_Sets_and_Notation.html#definitions-and-notation)：** 已於本章 [數系與符號約定](../Number_Sets_and_Notation.md)【定義 4】給出，此處直接引用

  $$\mathbf{Z}_n^* = \left\{a \in \mathbf{Z}_n \ \middle|\ \gcd(a, n) = 1\right\}$$

  * $\mathbf{Z}_n^*$ : 模 $n$ 可逆剩餘類集合 (The set of units modulo $n$) $[\text{集合}]$
  * $a$ : 剩餘類代表元 (Residue representative) $[a \in \mathbf{Z}_n]$
  * $n$ : 模數 (Modulus) $[n \in \mathbf{P}]$

* **【定義 1】 循環群與生成元 (Cyclic group and generator)：** 存在某個元素，它的冪次跑遍整個群

  $$\left(G, *\right) \ \text{為循環群} \quad \overset{\text{def}}{\Longleftrightarrow} \quad \exists\, g \in G \ \text{ such that } \ G = \left\{g^n \ \middle|\ n \in \mathbf{Z}\right\}$$

  * $G$ : 群的底層集合 (The underlying set of the group) $[\text{集合}]$
  * $g$ : 生成元 (A generator) $[g \in G]$
  * $n$ : 冪次 (Exponent) $[n \in \mathbf{Z}]$
  * 註：$n$ 的範圍是**整個 $\mathbf{Z}$**（含負數與 $0$），不是只有正整數。
    這一點在 (a) 用來說明 $-2 = \left(-1\right) + \left(-1\right)$ 也在生成的集合裡。
  * 註：群運算寫成加法時，$g^n$ 對應的記號是 $ng$，生成條件寫成
    $G = \left\{ng \ \middle|\ n \in \mathbf{Z}\right\}$。

+++

## 證明:

### (a) proof that the integers under addition form a cyclic group

加法記號下，$1$ 的「冪次」就是 $1$ 的整數倍：

$$\begin{gather*}
\left\{n \cdot 1 \ \middle|\ n \in \mathbf{Z}\right\} &\overset{\text{已知 1(b)}}{=}& \left\{\dots, -2, -1, 0, 1, 2, \dots\right\} \\
&=& \mathbf{Z}
\end{gather*}$$

故 $1$ 是生成元，$\left(\mathbf{Z}, +\right)$ 循環。同理 $-1$ 也是：

$$\begin{gather*}
\left\{n \cdot \left(-1\right) \ \middle|\ n \in \mathbf{Z}\right\} &\overset{\text{已知 1(b)}}{=}& \left\{\dots, 2, 1, 0, -1, -2, \dots\right\} \\
&=& \mathbf{Z}
\end{gather*}$$

* 註：投影片舉的三個例子對應如下 —— $3 = 1 + 1 + 1$（$n = 3$）、
  $-2 = \left(-1\right) + \left(-1\right)$（以 $-1$ 為生成元取 $n = 2$，或以 $1$ 為生成元取 $n = -2$）、
  $0 = 1^0$（$n = 0$，即【已知 1(b)】的 $g^0 = e$）。
* 註：$2$ **不是**生成元 —— $\left\{2n\right\}$ 只給出偶數，漏掉所有奇數。
  生成元必須「走得夠碎」才能踩遍全部。

### (b) proof that the units modulo seven form a cyclic group

由 [群的正例與反例](Group_Examples_and_Counterexamples.md)【證明 (f)】，
$\mathbf{Z}_7^* = \left\{1,2,3,4,5,6\right\}$。逐次計算 $3$ 的冪次：

$$\begin{gather*}
3^1 &=& 3 \\
3^2 &\overset{\text{已知 1(c)}}{=}& 3 \otimes 3 = 9 \bmod 7 = 2 \\
3^3 &\overset{\text{已知 1(c)}}{=}& 3^2 \otimes 3 = 2 \times 3 = 6 \bmod 7 = 6 \\
3^4 &\overset{\text{已知 1(c)}}{=}& 3^3 \otimes 3 = 6 \times 3 = 18 \bmod 7 = 4 \\
3^5 &\overset{\text{已知 1(c)}}{=}& 3^4 \otimes 3 = 4 \times 3 = 12 \bmod 7 = 5 \\
3^6 &\overset{\text{已知 1(c)}}{=}& 3^5 \otimes 3 = 5 \times 3 = 15 \bmod 7 = 1
\end{gather*}$$

收集這六個值：

$$\begin{gather*}
\left\{3^1, 3^2, 3^3, 3^4, 3^5, 3^6\right\} &=& \left\{3, 2, 6, 4, 5, 1\right\} \\
&=& \mathbf{Z}_7^*
\end{gather*}$$

六個冪次恰好踩遍 $\mathbf{Z}_7^*$ 的六個元素，故 $3$ 是生成元，$\left(\mathbf{Z}_7^*, \otimes\right)$ 循環。

* 註：$3^6 = 1$ 之後就開始重複（$3^7 = 3^1$），所以**不必再往下算**。
  這個「繞回原點的步數」就是 $3$ 的階，見 [元素的階與循環子群](Order_of_Element_and_Cyclic_Subgroup.md)。
* 註：投影片寫 $1 = 3^0 = 3^6$ —— 兩者都對，因為 $3^6 = e$ 而【已知 1(b)】定義 $3^0 = e$。

### (c) proof that the units modulo nine form a cyclic group

由【已知 3】，$\mathbf{Z}_9^* = \left\{1, 2, 4, 5, 7, 8\right\}$。先驗證 $2$ 是生成元：

$$\begin{gather*}
2^1 &=& 2 \\
2^2 &\overset{\text{已知 1(c)}}{=}& 4 \bmod 9 = 4 \\
2^3 &\overset{\text{已知 1(c)}}{=}& 8 \bmod 9 = 8 \\
2^4 &\overset{\text{已知 1(c)}}{=}& 16 \bmod 9 = 7 \\
2^5 &\overset{\text{已知 1(c)}}{=}& 7 \times 2 = 14 \bmod 9 = 5 \\
2^6 &\overset{\text{已知 1(c)}}{=}& 5 \times 2 = 10 \bmod 9 = 1
\end{gather*}$$

$$\begin{gather*}
\left\{2^1, 2^2, 2^3, 2^4, 2^5, 2^6\right\} &=& \left\{2, 4, 8, 7, 5, 1\right\} \\
&\overset{\text{已知 3}}{=}& \mathbf{Z}_9^*
\end{gather*}$$

再驗證 $5$ 也是生成元：

$$\begin{gather*}
5^1 &=& 5 \\
5^2 &\overset{\text{已知 1(c)}}{=}& 25 \bmod 9 = 7 \\
5^3 &\overset{\text{已知 1(c)}}{=}& 7 \times 5 = 35 \bmod 9 = 8 \\
5^4 &\overset{\text{已知 1(c)}}{=}& 8 \times 5 = 40 \bmod 9 = 4 \\
5^5 &\overset{\text{已知 1(c)}}{=}& 4 \times 5 = 20 \bmod 9 = 2 \\
5^6 &\overset{\text{已知 1(c)}}{=}& 2 \times 5 = 10 \bmod 9 = 1
\end{gather*}$$

$$\begin{gather*}
\left\{5^1, 5^2, 5^3, 5^4, 5^5, 5^6\right\} &=& \left\{5, 7, 8, 4, 2, 1\right\} \\
&\overset{\text{已知 3}}{=}& \mathbf{Z}_9^*
\end{gather*}$$

兩者都踩遍全部六個元素，故 $\left(\mathbf{Z}_9^*, \otimes\right)$ 循環，且 $2$ 與 $5$ 皆為生成元。

* 註：**$9$ 不是質數，$\mathbf{Z}_9^*$ 照樣循環。** 循環性與模數是否為質數沒有必然關係 ——
  (e) 的 $\mathbf{Z}_8^*$ 同樣不是質數模，卻不循環。

### (d) disprove that the rationals under addition form a cyclic group

反設 $\left(\mathbf{Q}, +\right)$ 循環，設生成元為 $g$。先排除 $g = 0$ 的情形：

$$\begin{gather*}
\left\{n \cdot 0 \ \middle|\ n \in \mathbf{Z}\right\} &=& \left\{0\right\} \\
\left\{0\right\} &\neq& \mathbf{Q}
\end{gather*}$$

故 $g \neq 0$，可寫成 $g = \dfrac{p}{q}$，其中 $p, q \in \mathbf{Z}$、$p \neq 0$、$q \neq 0$。
考慮這個有理數：

$$x = \frac{p}{2q} \in \mathbf{Q}$$

依【定義 1】，$x$ 必須是 $g$ 的某個整數倍：

$$\begin{gather*}
\frac{p}{2q} &\overset{\text{定義 1}}{=}& n \cdot \frac{p}{q} \qquad \text{for some } n \in \mathbf{Z} \\
\frac{1}{2q} &=& \frac{n}{q} \qquad \text{(兩邊同除以 } p \neq 0\text{)} \\
\frac{1}{2} &=& n \\
n &\notin& \mathbf{Z}
\end{gather*}$$

與 $n \in \mathbf{Z}$ 矛盾。故 $\left(\mathbf{Q}, +\right)$ 不是循環群。

* 註：直覺是「**永遠可以再切一半**」。不管你挑哪個有理數當生成元，
  它的一半就已經逃出你生成的集合。$\mathbf{Z}$ 沒有這個問題，因為整數無法再切。

### (e) disprove that the units modulo eight form a cyclic group

由【已知 3】，$\mathbf{Z}_8^* = \left\{1, 3, 5, 7\right\}$，共四個元素。
計算每個非單位元素的平方：

$$\begin{gather*}
3^2 &=& 9 \bmod 8 = 1 \\
5^2 &=& 25 \bmod 8 = 1 \\
7^2 &=& 49 \bmod 8 = 1
\end{gather*}$$

**每個元素平方都是 $1$。** 於是任一元素 $g \in \mathbf{Z}_8^*$ 生成的集合最多只有兩個元素：

$$\begin{gather*}
\left\{g^n \ \middle|\ n \in \mathbf{Z}\right\} &\overset{\text{已知 1(c)}}{=}& \left\{g^0, g^1\right\} \qquad \text{(因 } g^2 = 1 = g^0\text{，之後全部重複)} \\
\left|\left\{g^n \ \middle|\ n \in \mathbf{Z}\right\}\right| &\le& 2 \\
2 &<& 4 = \left|\mathbf{Z}_8^*\right| \\
\left\{g^n \ \middle|\ n \in \mathbf{Z}\right\} &\overset{\text{定義 1}}{\neq}& \mathbf{Z}_8^*
\end{gather*}$$

沒有任何元素能生成全部四個，故 $\left(\mathbf{Z}_8^*, \otimes\right)$ 不是循環群。

完整的凱萊表（依 [阿貝爾群與非阿貝爾群](Abelian_and_Non_Abelian_Group.md)【定義 2】）：

| $\otimes$ | 1 | 3 | 5 | 7 |
|---|---|---|---|---|
| **1** | 1 | 3 | 5 | 7 |
| **3** | 3 | 1 | 7 | 5 |
| **5** | 5 | 7 | 1 | 3 |
| **7** | 7 | 5 | 3 | 1 |

主對角線全是 $1$ —— 這正是「每個元素都是自己的反元素」的圖像。
這個群稱為 **Klein 四元群 (Klein four-group)**。

* 註：表對主對角線對稱，故 $\mathbf{Z}_8^*$ **是阿貝爾群**（也符合【證明 (f)】的逆命題不成立）。
  **阿貝爾但不循環** —— 這是兩個概念不等價的最小反例。

### (f) proof that every cyclic group is abelian

設 $G$ 循環，生成元為 $g$。任取 $a, b \in G$，依【定義 1】兩者都是 $g$ 的冪次，
而冪次之間的乘法只是指數相加，加法是交換的：

$$\begin{gather*}
a = g^m, \quad b &\overset{\text{定義 1}}{=}& g^n \qquad \text{for some } m, n \in \mathbf{Z} \\
a * b &=& g^m * g^n \\
a * b &\overset{\text{已知 1(c)}}{=}& g^{m+n} \\
a * b &=& g^{n+m} \qquad \text{(整數加法交換)} \\
a * b &\overset{\text{已知 1(c)}}{=}& g^n * g^m \\
a * b &=& b * a \\
\left(G, *\right) &\overset{\text{已知 2}}{=}& \text{阿貝爾群}
\end{gather*}$$

故 $a * b = b * a$ 對所有 $a, b \in G$ 成立，$G$ 是阿貝爾群。

* 註：**整個證明的重點只有一句** —— 循環群裡所有元素都是「同一個 $g$ 的冪次」，
  而冪次的乘法被指數的加法接管，整數加法是交換的，交換性就這樣被繼承下來。
* 註：逆命題不成立，反例見【證明 (e)】。

+++

## 意義與密碼學關聯 (Interpretation and Relevance to Cryptography)

### 循環群就是「一條首尾相接的跑道」

循環群的圖像非常單純：從 $e$ 出發，每次乘上 $g$ 走一步，走著走著會繞回 $e$，
然後永遠重複同一條路線。

$$e \ \to\ g \ \to\ g^2 \ \to\ g^3 \ \to\ \cdots \ \to\ g^{k-1} \ \to\ e$$

**整個群的結構被一個元素完全決定。** 這也是為什麼【證明 (f)】會成立 ——
一條跑道上沒有「岔路」，自然不會有順序問題。

### 離散對數問題：密碼學最重要的單向函數

循環群給了密碼學一個關鍵的**不對稱性**：

| 方向 | 問題 | 難度 |
|---|---|---|
| 正向 | 給 $g$ 與 $n$，算 $g^n$ | **容易**（快速冪，$O(\log n)$ 次乘法） |
| 逆向 | 給 $g$ 與 $g^n$，求 $n$ | **困難**（離散對數問題，DLP） |

【證明 (b)】裡我們從 $3^1$ 一路算到 $3^6$，那是**正向**，六步就走完。
但若有人給你 $3^x \bmod 7 = 5$ 要你求 $x$，在 $\mathbf{Z}_7^*$ 這種小群裡當然一眼看出 $x = 5$；
把模數換成 $2048$ 位元的質數，**目前沒有任何已知的有效演算法**。

Diffie–Hellman、ElGamal、DSA、以及橢圓曲線版本的 ECDH、ECDSA，
安全性全部建立在這個不對稱性上。

### 為什麼要挑生成元，不能隨便挑元素

Diffie–Hellman 要求公開參數裡的 $g$ 是**生成元**（或至少生成一個夠大的子群）。理由在【證明 (e)】：

若 $g$ 不是生成元，$\left\{g^n\right\}$ 只是 $G$ 的一小塊。
$\mathbf{Z}_8^*$ 有四個元素，但任一元素只生成兩個 —— **攻擊者要猜的空間直接砍半**。

實務上這對應到一類真實的攻擊（small subgroup attack）：
若協議沒有檢查對方送來的公鑰是否落在正確的大子群裡，
攻擊者可以送一個階很小的元素，把共享金鑰的可能值壓到只剩幾個，然後窮舉。

**挑生成元不是數學上的潔癖，是實際的安全需求。**

### 哪些 $\mathbf{Z}_n^*$ 是循環的

本檔給了三個資料點：$\mathbf{Z}_7^*$ 循環、$\mathbf{Z}_9^*$ 循環、$\mathbf{Z}_8^*$ 不循環。
完整的答案是一條經典定理（本章不證）：

$$\mathbf{Z}_n^* \ \text{循環} \quad \Longleftrightarrow \quad n \in \left\{1, 2, 4, p^k, 2p^k\right\} \qquad \left(p \ \text{為奇質數}\right)$$

對照：$7$ 是奇質數 $\to$ 循環；$9 = 3^2$ $\to$ 循環；$8 = 2^3$ 不在清單裡 $\to$ 不循環。

**這就是為什麼 Diffie–Hellman 一律選質數模數 $p$** —— $\mathbf{Z}_p^*$ 保證循環，
而且階為 $p-1$，只要 $p-1$ 有大質因數就夠安全。
