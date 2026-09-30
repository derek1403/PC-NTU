# Carmichael Numbers (Carmichael 數)

+++

## 證明目標:

`Arithmetic.pdf` p.46。投影片問：費馬小定理的逆命題成立嗎？
「若 $a^n \equiv a \pmod n$ 對**每一個** $a \in \mathbf{Z}$ 都成立，$n$ 一定是質數嗎？」答案是**否**。

* (a) $561 = 3 \times 11 \times 17$ 是合數。
* (b) 對每個質因數 $p \in \left\{3, 11, 17\right\}$ 與每個整數 $a$：

$$a^{561} \equiv a \pmod{p}$$

* (c) 合併三個質因數（投影片說「By Chinese Remainder Theorem」）：

$$a^{561} \equiv a \pmod{561} \qquad \text{for every } a \in \mathbf{Z}$$

* (d) **陳述不證**：$561$ 是**最小的** Carmichael 數（投影片的敘述）。本檔以程式窮舉驗證，不給手寫證明。

* $n$ : 待測的正整數 (The positive integer under test) $[n \in \mathbf{P}]$
* $a$ : 任意整數 (An arbitrary integer) $[a \in \mathbf{Z}]$
* $p$ : $561$ 的質因數 (A prime factor of $561$) $[p \in \left\{3, 11, 17\right\}]$
* 註：(b) 能成立的關鍵是 $561 - 1 = 560$ **同時被** $3 - 1 = 2$、$11 - 1 = 10$、$17 - 1 = 16$ 整除。
  這正是 Korselt 判準（見文末，陳述不證）的特例。
* 註：投影片寫「By Chinese Remainder Theorem」。嚴格來說這裡用到的只是 CRT 的唯一性那一半 ——
  「兩兩互質的因數都整除，則乘積整除」（[互質](../Factorization/Relatively_Prime.md)【證明 (c)】）。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [費馬小定理 (Fermat's little theorem)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Group/Order_of_Element_and_Cyclic_Subgroup.html#d-proof-of-fermats-little-theorem)：** 已於 Abstract_Algebra 章 [元素的階與循環子群](../../Abstract_Algebra/Group/Order_of_Element_and_Cyclic_Subgroup.md)【證明 (d)】完整證明（本章 [費馬小定理](Fermat_Little_Theorem.md) 引用），此處直接引用不再重證

  $$p \ \text{為質數},\ \ p \nmid a \quad \Longrightarrow \quad a^{p-1} \equiv 1 \pmod{p}$$

  * $p$ : 質數 (A prime) $[p \in \mathbf{P}]$
  * $a$ : 不被 $p$ 整除的整數 (An integer not divisible by $p$) $[a \in \mathbf{Z}]$

* **【已知 2】 [同餘的運算性質 (Arithmetic of congruences)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/Congruence/Congruence_Properties.html#d-proof-that-congruence-is-preserved-by-powers)：** 已於本章 [同餘的性質](../Congruence/Congruence_Properties.md)【證明 (a)(c)(d)】完整證明，此處直接引用不再重證

  * (a) 遞移性：

    $$u \equiv v,\ \ v \equiv w \quad \Longrightarrow \quad u \equiv w \pmod{m}$$

  * (b) 兩邊同乘：

    $$u \equiv v \quad \Longrightarrow \quad uc \equiv vc \pmod{m}$$

  * (c) 兩邊同取冪：

    $$u \equiv v \quad \Longrightarrow \quad u^{d} \equiv v^{d} \pmod{m}$$

  * $u,\ v,\ w,\ c$ : 任意整數 (Arbitrary integers) $[\mathbf{Z}]$
  * $m$ : 模數 (The modulus) $[m \in \mathbf{P}]$
  * $d$ : 正整數指數 (A positive exponent) $[d \in \mathbf{P}]$

* **【已知 3】 [同餘的整除刻畫 (Congruence as divisibility)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/Congruence/Congruence_Relation.html#b-proof-that-a-difference-divisible-by-the-modulus-gives-equal-remainders)：** 已於本章 [同餘關係](../Congruence/Congruence_Relation.md)【證明 (a)(b)】完整證明，此處直接引用不再重證

  $$u \equiv v \pmod{m} \quad \Longleftrightarrow \quad m \mid \left(u - v\right)$$

  * $u,\ v$ : 任意整數 (Arbitrary integers) $[u, v \in \mathbf{Z}]$
  * $m$ : 模數 (The modulus) $[m \in \mathbf{P}]$

* **【已知 4】 [互質因數相乘仍整除 (Coprime divisors multiply)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/Factorization/Relatively_Prime.html#c-proof-that-coprime-divisors-multiply)：** 已於本章 [互質](../Factorization/Relatively_Prime.md)【證明 (c)】完整證明，此處直接引用不再重證

  $$m_1 \mid y,\ \ m_2 \mid y,\ \ m_1 \perp m_2 \quad \Longrightarrow \quad m_1 m_2 \mid y$$

  * $m_1,\ m_2$ : 互質的正整數 (Coprime positive integers) $[m_1, m_2 \in \mathbf{P}]$
  * $y$ : 被整除的整數 (The integer being divided) $[y \in \mathbf{Z}]$

* **【已知 5】 [質數與不被它整除的數互質 (A prime is coprime to what it does not divide)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/Factorization/Euclid_Lemma.html#a-proof-that-a-prime-is-coprime-to-every-integer-it-does-not-divide)：** 已於本章 [歐幾里得引理](../Factorization/Euclid_Lemma.md)【證明 (a)】完整證明，此處直接引用不再重證

  $$p \ \text{為質數},\ \ p \nmid a \quad \Longrightarrow \quad \gcd(p, a) = 1$$

  * $p$ : 質數 (A prime) $[p \in \mathbf{P}]$
  * $a$ : 任意整數 (An arbitrary integer) $[a \in \mathbf{Z}]$

* **【定義 1】 Carmichael 數 (Carmichael number)：** 能騙過「所有底數」的費馬測試的合數

  $$n \ \text{為 Carmichael 數} \quad \overset{\text{def}}{\Longleftrightarrow} \quad n \ \text{為合數},\ \ a^{n} \equiv a \pmod{n} \ \text{ for all } a \in \mathbf{Z}$$

  * $n$ : 正整數 (A positive integer) $[n \in \mathbf{P}]$
  * $a$ : 任意整數 (An arbitrary integer) $[a \in \mathbf{Z}]$

* **【推導 1】 指數滿足整除條件時的費馬型同餘 (A Fermat-type congruence when the exponent condition holds)：** 【證明 (b)】要用。
  設 $p$ 為質數、$\left(p - 1\right) \mid \left(n - 1\right)$，寫 $n - 1 = \left(p - 1\right)k$，則對所有 $a$，$a^n \equiv a \pmod p$

  * (a) $p \nmid a$：

    $$\begin{gather*}
    a^{n} &=& a \cdot \left(a^{p-1}\right)^{k} \\
    \left(a^{p-1}\right)^{k} &\overset{\text{已知 1,已知 2(c)}}{\equiv}& 1^{k} \pmod{p} \\
    a \cdot \left(a^{p-1}\right)^{k} &\overset{\text{已知 2(b)}}{\equiv}& a \pmod{p} \\
    a^{n} &\equiv& a \pmod{p}
    \end{gather*}$$

  * (b) $p \mid a$：

    $$\begin{gather*}
    a &\overset{\text{已知 3}}{\equiv}& 0 \pmod{p} \\
    a^{n} &\overset{\text{已知 2(c)}}{\equiv}& 0 \pmod{p} \\
    a^{n} &\overset{\text{已知 2(a)}}{\equiv}& a \pmod{p}
    \end{gather*}$$

  * $p$ : 質數 (A prime) $[p \in \mathbf{P}]$
  * $n$ : 指數 (The exponent) $[n \in \mathbf{P}]$
  * $k$ : 商 (The quotient) $[k \in \mathbf{P}]$
  * $a$ : 任意整數 (An arbitrary integer) $[a \in \mathbf{Z}]$

+++

## 證明:

### (a) proof that five hundred sixty-one is composite

$$\begin{gather*}
3 \times 11 &=& 33 \\
33 \times 17 &=& 561
\end{gather*}$$

$561$ 有真因數 $3$，不是質數。

### (b) proof of the congruence modulo each prime factor

$560$ 同時是 $2$、$10$、$16$ 的倍數，三個質因數都滿足【推導 1】的條件：

$$\begin{gather*}
560 &=& \left(3 - 1\right) \times 280 \\
a^{561} &\overset{\text{推導 1(a)(b)}}{\equiv}& a \pmod{3} \\
560 &=& \left(11 - 1\right) \times 56 \\
a^{561} &\overset{\text{推導 1(a)(b)}}{\equiv}& a \pmod{11} \\
560 &=& \left(17 - 1\right) \times 35 \\
a^{561} &\overset{\text{推導 1(a)(b)}}{\equiv}& a \pmod{17}
\end{gather*}$$

與投影片的三行一致（投影片寫的 $a\left(a^2\right)^{280}$、$a\left(a^{10}\right)^{56}$、$a\left(a^{16}\right)^{35}$ 就是【推導 1(a)】的第一行）。

### (c) proof of the congruence modulo five hundred sixty-one

三個質因數都整除 $a^{561} - a$。它們兩兩互質（相異質數互不整除），分兩步合併：

$$\begin{gather*}
3 &\overset{\text{已知 3,證明 (b)}}{\mid}& a^{561} - a \\
11 &\overset{\text{已知 3,證明 (b)}}{\mid}& a^{561} - a \\
17 &\overset{\text{已知 3,證明 (b)}}{\mid}& a^{561} - a \\
\gcd(3, 11) &\overset{\text{已知 5}}{=}& 1 \qquad \text{(} 3 \nmid 11 \text{)} \\
33 &\overset{\text{已知 4}}{\mid}& a^{561} - a \\
\gcd(17, 33) &\overset{\text{已知 5}}{=}& 1 \qquad \text{(} 17 \nmid 33 \text{)} \\
561 &\overset{\text{已知 4}}{\mid}& a^{561} - a \\
a^{561} &\overset{\text{已知 3}}{\equiv}& a \pmod{561}
\end{gather*}$$

配合 (a)：

$$\begin{gather*}
561 \ \text{為合數},\ \ a^{561} \equiv a \pmod{561} \ \forall a &\overset{\text{定義 1}}{\Longrightarrow}& 561 \ \text{為 Carmichael 數}
\end{gather*}$$

與投影片一致。

### (d) statement of minimality verified by computation

**陳述不證**：投影片說 $561$ 是最小的 Carmichael 數。一個手寫證明需要逐一排除 $561$ 以下的所有合數
（或先證 Korselt 判準再做有限的枚舉），本檔不做。以程式窮舉 $n < 2000$ 的所有合數、檢查所有底數 $0 \le a < n$，
得到的 Carmichael 數恰為 $561,\ 1105,\ 1729$，確認 $561$ 最小（見文末程式）。

+++

## 意義與密碼學關聯 (Interpretation and Relevance to Cryptography)

### 為什麼 Carmichael 數讓費馬測試破產

[費馬小定理](Fermat_Little_Theorem.md) 的測試是「挑個 $a$，檢查 $a^n \equiv a$」。對 $341$ 這種偽質數，換個底數（如 $a = 3$）就能抓到。
但 Carmichael 數對**每一個**底數都通過 —— 換多少個 $a$ 都沒用。更糟的是，Alford–Granville–Pomerance（1994）證明了
**Carmichael 數有無窮多個**，所以不能靠查表排除。

這就是實務上一律用 **Miller–Rabin** 的原因：它多檢查了「$1$ 的平方根只能是 $\pm 1$」這個條件，
對 Carmichael 數同樣有效。RSA 金鑰產生時的質數測試（OpenSSL `BN_is_prime`）用的正是 Miller–Rabin。

### Korselt 判準（陳述不證）

合數 $n$ 是 Carmichael 數，若且唯若 $n$ **無平方因子**，且對 $n$ 的每個質因數 $p$ 都有 $\left(p - 1\right) \mid \left(n - 1\right)$。

本檔的【推導 1】加上【證明 (c)】其實就是 Korselt 判準的「若」方向在 $n = 561$ 的實例；
「只若」方向需要原根的存在性，超出本章範圍。

### 也是 RSA 的警訊

RSA 的正確性依賴 $m^{ed} \equiv m \pmod n$。Carmichael 數說明：這種「對所有 $m$ 都成立」的冪次恆等式，
**在合數模數下也可能成立** —— RSA 的 $n = pq$ 本身就是利用這個現象（由 CRT 把兩個質數的費馬小定理拼起來），
與本檔【證明 (c)】的結構完全相同。

### 程式思維

```python
def is_prime(n):
    return n > 1 and all(n % d for d in range(2, int(n**0.5) + 1))

def is_carmichael(n):
    return not is_prime(n) and n > 1 and all(pow(a, n, n) == a for a in range(n))

assert 561 == 3 * 11 * 17 and is_carmichael(561)                  # 證明 (a)(c)
assert [n for n in range(2, 2000) if is_carmichael(n)] == [561, 1105, 1729]   # 證明 (d)
assert pow(3, 341, 341) != 3                                      # 341 只騙得過底數 2
```
