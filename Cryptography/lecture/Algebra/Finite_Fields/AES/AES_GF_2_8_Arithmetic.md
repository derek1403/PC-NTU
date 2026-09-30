# AES GF(2^8) Arithmetic (AES 的 GF(2^8) 算術)

+++

## 證明目標:

`FiniteFields.pdf` p.17（「AES：$GF_{2^8}$」）與 p.24（$n = 8$ 表的第一列 $100011011$，$e = 51$）。
本檔把全章的定理落地到 AES 規格書（FIPS-197 §4）的具體運算，**每個數值都以 Python 驗算**。

* (a) 位元組即體元素：$GF(2^8) = GF(2)[x]/\left\langle m(x) \right\rangle$，$m(x) = x^8 + x^4 + x^3 + x + 1 = \texttt{0x11B}$；加法是 XOR：

$$\left\{57\right\} \oplus \left\{83\right\} = \left\{d4\right\}$$

* (b) `xtime`（乘以 $\left\{02\right\}$）：

$$\left\{02\right\} \bullet b = \begin{cases} b \ll 1, & b_7 = 0 \\ \left(b \ll 1\right) \oplus \left\{1b\right\}, & b_7 = 1 \end{cases}$$

* (c) FIPS-197 的乘法例子：

$$\left\{57\right\} \bullet \left\{83\right\} = \left\{c1\right\}, \qquad \left\{57\right\} \bullet \left\{13\right\} = \left\{fe\right\}$$

* (d) 乘法反元素（S-box 第一步）：

$$\left\{53\right\}^{-1} = \left\{ca\right\}$$

* (e) $\left\{02\right\}$ 的階是 $51$（$m$ **不是**本原多項式），$\left\{03\right\}$ 的階是 $255$（生成元）。
* (f) S-box 的一個值：

$$S\!\left(\left\{53\right\}\right) = \left\{ed\right\}$$

* $\left\{hh\right\}$ : 十六進位表示的位元組 (A byte in hexadecimal) $[\left\{00\right\}, \dots, \left\{ff\right\}]$
* $m(x)$ : AES 的模多項式 (The AES reduction polynomial) $[m \in GF(2)[x]]$
* $\oplus$ : 體加法（位元 XOR）(Field addition, bitwise XOR) $[GF(2^8)^2 \to GF(2^8)]$
* $\bullet$ : 體乘法 (Field multiplication) $[GF(2^8)^2 \to GF(2^8)]$
* $b$ : 位元組，位元 $b_7 \dots b_0$ (A byte with bits $b_7 \dots b_0$) $[b \in GF(2^8)]$
* $S$ : AES S-box (The AES substitution box) $[GF(2^8) \to GF(2^8)]$
* 註：本檔是**應用檔**：數學全部引用本章已證的定理，本檔只負責把它們對到 AES 的具體數字。
* 註：投影片沒有 AES 的數值例子；(a)–(f) 的例子取自 FIPS-197（§4.1、§4.2、§5.1.1），皆以 Python 驗算。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [GF(p^n) 的構造 (Construction of GF(p^n))](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Finite_Fields/Construction/Construction_of_GF_p_n.html#a-proof-that-the-remainder-set-is-a-field-with-p-to-the-n-elements)：** 已於本章 [GF(p^n) 的構造](../Construction/Construction_of_GF_p_n.md)【證明 (a)】完整證明，此處直接引用不再重證

  $$m \ \text{不可約},\ \deg m = 8 \quad \Longrightarrow \quad \left\{\text{次數} < 8 \text{ 的 } GF(2)[x] \text{ 多項式}\right\} \ \text{配上「相加」與「相乘後模 } m\text{」是 } 256 \text{ 元素的體}$$

* **【已知 2】 [AES 模數的不可約性與階 (Irreducibility and order of the AES modulus)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Finite_Fields/Multiplicative_Group/Order_of_a_Polynomial.html#d-verify-entries-of-the-table-of-irreducible-polynomials-over-the-binary-field)：** 已於本章 [多項式的階](../Multiplicative_Group/Order_of_a_Polynomial.md)【證明 (b)(d)】證明並驗算（投影片 p.24 表的 $n = 8$ 第一列）

  * (a) 不可約：

    $$x^8 + x^4 + x^3 + x + 1 \ \text{在 } GF(2) \text{ 上不可約}$$

  * (b) 階（等於根 $\left[x\right] = \left\{02\right\}$ 的乘法階）：

    $$\mathrm{ord}\left(x^8 + x^4 + x^3 + x + 1\right) = o\!\left(\left\{02\right\}\right) = 51$$

* **【已知 3】 [多項式的除法原理 (Division algorithm for polynomials)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Finite_Fields/Polynomial_Arithmetic/Division_Algorithm_for_Polynomials.html#a-proof-of-the-existence-of-the-quotient-and-remainder)：** 已於本章 [多項式的除法原理](../Polynomial_Arithmetic/Division_Algorithm_for_Polynomials.md)【推導 1】【證明 (a)】完整證明，此處直接引用不再重證。被除式次數恰為 $8$ 時一圈即完成：

  $$\deg a = 8 \quad \Longrightarrow \quad a \bmod m = a - m = a \oplus m$$

  * $a$ : 被除式 (The dividend) $[a \in GF(2)[x]]$

* **【已知 4】 [擴展歐幾里得演算法 (Extended Euclidean algorithm)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Finite_Fields/Polynomial_Arithmetic/Euclidean_Domain.html#e-proof-that-the-extended-euclidean-algorithm-works-for-polynomials)：** 已於本章 [歐幾里得整環](../Polynomial_Arithmetic/Euclidean_Domain.md)【證明 (e)】完整證明，此處直接引用不再重證

  $$\gcd\left(m, a\right) = 1 \quad \Longrightarrow \quad v\,m + u\,a = 1, \qquad a^{-1} = u \bmod m$$

* **【已知 5】 [有限體版費馬 (Fermat's theorem in a finite field)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Finite_Fields/Structure/Roots_of_x_q_minus_x.html#a-proof-that-every-element-satisfies-the-finite-field-version-of-fermats-theorem)：** 已於本章 [$x^q - x$ 的根](../Structure/Roots_of_x_q_minus_x.md)【證明 (a)】完整證明，此處直接引用不再重證

  $$a \in GF(2^8)^* \quad \Longrightarrow \quad a^{255} = 1, \qquad a^{-1} = a^{254}$$

* **【已知 6】 [本原元判準 (The prime divisor test)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Finite_Fields/Multiplicative_Group/Primitive_Polynomial.html#c-proof-of-the-prime-divisor-test-for-primitive-elements)：** 已於本章 [本原多項式](../Multiplicative_Group/Primitive_Polynomial.md)【證明 (c)】完整證明，此處直接引用不再重證

  $$o(a) = N \quad \Longleftrightarrow \quad a^{N/r} \neq 1 \ \text{對 } N \text{ 的每個質因數 } r$$

  * $N$ : 群的階 (The group order) $[N = 255 = 3 \cdot 5 \cdot 17]$

* **【已知 7】 [AES S-box 的仿射變換 (The affine transformation of the AES S-box)](https://csrc.nist.gov/pubs/fips/197/final)：** FIPS-197 §5.1.1 的定義，外部規格直接引用

  $$b_i' = b_i \oplus b_{(i+4) \bmod 8} \oplus b_{(i+5) \bmod 8} \oplus b_{(i+6) \bmod 8} \oplus b_{(i+7) \bmod 8} \oplus c_i, \qquad c = \left\{63\right\}$$

  * $b_i$ : 反元素的第 $i$ 位元 (Bit $i$ of the inverse) $[b_i \in GF(2)]$
  * $c_i$ : 常數 $\left\{63\right\} = 01100011_2$ 的第 $i$ 位元 (Bit $i$ of the constant) $[c_i \in GF(2)]$
  * 註：它是 $GF(2)^8$ 上的仿射映射 $b \mapsto Ab \oplus c$，$A \in GL_8(\mathbf{Z}_2)$
    （見 [一般線性群的階](../../Abstract_Algebra/Group/General_Linear_Group_Order.md) 文末）。

* **【定義 1】 位元組與多項式的對應 (Bytes as polynomials)：** FIPS-197 §4

  $$b_7 b_6 \cdots b_0 \ \overset{\text{def}}{\longleftrightarrow} \ b_7 x^7 + b_6 x^6 + \cdots + b_1 x + b_0$$

  * 例：$\left\{57\right\} = 01010111_2 \leftrightarrow x^6 + x^4 + x^2 + x + 1$，$\left\{02\right\} \leftrightarrow x$，$\left\{03\right\} \leftrightarrow x + 1$。

+++

## 證明:

### (a) verify that bytes form the field and that addition is exclusive or

由【已知 2(a)】$m$ 不可約，【已知 1】給出 $256$ 元素的體，其元素經【定義 1】恰為所有位元組。
加法是係數逐項模 $2$ 相加，即逐位元 XOR：

$$\begin{gather*}
\left\{57\right\} \oplus \left\{83\right\} &\overset{\text{定義 1}}{=}& \left(x^6 + x^4 + x^2 + x + 1\right) + \left(x^7 + x + 1\right) \\
&\overset{\text{已知 1,已知 2(a)}}{=}& x^7 + x^6 + x^4 + x^2 \\
&\overset{\text{定義 1}}{=}& \left\{d4\right\}
\end{gather*}$$

與 FIPS-197 §4.1 一致（$01010111 \oplus 10000011 = 11010100$）。

### (b) proof of the xtime formula

乘以 $x$ 使每個係數升一次；若原本 $b_7 = 1$，結果次數為 $8$，由【已知 3】減去（XOR）$m$ 一次：

$$\begin{gather*}
x \cdot b(x) &=& b_7 x^8 + b_6 x^7 + \cdots + b_0 x \\
x \cdot b(x) \bmod m &\overset{\text{已知 3}}{=}& \begin{cases} b \ll 1, & b_7 = 0 \\ \left(b \ll 1\right) \oplus \texttt{0x11B}, & b_7 = 1 \end{cases}
\end{gather*}$$

截成 $8$ 位元後 $\texttt{0x11B}$ 的第 $8$ 位元與移出的 $b_7$ 抵銷，只剩 $\left\{1b\right\}$。與 FIPS-197 §4.2.1 一致。

### (c) verify the multiplication examples

**直接乘再取模**（FIPS-197 §4.2）：

$$\begin{gather*}
\left(x^6 + x^4 + x^2 + x + 1\right)\left(x^7 + x + 1\right) &=& x^{13} + x^{11} + x^9 + x^8 + x^6 + x^5 + x^4 + x^3 + 1 \\
\left(x^{13} + x^{11} + x^9 + x^8 + x^6 + x^5 + x^4 + x^3 + 1\right) \bmod m &\overset{\text{已知 1}}{=}& x^7 + x^6 + 1 \\
\left\{57\right\} \bullet \left\{83\right\} &\overset{\text{定義 1}}{=}& \left\{c1\right\}
\end{gather*}$$

**用 xtime 連乘**（FIPS-197 §4.2.1）：$\left\{13\right\} = \left\{01\right\} \oplus \left\{02\right\} \oplus \left\{10\right\}$，
而 $\left\{57\right\}$ 反覆乘以 $\left\{02\right\}$：

$$\begin{gather*}
\left\{57\right\} \bullet \left\{02\right\} &\overset{\text{證明 (b)}}{=}& \left\{ae\right\} \\
\left\{57\right\} \bullet \left\{04\right\} &\overset{\text{證明 (b)}}{=}& \left\{47\right\} \qquad \text{(} \left\{ae\right\} \text{ 的 } b_7 = 1\text{，XOR } \left\{1b\right\}\text{)} \\
\left\{57\right\} \bullet \left\{08\right\} &\overset{\text{證明 (b)}}{=}& \left\{8e\right\} \\
\left\{57\right\} \bullet \left\{10\right\} &\overset{\text{證明 (b)}}{=}& \left\{07\right\} \\
\left\{57\right\} \bullet \left\{13\right\} &=& \left\{57\right\} \oplus \left\{ae\right\} \oplus \left\{07\right\} \qquad \text{(分配律)} \\
\left\{57\right\} \bullet \left\{13\right\} &=& \left\{fe\right\}
\end{gather*}$$

兩者都與 FIPS-197 一致。

### (d) verify the inverse of the byte fifty-three

對 $m = \texttt{0x11B}$ 與 $a = \left\{53\right\} = x^6 + x^4 + x + 1$ 跑擴展歐幾里得（【已知 4】），右欄是餘式寫成 $u \cdot a \pmod m$ 的係數 $u$：

$$\begin{gather*}
m &=& \left(x^2 + 1\right) a + x^2 \qquad \Rightarrow \ u = x^2 + 1 \\
a &=& \left(x^4 + x^2\right) x^2 + \left(x + 1\right) \qquad \Rightarrow \ u = 1 + \left(x^4 + x^2\right)\left(x^2 + 1\right) = x^6 + x^2 + 1 \\
x^2 &=& \left(x + 1\right)\left(x + 1\right) + 1 \qquad \Rightarrow \ u = \left(x^2 + 1\right) + \left(x + 1\right)\left(x^6 + x^2 + 1\right) = x^7 + x^6 + x^3 + x
\end{gather*}$$

最後餘式為 $1$，故

$$\begin{gather*}
\left\{53\right\}^{-1} &\overset{\text{已知 4}}{=}& x^7 + x^6 + x^3 + x \\
&\overset{\text{定義 1}}{=}& \left\{ca\right\}
\end{gather*}$$

驗算：$\left\{53\right\} \bullet \left\{ca\right\} = \left\{01\right\}$，且 $\left\{53\right\}^{254} = \left\{ca\right\}$（【已知 5】的另一種算法），兩者皆以 Python 確認。
與 FIPS-197 §5.1.1 的 S-box 例子一致。

* 註：每一列右側的「$\Rightarrow u$」是擴展歐幾里得的遞推 $u_{i+1} = u_{i-1} + q_i u_i$（$GF(2)$ 中減即加），與
  [歐幾里得整環](../Polynomial_Arithmetic/Euclidean_Domain.md) 文末的程式同一套。

### (e) verify the orders of the bytes two and three

**$\left\{02\right\}$**：由【已知 2(b)】直接得 $o\!\left(\left\{02\right\}\right) = 51$；以【已知 6】的精神核對（$51 = 3 \cdot 17$）：

$$\begin{gather*}
\left\{02\right\}^{3} &=& \left\{08\right\} \neq 1 \\
\left\{02\right\}^{17} &=& \left\{bc\right\} \neq 1 \\
\left\{02\right\}^{51} &\overset{\text{已知 2(b)}}{=}& \left\{01\right\}
\end{gather*}$$

**$\left\{03\right\}$**：$255 = 3 \cdot 5 \cdot 17$，檢查 $255/3 = 85$、$255/5 = 51$、$255/17 = 15$ 三個冪次：

$$\begin{gather*}
\left\{03\right\}^{85} &=& \left\{bd\right\} \neq 1 \\
\left\{03\right\}^{51} &=& \left\{0c\right\} \neq 1 \\
\left\{03\right\}^{15} &=& \left\{35\right\} \neq 1 \\
o\!\left(\left\{03\right\}\right) &\overset{\text{已知 6}}{=}& 255
\end{gather*}$$

故 $\left\{03\right\}$ 是 $GF(2^8)^*$ 的生成元，而 $\left\{02\right\}$ 不是。

### (f) verify one value of the S-box

$S(b) = A \cdot b^{-1} \oplus c$（$\left\{00\right\}$ 約定映到 $\left\{00\right\}$ 再做仿射）。由【證明 (d)】$\left\{53\right\}^{-1} = \left\{ca\right\} = 11001010_2$，
即 $b_7 \dots b_0 = 1,1,0,0,1,0,1,0$；$c = \left\{63\right\}$ 即 $c_7 \dots c_0 = 0,1,1,0,0,0,1,1$。逐位元套【已知 7】：

$$\begin{gather*}
b_0' &\overset{\text{已知 7}}{=}& 0 \oplus 0 \oplus 0 \oplus 1 \oplus 1 \oplus 1 = 1 \\
b_1' &\overset{\text{已知 7}}{=}& 1 \oplus 0 \oplus 1 \oplus 1 \oplus 0 \oplus 1 = 0 \\
b_2' &\overset{\text{已知 7}}{=}& 0 \oplus 1 \oplus 1 \oplus 0 \oplus 1 \oplus 0 = 1 \\
b_3' &\overset{\text{已知 7}}{=}& 1 \oplus 1 \oplus 0 \oplus 1 \oplus 0 \oplus 0 = 1 \\
b_4' &\overset{\text{已知 7}}{=}& 0 \oplus 0 \oplus 1 \oplus 0 \oplus 1 \oplus 0 = 0 \\
b_5' &\overset{\text{已知 7}}{=}& 0 \oplus 1 \oplus 0 \oplus 1 \oplus 0 \oplus 1 = 1 \\
b_6' &\overset{\text{已知 7}}{=}& 1 \oplus 0 \oplus 1 \oplus 0 \oplus 0 \oplus 1 = 1 \\
b_7' &\overset{\text{已知 7}}{=}& 1 \oplus 1 \oplus 0 \oplus 0 \oplus 1 \oplus 0 = 1
\end{gather*}$$

$b_7' \dots b_0' = 11101101_2$：

$$S\!\left(\left\{53\right\}\right) \overset{\text{證明 (d),已知 7}}{=} \left\{ed\right\}$$

與 FIPS-197 §5.1.1 的例子（Figure 7 表中 $x = 5$、$y = 3$ 格）一致。

* 註：每一列的六項依序是 $b_i, b_{i+4}, b_{i+5}, b_{i+6}, b_{i+7}, c_i$（下標模 $8$）。

+++

## 意義與密碼學關聯 (Interpretation and Relevance to Cryptography)

### 全章定理在 AES 中的落點

| AES 的運算 | 用到的定理 |
|---|---|
| 位元組是體元素 | [GF(p^n) 的構造](../Construction/Construction_of_GF_p_n.md)、[不可約多項式](../../Abstract_Algebra/Field/Irreducible_Polynomial.md) |
| 加法 = XOR | 特徵 $2$（[有限體的階](../Structure/Order_of_a_Finite_Field.md) 的質子體 $GF(2)$） |
| `xtime` | [多項式的除法原理](../Polynomial_Arithmetic/Division_Algorithm_for_Polynomials.md) |
| S-box 的反元素 | [歐幾里得整環](../Polynomial_Arithmetic/Euclidean_Domain.md) 或 [$x^q - x$ 的根](../Structure/Roots_of_x_q_minus_x.md)（$a^{254}$） |
| `MixColumns` 的係數 $\left\{02\right\}, \left\{03\right\}$ | 本檔 (b)(c) |
| 選 $m(x)$ 不影響結構 | [$GF(p^n)$ 的唯一性](../Structure/Uniqueness_of_GF_p_n.md) |
| 塔式硬體實作 | [GF(p^n) 的子體](../Structure/Subfields_of_GF_p_n.md)、[塔定理](../../Abstract_Algebra/Field/Tower_Law.md) |

### 為什麼 S-box 用「反元素」

$x \mapsto x^{-1}$（即 $x^{254}$）在 $GF(2^8)$ 上有極佳的**非線性**：最大差分機率 $4/256$、最大線性偏差 $16/256$，
是 Nyberg（1993）證明的近乎最優。仿射變換則破壞 $x^{-1}$ 的代數簡潔性（例如 $0 \mapsto 0$、$1 \mapsto 1$ 的不動點）。
**「反元素存在」本身就依賴 $m$ 不可約** —— 若 $m$ 可約，某些位元組沒有反元素，S-box 無法定義。

### $\left\{02\right\}$ 不是生成元的後果

(e) 說 $\left\{02\right\}$ 的階只有 $51$。實作 $\log$/$\exp$ 查表乘法時必須以 $\left\{03\right\}$（或其他生成元）為底，
否則表只能覆蓋 $51$ 個非零元素。這是 AES 實作者常踩的坑，而原因就在投影片 p.24 那張表的一個數字。

### 程式思維

```python
def xtime(a):
    """證明 (b)：乘以 {02}。"""
    a <<= 1
    return a ^ 0x11B if a & 0x100 else a

def gmul(a, b):
    """GF(2^8) 乘法：b 的每個位元對應一次 xtime（證明 (c) 的連乘法）。"""
    r = 0
    while b:
        if b & 1:
            r ^= a
        a, b = xtime(a), b >> 1
    return r

def ginv(a):
    """證明 (d)：a^{-1} = a^{254}（已知 5），0 映到 0。"""
    r = 1
    for _ in range(254):
        r = gmul(r, a)
    return r if a else 0

def sbox(a):
    """證明 (f)：反元素後接仿射變換。"""
    b, r = ginv(a), 0
    for i in range(8):
        bit = (b >> i) ^ (b >> (i + 4) % 8) ^ (b >> (i + 5) % 8) ^ (b >> (i + 6) % 8) ^ (b >> (i + 7) % 8) ^ (0x63 >> i)
        r |= (bit & 1) << i
    return r

assert 0x57 ^ 0x83 == 0xD4                                  # (a)
assert gmul(0x57, 0x83) == 0xC1 and gmul(0x57, 0x13) == 0xFE # (c)
assert ginv(0x53) == 0xCA                                    # (d)
assert sbox(0x53) == 0xED and sbox(0x00) == 0x63             # (f)
assert sorted(sbox(a) for a in range(256)) == list(range(256))   # S-box 是排列
```
