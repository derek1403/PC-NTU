# Modular Inverse (模反元素)

+++

## 證明目標:

`Arithmetic.pdf` p.30–32。模 $m$ 的世界裡「除以 $a$」的意思是「乘以 $a$ 的反元素」。
本檔回答三個問題：**什麼時候有反元素？怎麼算？怎麼用來解一次同餘式？**

* (a)(b) 投影片的定理（證明留作習題）：

$$a^{-1} \bmod m \ \text{存在} \quad \Longleftrightarrow \quad a \perp m$$

* (c) 投影片的應用：一次同餘式的解

$$a \perp m: \qquad ax \equiv b \pmod{m} \quad \Longleftrightarrow \quad x \equiv a^{-1} b \pmod{m}$$

* (d) 投影片 p.31 的矩陣演算法正確（**需補一步取模**，見註）。
* (e) 驗證投影片 p.32 的例子：

$$160^{-1} \equiv 205 \pmod{841}, \qquad 160x \equiv 7 \pmod{841} \ \Longrightarrow \ x \equiv 594 \pmod{841}$$

* (f) 投影片演算法的輸出可能是負數：以 $3^{-1} \bmod 7$ 為例。

* $a$ : 要求反元素的整數 (The integer to invert) $[a \in \mathbf{Z}]$
* $m$ : 模數 (The modulus) $[m \in \mathbf{P}]$
* $a^{-1} \bmod m$ : $a$ 模 $m$ 的反元素 (The inverse of $a$ modulo $m$) $[a^{-1} \bmod m \in \mathbf{P}]$
* $b$ : 同餘式右邊 (The right-hand side) $[b \in \mathbf{Z}]$
* $x$ : 未知數 (The unknown) $[x \in \mathbf{Z}]$
* 註（**投影片的演算法漏一步**）：p.31 的演算法在 $r_0 = 1$ 時「Return $x_0$ [$= a^{-1} \bmod m$]」，
  但 $x_0$ **可能是負數或不在 $\left[1, m\right]$ 內**，而投影片 p.30 的定義要求反元素是**最小的正整數**。
  正確的輸出是 $x_0 \bmod m$（當 $m = 1$ 時改輸出 $1$）。p.32 的例子剛好得到正數 $205$，所以沒有暴露這個問題；(f) 給出一個會出錯的例子。
* 註：Abstract_Algebra 章 [數系與符號約定](../../Abstract_Algebra/Number_Sets_and_Notation.md)【已知 3】
  把 (a)(b) 當成外部已知引用，本檔把它證出來。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [互質的組合刻畫 (Coprimality via combinations)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/GCD/Bezout_Identity.html#d-proof-that-a-combination-equal-to-one-forces-coprimality)：** 已於本章 [貝祖等式](../GCD/Bezout_Identity.md)【證明 (c)(d)】完整證明，此處直接引用不再重證

  $$\gcd(a, m) = 1 \quad \Longleftrightarrow \quad \exists\, x, y \in \mathbf{Z} \ \text{ such that } \ ax + my = 1$$

  * $a$ : 任意整數 (An arbitrary integer) $[a \in \mathbf{Z}]$
  * $m$ : 模數 (The modulus) $[m \in \mathbf{P}]$
  * $x,\ y$ : 組合係數 (Combination coefficients) $[x, y \in \mathbf{Z}]$

* **【已知 2】 [同餘的整除刻畫 (Congruence as divisibility)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/Congruence/Congruence_Relation.html#b-proof-that-a-difference-divisible-by-the-modulus-gives-equal-remainders)：** 已於本章 [同餘關係](Congruence_Relation.md)【證明 (a)(b)(c)】完整證明，此處直接引用不再重證

  * (a) 整除刻畫：

    $$u \equiv v \pmod{m} \quad \Longleftrightarrow \quad m \mid \left(u - v\right)$$

  * (b) 與自己的餘數同餘：

    $$u \equiv \left(u \bmod m\right) \pmod{m}$$

  * $u,\ v$ : 任意整數 (Arbitrary integers) $[u, v \in \mathbf{Z}]$
  * $m$ : 模數 (The modulus) $[m \in \mathbf{P}]$

* **【已知 3】 [同餘的運算性質 (Arithmetic of congruences)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/Congruence/Congruence_Properties.html#e-proof-that-congruences-can-be-multiplied-together)：** 已於本章 [同餘的性質](Congruence_Properties.md)【證明 (a)(c)(e)】完整證明，此處直接引用不再重證

  * (a) 遞移性：

    $$u \equiv v,\ \ v \equiv w \quad \Longrightarrow \quad u \equiv w \pmod{m}$$

  * (b) 兩邊同乘：

    $$u \equiv v \quad \Longrightarrow \quad uc \equiv vc \pmod{m}$$

  * $u,\ v,\ w,\ c$ : 任意整數 (Arbitrary integers) $[\mathbf{Z}]$
  * $m$ : 模數 (The modulus) $[m \in \mathbf{P}]$

* **【已知 4】 [擴展歐幾里得演算法 (Extended Euclidean algorithm)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/GCD/Extended_Euclidean_Algorithm.html#b-proof-of-the-inductive-step-for-the-next-remainder)：** 已於本章 [擴展歐幾里得演算法](../GCD/Extended_Euclidean_Algorithm.md)【定義 1】【證明 (a)(b)(c)】【證明 (e)】給出並證明，此處直接引用不再重證。
  以 $\left(a, m\right)$ 為輸入（$m > 0$）

  * (a) 不變量：每一步都有

    $$r_k = a x_k + m y_k$$

  * (b) 終止與輸出：矩陣迴圈在有限步後停下，第一列的 $r$ 等於 gcd

    $$r_{\text{final}} = \gcd(a, m)$$

  * $r_k,\ x_k,\ y_k$ : 第 $k$ 步的餘數與係數 (The $k$-th remainder and coefficients) $[\mathbf{Z}]$
  * $a$ : 輸入整數 (The input integer) $[a \in \mathbf{Z}]$
  * $m$ : 輸入模數 (The input modulus) $[m \in \mathbf{P}]$

* **【已知 5】 [良序原理 (Well-ordering principle)](https://mathworld.wolfram.com/WellOrderingPrinciple.html)：** 標準結果，本章直接引用不再重證

  $$\varnothing \neq T \subseteq \mathbf{P} \quad \Longrightarrow \quad \min T \ \text{存在}$$

  * $T$ : 正整數的非空子集 (A non-empty set of positive integers) $[T \subseteq \mathbf{P}]$

* **【定義 1】 模反元素 (Modular inverse)：** 投影片 p.30 的定義

  $$a^{-1} \bmod m \overset{\text{def}}{=} \min\left\{c \in \mathbf{P} \ \middle|\ ac \equiv 1 \pmod{m}\right\}$$

  * $a^{-1} \bmod m$ : $a$ 模 $m$ 的反元素 (The inverse of $a$ modulo $m$) $[a^{-1} \bmod m \in \mathbf{P}]$
  * $a$ : 要求反元素的整數 (The integer to invert) $[a \in \mathbf{Z}]$
  * $m$ : 模數 (The modulus) $[m \in \mathbf{P}]$
  * $c$ : 候選反元素 (A candidate inverse) $[c \in \mathbf{P}]$
  * 註：「反元素存在」的意思就是這個集合**非空**（非空則由【已知 5】最小值自動存在）。
  * 註：若 $c$ 是一個反元素，$c \bmod m$（為 $0$ 時改取 $m$）也是，所以最小者落在 $\left[1, m\right]$；$m > 1$ 時落在 $\left[1, m-1\right]$。

+++

## 證明:

### (a) proof (⇒) that an inverse forces coprimality

有反元素 $c$，就把「$ac \equiv 1$」翻成一個湊出 $1$ 的組合：

$$\begin{gather*}
ac &\overset{\text{定義 1}}{\equiv}& 1 \pmod{m} \\
ac - 1 &\overset{\text{已知 2(a)}}{=}& mk \qquad \text{for some } k \in \mathbf{Z} \\
ac + m\left(-k\right) &=& 1 \\
\gcd(a, m) &\overset{\text{已知 1}}{=}& 1
\end{gather*}$$

### (b) proof (⇐) that coprimality gives an inverse

由【已知 1】取 $ax + my = 1$，則 $x$ 已經滿足 $ax \equiv 1$。$x$ 可能不是正的，加上夠多個 $m$ 把它推成正數，同餘不變：

$$\begin{gather*}
ax + my &\overset{\text{已知 1}}{=}& 1 \\
ax - 1 &=& m\left(-y\right) \\
ax &\overset{\text{已知 2(a)}}{\equiv}& 1 \pmod{m} \\
c_0 &\overset{\text{let}}{=}& x + m\left(\left|x\right| + 1\right) \\
c_0 &\ge& x + \left|x\right| + 1 \qquad \text{(} m \ge 1 \text{)} \\
x + \left|x\right| + 1 &\ge& 1 \\
a c_0 - ax &=& m \cdot a\left(\left|x\right| + 1\right) \\
a c_0 &\overset{\text{已知 2(a),已知 3(a)}}{\equiv}& 1 \pmod{m}
\end{gather*}$$

於是 $c_0$ 屬於【定義 1】的集合，集合非空，最小值存在：

$$\begin{gather*}
a^{-1} \bmod m &\overset{\text{定義 1,已知 5}}{=}& \min\left\{c \in \mathbf{P} \ \middle|\ ac \equiv 1\right\}
\end{gather*}$$

(a)(b) 合起來即投影片的定理。

### (c) proof that the linear congruence is solved by the inverse

記 $c = a^{-1} \bmod m$（由 (b) 存在）。

**任何解都 $\equiv cb$**：把 $ax \equiv b$ 兩邊乘 $c$，左邊的 $ca$ 同餘於 $1$：

$$\begin{gather*}
c\left(ax\right) &\overset{\text{已知 3(b)}}{\equiv}& cb \pmod{m} \\
\left(ca\right)x &\overset{\text{已知 3(b)}}{\equiv}& 1 \cdot x \pmod{m} \qquad \text{(} ca \equiv 1 \text{)} \\
x &\overset{\text{已知 3(a)}}{\equiv}& cb \pmod{m}
\end{gather*}$$

**$cb$ 確實是解**：

$$\begin{gather*}
a\left(cb\right) &=& \left(ac\right) b \\
\left(ac\right) b &\overset{\text{已知 3(b)}}{\equiv}& 1 \cdot b \pmod{m} \\
a\left(cb\right) &\overset{\text{已知 3(a)}}{\equiv}& b \pmod{m}
\end{gather*}$$

與投影片「$x \equiv a^{-1}\left(ax\right) \equiv a^{-1} b$」一致。

### (d) proof that the matrix algorithm computes the inverse

投影片 p.31 的演算法就是 [擴展歐幾里得演算法](../GCD/Extended_Euclidean_Algorithm.md) 以 $\left(a, m\right)$ 為輸入、**只記 $x$ 欄**（$y$ 欄不影響 $r, x$ 的更新）。
由不變量，每一步 $r_k$ 都與 $a x_k$ 模 $m$ 同餘；結束時 $r = \gcd(a, m)$：

$$\begin{gather*}
r_k &\overset{\text{已知 4(a)}}{=}& a x_k + m y_k \\
r_k &\overset{\text{已知 2(a)}}{\equiv}& a x_k \pmod{m} \\
r_{\text{final}} &\overset{\text{已知 4(b)}}{=}& \gcd(a, m)
\end{gather*}$$

**若 $r_{\text{final}} = 1$**：$a x_{\text{final}} \equiv 1$，而 $x_{\text{final}} \bmod m$ 與它同餘，也是反元素：

$$\begin{gather*}
a x_{\text{final}} &\equiv& 1 \pmod{m} \\
a\left(x_{\text{final}} \bmod m\right) &\overset{\text{已知 2(b),已知 3(b)}}{\equiv}& 1 \pmod{m}
\end{gather*}$$

**若 $r_{\text{final}} \neq 1$**：$\gcd(a, m) \neq 1$，由【證明 (a)】反元素不存在，輸出「No Inverse」正確。

* 註：因此演算法的第一個分支應回傳 **$x_0 \bmod m$** 而不是 $x_0$。
  $x_0 \bmod m \in \left[0, m-1\right]$，且 $m > 1$ 時它不可能是 $0$（$a \cdot 0 \equiv 0 \not\equiv 1$），恰好就是【定義 1】的最小正反元素。

### (e) verify the example of one hundred sixty modulo eight hundred forty-one

依投影片 p.32 逐步（每一列是一次矩陣更新後的 $\left(r_0, x_0 ;\ r_1, x_1\right)$，$q = \left\lfloor r_0 / r_1 \right\rfloor$ 取自更新前）：

| 步 | $q$ | $r_0$ | $x_0$ | $r_1$ | $x_1$ |
|---|---|---|---|---|---|
| 起始 | | 160 | 1 | 841 | 0 |
| 1 | 0 | 841 | 0 | 160 | 1 |
| 2 | 5 | 160 | 1 | 41 | $-5$ |
| 3 | 3 | 41 | $-5$ | 37 | 16 |
| 4 | 1 | 37 | 16 | 4 | $-21$ |
| 5 | 9 | 4 | $-21$ | 1 | 205 |
| 6 | 4 | 1 | 205 | 0 | $-841$ |

$r_1 = 0$ 停止，$r_0 = 1$，故反元素是 $205 \bmod 841 = 205$。驗算並解方程式：

$$\begin{gather*}
160 \times 205 &=& 32800 \\
32800 &=& 39 \times 841 + 1 \\
160 \times 205 &\overset{\text{已知 2(a)}}{\equiv}& 1 \pmod{841} \\
x &\overset{\text{證明 (c)}}{\equiv}& 205 \times 7 \pmod{841} \\
x &\equiv& 1435 \pmod{841} \\
x &\overset{\text{已知 2(b)}}{\equiv}& 594 \pmod{841}
\end{gather*}$$

與投影片一致（$1435 = 841 + 594$）。

### (f) verify that the raw output can be negative

以 $a = 3$、$m = 7$ 跑投影片的演算法：

| 步 | $q$ | $r_0$ | $x_0$ | $r_1$ | $x_1$ |
|---|---|---|---|---|---|
| 起始 | | 3 | 1 | 7 | 0 |
| 1 | 0 | 7 | 0 | 3 | 1 |
| 2 | 2 | 3 | 1 | 1 | $-2$ |
| 3 | 3 | 1 | $-2$ | 0 | 7 |

投影片會回傳 $x_0 = -2$，但它不是正整數，不符合【定義 1】。補上取模後：

$$\begin{gather*}
-2 \bmod 7 &=& 5 \\
3 \times 5 &=& 15 \\
15 &\overset{\text{已知 2(a)}}{\equiv}& 1 \pmod{7} \\
3^{-1} \bmod 7 &\overset{\text{定義 1}}{=}& 5 \qquad \text{(} 3 \times 1, 3 \times 2, 3 \times 3, 3 \times 4 \text{ 模 } 7 \text{ 為 } 3, 6, 2, 5 \text{，都不是 } 1 \text{)}
\end{gather*}$$

+++

## 意義與密碼學關聯 (Interpretation and Relevance to Cryptography)

### 反元素 = 模世界裡的除法

在 $\mathbf{Z}_m$ 裡，「$b / a$」唯一合理的意思是 $b \times a^{-1}$。(a)(b) 說這個除法**只對與 $m$ 互質的 $a$ 有定義**。
這把 [凱萊表](../Division/Cayley_Tables_of_Z6.md) 上「哪一列找不到 $1$」的觀察變成了定理：
找不到 $1$ 的列，恰好是與模數有公因數的那些。

### RSA 私鑰就是一個模反元素

RSA 的私鑰 $d$ 定義為

$$d = e^{-1} \bmod \varphi(n)$$

公鑰指數 $e$ 必須與 $\varphi(n)$ 互質 —— 否則由 (a) 私鑰根本不存在。
常用的 $e = 65537$ 是質數，只要 $\varphi(n)$ 不是它的倍數就行。

### 實作上的三個坑

1. **負數輸出**：(f) 的問題在實作中很常見，C 語言尤其要小心 `%` 對負數的行為。
2. **不存在的反元素**：必須檢查 $r_0 = 1$，否則會回傳一個錯誤的數字而不是報錯。
   Python 的 `pow(a, -1, m)` 在不存在時丟出 `ValueError`，這是正確的設計。
3. **時間旁通道**：演算法的步數依賴輸入。若 $a$ 是秘密（例如 ECDSA 的 nonce $k$），
   應改用費馬小定理 $a^{-1} = a^{p-2} \bmod p$（見 [費馬小定理](../Fermat_Euler/Fermat_Little_Theorem.md)）或常數時間的二進位演算法。

### 程式思維

```python
def inverse_mod(a, m):
    """投影片 p.31，補上最後的取模。"""
    r0, x0, r1, x1 = a, 1, m, 0
    while r1 != 0:
        q = r0 // r1
        r0, x0, r1, x1 = r1, x1, r0 - q * r1, x0 - q * x1
    if r0 != 1:
        return None                         # No Inverse（證明 (a)）
    return x0 % m if m > 1 else 1           # 證明 (d) 的註

assert inverse_mod(160, 841) == 205 == pow(160, -1, 841)
assert (205 * 7) % 841 == 594               # 證明 (e)
assert inverse_mod(3, 7) == 5               # 證明 (f)：不取模會得到 -2
assert inverse_mod(6, 15) is None
```
