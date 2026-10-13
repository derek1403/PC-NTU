# 樣本變異數為什麼除以 $N-1$ (Why the Sample Variance Divides by $N-1$)

算樣本變異數時必須先用同一批資料算出 $\bar{X}$，而 $\bar{X}$ 天生離這批資料最近，所以 $\sum(X_i - \bar{X})^2$ 會系統性地偏小。
平均起來它只等於 $(N-1)\sigma^2$，除以 $N-1$ 才能得到不偏的估計。（大小寫分工見 [03_notation_X_vs_x.md](../03_notation_X_vs_x.md)。）

## 假設與已知 (Assumptions & Preliminaries)

* **【假設 1】獨立同分布 (i.i.d.)：** 同 [03_standard_error.md](03_standard_error.md)【假設 1】。

  * (a)

  $$\mathbb{E}[X_i] = \mu$$

  * (b)

  $$\mathrm{Var}(X_i) = \sigma^2$$

  * (c)

  $$X_i,\ X_j \text{ 兩兩獨立}\quad (i \neq j)$$

  * $X_i$ : 第 $i$ 筆觀測的隨機變數 (Random variable of the $i$-th observation)，$i = 1,\dots,N$
  * $\mu, \sigma^2$ : 母體平均與變異數 (Population mean & variance)

* **【定義 1】樣本平均與樣本變異數 (Sample Mean & Sample Variance)：** 兩者都是隨機變數；手上資料算出的值分別記為 $\bar{x}$、$s^2$。

  * (a)

  $$\bar{X} \overset{\text{def}}{=} \frac{1}{N}\sum_{i=1}^{N} X_i$$

  * (b)

  $$S^2 \overset{\text{def}}{=} \frac{1}{N-1}\sum_{i=1}^{N}(X_i - \bar{X})^2$$

  * $\bar{X}$ : 樣本平均隨機變數 (Sample mean)
  * $S^2$ : 樣本變異數隨機變數 (Sample variance)

* **【已知 1】[變異數的另一種寫法 (Variance Shortcut)](../01_tool/03_expectation_rules.md)：** 平方的期望值 = 變異數 + 平均的平方。（tool 03 (c) 移項。）

  $$\mathbb{E}[Y^2] = \mathrm{Var}(Y) + \big(\mathbb{E}[Y]\big)^2$$

  * $Y$ : 任意隨機變數 (Random variable)，本證明中取 $X_i$ 或 $\bar{X}$

* **【已知 2】[標準誤 (Standard Error)](03_standard_error.md)：** 樣本平均不偏，變異數是單筆的 $1/N$。

  * (a)

  $$\mathbb{E}[\bar{X}] = \mu$$

  * (b)

  $$\mathrm{Var}(\bar{X}) = \frac{\sigma^2}{N}$$

* **【已知 3】[期望值線性 (Linearity of Expectation)](../01_tool/03_expectation_rules.md)：** 常數可以提出來，和的期望值等於期望值的和（不需獨立）。

  $$\mathbb{E}\Big[\sum_i a_i Y_i\Big] = \sum_i a_i\,\mathbb{E}[Y_i]$$

  * $a_i$ : 任意常數 (Constants)
  * $Y_i$ : 任意隨機變數 (Random variables)

* **【推導 1】離差平方和的展開 (Sum of Squared Deviations)：** 把平方拆開，交叉項剛好用 $\sum X_i = N\bar{X}$ 化掉。

  $$\begin{gather*}
  \sum_i (X_i - \bar{X})^2 &=& \sum_i X_i^2 - 2\bar{X}\sum_i X_i + N\bar{X}^2 \\
  &\overset{\text{定義 1(a)}}{=}& \sum_i X_i^2 - 2N\bar{X}^2 + N\bar{X}^2 \\
  &=& \sum_i X_i^2 - N\bar{X}^2
  \end{gather*}$$

* **【推導 2】兩個平方項的期望值 (Expected Squares)：** 單筆觀測的平方比平均的平方多了整整 $\sigma^2$ 的散布，而平均的平方只多 $\sigma^2/N$。

  * (a) 單筆

  $$\mathbb{E}[X_i^2] \overset{\text{已知 1,假設 1(a)(b)}}{=} \sigma^2 + \mu^2$$

  * (b) 樣本平均

  $$\mathbb{E}[\bar{X}^2] \overset{\text{已知 1,2(a)(b)}}{=} \frac{\sigma^2}{N} + \mu^2$$

## proof

$$\begin{gather*}
\mathbb{E}\Big[\sum_i (X_i - \bar{X})^2\Big] &\overset{\text{推導 1}}{=}& \mathbb{E}\Big[\sum_i X_i^2 - N\bar{X}^2\Big] \\
\mathbb{E}\Big[\sum_i (X_i - \bar{X})^2\Big] &\overset{\text{已知 3}}{=}& \sum_i \mathbb{E}[X_i^2] - N\,\mathbb{E}[\bar{X}^2] \\
\mathbb{E}\Big[\sum_i (X_i - \bar{X})^2\Big] &\overset{\text{推導 2(a)(b)}}{=}& N(\sigma^2 + \mu^2) - N\Big(\frac{\sigma^2}{N} + \mu^2\Big) \\
\mathbb{E}\Big[\sum_i (X_i - \bar{X})^2\Big] &=& (N - 1)\,\sigma^2 \\
\mathbb{E}[S^2] &\overset{\text{定義 1(b),已知 3}}{=}& \sigma^2
\end{gather*}$$

$\blacksquare$

## 結論

$$\boxed{S^2 = \frac{1}{N-1}\sum_{i=1}^{N}(X_i - \bar{X})^2 \quad\text{滿足}\quad \mathbb{E}[S^2] = \sigma^2}$$

實際計算時代入資料，得到的是它的一個實現值 $s^2 = \frac{1}{N-1}\sum(x_i - \bar{x})^2$。
少掉的那一個 $\sigma^2$，正是【推導 2(b)】裡的 $N\cdot\frac{\sigma^2}{N}$：用 $\bar{X}$ 代替真值 $\mu$ 所付的代價，也就是教科書說的「損失一個自由度」。
（教科書把 $\frac{1}{N}\sum(x_i-\bar{x})^2$ 拆成 $(x_i-\mu)$ 與 $(\bar{x}-\mu)$ 兩項，第二項就是這個偏差。）
