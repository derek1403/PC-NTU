# HW5 Q2：誤差為 AR(1) 時的迴歸顯著性檢定
# 執行方式：在 hw5 資料夾輸入  py hw5_q2.py
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

SEED = 2026
n = 200
B = 2000
rng = np.random.default_rng(SEED)

t_idx = np.arange(1, n + 1)
x = -1 + 2 * (t_idx - 1) / (n - 1)        # x 從 -1 到 1 等間距


# 產生 AR(1) 誤差：eps_1 ~ N(0,1)，eps_t = phi*eps_{t-1} + u_t，u_t ~ N(0, 1-phi^2)
def ar1_noise(phi):
    eps = np.zeros(n)
    eps[0] = rng.normal(0, 1)
    u = rng.normal(0, np.sqrt(1 - phi**2), n)
    for t in range(1, n):
        eps[t] = phi * eps[t - 1] + u[t]
    return eps


# OLS 擬合 y = a + b x，回傳截距、斜率、斜率的標準誤
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


phi_list = [0.0, 0.5, 0.9]
t_crit = stats.t.ppf(0.975, n - 2)
print("seed =", SEED, " n =", n, " B =", B, " t_crit = %.4f" % t_crit)

fig, axes = plt.subplots(1, 3, figsize=(15, 4.5))

for k in range(3):
    phi = phi_list[k]

    # ===== (a) 原始資料與 OLS =====
    y = 1 + 0.4 * x + ar1_noise(phi)
    a_hat, b_hat, se_b = ols(x, y)

    # ===== (b-1) 傳統 OLS t 檢定 =====
    T = b_hat / se_b
    p_ols = 2 * stats.t.sf(abs(T), n - 2)     # 雙尾 p 值

    # ===== (b-2) 在 H0 (b = 0) 下產生 B 筆替代資料 =====
    b_null = np.zeros(B)
    se_null = np.zeros(B)
    for j in range(B):
        y0 = 1 + 0.0 * x + ar1_noise(phi)     # 把 0.4 換成 0，其餘都一樣
        a0, b0, se0 = ols(x, y0)
        b_null[j] = b0
        se_null[j] = se0

    p_sur = np.mean(np.abs(b_null) >= abs(b_hat))     # 替代資料的雙尾 p 值
    crit_sur = np.percentile(np.abs(b_null), 95)      # |b| 的 5% 臨界值
    sd_null = np.std(b_null, ddof=1)                  # H0 下斜率的真實分散程度
    # H0 為真時，傳統 t 檢定誤拒絕 H0 的比例（理想上應該是 5%）
    reject_rate = np.mean(np.abs(b_null / se_null) > t_crit)

    print("\n===== phi = %.1f =====" % phi)
    print("b_hat = %.4f, SE_OLS = %.4f, T = %.3f, OLS p = %.2e  -> %s"
          % (b_hat, se_b, T, p_ols, "拒絕 H0" if p_ols < 0.05 else "不拒絕 H0"))
    print("替代資料: 斜率標準差 = %.4f (SE_OLS 的 %.2f 倍), |b| 臨界值 = %.4f"
          % (sd_null, sd_null / se_b, crit_sur))
    print("替代資料 p = %.4f  -> %s" % (p_sur, "拒絕 H0" if p_sur < 0.05 else "不拒絕 H0"))
    print("H0 為真時，OLS t 檢定的誤拒絕率 = %.3f（應為 0.05）" % reject_rate)

    # 畫 H0 下的斜率分布，並標出原始 OLS 斜率
    ax = axes[k]
    ax.hist(b_null, bins=40, density=True, color="lightgray", edgecolor="gray", label="slopes under H0")
    ax.axvline(b_hat, color="r", lw=2, label="original b_hat = %.3f" % b_hat)
    ax.axvline(crit_sur, color="b", ls="--", label="surrogate 5% critical |b|")
    ax.axvline(-crit_sur, color="b", ls="--")
    # 傳統 OLS t 檢定的 5% 臨界值：|b| > t_crit * SE_OLS 就判定顯著
    ax.axvline(t_crit * se_b, color="g", ls=":", lw=2, label="OLS 5% critical |b|")
    ax.axvline(-t_crit * se_b, color="g", ls=":", lw=2)
    ax.set_title("phi = %.1f,  surrogate p = %.3f" % (phi, p_sur))
    ax.set_xlabel("slope")
    ax.legend(fontsize=8)

plt.tight_layout()
plt.savefig("q2_surrogate.png", dpi=150)
