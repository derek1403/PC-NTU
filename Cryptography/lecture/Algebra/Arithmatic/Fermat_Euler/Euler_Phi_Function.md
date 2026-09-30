# Euler Phi Function (尤拉函數)

+++

## 證明目標:

`Arithmetic.pdf` p.47、p.49–50。尤拉函數 $\varphi(n)$ 數的是「$1$ 到 $n$ 之間與 $n$ 互質的整數有幾個」。
它在 Abstract_Algebra 章已被定義，並證明了 $\left|\mathbf{Z}_n^*\right| = \varphi(n)$；該章把**具體算法**留給本章。

* (a) 投影片的 Remark（引用 Abstract_Algebra 章）：

$$\left|\mathbf{Z}_n^*\right| = \varphi(n)$$

* (b)(c) 投影片的命題（兩個方向）：

$$p > 0 \ \text{為質數} \quad \Longleftrightarrow \quad \varphi(p) = p - 1$$

* (d) 質數冪：

$$\varphi\left(p^k\right) = p^{k-1}\left(p - 1\right) \qquad \left(p \ \text{為質數},\ k \in \mathbf{P}\right)$$

* (e) 驗證：$\varphi(1) = 1$、$\varphi(7) = 6$、$\varphi(8) = 4$、$\varphi(9) = 6$。

* $\varphi$ : 尤拉函數 (Euler's totient function) $[\mathbf{P} \to \mathbf{P}]$
* $n$ : 正整數 (A positive integer) $[n \in \mathbf{P}]$
* $p$ : 正整數或質數，依上下文 (A positive integer or a prime) $[p \in \mathbf{P}]$
* $k$ : 指數 (An exponent) $[k \in \mathbf{P}]$
* 註：投影片記作 $\phi$，本章依 Abstract_Algebra 章慣例統一用 $\varphi$。
* 註：第三條性質 $\varphi(mn) = \varphi(m)\varphi(n)$（$m \perp n$）另立一檔：[尤拉函數的乘法性](Euler_Phi_Multiplicativity.md)。
* 註：投影片 p.47 是尤拉的生平（1707–1783，瑞士數學家與物理學家），放在 [尤拉定理](Euler_Theorem.md) 的意義段。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [尤拉函數的定義 (Definition of Euler's totient function)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Group/Group_Order.html#assumptions-preliminaries)：** 已於 Abstract_Algebra 章 [群的階](../../Abstract_Algebra/Group/Group_Order.md)【定義 3】給出，此處直接引用

  $$\varphi(n) = \left|\left\{x \in \mathbf{Z} \ \middle|\ 1 \le x \le n,\ \gcd(x, n) = 1\right\}\right|$$

  * $\varphi$ : 尤拉函數 (Euler's totient function) $[\mathbf{P} \to \mathbf{P}]$
  * $n$ : 正整數 (A positive integer) $[n \in \mathbf{P}]$
  * $x$ : 被計數的整數 (The integers being counted) $[x \in \mathbf{Z}]$

* **【已知 2】 [群的階與尤拉函數 (Group orders and the totient)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Group/Group_Order.html#c-proof-of-the-order-of-the-units-modulo-a-general-number)：** 已於 Abstract_Algebra 章 [群的階](../../Abstract_Algebra/Group/Group_Order.md)【證明 (b)(c)】完整證明，此處直接引用不再重證

  * (a) 一般模數：

    $$\left|\mathbf{Z}_n^*\right| = \varphi(n)$$

  * (b) 質數模數：

    $$\left|\mathbf{Z}_p^*\right| = p - 1 \qquad \left(p \ \text{為質數}\right)$$

  * $\mathbf{Z}_n^*$ : 模 $n$ 可逆剩餘類集合 (The set of units modulo $n$) $[\text{集合}]$
  * $n$ : 模數 (The modulus) $[n \in \mathbf{P}]$
  * $p$ : 質數 (A prime) $[p \in \mathbf{P}]$

* **【已知 3】 [質數與合數 (Primes and composites)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/Factorization/Euclid_Lemma.html#a-proof-that-a-prime-is-coprime-to-every-integer-it-does-not-divide)：** 已於本章 [歐幾里得引理](../Factorization/Euclid_Lemma.md)【定義 1】【證明 (a)】給出並證明，此處直接引用不再重證

  * (a) 合數有真因數：

    $$p > 1 \ \text{不是質數} \quad \Longrightarrow \quad \exists\, d \ \text{ with } \ 1 < d < p,\ d \mid p$$

  * (b) 質數與不被它整除的數互質：

    $$p \ \text{為質數},\ \ p \nmid x \quad \Longrightarrow \quad \gcd(p, x) = 1$$

  * $p$ : 正整數或質數 (A positive integer or a prime) $[p \in \mathbf{P}]$
  * $d$ : 真因數 (A proper divisor) $[d \in \mathbf{P}]$
  * $x$ : 任意整數 (An arbitrary integer) $[x \in \mathbf{Z}]$

* **【已知 4】 [公因數給出 gcd 的下界 (A common divisor bounds the gcd from below)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/GCD/Greatest_Common_Divisor.html#assumptions-preliminaries)：** 已於本章 [最大公因數](../GCD/Greatest_Common_Divisor.md)【定義 2】給出（gcd 是公因數的最大者），此處直接引用

  $$d \mid x,\ \ d \mid n \quad \Longrightarrow \quad \gcd(x, n) \ge d$$

  * $d$ : 公因數 (A common divisor) $[d \in \mathbf{P}]$
  * $x,\ n$ : 整數 (Integers) $[x, n \in \mathbf{Z}]$

* **【已知 5】 [互質對乘法封閉 (Coprimality is closed under products)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/Factorization/Relatively_Prime.html#b-proof-that-coprimality-to-a-modulus-is-closed-under-products)：** 已於本章 [互質](../Factorization/Relatively_Prime.md)【證明 (b)】完整證明，此處直接引用不再重證（反覆套用）

  $$x \perp p \quad \Longrightarrow \quad x \perp p^{k}$$

  * $x$ : 任意整數 (An arbitrary integer) $[x \in \mathbf{Z}]$
  * $p$ : 質數 (A prime) $[p \in \mathbf{P}]$
  * $k$ : 指數 (An exponent) $[k \in \mathbf{P}]$

+++

## 證明:

### (a) proof that the totient counts the units

直接引用：

$$\begin{gather*}
\left|\mathbf{Z}_n^*\right| &\overset{\text{已知 2(a)}}{=}& \varphi(n)
\end{gather*}$$

與投影片 p.49 的 Remark 一致。

### (b) proof (⇒) that a prime has totient one less than itself

$$\begin{gather*}
\varphi(p) &\overset{\text{已知 2(a)}}{=}& \left|\mathbf{Z}_p^*\right| \\
&\overset{\text{已知 2(b)}}{=}& p - 1
\end{gather*}$$

* 註：投影片的理由「$p$ is prime $\Rightarrow a \perp p$ for each $1 \le a \le p-1$」正是 Abstract_Algebra 章 [群的階](../../Abstract_Algebra/Group/Group_Order.md)【證明 (b)】的內容。

### (c) proof (⇐) that a non-prime has a smaller totient

證逆否命題：$p$ 不是質數 $\Rightarrow \varphi(p) \neq p - 1$。

**情形一：$p = 1$。** $1 \le x \le 1$ 只有 $x = 1$，且 $\gcd(1, 1) = 1$：

$$\begin{gather*}
\varphi(1) &\overset{\text{已知 1}}{=}& \left|\left\{1\right\}\right| \\
\varphi(1) &=& 1 \\
1 &\neq& 1 - 1
\end{gather*}$$

**情形二：$p > 1$ 為合數。** 取真因數 $d$；$d$ 與 $p$ 本身都在 $\left[1, p\right]$ 裡、都與 $p$ 不互質，至少少算兩個：

$$\begin{gather*}
d &\overset{\text{已知 3(a)}}{\mid}& p \qquad \text{with } 1 < d < p \\
\gcd(d, p) &\overset{\text{已知 4}}{\ge}& d \\
d &>& 1 \\
\gcd(p, p) &\overset{\text{已知 4}}{\ge}& p \\
p &>& 1 \\
\varphi(p) &\overset{\text{已知 1}}{\le}& p - 2
\end{gather*}$$

兩種情形都 $\varphi(p) \neq p - 1$，與投影片一致。

### (d) proof of the formula for a prime power

$\left[1, p^k\right]$ 裡與 $p^k$ **不**互質的，恰好是 $p$ 的倍數：

**($p \mid x \Rightarrow$ 不互質)**：$p$ 是 $x$ 與 $p^k$ 的公因數。
**($p \nmid x \Rightarrow$ 互質)**：由【已知 3(b)】$x \perp p$，再由【已知 5】$x \perp p^k$。

$$\begin{gather*}
p \mid x &\overset{\text{已知 4}}{\Longrightarrow}& \gcd\left(x, p^k\right) \ge p \\
p &>& 1 \\
p \nmid x &\overset{\text{已知 3(b)}}{\Longrightarrow}& x \perp p \\
x \perp p &\overset{\text{已知 5}}{\Longrightarrow}& x \perp p^{k}
\end{gather*}$$

$\left[1, p^k\right]$ 裡 $p$ 的倍數是 $p, 2p, \dots, p^{k-1} \cdot p$，共 $p^{k-1}$ 個（投影片 p.50 的集合 $S$）。從 $p^k$ 個數裡扣掉它們：

$$\begin{gather*}
\varphi\left(p^k\right) &\overset{\text{已知 1}}{=}& p^k - \left|\left\{p, 2p, \dots, p^{k-1} p\right\}\right| \\
&=& p^k - p^{k-1} \\
&=& p^{k-1}\left(p - 1\right)
\end{gather*}$$

與投影片一致。

### (e) verify four small values

$$\begin{gather*}
\varphi(1) &\overset{\text{證明 (c)}}{=}& 1 \\
\varphi(7) &\overset{\text{證明 (b)}}{=}& 7 - 1 \\
\varphi(7) &=& 6 \\
\varphi(8) &\overset{\text{證明 (d)}}{=}& 2^{2}\left(2 - 1\right) \\
\varphi(8) &=& 4 \\
\varphi(9) &\overset{\text{證明 (d)}}{=}& 3^{1}\left(3 - 1\right) \\
\varphi(9) &=& 6
\end{gather*}$$

逐一列舉核對：$\mathbf{Z}_8^* = \left\{1, 3, 5, 7\right\}$、$\mathbf{Z}_9^* = \left\{1, 2, 4, 5, 7, 8\right\}$；
後者與 Abstract_Algebra 章 [群的階](../../Abstract_Algebra/Group/Group_Order.md)【證明 (c)】的 $\left|\mathbf{Z}_9^*\right| = 6$ 一致。

+++

## 意義與密碼學關聯 (Interpretation and Relevance to Cryptography)

### $\varphi(n)$ 是 RSA 的秘密

RSA 的公鑰是 $\left(n, e\right)$，私鑰 $d = e^{-1} \bmod \varphi(n)$。**知道 $\varphi(n)$ 就能算出私鑰**，所以 $\varphi(n)$ 必須保密。
對 $n = pq$：

$$\varphi(n) = \left(p - 1\right)\left(q - 1\right)$$

（由 [乘法性](Euler_Phi_Multiplicativity.md) 與本檔 (b)）。反過來，**知道 $\varphi(n)$ 也就能分解 $n$**：
$p + q = n - \varphi(n) + 1$，再解一元二次方程。所以「求 $\varphi(n)$」與「分解 $n$」一樣難 —— 這是 RSA 安全性的另一種表述。

### 一個（很慢的）質數判準

「$\varphi(p) = p - 1 \Leftrightarrow p$ 為質數」在理論上完美，但計算 $\varphi(p)$ 需要知道 $p$ 的分解，
所以它不能當實用的質數測試。實用的是 [費馬小定理](Fermat_Little_Theorem.md) 衍生的 Miller–Rabin。

### 程式思維

```python
from math import gcd
def phi(n):
    """已知 1 的直譯：O(n log n)，只適合小數字。"""
    return sum(1 for x in range(1, n + 1) if gcd(x, n) == 1)

assert [phi(n) for n in (1, 7, 8, 9)] == [1, 6, 4, 6]              # 證明 (e)
assert all((phi(p) == p - 1) == (p > 1 and all(p % d for d in range(2, p)))
           for p in range(1, 200))                                  # 證明 (b)(c)
assert all(phi(p**k) == p**(k-1) * (p - 1) for p in (2, 3, 5, 7) for k in range(1, 5))   # 證明 (d)
```
