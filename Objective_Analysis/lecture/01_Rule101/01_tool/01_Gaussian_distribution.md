# 高斯分布 (Gaussian Distribution)

高斯分布（常態分布）是一條以平均值為中心、左右對稱的鐘形曲線，只要兩個參數就完全決定：
**平均值 $\mu$ 決定中心在哪裡，標準差 $\sigma$ 決定有多寬**。
同一條曲線在不同脈絡下會寫成不同長相，下面列出本課會遇到的四種寫法，它們全都是同一個函數。

## 1. 標準形式 (Standard Form)

$$f(x) = \frac{1}{\sigma\sqrt{2\pi}}\exp\left(-\frac{(x-\mu)^2}{2\sigma^2}\right)$$

* $\mu$ : 平均值、期望值 (Mean)，曲線中心
* $\sigma$ : 標準差 (Standard deviation)，曲線寬度；$\sigma^2$ 為變異數 (Variance)
* $\frac{1}{\sigma\sqrt{2\pi}}$ : 正規化常數，讓 $\int_{-\infty}^{\infty} f\,dx = 1$（見 [02_Gaussian_integrals.md](02_Gaussian_integrals.md)）

常記作 $X \sim \mathcal{N}(\mu, \sigma^2)$。

## 2. 標準化形式 (Standardized, $z$-score)

令 $z = \frac{x-\mu}{\sigma}$（離平均幾個標準差），分布變成與單位無關的 $\mathcal{N}(0,1)$：

$$f(z) = \frac{1}{\sqrt{2\pi}}\exp\left(-\frac{z^2}{2}\right)$$

（$dx = \sigma\,dz$，所以分母的 $\sigma$ 消失。）

## 3. 精度形式 (Precision Form)

Gauss 原始推導裡的寫法（見 [02_Gauss_mean_optimal_Gaussian.md](../02_proof/02_Gauss_mean_optimal_Gaussian.md)），用**精度** $h = 1/\sigma^2$ 取代變異數：

$$f(e) = A\,\exp\left(-\frac{h}{2}e^2\right),\qquad h = \frac{1}{\sigma^2},\quad A = \sqrt{\frac{h}{2\pi}}$$

* $e = x - \mu$ : 誤差 (Error)，觀測值偏離真值的量

精度越大越集中。貝氏更新時「精度相加」（見 [06_Gaussian_product_posterior.md](../02_proof/06_Gaussian_product_posterior.md)），用這個寫法最方便。

## 4. 指數二次形式 (Exponential-of-Quadratic Form)

最大熵推導直接得到的形式（見 [01_max_entropy_Gaussian.md](../02_proof/01_max_entropy_Gaussian.md)），三個乘數各對應一條約束：

$$f(x) = \exp\Big(-1 - \lambda_0 - \lambda_1 x - \lambda_2 (x-\mu)^2\Big)$$

* $\lambda_0$ : 對應「機率和為 1」，最後變成正規化常數 $e^{-1-\lambda_0} = \frac{1}{\sigma\sqrt{2\pi}}$
* $\lambda_1$ : 對應「平均為 $\mu$」，最後會得到 $\lambda_1 = 0$
* $\lambda_2$ : 對應「變異數為 $\sigma^2$」，最後會得到 $\lambda_2 = \frac{1}{2\sigma^2}$

代入這三個值就回到第 1 節的標準形式。
若改用偏差 $\mu_i = x - \mu$ 當變數（$x = \mu + \mu_i$），同一式寫成

$$f = \exp\Big(-1 - \lambda_0 - \lambda_1(\mu + \mu_i) - \lambda_2\,\mu_i^2\Big)$$

這就是「$\exp(-1-\lambda_0-\lambda_1(\mu_i+\mu)-\lambda_2\mu_i^2)$」那個寫法的來源。

## 性質速查 (Properties)

| 量 | 值 | 出處 |
|---|---|---|
| 平均 $\mathbb{E}[X]$ | $\mu$ | 對稱性 |
| 變異數 $\mathbb{E}[(X-\mu)^2]$ | $\sigma^2$ | [02_Gaussian_integrals.md](02_Gaussian_integrals.md) |
| 偏度 $a_3$ | $0$ | [05_Gaussian_skewness_kurtosis.md](../02_proof/05_Gaussian_skewness_kurtosis.md) |
| 峰度 $a_4$ | $3$ | [05_Gaussian_skewness_kurtosis.md](../02_proof/05_Gaussian_skewness_kurtosis.md) |
| 熵 $-\int f\ln f\,dx$ | $\frac{1}{2}\ln(2\pi e\sigma^2)$ | [01_max_entropy_Gaussian.md](../02_proof/01_max_entropy_Gaussian.md) |
| $\Pr(\lvert z\rvert \le 1, 2, 3)$ | $68.27\%,\ 95.45\%,\ 99.73\%$ | 查表 |
