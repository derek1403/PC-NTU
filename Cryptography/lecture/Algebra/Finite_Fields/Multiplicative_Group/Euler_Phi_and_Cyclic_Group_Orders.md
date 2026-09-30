# Euler Phi and Cyclic Group Orders (尤拉函數與循環群中元素的階)

+++

## 證明目標:

**本檔內容主要出自補充講義** `Introduction_to_Finite_Fields.pdf` §7.3.2–§7.3.4（式 (7.1)、Exercise 3）；
投影片 p.39 只用一句「there are exactly $\phi(d)$ elements of order $d$」帶過。
這是「$GF(q)^*$ 是循環群」證明的純群論部分：**循環群裡各階元素的個數由尤拉函數決定**。

* (a) 階的整除性質：

$$g^k = e \quad \Longleftrightarrow \quad o(g) \mid k$$

* (b) 冪次的階：

$$o\!\left(g^k\right) = \frac{o(g)}{\gcd\left(o(g),\ k\right)}$$

* (c) $n$ 階循環群 $G = \left\langle g \right\rangle$ 中，對每個 $d \mid n$，階為 $d$ 的元素**恰有 $\varphi(d)$ 個**，
  它們全落在唯一的 $d$ 階循環子群 $\left\langle g^{n/d} \right\rangle$ 裡。

* (d) 補充講義式 (7.1)（高斯恆等式）：

$$n = \sum_{d \mid n}\varphi(d)$$

* (e) 驗證補充講義的 $\mathbf{Z}_{10}$ 例子，並證 Exercise 3：$\varphi(n) \ge 1$。

* $G$ : 有限群 (A finite group) $[\text{群}]$
* $g$ : 群元素或生成元 (A group element or generator) $[g \in G]$
* $e$ : 單位元素 (The identity) $[e \in G]$
* $o(g)$ : $g$ 的階 (The order of $g$) $[o(g) \in \mathbf{P}]$
* $k$ : 整數冪次 (An integer exponent) $[k \in \mathbf{Z}]$
* $n$ : 循環群的階 (The order of the cyclic group) $[n \in \mathbf{P}]$
* $d$ : $n$ 的正因數 (A positive divisor of $n$) $[d \in \mathbf{P},\ d \mid n]$
* $\varphi$ : 尤拉函數 (Euler's totient function) $[\mathbf{P} \to \mathbf{P}]$
* 註：投影片寫 $\phi$、本章沿用 Abstract_Algebra 的 $\varphi$，兩者同義。
* 註：補充講義以加法記號（$\mathbf{Z}_n$、$ig$）敘述；本檔用乘法記號（$g^k$），以便直接套到 $GF(q)^*$。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [元素的階與冪次化簡 (Order of an element and reduction of exponents)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Group/Order_of_Element_and_Cyclic_Subgroup.html#a-proof-that-the-powers-of-an-element-form-a-subgroup-of-size-equal-to-the-order)：** 已於 [元素的階與循環子群](../../Abstract_Algebra/Group/Order_of_Element_and_Cyclic_Subgroup.md)【定義 1】【推導 2】【證明 (a)(b)】完整證明，此處直接引用不再重證

  * (a) 階的定義（最小性）：

    $$o(g) = \min\left\{m \in \mathbf{P} \ \middle|\ g^m = e\right\}$$

  * (b) 冪次化簡：

    $$k = q \cdot o(g) + r,\ 0 \le r < o(g) \quad \Longrightarrow \quad g^k = g^r$$

  * (c) 循環子群的大小與階整除群階：

    $$\left|\left\langle g \right\rangle\right| = o(g), \qquad o(g) \ \Big|\ \left|G\right|$$

  * (d) 指數律：

    $$\left(g^a\right)^b = g^{ab}$$

  * $q,\ r$ : 商與餘數 (Quotient and remainder) $[q, r \in \mathbf{Z}]$
  * $a,\ b$ : 整數 (Integers) $[a, b \in \mathbf{Z}]$

* **【已知 2】 [最大公因數的三條性質 (Three properties of the gcd)](https://mathworld.wolfram.com/GreatestCommonDivisor.html)：** 初等數論的標準結果，直接引用不再重證（整數算術另見本課程 Arithmetic 章）

  * (a) 整數的歐幾里得引理：

    $$a \mid bc,\ \gcd(a, b) = 1 \quad \Longrightarrow \quad a \mid c$$

  * (b) 除掉 gcd 後互質：

    $$d = \gcd(n, k) \quad \Longrightarrow \quad \gcd\!\left(\tfrac{n}{d},\ \tfrac{k}{d}\right) = 1$$

  * (c) 公因數可以提出：

    $$\gcd\left(ca,\ cb\right) = c \cdot \gcd\left(a, b\right) \qquad \left(c \in \mathbf{P}\right)$$

  * $a,\ b,\ c,\ n,\ k$ : 整數 (Integers) $[\in \mathbf{Z}]$

* **【已知 3】 [尤拉函數 (Euler's totient function)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Group/Group_Order.html#c-proof-of-the-order-of-the-units-modulo-a-general-number)：** 已於 [數系與符號約定](../../Abstract_Algebra/Number_Sets_and_Notation.md)【定義 4】與 [群的階](../../Abstract_Algebra/Group/Group_Order.md)【證明 (c)】給出，此處直接引用

  $$\varphi(d) = \left|\left\{j \in \left\{0, 1, \dots, d - 1\right\} \ \middle|\ \gcd(j, d) = 1\right\}\right| = \left|\mathbf{Z}_d^*\right|$$

  * $j$ : 候選的剩餘類代表元 (A candidate residue) $[j \in \mathbf{Z}_d]$
  * 註：$d = 1$ 時 $\mathbf{Z}_1 = \left\{0\right\}$ 且 $\gcd(0, 1) = 1$，故 $\varphi(1) = 1$。

* **【假設 1】 有限群中的元素 (An element of a finite group)：** 【證明 (a)(b)】的前提

  $$\left|G\right| < \infty, \qquad g \in G, \qquad n \overset{\text{let}}{=} o(g)$$

  * $G$ : 有限群 (A finite group) $[\text{群}]$

* **【假設 2】 $n$ 階循環群 (A cyclic group of order n)：** 【證明 (c)(d)】的前提

  $$G = \left\langle g \right\rangle = \left\{g^0, g^1, \dots, g^{n-1}\right\}, \qquad \left|G\right| = o(g) = n$$

  * $g$ : 生成元 (A generator) $[g \in G]$
  * 註：例如 $\left(\mathbf{Z}_n, +\right)$ 由 $1$ 生成（加法記號下 $g^k$ 寫成 $k \cdot 1 = k$），故對每個 $n$ 這樣的群都存在。

+++

## 證明:

### (a) proof that a power is the identity exactly when the order divides the exponent

**($\Leftarrow$)**：$k = n m$，則

$$\begin{gather*}
g^k &\overset{\text{假設 1,已知 1(d)}}{=}& \left(g^{n}\right)^{m} \\
&\overset{\text{已知 1(a)}}{=}& e^m = e
\end{gather*}$$

**($\Rightarrow$)**：設 $g^k = e$，除法原理寫 $k = qn + r$：

$$\begin{gather*}
e = g^k &\overset{\text{已知 1(b)}}{=}& g^r, \qquad 0 \le r < n \\
r &\overset{\text{已知 1(a)}}{=}& 0 \qquad \text{(若 } r > 0\text{，與 } n \text{ 的最小性矛盾)} \\
n &\mid& k
\end{gather*}$$

* 註：投影片 p.39 的 Note「$o(a) = o\left(\left\langle a \right\rangle\right) \mid o(G)$ by Lagrange's Theorem」是 (a) 取 $k = \left|G\right|$ 的形式，已由【已知 1(c)】給出。

### (b) proof of the order of a power

設 $d = \gcd(n, k)$。由【證明 (a)】，$\left(g^k\right)^m = e$ 等價於 $n \mid km$；兩邊除以 $d$ 後用歐幾里得引理：

$$\begin{gather*}
\left(g^k\right)^m = e &\overset{\text{已知 1(d),證明 (a)}}{\Longleftrightarrow}& n \mid km \\
n \mid km &\Longleftrightarrow& \tfrac{n}{d} \ \Big|\ \tfrac{k}{d}\,m \\
\tfrac{n}{d} \ \Big|\ \tfrac{k}{d}\,m &\overset{\text{已知 2(a)(b)}}{\Longleftrightarrow}& \tfrac{n}{d} \ \Big|\ m
\end{gather*}$$

使 $\left(g^k\right)^m = e$ 的最小正整數 $m$ 因此是 $n/d$：

$$o\!\left(g^k\right) \overset{\text{已知 1(a)}}{=} \frac{n}{\gcd(n, k)}$$

與補充講義 §7.3.4「$\left|S(m)\right| = n / \gcd(m, n)$」一致。

### (c) proof that a cyclic group has exactly phi of d elements of each order d

由【假設 2】，$G$ 的元素是 $g^k$（$0 \le k < n$，兩兩相異）。先刻畫哪些 $k$ 使 $g^k$ 的階為 $d$
（$j$ 為 $k$ 除以 $n/d$ 的商）：

$$\begin{gather*}
o\!\left(g^k\right) = d &\overset{\text{證明 (b)}}{\Longleftrightarrow}& \gcd(n, k) = \tfrac{n}{d} \\
\gcd(n, k) = \tfrac{n}{d} &\Longleftrightarrow& k = \tfrac{n}{d}\,j,\ \ \gcd\!\left(\tfrac{n}{d}\,d,\ \tfrac{n}{d}\,j\right) = \tfrac{n}{d} \\
\gcd\!\left(\tfrac{n}{d}\,d,\ \tfrac{n}{d}\,j\right) = \tfrac{n}{d} &\overset{\text{已知 2(c)}}{\Longleftrightarrow}& \gcd(d, j) = 1
\end{gather*}$$

（第二列的「$\Rightarrow$」：$\gcd(n,k) = n/d$ 整除 $k$，故 $k$ 是 $n/d$ 的倍數；$0 \le k < n$ 使 $0 \le j < d$。）
於是階為 $d$ 的元素與「$0 \le j < d$、$\gcd(j,d) = 1$」的 $j$ 一一對應：

$$\begin{gather*}
\left\{x \in G \ \middle|\ o(x) = d\right\} &\overset{\text{假設 2}}{=}& \left\{\left(g^{n/d}\right)^j \ \middle|\ 0 \le j < d,\ \gcd(j, d) = 1\right\} \\
\left|\left\{x \in G \ \middle|\ o(x) = d\right\}\right| &\overset{\text{已知 3}}{=}& \varphi(d)
\end{gather*}$$

這些元素全是 $h = g^{n/d}$ 的冪次，而 $o(h) = d$，故全落在 $d$ 階循環子群 $\left\langle h \right\rangle$ 裡：

$$\begin{gather*}
o\!\left(g^{n/d}\right) &\overset{\text{證明 (b)}}{=}& \frac{n}{\gcd\left(n,\ n/d\right)} = \frac{n}{n/d} = d \\
\left|\left\langle g^{n/d} \right\rangle\right| &\overset{\text{已知 1(c)}}{=}& d
\end{gather*}$$

任何 $d$ 階元素 $x$ 生成的子群 $\left\langle x \right\rangle$ 也是 $d$ 階且包含於 $\left\langle h \right\rangle$，故等於它 —— **$d$ 階循環子群唯一**。

### (d) proof of Gauss's identity for Euler's function

$G$ 的每個元素都有唯一的階，且階整除 $n$（【已知 1(c)】）。按階分類後計數：

$$\begin{gather*}
n = \left|G\right| &\overset{\text{假設 2}}{=}& \sum_{d \mid n}\left|\left\{x \in G \ \middle|\ o(x) = d\right\}\right| \\
n &\overset{\text{證明 (c)}}{=}& \sum_{d \mid n}\varphi(d)
\end{gather*}$$

與補充講義式 (7.1) 一致。

* 註：$n$ 階循環群對每個 $n$ 都存在（【假設 2】的註），所以 (7.1) 是**關於整數的恆等式**，與群無關。

### (e) verify the example of the residues modulo ten

在 $\left(\mathbf{Z}_{10}, +\right)$ 中（生成元 $1$，加法記號下 $o(m) = 10 / \gcd(m, 10)$）：

$$\begin{gather*}
o(0) &\overset{\text{證明 (b)}}{=}& 10/10 = 1 \\
o(5) &\overset{\text{證明 (b)}}{=}& 10/5 = 2 \\
o(2) = o(4) = o(6) = o(8) &\overset{\text{證明 (b)}}{=}& 10/2 = 5 \\
o(1) = o(3) = o(7) = o(9) &\overset{\text{證明 (b)}}{=}& 10/1 = 10 \\
1 + 1 + 4 + 4 &=& \varphi(1) + \varphi(2) + \varphi(5) + \varphi(10) = 10
\end{gather*}$$

與補充講義 §7.3.4 的列表一致。**Exercise 3**：$1$ 在 $\mathbf{Z}_n$ 中的階是 $n$（$\gcd(1, n) = 1$），
故由【證明 (c)】階為 $n$ 的元素至少一個：

$$\varphi(n) \overset{\text{證明 (c)}}{=} \left|\left\{x \in \mathbf{Z}_n \ \middle|\ o(x) = n\right\}\right| \ge 1$$

+++

## 意義與密碼學關聯 (Interpretation and Relevance to Cryptography)

### 生成元有多少個

(c) 取 $d = n$：**$n$ 階循環群恰有 $\varphi(n)$ 個生成元**。
[循環群](../../Abstract_Algebra/Group/Cyclic_Group.md) 文末的「$\mathbf{Z}_n^*$ 循環時有 $\varphi\left(\varphi(n)\right)$ 個生成元」就是這條。
對 Diffie–Hellman 的 $GF(p)^*$（階 $p - 1$），隨機挑一個元素是生成元的機率為

$$\frac{\varphi(p - 1)}{p - 1} = \prod_{r \mid p-1}\left(1 - \frac{1}{r}\right)$$

對**安全質數** $p = 2r' + 1$（$r'$ 也是質數）這個機率約為 $1/2$，所以隨機試幾次就找得到。

### (b) 是小子群攻擊的算術基礎

$o\!\left(g^k\right) = n / \gcd(n, k)$ 說：**指數與群階有公因數，元素的階就會縮小**。
攻擊者送出 $g^{n/r}$（$r$ 是 $n$ 的小質因數），它的階只有 $r$，
受害者算出的共享值只有 $r$ 種可能 —— 這就是 small subgroup attack。
防禦方法是選 $n$ 為大質數（或大質數乘小餘因子）的子群，並檢查收到的元素的階。

### 程式思維

```python
from math import gcd
phi = lambda d: sum(1 for j in range(d) if gcd(j, d) == 1)

n = 10
orders = [n // gcd(m, n) for m in range(n)]                       # 證明 (b)
assert orders == [1, 10, 5, 10, 5, 2, 5, 10, 5, 10]                # 證明 (e)
assert all(orders.count(d) == phi(d) for d in (1, 2, 5, 10))       # 證明 (c)
assert all(sum(phi(d) for d in range(1, m + 1) if m % d == 0) == m for m in range(1, 500))   # 證明 (d)
```
