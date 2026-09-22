# Uniqueness of Inverse (反元素唯一)

+++

## 證明目標:

[群的定義](Group_Definition.md)【定義 2(d)】只保證每個元素的反元素**存在**，沒有說它**唯一**。
本檔補上唯一性：

* (a) 群 $\left(G, *\right)$ 中每個元素 $a$ 的反元素唯一：

$$b = c \qquad \text{for any two inverses } b, c \text{ of } a$$

* $G$ : 群的底層集合 (The underlying set of the group) $[\text{集合}]$
* $*$ : 群運算 (Group operation) $[G \times G \to G]$
* $a$ : 任意群元素 (An arbitrary group element) $[a \in G]$
* $b,\ c$ : $a$ 的兩個（假定可能相異的）反元素 (Two putative inverses of $a$) $[b, c \in G]$
* 註：證完之後，記號 $a^{-1}$（定冠詞的「**那個**」反元素）才是合法的，
  [群的定義](Group_Definition.md)【定義 3(c)】的負冪次 $g^{-n}$ 也才是良定義的。
* 註：與 [單位元素唯一](Uniqueness_of_Identity.md) 不同，**本證明用到了結合律**。
  沒有結合律的話這條命題不成立 —— 一個元素可以有多個相異的反元素。
* 註：同一結論亦見 [Theory_Playground](https://derek1403.github.io/Theory_Playground/_build/html/02_Concepts/Abstract_Algebra/proof_group_fundamental_theory.html)，
  本章依統一風格重新證明一次，以維持引用鏈自洽。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [群的公理 (Group axioms)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Group/Group_Definition.html#definitions-and-notation)：** 已於本章 [群的定義](Group_Definition.md)【定義 2】給出，此處引用其中兩條

  * (a) 結合律：

    $$a * \left(b * c\right) = \left(a * b\right) * c \qquad \text{for all } a, b, c \in G$$

  * (b) 單位元素：

    $$a * e = e * a = a \qquad \text{for all } a \in G$$

  * $G$ : 群的底層集合 (The underlying set of the group) $[\text{集合}]$
  * $*$ : 群運算 (Group operation) $[G \times G \to G]$
  * $a,\ b,\ c$ : 群元素 (Group elements) $[a, b, c \in G]$
  * $e$ : 單位元素 (The identity element) $[e \in G]$

* **【已知 2】 [單位元素唯一 (Uniqueness of the identity)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Group/Uniqueness_of_Identity.html#a-proof-uniqueness-of-the-identity-element)：** 已於本章 [單位元素唯一](Uniqueness_of_Identity.md)【證明 (a)】完整證明，此處直接引用不再重證

  $$e_1 = e_2 \qquad \text{for any two identities } e_1, e_2 \in G$$

  * $e_1,\ e_2$ : 兩個單位元素 (Two identity elements) $[e_1, e_2 \in G]$
  * $G$ : 群的底層集合 (The underlying set of the group) $[\text{集合}]$
  * 註：本檔靠這一條，才能在證明中放心地寫「**那個**」單位元素 $e$ 而不引起歧義。

* **【假設 1】 兩個反元素 (Two putative inverses)：** 設 $b$ 與 $c$ 都是 $a$ 的反元素，兩者**各自**滿足反元素公理

  * (a) $b$ 是 $a$ 的反元素：

    $$a * b = b * a = e$$

  * (b) $c$ 是 $a$ 的反元素：

    $$a * c = c * a = e$$

  * $a$ : 任意群元素 (An arbitrary group element) $[a \in G]$
  * $b,\ c$ : $a$ 的兩個（假定可能相異的）反元素 (Two putative inverses of $a$) $[b, c \in G]$
  * $e$ : 單位元素 (The identity element) $[e \in G]$
  * 註：這裡**沒有假設** $b \neq c$。本證明是直接證明「任兩個反元素必相等」，與「唯一」同義。

+++

## 證明:

### (a) proof uniqueness of the inverse element

起手式是 $b$ 自己，然後把 $e$ 拆成 $a * c$ 塞進去，再用結合律把括號挪到另一邊 ——
括號一挪，$b * a$ 就併成 $e$，$b$ 於是被擠掉，只剩 $c$。

$$\begin{gather*}
b &\overset{\text{已知 1(b),已知 2}}{=}& b * e \\
&\overset{\text{假設 1(b)}}{=}& b * \left(a * c\right) \\
&\overset{\text{已知 1(a)}}{=}& \left(b * a\right) * c \\
&\overset{\text{假設 1(a)}}{=}& e * c \\
&\overset{\text{已知 1(b)}}{=}& c
\end{gather*}$$

故 $b = c$，反元素唯一。此後把 $a$ 的反元素記作 $a^{-1}$。

+++

## 意義與密碼學關聯 (Interpretation and Relevance to Cryptography)

### 結合律是這裡的真正主角

整條鏈只有一步是「有內容」的，就是第三步的結合律：

$$b * \left(a * c\right) \quad \longrightarrow \quad \left(b * a\right) * c$$

前面兩步只是把 $b$ 打扮成 $b * \left(a * c\right)$，後面兩步只是收尾。
**括號往左挪的那一瞬間，$b$ 與 $a$ 相遇並同歸於盡** —— 這就是全部的證明。

拿掉結合律，命題立刻失效。例如在非結合的結構裡，可以構造出一個元素有兩個相異「反元素」的例子，
因為 $b * \left(a * c\right)$ 與 $\left(b * a\right) * c$ 不再相等，上面那條鏈斷在第三步。

這也解釋了為什麼 [群的正例與反例](Group_Examples_and_Counterexamples.md)【證明 (i)】
把 $\left(\mathbf{Z}, -\right)$ 壞掉的原因歸結為結合律 ——
**結合律一倒，反元素的整套理論跟著倒。**

### $a^{-1}$ 這個記號要付出的代價

平常寫 $a^{-1}$ 寫得很順手，但這個記號背後其實壓著兩條定理：

1. [單位元素唯一](Uniqueness_of_Identity.md) —— 讓「$a * b = e$」裡的 $e$ 是確定的；
2. 本檔 —— 讓滿足該式的 $b$ 是確定的。

兩條都證完，$a \mapsto a^{-1}$ 才是一個**函數**（每個輸入對到唯一輸出）。
在那之前它只是一個關係，不能寫成函數記號。

### 密碼學上的對應：解密金鑰必須唯一

加密 $c = a * m$、解密 $m = a^{-1} * c$。如果 $a$ 有兩個相異的反元素 $b \neq c$，
那麼「解密金鑰」這個詞就失去意義 —— 會有兩把不同的金鑰都能解開同一則密文。

實際的後果是**安全性證明會垮掉**：密碼學的標準論證形式是「若攻擊者能還原明文，
則他必定掌握了金鑰」，而這個推論正是靠反元素唯一。
反元素不唯一時，攻擊者可以拿到一把「不是原金鑰但一樣能解密」的東西，
原本的歸約 (reduction) 就不成立了。

**反元素唯一是「破解 = 找到金鑰」這個等式的數學基礎。**
