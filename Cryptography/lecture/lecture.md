# Lecture (課程講義)

本章收錄 Cryptography 課程的講義整理。

## Algebra (代數)

密碼學的數學地基。目前分成三個部分：

| 子目錄 | 來源投影片 | 狀態 |
|---|---|---|
| [Abstract_Algebra](Algebra/Abstract_Algebra/Abstract_Algebra.md) | `Algebra.pdf`（54 頁） | **已完整整理** —— 49 個檔案，一個概念／定理一個 md |
| `Arithmatic` | `Arithmetic.pptx` | 整數運算、GCD、模運算（既有 notebook） |
| `Finite_Fields` | `FiniteFields.pdf` | 尚未整理 |

### 抽象代數這一章怎麼讀

[抽象代數](Algebra/Abstract_Algebra/Abstract_Algebra.md) 依照
**群 (Group) $\to$ 環 (Ring) $\to$ 體 (Field)** 的順序建構，每個檔案是一個獨立的概念或定理，
格式固定為：

$$\text{證明目標} \ \to \ \text{假設與已知（卡片）} \ \to \ \text{證明} \ \to \ \text{意義與密碼學關聯}$$

* **每個檔案自帶完整的前置知識**，不必先讀完前面所有檔案；
* 證明中每個有依據的等號都掛著 `\overset{\text{已知 1}}{=}` 之類的標註，可逐步回溯；
* 想查某條定理有沒有被證過，先看 [定理索引表](Algebra/Abstract_Algebra/theorems_index.md)。

### 這一章與密碼學的連結

| 代數結果 | 密碼學用途 |
|---|---|
| 拉格朗日定理 $\to$ 尤拉定理 | **RSA 解密之所以成立** |
| 循環群與離散對數 | **Diffie–Hellman、ElGamal、ECC** |
| 中國剩餘定理 | **RSA-CRT 加速、Kyber 的 NTT** |
| 模不可約多項式的商環是體 | **AES 的 $GF(2^8)$** |
| 一般線性群 $GL_8(\mathbf{Z}_2)$ | **AES S-box 的仿射變換** |
