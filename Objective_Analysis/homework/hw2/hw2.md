# Objective Analysis Week 02 Homework

## Question 1. Maximum-Entropy Distributions

Let $X$ be a continuous random variable with probability density function (PDF) $p(x)$. Its differential entropy is

$$S[p] = -\int_{\mathcal{X}} p(x) \ln p(x) \, dx,$$

where $\mathcal{X}$ is the domain of $X$. Use natural logarithms and require $p(x) \geq 0$ throughout this question.

Consider the following two separate maximization problems.

* (a) Normalization on a finite interval

    Suppose $X$ is restricted to a fixed interval $[a, b]$, where $a < b$. In addition to nonnegativity, the only constraint is

    $$\int_{a}^{b} p(x) \, dx = 1.$$

    Use a Lagrange multiplier to find the PDF that maximizes the differential entropy. Identify the resulting distribution.

* (b) Fixed mean and variance on the real line

    Now let $X$ take values over the entire real line, rather than on the finite interval in part (a). Require the PDF to satisfy

    $$\int_{-\infty}^{\infty} p(x) \, dx = 1,$$

    $$\int_{-\infty}^{\infty} x p(x) \, dx = \mu_x,$$

    $$\int_{-\infty}^{\infty} (x - \mu_x)^2 p(x) \, dx = \sigma_x^2,$$

    where $\mu_x$ is the prescribed mean and $\sigma_x^2 > 0$ is the prescribed variance.

    Use Lagrange multipliers to show that the entropy-maximizing PDF is a Gaussian distribution with mean $\mu_x$ and variance $\sigma_x^2$. Write the normalized PDF explicitly.

* **For both parts：** Show how you obtain the stationary PDF and briefly explain why it maximizes the entropy.

* **Hint：** Construct a constrained functional and set its first variation with respect to $p$ equal to zero. You may use the fact that entropy is strictly concave in $p$, so a stationary solution subject to these linear constraints is a global maximum.


## Answer 1

### (a)

$$\mathcal{L}[p] = -\int_{a}^{b} p(x) \ln p(x) \, dx - \lambda_0 \left( \int_{a}^{b} p(x) \, dx - 1 \right)$$



$$\begin{aligned}
0 &= \dfrac{\partial \mathcal{L}}{\partial p} \\
0 &= \dfrac{\partial }{\partial p} \left[ -\int_{a}^{b} p(x) \ln p(x) \, dx - \lambda_0 \left( \int_{a}^{b} p(x) \, dx - 1 \right) \right] \\
0 &= \frac{\partial}{\partial p} \big[ -p(x) \ln p(x) - \lambda_0 p(x) \big] \\
0 &= -\ln p(x) - 1 - \lambda_0 \\
\ln p(x) &=  -(1 + \lambda_0) \\
p(x) &= e^{-(1 + \lambda_0)} \\
\end{aligned}$$


$$\begin{aligned}
1 &= \int_{a}^{b} p(x) \, dx \\
1 &= \int_{a}^{b} e^{-(1 + \lambda_0)} \, dx \\
1 &= (b-a) e^{-(1 + \lambda_0)}  \\
e^{-(1 + \lambda_0)} &= \frac{1}{b-a} \\
p(x) &= \begin{cases} 
\frac{1}{b - a}&, & a \le x \le b \\
0 &, & \text{otherwise} \end{cases} 
\end{aligned}$$


* 駐點解能最大化熵
  
  因為函數 $g(p) = -p \ln p$ 的二階導數為 $g''(p) = -\frac{1}{p} < 0$（當 $p > 0$），這表示微分熵泛函 $S[p]$ 對於 $p$ 是嚴格凹函數（strictly concave）。此外，正規化條件是關於 $p$ 的線性約束（linear constraint），因此在線性約束下求得的駐點解（stationary solution）必然是唯一的全域最大值（global maximum）

### (b)

$$\mathcal{L}[p] = -\int_{-\infty}^{\infty} p(x) \ln p(x) \, dx 
- \lambda_0 \left( \int_{-\infty}^{\infty} p(x) \, dx - 1 \right) 
- \lambda_1 \left( \int_{-\infty}^{\infty} x \, p(x) \, dx - \mu_x \right) 
- \lambda_2 \left( \int_{-\infty}^{\infty} (x - \mu_x)^2 p(x) \, dx 
- \sigma_x^2 \right)$$



* 中間的 $x$ 改寫為 $(x - \mu_x) + \mu_x$，並將常數項合併為 $A = e^{-(1 + \lambda_0 + \lambda_1 \mu_x)}$
* 為了使 $p(x)$ 在 $(-\infty, \infty)$ 上可積分，必須要求 $\lambda_2 > 0$
* $B = A e^{\frac{\lambda_1^2}{4\lambda_2}} > 0$

$$\begin{aligned}
0 &= \dfrac{\partial \mathcal{L}}{\partial p} \\
0 &= \dfrac{\partial }{\partial p} \left[ -\int_{-\infty}^{\infty} p(x) \ln p(x) \, dx 
- \lambda_0 \left( \int_{-\infty}^{\infty} p(x) \, dx - 1 \right) 
- \lambda_1 \left( \int_{-\infty}^{\infty} x \, p(x) \, dx - \mu_x \right) 
- \lambda_2 \left( \int_{-\infty}^{\infty} (x - \mu_x)^2 p(x) \, dx 
- \sigma_x^2 \right) \right] \\
0 &= -\ln p(x) - 1 - \lambda_0 - \lambda_1 x - \lambda_2 (x - \mu_x)^2 \\
\ln p(x) &= -(1 + \lambda_0) - \lambda_1 x - \lambda_2 (x - \mu_x)^2 \\
p(x) &= A \exp\Big( -\lambda_1 (x - \mu_x) - \lambda_2 (x - \mu_x)^2 \Big) \\
\end{aligned}$$


$$\begin{aligned}
p(u) = B \exp\left[ -\lambda_2 \left( u + \frac{\lambda_1}{2\lambda_2} \right)^2 \right]
\end{aligned}$$




* 推導  $w = u + \frac{\lambda_1}{2\lambda_2}$

$$\begin{aligned}
0 &= \dfrac{\partial \mathcal{L}}{\partial \lambda_1} \\
0 &= \dfrac{\partial }{\partial p} \left[ -\int_{-\infty}^{\infty} p(x) \ln p(x) \, dx 
- \lambda_0 \left( \int_{-\infty}^{\infty} p(x) \, dx - 1 \right) 
- \lambda_1 \left( \int_{-\infty}^{\infty} x \, p(x) \, dx - \mu_x \right) 
- \lambda_2 \left( \int_{-\infty}^{\infty} (x - \mu_x)^2 p(x) \, dx 
- \sigma_x^2 \right) \right] \\
0 &= \int_{-\infty}^{\infty} x \, p(x) \, dx - \mu_x  \\
0 &= \int_{-\infty}^{\infty} x \, p(x) \, dx - \mu_x  \int_{-\infty}^{\infty} \, p(x) \, dx \\
0 &= \int_{-\infty}^{\infty} (x - \mu_x) p(x) \, dx \\
0 &= B \int_{-\infty}^{\infty} u \exp\left[ -\lambda_2 \left( u + \frac{\lambda_1}{2\lambda_2} \right)^2 \right] \, du \\
0 &= B \int_{-\infty}^{\infty} \left( w - \frac{\lambda_1}{2\lambda_2} \right) e^{-\lambda_2 w^2} \, dw \\
0 &= B \left( 0 - \frac{\lambda_1}{2\lambda_2} \sqrt{\frac{\pi}{\lambda_2}} \right) \\
0 &= \lambda_1 \\
\end{aligned}$$


$$p(x) = A e^{-\lambda_2 (x - \mu_x)^2}$$



* 推導
* $\int_{-\infty}^{\infty} e^{-\lambda_2 u^2} du = \sqrt{\frac{\pi}{\lambda_2}}$

$$\begin{aligned}
\int_{-\infty}^{\infty} p(x) \, dx &= 1 \\
\int_{-\infty}^{\infty} A e^{-\lambda_2 (x - \mu_x)^2} \, dx &= 1 \\
A \sqrt{\frac{\pi}{\lambda_2}}&= 1 \\
A &= \sqrt{\frac{\lambda_2}{\pi}} \\
\end{aligned}$$

* 推導
* $\int_{-\infty}^{\infty} u^2 e^{-\lambda_2 u^2} du = \frac{1}{2\lambda_2}\sqrt{\frac{\pi}{\lambda_2}}$


$$\begin{aligned}
\int_{-\infty}^{\infty} (x - \mu_x)^2 p(x) \, dx &= \sigma_x^2 \\
\int_{-\infty}^{\infty} (x - \mu_x)^2 A e^{-\lambda_2 (x - \mu_x)^2} \, dx &= \sigma_x^2 \\
A \cdot \frac{1}{2\lambda_2}\sqrt{\frac{\pi}{\lambda_2}} &= \sigma_x^2 \\
\frac{1}{2\lambda_2}&= \sigma_x^2 \\
\lambda_2 &= \frac{1}{2\sigma_x^2} \\
A &= \frac{1}{\sqrt{2\pi \sigma_x^2}}
\end{aligned}$$

$$p(x) = \frac{1}{\sqrt{2\pi \sigma_x^2}} \exp\left( -\frac{(x - \mu_x)^2}{2\sigma_x^2} \right)$$


* 此駐點解能最大化熵
  
  與 (a) 小題相同，微分熵泛函 $S[p] = -\int p(x) \ln p(x) \, dx$ 對於 $p(x)$ 是嚴格凹函數（strictly concave），且正規化、期望值與變異數這三個約束條件皆為關於 $p(x)$ 的線性約束（linear constraints）。因此，由一階變分為零所求得的駐點解即為唯一的全域最大值（global maximum


## Question 2. Verifying the Odd Symmetry of $\phi$

Consider independent observations

$$x_i = \mu + \varepsilon_i, \quad i = 1, \dots, N,$$

where $\mu \in \mathbb{R}$ is an unknown location parameter. The errors $\varepsilon_i$ share a common, strictly positive, differentiable PDF $f(e)$ on $\mathbb{R}$. Define

$$\phi(e) = \frac{f'(e)}{f(e)}.$$

Suppose we require the sample mean

$$\bar{x} = \frac{1}{N} \sum_{i=1}^{N} x_i$$

to be a maximum-likelihood estimate of $\mu$ for every possible sample. At $\mu = \bar{x}$, the deviations

$$e_i = x_i - \bar{x}$$

satisfy $\sum_{i=1}^{N} e_i = 0$. The first-order likelihood condition then requires

$$\sum_{i=1}^{N} \phi(e_i) = 0.$$

For $N = 2$, consider the deviations

$$e_1 = d, \quad e_2 = -d,$$

where $d$ is any real number.

* (a)
  
  Substitute these deviations into the likelihood condition and show that 
  
  $$\phi(-d) = -\phi(d).$$ 
  
  Is $\phi$ an odd or an even function?

* (b) 
  
  Verify that the proposed linear form 
  
  $$\phi(e) = -he, \quad h > 0,$$ 
  
  satisfies this symmetry condition.

* **Note：** This question concerns the symmetry of $\phi$ not of the PDF $f$ . You are asked to verify the
proposed linear form; odd symmetry alone does not establish linearity.


## Answer 2


### (a) 

Cauchy 函數方程 $\varphi(a + b) = \varphi(a) + \varphi(b)$

$$\begin{aligned}
\sum_{i=1}^{N} \phi(e_i) &= 0 \\
\phi(e_1) + \phi(e_2) &= 0 \\
\phi(d) + \phi(-d) &= 0 \\
\phi(-d) &= -\phi(d) \\
\end{aligned}$$

奇函數 odd function

### (b) 

$$\begin{aligned}
\phi(e) &= -he \\
\phi(-d) &= -h(-d) \\
&= hd \\
\end{aligned}$$

$$\begin{aligned}
\phi(e) &= -he \\
-\phi(d) &= -(-h(d)) \\
&= hd \\
\end{aligned}$$

$$\phi(-d) = hd = -\phi(d)$$


順帶一提，當 $\phi(e) = \frac{f'(e)}{f(e)} = -he$ 時，兩邊對 $e$ 積分就會得到 $\ln f(e) = -\frac{1}{2}he^2 + C \implies f(e) \propto e^{-\frac{1}{2}he^2}$，這正是高斯分佈的推導基礎——高斯定理指出，當樣本平均數 $\bar{x}$ 對任意樣本都是位置參數 $\mu$ 的最大似然估計量時，誤差分佈必然為高斯分佈。


## Question 3. Maximum Likelihood for Categorical Forecasts


Consider a simplified subseasonal-to-seasonal (S2S) precipitation forecast with three mutually exclusive and exhaustive categories: Below Normal ($i = 0$), Near Normal ($i = 1$), and Above Normal ($i = 2$). The category thresholds are prescribed and held fixed.

Suppose $N$ independent verification cases are represented by the **same** forecast probability vector $\mathbf{p} = (p_0, p_1, p_2)$, where $p_i > 0$ and $\sum_{i=0}^{2} p_i = 1$. Let $n_i$ be the observed number of cases in category $i$, and define

$$q_i = \frac{n_i}{N}, \quad \sum_{i=0}^{2} q_i = 1.$$

Assume every category is observed at least once, so $q_i > 0$.


* (a) Constructing the log-likelihood
The likelihood of the observed category counts is

$$\mathcal{P}(\mathbf{n} \mid \mathbf{p}) = \frac{N!}{n_0! n_1! n_2!} \prod_{i=0}^{2} p_i^{n_i}.$$

The multinomial coefficient does not depend on $\mathbf{p}$. Omit this factor throughout the exercise and define the log-likelihood, up to this additive constant, as

$$\ell(\mathbf{p}) = \ln \left( \prod_{i=0}^{2} p_i^{n_i} \right).$$

Express $\ell(\mathbf{p})$ in terms of $N$, $q_i$, and $\ln p_i$. Use natural logarithms.


* (b) Finding the maximum-likelihood probabilities
Treat the observed frequencies $q_i$ as fixed constants.

  * Construct a Lagrangian to maximize $\ell(\mathbf{p})$ subject to $\sum_{i=0}^{2} p_i = 1$.
  * Show that the maximum occurs at $p_i = q_i$. Briefly justify why the stationary solution is a maximum.
  * Define $S(\mathbf{q}) = -\sum_{i=0}^{2} q_i \ln q_i$, the discrete Shannon entropy of the observed relative-frequency distribution. Show that $\ell_{\max}/N = -S(\mathbf{q})$.


* (c) Comparing two forecast distributions
Let $N = 100$ and $\mathbf{q} = (0.1, 0.5, 0.4)$. Compare

$$\text{Model A: } \mathbf{p}_A = (0.1, 0.5, 0.4), \quad \text{Model B: } \mathbf{p}_B = (1/3, 1/3, 1/3).$$

Calculate $\ell(\mathbf{p})$ and the forecast entropy $S(\mathbf{p}) = -\sum_{i=0}^{2} p_i \ln p_i$ for each model. Explain why Model B has a lower log-likelihood even though its forecast entropy is higher. Distinguish uncertainty within a forecast distribution from agreement with the observed frequencies.


## Answer 3

### (a)

* $q_i = \frac{n_i}{N}$

$$\begin{aligned}
l(p) &= \ln\left(\prod_{i=0}^{2} p_i^{n_i}\right) \\
&= \sum_{i=0}^{2} \ln\left(p_i^{n_i}\right) \\
&= \sum_{i=0}^{2} n_i \ln p_i \\
&= \sum_{i=0}^{2} (N q_i) \ln p_i \\
&= N \sum_{i=0}^{2} q_i \ln p_i
\end{aligned}$$

### (b)

將觀測頻率 $q_i$ 視為固定常數。   
(i) 建立拉格朗日函數（Lagrangian），以在受限於 $\sum_{i=0}^{2} p_i = 1$ 的條件下最大化 $l(p)$。   
(ii) 證明最大值發生在 $p_i = q_i$，並簡要說明為何此駐點解為最大值。   
(iii) 定義 $S(q) = -\sum_{i=0}^{2} q_i \ln q_i$ 為觀測相對頻率分佈的離散夏農熵（discrete Shannon entropy），請證明 $l_{\max} / N = -S(q)$。

(i)

$$\mathcal{L}(p, \lambda) = N \sum_{i=0}^{2} q_i \ln p_i - \lambda \left( \sum_{i=0}^{2} p_i - 1 \right)$$

(ii) $\sum_{i=0}^{2} q_i = 1$

$$\begin{aligned}
\frac{\partial \mathcal{L}}{\partial p_i} &= 0 \\
\frac{N q_i}{p_i} - \lambda &= 0 \\
p_i &= \frac{N q_i}{\lambda}
\end{aligned}$$

$$\begin{aligned}
\sum_{i=0}^{2} p_i &= 1 \\
\frac{N}{\lambda} \sum_{i=0}^{2} q_i  &= 1\\
\frac{N}{\lambda} (1) &= 1 \\
\lambda &= N
\end{aligned}$$

$$ p_i = q_i$$

$l(p)$ 在定義域上為嚴格凹函數，所以極值是最大值

(iii)

$$\begin{aligned}
l(p) &= N \sum_{i=0}^{2} q_i \ln p_i \\
\frac{l(p)}{N} &=  \sum_{i=0}^{2} q_i \ln p_i \\
\frac{l_{\text{max}}}{N} &=  \sum_{i=0}^{2} q_i \ln p_i \\
-S(q) &=  \sum_{i=0}^{2} q_i \ln p_i \\
\end{aligned}$$

### (c)
(c) 比較兩個預報分佈 (Comparing two forecast distributions)   


設 $N = 100$ 且 $q = (0.1, 0.5, 0.4)$，比較以下兩個模型：   
* 模型 A (Model A)：$p_A = (0.1, 0.5, 0.4)$   
* 模型 B (Model B)：$p_B = (1/3, 1/3, 1/3)$   

請計算每個模型的 $l(p)$ 與預報熵 $S(p) = -\sum_{i=0}^{2} p_i \ln p_i$。請解釋為何模型 B 的預報熵較高，但其對數似然值卻較低；並區分「預報分佈內部的不確定性（uncertainty within a forecast distribution）」與「和觀測頻率之間的吻合度（agreement with the observed frequencies）」。 





已知 $N = 100$，觀測相對頻率為 $q = (0.1, 0.5, 0.4)$。

#### 1. 計算 Model A 與 Model B 的 $S(p)$ 與 $l(p)$

* **Model A**：$p_A = (0.1, 0.5, 0.4)$（完美吻合觀測頻率，即 $p_A = q$）


* **預報熵** $S(p_A)$：

$$\begin{aligned}     S(p_A) &= -\sum_{i=0}^{2} p_{A,i} \ln p_{A,i} \\     &= -\big( 0.1 \ln 0.1 + 0.5 \ln 0.5 + 0.4 \ln 0.4 \big) \\     &\approx -\big( 0.1(-2.3026) + 0.5(-0.6931) + 0.4(-0.9163) \big) \\     &\approx -\big( -0.2303 - 0.3466 - 0.3665 \big) = \mathbf{0.9433}     \end{aligned}$$


* **對數似然值** $l(p_A)$：
因為 $p_A = q$，由 (b)(iii) 可知 $l(p_A) = l_{\max} = -N S(q)$：



$$l(p_A) = -100 \times 0.943348 \approx \mathbf{-94.33}$$




* **Model B**：$p_B = (1/3, 1/3, 1/3)$（均勻分佈預報）


* **預報熵** $S(p_B)$：

$$S(p_B) = -\sum_{i=0}^{2} \frac{1}{3} \ln\left(\frac{1}{3}\right) = -3 \times \frac{1}{3} (-\ln 3) = \ln 3 \approx \mathbf{1.0986}$$


* **對數似然值** $l(p_B)$：

$$\begin{aligned}     l(p_B) &= N \sum_{i=0}^{2} q_i \ln p_{B,i} \\     &= 100 \times \big( 0.1 \ln(1/3) + 0.5 \ln(1/3) + 0.4 \ln(1/3) \big) \\     &= 100 \times (0.1 + 0.5 + 0.4) \ln(1/3) \\     &= -100 \ln 3 \approx \mathbf{-109.86}     \end{aligned}$$





| 模型 | 預報機率向量 $p$<br> | 預報熵 $S(p)$<br> | 對數似然值 $l(p)$<br> |
| --- | --- | --- | --- |
| **Model A**<br> | $(0.1, 0.5, 0.4)$<br> | $\mathbf{0.9433}$ | $\mathbf{-94.33}$（較高，擬合較佳） |
| **Model B**<br> | $(1/3, 1/3, 1/3)$<br> | $\mathbf{1.0986}$（較高，不確定性較大） | $\mathbf{-109.86}$ |

---

#### **2. 物理與統計意義解釋：預報內部不確定性 vs. 與觀測的吻合度**

* **預報分佈內部的不確定性（Uncertainty within a forecast distribution — 由 $S(p)$ 衡量）**：
預報熵 $S(p) = -\sum p_i \ln p_i$ 僅取決於預報機率 $p$ 本身，用來衡量**預報系統自身的分散程度或「不確定性」**，與實際觀測結果 $q$ 完全無關。Model B 將三個類別的機率皆設為 $1/3$（均勻分佈），代表預報沒有提供任何傾向特定類別的資訊，因此具有三類別中可能達到的最高預報熵（$S(p_B) = \ln 3 \approx 1.0986 > S(p_A) \approx 0.9433$）。


* **與觀測頻率的吻合度（Agreement with the observed frequencies — 由 $l(p)$ 衡量）**：
對數似然函數 $l(p) = N \sum q_i \ln p_i$ 衡量的是**預報分佈 $p$ 對實際觀測頻率 $q$ 的解釋能力與吻合程度**。從資訊理論來看，我們可以將 $l(p)/N$ 改寫為：



$$\frac{l(p)}{N} = \sum_{i=0}^{2} q_i \ln p_i = -S(q) - \sum_{i=0}^{2} q_i \ln\left(\frac{q_i}{p_i}\right) = -S(q) - D_{\text{KL}}(q \parallel p)$$



其中 $D_{\text{KL}}(q \parallel p) \ge 0$ 為衡量 $q$ 與 $p$ 差異的相對熵（Kullback-Leibler divergence）。
* **為何 Model B 的預報熵較高，對數似然值卻較低？**
因為最大化預報熵 $S(p)$ 只是讓預報本身變得「最模糊、最均勻」，並不等於貼近真實大氣狀態。實際觀測頻率 $q = (0.1, 0.5, 0.4)$ 明顯偏向正常（$i=1$）與偏多（$i=2$）：


* **Model A** 準確捕捉到這個分佈特徵（$p_A = q$），沒有任何分佈偏差懲罰（$D_{\text{KL}} = 0$），因此獲得最高可能的對數似然值（$-94.33$）。


* **Model B** 給出毫無鑑別度的均勻機率（$p_B \neq q$），與實際觀測頻率不符（產生了 $D_{\text{KL}}(q \parallel p_B) > 0$ 的偏差懲罰），因此即使它的預報熵最高，其對數似然值（$-109.86$）仍顯著低於 Model A。





## 比較

這正是把第一題（最大熵原理，Maximum Entropy）和第三題（最大似然估計，Maximum Likelihood）串聯起來最核心的觀念：**「熵（Entropy）」衡量的是「不確定性（Uncertainty）或模糊程度」，而不是「預報的好壞或準確度」**。

為什麼第一題我們要「選熵最大的分佈」，到了第三題，熵最大的 Model B 卻變成比較差的模型？關鍵在於「我們手上有多少已知資訊（約束條件）」**以及**「我們現在的任務是什麼」。

---

### **1. 為什麼在 Q1 我們要選「熵最大」的分佈？（建立先驗分佈：不「不懂裝懂」）**

在第一題中，我們**沒有完整的觀測分佈資料**，手上只有極少數的條件：

* **Q1(a)**：只知道變數落在 $[a, b]$ 之間，其他一無所知。


* **Q1(b)**：只知道平均數是 $\mu_x$、變異數是 $\sigma_x^2$，其他高階特徵一無所知。



在這種「資訊不足」的情況下，如果我們隨便挑一個「熵比較小」的分佈（例如在 $[a, b]$ 裡面故意畫一個偏向某邊的尖峰），就代表我們**在沒有觀測證據的情況下，自己亂加了主觀假設（人為偏見）**。

因此，統計學上的最大熵原理（Principle of Maximum Entropy）告訴我們：

> **「在滿足所有已知約束條件（Constraints）的前提下，我們應該選擇熵最大（不確定性最高、最平坦）的分佈。」**

這樣做的目的不是因為「熵大代表準確」，而是為了**誠實面對未知（保持最大程度的中立與不偏頗）**——除了已知的 $\mu_x$ 和 $\sigma_x^2$ 之外，不多做任何沒有根據的猜測。

---

### **2. 為什麼在 Q3 中，熵最大的 Model B 反而是壞預報？（預報校驗：不能「有資料還裝傻」）**

到了第三題，情境完全不同了：我們現在是在做**降雨預報校驗（Forecast Verification）**，而且手上有 $N = 100$ 次真實的大氣觀測頻率 $q = (0.1, 0.5, 0.4)$。

這時候來看兩個模型的物理意義：

* **Model B：$p_B = (1/3, 1/3, 1/3)$（熵最大，$S = 1.0986$）**


在三分類預報中，給出 $(1/3, 1/3, 1/3)$ 代表預報員說：**「偏少、正常、偏多的機率通通一樣，我完全不知道會不會下雨！」**


它的預報熵 $S(p_B)$ 最大，代表這個預報**內部的不確定性最高（最模糊、資訊量為零）**。如果氣象局每天都報 $(1/3, 1/3, 1/3)$，雖然它的熵最大，但對使用者來說毫無參考價值，而且完全違背了真實氣候背景中「正常與偏多佔了 90%（$0.5 + 0.4$）、偏少只佔 10%（$0.1$）」的觀測事實。


* **Model A：$p_A = (0.1, 0.5, 0.4)$（熵較小，$S = 0.9433$）**


Model A 的熵比較小，代表它**消除了部分不確定性**，明確指出「正常（50%）與偏多（40%）的機率較高，偏少（10%）的機率很低」。更重要的是，這個分佈完美吻合真實觀測 $q = (0.1, 0.5, 0.4)$，因此在似然函數 $l(p)$ 的評分下拿到最高分（$-94.33 > -109.86$）。



---

### **3. 把 Q1 與 Q3 統一起來看：約束條件決定一切**

其實 Q1 和 Q3 並沒有矛盾！

* 在 **Q1(a)** 中，因為**沒有任何額外資訊**，唯一約束只有 $\int_a^b p(x)dx = 1$，所以最大熵分佈是均勻分佈（就像 Model B 的 $1/3, 1/3, 1/3$）。


* 在 **Q1(b)** 中，當我們**加入了 $\mu_x$ 和 $\sigma_x^2$ 的約束條件**後，我們就不能再選均勻分佈了，而必須在「符合 $\mu_x$ 與 $\sigma_x^2$」的函數裡面挑熵最大的（也就是高斯分佈）。


* 在 **Q3** 中，我們已經透過 $N = 100$ 次觀測，直接知道了真實世界的類別機率分佈就是 $q = (0.1, 0.5, 0.4)$。當真實分佈已經揭曉時，預報的目標是**貼近真實觀測（最大化似然函數 $l(p)$）**，而不是閉著眼睛追求最大的模糊度（最大化 $S(p)$）。



|比較維度 | 第一題 (Q1)：最大熵原理 (MaxEnt) | 第三題 (Q3)：最大似然估計 (MLE)|
| --- | --- | --- |
| **手上的資訊** | 只有部分統計矩（例如只知區間 $[a,b]$，或只知 $\mu_x, \sigma_x^2$）| 已有實際觀測到的完整類別頻率 $q = (0.1, 0.5, 0.4)$<br> |
| **核心目標** | **避免人為偏見**：在滿足已知條件下，讓未知部分保持最大不確定性 | **吻合觀測事實**：讓預報分佈 $p$ 越接近真實觀測 $q$ 越好|
| **數學操作** | 在約束條件下 **最大化熵** $S[p]$<br> | **最大化對數似然** $l(p)$（等價於最小化 $q$ 與 $p$ 的相對熵 $D_{\text{KL}}$） |
| **「熵很大」代表什麼？** | 代表沒有亂加額外假設（誠實反映無知） | 代表預報本身非常模糊、缺乏鑑別度（如 $1/3, 1/3, 1/3$ 亂猜） |

簡言之：當你沒有資料時，要選「熵最大」的分佈才不會不懂裝懂（Q1）；但當你已經有真實觀測資料時，還給出「熵最大」的均勻預報，就是在裝傻了（Q3）！