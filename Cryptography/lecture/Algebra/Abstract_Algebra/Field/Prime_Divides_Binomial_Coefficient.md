# Prime Divides Binomial Coefficient (質數整除二項式係數)

+++

## 證明目標:

`Algebra.pdf` p.47（上半）。一條純數論的引理，但它是 [新生之夢](Freshmans_Dream.md) 的**唯一**支柱 ——
帕斯卡三角形的第 $p$ 列（$p$ 為質數）除了頭尾兩個 $1$ 之外，**全部是 $p$ 的倍數**。

* (a) 主結論：

$$p \ \Bigg|\ \binom{p}{i} \qquad \text{for } 1 \le i \le p-1,\ p \ \text{為質數}$$

* (b) 用 $p = 5$ 驗證：

$$\binom{5}{1} = 5, \quad \binom{5}{2} = 10, \quad \binom{5}{3} = 10, \quad \binom{5}{4} = 5 \qquad \text{全部是 } 5 \ \text{的倍數}$$

* (c) **質數性不可省** —— $p = 4$ 時 $\dbinom{4}{2} = 6$ 不是 $4$ 的倍數。

* $p$ : 質數 (A prime) $[p \in \mathbf{P}]$
* $i$ : 二項式係數的下標 (The lower index of the binomial coefficient) $[i \in \mathbf{Z},\ 1 \le i \le p-1]$
* $\dbinom{p}{i}$ : 二項式係數 (The binomial coefficient) $[\dbinom{p}{i} \in \mathbf{P}]$
* 註：**投影片寫的範圍是 $2 \le i \le p-1$**，比本檔窄一格。
  $i = 1$ 的情形其實也成立且更明顯（$\dbinom{p}{1} = p$），
  而 [新生之夢](Freshmans_Dream.md) 需要**整個** $1 \le i \le p-1$ 的範圍，
  故本檔採較寬的敘述。結論本身沒有改變。
* 註：$i = 0$ 與 $i = p$ 兩端是 $\dbinom{p}{0} = \dbinom{p}{p} = 1$，**不**被 $p$ 整除 ——
  這兩項正是 [新生之夢](Freshmans_Dream.md) 裡唯一存活下來的 $a^p$ 與 $b^p$。
* 註：本檔是純整數的命題，與體無關。它在 [新生之夢](Freshmans_Dream.md) 才會被搬到特徵 $p$ 的體上。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [二項式係數的定義 (Definition of the binomial coefficient)](https://mathworld.wolfram.com/BinomialCoefficient.html)：** 組合學的標準定義，本章直接引用不再重證

  * (a) 階乘形式：

    $$\binom{n}{i} \overset{\text{def}}{=} \frac{n!}{i!\,\left(n-i\right)!}$$

  * (b) 連乘形式（投影片採用的寫法）：

    $$\binom{n}{i} = \frac{n\left(n-1\right)\cdots\left(n-i+1\right)}{i!}$$

  * (c) 二項式係數是**整數**（它是組合計數的結果）：

    $$\binom{n}{i} \in \mathbf{N}$$

  * $n$ : 上標 (The upper index) $[n \in \mathbf{N}]$
  * $i$ : 下標 (The lower index) $[i \in \mathbf{Z},\ 0 \le i \le n]$
  * $\dbinom{n}{i}$ : 二項式係數 (The binomial coefficient) $[\dbinom{n}{i} \in \mathbf{N}]$
  * 註：(c) 這件事本身不平凡（分母的 $i!$ 恰好約得乾淨），但它是組合意義的直接後果
    —— 從 $n$ 個東西裡選 $i$ 個的方法數必定是整數。本章直接引用。

* **【已知 2】 [歐幾里得引理與互質性 (Euclid's lemma and coprimality)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Ring/Zero_Divisor.html#assumptions-preliminaries)：** 已於本章 [群的正例與反例](../Group/Group_Examples_and_Counterexamples.md)【已知 6】與 [零因子](../Ring/Zero_Divisor.md)【已知 3】引用，此處再次引用

  * (a) 歐幾里得引理：

    $$p \ \text{為質數}, \quad p \mid ab \quad \Longrightarrow \quad p \mid a \ \text{ 或 } \ p \mid b$$

  * (b) 推廣到多個因子（對 (a) 做歸納即得，本章直接引用）：

    $$p \ \text{為質數}, \quad p \mid a_1 a_2 \cdots a_k \quad \Longrightarrow \quad p \mid a_j \ \text{ for some } j$$

  * $p$ : 質數 (A prime) $[p \in \mathbf{P}]$
  * $a,\ b,\ a_j$ : 任意整數 (Arbitrary integers) $[a, b, a_j \in \mathbf{Z}]$
  * $k,\ j$ : 因子個數與指標 (The number of factors and the index) $[k, j \in \mathbf{P}]$

* **【推導 1】 質數不整除比它小的數的階乘 (A prime does not divide the factorial of a smaller number)：** 【證明 (a)】要用

  $$\begin{gather*}
  m! &=& 1 \times 2 \times \cdots \times m \qquad \left(1 \le m < p\right) \\
  1 \le t \le m &<& p \qquad \text{for every factor } t \\
  p &\nmid& t \qquad \text{(因 } p \text{ 為質數且 } t < p\text{，唯一的正因數是 } 1 \text{ 與 } p\text{)} \\
  p &\overset{\text{已知 2(b)}}{\nmid}& m!
  \end{gather*}$$

  * $p$ : 質數 (A prime) $[p \in \mathbf{P}]$
  * $m$ : 比 $p$ 小的正整數 (A positive integer smaller than $p$) $[m \in \mathbf{P},\ m < p]$
  * $t$ : $m!$ 的一個因子 (A factor of $m!$) $[t \in \mathbf{P},\ t \le m]$
  * 註：最後一行是【已知 2(b)】的**逆否形式** ——
    若 $p$ 整除乘積，則必整除某個因子；每個因子都不被整除，故乘積也不被整除。
  * 註：**這裡用到了質數性兩次**：一次確認 $t < p$ 時 $p \nmid t$，
    一次套用歐幾里得引理。合數沒有這個性質（例如 $4 \mid 4! = 24$ 雖然 $4 \nmid 1,2,3$ ——
    嗯，$4 \mid 4$ 但 $4$ 不在 $3!$ 裡；取 $m = 3$、合數 $n = 4$，$4 \nmid 6 = 3!$，
    但 $n = 6$、$m = 4$ 時 $6 \mid 24 = 4!$，歐幾里得引理失效）。

+++

## 證明:

### (a) proof that a prime divides the interior binomial coefficients

設 $p$ 為質數、$1 \le i \le p-1$。把【已知 1(a)】的分母乘到左邊，化成整數等式：

$$\begin{gather*}
\binom{p}{i} &\overset{\text{已知 1(a)}}{=}& \frac{p!}{i!\left(p-i\right)!} \\
\binom{p}{i} \cdot i! \cdot \left(p-i\right)! &=& p! \\
p! &=& p \times \left(p-1\right)! \\
\binom{p}{i} \cdot i! \cdot \left(p-i\right)! &=& p \times \left(p-1\right)!
\end{gather*}$$

右端顯然被 $p$ 整除，故左端也是。左端是三個整數的乘積（【已知 1(c)】保證第一個是整數），
套用歐幾里得引理：

$$\begin{gather*}
p &\Bigg|& \binom{p}{i} \cdot i! \cdot \left(p-i\right)! \\
p \ \Bigg|\ \binom{p}{i} \quad \text{或} \quad p \mid i! \quad \text{或} \quad p &\overset{\text{已知 2(b)}}{\mid}& \left(p-i\right)!
\end{gather*}$$

後兩個可能性被【推導 1】排除 —— 因為 $1 \le i \le p-1$ 保證兩個階乘的上標都小於 $p$：

$$\begin{gather*}
1 \le i &\le& p - 1 < p \\
1 \le p - i &\le& p - 1 < p \\
p &\overset{\text{推導 1}}{\nmid}& i! \\
p &\overset{\text{推導 1}}{\nmid}& \left(p-i\right)! \\
p &\Bigg|& \binom{p}{i}
\end{gather*}$$

* 註：**投影片的寫法**用的是【已知 1(b)】的連乘形式：
  分子 $p\left(p-1\right)\cdots\left(p-i+1\right)$ **明顯含一個 $p$**，
  而分母 $i!$ 與 $p$ 互質（【推導 1】），所以那個 $p$ 約不掉，必定留在商裡。
  兩種寫法的邏輯核心相同，本檔採階乘形式是為了避免處理「分數的整除」。
* 註：**$i$ 的範圍限制是本命題的全部要害**。$i = 0$ 或 $i = p$ 時
  $\left(p-i\right)!$ 或 $i!$ 會變成 $p!$，裡面就含 $p$ 了，【推導 1】失效 ——
  而那兩項的值恰好是 $1$，確實不被 $p$ 整除。

### (b) verify the fifth row of Pascal's triangle

取 $p = 5$，逐一計算 $1 \le i \le 4$：

$$\begin{gather*}
\binom{5}{1} &\overset{\text{已知 1(a)}}{=}& \frac{120}{1 \times 24} = 5 \\
\binom{5}{2} &\overset{\text{已知 1(a)}}{=}& \frac{120}{2 \times 6} = 10 \\
\binom{5}{3} &\overset{\text{已知 1(a)}}{=}& \frac{120}{6 \times 2} = 10 \\
\binom{5}{4} &\overset{\text{已知 1(a)}}{=}& \frac{120}{24 \times 1} = 5
\end{gather*}$$

四個值都是 $5$ 的倍數，與【證明 (a)】一致。完整的第五列是：

$$1, \quad 5, \quad 10, \quad 10, \quad 5, \quad 1$$

**頭尾的兩個 $1$ 不被 $5$ 整除，中間四個全被整除** —— 這就是
[新生之夢](Freshmans_Dream.md) 會發生的原因。

### (c) disprove the claim for a composite upper index

取 $p = 4$（合數）、$i = 2$：

$$\begin{gather*}
\binom{4}{2} &\overset{\text{已知 1(a)}}{=}& \frac{24}{2 \times 2} = 6 \\
6 &=& 4 \times 1 + 2 \\
4 &\nmid& 6
\end{gather*}$$

故 $4 \nmid \dbinom{4}{2}$，**質數性不可省**。完整的第四列是：

$$1, \quad 4, \quad 6, \quad 4, \quad 1$$

中間的 $6$ 破壞了規律。

* 註：失敗的原因追溯到【推導 1】—— $4 \mid 2! \times 2! = 4$，
  所以分母吃掉了分子的那個 $4$。歐幾里得引理對合數不成立，整條論證在那裡斷掉。
* 註：這也預告了 [新生之夢](Freshmans_Dream.md) 為什麼只在特徵為**質數**時成立。

+++

## 意義與密碼學關聯 (Interpretation and Relevance to Cryptography)

### 帕斯卡三角形裡的質數指紋

把前幾列並排，被 $p$ 整除的項標成 $\bullet$：

| $n$ | 第 $n$ 列 | $n$ 是質數？ | 中間項全被 $n$ 整除？ |
|---|---|---|---|
| $2$ | $1,\ 2,\ 1$ | **是** | **是**（$2$） |
| $3$ | $1,\ 3,\ 3,\ 1$ | **是** | **是**（$3, 3$） |
| $4$ | $1,\ 4,\ \mathbf{6},\ 4,\ 1$ | 否 | **否**（$6$ 壞了） |
| $5$ | $1,\ 5,\ 10,\ 10,\ 5,\ 1$ | **是** | **是** |
| $6$ | $1,\ 6,\ \mathbf{15},\ \mathbf{20},\ \mathbf{15},\ 6,\ 1$ | 否 | **否** |
| $7$ | $1,\ 7,\ 21,\ 35,\ 35,\ 21,\ 7,\ 1$ | **是** | **是** |

**「第 $n$ 列的中間項是否全被 $n$ 整除」恰好就是「$n$ 是不是質數」** ——
【證明 (a)】給了一個方向，【證明 (c)】的失敗給了另一個方向的直覺。

這其實可以當成一個（極慢的）質數測試，但它的真正價值在下一檔。

### 這條引理唯一的用途

本檔是全章最「工具性」的一檔 —— 它本身沒有密碼學應用，
存在的唯一理由是撐起 [新生之夢](Freshmans_Dream.md)：

$$\left(a+b\right)^p = \sum_{i=0}^{p}\binom{p}{i}a^i b^{p-i} \ \overset{\text{特徵 } p}{=} \ a^p + b^p$$

在特徵 $p$ 的體裡，**被 $p$ 整除的係數全部變成 $0$**（因為 $p \cdot 1_F = 0$），
只剩 $i = 0$ 與 $i = p$ 兩項。中間那些項之所以全部消失，就是本檔證的事。

而新生之夢是 **Frobenius 自同態** $x \mapsto x^p$ 的基礎，
後者用在：

* **Schoof 演算法** —— 橢圓曲線的點計數，ECC 參數產生的核心工具；
* **配對密碼學** —— Frobenius 映射用來加速 Miller 演算法；
* **有限體的建構** —— $GF(p^n)$ 的元素恰好是 $x^{p^n} = x$ 的解。

**一條關於帕斯卡三角形的小觀察，撐起了整個有限體理論。**

### 程式思維

```python
from math import comb

def prime_divides_interior(p):
    """檢查第 p 列的中間項是否全被 p 整除（證明 (a)）。"""
    return all(comb(p, i) % p == 0 for i in range(1, p))

assert prime_divides_interior(5)        # 質數
assert prime_divides_interior(7)
assert not prime_divides_interior(4)    # 合數，證明 (c)
assert not prime_divides_interior(6)
```

注意這段程式**可以當質數測試用**，但它要算 $p-1$ 個二項式係數，
而那些數字大得嚇人（$\dbinom{p}{p/2} \approx 2^p/\sqrt{p}$）。
實務上的質數測試用的是 Miller–Rabin
（見 [元素的階與循環子群](../Group/Order_of_Element_and_Cyclic_Subgroup.md) 文末），
複雜度是多項式時間。
