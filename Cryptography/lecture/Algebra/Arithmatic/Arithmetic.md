# Arithmetic (整數算術)

公鑰密碼學的計算引擎。本章把 `Arithmetic.pdf`（56 頁投影片）拆成**一個概念／定理一個檔案**，
每一條命題都給出逐步、可回溯的完整證明；每一個演算法都證明「不變量、終止、輸出正確」三件事；
每一個數值例子都用 Python 驗算過。

+++

## 為什麼密碼學要學這個

[Abstract_Algebra](../Abstract_Algebra/Abstract_Algebra.md) 告訴你密碼系統**是什麼結構**；本章告訴你**怎麼在上面算**。

| 密碼學零件 | 用到的算術 | 本章對應 |
|---|---|---|
| RSA 金鑰產生：檢查 $\gcd\left(e, \varphi(n)\right) = 1$ | 歐幾里得演算法 | [歐幾里得演算法](GCD/Euclidean_Algorithm.md) |
| RSA 私鑰 $d = e^{-1} \bmod \varphi(n)$ | 擴展歐幾里得、模反元素 | [擴展歐幾里得演算法](GCD/Extended_Euclidean_Algorithm.md)、[模反元素](Congruence/Modular_Inverse.md) |
| RSA 的 $\varphi(n) = (p-1)(q-1)$ | 尤拉函數的乘法性 | [尤拉函數的乘法性](Fermat_Euler/Euler_Phi_Multiplicativity.md) |
| RSA 為什麼能解密 | 尤拉定理、指數化簡 | [尤拉定理](Fermat_Euler/Euler_Theorem.md) |
| RSA-CRT 解密加速四倍 | 中國剩餘定理（Garner 形式） | [兩個模數的中國剩餘定理](CRT/Two_Moduli_CRT.md) |
| RSA 的安全性：分解 $n$ 很難 | 算術基本定理 | [算術基本定理](Factorization/Fundamental_Theorem_of_Arithmetic.md) |
| 大質數產生（Miller–Rabin 的前身） | 費馬小定理、Carmichael 數 | [費馬小定理](Fermat_Euler/Fermat_Little_Theorem.md)、[Carmichael 數](Fermat_Euler/Carmichael_Numbers.md) |
| ECC 在 $\mathbf{F}_p$ 上的常數時間求逆 | $a^{-1} = a^{p-2}$ | [費馬小定理](Fermat_Euler/Fermat_Little_Theorem.md)【證明 (d)】 |
| 常數時間 gcd（libsecp256k1 等） | 二進位 gcd | [Stein 二進位 GCD](GCD/Stein_Binary_GCD.md) |
| Kyber / ML-KEM 的係數表示 | 完全剩餘系的代表元選法 | [完全剩餘系](Fermat_Euler/Complete_Residue_System.md) |
| 秘密分享、RNS 加速 | 中國剩餘定理（高斯形式） | [中國剩餘定理](CRT/Chinese_Remainder_Theorem.md) |

+++

## 學習地圖：除法 $\to$ gcd $\to$ 分解 $\to$ 同餘 $\to$ CRT $\to$ 費馬與尤拉

七個主題是**一條依賴鏈** —— 每一段都只用前面已證的東西：

$$\text{除法原理} \ \longrightarrow \ \gcd \ \longrightarrow \ \text{貝祖等式} \ \longrightarrow \ \text{歐幾里得引理} \ \longrightarrow \ \text{模反元素} \ \longrightarrow \ \text{CRT} \ \longrightarrow \ \varphi \ \text{與尤拉定理}$$

### 1. 除法與取模 (Division)

* **基本功**：[取整函數](Division/Floor_and_Ceiling.md) $\to$ **[取模函數](Division/Modular_Function.md)**（除法原理：商與餘數唯一）
* **具體的例子**：[$\mathbf{Z}_6$ 的凱萊表](Division/Cayley_Tables_of_Z6.md)（$\mathbf{Z}_6$ 不是體、$\mathbf{Z}_7$ 是）

### 2. 最大公因數 (GCD)

* **基本功**：[整除的基本性質](GCD/Divisibility_Basics.md)（投影片未列，本章補）$\to$ [最大公因數](GCD/Greatest_Common_Divisor.md)
* **演算法的數學核心**：[GCD 的平移不變性](GCD/GCD_Shift_Invariance.md)：$\gcd(a, b) = \gcd(b, a \bmod b)$
* **三個演算法**：**[歐幾里得演算法](GCD/Euclidean_Algorithm.md)** $\to$ **[擴展歐幾里得演算法](GCD/Extended_Euclidean_Algorithm.md)** $\to$ [Stein 二進位 GCD](GCD/Stein_Binary_GCD.md)
* **gcd 的第二種刻畫**：**[貝祖等式](GCD/Bezout_Identity.md)**（gcd 是最小正組合；互質 $\Leftrightarrow$ 湊得出 $1$）

### 3. 質因數分解 (Factorization)

* [互質](Factorization/Relatively_Prime.md) $\to$ [歐幾里得引理](Factorization/Euclid_Lemma.md) $\to$ **[算術基本定理](Factorization/Fundamental_Theorem_of_Arithmetic.md)** $\to$ [最小公倍數](Factorization/Least_Common_Multiple.md)

### 4. 同餘 (Congruence)

* [同餘關係](Congruence/Congruence_Relation.md) $\to$ [同餘的性質](Congruence/Congruence_Properties.md) $\to$ **[模反元素](Congruence/Modular_Inverse.md)**

### 5. 中國剩餘定理 (CRT)

* [座標表示](CRT/CRT_Coordinate_Representation.md) $\to$ [兩個模數的 CRT](CRT/Two_Moduli_CRT.md) $\to$ **[中國剩餘定理](CRT/Chinese_Remainder_Theorem.md)** $\to$ [中國剩餘演算法](CRT/Chinese_Remainder_Algorithm.md)

### 6. 費馬與尤拉 (Fermat and Euler)

* **費馬**：[費馬小定理](Fermat_Euler/Fermat_Little_Theorem.md) $\to$ [Carmichael 數](Fermat_Euler/Carmichael_Numbers.md)
* **尤拉**：[完全剩餘系](Fermat_Euler/Complete_Residue_System.md) $\to$ [尤拉函數](Fermat_Euler/Euler_Phi_Function.md) $\to$ [尤拉函數的乘法性](Fermat_Euler/Euler_Phi_Multiplicativity.md) $\to$ [化簡剩餘系](Fermat_Euler/Reduced_Residue_System.md) $\to$ **[尤拉定理](Fermat_Euler/Euler_Theorem.md)**
* **尾聲**：[費馬最後定理](Fermat_Euler/Fermat_Last_Theorem.md)（陳述不證，只證化約引理）

+++

## 與 Abstract_Algebra 章的分工

兩章有幾條定理「重疊」。本章的原則是**引用免證** —— Abstract_Algebra 已證的一律用帶超連結的【已知】卡片引用：

| 結論 | 在哪裡證 | 本章怎麼處理 |
|---|---|---|
| 費馬小定理、尤拉定理 | Abstract_Algebra（拉格朗日定理的特例） | 引用；本章證其推論（$a^p \equiv a$、指數化簡、RSA） |
| 中國剩餘定理（環同構） | Abstract_Algebra（理想與商環） | 引用；本章證**可計算的**版本（Garner 公式、高斯公式、遞迴演算法） |
| $\left\|\mathbf{Z}_n^*\right\| = \varphi(n)$、$\varphi$ 的定義 | Abstract_Algebra | 引用；本章證 $\varphi$ 的算法（質數冪、乘法性、乘積公式） |
| $\mathbf{Z}_p$ 是體、$\mathbf{Z}$ 是 PID | Abstract_Algebra | 引用 |
| 除法原理、貝祖等式、歐幾里得引理、模反元素判準 | Abstract_Algebra **當外部已知引用，未證** | **本章完整證明** |

最後一列補上了 Abstract_Algebra 章的外部依賴 —— 兩章合起來，從整數的除法一路到 RSA，**每一步都有證明**。

+++

## 怎麼用這本筆記

* **查式子**：[定理索引表](theorems_index.md) 收錄本章**已經逐步證過**的所有結論。
  寫新推導時先查這張表，凡是表上有的一律**引用，不重證**。
* **讀單一定理**：每個檔案都自帶完整的「假設與已知」，**不需要先讀完前面所有檔案**。
  證明中每一個有依據的等號都掛著 `\overset{\text{已知 1}}{=}` 之類的標註，
  順著標註往上找就能回溯到該檔的某張卡片，或經超連結回溯到另一個檔案（包括 Abstract_Algebra 章）。
* **跑程式**：每個檔案文末的「程式思維」都是可以直接執行的 Python，並用 `assert` 核對本檔的數值結果。

+++

## 本章書寫慣例 (Writing Conventions)

本章完全沿用 [Abstract_Algebra](../Abstract_Algebra/Abstract_Algebra.md) 的**書寫慣例 A1–A8**
（型別欄取代單位欄、反設寫成【假設】卡片、iff 拆 (⇒)(⇐)、集合等式拆雙向包含、歸納法拆基底與歸納步驟、
例子逐條驗、邏輯蘊涵放 `gather*` 關係欄、【推導】卡片當減壓閥）。
本章因為大量處理**演算法**與**數值計算**，另外補充兩條：

* **A9 演算法正確性三件套**：每個演算法先寫成【定義】卡片（狀態序列或遞迴式），再分開證明
  **不變量**（通常用歸納法，依 A5 拆基底與歸納步驟）、**終止性**（嚴格遞減的非負整數不能無限下去）、
  **輸出正確**（終止時不變量給出答案）。範例：[歐幾里得演算法](GCD/Euclidean_Algorithm.md)、
  [擴展歐幾里得演算法](GCD/Extended_Euclidean_Algorithm.md)、[中國剩餘演算法](CRT/Chinese_Remainder_Algorithm.md)。

* **A10 數值例子必須可重現**：每個數值例子在 `gather*` 裡逐步算（取模的每一步都寫出「商 $\times$ 模 $+$ 餘」），
  並在文末「程式思維」用 `assert` 驗算。投影片的數值若有誤，以驗算結果為準並在「註」中標示。

不變的鐵則：每個援引都要 `\overset` 標註；`gather*` 的左式**全有或全無**；一行只有一個關係；
引用鏈必須是有向無環圖（不可引用後面才證的結果）；投影片若有錯誤或漏條件，照正確數學寫並在「註」明確標出差異。

+++

## 資料來源

* 投影片：`Arithmetic.pdf`（Introduction to Cryptography，56 頁）
* 相關章節：[Abstract_Algebra](../Abstract_Algebra/Abstract_Algebra.md)（群、環、體）、`Finite_Fields/`（有限體）
