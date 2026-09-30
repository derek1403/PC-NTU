# 已知平均與變異數時，最大熵分布是高斯分布 (Maximum Entropy with Known Mean and Variance)

只知道平均 $\mu$ 與變異數 $\sigma^2$ 時，「除此之外不多做任何假設」的分布（熵最大的分布）就是高斯分布 $\mathcal{N}(\mu,\sigma^2)$。

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】[多約束 Lagrange 條件 (Lagrange Condition)](../../00_Chapter0/01_tool/01_Lagrange_multiplier/02_advanced_use.md)：** 每條約束配一個乘數，極值點必使 Lagrangian 對所有變數的偏導數同時為零。

  $$\mathcal{L} = S - \sum_{n}\lambda_n\big(g_n - c_n\big),\qquad \frac{\partial \mathcal{L}}{\partial p_i} = 0$$

  * $S$ : 要最大化的目標函數 (Objective)。本證明中是離散化後的熵 $S = -\sum_i p_i\ln p_i$（見【推導 1】）
  * $p_i$ : 未知數，第 $i$ 格的機率 (Probability of bin $i$)，每一個 $p_i$ 都是一個獨立的變數
  * $g_n = c_n$ : 第 $n$ 條約束 (Constraint)。本證明有三條：總機率、平均、變異數（見【推導 1(b)】）
  * $\lambda_n$ : 第 $n$ 條約束的乘數 (Lagrange multiplier)，本證明記為 $\lambda_0, \lambda_1, \lambda_2$
  * $\mathcal{L}$ : Lagrangian，把目標與約束合成一個函數

* **【已知 2】[高斯積分 (Gaussian Integrals)](../01_tool/02_Gaussian_integrals.md)：** 本證明用到其中三條（$a > 0$）。

  * (a) 
  
  $$\int_{-\infty}^{\infty} e^{-a(x-m)^2}\,dx = \sqrt{\frac{\pi}{a}}$$

  * (b) 
  
  $$\int_{-\infty}^{\infty} (x-m)^2 e^{-a(x-m)^2}\,dx = \frac{\sqrt{\pi}}{2}\,a^{-3/2}$$

  * (c) 
  
  $$\int_{-\infty}^{\infty} (x-m)\,e^{-a(x-m)^2}\,dx = 0$$

* **【定義 1】[資訊熵 (Information Entropy)](../00_Rule101.md)：** 資訊量 $-\ln f$ 的期望值，量度分布「有多不確定」；熵越大，代表分布越沒有偏好、隱含的假設越少。

  $$H[f] \overset{\text{def}}{=} -\int_{-\infty}^{\infty} f(x)\ln f(x)\,dx$$

* **【假設 1】已知的三件事 (Constraints)：** 我們只知道 $f$ 是機率密度、平均是 $\mu$、變異數是 $\sigma^2$，除此之外一無所知。

  (a) $$\int_{-\infty}^{\infty} f\,dx = 1$$

  (b) $$\int_{-\infty}^{\infty} x\,f\,dx = \mu$$

  (c) $$\int_{-\infty}^{\infty} (x-\mu)^2 f\,dx = \sigma^2$$

* **【定義 2】離散化 (Discretization)：** 把實數軸切成寬 $\Delta x$ 的小格，第 $i$ 格的機率記為 $p_i$。未知數從「一整個函數 $f$」變成「有限多個數 $p_i$」，就能直接用【已知 1】。

  $$p_i \overset{\text{def}}{=} f(x_i)\,\Delta x$$

* **【推導 1】離散後的熵與約束 (Discretized Entropy & Constraints)：** 積分換成黎曼和。熵只多出一個常數 $\ln\Delta x$，不影響「誰最大」，所以只需要最大化 $S = -\sum_i p_i\ln p_i$。

  * (a) 
  
  $$\begin{gather*}
  H &\overset{\text{定義 1}}{=}& -\int_{-\infty}^{\infty} f(x)\ln f(x)\,dx \\
  &\approx& -\sum_i f(x_i)\ln f(x_i)\,\Delta x \\
  &\overset{\text{定義 2}}{=}& -\sum_i p_i \ln\frac{p_i}{\Delta x} \\
  &=& -\sum_i \Big( p_i (\ln p_i - \ln \Delta x) \Big)\\
  &=& -\sum_i \Big( p_i \ln p_i\Big) + \sum_i \Big(p_i \ln \Delta x \Big)\\
  &\overset{\text{假設 1(a)}}{=}& -\sum_i \Big( p_i\ln p_i \Big)+ 1 \cdot \ln\Delta x
  \end{gather*}$$

  * (b) 
  
  $$\sum_i p_i = 1,\qquad \sum_i x_i\,p_i = \mu,\qquad \sum_i (x_i - \mu)^2 p_i = \sigma^2$$


* **【推導 2】熵項、總機率項：** 

  * (a) 熵項

  $$\begin{gather*}
  \frac{\partial}{\partial p_i}\Big[-\sum_j p_j\ln p_j\Big] &=& -\frac{\partial}{\partial p_i}\Big[p_i\ln p_i\Big] \\
  &=& -\Big(\ln p_i + p_i\cdot\frac{1}{p_i}\Big) \\
  &=& -\ln p_i - 1
  \end{gather*}$$

  * (b) 總機率項

  $$\frac{\partial}{\partial p_i}\Big[\lambda_0\Big(\sum_j p_j - 1\Big)\Big] = \lambda_0$$

  * (c) 平均項

  $$\frac{\partial}{\partial p_i}\Big[\lambda_1\Big(\sum_j x_j\,p_j - \mu\Big)\Big] = \lambda_1 x_i$$

  * (d) 變異數項

  $$\frac{\partial}{\partial p_i}\Big[\lambda_2\Big(\sum_j (x_j - \mu)^2 p_j - \sigma^2\Big)\Big] = \lambda_2 (x_i - \mu)^2$$


## proof

### (a) 離散問題：用 Lagrange 解出 $p_i$ 的形狀

$$\begin{gather*}
0 &\overset{\text{已知 1}}{=}& \frac{\partial}{\partial p_i}\Big[ \mathcal{L} \Big] \\
0 &\overset{\text{已知 1}}{=}& \frac{\partial}{\partial p_i}\Big[ S - \lambda_0\Big(\sum_j p_j - 1\Big) - \lambda_1\Big(\sum_j x_j\,p_j - \mu\Big) - \lambda_2\Big(\sum_j (x_j - \mu)^2 p_j - \sigma^2\Big) \Big]  \\
0 &\overset{\text{推導 1}}{=}&  \frac{\partial}{\partial p_i}\Big[ -\sum_j p_j\ln p_j - \lambda_0\Big(\sum_j p_j - 1\Big) - \lambda_1\Big(\sum_j x_j\,p_j - \mu\Big) - \lambda_2\Big(\sum_j (x_j - \mu)^2 p_j - \sigma^2\Big) \Big] \\
0 &\overset{\text{推導 2(a)(b)(c)(d)}}{=}&  (-\ln p_i - 1) - \lambda_0 - \lambda_1 x_i - \lambda_2 (x_i - \mu)^2 \\
\ln p_i &=& -1 - \lambda_0 - \lambda_1 x_i - \lambda_2 (x_i - \mu)^2 \\
p_i &=& \exp\Big(-1 - \lambda_0 - \lambda_1 x_i - \lambda_2 (x_i - \mu)^2\Big)
\end{gather*}$$



（與 [Q17 三能階最大熵](../../00_Chapter0/01_tool/01_Lagrange_multiplier/05_problems/Q17_three_level_negative_temperature.md) 完全同一結構，只是約束從「平均能量」換成「平均與變異數」。）

### (b) 回到連續，用三條約束定出乘數並代回

* (b-1) 回到連續：$\Delta x \to 0$，把 $\ln\Delta x$ 併進常數 $\lambda_0' = \lambda_0 + \ln\Delta x$：

  $$\begin{gather*}
  f(x_i)\,\Delta x &\overset{\text{定義 2}}{=}& p_i  \\
  f(x)\,\Delta x &\overset{\text{(a)}}{=}& \exp\Big(-1 - \lambda_0 - \lambda_1 x - \lambda_2 (x - \mu)^2\Big) \\
  f(x) &=&\frac{1}{\Delta x} \exp\Big(-1 - \lambda_0 - \lambda_1 x - \lambda_2 (x - \mu)^2\Big) \\
  f(x) &\overset{\text{配方法}}{=}& \frac{e^{-1-\lambda_0}}{\Delta x}\exp\Big(-\lambda_2\big[(x-\mu)^2 + \tfrac{\lambda_1}{\lambda_2}(x-\mu)\big] - \lambda_1\mu\Big) \\ 
  f(x) &=& \underbrace{\frac{e^{-1-\lambda_0-\lambda_1\mu + \frac{\lambda_1^2}{4\lambda_2}}}{\Delta x}}_{\text{與 } x \text{ 無關的常數，打包為 } C} \exp\Bigg(-\lambda_2\,\Big(x - \underbrace{\big(\mu - \tfrac{\lambda_1}{2\lambda_2}\big)}_{\text{對稱中心，記為 } m}\Big)^2\Bigg) \\ 
  f(x) &=& C\,\exp\Big(-\lambda_2\,(x - m)^2\Big) 
  \end{gather*}$$

  $f$ 要能積分成 $1$，必須 $\lambda_2 > 0$。

* (b-2) 平均約束決定中心，得 $\lambda_1 = 0$：

  $$\begin{gather*}
  \mu &\overset{\text{假設 1(b)}}{=}& \int x\,f\,dx \\
  \mu &=& \int (x - m)\,f\,dx + m\int f\,dx \\
  \mu &\overset{\text{已知 2(c),假設 1(a)}}{=}& 0 + m \\
  \lambda_1 &\overset{\text{(b-1)}}{=}& 0
  \end{gather*}$$

* (b-3) 正規化決定 $C$：

  $$\begin{gather*}
  1 &\overset{\text{假設 1(a)}}{=}& C\int e^{-\lambda_2(x-\mu)^2}\,dx \\
  1 &\overset{\text{已知 2(a)}}{=}& C\sqrt{\frac{\pi}{\lambda_2}} \\
  C &=& \sqrt{\frac{\lambda_2}{\pi}}
  \end{gather*}$$

* (b-4) 變異數約束決定 $\lambda_2$：

  $$\begin{gather*}
  \sigma^2 &\overset{\text{假設 1(c)}}{=}& C\int (x-\mu)^2 e^{-\lambda_2(x-\mu)^2}\,dx \\
  \sigma^2 &\overset{\text{已知 2(b),(b-3)}}{=}& \sqrt{\frac{\lambda_2}{\pi}}\cdot\frac{\sqrt{\pi}}{2}\,\lambda_2^{-3/2} \\
  \sigma^2 &=& \frac{1}{2\lambda_2} \\
  \lambda_2 &=& \frac{1}{2\sigma^2}
  \end{gather*}$$

* (b-5) 代回，得到高斯分布：

  $$\begin{gather*}
  f(x) &\overset{\text{(b-1)}}{=}& C\,\exp\Big(-\lambda_2\,(x - m)^2\Big) \\
  f(x) &\overset{\text{(b-2)(b-3)(b-4)}}{=}& \sqrt{\frac{1}{2\pi\sigma^2}}\exp\left(-\frac{(x-\mu)^2}{2\sigma^2}\right)
  \end{gather*}$$

### (c) 該分布是最大熵

$-p\ln p$ 的二階導數 $-1/p < 0$，所以 $S$ 是凹函數；約束全是線性的，凹函數在線性約束上的駐點就是唯一的全域最大值。$\blacksquare$

## 結論

$$\boxed{\text{已知 } \mu,\ \sigma^2 \text{ 且不多做假設} \quad\text{得}\quad f = \mathcal{N}(\mu, \sigma^2)}$$

最大的熵值是 $H = \frac{1}{2}\ln(2\pi e\,\sigma^2)$：同樣的變異數下，任何其他分布的熵都比它小，也就是都「偷偷多假設了什麼」。
高斯分布也可以從完全不同的原則推出來，見 [02_Gauss_mean_optimal_Gaussian.md](02_Gauss_mean_optimal_Gaussian.md)。
