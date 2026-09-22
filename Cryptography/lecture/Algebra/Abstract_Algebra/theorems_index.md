# 定理索引表 (Theorems Index)

本頁是 **Cryptography 這本筆記自己的**定理索引，只收錄 `lecture/Algebra/Abstract_Algebra/` 底下
**已經逐步證明過**的結論。

**用途**：撰寫新的推導時，凡是**本庫已經證明過**的定理，一律用**帶超連結的【已知】卡片**直接引用，
**不得重證**（見推導風格規範 `PC-NTU/.claude/skills/derivation-style-review/SKILL.md` §10「引用免證」）。
寫新推導前**先查本表**，不要重讀整章；證出新的可引用結論後，**回頭補一列**。

**單一職責原則**：本表**只收錄本章內部已證的定理**。外部知識庫（如
[Theory_Playground](https://derek1403.github.io/Theory_Playground/_build/html/intro.html)）
的推導由該庫自行維護索引，本章的檔案只在【已知】卡片內以超連結引用，
這樣外部改動時本表不必跟著改。

引用卡片寫法：

```markdown
* **【已知 1】 [拉格朗日定理 (Lagrange's theorem)](連結)：** 此定理已於本章 ⟨出處⟩ 完整證明，此處直接引用不再重證

  $$\left|H\right| \ \Big|\ \left|G\right|$$

  * $G$ : 有限群 (A finite group) $[\text{集合}]$
  * $H$ : $G$ 的子群 (A subgroup of $G$) $[H \le G]$
```

**連結慣例**：

* 有 proof 小節 anchor 的，連到 anchor（anchor 取自標題中的**英文**；改英文標題＝改 anchor，本表要同步更新）。
* 只有頁面層級 anchor 的，連到 `.html` 頁面本身。
* 連結一律走 `_build/html` 的線上網址
  （`https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/…`），
  這樣在檔案內、GitHub 上、Jupyter Book 內都點得開。
* 本表以下的連結全部以 `⟨BASE⟩` 代表該網址前綴，實際連結已展開。

**規模**：49 個檔案、295 張【已知／假設／定義／推導】卡片、169 個證明小節。

---

## Group (群)

| 名稱 (Name) | LaTeX Statement | 連結 (Link) | 前提／適用條件 |
|---|---|---|---|
| 單位元素唯一 (Uniqueness of the identity) | `e_1 = e_2` | [Uniqueness_of_Identity #a-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Group/Uniqueness_of_Identity.html#a-proof-uniqueness-of-the-identity-element) | 只需單位元素公理；對么半群、環的乘法同樣適用 |
| 反元素唯一 (Uniqueness of the inverse) | `b = c \ \text{ for any two inverses of } a` | [Uniqueness_of_Inverse #a-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Group/Uniqueness_of_Inverse.html#a-proof-uniqueness-of-the-inverse-element) | **需要結合律**；證完後記號 $a^{-1}$ 才合法 |
| 反元素的反元素 (Inverse of an inverse) | `\left(a^{-1}\right)^{-1} = a` | [Inverse_of_an_Inverse #a-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Group/Inverse_of_an_Inverse.html#a-proof-that-taking-the-inverse-twice-returns-the-original-element) | 任意群 |
| 乘積的反元素 (Inverse of a product) | `\left(a * b\right)^{-1} = b^{-1} * a^{-1}` | [Inverse_of_a_Product #a-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Group/Inverse_of_a_Product.html#a-proof-of-the-inverse-of-a-product) | 任意群；**順序必須顛倒**，交換群才可對調 |
| 左／右消去律 (Cancellation laws) | `a * b = a * c \Longrightarrow b = c` | [Unique_Solution_and_Cancellation_Law #a-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Group/Unique_Solution_and_Cancellation_Law.html#a-proof-of-the-left-cancellation-law) | 任意群；靠 $a^{-1}$ 存在（與環的無零因子不同） |
| 一次方程唯一解 (Unique solution) | `a * x = b \Longrightarrow x = a^{-1} * b` | [Unique_Solution_and_Cancellation_Law #c-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Group/Unique_Solution_and_Cancellation_Law.html#c-proof-existence-and-uniqueness-of-the-solution-to-the-left-equation) | 任意群；$y * a = b$ 的解是 $b * a^{-1}$，**兩者不同** |
| 有限集上單射等價滿射 (Injective iff surjective on a finite set) | `f \ \text{單射} \Longleftrightarrow f \ \text{滿射}` | [Permutation #a-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Group/Permutation.html#a-proof-the-equivalence-of-injectivity-and-surjectivity-on-a-finite-set) | **僅限有限集**；驗證 S-box 可逆時只需檢查不撞號 |
| 對稱群是群 (The symmetric group is a group) | `\left(S_n, \circ\right) \ \text{為群}` | [Symmetric_Group #a-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Group/Symmetric_Group.html#a-proof-that-the-symmetric-group-is-a-group) | 任意 $n$；$n \ge 3$ 時非交換 |
| 對稱群的階 (Order of the symmetric group) | `\left\|S_n\right\| = n!` | [Symmetric_Group #b-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Group/Symmetric_Group.html#b-proof-of-the-order-of-the-symmetric-group) | $\left\|S_{256}\right\| = 256! \approx 10^{507}$（AES S-box 空間） |
| 循環群必為阿貝爾群 (Cyclic implies abelian) | `G \ \text{循環} \Longrightarrow G \ \text{阿貝爾}` | [Cyclic_Group #f-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Group/Cyclic_Group.html#f-proof-that-every-cyclic-group-is-abelian) | **逆命題不成立**（$\mathbf{Z}_8^*$ 為反例） |
| 可逆剩餘類的階 (Order of the units modulo n) | `\left\|\mathbf{Z}_n^*\right\| = \varphi(n)` | [Group_Order #c-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Group/Group_Order.html#c-proof-of-the-order-of-the-units-modulo-a-general-number) | 任意 $n \ge 2$；$p$ 為質數時等於 $p-1$ |
| 一般線性群的階 (Order of the general linear group) | `\left\|GL_n(\mathbf{Z}_q)\right\| = \prod_{k=0}^{n-1}\left(q^n - q^k\right)` | [General_Linear_Group_Order #a-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Group/General_Linear_Group_Order.html#a-proof-of-the-order-of-the-general-linear-group-over-a-prime-field) | **$q$ 必須是質數**；$\left\|GL_8(\mathbf{Z}_2)\right\| \approx 5.35\times10^{18}$ |
| 子群判別法 (Subgroup criterion) | `H \le G \Longleftrightarrow H \neq \varnothing,\ ab \in H,\ a^{-1} \in H` | [Subgroup_Criterion #b-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Group/Subgroup_Criterion.html#b-proof-of-the-backward-direction) | **非空條件投影片漏列**，本章補上 |
| 陪集相等的充要條件 (Coset equality criterion) | `g_1H = g_2H \Longleftrightarrow g_1^{-1} * g_2 \in H` | [Coset_Equality_Criterion #b-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Group/Coset_Equality_Criterion.html#b-proof-of-the-backward-direction-for-left-cosets) | 右陪集版本是 $g_2 * g_1^{-1} \in H$，**順序相反** |
| 陪集等勢 (Cosets are equinumerous) | `\left\|gH\right\| = \left\|H\right\|` | [Coset_Partition #a-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Group/Coset_Partition.html#a-proof-that-every-coset-has-the-same-size-as-the-subgroup) | 有限無限皆成立；靠左消去律 |
| 陪集分割 (Cosets form a partition) | `\bigcup_{g} gH = G,\quad g_1H \cap g_2H = \varnothing \ \text{或相等}` | [Coset_Partition #d-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Group/Coset_Partition.html#d-proof-that-the-left-cosets-form-a-partition) | **投影片未列**，本章補以支撐拉格朗日定理與 $\left\|SL_2\right\|$ |
| **拉格朗日定理 (Lagrange's theorem)** | `\left\|H\right\| \ \Big\| \ \left\|G\right\|` | [Lagrange_Theorem #a-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Group/Lagrange_Theorem.html#a-proof-of-lagranges-theorem) | **$G$ 必須有限**；逆命題不成立（$A_4$ 無 $6$ 階子群） |
| 指標公式 (Index formula) | `\left[G:H\right] = \left\|G\right\| / \left\|H\right\|` | [Lagrange_Theorem #b-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Group/Lagrange_Theorem.html#b-proof-of-the-index-formula) | 同上 |
| 循環子群的階 (Order of a cyclic subgroup) | `\left\|\langle g \rangle\right\| = o(g)` | [Order_of_Element #a-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Group/Order_of_Element_and_Cyclic_Subgroup.html#a-proof-that-the-powers-of-an-element-form-a-subgroup-of-size-equal-to-the-order) | $G$ 有限（否則 $o(g)$ 可能不存在） |
| **元素的階整除群的階** (Order of an element divides the group order) | `o(g) \ \Big\| \ \left\|G\right\|` | [Order_of_Element #b-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Group/Order_of_Element_and_Cyclic_Subgroup.html#b-proof-that-the-order-of-an-element-divides-the-order-of-the-group) | $G$ 有限；**質數階群的每個非單位元素都是生成元** |
| **尤拉定理 (Euler's theorem)** | `a^{\varphi(n)} \equiv 1 \pmod{n}` | [Order_of_Element #c-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Group/Order_of_Element_and_Cyclic_Subgroup.html#c-proof-of-eulers-theorem) | **$\gcd(a,n)=1$ 不可省**；投影片未列，本章補。**RSA 解密的依據** |
| **費馬小定理 (Fermat's little theorem)** | `a^{p-1} \equiv 1 \pmod{p}` | [Order_of_Element #d-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Group/Order_of_Element_and_Cyclic_Subgroup.html#d-proof-of-fermats-little-theorem) | $p$ 質數、$p \nmid a$；投影片未列，本章補 |
| 特殊線性群的階 (Order of the special linear group) | `\left\|SL_n(\mathbf{Z}_q)\right\| = \left\|GL_n(\mathbf{Z}_q)\right\| / (q-1)` | [Special_Linear_Subgroup_Index #d-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Group/Special_Linear_Subgroup_Index.html#d-proof-of-the-order-of-the-special-linear-group) | $q$ 質數；$\left\|SL_2(\mathbf{Z}_7)\right\| = 336$ |
| 同態的基本性質 (Basic properties of a homomorphism) | `f(e_G) = e_H,\quad f(a^{-1}) = f(a)^{-1}` | [Group_Homomorphism #a-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Group/Group_Homomorphism_and_Isomorphism.html#a-proof-of-the-basic-properties-of-a-homomorphism) | 任意群同態 |

## Ring (環)

| 名稱 (Name) | LaTeX Statement | 連結 (Link) | 前提／適用條件 |
|---|---|---|---|
| 乘以零得零 (Multiplication by zero) | `a \times 0 = 0 \times a = 0` | [Ring_Basic_Propositions #a-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Ring/Ring_Basic_Propositions.html#a-proof-that-multiplication-by-zero-gives-zero) | 任意環；**唯一工具是分配律** |
| 負號提出 (Sign extraction) | `\left(-a\right)b = a\left(-b\right) = -\left(ab\right)` | [Ring_Basic_Propositions #b-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Ring/Ring_Basic_Propositions.html#b-proof-that-a-negative-factor-pulls-the-sign-out) | 任意環 |
| 減法的分配律 (Distributivity over subtraction) | `a\left(b-c\right) = ab - ac` | [Ring_Basic_Propositions #c-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Ring/Ring_Basic_Propositions.html#c-proof-of-the-distributive-law-over-subtraction) | 任意環；減法是定義出來的簡寫 |
| 乘以負一 (Multiplying by minus one) | `\left(-1\right)a = -a` | [Ring_Basic_Propositions #d-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Ring/Ring_Basic_Propositions.html#d-proof-that-multiplying-by-minus-one-negates) | **需含單位元**；$\mathbf{Z}_n$ 裡 $-1 = n-1$ |
| 零環的刻畫 (Characterization of the zero ring) | `1 = 0 \Longleftrightarrow R = \left\{0\right\}` | [Ring_Basic_Propositions #e](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Ring/Ring_Basic_Propositions.html#e-discussion-of-the-condition-that-one-differs-from-zero) | 投影片把 $1 \neq 0$ 列為命題，**實為約定**，本章改列為等價刻畫 |
| 子環判別法 (Subring criterion) | `S \le R \Longleftrightarrow S \neq \varnothing,\ a-b \in S,\ ab \in S` | [Subring #a-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Ring/Subring.html#a-proof-of-the-subring-criterion) | 「減法封閉」一條抵兩條；**本章採「子環不必含 $1$」的慣例** |
| 零因子的模數判準 (Zero divisor criterion modulo n) | `\mathbf{Z}_n \ \text{有零因子} \Longleftrightarrow n \ \text{為合數}` | [Zero_Divisor #b-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Ring/Zero_Divisor.html#b-proof-of-the-criterion-for-the-existence-of-zero-divisors-modulo-n) | $n \ge 2$；**找到 $\mathbf{Z}_n$ 的零因子等於分解 $n$** |
| 無零因子等價消去律 (No zero divisors iff cancellation) | `R \ \text{無零因子} \Longleftrightarrow \left[ab=ac,\ a \neq 0 \Rightarrow b=c\right]` | [Zero_Divisor #c-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Ring/Zero_Divisor.html#c-proof-that-the-absence-of-zero-divisors-is-equivalent-to-the-cancellation-law) | 任意環；**投影片未列**，本章補 |
| 無零因子由子環繼承 (Absence of zero divisors passes to subrings) | `S \le R,\ R \ \text{整環} \Longrightarrow S \ \text{整環}` | [Integral_Domain #a](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Ring/Integral_Domain.html#assumptions-preliminaries) | 【推導 1】；零元素必須相同 |
| 整環上的多項式環仍是整環 (Polynomial ring over an integral domain) | `R \ \text{整環} \Longrightarrow R[x] \ \text{整環},\quad \deg(fg) = \deg f + \deg g` | [Integral_Domain #b](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Ring/Integral_Domain.html#assumptions-preliminaries) | 【推導 2】；可無限次遞迴套用 |
| 理想判別法 (Ideal criterion) | `I \trianglelefteq R \Longleftrightarrow I \neq \varnothing,\ a-b \in I,\ ar \in I` | [Ideal #a](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Ring/Ideal.html#assumptions-preliminaries) | 【推導 1】；**$r$ 取遍整個 $R$**（與子環的差別） |
| $aR$ 恆為理想 (The set of multiples is an ideal) | `aR = \left\{ar \mid r \in R\right\} \trianglelefteq R` | [Ideal #b-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Ring/Ideal.html#b-proof-that-the-set-of-multiples-of-an-element-is-an-ideal) | 交換環；這就是主理想 $\left\langle a \right\rangle$ |
| 理想的交與和仍是理想 (Intersection and sum of ideals) | `I_1 \cap I_2,\ I_1 + I_2 \trianglelefteq R` | [Ideal #e-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Ring/Ideal.html#e-proof-that-the-intersection-and-the-sum-of-two-ideals-are-ideals) | **聯集一般不是理想**；$\mathbf{Z}$ 中交對應 lcm、和對應 gcd |
| **$\mathbf{Z}$ 是 PID** (The integers form a PID) | `I \trianglelefteq \mathbf{Z} \Longrightarrow I = \left\langle d \right\rangle` | [Principal_Ideal #c-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Ring/Principal_Ideal.html#c-proof-that-every-ideal-of-the-integers-is-principal) | 靠除法原理；$d$ 是 $I$ 的最小正元素 |
| 生成理想與 gcd (Generated ideal equals the gcd ideal) | `\left\langle a, b \right\rangle = \left\langle \gcd(a,b) \right\rangle` | [Principal_Ideal #d](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Ring/Principal_Ideal.html#d-verify-that-the-ideal-generated-by-fifteen-and-twenty-one-is-principal) | 在 $\mathbf{Z}$ 或任一 PID 中 |
| $\mathbf{Q}[x,y]$ 不是 PID | `\left\langle x, y \right\rangle \ \text{非主理想}` | [Principal_Ideal #e-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Ring/Principal_Ideal.html#e-disprove-that-the-ideal-generated-by-two-indeterminates-is-principal) | 未定元 $\ge 2$ 即失去 PID 性質 |
| $\mathbf{Z}[x]$ 不是 PID | `E = \left\langle 2, x \right\rangle \ \text{非主理想}` | [Non_Principal_Ideal_in_Z_x #b-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Ring/Non_Principal_Ideal_in_Z_x.html#b-proof-that-the-ideal-is-not-principal) | 係數環不是體即失去 PID 性質 |
| 模理想的同餘是等價關係 (Congruence modulo an ideal is an equivalence relation) | `a \equiv b \pmod{I} \Longleftrightarrow a - b \in I` | [Congruence_Class #a-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Ring/Congruence_Class_Modulo_Ideal.html#a-proof-that-congruence-modulo-an-ideal-is-an-equivalence-relation) | **只需加法子群**，不必是理想 |
| 同餘類就是陪集 (Congruence classes are cosets) | `a + I = \left\{a + c \mid c \in I\right\}` | [Congruence_Class #b-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Ring/Congruence_Class_Modulo_Ideal.html#b-proof-that-a-congruence-class-is-a-coset) | 於是陪集分割的三條引理全部適用 |
| **商環的良定義性 (Well-definedness of the quotient ring)** | `\left(a+I\right)\left(b+I\right) = ab + I` | [Quotient_Ring #b-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Ring/Quotient_Ring.html#b-proof-that-multiplication-is-well-defined) | **乘法的良定義必須用吸收性** —— 子環辦不到 |
| 商環是環 (The quotient is a ring) | `R/I \ \text{為環}` | [Quotient_Ring #c-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Ring/Quotient_Ring.html#c-proof-that-the-quotient-is-a-ring) | $I$ 必須是理想 |
| $\mathbf{Z}/n\mathbf{Z} \cong \mathbf{Z}_n$ | `\mathbf{Z}/n\mathbf{Z} \cong \mathbf{Z}_n` | [Quotient_Ring #e-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Ring/Quotient_Ring.html#e-proof-that-the-integers-modulo-the-multiples-of-n-form-the-ring-of-residues) | **「取模」的正式定義** |
| 核是理想 (The kernel is an ideal) | `\ker f \trianglelefteq R` | [Ring_Homomorphism #b-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Ring/Ring_Homomorphism_and_Kernel.html#b-proof-that-the-kernel-is-an-ideal) | 任意環同態；吸收性來自 $0$ 是乘法吸收元 |
| 單射等價核平凡 (Injective iff trivial kernel) | `f \ \text{單射} \Longleftrightarrow \ker f = \left\{0\right\}` | [Ring_Homomorphism #c-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Ring/Ring_Homomorphism_and_Kernel.html#c-proof-that-injectivity-is-equivalent-to-a-trivial-kernel) | **投影片未列**，本章補 |
| **中國剩餘定理 (Chinese remainder theorem)** | `R/\left(I_1 \cap \cdots \cap I_k\right) \cong R/I_1 \times \cdots \times R/I_k` | [Chinese_Remainder_Theorem #c-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Ring/Chinese_Remainder_Theorem.html#c-proof-of-surjectivity-and-the-isomorphism) | **理想必須兩兩互質**（$I_i + I_j = R$）。RSA-CRT、Kyber 的 NTT |

## Field (體)

| 名稱 (Name) | LaTeX Statement | 連結 (Link) | 前提／適用條件 |
|---|---|---|---|
| **$\mathbf{Z}_p$ 是體的充要條件** (Residues modulo p form a field) | `\mathbf{Z}_p \ \text{為體} \Longleftrightarrow p \ \text{為質數}` | [Field_Definition #b-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Field/Field_Definition.html#b-proof-that-the-residues-modulo-a-prime-form-a-field) | **密碼學一律用質數模的理由**；$GF(2^8) \neq \mathbf{Z}_{256}$ |
| 體必為整環 (Every field is an integral domain) | `F \ \text{為體} \Longrightarrow F \ \text{無零因子}` | [Field_Definition #d-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Field/Field_Definition.html#d-proof-that-every-field-is-an-integral-domain) | **逆命題不成立**（$\mathbf{Z}$ 為反例） |
| **體的特徵必為質數** (The characteristic of a field is prime) | `\mathrm{ch}(F) = p > 0 \Longrightarrow p \ \text{為質數}` | [Characteristic_of_a_Field #b-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Field/Characteristic_of_a_Field.html#b-proof-that-a-positive-characteristic-must-be-prime) | **必須是體**（$\mathbf{Z}_6$ 的特徵是合數 $6$） |
| 有限體的特徵為正 (Finite fields have positive characteristic) | `\left\|F\right\| < \infty \Longrightarrow \mathrm{ch}(F) > 0` | [Characteristic_of_a_Field #d-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Field/Characteristic_of_a_Field.html#d-proof-that-a-finite-field-has-positive-characteristic) | 鴿籠原理；**投影片未列**，本章補 |
| 質數整除二項式係數 (A prime divides the interior binomial coefficients) | `p \ \Big\| \ \binom{p}{i} \quad (1 \le i \le p-1)` | [Prime_Divides_Binomial_Coefficient #a-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Field/Prime_Divides_Binomial_Coefficient.html#a-proof-that-a-prime-divides-the-interior-binomial-coefficients) | **$p$ 必須是質數**；投影片的範圍寫成 $2 \le i$，本章放寬至 $1 \le i$ |
| **新生之夢 (Freshman's dream)** | `\left(a+b\right)^{p^n} = a^{p^n} + b^{p^n}` | [Freshmans_Dream #b-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Field/Freshmans_Dream.html#b-proof-of-the-inductive-step) | **$\mathrm{ch}(F) = p$**；指數必須恰為 $p$ 的冪。Frobenius 自同態的基礎 |
| 子體判別法 (Subfield criterion) | `K \ \text{子體} \Longleftrightarrow \left\|K\right\| \ge 2,\ a-b \in K,\ ab^{-1} \in K` | [Subfield_and_Field_Extension #a-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Field/Subfield_and_Field_Extension.html#a-proof-of-the-subfield-criterion) | **「至少兩個元素」不能寫成「非空」**（否則零環會混進來） |
| 大體是小體上的向量空間 (The larger field is a vector space) | `L : K \Longrightarrow L \ \text{為 } K\text{-向量空間}` | [Subfield_and_Field_Extension #c-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Field/Subfield_and_Field_Extension.html#c-proof-that-the-larger-field-is-a-vector-space-over-the-subfield) | 向量空間公理全部是體公理的子集；$\left[L:K\right] = n \Rightarrow \left\|L\right\| = \left\|K\right\|^n$ |
| 二三次不可約判別法 (Root criterion for degrees two and three) | `\deg f \in \{2,3\} \Longrightarrow \left[f \ \text{不可約} \Leftrightarrow f \ \text{無根}\right]` | [Irreducible_Polynomial #a-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Field/Irreducible_Polynomial.html#a-proof-of-the-root-criterion-for-degrees-two-and-three) | **只對次數 $2,3$ 成立**；$x^4+x^2+1 \in \mathbf{Z}_2[x]$ 無根卻可約 |
| **塔定理 (Tower law)** | `\left[M:K\right] = \left[M:L\right]\left[L:K\right]` | [Tower_Law #a-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Field/Tower_Law.html#a-proof-of-the-tower-law) | $K \subseteq L \subseteq M$；基底是兩層基底的乘積。配對密碼學的塔式實作 |
| **模不可約多項式的商環是體** (Quotient by an irreducible polynomial is a field) | `p(x) \ \text{不可約} \Longrightarrow F[x]/\left\langle p \right\rangle \ \text{為體}` | [Quotient_by_Irreducible #a-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Field/Quotient_by_Irreducible_is_Field.html#a-proof-that-the-quotient-by-an-irreducible-polynomial-is-a-field) | **$GF(2^8)$ 的唯一造法**；與「$\mathbf{Z}_p$ 是體」是同一條定理在兩個 PID 上的實例 |
| 商環的擴張次數 (Degree of the quotient extension) | `\left[F[x]/\left\langle p \right\rangle : F\right] = \deg p` | [Quotient_by_Irreducible #b-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Field/Quotient_by_Irreducible_is_Field.html#b-proof-of-the-degree-of-the-extension) | 基底 $\left\{1,\bar{x},\dots,\bar{x}^{\deg p - 1}\right\}$；**AES 位元組表示的來源** |
| 單擴張是體 (A simple extension is a field) | `K(a) = \left\{f(a)/g(a) \mid g(a) \neq 0\right\} \ \text{為體}` | [Simple_Extension #a-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Field/Simple_Extension.html#a-proof-that-the-simple-extension-is-a-field) | $L$ 必須是體（通分需要無零因子） |
| 單擴張是最小子體 (The simple extension is the smallest such subfield) | `K \subseteq M,\ a \in M \Longrightarrow K(a) \subseteq M` | [Simple_Extension #b-proof](https://derek1403.github.io/PC-NTU/Cryptography/_build/html/lecture/Algebra/Abstract_Algebra/Field/Simple_Extension.html#b-proof-that-the-simple-extension-is-the-smallest-such-subfield) | 「由 $a$ 生成」的精確意思 |

---

## 未證明但已陳述的結論 (Stated Without Proof)

以下結論在本章中被**明確標示為未證明**，引用時請一併標示出處與「本章未證」：

| 名稱 | 出處 | 為什麼沒證 |
|---|---|---|
| 橢圓曲線點群的結合律 | [群的正例與反例](Group/Group_Examples_and_Counterexamples.md#stated-without-proof) | 需射影幾何的 Cayley–Bacharach 定理或除子理論 |
| **本原元定理** (Primitive element theorem) | [本原元定理](Field/Primitive_Element_Theorem.md#a-statement-of-the-theorem) | 需可分性與中間體有限性（伽羅瓦理論） |
| 第一同構定理 $R/\ker f \cong \mathrm{im}\,f$ | [環同態與核](Ring/Ring_Homomorphism_and_Kernel.md) 文末 | 本章以三個例子說明，未正式證明 |
| 有限體的階必為質數冪、$GF(q)^*$ 為循環群 | [體的定義](Field/Field_Definition.md) 文末、[本原元定理](Field/Primitive_Element_Theorem.md) 文末 | 超出投影片範圍 |
| $\mathbf{Z}_n^*$ 循環的充要條件 | [循環群](Group/Cyclic_Group.md) 文末 | 超出投影片範圍 |
