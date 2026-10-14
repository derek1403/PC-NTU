# HW4 Q2：用蒙地卡羅模擬推導 t 分布
# 執行方式：在 hw4 資料夾輸入  py hw4_q2.py
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# ===== 參數 =====
SEED = 2026      # 固定亂數種子
M = 10000        # 蒙地卡羅實驗次數
N = 5            # 每次實驗的樣本數
nu = N - 1       # t 分布自由度

rng = np.random.default_rng(SEED)

# ===== (a) 蒙地卡羅模擬 =====
# x 的形狀是 (M, N)：每一列是一次實驗的 N 個樣本，母體為 N(0, 1)
x = rng.normal(0.0, 1.0, size=(M, N))

xbar = np.mean(x, axis=1)          # 每次實驗的樣本平均（對每一列取平均）
s2 = np.var(x, axis=1)             # 有偏樣本變異數（np.var 預設除以 N）
t = (xbar - 0.0) / np.sqrt(s2 / (N - 1))   # t 統計量，共 M 個

# ===== (b) 理論 PDF =====
tt = np.linspace(-6, 6, 1001)
f_t = stats.t.pdf(tt, df=nu)       # t 分布（已含正規化常數 f0）
f_z = stats.norm.pdf(tt)           # 標準常態 N(0, 1)

# ===== 畫圖 =====
bins = np.arange(-6, 6.01, 0.2)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4.5))

# 左圖：一般座標
ax1.hist(t, bins=bins, density=True, color="lightgray", edgecolor="gray", label="Monte Carlo")
ax1.plot(tt, f_t, "b-", lw=2, label="t-distribution (nu=4)")
ax1.plot(tt, f_z, "r--", lw=2, label="N(0,1)")
ax1.set_xlabel("t")
ax1.set_ylabel("probability density")
ax1.set_title("linear scale")
ax1.legend()

# 右圖：對數座標，方便看尾部
ax2.hist(t, bins=bins, density=True, color="lightgray", edgecolor="gray", label="Monte Carlo")
ax2.plot(tt, f_t, "b-", lw=2, label="t-distribution (nu=4)")
ax2.plot(tt, f_z, "r--", lw=2, label="N(0,1)")
ax2.set_yscale("log")
ax2.set_ylim(1e-4, 1)
ax2.set_xlabel("t")
ax2.set_title("log scale (tails)")
ax2.legend()

plt.tight_layout()
plt.savefig("q2_t_distribution.png", dpi=150)

# ===== 數值檢查 =====
print("seed =", SEED, " M =", M, " N =", N, " nu =", nu)
print("t 的平均   : MC = %.4f   理論 = 0" % np.mean(t))
print("t 的變異數 : MC = %.4f   t 分布 = %.4f   常態 = 1" % (np.var(t), nu / (nu - 2)))

for c in [2, 3, 4]:
    p_mc = np.mean(np.abs(t) > c)              # 模擬中 |t| > c 的比例
    p_t = 2 * stats.t.sf(c, df=nu)             # t 分布的雙尾機率（sf = 1 - cdf）
    p_z = 2 * stats.norm.sf(c)                 # 常態的雙尾機率
    print("P(|t| > %d) : MC = %.4f   t 分布 = %.4f   常態 = %.4f" % (c, p_mc, p_t, p_z))
