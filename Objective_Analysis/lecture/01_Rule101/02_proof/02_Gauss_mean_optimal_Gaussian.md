# 「平均值是最佳估計」推出高斯分布 (Gauss: Optimal Mean Implies Gaussian Errors)

> 十九世紀初的天文學家反覆測量同一顆星星的位置，每次讀數都不一樣，但真實位置 $\mu$ 只有一個。
> 大家早就習慣拿**算術平均** $\bar{x}$ 當最佳估計，卻沒人說得出為什麼不是中位數或別的組合。
> Gauss（*Theoria Motus*, 1809）反過來問：**如果平均值永遠是最佳估計，誤差該服從什麼分布？** 答案是高斯分布。

## 假設與已知 (Assumptions & Preliminaries)

* **【假設 1】誤差模型 (Error Model)：** 每次觀測 = 真值 + 誤差，誤差彼此獨立、來自同一個平滑且處處為正的密度 $f$。

  * (a)

  $$x_i = \mu + e_i,\qquad i = 1,\dots,N$$

  * (b)

  $$e_i \overset{\text{i.i.d.}}{\sim} f(e),\qquad f \in C^1,\ f > 0$$

  * $x_i$ : 第 $i$ 次觀測值 (Observation)
  * $\mu$ : 未知真值 (True value)
  * $e_i$ : 觀測誤差 (Measurement error)
  * $N$ : 觀測次數 (Sample size)
  * $f(e)$ : 誤差的機率密度 (Error PDF)，形狀未知，正是要求的東西
  * $C^1$ : 一階導數存在且連續 (Continuously differentiable)
  * i.i.d. : 獨立同分布 (Independent and identically distributed)

* **【假設 2】Gauss 的要求 (Gauss's Postulate)：** 不論抽到哪一組樣本、樣本數 $N$ 是多少，最大概似估計都恰好是算術平均。

  $$\hat{\mu}_{\text{MLE}} = \bar{x} \overset{\text{def}}{=} \frac{1}{N}\sum_{i=1}^{N} x_i$$

  * $\hat{\mu}_{\text{MLE}}$ : $\mu$ 的最大概似估計 (Maximum likelihood estimate)，由【已知 1】算出的最佳估計
  * $\bar{x}$ : 算術平均 (Sample mean)

* **【定義 1】概似函數 (Likelihood)：** 給定候選真值 $\mu$，觀測到這組資料的機率密度；誤差彼此獨立，所以是各筆密度的乘積。

  $$L(\mu) \overset{\text{def}}{=} \prod_{i=1}^{N} f(x_i - \mu)$$

  * $L(\mu)$ : 概似函數 (Likelihood)，是 $\mu$ 的函數，資料 $x_i$ 視為已知
  * $x_i - \mu$ : 若真值是 $\mu$，第 $i$ 筆觀測的誤差

* **【已知 1】最大概似 (Maximum Likelihood)：** 最佳估計是讓「實際看到這組資料」機率最大的 $\mu$；$\ln$ 單調遞增，最大化 $L$ 等於最大化 $\ln L$，極值處導數為零。

  $$\frac{d}{d\mu}\Big[\ln L(\mu)\Big]_{\mu = \hat{\mu}} = 0$$

  * $\ln L(\mu)$ : 對數概似 (Log-likelihood)，把連乘變成連加，較好微分
  * $\hat{\mu}$ : 使 $L$ 最大的 $\mu$，即【假設 2】的 $\hat{\mu}_{\text{MLE}}$

* **【已知 2】Cauchy 函數方程 (Cauchy's Functional Equation)：** 連續函數若滿足「和的函數值 = 函數值的和」，它只能是過原點的直線。

  $$\varphi(a + b) = \varphi(a) + \varphi(b)\ \ \forall a, b,\ \ \varphi \text{ 連續} \quad \Rightarrow \quad \varphi(e) = k\,e$$

  * $\varphi$ : 任意實函數 (Real function)。本證明要說明【定義 2】的 $\varphi^*$ 滿足這裡的條件（見 proof (b)）
  * $a, b$ : 任意兩個實數
  * $k$ : 直線的斜率，常數

* **【已知 3】[高斯分布的精度形式 (Precision Form)](../01_tool/01_Gaussian_distribution.md)：** 用精度 $h$ 寫的高斯分布；正規化常數與變異數都可由 [高斯積分](../01_tool/02_Gaussian_integrals.md) (a)(b) 算出。

  * (a) 形式

  $$f(e) = A\,e^{-\frac{h}{2}e^2}$$

  * (b) 正規化

  $$\int_{-\infty}^{\infty} f\,de = 1 \quad\text{則}\quad A = \sqrt{\frac{h}{2\pi}}$$

  * (c) 變異數

  $$\int_{-\infty}^{\infty} e^2 f\,de = \frac{1}{h} = \sigma^2$$

  * $A$ : 正規化常數 (Normalization constant)
  * $h$ : 精度 (Precision)，變異數的倒數，越大越集中
  * $\sigma^2$ : 誤差變異數 (Error variance)

* **【定義 2】對數導數 (Log-derivative)：** $\ln f$ 的斜率；Gauss 的要求會直接限制它的形狀。

  $$\begin{gather*}
  \varphi^*(e) &\overset{\text{def}}{=}& \frac{f'(e)}{f(e)} \\
  &=& \frac{d}{de}\Big[\ln f(e)\Big]
  \end{gather*}$$

  * $\varphi^*(e)$ : 誤差密度的對數導數 (Log-derivative of the error PDF)

## proof

(a) 概似方程（對任何 $f$ 都成立，還沒用到高斯）：

$$\begin{gather*}
0 &\overset{\text{已知 1}}{=}& \frac{d}{d\mu}\Big[\ln L(\mu)\Big] \\
0 &\overset{\text{定義 1}}{=}& \frac{d}{d\mu}\Big[\sum_{i=1}^{N}\ln f(x_i - \mu)\Big] \\
0 &\overset{\text{定義 2}}{=}& -\sum_{i=1}^{N}\varphi^*(x_i - \mu)
\end{gather*}$$

(b) 證明 $\varphi^*$ 滿足 Cauchy 方程，也就是 $\varphi^*$ 可以當作【已知 2】的 $\varphi$：

* (b-1) 由【假設 2】，$\mu = \bar{x}$ 必須是 (a) 的解。令偏差 $d_i = x_i - \bar{x}$，它們的和恆為 $0$，而且任何和為 $0$ 的一組 $d_i$ 都可能被抽到：

  $$\sum_{i=1}^{N} d_i = 0 \quad\text{則}\quad \sum_{i=1}^{N}\varphi^*(d_i) = 0$$

* (b-2) 取 $N = 2$、$d_1 = d$、$d_2 = -d$，得 $\varphi^*$ 是奇函數：

  $$\begin{gather*}
  \varphi^*(d) + \varphi^*(-d) &\overset{\text{(b-1)}}{=}& 0 \\
  \varphi^*(-d) &=& -\varphi^*(d)
  \end{gather*}$$

* (b-3) 取 $N = 3$、$d_3 = -(d_1 + d_2)$，得可加性：

  $$\begin{gather*}
  0 &\overset{\text{(b-1)}}{=}& \varphi^*(d_1) + \varphi^*(d_2) + \varphi^*\big(-(d_1 + d_2)\big) \\
  0 &\overset{\text{(b-2)}}{=}& \varphi^*(d_1) + \varphi^*(d_2) - \varphi^*(d_1 + d_2) \\
  \varphi^*(d_1 + d_2) &=& \varphi^*(d_1) + \varphi^*(d_2)
  \end{gather*}$$

(c) $f \in C^1$ 且 $f > 0$，所以 $\varphi^*$ 連續，加上 (b) 就能用 Cauchy 方程。記 $k = -h$，$h > 0$ 才能讓 $f$ 往兩側衰減而不是爆掉：

$$\begin{gather*}
\varphi^*(e) &\overset{\text{(b)}}{=}& \varphi(e) \\
\varphi^*(e) &\overset{\text{已知 2,假設 1(b)}}{=}& k\,e \\
\varphi^*(e) &=& -h\,e \\
\frac{d}{de}\Big[\ln f(e)\Big] &\overset{\text{定義 2}}{=}& -h\,e \\
\ln f(e) &=& -\frac{h}{2}e^2 + c \\
f(e) &=& A\,\exp\left(-\frac{h}{2}e^2\right) \\
f(x - \mu) &\overset{\text{已知 3(a)(b)(c)}}{=}& \frac{1}{\sigma\sqrt{2\pi}}\exp\left(-\frac{(x-\mu)^2}{2\sigma^2}\right)
\end{gather*}$$

$\blacksquare$

## 結論

「算術平均是最佳估計」這**一個**要求，就把誤差分布逼成高斯分布。
這與 [01_max_entropy_Gaussian.md](01_max_entropy_Gaussian.md) 的「已知 $\mu, \sigma^2$ 下最大熵」是兩個毫不相干的原則，卻得到同一條曲線，這正是高斯分布在統計中地位特殊的原因。

> 歷史註記：de Moivre（1733）更早從二項分布的極限得到同一條曲線，那是中央極限定理的前身；Laplace 後來把兩條路線統一。（見 [99_textbook.md](../99_textbook.md) "A note on priority"。）
