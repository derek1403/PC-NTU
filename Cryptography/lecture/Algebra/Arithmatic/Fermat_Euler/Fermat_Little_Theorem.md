# Fermat Little Theorem (費馬小定理)

+++

## 證明目標:

`Arithmetic.pdf` p.44–45。**費馬小定理本身已在 Abstract_Algebra 章用拉格朗日定理證完**
（[元素的階與循環子群](../../Abstract_Algebra/Group/Order_of_Element_and_Cyclic_Subgroup.md)【證明 (d)】），本檔引用不重證。
本檔證明投影片的**系理**，並補上兩個密碼學上最常用的推論。

* (a) 投影片的前提「$a \perp p$」與 Abstract_Algebra 章的前提「$p \nmid a$」等價，所以兩章說的是同一條定理：

$$p \ \text{為質數},\ \ a \perp p \quad \Longrightarrow \quad a^{p-1} \equiv 1 \pmod{p}$$

* (b) 投影片的系理（**不需要互質**）：

$$p \ \text{為質數},\ \ a \in \mathbf{Z} \quad \Longrightarrow \quad a^{p} \equiv a \pmod{p}$$

* (c) 反過來不成立：$341 = 11 \times 31$ 是合數，卻滿足 $2^{341} \equiv 2 \pmod{341}$。
* (d) 用費馬小定理求反元素（投影片未列，本章補）：

$$p \nmid a \quad \Longrightarrow \quad a^{-1} \equiv a^{p-2} \pmod{p}$$

  並驗證 $3^{-1} \equiv 3^{5} \equiv 5 \pmod 7$。

* $p$ : 質數 (A prime) $[p \in \mathbf{P}]$
* $a$ : 任意整數 (An arbitrary integer) $[a \in \mathbf{Z}]$
* 註：投影片 p.45 的證明（$\left\{a, 2a, \dots, (p-1)a\right\}$ 模 $p$ 是 $\left\{1, \dots, p-1\right\}$ 的排列）是另一條證明路線，
  它推廣到合數模數就是 [化簡剩餘系](Reduced_Residue_System.md) 文末的論證。本章依「引用免證」原則採用 Abstract_Algebra 章已完成的群論證明。
* 註（**投影片的歷史敘述有誤**）：p.44 說「The Chinese knew $p \mid \left(2^p - 2\right)$ as early as 500 B.C.」。
  這是流傳甚廣的**訛傳**（所謂 “Chinese hypothesis”），源自 19 世紀末對中國古籍的誤讀，沒有可靠的史料支持。
  而且「$n \mid 2^n - 2 \Rightarrow n$ 為質數」這個傳說中的命題本身是**錯的** —— 正是 (c) 的 $341$。
  Fermat 於 1640 年在信中陳述此定理、Euler 於 1736 年發表第一個證明，這兩點投影片正確。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [費馬小定理 (Fermat's little theorem)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Group/Order_of_Element_and_Cyclic_Subgroup.html#d-proof-of-fermats-little-theorem)：** 已於 Abstract_Algebra 章 [元素的階與循環子群](../../Abstract_Algebra/Group/Order_of_Element_and_Cyclic_Subgroup.md)【證明 (d)】完整證明，此處直接引用不再重證

  $$p \ \text{為質數},\ \ p \nmid a \quad \Longrightarrow \quad a^{p-1} \equiv 1 \pmod{p}$$

  * $p$ : 質數 (A prime) $[p \in \mathbf{P}]$
  * $a$ : 不被 $p$ 整除的整數 (An integer not divisible by $p$) $[a \in \mathbf{Z}]$

* **【已知 2】 [質數與互質 (Primes and coprimality)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/Factorization/Euclid_Lemma.html#a-proof-that-a-prime-is-coprime-to-every-integer-it-does-not-divide)：** 已於本章 [歐幾里得引理](../Factorization/Euclid_Lemma.md)【證明 (a)】與 [最大公因數](../GCD/Greatest_Common_Divisor.md)【定義 2】給出並證明，此處直接引用不再重證

  * (a) 不整除則互質：

    $$p \nmid a \quad \Longrightarrow \quad \gcd(p, a) = 1$$

  * (b) 整除則 gcd 為 $p$（$p$ 本身是公因數，且沒有公因數超過 $p$）：

    $$p \mid a \quad \Longrightarrow \quad \gcd(p, a) = p \neq 1$$

  * $p$ : 質數 (A prime) $[p \in \mathbf{P}]$
  * $a$ : 任意整數 (An arbitrary integer) $[a \in \mathbf{Z}]$

* **【已知 3】 [同餘的運算性質 (Arithmetic of congruences)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/Congruence/Congruence_Properties.html#d-proof-that-congruence-is-preserved-by-powers)：** 已於本章 [同餘的性質](../Congruence/Congruence_Properties.md)【證明 (a)(c)(d)】完整證明，此處直接引用不再重證

  * (a) 遞移性：

    $$u \equiv v,\ \ v \equiv w \quad \Longrightarrow \quad u \equiv w \pmod{m}$$

  * (b) 兩邊同乘：

    $$u \equiv v \quad \Longrightarrow \quad uc \equiv vc \pmod{m}$$

  * (c) 兩邊同取冪：

    $$u \equiv v \quad \Longrightarrow \quad u^{d} \equiv v^{d} \pmod{m}$$

  * $u,\ v,\ w,\ c$ : 任意整數 (Arbitrary integers) $[\mathbf{Z}]$
  * $m$ : 模數 (The modulus) $[m \in \mathbf{P}]$
  * $d$ : 正整數指數 (A positive exponent) $[d \in \mathbf{P}]$

* **【已知 4】 [同餘的整除刻畫 (Congruence as divisibility)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/Congruence/Congruence_Relation.html#b-proof-that-a-difference-divisible-by-the-modulus-gives-equal-remainders)：** 已於本章 [同餘關係](../Congruence/Congruence_Relation.md)【證明 (a)(b)】完整證明，此處直接引用不再重證

  $$u \equiv v \pmod{m} \quad \Longleftrightarrow \quad m \mid \left(u - v\right)$$

  * $u,\ v$ : 任意整數 (Arbitrary integers) $[u, v \in \mathbf{Z}]$
  * $m$ : 模數 (The modulus) $[m \in \mathbf{P}]$

+++

## 證明:

### (a) proof that the two formulations of the hypothesis agree

$a \perp p$ 即 $\gcd(p, a) = 1$。由【已知 2】的 (a)(b)，它恰好等價於 $p \nmid a$，於是投影片的版本就是【已知 1】：

$$\begin{gather*}
p \nmid a &\overset{\text{已知 2(a)}}{\Longrightarrow}& \gcd(p, a) = 1 \\
p \mid a &\overset{\text{已知 2(b)}}{\Longrightarrow}& \gcd(p, a) \neq 1 \\
a \perp p &\Longleftrightarrow& p \nmid a \\
a^{p-1} &\overset{\text{已知 1}}{\equiv}& 1 \pmod{p}
\end{gather*}$$

### (b) proof of the corollary for every integer

**情形一：$p \nmid a$。** 在費馬小定理兩邊乘 $a$：

$$\begin{gather*}
a^{p-1} &\overset{\text{已知 1}}{\equiv}& 1 \pmod{p} \\
a^{p-1} \cdot a &\overset{\text{已知 3(b)}}{\equiv}& 1 \cdot a \pmod{p} \\
a^{p} &\equiv& a \pmod{p}
\end{gather*}$$

**情形二：$p \mid a$。** 則 $a \equiv 0$，取 $p$ 次方仍是 $0$：

$$\begin{gather*}
a &\overset{\text{已知 4}}{\equiv}& 0 \pmod{p} \\
a^{p} &\overset{\text{已知 3(c)}}{\equiv}& 0^{p} \pmod{p} \\
a^{p} &\overset{\text{已知 3(a)}}{\equiv}& a \pmod{p} \qquad \text{(兩者都} \equiv 0 \text{)}
\end{gather*}$$

兩種情形都成立，與投影片 p.45 的 i) ii) 一致。

### (c) verify that three hundred forty-one is a base-two pseudoprime

$341 = 11 \times 31$ 是合數。關鍵觀察：$2^{10} = 1024 = 3 \times 341 + 1$，所以 $2^{10}$ 模 $341$ 就是 $1$：

$$\begin{gather*}
2^{10} - 1 &=& 3 \times 341 \\
2^{10} &\overset{\text{已知 4}}{\equiv}& 1 \pmod{341} \\
\left(2^{10}\right)^{34} &\overset{\text{已知 3(c)}}{\equiv}& 1^{34} \pmod{341} \\
2^{340} &\equiv& 1 \pmod{341} \\
2^{341} &\overset{\text{已知 3(b)}}{\equiv}& 2 \pmod{341}
\end{gather*}$$

合數 $341$ 也滿足 $341 \mid 2^{341} - 2$。**費馬小定理的逆命題不成立**，只看一個底數 $2$ 無法判定質數。
下一檔 [Carmichael 數](Carmichael_Numbers.md) 說明：即使檢查**所有**底數也不行。

### (d) proof that the inverse is a power

$a \cdot a^{p-2} = a^{p-1} \equiv 1$，所以 $a^{p-2}$ 就是一個反元素：

$$\begin{gather*}
a \cdot a^{p-2} &=& a^{p-1} \\
a \cdot a^{p-2} &\overset{\text{已知 1}}{\equiv}& 1 \pmod{p}
\end{gather*}$$

**驗證 $3^{-1} \bmod 7$**：

$$\begin{gather*}
3^{7-2} &=& 3^5 \\
3^5 &=& 243 \\
243 &=& 34 \times 7 + 5 \\
3^{5} &\overset{\text{已知 4}}{\equiv}& 5 \pmod{7} \\
3 \times 5 &=& 2 \times 7 + 1
\end{gather*}$$

與 [模反元素](../Congruence/Modular_Inverse.md)【證明 (f)】用擴展歐幾里得算出的 $3^{-1} \bmod 7 = 5$ 一致。

+++

## 意義與密碼學關聯 (Interpretation and Relevance to Cryptography)

### 費馬測試：最便宜的質數篩

(b) 反過來用：若 $a^n \not\equiv a \pmod n$，則 $n$ **一定是合數**。
一次模冪運算就能淘汰絕大多數合數，RSA 產生大質數時第一關就是它。
但 (c) 說明**通過測試不代表是質數**（$341$ 叫做「以 $2$ 為底的偽質數」）。實務上改用 Miller–Rabin，
它對每個合數都有至少 $3/4$ 的底數能抓出來，而 [Carmichael 數](Carmichael_Numbers.md) 讓費馬測試完全失效。

### 常數時間的模反元素

(d) 的 $a^{-1} = a^{p-2} \bmod p$ 在密碼學實作裡非常重要。
[擴展歐幾里得演算法](../GCD/Extended_Euclidean_Algorithm.md) 的步數依賴輸入，會洩漏時間資訊；
而模冪運算可以寫成**固定步數**（Montgomery ladder），不論 $a$ 是多少都跑一樣久。
橢圓曲線密碼（如 Curve25519 的實作）在質數體 $\mathbf{F}_p$ 上求反元素，標準做法就是算 $a^{p-2}$。

### 與 Abstract_Algebra 章的關係

|  | Abstract_Algebra 章 | 本章 |
|---|---|---|
| 證明路線 | 拉格朗日定理：$o(a)$ 整除 $\left\|\mathbf{Z}_p^*\right\| = p-1$ | 投影片：$\left\{a, 2a, \dots, (p-1)a\right\}$ 是 $\left\{1, \dots, p-1\right\}$ 的排列 |
| 本質 | 子群的階整除群的階 | 乘以 $a$ 是 $\mathbf{Z}_p^*$ 上的雙射 |

兩條路線殊途同歸：「乘以 $a$ 是雙射」正是「$\mathbf{Z}_p^*$ 是群」的一部分。

### 程式思維

```python
for p in [2, 3, 5, 7, 11, 13, 101]:
    assert all(pow(a, p, p) == a % p for a in range(-50, 50))     # 證明 (b)
assert 341 == 11 * 31 and pow(2, 341, 341) == 2                   # 證明 (c)
assert pow(3, 7 - 2, 7) == 5 == pow(3, -1, 7)                     # 證明 (d)
```
