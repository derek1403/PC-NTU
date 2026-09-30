# Fundamental Theorem of Arithmetic (算術基本定理)

+++

## 證明目標:

`Arithmetic.pdf` p.24。每個大於 $1$ 的整數都能拆成質數的乘積，**而且拆法唯一**。
投影片的證明只有兩行：「Existence: Easy」「Uniqueness: Apply the last Corollary」。本檔把兩行展開成完整的歸納法。

* (a)(b) **存在性**（強歸納法：基底 + 歸納步驟）：每個整數 $a > 1$ 都是質數的乘積

$$a = p_1 p_2 \cdots p_r, \qquad p_i \ \text{為質數}$$

* (c)(d) **唯一性**（對質因數個數歸納：基底 + 歸納步驟）：若兩個質數乘積相等，則個數相同且排序後逐項相同

$$p_1 p_2 \cdots p_r = q_1 q_2 \cdots q_s,\ \ p_1 \le \cdots \le p_r,\ \ q_1 \le \cdots \le q_s \quad \Longrightarrow \quad r = s,\ \ p_i = q_i$$

* (e) 投影片的反例：在 $\mathbf{Z}\left[\sqrt{-5}\right]$ 裡唯一分解**失敗**：

$$6 = 2 \times 3 = \left(1 - \sqrt{-5}\right)\left(1 + \sqrt{-5}\right)$$

  且 $2,\ 3,\ 1 - \sqrt{-5},\ 1 + \sqrt{-5}$ 四者在 $\mathbf{Z}\left[\sqrt{-5}\right]$ 中都不可約。

* $a$ : 大於 $1$ 的整數 (An integer greater than one) $[a \in \mathbf{P},\ a \ge 2]$
* $p_i,\ q_j$ : 質數 (Primes) $[p_i, q_j \in \mathbf{P}]$
* $r,\ s$ : 質因數的個數（含重複） (The number of prime factors, with multiplicity) $[r, s \in \mathbf{P}]$
* 註：投影片寫「is itself prime **or** can be written uniquely as a product of primes」。
  本檔把「質數本身」視為 $r = 1$ 的乘積，兩種情形合併處理。
* 註：唯一性是「**排序後**相同」—— $12 = 2 \times 2 \times 3 = 3 \times 2 \times 2$ 只是順序不同，算同一種分解。
* 註：投影片的 Remark「$\mathbf{Z}$ is a UFD (Unique Factorization Domain)」就是 (a)–(d) 的結論配上
  $\mathbf{Z}$ 是整環（Abstract_Algebra 章 [整環](../../Abstract_Algebra/Ring/Integral_Domain.md)）。
  (e) 說明這**不是**每個整環都有的性質。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [歐幾里得引理（k 個因子） (Euclid's lemma for k factors)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/Factorization/Euclid_Lemma.html#d-proof-of-the-inductive-step-for-k-factors)：** 已於本章 [歐幾里得引理](Euclid_Lemma.md)【證明 (c)(d)】完整證明，此處直接引用不再重證

  $$p \mid a_1 a_2 \cdots a_k \quad \Longrightarrow \quad p \mid a_i \ \text{ for some } i$$

  * $p$ : 質數 (A prime) $[p \in \mathbf{P}]$
  * $a_i$ : 因子 (Factors) $[a_i \in \mathbf{Z}]$
  * $k$ : 因子個數 (The number of factors) $[k \in \mathbf{P}]$

* **【已知 2】 [質數與合數 (Primes and composites)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/Factorization/Euclid_Lemma.html#assumptions-preliminaries)：** 已於本章 [歐幾里得引理](Euclid_Lemma.md)【定義 1】給出，此處直接引用

  * (a) 質數的正因數只有 $1$ 與自己：

    $$p \ \text{為質數},\ d \in \mathbf{P},\ d \mid p \quad \Longrightarrow \quad d \in \left\{1, p\right\}$$

  * (b) 合數有真因數：

    $$a > 1 \ \text{不是質數} \quad \Longrightarrow \quad a = bc \ \text{ with } \ 1 < b,\ c < a$$

  * $p$ : 質數 (A prime) $[p \in \mathbf{P}]$
  * $a,\ b,\ c,\ d$ : 正整數 (Positive integers) $[a, b, c, d \in \mathbf{P}]$

* **【定義 1】 整數環 $\mathbf{Z}\left[\sqrt{-5}\right]$ 與範數 (The ring and its norm)：** 【證明 (e)】要用。記 $s = \sqrt{-5}$，$s^2 = -5$

  * (a) 環與範數：

    $$\mathbf{Z}\left[\sqrt{-5}\right] \overset{\text{def}}{=} \left\{a + b s \ \middle|\ a, b \in \mathbf{Z}\right\}, \qquad N\left(a + bs\right) \overset{\text{def}}{=} a^2 + 5b^2$$

  * (b) 單位與不可約元素：

    $$u \ \text{為單位} \ \overset{\text{def}}{\Longleftrightarrow} \ \exists\, v,\ uv = 1; \qquad \alpha \ \text{不可約} \ \overset{\text{def}}{\Longleftrightarrow} \ \alpha \neq 0,\ \alpha \ \text{非單位},\ \alpha = \beta\gamma \Rightarrow \beta \ \text{或} \ \gamma \ \text{為單位}$$

  * $s$ : $\sqrt{-5}$ (The square root of minus five) $[s \in \mathbf{C}]$
  * $a,\ b$ : 整係數 (Integer coefficients) $[a, b \in \mathbf{Z}]$
  * $N$ : 範數 (The norm) $[\mathbf{Z}\left[\sqrt{-5}\right] \to \mathbf{N}]$
  * $u,\ v,\ \alpha,\ \beta,\ \gamma$ : 環元素 (Ring elements) $[\in \mathbf{Z}\left[\sqrt{-5}\right]]$
  * 註：$N(a + bs) = \left|a + b\sqrt{5}\,i\right|^2$，即複數絕對值的平方。

* **【假設 1】 存在性的強歸納假設 (Strong induction hypothesis for existence)：** 【證明 (b)】要用

  $$\text{每個滿足 } 2 \le b < a \text{ 的整數 } b \text{ 都是質數的乘積}$$

  * $a$ : 目前處理的整數 (The integer being handled) $[a \in \mathbf{P},\ a \ge 3]$
  * $b$ : 比 $a$ 小的整數 (A smaller integer) $[b \in \mathbf{P}]$

* **【假設 2】 唯一性的歸納假設 (Induction hypothesis for uniqueness)：** 【證明 (d)】要用。設 $r - 1$ 個質數的乘積分解唯一

  $$p_1 \cdots p_{r-1} = q_1 \cdots q_{t} \ \ \text{（皆為質數，已排序）} \quad \Longrightarrow \quad r - 1 = t,\ \ p_i = q_i$$

  * $p_i,\ q_j$ : 質數 (Primes) $[p_i, q_j \in \mathbf{P}]$
  * $r,\ t$ : 質因數個數 (Numbers of prime factors) $[r, t \in \mathbf{P}]$

* **【推導 1】 範數是乘法的 (The norm is multiplicative)：** 【證明 (e)】要用。直接展開，兩個交叉項 $\pm 10abcd$ 互相抵消

  $$\begin{gather*}
  \left(a + bs\right)\left(c + ds\right) &\overset{\text{定義 1(a)}}{=}& \left(ac - 5bd\right) + \left(ad + bc\right)s \\
  N\left(\left(a + bs\right)\left(c + ds\right)\right) &\overset{\text{定義 1(a)}}{=}& \left(ac - 5bd\right)^2 + 5\left(ad + bc\right)^2 \\
  N\left(\left(a + bs\right)\left(c + ds\right)\right) &=& a^2c^2 + 25b^2d^2 + 5a^2d^2 + 5b^2c^2 \\
  N\left(\left(a + bs\right)\left(c + ds\right)\right) &=& \left(a^2 + 5b^2\right)\left(c^2 + 5d^2\right) \\
  N\left(\left(a + bs\right)\left(c + ds\right)\right) &\overset{\text{定義 1(a)}}{=}& N\left(a + bs\right) N\left(c + ds\right)
  \end{gather*}$$

  * $a,\ b,\ c,\ d$ : 整係數 (Integer coefficients) $[a, b, c, d \in \mathbf{Z}]$
  * $s$ : $\sqrt{-5}$ $[s^2 = -5]$
  * 註：由此**單位的範數是 $1$**：$uv = 1 \Rightarrow N(u)N(v) = N(1) = 1$，兩個非負整數相乘為 $1$ 只能都是 $1$。
    反之 $N(a + bs) = a^2 + 5b^2 = 1$ 只有 $a = \pm 1,\ b = 0$。故單位恰為 $\pm 1$。

+++

## 證明:

### (a) proof of the base case of existence

$a = 2$ 的正因數只有 $1, 2$，它本身是質數，是 $r = 1$ 的乘積：

$$\begin{gather*}
2 &\overset{\text{已知 2(a)}}{=}& p_1 \qquad \text{(} p_1 = 2 \text{ 為質數)}
\end{gather*}$$

### (b) proof of the inductive step of existence

設 $a \ge 3$。若 $a$ 是質數，同 (a) 完成。否則由【已知 2(b)】拆成兩個較小的數，兩者都有分解，接起來即可：

$$\begin{gather*}
a &\overset{\text{已知 2(b)}}{=}& b c \qquad \text{with } 1 < b,\ c < a \\
b &\overset{\text{假設 1}}{=}& p_1 \cdots p_k \\
c &\overset{\text{假設 1}}{=}& p_{k+1} \cdots p_r \\
a &=& p_1 \cdots p_k\, p_{k+1} \cdots p_r
\end{gather*}$$

由 (a)(b) 與強歸納法，每個 $a \ge 2$ 都是質數的乘積。這就是投影片的「Existence: Easy」。

### (c) proof of the base case of uniqueness

設 $r = 1$，即 $p_1 = q_1 \cdots q_s$。若 $s \ge 2$，則 $q_1$ 是 $p_1$ 的正因數，且 $1 < q_1 < p_1$（因為剩下的 $q_2 \cdots q_s \ge 2$），與 $p_1$ 為質數矛盾：

$$\begin{gather*}
q_1 &\mid& p_1 \\
q_1 &\overset{\text{已知 2(a)}}{\in}& \left\{1, p_1\right\} \\
q_1 &\neq& 1 \qquad \text{(質數大於 } 1 \text{)} \\
q_1 &\neq& p_1 \qquad \text{(否則 } q_2 \cdots q_s = 1 \text{，但每個 } q_j \ge 2 \text{)}
\end{gather*}$$

故 $s = 1$、$q_1 = p_1$。

### (d) proof of the inductive step of uniqueness

設 $r \ge 2$ 且 $p_1 \cdots p_r = q_1 \cdots q_s$。（$s = 1$ 的情形與 (c) 對稱，同樣矛盾，故 $s \ge 2$。）
$p_r$ 整除右邊，由歐幾里得引理整除某個 $q_j$；$q_j$ 是質數而 $p_r > 1$，只能相等：

$$\begin{gather*}
p_r &\mid& q_1 q_2 \cdots q_s \\
p_r &\overset{\text{已知 1}}{\mid}& q_j \qquad \text{for some } j \\
p_r &\overset{\text{已知 2(a)}}{=}& q_j \qquad \text{(} p_r \neq 1 \text{)} \\
p_1 \cdots p_{r-1} &=& \prod_{i \neq j} q_i \qquad \text{(兩邊約去 } p_r = q_j \neq 0 \text{)}
\end{gather*}$$

左邊是 $r - 1$ 個質數、右邊是 $s - 1$ 個質數。由歸納假設：

$$\begin{gather*}
r - 1 &\overset{\text{假設 2}}{=}& s - 1 \\
\left\{p_1, \dots, p_{r-1}\right\} &\overset{\text{假設 2}}{=}& \left\{q_i\right\}_{i \neq j} \qquad \text{(作為多重集合)}
\end{gather*}$$

兩邊再各補回相等的 $p_r = q_j$，得 $r = s$ 且兩個多重集合相等，排序後逐項相同。
由 (c)(d) 與歸納法，唯一性成立。這就是投影片的「Uniqueness: Apply the last Corollary」。

### (e) disprove unique factorization in the ring with the square root of minus five

**兩種分解**：直接展開右邊：

$$\begin{gather*}
\left(1 - s\right)\left(1 + s\right) &=& 1 - s^2 \\
&\overset{\text{定義 1(a)}}{=}& 1 - \left(-5\right) \\
&=& 6 \\
&=& 2 \times 3
\end{gather*}$$

**四個因子都不可約**：先算範數。若 $\alpha = \beta\gamma$ 且 $\beta, \gamma$ 都不是單位，則由【推導 1】兩者的範數都 $> 1$ 且相乘為 $N(\alpha)$：

$$\begin{gather*}
N(2) &\overset{\text{定義 1(a)}}{=}& 4 \\
N(3) &\overset{\text{定義 1(a)}}{=}& 9 \\
N\left(1 \pm s\right) &\overset{\text{定義 1(a)}}{=}& 1^2 + 5 \times \left(\pm 1\right)^2 \\
N\left(1 \pm s\right) &=& 6 \\
N(\beta)\, N(\gamma) &\overset{\text{推導 1}}{=}& N(\alpha)
\end{gather*}$$

於是 $2$ 要拆需要範數 $2$ 的元素，$3$ 要拆需要範數 $3$ 的元素，$1 \pm s$ 要拆需要範數 $2$ 與 $3$ 的元素。
**但範數 $2$、$3$ 的元素根本不存在**：

$$\begin{gather*}
a^2 + 5b^2 &\ge& 5 \qquad \text{(若 } b \neq 0 \text{)} \\
a^2 &\notin& \left\{2, 3\right\} \qquad \text{(若 } b = 0 \text{，完全平方數只有 } 0, 1, 4, 9, \dots \text{)} \\
N(\beta) &\notin& \left\{2, 3\right\}
\end{gather*}$$

故四者都不可約（【定義 1(b)】）。

**兩種分解真的不同**：$2$ 不是 $1 \pm s$ 的單位倍（單位只有 $\pm 1$，而 $N(2) = 4 \neq 6 = N\left(\pm\left(1 \pm s\right)\right)$）。
所以 $6$ 在 $\mathbf{Z}\left[\sqrt{-5}\right]$ 有兩種本質不同的不可約分解，唯一分解失敗，與投影片一致。

+++

## 意義與密碼學關聯 (Interpretation and Relevance to Cryptography)

### 存在容易、唯一才是重點

存在性的證明是**非建設性**的 —— 它說分解存在，卻沒說怎麼快速找到。
實際上找到 $n = pq$ 的分解（$p, q$ 各 $1024$ 位元）是目前公認的困難問題，**RSA 的安全性就押在這上面**。

唯一性則是讓 RSA **能夠被定義**的前提：私鑰由 $p, q$ 決定，若 $n$ 有兩種分解，
「$n$ 的質因數」這句話就沒有意義，$\varphi(n) = (p-1)(q-1)$ 也就不是良定義。

### 為什麼 $\mathbf{Z}\left[\sqrt{-5}\right]$ 的反例重要

它說明唯一分解是 $\mathbf{Z}$ 的**特殊恩典**，不是理所當然。在整數環裡能成立，
是因為有 [歐幾里得引理](Euclid_Lemma.md)，而那又來自 [貝祖等式](../GCD/Bezout_Identity.md) ——
**$\mathbf{Z}$ 有除法原理 $\Rightarrow$ PID $\Rightarrow$ UFD**。$\mathbf{Z}\left[\sqrt{-5}\right]$ 沒有好的除法原理，鏈條從第一環就斷了。

歷史上，Lamé 在 1847 年宣稱證明了費馬最後定理，錯誤正是**默認了類似的環有唯一分解**。
Kummer 指出這個漏洞，並發明「理想數」來修補 —— 這就是 Abstract_Algebra 章 [理想](../../Abstract_Algebra/Ring/Ideal.md) 的起源。

**數域篩法 (Number Field Sieve)** —— 目前分解 RSA 模數最快的演算法 —— 正是在 $\mathbf{Z}\left[\alpha\right]$ 這類環裡工作，
必須處理唯一分解失敗的問題，靠的就是理想的唯一分解（Dedekind 整環）。

### 程式思維

```python
def factorize(n):
    """試除法：存在性的建設性版本，只適合小數字。"""
    fs, d = [], 2
    while d * d <= n:
        while n % d == 0:
            fs.append(d); n //= d
        d += 1
    if n > 1: fs.append(n)
    return fs                     # 已排序 —— 唯一性保證答案只有這一個

assert factorize(360) == [2, 2, 2, 3, 3, 5]
# Z[√-5] 裡沒有範數 2 或 3 的元素（證明 (e)）
assert not [(a, b) for a in range(-3, 4) for b in range(-2, 3) if a*a + 5*b*b in (2, 3)]
```
