# HW11 Q1 (a)(b)：8 點 2D 資料上的 k-means、Batch SOM、VAE
# 執行方式：py -X utf8 hw11_q1ab.py
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

from vae_numpy import VAE

HERE = Path(__file__).resolve().parent
SEED = 0

# 資料與 eof_scatter_2d.py 相同
X = np.array([[-4, -2], [-2, -4], [-2, 0], [0, -2],
              [0, 2], [2, 0], [2, 4], [4, 2]], dtype=float)
X -= X.mean(0)
M = X.shape[0]

C_DOT, C_KM, C_SOM, C_MUTE = "#0b0b0b", "#eb6834", "#2a78d6", "#8c8b86"


def sqd(X, C):
    """||x_n − c_j||²，回傳 [M × k]。"""
    return ((X[:, None, :] - C[None, :, :]) ** 2).sum(-1)


def style(ax, lim=5.4):
    ax.set_aspect("equal"); ax.set_xlim(-lim, lim); ax.set_ylim(-lim, lim)
    ax.axhline(0, color=C_MUTE, lw=0.7, zorder=0); ax.axvline(0, color=C_MUTE, lw=0.7, zorder=0)
    ax.grid(True, color=C_MUTE, alpha=0.2, lw=0.6)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)


# ═════════════════════════════════════════════════════════════════════════════
# (a) k-means (k=4) vs. Batch SOM (2×2)
# ═════════════════════════════════════════════════════════════════════════════
km4 = KMeans(n_clusters=4, n_init=50, random_state=SEED).fit(X)
mu4 = km4.cluster_centers_
d4 = sqd(X, mu4)
lab4 = d4.argmin(1)
J4 = d4.min(1).sum()
Eq4 = np.sqrt(d4.min(1)).mean()
print("===== (a) k-means k = 4 =====")
for i in np.argsort(mu4[:, 0] + mu4[:, 1]):
    print(f"  mu = ({mu4[i,0]:+.3f}, {mu4[i,1]:+.3f}),  members = {(np.where(lab4 == i)[0] + 1).tolist()}")
print(f"  J = {J4:.4f},  Eq = {Eq4:.4f},  sklearn inertia = {km4.inertia_:.4f}")

# 2×2 SOM：節點順序 (0,0), (0,1), (1,0), (1,1)
GRID = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=float)
NODE0 = np.array([[-3, -3], [-1, 1], [1, -1], [3, 3]], dtype=float)
GD2 = sqd(GRID, GRID)                                    # ||g_i − g_j||²
GL1 = np.abs(GRID[:, None, :] - GRID[None, :, :]).sum(-1)  # ||g_i − g_j||_1


def batch_som(X, nodes, sigma, max_iter=1000, tol=1e-12):
    H = np.exp(-GD2 / (2 * sigma**2))
    for it in range(1, max_iter + 1):
        c = sqd(X, nodes).argmin(1)                      # BMU
        Hn = H[c]                                        # h_{c(n) j}，[M × k]
        new = (Hn.T @ X) / Hn.sum(0)[:, None]
        if np.max(np.abs(new - nodes)) < tol:
            return new, it
        nodes = new
    return nodes, it


def som_diag(X, nodes, sigma):
    d = sqd(X, nodes)
    order = np.argsort(d, axis=1, kind="stable")         # 平手時取編號較小的節點
    c1, c2 = order[:, 0], order[:, 1]
    H = np.exp(-GD2 / (2 * sigma**2))
    return dict(J=d[np.arange(M), c1].sum(),
                Eq=np.sqrt(d[np.arange(M), c1]).mean(),
                Et=np.mean(GL1[c1, c2] > 1),
                E=(H[c1] * d).sum(),
                c1=c1, c2=c2, d=d)


rows = [("k-means (k=4)", J4, Eq4, np.nan)]
soms = {}
for sig in (2.0, 0.8, 0.05):
    nodes, it = batch_som(X, NODE0.copy(), sig)
    D = som_diag(X, nodes, sig)
    soms[sig] = (nodes, D)
    rows.append((f"SOM sigma={sig}", D["J"], D["Eq"], D["Et"]))
    print(f"\n===== (a) Batch SOM, sigma = {sig} （{it} 次迭代收斂）=====")
    for j, g in enumerate(GRID.astype(int)):
        print(f"  n{tuple(g.tolist())} = ({nodes[j,0]:+.4f}, {nodes[j,1]:+.4f})")
    print(f"  J_BMU = {D['J']:.4f}, Eq = {D['Eq']:.4f}, Et = {D['Et']:.3f}, E (加權) = {D['E']:.4f}")
    print(f"  BMU c1 = {D['c1'].tolist()},  2nd BMU c2 = {D['c2'].tolist()}")
    # 平手檢查：第 2 名與第 3 名距離相同
    ds = np.sort(D["d"], 1)
    ties = np.where(np.isclose(ds[:, 1], ds[:, 2]))[0]
    if ties.size:
        print(f"  注意：第 2 BMU 平手的觀測 = {(ties + 1).tolist()}")
        # 平手時所有可能的 Et 範圍
        lo = hi = 0
        for n in range(M):
            cand = np.where(np.isclose(D["d"][n], ds[n, 1]))[0]
            errs = GL1[D["c1"][n], cand] > 1
            lo += errs.all(); hi += errs.any()
        print(f"  平手造成的 Et 可能範圍 = [{lo/M:.3f}, {hi/M:.3f}]")

# 窮舉全部 4-分割，找出所有全域最佳解
from itertools import product
best = {}
for lab in product(range(4), repeat=M):
    if lab[0] != 0 or len(set(lab)) < 4:
        continue
    lab = np.array(lab)
    if any(lab[:i].max() + 1 < lab[i] for i in range(1, M)):   # 標準化標籤，去除重複
        continue
    J = sum(((X[lab == i] - X[lab == i].mean(0)) ** 2).sum() for i in range(4))
    best.setdefault(round(J, 9), []).append(lab)
Jmin = min(best)
print(f"\n窮舉：全域最小 J = {Jmin}，共有 {len(best[Jmin])} 種分割達到")
for lab in best[Jmin]:
    print("   ", [(np.where(lab == i)[0] + 1).tolist() for i in range(4)])

km_som = KMeans(n_clusters=4, init=NODE0, n_init=1).fit(X)
print(f"k-means（以 SOM 初始節點起算）centroids = {km_som.cluster_centers_.tolist()}, J = {km_som.inertia_:.4f}")
n005 = soms[0.05][0]
print(f"max |SOM(sigma=0.05) − k-means(同初值)| = {np.abs(n005 - km_som.cluster_centers_).max():.2e}")
match = np.max(np.min(np.sqrt(sqd(n005, mu4)), axis=1))
print(f"\n sigma=0.05 節點與 k-means centroid 的最大配對距離 = {match:.2e}")

print("\n===== (a) 摘要表 =====")
print(f"{'method':18s} {'J_BMU':>8s} {'Eq':>8s} {'Et':>8s}")
for name, J, Eq, Et in rows:
    print(f"{name:18s} {J:8.4f} {Eq:8.4f} {'—' if np.isnan(Et) else f'{Et:8.3f}':>8s}")

# ── 圖 (a) ──────────────────────────────────────────────────────────────────
fig, axs = plt.subplots(1, 4, figsize=(19, 5.2))
style(axs[0])
axs[0].scatter(*X.T, s=70, color=C_DOT, edgecolor="white", lw=1.4, zorder=5, label="observations")
axs[0].scatter(*mu4.T, s=260, marker="*", color=C_KM, edgecolor="k", lw=0.6, zorder=6, label="k-means centroid")
for n in range(M):
    axs[0].plot([X[n, 0], mu4[lab4[n], 0]], [X[n, 1], mu4[lab4[n], 1]], color=C_KM, lw=0.8, alpha=0.6)
axs[0].set_title(f"k-means (k=4)\nJ={J4:.2f}, $E_q$={Eq4:.3f}", fontsize=11)
axs[0].legend(loc="upper left", fontsize=8.5)
EDGES = [(0, 1), (0, 2), (1, 3), (2, 3)]                 # 2×2 lattice 上的相鄰節點
for ax, sig in zip(axs[1:], (2.0, 0.8, 0.05)):
    nodes, D = soms[sig]
    style(ax)
    ax.scatter(*X.T, s=70, color=C_DOT, edgecolor="white", lw=1.4, zorder=5)
    ax.scatter(*NODE0.T, s=40, marker="x", color=C_MUTE, zorder=3, label="initial nodes")
    ax.scatter(*mu4.T, s=230, marker="*", facecolor="none", edgecolor=C_KM, lw=1.2, zorder=4,
               label="k-means centroid")
    for a, b in EDGES:
        ax.plot(*nodes[[a, b]].T, color=C_SOM, lw=2, zorder=6)
    ax.scatter(*nodes.T, s=90, color=C_SOM, edgecolor="white", lw=1.2, zorder=7, label="SOM node")
    done = []
    for j, g in enumerate(GRID.astype(int)):
        same = [i for i in range(4) if np.allclose(nodes[i], nodes[j], atol=1e-3)]
        if j in done:
            continue
        done += same
        txt = "=".join(f"({GRID[i,0]:.0f},{GRID[i,1]:.0f})" for i in same)
        ax.annotate(txt, nodes[j], xytext=(6, -14), textcoords="offset points",
                    fontsize=8.5, color=C_SOM, fontweight="bold", zorder=8)
    ax.set_title(f"Batch SOM 2×2, $\\sigma$={sig}\n$J_{{BMU}}$={D['J']:.2f}, "
                 f"$E_q$={D['Eq']:.3f}, $E_t$={D['Et']:.3f}", fontsize=11)
    ax.legend(loc="upper left", fontsize=8)
    if sig == 0.05:
        ax.text(0.98, 0.02, "nodes = k-means started from the same\ninitial nodes (J = 16, exact match).\n"
                "Stars = seed-0 k-means: another of the\n5 tied global minima with J = 16.",
                transform=ax.transAxes, ha="right", va="bottom", fontsize=8, color="#52514e",
                bbox=dict(fc="white", ec=C_MUTE, alpha=0.9))
fig.tight_layout()
fig.savefig(HERE / "q1a_kmeans_som.png", dpi=150, bbox_inches="tight", facecolor="white")
plt.close(fig)
print("wrote q1a_kmeans_som.png")


# ═════════════════════════════════════════════════════════════════════════════
# (b) k-means (k=2) vs. 1D VAE
# ═════════════════════════════════════════════════════════════════════════════
km2 = KMeans(n_clusters=2, n_init=50, random_state=SEED).fit(X)
mu2, lab2 = km2.cluster_centers_, km2.labels_
if mu2[0].sum() > 0:                                     # 讓 cluster 0 在負側（外觀）
    mu2, lab2 = mu2[::-1], 1 - lab2
Xk = mu2[lab2]
tot = np.sum(X**2)
mse_k, r2_k = np.sum((X - Xk) ** 2) / M, 1 - np.sum((X - Xk) ** 2) / tot
print("\n===== (b) k-means k = 2 =====")
print(f"  mu = {mu2.tolist()},  labels = {lab2.tolist()}")
print(f"  MSE = {mse_k:.4f},  R² = {r2_k:.4f}")

print("\n===== (b) VAE (latent k = 1, 16 tanh, sigma_x² = 0.5, Adam 2000 epochs) =====")
vae = VAE(2, 16, 1, sigma_x2=0.5, seed=SEED)
hist = vae.fit(X, epochs=2000, lr=1e-2, log_every=500)
_, mu_z, lv_z = vae.encode(X)
s_z = np.exp(0.5 * lv_z)
Xv = vae.reconstruct(X)
mse_v, r2_v = np.sum((X - Xv) ** 2) / M, 1 - np.sum((X - Xv) ** 2) / tot
KLf = np.sum(mu_z**2 + s_z**2 - lv_z - 1) / (2 * M)
print(f"  final (deterministic) rec term = {np.sum((X-Xv)**2)/(2*0.5*M):.4f}, KL = {KLf:.4f}")
for n in range(M):
    print(f"  x{n+1} = ({X[n,0]:+.0f},{X[n,1]:+.0f}):  mu_z = {mu_z[n,0]:+.3f}, sigma_z = {s_z[n,0]:.3f}, "
          f"x̂ = ({Xv[n,0]:+.3f}, {Xv[n,1]:+.3f}), k-means label = {lab2[n]}")
print(f"  MSE = {mse_v:.4f},  R² = {r2_v:.4f}")
z1 = X @ np.array([1, 1]) / np.sqrt(2)
print(f"  corr(mu_z, PC1) = {np.corrcoef(mu_z[:,0], z1)[0,1]:+.4f}")
# EOF1 截斷（最佳 rank-1 線性重建）作為參考
mse_e = np.sum((X - np.outer(z1, [1, 1]) / np.sqrt(2)) ** 2) / M
print(f"  參考：EOF1 截斷  MSE = {mse_e:.4f}, R² = {1 - mse_e*M/tot:.4f}")

print("\n===== (b) 摘要表 =====")
print(f"{'method':22s} {'MSE':>8s} {'R²':>8s}")
print(f"{'k-means (k=2)':22s} {mse_k:8.4f} {r2_k:8.4f}")
print(f"{'VAE (k=1 latent)':22s} {mse_v:8.4f} {r2_v:8.4f}")
print(f"{'(ref) EOF1 truncation':22s} {mse_e:8.4f} {1-mse_e*M/tot:8.4f}")

# 生成樣本與流形曲線
zz = np.linspace(-2.5, 2.5, 401)[:, None]
curve = vae.decode(zz)[1]
zg = np.random.default_rng(123).standard_normal((100, 1))
Xg = vae.decode(zg)[1]

# ── 圖 (b) ──────────────────────────────────────────────────────────────────
CL = ["#2a78d6", "#eb6834"]
fig, (a0, a1) = plt.subplots(1, 2, figsize=(14, 5.6), gridspec_kw={"width_ratios": [1.1, 1]})
zp = np.linspace(-3.5, 3.5, 400)
a0.fill_between(zp, np.exp(-zp**2 / 2) / np.sqrt(2 * np.pi), color=C_MUTE, alpha=0.18)
a0.plot(zp, np.exp(-zp**2 / 2) / np.sqrt(2 * np.pi), color=C_MUTE, lw=1.6, label="prior $\\mathcal{N}(0,1)$")
yk = 0.03 + 0.035 * np.arange(M)                         # 垂直錯開，避免誤差棒重疊
for n in range(M):
    a0.errorbar(mu_z[n, 0], yk[n], xerr=s_z[n, 0], fmt="o", ms=7, color=CL[lab2[n]],
                ecolor=CL[lab2[n]], capsize=3, lw=1.4)
    a0.annotate(f"$x_{n+1}$", (mu_z[n, 0], yk[n]), xytext=(6, 3), textcoords="offset points", fontsize=8.5)
for c in (0, 1):
    a0.plot([], [], "o", color=CL[c], label=f"$\\mu_\\phi(x_n)\\pm\\sigma_\\phi$, k-means cluster {c+1}")
a0.set_xlabel("latent $z$"); a0.set_ylabel("prior density")
a0.set_xlim(-3.5, 3.5); a0.set_ylim(0, 0.45)
a0.set_title("1D latent space: encoded posteriors vs prior", fontsize=11)
a0.legend(loc="upper left", fontsize=8.5)
for s in ("top", "right"):
    a0.spines[s].set_visible(False)

style(a1)
a1.scatter(*Xg.T, s=14, color="#1baf7a", alpha=0.55, zorder=3, label="100 generated $g_\\theta(z),\\ z\\sim\\mathcal{N}(0,1)$")
a1.plot(*curve.T, color="#7b4fd6", lw=2.2, zorder=4, label="manifold $g_\\theta(z),\\ z\\in[-2.5,2.5]$")
for c in (0, 1):
    m = lab2 == c
    a1.scatter(*X[m].T, s=80, color=CL[c], edgecolor="white", lw=1.4, zorder=6)
a1.scatter(*mu2.T, s=300, marker="*", color="k", edgecolor="white", lw=0.8, zorder=7, label="k-means centroid (k=2)")
a1.scatter(*Xv.T, s=36, marker="D", facecolor="none", edgecolor="#7b4fd6", lw=1.2, zorder=5,
           label="VAE recon $g_\\theta(\\mu_\\phi(x_n))$")
a1.set_xlabel("station A"); a1.set_ylabel("station B")
a1.set_title(f"2D data space\nk-means: MSE={mse_k:.2f}, $R^2$={r2_k:.3f}   |   "
             f"VAE: MSE={mse_v:.2f}, $R^2$={r2_v:.3f}", fontsize=11)
a1.legend(loc="upper left", fontsize=8)
fig.tight_layout()
fig.savefig(HERE / "q1b_kmeans_vae.png", dpi=150, bbox_inches="tight", facecolor="white")
plt.close(fig)
print("wrote q1b_kmeans_vae.png")

# 訓練曲線（附錄）
fig, ax = plt.subplots(figsize=(6, 3.6))
ax.plot(hist[:, 0], label="L (stochastic)"); ax.plot(hist[:, 1], label="rec"); ax.plot(hist[:, 2], label="KL")
ax.set_yscale("log"); ax.set_xlabel("epoch"); ax.legend(); ax.set_title("VAE training (toy)")
fig.tight_layout(); fig.savefig(HERE / "q1b_vae_loss.png", dpi=130); plt.close(fig)
