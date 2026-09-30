# Chinese Remainder Algorithm (中國剩餘演算法)

+++

## 證明目標:

`Arithmetic.pdf` p.42，以及 p.40 的「Proof 1: Induction on $r$」。
[高斯公式](Chinese_Remainder_Theorem.md) 一次處理所有方程；本檔的演算法則**每次合併最後兩條**，
把 $r$ 條方程縮成 $r - 1$ 條，遞迴到只剩一條。

演算法（投影片 p.42）：

```text
Function CRA(a, m, r)
    If r = 1 Then CRA = a_1
    Else
        t       = m_{r-1}^{-1} (a_r - a_{r-1}) mod m_r
        a_{r-1} = a_{r-1} + t m_{r-1}
        m_{r-1} = m_{r-1} m_r
        CRA     = CRA(a, m, r-1)
    End If
```

* (a)(b) **正確性**（對 $r$ 歸納：基底 + 歸納步驟）：若 $m_1, \dots, m_r$ 兩兩互質，則

$$\mathrm{CRA}\left(\mathbf{a}, \mathbf{m}, r\right) \equiv a_i \pmod{m_i} \qquad \text{for all } 1 \le i \le r$$

* (c) 以《孫子算經》的例子追蹤一次執行：

$$\mathrm{CRA}\left(\left(2, 3, 2\right), \left(3, 5, 7\right), 3\right) = 23$$

* $\mathbf{a} = \left(a_1, \dots, a_r\right)$ : 餘數向量 (The vector of residues) $[a_i \in \mathbf{Z}]$
* $\mathbf{m} = \left(m_1, \dots, m_r\right)$ : 模數向量，兩兩互質 (The vector of pairwise coprime moduli) $[m_i \in \mathbf{P}]$
* $r$ : 目前的方程式個數 (The current number of congruences) $[r \in \mathbf{P}]$
* $t$ : 合併時的修正量 (The correction term in a merge) $[t \in \left\{0, \dots, m_r - 1\right\}]$
* 註：每一次合併就是一次 [兩個模數的中國剩餘定理](Two_Moduli_CRT.md)（Garner 形式），
  把 $\left(a_{r-1}, m_{r-1}\right)$ 與 $\left(a_r, m_r\right)$ 換成一條等價的 $\left(a', m_{r-1} m_r\right)$。
* 註：若一開始 $0 \le a_i < m_i$，則每次合併後的 $a' = a_{r-1} + t\, m_{r-1} < m_{r-1} + \left(m_r - 1\right) m_{r-1} = m_{r-1} m_r$，
  所以最終輸出自動落在 $\left[0, M\right)$，不必再取模。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [兩個模數的中國剩餘定理 (CRT for two moduli)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/CRT/Two_Moduli_CRT.html#c-proof-that-the-whole-congruence-class-solves-the-system)：** 已於本章 [兩個模數的中國剩餘定理](Two_Moduli_CRT.md)【證明 (a)(c)】完整證明，此處直接引用不再重證。設 $n_1 \perp n_2$、$s = n_1^{-1}\left(b_2 - b_1\right) \bmod n_2$、$b' = b_1 + n_1 s$

  * (a) $b'$ 滿足兩條：

    $$b' \equiv b_1 \pmod{n_1}, \qquad b' \equiv b_2 \pmod{n_2}$$

  * (b) 與 $b'$ 模 $n_1 n_2$ 同餘的數也滿足兩條：

    $$z \equiv b' \pmod{n_1 n_2} \quad \Longrightarrow \quad z \equiv b_1 \pmod{n_1},\ \ z \equiv b_2 \pmod{n_2}$$

  * $n_1,\ n_2$ : 互質的模數 (Coprime moduli) $[n_1, n_2 \in \mathbf{P}]$
  * $b_1,\ b_2$ : 給定的餘數 (Prescribed residues) $[b_1, b_2 \in \mathbf{Z}]$
  * $s$ : 修正量 (The correction term) $[s \in \mathbf{Z}]$
  * $b'$ : 合併後的餘數 (The merged residue) $[b' \in \mathbf{Z}]$
  * $z$ : 任意整數 (An arbitrary integer) $[z \in \mathbf{Z}]$

* **【已知 2】 [互質對乘法封閉 (Coprimality is closed under products)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/Factorization/Relatively_Prime.html#b-proof-that-coprimality-to-a-modulus-is-closed-under-products)：** 已於本章 [互質](../Factorization/Relatively_Prime.md)【證明 (b)】完整證明，此處直接引用不再重證

  $$u \perp w,\ \ v \perp w \quad \Longrightarrow \quad uv \perp w$$

  * $u,\ v,\ w$ : 正整數 (Positive integers) $[u, v, w \in \mathbf{P}]$

* **【定義 1】 一次合併 (One merge step)：** 投影片 Else 分支的三行，把最後兩條換成一條

  $$\begin{gather*}
  t &\overset{\text{def}}{=}& m_{r-1}^{-1}\left(a_r - a_{r-1}\right) \bmod m_r \\
  a' &\overset{\text{def}}{=}& a_{r-1} + t\, m_{r-1} \\
  m' &\overset{\text{def}}{=}& m_{r-1}\, m_r
  \end{gather*}$$

  * $t$ : 修正量 (The correction term) $[t \in \mathbf{Z}]$
  * $a'$ : 合併後的餘數 (The merged residue) $[a' \in \mathbf{Z}]$
  * $m'$ : 合併後的模數 (The merged modulus) $[m' \in \mathbf{P}]$
  * 註：遞迴呼叫的新輸入是 $\left(a_1, \dots, a_{r-2}, a'\right)$ 與 $\left(m_1, \dots, m_{r-2}, m'\right)$。

* **【假設 1】 歸納假設 (Induction hypothesis)：** 【證明 (b)】對 $r$ 歸納時的假設。
  設演算法對任意 $r - 1$ 條兩兩互質的方程式都正確：輸入 $\left(c_1, \dots, c_{r-1}\right)$、$\left(n_1, \dots, n_{r-1}\right)$ 時輸出 $z$ 滿足

  $$z \equiv c_j \pmod{n_j} \qquad \text{for all } 1 \le j \le r - 1$$

  * $c_j$ : 餘數 (Residues) $[c_j \in \mathbf{Z}]$
  * $n_j$ : 兩兩互質的模數 (Pairwise coprime moduli) $[n_j \in \mathbf{P}]$
  * $z$ : 遞迴的輸出 (The output of the recursive call) $[z \in \mathbf{Z}]$

+++

## 證明:

### (a) proof of the base case with a single congruence

$r = 1$ 時直接回傳 $a_1$，而 $a_1 - a_1 = 0$ 被 $m_1$ 整除：

$$\begin{gather*}
\mathrm{CRA}\left(\mathbf{a}, \mathbf{m}, 1\right) &=& a_1 \qquad \text{(If 分支，不經合併)} \\
a_1 &\equiv& a_1 \pmod{m_1}
\end{gather*}$$

### (b) proof of the inductive step by merging the last two congruences

設 $r \ge 2$。**合併後的輸入仍然兩兩互質**：$m' = m_{r-1} m_r$ 的兩個因子都與其他每個 $m_j$ 互質：

$$\begin{gather*}
m_{r-1} \perp m_j,\ \ m_r \perp m_j &\overset{\text{已知 2}}{\Longrightarrow}& m' \perp m_j \qquad \left(j \le r - 2\right)
\end{gather*}$$

**遞迴呼叫的輸出滿足新的 $r - 1$ 條**：

$$\begin{gather*}
z &\overset{\text{假設 1}}{\equiv}& a_j \pmod{m_j} \qquad \left(j \le r-2\right) \\
z &\overset{\text{假設 1}}{\equiv}& a' \pmod{m'}
\end{gather*}$$

**再把最後一條拆回原本的兩條**：$a'$ 就是【已知 1】取 $\left(n_1, b_1\right) = \left(m_{r-1}, a_{r-1}\right)$、$\left(n_2, b_2\right) = \left(m_r, a_r\right)$ 的構造解：

$$\begin{gather*}
a' &\overset{\text{定義 1,已知 1(a)}}{=}& a_{r-1} + t\, m_{r-1} \qquad \text{(兩條都滿足)} \\
z \equiv a' \pmod{m_{r-1} m_r} &\overset{\text{已知 1(b)}}{\Longrightarrow}& z \equiv a_{r-1} \pmod{m_{r-1}},\ \ z \equiv a_r \pmod{m_r}
\end{gather*}$$

$z$ 滿足全部 $r$ 條。由 (a)(b) 與歸納法，演算法對所有 $r$ 正確。這也就是投影片的「Proof 1: Induction on $r$」。

### (c) verify a trace on the Sunzi example

輸入 $\mathbf{a} = \left(2, 3, 2\right)$、$\mathbf{m} = \left(3, 5, 7\right)$、$r = 3$。

**第一次合併**（$r = 3$，合併模 $5$ 與模 $7$）：$5^{-1} \bmod 7 = 3$（$5 \times 3 = 15 = 2 \times 7 + 1$）：

$$\begin{gather*}
t &\overset{\text{定義 1}}{=}& 3 \times \left(2 - 3\right) \bmod 7 \\
t &=& -3 \bmod 7 \\
t &=& 4 \\
a' &\overset{\text{定義 1}}{=}& 3 + 4 \times 5 \\
a' &=& 23 \\
m' &\overset{\text{定義 1}}{=}& 5 \times 7 \\
m' &=& 35
\end{gather*}$$

**第二次合併**（$r = 2$，合併模 $3$ 與模 $35$）：$3^{-1} \bmod 35 = 12$（$3 \times 12 = 36 = 35 + 1$）：

$$\begin{gather*}
t &\overset{\text{定義 1}}{=}& 12 \times \left(23 - 2\right) \bmod 35 \\
t &=& 252 \bmod 35 \\
t &=& 7 \\
a' &\overset{\text{定義 1}}{=}& 2 + 7 \times 3 \\
a' &=& 23 \\
m' &\overset{\text{定義 1}}{=}& 3 \times 35 \\
m' &=& 105
\end{gather*}$$

**$r = 1$**：回傳 $23$，與 [中國剩餘定理](Chinese_Remainder_Theorem.md)【證明 (d)】的高斯公式結果一致。

* 註：兩次合併都算出 $23$，但意義不同。第一次的 $23$ 是「模 $5$ 餘 $3$、模 $7$ 餘 $2$」的最小非負解（模 $35$）；
  第二次是從 $a_1 = 2$ 出發、加上 $3$ 的倍數去湊「模 $35$ 餘 $23$」，得到模 $105$ 的解。
  兩者數值相同，只因為 $23$ 本身恰好也 $\equiv 2 \pmod 3$ —— 模 $105$ 的最小非負解碰巧落在 $\left[0, 35\right)$ 裡。

+++

## 意義與密碼學關聯 (Interpretation and Relevance to Cryptography)

### 兩種演算法的取捨

| | 高斯公式（[中國剩餘定理](Chinese_Remainder_Theorem.md)） | 本檔（逐次合併 / Garner） |
|---|---|---|
| 反元素 | $r$ 個，模數分別是 $m_i$ | $r - 1$ 個，模數分別是 $m_r, m_{r-1}m_r, \dots$ |
| 中間量大小 | 先算出最多 $\approx M^2$ 的和再取模 | 每一步都不超過目前的乘積 |
| 預先計算 | $M_i y_i$ 可以預存，之後每次只做 $r$ 次乘加 | 反元素可以預存 |
| 適合 | 模數固定、要重複還原很多次 | 模數逐步增加、或 $r = 2$ |

$r = 2$ 時本檔的形式只要**一個**反元素，這正是 RSA-CRT 的私鑰檔只存一個 `iqmp` 的原因。

### 遞迴 = 把問題縮小一號

這個演算法是「**用已經證完的小情形去證大情形**」的程式版：
$r$ 條的正確性直接建立在 $r - 1$ 條的正確性 + 兩條的 CRT 上。
程式的遞迴結構與證明的歸納結構**一模一樣** —— 這也是為什麼【證明 (b)】幾乎只是把程式逐行翻譯成數學。

### 程式思維

```python
def cra(a, m, r=None):
    """投影片 p.42 的遞迴；為了不改動呼叫者的串列，這裡複製一份。"""
    a, m = list(a), list(m)
    r = len(a) if r is None else r
    if r == 1:
        return a[0]
    t = (pow(m[r-2], -1, m[r-1]) * (a[r-1] - a[r-2])) % m[r-1]   # 定義 1
    a[r-2] = a[r-2] + t * m[r-2]
    m[r-2] = m[r-2] * m[r-1]
    return cra(a, m, r - 1)

assert cra([2, 3, 2], [3, 5, 7]) == 23                          # 證明 (c)
assert pow(5, -1, 7) == 3 and pow(3, -1, 35) == 12
```
