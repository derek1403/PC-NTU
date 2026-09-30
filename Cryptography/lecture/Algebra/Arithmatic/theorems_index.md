# 定理索引表 (Theorems Index)

本頁是 **Cryptography 這本筆記自己的**定理索引，只收錄 `lecture/Algebra/Arithmatic/` 底下
**已經逐步證明過**的結論。

**用途**：撰寫新的推導時，凡是**本庫已經證明過**的定理，一律用**帶超連結的【已知】卡片**直接引用，
**不得重證**（見推導風格規範 `PC-NTU/.claude/skills/derivation-style-review/SKILL.md` §10「引用免證」）。
寫新推導前**先查本表**，不要重讀整章；證出新的可引用結論後，**回頭補一列**。

**單一職責原則**：本表**只收錄本章內部已證的定理**。Abstract_Algebra 章的定理（群、拉格朗日、費馬小定理、尤拉定理、
環論版中國剩餘定理…）由 [該章的索引](../Abstract_Algebra/theorems_index.md) 維護；本章的檔案只在【已知】卡片內以超連結引用。

引用卡片寫法：

```markdown
* **【已知 1】 [貝祖等式 (Bézout's identity)](連結)：** 已於本章 ⟨出處⟩ 完整證明，此處直接引用不再重證

  $$\gcd(a, b) = \min\left\{ax + by \ \middle|\ ax + by > 0\right\}$$

  * $a,\ b$ : 不全為零的整數 (Integers, not both zero) $[a, b \in \mathbf{Z}]$
```

**連結慣例**：

* 有 proof 小節 anchor 的，連到 anchor（anchor 取自標題中的**英文**；改英文標題＝改 anchor，本表要同步更新）。
* 連結一律走 `_build/html` 的線上網址
  （`https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/…`），
  這樣在檔案內、GitHub 上、Jupyter Book 內都點得開。
* 注意資料夾名稱是 `Arithmatic`（沿用既有拼法），不是 `Arithmetic`。

**規模**：29 個檔案（不含本頁與章首頁）、142 張【已知／假設／定義／推導】卡片、131 個證明小節。

---

## Division (除法與取模)

| 名稱 (Name) | LaTeX Statement | 連結 (Link) | 前提／適用條件 |
|---|---|---|---|
| 地板函數的夾擠不等式 (Sandwich inequality for the floor) | `\lfloor x \rfloor \le x < \lfloor x \rfloor + 1` | [Floor_and_Ceiling #a-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/Division/Floor_and_Ceiling.html#a-proof-of-existence-and-the-sandwich-inequality) | 任意實數；天花板對稱 |
| 地板函數的刻畫 (Characterization of the floor) | `n \le x < n+1 \Longrightarrow n = \lfloor x \rfloor` | [Floor_and_Ceiling #b-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/Division/Floor_and_Ceiling.html#b-proof-of-the-characterization-of-the-floor) | $n$ 為整數；**負數往 $-\infty$ 取整** |
| 餘數的範圍 (Range of the remainder) | `0 \le n \bmod m < m` | [Modular_Function #a-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/Division/Modular_Function.html#a-proof-that-the-remainder-lies-between-zero-and-the-modulus) | **$m$ 必須為正**；$n$ 可為負 |
| **除法原理 (Division algorithm)** | `n = \lfloor n/m \rfloor m + (n \bmod m)，商與餘數唯一` | [Modular_Function #b-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/Division/Modular_Function.html#b-proof-of-the-division-algorithm-with-uniqueness) | $m \in \mathbf{P}$；Abstract_Algebra 章當外部已知引用，本章補證 |
| 整除等價餘數為零 (Divisibility iff zero remainder) | `m \mid n \Longleftrightarrow n \bmod m = 0` | [Modular_Function #c-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/Division/Modular_Function.html#c-proof-that-divisibility-forces-a-zero-remainder) | (⇐) 見同檔 (d) |
| $\mathbf{Z}_6$ 不是體 (The residues modulo six do not form a field) | `2 \otimes b \neq 1,\quad 2 \otimes 3 = 0` | [Cayley_Tables_of_Z6 #b](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/Division/Cayley_Tables_of_Z6.html#b-disprove-that-the-residues-modulo-six-form-a-field) | 具體實例；一般定理見 Abstract_Algebra |

## GCD (最大公因數)

| 名稱 (Name) | LaTeX Statement | 連結 (Link) | 前提／適用條件 |
|---|---|---|---|
| 整除線性組合 (A common divisor divides every combination) | `d \mid a,\ d \mid b \Longrightarrow d \mid ax + by` | [Divisibility_Basics #a-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/GCD/Divisibility_Basics.html#a-proof-that-a-common-divisor-divides-every-linear-combination) | 任意整數；**全章引用最多的一條** |
| 整除遞移 (Transitivity of divisibility) | `d \mid a,\ a \mid b \Longrightarrow d \mid b` | [Divisibility_Basics #b-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/GCD/Divisibility_Basics.html#b-proof-that-divisibility-is-transitive) | 任意整數 |
| 因數的大小界 (Size bound for divisors) | `d \mid a,\ a \neq 0 \Longrightarrow \lvert d \rvert \le \lvert a \rvert` | [Divisibility_Basics #e-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/GCD/Divisibility_Basics.html#e-proof-that-a-divisor-of-a-nonzero-integer-is-no-larger-in-absolute-value) | **$a \neq 0$**（$0$ 被所有非零數整除） |
| gcd 存在且為正 (Existence and positivity of the gcd) | `\gcd(a, b) \in \mathbf{P}` | [Greatest_Common_Divisor #a-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/GCD/Greatest_Common_Divisor.html#a-proof-that-the-greatest-common-divisor-exists-and-is-positive) | **$a, b$ 不全為零** |
| gcd 的基本命題 (Basic propositions of the gcd) | `\gcd(a,0) = \lvert a \rvert,\ \gcd(a,b) = \gcd(\lvert a \rvert, \lvert b \rvert) = \gcd(b,a)` | [Greatest_Common_Divisor #d-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/GCD/Greatest_Common_Divisor.html#d-proof-that-the-gcd-ignores-signs-and-order) | 不全為零；$\gcd(a,a) = a$ 見同檔 (c) |
| **GCD 平移不變性 (Shift invariance)** | `\gcd(a, b) = \gcd(a + kb, b)` | [GCD_Shift_Invariance #c-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/GCD/GCD_Shift_Invariance.html#c-proof-of-the-shift-invariance-theorem) | 不全為零；任意 $k \in \mathbf{Z}$ |
| 歐幾里得遞迴 (Euclidean recursion) | `\gcd(a, b) = \gcd(b, a \bmod b)` | [GCD_Shift_Invariance #d-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/GCD/GCD_Shift_Invariance.html#d-proof-of-the-corollary-using-the-remainder) | **$b > 0$** |
| **歐幾里得演算法正確 (Correctness of the Euclidean algorithm)** | `\gcd(a_i, b_i) = \gcd(a, b)，終止時輸出 \gcd` | [Euclidean_Algorithm #d-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/GCD/Euclidean_Algorithm.html#d-proof-that-the-output-is-the-gcd) | **輸入需先轉非負**（投影片漏條件）；$O(\log b)$ 輪 |
| 擴展歐幾里得不變量 (Invariant of the extended algorithm) | `r_k = a x_k + b y_k` | [Extended_Euclidean_Algorithm #b-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/GCD/Extended_Euclidean_Algorithm.html#b-proof-of-the-inductive-step-for-the-next-remainder) | $b > 0$；對任意商 $q$ 都保持 |
| **貝祖係數存在 (Existence of Bézout coefficients)** | `\exists\, x, y:\ ax + by = \gcd(a, b)` | [Extended_Euclidean_Algorithm #c-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/GCD/Extended_Euclidean_Algorithm.html#c-proof-of-the-existence-of-bezout-coefficients) | 不全為零；可由演算法算出 |
| 矩陣版等價 (Matrix version equivalence) | `[[0,1],[1,-q]] \cdot [\text{兩列}] = [\text{下兩列}]` | [Extended_Euclidean_Algorithm #e-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/GCD/Extended_Euclidean_Algorithm.html#e-proof-that-the-matrix-version-is-the-same-recursion) | 投影片 p.18 |
| **貝祖等式：gcd 是最小正組合 (Bézout: the gcd is the least positive combination)** | `\gcd(a, b) = \min\{ax + by > 0\}` | [Bezout_Identity #a-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/GCD/Bezout_Identity.html#a-proof-that-the-gcd-is-the-smallest-positive-combination) | 不全為零；與 Abstract_Algebra 的 $\langle a,b \rangle = \langle \gcd \rangle$ 一致 |
| 公因數整除 gcd (Every common divisor divides the gcd) | `c \mid a,\ c \mid b \Longrightarrow c \mid \gcd(a, b)` | [Bezout_Identity #b-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/GCD/Bezout_Identity.html#b-proof-that-every-common-divisor-divides-the-gcd) | 投影片未列，本章補 |
| **互質的組合刻畫 (Coprime iff a combination equals one)** | `\gcd(a, b) = 1 \Longleftrightarrow \exists\, x, y:\ ax + by = 1` | [Bezout_Identity #d-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/GCD/Bezout_Identity.html#d-proof-that-a-combination-equal-to-one-forces-coprimality) | (⇒) 見同檔 (c)；**證明互質的標準手法** |
| Stein 三性質 (Stein's three properties) | `\gcd(a,b) = 2\gcd(\tfrac a2, \tfrac b2) = \gcd(\tfrac a2, b) = \gcd(\tfrac{a-b}{2}, b)` | [Stein_Binary_GCD #c-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/GCD/Stein_Binary_GCD.html#c-proof-of-the-both-odd-property) | 依序為「皆偶」「偶奇」「皆奇」；投影片只證第三條 |

## Factorization (質因數分解)

| 名稱 (Name) | LaTeX Statement | 連結 (Link) | 前提／適用條件 |
|---|---|---|---|
| **廣義歐幾里得引理 (Generalized Euclid lemma)** | `a \mid bc,\ a \perp b \Longrightarrow a \mid c` | [Relatively_Prime #a-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/Factorization/Relatively_Prime.html#a-proof-of-the-generalized-euclid-lemma) | **互質不可省**（$6 \mid 4 \times 9$） |
| 互質對乘法封閉 (Coprimality is closed under products) | `a \perp m,\ b \perp m \Longrightarrow ab \perp m` | [Relatively_Prime #b-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/Factorization/Relatively_Prime.html#b-proof-that-coprimality-to-a-modulus-is-closed-under-products) | 投影片未列，本章補；CRT 與 $\varphi$ 要用 |
| 互質因數相乘仍整除 (Coprime divisors multiply) | `m_1 \mid x,\ m_2 \mid x,\ m_1 \perp m_2 \Longrightarrow m_1 m_2 \mid x` | [Relatively_Prime #c-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/Factorization/Relatively_Prime.html#c-proof-that-coprime-divisors-multiply) | 投影片 p.39 直接使用未證，本章補；**CRT 唯一性的核心** |
| 質數與不被它整除者互質 (A prime is coprime to what it does not divide) | `p \nmid a \Longrightarrow \gcd(p, a) = 1` | [Euclid_Lemma #a-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/Factorization/Euclid_Lemma.html#a-proof-that-a-prime-is-coprime-to-every-integer-it-does-not-divide) | $p$ 為質數 |
| **歐幾里得引理 (Euclid's lemma)** | `p \mid ab \Longrightarrow p \mid a \ \text{or}\ p \mid b` | [Euclid_Lemma #b-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/Factorization/Euclid_Lemma.html#b-proof-of-euclids-lemma-for-two-factors) | **$p$ 必須是質數**；Abstract_Algebra 章當外部已知引用，本章補證 |
| 歐幾里得引理（$k$ 個因子） (Euclid's lemma for k factors) | `p \mid a_1 \cdots a_k \Longrightarrow p \mid a_i` | [Euclid_Lemma #d-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/Factorization/Euclid_Lemma.html#d-proof-of-the-inductive-step-for-k-factors) | 歸納法；基底見同檔 (c) |
| **算術基本定理：存在性 (FTA, existence)** | `a \ge 2 \Longrightarrow a = p_1 \cdots p_r` | [Fundamental_Theorem_of_Arithmetic #b-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/Factorization/Fundamental_Theorem_of_Arithmetic.html#b-proof-of-the-inductive-step-of-existence) | 強歸納法；非建設性 |
| **算術基本定理：唯一性 (FTA, uniqueness)** | `p_1 \cdots p_r = q_1 \cdots q_s \Longrightarrow r = s,\ p_i = q_i` | [Fundamental_Theorem_of_Arithmetic #d-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/Factorization/Fundamental_Theorem_of_Arithmetic.html#d-proof-of-the-inductive-step-of-uniqueness) | 排序後逐項相同；**$\mathbf{Z}[\sqrt{-5}]$ 不成立**（同檔 (e)） |
| 因數的指數刻畫 (Exponent characterization of divisors) | `d \mid n \Longleftrightarrow c_i \le e_i` | [Least_Common_Multiple #a-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/Factorization/Least_Common_Multiple.html#a-proof-of-the-exponent-characterization-of-divisors) | 正整數；投影片未列，本章補 |
| gcd 與 lcm 的指數公式 (Exponent formulas) | `\gcd = \prod p_i^{\min(e_i,f_i)},\ \mathrm{lcm} = \prod p_i^{\max(e_i,f_i)}` | [Least_Common_Multiple #c-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/Factorization/Least_Common_Multiple.html#c-proof-of-the-exponent-formula-for-the-lcm) | gcd 版見同檔 (b)；投影片只陳述，本章補證 |
| **$ab = \gcd \times \mathrm{lcm}$** | `ab = \gcd(a, b)\,\mathrm{lcm}(a, b)` | [Least_Common_Multiple #d-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/Factorization/Least_Common_Multiple.html#d-proof-of-the-product-formula) | $a, b \in \mathbf{P}$；**算 lcm 不必分解** |

## Congruence (同餘)

| 名稱 (Name) | LaTeX Statement | 連結 (Link) | 前提／適用條件 |
|---|---|---|---|
| **同餘的整除刻畫 (Congruence as divisibility)** | `a \bmod m = b \bmod m \Longleftrightarrow m \mid (a - b)` | [Congruence_Relation #b-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/Congruence/Congruence_Relation.html#b-proof-that-a-difference-divisible-by-the-modulus-gives-equal-remainders) | 使兩章的同餘定義一致；(⇒) 見同檔 (a) |
| 與自己的餘數同餘 (Congruent to its own remainder) | `a \equiv (a \bmod m) \pmod m` | [Congruence_Relation #c-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/Congruence/Congruence_Relation.html#c-proof-that-every-integer-is-congruent-to-its-remainder) | 「取模可以隨時做」 |
| 同餘保持加、乘、冪 (Congruence respects +, ×, powers) | `a \equiv b \Longrightarrow a+c \equiv b+c,\ ac \equiv bc,\ a^d \equiv b^d` | [Congruence_Properties #d-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/Congruence/Congruence_Properties.html#d-proof-that-congruence-is-preserved-by-powers) | 加法、乘法見同檔 (b)(c) |
| 同餘式相乘 (Congruences multiply) | `a \equiv b,\ c \equiv e \Longrightarrow ac \equiv be` | [Congruence_Properties #e-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/Congruence/Congruence_Properties.html#e-proof-that-congruences-can-be-multiplied-together) | 投影片未列，本章補 |
| 帶 gcd 的消去律 (Cancellation with the gcd) | `ab \equiv ac \pmod m \Longrightarrow b \equiv c \pmod{m/\gcd(a,m)}` | [Congruence_Properties #f-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/Congruence/Congruence_Properties.html#f-proof-of-cancellation-with-the-gcd) | **模數要跟著除**；投影片記號 $d$ 與冪次撞名，本章改記 $g$ |
| **互質消去律 (Cancellation of a coprime factor)** | `a \perp m,\ ab \equiv ac \Longrightarrow b \equiv c \pmod m` | [Congruence_Properties #g-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/Congruence/Congruence_Properties.html#g-proof-of-cancellation-for-a-coprime-factor) | **互質不可省** |
| **模反元素存在判準 (Criterion for a modular inverse)** | `a^{-1} \bmod m \ \text{存在} \Longleftrightarrow a \perp m` | [Modular_Inverse #b-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/Congruence/Modular_Inverse.html#b-proof-that-coprimality-gives-an-inverse) | (⇒) 見同檔 (a)；Abstract_Algebra 章當外部已知引用，本章補證 |
| 一次同餘式的解 (Solving a linear congruence) | `ax \equiv b \Longleftrightarrow x \equiv a^{-1} b \pmod m` | [Modular_Inverse #c-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/Congruence/Modular_Inverse.html#c-proof-that-the-linear-congruence-is-solved-by-the-inverse) | $a \perp m$ |
| 反元素演算法正確 (Correctness of the inverse algorithm) | `r_{\text{final}} = 1 \Longrightarrow a\,(x_{\text{final}} \bmod m) \equiv 1` | [Modular_Inverse #d-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/Congruence/Modular_Inverse.html#d-proof-that-the-matrix-algorithm-computes-the-inverse) | **投影片漏了最後取模**，原輸出可能為負（同檔 (f)） |

## CRT (中國剩餘定理)

| 名稱 (Name) | LaTeX Statement | 連結 (Link) | 前提／適用條件 |
|---|---|---|---|
| 互質模數給出同構 (Coprime moduli give an isomorphism) | `\gcd(m_1, m_2) = 1 \Longrightarrow \mathbf{Z}_{m_1 m_2} \cong \mathbf{Z}_{m_1} \times \mathbf{Z}_{m_2}` | [CRT_Coordinate_Representation #c-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/CRT/CRT_Coordinate_Representation.html#c-proof-that-coprime-moduli-give-an-isomorphism) | 引用 Abstract_Algebra 的環論 CRT |
| **不互質則不同構 (Non-coprime moduli give no isomorphism)** | `\gcd(m_1, m_2) > 1 \Longrightarrow \mathbf{Z}_{m_1 m_2} \not\cong \mathbf{Z}_{m_1} \times \mathbf{Z}_{m_2}` | [CRT_Coordinate_Representation #d-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/CRT/CRT_Coordinate_Representation.html#d-proof-that-non-coprime-moduli-give-no-isomorphism) | **任何**映射都不行；投影片只陳述，本章補證 |
| **兩個模數的 CRT：構造 (Two-moduli CRT, construction)** | `x = a_1 + m_1\,[m_1^{-1}(a_2 - a_1) \bmod m_2]` | [Two_Moduli_CRT #a-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/CRT/Two_Moduli_CRT.html#a-proof-that-the-constructed-number-solves-both-congruences) | $m_1 \perp m_2$；**Garner 形式，RSA-CRT 的實作公式** |
| 兩個模數的 CRT：唯一性 (Two-moduli CRT, uniqueness) | `x_1 \equiv x_2 \pmod{m_1 m_2}` | [Two_Moduli_CRT #b-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/CRT/Two_Moduli_CRT.html#b-proof-that-any-two-solutions-agree-modulo-the-product) | 解集恰為一個同餘類（同檔 (c)） |
| **中國剩餘定理：高斯公式 (CRT, Gauss's formula)** | `x = \sum a_i M_i y_i,\ \ y_i \equiv M_i^{-1} \pmod{m_i}` | [Chinese_Remainder_Theorem #a-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/CRT/Chinese_Remainder_Theorem.html#a-proof-that-gausss-formula-gives-a-solution) | **兩兩互質**（全體 gcd 為 $1$ 不夠） |
| 中國剩餘定理：唯一性 (CRT, uniqueness modulo M) | `x \equiv x' \pmod{M}` | [Chinese_Remainder_Theorem #b-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/CRT/Chinese_Remainder_Theorem.html#b-proof-that-the-solution-is-unique-modulo-the-product) | 只確定到模 $M$（韓信點兵） |
| 中國剩餘演算法正確 (Correctness of the CRA) | `\mathrm{CRA}(\mathbf{a}, \mathbf{m}, r) \equiv a_i \pmod{m_i}` | [Chinese_Remainder_Algorithm #b-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/CRT/Chinese_Remainder_Algorithm.html#b-proof-of-the-inductive-step-by-merging-the-last-two-congruences) | 兩兩互質；投影片的 Proof 1 |

## Fermat and Euler (費馬與尤拉)

| 名稱 (Name) | LaTeX Statement | 連結 (Link) | 前提／適用條件 |
|---|---|---|---|
| 費馬小定理的系理 (Corollary of Fermat's little theorem) | `a^p \equiv a \pmod p` | [Fermat_Little_Theorem #b-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/Fermat_Euler/Fermat_Little_Theorem.html#b-proof-of-the-corollary-for-every-integer) | $p$ 質數、**任意** $a$；定理本身見 Abstract_Algebra |
| 以費馬求反元素 (Inverse by Fermat) | `a^{-1} \equiv a^{p-2} \pmod p` | [Fermat_Little_Theorem #d-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/Fermat_Euler/Fermat_Little_Theorem.html#d-proof-that-the-inverse-is-a-power) | $p \nmid a$；**常數時間實作** |
| 偽質數 341 (The pseudoprime 341) | `2^{341} \equiv 2 \pmod{341}` | [Fermat_Little_Theorem #c](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/Fermat_Euler/Fermat_Little_Theorem.html#c-verify-that-three-hundred-forty-one-is-a-base-two-pseudoprime) | 費馬小定理的逆命題不成立 |
| **561 是 Carmichael 數 (561 is a Carmichael number)** | `a^{561} \equiv a \pmod{561}\ \forall a` | [Carmichael_Numbers #c-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/Fermat_Euler/Carmichael_Numbers.html#c-proof-of-the-congruence-modulo-five-hundred-sixty-one) | 「最小」僅程式驗證（同檔 (d)） |
| 完全剩餘系判別法 (Criterion for a complete residue system) | `\lvert C \rvert = m,\ \text{兩兩不同餘} \Longrightarrow C\ \text{完全剩餘系}` | [Complete_Residue_System #c-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/Fermat_Euler/Complete_Residue_System.html#c-proof-that-m-pairwise-incongruent-integers-form-a-complete-residue-system) | 等價刻畫（取餘數為雙射）見同檔 (a) |
| $\varphi$ 的質數判準 (Prime iff totient is one less) | `p\ \text{質數} \Longleftrightarrow \varphi(p) = p - 1` | [Euler_Phi_Function #c-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/Fermat_Euler/Euler_Phi_Function.html#c-proof-that-a-non-prime-has-a-smaller-totient) | $p > 0$；(⇒) 見同檔 (b) |
| **質數冪的 $\varphi$ (Totient of a prime power)** | `\varphi(p^k) = p^{k-1}(p - 1)` | [Euler_Phi_Function #d-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/Fermat_Euler/Euler_Phi_Function.html#d-proof-of-the-formula-for-a-prime-power) | $p$ 質數、$k \ge 1$ |
| 與乘積互質的拆分 (Coprime to a product) | `a \perp mn \Longleftrightarrow a \perp m,\ a \perp n` | [Euler_Phi_Multiplicativity #a-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/Fermat_Euler/Euler_Phi_Multiplicativity.html#a-proof-that-coprimality-to-a-product-splits-into-the-two-factors) | 任意 $m, n$ |
| **$\varphi$ 的乘法性 (Multiplicativity of the totient)** | `\varphi(mn) = \varphi(m)\varphi(n)` | [Euler_Phi_Multiplicativity #e-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/Fermat_Euler/Euler_Phi_Multiplicativity.html#e-proof-of-multiplicativity) | **$m \perp n$ 不可省**（$\varphi(4) \neq \varphi(2)^2$） |
| **$\varphi$ 的乘積公式 (Product formula for the totient)** | `\varphi(n) = \prod p_i^{e_i - 1}(p_i - 1)` | [Euler_Phi_Multiplicativity #f-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/Fermat_Euler/Euler_Phi_Multiplicativity.html#f-proof-of-the-product-formula) | 需要分解 $n$ —— **RSA 的陷門** |
| 化簡剩餘系的縮放 (Scaling a reduced residue system) | `a \perp n \Longrightarrow aR\ \text{仍為化簡剩餘系}` | [Reduced_Residue_System #b-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/Fermat_Euler/Reduced_Residue_System.html#b-proof-that-scaling-by-a-coprime-integer-preserves-a-reduced-residue-system) | 投影片的尤拉定理證明路線 |
| **指數模 $\varphi(n)$ 化簡 (Exponent reduction)** | `a^k \equiv a^{k \bmod \varphi(n)} \pmod n` | [Euler_Theorem #b-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/Fermat_Euler/Euler_Theorem.html#b-proof-that-exponents-can-be-reduced-modulo-phi-of-n) | **$a \perp n$ 不可省**；RSA 解密的依據；尤拉定理本身見 Abstract_Algebra |
| 費馬最後定理的化約 (Reduction of FLT) | `n\ \text{有反例} \Longrightarrow e \mid n\ \text{有反例}` | [Fermat_Last_Theorem #b-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Arithmatic/Fermat_Euler/Fermat_Last_Theorem.html#b-proof-that-a-counterexample-descends-to-every-divisor) | 只需證 $n = 4$ 與奇質數（同檔 (c)） |

---

## 未證明但已陳述的結論 (Stated Without Proof)

以下結論在本章中被**明確標示為未證明**，引用時請一併標示出處與「本章未證」：

| 名稱 | 出處 | 為什麼沒證 |
|---|---|---|
| **費馬最後定理** (Fermat's last theorem) | [費馬最後定理](Fermat_Euler/Fermat_Last_Theorem.md#a-statement-of-fermats-last-theorem-without-proof) | Wiles–Taylor（1995），需橢圓曲線的模性定理 |
| $561$ 是**最小的** Carmichael 數 | [Carmichael 數](Fermat_Euler/Carmichael_Numbers.md#d-statement-of-minimality-verified-by-computation) | 僅以程式窮舉 $n < 2000$ 驗證，無手寫證明 |
| Korselt 判準 | [Carmichael 數](Fermat_Euler/Carmichael_Numbers.md) 文末 | 「只若」方向需原根存在性 |
| Carmichael 數有無窮多個 | [Carmichael 數](Fermat_Euler/Carmichael_Numbers.md) 文末 | Alford–Granville–Pomerance（1994） |
| 歐幾里得演算法的對數步數、Lamé 定理 | [歐幾里得演算法](GCD/Euclidean_Algorithm.md) 文末 | 只給「每兩輪減半」的論證草稿，未正式證明 |
