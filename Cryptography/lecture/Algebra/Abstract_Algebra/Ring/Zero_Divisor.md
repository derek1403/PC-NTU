# Zero Divisor (零因子)

+++

## 證明目標:

`Algebra.pdf` p.31。兩個**非零**的東西相乘卻得到 $0$ —— 這在 $\mathbf{Z}$ 裡不可能發生，
但在 $\mathbf{Z}_6$ 裡稀鬆平常。這個現象決定了環「好不好用」。

* (a) $2$ 與 $3$ 是 $\mathbf{Z}_6$ 的零因子：

$$2 \otimes 3 = 6 \equiv 0 \pmod 6, \qquad 2 \neq 0, \quad 3 \neq 0$$

* (b) $\mathbf{Z}_n$ 有零因子的充要條件：

$$\mathbf{Z}_n \ \text{有零因子} \quad \Longleftrightarrow \quad n \ \text{為合數} \qquad \left(n \ge 2\right)$$

* (c) 零因子恰好就是乘法消去律失效的原因：

$$R \ \text{無零因子} \quad \Longleftrightarrow \quad \left[\, ab = ac,\ a \neq 0 \ \Longrightarrow \ b = c \,\right]$$

* $R$ : 環的底層集合 (The underlying set of the ring) $[\text{集合}]$
* $a,\ b,\ c$ : 環元素 (Ring elements) $[a, b, c \in R]$
* $0$ : 加法單位元素 (The additive identity) $[0 \in R]$
* $\mathbf{Z}_n$ : 模 $n$ 剩餘類環 (The ring of residues modulo $n$) $[\text{集合}]$
* $n$ : 模數 (Modulus) $[n \in \mathbf{P}]$
* 註：(c) 不在投影片上，但它說明了**為什麼要在乎零因子** ——
  沒有零因子，$\mathbf{Z}$ 裡「兩邊同除以 $a$」的直覺才能搬過來。
* 註：(b) 的條件是 $n \ge 2$。$n = 1$ 時 $\mathbf{Z}_1 = \left\{0\right\}$ 是零環，
  沒有非零元素，故沒有零因子；而 $1$ 既非質數也非合數，不在敘述範圍內。
* 註：無零因子的環另有專名，見 [整環](Integral_Domain.md)。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [環的公理與基本命題 (Ring axioms and basic propositions)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Ring/Ring_Basic_Propositions.html#a-proof-that-multiplication-by-zero-gives-zero)：** 已於本章 [環的定義](Ring_Definition.md)【定義 1】與 [環的基本命題](Ring_Basic_Propositions.md)【證明 (a)(c)】給出，此處直接引用不再重證

  * (a) 分配律與減法分配律：

    $$a\left(b + c\right) = ab + ac, \qquad a\left(b - c\right) = ab - ac$$

  * (b) 乘以零得零：

    $$a \times 0 = 0 \times a = 0$$

  * $R$ : 環的底層集合 (The underlying set of the ring) $[\text{集合}]$
  * $a,\ b,\ c$ : 環元素 (Ring elements) $[a, b, c \in R]$
  * $0$ : 加法單位元素 (The additive identity) $[0 \in R]$

* **【已知 2】 [模 $n$ 剩餘類環 (The ring of residues modulo $n$)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Ring/Ring_Examples.html#c-verify-that-the-residues-modulo-n-form-a-ring)：** 已於本章 [環的例子](Ring_Examples.md)【證明 (c)】完整證明，此處直接引用不再重證

  $$\mathbf{Z}_n = \left\{0, 1, \dots, n-1\right\} \ \text{ 配 } \oplus, \otimes \ \text{ 是環}, \qquad a \otimes b = \left(a \times b\right) \bmod n$$

  * $\mathbf{Z}_n$ : 模 $n$ 剩餘類環 (The ring of residues modulo $n$) $[\text{集合}]$
  * $\oplus,\ \otimes$ : 模 $n$ 加法與乘法 (Addition and multiplication modulo $n$) $[\mathbf{Z}_n \times \mathbf{Z}_n \to \mathbf{Z}_n]$
  * $a,\ b$ : 剩餘類代表元 (Residue representatives) $[a, b \in \mathbf{Z}_n]$
  * $n$ : 模數 (Modulus) $[n \in \mathbf{P}]$

* **【已知 3】 [歐幾里得引理 (Euclid's lemma)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Group/Group_Examples_and_Counterexamples.html#assumptions-preliminaries)：** 已於本章 [群的正例與反例](../Group/Group_Examples_and_Counterexamples.md)【已知 6】引用，此處再次引用

  $$p \ \text{為質數}, \quad p \mid ab \quad \Longrightarrow \quad p \mid a \ \text{ 或 } \ p \mid b$$

  * $p$ : 質數 (A prime) $[p \in \mathbf{P}]$
  * $a,\ b$ : 任意整數 (Arbitrary integers) $[a, b \in \mathbf{Z}]$

* **【已知 4】 [合數的定義 (Definition of a composite number)](https://mathworld.wolfram.com/CompositeNumber.html)：** 初等數論的標準定義，本章直接引用

  $$n \ \text{為合數} \quad \overset{\text{def}}{\Longleftrightarrow} \quad n = ab \ \text{ for some } a, b \in \mathbf{Z} \ \text{ with } \ 1 < a < n,\ 1 < b < n$$

  * $n$ : 被檢查的整數 (The integer under test) $[n \in \mathbf{P},\ n \ge 2]$
  * $a,\ b$ : 真因數 (Proper divisors) $[a, b \in \mathbf{Z}]$
  * 註：$n \ge 2$ 時「合數」與「質數」互補 —— 不是質數就是合數。$n = 1$ 兩者皆非。

* **【定義 1】 零因子 (Zero divisor)：** 兩個非零元素相乘卻得到零

  $$a, b \ \text{為 } R \text{ 的零因子} \quad \overset{\text{def}}{\Longleftrightarrow} \quad a \neq 0, \quad b \neq 0, \quad ab = 0$$

  * $a,\ b$ : 環元素 (Ring elements) $[a, b \in R]$
  * $R$ : 環的底層集合 (The underlying set of the ring) $[\text{集合}]$
  * $0$ : 加法單位元素 (The additive identity) $[0 \in R]$
  * 註：**$0$ 本身不算零因子**，定義明確要求 $a \neq 0$ 且 $b \neq 0$。
    [環的基本命題](Ring_Basic_Propositions.md)【證明 (a)】說 $a \times 0 = 0$ 對任何 $a$ 都成立，
    若不排除 $0$，每個環都會「有零因子」，這個概念就毫無鑑別力。
  * 註：零因子是**成對**出現的 —— $a$ 是零因子時必定存在搭檔 $b$。
    習慣上也說「$a$ 是一個零因子」，意思是「存在非零的 $b$ 使 $ab = 0$」。

* **【假設 1】 反設：無零因子卻消去律失效 (Proof by contradiction)：** 【證明 (c)】($\Rightarrow$) 方向要用

  $$R \ \text{無零因子}, \qquad ab = ac, \quad a \neq 0, \quad b \neq c$$

  * $R$ : 環的底層集合 (The underlying set of the ring) $[\text{集合}]$
  * $a,\ b,\ c$ : 環元素 (Ring elements) $[a, b, c \in R]$

+++

## 證明:

### (a) verify the zero divisors in the residues modulo six

依【已知 2】計算 $2 \otimes 3$：

$$\begin{gather*}
2 \otimes 3 &\overset{\text{已知 2}}{=}& \left(2 \times 3\right) \bmod 6 \\
2 \otimes 3 &=& 6 \bmod 6 \\
2 \otimes 3 &=& 0 \\
2 \neq 0, \quad 3 &\neq& 0 \\
2, 3 &\overset{\text{定義 1}}{=}& \mathbf{Z}_6 \ \text{的零因子}
\end{gather*}$$

與投影片一致。$\mathbf{Z}_6$ 的零因子共有三個 —— $2, 3, 4$：

$$\begin{gather*}
2 \otimes 3 &=& 0 \\
3 \otimes 4 &=& 12 \bmod 6 = 0 \\
4 \otimes 3 &=& 0
\end{gather*}$$

$1$ 與 $5$ 不是零因子（它們與 $6$ 互質，可逆）。

### (b) proof of the criterion for the existence of zero divisors modulo n

**($\Leftarrow$) $n$ 為合數推出有零因子。** 依【已知 4】把 $n$ 拆成兩個真因數：

$$\begin{gather*}
n &\overset{\text{已知 4}}{=}& ab \qquad \text{with } 1 < a < n,\ 1 < b < n \\
a \neq 0, \quad b &\neq& 0 \qquad \text{(因 } 1 < a, b\text{，兩者都是 } \mathbf{Z}_n \text{ 的非零元素)} \\
a \otimes b &\overset{\text{已知 2}}{=}& \left(a \times b\right) \bmod n \\
a \otimes b &=& n \bmod n \\
a \otimes b &=& 0 \\
a, b &\overset{\text{定義 1}}{=}& \mathbf{Z}_n \ \text{的零因子}
\end{gather*}$$

**($\Rightarrow$) 有零因子推出 $n$ 為合數。** 證逆否命題：$n$ 為質數則無零因子。
設 $p$ 為質數、$a \otimes b = 0$：

$$\begin{gather*}
a \otimes b &\overset{\text{已知 2}}{=}& \left(a \times b\right) \bmod p = 0 \\
p &\mid& ab \\
p \mid a \ \text{ 或 } \ p &\overset{\text{已知 3}}{\mid}& b \\
a \equiv 0 \ \text{ 或 } \ b &\equiv& 0 \pmod p \\
a = 0 \ \text{ 或 } \ b &=& 0 \qquad \text{(在 } \mathbf{Z}_p \text{ 中)}
\end{gather*}$$

兩個因子至少有一個是 $0$，故依【定義 1】不構成零因子。逆否成立，原命題成立。

兩個方向都證完，故 $\mathbf{Z}_n$ 有零因子 $\Leftrightarrow$ $n$ 為合數（$n \ge 2$）。

* 註：**歐幾里得引理是 ($\Rightarrow$) 方向的全部內容**。它說「質數整除乘積就一定整除某個因子」——
  換句話說質數無法被「拆散到兩個因子裡」，這正是 $\mathbf{Z}_p$ 沒有零因子的原因。
* 註：與投影片一致：「$\mathbf{Z}_p$ has no zero divisors for every prime $p$」、
  「$\mathbf{Z}_n$ has zero divisors if and only if $n$ is composite」。

### (c) proof that the absence of zero divisors is equivalent to the cancellation law

**($\Rightarrow$) 無零因子推出消去律成立。** 反設消去律失效（【假設 1】）：

$$\begin{gather*}
ab &\overset{\text{假設 1}}{=}& ac \\
ab - ac &=& 0 \\
a\left(b - c\right) &\overset{\text{已知 1(a)}}{=}& 0 \\
a \neq 0, \quad b - c &\overset{\text{假設 1}}{\neq}& 0 \qquad \text{(因 } b \neq c\text{)} \\
a,\ b - c &\overset{\text{定義 1}}{=}& R \ \text{的零因子}
\end{gather*}$$

與【假設 1】的「$R$ 無零因子」矛盾。故消去律成立。

**($\Leftarrow$) 消去律成立推出無零因子。** 設 $ab = 0$ 且 $a \neq 0$：

$$\begin{gather*}
ab &=& 0 \\
ab &\overset{\text{已知 1(b)}}{=}& a \times 0 \\
b &=& 0 \qquad \text{(消去律，因 } a \neq 0\text{)}
\end{gather*}$$

兩個因子不可能同時非零，故依【定義 1】無零因子。

* 註：**這條命題是「零因子」這個概念的存在理由**。
  它說：在無零因子的環裡，你可以像在 $\mathbf{Z}$ 裡一樣「兩邊同除以 $a$」；
  一旦有零因子，這個從小用到大的動作就失效。
* 註：**注意這與群的消去律不同**。[唯一解與消去律](../Group/Unique_Solution_and_Cancellation_Law.md)
  的消去律靠的是 $a^{-1}$ **存在**；本檔的消去律靠的是**無零因子**。
  $\left(\mathbf{Z}, \times\right)$ 不是群（$2$ 沒有倒數）卻有消去律 ——
  兩個條件互相獨立，見文末。

+++

## 意義與密碼學關聯 (Interpretation and Relevance to Cryptography)

### 零因子是「壞掉的除法」

$\mathbf{Z}_6$ 裡這個式子成立：

$$2 \otimes 2 = 4 = 2 \otimes 5, \qquad \text{但} \quad 2 \neq 5$$

**兩邊都有 $2$，卻不能約掉。** 原因就是 $2$ 是零因子（【證明 (a)】），
依【證明 (c)】消去律必然失效。

對照 $\mathbf{Z}_7$（質數模，無零因子）：

$$2 \otimes b = 2 \otimes c \quad \Longrightarrow \quad b = c$$

約分永遠合法。**這就是密碼學一律用質數模的第一個理由。**

### 三個條件的階梯

本章到這裡出現了三個越來越強的乘法條件，很容易混淆：

| 條件 | 意思 | 例子 | 反例 |
|---|---|---|---|
| **無零因子** | $ab = 0 \Rightarrow a=0$ 或 $b=0$ | $\mathbf{Z}$、$\mathbf{Z}_p$ | $\mathbf{Z}_6$、$C(\mathbf{R})$ |
| **消去律** | $ab=ac,\ a \neq 0 \Rightarrow b=c$ | 同上（【證明 (c)】兩者等價） | 同上 |
| **有乘法反元素** | 每個 $a \neq 0$ 都有 $a^{-1}$ | $\mathbf{Q}$、$\mathbf{Z}_p$ | **$\mathbf{Z}$** |

**第三個嚴格強於前兩個**：$\mathbf{Z}$ 無零因子（可以約分）但沒有倒數（不能除）。
有反元素一定無零因子（若 $ab=0$ 且 $a \neq 0$，兩邊乘 $a^{-1}$ 得 $b=0$），反之不然。

前兩個條件成立的環叫 [整環](Integral_Domain.md)，三個都成立的叫 [體](../Field/Field_Definition.md)。

### $C(\mathbf{R})$ 的零因子：連續函數也會

[環的例子](Ring_Examples.md)【證明 (d)】提到 $C(\mathbf{R})$ 有零因子。具體構造：

$$f(x) = \max\left(0, -x\right), \qquad g(x) = \max\left(0, x\right)$$

兩者都連續、都不是零函數（$f(-1) = 1$、$g(1) = 1$），但

$$f(x)g(x) = 0 \qquad \text{for all } x \in \mathbf{R}$$

因為在任何一點，$f$ 與 $g$ 至少有一個是 $0$。**「各自在互補的區間上為零」是函數環產生零因子的標準手法。**

### 密碼學上的對應：RSA 的模數 $n = pq$ 一定有零因子

這是個關鍵的觀察。RSA 的模數是兩個質數的乘積，所以 $n$ **必然是合數**，
依【證明 (b)】$\mathbf{Z}_n$ **必然有零因子** —— 具體來說 $p$ 與 $q$ 就是一對：

$$p \otimes q = n \equiv 0 \pmod n$$

這不只是理論上的瑕疵，而是**RSA 安全性的核心**：

* 若攻擊者能找到 $\mathbf{Z}_n$ 的任何一對零因子，他就**分解了 $n$** ——
  因為零因子必定是 $n$ 的真因數的倍數，取 $\gcd$ 就能拆出 $p$ 或 $q$。
* 反過來說，「$\mathbf{Z}_n$ 的零因子難找」與「$n$ 難分解」是**同一件事**。

所以零因子在 RSA 裡有雙重身分：**它是 $\mathbf{Z}_n$ 的缺陷，同時也是 RSA 的安全基礎。**

實務上這也產生一個真實的攻擊面：若 RSA 實作在運算中不慎洩漏了某個
$\gcd(x, n) \neq 1$ 的中間值（例如透過錯誤訊息或時間差），$n$ 就被分解了。
這是 **fault attack** 的原理之一。

### 程式思維

```python
# Z_n 裡「除法」必須先檢查可逆性
def div_mod(a, b, n):
    try:
        return a * pow(b, -1, n) % n     # b 可逆才有意義
    except ValueError:
        raise ZeroDivisionError(f"{b} 在 Z_{n} 中不可逆（gcd({b},{n}) != 1）")

# 找零因子 == 分解 n
from math import gcd
def find_factor_from_zero_divisor(b, n):
    g = gcd(b, n)
    return g if 1 < g < n else None      # 拿到 n 的一個真因數
```

第二個函式就是上一段說的攻擊：**手上有一個零因子，就等於分解了 $n$**。
