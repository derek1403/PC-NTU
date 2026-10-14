# T2 小考 Q2 解答：迴歸斜率的 pairs bootstrap 信賴區間
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

n = 50
B = 1000
rng = np.random.default_rng(0)

# 依照題目指定的順序產生資料
x = rng.uniform(-1, 1, n)
eps = rng.normal(0, 1, n)
y = 1 + 0.5 * x + eps


# OLS：回傳截距、斜率、斜率標準誤
def ols(x, y):
    xm = np.mean(x)
    ym = np.mean(y)
    Sxx = np.sum((x - xm) ** 2)
    b = np.sum((x - xm) * (y - ym)) / Sxx
    a = ym - b * xm
    resid = y - (a + b * x)
    s2 = np.sum(resid**2) / (len(x) - 2)
    se_b = np.sqrt(s2 / Sxx)
    return a, b, se_b


# (a) OLS 與傳統 95% 信賴區間
a_hat, b_hat, se_b = ols(x, y)
t_crit = stats.t.ppf(0.975, n - 2)
ci_ols = [b_hat - t_crit * se_b, b_hat + t_crit * se_b]
print("a_hat = %.4f, b_hat = %.4f, SE = %.4f, t_crit = %.4f" % (a_hat, b_hat, se_b, t_crit))
print("OLS 95%% CI       = [%.4f, %.4f]" % (ci_ols[0], ci_ols[1]))

# (b) pairs bootstrap：同一組索引同時抽 x 與 y
b_boot = np.zeros(B)
for j in range(B):
    idx = rng.integers(0, n, n)
    a_j, b_j, se_j = ols(x[idx], y[idx])
    b_boot[j] = b_j

ci_boot = np.percentile(b_boot, [2.5, 97.5])
print("bootstrap 斜率標準差 = %.4f" % np.std(b_boot, ddof=1))
print("bootstrap 95%% CI = [%.4f, %.4f]" % (ci_boot[0], ci_boot[1]))

# 畫圖
plt.hist(b_boot, bins=30, color="lightgray", edgecolor="gray")
plt.axvline(b_hat, color="r", lw=2, label="b_hat")
plt.axvline(ci_boot[0], color="b", ls="--", label="bootstrap 95% CI")
plt.axvline(ci_boot[1], color="b", ls="--")
plt.xlabel("bootstrap slope")
plt.legend()
plt.savefig("sol_q2.png", dpi=120)
