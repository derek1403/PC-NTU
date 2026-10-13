"""Objective Analysis HW4 Q2: Monte Carlo derivation of the t-distribution.

挖空處以 ___1___、___2___ ... 表示（對應 hw4.md Answer 2 的「程式空格」），
全部填完後執行：

    python hw4_q2.py

會在終端機印出數值結果，並把圖存成同資料夾的 q2_t_distribution.png。
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

SEED = 2026          # 固定亂數種子，讓結果可重現
M = 10_000           # 蒙地卡羅實驗次數
N = 5                # 每次實驗的樣本數
nu = ___1___         # t 分布的自由度（用 N 表示）

rng = np.random.default_rng(SEED)

# ---------------------------------------------------------------
# (a) Monte Carlo simulation
# ---------------------------------------------------------------
# 一次抽出所有實驗的樣本：每一列（row）是一次實驗，共 M 列、N 行
x = rng.normal(loc=___2___, scale=___3___, size=(M, N))

xbar = x.mean(axis=___4___)                       # 每次實驗的樣本平均，shape (M,)
s2 = ((x - xbar[:, None]) ** 2).mean(axis=1)      # 有偏樣本變異數（除以 N），shape (M,)
t = (xbar - 0.0) / np.sqrt(___5___)               # t 統計量，shape (M,)

# ---------------------------------------------------------------
# (b) Theoretical PDFs
# ---------------------------------------------------------------
tt = np.linspace(-6, 6, 1001)
f_t = stats.t.pdf(tt, df=___6___)                 # t 分布 PDF（已含正規化常數 f0(nu)）
f_z = ___7___                                     # 標準常態 N(0, 1) 的 PDF（參考上一行的寫法）

# ---------------------------------------------------------------
# Plot
# ---------------------------------------------------------------
dx = 0.2
bins = np.arange(-6, 6 + dx / 2, dx)
# 機率密度 = 次數 / (M * 組距)。用全部 M 個 t 值正規化，
# 落在 ±6 以外的少數極端值也算在分母內（density=True 只會用畫面內的值正規化）
weights = np.full(M, 1.0 / (M * dx))

fig, axes = plt.subplots(1, 2, figsize=(12, 4.5))
for ax, logy in zip(axes, [False, True]):
    ax.hist(t, bins=bins, weights=weights, color="0.8", edgecolor="0.5",
            label=f"Monte Carlo ($M$={M}, $N$={N})")
    ax.plot(tt, f_t, "C0", lw=2, label=rf"t-distribution, $\nu$={nu}")
    ax.plot(tt, f_z, "C3--", lw=2, label=r"standard normal $\mathcal{N}(0,1)$")
    ax.set_xlabel("$t$")
    ax.set_ylabel("probability density")
    ax.set_xlim(-6, 6)
    if logy:
        ax.set_yscale("log")
        ax.set_ylim(1e-4, 1)
        ax.set_title("log scale (tails)")
    else:
        ax.set_title("linear scale")
    ax.legend(fontsize=9)
fig.tight_layout()
fig.savefig("q2_t_distribution.png", dpi=150)

# ---------------------------------------------------------------
# Numerical checks
# ---------------------------------------------------------------
print(f"seed = {SEED}, M = {M}, N = {N}, nu = {nu}")
print(f"mean of t     : MC = {t.mean():.4f}   theory = 0")
print(f"variance of t : MC = {t.var():.4f}   t-dist = {nu / (nu - 2):.4f}   normal = 1")
for c in [2, 3, 4]:
    mc = np.mean(np.abs(t) > c)
    th_t = 2 * stats.t.sf(c, df=nu)
    th_z = 2 * stats.norm.sf(c)
    print(f"P(|t| > {c})   : MC = {mc:.4f}   t-dist = {th_t:.4f}   normal = {th_z:.4f}")
