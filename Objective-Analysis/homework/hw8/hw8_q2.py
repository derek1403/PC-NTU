# HW8 Q2(b)：Lag-1 Granger causality 數值實驗
# 執行方式：在 hw8 資料夾輸入  py hw8_q2.py
import numpy as np
import matplotlib.pyplot as plt

N = 200
SEED = 42
alphas = [0.1, 0.3, 0.5, 0.7, 0.9]
betas = [0.1, 0.3, 0.5, 0.7, 0.9]


# 產生 y（先）與 eta（後），每組參數都重設 seed
def simulate(alpha, beta, N=N, seed=SEED):
    rng = np.random.default_rng(seed)
    y = np.empty(N)
    y[0] = rng.standard_normal()                 # y_1 ~ N(0,1)
    eps = rng.standard_normal(N - 1)             # eps_2, ..., eps_N
    for t in range(1, N):
        y[t] = alpha * y[t - 1] + np.sqrt(1 - alpha**2) * eps[t - 1]
    eta = rng.standard_normal(N)                 # eta_1, ..., eta_N
    x = beta * y + eta
    return y, x


# 置中後的 OLS（等價於含截距），回傳 R^2
def r2_ols(target, *predictors):
    yc = target - target.mean()
    X = np.column_stack([p - p.mean() for p in predictors])
    coef, *_ = np.linalg.lstsq(X, yc, rcond=None)
    resid = yc - X @ coef
    return 1 - np.sum(resid**2) / np.sum(yc**2)


R2_R = np.zeros((len(alphas), len(betas)))
R2_U = np.zeros_like(R2_R)

for i, a in enumerate(alphas):
    for j, b in enumerate(betas):
        y, x = simulate(a, b)
        yt, ylag, xlag = y[1:], y[:-1], x[:-1]   # t = 2..N，共 N-1 筆
        R2_R[i, j] = r2_ols(yt, ylag)
        R2_U[i, j] = r2_ols(yt, ylag, xlag)

dR2 = R2_U - R2_R

np.set_printoptions(precision=4, suppress=True)
print("R2_R (rows: alpha, cols: beta)\n", R2_R)
print("R2_U\n", R2_U)
print("Delta R2\n", dR2)
print("母體值 alpha^2:", np.array(alphas) ** 2)
print("R2_U 沿 beta 的最大差異:", np.max(np.ptp(R2_U, axis=1)))

# ---- 三張熱圖 ----
fig, axes = plt.subplots(1, 3, figsize=(15, 4.5), constrained_layout=True)
panels = [
    (R2_R, r"$R^2_R$", "viridis", "{:.3f}"),
    (R2_U, r"$R^2_U$", "viridis", "{:.3f}"),
    (dR2, r"$\Delta R^2 = R^2_U - R^2_R$", "magma", "{:.4f}"),
]
for ax, (Z, title, cmap, fmt) in zip(axes, panels):
    if Z is dR2:
        im = ax.imshow(Z, origin="lower", cmap=cmap)
    else:
        im = ax.imshow(Z, origin="lower", cmap=cmap, vmin=0, vmax=max(R2_R.max(), R2_U.max()))
    ax.set_xticks(range(len(betas)), betas)
    ax.set_yticks(range(len(alphas)), alphas)
    ax.set_xlabel(r"$\beta$")
    ax.set_ylabel(r"$\alpha$")
    ax.set_title(title)
    for i in range(len(alphas)):
        for j in range(len(betas)):
            v = Z[i, j]
            color = "white" if v < 0.5 * Z.max() else "black"
            ax.text(j, i, fmt.format(v), ha="center", va="center", color=color, fontsize=9)
    fig.colorbar(im, ax=ax, shrink=0.85)

fig.suptitle(f"Lag-1 Granger regression, N = {N}, seed = {SEED}")
fig.savefig("q2_heatmaps.png", dpi=150)
print("已存檔 q2_heatmaps.png")
