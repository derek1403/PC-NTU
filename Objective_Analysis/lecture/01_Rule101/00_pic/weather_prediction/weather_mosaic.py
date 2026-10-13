"""
weather_mosaic.py
-----------------
用「面積 = 機率」的矩形分割畫今天／明天下雨的聯合機率。
用於 01_problems/01_weather_prediction.md。

* 橫向：今天下雨 N（寬 0.6）| 今天沒下雨 Ñ（寬 0.4）
* 縱向：在每一欄裡，再依「明天下雨 T / 沒下雨 T̃」切開
* 左圖：只知道 Pr(N)、Pr(T|N)，右邊那一欄還不知道怎麼切
* 右圖：補上 Pr(T|Ñ) = 0.2 之後的完整聯合機率表
"""

import os

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

plt.rcParams["font.sans-serif"] = ["Microsoft JhengHei", "Noto Sans TC", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False
OUT = os.path.dirname(os.path.abspath(__file__))

P_N = 0.6          # 今天下雨
P_T_N = 0.8        # 今天下雨 → 明天下雨
P_T_NN = 0.2       # 今天沒下雨 → 明天下雨（情況 1 補上的條件）

RAIN = "#64B5F6"   # 明天下雨
DRY = "#FFE082"    # 明天沒下雨
UNKNOWN = "#E0E0E0"


def cell(ax, x, y, w, h, color, text, hatch=None):
    ax.add_patch(mpatches.Rectangle((x, y), w, h, facecolor=color, edgecolor="black",
                                    lw=2, hatch=hatch))
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=11)


def frame(ax, title):
    ax.set_xlim(-0.02, 1.02)
    ax.set_ylim(-0.12, 1.08)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title(title, fontsize=13, fontweight="bold", pad=48)
    # 欄位標題
    ax.text(P_N / 2, 1.03, r"今天下雨 $N$" + f"\n寬 = {P_N}", ha="center", va="bottom", fontsize=11)
    ax.text(P_N + (1 - P_N) / 2, 1.03, r"今天沒下雨 $\widetilde{N}$" + f"\n寬 = {1 - P_N:.1f}",
            ha="center", va="bottom", fontsize=11)


fig, axes = plt.subplots(1, 2, figsize=(13, 6.5))

# ── 左圖：只知道今天下雨那一欄 ────────────────────────────────────────────────
ax = axes[0]
frame(ax, "(a) 只知道 $\\Pr(N)$ 與 $\\Pr(T \\mid N)$")
h_t = P_T_N
cell(ax, 0, 1 - h_t, P_N, h_t, RAIN,
     r"$N \cap T$" + f"\n{P_N} × {P_T_N} = {P_N * P_T_N:.2f}")
cell(ax, 0, 0, P_N, 1 - h_t, DRY,
     r"$N \cap \widetilde{T}$" + f"\n{P_N} × {1 - P_T_N:.1f} = {P_N * (1 - P_T_N):.2f}")
cell(ax, P_N, 0, 1 - P_N, 1, UNKNOWN, "", hatch="//")
ax.text(P_N + (1 - P_N) / 2, 0.5, "?\n這一欄要怎麼切\n還不知道", ha="center", va="center", fontsize=11,
        bbox=dict(boxstyle="round,pad=0.4", fc="white", ec="#9E9E9E"))
ax.text(0.5, -0.07, "缺一個條件 → 算不出 $\\Pr(T)$、$\\Pr(N \\mid T)$",
        ha="center", fontsize=11, color="#C62828")

# ── 右圖：補上 Pr(T|Ñ) 後的完整分割 ───────────────────────────────────────────
ax = axes[1]
frame(ax, "(b) 補上 $\\Pr(T \\mid \\widetilde{N}) = 0.2$")
cell(ax, 0, 1 - P_T_N, P_N, P_T_N, RAIN, r"$N \cap T$" + f"\n{P_N * P_T_N:.2f}")
cell(ax, 0, 0, P_N, 1 - P_T_N, DRY, r"$N \cap \widetilde{T}$" + f"\n{P_N * (1 - P_T_N):.2f}")
cell(ax, P_N, 1 - P_T_NN, 1 - P_N, P_T_NN, RAIN,
     r"$\widetilde{N} \cap T$" + f"\n{(1 - P_N) * P_T_NN:.2f}")
cell(ax, P_N, 0, 1 - P_N, 1 - P_T_NN, DRY,
     r"$\widetilde{N} \cap \widetilde{T}$" + f"\n{(1 - P_N) * (1 - P_T_NN):.2f}")
p_t = P_N * P_T_N + (1 - P_N) * P_T_NN
ax.text(0.5, -0.07,
        rf"藍色總面積 $\Pr(T) = {P_N * P_T_N:.2f} + {(1 - P_N) * P_T_NN:.2f} = {p_t:.2f}$；"
        rf"$\Pr(N \mid T) = {P_N * P_T_N:.2f}/{p_t:.2f} \approx {P_N * P_T_N / p_t:.3f}$",
        ha="center", fontsize=11)

handles = [mpatches.Patch(facecolor=RAIN, edgecolor="black", label=r"明天下雨 $T$"),
           mpatches.Patch(facecolor=DRY, edgecolor="black", label=r"明天沒下雨 $\widetilde{T}$")]
fig.legend(handles=handles, loc="lower center", ncol=2, fontsize=11, frameon=False,
           bbox_to_anchor=(0.5, 0.04))
fig.suptitle("面積 = 機率：今天與明天下雨的聯合機率", fontsize=15, fontweight="bold", y=1.08)

fig.savefig(os.path.join(OUT, "weather_mosaic.png"), dpi=150, bbox_inches="tight")
print("wrote weather_mosaic.png")
