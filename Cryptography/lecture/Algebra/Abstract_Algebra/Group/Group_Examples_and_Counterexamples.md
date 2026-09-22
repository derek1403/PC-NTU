# Group Examples and Counterexamples (群的正例與反例)

+++

## 證明目標:

把 `Algebra.pdf` p.5（正例）與 p.6（反例）的每一條**逐一驗證到底**。
正例要把四條公理全部檢查過；反例要明確指出**壞掉的是哪一條公理**並給出具體的反例元素。

* (a)–(f) 以下六組都是群：

$$\left(\mathbf{Z}, +\right), \quad \left(\mathbf{Q}^*, \times\right), \quad \left(5\mathbf{Z}, +\right), \quad \left(\left\{1, -1\right\}, \times\right), \quad \left(\mathbf{Z}_6, \oplus\right), \quad \left(\mathbf{Z}_7^*, \otimes\right)$$

* (g)–(j) 以下四組都**不是**群，且四條公理各壞一條：

$$\left(\mathbf{Z}_7, +\right)_{\text{不取模}}, \quad \left(\mathbf{P}, +\right), \quad \left(\mathbf{Z}, -\right), \quad \left(2\mathbf{Z}+1, \times\right)$$

* 註：投影片 p.5 另列了 $\mathbf{Q}, \mathbf{R}, \mathbf{C}$ 配 $+$ 與 $\mathbf{R}^*, \mathbf{C}^*$ 配 $\times$。
  它們與【證明 (a)】【證明 (b)】的驗證**逐字相同**（只換底層數系），依平行邏輯收束原則不另列，
  於【證明 (a)】【證明 (b)】的註中說明。
* 註：投影片 p.5 最後一條「橢圓曲線上的點配點加法」也是群，但其**結合律**的證明需要射影幾何或
  除子理論，遠超本章範圍。本檔只陳述結論並註明，**不假裝證明它**，見文末。
* 註：本檔是全章驗證四公理的示範樣板。往後的檔案若要驗證某個集合是群，直接沿用這裡的格式。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [群的定義 (Definition of a group)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Group/Group_Definition.html#definitions-and-notation)：** 四條公理，已於本章 [群的定義](Group_Definition.md)【定義 2】給出，此處直接引用

  * (a) 封閉性：

    $$a * b \in G \qquad \text{for all } a, b \in G$$

  * (b) 結合律：

    $$a * \left(b * c\right) = \left(a * b\right) * c \qquad \text{for all } a, b, c \in G$$

  * (c) 單位元素：存在 $e \in G$ 使得

    $$a * e = e * a = a \qquad \text{for all } a \in G$$

  * (d) 反元素：對每個 $a \in G$ 存在 $b \in G$ 使得

    $$a * b = b * a = e$$

  * $G$ : 群的底層集合 (The underlying set of the group) $[\text{集合}]$
  * $*$ : 群運算 (Group operation) $[G \times G \to G]$
  * $a,\ b,\ c$ : 群元素 (Group elements) $[a, b, c \in G]$
  * $e$ : 單位元素 (Identity element) $[e \in G]$

* **【已知 2】 [數系與符號約定 (Number sets and notation)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Number_Sets_and_Notation.html#definitions-and-notation)：** 已於本章 [數系與符號約定](../Number_Sets_and_Notation.md) 定義，此處直接引用

  $$\mathbf{Z}_n = \left\{0, 1, \dots, n-1\right\}, \qquad \mathbf{Z}_n^* = \left\{a \in \mathbf{Z}_n \ \middle|\ \gcd(a, n) = 1\right\}, \qquad \mathbf{P} = \left\{1, 2, 3, \dots\right\}$$

  * $\mathbf{Z}_n$ : 模 $n$ 剩餘類集合 (The set of residues modulo $n$) $[\text{集合}]$
  * $\mathbf{Z}_n^*$ : 模 $n$ 可逆剩餘類集合 (The set of units modulo $n$) $[\text{集合}]$
  * $\mathbf{P}$ : 正整數集合 (The set of positive integers) $[\text{集合}]$
  * $\mathbf{Q}^*$ : 非零有理數集合 (The set of non-zero rationals) $[\text{集合}]$
  * $n$ : 模數 (Modulus) $[n \in \mathbf{P}]$
  * $\gcd$ : 最大公因數 (Greatest common divisor) $[\mathbf{Z} \times \mathbf{Z} \to \mathbf{N}]$

* **【已知 3】 [整數算術的基本性質 (Basic arithmetic of the integers)](https://mathworld.wolfram.com/Integer.html)：** 小學算術，本章直接引用不再重證

  * (a) 加法結合律與乘法結合律：

    $$a + \left(b + c\right) = \left(a + b\right) + c, \qquad a \times \left(b \times c\right) = \left(a \times b\right) \times c$$

  * (b) 加法單位元素與乘法單位元素：

    $$a + 0 = 0 + a = a, \qquad a \times 1 = 1 \times a = a$$

  * (c) 加法反元素：

    $$a + \left(-a\right) = \left(-a\right) + a = 0$$

  * (d) 交換律：

    $$a + b = b + a, \qquad a \times b = b \times a$$

  * $a,\ b,\ c$ : 任意整數（或有理數、實數、複數）(Arbitrary integers, or rationals, reals, complex numbers) $[a, b, c \in \mathbf{Z}]$

* **【已知 4】 [模運算與同餘相容 (Compatibility of modular arithmetic with congruence)](https://mathworld.wolfram.com/Congruence.html)：** 初等數論的標準結果，本章直接引用不再重證。這一條保證模 $n$ 加法與模 $n$ 乘法都是良定義的，且**直接從 $\mathbf{Z}$ 繼承結合律**

  * (a) 運算與取模可交換次序：

    $$\left(a + b\right) \bmod n = \left(\left(a \bmod n\right) + \left(b \bmod n\right)\right) \bmod n, \qquad \left(a \times b\right) \bmod n = \left(\left(a \bmod n\right) \times \left(b \bmod n\right)\right) \bmod n$$

  * (b) 故結合律由 $\mathbf{Z}$ 繼承：

    $$a \oplus \left(b \oplus c\right) = \left(a \oplus b\right) \oplus c, \qquad a \otimes \left(b \otimes c\right) = \left(a \otimes b\right) \otimes c$$

  * $a,\ b,\ c$ : 任意整數 (Arbitrary integers) $[a, b, c \in \mathbf{Z}]$
  * $n$ : 模數 (Modulus) $[n \in \mathbf{P}]$
  * $\oplus$ : 模 $n$ 加法 (Addition modulo $n$) $[\mathbf{Z}_n \times \mathbf{Z}_n \to \mathbf{Z}_n]$
  * $\otimes$ : 模 $n$ 乘法 (Multiplication modulo $n$) $[\mathbf{Z}_n \times \mathbf{Z}_n \to \mathbf{Z}_n]$

* **【已知 5】 [模逆元存在的充要條件 (Criterion for the existence of a modular inverse)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Number_Sets_and_Notation.html#assumptions-preliminaries)：** 已於本章 [數系與符號約定](../Number_Sets_and_Notation.md)【已知 3】引用，此處再次引用

  $$\exists\, b \in \mathbf{Z}_n \ \text{ such that } \ a \otimes b = 1 \quad \Longleftrightarrow \quad \gcd(a, n) = 1$$

  * $a,\ b$ : 剩餘類代表元 (Residue representatives) $[a, b \in \mathbf{Z}_n]$
  * $n$ : 模數 (Modulus) $[n \in \mathbf{P}]$
  * $\otimes$ : 模 $n$ 乘法 (Multiplication modulo $n$) $[\mathbf{Z}_n \times \mathbf{Z}_n \to \mathbf{Z}_n]$
  * $\gcd$ : 最大公因數 (Greatest common divisor) $[\mathbf{Z} \times \mathbf{Z} \to \mathbf{N}]$

* **【已知 6】 [歐幾里得引理 (Euclid's lemma)](https://mathworld.wolfram.com/EuclidsLemma.html)：** 初等數論的標準結果，本章直接引用不再重證。【證明 (f)】的封閉性靠這一條

  $$p \ \text{為質數}, \quad p \mid ab \quad \Longrightarrow \quad p \mid a \ \text{ 或 } \ p \mid b$$

  * $p$ : 質數 (A prime) $[p \in \mathbf{P}]$
  * $a,\ b$ : 任意整數 (Arbitrary integers) $[a, b \in \mathbf{Z}]$

* **【定義 1】 五的倍數集合 (The set of multiples of five)：**

  $$5\mathbf{Z} \overset{\text{def}}{=} \left\{5a \ \middle|\ a \in \mathbf{Z}\right\}$$

  * $5\mathbf{Z}$ : 五的倍數集合 (The set of multiples of five) $[\text{集合}]$
  * $a$ : 整數係數 (Integer coefficient) $[a \in \mathbf{Z}]$
  * $\mathbf{Z}$ : 整數集合 (The set of integers) $[\text{集合}]$

* **【定義 2】 奇數集合 (The set of odd integers)：**

  $$2\mathbf{Z} + 1 \overset{\text{def}}{=} \left\{2a + 1 \ \middle|\ a \in \mathbf{Z}\right\}$$

  * $2\mathbf{Z} + 1$ : 奇數集合 (The set of odd integers) $[\text{集合}]$
  * $a$ : 整數係數 (Integer coefficient) $[a \in \mathbf{Z}]$
  * $\mathbf{Z}$ : 整數集合 (The set of integers) $[\text{集合}]$

+++

## 證明:

### (a) proof the integers under addition form a group

四條公理逐條檢查 $\left(\mathbf{Z}, +\right)$：

$$\begin{gather*}
a + b &\in& \mathbf{Z} \qquad \text{(封閉性，整數相加仍為整數)} \\
a + \left(b + c\right) &\overset{\text{已知 3(a)}}{=}& \left(a + b\right) + c \qquad \text{(結合律)} \\
a + 0 &\overset{\text{已知 3(b)}}{=}& a \qquad \text{(單位元素 } e = 0 \in \mathbf{Z}\text{)} \\
a + \left(-a\right) &\overset{\text{已知 3(c)}}{=}& 0 \qquad \text{(反元素 } a^{-1} = -a \in \mathbf{Z}\text{)}
\end{gather*}$$

四條全中，故 $\left(\mathbf{Z}, +\right)$ 是群。

* 註：$\left(\mathbf{Q}, +\right)$、$\left(\mathbf{R}, +\right)$、$\left(\mathbf{C}, +\right)$ 的驗證
  **與本小節逐字相同**（【已知 3】的四條性質在這三個數系上同樣成立，單位元素同樣是 $0$，
  反元素同樣是 $-a$），故不另立小節。
* 註：本小節的單位元素是 $0$ 而非 $1$ —— **單位元素由運算決定，不是集合裡「看起來最特別」的那個元素**。

### (b) proof the non-zero rationals under multiplication form a group

四條公理逐條檢查 $\left(\mathbf{Q}^*, \times\right)$。先確認封閉性（這是本例唯一需要動腦的一條）：

$$\begin{gather*}
a \neq 0, \quad b &\neq& 0 \\
a \times b &\neq& 0 \qquad \text{(有理數無零因子)} \\
a \times b &\in& \mathbf{Q}^* \qquad \text{(封閉性)}
\end{gather*}$$

其餘三條：

$$\begin{gather*}
a \times \left(b \times c\right) &\overset{\text{已知 3(a)}}{=}& \left(a \times b\right) \times c \qquad \text{(結合律)} \\
a \times 1 &\overset{\text{已知 3(b)}}{=}& a \qquad \text{(單位元素 } e = 1 \in \mathbf{Q}^*\text{)} \\
a \times \frac{1}{a} &=& 1 \qquad \text{(反元素 } a^{-1} = \tfrac{1}{a} \in \mathbf{Q}^*\text{)}
\end{gather*}$$

四條全中，故 $\left(\mathbf{Q}^*, \times\right)$ 是群。

* 註：$\left(\mathbf{R}^*, \times\right)$、$\left(\mathbf{C}^*, \times\right)$ 的驗證與本小節逐字相同，故不另立小節。
* 註：**必須先把 $0$ 挖掉**才成立 —— $\left(\mathbf{Q}, \times\right)$ 不是群，因為 $0$ 沒有乘法反元素。
  這就是【已知 2】裡星號記號的全部意義。

### (c) proof the multiples of five under addition form a group

$5\mathbf{Z}$ 的元素都長成 $5a$ 的樣子（【定義 1】），逐條檢查：

$$\begin{gather*}
5a + 5b &=& 5\left(a + b\right) \\
5a + 5b &\overset{\text{定義 1}}{\in}& 5\mathbf{Z} \qquad \text{(封閉性，因 } a + b \in \mathbf{Z}\text{)} \\
5a + \left(5b + 5c\right) &\overset{\text{已知 3(a)}}{=}& \left(5a + 5b\right) + 5c \qquad \text{(結合律，由 } \mathbf{Z} \text{ 繼承)} \\
0 &=& 5 \times 0 \\
0 &\in& 5\mathbf{Z} \qquad \text{(單位元素 } e = 0\text{)} \\
5a + 5\left(-a\right) &\overset{\text{已知 3(c)}}{=}& 0 \qquad \text{(反元素 } \left(5a\right)^{-1} = 5\left(-a\right) \in 5\mathbf{Z}\text{)}
\end{gather*}$$

四條全中，故 $\left(5\mathbf{Z}, +\right)$ 是群。

* 註：把 $5$ 換成任意 $n \in \mathbf{Z}$ 論證完全不變，故 $\left(n\mathbf{Z}, +\right)$ 對所有 $n$ 都是群。
* 註：$5\mathbf{Z} \subseteq \mathbf{Z}$ 且兩者用同一個運算，所以本例其實是
  [子群的例子](Subgroup_Examples.md) 的預告 —— 用 [子群判別法](Subgroup_Criterion.md) 只需檢查兩條而非四條。

### (d) proof the two-element sign set under multiplication forms a group

$\left\{1, -1\right\}$ 只有兩個元素，封閉性用完整的乘法表檢查：

$$\begin{gather*}
1 \times 1 &=& 1 \\
1 \times \left(-1\right) &=& -1 \\
\left(-1\right) \times 1 &=& -1 \\
\left(-1\right) \times \left(-1\right) &=& 1
\end{gather*}$$

四個乘積都落在 $\left\{1, -1\right\}$ 內，封閉性成立。其餘三條：

$$\begin{gather*}
a \times \left(b \times c\right) &\overset{\text{已知 3(a)}}{=}& \left(a \times b\right) \times c \qquad \text{(結合律，由 } \mathbf{Z} \text{ 繼承)} \\
a \times 1 &\overset{\text{已知 3(b)}}{=}& a \qquad \text{(單位元素 } e = 1\text{)} \\
1 \times 1 &=& 1 \qquad \text{(} 1 \text{ 的反元素是自己)} \\
\left(-1\right) \times \left(-1\right) &=& 1 \qquad \text{(} -1 \text{ 的反元素也是自己)}
\end{gather*}$$

四條全中，故 $\left(\left\{1, -1\right\}, \times\right)$ 是群。

### (e) proof the residues modulo six under addition form a group

$\mathbf{Z}_6 = \left\{0,1,2,3,4,5\right\}$ 配模 $6$ 加法 $\oplus$，逐條檢查：

$$\begin{gather*}
a \oplus b &\overset{\text{已知 4(a)}}{=}& \left(a + b\right) \bmod 6 \\
a \oplus b &\in& \left\{0, 1, 2, 3, 4, 5\right\} \qquad \text{(封閉性，餘數必落在 } 0 \text{ 到 } 5\text{)} \\
a \oplus b &\overset{\text{已知 2}}{\in}& \mathbf{Z}_6 \\
a \oplus \left(b \oplus c\right) &\overset{\text{已知 4(b)}}{=}& \left(a \oplus b\right) \oplus c \qquad \text{(結合律)} \\
a \oplus 0 &\overset{\text{已知 3(b)}}{=}& a \qquad \text{(單位元素 } e = 0 \in \mathbf{Z}_6\text{)}
\end{gather*}$$

反元素分成 $a = 0$ 與 $a \neq 0$ 兩種情形：

$$\begin{gather*}
0 \oplus 0 &=& 0 \qquad \text{(} 0 \text{ 的反元素是自己)} \\
a \oplus \left(6 - a\right) &=& 6 \bmod 6 \\
a \oplus \left(6 - a\right) &=& 0 \qquad \text{(} a \neq 0 \text{ 的反元素是 } 6 - a \in \mathbf{Z}_6\text{)}
\end{gather*}$$

四條全中，故 $\left(\mathbf{Z}_6, \oplus\right)$ 是群。

* 註：把 $6$ 換成任意 $n \in \mathbf{P}$ 論證完全不變，故 $\left(\mathbf{Z}_n, \oplus\right)$ 對所有 $n$ 都是群。
  **$n$ 是不是質數完全無所謂** —— 這一點在【證明 (f)】會變得不一樣。

### (f) proof the units modulo seven under multiplication form a group

因 $7$ 為質數，$\left\{1,2,3,4,5,6\right\}$ 每個元素都與 $7$ 互質，故：

$$\begin{gather*}
\mathbf{Z}_7^* &\overset{\text{已知 2}}{=}& \left\{a \in \mathbf{Z}_7 \ \middle|\ \gcd(a, 7) = 1\right\} \\
\mathbf{Z}_7^* &=& \left\{1, 2, 3, 4, 5, 6\right\}
\end{gather*}$$

封閉性要證「兩個與 $7$ 互質的數相乘後仍與 $7$ 互質」，用歐幾里得引理的逆否命題：

$$\begin{gather*}
\gcd(a, 7) = 1, \quad \gcd(b, 7) &=& 1 \\
7 \nmid a, \quad 7 &\nmid& b \qquad \text{(} 7 \text{ 為質數，故互質等價於不整除)} \\
7 &\overset{\text{已知 6}}{\nmid}& ab \qquad \text{(歐幾里得引理的逆否)} \\
\gcd\left(ab \bmod 7,\ 7\right) &=& 1 \\
a \otimes b &\in& \mathbf{Z}_7^* \qquad \text{(封閉性)}
\end{gather*}$$

其餘三條：

$$\begin{gather*}
a \otimes \left(b \otimes c\right) &\overset{\text{已知 4(b)}}{=}& \left(a \otimes b\right) \otimes c \qquad \text{(結合律)} \\
a \otimes 1 &\overset{\text{已知 3(b)}}{=}& a \qquad \text{(單位元素 } e = 1 \in \mathbf{Z}_7^*\text{)}
\end{gather*}$$

反元素的存在性直接由模逆元判準給出，因為 $\mathbf{Z}_7^*$ 的元素依定義都滿足 $\gcd(a,7)=1$：

$$\begin{gather*}
\gcd(a, 7) = 1 &\overset{\text{已知 5}}{\Longrightarrow}& \exists\, b \in \mathbf{Z}_7^* \ \text{ with } \ a \otimes b = 1
\end{gather*}$$

把六個反元素明確算出來：

$$\begin{gather*}
1 \otimes 1 &=& 1 \\
2 \otimes 4 &=& 8 \bmod 7 \\
2 \otimes 4 &=& 1 \\
3 \otimes 5 &=& 15 \bmod 7 \\
3 \otimes 5 &=& 1 \\
6 \otimes 6 &=& 36 \bmod 7 \\
6 \otimes 6 &=& 1
\end{gather*}$$

即 $1^{-1}=1$、$2^{-1}=4$、$4^{-1}=2$、$3^{-1}=5$、$5^{-1}=3$、$6^{-1}=6$，六個元素都可逆。
四條全中，故 $\left(\mathbf{Z}_7^*, \otimes\right)$ 是群。

* 註：**這裡 $7$ 是質數這件事被用到了兩次**：一次讓 $\mathbf{Z}_7^*$ 恰好是 $\left\{1,\dots,6\right\}$，
  一次讓封閉性可以套歐幾里得引理。但 $\left(\mathbf{Z}_n^*, \otimes\right)$ 對**任意** $n$ 都是群，
  只是 $n$ 為合數時 $\mathbf{Z}_n^*$ 會少掉一些元素（見 [群的階](Group_Order.md)）。

### (g) disprove closure for the residues modulo seven under un-modded addition

投影片 p.6 第一條：$\mathbf{Z}_7 = \left\{0,1,2,3,4,5,6\right\}$ 配**普通加法**（不取模）。
取 $a = 5$、$b = 4$：

$$\begin{gather*}
5 + 4 &=& 9 \\
9 &\notin& \left\{0, 1, 2, 3, 4, 5, 6\right\} \\
5 + 4 &\overset{\text{已知 1(a)}}{\notin}& \mathbf{Z}_7
\end{gather*}$$

**封閉性（【已知 1(a)】）失敗**，故不是群。

* 註：其餘三條公理其實都成立（結合律由 $\mathbf{Z}$ 繼承、$0$ 是單位元素、…），
  但只要壞一條就不是群。本例與【證明 (e)】的差別**只在有沒有取模**。

### (h) disprove the existence of an identity for the positive integers under addition

投影片 p.6 第二條：$\mathbf{P} = \left\{1,2,3,\dots\right\}$ 配加法。
假設單位元素 $e \in \mathbf{P}$ 存在，則對 $a = 1$ 必須成立：

$$\begin{gather*}
1 + e &\overset{\text{已知 1(c)}}{=}& 1 \\
e &=& 0 \\
e &\overset{\text{已知 2}}{\notin}& \mathbf{P}
\end{gather*}$$

**單位元素（【已知 1(c)】）不存在**，故不是群。

* 註：封閉性成立（正整數相加仍為正整數）、結合律成立，壞掉的只有單位元素這一條。
* 註：把 $0$ 加回去變成 $\left(\mathbf{N}, +\right)$ 仍然不是群 —— 這次單位元素有了，
  但 $1$ 找不到反元素（需要 $-1 \notin \mathbf{N}$），**壞在反元素那一條**。
  一定要把負數也加回去，才得到【證明 (a)】的 $\left(\mathbf{Z}, +\right)$。

### (i) disprove associativity for the integers under subtraction

投影片 p.6 第三條：$\mathbf{Z}$ 配減法。取 $a = 1$、$b = 2$、$c = 3$，左右兩邊分別算：

$$\begin{gather*}
1 - \left(2 - 3\right) &=& 1 - \left(-1\right) \\
1 - \left(2 - 3\right) &=& 2 \\
\left(1 - 2\right) - 3 &=& \left(-1\right) - 3 \\
\left(1 - 2\right) - 3 &=& -4 \\
2 &\neq& -4 \\
1 - \left(2 - 3\right) &\overset{\text{已知 1(b)}}{\neq}& \left(1 - 2\right) - 3
\end{gather*}$$

**結合律（【已知 1(b)】）失敗**，故不是群。

* 註：封閉性成立、$a - 0 = a$ 看似有右單位元素（但 $0 - a = -a \neq a$，故連單位元素都不合格）。
  投影片指出的是結合律，這是最本質的那一條 —— 沒有結合律，
  [群的定義](Group_Definition.md)【定義 3(b)】的冪次 $g^n$ 根本無法定義。

### (j) disprove the existence of inverses for the odd integers under multiplication

投影片 p.6 第四條：$2\mathbf{Z}+1$ 配乘法（【定義 2】）。先確認前三條都成立：

$$\begin{gather*}
\left(2a+1\right)\left(2b+1\right) &=& 4ab + 2a + 2b + 1 \\
\left(2a+1\right)\left(2b+1\right) &=& 2\left(2ab + a + b\right) + 1 \\
\left(2a+1\right)\left(2b+1\right) &\overset{\text{定義 2}}{\in}& 2\mathbf{Z}+1 \qquad \text{(封閉性成立，因 } 2ab+a+b \in \mathbf{Z}\text{)} \\
a \times \left(b \times c\right) &\overset{\text{已知 3(a)}}{=}& \left(a \times b\right) \times c \qquad \text{(結合律成立)} \\
1 &=& 2 \times 0 + 1 \\
1 &\in& 2\mathbf{Z}+1 \qquad \text{(單位元素 } e = 1 \text{ 存在)}
\end{gather*}$$

但反元素這一條壞了。取 $a = 3 \in 2\mathbf{Z}+1$，假設其反元素 $b$ 存在：

$$\begin{gather*}
3 \times b &\overset{\text{已知 1(d)}}{=}& 1 \\
b &=& \frac{1}{3} \\
b &\notin& \mathbf{Z} \\
b &\notin& 2\mathbf{Z}+1
\end{gather*}$$

**反元素（【已知 1(d)】）不存在**，故不是群。

* 註：本例是四個反例中**唯一前三條全部成立**的一個 —— 只壞最後一條。
  這種「有封閉性、有結合律、有單位元素、但不見得有反元素」的結構稱為**么半群 (Monoid)**，
  本章不深入討論。

+++

## 未證明的部分 (Stated Without Proof)

投影片 p.5 最後一條列出**橢圓曲線上的點配點加法**也是群：

$$E = \left\{\left(x, y\right) \in \mathbf{R}^2 \ \middle|\ y^2 = x^3 + ax + b\right\} \cup \left\{\infty\right\}$$

* 封閉性、單位元素（無窮遠點 $\infty$）、反元素（$\left(x, y\right)^{-1} = \left(x, -y\right)$）
  都可以由幾何作圖直接讀出。
* **但結合律的證明極為冗長**，標準做法需要射影幾何的 Cayley–Bacharach 定理，
  或代數幾何的除子 (divisor) 理論。這超出本章範圍。

本檔**不假裝證明它**，僅陳述結論並註明出處：見 Silverman,
*The Arithmetic of Elliptic Curves*, Ch. III。

+++

## 意義與密碼學關聯 (Interpretation and Relevance to Cryptography)

### 四個反例是四條公理的「壓力測試」

投影片挑這四個反例不是隨便選的 —— 它們**一條公理壞一個**，剛好構成一組完整的對照：

| 反例 | 壞掉的公理 | 其他三條 | 修好的辦法 |
|---|---|---|---|
| $\left(\mathbf{Z}_7, +\right)$ 不取模 | 封閉性 | 都成立 | 加上取模 $\to$【證明 (e)】 |
| $\left(\mathbf{P}, +\right)$ | 單位元素 | 都成立 | 補上 $0$ 與負數 $\to$【證明 (a)】 |
| $\left(\mathbf{Z}, -\right)$ | 結合律 | — | 換成加法 $\to$【證明 (a)】 |
| $\left(2\mathbf{Z}+1, \times\right)$ | 反元素 | **全都成立** | 換到 $\mathbf{Q}^*$ $\to$【證明 (b)】 |

**檢查一個結構是不是群，就照這四條依序掃過去。** 實務上壞掉的順序也大致如此：
封閉性最常壞（忘了取模），反元素次之（忘了把不可逆的元素挖掉）。

### $\mathbf{Z}_n$ 與 $\mathbf{Z}_n^*$：密碼學為什麼同時需要這兩個

【證明 (e)】與【證明 (f)】是本檔最重要的兩個例子，因為 RSA 同時用到它們：

* $\left(\mathbf{Z}_n, \oplus\right)$ —— **明文空間**。任意 $n$ 都是群，不挑。
* $\left(\mathbf{Z}_n^*, \otimes\right)$ —— **金鑰空間**。必須把 $\gcd(a,n) \neq 1$ 的元素挖掉，
  否則反元素公理會壞掉，也就是**解密會失敗**。

RSA 要求 $\gcd\left(e, \varphi(n)\right) = 1$，在群論語言裡就是一句話：
**$e$ 必須是 $\mathbf{Z}_{\varphi(n)}^*$ 的元素，否則它在那個群裡沒有反元素，私鑰 $d$ 不存在。**

### 程式思維：怎麼把這四條寫成測試

```python
def is_group(elements, op, identity):
    # 1. 封閉性
    if any(op(a, b) not in elements for a in elements for b in elements):
        return False
    # 2. 結合律
    if any(op(a, op(b, c)) != op(op(a, b), c)
           for a in elements for b in elements for c in elements):
        return False
    # 3. 單位元素
    if any(op(a, identity) != a or op(identity, a) != a for a in elements):
        return False
    # 4. 反元素
    return all(any(op(a, b) == identity and op(b, a) == identity for b in elements)
               for a in elements)
```

有限群可以這樣暴力驗（$\left|G\right|^3$ 次運算），無限群就只能像本檔一樣用代數論證。
**這也是為什麼密碼學只用有限群** —— 不只是因為電腦存不下無限集合，
更因為安全性分析需要「元素個數」這個量（見 [群的階](Group_Order.md)）。
