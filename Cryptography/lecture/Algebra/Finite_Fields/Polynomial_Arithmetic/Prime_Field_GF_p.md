# Prime Field GF(p) (質體 GF(p))

+++

## 證明目標:

`FiniteFields.pdf` p.2、p.4；(c) 取自補充講義 `Introduction_to_Finite_Fields.pdf` §7.4.1（Theorem 7.6）。
有限體家族裡最小、最基本的成員 —— **元素個數為質數 $p$ 的體**，
它是之後所有 $GF(p^n)$ 的係數來源。

* (a) 投影片 p.4 的 $GF(2)$ 凱萊表：

$$\begin{array}{c|cc} \oplus & 0 & 1 \\ \hline 0 & 0 & 1 \\ 1 & 1 & 0 \end{array} \qquad \begin{array}{c|cc} \otimes & 0 & 1 \\ \hline 0 & 0 & 0 \\ 1 & 0 & 1 \end{array}$$

* (b) 投影片 p.4 的聯立方程在 $GF(7)$ 上的唯一解：

$$\begin{cases} 3x + y + 4z + 1 = 0 \\ 6x + 5y + 3z + 6 = 0 \\ x + 4y + 2z + 5 = 0 \end{cases} \quad \Longrightarrow \quad \left(x, y, z\right) = \left(2, 4, 6\right)$$

* (c) 質體的唯一性（補充講義 Theorem 7.6，投影片未列）：

$$\left|F\right| = p \ \text{為質數} \quad \Longrightarrow \quad F \cong \mathbf{Z}_p$$

* $GF(p)$ : 含 $p$ 個元素的伽羅瓦體 (The Galois field with $p$ elements) $[\text{體}]$
* $\mathbf{Z}_p$ : 模 $p$ 剩餘類環 (The ring of residues modulo $p$) $[\text{集合}]$
* $p$ : 質數 (A prime) $[p \in \mathbf{P}]$
* $F$ : 任意一個恰有 $p$ 個元素的體 (An arbitrary field with $p$ elements) $[\text{體}]$
* $x,\ y,\ z$ : 未知數 (Unknowns) $[x, y, z \in GF(7)]$
* 註：投影片 p.2 的定義：**有限體 (finite field)** 又稱**伽羅瓦體 (Galois field)**，就是只含有限個元素的體。
  本章記號：投影片的 $GF_q$、補充講義的 $\mathbb{F}_q$、本章的 $GF(q)$ 三者同義。
* 註：「$\mathbf{Z}_p$ 是體 $\Leftrightarrow$ $p$ 是質數」已於
  [體的定義](../../Abstract_Algebra/Field/Field_Definition.md)【證明 (b)】證明，本檔不重證，
  只補上 (c)：**$p$ 個元素的體只有一個**（同構意義下），所以 $GF(p) = \mathbf{Z}_p$ 這個記號是合法的。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [質數模剩餘類是體 (The residues modulo a prime form a field)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Field/Field_Definition.html#b-proof-that-the-residues-modulo-a-prime-form-a-field)：** 已於 [體的定義](../../Abstract_Algebra/Field/Field_Definition.md)【證明 (b)】完整證明，此處直接引用不再重證

  * (a) 體的判準：

    $$\mathbf{Z}_p \ \text{為體} \quad \Longleftrightarrow \quad p \ \text{為質數}$$

  * (b) 運算的定義（先做整數運算再取餘數）：

    $$a \oplus b = \left(a + b\right) \bmod p, \qquad a \otimes b = \left(ab\right) \bmod p$$

  * $\mathbf{Z}_p$ : 模 $p$ 剩餘類環 (The ring of residues modulo $p$) $[\left\{0, 1, \dots, p-1\right\}]$
  * $a,\ b$ : 剩餘類代表元 (Residue representatives) $[a, b \in \mathbf{Z}_p]$
  * $p$ : 質數 (A prime) $[p \in \mathbf{P}]$

* **【已知 2】 [元素的階整除群的階 (The order of an element divides the group order)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Group/Order_of_Element_and_Cyclic_Subgroup.html#b-proof-that-the-order-of-an-element-divides-the-order-of-the-group)：** 已於 [元素的階與循環子群](../../Abstract_Algebra/Group/Order_of_Element_and_Cyclic_Subgroup.md)【證明 (b)】與【推導 2】完整證明，此處直接引用不再重證。以加法記號寫出

  * (a) 階整除群的階：

    $$o(g) \ \Big|\ \left|G\right|$$

  * (b) 倍數可以化簡到 $0$ 與 $o(g)-1$ 之間：

    $$m = q \cdot o(g) + r,\ 0 \le r < o(g) \quad \Longrightarrow \quad m \cdot g = r \cdot g$$

  * (c) 階的最小性：

    $$0 < r < o(g) \quad \Longrightarrow \quad r \cdot g \neq 0$$

  * $G$ : 有限加法群 (A finite additive group) $[\text{集合}]$
  * $g$ : 群元素 (A group element) $[g \in G]$
  * $o(g)$ : $g$ 的（加法）階 (The additive order of $g$) $[o(g) \in \mathbf{P}]$
  * $m,\ q,\ r$ : 整數 (Integers) $[m, q, r \in \mathbf{Z}]$

* **【已知 3】 [整數倍記號與分配律 (Integer multiples and distributivity)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Ring/Ring_Definition.html#definitions-and-notation)：** 已於 [環的定義](../../Abstract_Algebra/Ring/Ring_Definition.md)【定義 2(c)】給出，此處直接引用

  * (a) 整數倍的加法：

    $$k \cdot 1_F + l \cdot 1_F = \left(k + l\right) \cdot 1_F$$

  * (b) 整數倍的乘法（分配律展開 $kl$ 個 $1_F \times 1_F$）：

    $$\left(k \cdot 1_F\right)\left(l \cdot 1_F\right) = \left(kl\right) \cdot 1_F$$

  * $k,\ l$ : 非負整數 (Non-negative integers) $[k, l \in \mathbf{N}]$
  * $1_F$ : $F$ 的乘法單位元素 (The multiplicative identity of $F$) $[1_F \in F]$

* **【已知 4】 [有限集上單射等價滿射 (Injective iff surjective on a finite set)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Group/Permutation.html#a-proof-the-equivalence-of-injectivity-and-surjectivity-on-a-finite-set)：** 已於 [排列](../../Abstract_Algebra/Group/Permutation.md)【證明 (a)】完整證明，此處直接引用不再重證

  $$\left|A\right| = \left|B\right| < \infty, \quad \phi : A \to B \ \text{單射} \quad \Longrightarrow \quad \phi \ \text{雙射}$$

  * $A,\ B$ : 兩個等大的有限集 (Two finite sets of equal size) $[\text{集合}]$
  * $\phi$ : 映射 (A map) $[A \to B]$

* **【定義 1】 體同構 (Field isomorphism)：** 補充講義 §7.4.1 的定義 —— 一個把加法表與乘法表同時搬過去的雙射

  $$F \cong G \quad \overset{\text{def}}{\Longleftrightarrow} \quad \exists\ \text{雙射}\ h : F \to G, \quad h\left(a + b\right) = h(a) + h(b), \quad h\left(ab\right) = h(a)\,h(b)$$

  * $F,\ G$ : 兩個體 (Two fields) $[\text{體}]$
  * $h$ : 同構映射 (The isomorphism) $[F \to G]$
  * $a,\ b$ : 體元素 (Field elements) $[a, b \in F]$

* **【假設 1】 恰有 $p$ 個元素的體 (A field with exactly p elements)：** 【證明 (c)】的出發點

  $$\left|F\right| = p, \qquad p \ \text{為質數}$$

  * $F$ : 被研究的體 (The field under study) $[\text{體}]$
  * $p$ : 質數 (A prime) $[p \in \mathbf{P}]$

* **【推導 1】 $GF(7)$ 裡需要的兩個反元素 (Two inverses in GF(7))：** 【證明 (b)】消去時要用

  * (a) $3$ 的反元素是 $5$：

    $$3 \otimes 5 \overset{\text{已知 1(b)}}{=} 15 \bmod 7 = 1$$

  * (b) $6$ 的反元素是 $6$：

    $$6 \otimes 6 \overset{\text{已知 1(b)}}{=} 36 \bmod 7 = 1$$

  * 註：$GF(7)$ 裡「除以 $3$」就是「乘以 $5$」，「除以 $6$」就是「乘以 $6$」——
    這就是高斯消去法能在有限體上照做的原因：**每個非零係數都可逆**（【已知 1(a)】）。

* **【推導 2】 $1_F$ 的加法階恰為 $p$ (The additive order of the identity is p)：** 【證明 (c)】的樞紐

  $$\begin{gather*}
  o\!\left(1_F\right) &\overset{\text{已知 2(a)}}{\Big|}& \left|F\right| \\
  o\!\left(1_F\right) &\overset{\text{假設 1}}{\Big|}& p \\
  o\!\left(1_F\right) &\in& \left\{1,\ p\right\} \qquad \text{(} p \text{ 為質數)} \\
  1 \cdot 1_F = 1_F &\neq& 0 \qquad \text{(體要求 } 1 \neq 0\text{)} \\
  o\!\left(1_F\right) &=& p
  \end{gather*}$$

  * $o\!\left(1_F\right)$ : $1_F$ 在 $\left(F, +\right)$ 中的階 (The additive order of $1_F$) $[o(1_F) \in \mathbf{P}]$
  * 註：這同時說明 $\mathrm{ch}(F) = p$（見 [體的特徵](../../Abstract_Algebra/Field/Characteristic_of_a_Field.md)【定義 1】）。

+++

## 證明:

### (a) verify the Cayley tables of the field with two elements

依【已知 1(b)】逐格計算。加法表：

$$\begin{gather*}
0 \oplus 0 &\overset{\text{已知 1(b)}}{=}& 0 \bmod 2 = 0 \\
0 \oplus 1 = 1 \oplus 0 &\overset{\text{已知 1(b)}}{=}& 1 \bmod 2 = 1 \\
1 \oplus 1 &\overset{\text{已知 1(b)}}{=}& 2 \bmod 2 = 0
\end{gather*}$$

乘法表：

$$\begin{gather*}
0 \otimes 0 = 0 \otimes 1 = 1 \otimes 0 &\overset{\text{已知 1(b)}}{=}& 0 \bmod 2 = 0 \\
1 \otimes 1 &\overset{\text{已知 1(b)}}{=}& 1 \bmod 2 = 1
\end{gather*}$$

與投影片一致。

* 註：**$GF(2)$ 的加法就是 XOR、乘法就是 AND** —— 這是所有二元有限體能直接用邏輯閘實作的起點。
* 註：$1 \oplus 1 = 0$ 說明在 $GF(2)$ 裡 $-1 = 1$，**加法與減法是同一件事**。

### (b) solve the linear system over the field with seven elements

把三條方程記為 $E_1, E_2, E_3$。**第一步**：$E_1$ 乘以 $3^{-1} = 5$，使 $x$ 的係數變成 $1$：

$$\begin{gather*}
5 \otimes E_1 : \ 15x + 5y + 20z + 5 &=& 0 \\
E_1' : \ x + 5y + 6z + 5 &\overset{\text{推導 1(a),已知 1(b)}}{=}& 0
\end{gather*}$$

**第二步**：用 $E_1'$ 消去 $E_2, E_3$ 的 $x$：

$$\begin{gather*}
E_2 - 6E_1' : \ \left(5 - 30\right)y + \left(3 - 36\right)z + \left(6 - 30\right) &=& 0 \\
E_2 - 6E_1' : \ 3y + 2z + 4 &\overset{\text{已知 1(b)}}{=}& 0 \\
E_2' = 5 \otimes \left(E_2 - 6E_1'\right) : \ y + 3z + 6 &\overset{\text{推導 1(a),已知 1(b)}}{=}& 0 \\
E_3 - E_1' : \ \left(4 - 5\right)y + \left(2 - 6\right)z + \left(5 - 5\right) &=& 0 \\
E_3 - E_1' : \ 6y + 3z &\overset{\text{已知 1(b)}}{=}& 0
\end{gather*}$$

**第三步**：用 $E_2'$ 消去 $y$，再把 $z$ 的係數化成 $1$：

$$\begin{gather*}
\left(E_3 - E_1'\right) - 6E_2' : \ \left(3 - 18\right)z - 36 &=& 0 \\
\left(E_3 - E_1'\right) - 6E_2' : \ 6z + 6 &\overset{\text{已知 1(b)}}{=}& 0 \\
E_3' = 6 \otimes \left(6z + 6\right) : \ z + 1 &\overset{\text{推導 1(b),已知 1(b)}}{=}& 0
\end{gather*}$$

得到投影片左欄的上三角系統。**回代**：

$$\begin{gather*}
z &\overset{\text{已知 1(b)}}{=}& -1 \bmod 7 = 6 \\
y + 3 \cdot 6 + 6 &=& 0 \qquad \text{(} E_2' \text{ 代入 } z = 6\text{)} \\
y + 3 &\overset{\text{已知 1(b)}}{=}& 0 \qquad \text{(} 24 \bmod 7 = 3\text{)} \\
y &\overset{\text{已知 1(b)}}{=}& -3 \bmod 7 = 4 \\
x + 5 \cdot 4 + 6 \cdot 6 + 5 &=& 0 \qquad \text{(} E_1' \text{ 代入 } y, z\text{)} \\
x + 5 &\overset{\text{已知 1(b)}}{=}& 0 \qquad \text{(} 61 \bmod 7 = 5\text{)} \\
x &\overset{\text{已知 1(b)}}{=}& -5 \bmod 7 = 2
\end{gather*}$$

$\left(x, y, z\right) = \left(2, 4, 6\right)$，與投影片右欄一致（中欄的 $x+5=0$、$y+3=0$、$z+1=0$ 即上面的中間式）。
代回原方程驗算：

$$\begin{gather*}
3 \cdot 2 + 4 + 4 \cdot 6 + 1 &=& 35 \equiv 0 \pmod 7 \\
6 \cdot 2 + 5 \cdot 4 + 3 \cdot 6 + 6 &=& 56 \equiv 0 \pmod 7 \\
2 + 4 \cdot 4 + 2 \cdot 6 + 5 &=& 35 \equiv 0 \pmod 7
\end{gather*}$$

* 註：消去過程每一步都是可逆的列運算（乘以非零常數、加上另一列的倍數），
  所以解**唯一**。這與實數上的高斯消去法完全相同 —— **線性代數只需要「體」，不需要「實數」**。

### (c) proof that every field with a prime number of elements is the residue field

設 $F$ 滿足【假設 1】。定義

$$\phi : \mathbf{Z}_p \to F, \qquad \phi(k) \overset{\text{let}}{=} k \cdot 1_F$$

**單射**：設 $\phi(k) = \phi(l)$，不妨 $0 \le l \le k \le p-1$：

$$\begin{gather*}
k \cdot 1_F &=& l \cdot 1_F \\
\left(k - l\right) \cdot 1_F &\overset{\text{已知 3(a)}}{=}& 0 \\
0 \le k - l &\overset{\text{推導 2}}{<}& o\!\left(1_F\right) \\
k - l &\overset{\text{已知 2(c)}}{=}& 0
\end{gather*}$$

**雙射**：兩邊都有 $p$ 個元素：

$$\begin{gather*}
\left|\mathbf{Z}_p\right| &\overset{\text{假設 1}}{=}& \left|F\right| \\
\phi &\overset{\text{已知 4}}{=}& \text{雙射}
\end{gather*}$$

**保加法**：$k \oplus l = \left(k + l\right) \bmod p$，而 $1_F$ 的 $p$ 倍是 $0$，餘數與原數給出同一個倍數：

$$\begin{gather*}
\phi\left(k \oplus l\right) &\overset{\text{已知 1(b)}}{=}& \left(\left(k + l\right) \bmod p\right) \cdot 1_F \\
&\overset{\text{已知 2(b),推導 2}}{=}& \left(k + l\right) \cdot 1_F \\
&\overset{\text{已知 3(a)}}{=}& k \cdot 1_F + l \cdot 1_F \\
&=& \phi(k) + \phi(l)
\end{gather*}$$

**保乘法**：同理

$$\begin{gather*}
\phi\left(k \otimes l\right) &\overset{\text{已知 1(b)}}{=}& \left(kl \bmod p\right) \cdot 1_F \\
&\overset{\text{已知 2(b),推導 2}}{=}& \left(kl\right) \cdot 1_F \\
&\overset{\text{已知 3(b)}}{=}& \left(k \cdot 1_F\right)\left(l \cdot 1_F\right) \\
&=& \phi(k)\,\phi(l)
\end{gather*}$$

故

$$F \overset{\text{定義 1}}{\cong} \mathbf{Z}_p$$

與補充講義 Theorem 7.6 一致（講義的對應 $\underbrace{1 \oplus \cdots \oplus 1}_{i} \leftrightarrow i$ 就是本證明的 $\phi$）。

* 註：證明**只用到加法群的結構**（$1_F$ 的加法階）與分配律 —— 乘法結構被分配律「免費」決定。
* 註：同一個想法推廣到任意有限體，就是 [有限體的階](../Structure/Order_of_a_Finite_Field.md)
  的「質子體」：任何有限體都含一份 $GF(p)$。

+++

## 意義與密碼學關聯 (Interpretation and Relevance to Cryptography)

### 質體是密碼學的第一個工作台

$GF(p)$ 是最「便宜」的有限體 —— 運算就是整數加乘再取餘數，**不需要任何多項式**。

| 密碼系統 | 使用的體 |
|---|---|
| Diffie–Hellman、DSA、ElGamal | $GF(p)^*$，$p$ 為 2048 位元以上的質數 |
| ECDSA（P-256）、X25519 | $GF(p)$ 上的橢圓曲線，$p = 2^{256} - 2^{224} + \cdots$ 或 $2^{255} - 19$ |
| Shamir 秘密分享 | $GF(p)$ 上的多項式插值 |

### (b) 的線性代數就是 Shamir 秘密分享

【證明 (b)】解的是 $3 \times 3$ 聯立方程。Shamir $(t, n)$ 門檻秘密分享把秘密藏在
$GF(p)$ 上一個 $t-1$ 次多項式的常數項；收集到 $t$ 個點後，
解的正是一個 $t \times t$ 的 Vandermonde 線性系統 —— **與本檔 (b) 是同一種計算**。
能解的前提是「每個非零係數都可逆」，也就是 $p$ 必須是質數。

### (c) 的意義：記號 $GF(p)$ 是良定義的

(c) 保證「$p$ 個元素的體」只有一種。所以規格書裡寫「在 $GF(p)$ 上運算」不會有歧義 ——
不管你怎麼實作，只要元素個數是 $p$ 且滿足體公理，運算表就一定與 $\mathbf{Z}_p$ 相同。
這個「元素個數決定一切」的現象，在 [$GF(p^n)$ 的唯一性](../Structure/Uniqueness_of_GF_p_n.md) 會推廣到所有有限體。
