# Euler Theorem (尤拉定理)

+++

## 證明目標:

`Arithmetic.pdf` p.47、p.54。**尤拉定理本身已在 Abstract_Algebra 章用拉格朗日定理證完**
（[元素的階與循環子群](../../Abstract_Algebra/Group/Order_of_Element_and_Cyclic_Subgroup.md)【證明 (c)】），本檔引用不重證。
本檔證明它的兩個推論、驗證投影片的例子，並展示它如何讓 RSA 能夠解密。

* (a) 投影片的 Remark：費馬小定理是尤拉定理的特例。

$$a \perp p \quad \Longrightarrow \quad a^{\varphi(p)} = a^{p-1} \equiv 1 \pmod{p}$$

* (b) **指數可以模 $\varphi(n)$ 化簡**（投影片未明列，但例子正是這樣算的）：

$$a \perp n \quad \Longrightarrow \quad a^{k} \equiv a^{k \bmod \varphi(n)} \pmod{n}$$

* (c) 驗證投影片的例子：

$$11^{2006} \equiv 16 \pmod{21}$$

* $a$ : 與模數互質的整數 (An integer coprime to the modulus) $[a \in \mathbf{Z}]$
* $n$ : 模數 (The modulus) $[n \in \mathbf{P}]$
* $p$ : 質數 (A prime) $[p \in \mathbf{P}]$
* $k$ : 非負整數指數 (A non-negative exponent) $[k \in \mathbf{N}]$
* $\varphi$ : 尤拉函數 (Euler's totient function) $[\mathbf{P} \to \mathbf{P}]$
* 註：投影片的證明「Similar to the proof of Fermat's Little Theorem, where complete residue system is replaced by reduced residue system」
  的三行版本寫在 [化簡剩餘系](Reduced_Residue_System.md) 的意義段；本檔依引用免證原則採用 Abstract_Algebra 章的群論證明。
* 註：**$a \perp n$ 不可省**。$a = 3$、$n = 6$：$\varphi(6) = 2$，但 $3^2 = 9 \equiv 3 \not\equiv 1 \pmod 6$。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [尤拉定理 (Euler's theorem)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Group/Order_of_Element_and_Cyclic_Subgroup.html#c-proof-of-eulers-theorem)：** 已於 Abstract_Algebra 章 [元素的階與循環子群](../../Abstract_Algebra/Group/Order_of_Element_and_Cyclic_Subgroup.md)【證明 (c)】完整證明，此處直接引用不再重證

  $$\gcd(a, n) = 1 \quad \Longrightarrow \quad a^{\varphi(n)} \equiv 1 \pmod{n}$$

  * $a$ : 與 $n$ 互質的整數 (An integer coprime to $n$) $[a \in \mathbf{Z}]$
  * $n$ : 模數 (The modulus) $[n \in \mathbf{P}]$
  * $\varphi$ : 尤拉函數 (Euler's totient function) $[\mathbf{P} \to \mathbf{P}]$

* **【已知 2】 [尤拉函數的值 (Values of the totient)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/Fermat_Euler/Euler_Phi_Multiplicativity.html#e-proof-of-multiplicativity)：** 已於本章 [尤拉函數](Euler_Phi_Function.md)【證明 (b)】與 [尤拉函數的乘法性](Euler_Phi_Multiplicativity.md)【證明 (e)】完整證明，此處直接引用不再重證

  * (a) 質數：

    $$\varphi(p) = p - 1$$

  * (b) 乘法性：

    $$\varphi(mn) = \varphi(m)\varphi(n) \qquad \left(m \perp n\right)$$

  * $p$ : 質數 (A prime) $[p \in \mathbf{P}]$
  * $m,\ n$ : 互質的正整數 (Coprime positive integers) $[m, n \in \mathbf{P}]$

* **【已知 3】 [同餘的運算性質 (Arithmetic of congruences)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/Congruence/Congruence_Properties.html#e-proof-that-congruences-can-be-multiplied-together)：** 已於本章 [同餘的性質](../Congruence/Congruence_Properties.md)【證明 (a)(c)(d)】完整證明，此處直接引用不再重證

  * (a) 遞移性：

    $$u \equiv v,\ \ v \equiv w \quad \Longrightarrow \quad u \equiv w \pmod{m}$$

  * (b) 兩邊同乘：

    $$u \equiv v \quad \Longrightarrow \quad uc \equiv vc \pmod{m}$$

  * (c) 兩邊同取冪：

    $$u \equiv v \quad \Longrightarrow \quad u^{d} \equiv v^{d} \pmod{m}$$

  * $u,\ v,\ w,\ c$ : 任意整數 (Arbitrary integers) $[\mathbf{Z}]$
  * $m$ : 模數 (The modulus) $[m \in \mathbf{P}]$
  * $d$ : 正整數指數 (A positive exponent) $[d \in \mathbf{P}]$

* **【已知 4】 [除法原理與同餘 (Division algorithm and congruence)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/Congruence/Congruence_Relation.html#b-proof-that-a-difference-divisible-by-the-modulus-gives-equal-remainders)：** 已於本章 [取模函數](../Division/Modular_Function.md)【證明 (b)】與 [同餘關係](../Congruence/Congruence_Relation.md)【證明 (a)(b)】完整證明，此處直接引用不再重證

  * (a) 除法原理：

    $$k = q\,\varphi(n) + \left(k \bmod \varphi(n)\right), \qquad q = \left\lfloor k / \varphi(n) \right\rfloor$$

  * (b) 同餘的整除刻畫：

    $$u \equiv v \pmod{m} \quad \Longleftrightarrow \quad m \mid \left(u - v\right)$$

  * $k$ : 非負整數 (A non-negative integer) $[k \in \mathbf{N}]$
  * $q$ : 商 (The quotient) $[q \in \mathbf{N}]$
  * $u,\ v$ : 任意整數 (Arbitrary integers) $[u, v \in \mathbf{Z}]$
  * $m,\ n$ : 模數 (Moduli) $[m, n \in \mathbf{P}]$

* **【已知 5】 [互質的組合判準 (Coprimality via a combination)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/GCD/Bezout_Identity.html#d-proof-that-a-combination-equal-to-one-forces-coprimality)：** 已於本章 [貝祖等式](../GCD/Bezout_Identity.md)【證明 (d)】完整證明，此處直接引用不再重證

  $$ax + ny = 1 \ \text{ for some } x, y \in \mathbf{Z} \quad \Longrightarrow \quad \gcd(a, n) = 1$$

  * $a$ : 整數 (An integer) $[a \in \mathbf{Z}]$
  * $n$ : 正整數 (A positive integer) $[n \in \mathbf{P}]$
  * $x,\ y$ : 組合係數 (Combination coefficients) $[x, y \in \mathbf{Z}]$

+++

## 證明:

### (a) proof that Fermat's little theorem is a special case

取 $n = p$ 為質數：

$$\begin{gather*}
a^{\varphi(p)} &\overset{\text{已知 1}}{\equiv}& 1 \pmod{p} \\
\varphi(p) &\overset{\text{已知 2(a)}}{=}& p - 1 \\
a^{p-1} &\equiv& 1 \pmod{p}
\end{gather*}$$

與 [費馬小定理](Fermat_Little_Theorem.md)【證明 (a)】一致，也與投影片的 Remark 一致。

### (b) proof that exponents can be reduced modulo phi of n

把 $k$ 用除法原理拆成 $q\,\varphi(n) + r$，$\varphi(n)$ 那一份整包變成 $1$：

$$\begin{gather*}
a^{k} &\overset{\text{已知 4(a)}}{=}& \left(a^{\varphi(n)}\right)^{q} \cdot a^{r} \qquad \left(r = k \bmod \varphi(n)\right) \\
\left(a^{\varphi(n)}\right)^{q} &\overset{\text{已知 1,已知 3(c)}}{\equiv}& 1^{q} \pmod{n} \\
\left(a^{\varphi(n)}\right)^{q} \cdot a^{r} &\overset{\text{已知 3(b)}}{\equiv}& a^{r} \pmod{n} \\
a^{k} &\equiv& a^{k \bmod \varphi(n)} \pmod{n}
\end{gather*}$$

### (c) verify the example of eleven to the power two thousand six modulo twenty-one

**前置**：$11 \perp 21$，且 $\varphi(21) = 12$：

$$\begin{gather*}
11 \times 2 + 21 \times \left(-1\right) &=& 1 \\
\gcd(11, 21) &\overset{\text{已知 5}}{=}& 1 \\
\varphi(21) &\overset{\text{已知 2(b)}}{=}& \varphi(3)\,\varphi(7) \\
\varphi(21) &\overset{\text{已知 2(a)}}{=}& 2 \times 6 \\
\varphi(21) &=& 12
\end{gather*}$$

**化簡指數**：$2006 = 12 \times 167 + 2$：

$$\begin{gather*}
11^{2006} &\overset{\text{證明 (b)}}{\equiv}& 11^{2006 \bmod 12} \pmod{21} \\
11^{2006} &\equiv& 11^{2} \pmod{21} \\
11^{2} &=& 121 \\
121 - 16 &=& 5 \times 21 \\
11^{2006} &\overset{\text{已知 4(b),已知 3(a)}}{\equiv}& 16 \pmod{21}
\end{gather*}$$

與投影片 p.54 一致（投影片寫的 $\left(11^{\varphi(21)}\right)^{167} \cdot 11^2 \equiv 1^{167} \cdot 121$ 正是【證明 (b)】的第一、二行）。

+++

## 意義與密碼學關聯 (Interpretation and Relevance to Cryptography)

### RSA 為什麼能解密：一個完整的小例子

RSA 的正確性就是【證明 (b)】：$ed \equiv 1 \pmod{\varphi(n)}$ 讓 $m^{ed}$ 的指數化簡成 $1$。
用小數字走一遍（全部數值已用程式核對）：

| 步驟 | 計算 | 結果 |
|---|---|---|
| 選質數 | $p = 5$、$q = 11$ | $n = 55$ |
| 算 $\varphi(n)$ | $\varphi(55) = 4 \times 10$（[乘法性](Euler_Phi_Multiplicativity.md)） | $40$ |
| 公鑰指數 | $e = 3$，$\gcd(3, 40) = 1$ | $e = 3$ |
| 私鑰 | $d = 3^{-1} \bmod 40$（[模反元素](../Congruence/Modular_Inverse.md)），$3 \times 27 = 81 = 2 \times 40 + 1$ | $d = 27$ |
| 加密 $m = 7$ | $c = 7^3 \bmod 55 = 343 \bmod 55$ | $c = 13$ |
| 解密 | $13^{27} \bmod 55$ | $7$ |

解密為什麼回到 $7$：$ed = 81 = 2 \times 40 + 1$，而 $7 \perp 55$，由【證明 (b)】
$7^{81} \equiv 7^{81 \bmod 40} = 7^{1} \pmod{55}$。

（$\gcd(m, n) \neq 1$ 的極少數明文要另外用 [中國剩餘定理](../CRT/Chinese_Remainder_Theorem.md) 分別在模 $p$、模 $q$ 下用
[費馬小定理](Fermat_Little_Theorem.md)【證明 (b)】的 $a^p \equiv a$ 處理，結論仍成立 —— 與 [Carmichael 數](Carmichael_Numbers.md)【證明 (c)】的論證結構相同。）

### 尤拉其人

投影片 p.47：Leonhard Euler（1707–1783），瑞士數學家與物理學家，在微積分、數論、拓樸都有奠基性貢獻，
現代數學的許多記號（$f(x)$、$e$、$i$、$\sum$、$\pi$ 的普及）都出自他。
他在 1736 年給出費馬小定理的第一個發表證明，1763 年推廣成本檔的定理，並引入今日稱為尤拉函數的計數函數
（記號 $\varphi$ 則是後來由高斯普及的）。

### 程式思維：快速冪 (square-and-multiply)

```python
def power_mod(a, k, n):
    """由低位到高位掃描 k 的二進位（取模函數的進位轉換），O(log k) 次乘法。"""
    result, base = 1, a % n
    while k > 0:
        if k & 1:
            result = result * base % n      # 這一位是 1：乘進答案
        base = base * base % n              # 平方，準備下一位
        k >>= 1
    return result

assert power_mod(11, 2006, 21) == 16 == pow(11, 2006 % 12, 21)    # 證明 (c)
p, q, e = 5, 11, 3
n, phi_n = p * q, (p - 1) * (q - 1)
d = pow(e, -1, phi_n)
assert (n, phi_n, d) == (55, 40, 27)
c = power_mod(7, e, n)
assert c == 13 and power_mod(c, d, n) == 7                         # RSA 小例子
assert pow(3, 2, 6) != 1                                           # 互質條件不可省
```
