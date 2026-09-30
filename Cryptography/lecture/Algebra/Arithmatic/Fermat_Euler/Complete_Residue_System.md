# Complete Residue System (完全剩餘系)

+++

## 證明目標:

`Arithmetic.pdf` p.48。「每個同餘類恰好挑一個代表」的集合。
它是 [尤拉函數的乘法性](Euler_Phi_Multiplicativity.md) 與 [化簡剩餘系](Reduced_Residue_System.md) 的基礎工具。

* (a) 完全剩餘系的等價刻畫：$C$ 是完全剩餘系，若且唯若「取餘數」是 $C$ 到 $\mathbf{Z}_m$ 的雙射

$$\rho : C \to \left\{0, 1, \dots, m-1\right\}, \qquad \rho(c) = c \bmod m$$

* (b) 完全剩餘系恰有 $m$ 個元素。
* (c) 判別法（投影片未列，本章補）：**$m$ 個兩兩不同餘的整數**必構成完全剩餘系。
* (d) $\left\{0, 1, \dots, m-1\right\}$ 是完全剩餘系（投影片稱為 least non-negative residue system）。
* (e) 驗證投影片的三個模 $7$ 例子：

$$\left\{0, 1, 2, 3, 4, 5, 6\right\}, \qquad \left\{-3, -2, -1, 0, 1, 2, 3\right\}, \qquad \left\{-15, -10, -5, 1, 3, 5, 7\right\}$$

* $C$ : 整數的子集 (A set of integers) $[C \subseteq \mathbf{Z}]$
* $m$ : 模數 (The modulus) $[m \in \mathbf{P}]$
* $\rho$ : 取餘數映射 (The reduction map) $[C \to \mathbf{Z}_m]$
* 註：投影片寫「$C \subset \mathbf{Z}$」，這裡的 $\subset$ 指一般的子集（$\subseteq$），不是真子集的意思。
* 註：投影片的 Remark「1) existence 2) uniqueness of each entry in $C$」正是 (a) 的「滿射」與「單射」。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [同餘與取模 (Congruence and remainders)](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/Congruence/Congruence_Relation.html#c-proof-that-every-integer-is-congruent-to-its-remainder)：** 已於本章 [同餘關係](../Congruence/Congruence_Relation.md)【定義 1】【證明 (c)】與 [取模函數](../Division/Modular_Function.md)【證明 (a)(b)】給出並證明，此處直接引用不再重證

  * (a) 同餘的定義：

    $$u \equiv v \pmod{m} \quad \Longleftrightarrow \quad u \bmod m = v \bmod m$$

  * (b) 餘數落在 $\left[0, m\right)$，且 $\left[0, m\right)$ 裡的數就是自己的餘數：

    $$0 \le u \bmod m < m, \qquad 0 \le r < m \ \Longrightarrow \ r \bmod m = r$$

  * $u,\ v$ : 任意整數 (Arbitrary integers) $[u, v \in \mathbf{Z}]$
  * $r$ : 落在 $\left[0, m\right)$ 的整數 (An integer in $\left[0, m\right)$) $[r \in \mathbf{Z}_m]$
  * $m$ : 模數 (The modulus) $[m \in \mathbf{P}]$

* **【已知 2】 [鴿籠原理 (Pigeonhole principle)](https://mathworld.wolfram.com/DirichletsBoxPrinciple.html)：** 有限集合的標準結果，本章直接引用不再重證。等大小的有限集合之間，單射必是雙射

  $$f : A \to B \ \text{單射},\ \ \left|A\right| = \left|B\right| < \infty \quad \Longrightarrow \quad f \ \text{雙射}$$

  * $A,\ B$ : 有限集合 (Finite sets) $[\text{集合}]$
  * $f$ : 映射 (A map) $[A \to B]$
  * 註：與 Abstract_Algebra 章 [排列](../../Abstract_Algebra/Group/Permutation.md)【證明 (a)】的「有限集上單射等價滿射」是同一條原理。

* **【定義 1】 完全剩餘系 (Complete residue system)：** 投影片的兩條

  * (a) 存在（每個整數都有代表）：

    $$\forall\, a \in \mathbf{Z},\ \exists\, c \in C \ \text{ such that } \ a \equiv c \pmod{m}$$

  * (b) 唯一（代表不重複）：

    $$c, d \in C,\ \ c \equiv d \pmod{m} \quad \Longrightarrow \quad c = d$$

  * $C$ : 候選集合 (The candidate set) $[C \subseteq \mathbf{Z}]$
  * $a$ : 任意整數 (An arbitrary integer) $[a \in \mathbf{Z}]$
  * $c,\ d$ : $C$ 的元素 (Elements of $C$) $[c, d \in C]$
  * $m$ : 模數 (The modulus) $[m \in \mathbf{P}]$

+++

## 證明:

### (a) proof that a complete residue system is exactly a bijection onto the residues

**唯一 $\Longleftrightarrow$ $\rho$ 單射**：兩個元素同餘，正是它們的餘數相同：

$$\begin{gather*}
c \equiv d \pmod{m} &\overset{\text{已知 1(a)}}{\Longleftrightarrow}& \rho(c) = \rho(d) \\
\left[\rho(c) = \rho(d) \Rightarrow c = d\right] &\overset{\text{定義 1(b)}}{\Longleftrightarrow}& C \ \text{滿足唯一性}
\end{gather*}$$

**存在 $\Longleftrightarrow$ $\rho$ 滿射**：每個 $r \in \left\{0, \dots, m-1\right\}$ 都是某個整數（例如 $r$ 自己）的餘數，
所以「每個整數都有同餘的代表」等價於「每個餘數都被某個 $c$ 打到」：

$$\begin{gather*}
a \equiv c \pmod{m} &\overset{\text{已知 1(a)}}{\Longleftrightarrow}& a \bmod m = \rho(c) \\
r &\overset{\text{已知 1(b)}}{=}& r \bmod m \qquad \text{for every } 0 \le r < m \\
\left[\forall r,\ \exists c:\ \rho(c) = r\right] &\overset{\text{定義 1(a)}}{\Longleftrightarrow}& C \ \text{滿足存在性}
\end{gather*}$$

兩者合起來：$C$ 是完全剩餘系 $\Longleftrightarrow$ $\rho$ 是雙射。

### (b) proof that a complete residue system has exactly m elements

$\rho$ 是 $C$ 到 $m$ 元集合 $\left\{0, \dots, m-1\right\}$ 的雙射：

$$\begin{gather*}
\left|C\right| &\overset{\text{證明 (a)}}{=}& \left|\left\{0, 1, \dots, m-1\right\}\right| \\
&=& m
\end{gather*}$$

### (c) proof that m pairwise incongruent integers form a complete residue system

設 $\left|C\right| = m$ 且 $C$ 中元素兩兩不同餘。則 $\rho$ 單射，而兩邊都是 $m$ 個元素，由鴿籠原理 $\rho$ 雙射：

$$\begin{gather*}
\text{兩兩不同餘} &\overset{\text{證明 (a)}}{\Longrightarrow}& \rho \ \text{單射} \\
\rho \ \text{單射},\ \left|C\right| = m &\overset{\text{已知 2}}{\Longrightarrow}& \rho \ \text{雙射} \\
\rho \ \text{雙射} &\overset{\text{證明 (a)}}{\Longrightarrow}& C \ \text{為完全剩餘系}
\end{gather*}$$

* 註：這個判別法很省事 —— 只要**數個數**並檢查**不撞號**，不必逐一確認每個整數都有代表。

### (d) proof that the least non-negative residues form a complete residue system

$C = \left\{0, \dots, m-1\right\}$ 上的 $\rho$ 是恆等映射（每個元素都是自己的餘數），當然是雙射：

$$\begin{gather*}
\rho(r) &\overset{\text{已知 1(b)}}{=}& r \qquad \text{for all } 0 \le r < m \\
\rho \ \text{為恆等映射（雙射）} &\overset{\text{證明 (a)}}{\Longrightarrow}& \left\{0, \dots, m-1\right\} \ \text{為完全剩餘系}
\end{gather*}$$

### (e) verify the three examples modulo seven

三個集合都有 $7$ 個元素，由 (c) 只需檢查餘數兩兩不同。逐一取模 $7$：

$$\begin{gather*}
\left\{0, 1, 2, 3, 4, 5, 6\right\} \bmod 7 &\overset{\text{已知 1(b)}}{=}& \left\{0, 1, 2, 3, 4, 5, 6\right\} \\
\left\{-3, -2, -1, 0, 1, 2, 3\right\} \bmod 7 &=& \left\{4, 5, 6, 0, 1, 2, 3\right\} \\
\left\{-15, -10, -5, 1, 3, 5, 7\right\} \bmod 7 &=& \left\{6, 4, 2, 1, 3, 5, 0\right\}
\end{gather*}$$

（例如 $-15 = \left(-3\right) \times 7 + 6$、$-10 = \left(-2\right) \times 7 + 4$、$-5 = \left(-1\right) \times 7 + 2$。）
三組餘數都恰好是 $0$ 到 $6$ 各一次，兩兩不同，由 (c) 三者都是模 $7$ 的完全剩餘系，與投影片一致。

+++

## 意義與密碼學關聯 (Interpretation and Relevance to Cryptography)

### 同一個 $\mathbf{Z}_m$，不同的代表元

三個例子是**同一個** $\mathbf{Z}_7$ 的三種寫法。實作上兩種最常見：

| 代表元選法 | 集合 | 用途 |
|---|---|---|
| 最小非負 | $\left\{0, \dots, m-1\right\}$ | 一般模運算、儲存 |
| 對稱（絕對值最小） | $\left\{-\left\lfloor m/2 \right\rfloor, \dots, \left\lfloor m/2 \right\rfloor\right\}$ | 格密碼 |

後量子標準 **Kyber / ML-KEM** 在解密時要判斷一個係數「接近 $0$ 還是接近 $q/2$」，
這時必須用**對稱**代表元（第二個例子的推廣）才能直接比較大小。
選錯代表元系統，解密就會失敗 —— 這是完全剩餘系在實作裡的真實後果。

### 判別法的用途

[尤拉函數的乘法性](Euler_Phi_Multiplicativity.md) 要證明某一行 $\left\{j, n + j, \dots, (m-1)n + j\right\}$ 是模 $m$ 的完全剩餘系，
用的正是 (c)：它有 $m$ 個元素，且（因 $m \perp n$）兩兩不同餘。

### 程式思維

```python
def is_crs(C, m):
    """證明 (a)：取餘數是到 {0,...,m-1} 的雙射。"""
    return sorted(c % m for c in C) == list(range(m))

assert is_crs(range(7), 7)
assert is_crs([-3, -2, -1, 0, 1, 2, 3], 7)
assert is_crs([-15, -10, -5, 1, 3, 5, 7], 7)
assert not is_crs([0, 1, 2, 3, 4, 5, 7], 7)      # 0 與 7 同餘
```
