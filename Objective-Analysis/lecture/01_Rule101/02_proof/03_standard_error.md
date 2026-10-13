# 樣本平均的標準誤 (Standard Error of the Sample Mean)

把 $N$ 筆獨立觀測取平均，平均值仍以真值 $\mu$ 為中心（不偏），但它的散布只剩單筆的 $1/\sqrt{N}$。這是 $z$／$t$ 檢定與信賴區間的基礎。

## 假設與已知 (Assumptions & Preliminaries)

* **【假設 1】獨立同分布 (i.i.d.)：** $N$ 筆觀測彼此獨立，且來自同一個平均 $\mu$、變異數 $\sigma^2$ 的母體（**不需要**是高斯）。

  * (a)

  $$\mathbb{E}[X_i] = \mu$$

  * (b)

  $$\mathrm{Var}(X_i) = \sigma^2$$

  * (c)

  $$X_i,\ X_j \text{ 兩兩獨立}\quad (i \neq j)$$

  * $X_i$ : 第 $i$ 筆觀測的隨機變數 (Random variable of the $i$-th observation)，$i = 1,\dots,N$
  * $N$ : 樣本數 (Sample size)
  * $\mu$ : 母體平均 (Population mean)
  * $\sigma^2$ : 母體變異數 (Population variance)

* **【定義 1】樣本平均 (Sample Mean)：** $N$ 筆觀測的算術平均，本身也是一個隨機變數（換一批資料就換一個值），所以用大寫。（大小寫分工見 [03_notation_X_vs_x.md](../03_notation_X_vs_x.md)。）

  $$\bar{X} \overset{\text{def}}{=} \frac{1}{N}\sum_{i=1}^{N} X_i$$

  * $\bar{X}$ : 樣本平均隨機變數 (Sample mean)；手上這批資料算出的值記為 $\bar{x}$

* **【已知 1】[期望值與變異數的運算規則 (Rules for Expectation and Variance)](../01_tool/03_expectation_rules.md)：** 期望值是線性的；變異數在縮放時變平方倍，而對獨立變數可直接相加。

  * (a)

  $$\mathbb{E}[aX] = a\,\mathbb{E}[X]$$

  * (b)

  $$\mathbb{E}\Big[\sum_i X_i\Big] = \sum_i \mathbb{E}[X_i]$$

  * (c)

  $$\mathrm{Var}(aX) = a^2\,\mathrm{Var}(X)$$

  * (d)

  $$\mathrm{Var}\Big(\sum_i X_i\Big) = \sum_i \mathrm{Var}(X_i) \quad (\text{兩兩獨立時})$$

  * $a$ : 任意常數 (Constant)
  * $X, X_i$ : 任意隨機變數 (Random variables)

## proof

### (a) 樣本平均不偏

$$\begin{gather*}
\mathbb{E}[\bar{X}] &\overset{\text{定義 1}}{=}& \mathbb{E}\Big[\frac{1}{N}\sum_{i} X_i\Big] \\
&\overset{\text{已知 1(a)(b)}}{=}& \frac{1}{N}\sum_{i}\mathbb{E}[X_i] \\
&\overset{\text{假設 1(a)}}{=}& \frac{1}{N}\cdot N\mu \\
&=& \mu
\end{gather*}$$

### (b) 樣本平均的變異數與標準誤

$$\begin{gather*}
\mathrm{Var}(\bar{X}) &\overset{\text{定義 1}}{=}& \mathrm{Var}\Big(\frac{1}{N}\sum_{i} X_i\Big) \\
\mathrm{Var}(\bar{X}) &\overset{\text{已知 1(c)}}{=}& \frac{1}{N^2}\,\mathrm{Var}\Big(\sum_{i} X_i\Big) \\
\mathrm{Var}(\bar{X}) &\overset{\text{已知 1(d),假設 1(b)(c)}}{=}& \frac{1}{N^2}\cdot N\sigma^2 \\
\mathrm{Var}(\bar{X}) &=& \frac{\sigma^2}{N} \\
\sigma_{\bar{X}} &=& \frac{\sigma}{\sqrt{N}}
\end{gather*}$$

（標準誤 $\sigma_{\bar{X}}$ 就是 $\mathrm{Var}(\bar{X})$ 的平方根。）$\blacksquare$

## 結論

$$\boxed{\mathbb{E}[\bar{X}] = \mu,\qquad \sigma_{\bar{X}} = \frac{\sigma}{\sqrt{N}}}$$

資料量變成 4 倍，平均的不確定度只減半。
**獨立**是關鍵：大氣時間序列常有自相關，相鄰資料不獨立，有效樣本數 $N_{\text{eff}} < N$，直接用 $\sigma/\sqrt{N}$ 會高估精確度。
