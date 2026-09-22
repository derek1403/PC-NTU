# Unique Solution and Cancellation Law (唯一解與消去律)

+++

## 證明目標:

`Algebra.pdf` p.8 第 5 條命題。這是群論裡第一條真正「能拿來算東西」的結果 ——
它說**群裡的一次方程式一定解得出來，而且只有一個解**。

* (a) 左消去律：

$$a * b = a * c \quad \Longrightarrow \quad b = c$$

* (b) 右消去律：

$$a * b = c * b \quad \Longrightarrow \quad a = c$$

* (c) 方程式 $a * x = b$ 在 $G$ 中有唯一解：

$$x = a^{-1} * b$$

* (d) 方程式 $y * a = b$ 在 $G$ 中有唯一解：

$$y = b * a^{-1}$$

* $G$ : 群的底層集合 (The underlying set of the group) $[\text{集合}]$
* $*$ : 群運算 (Group operation) $[G \times G \to G]$
* $a,\ b,\ c$ : 群元素 (Group elements) $[a, b, c \in G]$
* $x,\ y$ : 待解的未知元素 (The unknowns to be solved for) $[x, y \in G]$
* $a^{-1}$ : $a$ 的反元素 (The inverse of $a$) $[a^{-1} \in G]$
* 註：(c) 與 (d) 的解**長得不一樣**（$a^{-1} * b$ 對 $b * a^{-1}$）。
  非交換群裡兩者是不同的元素，**不可混用**。
* 註：先證 (a)(b) 再證 (c)(d)，因為唯一性那一半正好就是消去律。順序不可對調
  —— 那會變成前向引用。
* 註：本檔是整章第一次出現「**存在性 + 唯一性**」兩段式的證明結構，
  後面 [拉格朗日定理](Lagrange_Theorem.md)、[中國剩餘定理](../Ring/Chinese_Remainder_Theorem.md)
  都會再用到這個骨架。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [群的公理 (Group axioms)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Group/Group_Definition.html#definitions-and-notation)：** 已於本章 [群的定義](Group_Definition.md)【定義 2】給出，此處引用其中三條

  * (a) 封閉性：

    $$a * b \in G \qquad \text{for all } a, b \in G$$

  * (b) 結合律：

    $$a * \left(b * c\right) = \left(a * b\right) * c \qquad \text{for all } a, b, c \in G$$

  * (c) 單位元素：

    $$a * e = e * a = a \qquad \text{for all } a \in G$$

  * $G$ : 群的底層集合 (The underlying set of the group) $[\text{集合}]$
  * $*$ : 群運算 (Group operation) $[G \times G \to G]$
  * $a,\ b,\ c$ : 群元素 (Group elements) $[a, b, c \in G]$
  * $e$ : 單位元素 (The identity element) $[e \in G]$
  * 註：(a) 在【證明 (c)】用來保證 $a^{-1} * b$ 確實落在 $G$ 裡 ——
    否則「解存在」這句話沒有意義（解必須是群裡的元素）。

* **【已知 2】 [反元素唯一 (Uniqueness of the inverse)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Group/Uniqueness_of_Inverse.html#a-proof-uniqueness-of-the-inverse-element)：** 已於本章 [反元素唯一](Uniqueness_of_Inverse.md)【證明 (a)】完整證明，此處直接引用不再重證

  $$a * a^{-1} = a^{-1} * a = e \qquad \text{and } a^{-1} \text{ is the only such element}$$

  * $a$ : 任意群元素 (An arbitrary group element) $[a \in G]$
  * $a^{-1}$ : $a$ 的反元素 (The inverse of $a$) $[a^{-1} \in G]$
  * $e$ : 單位元素 (The identity element) $[e \in G]$

* **【假設 1】 兩個解 (Two putative solutions)：** 【證明 (c)】【證明 (d)】的唯一性部分要用。
  設 $x_1, x_2$ 都是 $a * x = b$ 的解、$y_1, y_2$ 都是 $y * a = b$ 的解

  * (a) 對 $a * x = b$：

    $$a * x_1 = b, \qquad a * x_2 = b$$

  * (b) 對 $y * a = b$：

    $$y_1 * a = b, \qquad y_2 * a = b$$

  * $x_1,\ x_2$ : $a * x = b$ 的兩個（假定可能相異的）解 (Two putative solutions) $[x_1, x_2 \in G]$
  * $y_1,\ y_2$ : $y * a = b$ 的兩個（假定可能相異的）解 (Two putative solutions) $[y_1, y_2 \in G]$
  * $a,\ b$ : 群元素 (Group elements) $[a, b \in G]$

+++

## 證明:

### (a) proof of the left cancellation law

左右兩邊同時**從左邊**乘上 $a^{-1}$，然後把括號往左挪，$a^{-1} * a$ 併成 $e$：

$$\begin{gather*}
a * b &=& a * c \\
a^{-1} * \left(a * b\right) &=& a^{-1} * \left(a * c\right) \\
\left(a^{-1} * a\right) * b &\overset{\text{已知 1(b)}}{=}& \left(a^{-1} * a\right) * c \\
e * b &\overset{\text{已知 2}}{=}& e * c \\
b &\overset{\text{已知 1(c)}}{=}& c
\end{gather*}$$

故 $a * b = a * c \Rightarrow b = c$。

* 註：**一定要從左邊乘**。非交換群裡從右邊乘 $a^{-1}$ 得到的是
  $a * b * a^{-1} = a * c * a^{-1}$，中間的 $a$ 消不掉。

### (b) proof of the right cancellation law

與【證明 (a)】完全對稱，這次左右兩邊同時**從右邊**乘上 $b^{-1}$：

$$\begin{gather*}
a * b &=& c * b \\
\left(a * b\right) * b^{-1} &=& \left(c * b\right) * b^{-1} \\
a * \left(b * b^{-1}\right) &\overset{\text{已知 1(b)}}{=}& c * \left(b * b^{-1}\right) \\
a * e &\overset{\text{已知 2}}{=}& c * e \\
a &\overset{\text{已知 1(c)}}{=}& c
\end{gather*}$$

故 $a * b = c * b \Rightarrow a = c$。

### (c) proof existence and uniqueness of the solution to the left equation

**存在性**：直接把 $x = a^{-1} * b$ 代回去驗算。先由【已知 1(a)】確認它是 $G$ 的元素，再驗算：

$$\begin{gather*}
a * \left(a^{-1} * b\right) &\overset{\text{已知 1(b)}}{=}& \left(a * a^{-1}\right) * b \\
&\overset{\text{已知 2}}{=}& e * b \\
&\overset{\text{已知 1(c)}}{=}& b
\end{gather*}$$

故 $x = a^{-1} * b$ 確實是一個解。

**唯一性**：設 $x_1, x_2$ 都是解，由【假設 1(a)】兩者代進去都得到 $b$，再套左消去律：

$$\begin{gather*}
a * x_1 &\overset{\text{假設 1(a)}}{=}& b \\
a * x_1 &\overset{\text{假設 1(a)}}{=}& a * x_2 \\
x_1 &\overset{\text{證明 (a)}}{=}& x_2
\end{gather*}$$

存在且唯一，故 $a * x = b$ 的解恰為 $x = a^{-1} * b$。

### (d) proof existence and uniqueness of the solution to the right equation

與【證明 (c)】完全對稱。**存在性**：把 $y = b * a^{-1}$ 代回去驗算：

$$\begin{gather*}
\left(b * a^{-1}\right) * a &\overset{\text{已知 1(b)}}{=}& b * \left(a^{-1} * a\right) \\
&\overset{\text{已知 2}}{=}& b * e \\
&\overset{\text{已知 1(c)}}{=}& b
\end{gather*}$$

**唯一性**：設 $y_1, y_2$ 都是解，套右消去律：

$$\begin{gather*}
y_1 * a &\overset{\text{假設 1(b)}}{=}& b \\
y_1 * a &\overset{\text{假設 1(b)}}{=}& y_2 * a \\
y_1 &\overset{\text{證明 (b)}}{=}& y_2
\end{gather*}$$

存在且唯一，故 $y * a = b$ 的解恰為 $y = b * a^{-1}$。

+++

## 意義與密碼學關聯 (Interpretation and Relevance to Cryptography)

### 消去律 $\neq$ 無零因子

消去律長得很像「$ab = ac$ 且 $a \neq 0$ 就可以約掉 $a$」，但兩者的**理由完全不同**：

* 群裡能消去，是因為 $a^{-1}$ **存在**（每個元素都有反元素）；
* 環裡能不能消去，要看有沒有 [零因子](../Ring/Zero_Divisor.md)。

$\left(\mathbf{Z}, \times\right)$ 不是群（除了 $\pm1$ 沒人有反元素），
但 $2x = 2y \Rightarrow x = y$ 仍然成立 —— 靠的是 $\mathbf{Z}$ 沒有零因子，不是靠反元素。
反過來 $\mathbf{Z}_6$ 裡 $2 \times 2 = 2 \times 5 = 4$ 但 $2 \neq 5$，消去律失效。

**群保證消去律，但消去律不保證是群。** 這條界線在 [整環](../Ring/Integral_Domain.md) 會再談。

### 唯一解＝凱萊表每列每行都是一個排列

【證明 (c)】說「固定 $a$，方程式 $a * x = b$ 對每個 $b$ 恰有一解」。
換句話說，映射

$$L_a : G \to G, \qquad x \mapsto a * x$$

是**雙射**（每個 $b$ 恰被一個 $x$ 打到）。這給出一個非常有用的圖像：

**群的凱萊表 (Cayley table) 裡，每一列與每一行都是 $G$ 全體元素的一個排列，
不會有任何元素重複或缺席。**

去看 [阿貝爾群與非阿貝爾群](Abelian_and_Non_Abelian_Group.md) 裡 $\mathbf{Z}_9^*$ 的凱萊表，
每列每行確實都是 $\left\{1,2,4,5,7,8\right\}$ 的重排 —— 這不是巧合，是本命題。

這個觀察還會再出場兩次：

* [對稱群](Symmetric_Group.md) —— $L_a$ 是 $G$ 上的排列，這是 Cayley 定理的起點；
* [陪集分割](Coset_Partition.md) —— 同樣的雙射論證用來證明「所有陪集一樣大」，
  進而導出 [拉格朗日定理](Lagrange_Theorem.md)。

### 密碼學上的對應：完美保密的數學基礎

一次性密碼本 (One-Time Pad) 的完美保密性，本質上就是本命題。

在群 $G$ 裡用金鑰 $k$ 加密明文 $m$ 得 $c = k * m$。攻擊者看到 $c$，想猜 $m$。
由【證明 (d)】，對**任何**一個候選明文 $m'$，都恰好存在一把金鑰
$k' = c * \left(m'\right)^{-1}$ 使得 $k' * m' = c$。

**每個明文都「同樣說得通」，而且對應的金鑰數量完全相同（恰好一把）。**
若金鑰是均勻隨機選的，攻擊者看到密文之後對明文的機率分布與看到之前一模一樣 ——
這正是完美保密 (perfect secrecy) 的定義。

若消去律失效（某些 $a$ 沒有反元素），有些明文對應的金鑰會比較多、有些比較少，
攻擊者就能從密文中榨出資訊。**群結構是完美保密的必要條件。**
