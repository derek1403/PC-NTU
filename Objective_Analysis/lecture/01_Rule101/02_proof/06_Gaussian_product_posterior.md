# 高斯先驗 × 高斯概似 = 高斯後驗 (Gaussian Prior × Gaussian Likelihood → Gaussian Posterior)

模式預報（先驗）與儀器觀測（概似）各自帶著高斯誤差，用貝氏定理合併後，結果仍是高斯：**精度相加、平均是精度加權平均**。這就是資料同化中一步 Kalman 更新。

## 假設與已知 (Assumptions & Preliminaries)

* **【假設 1】先驗與概似皆為高斯 (Gaussian Prior & Likelihood)：** 模式預報帶高斯誤差；觀測 = 真值 + 高斯雜訊。

  * (a) 先驗

  $$f(x) = \mathcal{N}(\mu_0,\ \sigma_0^2)$$

  * (b) 概似

  $$f(y \mid x) = \mathcal{N}(x,\ \sigma_w^2)$$

  * $x$ : 真實狀態 (True state)，要估計的量
  * $y$ : 觀測值 (Observation)
  * $\mu_0, \sigma_0^2$ : 先驗平均與變異數 (Prior mean & variance)，資料同化中的背景場 $x^b$、$\sigma_b^2$
  * $\sigma_w^2$ : 觀測誤差變異數 (Observation error variance)，資料同化中的 $\sigma_o^2$

* **【已知 1】連續形式的貝氏定理 (Bayes' Theorem)：** 後驗正比於概似乘先驗；分母 $f(y)$ 與 $x$ 無關，只是正規化常數。（見 [99_textbook.md](../99_textbook.md) "From the product rule of probability to Bayes' theorem"。）

  $$f(x \mid y) \propto f(y \mid x)\,f(x)$$

  * $f(x \mid y)$ : 後驗 (Posterior)，看到觀測後對真值的信念
  * $f(y \mid x)$ : 概似 (Likelihood)，若真值是 $x$，看到 $y$ 的機率
  * $f(x)$ : 先驗 (Prior)，看到觀測前對真值的信念

* **【已知 2】[高斯分布的判別 (Recognizing a Gaussian)](../01_tool/01_Gaussian_distribution.md)：** 任何「對數是開口向下的二次式」的密度都是高斯；二次項係數決定變異數、一次項決定中心。

  $$\ln g(x) = -\frac{(x - m)^2}{2s^2} + \text{const} \quad\text{則}\quad g = \mathcal{N}(m, s^2)$$

  * $g$ : 任意機率密度 (PDF)，本證明中取後驗 $f(x \mid y)$
  * $m, s^2$ : 任意中心與變異數，本證明中對應【定義 1】的 $\mu_1, \sigma_1^2$

* **【定義 1】後驗參數 (Posterior Parameters)：** 後驗的精度是兩個精度的和；後驗平均是兩個平均以精度加權。

  * (a)

  $$\frac{1}{\sigma_1^2} \overset{\text{def}}{=} \frac{1}{\sigma_0^2} + \frac{1}{\sigma_w^2}$$

  * (b)

  $$\mu_1 \overset{\text{def}}{=} \sigma_1^2\left(\frac{\mu_0}{\sigma_0^2} + \frac{y}{\sigma_w^2}\right)$$

  * $\mu_1, \sigma_1^2$ : 後驗平均與變異數 (Posterior mean & variance)，資料同化中的分析場 $x^a$、$\sigma_a^2$

* **【定義 2】總誤差與 Kalman 增益 (Total Error & Kalman Gain)：** $K$ 是背景誤差佔總誤差的比例，決定要往觀測拉多少。

  * (a)

  $$S \overset{\text{def}}{=} \sigma_0^2 + \sigma_w^2$$

  * (b)

  $$K \overset{\text{def}}{=} \frac{\sigma_0^2}{S}$$

  * $S$ : 背景與觀測的總誤差變異數 (Total error variance)
  * $K$ : Kalman 增益 (Kalman gain)，$0 \le K \le 1$

* **【推導 1】後驗變異數的另一種寫法 (Posterior Variance)：** 把【定義 1(a)】的倒數通分取倒數。

  $$\begin{gather*}
  \sigma_1^2 &\overset{\text{定義 1(a)}}{=}& \frac{\sigma_0^2\,\sigma_w^2}{\sigma_0^2 + \sigma_w^2} \\
  &\overset{\text{定義 2(a)}}{=}& \frac{\sigma_0^2\,\sigma_w^2}{S}
  \end{gather*}$$

## proof

### (a) 後驗是高斯：取對數，與 $x$ 無關的項都丟進常數，對 $x$ 配方

$$\begin{gather*}
\ln f(x \mid y) &\overset{\text{已知 1,假設 1}}{=}& -\frac{(y - x)^2}{2\sigma_w^2} - \frac{(x - \mu_0)^2}{2\sigma_0^2} + \text{const} \\
&=& -\frac{1}{2}\left[\left(\frac{1}{\sigma_w^2} + \frac{1}{\sigma_0^2}\right)x^2 - 2\left(\frac{y}{\sigma_w^2} + \frac{\mu_0}{\sigma_0^2}\right)x\right] + \text{const} \\
&\overset{\text{定義 1}}{=}& -\frac{1}{2\sigma_1^2}\Big[x^2 - 2\mu_1 x\Big] + \text{const} \\
&=& -\frac{(x - \mu_1)^2}{2\sigma_1^2} + \text{const}
\end{gather*}$$

由【已知 2】，$f(x \mid y) = \mathcal{N}(\mu_1, \sigma_1^2)$。

### (b) 改寫成 Kalman 形式

* (b-1) 後驗平均

  $$\begin{gather*}
  \mu_1 &\overset{\text{定義 1(b),推導 1}}{=}& \frac{\sigma_0^2\sigma_w^2}{S}\left(\frac{\mu_0}{\sigma_0^2} + \frac{y}{\sigma_w^2}\right) \\
  &=& \frac{\sigma_w^2\,\mu_0 + \sigma_0^2\,y}{S} \\
  &\overset{\text{定義 2(a)}}{=}& \mu_0 + \frac{\sigma_0^2}{S}\,(y - \mu_0) \\
  &\overset{\text{定義 2(b)}}{=}& \mu_0 + K\,(y - \mu_0)
  \end{gather*}$$

* (b-2) 後驗變異數

  $$\begin{gather*}
  \sigma_1^2 &\overset{\text{推導 1}}{=}& \frac{\sigma_0^2\,\sigma_w^2}{S} \\
  &\overset{\text{定義 2(a)}}{=}& \sigma_0^2\left(1 - \frac{\sigma_0^2}{S}\right) \\
  &\overset{\text{定義 2(b)}}{=}& (1 - K)\,\sigma_0^2
  \end{gather*}$$

$\blacksquare$

## 結論

$$\boxed{\frac{1}{\sigma_1^2} = \frac{1}{\sigma_0^2} + \frac{1}{\sigma_w^2},\qquad x^a = x^b + K\,(y^o - x^b),\qquad \sigma_a^2 = (1-K)\,\sigma_b^2}$$

* **精度相加**：後驗永遠比先驗和觀測都更確定（$\sigma_1 < \sigma_0$ 且 $\sigma_1 < \sigma_w$）
* **$K \to 0$**（儀器很吵）：分析場貼近預報；**$K \to 1$**（預報很不準）：分析場貼近觀測

同一件事的最佳化版本：最小化 $J = -2\ln f(x \mid y)$ 就是 3D-Var。[Q08 1D-Var](../../00_Chapter0/01_tool/01_Lagrange_multiplier/05_problems/Q08_1DVar_data_assimilation.md) 用 Lagrange 乘數解的就是加了物理約束的這個代價函數，「越不可信的觀測被拉得越多」正是 $K$ 的角色。
