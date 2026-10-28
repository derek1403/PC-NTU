# Objective Analysis Week 06 Homework — 完整解答

題目原文與中文翻譯見 [hw6.md](hw6.md)。

---

## Answer 1. Multivariate AR(1): Covariance and Stability

模型：$\mathbf{x}_{n+1} = \mathbf{A}\mathbf{x}_n + \boldsymbol\eta_n$，$\boldsymbol\eta_n \sim \mathcal{N}(\mathbf{0}, \mathbf{Q})$，$\mathbf{Q} = \mathbf{I}_2 - \mathbf{A}\mathbf{A}^\mathsf{T}$。$\boldsymbol\eta_n$ 與 $\mathbf{x}_n, \mathbf{x}_{n-1}, \dots$ 獨立，且 $\mathbb{E}[\mathbf{x}_0] = \mathbf{0}$。

### (a) 雜訊共變異數與穩定性

* **用 SVD 寫出 $\mathbf{Q}$**

  因為 $(\mathbf{U}\boldsymbol\Sigma\mathbf{V}^\mathsf{T})^\mathsf{T} = \mathbf{V}\boldsymbol\Sigma\mathbf{U}^\mathsf{T}$（$\boldsymbol\Sigma$ 是對角矩陣，所以 $\boldsymbol\Sigma^\mathsf{T} = \boldsymbol\Sigma$），而且正交矩陣 $\mathbf{V}$ 滿足 $\mathbf{V}^\mathsf{T}\mathbf{V} = \mathbf{I}$，所以

  $$\mathbf{A}\mathbf{A}^\mathsf{T} = \mathbf{U}\boldsymbol\Sigma\mathbf{V}^\mathsf{T}\mathbf{V}\boldsymbol\Sigma\mathbf{U}^\mathsf{T} = \mathbf{U}\boldsymbol\Sigma^2\mathbf{U}^\mathsf{T}$$

  $\mathbf{U}$ 也是正交矩陣，所以 $\mathbf{I}_2 = \mathbf{U}\mathbf{U}^\mathsf{T}$。兩式相減得到

  $$\boxed{\mathbf{Q} = \mathbf{U}\left(\mathbf{I}_2 - \boldsymbol\Sigma^2\right)\mathbf{U}^\mathsf{T} = \mathbf{U}\,\mathrm{diag}\!\left(1 - s_1^2,\ 1 - s_2^2\right)\mathbf{U}^\mathsf{T}}$$

* **Admissibility 條件**

  上式就是 $\mathbf{Q}$ 的特徵分解，所以 $\mathbf{Q}$ 的特徵值是 $1 - s_1^2$ 和 $1 - s_2^2$。共變異數矩陣必須半正定，也就是每個特徵值都要 $\ge 0$。因為奇異值本身 $s_i \ge 0$，所以條件為

  $$\boxed{0 \le s_i \le 1,\ i = 1, 2} \quad \Longleftrightarrow \quad \|\mathbf{A}\|_2 = s_{\max} \le 1$$

* **Asymptotic stability 條件**

  拿掉雜訊後，$\mathbf{x}_n = \mathbf{A}^n\mathbf{x}_0$。若 $\mathbf{A} = \mathbf{E}\boldsymbol\Lambda\mathbf{E}^{-1}$，則 $\mathbf{A}^n = \mathbf{E}\boldsymbol\Lambda^n\mathbf{E}^{-1}$。要讓任何 $\mathbf{x}_0$ 都滿足 $\mathbf{x}_n \to \mathbf{0}$，每一個 $\lambda_i^n$ 都必須趨近於 $0$。特徵值可能是負數或複數，所以條件要加在絕對值上：

  $$\boxed{|\lambda_i| < 1,\ i = 1, 2} \quad \Longleftrightarrow \quad \rho(\mathbf{A}) < 1$$

  （若 $\mathbf{A}$ 不可對角化，用 Jordan 形式可得到相同的結論。）

* **Admissibility 不能保證 asymptotic stability**

  反例是 $\mathbf{A} = \mathrm{diag}(1, 0.5)$。它的奇異值為 $s_1 = 1$、$s_2 = 0.5$，兩者都 $\le 1$，所以 $\mathbf{Q} = \mathrm{diag}(0, 0.75)$ 是 admissible 的。但它的特徵值 $\lambda_1 = 1$ 不滿足 $|\lambda_1| < 1$，所以系統不是漸近穩定的。

  一般來說 $|\lambda_i| \le s_{\max}$。所以若 $s_{\max} < 1$，系統就一定穩定。兩個條件的差別只出在邊界上：admissibility 允許 $s_i = 1$，stability 卻不允許 $|\lambda_i| = 1$。

### (b) 共變異數平衡與邊際模態

* **推導 $\mathbf{P}_{n+1} = \mathbf{A}\mathbf{P}_n\mathbf{A}^\mathsf{T} + \mathbf{Q}$**

  $$\mathbf{P}_{n+1} = \mathbb{E}\big[(\mathbf{A}\mathbf{x}_n + \boldsymbol\eta_n)(\mathbf{A}\mathbf{x}_n + \boldsymbol\eta_n)^\mathsf{T}\big] = \mathbf{A}\,\mathbb{E}[\mathbf{x}_n\mathbf{x}_n^\mathsf{T}]\,\mathbf{A}^\mathsf{T} + \mathbf{A}\,\mathbb{E}[\mathbf{x}_n\boldsymbol\eta_n^\mathsf{T}] + \mathbb{E}[\boldsymbol\eta_n\mathbf{x}_n^\mathsf{T}]\,\mathbf{A}^\mathsf{T} + \mathbb{E}[\boldsymbol\eta_n\boldsymbol\eta_n^\mathsf{T}]$$

  因為 $\boldsymbol\eta_n$ 與 $\mathbf{x}_n$ **獨立**，所以 $\mathbb{E}[\mathbf{x}_n\boldsymbol\eta_n^\mathsf{T}] = \mathbb{E}[\mathbf{x}_n]\,\mathbb{E}[\boldsymbol\eta_n]^\mathsf{T}$；又因為 $\boldsymbol\eta_n$ 的平均為零，這一項等於 $\mathbf{0}$。另一個交叉項是它的轉置，也等於 $\mathbf{0}$。最後一項是 $\mathbf{Q}$。因此

  $$\boxed{\mathbf{P}_{n+1} = \mathbf{A}\mathbf{P}_n\mathbf{A}^\mathsf{T} + \mathbf{Q}}$$

  （$\mathbb{E}[\mathbf{x}_n] = \mathbf{0}$ 對所有 $n$ 成立，因為 $\mathbb{E}[\mathbf{x}_{n+1}] = \mathbf{A}\,\mathbb{E}[\mathbf{x}_n]$，而 $\mathbb{E}[\mathbf{x}_0] = \mathbf{0}$。所以 $\mathbf{P}_n$ 就是共變異數矩陣。）

* **$\mathbf{P} = \mathbf{I}_2$ 是穩態解**

  穩態共變異數方程為 $\mathbf{P} = \mathbf{A}\mathbf{P}\mathbf{A}^\mathsf{T} + \mathbf{Q}$。代入 $\mathbf{P} = \mathbf{I}_2$：

  $$\mathbf{A}\mathbf{I}_2\mathbf{A}^\mathsf{T} + \mathbf{Q} = \mathbf{A}\mathbf{A}^\mathsf{T} + \mathbf{I}_2 - \mathbf{A}\mathbf{A}^\mathsf{T} = \mathbf{I}_2 \;\checkmark$$

  這行代數對任何 $\mathbf{A}$ 都成立。「whenever $\mathbf{Q}$ is admissible」這個條件的作用是：只有當 $\mathbf{Q}$ 半正定時，才存在共變異數為 $\mathbf{Q}$ 的雜訊 $\boldsymbol\eta_n$，這個模型才有定義。所以只有在這個條件下，$\mathbf{P} = \mathbf{I}_2$ 才是某個真實隨機過程的穩態共變異數，而不只是一個代數解。

* **$\mathbf{A} = \mathrm{diag}(1, 0.5)$：初始擾動會衰減嗎？**

  沒有雜訊時，$X_{1,n} = 1^n X_{1,0} = X_{1,0}$，$X_{2,n} = 0.5^n X_{2,0} \to 0$。第二個分量的擾動會衰減，但第一個分量的擾動**永遠不會衰減**。$\lambda_1 = 1$ 對應的是一個邊際模態（marginal mode），所以系統**不是**漸近穩定的。

* **$\sup_n \mathbb{E}\|\mathbf{x}_n\|_2^2 < \infty$ 嗎？**

  此時 $\mathbf{Q} = \mathrm{diag}(0, 0.75)$。$\mathbf{A}$、$\mathbf{Q}$ 都是對角矩陣，所以共變異數平衡式拆成兩條純量遞迴式：

  $$P_{11,n+1} = P_{11,n} \;\Rightarrow\; P_{11,n} = P_{11,0}$$

  $$P_{22,n+1} = 0.25\,P_{22,n} + 0.75 \;\Rightarrow\; P_{22,n} = 1 + 0.25^n\,(P_{22,0} - 1) \to 1$$

  因此 $\mathbb{E}\|\mathbf{x}_n\|_2^2 = \mathrm{tr}\,\mathbf{P}_n = P_{11,0} + 1 + 0.25^n(P_{22,0} - 1)$。

  $$\boxed{\sup_n \mathbb{E}\|\mathbf{x}_n\|_2^2 = P_{11,0} + \max(P_{22,0},\, 1) < \infty}$$

  所以變異數有界，雖然系統不是漸近穩定的。

* **$\mathbf{x}_0 \sim \mathcal{N}(\mathbf{0}, \mathbf{I}_2)$ 時，過程平穩嗎？**

  **是。** 此時 $\mathbf{P}_0 = \mathbf{I}_2$，由穩態方程和歸納法可得 $\mathbf{P}_n = \mathbf{I}_2$ 對所有 $n$ 成立。兩個時刻之間的共變異數為

  $$\mathbb{E}[\mathbf{x}_{n+k}\mathbf{x}_n^\mathsf{T}] = \mathbb{E}\Big[\Big(\mathbf{A}^k\mathbf{x}_n + \sum_{j=0}^{k-1}\mathbf{A}^{k-1-j}\boldsymbol\eta_{n+j}\Big)\mathbf{x}_n^\mathsf{T}\Big] = \mathbf{A}^k\mathbf{P}_n = \mathbf{A}^k$$

  這個結果只跟時間差 $k$ 有關。此外，過程是平均為零的高斯過程（$\mathbf{x}_0$ 與所有雜訊都是高斯，線性組合仍是高斯），所以所有聯合分布都只由均值和共變異數決定。因此這個過程是**嚴格平穩**的。

* **平穩性與漸近穩定性的差別**

  平穩性描述的是**分布**，它問的是「過程的統計性質會不會隨時間改變」。漸近穩定性描述的是**確定性動力學 $\mathbf{A}$**，它問的是「初始擾動會不會被遺忘」。

  這個例子是平穩的，但不是漸近穩定的。第一個分量的雜訊變異數 $Q_{11} = 0$，係數又是 1，所以 $X_{1,n} = X_{1,0}$ 對所有 $n$ 都成立。它一直都是同一個隨機變數，分布當然不變，但它也從來沒有忘記初始值。

  平穩性在這裡只是因為「剛好從穩態分布出發」。若改用 $\mathbf{x}_0 \sim \mathcal{N}(\mathbf{0}, \mathrm{diag}(4, 1))$，則 $P_{11,n} = 4$ 永遠不會收斂到 1，過程也就不再平穩。對比之下，一個漸近穩定的系統從任何初始共變異數出發，$\mathbf{P}_n$ 都會收斂到唯一的穩態解。

### (c) 無界變異數

* **$\mathbf{I}_2 - \mathbf{A}\mathbf{A}^\mathsf{T}$ 不是合法的共變異數**

  $\mathbf{A} = \mathrm{diag}(1.1, 0.5)$，$\mathbf{A}\mathbf{A}^\mathsf{T} = \mathrm{diag}(1.21, 0.25)$，所以

  $$\mathbf{I}_2 - \mathbf{A}\mathbf{A}^\mathsf{T} = \mathrm{diag}(-0.21,\ 0.75)$$

  第一個對角元素是負的，也就是說雜訊第一個分量的變異數會是 $-0.21 < 0$，這是不可能的。用 (a) 的語言來說，$s_1 = 1.1 > 1$，違反 admissibility 條件。

* **改用 $\mathbf{Q} = \mathbf{I}_2$、$\mathbf{x}_0 = \mathbf{0}$，推導 $\mathrm{Var}(X_{1,n})$**

  第一個分量滿足 $X_{1,n+1} = 1.1\,X_{1,n} + \eta_{1,n}$，$\mathrm{Var}(\eta_{1,n}) = 1$。由共變異數平衡式：

  $$\mathrm{Var}(X_{1,n+1}) = 1.21\,\mathrm{Var}(X_{1,n}) + 1, \qquad \mathrm{Var}(X_{1,0}) = 0$$

  展開得到等比級數：

  $$\boxed{\mathrm{Var}(X_{1,n}) = \sum_{k=0}^{n-1} 1.21^k = \frac{1.21^n - 1}{0.21}} \xrightarrow{n\to\infty} \infty$$

  因為 $1.21 > 1$，變異數以指數速度發散，所以不存在平穩分布。（第二個分量 $\mathrm{Var}(X_{2,n}) = \frac{1 - 0.25^n}{0.75} \to \frac{4}{3}$ 仍有界。）

* **「變異數隨時間無界」與「高斯分布的支撐集無界」的差別**

  在任何**固定**時刻 $n$，$X_{1,n}$ 都是高斯分布 $\mathcal{N}\big(0, \frac{1.21^n - 1}{0.21}\big)$。它的支撐集是整條實數線，任何值都有正的機率密度，但它的變異數是一個**有限**的數。這是單一分布的性質，即使是穩定的 AR(1)，每個時刻的分布也一樣有無界的支撐集。

  「變異數隨時間無界」則是說：隨著 $n$ 增加，這個分布的寬度本身無限制地長大，也就是 $\sup_n \mathrm{Var}(X_{1,n}) = \infty$。這是整個**過程**隨時間的性質，代表系統不穩定，而不是單一分布的形狀。

---

## Answer 2. One-dimensional DDPM

### (a) 前向分布

* **推導 $q(x_t \mid x_0)$**

  用歸納法證明 $q(x_t \mid x_0) = \mathcal{N}\big(x_t;\ \sqrt{\bar\alpha_t}\,x_0,\ 1 - \bar\alpha_t\big)$。

  當 $t = 1$：$x_1 = \sqrt{\alpha_1}\,x_0 + \sqrt{\beta_1}\,\xi_1$，平均為 $\sqrt{\bar\alpha_1}\,x_0$，變異數為 $\beta_1 = 1 - \bar\alpha_1$，成立。

  假設對 $t-1$ 成立，即 $x_{t-1} = \sqrt{\bar\alpha_{t-1}}\,x_0 + \sqrt{1 - \bar\alpha_{t-1}}\,\epsilon'$，其中 $\epsilon' \sim \mathcal{N}(0,1)$ 與 $\xi_t$ 獨立。代入前向過程：

  $$x_t = \sqrt{\alpha_t}\sqrt{\bar\alpha_{t-1}}\,x_0 + \underbrace{\sqrt{\alpha_t(1 - \bar\alpha_{t-1})}\,\epsilon' + \sqrt{\beta_t}\,\xi_t}_{\text{兩個獨立高斯之和}}$$

  平均為 $\sqrt{\bar\alpha_t}\,x_0$。兩個獨立高斯之和仍是高斯，變異數相加：

  $$\alpha_t(1 - \bar\alpha_{t-1}) + \beta_t = \alpha_t - \bar\alpha_t + 1 - \alpha_t = 1 - \bar\alpha_t$$

  因此

  $$\boxed{q(x_t \mid x_0) = \mathcal{N}\big(x_t;\ \sqrt{\bar\alpha_t}\,x_0,\ 1 - \bar\alpha_t\big)}, \qquad x_t = \sqrt{\bar\alpha_t}\,x_0 + \sqrt{1 - \bar\alpha_t}\,\epsilon,\quad \epsilon \sim \mathcal{N}(0,1)$$

  也就是說，不需要一步一步跑 $t$ 次，就可以直接從 $x_0$ 抽出 $x_t$。

* **$\bar\alpha_t \to 0$ 時**

  平均 $\sqrt{\bar\alpha_t}\,x_0 \to 0$，變異數 $1 - \bar\alpha_t \to 1$，所以 $q(x_t \mid x_0) \to \mathcal{N}(0, 1)$，與 $x_0$ 無關。前向過程把資料的所有資訊都抹掉了：不管 $x_0 = -2$ 還是 $x_0 = 2$，最後都變成標準常態。

  對整個資料分布而言也一樣：$q(x_t) = \tfrac12\mathcal{N}\big(-2\sqrt{\bar\alpha_t},\ 1 - 0.75\bar\alpha_t\big) + \tfrac12\mathcal{N}\big(2\sqrt{\bar\alpha_t},\ 1 - 0.75\bar\alpha_t\big)$，當 $\bar\alpha_t \to 0$ 時雙峰合併成單一的 $\mathcal{N}(0, 1)$。

### (b) 訓練目標與條件機率

* **均方誤差訓練目標**

  $$\boxed{L(\theta) = \mathbb{E}_{x_0 \sim q_{\mathrm{data}},\ t \sim \mathrm{U}\{1,\dots,T\},\ \epsilon \sim \mathcal{N}(0,1)}\Big[\big(\epsilon - \epsilon_\theta\big(\sqrt{\bar\alpha_t}\,x_0 + \sqrt{1 - \bar\alpha_t}\,\epsilon,\ t\big)\big)^2\Big]}$$

* **目標 $\epsilon$ 是哪一種雜訊？**

  目標 $\epsilon$ 是 (a) 中**標準化的累積雜訊**，不是 $t-1 \to t$ 這一步加入的 $\xi_t$。展開前向過程可得

  $$\sqrt{1 - \bar\alpha_t}\,\epsilon = \sum_{s=1}^{t}\sqrt{\frac{\bar\alpha_t}{\bar\alpha_s}}\sqrt{\beta_s}\,\xi_s$$

  所以 $\epsilon$ 是從第 1 步到第 $t$ 步所有雜訊的加權總和，再除以總標準差 $\sqrt{1 - \bar\alpha_t}$ 標準化成 $\mathcal{N}(0,1)$。

* **數值計算**

  $\sqrt{\bar\alpha_t} = \sqrt{0.64} = 0.8$，$\sqrt{1 - \bar\alpha_t} = \sqrt{0.36} = 0.6$：

  $$x_t = 0.8 \times 2 + 0.6 \times (-1) = 1.6 - 0.6 = \boxed{1.0}$$

  $$\text{squared error} = \big(\epsilon - \epsilon_\theta(x_t, t)\big)^2 = \big(-1 - (-0.8)\big)^2 = (-0.2)^2 = \boxed{0.04}$$

* **$q(x_{t-1} \mid x_t, x_0)$ 與 $p_\theta(x_{t-1} \mid x_t)$ 的差別**

  $q(x_{t-1} \mid x_t, x_0)$ 是**前向過程的真實後驗**。給定 $x_t$ **和** $x_0$，它可以用貝氏定理精確算出來，結果是一個高斯分布（推導見 Week 07 Q1）。它只在訓練時可用，因為訓練時我們手上有 $x_0$。

  $p_\theta(x_{t-1} \mid x_t)$ 是**學出來的反向模型**。它只以 $x_t$ 為條件，均值由神經網路 $\epsilon_\theta$ 決定。它要近似的是 $q(x_{t-1} \mid x_t) = \int q(x_{t-1} \mid x_t, x_0)\,q(x_0 \mid x_t)\,dx_0$，也就是把所有可能的 $x_0$ 平均起來之後的反向分布。這個積分需要知道資料分布，一般無法直接計算，所以才需要學。

* **為什麼生成時不能需要 $x_0$？**

  生成的目的就是要產生一個**新的** $x_0$。如果生成時需要輸入原始的 $x_0$，那就等於答案已經在手上，模型最多只能把它重建出來，而不能從資料分布中抽出新的樣本。所以生成程序只能從純雜訊 $x_T$ 出發，每一步只用當下的 $x_t$。

### (c) 反向抽樣

* **虛擬碼**

  ```text
  輸入：訓練好的 ε_θ、雜訊排程 {β_t}、反向標準差 {σ_t}
  α_t = 1 − β_t,  ᾱ_t = ∏_{s≤t} α_s

  x_T ~ N(0, 1)                         # 起始分布：因為 ᾱ_T ≈ 0，q(x_T) ≈ N(0, 1)
  for t = T, T−1, ..., 2:
      ε̂  = ε_θ(x_t, t)
      μ  = (1/√α_t) · ( x_t − β_t/√(1 − ᾱ_t) · ε̂ )
      z  ~ N(0, 1)                      # 每一步都重新抽
      x_{t−1} = μ + σ_t · z
  x_0 = (1/√α_1) · ( x_1 − β_1/√(1 − ᾱ_1) · ε_θ(x_1, 1) )   # t = 1 不加雜訊
  return x_0
  ```

  （常見的 $\sigma_t$ 選擇是 $\sigma_t^2 = \beta_t$ 或 $\sigma_t^2 = \tilde\beta_t = \frac{1 - \bar\alpha_{t-1}}{1 - \bar\alpha_t}\beta_t$。）

* **為什麼生成不會重走某個訓練樣本的前向雜訊路徑？**

  第一，起點 $x_T$ 和每一步的 $z_t$ 都是**全新的獨立抽樣**，跟任何訓練樣本當初的 $\epsilon$ 或 $\xi_t$ 都無關，那些實現值也從來沒有被存下來。

  第二，網路學到的不是某一個訓練樣本的雜訊，而是條件期望 $\epsilon_\theta(x_t, t) \approx \mathbb{E}[\epsilon \mid x_t]$，也就是把所有可能產生這個 $x_t$ 的訓練樣本平均起來的結果。許多不同的 $x_0$（例如 $-2$ 附近和 $2$ 附近的點）都可能擴散到同一個 $x_t$，所以反向過程在每一步都是在「機率上合理的方向」中隨機挑選，最後落在資料分布的某個位置，而不是重建某個特定的訓練樣本。在本題中，同一個起點 $x_T$ 配上不同的 $z_t$，可能落在 $-2$ 那一峰，也可能落在 $2$ 那一峰。
