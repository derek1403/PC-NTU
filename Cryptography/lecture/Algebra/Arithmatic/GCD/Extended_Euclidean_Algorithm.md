# Extended Euclidean Algorithm (擴展歐幾里得演算法)

+++

## 證明目標:

`Arithmetic.pdf` p.14–18。在跑歐幾里得演算法的同時，**順手記帳**：
每一個餘數都寫成 $a$ 與 $b$ 的整係數組合。跑到最後，gcd 自然也是一個組合。

* (a)(b) 投影片 p.16 的歸納法：對每個 $k$，第 $k$ 個餘數都是 $a, b$ 的組合：

$$r_k = a x_k + b y_k \qquad \text{for each } k \in \mathbf{N}$$

* (c) **定理（貝祖係數存在）**：對任意不全為零的 $a, b \in \mathbf{Z}$，存在 $x, y \in \mathbf{Z}$ 使

$$ax + by = \gcd(a, b)$$

* (d) 驗證投影片的例子：$a = 100$、$b = 35$：

$$\gcd(100, 35) = 5 = \left(-1\right) \times 100 + 3 \times 35$$

* (e) 投影片 p.18 的矩陣版本與 (a)(b) 的遞迴是同一個演算法。

* $a,\ b$ : 輸入整數 (The input integers) $[a, b \in \mathbf{Z}]$
* $r_k$ : 第 $k$ 個餘數 (The $k$-th remainder) $[r_k \in \mathbf{N}]$
* $q_k$ : 第 $k$ 個商 (The $k$-th quotient) $[q_k \in \mathbf{Z}]$
* $x_k,\ y_k$ : 第 $k$ 組貝祖係數 (The $k$-th pair of Bézout coefficients) $[x_k, y_k \in \mathbf{Z}]$
* 註（**投影片漏條件**）：投影片 p.16 寫「Given $a, b \in \mathbf{Z}$」，但 (c) 需要 **$a, b$ 不全為零**，gcd 才有定義。
  另外遞迴裡的 $q_{i+1} = \left\lfloor r_{i-1}/r_i \right\rfloor$ 只有在 $r_i > 0$ 時才讓 $r_{i+1}$ 成為真正的餘數；
  本檔先處理 $b > 0$，再在【證明 (c)】用正負號把一般情形化歸過來。
* 註：投影片 p.14 的應用（$b = p$ 為質數時 $x$ 就是 $a$ 的模反元素）見 [模反元素](../Congruence/Modular_Inverse.md)。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [取模函數 (Modular function)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/Division/Modular_Function.html#assumptions-preliminaries)：** 已於本章 [取模函數](../Division/Modular_Function.md)【定義 1】給出，此處直接引用

  $$n \bmod m = n - \left\lfloor \frac{n}{m} \right\rfloor m \qquad \left(m \in \mathbf{P}\right)$$

  * $n$ : 被除數 (The dividend) $[n \in \mathbf{Z}]$
  * $m$ : 模數 (The modulus) $[m \in \mathbf{P}]$

* **【已知 2】 [歐幾里得演算法的正確性 (Correctness of the Euclidean algorithm)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/GCD/Euclidean_Algorithm.html#d-proof-that-the-output-is-the-gcd)：** 已於本章 [歐幾里得演算法](Euclidean_Algorithm.md)【定義 1】【證明 (c)(d)】給出並證明，此處直接引用不再重證。
  設 $b > 0$，狀態序列 $\left(a_0, b_0\right) = \left(a, b\right)$、$\left(a_{j+1}, b_{j+1}\right) = \left(b_j,\ a_j \bmod b_j\right)$ 必在有限輪 $n$ 後停在 $b_n = 0$，且

  $$a_n = \gcd(a, b)$$

  * $a_j,\ b_j$ : 歐幾里得演算法第 $j$ 輪的狀態 (The state after round $j$) $[a_j \in \mathbf{Z},\ b_j \in \mathbf{N}]$
  * $n$ : 總輪數 (The number of rounds) $[n \in \mathbf{N}]$

* **【已知 3】 [最大公因數的基本命題 (Basic propositions of the gcd)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/GCD/Greatest_Common_Divisor.html#d-proof-that-the-gcd-ignores-signs-and-order)：** 已於本章 [最大公因數](Greatest_Common_Divisor.md)【證明 (c)(d)】完整證明，此處直接引用不再重證

  * (a) 正負號無關：

    $$\gcd(a, b) = \gcd\left(a, \left|b\right|\right)$$

  * (b) 與零的 gcd：

    $$\gcd(a, 0) = \left|a\right| \qquad \left(a \neq 0\right)$$

  * $a,\ b$ : 不全為零的整數 (Integers, not both zero) $[a, b \in \mathbf{Z}]$

* **【定義 1】 擴展歐幾里得的遞迴 (The extended Euclidean recursion)：** 投影片 p.16 的四條遞迴式，設 $b > 0$

  * (a) 起始值：

    $$\begin{gather*}
    \left(r_0, x_0, y_0\right) &\overset{\text{def}}{=}& \left(a, 1, 0\right) \\
    \left(r_1, x_1, y_1\right) &\overset{\text{def}}{=}& \left(b, 0, 1\right)
    \end{gather*}$$

  * (b) 遞迴（當 $r_i \neq 0$ 時，$i \ge 1$）：

    $$\begin{gather*}
    q_{i+1} &\overset{\text{def}}{=}& \left\lfloor \frac{r_{i-1}}{r_i} \right\rfloor \\
    r_{i+1} &\overset{\text{def}}{=}& r_{i-1} - r_i\, q_{i+1} \\
    x_{i+1} &\overset{\text{def}}{=}& x_{i-1} - x_i\, q_{i+1} \\
    y_{i+1} &\overset{\text{def}}{=}& y_{i-1} - y_i\, q_{i+1}
    \end{gather*}$$

  * $r_i,\ x_i,\ y_i,\ q_i$ : 見證明目標的符號清單 (See the symbol list above) $[\mathbf{Z}]$
  * $a$ : 輸入整數 (The first input) $[a \in \mathbf{Z}]$
  * $b$ : 輸入正整數 (The second input) $[b \in \mathbf{P}]$
  * $i$ : 步數指標 (Step index) $[i \in \mathbf{P}]$
  * 註：$r, x, y$ 三條遞迴**長得一模一樣**，都是「前前項 $-$ 前項 $\times$ 商」。
    這個結構就是證明能成立的原因：組合關係 $r = ax + by$ 是線性的，會被同一個運算保持。

* **【假設 1】 歸納假設 (Induction hypothesis)：** 【證明 (b)】對 $i$ 做（兩步）歸納時的假設。設前兩項都已是組合

  $$r_{i-1} = a x_{i-1} + b y_{i-1}, \qquad r_i = a x_i + b y_i$$

  * $r_{i-1},\ r_i$ : 前兩個餘數 (The previous two remainders) $[r_{i-1}, r_i \in \mathbf{N}]$
  * $x_{i-1},\ x_i,\ y_{i-1},\ y_i$ : 對應的係數 (The corresponding coefficients) $[\mathbf{Z}]$

* **【推導 1】 餘數序列就是歐幾里得演算法的狀態序列 (The remainders reproduce the Euclidean states)：** 【證明 (c)】要用。
  因為 $r_i > 0$ 時 $r_{i+1}$ 恰好是真正的餘數

  $$\begin{gather*}
  r_{i+1} &\overset{\text{定義 1(b)}}{=}& r_{i-1} - \left\lfloor \frac{r_{i-1}}{r_i} \right\rfloor r_i \\
  r_{i+1} &\overset{\text{已知 1}}{=}& r_{i-1} \bmod r_i
  \end{gather*}$$

  於是與【已知 2】的 $\left(a_j, b_j\right)$ 逐項對應（對 $j$ 歸納，起點 $\left(a_0, b_0\right) = \left(r_0, r_1\right)$）：

  $$\left(a_j, b_j\right) = \left(r_j, r_{j+1}\right) \qquad \text{for all } j$$

  * $r_i$ : 第 $i$ 個餘數 (The $i$-th remainder) $[r_i \in \mathbf{N}]$
  * $a_j,\ b_j$ : 歐幾里得演算法的狀態 (The Euclidean states) $[a_j \in \mathbf{Z},\ b_j \in \mathbf{N}]$
  * $j$ : 輪數指標 (Round index) $[j \in \mathbf{N}]$
  * 註：由此 $r_1 > r_2 > \cdots \ge 0$，而且【已知 2】的「停在 $b_n = 0$、$a_n = \gcd$」翻譯成
    投影片 p.16 最後一行的「$r_{n+1} = 0$ and $r_n = \gcd(a, b)$」。

+++

## 證明:

以下 (a)(b) 設 $b > 0$。

### (a) proof of the base case for the two starting remainders

$$\begin{gather*}
a x_0 + b y_0 &\overset{\text{定義 1(a)}}{=}& a \times 1 + b \times 0 \\
&=& a \\
&\overset{\text{定義 1(a)}}{=}& r_0
\end{gather*}$$

$$\begin{gather*}
a x_1 + b y_1 &\overset{\text{定義 1(a)}}{=}& a \times 0 + b \times 1 \\
&=& b \\
&\overset{\text{定義 1(a)}}{=}& r_1
\end{gather*}$$

### (b) proof of the inductive step for the next remainder

把【假設 1】代入 $r_{i+1}$ 的遞迴，按 $a$ 與 $b$ 重新整理，括號內恰好是 $x_{i+1}$ 與 $y_{i+1}$ 的遞迴：

$$\begin{gather*}
r_{i+1} &\overset{\text{定義 1(b)}}{=}& r_{i-1} - r_i\, q_{i+1} \\
&\overset{\text{假設 1}}{=}& \left(a x_{i-1} + b y_{i-1}\right) - \left(a x_i + b y_i\right) q_{i+1} \\
&=& a\left(x_{i-1} - x_i\, q_{i+1}\right) + b\left(y_{i-1} - y_i\, q_{i+1}\right) \\
&\overset{\text{定義 1(b)}}{=}& a x_{i+1} + b y_{i+1}
\end{gather*}$$

由 (a)(b) 與歸納法，對每個 $k$ 都有 $r_k = a x_k + b y_k$，與投影片一致。

### (c) proof of the existence of Bezout coefficients

**情形一：$b > 0$。** 由【推導 1】與【已知 2】，遞迴停在 $r_{n+1} = 0$，且 $r_n = \gcd(a, b)$；再套【證明 (a)(b)】：

$$\begin{gather*}
\gcd(a, b) &\overset{\text{已知 2}}{=}& a_n \\
&\overset{\text{推導 1}}{=}& r_n \\
&\overset{\text{證明 (a)(b)}}{=}& a x_n + b y_n
\end{gather*}$$

取 $x = x_n$、$y = y_n$ 即可。

**情形二：$b < 0$。** 對 $\left(a, \left|b\right|\right)$ 用情形一得 $x', y'$，再把負號吸進 $y$：

$$\begin{gather*}
\gcd(a, b) &\overset{\text{已知 3(a)}}{=}& \gcd\left(a, \left|b\right|\right) \\
&=& a x' + \left|b\right| y' \\
&=& a x' + b\left(-y'\right)
\end{gather*}$$

**情形三：$b = 0$。** 則 $a \neq 0$，取 $x = \pm 1$（與 $a$ 同號）、$y = 0$：

$$\begin{gather*}
\gcd(a, 0) &\overset{\text{已知 3(b)}}{=}& \left|a\right| \\
&=& a \times \left(\pm 1\right) + 0 \times 0
\end{gather*}$$

三種情形都找得到 $x, y$，定理得證。

### (d) verify the example of the pair one hundred and thirty-five

依【定義 1】逐行填表（與投影片 p.17 的表相同）：

| $k$ | $r_k$ | $q_k$ | $x_k$ | $y_k$ |
|---|---|---|---|---|
| 0 | 100 | | 1 | 0 |
| 1 | 35 | | 0 | 1 |
| 2 | 30 | 2 | 1 | $-2$ |
| 3 | 5 | 1 | $-1$ | 3 |
| 4 | 0 | 6 | | |

逐格的計算：

$$\begin{gather*}
q_2 &\overset{\text{定義 1(b)}}{=}& \left\lfloor 100 / 35 \right\rfloor \\
q_2 &=& 2 \\
r_2 &\overset{\text{定義 1(b)}}{=}& 100 - 35 \times 2 \\
r_2 &=& 30 \\
x_2 &\overset{\text{定義 1(b)}}{=}& 1 - 0 \times 2 \\
x_2 &=& 1 \\
y_2 &\overset{\text{定義 1(b)}}{=}& 0 - 1 \times 2 \\
y_2 &=& -2 \\
q_3 &\overset{\text{定義 1(b)}}{=}& \left\lfloor 35 / 30 \right\rfloor \\
q_3 &=& 1 \\
r_3 &\overset{\text{定義 1(b)}}{=}& 35 - 30 \times 1 \\
r_3 &=& 5 \\
x_3 &\overset{\text{定義 1(b)}}{=}& 0 - 1 \times 1 \\
x_3 &=& -1 \\
y_3 &\overset{\text{定義 1(b)}}{=}& 1 - \left(-2\right) \times 1 \\
y_3 &=& 3 \\
q_4 &\overset{\text{定義 1(b)}}{=}& \left\lfloor 30 / 5 \right\rfloor \\
q_4 &=& 6 \\
r_4 &\overset{\text{定義 1(b)}}{=}& 30 - 5 \times 6 \\
r_4 &=& 0
\end{gather*}$$

$r_4 = 0$ 停止，gcd 是 $r_3$。驗算組合：

$$\begin{gather*}
\gcd(100, 35) &\overset{\text{證明 (c)}}{=}& r_3 \\
&\overset{\text{證明 (b)}}{=}& 100 \times x_3 + 35 \times y_3 \\
&=& 100 \times \left(-1\right) + 35 \times 3 \\
&=& -100 + 105 \\
&=& 5
\end{gather*}$$

與投影片 p.15、p.17 一致（$x = -1$、$y = 3$）。

* 註：投影片 p.15 用的是**倒推法**：$5 = 35 - 30 = 35 - \left(100 - 2 \times 35\right) = \left(-1\right) \times 100 + 3 \times 35$。
  倒推法要先跑完再回頭代，本檔的遞迴則是**邊跑邊記帳**，只需常數額外空間 —— 實作上都用後者。

### (e) proof that the matrix version is the same recursion

投影片 p.18 把相鄰兩列 $\left(r, x, y\right)$ 疊成 $2 \times 3$ 矩陣，每一輪左乘一個 $2 \times 2$ 矩陣。展開矩陣乘法：

$$\begin{bmatrix} 0 & 1 \\ 1 & -q_{i+1} \end{bmatrix}
\begin{bmatrix} r_{i-1} & x_{i-1} & y_{i-1} \\ r_i & x_i & y_i \end{bmatrix}
= \begin{bmatrix} r_i & x_i & y_i \\ r_{i-1} - q_{i+1} r_i & x_{i-1} - q_{i+1} x_i & y_{i-1} - q_{i+1} y_i \end{bmatrix}$$

右邊第二列逐項套【定義 1(b)】：

$$\begin{bmatrix} r_i & x_i & y_i \\ r_{i-1} - q_{i+1} r_i & x_{i-1} - q_{i+1} x_i & y_{i-1} - q_{i+1} y_i \end{bmatrix}
\overset{\text{定義 1(b)}}{=} \begin{bmatrix} r_i & x_i & y_i \\ r_{i+1} & x_{i+1} & y_{i+1} \end{bmatrix}$$

第一列把舊的第二列搬上來，第二列就是【定義 1(b)】的三條遞迴。起始矩陣
$\left[\begin{smallmatrix} a & 1 & 0 \\ b & 0 & 1 \end{smallmatrix}\right]$ 就是【定義 1(a)】。
迴圈在第二列的 $r$ 變成 $0$ 時停下，此時第一列是 $\left(r_n, x_n, y_n\right)$，
回傳 $\left[d, x, y\right] = \left[r_0, x_0, y_0\right]$（矩陣記號下的第一列）即【證明 (c)】的結論。

+++

## 意義與密碼學關聯 (Interpretation and Relevance to Cryptography)

### 為什麼要「擴展」：gcd 本身不夠用

光知道 $\gcd(a, b) = 1$ 只告訴你「$a$ 在模 $b$ 下可逆」，但**沒告訴你反元素是誰**。
擴展版給出 $ax + by = 1$，兩邊模 $b$：

$$a x \equiv 1 \pmod{b}$$

**$x$ 就是 $a$ 的模反元素**（投影片 p.14 的 Application）。這是整個公鑰密碼學最常呼叫的子程序之一：

| 場合 | 算什麼 |
|---|---|
| RSA 金鑰產生 | 私鑰 $d = e^{-1} \bmod \varphi(n)$ |
| RSA-CRT | 係數 `iqmp` $= q^{-1} \bmod p$ |
| ECC 點加法（仿射座標） | 斜率裡的分母反元素 $\left(x_2 - x_1\right)^{-1} \bmod p$ |
| [中國剩餘定理](../CRT/Chinese_Remainder_Theorem.md) | 各分量的 $M_i^{-1} \bmod m_i$ |

### 不變量的威力

【證明 (b)】沒有用到 $q_{i+1}$ 的任何性質 —— 它可以是**任意整數**，
組合關係 $r = ax + by$ 照樣被保持。取地板只是為了讓 $r$ 變小、演算法會結束。
這種「先找一個被每一步保持的不變量，再證它會結束」的寫法，是證明演算法正確性的標準範式。

### 旁通道的隱患

擴展歐幾里得的輪數與商的大小**取決於輸入**。若用它計算與秘密有關的反元素
（例如 ECDSA 的 $k^{-1}$），執行時間會洩漏 $k$ 的資訊。
實務上的常數時間實作改用費馬小定理 $k^{-1} = k^{p-2} \bmod p$
（見 [費馬小定理](../Fermat_Euler/Fermat_Little_Theorem.md)），或特別設計的常數時間 gcd 演算法（如 Bernstein–Yang）。

### 程式思維

```python
def ext_gcd(a, b):
    """投影片 p.18 矩陣版：(r0,x0,y0),(r1,x1,y1) 兩列滾動。b > 0。"""
    r0, x0, y0, r1, x1, y1 = a, 1, 0, b, 0, 1
    while r1 != 0:
        q = r0 // r1
        r0, x0, y0, r1, x1, y1 = r1, x1, y1, r0 - q*r1, x0 - q*x1, y0 - q*y1
        assert r1 == a*x1 + b*y1               # 證明 (b) 的不變量
    return r0, x0, y0

assert ext_gcd(100, 35) == (5, -1, 3)
```
