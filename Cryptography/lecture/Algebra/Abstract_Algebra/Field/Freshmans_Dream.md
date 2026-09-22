# Freshman's Dream (新生之夢)

+++

## 證明目標:

`Algebra.pdf` p.47（下半）。高中生最愛犯的錯誤 $\left(a+b\right)^2 = a^2 + b^2$，
在特徵 $p$ 的體裡**把指數換成 $p$ 就是對的**。

* (a) 基本情形：

$$\left(a + b\right)^p = a^p + b^p \qquad \left(\mathrm{ch}(F) = p\right)$$

* (b) 歸納步驟 —— 指數可以一路推到 $p$ 的任意次冪：

$$\left(a + b\right)^{p^n} = a^{p^n} + b^{p^n} \qquad \text{for all } n \in \mathbf{P}$$

* (c) 用 $\mathbf{Z}_5$ 與 $\mathbf{Z}_2$ 驗證。

* $F$ : 特徵為 $p$ 的體 (A field of characteristic $p$) $[\text{集合}]$
* $a,\ b$ : 體元素 (Field elements) $[a, b \in F]$
* $p$ : 體的特徵，必為質數 (The characteristic, necessarily prime) $[p \in \mathbf{P}]$
* $n$ : 冪次的層數 (The exponent level) $[n \in \mathbf{P}]$
* 註：**這個等式在 $\mathbf{Q}, \mathbf{R}, \mathbf{C}$ 裡是錯的** ——
  那些體的特徵是 $0$（[體的特徵](Characteristic_of_a_Field.md)【證明 (c)】），
  中間項不會消失。「新生之夢」這個名字就是在取笑把它用錯地方的人。
* 註：整條證明的支柱是 [質數整除二項式係數](Prime_Divides_Binomial_Coefficient.md) ——
  中間的 $p-1$ 個二項式係數全被 $p$ 整除，在特徵 $p$ 的體裡全部歸零。
* 註：映射 $\phi(x) = x^p$ 因此是一個**環同態**（保加法由本檔給出、保乘法顯然），
  稱為 **Frobenius 自同態**。它是有限體理論的核心工具，見文末。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [體的特徵 (Characteristic of a field)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Field/Characteristic_of_a_Field.html#b-proof-that-a-positive-characteristic-must-be-prime)：** 已於本章 [體的特徵](Characteristic_of_a_Field.md)【定義 1】【證明 (b)】給出並證明，此處直接引用不再重證

  * (a) 特徵的定義：

    $$\mathrm{ch}(F) = p \quad \Longrightarrow \quad p \cdot 1_F = 0$$

  * (b) 正特徵必為質數：

    $$\mathrm{ch}(F) = p > 0 \quad \Longrightarrow \quad p \ \text{為質數}$$

  * $F$ : 體的底層集合 (The underlying set of the field) $[\text{集合}]$
  * $\mathrm{ch}(F)$ : $F$ 的特徵 (The characteristic of $F$) $[\mathrm{ch}(F) \in \mathbf{N}]$
  * $1_F$ : $F$ 的乘法單位元素 (The multiplicative identity of $F$) $[1_F \in F]$
  * $p$ : 特徵值 (The characteristic value) $[p \in \mathbf{P}]$
  * 註：(b) 是本檔能引用 [質數整除二項式係數](Prime_Divides_Binomial_Coefficient.md) 的前提 ——
    那條引理只對質數成立。

* **【已知 2】 [質數整除二項式係數 (A prime divides the interior binomial coefficients)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Field/Prime_Divides_Binomial_Coefficient.html#a-proof-that-a-prime-divides-the-interior-binomial-coefficients)：** 已於本章 [質數整除二項式係數](Prime_Divides_Binomial_Coefficient.md)【證明 (a)】完整證明，此處直接引用不再重證

  $$p \ \Bigg|\ \binom{p}{i} \qquad \text{for } 1 \le i \le p-1$$

  * $p$ : 質數 (A prime) $[p \in \mathbf{P}]$
  * $i$ : 二項式係數的下標 (The lower index) $[i \in \mathbf{Z},\ 1 \le i \le p-1]$
  * $\dbinom{p}{i}$ : 二項式係數 (The binomial coefficient) $[\dbinom{p}{i} \in \mathbf{P}]$

* **【已知 3】 [二項式定理 (Binomial theorem)](https://mathworld.wolfram.com/BinomialTheorem.html)：** 對任何**交換**環都成立的標準結果（用歸納法與分配律證出），本章直接引用不再重證

  $$\left(a + b\right)^m = \sum_{i=0}^{m}\binom{m}{i}\,a^{i}\,b^{m-i}$$

  * $a,\ b$ : 交換環中的元素 (Elements of a commutative ring) $[a, b \in R]$
  * $m$ : 指數 (The exponent) $[m \in \mathbf{N}]$
  * $i$ : 求和指標 (The summation index) $[i \in \mathbf{N}]$
  * $\dbinom{m}{i}$ : 二項式係數 (The binomial coefficient) $[\dbinom{m}{i} \in \mathbf{N}]$
  * 註：**交換性是必要的** —— 非交換環裡 $\left(a+b\right)^2 = a^2 + ab + ba + b^2$ 無法合併成 $2ab$。
    體依 [體的定義](Field_Definition.md)【定義 1】必定交換，故適用。
  * 註：式中的 $\dbinom{m}{i}a^ib^{m-i}$ 是**整數倍**（見 [環的定義](../Ring/Ring_Definition.md)【定義 2(c)】），
    不是體的乘法。這個區分在【推導 1】處理。

* **【已知 4】 [整數倍記號與環的公理 (Integer multiples and ring axioms)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Ring/Ring_Definition.html#definitions-and-notation)：** 已於本章 [環的定義](../Ring/Ring_Definition.md)【定義 1】【定義 2(c)】給出，此處直接引用

  * (a) 整數倍：

    $$m \cdot x \overset{\text{def}}{=} \underbrace{x + \cdots + x}_{m \ \text{個}}$$

  * (b) 分配律與結合律：

    $$x\left(y+z\right) = xy + xz, \qquad x\left(yz\right) = \left(xy\right)z$$

  * (c) 乘以零得零（[環的基本命題](../Ring/Ring_Basic_Propositions.md)【證明 (a)】）：

    $$0 \times x = 0$$

  * $x,\ y,\ z$ : 環元素 (Ring elements) $[x, y, z \in R]$
  * $m$ : 正整數 (A positive integer) $[m \in \mathbf{P}]$

* **【假設 1】 歸納假設 (Induction hypothesis)：** 【證明 (b)】對 $n$ 做歸納時的假設。設結論對 $n$ 成立

  $$\left(a + b\right)^{p^{n}} = a^{p^{n}} + b^{p^{n}}$$

  * $a,\ b$ : 體元素 (Field elements) $[a, b \in F]$
  * $p$ : 體的特徵 (The characteristic of the field) $[p \in \mathbf{P}]$
  * $n$ : 歸納變數 (The induction variable) $[n \in \mathbf{P}]$
  * 註：歸納的基底情形 $n = 1$ 由【證明 (a)】給出，不需要本假設。

* **【推導 1】 特徵 $p$ 讓任何元素的 $p$ 倍歸零 (Characteristic p annihilates every element)：** 【證明 (a)】的關鍵。
  【已知 1(a)】只說 $p \cdot 1_F = 0$，本卡片把它推廣到**所有**元素

  $$\begin{gather*}
  p \cdot x &\overset{\text{已知 4(a)}}{=}& \underbrace{x + \cdots + x}_{p} \\
  p \cdot x &\overset{\text{已知 4(a)}}{=}& \underbrace{1_F \times x + \cdots + 1_F \times x}_{p} \\
  p \cdot x &\overset{\text{已知 4(b)}}{=}& \left(\underbrace{1_F + \cdots + 1_F}_{p}\right) \times x \\
  p \cdot x &\overset{\text{已知 4(a)}}{=}& \left(p \cdot 1_F\right) \times x \\
  p \cdot x &\overset{\text{已知 1(a)}}{=}& 0 \times x \\
  p \cdot x &\overset{\text{已知 4(c)}}{=}& 0
  \end{gather*}$$

  * $x$ : 任意體元素 (An arbitrary field element) $[x \in F]$
  * $p$ : 體的特徵 (The characteristic of the field) $[p \in \mathbf{P}]$
  * $1_F$ : $F$ 的乘法單位元素 (The multiplicative identity of $F$) $[1_F \in F]$
  * 註：第三行用的是**反向的分配律** —— 把 $p$ 個相同的 $x$ 合併，
    提出共同的 $x$，剩下 $p$ 個 $1_F$ 相加。
  * 註：更一般地，$m \cdot x = 0$ 只要 $p \mid m$ ——
    把 $m = pk$ 代入即得 $m \cdot x = k \cdot \left(p \cdot x\right) = k \cdot 0 = 0$。
    【證明 (a)】用的就是這個推廣形式。

* **【推導 2】 被 $p$ 整除的係數項全部消失 (Coefficients divisible by p vanish)：** 【證明 (a)】要用

  $$\begin{gather*}
  \binom{p}{i} &\overset{\text{已知 2}}{=}& p\,k_i \qquad \text{for some } k_i \in \mathbf{Z},\ 1 \le i \le p-1 \\
  \binom{p}{i}\,a^{i}b^{p-i} &\overset{\text{已知 4(a)}}{=}& \left(p\,k_i\right) \cdot \left(a^{i}b^{p-i}\right) \\
  \binom{p}{i}\,a^{i}b^{p-i} &\overset{\text{已知 4(a)}}{=}& k_i \cdot \left(p \cdot a^{i}b^{p-i}\right) \\
  \binom{p}{i}\,a^{i}b^{p-i} &\overset{\text{推導 1}}{=}& k_i \cdot 0 \\
  \binom{p}{i}\,a^{i}b^{p-i} &=& 0
  \end{gather*}$$

  * $a,\ b$ : 體元素 (Field elements) $[a, b \in F]$
  * $p$ : 體的特徵 (The characteristic of the field) $[p \in \mathbf{P}]$
  * $i$ : 求和指標 (The summation index) $[i \in \mathbf{Z},\ 1 \le i \le p-1]$
  * $k_i$ : 商 (The quotient) $[k_i \in \mathbf{Z}]$
  * 註：**$i$ 的範圍限制在這裡再次是要害** —— 只有 $1 \le i \le p-1$ 的項會消失，
    $i = 0$ 與 $i = p$ 的係數都是 $1$，不被 $p$ 整除，因此存活下來。

+++

## 證明:

### (a) proof of the base case

由【已知 1(b)】，$p$ 是質數，故【已知 2】適用。展開二項式後，
中間的 $p-1$ 項全部由【推導 2】歸零：

$$\begin{gather*}
\left(a + b\right)^p &\overset{\text{已知 3}}{=}& \sum_{i=0}^{p}\binom{p}{i}\,a^{i}b^{p-i} \\
\left(a + b\right)^p &=& \binom{p}{0}b^{p} + \sum_{i=1}^{p-1}\binom{p}{i}a^{i}b^{p-i} + \binom{p}{p}a^{p} \\
\left(a + b\right)^p &\overset{\text{推導 2}}{=}& \binom{p}{0}b^{p} + 0 + \binom{p}{p}a^{p} \\
\left(a + b\right)^p &=& b^{p} + a^{p} \\
\left(a + b\right)^p &=& a^{p} + b^{p}
\end{gather*}$$

與投影片一致。

* 註：第三行是整條證明的全部內容 —— **中間那一整排消失了**。
  消失的原因是【已知 2】（係數被 $p$ 整除）加上【推導 1】（特徵 $p$ 讓 $p$ 倍歸零），
  兩者缺一不可。
* 註：$\dbinom{p}{0} = \dbinom{p}{p} = 1$，故最後兩項的係數是 $1 \cdot x = x$，原封不動。

### (b) proof of the inductive step

**基底情形 $n = 1$** 就是【證明 (a)】。

**歸納步驟**：設結論對 $n$ 成立（【假設 1】），證明它對 $n+1$ 也成立。
把 $p^{n+1}$ 次方拆成「先 $p^n$ 次方、再 $p$ 次方」：

$$\begin{gather*}
\left(a + b\right)^{p^{n+1}} &\overset{\text{已知 4(b)}}{=}& \left[\left(a+b\right)^{p^{n}}\right]^{p} \\
\left(a + b\right)^{p^{n+1}} &\overset{\text{假設 1}}{=}& \left[a^{p^{n}} + b^{p^{n}}\right]^{p} \\
\left(a + b\right)^{p^{n+1}} &\overset{\text{證明 (a)}}{=}& \left(a^{p^{n}}\right)^{p} + \left(b^{p^{n}}\right)^{p} \\
\left(a + b\right)^{p^{n+1}} &\overset{\text{已知 4(b)}}{=}& a^{p^{n+1}} + b^{p^{n+1}}
\end{gather*}$$

歸納完成，故對所有 $n \in \mathbf{P}$ 成立。

與投影片的三行（$n = 2$ 的情形加上「by induction」）完全對應：

| 投影片 | 本檔 |
|---|---|
| $\left(a+b\right)^{p^2} = \left[\left(a+b\right)^p\right]^p$ | 第一行 |
| $= \left[a^p + b^p\right]^p$ | 第二行（投影片用的是 $n=1$ 的結論，本檔用【假設 1】） |
| $= \left(a^p\right)^p + \left(b^p\right)^p = a^{p^2} + b^{p^2}$ | 第三、四行 |
| by induction | 歸納完成 |

* 註：**第三行把【證明 (a)】套在 $a^{p^n}$ 與 $b^{p^n}$ 這兩個新元素上** ——
  【證明 (a)】對**任意**兩個體元素都成立，不限於原本的 $a, b$，
  所以可以這樣反覆套用。

### (c) verify in two concrete finite fields

**在 $\mathbf{Z}_5$（特徵 $5$）中**，取 $a = 1$、$b = 2$：

$$\begin{gather*}
\left(1 + 2\right)^5 &=& 3^5 \\
3^5 &=& 243 \\
243 \bmod 5 &=& 3 \\
1^5 + 2^5 &=& 1 + 32 \\
1 + 32 &=& 33 \\
33 \bmod 5 &=& 3
\end{gather*}$$

兩邊都是 $3$，等式成立。

**在 $\mathbf{Z}_2$（特徵 $2$）中**，取 $a = b = 1$：

$$\begin{gather*}
\left(1 + 1\right)^2 &=& 0^2 = 0 \\
1^2 + 1^2 &=& 1 + 1 \\
1 + 1 \bmod 2 &=& 0
\end{gather*}$$

兩邊都是 $0$，等式成立。

**對照：在 $\mathbf{Q}$（特徵 $0$）中等式失敗**：

$$\begin{gather*}
\left(1 + 2\right)^5 &=& 243 \\
1^5 + 2^5 &=& 33 \\
243 &\neq& 33
\end{gather*}$$

與【證明 (a)】的前提一致 —— 特徵必須是正的質數，等式才成立。

+++

## 意義與密碼學關聯 (Interpretation and Relevance to Cryptography)

### 為什麼中間項會消失

整件事只有一句話：

$$\text{帕斯卡三角形第 } p \text{ 列的中間項全被 } p \text{ 整除，而特徵 } p \text{ 的體裡 } p \cdot x = 0$$

兩個事實撞在一起，中間項就人間蒸發了。
第一個事實是 [質數整除二項式係數](Prime_Divides_Binomial_Coefficient.md)，
第二個是本檔的【推導 1】。

看 $p = 5$ 的具體樣子：

$$\left(a+b\right)^5 = a^5 + \underbrace{5a^4b + 10a^3b^2 + 10a^2b^3 + 5ab^4}_{\text{在 } \mathbf{Z}_5 \text{ 裡全是 } 0} + b^5$$

$5, 10, 10, 5$ 在 $\mathbf{Z}_5$ 裡都是 $0$。剩下 $a^5 + b^5$。

### Frobenius 自同態

【證明 (a)】說映射

$$\phi : F \to F, \qquad \phi(x) = x^p$$

保加法。它顯然也保乘法（$\left(ab\right)^p = a^pb^p$，靠交換性），
所以依 [環同態與核](../Ring/Ring_Homomorphism_and_Kernel.md)【定義 1】它是**環同態**。

在有限體上它甚至是**自同構**（[環同態與核](../Ring/Ring_Homomorphism_and_Kernel.md)【定義 3(b)】）——
核是 $\left\{x \ \middle|\ x^p = 0\right\} = \left\{0\right\}$（體無零因子），故單射；
有限集上單射即滿射（[排列](../Group/Permutation.md)【證明 (a)】）。

這個 **Frobenius 自同構**是有限體理論的引擎：

$$GF(p^n) = \left\{x \in \overline{GF(p)} \ \middle|\ x^{p^n} = x\right\} = \left\{x \ \middle|\ \phi^n(x) = x\right\}$$

**$GF(p^n)$ 的元素恰好是 Frobenius 映射迭代 $n$ 次後的不動點。**
這個刻畫是建構有限體的標準方法之一。

### 密碼學上的三個應用

**1. Schoof 演算法（橢圓曲線點計數）**

ECC 的參數產生需要知道曲線上的點數 $\#E\!\left(GF(p)\right)$。
Schoof 演算法的核心是 Frobenius 映射滿足的特徵方程：

$$\phi^2 - t\phi + p = 0$$

算出 $t$ 就得到點數 $\#E = p + 1 - t$。**沒有 Frobenius 就沒有實用的 ECC 參數產生。**

**2. $GF(2^n)$ 上的平方運算是線性的**

特徵 $2$ 時 $\left(a+b\right)^2 = a^2 + b^2$，所以「平方」是一個**線性變換**。
硬體上這意味著：

```
平方 = 位元交錯（把每個位元之間插入 0）+ 模約化
```

**不需要乘法器**，只要接線加 XOR。這讓 $GF(2^n)$ 上的冪運算比一般乘法快得多，
是 AES-GCM 的 GHASH 與二元體 ECC 能做到高吞吐量的原因。

**3. 配對密碼學的加速**

配對運算（Miller 演算法）裡大量出現 $x^{p^k}$ 這種冪次。
由本檔，它們可以用 Frobenius 映射一步完成，
而不必跑完整的模冪演算法。這是 BLS 簽章等配對式方案能實用化的關鍵優化之一。

### 一個反直覺的提醒

新生之夢**只對 $p$ 次方成立，不對其他指數成立**。
在 $\mathbf{Z}_5$ 裡：

$$\left(1+2\right)^2 = 9 \equiv 4, \qquad 1^2 + 2^2 = 5 \equiv 0, \qquad 4 \neq 0$$

$\left(a+b\right)^2 \neq a^2 + b^2$ —— 因為 $\dbinom{2}{1} = 2$ 不被 $5$ 整除。
**指數必須恰好是特徵（或其冪次）。** 這是實作時最容易搞錯的地方。
