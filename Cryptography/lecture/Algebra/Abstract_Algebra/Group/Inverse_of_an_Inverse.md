# Inverse of an Inverse (反元素的反元素)

+++

## 證明目標:

* (a) 取兩次反元素會回到原處：

$$\left(a^{-1}\right)^{-1} = a \qquad \text{for all } a \in G$$

* $G$ : 群的底層集合 (The underlying set of the group) $[\text{集合}]$
* $*$ : 群運算 (Group operation) $[G \times G \to G]$
* $a$ : 任意群元素 (An arbitrary group element) $[a \in G]$
* $a^{-1}$ : $a$ 的反元素 (The inverse of $a$) $[a^{-1} \in G]$
* 註：這條命題說的是「取反元素」這個映射 $a \mapsto a^{-1}$ 是一個**對合 (involution)**，
  也就是自己是自己的反函數。
* 註：本檔的寫法刻意與 [反元素唯一](Uniqueness_of_Inverse.md)【證明 (a)】**同一個骨架**
  （$x = x * e = x * (\text{拆開的 } e) = \cdots$），只是把 $b$ 換成 $\left(a^{-1}\right)^{-1}$。
  認出這個骨架就不必分別記憶。
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

* **【已知 2】 [反元素唯一 (Uniqueness of the inverse)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Group/Uniqueness_of_Inverse.html#a-proof-uniqueness-of-the-inverse-element)：** 已於本章 [反元素唯一](Uniqueness_of_Inverse.md)【證明 (a)】完整證明，此處直接引用不再重證。正因為唯一，記號 $a^{-1}$ 與 $\left(a^{-1}\right)^{-1}$ 才是良定義的

  $$a * a^{-1} = a^{-1} * a = e \qquad \text{and } a^{-1} \text{ is the only such element}$$

  * $a$ : 任意群元素 (An arbitrary group element) $[a \in G]$
  * $a^{-1}$ : $a$ 的反元素 (The inverse of $a$) $[a^{-1} \in G]$
  * $e$ : 單位元素 (The identity element) $[e \in G]$

* **【推導 1】 把已知 2 套在 $a^{-1}$ 身上 (Applying the inverse axiom to $a^{-1}$)：** $a^{-1}$ 本身也是群的元素，故它也有反元素，記作 $\left(a^{-1}\right)^{-1}$

  $$a^{-1} * \left(a^{-1}\right)^{-1} = \left(a^{-1}\right)^{-1} * a^{-1} \overset{\text{已知 2}}{=} e$$

  * $a^{-1}$ : $a$ 的反元素 (The inverse of $a$) $[a^{-1} \in G]$
  * $\left(a^{-1}\right)^{-1}$ : $a^{-1}$ 的反元素 (The inverse of $a^{-1}$) $[\left(a^{-1}\right)^{-1} \in G]$
  * $e$ : 單位元素 (The identity element) $[e \in G]$
  * 註：這張卡片本身沒有做任何計算，只是把【已知 2】的 $a$ **改代成 $a^{-1}$**。
    寫成獨立卡片是為了讓證明段的每一次引用都指得明確。

+++

## 證明:

### (a) proof that taking the inverse twice returns the original element

起手式取 $\left(a^{-1}\right)^{-1}$，把 $e$ 拆成 $a^{-1} * a$ 塞進去，
再用結合律把括號往左挪 —— 括號一挪，$\left(a^{-1}\right)^{-1} * a^{-1}$ 併成 $e$，於是只剩 $a$。

$$\begin{gather*}
\left(a^{-1}\right)^{-1} &\overset{\text{已知 1(b)}}{=}& \left(a^{-1}\right)^{-1} * e \\
&\overset{\text{已知 2}}{=}& \left(a^{-1}\right)^{-1} * \left(a^{-1} * a\right) \\
&\overset{\text{已知 1(a)}}{=}& \left(\left(a^{-1}\right)^{-1} * a^{-1}\right) * a \\
&\overset{\text{推導 1}}{=}& e * a \\
&\overset{\text{已知 1(b)}}{=}& a
\end{gather*}$$

故 $\left(a^{-1}\right)^{-1} = a$。

+++

## 意義與密碼學關聯 (Interpretation and Relevance to Cryptography)

### 另一種看法：$a$ 本身就符合資格

上面的鏈是純代數的走法。還有一個更短的想法，值得放在心裡當作檢查：

由【已知 2】，$a^{-1} * a = a * a^{-1} = e$。這句話**同時**可以讀成兩件事：

* 「$a^{-1}$ 是 $a$ 的反元素」 —— 這是原本的讀法；
* 「$a$ 是 $a^{-1}$ 的反元素」 —— 把主詞換過來，式子一字不改。

第二種讀法說明 $a$ **符合「$a^{-1}$ 的反元素」的定義**。
而 [反元素唯一](Uniqueness_of_Inverse.md) 說符合這個定義的元素只有一個，
那個元素叫做 $\left(a^{-1}\right)^{-1}$。兩者只好相等。

**「$x$ 是 $y$ 的反元素」這句話是對稱的** —— 這就是本命題的全部內容。
上面那條五行的鏈，不過是把這個對稱性用代數重講一遍。

### 對合的意義：加密與解密是同一件事的兩面

映射 $a \mapsto a^{-1}$ 是對合，意思是**做兩次等於什麼都沒做**。
在密碼學裡這對應到一個很實際的性質：

$$m \ \xrightarrow{\ \text{用 } a \text{ 加密}\ } \ a * m \ \xrightarrow{\ \text{用 } a^{-1} \text{ 解密}\ } \ m$$

反過來，用 $a^{-1}$ 當加密金鑰、$a$ 當解密金鑰，整套系統一樣能運作。
**加密與解密在數學上沒有主從之分**，誰當哪個純粹是約定。

RSA 正是靠這件事才能同時做「加密」與「數位簽章」：

| 用途 | 誰先用 | 誰後用 |
|---|---|---|
| 加密 | 公鑰 $e$ | 私鑰 $d$ |
| 簽章 | 私鑰 $d$ | 公鑰 $e$ |

兩者用的是**同一對金鑰、同一套運算**，只是順序對調。這在群論裡就是
$\left(a^{-1}\right)^{-1} = a$ 的直接後果。

### 程式思維

對合在程式裡最熟悉的例子是 XOR：

```python
cipher = plain ^ key
plain  = cipher ^ key      # 同一個 key，同一個運算
```

$\left(\mathbf{Z}_2^n, \oplus\right)$ 這個群裡**每個元素都是自己的反元素**
（$k \oplus k = 0$），所以連 $\left(a^{-1}\right)^{-1} = a$ 都退化成 $a^{-1} = a$。
一次性密碼本 (One-Time Pad) 能成立，靠的正是這個群的這個性質。
