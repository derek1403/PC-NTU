# 大寫 $X$ 與小寫 $x$ (Random Variable vs. Observed Value)

統計符號的大小寫有固定分工：**大寫是「還沒抽」的隨機變數，小寫是「抽完了」的數字**。
混用時最常見的後果，是寫出 $\mathrm{Var}(\bar{x})$ 這種字面上等於 $0$ 的式子。

## 1. 三種角色

| 角色 | 寫法 | 例（明天 00Z 的探空溫度） | 有沒有分布？ |
|---|---|---|---|
| 隨機變數 (Random variable) | 大寫 $X$ | 明天會量到的溫度，現在還不知道 | 有：可談 $\mathbb{E}[X]$、$\mathrm{Var}(X)$ |
| 實現值 (Realization) | 小寫 $x$ | 明天量完，讀數是 $-17\ ^\circ\text{C}$ | 沒有：就是一個固定的數 |
| 母體參數 (Parameter) | 希臘字母 $\mu, \sigma^2$ | 氣候上真正的平均與變異 | 沒有：固定但未知的常數 |

機率密度裡的 $x$ 則是**函數的引數**，用來描述「$X$ 落在 $x$ 附近的機率」：

$$\Pr(X \le x) = F(x) = \int_{-\infty}^{x} f(t)\,dt$$

## 2. 樣本統計量的對照

| 量 | 隨機變數（推論時用） | 實現值（手上資料算出的數） |
|---|---|---|
| 第 $i$ 筆 | $X_i$ | $x_i$ |
| 樣本平均 | $\bar{X} = \frac{1}{N}\sum X_i$ | $\bar{x} = \frac{1}{N}\sum x_i$ |
| 樣本變異數 | $S^2 = \frac{1}{N-1}\sum (X_i - \bar{X})^2$ | $s^2 = \frac{1}{N-1}\sum (x_i - \bar{x})^2$ |
| $z$ 統計量 | $Z = \frac{\bar{X} - \mu}{\sigma/\sqrt{N}}$ | $z_{\text{obs}} = \frac{\bar{x} - \mu}{\sigma/\sqrt{N}}$ |

## 3. 什麼時候用哪一個

* **談「重抽很多次會怎樣」用大寫**：不偏 $\mathbb{E}[\bar{X}] = \mu$、標準誤 $\sigma_{\bar{X}} = \sigma/\sqrt{N}$、$\mathbb{E}[S^2] = \sigma^2$，說的都是 $\bar{X}$、$S^2$ 在所有可能樣本上的分布（見 [03_standard_error](02_proof/03_standard_error.md)、[04_sample_variance_N-1](02_proof/04_sample_variance_N-1.md)）。
* **談「這批資料算出多少」用小寫**：描述統計、代入數字時用 $\bar{x}$、$s$。
* **檢定就是把兩者接起來**：先用大寫 $Z$ 的分布算出拒絕域，再把小寫 $z_{\text{obs}}$ 代進去看落在哪裡。

課本也是這樣分：描述統計（Mean、Variance 小節）用 $\bar{x}$；標準誤與 $z$ 檢定（"Estimating the statistical significance of the sample mean"）改用 $\overline{X}$、$\sigma_{\overline{X}}$。（見 [99_textbook.md](99_textbook.md)。）
