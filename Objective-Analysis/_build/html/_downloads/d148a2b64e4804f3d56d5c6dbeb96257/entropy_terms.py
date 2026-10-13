"""
entropy_terms.py
----------------
資訊量 I(p) = -ln p 與單項熵貢獻 g(p) = -p ln p 隨 p 的變化。
用於 00_Rule101.md §1.3。
"""

import os

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["Microsoft JhengHei", "Noto Sans TC", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False
OUT = os.path.dirname(os.path.abspath(__file__))

p = np.linspace(1e-4, 1, 1000)
info = -np.log(p)
contrib = -p * np.log(p)
p_star = 1 / np.e

fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(p, info, color="#1565C0", lw=2.5, label=r"資訊量 $I(p) = -\ln p$")
ax.plot(p, contrib, color="#E65100", lw=2.5, label=r"單項熵貢獻 $g(p) = -p\ln p$")

ax.plot(p_star, p_star, "o", color="#E65100", ms=8, zorder=5)
ax.annotate(r"最大值在 $p = 1/e \approx 0.368$" "\n" r"$g = 1/e \approx 0.368$",
            xy=(p_star, p_star), xytext=(0.5, 1.1),
            fontsize=11, color="#E65100",
            arrowprops=dict(arrowstyle="->", color="#E65100"))
ax.annotate("罕見事件：驚喜大", xy=(0.06, -np.log(0.06)), xytext=(0.15, 2.6),
            fontsize=11, color="#1565C0",
            arrowprops=dict(arrowstyle="->", color="#1565C0"))
ax.annotate("必然事件：沒有驚喜", xy=(1, 0), xytext=(0.62, 0.55),
            fontsize=11, color="#555555",
            arrowprops=dict(arrowstyle="->", color="#555555"))

ax.set_xlim(0, 1)
ax.set_ylim(0, 3)
ax.set_xlabel("事件機率 $p$", fontsize=12)
ax.set_ylabel("值", fontsize=12)
ax.set_title("資訊量 vs. 單項熵貢獻", fontsize=14, fontweight="bold")
ax.grid(alpha=0.3)
ax.legend(fontsize=11, loc="upper right")

fig.savefig(os.path.join(OUT, "entropy_terms.png"), dpi=150, bbox_inches="tight")
print("wrote entropy_terms.png")
