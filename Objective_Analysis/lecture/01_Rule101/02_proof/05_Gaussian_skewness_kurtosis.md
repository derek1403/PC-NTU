# 高斯分布的偏度為 0、峰度為 3 (Skewness and Kurtosis of the Gaussian)

偏度量度左右是否對稱，峰度量度尾巴有多厚。高斯分布的這兩個值（$0$ 與 $3$）是判斷資料「像不像高斯」的標準尺。

## 假設與已知 (Assumptions & Preliminaries)

* **【定義 1】中心動差與無因次化 (Central Moments, Standardized)：** $r$ 階中心動差是「離平均的 $r$ 次方」的期望值；除以 $\sigma^r$ 讓它與單位無關，才能跨變數比較。

  * (a)

  $$m_r \overset{\text{def}}{=} \mathbb{E}\big[(X-\mu)^r\big] = \int_{-\infty}^{\infty} (x-\mu)^r f(x)\,dx$$

  * (b)

  $$a_r \overset{\text{def}}{=} \frac{m_r}{\sigma^r}$$

  * $r$ : 動差階數 (Order)
  * $m_r$ : $r$ 階中心動差 (Central moment)
  * $a_r$ : 無因次化動差 (Standardized moment)；$a_3$ 為偏度 (Skewness)，$a_4$ 為峰度 (Kurtosis)
  * $f(x)$ : 機率密度 (PDF)

* **【已知 1】[高斯分布 (Gaussian Distribution)](../01_tool/01_Gaussian_distribution.md)：**

  $$f(x) = \frac{1}{\sigma\sqrt{2\pi}}\exp\left(-\frac{(x-\mu)^2}{2\sigma^2}\right)$$

  * $\mu$ : 平均 (Mean)
  * $\sigma$ : 標準差 (Standard deviation)

* **【已知 2】[高斯積分 (Gaussian Integrals)](../01_tool/02_Gaussian_integrals.md)：** 把中心平移到 $\mu$（tool 02 (e)），本證明取 $a = \frac{1}{2\sigma^2}$。

  * (a) 奇次方

  $$\int_{-\infty}^{\infty} (x-\mu)^{2k+1} \exp\Big(-a(x-\mu)^2\Big)\,dx = 0$$

  * (b) 四次方

  $$\int_{-\infty}^{\infty} (x-\mu)^4 \exp\Big(-a(x-\mu)^2\Big)\,dx = \frac{3\sqrt{\pi}}{4}\,a^{-5/2}$$

  * $a$ : 任意正常數 (Positive constant)
  * $k$ : 非負整數 (Non-negative integer)

## proof

### (a) 偏度：被積函數對 $\mu$ 是奇函數，左右抵消

$$\begin{gather*}
a_3 &\overset{\text{定義 1(b)}}{=}& \frac{m_3}{\sigma^3} \\
&\overset{\text{定義 1(a),已知 1}}{=}& \frac{1}{\sigma^3}\cdot\frac{1}{\sigma\sqrt{2\pi}}\int (x-\mu)^3 \exp\left(-\frac{(x-\mu)^2}{2\sigma^2}\right)dx \\
&\overset{\text{已知 2(a)}}{=}& 0
\end{gather*}$$

### (b) 峰度

$$\begin{gather*}
a_4 &\overset{\text{定義 1(b)}}{=}& \frac{m_4}{\sigma^4} \\
&\overset{\text{定義 1(a),已知 1}}{=}& \frac{1}{\sigma^4}\cdot\frac{1}{\sigma\sqrt{2\pi}}\int (x-\mu)^4 \exp\left(-\frac{(x-\mu)^2}{2\sigma^2}\right)dx \\
&\overset{\text{已知 2(b)}}{=}& \frac{1}{\sigma^5\sqrt{2\pi}}\cdot\frac{3\sqrt{\pi}}{4}\,(2\sigma^2)^{5/2} \\
&=& \frac{1}{\sigma^5\sqrt{2\pi}}\cdot\frac{3\sqrt{\pi}}{4}\cdot 4\sqrt{2}\,\sigma^5 \\
&=& 3
\end{gather*}$$

$\blacksquare$

## 結論

$$\boxed{a_3 = 0,\qquad a_4 = 3}$$

實務上常用**超額峰度** $a_4 - 3$：大於 $0$ 代表比高斯更尖、尾巴更厚（極端值較多，例如降雨）；小於 $0$ 代表較平。
