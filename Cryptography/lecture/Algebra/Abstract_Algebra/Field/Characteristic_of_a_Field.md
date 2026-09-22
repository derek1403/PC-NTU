# Characteristic of a Field (體的特徵)

+++

## 證明目標:

`Algebra.pdf` p.46。體裡把 $1$ 一直加下去，有兩種結局：永遠加不到 $0$（特徵 $0$），
或走幾步就繞回 $0$（特徵 $p$）。投影片證明第二種情形的步數**必定是質數**。

* (a) 特徵的定義：

$$\mathrm{ch}(F) \overset{\text{def}}{=} \min\left\{p \in \mathbf{P} \ \middle|\ p \cdot 1_F = 0\right\} \ \text{（若存在），否則定為 } 0$$

* (b) **特徵若為正，則必為質數**（投影片唯一附完整 Proof 的定理之一）：

$$\mathrm{ch}(F) = p > 0 \quad \Longrightarrow \quad p \ \text{為質數}$$

* (c) 具體的特徵值：

$$\mathrm{ch}\!\left(\mathbf{Q}\right) = \mathrm{ch}\!\left(\mathbf{R}\right) = \mathrm{ch}\!\left(\mathbf{C}\right) = 0, \qquad \mathrm{ch}\!\left(\mathbf{Z}_p\right) = p$$

* (d) **有限體的特徵必為正**（投影片未列，但說明了特徵 $0$ 只能發生在無限體）。

* $F$ : 體的底層集合 (The underlying set of the field) $[\text{集合}]$
* $\mathrm{ch}(F)$ : $F$ 的特徵 (The characteristic of $F$) $[\mathrm{ch}(F) \in \mathbf{N}]$
* $1_F$ : $F$ 的乘法單位元素 (The multiplicative identity of $F$) $[1_F \in F]$
* $p$ : 特徵值 (The characteristic value) $[p \in \mathbf{N}]$
* $q_1,\ q_2$ : $p$ 的假定真因數 (Putative proper divisors of $p$) $[q_1, q_2 \in \mathbf{Z}]$
* 註：$p \cdot 1_F$ 裡的 $p$ 是**整數**、$1_F$ 是**體元素**，兩者相乘不是體的乘法 ——
  它是 [環的定義](../Ring/Ring_Definition.md)【定義 2(c)】的「加 $p$ 次」簡寫。
  這個區分是本檔的關鍵，【推導 1】處理它。
* 註：(b) 的核心是**體沒有零因子**（[體的定義](Field_Definition.md)【證明 (d)】）。
  換成一般的環，結論不成立 —— 例如 $\mathbf{Z}_6$ 的「特徵」是 $6$，不是質數。
* 註：特徵 $p$ 的體有一個驚人的性質，見 [新生之夢](Freshmans_Dream.md)。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [體的定義與體必為整環 (Field definition and fields are integral domains)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Field/Field_Definition.html#d-proof-that-every-field-is-an-integral-domain)：** 已於本章 [體的定義](Field_Definition.md)【定義 1】【證明 (b)(d)】給出並證明，此處直接引用不再重證

  * (a) 體的定義：

    $$F \ \text{為體} \quad \Longleftrightarrow \quad F \ \text{為交換含單位元環且每個非零元素可逆}$$

  * (b) 體無零因子：

    $$ab = 0 \quad \Longrightarrow \quad a = 0 \ \text{ 或 } \ b = 0$$

  * (c) 質數模的剩餘類環是體：

    $$\mathbf{Z}_p \ \text{為體} \quad \Longleftrightarrow \quad p \ \text{為質數}$$

  * $F$ : 體的底層集合 (The underlying set of the field) $[\text{集合}]$
  * $a,\ b$ : 體元素 (Field elements) $[a, b \in F]$
  * $p$ : 質數 (A prime) $[p \in \mathbf{P}]$
  * $\mathbf{Z}_p$ : 模 $p$ 剩餘類體 (The field of residues modulo $p$) $[\text{集合}]$

* **【已知 2】 [整數倍記號與分配律 (Integer multiple notation and distributivity)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Ring/Ring_Definition.html#definitions-and-notation)：** 已於本章 [環的定義](../Ring/Ring_Definition.md)【定義 1(d)】【定義 2(c)】給出，此處直接引用

  * (a) 分配律：

    $$a\left(b + c\right) = ab + ac, \qquad \left(a+b\right)c = ac + bc$$

  * (b) 整數倍：

    $$n \cdot a \overset{\text{def}}{=} \underbrace{a + a + \cdots + a}_{n \ \text{個}} \qquad \left(n \in \mathbf{P}\right)$$

  * $a,\ b,\ c$ : 環元素 (Ring elements) $[a, b, c \in R]$
  * $n$ : 正整數 (A positive integer) $[n \in \mathbf{P}]$
  * 註：(b) 的 $n$ **不是環的元素**，$n \cdot a$ 是簡寫不是乘法。
    這個區分在【推導 1】會變得很重要。

* **【已知 3】 [良序原理與鴿籠原理 (Well-ordering and pigeonhole principles)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Group/Order_of_Element_and_Cyclic_Subgroup.html#assumptions-preliminaries)：** 已於本章 [元素的階與循環子群](../Group/Order_of_Element_and_Cyclic_Subgroup.md)【已知 6(a)】【推導 1】與 [排列](../Group/Permutation.md)【已知 1(c)】引用，此處再次引用

  * (a) 良序原理：

    $$S \subseteq \mathbf{P},\ S \neq \varnothing \quad \Longrightarrow \quad S \ \text{有最小元素}$$

  * (b) 鴿籠原理：有限集合上無窮多個元素必有重複。

    $$\left|T\right| < \infty, \ \left\{x_1, x_2, \dots\right\} \subseteq T \quad \Longrightarrow \quad \exists\, i \neq j \ \text{ with } \ x_i = x_j$$

  * $S$ : 正整數的非空子集 (A non-empty subset of the positive integers) $[S \subseteq \mathbf{P}]$
  * $T$ : 有限集合 (A finite set) $[\text{集合}]$
  * $x_i$ : $T$ 中的元素 (Elements of $T$) $[x_i \in T]$
  * $i,\ j$ : 指標 (Indices) $[i, j \in \mathbf{P}]$

* **【已知 4】 [合數的定義 (Definition of a composite number)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Ring/Zero_Divisor.html#assumptions-preliminaries)：** 已於本章 [零因子](../Ring/Zero_Divisor.md)【已知 4】引用，此處再次引用

  $$n \ \text{為合數} \quad \Longleftrightarrow \quad n = q_1 q_2 \ \text{ with } \ 2 \le q_1 < n,\ 2 \le q_2 < n$$

  * $n$ : 被檢查的整數 (The integer under test) $[n \in \mathbf{P},\ n \ge 2]$
  * $q_1,\ q_2$ : 真因數 (Proper divisors) $[q_1, q_2 \in \mathbf{Z}]$

* **【定義 1】 體的特徵 (Characteristic of a field)：**

  $$\mathrm{ch}(F) \overset{\text{def}}{=} \begin{cases} \min\left\{p \in \mathbf{P} \ \middle|\ p \cdot 1_F = 0\right\}, & \text{若該集合非空} \\[2mm] 0, & \text{否則} \end{cases}$$

  * $\mathrm{ch}(F)$ : $F$ 的特徵 (The characteristic of $F$) $[\mathrm{ch}(F) \in \mathbf{N}]$
  * $F$ : 體的底層集合 (The underlying set of the field) $[\text{集合}]$
  * $1_F$ : $F$ 的乘法單位元素 (The multiplicative identity of $F$) $[1_F \in F]$
  * $p$ : 候選的特徵值 (A candidate characteristic) $[p \in \mathbf{P}]$
  * 註：最小值的存在性由【已知 3(a)】保證（集合非空時）。
  * 註：投影片的寫法是「the smallest positive integer $p$ such that $p \cdot 1_F = 0$ if such a $p$ exists,
    and is defined to be $0$ otherwise」，與本定義完全相同。

* **【假設 1】 反設：特徵是合數 (Proof by contradiction)：** 【證明 (b)】的出發點。
  依【已知 4】把 $p$ 拆成兩個真因數

  $$p = q_1 q_2 \qquad \text{with } 2 \le q_1 < p,\ 2 \le q_2 < p$$

  * $p$ : 體的特徵 (The characteristic of the field) $[p \in \mathbf{P}]$
  * $q_1,\ q_2$ : $p$ 的真因數 (Proper divisors of $p$) $[q_1, q_2 \in \mathbf{Z}]$
  * 註：投影片寫「Suppose not. Let $p = q_1q_2$, $q_1, q_2 \ge 2$」——
    本卡片補上了 $q_1, q_2 < p$ 這個從 $q_1q_2 = p$ 與 $q_i \ge 2$ 自動得到的界，
    因為【證明 (b)】的矛盾正是靠它與最小性衝突。

* **【推導 1】 整數倍可以拆成體的乘法 (Integer multiples factor as field products)：** 【證明 (b)】的樞紐。
  $\left(q_1 q_2\right) \cdot 1_F$ 這個「加 $q_1q_2$ 次」可以寫成兩個「加若干次」的**乘積**

  $$\begin{gather*}
  \left(q_1 \cdot 1_F\right)\left(q_2 \cdot 1_F\right) &\overset{\text{已知 2(b)}}{=}& \left(\underbrace{1_F + \cdots + 1_F}_{q_1}\right)\left(\underbrace{1_F + \cdots + 1_F}_{q_2}\right) \\
  \left(q_1 \cdot 1_F\right)\left(q_2 \cdot 1_F\right) &\overset{\text{已知 2(a)}}{=}& \underbrace{1_F \times 1_F + \cdots + 1_F \times 1_F}_{q_1 q_2 \ \text{項}} \\
  \left(q_1 \cdot 1_F\right)\left(q_2 \cdot 1_F\right) &\overset{\text{已知 1(a)}}{=}& \underbrace{1_F + \cdots + 1_F}_{q_1 q_2} \\
  \left(q_1 \cdot 1_F\right)\left(q_2 \cdot 1_F\right) &\overset{\text{已知 2(b)}}{=}& \left(q_1 q_2\right) \cdot 1_F
  \end{gather*}$$

  * $q_1,\ q_2$ : 正整數 (Positive integers) $[q_1, q_2 \in \mathbf{P}]$
  * $1_F$ : $F$ 的乘法單位元素 (The multiplicative identity of $F$) $[1_F \in F]$
  * $F$ : 體的底層集合 (The underlying set of the field) $[\text{集合}]$
  * 註：第二行是**把分配律展開 $q_1 \times q_2$ 次**的結果 ——
    左括號的每一項都要乘到右括號的每一項，共 $q_1 q_2$ 個 $1_F \times 1_F$。
  * 註：第三行用了 $1_F \times 1_F = 1_F$（單位元素性質）。
  * 註：**這張卡片是整條證明的橋** —— 它把「整數的乘法 $q_1q_2$」翻譯成「體的乘法」，
    這樣才能套用「體無零因子」。

+++

## 證明:

### (a) verify the characteristic of the residues modulo a prime

由【定義 1】，要找最小的 $n$ 使 $n \cdot 1 = 0$ 在 $\mathbf{Z}_p$ 中成立。
$\mathbf{Z}_p$ 的 $1_F$ 就是數字 $1$，故 $n \cdot 1 = n \bmod p$：

$$\begin{gather*}
n \cdot 1 &\overset{\text{已知 2(b)}}{=}& \underbrace{1 + \cdots + 1}_{n} = n \bmod p \\
n \bmod p = 0 &\Longleftrightarrow& p \mid n \\
\min\left\{n \in \mathbf{P} \ \middle|\ p \mid n\right\} &=& p \\
\mathrm{ch}\!\left(\mathbf{Z}_p\right) &\overset{\text{定義 1}}{=}& p
\end{gather*}$$

與投影片一致。

### (b) proof that a positive characteristic must be prime

設 $\mathrm{ch}(F) = p > 0$。反設 $p$ 為合數（【假設 1】），把它拆成 $q_1 q_2$。
用【推導 1】把整數的拆解翻譯成體的乘法：

$$\begin{gather*}
0 &\overset{\text{定義 1}}{=}& p \cdot 1_F \\
p &\overset{\text{已知 4}}{=}& q_1 q_2 \\
0 &\overset{\text{假設 1}}{=}& \left(q_1 q_2\right) \cdot 1_F \\
0 &\overset{\text{推導 1}}{=}& \left(q_1 \cdot 1_F\right)\left(q_2 \cdot 1_F\right)
\end{gather*}$$

$F$ 是體故無零因子（【已知 1(b)】），兩個因子至少有一個是 $0$：

$$\begin{gather*}
q_1 \cdot 1_F = 0 \ \text{ 或 } \ q_2 \cdot 1_F &\overset{\text{已知 1(b)}}{=}& 0 \\
2 \le q_1 < p, \quad 2 \le q_2 &\overset{\text{假設 1}}{<}& p
\end{gather*}$$

但這表示**存在一個比 $p$ 更小的正整數也把 $1_F$ 送到 $0$**，與【定義 1】的最小性矛盾。
故 $p$ 不可能是合數，必為質數。

與投影片的 Proof 逐步對應：

| 投影片 | 本檔 |
|---|---|
| Suppose not. Let $p = q_1q_2$, $q_1,q_2 \ge 2$ | 【假設 1】 |
| $0 = p\cdot 1_F = (q_1q_2)\cdot 1_F = (q_1\cdot 1_F)(q_2\cdot 1_F)$ | 【推導 1】＋第一段 |
| $\therefore q_1\cdot 1_F = 0$ or $q_2\cdot 1_F = 0$ | 第二段第一行（靠【已知 1(b)】） |
| contradicting to the minimality of $p$ | 第二段第二行 |

* 註：**投影片沒有明說的兩件事**，本檔補上了：
  (i) 從 $\left(q_1\cdot 1_F\right)\left(q_2\cdot 1_F\right) = 0$ 推到「其中之一為 $0$」
  用的是**體無零因子**（【已知 1(b)】）—— 這是體這個前提唯一被用到的地方；
  (ii) $q_1, q_2 < p$ 這個界，否則談不上「與最小性矛盾」。
* 註：**把「體」換成「環」結論就不成立**。$\mathbf{Z}_6$ 作為環的特徵是 $6$（合數）——
  因為它有零因子，$2 \cdot 1 = 2 \neq 0$、$3 \cdot 1 = 3 \neq 0$，
  但 $\left(2 \cdot 1\right)\left(3 \cdot 1\right) = 6 = 0$。

### (c) verify the characteristic of the infinite number fields

$\mathbf{Q}, \mathbf{R}, \mathbf{C}$ 的 $1_F$ 就是數字 $1$，而 $n \cdot 1 = n$：

$$\begin{gather*}
n \cdot 1 &\overset{\text{已知 2(b)}}{=}& n \\
n &\neq& 0 \qquad \text{for all } n \in \mathbf{P} \\
\left\{n \in \mathbf{P} \ \middle|\ n \cdot 1 = 0\right\} &=& \varnothing \\
\mathrm{ch}\!\left(\mathbf{Q}\right) = \mathrm{ch}\!\left(\mathbf{R}\right) = \mathrm{ch}\!\left(\mathbf{C}\right) &\overset{\text{定義 1}}{=}& 0
\end{gather*}$$

* 註：**特徵 $0$ 不代表「$0 \cdot 1 = 0$」**，而是「**沒有任何正整數**能把 $1$ 加成 $0$」。
  $0$ 只是這種情形的約定記號。

### (d) proof that a finite field has positive characteristic

設 $F$ 有限。考慮 $1_F, 2 \cdot 1_F, 3 \cdot 1_F, \dots$ 這個無窮序列，
由鴿籠原理必有重複：

$$\begin{gather*}
\left|F\right| &<& \infty \\
\exists\, i < j \ \text{ with } \ i \cdot 1_F &\overset{\text{已知 3(b)}}{=}& j \cdot 1_F \\
j \cdot 1_F - i \cdot 1_F &=& 0 \\
\left(j - i\right) \cdot 1_F &\overset{\text{已知 2(b)}}{=}& 0 \\
j - i &\in& \mathbf{P} \\
\left\{n \in \mathbf{P} \ \middle|\ n \cdot 1_F = 0\right\} &\neq& \varnothing \\
\mathrm{ch}(F) &\overset{\text{定義 1,已知 3(a)}}{>}& 0
\end{gather*}$$

配合【證明 (b)】，**有限體的特徵必定是某個質數 $p$**。

* 註：這與 [元素的階與循環子群](../Group/Order_of_Element_and_Cyclic_Subgroup.md)【推導 1】
  的論證**逐字相同**（鴿籠 + 相減），只是那裡處理的是乘法群的階、這裡是加法的特徵。

+++

## 意義與密碼學關聯 (Interpretation and Relevance to Cryptography)

### 特徵是「$1$ 走幾步繞回 $0$」

特徵的直覺是**把 $1$ 一直加下去的軌跡**：

$$1 \to 2 \to 3 \to \cdots$$

* 在 $\mathbf{Q}$ 裡走不完，永遠到不了 $0$ $\Rightarrow$ $\mathrm{ch} = 0$；
* 在 $\mathbf{Z}_7$ 裡走七步繞回 $0$ $\Rightarrow$ $\mathrm{ch} = 7$。

【證明 (d)】說有限體一定會繞回來（位置有限，走著走著必定重複）。
【證明 (b)】說繞回來的步數一定是質數 —— 因為若能拆成 $q_1 \times q_2$，
就會在更早的 $q_1$ 步或 $q_2$ 步就繞回去了。

### 密碼學只用兩種特徵

實務上幾乎只會遇到兩種：

| 特徵 | 體 | 用在哪 |
|---|---|---|
| $2$ | $GF(2)$、$GF(2^8)$、$GF(2^{128})$ | AES、GCM、CRC、LFSR |
| 大質數 $p$ | $GF(p)$、$GF(p^2)$ | RSA、DH、ECC、Kyber |

**特徵 $2$ 的體在硬體上特別好實作**，因為：

* 加法 $=$ XOR（$1 + 1 = 0$，沒有進位）；
* $-a = a$（由 [環的基本命題](../Ring/Ring_Basic_Propositions.md) 文末，$\mathrm{ch} = 2$ 時 $-1 = 1$）；
* 加法與減法是**同一個運算**。

AES 的每一個「加法」都是一行 XOR，沒有任何進位邏輯 ——
這讓它在 8 位元微控制器上也跑得動。**這個效率優勢直接來自特徵是 $2$。**

### 特徵 $p$ 的體有「新生之夢」

特徵為 $p$ 時會出現一個在實數裡絕不可能的等式：

$$\left(a + b\right)^p = a^p + b^p$$

高中生最愛犯的錯誤，在特徵 $p$ 的體裡**是對的**。
證明見 [新生之夢](Freshmans_Dream.md)，它依賴 [質數整除二項式係數](Prime_Divides_Binomial_Coefficient.md)，
而後者又依賴本檔的「特徵必為質數」。

這個性質在密碼學裡不是趣聞 —— 它是 **Frobenius 自同態**的基礎，
而 Frobenius 映射用在橢圓曲線的點計數（Schoof 演算法）與配對密碼學裡。

### 為什麼 $\mathbf{Z}_6$ 不算

【證明 (b)】的註指出 $\mathbf{Z}_6$ 的「特徵」是合數 $6$。
這不是定理的反例，而是**前提不滿足** —— $\mathbf{Z}_6$ 不是體（有零因子）。

這再次說明 [零因子](../Ring/Zero_Divisor.md) 的重要性：
**無零因子是一切「從乘積為零推出某個因子為零」的論證的前提**，
而這類論證在代數裡無所不在。

### 程式思維

```python
def characteristic(add_one, zero, one, limit=10**6):
    """把 1 一直加下去，看幾步回到 0。回傳 0 表示特徵為 0（在 limit 內沒繞回）。"""
    x, n = one, 1
    while x != zero:
        x = add_one(x)
        n += 1
        if n > limit:
            return 0
    return n

# Z_7: 特徵 7
assert characteristic(lambda x: (x + 1) % 7, 0, 1) == 7
# GF(2^8): 特徵 2（加法是 XOR，1 XOR 1 = 0）
assert characteristic(lambda x: x ^ 1, 0, 1) == 2
```

第二個斷言展示了 $GF(2^8)$ 的特徵是 $2$ 而不是 $256$ ——
**特徵看的是加法的週期，不是元素個數**。
$GF(2^8)$ 有 $256$ 個元素但特徵只有 $2$，兩者不可混為一談。
