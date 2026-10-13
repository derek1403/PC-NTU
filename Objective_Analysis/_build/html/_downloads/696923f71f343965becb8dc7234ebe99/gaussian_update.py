"""
gaussian_update.py
------------------
高斯先驗 × 高斯概似 → 高斯後驗（純量資料同化）。
用於 00_Rule101.md §8.1 與 01_problems/04_Data_Assimilation.md。

輸出兩張圖：
* gaussian_update.png  ：本題數字（預報 -20°C、探空 -17°C）的一次更新
* kalman_gain_cases.png：誤差大小不同時，Kalman gain 怎麼決定分析場靠向誰
"""

import os

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["Microsoft JhengHei", "Noto Sans TC", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False
OUT = os.path.dirname(os.path.abspath(__file__))

XB, YO = -20.0, -17.0   # 背景場、觀測
PRIOR, OBS, POST = "#1565C0", "#E65100", "#2E7D32"


def gauss(x, mu, var):
    return np.exp(-(x - mu) ** 2 / (2 * var)) / np.sqrt(2 * np.pi * var)


def update(vb, vo):
    k = vb / (vb + vo)
    return k, XB + k * (YO - XB), (1 - k) * vb


def draw(ax, vb, vo, legend=True):
    k, xa, va = update(vb, vo)
    x = np.linspace(-30, -8, 800)
    ax.plot(x, gauss(x, XB, vb), "--", color=PRIOR, lw=2,
            label=rf"先驗／背景場 $\mathcal{{N}}({XB:g},\ {vb:g})$")
    ax.plot(x, gauss(x, YO, vo), "--", color=OBS, lw=2,
            label=rf"概似／觀測 $\mathcal{{N}}({YO:g},\ {vo:g})$")
    ax.plot(x, gauss(x, xa, va), "-", color=POST, lw=2.8,
            label=rf"後驗／分析場 $\mathcal{{N}}({xa:g},\ {va:g})$")
    ax.fill_between(x, gauss(x, xa, va), color=POST, alpha=0.15)
    for mu, c in [(XB, PRIOR), (YO, OBS), (xa, POST)]:
        ax.axvline(mu, color=c, lw=1, alpha=0.6)
    ax.set_xlabel("溫度 $x$（°C）", fontsize=11)
    ax.set_ylabel("機率密度", fontsize=11)
    ax.grid(alpha=0.3)
    if legend:
        ax.legend(fontsize=10, loc="upper right")
    return k, xa, va


# ── 圖 1：本題的一次更新 ───────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(9, 5))
k, xa, va = draw(ax, 1.0, 4.0)
ax.set_xlim(-25, -12)
ax.legend(fontsize=10, loc="upper left")
ax.annotate(rf"$x^a = x^b + K(y - x^b) = {XB:g} + {k:g}\times{YO - XB:g} = {xa:g}$" "\n"
            rf"$\sigma_a^2 = (1-K)\,\sigma_b^2 = {va:g}$",
            xy=(xa, gauss(xa, xa, va)), xytext=(-17.8, 0.30), fontsize=11,
            arrowprops=dict(arrowstyle="->", color=POST))
ax.set_title(rf"高斯 × 高斯 = 高斯：Kalman gain $K = \sigma_b^2/(\sigma_b^2+\sigma_o^2) = {k:g}$",
             fontsize=13, fontweight="bold")
fig.savefig(os.path.join(OUT, "gaussian_update.png"), dpi=150, bbox_inches="tight")
print("wrote gaussian_update.png")

# ── 圖 2：誤差大小不同的三種情況 ───────────────────────────────────────────────
cases = [("預報較準", 1.0, 4.0), ("兩者一樣準", 4.0, 4.0), ("預報很不準", 16.0, 4.0)]
fig, axes = plt.subplots(1, 3, figsize=(16, 4.8), sharey=True)
for i, (ax, (name, vb, vo)) in enumerate(zip(axes, cases)):
    k, xa, va = draw(ax, vb, vo, legend=(i == 0))
    ax.set_xlim(-30, -8)
    ax.set_title(rf"{name}：$\sigma_b^2={vb:g},\ \sigma_o^2={vo:g}$" "\n"
                 rf"$K = {k:g}$，$x^a = {xa:g}$，$\sigma_a^2 = {va:g}$", fontsize=12)
    if i:
        ax.set_ylabel("")
fig.suptitle(r"$K \to 0$ 貼近預報、$K \to 1$ 貼近觀測；分析場永遠比兩者都窄",
             fontsize=14, fontweight="bold", y=1.04)
fig.savefig(os.path.join(OUT, "kalman_gain_cases.png"), dpi=150, bbox_inches="tight")
print("wrote kalman_gain_cases.png")
