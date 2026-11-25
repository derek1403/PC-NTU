# HW10 Q1 (c)：ERA5 DJF Z200 anomalies 的 EOF 與 k-means
# 執行方式：py -X utf8 hw10_q1c.py
#
# 記憶體考量：資料 3881 x 38400 (float32 約 0.6 GB)。程式只保留一份加權矩阵 Xw，
# 未加權的量用  X = Xw / sqrt(cos θ)  (逐格點) 還原，不另外存一份 X。
from pathlib import Path

import numpy as np
import xarray as xr
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

HERE = Path(__file__).resolve().parent
SEED = 0

try:                                   # 有 cartopy 就畫海岸線
    import cartopy.crs as ccrs
    HAS_CARTOPY = True
except ImportError:
    HAS_CARTOPY = False

# ── 讀資料、整理成 X [M x N] ──────────────────────────────────────────────────
ds = xr.open_dataset(HERE / "ERA5_Z200_anom_DJF.nc")
z = ds["z200_anom"].transpose("time", "lat", "lon")
lat, lon = ds["lat"].values, ds["lon"].values
M, ny, nx = z.shape
N = ny * nx
print(f"M = {M}, (lat, lon) = ({ny}, {nx}), N = {N}, units = {z.attrs.get('units', 'm')}")

Xw = z.values.reshape(M, N).astype(np.float32)          # 先放 X
Xw -= Xw.mean(axis=0, keepdims=True)                     # 確保 zero-mean
print("max |column mean| =", np.abs(Xw.mean(axis=0)).max())

w = np.sqrt(np.cos(np.deg2rad(lat)))                     # sqrt(cos θ)，長度 ny
wvec = np.repeat(w, nx).astype(np.float32)               # 對應到 N 個格點
Xw *= wvec                                               # 原地加權：Xw = X * sqrt(cos θ)
area = np.repeat(np.cos(np.deg2rad(lat)), nx)            # 面積權重 cos θ（算 pattern corr 用）


def unweight(v):
    """加權空間 → 物理單位 (m)。"""
    return v / wvec


def to_map(v):
    return np.asarray(v).reshape(ny, nx)


def pcorr(a, b):
    """面積加權 (cos θ) 的 centered spatial pattern correlation。"""
    a = a - np.sum(area * a) / area.sum()
    b = b - np.sum(area * b) / area.sum()
    return np.sum(area * a * b) / np.sqrt(np.sum(area * a * a) * np.sum(area * b * b))


# ═════════════════════════════════════════════════════════════════════════════
# EOF：用 M x M 的 Gram 矩陣 Xw Xw^T（N >> M）
# ═════════════════════════════════════════════════════════════════════════════
G = (Xw @ Xw.T).astype(np.float64)                       # [M x M]
s2, U = np.linalg.eigh(G)
o = np.argsort(s2)[::-1]
s2, U = np.clip(s2[o], 0, None), U[:, o]
lam = s2 / M                                             # C = Xw^T Xw / M 的特徵值
frac = lam / lam.sum()
print("\n前 5 個解釋變異比例 (%):", np.round(100 * frac[:5], 2))

K = 2
# EOF e_j = Xw^T u_j / sigma_j（單位向量，加權空間）
Ew = np.stack([(Xw.T @ U[:, j].astype(np.float32)) / np.sqrt(s2[j]) for j in range(K)], axis=1)
Ew = Ew.astype(np.float64)
Zpc = np.sqrt(s2[:K]) * U[:, :K]                         # PC z_j = Xw e_j = sigma_j u_j
print("EOF 正交性 E^T E =\n", np.round(Ew.T @ Ew, 6))
print("var(z_j) =", Zpc.var(axis=0), " lam_j =", lam[:K])

Zt = (Zpc - Zpc.mean(0)) / Zpc.std(0)                    # 標準化 PC
# d_j = z~_j^T X / M  （X 未加權 = Xw / wvec）
D = np.stack([unweight((Zt[:, j].astype(np.float32) @ Xw) / M) for j in range(K)], axis=1)

# 符號約定：讓 d_j 在其最大絕對值處為正（純屬外觀）
for j in range(K):
    if D[np.argmax(np.abs(D[:, j])), j] < 0:
        D[:, j] *= -1; Ew[:, j] *= -1; Zpc[:, j] *= -1; Zt[:, j] *= -1


# ═════════════════════════════════════════════════════════════════════════════
# 繪圖工具
# ═════════════════════════════════════════════════════════════════════════════
def make_axes(nrow, ncol, figsize):
    kw = {"subplot_kw": {"projection": ccrs.PlateCarree(central_longitude=200)}} if HAS_CARTOPY else {}
    fig, axs = plt.subplots(nrow, ncol, figsize=figsize, squeeze=False,
                            gridspec_kw={"hspace": 0.28 if HAS_CARTOPY else 0.38, "wspace": 0.12}, **kw)
    return fig, axs.ravel()


def plot_map(ax, field, title, vmax, cmap="RdBu_r"):
    lev = np.linspace(-vmax, vmax, 21)
    kw = {"transform": ccrs.PlateCarree()} if HAS_CARTOPY else {}
    cf = ax.contourf(lon, lat, to_map(field), levels=lev, cmap=cmap, extend="both", **kw)
    if HAS_CARTOPY:
        ax.coastlines(lw=0.6)
        ax.set_extent([lon.min(), lon.max(), lat.min(), lat.max()], crs=ccrs.PlateCarree())
        gl = ax.gridlines(draw_labels=True, lw=0.3, alpha=0.5)
        gl.top_labels = gl.right_labels = False
    else:
        ax.set_xlabel("lon (°E)"); ax.set_ylabel("lat (°N)")
        ax.set_aspect("auto")
    ax.set_title(title, fontsize=10.5)
    return cf


def nice_vmax(*fields):
    v = max(np.nanpercentile(np.abs(f), 99.5) for f in fields)
    return float(np.ceil(v / 10) * 10)


def save(fig, cf, name, label="Z200 anomaly (m)"):
    fig.colorbar(cf, ax=fig.axes, orientation="horizontal", fraction=0.05, pad=0.08,
                 shrink=0.7, label=label)
    fig.savefig(HERE / name, dpi=150, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("wrote", name)


# ── EOF 圖 ───────────────────────────────────────────────────────────────────
fig, axs = make_axes(1, 2, (15, 4.6))
vm = nice_vmax(D[:, 0], D[:, 1])
for j in range(K):
    cf = plot_map(axs[j], D[:, j], f"EOF{j+1} regression $d_{j+1}$ (m)  —  "
                                   f"{100*frac[j]:.1f}% variance", vm)
save(fig, cf, "q1c_eof.png")


# ═════════════════════════════════════════════════════════════════════════════
# k-means（在 Xw 上）
# ═════════════════════════════════════════════════════════════════════════════
def run_kmeans(k):
    km = KMeans(n_clusters=k, n_init=20, random_state=SEED).fit(Xw)
    lab = km.labels_
    cnt = np.bincount(lab, minlength=k)
    o = np.argsort(-cnt)                                  # 依出現頻率排序
    remap = np.empty(k, int); remap[o] = np.arange(k)
    lab = remap[lab]
    Cw = km.cluster_centers_[o].astype(np.float64)        # 加權空間的 centroid
    mu = np.stack([unweight(Cw[i]) for i in range(k)])    # 物理單位 (m)
    return lab, Cw, mu, cnt[o]


res = {}
for k in (2, 4):
    lab, Cw, mu, cnt = run_kmeans(k)
    res[k] = (lab, Cw, mu, cnt)
    print(f"\nk = {k}: |S_i| = {cnt.tolist()}, 頻率 (%) = {np.round(100*cnt/M, 1).tolist()}")
    nr, nc = (1, 2) if k == 2 else (2, 2)
    fig, axs = make_axes(nr, nc, (15, 4.6) if k == 2 else (15, 6.4))
    vm = nice_vmax(*mu)
    for i in range(k):
        cf = plot_map(axs[i], mu[i], f"k={k}, cluster {i+1}: $\\mu_{i+1}$ (m)  —  "
                                     f"{100*cnt[i]/M:.1f}% of days", vm)
    save(fig, cf, f"q1c_kmeans_k{k}.png")


# ═════════════════════════════════════════════════════════════════════════════
# 比較 (a)：k = 2 的相位不對稱
# ═════════════════════════════════════════════════════════════════════════════
lab2, Cw2, mu2, cnt2 = res[2]
r1, r2 = pcorr(D[:, 0], mu2[0]), pcorr(D[:, 0], mu2[1])
pos = Zt[:, 0] > 0
agree = max(np.mean((lab2 == 0) == pos), np.mean((lab2 == 1) == pos))
print("\n===== 比較 (a) k = 2 =====")
print(f"r(d1, mu1) = {r1:.3f},  r(d1, mu2) = {r2:.3f}")
print(f"r(d2, mu1) = {pcorr(D[:,1], mu2[0]):.3f},  r(d2, mu2) = {pcorr(D[:,1], mu2[1]):.3f}")
print(f"label 與 sign(z~1) 的時間一致率 = {100*agree:.1f}%")
S = mu2[0] + mu2[1]
amp = lambda f: np.sqrt(np.sum(area * f**2) / area.sum())   # 面積加權 RMS
print(f"RMS: |mu1| = {amp(mu2[0]):.1f} m, |mu2| = {amp(mu2[1]):.1f} m, |mu1+mu2| = {amp(S):.1f} m")
print(f"max |mu1+mu2| = {np.abs(S).max():.1f} m")
# 由 zero-mean 限制 |S1| mu1 + |S2| mu2 = 0 → mu1 + mu2 = (1 - |S1|/|S2|) mu1
print(f"檢查 |S1|mu1+|S2|mu2 = 0: max = {np.abs(cnt2[0]*mu2[0] + cnt2[1]*mu2[1]).max():.2e} m")
print(f"pcorr(mu1, -mu2) = {pcorr(mu2[0], -mu2[1]):.4f}  (應為 1)")

fig, axs = make_axes(1, 1, (8.5, 4.6))
vm = nice_vmax(S)
cf = plot_map(axs[0], S, f"k=2 phase asymmetry $\\mu_1+\\mu_2$ (m)\n"
                         f"$r(d_1,\\mu_1)$={r1:.2f}, $r(d_1,\\mu_2)$={r2:.2f}, "
                         f"agreement with sign($\\tilde z_1$) = {100*agree:.1f}%", vm)
save(fig, cf, "q1c_k2_asymmetry.png")


# ═════════════════════════════════════════════════════════════════════════════
# 比較 (b)：k = 4 的 EOF 截斷殘差
# ═════════════════════════════════════════════════════════════════════════════
lab4, Cw4, mu4, cnt4 = res[4]
print("\n===== 比較 (b) k = 4 =====")
coef = Cw4 @ Ew                                          # (mu_i,w · e_j)
mu_hat = np.stack([unweight(coef[i] @ Ew.T) for i in range(4)])
resid = mu4 - mu_hat
for i in range(4):
    ev = 1 - np.sum(area * resid[i]**2) / np.sum(area * mu4[i]**2)
    print(f"cluster {i+1}: 投影係數 (e1, e2) = ({coef[i,0]:8.1f}, {coef[i,1]:8.1f}), "
          f"RMS mu = {amp(mu4[i]):5.1f} m, RMS resid = {amp(resid[i]):5.1f} m, "
          f"2-EOF 解釋 {100*ev:5.1f}%, r(mu, mu_hat) = {pcorr(mu4[i], mu_hat[i]):.3f}")

R = np.array([[pcorr(mu4[i], mu4[j]) for j in range(4)] for i in range(4)])
print("\n4x4 pattern correlation r(mu_i, mu_j):")
print("        " + "".join(f"  mu{j+1:<5d}" for j in range(4)))
for i in range(4):
    print(f"  mu{i+1}  " + "".join(f"{R[i,j]:8.3f}" for j in range(4)))

fig, axs = make_axes(2, 2, (15, 6.4))
vm = nice_vmax(*resid)
for i in range(4):
    cf = plot_map(axs[i], resid[i], f"k=4 cluster {i+1}: $\\mu_{i+1}-\\hat\\mu_{i+1}$ (m)  —  "
                                    f"RMS {amp(resid[i]):.1f} m ({100*cnt4[i]/M:.1f}% of days)", vm)
save(fig, cf, "q1c_k4_residual.png")

np.savez(HERE / "q1c_results.npz", D=D, frac=frac[:10], mu2=mu2, cnt2=cnt2, mu4=mu4,
         cnt4=cnt4, mu_hat=mu_hat, R=R, lat=lat, lon=lon)
print("\ncartopy:", HAS_CARTOPY)
