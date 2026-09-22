# Irreducible Polynomial (不可約多項式)

+++

## 證明目標:

`Algebra.pdf` p.49。多項式版本的「質數」。它是
[模不可約多項式的商環是體](Quotient_by_Irreducible_is_Field.md) 的入場券 ——
也就是 $GF(2^8)$ 能被造出來的原因。

* (a) 二次與三次的判別法（投影片未列，但三個例子都靠它）：

$$\deg f \in \left\{2, 3\right\} \quad \Longrightarrow \quad \left[\, f \ \text{不可約} \ \Longleftrightarrow \ f \ \text{在 } F \text{ 中無根} \,\right]$$

* (b) 投影片的三組例子：

$$x^2 + 2 \ \text{在 } \mathbf{Z}_5[x] \ \text{不可約}, \qquad x^2 + 2 = \left(x+1\right)\left(x+2\right) \ \text{在 } \mathbf{Z}_3[x] \ \text{可約}$$

$$x^2 + 1 \ \text{在 } \mathbf{Z}[x] \ \text{不可約}, \qquad x^2 + 1 = \left(x+i\right)\left(x-i\right) \ \text{在 } \mathbf{C}[x] \ \text{可約}$$

* (c) **判別法只對次數 $2, 3$ 成立** —— $x^4 + 1$ 在 $\mathbf{Z}_2[x]$ 中無根卻可約。

* $F$ : 係數所在的體 (The field of coefficients) $[\text{體}]$
* $F[x]$ : 多項式環 (The polynomial ring) $[\text{集合}]$
* $f,\ g,\ h$ : 多項式 (Polynomials) $[f, g, h \in F[x]]$
* $p(x)$ : 不可約多項式 (An irreducible polynomial) $[p(x) \in F[x]]$
* $c$ : 非零常數 (A non-zero constant) $[c \in F \setminus \left\{0\right\}]$
* 註：**「不可約」永遠是相對於某個係數環（或體）而言**。
  同一個多項式在不同的係數體上可約性完全不同 —— (b) 的兩組例子就是為了說明這件事。
* 註：**投影片的第三個例子 $\mathbf{Z}[x]$ 嚴格來說超出了定義的範圍**，
  因為【定義 1】要求係數在**體**上，而 $\mathbf{Z}$ 不是體
  （[體的定義](Field_Definition.md)【證明 (c)】）。不可約性對一般整環仍可定義，
  只是「單位元素」的集合從 $F \setminus \left\{0\right\}$ 縮成 $\left\{\pm 1\right\}$。
  本檔在【定義 2】補上這個版本並在【證明 (b)】說明。
* 註：(c) 的警告很重要 —— 實務上判斷 $GF(2^8)$ 用的八次多項式是否不可約，
  **不能**只檢查有沒有根。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [多項式環與次數可加性 (The polynomial ring and additivity of degree)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Ring/Integral_Domain.html#assumptions-preliminaries)：** 已於本章 [環的例子](../Ring/Ring_Examples.md)【定義 2】與 [整環](../Ring/Integral_Domain.md)【推導 2】給出並證明，此處直接引用不再重證

  * (a) 多項式環：

    $$F[x] = \left\{\sum_{i=0}^{m} a_i x^i \ \middle|\ m \in \mathbf{N},\ a_i \in F\right\}$$

  * (b) 次數可加（$F$ 為整環時）：

    $$\deg\left(gh\right) = \deg g + \deg h \qquad \left(g, h \neq 0\right)$$

  * $F$ : 係數所在的體 (The field of coefficients) $[\text{體}]$
  * $F[x]$ : 多項式環 (The polynomial ring) $[\text{集合}]$
  * $g,\ h$ : 非零多項式 (Non-zero polynomials) $[g, h \in F[x]]$
  * $a_i$ : 多項式係數 (Polynomial coefficients) $[a_i \in F]$
  * $\deg$ : 多項式的次數 (The degree) $[F[x] \setminus \left\{0\right\} \to \mathbf{N}]$
  * 註：體必為整環（[體的定義](Field_Definition.md)【證明 (d)】），故 (b) 適用。

* **【已知 2】 [因式定理 (Factor theorem)](https://mathworld.wolfram.com/PolynomialRemainderTheorem.html)：** 由多項式除法直接得到的標準結果，本章直接引用不再重證

  $$f(a) = 0 \quad \Longleftrightarrow \quad \left(x - a\right) \mid f(x) \qquad \left(a \in F,\ F \ \text{為體}\right)$$

  * $f$ : 多項式 (A polynomial) $[f \in F[x]]$
  * $a$ : 體元素 (A field element) $[a \in F]$
  * $F$ : 係數所在的體 (The field of coefficients) $[\text{體}]$
  * 註：證明是把 $f$ 對 $x - a$ 做帶餘除法得 $f = q\left(x-a\right) + r$（$r$ 為常數），
    代入 $x = a$ 得 $r = f(a)$。**多項式除法需要首項係數可逆**，
    這裡除數 $x-a$ 的首項係數是 $1$，故對任意交換含單位元環都成立。

* **【已知 3】 [體的定義與可逆元素 (Field definition and units)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Field/Field_Definition.html#b-proof-that-the-residues-modulo-a-prime-form-a-field)：** 已於本章 [體的定義](Field_Definition.md)【定義 1】【證明 (b)】給出並證明，此處直接引用不再重證

  * (a) 體的非零元素皆可逆：

    $$\forall\, a \in F \setminus \left\{0\right\}, \ \exists\, a^{-1} \in F$$

  * (b) 質數模的剩餘類是體：

    $$\mathbf{Z}_p \ \text{為體} \quad \Longleftrightarrow \quad p \ \text{為質數}$$

  * $F$ : 體的底層集合 (The underlying set of the field) $[\text{集合}]$
  * $a$ : 非零體元素 (A non-zero field element) $[a \in F \setminus \left\{0\right\}]$
  * $p$ : 質數 (A prime) $[p \in \mathbf{P}]$

* **【定義 1】 不可約多項式（係數在體上）(Irreducible polynomial over a field)：** 除了「自己的常數倍」與「非零常數」之外沒有別的因式

  $$p(x) \ \text{不可約} \quad \overset{\text{def}}{\Longleftrightarrow} \quad \deg p \ge 1 \ \text{ 且 } \ \left[\, p = gh \ \Longrightarrow \ \deg g = 0 \ \text{ 或 } \ \deg h = 0 \,\right]$$

  * $p(x)$ : 被檢查的多項式 (The polynomial under test) $[p(x) \in F[x]]$
  * $g,\ h$ : 因式 (Factors) $[g, h \in F[x]]$
  * $F$ : 係數所在的體 (The field of coefficients) $[\text{體}]$
  * $\deg$ : 多項式的次數 (The degree) $[F[x] \setminus \left\{0\right\} \to \mathbf{N}]$
  * 註：投影片的措辭是「its only divisors are its **associates** $\left[cp(x)\right]$ and non-zero constants」。
    兩種寫法等價 —— 若 $p = gh$ 且兩者次數都 $\ge 1$，
    由【已知 1(b)】兩者次數都 $< \deg p$，就出現了「非常數倍、非常數」的因式。
  * 註：$\deg p \ge 1$（**非常數**）這個條件不可省。常數（含 $0$ 與單位元素）
    按慣例既不算可約也不算不可約，正如 $1$ 既非質數也非合數。

* **【定義 2】 不可約多項式（係數在整環上）(Irreducible polynomial over an integral domain)：** 投影片 $\mathbf{Z}[x]$ 例子所需的版本

  $$p(x) \ \text{在 } R[x] \text{ 中不可約} \quad \overset{\text{def}}{\Longleftrightarrow} \quad \deg p \ge 1 \ \text{ 且 } \ \left[\, p = gh \ \Longrightarrow \ g \ \text{或} \ h \ \text{是 } R \ \text{的可逆元素} \,\right]$$

  * $p(x)$ : 被檢查的多項式 (The polynomial under test) $[p(x) \in R[x]]$
  * $g,\ h$ : 因式 (Factors) $[g, h \in R[x]]$
  * $R$ : 係數所在的整環 (The coefficient integral domain) $[\text{環}]$
  * 註：**與【定義 1】的差別**：體裡所有非零常數都可逆，故「次數為 $0$」等價於「可逆」；
    但 $\mathbf{Z}$ 裡只有 $\pm 1$ 可逆，所以 $2x$ 在 $\mathbf{Z}[x]$ 中**可約**
    （$2x = 2 \times x$，$2$ 不可逆），在 $\mathbf{Q}[x]$ 中卻不可約。
  * 註：$F$ 為體時兩個定義一致，故本檔對 $\mathbf{Z}_5[x]$、$\mathbf{Z}_3[x]$、$\mathbf{C}[x]$
    用【定義 1】，對 $\mathbf{Z}[x]$ 用【定義 2】。

* **【假設 1】 反設：二次或三次多項式可約 (Proof by contradiction)：** 【證明 (a)】($\Leftarrow$) 方向要用

  $$f = gh \qquad \text{with } \deg g \ge 1,\ \deg h \ge 1,\ \deg f \in \left\{2, 3\right\}$$

  * $f,\ g,\ h$ : 多項式 (Polynomials) $[f, g, h \in F[x]]$
  * $\deg$ : 多項式的次數 (The degree) $[F[x] \setminus \left\{0\right\} \to \mathbf{N}]$

+++

## 證明:

### (a) proof of the root criterion for degrees two and three

**($\Rightarrow$) 不可約推出無根。** 證逆否 —— 有根則可約。設 $f(a) = 0$：

$$\begin{gather*}
f(a) &=& 0 \\
\left(x - a\right) &\overset{\text{已知 2}}{\mid}& f(x) \\
f &=& \left(x-a\right)\,q(x) \qquad \text{for some } q \in F[x] \\
\deg q &\overset{\text{已知 1(b)}}{=}& \deg f - 1 \ge 1 \qquad \text{(因 } \deg f \ge 2\text{)} \\
f &\overset{\text{定義 1}}{=}& \text{可約}
\end{gather*}$$

**($\Leftarrow$) 無根推出不可約。** 反設 $f$ 可約（【假設 1】），拆成兩個次數 $\ge 1$ 的因式：

$$\begin{gather*}
\deg g + \deg h &\overset{\text{已知 1(b)}}{=}& \deg f \le 3 \\
\deg g \ge 1, \quad \deg h &\overset{\text{假設 1}}{\ge}& 1 \\
\min\left(\deg g,\ \deg h\right) &=& 1 \qquad \text{(兩個 } \ge 1 \text{ 的數相加 } \le 3\text{，必有一個是 } 1\text{)}
\end{gather*}$$

不妨設 $\deg g = 1$，寫成 $g = cx + d$（$c \neq 0$）。$F$ 是體故 $c^{-1}$ 存在：

$$\begin{gather*}
g\!\left(-dc^{-1}\right) &=& c\left(-dc^{-1}\right) + d \\
g\!\left(-dc^{-1}\right) &\overset{\text{已知 3(a)}}{=}& -d + d = 0 \\
f\!\left(-dc^{-1}\right) &=& g\!\left(-dc^{-1}\right)\,h\!\left(-dc^{-1}\right) \\
f\!\left(-dc^{-1}\right) &=& 0
\end{gather*}$$

$f$ 有根 $-dc^{-1} \in F$，與「無根」矛盾。故 $f$ 不可約。

* 註：**$F$ 是體在這裡是必要的** —— 一次式 $cx + d$ 要有根需要 $c^{-1}$ 存在。
  在 $\mathbf{Z}[x]$ 裡 $2x + 1$ 沒有整數根，但它確實是一次式。
* 註：**這個判別法只對次數 $2, 3$ 成立**，理由就在第一段的
  「兩個 $\ge 1$ 的數相加 $\le 3$ 必有一個是 $1$」——
  次數 $4$ 時可以拆成 $2 + 2$，兩個因式都沒有根。見【證明 (c)】。

### (b) verify the four examples from the slides

**$x^2 + 2$ 在 $\mathbf{Z}_5[x]$ 中不可約。** $5$ 是質數故 $\mathbf{Z}_5$ 是體（【已知 3(b)】）。
逐一代入五個元素檢查有無根：

$$\begin{gather*}
0^2 + 2 &=& 2 \\
1^2 + 2 &=& 3 \\
2^2 + 2 &=& 6 \bmod 5 = 1 \\
3^2 + 2 &=& 11 \bmod 5 = 1 \\
4^2 + 2 &=& 18 \bmod 5 = 3
\end{gather*}$$

五個值都不是 $0$，故無根。由【證明 (a)】（$\deg = 2$）：

$$x^2 + 2 \ \text{在 } \mathbf{Z}_5[x] \ \text{不可約}$$

**$x^2 + 2$ 在 $\mathbf{Z}_3[x]$ 中可約。** 同樣逐一檢查：

$$\begin{gather*}
0^2 + 2 &=& 2 \\
1^2 + 2 &=& 3 \bmod 3 = 0 \\
2^2 + 2 &=& 6 \bmod 3 = 0
\end{gather*}$$

$x = 1$ 與 $x = 2$ 都是根，故可約。投影片給的分解直接驗算：

$$\begin{gather*}
\left(x+1\right)\left(x+2\right) &=& x^2 + 3x + 2 \\
3 \bmod 3 &=& 0 \\
\left(x+1\right)\left(x+2\right) &=& x^2 + 2
\end{gather*}$$

與投影片一致。

* 註：$x + 1 = x - 2$ 對應根 $x = 2$、$x + 2 = x - 1$ 對應根 $x = 1$（在 $\mathbf{Z}_3$ 中 $-1 = 2$、$-2 = 1$），
  與【已知 2】的因式定理一致。
* 註：**同一個多項式，換個係數體結論就翻過來** —— 這是本檔最重要的觀察。

**$x^2 + 1$ 在 $\mathbf{Z}[x]$ 中不可約**（用【定義 2】）。反設它可約：

$$\begin{gather*}
x^2 + 1 &\overset{\text{定義 2}}{=}& gh \qquad \text{with } g, h \ \text{皆不可逆} \\
\deg g + \deg h &\overset{\text{已知 1(b)}}{=}& 2 \\
\deg g = \deg h &=& 1 \qquad \text{(不可逆的常數會使首項係數乘積不為 } 1\text{)} \\
x^2 + 1 &=& \left(ax+b\right)\left(cx+d\right) \qquad \text{with } ac = 1,\ bd = 1,\ ad+bc = 0 \\
a = c = \pm 1, \quad b = d &=& \pm 1 \qquad \text{(整數解)} \\
ad + bc &=& \pm 2 \neq 0
\end{gather*}$$

矛盾，故 $x^2+1$ 在 $\mathbf{Z}[x]$ 中不可約。

**$x^2 + 1$ 在 $\mathbf{C}[x]$ 中可約**（用【定義 1】）。$\mathbf{C}$ 中 $i^2 = -1$，故有根：

$$\begin{gather*}
i^2 + 1 &=& -1 + 1 = 0 \\
\left(-i\right)^2 + 1 &=& -1 + 1 = 0 \\
\left(x + i\right)\left(x - i\right) &=& x^2 - i^2 \\
\left(x + i\right)\left(x - i\right) &=& x^2 + 1
\end{gather*}$$

與投影片一致。

* 註：$x^2+1$ 在 $\mathbf{R}[x]$ 中也不可約（實數平方非負，$a^2 + 1 > 0$ 永遠有根不了）——
  這正是 [模不可約多項式的商環是體](Quotient_by_Irreducible_is_Field.md)
  能用 $\mathbf{R}[x]/\left\langle x^2+1 \right\rangle$ 造出 $\mathbf{C}$ 的原因。

### (c) disprove the root criterion for higher degrees

取 $f = x^4 + 1 \in \mathbf{Z}_2[x]$。先檢查有無根：

$$\begin{gather*}
0^4 + 1 &=& 1 \\
1^4 + 1 &=& 2 \bmod 2 = 0
\end{gather*}$$

咦，$x = 1$ 是根。換一個更乾淨的例子 —— 取 $f = x^4 + x^2 + 1 \in \mathbf{Z}_2[x]$：

$$\begin{gather*}
0^4 + 0^2 + 1 &=& 1 \\
1^4 + 1^2 + 1 &=& 3 \bmod 2 = 1
\end{gather*}$$

**無根**。但它確實可約：

$$\begin{gather*}
\left(x^2 + x + 1\right)^2 &=& x^4 + x^2 + 1 + 2x^3 + 2x^2 + 2x \\
2 \bmod 2 &=& 0 \\
\left(x^2 + x + 1\right)^2 &=& x^4 + x^2 + 1
\end{gather*}$$

它拆成兩個二次式的乘積，**兩個因式各自都沒有根**，所以「檢查根」完全看不出來。

$$\deg f = 4 \quad \Longrightarrow \quad \text{【證明 (a)】的判別法不適用}$$

* 註：展開時用了 [新生之夢](Freshmans_Dream.md)【證明 (a)】——
  $\mathbf{Z}_2$ 的特徵是 $2$，故 $\left(a+b+c\right)^2 = a^2+b^2+c^2$，交叉項全消。
* 註：**次數 $\ge 4$ 必須用別的方法判斷不可約性**（試除所有低次不可約多項式、
  Rabin 檢驗、或查表）。AES 用的 $x^8+x^4+x^3+x+1$ 是八次，
  它的不可約性是查表得到的，不是靠檢查根。

+++

## 意義與密碼學關聯 (Interpretation and Relevance to Cryptography)

### 不可約多項式 $=$ 多項式世界的質數

把兩邊並排：

| 整數 $\mathbf{Z}$ | 多項式 $F[x]$ |
|---|---|
| 質數 $p$ | 不可約多項式 $p(x)$ |
| 可逆元素 $\pm 1$ | 非零常數 $c$ |
| $\mathbf{Z}/\left\langle p \right\rangle = \mathbf{Z}_p$ 是**體** | $F[x]/\left\langle p(x) \right\rangle$ 是**體** |
| 算術基本定理（唯一分解） | 多項式唯一分解 |
| $\mathbf{Z}$ 是 PID | $F[x]$ 是 PID |

**右欄的第三列就是 $GF(2^8)$ 的造法**，見
[模不可約多項式的商環是體](Quotient_by_Irreducible_is_Field.md)。

### 「不可約」永遠要問「在哪裡」

本檔最重要的教訓是【證明 (b)】的對照：

$$x^2 + 2 \ \begin{cases} \text{在 } \mathbf{Z}_5[x] \ \text{不可約} \\ \text{在 } \mathbf{Z}_3[x] \ \text{可約} \end{cases} \qquad x^2 + 1 \ \begin{cases} \text{在 } \mathbf{R}[x] \ \text{不可約} \\ \text{在 } \mathbf{C}[x] \ \text{可約} \end{cases}$$

**沒有「絕對的不可約」。** 這與質數不同 —— $7$ 在 $\mathbf{Z}$ 裡永遠是質數，
但在 $\mathbf{Z}[i]$ 裡 $5 = \left(2+i\right)\left(2-i\right)$ 就不是質數了。

實務上這意味著：講 $GF(2^8)$ 的生成多項式時，**必須說明是在 $\mathbf{Z}_2[x]$ 上不可約**。
同一個多項式在 $\mathbf{Z}_3[x]$ 上可能分解得四分五裂。

### AES 的那個多項式

AES 用的是：

$$m(x) = x^8 + x^4 + x^3 + x + 1 \qquad \text{（十六進位 } \texttt{0x11B}\text{）}$$

它在 $\mathbf{Z}_2[x]$ 上不可約。八次多項式在 $\mathbf{Z}_2[x]$ 上共有 $2^8 = 256$ 個首一的，
其中**恰好 $30$ 個不可約**。AES 從這 $30$ 個裡挑了係數最少的那一個
（只有五項，硬體上模約化最省閘）。

$$\text{不可約的八次多項式個數} = \frac{1}{8}\sum_{d \mid 8}\mu(d)\,2^{8/d} = \frac{2^8 - 2^4}{8} = 30$$

**這個數字是有限體理論算出來的**（本章不證這條公式），
但重點是：候選者很少，而且它們全部都給出**同構的**體 ——
挑哪一個只影響實作效率，不影響數學結構。

### 為什麼 CRC 也用不可約多項式

CRC 校驗碼的生成多項式也常選不可約（或其乘積）的多項式。
理由是不可約多項式的倍數集合 $\left\langle p(x) \right\rangle$ 構成一個
[主理想](../Ring/Principal_Ideal.md)，而「錯誤被偵測不到」等價於「錯誤模式落在這個理想裡」。

$p(x)$ 次數越高、結構越好，理想就越「稀疏」，漏掉錯誤的機率就越低。
CRC-32 的生成多項式 $\texttt{0x04C11DB7}$ 是三十二次的，經過精心挑選以最大化偵錯能力。

### 程式思維

```python
def has_root(coeffs, p):
    """檢查 Z_p[x] 中的多項式有沒有根（證明 (a)，僅適用於次數 2, 3）。"""
    def evaluate(x):
        return sum(c * pow(x, i, p) for i, c in enumerate(coeffs)) % p
    return any(evaluate(a) == 0 for a in range(p))

# x^2 + 2 的係數列表是 [2, 0, 1]
assert not has_root([2, 0, 1], 5)     # Z_5 中無根 -> 不可約
assert has_root([2, 0, 1], 3)         # Z_3 中有根 -> 可約

# 次數 >= 4 時這個函式會誤判！
assert not has_root([1, 0, 1, 0, 1], 2)   # x^4+x^2+1 無根，但可約（證明 (c)）
```

最後一行是**刻意留下的陷阱** —— `has_root` 回傳 `False` 不代表不可約。
判斷高次不可約性要用 Rabin 測試：

```python
# f 不可約 <=> x^(q^n) ≡ x (mod f) 且 gcd(x^(q^(n/d)) - x, f) = 1 對所有質因數 d
```

那條判準的原理正是 [新生之夢](Freshmans_Dream.md) 文末的
Frobenius 映射不動點刻畫。
