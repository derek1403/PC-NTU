"""
covid_base_rate.py
------------------
快篩的基本比率問題。用於 01_problems/02_COVID-19.md。

* 左圖：10 萬人普篩、快篩陽性的 5,095 人裡，真陽性只佔一小條（面積 = 人數）
* 右圖：陽性預測值 Pr(C|+) 隨盛行率 Pr(C) 的變化（偽陽性 5%、無偽陰性）
"""

import os

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

plt.rcParams["font.sans-serif"] = ["Microsoft JhengHei", "Noto Sans TC", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False
OUT = os.path.dirname(os.path.abspath(__file__))

N_PEOPLE = 100_000
P_C = 0.001          # 盛行率
FPR = 0.05           # 偽陽性率 Pr(+|~C)
TPR = 1.0            # 1 - 偽陰性率

TRUE_POS = "#E53935"
FALSE_POS = "#FFB74D"

n_c = N_PEOPLE * P_C
tp = n_c * TPR
fp = (N_PEOPLE - n_c) * FPR
n_pos = tp + fp


def ppv(prior):
    return TPR * prior / (TPR * prior + FPR * (1 - prior))


fig, axes = plt.subplots(1, 2, figsize=(14, 5.8), gridspec_kw=dict(width_ratios=[1, 1.15]))

# ── 左圖：快篩陽性的人裡面，誰是真的？ ─────────────────────────────────────────
ax = axes[0]
ax.set_xlim(-0.02, 1.02)
ax.set_ylim(-0.25, 1.15)
ax.axis("off")
w_tp = tp / n_pos
ax.add_patch(mpatches.Rectangle((0, 0), w_tp, 1, facecolor=TRUE_POS, edgecolor="black", lw=2))
ax.add_patch(mpatches.Rectangle((w_tp, 0), 1 - w_tp, 1, facecolor=FALSE_POS, edgecolor="black", lw=2))
ax.text(0.5 + w_tp / 2, 0.5,
        f"偽陽性（沒感染）\n{N_PEOPLE - n_c:,.0f} × {FPR} $\\approx$ {fp:,.0f} 人",
        ha="center", va="center", fontsize=13)
ax.annotate(f"真陽性 {tp:,.0f} 人\n（只佔 {w_tp:.1%}）",
            xy=(w_tp / 2, 0.85), xytext=(0.08, 1.06),
            fontsize=12, color=TRUE_POS, fontweight="bold",
            arrowprops=dict(arrowstyle="->", color=TRUE_POS, lw=1.5))
ax.text(0.5, -0.12,
        rf"$\Pr(C \mid +) = \dfrac{{{tp:,.0f}}}{{{n_pos:,.0f}}} \approx {tp / n_pos * 100:.1f}\%$",
        ha="center", va="center", fontsize=14)
ax.set_title(f"(a) 10 萬人普篩，快篩陽性的 {n_pos:,.0f} 人（面積 = 人數）",
             fontsize=13, fontweight="bold")

# ── 右圖：盛行率越高，陽性越可信 ───────────────────────────────────────────────
ax = axes[1]
prior = np.logspace(-4, 0, 400)
ax.semilogx(prior, ppv(prior), color="#1565C0", lw=2.5)
cases = [(0.001, "不盛行，全民普篩"), (0.01, "開始擴散"), (0.10, "大流行，全民普篩"),
         (0.20, "只篩有症狀者")]
offsets = [(12, 12), (12, -4), (-150, 6), (12, -26)]
for (pc, label), (dx, dy) in zip(cases, offsets):
    ax.plot(pc, ppv(pc), "o", color="#C62828", ms=8, zorder=5)
    ax.annotate(f"{label}\n$\\Pr(C)$ = {pc:g} → {ppv(pc):.0%}", xy=(pc, ppv(pc)),
                xytext=(dx, dy), textcoords="offset points", fontsize=10.5)
ax.set_xlim(1e-4, 1)
ax.set_xticks([1e-4, 1e-3, 1e-2, 1e-1, 1])
ax.set_xticklabels(["0.01%", "0.1%", "1%", "10%", "100%"])
ax.minorticks_off()
ax.set_ylim(0, 1.05)
ax.set_xlabel(r"盛行率（先驗）$\Pr(C)$", fontsize=12)
ax.set_ylabel(r"陽性預測值 $\Pr(C \mid +)$", fontsize=12)
ax.set_title("(b) 同一支快篩，先驗不同，陽性的可信度天差地遠", fontsize=13, fontweight="bold")
ax.grid(alpha=0.3, which="both")

fig.suptitle("基本比率：偽陽性率只有 5%，為什麼陽性大多是假的？", fontsize=15, fontweight="bold")
fig.tight_layout()
fig.savefig(os.path.join(OUT, "covid_base_rate.png"), dpi=150, bbox_inches="tight")
print("wrote covid_base_rate.png")
