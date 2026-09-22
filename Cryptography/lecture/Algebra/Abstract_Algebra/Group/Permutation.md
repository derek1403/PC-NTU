# Permutation (排列)

+++

## 證明目標:

`Algebra.pdf` p.9。排列是「把集合裡的元素重新洗牌」的精確說法，
也是下一檔 [對稱群](Symmetric_Group.md) 的建材。

* (a) 有限集合上，三個條件互相等價：

$$f \ \text{單射} \quad \Longleftrightarrow \quad f \ \text{滿射} \quad \Longleftrightarrow \quad f \ \text{是排列}$$

* (b) 排列的合成仍是排列（供 [對稱群](Symmetric_Group.md) 驗證封閉性用）：

$$f, g \ \text{皆為 } T \text{ 上的排列} \quad \Longrightarrow \quad f \circ g \ \text{亦為 } T \text{ 上的排列}$$

* $T$ : 一個集合 (A set) $[\text{集合}]$
* $f,\ g$ : $T$ 到自身的函數 (Functions from $T$ to itself) $[T \to T]$
* $\circ$ : 函數合成 (Function composition) $[\left(T \to T\right) \times \left(T \to T\right) \to \left(T \to T\right)]$
* 註：(a) **只對有限集合成立**。無限集合上單射未必滿射 —— 例如
  $f : \mathbf{Z} \to \mathbf{Z}$，$f(x) = 2x$ 是單射但不是滿射。
  這個區別在 [群的階](Group_Order.md) 討論可數性時還會再出現。
* 註：(a) 是密碼學實作上的實用結論：**驗證一個 S-box 是排列，只需檢查它不會把兩個輸入送到同一個輸出**，
  不必另外檢查每個輸出都被打到。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [有限集合的基數性質 (Cardinality of finite sets)](https://mathworld.wolfram.com/PigeonholePrinciple.html)：** 集合論的標準結果，本章直接引用不再重證

  * (a) 子集的基數不會更大：

    $$S \subseteq T \quad \Longrightarrow \quad \left|S\right| \le \left|T\right|$$

  * (b) 有限集合的子集若基數相同則必相等：

    $$S \subseteq T, \quad \left|S\right| = \left|T\right| < \infty \quad \Longrightarrow \quad S = T$$

  * (c) 鴿籠原理：若 $f$ 把 $T$ 中兩個相異元素送到同一個像，則像集會變小：

    $$\exists\, x \neq y \ \text{ with } \ f(x) = f(y) \quad \Longrightarrow \quad \left|f(T)\right| < \left|T\right|$$

  * $S,\ T$ : 有限集合 (Finite sets) $[\text{集合}]$
  * $\left|T\right|$ : $T$ 的基數 (The cardinality of $T$) $[\left|T\right| \in \mathbf{N}]$
  * $f$ : 函數 (A function) $[T \to T]$
  * $f(T)$ : $f$ 的像集 (The image of $f$) $[f(T) \subseteq T]$
  * $x,\ y$ : 定義域中的元素 (Elements of the domain) $[x, y \in T]$

* **【定義 1】 單射 (Injective, one-to-one)：** 相異的輸入送到相異的輸出，絕不撞號

  $$f \ \text{單射} \quad \overset{\text{def}}{\Longleftrightarrow} \quad \left[\, f(x) = f(y) \ \Longrightarrow \ x = y \,\right] \quad \text{for all } x, y \in T$$

  * $f$ : 函數 (A function) $[T \to T]$
  * $T$ : 定義域與值域 (The domain and codomain) $[\text{集合}]$
  * $x,\ y$ : 定義域中的元素 (Elements of the domain) $[x, y \in T]$

* **【定義 2】 滿射 (Surjective, onto)：** 值域中每個元素都被打到，沒有人被遺漏

  $$f \ \text{滿射} \quad \overset{\text{def}}{\Longleftrightarrow} \quad \forall\, z \in T, \ \exists\, x \in T \ \text{ such that } \ f(x) = z$$

  * $f$ : 函數 (A function) $[T \to T]$
  * $T$ : 定義域與值域 (The domain and codomain) $[\text{集合}]$
  * $x,\ z$ : 定義域與值域中的元素 (Elements of the domain and codomain) $[x, z \in T]$
  * 註：等價的寫法是 $f(T) = T$，本檔證明中採用這個形式。

* **【定義 3】 雙射與排列 (Bijective and permutation)：**

  * (a) 雙射：同時是單射與滿射：

    $$f \ \text{雙射} \quad \overset{\text{def}}{\Longleftrightarrow} \quad f \ \text{單射且 } f \ \text{滿射}$$

  * (b) 排列：從集合 $T$ **到自身**的雙射：

    $$f \ \text{是 } T \text{ 上的排列} \quad \overset{\text{def}}{\Longleftrightarrow} \quad f : T \to T \ \text{ 為雙射}$$

  * $f$ : 函數 (A function) $[T \to T]$
  * $T$ : 集合 (A set) $[\text{集合}]$
  * 註：「**到自身**」這四個字是關鍵。$f : \left\{1,2\right\} \to \left\{a,b\right\}$ 也可以是雙射，
    但那不叫排列 —— 排列的定義域與值域必須是**同一個**集合，這樣才談得上「重新排」。

* **【定義 4】 二列陣列表示 (Two-row array notation)：** 有限集 $T = \left\{1, 2, \dots, n\right\}$ 上的排列，上排寫輸入、下排寫對應的輸出

  $$f = \begin{pmatrix} 1 & 2 & \cdots & n \\ f(1) & f(2) & \cdots & f(n) \end{pmatrix}$$

  * $f$ : $T$ 上的排列 (A permutation of $T$) $[T \to T]$
  * $n$ : 集合的大小 (The size of the set) $[n \in \mathbf{P}]$
  * 註：投影片 p.9 的例子 $T = \left\{1,2,3\right\}$、$f(1)=2$、$f(2)=3$、$f(3)=1$ 寫成

    $$f = \begin{pmatrix} 1 & 2 & 3 \\ 2 & 3 & 1 \end{pmatrix}$$

  * 註（**dangling 標註**）：本卡片只是一套書寫格式，不是推導的依據，故本檔的證明段**不會**以
    `\overset{\text{定義 4}}` 引用它；它真正被使用是在 [對稱群](Symmetric_Group.md)【證明 (c)】列出 $S_3$ 時。
  * 註：下排恰好是上排的重排 —— 這正是「排列」這個中文譯名的由來，
    也是【證明 (a)】要保證的事（下排不重複、不缺漏）。

* **【定義 5】 函數合成 (Function composition)：** 先做右邊那個，再做左邊那個

  $$\left(f \circ g\right)(x) \overset{\text{def}}{=} f\left(g(x)\right)$$

  * $f,\ g$ : $T$ 到自身的函數 (Functions from $T$ to itself) $[T \to T]$
  * $x$ : 定義域中的元素 (An element of the domain) $[x \in T]$
  * 註：**順序是由右往左**。這個約定在 [對稱群](Symmetric_Group.md) 計算 $S_3$ 的乘法時很容易寫反。

+++

## 證明:

### (a) proof the equivalence of injectivity and surjectivity on a finite set

設 $T$ 為**有限**集合、$f : T \to T$。

**($\Rightarrow$) 單射推出滿射。** 單射意味著 $T$ 中 $\left|T\right|$ 個相異元素被送到 $\left|T\right|$ 個相異的像，
故像集恰好與 $T$ 一樣大；而像集又是 $T$ 的子集，只好整個填滿：

$$\begin{gather*}
f \ \text{單射} &\overset{\text{定義 1}}{\Longrightarrow}& \left|f(T)\right| = \left|T\right| \\
f(T) &\subseteq& T \\
f(T) &\overset{\text{已知 1(b)}}{=}& T \\
f &\overset{\text{定義 2}}{\Longrightarrow}& \text{滿射}
\end{gather*}$$

**($\Leftarrow$) 滿射推出單射。** 反過來，滿射保證像集填滿 $T$；若 $f$ 不是單射，
鴿籠原理會讓像集縮小，兩者矛盾：

$$\begin{gather*}
f \ \text{滿射} &\overset{\text{定義 2,定義 3}}{\Longrightarrow}& f(T) = T \\
\left|f(T)\right| &=& \left|T\right| \\
f \ \text{非單射} &\overset{\text{已知 1(c)}}{\Longrightarrow}& \left|f(T)\right| < \left|T\right|
\end{gather*}$$

最後兩行互相矛盾，故 $f$ 必為單射。

兩個方向都證完，加上【定義 3】，三個條件在有限集上互相等價。

* 註：這裡的矛盾來自「$f$ 非單射」這個暫時的設想，屬於局部反證，
  結論只影響本小節，故不另立【假設】卡片。

### (b) proof that the composition of two permutations is a permutation

設 $f, g$ 都是 $T$ 上的排列。**單射**：

$$\begin{gather*}
\left(f \circ g\right)(x) &\overset{\text{定義 5}}{=}& f\left(g(x)\right) \\
f\left(g(x)\right) &=& f\left(g(y)\right) \\
g(x) &\overset{\text{定義 1}}{=}& g(y) \qquad \text{(} f \text{ 單射)} \\
x &\overset{\text{定義 1}}{=}& y \qquad \text{(} g \text{ 單射)}
\end{gather*}$$

**滿射**：任取 $z \in T$，先用 $f$ 的滿射性找到中繼點，再用 $g$ 的滿射性找到源頭：

$$\begin{gather*}
\exists\, w \in T \ \text{ with } \ f(w) &\overset{\text{定義 2}}{=}& z \qquad \text{(} f \text{ 滿射)} \\
\exists\, x \in T \ \text{ with } \ g(x) &\overset{\text{定義 2}}{=}& w \qquad \text{(} g \text{ 滿射)} \\
\left(f \circ g\right)(x) &\overset{\text{定義 5}}{=}& f\left(g(x)\right) \\
\left(f \circ g\right)(x) &=& f(w) \\
\left(f \circ g\right)(x) &=& z
\end{gather*}$$

單射與滿射都成立，故 $f \circ g$ 是 $T$ 上的排列。

+++

## 意義與密碼學關聯 (Interpretation and Relevance to Cryptography)

### 每一個區塊加密法就是一個排列

投影片 p.9 的 Remark 是整張投影片最重要的一句話：

$$\text{DES}_k : \left\{0,1\right\}^{64} \to \left\{0,1\right\}^{64}, \qquad \text{AES}_k : \left\{0,1\right\}^{128} \to \left\{0,1\right\}^{128}$$

**固定金鑰 $k$ 之後，區塊加密法是明文空間上的一個排列。** 理由很直接：

* 它必須是**單射** —— 兩個不同明文若加密成同一個密文，解密方無從得知原文是哪一個；
* 由【證明 (a)】，有限集上單射自動就是滿射，所以它同時是**雙射**，也就是排列；
* 雙射保證**解密函數 $\text{DES}_k^{-1}$ 存在且唯一**。

換句話說：「加密必須可逆」這個需求，在數學上就是「加密函數必須是排列」。

### 為什麼實作只需檢查單射

【證明 (a)】在實作上省了一半的工。設計一個 $8 \times 8$ 的 S-box（$\left\{0,1\right\}^8$ 上的函數），
要驗證它可逆時：

```python
def is_permutation(sbox):          # sbox: list of 256 ints
    return len(set(sbox)) == 256   # 只檢查「沒有重複」
```

不必再另外檢查「$0$ 到 $255$ 每個值都出現過」—— 由【證明 (a)】，前者自動蘊涵後者。
（當然，`len(set(...)) == 256` 這個寫法其實兩件事一起檢查掉了，
但概念上你只需要說服自己「沒撞號」。）

**這個捷徑只在有限集上成立**，而密碼學剛好永遠在有限集上工作。

### 合成的封閉性通往群結構

【證明 (b)】看起來是技術細節，其實是下一檔的入場券：
排列合成後仍是排列，正是 [對稱群](Symmetric_Group.md) $S_n$ 的**封閉性公理**。
把「單位元素＝恆等排列」「反元素＝反函數」補上，$S_n$ 就成為一個群。

在密碼學裡這對應到：**多輪加密的合成仍然是一個排列**。
AES 的十輪每一輪都是排列，合起來還是排列，所以整體仍然可逆 ——
這件事不需要重新驗證，由【證明 (b)】自動保證。
