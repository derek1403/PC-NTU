# HW5 Q1：迴歸斜率的 bootstrap 信賴區間
# 執行方式：在 hw5 資料夾輸入  py hw5_q1.py
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

SEED = 2026
n = 200
B = 2000
rng = np.random.default_rng(SEED)

# 兩種情況共用同一組 x 與誤差，只有真實斜率 b 不同，方便比較
x = rng.uniform(-1, 1, n)
eps = rng.normal(0, 1, n)


# OLS 擬合 y = a + b x，回傳截距、斜率、斜率的標準誤
def ols(x, y):
    xm = np.mean(x)
    ym = np.mean(y)
    Sxx = np.sum((x - xm) ** 2)
    b = np.sum((x - xm) * (y - ym)) / Sxx
    a = ym - b * xm
    resid = y - (a + b * x)
    s2 = np.sum(resid**2) / (len(x) - 2)      # 殘差變異數（自由度 n-2）
    se_b = np.sqrt(s2 / Sxx)                  # SE_OLS(b_hat)
    return a, b, se_b


b_list = [0.0, 0.4]
fig1, axes1 = plt.subplots(1, 2, figsize=(11, 4.5))   # (a) 散布圖 + 擬合線
fig2, axes2 = plt.subplots(1, 2, figsize=(11, 4.5))   # (b) bootstrap 斜率分布

t_crit = stats.t.ppf(0.975, n - 2)          # t_{0.975, n-2}
print("seed =", SEED, " n =", n, " B =", B, " t_crit = %.4f" % t_crit)

for k in range(2):
    b_true = b_list[k]
    y = 1 + b_true * x + eps

    # ===== (a) OLS =====
    a_hat, b_hat, se_b = ols(x, y)

    # ===== (b) pairs bootstrap：用同一組索引同時抽 x 和 y =====
    b_boot = np.zeros(B)
    for j in range(B):
        idx = rng.integers(0, n, n)          # 有放回地抽 n 個索引
        a_j, b_j, se_j = ols(x[idx], y[idx])
        b_boot[j] = b_j

    # ===== (c) 信賴區間 =====
    ci_boot = np.percentile(b_boot, [2.5, 97.5])               # percentile bootstrap CI
    ci_ols = [b_hat - t_crit * se_b, b_hat + t_crit * se_b]   # 傳統 OLS CI

    print("\n===== b = %.1f =====" % b_true)
    print("OLS: a_hat = %.4f, b_hat = %.4f, SE_OLS = %.4f" % (a_hat, b_hat, se_b))
    print("bootstrap 斜率: 平均 = %.4f, 標準差 = %.4f" % (np.mean(b_boot), np.std(b_boot, ddof=1)))
    print("95%% bootstrap CI = [%.4f, %.4f]  寬度 = %.4f" % (ci_boot[0], ci_boot[1], ci_boot[1] - ci_boot[0]))
    print("95%% OLS CI       = [%.4f, %.4f]  寬度 = %.4f" % (ci_ols[0], ci_ols[1], ci_ols[1] - ci_ols[0]))

    # 畫 (a)
    xg = np.linspace(-1, 1, 100)
    ax = axes1[k]
    ax.scatter(x, y, s=12, color="gray", label="observations")
    ax.plot(xg, a_hat + b_hat * xg, "r-", lw=2, label="OLS: y = %.3f + %.3f x" % (a_hat, b_hat))
    ax.set_title("b = %.1f" % b_true)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend()

    # 畫 (b)(c)
    ax = axes2[k]
    ax.hist(b_boot, bins=40, density=True, color="lightgray", edgecolor="gray", label="bootstrap slopes")
    ax.axvline(b_hat, color="r", lw=2, label="b_hat = %.3f" % b_hat)
    ax.axvline(ci_boot[0], color="b", ls="--", label="bootstrap 95% CI")
    ax.axvline(ci_boot[1], color="b", ls="--")
    ax.axvline(ci_ols[0], color="g", ls=":", lw=2, label="OLS 95% CI")
    ax.axvline(ci_ols[1], color="g", ls=":", lw=2)
    ax.set_title("bootstrap distribution of slope (b = %.1f)" % b_true)
    ax.set_xlabel("slope b*")
    ax.legend(fontsize=8)

fig1.tight_layout()
fig1.savefig("q1_fit.png", dpi=150)
fig2.tight_layout()
fig2.savefig("q1_bootstrap.png", dpi=150)
