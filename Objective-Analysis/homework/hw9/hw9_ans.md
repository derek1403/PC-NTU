# Objective Analysis Week 09 Homework — 解答

題目見 [Week09.11,04.pdf](Week09.11,04.pdf)；程式 [hw9_q1.py](hw9_q1.py)。

> **待補**：本機沒有 `W.nc`。把檔案放進 hw9 資料夾後執行 `py -X utf8 hw9_q1.py`，再把輸出的數字填入標 ▢ 的地方。程式已經用模擬資料測試過，所有檢查都通過。

---

## (a) 資料準備

* 資料來源、單位、座標範圍、取樣間隔：▢（程式開頭會印出 `ds`、`units`、各維度範圍，以及 `np.diff(time)`）
* 維度 (time, level, lat, lon) = ▢
* 只保留在**所有**時間、所有層都是有限值的水平格點（`np.all(np.isfinite)`），不把缺值補成 0。保留格點數 $R$ = ▢
* 在每個格點、每一層分別扣掉時間平均：$\omega'(t,p,\mathbf r)=\omega-\overline{\omega}(p,\mathbf r)$
* **樣本排序**：time 為外層、space 為內層，第 $(t,\mathbf r)$ 個樣本在第 $i_t R + i_r$ 列。$X\in\mathbb R^{N\times L}$，其中 $N=N_t\times R$ = ▢，$L$ = 層數 ▢
* 驗證各欄平均約為 0：$\max_j|\bar X_{:,j}|$ ≈ ▢（應為 $10^{-16}$–$10^{-12}$ 量級）

## (b) 共變異矩陣特徵分解

$C=\frac{1}{N-1}X^TX$（$L\times L$，對稱半正定）。用 `np.linalg.eigh` 求特徵值，並由大到小排序。`eigh` 回傳的特徵向量已經是正交歸一的，即 $e_i^Te_j=\delta_{ij}$。PC 為 $a_k=Xe_k$。

**驗證 PC 的變異數等於特徵值**：$X$ 的各欄平均為 0，所以 $a_k$ 的平均也是 0。

$$
\text{Var}(a_k)=\frac{a_k^Ta_k}{N-1}=e_k^T\frac{X^TX}{N-1}e_k=e_k^TCe_k=\lambda_k
$$

數值結果：$\max|\text{Var}(a_k)-\lambda_k|/\lambda_1$ ≈ ▢（機器精度）

## (c) SVD

使用 economy SVD：$X=U\Sigma V^T$，其中 $U\in\mathbb R^{N\times L}$，$\Sigma=\text{diag}(\sigma_1\ge\dots\ge\sigma_L)$，$V\in\mathbb R^{L\times L}$。

$$
C=\frac{X^TX}{N-1}=\frac{V\Sigma U^TU\Sigma V^T}{N-1}=V\,\frac{\Sigma^2}{N-1}\,V^T
$$

上式正是 $C$ 的特徵分解，因此：

* $\boxed{\lambda_k=\sigma_k^2/(N-1)}$
* **右奇異向量 $v_k$ 就是垂直 EOF $e_k$**
* PC：$a_k=Xv_k=U\Sigma V^Tv_k=\boxed{\sigma_k u_k}$，也就是 $A=U\Sigma$

**為什麼兩種方法等價**：兩者都得到 $X^TX$ 的同一個特徵分解，差別只在 SVD 沒有直接算出 $X^TX$ 這個矩陣。剩下的不確定性有兩種：

* $(u_k,v_k)\to(-u_k,-v_k)$ 時 $X$ 不變，所以 EOF 與 PC 的符號是任意的。
* 若有重複的特徵值，該特徵子空間內任何正交基都合法，因此可能相差一個旋轉。

數值上，SVD 不必形成 $X^TX$，避免了條件數平方化，所以比較穩定。

數值結果（符號對齊後）：$\max|V-E|$ ≈ ▢，$\max|U\Sigma-XE|$ ≈ ▢，$\max|\sigma_k^2/(N-1)-\lambda_k|$ ≈ ▢

兩種方法在程式裡分開計算（`eigh` 與 `svd`），沒有使用任何 EOF 或 PCA 套件。

## (d) 解釋變異比例

$$
f_k=\frac{\lambda_k}{\sum_j\lambda_j}=\frac{\sigma_k^2/(N-1)}{\sum_j\sigma_j^2/(N-1)}=\boxed{\frac{\sigma_k^2}{\sum_{j=1}^L\sigma_j^2}}
$$

另外 $\sum_j\sigma_j^2=\|X\|_F^2=(N-1)\,\text{tr}(C)$，也就是總異常變異。

* $f_k$（%）= ▢
* 兩種方法的 $\max|f^{\text{eig}}_k-f^{\text{svd}}_k|$ ≈ ▢（約 $10^{-16}$）
* $K_{90}$ = ▢，兩種方法相同 ▢（差異只在機器精度，除非某個 $F_K$ 剛好非常接近 90%）

![variance](q1_variance.png)

附圖：前三個 EOF 的垂直剖面 [q1_eofs.png](q1_eofs.png)。EOF1 通常是單峰的深對流結構，峰值在 400–500 hPa，各層同號（$\omega<0$ 代表整層上升）。EOF2 通常是上下反號的 top-heavy／bottom-heavy 雙峰結構（▢ 依實際結果描述）。
