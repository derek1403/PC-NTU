# Objective Analysis Week 06 Homework

## Question 1. Multivariate AR(1): Covariance and Stability

Consider

$$\mathbf{x}_{n+1} = \mathbf{A}\mathbf{x}_n + \boldsymbol{\eta}_n, \qquad \mathbf{x}_n \in \mathbb{R}^2,$$

with independent zero-mean Gaussian innovations, independent of the current state and its past. Their proposed covariance is

$$\mathbf{Q} = \mathbf{I}_2 - \mathbf{A}\mathbf{A}^\mathsf{T}.$$

Assume a zero-mean initial state with finite covariance, independent of future innovations. A covariance matrix must be positive semidefinite.

* (a) **Noise covariance and stability.** Using the singular value decomposition $\mathbf{A} = \mathbf{U}\boldsymbol{\Sigma}\mathbf{V}^\mathsf{T}$, $\boldsymbol{\Sigma} = \mathrm{diag}(s_1, s_2)$, derive $\mathbf{Q}$ in terms of $\mathbf{U}$ and $\boldsymbol{\Sigma}$. State the condition on the singular values for $\mathbf{Q}$ to be admissible, and the condition on the eigenvalues of $\mathbf{A}$ for asymptotic stability. Does admissibility alone guarantee asymptotic stability?
* (b) **Covariance balance and a marginal mode.** Derive $\mathbf{P}_{n+1} = \mathbf{A}\mathbf{P}_n\mathbf{A}^\mathsf{T} + \mathbf{Q}$, $\mathbf{P}_n = \mathbb{E}[\mathbf{x}_n\mathbf{x}_n^\mathsf{T}]$, and verify that $\mathbf{P} = \mathbf{I}_2$ satisfies the stationary covariance equation whenever $\mathbf{Q}$ is admissible. For $\mathbf{A} = \mathrm{diag}(1, 0.5)$, determine whether initial perturbations decay and whether $\sup_n \mathbb{E}\|\mathbf{x}_n\|_2^2 < \infty$. If $\mathbf{x}_0 \sim \mathcal{N}(\mathbf{0}, \mathbf{I}_2)$, is the process stationary? Explain the distinction between stationarity and asymptotic stability.
* (c) **Unbounded variance.** Let $\mathbf{A} = \mathrm{diag}(1.1, 0.5)$. Explain why $\mathbf{I}_2 - \mathbf{A}\mathbf{A}^\mathsf{T}$ is not a valid covariance. Instead prescribe $\mathbf{Q} = \mathbf{I}_2$ and $\mathbf{x}_0 = \mathbf{0}$. Derive $\mathrm{Var}(X_{1,n})$ and show that it diverges. Briefly distinguish unbounded variance over time from the unbounded support of a Gaussian distribution.

### 中文翻譯

> **問題 1：多變量 AR(1)——共變異數與穩定性**
>
> 考慮 $\mathbf{x}_{n+1} = \mathbf{A}\mathbf{x}_n + \boldsymbol{\eta}_n$，$\mathbf{x}_n \in \mathbb{R}^2$，其中創新項（innovation）$\boldsymbol{\eta}_n$ 為彼此獨立、平均為零的高斯雜訊，且與當前狀態及其過去獨立。有人提議其共變異數為 $\mathbf{Q} = \mathbf{I}_2 - \mathbf{A}\mathbf{A}^\mathsf{T}$。
>
> 假設初始狀態平均為零、共變異數有限，且與未來的創新項獨立。共變異數矩陣必須是半正定的。
>
> * (a) **雜訊共變異數與穩定性**：利用奇異值分解 $\mathbf{A} = \mathbf{U}\boldsymbol{\Sigma}\mathbf{V}^\mathsf{T}$，$\boldsymbol{\Sigma} = \mathrm{diag}(s_1, s_2)$，以 $\mathbf{U}$ 與 $\boldsymbol{\Sigma}$ 表示 $\mathbf{Q}$。寫出奇異值需滿足什麼條件 $\mathbf{Q}$ 才是可容許的（admissible），以及 $\mathbf{A}$ 的特徵值需滿足什麼條件系統才漸近穩定（asymptotically stable）。單靠可容許性能保證漸近穩定嗎？
> * (b) **共變異數平衡與邊際模態**：推導 $\mathbf{P}_{n+1} = \mathbf{A}\mathbf{P}_n\mathbf{A}^\mathsf{T} + \mathbf{Q}$，其中 $\mathbf{P}_n = \mathbb{E}[\mathbf{x}_n\mathbf{x}_n^\mathsf{T}]$，並驗證只要 $\mathbf{Q}$ 可容許，$\mathbf{P} = \mathbf{I}_2$ 就滿足穩態共變異數方程。對 $\mathbf{A} = \mathrm{diag}(1, 0.5)$，判斷初始擾動是否衰減，以及 $\sup_n \mathbb{E}\|\mathbf{x}_n\|_2^2 < \infty$ 是否成立。若 $\mathbf{x}_0 \sim \mathcal{N}(\mathbf{0}, \mathbf{I}_2)$，此過程是否平穩（stationary）？說明平穩性與漸近穩定性的差別。
> * (c) **無界變異數**：令 $\mathbf{A} = \mathrm{diag}(1.1, 0.5)$。解釋為何 $\mathbf{I}_2 - \mathbf{A}\mathbf{A}^\mathsf{T}$ 不是合法的共變異數。改為指定 $\mathbf{Q} = \mathbf{I}_2$、$\mathbf{x}_0 = \mathbf{0}$，推導 $\mathrm{Var}(X_{1,n})$ 並證明它發散。簡要區分「變異數隨時間無界」與「高斯分布的支撐集無界」。


## Answer 1.

### 基本知識

* **1. 這個模型在做什麼**

  這個模型描述一個二維狀態 $\mathbf{x}_n$ 如何一步一步隨時間演化：

  $$\mathbf{x}_{n+1} = \mathbf{A}\mathbf{x}_n + \boldsymbol{\eta}_n$$

  在每一步中，模型先把目前的狀態 $\mathbf{x}_n$ 乘上矩陣 $\mathbf{A}$，這一項代表系統本身的演化規則（例如讓狀態變大、變小或旋轉）。接著，模型再加上一個隨機雜訊 $\boldsymbol\eta_n$，這一項代表系統每一步受到的隨機擾動。

  雜訊 $\boldsymbol\eta_n$ 是一個隨機向量，所以它有一個共變異數矩陣 $\mathbf{Q} = \mathbb{E}[\boldsymbol\eta_n\boldsymbol\eta_n^\mathsf{T}]$。$\mathbf{Q}$ 的對角線元素是雜訊兩個分量各自的變異數，非對角線元素是兩個分量之間的共變異數。

* **2. Admissible（可容許的）**

  題目「提議」用 $\mathbf{Q} = \mathbf{I}_2 - \mathbf{A}\mathbf{A}^\mathsf{T}$ 當作雜訊的共變異數矩陣。可是，並不是任意一個矩陣都可以當作共變異數矩陣。如果某個矩陣有資格當作共變異數矩陣，我們就說這個矩陣是 **admissible（可容許的）**。所以「$\mathbf{Q}$ 是 admissible」這句話的意思是：「$\mathbf{Q} = \mathbf{I}_2 - \mathbf{A}\mathbf{A}^\mathsf{T}$ 真的可以是某個隨機向量的共變異數矩陣」。

  那麼，一個矩陣要滿足什麼條件，才有資格當作共變異數矩陣呢？關鍵在於**變異數不可以是負數**。我們任取一個固定的向量 $\mathbf{v}$，把雜訊投影到 $\mathbf{v}$ 上，得到一個純量隨機變數 $\mathbf{v}^\mathsf{T}\boldsymbol\eta$。這個純量的變異數可以用 $\mathbf{Q}$ 算出來：

  $$\mathrm{Var}(\mathbf{v}^\mathsf{T}\boldsymbol\eta) = \mathbb{E}[(\mathbf{v}^\mathsf{T}\boldsymbol\eta)^2] = \mathbf{v}^\mathsf{T}\,\mathbb{E}[\boldsymbol\eta\boldsymbol\eta^\mathsf{T}]\,\mathbf{v} = \mathbf{v}^\mathsf{T}\mathbf{Q}\mathbf{v}$$

  因為任何變異數都必須 $\ge 0$，所以 $\mathbf{Q}$ 必須對**每一個**向量 $\mathbf{v}$ 都滿足 $\mathbf{v}^\mathsf{T}\mathbf{Q}\mathbf{v} \ge 0$。滿足這個性質的對稱矩陣叫做**半正定矩陣（positive semidefinite, PSD）**。

  線性代數告訴我們：一個對稱矩陣是半正定的，若且唯若它的**所有特徵值都 $\ge 0$**。（直觀理解：如果 $\mathbf{Q}$ 有一個負的特徵值 $\mu < 0$，取 $\mathbf{v}$ 為對應的特徵向量，就會得到 $\mathrm{Var}(\mathbf{v}^\mathsf{T}\boldsymbol\eta) = \mu\|\mathbf{v}\|^2 < 0$，這是不可能的。）

  → **所以 (a) 要我們做的事是：算出 $\mathbf{Q}$ 的特徵值，然後要求這些特徵值都 $\ge 0$。這個要求會變成一個關於 $\mathbf{A}$ 的奇異值 $s_i$ 的條件。**

* **3. Asymptotic stability（漸近穩定）**

  漸近穩定描述的是 $\mathbf{A}$ 這個演化規則本身的性質，與雜訊無關。為了只看 $\mathbf{A}$ 的作用，我們先把雜訊拿掉，只看 $\mathbf{x}_{n+1} = \mathbf{A}\mathbf{x}_n$。

  假設系統一開始有一個初始擾動 $\mathbf{x}_0$。如果不論 $\mathbf{x}_0$ 是哪一個向量，狀態 $\mathbf{x}_n$ 都會隨著 $n \to \infty$ 而趨近於 $\mathbf{0}$，我們就說這個系統是 **asymptotically stable（漸近穩定的）**。換句話說，漸近穩定的系統最後會「忘記」它的初始狀態。

  → **所以 (a) 要我們做的事是：找出 $\mathbf{A}$ 的特徵值 $\lambda_i$ 要滿足什麼條件，才能保證 $\mathbf{A}^n \to \mathbf{0}$。**

* **4. 奇異值與特徵值的差別**

  奇異值分解（SVD）把 $\mathbf{A}$ 寫成 $\mathbf{A} = \mathbf{U}\boldsymbol\Sigma\mathbf{V}^\mathsf{T}$。其中 $\mathbf{U}$ 和 $\mathbf{V}$ 都是正交矩陣，也就是說 $\mathbf{U}^\mathsf{T}\mathbf{U} = \mathbf{I}$、$\mathbf{V}^\mathsf{T}\mathbf{V} = \mathbf{I}$，它們代表旋轉或鏡射，不會改變向量的長度。$\boldsymbol\Sigma = \mathrm{diag}(s_1, s_2)$ 裡的奇異值 $s_i \ge 0$ 代表 $\mathbf{A}$ 在各個方向上把向量拉長或縮短的倍率。

  特徵值 $\lambda_i$ 則是另一種東西：如果某個非零向量 $\mathbf{e}$ 滿足 $\mathbf{A}\mathbf{e} = \lambda\mathbf{e}$，那麼 $\lambda$ 就是 $\mathbf{A}$ 的特徵值。特徵值描述的是：沿著特徵向量方向，$\mathbf{A}$ 每作用一次會把向量乘上多少倍。

  一般來說，奇異值和特徵值**並不相同**。本題中，admissibility 由奇異值 $s_i$ 決定，stability 由特徵值 $\lambda_i$ 決定，所以兩個性質不一定同時成立。這正是 (a) 最後一個問題要我們看清楚的地方。

### (a) 雜訊共變異數與穩定性

* **1. 用 SVD 寫出 $\mathbf{Q}$**

  把 $\mathbf{A} = \mathbf{U}\boldsymbol\Sigma\mathbf{V}^\mathsf{T}$ 代入 $\mathbf{A}\mathbf{A}^\mathsf{T}$。因為 $(\mathbf{U}\boldsymbol\Sigma\mathbf{V}^\mathsf{T})^\mathsf{T} = \mathbf{V}\boldsymbol\Sigma\mathbf{U}^\mathsf{T}$（$\boldsymbol\Sigma$ 是對角矩陣，所以 $\boldsymbol\Sigma^\mathsf{T} = \boldsymbol\Sigma$），而且 $\mathbf{V}$ 是正交矩陣，滿足 $\mathbf{V}^\mathsf{T}\mathbf{V} = \mathbf{I}$，所以

  $$\mathbf{A}\mathbf{A}^\mathsf{T} = \mathbf{U}\boldsymbol\Sigma\mathbf{V}^\mathsf{T}\mathbf{V}\boldsymbol\Sigma\mathbf{U}^\mathsf{T} = \mathbf{U}\boldsymbol\Sigma^2\mathbf{U}^\mathsf{T}$$

  $\mathbf{U}$ 也是正交矩陣，所以單位矩陣可以寫成 $\mathbf{I} = \mathbf{U}\mathbf{U}^\mathsf{T} = \mathbf{U}\mathbf{I}\mathbf{U}^\mathsf{T}$。兩式相減得到

  $$\boxed{\mathbf{Q} = \mathbf{I}_2 - \mathbf{A}\mathbf{A}^\mathsf{T} = \mathbf{U}\left(\mathbf{I}_2 - \boldsymbol\Sigma^2\right)\mathbf{U}^\mathsf{T} = \mathbf{U}\,\mathrm{diag}\!\left(1 - s_1^2,\ 1 - s_2^2\right)\mathbf{U}^\mathsf{T}}$$

* **2. Admissibility 條件**

  上式是 $\mathbf{Q}$ 的特徵分解：$\mathbf{U}$ 的行向量是 $\mathbf{Q}$ 的特徵向量，$\mathbf{Q}$ 的特徵值是 $1 - s_1^2$ 和 $1 - s_2^2$。共變異數矩陣必須半正定，也就是所有特徵值都要 $\ge 0$，所以 $1 - s_i^2 \ge 0$。因為奇異值本身 $s_i \ge 0$，這個條件等價於

  $$\boxed{0 \le s_i \le 1, \quad i = 1, 2} \qquad \left(\text{即 } s_{\max} = \|\mathbf{A}\|_2 \le 1\right)$$

* **3. Asymptotic stability 條件**

  拿掉雜訊後，系統變成 $\mathbf{x}_{n+1} = \mathbf{A}\mathbf{x}_n$，所以 $\mathbf{x}_n = \mathbf{A}^n\mathbf{x}_0$。若 $\mathbf{A}$ 可對角化為 $\mathbf{A} = \mathbf{E}\boldsymbol\Lambda\mathbf{E}^{-1}$，則 $\mathbf{A}^n = \mathbf{E}\boldsymbol\Lambda^n\mathbf{E}^{-1}$，其中 $\boldsymbol\Lambda^n = \mathrm{diag}(\lambda_1^n, \lambda_2^n)$。要讓任意 $\mathbf{x}_0$ 都滿足 $\mathbf{x}_n \to \mathbf{0}$，每一個 $\lambda_i^n$ 都必須趨近於 $0$。特徵值可能是負數或複數，所以條件必須加在絕對值上：

  $$\boxed{|\lambda_i| < 1, \quad i = 1, 2} \qquad \left(\text{即譜半徑 } \rho(\mathbf{A}) < 1\right)$$

  （若 $\mathbf{A}$ 不可對角化，用 Jordan 形式可以得到同樣的條件。）

* **4. Admissibility 能保證 asymptotic stability 嗎？**

  **不能。** 反例是 $\mathbf{A} = \mathrm{diag}(1, 0.5)$。對角矩陣可以取 $\mathbf{U} = \mathbf{V} = \mathbf{I}$，所以奇異值是 $s_1 = 1$、$s_2 = 0.5$，兩者都 $\le 1$，因此 $\mathbf{Q} = \mathrm{diag}(0, 0.75)$ 是 admissible 的。可是 $\mathbf{A}$ 的特徵值是 $\lambda_1 = 1$、$\lambda_2 = 0.5$，其中 $|\lambda_1| = 1$ 不滿足 $|\lambda_i| < 1$，所以系統不是漸近穩定的。

  這個反例落在邊界 $s_{\max} = 1$ 上，這不是巧合。一般來說 $|\lambda_i| \le s_{\max}$，所以只要 $s_{\max} < 1$，就有 $|\lambda_i| < 1$，系統一定穩定。差別只出在等號：admissibility 允許 $s_i = 1$，stability 卻不允許 $|\lambda_i| = 1$。


### (b) 共變異數平衡與邊際模態

#### (b) 的名詞

* **1. $\mathbf{P}_n$ 與 covariance balance（共變異數平衡）**

  $\mathbf{P}_n = \mathbb{E}[\mathbf{x}_n\mathbf{x}_n^\mathsf{T}]$ 是狀態 $\mathbf{x}_n$ 在第 $n$ 步的共變異數矩陣（因為平均為零，二階動差就等於共變異數）。題目要我們推導 $\mathbf{P}_{n+1}$ 和 $\mathbf{P}_n$ 之間的關係式。這個關係式叫做「共變異數平衡」，因為它說明了每一步的變異數由兩個來源組成：一個來源是上一步的變異數經過 $\mathbf{A}$ 傳遞過來的部分，另一個來源是這一步新加入的雜訊。

* **2. Stationary covariance equation（穩態共變異數方程）**

  如果共變異數不再隨時間改變，也就是 $\mathbf{P}_{n+1} = \mathbf{P}_n = \mathbf{P}$，那麼把這個條件代入共變異數平衡式，就會得到一條只有 $\mathbf{P}$ 的方程式。這條方程式叫做穩態共變異數方程。題目要我們驗證：$\mathbf{P} = \mathbf{I}_2$ 是這條方程式的解。

* **3. Marginal mode（邊際模態）**

  $\mathbf{A}$ 的每一個特徵值對應一個「模態」，也就是一個沿特徵向量方向的運動。若 $|\lambda| < 1$，這個模態會衰減；若 $|\lambda| > 1$，這個模態會成長；若 $|\lambda| = 1$，這個模態既不衰減也不成長，我們稱它為**邊際模態**。$\mathbf{A} = \mathrm{diag}(1, 0.5)$ 的第一個分量就是邊際模態。

* **4. $\sup_n \mathbb{E}\|\mathbf{x}_n\|_2^2 < \infty$**

  $\mathbb{E}\|\mathbf{x}_n\|_2^2 = \mathbb{E}[X_{1,n}^2 + X_{2,n}^2] = \mathrm{tr}(\mathbf{P}_n)$ 是兩個分量的變異數總和。$\sup_n$ 是對所有時間步 $n$ 取最小上界。所以 $\sup_n \mathbb{E}\|\mathbf{x}_n\|_2^2 < \infty$ 的意思是：「存在一個固定的上限，使得狀態的總變異數在任何時刻都不會超過它」。換句話說，變異數不會隨時間無限制地長大。

* **5. Stationarity（平穩性）**

  如果一個隨機過程的統計性質不隨時間改變，我們就說它是**平穩的**。更精確地說，把整個過程往後平移任意 $k$ 步，所有的聯合分布都不會改變。對於平均為零的高斯過程，只要檢查兩件事：(i) 每個時刻的共變異數 $\mathbf{P}_n$ 都相同；(ii) 兩個時刻之間的共變異數 $\mathbb{E}[\mathbf{x}_{n+k}\mathbf{x}_n^\mathsf{T}]$ 只跟時間差 $k$ 有關，而跟起點 $n$ 無關。

  **平穩性與漸近穩定性的差別**在於它們描述的對象不同。平穩性描述的是**分布**：它問的是「統計性質會不會隨時間改變」。漸近穩定性描述的是**確定性動力學 $\mathbf{A}$**：它問的是「初始擾動會不會被遺忘」。這兩個性質不一定同時成立，(b) 的例子就是要讓你看到這一點。

#### (b) 填空

* **Step 1：推導共變異數平衡式**

  把 $\mathbf{x}_{n+1} = \mathbf{A}\mathbf{x}_n + \boldsymbol\eta_n$ 代入 $\mathbf{P}_{n+1}$ 的定義，然後展開成四項：

  $$\mathbf{P}_{n+1} = \mathbb{E}\big[(\mathbf{A}\mathbf{x}_n + \boldsymbol{\eta_n})(\mathbf{A}\mathbf{x}_n + \boldsymbol\eta_n)^\mathsf{T}\big] = \mathbf{A}\,\mathbb{E}[\mathbf{x}_n\mathbf{x}_n^\mathsf{T}]\,\mathbf{A}^\mathsf{T} + \mathbf{A}\,\mathbb{E}\big[\mathbf{x}_n \boldsymbol\eta_n^\mathsf{T}\big]+ \mathbb{E}\big[\boldsymbol\eta_n^\mathsf{T}\mathbf{x}_n\big]\,\mathbf{A}^\mathsf{T} + \mathbb{E}[\boldsymbol\eta_n\boldsymbol\eta_n^\mathsf{T}]$$

  > **提示 ①②**：你寫的 $\mathbf{x}_n^\mathsf{T}\boldsymbol\eta_n$ 是一個純量（$1\times 2$ 乘 $2\times 1$），但這裡需要的是 $2\times 2$ 矩陣。請把乘積一項一項展開：$(\mathbf{A}\mathbf{x}_n + \boldsymbol\eta_n)^\mathsf{T} = \mathbf{x}_n^\mathsf{T}\mathbf{A}^\mathsf{T} + \boldsymbol\eta_n^\mathsf{T}$。接著用左邊的 $\mathbf{A}\mathbf{x}_n$ 去乘右邊的 $\boldsymbol\eta_n^\mathsf{T}$，就得到含 $\mathbf{A}$ 在左邊的那一項；再用左邊的 $\boldsymbol\eta_n$ 去乘右邊的 $\mathbf{x}_n^\mathsf{T}\mathbf{A}^\mathsf{T}$，就得到含 $\mathbf{A}^\mathsf{T}$ 在右邊的那一項。期望值裡面的兩個向量分別是誰、順序是什麼？

  中間兩個交叉項等於 $0$：

  理由（用題目給的哪些假設？）④：x和eta獨立，且eta平均為0

  > **提示 ④**：「平均為 0」只用到一半，單靠它不夠。$\mathbb{E}[\mathbf{x}_n\boldsymbol\eta_n^\mathsf{T}]$ 是兩個隨機量乘積的期望值，一般來說 $\mathbb{E}[XY] \ne \mathbb{E}[X]\,\mathbb{E}[Y]$。題目第一段還給了 $\boldsymbol\eta_n$ 和 $\mathbf{x}_n$ 之間的什麼關係，讓你可以把期望值拆成 $\mathbb{E}[\mathbf{x}_n]\,\mathbb{E}[\boldsymbol\eta_n]^\mathsf{T}$？拆開之後，再用「平均為 0」讓它等於 $\mathbf{0}$。（另外，這一步其實用不到「高斯」這個條件。）

  最後一項 $\mathbb{E}[\boldsymbol\eta_n\boldsymbol\eta_n^\mathsf{T}] = \mathbf{Q}$，所以 $\mathbf{P}_{n+1} = \mathbf{A}\mathbf{P}_n\mathbf{A}^\mathsf{T} + \mathbf{Q}$。

* **Step 2：驗證 $\mathbf{P} = \mathbf{I}_2$ 是穩態解**

  令 $\mathbf{P}_{n+1} = \mathbf{P}_n = \mathbf{P}$，穩態共變異數方程為 $\mathbf{P} = \mathbf{A}\mathbf{P}\mathbf{A}^\mathsf{T} + \mathbf{Q}$：

  把 $\mathbf{P} = \mathbf{I}_2$ 代入右邊：$\mathbf{A}\mathbf{I}_2\mathbf{A}^\mathsf{T} + \mathbf{Q} = \mathbf{A}\mathbf{A}^\mathsf{T} + \left(\mathbf{I}_2 - \mathbf{A}\mathbf{A}^\mathsf{T}\right) = \mathbf{I}_2$，和左邊相等。

  為什麼題目要加上「whenever $\mathbf{Q}$ is admissible」？⑨：

  > **提示 ⑨**：$\mathbf{Q}$ 本來就被定義成 $\mathbf{I}_2 - \mathbf{A}\mathbf{A}^\mathsf{T}$，所以上面那行代數對**任何** $\mathbf{A}$ 都成立，這一點不需要 admissible。請想想：如果 $\mathbf{Q}$ 不是半正定的，世界上有沒有一個隨機向量 $\boldsymbol\eta_n$ 的共變異數剛好等於 $\mathbf{Q}$？如果這樣的雜訊不存在，這個模型 $\mathbf{x}_{n+1} = \mathbf{A}\mathbf{x}_n + \boldsymbol\eta_n$ 還有意義嗎？$\mathbf{P} = \mathbf{I}_2$ 這個「解」還能代表某個真實過程的共變異數嗎？

* **Step 3：$\mathbf{A} = \mathrm{diag}(1, 0.5)$ 的初始擾動會衰減嗎？**

  沒有雜訊時，$\mathbf{x}_n = \mathbf{A}^n\mathbf{x}_0$，所以

  $$X_{1,n} = 1^n \cdot X_{1,0}, \qquad X_{2,n} = 0.5^n \cdot X_{2,0}$$

  初始擾動會衰減嗎？（兩個分量分開回答）⑫： $X_{1,n}$ 不會衰減， $X_{2,n}$ 會衰減到 $0$

* **Step 4：$\sup_n \mathbb{E}\|\mathbf{x}_n\|_2^2 < \infty$ 嗎？**

  先算這個例子的雜訊共變異數：$\mathbf{Q} = \mathbf{I}_2 - \mathbf{A}\mathbf{A}^\mathsf{T} = \mathrm{diag}(0,0.75)$。

  因為 $\mathbf{A}$ 和 $\mathbf{Q}$ 都是對角矩陣，共變異數平衡式會拆成兩條純量遞迴式。把 $\mathbf{P}_n$ 的對角元素記為 $P_{11,n}$、$P_{22,n}$：

  * 第一個分量：$P_{11,n+1} = 1^{2} \times P_{11,n}  +0$，所以 $P_{11,n} = P_{11,0}$（用 $P_{11,0}$ 表示）。
  * 第二個分量：$P_{22,n+1} = 0.5^{2} \times\,P_{22,n} + 0.75$。當 $n \to \infty$ 時，$P_{22,n} \to 1$。（提示：令 $P_{22,n+1} = P_{22,n}$，解出不動點。）

  所以 $\mathbb{E}\|\mathbf{x}_n\|_2^2 = P_{11,n} + P_{22,n}$ 有上界嗎？⑲： 有，且上界是 ⑲'：

  > **提示 ⑲'**：「有上界」是對的，但 $P_{11,0}+1$ 不一定是上界。先解出 $P_{22,n}$ 的通式：令 $d_n = P_{22,n} - 1$，證明 $d_{n+1} = 0.25\, d_n$，所以 $P_{22,n} = 1 + 0.25^n(P_{22,0} - 1)$。如果 $P_{22,0} = 5$，$P_{22,n}$ 是從上方還是下方逼近 1？這時 $P_{22,n}$ 的最大值是多少？所以上界應該寫成什麼（可以用 $\max$）？

* **Step 5：若 $\mathbf{x}_0 \sim \mathcal{N}(\mathbf{0}, \mathbf{I}_2)$，過程平穩嗎？**

  此時 $\mathbf{P}_0 = \mathbf{I}_2$。由 Step 2 可知 $\mathbf{P}_n = \boxed{⑳\ \ }$ 對所有 $n$ 都成立。

  > **提示 ⑳**：你寫的是遞迴式本身，它本來就對所有 $n$ 成立，不需要 Step 2。這一格要的是 $\mathbf{P}_n$ 的**具體值**。從 $\mathbf{P}_0 = \mathbf{I}_2$ 開始，用 Step 2 的結果算 $\mathbf{P}_1 = \mathbf{A}\mathbf{I}_2\mathbf{A}^\mathsf{T} + \mathbf{Q} = ?$，再算 $\mathbf{P}_2$，然後用歸納法推廣。

  兩個時刻之間的共變異數為 $\mathbb{E}[\mathbf{x}_{n+k}\mathbf{x}_n^\mathsf{T}] = \boxed{㉑\ \ }\,\mathbf{P}_n$。

  > **提示 ㉑**：$\mathbf{A}^{2k}$ 是從哪裡來的？$\mathbf{P}_{n+1} = \mathbf{A}\mathbf{P}_n\mathbf{A}^\mathsf{T}$ 裡有兩個 $\mathbf{A}$，是因為 $\mathbf{x}_{n+1}$ 在左右**兩邊**都出現。但這裡只有左邊是 $\mathbf{x}_{n+k}$，右邊是 $\mathbf{x}_n^\mathsf{T}$。先寫 $k = 1$：$\mathbb{E}[\mathbf{x}_{n+1}\mathbf{x}_n^\mathsf{T}] = \mathbb{E}[(\mathbf{A}\mathbf{x}_n + \boldsymbol\eta_n)\mathbf{x}_n^\mathsf{T}] = ?$ 再推廣到 $k$。（㉒「是」不受影響，仍然正確。）（提示：把 $\mathbf{x}_{n+k}$ 用 $\mathbf{x}_n$ 和 $\boldsymbol\eta_n, \dots, \boldsymbol\eta_{n+k-1}$ 表示，再利用 Step 1 的理由丟掉雜訊項。）這個結果只跟 $k$ 有關嗎？㉒：是

  所以過程平穩嗎？㉓：是吧(?)

* **Step 6：平穩性與漸近穩定性的差別**

  這個例子是平穩的，但它是漸近穩定的嗎？㉔：不是，因為不同的初始X都沒有收斂到相同的數值

  請用一兩句話說明：第一個分量 $X_{1,n}$ 在整個過程中發生了什麼事？為什麼它的分布不變，但它卻從來沒有「忘記」初始值？㉕：分布不改變因為x的期望變異數矩陣並不會改變，沒有忘記因為都是A都是在乘1

  如果改成 $\mathbf{x}_0 \sim \mathcal{N}(\mathbf{0}, \mathrm{diag}(4, 1))$，$P_{11,n}$ 會收斂到 1 嗎？這說明了什麼？㉖：

  > **提示 ㉖**：$\mathbf{Q} = \mathbf{I}_2 - \mathbf{A}\mathbf{A}^\mathsf{T}$ 只跟 $\mathbf{A}$ 有關，跟初始分布 $\mathbf{x}_0$ 完全無關，所以改 $\mathbf{x}_0$ 不會影響 $\mathbf{Q}$ 是否 admissible。請直接用你在 ⑮ 得到的 $P_{11,n} = P_{11,0}$ 代入 $P_{11,0} = 4$：$P_{11,n}$ 會變成多少？會收斂到 1 嗎？再對比 $P_{22,n}$：不管 $P_{22,0}$ 是多少，它都會收斂到 1。這說明了：$\mathbf{P} = \mathbf{I}_2$ 雖然是穩態解，但只有「剛好從它出發」才會停在那裡。對一個漸近穩定的系統，從任何初始共變異數出發都會被「吸」到穩態，這個例子的第一個分量卻不會。


## Question 2. One-dimensional DDPM

Let $x_0$ be a scalar sample from the bimodal data distribution

$$q_{\mathrm{data}}(x) = \tfrac{1}{2}\mathcal{N}(x; -2, 0.25) + \tfrac{1}{2}\mathcal{N}(x; 2, 0.25),$$

where $\mathcal{N}(x; \mu, v)$ denotes a Gaussian density with mean $\mu$ and variance $v$. A denoising diffusion probabilistic model (DDPM) uses the forward process

$$x_t = \sqrt{\alpha_t}\, x_{t-1} + \sqrt{\beta_t}\, \xi_t, \qquad \alpha_t = 1 - \beta_t, \qquad \bar\alpha_t = \prod_{s=1}^{t} \alpha_s,$$

where $0 < \beta_t < 1$ and $\xi_t \overset{\text{iid}}{\sim} \mathcal{N}(0, 1)$ are independent of $x_0$. The index $t = 1, \dots, T$ denotes a diffusion step.

* (a) **Forward distribution.** Derive the conditional distribution $q(x_t \mid x_0)$ and show that $x_t$ can be sampled directly using $x_t = \sqrt{\bar\alpha_t}\, x_0 + \sqrt{1 - \bar\alpha_t}\, \epsilon$, $\epsilon \sim \mathcal{N}(0, 1)$. For fixed $x_0$, what happens to this distribution as $\bar\alpha_t \to 0$?
* (b) **Training target and conditional probabilities.** A neural network $\epsilon_\theta(x_t, t)$, with trainable parameters $\theta$, predicts noise from $x_t$ and $t$. Write its mean squared error training objective, with $x_0 \sim q_{\mathrm{data}}$, $t \sim \mathrm{Uniform}\{1, \dots, T\}$, and $\epsilon \sim \mathcal{N}(0, 1)$ sampled independently. Does its target $\epsilon$ represent the noise added only during $t-1 \to t$, or the standardized accumulated noise in part (a)? For $x_0 = 2$, $\bar\alpha_t = 0.64$, and $\epsilon = -1$, calculate $x_t$. If $\epsilon_\theta(x_t, t) = -0.8$, calculate the squared error. Explain the distinction between $q(x_{t-1} \mid x_t, x_0)$ and $p_\theta(x_{t-1} \mid x_t)$. Why can generation not require the original $x_0$ as input?
* (c) **Reverse sampling.** Use the supplied reverse mean $\mu_\theta(x_t, t) = \frac{1}{\sqrt{\alpha_t}}\left[x_t - \frac{\beta_t}{\sqrt{1 - \bar\alpha_t}}\epsilon_\theta(x_t, t)\right]$. For $t > 1$, sample $x_{t-1} = \mu_\theta(x_t, t) + \sigma_t z_t$, $z_t \sim \mathcal{N}(0, 1)$, where $\sigma_t$ is a prescribed reverse standard deviation and the $z_t$ are fresh independent draws. At $t = 1$, return $\mu_\theta(x_1, 1)$ without adding noise. Assuming $\bar\alpha_T$ is sufficiently small, write pseudocode for generating one new sample, including its starting distribution. Explain why generation does not retrace the exact forward noise realization of a training sample.

### 中文翻譯

> **問題 2：一維 DDPM**
>
> 令 $x_0$ 為來自雙峰資料分布 $q_{\mathrm{data}}(x) = \tfrac{1}{2}\mathcal{N}(x; -2, 0.25) + \tfrac{1}{2}\mathcal{N}(x; 2, 0.25)$ 的純量樣本，其中 $\mathcal{N}(x; \mu, v)$ 表示平均 $\mu$、變異數 $v$ 的高斯密度。去噪擴散機率模型（DDPM）使用前向過程 $x_t = \sqrt{\alpha_t}\, x_{t-1} + \sqrt{\beta_t}\, \xi_t$，$\alpha_t = 1 - \beta_t$，$\bar\alpha_t = \prod_{s=1}^{t} \alpha_s$，其中 $0 < \beta_t < 1$，$\xi_t$ 為獨立同分布的 $\mathcal{N}(0, 1)$ 且與 $x_0$ 獨立。指標 $t = 1, \dots, T$ 代表擴散步。
>
> * (a) **前向分布**：推導條件分布 $q(x_t \mid x_0)$，並證明 $x_t$ 可直接用 $x_t = \sqrt{\bar\alpha_t}\, x_0 + \sqrt{1 - \bar\alpha_t}\, \epsilon$ 抽樣。固定 $x_0$ 時，當 $\bar\alpha_t \to 0$ 這個分布會變成什麼？
> * (b) **訓練目標與條件機率**：神經網路 $\epsilon_\theta(x_t, t)$（可訓練參數 $\theta$）由 $x_t$ 與 $t$ 預測雜訊。寫出它的均方誤差訓練目標，其中 $x_0 \sim q_{\mathrm{data}}$、$t \sim \mathrm{Uniform}\{1, \dots, T\}$、$\epsilon \sim \mathcal{N}(0, 1)$ 彼此獨立抽樣。目標 $\epsilon$ 代表的是只在 $t-1 \to t$ 加入的雜訊，還是 (a) 中標準化後的累積雜訊？若 $x_0 = 2$、$\bar\alpha_t = 0.64$、$\epsilon = -1$，計算 $x_t$；若 $\epsilon_\theta(x_t, t) = -0.8$，計算平方誤差。說明 $q(x_{t-1} \mid x_t, x_0)$ 與 $p_\theta(x_{t-1} \mid x_t)$ 的差別。為什麼生成時不能需要原始的 $x_0$ 當輸入？
> * (c) **反向抽樣**：使用給定的反向平均 $\mu_\theta(x_t, t)$。對 $t > 1$，抽樣 $x_{t-1} = \mu_\theta(x_t, t) + \sigma_t z_t$，$z_t \sim \mathcal{N}(0, 1)$，其中 $\sigma_t$ 為指定的反向標準差，$z_t$ 每次重新獨立抽取。在 $t = 1$ 時回傳 $\mu_\theta(x_1, 1)$，不加雜訊。假設 $\bar\alpha_T$ 夠小，寫出生成一個新樣本的虛擬碼（含起始分布）。解釋為何生成過程不會重走某個訓練樣本當初的前向雜訊路徑。


## Answer 2.

（待填）
