# HW10 Q1 (a)(b)：2D toy 資料上的 EOF vs k-means
# 執行方式：py -X utf8 hw10_q1ab.py
# 以講義 eof_scatter_2d.py 的資料與 EOF 計算為基礎，加上 k-means。
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
from sklearn.cluster import KMeans

HERE = Path(__file__).resolve().parent
SEED = 0

C_EOF1, C_EOF2, C_MUTE = "#2a78d6", "#eb6834", "#8c8b86"
CL = ["#d62728", "#1f77b4", "#2ca02c"]          # cluster 顏色

# ── 講義的 8 點資料 ───────────────────────────────────────────────────────────
X0 = np.array([[-4, -2], [-2, -4], [-2, 0], [0, -2],
               [0, 2], [2, 0], [2, 4], [4, 2]], dtype=float)


def eof(X):
    """回傳 (lam, E)，C = X^T X / M，特徵值由大到小，EOF 第一分量取正號。"""
    M = X.shape[0]
    C = X.T @ X / M
    lam, E = np.linalg.eigh(C)
    o = np.argsort(lam)[::-1]
    lam, E = lam[o], E[:, o]
    for j in range(E.shape[1]):
        if E[0, j] < 0:
            E[:, j] *= -1
    return lam, E


def kmeans(X, k):
    """k-means；cluster 依 PC1 方向的centroid位置由小到大排序，讓編號固定。"""
    km = KMeans(n_clusters=k, n_init=50, random_state=SEED).fit(X)
    mu, lab = km.cluster_centers_, km.labels_
    _, E = eof(X)
    o = np.argsort(mu @ E[:, 0])                # 依 z1 排序
    remap = np.empty(k, int); remap[o] = np.arange(k)
    return mu[o], remap[lab], km.inertia_


def wcss(X, mu, lab):
    return sum(((X[lab == i] - mu[i]) ** 2).sum() for i in range(len(mu)))


def angle_deg(a, b):
    c = a @ b / np.linalg.norm(a) / np.linalg.norm(b)
    return np.degrees(np.arccos(np.clip(c, -1, 1)))


def style(ax, lim=5.6):
    ax.set_aspect("equal")
    ax.set_xlim(-lim, lim); ax.set_ylim(-lim, lim)
    ax.axhline(0, color=C_MUTE, lw=0.8, zorder=0)
    ax.axvline(0, color=C_MUTE, lw=0.8, zorder=0)
    ax.grid(True, color=C_MUTE, alpha=0.22, lw=0.6)
    ax.set_axisbelow(True)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)


def draw_data_space(ax, X, lam, E, mu, lab, title):
    angle = np.degrees(np.arctan2(E[1, 0], E[0, 0]))
    ax.add_patch(Ellipse((0, 0), 2 * np.sqrt(lam[0]), 2 * np.sqrt(lam[1]), angle=angle,
                         facecolor=C_MUTE, alpha=0.12, edgecolor=C_MUTE, lw=1.2, ls="--"))
    for j, c in enumerate([C_EOF1, C_EOF2]):
        v = E[:, j] * np.sqrt(lam[j])
        ax.plot([-v[0], v[0]], [-v[1], v[1]], color=c, lw=2.4, zorder=3,
                label=f"EOF {j+1} ($\\lambda_{j+1}$={lam[j]:.2f})")
    for i in range(len(mu)):
        m = lab == i
        ax.scatter(X[m, 0], X[m, 1], s=85, color=CL[i], edgecolor="white", lw=1.4, zorder=5,
                   label=f"cluster {i+1} ($|S_{i+1}|$={m.sum()})")
        ax.scatter(*mu[i], marker="*", s=420, color=CL[i], edgecolor="k", lw=1.0, zorder=6)
    ax.set_xlabel("anomaly at station A,  $x$"); ax.set_ylabel("anomaly at station B,  $y$")
    ax.set_title(title, fontsize=11.5)
    ax.legend(loc="upper left", fontsize=8.5, framealpha=0.92)


def draw_eof_space(ax, Z, lam, muZ, lab, title):
    s1, s2 = np.sqrt(lam[:2])
    ax.plot([-s1, s1], [0, 0], color=C_EOF1, lw=2.4, zorder=3)
    ax.plot([0, 0], [-s2, s2], color=C_EOF2, lw=2.4, zorder=3)
    for i in range(len(muZ)):
        m = lab == i
        ax.scatter(Z[m, 0], Z[m, 1], s=85, color=CL[i], edgecolor="white", lw=1.4, zorder=5)
        ax.scatter(*muZ[i], marker="*", s=420, color=CL[i], edgecolor="k", lw=1.0, zorder=6)
        ax.annotate(f"({muZ[i,0]:.2f}, {muZ[i,1]:.2f})", muZ[i], xytext=(8, 10),
                    textcoords="offset points", fontsize=9, color=CL[i], fontweight="bold")
    ax.set_xlabel(r"PC 1,  $z_1$"); ax.set_ylabel(r"PC 2,  $z_2$")
    ax.set_title(title, fontsize=11.5)


# ═════════════════════════════════════════════════════════════════════════════
# (a) k = 2
# ═════════════════════════════════════════════════════════════════════════════
X = X0 - X0.mean(axis=0)
M = X.shape[0]
lam, E = eof(X)
Z = X @ E
print("===== (a) =====")
print("C =\n", X.T @ X / M)
print("lambda =", lam, "\nE =\n", E)

mu, lab, inertia = kmeans(X, 2)
muZ = mu @ E
print("\nmu_1 =", mu[0], "  mu_2 =", mu[1])
print("mu in EOF space (z1, z2):\n", muZ)
d = mu[1] - mu[0]
print(f"angle(mu2 - mu1, e1) = {angle_deg(d, E[:, 0]):.6f} deg")

print("\n t   x   y      z1      z2   sign(z1)  label")
for t in range(M):
    print(f"{t+1:2d} {X[t,0]:3.0f} {X[t,1]:3.0f}  {Z[t,0]:6.3f}  {Z[t,1]:6.3f}"
          f"   {'+' if Z[t,0] > 0 else '-':>4}     {lab[t]+1}")
agree = np.mean((Z[:, 0] > 0) == (lab == 1))
print(f"label 與 sign(z1) 的一致率（cluster 2 ↔ z1>0）= {100*agree:.1f}%")

J = wcss(X, mu, lab)
trXX = np.trace(X.T @ X)
bound = trXX - M * lam[0]
print(f"\nJ = {J:.4f} (sklearn inertia = {inertia:.4f})")
print(f"tr(X^T X) = {trXX:.4f},  M*lambda1 = {M*lam[0]:.4f},  下界 = {bound:.4f}")
print(f"J >= bound ? {J >= bound - 1e-9}   (J - bound = {J-bound:.4f})")
# 也列出窮舉所有 2-partition 的最小 J，確認 k-means 找到的是全域最佳
best = min(wcss(X, np.array([X[m].mean(0), X[~m].mean(0)]), (~m).astype(int))
           for code in range(1, 2 ** (M - 1))
           for m in [np.array([(code >> t) & 1 for t in range(M)], bool)])
print(f"窮舉 127 種 2-partition 的最小 J = {best:.4f}")

fig, (a0, a1) = plt.subplots(1, 2, figsize=(12.5, 5.8))
style(a0); style(a1)
draw_data_space(a0, X, lam, E, mu, lab,
                "(a) Data space, k-means k=2\n"
                f"angle($\\mu_2-\\mu_1$, $e_1$) = {angle_deg(d, E[:,0]):.1f}°")
draw_eof_space(a1, Z, lam, muZ, lab,
               f"(a) EOF space $Z=XE$, k=2\n$J$={J:.1f} $\\geq$ tr$(X^TX)-M\\lambda_1$={bound:.1f}")
fig.tight_layout()
fig.savefig(HERE / "q1a_k2.png", dpi=150, bbox_inches="tight", facecolor="white")

# ═════════════════════════════════════════════════════════════════════════════
# (b) Experiment 1：k = 3
# ═════════════════════════════════════════════════════════════════════════════
print("\n===== (b) Exp 1: k = 3 =====")
mu3, lab3, _ = kmeans(X, 3)
muZ3 = mu3 @ E
for i in range(3):
    print(f"cluster {i+1}: |S|={np.sum(lab3==i)}, mu = {mu3[i]}, "
          f"(z1, z2) = ({muZ3[i,0]:.4f}, {muZ3[i,1]:.4f}), members = {np.where(lab3==i)[0]+1}")
print("max |z2| of centroids =", np.abs(muZ3[:, 1]).max())
J3 = wcss(X, mu3, lab3)
print(f"J(k=3) = {J3:.4f};  Ding–He 下界 tr - M(lam1+lam2) = {trXX - M*lam.sum():.4f}")

# 窮舉所有 3-partition：檢查全域最佳解是否唯一
import itertools
sols = {}
for code in itertools.product(range(3), repeat=M):
    if code[0] != 0 or len(set(code)) < 3:
        continue
    lb = np.array(code)
    groups = tuple(sorted(tuple(int(v) for v in np.where(lb == i)[0] + 1) for i in range(3)))
    sols[groups] = sum(((X[lb == i] - X[lb == i].mean(0)) ** 2).sum() for i in range(3))
Jmin = min(sols.values())
print(f"\n窮舉：全域最小 J = {Jmin:.4f}，達到最小值的分割共 {sum(abs(v-Jmin)<1e-9 for v in sols.values())} 種：")
for g, v in sols.items():
    if abs(v - Jmin) < 1e-9:
        zc = np.array([X[np.array(s) - 1].mean(0) @ E for s in g])
        print(f"  {g}:  centroids (z1,z2) = {np.round(zc, 3).tolist()}")
# 換不同 seed 看 sklearn 會落在哪一個
seen = {}
for sd in range(30):
    km = KMeans(3, n_init=50, random_state=sd).fit(X)
    g = tuple(sorted(tuple(int(v) for v in np.where(km.labels_ == i)[0] + 1) for i in range(3)))
    seen[g] = seen.get(g, 0) + 1
print("seed 0–29 的 k=3 結果分佈：", seen)

fig, (a0, a1) = plt.subplots(1, 2, figsize=(12.5, 5.8))
style(a0); style(a1)
draw_data_space(a0, X, lam, E, mu3, lab3, "(b) Exp 1: Data space, k=3")
draw_eof_space(a1, Z, lam, muZ3, lab3, "(b) Exp 1: EOF space, k=3 centroids")
fig.tight_layout()
fig.savefig(HERE / "q1b_exp1_k3.png", dpi=150, bbox_inches="tight", facecolor="white")

# ═════════════════════════════════════════════════════════════════════════════
# (b) Experiment 2：加入不對稱極端值
# ═════════════════════════════════════════════════════════════════════════════
print("\n===== (b) Exp 2: skewed =====")
Xs_raw = np.vstack([X0, [[6, -1], [6, 1]]])
print("新的欄平均 =", Xs_raw.mean(axis=0))
Xs = Xs_raw - Xs_raw.mean(axis=0)
lam_s, E_s = eof(Xs)
print("C_skew =\n", Xs.T @ Xs / Xs.shape[0])
print("lambda_skew =", lam_s, "\ne1_skew =", E_s[:, 0],
      f"(與 x 軸夾角 {np.degrees(np.arctan2(E_s[1,0], E_s[0,0])):.2f} deg)")
mu_s, lab_s, _ = kmeans(Xs, 2)
for i in range(2):
    print(f"cluster {i+1}: members = {np.where(lab_s==i)[0]+1}, mu = {mu_s[i]}")

tab = {
    "|S1|, |S2|": (np.sum(lab_s == 0), np.sum(lab_s == 1)),
    "||mu1||, ||mu2||": (np.linalg.norm(mu_s[0]), np.linalg.norm(mu_s[1])),
    "angle(mu1, -mu2) [deg]": angle_deg(mu_s[0], -mu_s[1]),
    "angle(mu2-mu1, e1) [deg]": angle_deg(mu_s[1] - mu_s[0], E_s[:, 0]),
}
ref = {"|S1|, |S2|": (np.sum(lab == 0), np.sum(lab == 1)),
       "||mu1||, ||mu2||": (np.linalg.norm(mu[0]), np.linalg.norm(mu[1])),
       "angle(mu1, -mu2) [deg]": angle_deg(mu[0], -mu[1]),
       "angle(mu2-mu1, e1) [deg]": angle_deg(mu[1] - mu[0], E[:, 0])}
print(f"\n{'quantity':28s} {'original (M=8)':>22s} {'skewed (M=10)':>22s}")
for key in tab:
    f = lambda v: (f"{v[0]:.3f}, {v[1]:.3f}" if isinstance(v, tuple) else f"{v:.3f}")
    print(f"{key:28s} {f(ref[key]):>22s} {f(tab[key]):>22s}")

fig, ax = plt.subplots(figsize=(6.6, 6.2))
style(ax, lim=6.6)
draw_data_space(ax, Xs, lam_s, E_s, mu_s, lab_s,
                "(b) Exp 2: skewed data ($M$=10), k=2\n"
                f"$|S|$=({tab['|S1|, |S2|'][0]}, {tab['|S1|, |S2|'][1]}),  "
                f"$\\|\\mu\\|$=({tab['||mu1||, ||mu2||'][0]:.2f}, {tab['||mu1||, ||mu2||'][1]:.2f}),  "
                f"∠($\\mu_1$,$-\\mu_2$)={tab['angle(mu1, -mu2) [deg]']:.1f}°")
fig.tight_layout()
fig.savefig(HERE / "q1b_exp2_skew.png", dpi=150, bbox_inches="tight", facecolor="white")
print("\n圖檔：q1a_k2.png, q1b_exp1_k3.png, q1b_exp2_skew.png")
