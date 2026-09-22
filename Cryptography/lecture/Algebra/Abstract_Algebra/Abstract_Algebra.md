# Abstract Algebra (抽象代數)

密碼學的地基。本章把 `Algebra.pdf`（54 頁投影片）拆成**一個概念／定理一個檔案**，
每一條命題都給出逐步、可回溯的完整證明。

+++

## 為什麼密碼學要學這個

現代密碼系統的每一個零件，拆開來看都是一個代數結構：

| 密碼學零件 | 底層代數結構 | 本章對應 |
|---|---|---|
| AES 的 S-box | $S_{256}$ 的一個排列 | [排列](Group/Permutation.md)、[對稱群](Group/Symmetric_Group.md) |
| AES S-box 的仿射變換矩陣 | $GL_8(\mathbf{Z}_2)$ 的一個元素 | [一般線性群的階](Group/General_Linear_Group_Order.md) |
| AES 的位元組運算 | 有限體 $GF(2^8)$ | [體的定義](Field/Field_Definition.md)、[不可約多項式](Field/Irreducible_Polynomial.md) |
| RSA 的 $\varphi(n)$ 與指數運算 | $\mathbf{Z}_n^*$ 這個交換群 | [群的階](Group/Group_Order.md)、[拉格朗日定理](Group/Lagrange_Theorem.md) |
| RSA 解密的加速（CRT） | 商環的直積分解 | [中國剩餘定理](Ring/Chinese_Remainder_Theorem.md) |
| Diffie–Hellman、ElGamal | 循環群與生成元 | [循環群](Group/Cyclic_Group.md) |
| 橢圓曲線密碼 (ECC) | 曲線上的點構成的阿貝爾群 | [群的定義](Group/Group_Definition.md) |
| 整數分解（Number Field Sieve） | Dedekind 整環、UFD、PID | [整環](Ring/Integral_Domain.md)、[主理想](Ring/Principal_Ideal.md) |

+++

## 學習地圖：群 $\to$ 環 $\to$ 體

三個結構是**逐層加碼**的關係 —— 每往下一層，就多要求一組運算或一組公理：

$$\text{群 (Group)} \ \xrightarrow{\ \text{再加一個乘法}\ } \ \text{環 (Ring)} \ \xrightarrow{\ \text{非零元素都可逆}\ } \ \text{體 (Field)}$$

| | 加法 $+$ | 乘法 $\times$ |
|---|---|---|
| **群 (Group)** | 只有**一個**運算，滿足封閉／結合／單位／反元素 | — |
| **環 (Ring)** | 阿貝爾群 | 封閉、結合、對加法分配 |
| **體 (Field)** | 阿貝爾群 | 再要求**每個非零元素都有乘法反元素** |

### 1. 群 (Group) 群

* **基本功**：[群的定義](Group/Group_Definition.md) $\to$ [正例與反例](Group/Group_Examples_and_Counterexamples.md)
* **四條基本命題**：[單位元素唯一](Group/Uniqueness_of_Identity.md)、[反元素唯一](Group/Uniqueness_of_Inverse.md)、[反元素的反元素](Group/Inverse_of_an_Inverse.md)、[乘積的反元素](Group/Inverse_of_a_Product.md)、[唯一解與消去律](Group/Unique_Solution_and_Cancellation_Law.md)
* **具體的群**：[排列](Group/Permutation.md) $\to$ [對稱群](Group/Symmetric_Group.md)、[阿貝爾群與非阿貝爾群](Group/Abelian_and_Non_Abelian_Group.md)、[循環群](Group/Cyclic_Group.md)
* **大小**：[群的階](Group/Group_Order.md)、[一般線性群的階](Group/General_Linear_Group_Order.md)
* **切開來看**：[子群判別法](Group/Subgroup_Criterion.md) $\to$ [子群的例子](Group/Subgroup_Examples.md) $\to$ [陪集](Group/Coset.md) $\to$ [陪集相等的充要條件](Group/Coset_Equality_Criterion.md) $\to$ [陪集分割](Group/Coset_Partition.md) $\to$ **[拉格朗日定理](Group/Lagrange_Theorem.md)**
* **應用**：[元素的階與循環子群](Group/Order_of_Element_and_Cyclic_Subgroup.md)、[特殊線性群的指標](Group/Special_Linear_Subgroup_Index.md)
* **結構的搬運**：[群同態與群同構](Group/Group_Homomorphism_and_Isomorphism.md)

### 2. 環 (Ring) 環

* **基本功**：[環的定義](Ring/Ring_Definition.md) $\to$ [環的例子](Ring/Ring_Examples.md) $\to$ [含單位元環與交換環](Ring/Ring_with_Identity_and_Commutative_Ring.md) $\to$ [環的基本命題](Ring/Ring_Basic_Propositions.md) $\to$ [子環](Ring/Subring.md)
* **好環與壞環**：[零因子](Ring/Zero_Divisor.md) $\to$ [整環](Ring/Integral_Domain.md)
* **理想**：[理想](Ring/Ideal.md) $\to$ [主理想](Ring/Principal_Ideal.md) $\to$ [$\mathbf{Z}[x]$ 中的非主理想](Ring/Non_Principal_Ideal_in_Z_x.md)
* **除掉理想**：[模理想的同餘類](Ring/Congruence_Class_Modulo_Ideal.md) $\to$ **[商環](Ring/Quotient_Ring.md)**
* **結構的搬運**：[環同態與核](Ring/Ring_Homomorphism_and_Kernel.md) $\to$ **[中國剩餘定理](Ring/Chinese_Remainder_Theorem.md)**

### 3. 體 (Field) 體

* **基本功**：[體的定義](Field/Field_Definition.md) $\to$ [體的特徵](Field/Characteristic_of_a_Field.md)
* **特徵 $p$ 的魔法**：[質數整除二項式係數](Field/Prime_Divides_Binomial_Coefficient.md) $\to$ **[新生之夢](Field/Freshmans_Dream.md)**
* **把體變大**：[子體與體擴張](Field/Subfield_and_Field_Extension.md) $\to$ [不可約多項式](Field/Irreducible_Polynomial.md) $\to$ [塔定理](Field/Tower_Law.md) $\to$ **[模不可約多項式的商環是體](Field/Quotient_by_Irreducible_is_Field.md)** $\to$ [單擴張](Field/Simple_Extension.md) $\to$ [本原元定理](Field/Primitive_Element_Theorem.md)

+++

## 怎麼用這本筆記

* **查式子**：[定理索引表](theorems_index.md) 收錄本章**已經逐步證過**的所有結論。
  寫新推導時先查這張表，凡是表上有的一律**引用，不重證**。
* **查符號**：[數系與符號約定](Number_Sets_and_Notation.md) 是全章共用的符號來源
  （$\mathbf{Z}$、$\mathbf{Z}_n$、$\mathbf{Z}_n^*$、$GL_n$、$SL_n$…）。
* **讀單一定理**：每個檔案都自帶完整的「假設與已知」，**不需要先讀完前面所有檔案**。
  證明中每一個有依據的等號都掛著 `\overset{\text{已知 1}}{=}` 之類的標註，
  順著標註往上找就能回溯到該檔的某張卡片，或經超連結回溯到另一個檔案。

+++

## 本章書寫慣例 (Writing Conventions)

本章遵循 [derivation-style-review](https://github.com/derek1403/PC-NTU/blob/main/.claude/skills/derivation-style-review/SKILL.md)
的推導風格：**先把所有已知／假設／定義／推導編號攤開，證明過程只做引用**。
該規範原為物理推導而寫，套用到抽象代數時補充以下八條（代號 A1–A8）：

* **A1 型別欄取代單位欄**：抽象代數沒有物理單位，符號清單末尾的中括號改標**型別／所屬**。

  ```
  * $G$ : 群 (Group) $[\text{集合}]$
  * $a,\ b$ : 群元素 (Group elements) $[a, b \in G]$
  * $*$ : 二元運算 (Binary operation) $[G \times G \to G]$
  * $\varphi$ : 尤拉函數 (Euler's totient function) $[\mathbb{Z}^{+} \to \mathbb{Z}^{+}]$
  ```

* **A2 反證法**：反設本身寫成一張**【假設 N】卡片**（例：「**【假設 1】 反設 (Proof by contradiction)**：
  $G$ 有兩個相異的單位元素」），矛盾鏈在證明段用 `gather*` 跑到底，
  末尾一句「與【假設 1】矛盾」收束。**不在證明段臨時宣告反設。**

* **A3 iff 拆雙向**：充要條件拆成 `### (a) proof (⇒) …` 與 `### (b) proof (⇐) …` 兩個子節，各一條 `gather*` 鏈。

* **A4 集合等式**：$A = B$ 拆成 `### (a) proof $A \subseteq B$` 與 `### (b) proof $B \subseteq A$`。

* **A5 數學歸納法**：拆成 `### (a) proof base case` 與 `### (b) proof inductive step`，
  **歸納假設寫成【假設 N】卡片**。

* **A6 例子也要逐條驗**：`Example` 型檔案裡每個例子給一個次級編號 `(a) (b) (c)`，
  四公理逐條用 `gather*` 驗；反例則明確指出**壞掉的是哪一條公理**並給出具體的反例元素。
  **禁止寫「顯然成立」。**

* **A7 邏輯蘊涵用關係欄**：比照不等式用 `&\ll&` 的做法，`gather*` 內把 $\Rightarrow$ 放在**關係欄**，
  一行一個蘊涵：

  ```
  $$\begin{gather*}
  a * b &\overset{\text{定義 1}}{=}& a * c \\
  b     &\overset{\text{推導 1}}{\Rightarrow}& c
  \end{gather*}$$
  ```

  **禁止**把 `A = B \Rightarrow C = D` 擠成一行。

* **A8 【推導】卡片是減壓閥**：本檔特有的局部引理提前算掉，讓主證明只剩一條乾淨的 `gather*`。

不變的鐵則：每個援引都要 `\overset` 標註；`gather*` 的左式**全有或全無**；
引用鏈必須是有向無環圖（不可引用後面才證的結果）；高對稱的平行操作收束在同一主標號下用 `(a)(b)(c)`。

+++

## 資料來源

* 投影片：`Algebra.pdf`（Introduction to Cryptography，54 頁）
* 相關但不屬於本章：[Arithmetic](../Arithmatic/Arithmetic.ipynb)（整數運算、GCD、模運算）、
  `Finite_Fields/FiniteFields.pdf`（有限體，尚未整理）
