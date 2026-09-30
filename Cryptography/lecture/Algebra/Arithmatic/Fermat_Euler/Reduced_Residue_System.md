# Reduced Residue System (化簡剩餘系)

+++

## 證明目標:

`Arithmetic.pdf` p.53。[完全剩餘系](Complete_Residue_System.md) 只保留**與 $n$ 互質**的那些代表，就是化簡剩餘系 ——
它是 $\mathbf{Z}_n^*$ 的一組代表元。投影片的命題「乘以與 $n$ 互質的數，化簡剩餘系仍是化簡剩餘系」
正是尤拉定理（投影片的證明路線）的核心。

* (a) 驗證 $n = 15$ 的第一個例子：

$$R_1 = \left\{1, 2, 4, 7, 8, 11, 13, 14\right\}$$

  是模 $15$ 的化簡剩餘系。

* (b) 投影片的命題：

$$R \ \text{為模 } n \text{ 的化簡剩餘系},\ \ a \perp n \quad \Longrightarrow \quad aR = \left\{ar \ \middle|\ r \in R\right\} \ \text{亦然}$$

* (c) 驗證第二個例子 $R_2 = 4R_1 = \left\{4, 8, 16, 28, 32, 44, 52, 56\right\}$，且模 $15$ 後恰為 $R_1$ 的重排：

$$R_2 \equiv \left\{4, 8, 1, 13, 2, 14, 7, 11\right\} \pmod{15}$$

* $n$ : 模數 (The modulus) $[n \in \mathbf{P}]$
* $R$ : 化簡剩餘系 (A reduced residue system) $[R \subseteq \mathbf{Z}]$
* $a$ : 與 $n$ 互質的整數 (An integer coprime to $n$) $[a \in \mathbf{Z}]$
* $aR$ : $R$ 的每個元素乘 $a$ (The set $R$ scaled by $a$) $[aR \subseteq \mathbf{Z}]$
* 註（**投影片的定義少寫「相異」**）：投影片 (ii) 寫「$r_1 \not\equiv r_2 \pmod n$ for all $r_1, r_2 \in R$」，
  字面上連 $r_1 = r_2$ 也要求不同餘，那是不可能的。正確的寫法是「**相異的** $r_1, r_2$ 模 $n$ 不同餘」，本檔依此修正。
* 註：投影片 p.53 的式子「$R_2 \equiv \left\{4, 8, 1, 13, 2, 14, 7, 11\right\} = R_1$」的意思是「作為集合相等」，順序不同無妨。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [互質對乘法封閉 (Coprimality is closed under products)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/Factorization/Relatively_Prime.html#b-proof-that-coprimality-to-a-modulus-is-closed-under-products)：** 已於本章 [互質](../Factorization/Relatively_Prime.md)【證明 (b)】完整證明，此處直接引用不再重證

  $$a \perp n,\ \ r \perp n \quad \Longrightarrow \quad ar \perp n$$

  * $a,\ r$ : 整數 (Integers) $[a, r \in \mathbf{Z}]$
  * $n$ : 模數 (The modulus) $[n \in \mathbf{P}]$

* **【已知 2】 [互質消去律 (Cancellation of a coprime factor)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/Congruence/Congruence_Properties.html#g-proof-of-cancellation-for-a-coprime-factor)：** 已於本章 [同餘的性質](../Congruence/Congruence_Properties.md)【證明 (g)】完整證明，此處直接引用不再重證

  $$a \perp n,\ \ ar_1 \equiv ar_2 \pmod{n} \quad \Longrightarrow \quad r_1 \equiv r_2 \pmod{n}$$

  * $a$ : 與 $n$ 互質的整數 (An integer coprime to $n$) $[a \in \mathbf{Z}]$
  * $r_1,\ r_2$ : 整數 (Integers) $[r_1, r_2 \in \mathbf{Z}]$
  * $n$ : 模數 (The modulus) $[n \in \mathbf{P}]$

* **【已知 3】 [尤拉函數的值 (Values of the totient)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/Fermat_Euler/Euler_Phi_Multiplicativity.html#e-proof-of-multiplicativity)：** 已於本章 [尤拉函數](Euler_Phi_Function.md)【證明 (b)】與 [尤拉函數的乘法性](Euler_Phi_Multiplicativity.md)【證明 (a)(e)】完整證明，此處直接引用不再重證

  * (a) 乘法性與質數值：

    $$\varphi(mn) = \varphi(m)\varphi(n) \ \left(m \perp n\right), \qquad \varphi(p) = p - 1$$

  * (b) 與乘積互質的拆分：

    $$x \perp mn \quad \Longleftrightarrow \quad x \perp m \ \text{ and } \ x \perp n$$

  * $m,\ n$ : 互質的正整數 (Coprime positive integers) $[m, n \in \mathbf{P}]$
  * $p$ : 質數 (A prime) $[p \in \mathbf{P}]$
  * $x$ : 整數 (An integer) $[x \in \mathbf{Z}]$

* **【已知 4】 [質數的互質判準 (Coprimality to a prime)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/Fermat_Euler/Fermat_Little_Theorem.html#a-proof-that-the-two-formulations-of-the-hypothesis-agree)：** 已於本章 [費馬小定理](Fermat_Little_Theorem.md)【證明 (a)】完整證明，此處直接引用不再重證

  $$x \perp p \quad \Longleftrightarrow \quad p \nmid x \qquad \left(p \ \text{為質數}\right)$$

  * $x$ : 整數 (An integer) $[x \in \mathbf{Z}]$
  * $p$ : 質數 (A prime) $[p \in \mathbf{P}]$

* **【已知 5】 [最小非負剩餘系 (The least non-negative residues)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/Fermat_Euler/Complete_Residue_System.html#d-proof-that-the-least-non-negative-residues-form-a-complete-residue-system)：** 已於本章 [完全剩餘系](Complete_Residue_System.md)【定義 1(b)】【證明 (d)】給出並證明，此處直接引用不再重證。$\left[0, n\right)$ 裡的相異整數兩兩不同餘

  $$0 \le u, v < n,\ \ u \neq v \quad \Longrightarrow \quad u \not\equiv v \pmod{n}$$

  * $u,\ v$ : $\left[0, n\right)$ 中的整數 (Integers in $\left[0, n\right)$) $[u, v \in \mathbf{Z}_n]$
  * $n$ : 模數 (The modulus) $[n \in \mathbf{P}]$

* **【定義 1】 化簡剩餘系 (Reduced residue system)：** 由 $\varphi(n)$ 個整數組成的集合 $R$，滿足

  * (a) 每個都與 $n$ 互質：

    $$r \perp n \qquad \text{for every } r \in R$$

  * (b) 相異元素兩兩不同餘：

    $$r_1, r_2 \in R,\ \ r_1 \neq r_2 \quad \Longrightarrow \quad r_1 \not\equiv r_2 \pmod{n}$$

  * $R$ : 候選集合，$\left|R\right| = \varphi(n)$ (The candidate set) $[R \subseteq \mathbf{Z}]$
  * $r,\ r_1,\ r_2$ : $R$ 的元素 (Elements of $R$) $[r, r_1, r_2 \in R]$
  * $n$ : 模數 (The modulus) $[n \in \mathbf{P}]$

+++

## 證明:

### (a) verify the first example modulo fifteen

**個數**：$15 = 3 \times 5$，$\varphi(15) = 2 \times 4 = 8$，而 $R_1$ 恰有 $8$ 個元素：

$$\begin{gather*}
\varphi(15) &\overset{\text{已知 3(a)}}{=}& \left(3 - 1\right)\left(5 - 1\right) \\
\varphi(15) &=& 8
\end{gather*}$$

**互質**：與 $15$ 互質等價於「不被 $3$ 也不被 $5$ 整除」。$\left[1, 14\right]$ 中被 $3$ 或 $5$ 整除的是 $3, 5, 6, 9, 10, 12$，剩下的正是 $R_1$：

$$\begin{gather*}
x \perp 15 &\overset{\text{已知 3(b)}}{\Longleftrightarrow}& x \perp 3 \ \text{ and } \ x \perp 5 \\
&\overset{\text{已知 4}}{\Longleftrightarrow}& 3 \nmid x \ \text{ and } \ 5 \nmid x
\end{gather*}$$

**不同餘**：$R_1 \subseteq \left[0, 15\right)$ 且元素相異，由【已知 5】兩兩不同餘。三條都成立，依【定義 1】$R_1$ 是化簡剩餘系：

$$\begin{gather*}
R_1 \subseteq \left[0, 15\right),\ \ \text{元素相異} &\overset{\text{已知 5}}{\Longrightarrow}& R_1 \ \text{兩兩不同餘} \\
\left|R_1\right| = \varphi(15),\ \ R_1 \ \text{滿足 (a)(b)} &\overset{\text{定義 1}}{\Longrightarrow}& R_1 \ \text{為化簡剩餘系}
\end{gather*}$$

### (b) proof that scaling by a coprime integer preserves a reduced residue system

**(i) 每個 $ar$ 都與 $n$ 互質**：

$$\begin{gather*}
r &\overset{\text{定義 1(a)}}{\perp}& n \qquad \text{for every } r \in R \\
a \perp n,\ \ r \perp n &\overset{\text{已知 1}}{\Longrightarrow}& ar \perp n
\end{gather*}$$

**(ii) 兩兩不同餘，而且個數沒有變少**：若 $ar_1 \equiv ar_2$，消去 $a$ 得 $r_1 \equiv r_2$，由 $R$ 的 (b) 只能 $r_1 = r_2$。
這同時說明 $r \mapsto ar$ 是單射（$ar_1 = ar_2$ 當然也同餘），所以 $\left|aR\right| = \left|R\right| = \varphi(n)$：

$$\begin{gather*}
a r_1 &\equiv& a r_2 \pmod{n} \\
r_1 &\overset{\text{已知 2}}{\equiv}& r_2 \pmod{n} \\
r_1 &\overset{\text{定義 1(b)}}{=}& r_2
\end{gather*}$$

三條都成立，$aR$ 是化簡剩餘系，與投影片一致。

### (c) verify the second example as a scaled copy of the first

$4 \perp 15$（$4 \times 4 - 15 = 1$），由 (b) $R_2 = 4R_1$ 是化簡剩餘系。逐一取模 $15$ 確認它就是 $R_1$ 的重排：

$$\begin{gather*}
R_2 &=& \left\{4 \times 1,\ 4 \times 2,\ 4 \times 4,\ 4 \times 7,\ 4 \times 8,\ 4 \times 11,\ 4 \times 13,\ 4 \times 14\right\} \\
R_2 &=& \left\{4,\ 8,\ 16,\ 28,\ 32,\ 44,\ 52,\ 56\right\} \\
R_2 \bmod 15 &=& \left\{4,\ 8,\ 1,\ 13,\ 2,\ 14,\ 7,\ 11\right\} \\
R_2 \bmod 15 &=& \left\{1,\ 2,\ 4,\ 7,\ 8,\ 11,\ 13,\ 14\right\} \\
4 \perp 15 &\overset{\text{證明 (b)}}{\Longrightarrow}& R_2 = 4R_1 \ \text{為化簡剩餘系}
\end{gather*}$$

（例如 $52 = 3 \times 15 + 7$、$56 = 3 \times 15 + 11$。）與投影片一致。

+++

## 意義與密碼學關聯 (Interpretation and Relevance to Cryptography)

### 投影片的尤拉定理證明路線

投影片 p.54 說尤拉定理的證明「Similar to the proof of Fermat's Little Theorem, where complete residue system is replaced by reduced residue system」。
有了 (b)，那個證明就是三行（以 $R = \left\{r_1, \dots, r_{\varphi(n)}\right\}$ 表示）：

1. $aR$ 與 $R$ 是同一組同餘類，所以兩者的乘積同餘：$\prod \left(a r_i\right) \equiv \prod r_i$；
2. 左邊提出 $a$：$a^{\varphi(n)} \prod r_i \equiv \prod r_i$；
3. $\prod r_i$ 與 $n$ 互質（【已知 1】），可以消去（【已知 2】）：$a^{\varphi(n)} \equiv 1$。

尤拉定理本身已在 Abstract_Algebra 章用拉格朗日定理證完，本章依引用免證原則**不重證**（見 [尤拉定理](Euler_Theorem.md)）；
這裡只是指出投影片的路線與本檔命題的關係。兩條路線的本質相同：「乘以 $a$」是群 $\mathbf{Z}_n^*$ 上的一個**排列**。

### 乘以 $a$ 是 $\mathbf{Z}_n^*$ 的排列

(b) 用群論的話說：映射 $x \mapsto ax$ 是 $\mathbf{Z}_n^*$ 到自己的雙射。
這個「乘法打亂」在密碼學裡隨處可見 —— RSA 的盲簽章（blind signature）正是把訊息乘上 $r^e$ 打亂，
簽完再乘回 $r^{-1}$；因為乘以可逆元是排列，打亂後的訊息**均勻分布**，簽章者看不出原始內容。

### 程式思維

```python
from math import gcd
n = 15
R1 = [x for x in range(1, n) if gcd(x, n) == 1]
assert R1 == [1, 2, 4, 7, 8, 11, 13, 14]                          # 證明 (a)
R2 = [4 * r for r in R1]
assert R2 == [4, 8, 16, 28, 32, 44, 52, 56]
assert sorted(r % n for r in R2) == R1                             # 證明 (c)
# 證明 (b)：對每個與 n 互質的 a，aR1 都是 R1 的重排
assert all(sorted(a * r % n for r in R1) == R1 for a in R1)
```
