# T2 小考 Q3 解答：AR(1) 誤差下，OLS t 檢定的誤拒絕率
import numpy as np
from scipy import stats

n = 100
M = 1000
x = np.linspace(-1, 1, n)
t_crit = stats.t.ppf(0.975, n - 2)
rng = np.random.default_rng(0)


# 產生 AR(1) 誤差（穩態變異數 = 1）
def ar1_noise(phi):
    eps = np.zeros(n)
    eps[0] = rng.normal(0, 1)
    u = rng.normal(0, np.sqrt(1 - phi**2), n)
    for t in range(1, n):
        eps[t] = phi * eps[t - 1] + u[t]
    return eps


# OLS：回傳斜率與斜率標準誤
def ols_slope(x, y):
    xm = np.mean(x)
    ym = np.mean(y)
    Sxx = np.sum((x - xm) ** 2)
    b = np.sum((x - xm) * (y - ym)) / Sxx
    a = ym - b * xm
    resid = y - (a + b * x)
    s2 = np.sum(resid**2) / (n - 2)
    return b, np.sqrt(s2 / Sxx)


print("t_crit = %.4f" % t_crit)
for phi in [0.0, 0.8]:
    b_all = np.zeros(M)
    se_all = np.zeros(M)
    for j in range(M):
        y = 1 + 0.0 * x + ar1_noise(phi)       # H0 為真：b = 0
        b_all[j], se_all[j] = ols_slope(x, y)

    reject = np.mean(np.abs(b_all / se_all) > t_crit)
    print("phi = %.1f: 誤拒絕率 = %.3f, 斜率真實標準差 = %.4f, SE_OLS 平均 = %.4f, 比值 = %.2f"
          % (phi, reject, np.std(b_all, ddof=1), np.mean(se_all), np.std(b_all, ddof=1) / np.mean(se_all)))
