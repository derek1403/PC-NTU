# Objective Analysis Week 11 — 題目中文版與說明

原文見 [Week11.pdf](Week11.pdf)，解答見 [hw11_ans.md](hw11_ans.md)。每一小題先列出題目翻譯，再以「💡 題目在問什麼」說明它的用意。

---

## Question 1. k-means、SOM 與 VAE 的比較

### 符號與定義

$X$ 是 $[M\times N]$ 的零平均距平矩陣（$M$ 個觀測 × $N$ 個格點），第 $n$ 列 $x_n$ 是第 $n$ 個觀測，向量長度定義為 $\|v\|=\sqrt{\sum_d v_d^2}$。

* **k-means（Part 6）**：把 $M$ 個觀測分成 $k$ 個互斥的群 $S_1,\dots,S_k$，並最小化群內平方和 $J=\sum_i\sum_{x_n\in S_i}\|x_n-\mu_i\|^2$，其中 $\mu_i$ 是群內平均。
* **Batch SOM（Part 6）**：把 $k=m\times p$ 個節點 $n_j$ 排在二維格子上，格子座標為 $g_j$。每個觀測被分配到距離最近的節點，也就是它的 Best Match Unit（BMU）$c(n)=\arg\min_j\|x_n-n_j\|^2$。鄰域函數是高斯函數 $h_{ij}=\exp(-\|g_i-g_j\|^2/2\sigma^2)$。Batch SOM 最小化鄰域加權的失真 $E=\sum_n\sum_j h_{c(n)j}\|x_n-n_j\|^2$，迭代公式是 $n_j\leftarrow\sum_n h_{c(n)j}x_n/\sum_n h_{c(n)j}$。訓練完成後用兩個診斷量評估：
  * 量化誤差 $E_q=\frac1M\sum_n\|x_n-n_{c(n)}\|$，也就是觀測到其 BMU 的平均距離。
  * 拓撲誤差 $E_t$：第一與第二 BMU 在格子上「不是上下左右相鄰」（$\|g_{c_1}-g_{c_2}\|_1>1$）的觀測比例。
* **VAE（Part 7）**：encoder 把 $x_n$ 映射到 $k$ 維連續 latent space 中的對角高斯分佈 $q_\phi(z|x_n)=\mathcal N(\mu_\phi,\mathrm{diag}\,\sigma_\phi^2)$，再以 reparameterization trick 抽樣 $z_n=\mu_\phi+\sigma_\phi\odot\epsilon_n$。decoder $g_\theta(z)$ 重建資料，觀測雜訊變異數 $\sigma_x^2$ 固定。訓練目標是負 ELBO：$L_{\rm VAE}=\frac{1}{2\sigma_x^2M}\sum_n\|x_n-\hat x_n\|^2+D_{\rm KL}$。

> 💡 **整體在問什麼**：這三種方法都是在用「少量的代表」來描述資料。k-means 用 $k$ 個彼此無關的離散中心；SOM 也用 $k$ 個離散中心，但規定它們排在一張格子上，相鄰的節點必須相似；VAE 則改用 $k$ 維連續座標，再由非線性 decoder 映回資料空間。這一題要你看出它們在「重建誤差」與「結構（拓撲、連續性）」之間各自做了什麼取捨。

---

## (a) k-means vs. Batch SOM

使用 `eof_scatter_2d.py` 的 8 點二維資料（$M=8,N=2$）。

* **基準 k-means（$k=4$）**：以 `n_init=50`、固定 seed 執行，並報告 4 個 centroid、群內平方和 $J$，以及到最近 centroid 的平均距離 $E_q$。
* **Batch SOM 鄰域寬度掃描（2×2 格子）**：初始節點為 $n_{(0,0)}=(-3,-3)$、$n_{(0,1)}=(-1,1)$、$n_{(1,0)}=(1,-1)$、$n_{(1,1)}=(3,3)$。分別在 $\sigma=2.0,\ 0.8,\ 0.05$ 下執行 Batch SOM 直到收斂。
* **作圖與表格**：
  1. 1×4 子圖：畫出 k-means 的 4 個 centroid，以及三種 $\sigma$ 訓練後的 SOM 節點；格子上相鄰的節點要用線連起來，以顯示地圖的拓撲。
  2. 摘要表：列出 k-means 與每個 SOM 的 $(J_{\rm BMU},E_q,E_t)$，其中 $J_{\rm BMU}=\sum_n\|x_n-n_{c(n)}\|^2$。
* 用數值驗證：當 $\sigma\to0$ 時，Batch SOM 會回到 k-means 的 centroid 與 $J=16$，但代價是拓撲誤差 $E_t$ 不為零。

> 💡 **題目在問什麼**：$\sigma$ 控制「節點被鄰居拉住的程度」。$\sigma$ 大時，每個節點的更新都混入了大量其他節點的資料，節點會往整體平均收縮；地圖很平滑、拓撲有序，但重建誤差大。$\sigma\to0$ 時 $h_{ij}\to\delta_{ij}$，迭代公式退化成 k-means 的 Lloyd 更新，於是重建誤差最小，但格子上的鄰居關係不再受到任何約束。

## (b) k-means vs. VAE

同樣使用這 8 點資料。

* **離散基準**：k-means，$k=2$（`n_init=50`、固定 seed）。
* **VAE**：latent 維度為 1；例如 encoder 與 decoder 各有一層 16 個 tanh 單元，decoder 雜訊變異數固定為 $\sigma_x^2=0.5$，用 Adam 訓練 2000 個 epoch，seed 固定。
* **作圖與表格**：
  1. 1×2 子圖。左圖（1D latent space）：畫出標準常態先驗 $\mathcal N(0,1)$，以及 8 個點的 posterior mean $\mu_\phi(x_n)$ 與 $\pm\sigma_\phi(x_n)$ 誤差棒，並依 $k=2$ 的分群結果著色。右圖（2D data space）：畫出 8 個觀測、2 個 k-means centroid（星號）、$z\in[-2.5,2.5]$ 時的連續流形曲線 $g_\theta(z)$，以及從先驗抽出 100 個 $z$ 解碼得到的新狀態。
  2. 摘要表：比較 k-means 與 VAE 的 MSE 與解釋變異比例 $R^2$；VAE 的重建使用確定性解碼 $\hat x_n=g_\theta(\mu_\phi(x_n))$。

> 💡 **題目在問什麼**：k-means 只能把每個點對應到 2 個點中的一個；VAE 用一個連續參數 $z$ 走過一條彎曲的曲線，所以能把每個點放到「曲線上最近的位置」。這一題要你比較「離散分類」與「連續非線性降維」的重建能力，並觀察 VAE 是一個生成模型：從先驗抽樣就能產生新的、落在資料流形上的狀態。

## (c) 應用於 ERA5 $Z_{200}$ 距平

讀取 ERA5 冬季（DJF，1979–2021）200 hPa 重力位高度距平（變數 `z200_anom`，單位 m），整理成 $[M\times N]=[\text{時間}\times\text{格點}]$，並乘上面積權重 $\sqrt{\cos\theta}$ 得到 $X_w$。

* **模型訓練（$k=4$）**：在 $X_w$ 上訓練 (a) k-means，$k=4$，`n_init=20`；(b) Batch SOM，2×2，$\sigma=0.8$；(c) VAE，4 維連續 latent，$\sigma_x^2$ 設為 $X_w$ 各格點變異數的平均，讓重建項與 KL 項有合理的相對尺度。
* **場重建**：對全部 $M$ 個冬季日重建距平場 $\hat X$（m）：k-means 用所屬 centroid、SOM 用 BMU 節點、VAE 用 $g_\theta(\mu_\phi(x_n))$。
  1. 摘要表：報告三種方法的面積加權 RMSE（m）與解釋變異比例 $R^2_{\rm recon}=1-\|X_w-\hat X_w\|_F^2/\|X_w\|_F^2$。
  2. 極端日地圖（1×4）：選出空間距平振幅最大（$\max_n\|x_{n,w}\|$）的那一天，畫出觀測、k-means regime、SOM BMU、VAE 重建四張圖，並在標題寫出每張重建圖與觀測的空間型態相關 $r$。

> 💡 **題目在問什麼**：在真實資料上，k-means 與 SOM 都只能用 4 張固定的地圖去代表每一天，所以極端日的振幅一定被嚴重低估；VAE 雖然也只有 4 個自由度，但它是連續的，可以調整振幅與型態。題目要你量化這三者在重建能力上的差距，並在單一極端事件上直觀地看到差異。
