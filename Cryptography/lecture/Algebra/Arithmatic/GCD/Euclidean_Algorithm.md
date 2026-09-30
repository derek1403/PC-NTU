# Euclidean Algorithm (歐幾里得演算法)

+++

## 證明目標:

`Arithmetic.pdf` p.10–12。人類最古老、至今仍在每一台電腦裡天天執行的演算法。
投影片給了迴圈版與遞迴版，並指出 $\gcd(a,b) = \gcd(b, a \bmod b) = \cdots$ 是**迴圈不變量**。
本檔把「不變量」「終止」「輸出正確」三件事分開證明。

演算法（迴圈版，投影片 p.12 左）：

```text
Input : a, b ∈ Z，不全為零
If b = 0 Then gcd = |a|
Else
    While b ≠ 0 do:  c = b;  b = a mod b;  a = c
    gcd = a
Return gcd
```

* (a)(b) **迴圈不變量**：每一輪之後 gcd 不變（歸納法的基底與歸納步驟）：

$$\gcd\left(a_i, b_i\right) = \gcd(a, b) \qquad \text{for every round } i$$

* (c) **終止性**：$b_i$ 嚴格遞減，至多 $b$ 輪就變成 $0$。
* (d) **輸出正確**：結束時的 $a_n$ 就是 $\gcd(a,b)$；$b = 0$ 分支輸出 $\left|a\right|$ 也正確。
* (e) 驗證投影片的例子：

$$\gcd(325, 234) = 13$$

* $a,\ b$ : 輸入整數 (The input integers) $[a, b \in \mathbf{Z}]$
* $a_i,\ b_i$ : 第 $i$ 輪結束時兩個變數的值 (The values of the two variables after round $i$) $[a_i, b_i \in \mathbf{Z}]$
* $n$ : 總輪數 (The number of rounds) $[n \in \mathbf{N}]$
* 註（**投影片漏條件**）：投影片的輸入允許 $b < 0$，但 $a \bmod b$ 只對 $b > 0$ 有定義
  （[取模函數](../Division/Modular_Function.md)【定義 1】）。
  本檔的分析假設 **$b \ge 0$**；負數輸入先用 $\gcd(a,b) = \gcd\left(\left|a\right|, \left|b\right|\right)$ 轉成非負再跑。
  若照 Python 的 `%`（負模數給負餘數）硬跑，迴圈版可能輸出**負的** gcd，例如 $\left(6, -4\right)$ 會得到 $-2$。
* 註：遞迴版（投影片 p.12 右）的每一次遞迴呼叫恰好對應迴圈版的一輪，論證完全相同，不另證。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [GCD 的平移不變性系理 (Corollary of shift invariance)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/GCD/GCD_Shift_Invariance.html#d-proof-of-the-corollary-using-the-remainder)：** 已於本章 [GCD 的平移不變性](GCD_Shift_Invariance.md)【證明 (d)】完整證明，此處直接引用不再重證

  $$b > 0 \quad \Longrightarrow \quad \gcd(a, b) = \gcd\left(b,\ a \bmod b\right)$$

  * $a$ : 任意整數 (An arbitrary integer) $[a \in \mathbf{Z}]$
  * $b$ : 正整數 (A positive integer) $[b \in \mathbf{P}]$

* **【已知 2】 [最大公因數的基本命題 (Basic propositions of the gcd)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/GCD/Greatest_Common_Divisor.html#c-proof-that-the-gcd-of-a-with-itself-and-with-zero-is-a)：** 已於本章 [最大公因數](Greatest_Common_Divisor.md)【證明 (c)(d)】完整證明，此處直接引用不再重證

  * (a) 與零的 gcd：

    $$\gcd(a, 0) = a \qquad \left(a \in \mathbf{P}\right)$$

  * (b) 正負號無關：

    $$\gcd(a, b) = \gcd\left(\left|a\right|, \left|b\right|\right)$$

  * $a,\ b$ : 不全為零的整數 (Integers, not both zero) $[a, b \in \mathbf{Z}]$

* **【已知 3】 [餘數的範圍 (Range of the remainder)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/Division/Modular_Function.html#a-proof-that-the-remainder-lies-between-zero-and-the-modulus)：** 已於本章 [取模函數](../Division/Modular_Function.md)【證明 (a)】完整證明，此處直接引用不再重證

  $$0 \le a \bmod b < b \qquad \left(b \in \mathbf{P}\right)$$

  * $a$ : 被除數 (The dividend) $[a \in \mathbf{Z}]$
  * $b$ : 模數 (The modulus) $[b \in \mathbf{P}]$

* **【已知 4】 [非負整數不能無限遞減 (No infinite descent in the non-negative integers)](https://mathworld.wolfram.com/WellOrderingPrinciple.html)：** 良序原理的直接推論，本章直接引用不再重證

  $$b_0 > b_1 > b_2 > \cdots \ge 0 \ \text{為整數} \quad \Longrightarrow \quad \text{數列至多有 } b_0 + 1 \ \text{項}$$

  * $b_i$ : 嚴格遞減的非負整數數列 (A strictly decreasing sequence of non-negative integers) $[b_i \in \mathbf{N}]$

* **【定義 1】 演算法的狀態序列 (The state sequence of the algorithm)：** 迴圈每跑一輪，$\left(a, b\right)$ 的更新規則

  $$\begin{gather*}
  \left(a_0, b_0\right) &\overset{\text{def}}{=}& \left(a, b\right) \\
  \left(a_{i+1}, b_{i+1}\right) &\overset{\text{def}}{=}& \left(b_i,\ a_i \bmod b_i\right) \qquad \text{(僅當 } b_i > 0 \text{)}
  \end{gather*}$$

  * $a_i,\ b_i$ : 第 $i$ 輪結束時的值 (The values after round $i$) $[a_i \in \mathbf{Z},\ b_i \in \mathbf{N}]$
  * $a,\ b$ : 輸入 (The inputs) $[a \in \mathbf{Z},\ b \in \mathbf{P}]$
  * $i$ : 輪數指標 (Round index) $[i \in \mathbf{N}]$
  * 註：這正是投影片 `c = b; b = a mod b; a = c` 三行的效果 —— $c$ 只是暫存舊的 $b$。

* **【假設 1】 歸納假設 (Induction hypothesis)：** 【證明 (b)】對輪數 $i$ 做歸納時的假設。
  設第 $i$ 輪之後不變量成立

  $$\gcd\left(a_i, b_i\right) = \gcd(a, b)$$

  * $a_i,\ b_i$ : 第 $i$ 輪結束時的值 (The values after round $i$) $[a_i \in \mathbf{Z},\ b_i \in \mathbf{N}]$
  * $i$ : 輪數指標 (Round index) $[i \in \mathbf{N}]$

+++

## 證明:

以下 (a)–(d) 皆設 $b > 0$（$b = 0$ 的分支在 (d) 末尾單獨處理）。

### (a) proof of the base case of the loop invariant

$$\begin{gather*}
\gcd\left(a_0, b_0\right) &\overset{\text{定義 1}}{=}& \gcd(a, b)
\end{gather*}$$

### (b) proof of the inductive step of the loop invariant

設第 $i$ 輪之後 $b_i > 0$（否則迴圈已經停了，沒有第 $i+1$ 輪）：

$$\begin{gather*}
\gcd\left(a_{i+1}, b_{i+1}\right) &\overset{\text{定義 1}}{=}& \gcd\left(b_i,\ a_i \bmod b_i\right) \\
&\overset{\text{已知 1}}{=}& \gcd\left(a_i, b_i\right) \\
&\overset{\text{假設 1}}{=}& \gcd(a, b)
\end{gather*}$$

由 (a)(b) 與歸納法，不變量對每一輪都成立 —— 這就是投影片說的 loop invariant。

### (c) proof that the algorithm terminates

每一輪新的 $b$ 是舊的 $a \bmod b$，嚴格小於舊的 $b$：

$$\begin{gather*}
b_{i+1} &\overset{\text{定義 1}}{=}& a_i \bmod b_i \\
0 &\overset{\text{已知 3}}{\le}& b_{i+1} \\
b_{i+1} &\overset{\text{已知 3}}{<}& b_i \\
b_0 > b_1 > b_2 > \cdots &\overset{\text{已知 4}}{\Longrightarrow}& \text{至多 } b + 1 \ \text{項}
\end{gather*}$$

數列不能永遠延續，而唯一讓它停下的方式是某個 $b_n = 0$（迴圈條件失敗）。故演算法在 $n \le b$ 輪內結束。

### (d) proof that the output is the gcd

結束時 $b_n = 0$，而 $a_n = b_{n-1} > 0$（上一輪還在跑，$b_{n-1} > 0$）。把不變量套在第 $n$ 輪：

$$\begin{gather*}
\gcd(a, b) &\overset{\text{證明 (b)}}{=}& \gcd\left(a_n, b_n\right) \\
&=& \gcd\left(a_n, 0\right) \\
&\overset{\text{已知 2(a)}}{=}& a_n
\end{gather*}$$

即投影片的 `Set gcd = a`。

**$b = 0$ 的分支**：此時 $a \neq 0$，投影片輸出 $\left|a\right|$：

$$\begin{gather*}
\gcd(a, 0) &\overset{\text{已知 2(b)}}{=}& \gcd\left(\left|a\right|, 0\right) \\
&\overset{\text{已知 2(a)}}{=}& \left|a\right|
\end{gather*}$$

兩個分支的輸出都正確。

### (e) verify the example of three hundred twenty-five and two hundred thirty-four

依【定義 1】逐輪計算（每一行的商與餘數見投影片 p.10 右的直式）：

$$\begin{gather*}
\gcd(325, 234) &\overset{\text{已知 1}}{=}& \gcd(234,\ 325 \bmod 234) \qquad \text{(} 325 = 1 \times 234 + 91 \text{)} \\
&=& \gcd(234, 91) \\
&\overset{\text{已知 1}}{=}& \gcd(91,\ 234 \bmod 91) \qquad \text{(} 234 = 2 \times 91 + 52 \text{)} \\
&=& \gcd(91, 52) \\
&\overset{\text{已知 1}}{=}& \gcd(52,\ 91 \bmod 52) \qquad \text{(} 91 = 1 \times 52 + 39 \text{)} \\
&=& \gcd(52, 39) \\
&\overset{\text{已知 1}}{=}& \gcd(39,\ 52 \bmod 39) \qquad \text{(} 52 = 1 \times 39 + 13 \text{)} \\
&=& \gcd(39, 13) \\
&\overset{\text{已知 1}}{=}& \gcd(13,\ 39 \bmod 13) \qquad \text{(} 39 = 3 \times 13 + 0 \text{)} \\
&=& \gcd(13, 0) \\
&\overset{\text{已知 2(a)}}{=}& 13
\end{gather*}$$

共 $5$ 輪，與投影片一致。

+++

## 意義與密碼學關聯 (Interpretation and Relevance to Cryptography)

### 歐幾里得與《幾何原本》

投影片 p.11 介紹了歐幾里得（約公元前 325–265 年），「幾何之父」。
《幾何原本》除了幾何，也收錄了數論結果 —— **歐幾里得引理**（通往 [算術基本定理](../Factorization/Fundamental_Theorem_of_Arithmetic.md)）
與**本檔的演算法**。兩千三百年後，它仍是求 gcd 的標準方法。

### 為什麼它快：對數步數

【證明 (c)】只給出很粗的界 $n \le b$。實際上它快得多：每**兩輪** $b$ 至少減半
（若 $b_{i+1} \le b_i / 2$ 則顯然；否則 $b_{i+2} = b_i \bmod b_{i+1} = b_i - b_{i+1} < b_i/2$）。
所以輪數是 $O\!\left(\log b\right)$ —— 對 $2048$ 位元的 RSA 模數，大約只要**幾千輪**。
最壞情況發生在相鄰的 Fibonacci 數上（Lamé 定理）。

對比：**分解**一個 $2048$ 位元的數，目前最好的演算法也需要天文數字的時間。
「gcd 容易、分解困難」的不對稱，是公鑰密碼能存在的原因之一。

### 密碼學用途

| 用途 | 算什麼 |
|---|---|
| RSA 金鑰產生 | 檢查 $\gcd\left(e, \varphi(n)\right) = 1$，確保私鑰存在 |
| RSA 弱金鑰偵測 | 對大量公鑰兩兩算 $\gcd\left(n_1, n_2\right)$，找共用質因數 |
| 模反元素 | [擴展歐幾里得演算法](Extended_Euclidean_Algorithm.md) 的副產品 |

### 程式思維

```python
def euclid(a, b):
    """投影片 p.12 迴圈版；先轉非負，避開負模數的問題（見證明目標的註）。"""
    a, b = abs(a), abs(b)
    assert a != 0 or b != 0
    while b != 0:          # 不變量：gcd(a, b) 不變（證明 (a)(b)）
        a, b = b, a % b    # b 嚴格遞減（證明 (c)）
    return a               # gcd(a, 0) = a（證明 (d)）

assert euclid(325, 234) == 13
assert euclid(-6, 4) == 2 and euclid(6, -4) == 2 and euclid(0, -7) == 7
```
