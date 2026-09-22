# Lagrange Theorem (拉格朗日定理)

+++

## 證明目標:

`Algebra.pdf` p.20（上半）。有限群論最核心的定理，也是本章前面所有工作的匯流點。

* (a) 子群的階整除母群的階：

$$\left|H\right| \ \Big|\ \left|G\right| \qquad \left(H \le G,\ \left|G\right| < \infty\right)$$

* (b) 相異左陪集的個數，恰好是兩個階的商，稱為 $H$ 在 $G$ 中的**指標**：

$$\left[G : H\right] = \frac{\left|G\right|}{\left|H\right|}$$

* $G$ : 有限群的底層集合 (The underlying set of a finite group) $[\text{集合}]$
* $H$ : $G$ 的子群 (A subgroup of $G$) $[H \le G]$
* $\left|G\right|,\ \left|H\right|$ : 兩者的階 (Their orders) $[\left|G\right|, \left|H\right| \in \mathbf{P}]$
* $\left[G : H\right]$ : $H$ 在 $G$ 中的指標 (The index of $H$ in $G$) $[\left[G:H\right] \in \mathbf{P}]$
* 註：**$G$ 必須有限。** 無限群的「整除」沒有意義（但 [陪集分割](Coset_Partition.md) 的三條引理對無限群仍成立，
  指標仍可定義為陪集的個數）。
* 註：本檔的證明**極短**，因為所有力氣都已經花在 [陪集分割](Coset_Partition.md) 了。
  那三條引理（陪集等勢、互斥、覆蓋）一旦到手，拉格朗日定理只是把它們寫成一個等式。
* 註：**逆命題不成立** —— $d \mid \left|G\right|$ 不保證 $G$ 有階為 $d$ 的子群。
  最小的反例是 $12$ 階的交錯群 $A_4$，它沒有 $6$ 階子群。本章不證這件事，但不要誤用定理。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [陪集分割 (Coset partition)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Group/Coset_Partition.html#d-proof-that-the-left-cosets-form-a-partition)：** 已於本章 [陪集分割](Coset_Partition.md) 完整證明，此處直接引用不再重證

  * (a) 陪集等勢（【陪集分割】【證明 (a)】）：

    $$\left|gH\right| = \left|H\right| \qquad \text{for all } g \in G$$

  * (b) 相異陪集互斥（【陪集分割】【證明 (b)】）：

    $$g_1H \neq g_2H \quad \Longrightarrow \quad g_1H \cap g_2H = \varnothing$$

  * (c) 陪集覆蓋整個群（【陪集分割】【證明 (c)】）：

    $$\bigcup_{g \in G} gH = G$$

  * $G$ : 有限群的底層集合 (The underlying set of a finite group) $[\text{集合}]$
  * $H$ : $G$ 的子群 (A subgroup of $G$) $[H \le G]$
  * $g,\ g_1,\ g_2$ : 陪集代表元 (Coset representatives) $[g, g_1, g_2 \in G]$
  * $gH$ : 左陪集 (A left coset) $[gH \subseteq G]$

* **【已知 2】 [有限集合分割的計數 (Counting a partition of a finite set)](https://mathworld.wolfram.com/SetPartition.html)：** 集合論的標準結果，本章直接引用不再重證。不重不漏地切開後，各塊大小相加就是全體

  $$\left\{A_1, \dots, A_k\right\} \ \text{為 } G \ \text{的分割} \quad \Longrightarrow \quad \left|G\right| = \sum_{i=1}^{k}\left|A_i\right|$$

  * $A_i$ : 分割中的一塊 (A block of the partition) $[A_i \subseteq G]$
  * $k$ : 塊數 (The number of blocks) $[k \in \mathbf{P}]$
  * $G$ : 被分割的有限集合 (The finite set being partitioned) $[\text{集合}]$
  * $i$ : 塊的指標 (Block index) $[i \in \left\{1, \dots, k\right\}]$

* **【定義 1】 指標 (Index)：** $H$ 在 $G$ 中的**相異**左陪集個數

  $$\left[G : H\right] \overset{\text{def}}{=} \left|\left\{gH \ \middle|\ g \in G\right\}\right|$$

  * $\left[G : H\right]$ : $H$ 在 $G$ 中的指標 (The index of $H$ in $G$) $[\left[G:H\right] \in \mathbf{P}]$
  * $H$ : $G$ 的子群 (A subgroup of $G$) $[H \le G]$
  * $G$ : 母群的底層集合 (The underlying set of the ambient group) $[\text{集合}]$
  * $g$ : 陪集代表元 (A coset representative) $[g \in G]$
  * 註：外層的 $\left|\cdot\right|$ 數的是**集合的集合**的大小 —— 重複的陪集只算一次。
    投影片把 $\left[G:H\right]$ 直接定義成 $\left|G\right|/\left|H\right|$，
    本檔改從「陪集個數」定義，再用【證明 (b)】證明兩者相等。
    **這樣定義比較誠實**：陪集個數是可以直接數的，而「商是整數」是要證的結論。

+++

## 證明:

### (a) proof of Lagrange's theorem

由【已知 1(b)(c)】，相異的左陪集構成 $G$ 的一個分割。設相異陪集共 $k$ 個，
分別記作 $g_1H, g_2H, \dots, g_kH$。

把【已知 2】的計數公式套上去，再用【已知 1(a)】把每一塊的大小換成 $\left|H\right|$：

$$\begin{gather*}
\left|G\right| &\overset{\text{已知 2}}{=}& \sum_{i=1}^{k}\left|g_iH\right| \\
&\overset{\text{已知 1(a)}}{=}& \sum_{i=1}^{k}\left|H\right| \\
&=& k\left|H\right|
\end{gather*}$$

$\left|G\right|$ 是 $\left|H\right|$ 的整數倍，即：

$$\left|H\right| \ \Big|\ \left|G\right|$$

### (b) proof of the index formula

【證明 (a)】的 $k$ 依【定義 1】就是指標。把 $\left|G\right| = k\left|H\right|$ 解出 $k$：

$$\begin{gather*}
\left|G\right| &\overset{\text{證明 (a)}}{=}& k\left|H\right| \\
k &=& \frac{\left|G\right|}{\left|H\right|} \\
\left[G : H\right] &\overset{\text{定義 1}}{=}& \frac{\left|G\right|}{\left|H\right|}
\end{gather*}$$

與投影片的定義式一致，且由【證明 (a)】保證這個商確實是整數。

* 註：$\left|H\right| \neq 0$ 因為 $H$ 至少含單位元素
  （[子群判別法](Subgroup_Criterion.md)【證明 (b)】），故除法合法。

+++

## 意義與密碼學關聯 (Interpretation and Relevance to Cryptography)

### 回頭檢查前面的例子

[子群的例子](Subgroup_Examples.md) 觀察到的整除現象，現在全部有了解釋：

| 子群 $H$ | $\left\|H\right\|$ | 母群 $G$ | $\left\|G\right\|$ | 指標 $\left[G:H\right]$ |
|---|---|---|---|---|
| $\left\{e,\left(123\right),\left(132\right)\right\}$ | $3$ | $S_3$ | $6$ | $2$ |
| $\left\{1, 8\right\}$ | $2$ | $\mathbf{Z}_9^*$ | $6$ | $3$ |
| $T_2(\mathbf{Z}_7)$ | $252$ | $GL_2(\mathbf{Z}_7)$ | $2016$ | $8$ |
| $\left\{e, \left(12\right)\right\}$ | $2$ | $S_3$ | $6$ | $3$ |

**指標就是「切出了幾塊蛋糕」。** $S_3$ 對 $\left\{e,\left(12\right)\right\}$ 切成三塊，
每塊兩個元素 —— [陪集](Coset.md)【證明 (a)】算出的
$\left(123\right)H = \left\{\left(123\right),\left(13\right)\right\}$ 就是其中一塊。

### 定理的威力：用「大小」反推「結構」

拉格朗日定理的價值不在於算出某個數字，而在於**它能一口氣排除掉大量可能性**：

* $\left|G\right| = 12$ 的群，子群的階只可能是 $1, 2, 3, 4, 6, 12$。
  **絕對不可能有階為 $5$ 的子群** —— 連找都不用找。
* $\left|G\right| = p$（質數）的群，子群只有 $\left\{e\right\}$ 與 $G$ 自己。
  **質數階的群沒有任何真子群。**

第二點在密碼學裡極其重要，見下一段。

### 為什麼密碼學偏愛質數階的群

[陪集分割](Coset_Partition.md) 文末提到 Legendre 符號攻擊 ——
攻擊者利用子群的存在，從元素「落在哪一塊」榨取資訊。

拉格朗日定理給出了根本的防禦：**把運算限制在質數階 $q$ 的子群裡**。
質數階的群沒有真子群，所以：

* 沒有可以利用的分割，攻擊者無從判斷「落在哪一塊」；
* 每個非單位元素的階都是 $q$（見 [元素的階與循環子群](Order_of_Element_and_Cyclic_Subgroup.md)），
  因此**每個非單位元素都是生成元**，不必擔心誤選到階很小的元素。

這就是為什麼：

| 協議 | 群的選擇 | 理由 |
|---|---|---|
| DSA / DH | $\mathbf{Z}_p^*$ 中階為 $q$ 的子群（$q \mid p-1$，$q$ 為質數） | 質數階，無真子群 |
| Ed25519 | 橢圓曲線群中階為 $\ell$ 的子群（$\ell$ 為質數） | 同上；曲線階 $= 8\ell$，需清除 cofactor |
| secp256k1（比特幣） | 階本身就是質數 | cofactor $= 1$，最乾淨 |

Ed25519 的 cofactor $8$ 是個實際的麻煩來源 ——
曲線群的階是 $8\ell$，所以存在階為 $2, 4, 8$ 的小子群。
實作若沒有乘上 cofactor 把元素推進大子群，就會受到 small subgroup attack。
**這個 $8$ 之所以存在、之所以危險，完全是拉格朗日定理在講的事。**

### 通往尤拉定理

拉格朗日定理最直接的密碼學後果還沒登場。下一檔
[元素的階與循環子群](Order_of_Element_and_Cyclic_Subgroup.md) 會證明系理
$o(g) \mid \left|G\right|$，再由它推出：

$$a^{\varphi(n)} \equiv 1 \pmod{n} \qquad \left(\gcd(a,n) = 1\right)$$

**這一行就是 RSA 解密之所以成立的全部理由。**
而它只是「$\left|H\right|$ 整除 $\left|G\right|$」的一個特例。

### 逆命題不成立：一個容易犯的錯

拉格朗日定理說「子群的階整除群的階」，**不是**「群的階的每個因數都有對應的子群」。

$A_4$（$12$ 階）沒有 $6$ 階子群，是最小的反例。

實務上這意味著：看到 $\left|G\right| = 2^{256}$ 不能直接斷言「存在階為 $2^{128}$ 的子群」。
不過對**循環群**（密碼學最常用的那種）逆命題確實成立 ——
循環群對每個 $d \mid \left|G\right|$ 都恰有一個 $d$ 階子群。
這是循環群結構單純的又一個好處，見 [循環群](Cyclic_Group.md)。
