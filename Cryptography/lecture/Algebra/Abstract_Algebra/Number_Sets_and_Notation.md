# Number Sets and Notation (數系與符號約定)

+++

## 本檔目標:

把 `Algebra.pdf` p.2 的符號約定攤開成一組可被引用的**【定義】卡片**。
本章其他所有檔案凡是用到 $\mathbf{Z}_n$、$\mathbf{Z}_n^*$、$GL_n$、$SL_n$ 等記號，
一律以 `\overset{\text{已知 N}}{=}` 回溯到本檔，**不再重複定義**。

* (a) 本檔給出七組符號：$\mathbf{Z}$、$\mathbf{N}$ 與 $\mathbf{P}$、$\mathbf{Z}_n$、$\mathbf{Z}_n^*$、
  $\mathbf{Q}, \mathbf{R}, \mathbf{C}$ 與 $\mathbf{Q}^*, \mathbf{R}^*, \mathbf{C}^*$、$GL_n(R)$、$SL_n(R)$。
* (b) 並驗證投影片給的例子：

$$\mathbf{Z}_{12}^* = \left\{1,\ 5,\ 7,\ 11\right\}$$

* 註：本檔**只有定義與驗證，沒有定理**。$\mathbf{Z}_n$ 與 $\mathbf{Z}_n^*$ 各自在什麼運算下構成群，
  是 [群的正例與反例](Group/Group_Examples_and_Counterexamples.md) 的工作，不在此處證明。
* 註：投影片用粗體 $\mathbf{Z}$ 表示整數集合，本章沿用此慣例；型別欄中出現的 $\mathbb{Z}$ 指同一個集合，
  粗體用於數學式內、空心體用於型別標註。
* 註（**dangling 標註**）：本檔的【定義 1】【定義 2】【定義 3】【定義 5】【定義 6】【定義 7】
  與【已知 3】【已知 4】在本檔內**不會**被 `\overset` 引用 —— 它們的用途是供**其他檔案**引用。
  這是刻意的，不是引用鏈斷裂。本檔唯一被內部引用的是【定義 4】（用於【驗證 (a)】）。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [整除與最大公因數 (Divisibility and the greatest common divisor)](https://mathworld.wolfram.com/GreatestCommonDivisor.html)：** 初等數論的標準記號，本章直接引用不再重證

  * (a) 整除：

    $$m \mid k \quad \overset{\text{def}}{\Longleftrightarrow} \quad \exists\, t \in \mathbf{Z} \ \text{ such that } \ k = mt$$

  * (b) 最大公因數：

    $$\gcd(a, n) \overset{\text{def}}{=} \max\left\{d \in \mathbf{P} \ \middle|\ d \mid a \ \text{ and } \ d \mid n\right\}$$

  * (c) 互質：

    $$a \ \text{與} \ n \ \text{互質} \quad \overset{\text{def}}{\Longleftrightarrow} \quad \gcd(a, n) = 1$$

  * $m,\ k$ : 任意整數 (Arbitrary integers) $[m, k \in \mathbf{Z}]$
  * $t$ : 整數倍數 (Integer multiplier) $[t \in \mathbf{Z}]$
  * $a$ : 被檢查的整數 (The integer under test) $[a \in \mathbf{Z}]$
  * $n$ : 模數 (Modulus) $[n \in \mathbf{P}]$
  * $d$ : 公因數 (Common divisor) $[d \in \mathbf{P}]$
  * $\gcd$ : 最大公因數 (Greatest common divisor) $[\mathbf{Z} \times \mathbf{Z} \to \mathbf{N}]$
  * 註：輾轉相除法與貝祖等式屬於 [Arithmetic](../Arithmatic/Arithmetic.ipynb) 的範圍，本章只用其結果。

* **【已知 2】 [同餘 (Congruence modulo $n$)](https://mathworld.wolfram.com/Congruence.html)：** 標準記號，本章直接引用不再重證

  $$a \equiv b \pmod{n} \quad \overset{\text{def}}{\Longleftrightarrow} \quad n \mid (a - b)$$

  * $a,\ b$ : 任意整數 (Arbitrary integers) $[a, b \in \mathbf{Z}]$
  * $n$ : 模數 (Modulus) $[n \in \mathbf{P}]$

* **【已知 3】 [模逆元存在的充要條件 (Criterion for the existence of a modular inverse)](https://mathworld.wolfram.com/ModularInverse.html)：** 貝祖等式的直接推論，屬初等數論，本章直接引用不再重證

  $$\exists\, b \in \mathbf{Z}_n \ \text{ such that } \ ab \equiv 1 \pmod{n} \quad \Longleftrightarrow \quad \gcd(a, n) = 1$$

  * $a$ : 被檢查的整數 (The integer under test) $[a \in \mathbf{Z}_n]$
  * $b$ : $a$ 的模逆元 (The modular inverse of $a$) $[b \in \mathbf{Z}_n]$
  * $n$ : 模數 (Modulus) $[n \in \mathbf{P}]$
  * $\gcd$ : 最大公因數 (Greatest common divisor) $[\mathbf{Z} \times \mathbf{Z} \to \mathbf{N}]$
  * 註：這一條是【定義 4】為什麼要用 $\gcd(a,n) = 1$ 當篩選條件的**唯一理由**。

* **【已知 4】 [矩陣行列式的乘法性 (Multiplicativity of the determinant)](https://mathworld.wolfram.com/Determinant.html)：** 線性代數的標準結果，本章直接引用不再重證。$GL_n$ 與 $SL_n$ 的封閉性都靠這一條

  $$\det\left(AB\right) = \det\left(A\right)\det\left(B\right)$$

  * $A,\ B$ : $n \times n$ 方陣 (Square matrices of size $n$) $[A, B \in M_n(R)]$
  * $\det$ : 行列式 (Determinant) $[M_n(R) \to R]$
  * $M_n(R)$ : 係數取自 $R$ 的 $n \times n$ 方陣全體 (All $n \times n$ matrices over $R$) $[\text{集合}]$
  * $R$ : 係數所在的環 (The coefficient ring) $[\text{環}]$
  * $n$ : 矩陣的邊長 (Matrix size) $[n \in \mathbb{Z}^{+}]$

+++

## 定義與符號 (Definitions and Notation)

* **【定義 1】 整數集合 (The set of integers)：**

  $$\mathbf{Z} \overset{\text{def}}{=} \left\{\dots,\ -3,\ -2,\ -1,\ 0,\ 1,\ 2,\ 3,\ \dots\right\}$$

  * $\mathbf{Z}$ : 整數集合 (The set of integers) $[\text{集合}]$

* **【定義 2】 非負整數與正整數 (Non-negative integers and positive integers)：**

  * (a) 非負整數：

    $$\mathbf{N} \overset{\text{def}}{=} \left\{0,\ 1,\ 2,\ 3,\ \dots\right\}$$

  * (b) 正整數：

    $$\mathbf{P} \overset{\text{def}}{=} \left\{1,\ 2,\ 3,\ \dots\right\}$$

  * $\mathbf{N}$ : 非負整數集合 (The set of non-negative integers) $[\text{集合}]$
  * $\mathbf{P}$ : 正整數集合 (The set of positive integers) $[\text{集合}]$
  * 註：兩者只差一個 $0$，但在 [群的正例與反例](Group/Group_Examples_and_Counterexamples.md) 裡是決定性的：
    $\left(\mathbf{P}, +\right)$ 因為缺 $0$ 而沒有單位元素，不是群。

* **【定義 3】 模 $n$ 剩餘類集合 (The set of residues modulo $n$)：** 把無限長的整數線捲成一個長度 $n$ 的圓環

  $$\mathbf{Z}_n \overset{\text{def}}{=} \left\{0,\ 1,\ 2,\ \dots,\ n-1\right\}$$

  * $\mathbf{Z}_n$ : 模 $n$ 剩餘類集合 (The set of residues modulo $n$) $[\text{集合}]$
  * $n$ : 模數 (Modulus) $[n \in \mathbf{P}]$
  * 註：$\mathbf{Z}_n$ 的元素嚴格來說是**同餘類** $\bar{a} = \left\{a + kn \mid k \in \mathbf{Z}\right\}$，
    這裡依投影片慣例以代表元 $0, 1, \dots, n-1$ 書寫。嚴格的同餘類觀點見
    [模理想的同餘類](Ring/Congruence_Class_Modulo_Ideal.md)。
  * 註：$\mathbf{Z}_n$ 預設配的運算是**模 $n$ 加法**與**模 $n$ 乘法**，後者在本章記作 $\otimes$。

* **【定義 4】 模 $n$ 可逆剩餘類集合 (The set of units modulo $n$)：** $\mathbf{Z}_n$ 裡與 $n$ 互質的那些元素

  $$\mathbf{Z}_n^* \overset{\text{def}}{=} \left\{a \in \mathbf{Z}_n \ \middle|\ \gcd(a, n) = 1\right\}$$

  * $\mathbf{Z}_n^*$ : 模 $n$ 可逆剩餘類集合 (The set of units modulo $n$) $[\text{集合}]$
  * $\mathbf{Z}_n$ : 模 $n$ 剩餘類集合 (The set of residues modulo $n$) $[\text{集合}]$
  * $a$ : 剩餘類代表元 (Residue representative) $[a \in \mathbf{Z}_n]$
  * $n$ : 模數 (Modulus) $[n \in \mathbf{P}]$
  * $\gcd$ : 最大公因數 (Greatest common divisor) $[\mathbf{Z} \times \mathbf{Z} \to \mathbf{N}]$
  * 註：星號 $*$ 在本章一律代表「**取出乘法可逆的元素**」。由【已知 3】，$\gcd(a,n)=1$ 正是
    $a$ 在模 $n$ 下存在乘法反元素的充要條件，故 $\mathbf{Z}_n^*$ 恰是 $\mathbf{Z}_n$ 中乘法可逆的元素全體。
  * 註：$\left|\mathbf{Z}_n^*\right| = \varphi(n)$ 見 [群的階](Group/Group_Order.md)。

* **【定義 5】 有理數、實數、複數 (Rational, real, and complex numbers)：**

  * (a) 三個數系：

    $$\mathbf{Q} \overset{\text{def}}{=} \left\{\frac{p}{q} \ \middle|\ p \in \mathbf{Z},\ q \in \mathbf{Z},\ q \neq 0\right\}, \qquad \mathbf{C} \overset{\text{def}}{=} \left\{a + bi \ \middle|\ a \in \mathbf{R},\ b \in \mathbf{R}\right\}$$

  * (b) 去掉零元素後的集合：

    $$\mathbf{Q}^* \overset{\text{def}}{=} \mathbf{Q} \setminus \left\{0\right\}, \qquad \mathbf{R}^* \overset{\text{def}}{=} \mathbf{R} \setminus \left\{0\right\}, \qquad \mathbf{C}^* \overset{\text{def}}{=} \mathbf{C} \setminus \left\{0\right\}$$

  * $\mathbf{Q},\ \mathbf{R},\ \mathbf{C}$ : 有理數、實數、複數集合 (The sets of rational, real, and complex numbers) $[\text{集合}]$
  * $\mathbf{Q}^*,\ \mathbf{R}^*,\ \mathbf{C}^*$ : 對應的非零元素集合 (The corresponding sets of non-zero elements) $[\text{集合}]$
  * $p,\ q$ : 分子與分母 (Numerator and denominator) $[p, q \in \mathbf{Z}]$
  * $a,\ b$ : 複數的實部與虛部 (Real and imaginary parts) $[a, b \in \mathbf{R}]$
  * $i$ : 虛數單位 (Imaginary unit) $[i \in \mathbf{C}]$，$i^2 = -1$
  * 註：$\mathbf{R}$ 取標準的實數集合，本章不涉及其由 $\mathbf{Q}$ 完備化的構造。
  * 註：加星號的理由與【定義 4】一致 —— **取出乘法可逆的元素**。
    在 $\mathbf{Q}, \mathbf{R}, \mathbf{C}$ 中唯一不可逆的元素就是 $0$。

* **【定義 6】 一般線性群 (General linear group)：** 係數取自 $R$ 的 $n \times n$ **可逆**矩陣全體

  $$GL_n(R) \overset{\text{def}}{=} \left\{A \in M_n(R) \ \middle|\ \det\left(A\right) \ \text{在} \ R \ \text{中可逆}\right\}$$

  * $GL_n(R)$ : 一般線性群 (General linear group) $[\text{集合}]$
  * $M_n(R)$ : 係數取自 $R$ 的 $n \times n$ 方陣全體 (All $n \times n$ matrices over $R$) $[\text{集合}]$
  * $A$ : 一個方陣 (A square matrix) $[A \in M_n(R)]$
  * $R$ : 係數所在的環 (The coefficient ring) $[\text{環}]$
  * $n$ : 矩陣的邊長 (Matrix size) $[n \in \mathbb{Z}^{+}]$
  * $\det$ : 行列式 (Determinant) $[M_n(R) \to R]$
  * 註：當 $R$ 是體時（如 $\mathbf{R}$、$\mathbf{Q}$、$\mathbf{Z}_p$），「$\det(A)$ 可逆」退化成
    $\det(A) \neq 0$，即投影片的寫法。$R$ 不是體時（如 $\mathbf{Z}$）兩者不等價，故此處採可逆的寫法。
  * 註：$GL_n(R)$ 配矩陣乘法構成群，且 $n \ge 2$ 時**非交換**，見
    [阿貝爾群與非阿貝爾群](Group/Abelian_and_Non_Abelian_Group.md)；其階的計數見
    [一般線性群的階](Group/General_Linear_Group_Order.md)。

* **【定義 7】 特殊線性群 (Special linear group)：** $GL_n(R)$ 中行列式恰為 $1$ 的那些矩陣

  $$SL_n(R) \overset{\text{def}}{=} \left\{A \in GL_n(R) \ \middle|\ \det\left(A\right) = 1\right\}$$

  * $SL_n(R)$ : 特殊線性群 (Special linear group) $[\text{集合}]$
  * $GL_n(R)$ : 一般線性群 (General linear group) $[\text{集合}]$
  * $A$ : 一個方陣 (A square matrix) $[A \in GL_n(R)]$
  * $\det$ : 行列式 (Determinant) $[M_n(R) \to R]$
  * $R$ : 係數所在的環 (The coefficient ring) $[\text{環}]$
  * $n$ : 矩陣的邊長 (Matrix size) $[n \in \mathbb{Z}^{+}]$
  * 註：$SL_n(R)$ 是 $GL_n(R)$ 的子群（見 [子群的例子](Group/Subgroup_Examples.md)），
    其指標的計算見 [特殊線性群的指標](Group/Special_Linear_Subgroup_Index.md)。

+++

## 驗證:

### (a) verify the set of units modulo twelve

投影片 p.2 給的例子是 $\mathbf{Z}_{12}^* = \left\{1, 5, 7, 11\right\}$。依【定義 4】，
逐一算出 $\mathbf{Z}_{12}$ 十二個元素與 $12$ 的最大公因數：

$$\begin{gather*}
\gcd(0, 12)  &\overset{\text{已知 1(b)}}{=}& 12 \\
\gcd(1, 12)  &\overset{\text{已知 1(b)}}{=}& 1 \\
\gcd(2, 12)  &\overset{\text{已知 1(b)}}{=}& 2 \\
\gcd(3, 12)  &\overset{\text{已知 1(b)}}{=}& 3 \\
\gcd(4, 12)  &\overset{\text{已知 1(b)}}{=}& 4 \\
\gcd(5, 12)  &\overset{\text{已知 1(b)}}{=}& 1 \\
\gcd(6, 12)  &\overset{\text{已知 1(b)}}{=}& 6 \\
\gcd(7, 12)  &\overset{\text{已知 1(b)}}{=}& 1 \\
\gcd(8, 12)  &\overset{\text{已知 1(b)}}{=}& 4 \\
\gcd(9, 12)  &\overset{\text{已知 1(b)}}{=}& 3 \\
\gcd(10, 12) &\overset{\text{已知 1(b)}}{=}& 2 \\
\gcd(11, 12) &\overset{\text{已知 1(b)}}{=}& 1
\end{gather*}$$

取出 $\gcd = 1$ 的那些代表元：

$$\begin{gather*}
\mathbf{Z}_{12}^* &\overset{\text{定義 4}}{=}& \left\{a \in \mathbf{Z}_{12} \ \middle|\ \gcd(a, 12) = 1\right\} \\
&\overset{\text{驗證 (a)}}{=}& \left\{1,\ 5,\ 7,\ 11\right\}
\end{gather*}$$

與投影片一致。

### (b) verify that the units are exactly the invertible residues

由【已知 3】，$\mathbf{Z}_{12}^*$ 的四個元素應該都在模 $12$ 乘法下可逆。直接把反元素找出來：

$$\begin{gather*}
1 \times 1   &=& 1 \\
1            &\overset{\text{已知 2}}{\equiv}& 1 \pmod{12} \\
5 \times 5   &=& 25 \\
25           &\overset{\text{已知 2}}{\equiv}& 1 \pmod{12} \\
7 \times 7   &=& 49 \\
49           &\overset{\text{已知 2}}{\equiv}& 1 \pmod{12} \\
11 \times 11 &=& 121 \\
121          &\overset{\text{已知 2}}{\equiv}& 1 \pmod{12}
\end{gather*}$$

四個元素都是自己的反元素，可逆性確認。反方向（$\gcd(a,12) > 1$ 的元素必不可逆）由【已知 3】直接給出，
不需另證。

+++

## 意義與密碼學關聯 (Interpretation and Relevance to Cryptography)

### $\mathbf{Z}_n$ 與 $\mathbf{Z}_n^*$ 是密碼學最常出現的兩個集合

幾乎所有公鑰密碼系統都活在這兩個集合裡，而且**用的是不同的那一個**：

* $\mathbf{Z}_n$ 配**加法**是一個群，$n$ 取任意正整數都成立。
* $\mathbf{Z}_n$ 配**乘法不是**群 —— $0$ 沒有反元素，$\gcd(a,n) > 1$ 的元素也沒有。
  把這些壞元素全部丟掉，剩下的才是 $\mathbf{Z}_n^*$，它配乘法才是群。

RSA 的公鑰指數 $e$ 必須滿足 $\gcd\left(e, \varphi(n)\right) = 1$，正是為了讓 $e \in \mathbf{Z}_{\varphi(n)}^*$，
這樣才找得到私鑰 $d$ 使 $ed \equiv 1 \pmod{\varphi(n)}$。
**「有沒有乘法反元素」這件事，就是 RSA 能不能解密的全部。**

### 程式思維

| 數學記號 | Python 對應 |
|---|---|
| $\mathbf{Z}$ | `int`（Python 的整數沒有位數上限） |
| $\mathbf{Z}_n$ | `range(n)`，或所有 `x % n` 的可能結果 |
| $\mathbf{Z}_n^*$ | `[a for a in range(n) if math.gcd(a, n) == 1]` |
| $\varphi(n)$ | `sympy.totient(n)` |
| $a \equiv b \pmod n$ | `a % n == b % n` |
| $a$ 在模 $n$ 下的反元素 | `pow(a, -1, n)`（Python 3.8+） |

`pow(a, -1, n)` 在 $\gcd(a,n) \neq 1$ 時會丟出 `ValueError`。這不是實作瑕疵，而是忠實反映了【已知 3】：
**$a \notin \mathbf{Z}_n^*$ 時反元素根本不存在。**

### 為什麼要區分 $\mathbf{N}$ 與 $\mathbf{P}$

差一個 $0$ 而已，但在群論裡是生死之別：$\left(\mathbf{N}, +\right)$ 有單位元素 $0$ 卻沒有反元素；
$\left(\mathbf{P}, +\right)$ 連單位元素都沒有。兩者都不是群 —— 但**壞掉的原因不同**，
這正是 [群的正例與反例](Group/Group_Examples_and_Counterexamples.md) 要逐條檢查的東西。

### $GL$ 與 $SL$ 為什麼值得單獨命名

這兩個是本章唯一的**非交換**群，用來說明「群不必滿足交換律」最省事。
而且它們在密碼學裡不是裝飾品：AES 的 S-box 仿射變換用的就是一個 $GL_8(\mathbf{Z}_2)$ 的元素
（見 [一般線性群的階](Group/General_Linear_Group_Order.md)）。
