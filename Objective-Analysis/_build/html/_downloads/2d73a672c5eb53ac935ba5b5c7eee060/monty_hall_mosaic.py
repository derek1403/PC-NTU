"""
monty_hall_mosaic.py
--------------------
三門問題的「面積 = 機率」分割。用於 01_problems/03_Monty_Hall_problem.md。

* 左圖：先依大獎位置 A/B/C 切成三欄（各 1/3），再依主持人開哪扇門切開。
        參賽者選 1 號門；M = 主持人打開 2 號門。
* 右圖：觀察到 M 之後，只留下 M 的面積，重新正規化 → 後驗。
"""

import os

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

plt.rcParams["font.sans-serif"] = ["Microsoft JhengHei", "Noto Sans TC", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False
OUT = os.path.dirname(os.path.abspath(__file__))

OPEN2 = "#81C784"   # 主持人開 2 號門（事件 M）
OPEN3 = "#E0E0E0"   # 主持人開 3 號門
STAY = "#64B5F6"
SWITCH = "#FF8A65"

# 大獎位置: (欄名, Pr(M | 位置), 綠色面積 = 先驗 × 概似)
columns = [(r"大獎在 1 號門 $A$", 0.5, r"\frac{1}{3} \times \frac{1}{2} = \frac{1}{6}"),
           (r"大獎在 2 號門 $B$", 0.0, ""),
           (r"大獎在 3 號門 $C$", 1.0, r"\frac{1}{3} \times 1 = \frac{1}{3}")]
w = 1 / 3

fig, axes = plt.subplots(1, 2, figsize=(16, 6.5), gridspec_kw=dict(width_ratios=[1.3, 1]))

# ── 左圖：先驗 × 概似 ─────────────────────────────────────────────────────────
ax = axes[0]
ax.set_xlim(-0.02, 1.02)
ax.set_ylim(-0.2, 1.15)
ax.axis("off")
for i, (name, p_m, area) in enumerate(columns):
    x = i * w
    if p_m > 0:
        ax.add_patch(mpatches.Rectangle((x, 1 - p_m), w, p_m, facecolor=OPEN2, edgecolor="black", lw=2))
        ax.text(x + w / 2, 1 - p_m / 2, f"開 2 號門\n${area}$",
                ha="center", va="center", fontsize=13)
    if p_m < 1:
        ax.add_patch(mpatches.Rectangle((x, 0), w, 1 - p_m, facecolor=OPEN3, edgecolor="black", lw=2))
        ax.text(x + w / 2, (1 - p_m) / 2, "開 3 號門", ha="center", va="center", fontsize=11, color="#555555")
    ax.text(x + w / 2, 1.03, name + "\n先驗 1/3", ha="center", va="bottom", fontsize=11)
ax.text(0.5, -0.1,
        r"綠色總面積 $\Pr(M) = \frac{1}{6} + 0 + \frac{1}{3} = \frac{1}{2}$",
        ha="center", fontsize=13)
ax.set_title("(a) 先驗（欄寬）× 概似（欄內高度）", fontsize=13, fontweight="bold", pad=38)

# ── 右圖：只留下觀察到的 M，重新正規化 ─────────────────────────────────────────
ax = axes[1]
ax.set_xlim(-0.02, 1.02)
ax.set_ylim(-0.2, 1.15)
ax.axis("off")
stay, switch = (1 / 6) / 0.5, (1 / 3) / 0.5
ax.add_patch(mpatches.Rectangle((0, 0.2), stay, 0.6, facecolor=STAY, edgecolor="black", lw=2))
ax.add_patch(mpatches.Rectangle((stay, 0.2), switch, 0.6, facecolor=SWITCH, edgecolor="black", lw=2))
ax.text(stay / 2, 0.5, "不換門\n大獎在 1 號門\n$\\Pr(A \\mid M) = \\frac{1}{3}$",
        ha="center", va="center", fontsize=12)
ax.text(stay + switch / 2, 0.5, "換門\n大獎在 3 號門\n$\\Pr(C \\mid M) = \\frac{2}{3}$",
        ha="center", va="center", fontsize=13, fontweight="bold")
ax.text(0.5, 0.05, r"$\frac{1/6}{1/2}$ 與 $\frac{1/3}{1/2}$：綠色面積各自佔多少",
        ha="center", fontsize=12)
ax.text(0.5, -0.1, r"2 號門被打開 → $\Pr(B \mid M) = 0$，整欄消失",
        ha="center", fontsize=12, color="#555555")
ax.set_title("(b) 看到主持人開 2 號門之後（後驗）", fontsize=13, fontweight="bold", pad=38)

fig.suptitle("三門問題：參賽者選 1 號門，主持人打開 2 號門", fontsize=15, fontweight="bold", y=1.04)
fig.savefig(os.path.join(OUT, "monty_hall_mosaic.png"), dpi=150, bbox_inches="tight")
print("wrote monty_hall_mosaic.png")
