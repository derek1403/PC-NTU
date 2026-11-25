# HW11 Q1 (c)：ERA5 DJF Z200 anomalies 上的 k-means、Batch SOM、VAE（皆為 k = 4）
# 執行方式：py -X utf8 hw11_q1c.py
#
# 資料沿用 hw10 的 ERA5_Z200_anom_DJF.nc（不重複複製）。
# 記憶體：只保留一份加權矩陣 Xw (float32, 3881 x 38400 ≈ 0.6 GB)。
import time
from pathlib import Path

import numpy as np
import xarray as xr
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

from vae_numpy import VAE

HERE = Path(__file__).resolve().parent
DATA = HERE.parent / "hw10" / "ERA5_Z200_anom_DJF.nc"
SEED = 0
T0 = time.time()
log = lambda *a: print(f"[{time.time()-T0:6.0f}s]", *a, flush=True)

# ── 讀資料、Xw = X √cosθ ─────────────────────────────────────────────────────
ds = xr.open_dataset(DATA)
z = ds["z200_anom"].transpose("time", "lat", "lon")
lat, lon, times = ds["lat"].values, ds["lon"].values, ds["time"].values
M, ny, nx = z.shape
N = ny * nx
Xw = z.values.reshape(M, N).astype(np.float32)
ds.close(); del z
Xw -= Xw.mean(0, keepdims=True)
wvec = np.repeat(np.sqrt(np.cos(np.deg2rad(lat))), nx).astype(np.float32)
area = np.repeat(np.cos(np.deg2rad(lat)), nx)
Xw *= wvec
log(f"M = {M}, N = {N} ({ny} x {nx})")

TOT = float(np.sum(Xw.astype(np.float64) ** 2))           # ||Xw||_F²
SUMCOS = area.sum()
meanvar = TOT / (M * N)                                   # 各格點變異的平均（zero-mean）
log(f"||Xw||_F² = {TOT:.4e},  mean grid-point variance of Xw = {meanvar:.2f} m²")


def unweight(v):
    return v / wvec


def pcorr(a, b):
    """面積加權 (cos θ)、扣除空間平均的 pattern correlation（物理單位）。"""
    a = a - np.sum(area * a) / SUMCOS
    b = b - np.sum(area * b) / SUMCOS
    return np.sum(area * a * b) / np.sqrt(np.sum(area * a * a) * np.sum(area * b * b))


def sse_lookup(C, lab, bs=500):
    """Σ_n ||x_n,w − C[lab_n]||²（分批計算，不另存 X̂）。"""
    s = 0.0
    for i0 in range(0, M, bs):
        r = Xw[i0:i0 + bs] - C[lab[i0:i0 + bs]]
        s += float(np.sum(r.astype(np.float64) ** 2))
    return s


def sqdist(C, bs=500):
    """||x_n − c_j||² [M × k]，以 ||x||² − 2x·c + ||c||² 計算（float64 累加）。"""
    out = np.empty((M, C.shape[0]))
    cc = np.sum(C.astype(np.float64) ** 2, 1)
    for i0 in range(0, M, bs):
        xb = Xw[i0:i0 + bs].astype(np.float64)
        out[i0:i0 + bs] = np.sum(xb**2, 1)[:, None] - 2 * xb @ C.T.astype(np.float64) + cc
    return np.maximum(out, 0)


def metrics(sse):
    return dict(SSE=sse, RMSE=np.sqrt(sse / (M * SUMCOS)), R2=1 - sse / TOT)


# ═════════════════════════════════════════════════════════════════════════════
# 參考：EOF（Gram 矩陣），用來初始化 SOM，並當作 rank-4 線性重建的基準
# ═════════════════════════════════════════════════════════════════════════════
G = np.zeros((M, M))
for i0 in range(0, N, 4800):
    blk = Xw[:, i0:i0 + 4800].astype(np.float64)
    G += blk @ blk.T
s2, U = np.linalg.eigh(G); del G
o = np.argsort(s2)[::-1]; s2, U = np.clip(s2[o], 0, None), U[:, o]
lam = s2 / M
E4 = np.stack([(U[:, j].astype(np.float32) @ Xw) / np.sqrt(s2[j]) for j in range(4)], 1)  # [N × 4]
res = {"EOF-4 truncation (ref)": metrics(TOT - s2[:4].sum())}
log(f"EOF 前 4 個解釋變異 (%) = {np.round(100*lam[:4]/lam.sum(), 2)}, 累積 {100*s2[:4].sum()/TOT:.2f}%")

# ═════════════════════════════════════════════════════════════════════════════
# (a) k-means, k = 4
# ═════════════════════════════════════════════════════════════════════════════
km = KMeans(n_clusters=4, n_init=20, random_state=SEED).fit(Xw)
cnt = np.bincount(km.labels_, minlength=4); oo = np.argsort(-cnt)
remap = np.empty(4, int); remap[oo] = np.arange(4)
lab_k = remap[km.labels_]; Ck = km.cluster_centers_[oo].astype(np.float32); cnt_k = cnt[oo]
res["k-means (k=4)"] = metrics(sse_lookup(Ck, lab_k))
log(f"k-means 完成：頻率 (%) = {np.round(100*cnt_k/M, 1).tolist()}, inertia = {km.inertia_:.4e}")
del km

# ═════════════════════════════════════════════════════════════════════════════
# (b) Batch SOM, 2×2, σ = 0.8（EOF1/EOF2 線性初始化）
# ═════════════════════════════════════════════════════════════════════════════
GRID = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], float)
GD2 = ((GRID[:, None] - GRID[None]) ** 2).sum(-1)
GL1 = np.abs(GRID[:, None] - GRID[None]).sum(-1)
SIG = 0.8
H = np.exp(-GD2 / (2 * SIG**2))
nodes = np.stack([(2 * g[0] - 1) * np.sqrt(lam[0]) * E4[:, 0] + (2 * g[1] - 1) * np.sqrt(lam[1]) * E4[:, 1]
                  for g in GRID]).astype(np.float32)
prev = None
for it in range(1, 201):
    d = sqdist(nodes)
    c = d.argmin(1)
    Hn = H[c].astype(np.float32)                          # [M × 4]
    nodes = ((Hn.T @ Xw) / Hn.sum(0)[:, None]).astype(np.float32)
    if prev is not None and np.array_equal(c, prev):
        break
    prev = c
d = sqdist(nodes)
order = np.argsort(d, 1)
lab_s, c2 = order[:, 0], order[:, 1]
Et = np.mean(GL1[lab_s, c2] > 1)
Eq = np.mean(np.sqrt(d[np.arange(M), lab_s]))
cnt_s = np.bincount(lab_s, minlength=4)
res["Batch SOM (2x2, σ=0.8)"] = metrics(sse_lookup(nodes, lab_s))
log(f"SOM 完成（{it} 次迭代）：BMU 頻率 (%) = {np.round(100*cnt_s/M,1).tolist()}, Eq = {Eq:.1f}, Et = {Et:.3f}")

# ═════════════════════════════════════════════════════════════════════════════
# (c) VAE, 4 維 latent
#     σx² = mean grid-point variance。為了數值穩定，訓練時把資料除以 s = √σx²，
#     此時 σx² 變成 1；兩個目標函數完全相同（||x−x̂||²/σx² 對同時縮放不變，KL 不受影響）。
# ═════════════════════════════════════════════════════════════════════════════
s = np.float32(np.sqrt(meanvar))
Xw /= s
HID, EPOCHS, LR, BATCH = 128, 150, 1e-3, 64
vae = VAE(N, HID, 4, sigma_x2=1.0, seed=SEED, dtype=np.float32)
log(f"VAE 開始訓練：hidden={HID}, epochs={EPOCHS}, batch={BATCH}, lr={LR}")
hist = vae.fit(Xw, epochs=EPOCHS, lr=LR, batch=BATCH, log_every=10)
mu_z = np.concatenate([vae.encode(Xw[i:i + 500])[1] for i in range(0, M, 500)])
lv_z = np.concatenate([vae.encode(Xw[i:i + 500])[2] for i in range(0, M, 500)])
sse_v = 0.0
for i0 in range(0, M, 500):
    r = Xw[i0:i0 + 500] - vae.decode(mu_z[i0:i0 + 500])[1]
    sse_v += float(np.sum(r.astype(np.float64) ** 2))
sse_v *= float(s) ** 2
Xw *= s                                                   # 還原單位
res["VAE (4-D latent)"] = metrics(sse_v)
KL = np.sum(mu_z**2 + np.exp(lv_z) - lv_z - 1) / (2 * M)
log(f"VAE 完成：KL = {KL:.2f} nats/sample, 平均 σ_z = {np.exp(0.5*lv_z).mean(0).round(3).tolist()}, "
    f"std(μ_z) = {mu_z.std(0).round(3).tolist()}")

# ── 摘要表 ───────────────────────────────────────────────────────────────────
print("\n===== Summary (area-weighted) =====")
print(f"{'method':26s} {'RMSE (m)':>10s} {'R²_recon':>10s}")
for k, v in res.items():
    print(f"{k:26s} {v['RMSE']:10.2f} {v['R2']:10.4f}")
print(f"（參考：若 X̂ = 0，RMSE = {np.sqrt(TOT/(M*SUMCOS)):.2f} m）")

# k-means centroid 與 SOM 節點的對應
Rks = np.array([[pcorr(unweight(Ck[i]), unweight(nodes[j])) for j in range(4)] for i in range(4)])
print("\npattern corr r(k-means μ_i, SOM n_j):  rows = cluster 1..4, cols = n(0,0) n(0,1) n(1,0) n(1,1)")
print(np.round(Rks, 3))
amp = lambda f: np.sqrt(np.sum(area * f**2) / SUMCOS)
print("RMS amplitude (m) k-means:", [round(amp(unweight(Ck[i])), 1) for i in range(4)],
      " SOM:", [round(amp(unweight(nodes[j])), 1) for j in range(4)])

# ═════════════════════════════════════════════════════════════════════════════
# 極端日
# ═════════════════════════════════════════════════════════════════════════════
nrm = np.sqrt(np.sum(Xw.astype(np.float64) ** 2, 1))
n0 = int(np.argmax(nrm))
x_obs = unweight(Xw[n0])
x_k = unweight(Ck[lab_k[n0]])
x_s = unweight(nodes[lab_s[n0]])
x_v = unweight(vae.decode(mu_z[n0:n0 + 1])[1][0] * s)
day = str(np.datetime_as_string(times[n0], unit="D"))
fields = [x_obs, x_k, x_s, x_v]
rr = [1.0] + [pcorr(x_obs, f) for f in fields[1:]]
ew = lambda f: np.sqrt(np.sum(area * (x_obs - f) ** 2) / SUMCOS)
print(f"\n極端日：{day}（index {n0}），||x_w|| = {nrm[n0]:.1f}（平均 {nrm.mean():.1f}）")
print(f"  k-means cluster {lab_k[n0]+1}, SOM BMU {tuple(GRID[lab_s[n0]].astype(int).tolist())}, "
      f"VAE μ_z = {mu_z[n0].round(2).tolist()}")
for nm, f, r in zip(["obs", "k-means", "SOM", "VAE"], fields, rr):
    print(f"  {nm:8s} r = {r:.3f}, area-wt RMS = {amp(f):6.1f} m, error RMS = {ew(f):6.1f} m")

try:
    import cartopy.crs as ccrs
    HAS_CARTOPY = True
except ImportError:
    HAS_CARTOPY = False


def make_axes(nrow, ncol, figsize):
    kw = {"subplot_kw": {"projection": ccrs.PlateCarree(central_longitude=200)}} if HAS_CARTOPY else {}
    fig, axs = plt.subplots(nrow, ncol, figsize=figsize, squeeze=False,
                            gridspec_kw={"hspace": 0.35, "wspace": 0.12}, **kw)
    return fig, axs.ravel()


def plot_map(ax, field, title, vmax):
    lev = np.linspace(-vmax, vmax, 21)
    kw = {"transform": ccrs.PlateCarree()} if HAS_CARTOPY else {}
    cf = ax.contourf(lon, lat, field.reshape(ny, nx), levels=lev, cmap="RdBu_r", extend="both", **kw)
    if HAS_CARTOPY:
        ax.coastlines(lw=0.5)
        ax.set_extent([lon.min(), lon.max(), lat.min(), lat.max()], crs=ccrs.PlateCarree())
    else:
        ax.set_xlabel("lon (°E)"); ax.set_ylabel("lat (°N)")
    ax.set_title(title, fontsize=10)
    return cf


def save(fig, cf, name):
    fig.colorbar(cf, ax=fig.axes, orientation="horizontal", fraction=0.05, pad=0.1, shrink=0.6,
                 label="Z200 anomaly (m)")
    fig.savefig(HERE / name, dpi=150, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    log("wrote", name)


fig, axs = make_axes(1, 4, (24, 3.9))
vm = float(np.ceil(np.percentile(np.abs(x_obs), 99.5) / 20) * 20)
titles = [f"Observed ERA5 Z200, {day}",
          f"k-means regime {lab_k[n0]+1}:  r = {rr[1]:.2f}",
          f"SOM BMU {tuple(GRID[lab_s[n0]].astype(int).tolist())}:  r = {rr[2]:.2f}",
          f"VAE $g_\\theta(\\mu_\\phi(x))$:  r = {rr[3]:.2f}"]
for ax, f, t in zip(axs, fields, titles):
    cf = plot_map(ax, f, t, vm)
save(fig, cf, "q1c_extreme_day.png")

# 附錄：k-means centroid 與 SOM 節點
fig, axs = make_axes(2, 4, (24, 7.6))
pats = [unweight(Ck[i]) for i in range(4)] + [unweight(nodes[j]) for j in range(4)]
vm = float(np.ceil(max(np.percentile(np.abs(p), 99.5) for p in pats) / 10) * 10)
for i in range(4):
    plot_map(axs[i], pats[i], f"k-means $\\mu_{i+1}$  ({100*cnt_k[i]/M:.1f}% of days)", vm)
for j in range(4):
    g = tuple(GRID[j].astype(int).tolist())
    cf = plot_map(axs[4 + j], pats[4 + j], f"SOM node {g}  ({100*cnt_s[j]/M:.1f}% of days)", vm)
save(fig, cf, "q1c_patterns.png")

fig, ax = plt.subplots(figsize=(6, 3.6))
ax.plot(hist[:, 1], label="rec"); ax.plot(hist[:, 2], label="KL")
ax.set_yscale("log"); ax.set_xlabel("epoch"); ax.legend(); ax.set_title("VAE training (ERA5, scaled units)")
fig.tight_layout(); fig.savefig(HERE / "q1c_vae_loss.png", dpi=130); plt.close(fig)

np.savez(HERE / "q1c_results.npz", Ck=Ck, nodes=nodes, lab_k=lab_k, lab_s=lab_s, mu_z=mu_z, lv_z=lv_z,
         hist=hist, n0=n0, fields=np.stack(fields), rr=rr,
         table=np.array([[v["RMSE"], v["R2"]] for v in res.values()]), names=np.array(list(res)))
log("done; cartopy =", HAS_CARTOPY)
