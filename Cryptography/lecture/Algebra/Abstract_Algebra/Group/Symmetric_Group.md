# Symmetric Group (對稱群)

+++

## 證明目標:

`Algebra.pdf` p.10。把 [排列](Permutation.md) 全部收集起來，配上合成運算，就得到本章第一個
**具體而且非交換**的群。

* (a) $\left(S_n, \circ\right)$ 是群：

$$S_n = \left\{f \ \middle|\ f \ \text{是} \ \left\{1, 2, \dots, n\right\} \ \text{上的排列}\right\}$$

* (b) 對稱群的階：

$$\left|S_n\right| = n!$$

* (c) 驗證投影片 p.10 的兩個計算：

$$\begin{pmatrix} 1 & 2 & 3 \\ 2 & 3 & 1 \end{pmatrix} \circ \begin{pmatrix} 1 & 2 & 3 \\ 2 & 3 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 2 & 3 \\ 3 & 1 & 2 \end{pmatrix}, \qquad \left(123\right)^{-1} = \left(132\right)$$

* $S_n$ : $n$ 次對稱群 (The symmetric group on $n$ letters) $[\text{集合}]$
* $n$ : 被排列的元素個數 (The number of letters) $[n \in \mathbf{P}]$
* $\circ$ : 函數合成 (Function composition) $[S_n \times S_n \to S_n]$
* $f$ : 一個排列 (A permutation) $[f \in S_n]$
* $\left|S_n\right|$ : $S_n$ 的階 (The order of $S_n$) $[\left|S_n\right| \in \mathbf{P}]$
* 註：$S_n$ 在 $n \ge 3$ 時**非交換**，反例見 [阿貝爾群與非阿貝爾群](Abelian_and_Non_Abelian_Group.md)【證明 (a)】。
  本檔只證它是群，不證它交換（因為不交換）。
* 註：(b) 的結果會在 [群的階](Group_Order.md) 被引用（$\left|S_3\right| = 6$、$\left|S_4\right| = 24$）。
* 註：AES 的 S-box 是 $S_{256}$ 的一個元素 —— 這是本檔與密碼學最直接的連結，見文末。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [群的公理 (Group axioms)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Group/Group_Definition.html#definitions-and-notation)：** 已於本章 [群的定義](Group_Definition.md)【定義 2】給出，此處直接引用

  * (a) 封閉性：$a * b \in G$；(b) 結合律：$a * \left(b * c\right) = \left(a * b\right) * c$；
    (c) 單位元素：$a * e = e * a = a$；(d) 反元素：$a * b = b * a = e$

    $$\text{Closure}, \quad \text{Associativity}, \quad \text{Identity}, \quad \text{Inverse}$$

  * $G$ : 群的底層集合 (The underlying set of the group) $[\text{集合}]$
  * $*$ : 群運算 (Group operation) $[G \times G \to G]$
  * $a,\ b,\ c$ : 群元素 (Group elements) $[a, b, c \in G]$
  * $e$ : 單位元素 (The identity element) $[e \in G]$

* **【已知 2】 [排列的定義與合成封閉性 (Permutations and closure under composition)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Group/Permutation.html#b-proof-that-the-composition-of-two-permutations-is-a-permutation)：** 已於本章 [排列](Permutation.md) 完整證明，此處直接引用不再重證

  * (a) 排列的定義：

    $$f \ \text{是 } T \text{ 上的排列} \quad \overset{\text{def}}{\Longleftrightarrow} \quad f : T \to T \ \text{ 為雙射}$$

  * (b) 合成的封閉性（【排列】【證明 (b)】）：

    $$f, g \ \text{皆為 } T \text{ 上的排列} \quad \Longrightarrow \quad f \circ g \ \text{亦為 } T \text{ 上的排列}$$

  * (c) 合成的定義：

    $$\left(f \circ g\right)(x) \overset{\text{def}}{=} f\left(g(x)\right)$$

  * $T$ : 被排列的集合 (The set being permuted) $[\text{集合}]$
  * $f,\ g$ : $T$ 上的排列 (Permutations of $T$) $[T \to T]$
  * $x$ : 定義域中的元素 (An element of the domain) $[x \in T]$
  * $\circ$ : 函數合成 (Function composition) $[\left(T \to T\right) \times \left(T \to T\right) \to \left(T \to T\right)]$

* **【已知 3】 [雙射的反函數存在 (Existence of the inverse function of a bijection)](https://mathworld.wolfram.com/Bijection.html)：** 集合論的標準結果，本章直接引用不再重證

  $$f : T \to T \ \text{ 為雙射} \quad \Longrightarrow \quad \exists\, f^{-1} : T \to T \ \text{ 為雙射，且 } \ f \circ f^{-1} = f^{-1} \circ f = \mathrm{id}_T$$

  * $f$ : 一個雙射 (A bijection) $[T \to T]$
  * $f^{-1}$ : $f$ 的反函數 (The inverse function of $f$) $[T \to T]$
  * $\mathrm{id}_T$ : $T$ 上的恆等函數 (The identity function on $T$) $[T \to T]$，$\mathrm{id}_T(x) = x$
  * $T$ : 集合 (A set) $[\text{集合}]$

* **【定義 1】 對稱群 (Symmetric group)：** 把 $\left\{1, 2, \dots, n\right\}$ 上的排列**全部**收集起來

  $$S_n \overset{\text{def}}{=} \left\{f \ \middle|\ f : \left\{1, 2, \dots, n\right\} \to \left\{1, 2, \dots, n\right\} \ \text{為雙射}\right\}$$

  * $S_n$ : $n$ 次對稱群 (The symmetric group on $n$ letters) $[\text{集合}]$
  * $n$ : 被排列的元素個數 (The number of letters) $[n \in \mathbf{P}]$
  * $f$ : 一個排列 (A permutation) $[f \in S_n]$
  * 註：$S_n$ 配的運算是**合成** $\circ$，不是別的。寫 $S_n$ 而不寫 $\left(S_n, \circ\right)$ 是慣例上的省略。

* **【定義 2】 循環記號 (Cycle notation)：** 把「$a_1 \to a_2 \to \cdots \to a_k \to a_1$、其餘元素不動」的排列簡寫成一串

  $$\left(a_1\, a_2\, \cdots\, a_k\right) \overset{\text{def}}{=} \left[\, f(a_1) = a_2,\ f(a_2) = a_3,\ \dots,\ f(a_k) = a_1,\ f(z) = z \ \text{ for } z \notin \left\{a_1, \dots, a_k\right\} \,\right]$$

  * $a_1, \dots, a_k$ : 循環中的元素 (The elements in the cycle) $[a_i \in \left\{1, \dots, n\right\}]$
  * $k$ : 循環長度 (Cycle length) $[k \in \mathbf{P}]$
  * $f$ : 對應的排列 (The corresponding permutation) $[f \in S_n]$
  * $z$ : 循環外的元素 (An element outside the cycle) $[z \in \left\{1, \dots, n\right\}]$
  * 註：恆等排列記作 $e$。長度 $2$ 的循環（如 $\left(12\right)$）稱為**對換 (transposition)**。
  * 註：同一個循環有多種寫法（$\left(123\right) = \left(231\right) = \left(312\right)$），起點可以任選，**但方向不能反**。
    投影片寫的 $\left(321\right)$ 方向相反，等於 $\left(132\right)$。

* **【推導 1】 函數合成的結合律 (Associativity of function composition)：** 把兩邊都作用在任意 $x$ 上，展開後長得一模一樣

  * (a) 左邊：

    $$\begin{gather*}
    \left(\left(f \circ g\right) \circ h\right)(x) &\overset{\text{已知 2(c)}}{=}& \left(f \circ g\right)\left(h(x)\right) \\
    &\overset{\text{已知 2(c)}}{=}& f\left(g\left(h(x)\right)\right)
    \end{gather*}$$

  * (b) 右邊：

    $$\begin{gather*}
    \left(f \circ \left(g \circ h\right)\right)(x) &\overset{\text{已知 2(c)}}{=}& f\left(\left(g \circ h\right)(x)\right) \\
    &\overset{\text{已知 2(c)}}{=}& f\left(g\left(h(x)\right)\right)
    \end{gather*}$$

  * $f,\ g,\ h$ : $T$ 到自身的函數 (Functions from $T$ to itself) $[T \to T]$
  * $x$ : 定義域中的元素 (An element of the domain) $[x \in T]$
  * 註：(a) 與 (b) 的最後一行相同，且對**每一個** $x$ 都成立，故兩個函數相等。
    函數相等的定義就是「在每一點取值都相同」。

+++

## 證明:

### (a) proof that the symmetric group is a group

四條公理逐條檢查 $\left(S_n, \circ\right)$：

$$\begin{gather*}
f \circ g &\overset{\text{已知 1,已知 2(b)}}{\in}& S_n \qquad \text{(封閉性)} \\
\left(f \circ g\right) \circ h &\overset{\text{推導 1(a)(b)}}{=}& f \circ \left(g \circ h\right) \qquad \text{(結合律)} \\
f \circ \mathrm{id} &\overset{\text{已知 3}}{=}& \mathrm{id} \circ f = f \qquad \text{(單位元素 } e = \mathrm{id}\text{)} \\
f \circ f^{-1} &\overset{\text{已知 3}}{=}& f^{-1} \circ f = \mathrm{id} \qquad \text{(反元素 } f^{-1} \in S_n\text{)} \\
\left(S_n, \circ\right) &\overset{\text{定義 1}}{=}& \text{群}
\end{gather*}$$

四條全中，故 $\left(S_n, \circ\right)$ 是群。

* 註：單位元素 $\mathrm{id}$ 本身是雙射（每個元素對到自己），故 $\mathrm{id} \in S_n$；
  反函數 $f^{-1}$ 由【已知 3】保證也是雙射，故 $f^{-1} \in S_n$。兩者都確實落在群裡。

### (b) proof of the order of the symmetric group

一個排列由它在 $1, 2, \dots, n$ 上的取值完全決定。依【排列】【定義 1】的單射性，
每選定一個值，下一個位置的可選範圍就少一個：

$$\begin{gather*}
f(1) &\ \text{有}\ & n \ \text{種選法} \\
f(2) &\ \text{有}\ & n - 1 \ \text{種選法} \qquad \text{(不可與 } f(1) \text{ 相同)} \\
f(3) &\ \text{有}\ & n - 2 \ \text{種選法} \qquad \text{(不可與 } f(1), f(2) \text{ 相同)} \\
\vdots &\ \vdots\ & \vdots \\
f(n) &\ \text{有}\ & 1 \ \text{種選法}
\end{gather*}$$

把各步的選法相乘：

$$\begin{gather*}
\left|S_n\right| &=& n \times \left(n-1\right) \times \left(n-2\right) \times \cdots \times 1 \\
&=& n!
\end{gather*}$$

* 註：這裡用到的是**單射**性（下排不可重複）。滿射性不必另外要求 ——
  由 [排列](Permutation.md)【證明 (a)】，有限集上單射自動滿射。
* 註：代入具體數值：$\left|S_3\right| = 3! = 6$、$\left|S_4\right| = 4! = 24$、
  $\left|S_{256}\right| = 256! \approx 10^{507}$。

### (c) verify the composition and the inverse in the symmetric group on three letters

先把 $S_3$ 的六個元素用兩種記號對照列出（由【證明 (b)】，$\left|S_3\right| = 6$，恰好這六個）：

$$S_3 = \left\{
\begin{pmatrix} 1 & 2 & 3 \\ 1 & 2 & 3 \end{pmatrix},
\begin{pmatrix} 1 & 2 & 3 \\ 2 & 1 & 3 \end{pmatrix},
\begin{pmatrix} 1 & 2 & 3 \\ 3 & 2 & 1 \end{pmatrix},
\begin{pmatrix} 1 & 2 & 3 \\ 1 & 3 & 2 \end{pmatrix},
\begin{pmatrix} 1 & 2 & 3 \\ 2 & 3 & 1 \end{pmatrix},
\begin{pmatrix} 1 & 2 & 3 \\ 3 & 1 & 2 \end{pmatrix}
\right\} = \left\{e,\ \left(12\right),\ \left(13\right),\ \left(23\right),\ \left(123\right),\ \left(132\right)\right\}$$

**投影片第一個計算**：$\left(123\right) \circ \left(123\right)$。令 $f = \left(123\right)$，
依【已知 2(c)】逐點計算（**由右往左**）：

$$\begin{gather*}
\left(f \circ f\right)(1) &\overset{\text{已知 2(c)}}{=}& f\left(f(1)\right) \\
\left(f \circ f\right)(1) &\overset{\text{定義 2}}{=}& f(2) \\
\left(f \circ f\right)(1) &\overset{\text{定義 2}}{=}& 3 \\
\left(f \circ f\right)(2) &\overset{\text{已知 2(c)}}{=}& f\left(f(2)\right) \\
\left(f \circ f\right)(2) &\overset{\text{定義 2}}{=}& f(3) \\
\left(f \circ f\right)(2) &\overset{\text{定義 2}}{=}& 1 \\
\left(f \circ f\right)(3) &\overset{\text{已知 2(c)}}{=}& f\left(f(3)\right) \\
\left(f \circ f\right)(3) &\overset{\text{定義 2}}{=}& f(1) \\
\left(f \circ f\right)(3) &\overset{\text{定義 2}}{=}& 2
\end{gather*}$$

把三個值填進二列陣列：

$$\begin{pmatrix} 1 & 2 & 3 \\ 2 & 3 & 1 \end{pmatrix} \circ \begin{pmatrix} 1 & 2 & 3 \\ 2 & 3 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 2 & 3 \\ 3 & 1 & 2 \end{pmatrix} = \left(132\right)$$

與投影片一致。

**投影片第二個計算**：$\left(123\right)^{-1} = \left(132\right)$。
依【已知 1(d)】只需驗證兩者合成得到 $\mathrm{id}$。令 $g = \left(132\right)$：

$$\begin{gather*}
\left(f \circ g\right)(1) &\overset{\text{定義 2}}{=}& f(3) = 1 \\
\left(f \circ g\right)(2) &\overset{\text{定義 2}}{=}& f(1) = 2 \\
\left(f \circ g\right)(3) &\overset{\text{定義 2}}{=}& f(2) = 3 \\
f \circ g &=& \mathrm{id}
\end{gather*}$$

同理 $g \circ f = \mathrm{id}$（$g$ 與 $f$ 的角色對調，計算逐字對稱）。
故 $\left(123\right)^{-1} = \left(132\right)$，與投影片一致。

* 註：投影片寫的是 $\left(123\right)^{-1} = \left(321\right) = \left(132\right)$。
  $\left(321\right)$ 表示 $3 \to 2 \to 1 \to 3$，與 $\left(132\right)$ 表示的
  $1 \to 3 \to 2 \to 1$ 是同一個排列 —— **反元素就是把箭頭全部反向**。

+++

## 意義與密碼學關聯 (Interpretation and Relevance to Cryptography)

### AES 的 S-box 是 $S_{256}$ 的一個元素

投影片 p.10 的 Remark。AES 的 S-box 把一個位元組（$0$ 到 $255$）映到另一個位元組，
而且必須可逆，故它就是 $\left\{0, 1, \dots, 255\right\}$ 上的一個排列：

$$\text{S-box} \in S_{256}, \qquad \left|S_{256}\right| \overset{\text{證明 (b)}}{=} 256! \approx 10^{507}$$

$256!$ 這個數字值得停下來想一下：**可能的 S-box 有 $10^{507}$ 種**，
而宇宙中的原子數量大約是 $10^{80}$。AES 從這麼大的空間裡挑了一個特定的排列 ——
挑的方式不是隨機的，而是用 $GF(2^8)$ 的乘法反元素加上一個仿射變換構造出來的，
見 [一般線性群的階](General_Linear_Group_Order.md) 與 [體的定義](../Field/Field_Definition.md)。

### 為什麼 S-box 不能自己設計

既然有 $10^{507}$ 種選擇，為什麼不隨便挑一個？因為**大部分排列的密碼學性質很差**。
S-box 需要同時滿足非線性度高、差分均勻性低、代數次數高等條件，
隨機挑中一個符合所有條件的機率極低。

這也是為什麼 $S_n$ 值得單獨拿出來研究 —— 它太大了，大到你必須有結構化的方法在裡面找元素，
而不能靠窮舉。

### 群運算的順序陷阱

【證明 (c)】特別標了「**由右往左**」。這在實作時是最常見的錯誤來源：

$$\left(f \circ g\right)(x) = f\left(g(x)\right) \qquad \text{先做 } g\text{，再做 } f$$

而程式裡寫 `apply(f, apply(g, x))` 或寫成 pipeline `x |> g |> f`，
視覺順序恰好相反。$S_n$ 在 $n \ge 3$ 時非交換，所以**寫反了答案就是錯的**，
不像 $\mathbf{Z}_n$ 那樣怎麼寫都對。

搭配 [乘積的反元素](Inverse_of_a_Product.md) 的「順序顛倒」規則一起記：
$\left(f \circ g\right)^{-1} = g^{-1} \circ f^{-1}$。
