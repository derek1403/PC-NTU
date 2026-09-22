# Uniqueness of Identity (單位元素唯一)

+++

## 證明目標:

[群的定義](Group_Definition.md)【定義 2(c)】只保證單位元素**存在**，沒有說它**唯一**。
本檔補上唯一性：

* (a) 群 $\left(G, *\right)$ 的單位元素唯一：

$$e_1 = e_2 \qquad \text{for any two identities } e_1, e_2 \in G$$

* $G$ : 群的底層集合 (The underlying set of the group) $[\text{集合}]$
* $*$ : 群運算 (Group operation) $[G \times G \to G]$
* $e_1,\ e_2$ : 兩個（假定可能相異的）單位元素 (Two putative identity elements) $[e_1, e_2 \in G]$
* 註：證完之後，記號 $e$（定冠詞的「**那個**」單位元素）才是合法的。在此之前只能說「某一個單位元素」。
* 註：本證明**只用到單位元素公理一條**，完全沒用到封閉性、結合律或反元素。
  這代表結論比看起來更強 —— 任何有單位元素的結構（么半群、環的乘法…）都適用。
* 註：同一結論亦見 [Theory_Playground](https://derek1403.github.io/Theory_Playground/_build/html/02_Concepts/Abstract_Algebra/proof_group_fundamental_theory.html)，
  本章依統一風格重新證明一次，以維持引用鏈自洽。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [單位元素公理 (Identity axiom)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Group/Group_Definition.html#definitions-and-notation)：** 已於本章 [群的定義](Group_Definition.md)【定義 2(c)】給出，此處直接引用

  $$a * e = e * a = a \qquad \text{for all } a \in G$$

  * $G$ : 群的底層集合 (The underlying set of the group) $[\text{集合}]$
  * $*$ : 群運算 (Group operation) $[G \times G \to G]$
  * $a$ : 任意群元素 (An arbitrary group element) $[a \in G]$
  * $e$ : 單位元素 (An identity element) $[e \in G]$

* **【假設 1】 兩個單位元素 (Two putative identities)：** 設 $G$ 中有兩個單位元素，暫且分別叫 $e_1$ 與 $e_2$。
  兩者**各自**滿足【已知 1】

  * (a) $e_1$ 是單位元素：

    $$a * e_1 = e_1 * a = a \qquad \text{for all } a \in G$$

  * (b) $e_2$ 是單位元素：

    $$a * e_2 = e_2 * a = a \qquad \text{for all } a \in G$$

  * $e_1,\ e_2$ : 兩個（假定可能相異的）單位元素 (Two putative identity elements) $[e_1, e_2 \in G]$
  * $a$ : 任意群元素 (An arbitrary group element) $[a \in G]$
  * 註：這裡**沒有假設** $e_1 \neq e_2$。本證明不是反證法，而是直接證明「任兩個單位元素必相等」，
    這與「唯一」是同一件事。

+++

## 證明:

### (a) proof uniqueness of the identity element

關鍵在於**同一個乘積 $e_1 * e_2$ 可以用兩種方式化簡**：把 $e_2$ 當單位元素看，它等於 $e_1$；
把 $e_1$ 當單位元素看，它等於 $e_2$。

$$\begin{gather*}
e_1 &\overset{\text{已知 1,假設 1(b)}}{=}& e_1 * e_2 \\
e_1 &\overset{\text{已知 1,假設 1(a)}}{=}& e_2
\end{gather*}$$

故 $e_1 = e_2$，單位元素唯一。

+++

## 意義與密碼學關聯 (Interpretation and Relevance to Cryptography)

### 這個證明為什麼「太短了」

整個證明只有兩行，因為它把全部力氣花在**找對起手式**：$e_1 * e_2$。

這個乘積是刻意挑的 —— 它同時「碰到」了 $e_1$ 與 $e_2$，因此兩條單位元素性質都能作用在它身上，
而且作用的結果是**不同的兩個元素**。既然同一個東西等於兩個元素，那兩個元素只好相等。

這種「造一個能被兩邊各自化簡的中間量」的手法，在本章反覆出現：

* [反元素唯一](Uniqueness_of_Inverse.md) 用的是 $b * \left(a * c\right)$；
* [反元素的反元素](Inverse_of_an_Inverse.md) 用的是 $a^{-1} * \left(a^{-1}\right)^{-1}$。

**認出這個模式，這四條命題就沒有一條需要背。**

### 唯一性讓記號變得合法

沒有唯一性，「$e$」這個記號是危險的 —— 你寫下 $a * e = a$ 時，讀者不知道你指的是哪一個單位元素。
證完唯一性之後：

* $e$ 可以當成一個確定的元素來用；
* [群的定義](Group_Definition.md)【定義 3(c)】的 $g^0 \overset{\text{def}}{=} e$ 才是良定義的；
* 後面所有以 $e$ 為終點的論證（如 [元素的階](Order_of_Element_and_Cyclic_Subgroup.md) 中
  $g^n = e$ 的最小 $n$）才有意義。

**唯一性不是錦上添花，是讓後續整套記號系統能運作的前提。**

### 密碼學上的對應

在密碼學實作裡，單位元素就是「什麼都不做」的那把金鑰，或橢圓曲線上的無窮遠點 $\infty$。
唯一性保證了一件關鍵的事：**不存在第二個「什麼都不做」的元素**。

若存在兩個相異的單位元素，那麼 $a * e_1$ 與 $a * e_2$ 會是同一個密文卻來自不同金鑰 ——
金鑰空間與密文空間的對應關係就會破裂，安全性分析（例如「猜中金鑰的機率是 $1/\left|G\right|$」）
全部失效。
