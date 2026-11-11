# HW9 Q1：熱帶 omega 垂直結構 EOF（共變異特徵分解 vs SVD）
# 執行方式：把 W.nc 放在 hw9 資料夾，輸入  py hw9_q1.py   （或 py hw9_q1.py 路徑/W.nc）
import sys
import numpy as np
import xarray as xr
import matplotlib.pyplot as plt

path = sys.argv[1] if len(sys.argv) > 1 else "W.nc"
ds = xr.open_dataset(path)

# ---------- (a) 資料檢查 ----------
print(ds)
var = [v for v in ds.data_vars if ds[v].ndim >= 3][0]
w = ds[var]
dims = w.dims
lev = next(d for d in dims if d.lower() in ("level", "lev", "plev", "pressure_level", "isobaricinhpa", "pressure"))
tim = next(d for d in dims if "time" in d.lower())
hor = [d for d in dims if d not in (lev, tim)]  # 例如 (latitude, longitude)

print(f"\n變數 {var}，單位 {w.attrs.get('units', '?')}，long_name: {w.attrs.get('long_name', '?')}")
print("來源:", ds.attrs.get("source", ds.attrs.get("institution", ds.attrs.get("history", "?")))[:200])
print("維度:", dict(w.sizes))
for d in dims:
    c = ds[d].values
    print(f"  {d}: {c.min()} ~ {c.max()}  (n={c.size})")
t = ds[tim].values
if t.size > 1:
    print("  取樣間隔:", np.unique(np.diff(t))[:5])

# 排成 (time, level, space)
w = w.transpose(tim, lev, *hor)
nt, L = w.sizes[tim], w.sizes[lev]
W = w.values.reshape(nt, L, -1).astype(np.float64)
valid = np.all(np.isfinite(W), axis=(0, 1))     # 每個時間、每層都有值才保留
W = W[:, :, valid]
R = W.shape[2]
print(f"\n水平格點總數 {valid.size}，保留 {R}")

# 各格點、各層扣時間平均
Wp = W - W.mean(axis=0, keepdims=True)
# 樣本排序：(time, space) 中 space 變最快 → 列 index = it*R + ir
X = Wp.transpose(0, 2, 1).reshape(nt * R, L)
N = X.shape[0]
print(f"X: N = {N} (= {nt} times x {R} points), L = {L}")
print("各欄平均最大絕對值:", np.abs(X.mean(axis=0)).max(), " (資料標準差量級:", X.std(), ")")

# ---------- (b) 共變異矩陣特徵分解 ----------
C = X.T @ X / (N - 1)
lam, E = np.linalg.eigh(C)
idx = np.argsort(lam)[::-1]
lam, E = lam[idx], E[:, idx]
A = X @ E                                        # PCs, a_k = X e_k
print("\n(b) 正交性 max|E^T E - I| =", np.abs(E.T @ E - np.eye(L)).max())
var_pc = A.var(axis=0, ddof=1)
print("lambda_k       :", lam)
print("Var(a_k), N-1  :", var_pc)
print("max |Var - lambda| / lambda_1 =", np.abs(var_pc - lam).max() / lam[0])

# ---------- (c) SVD ----------
U, s, Vt = np.linalg.svd(X, full_matrices=False)   # economy SVD
V = Vt.T
lam_svd = s**2 / (N - 1)
print("\n(c) max |s^2/(N-1) - lambda| / lambda_1 =", np.abs(lam_svd - lam).max() / lam[0])
# 對齊符號後比較 EOF 與 PC
sign = np.sign(np.sum(V * E, axis=0))
V_al = V * sign
print("max |V - E| (符號對齊後) =", np.abs(V_al - E).max())
A_svd = U * s * sign                               # a_k = u_k sigma_k
print("max |U Sigma - X E| / max|A| =", np.abs(A_svd - A).max() / np.abs(A).max())

# ---------- (d) 解釋變異 ----------
f_eig = lam / lam.sum()
f_svd = s**2 / np.sum(s**2)
print("\n(d) f_k (eig) %:", np.round(100 * f_eig, 3))
print("    f_k (svd) %:", np.round(100 * f_svd, 3))
print("max |f_eig - f_svd| =", np.abs(f_eig - f_svd).max())
F_eig, F_svd = np.cumsum(f_eig), np.cumsum(f_svd)
K90_eig = int(np.argmax(F_eig > 0.90)) + 1
K90_svd = int(np.argmax(F_svd > 0.90)) + 1
print(f"K90: eig = {K90_eig}, svd = {K90_svd}  (F = {100*F_eig[K90_eig-1]:.2f}%)")

k = np.arange(1, L + 1)
fig, ax = plt.subplots(1, 2, figsize=(12, 4.5), constrained_layout=True)
ax[0].plot(k, 100 * f_eig, "o-", label="Covariance eig", ms=8)
ax[0].plot(k, 100 * f_svd, "x--", label="SVD", ms=8)
ax[0].set(xlabel="Mode k", ylabel="Explained variance (%)", title="Explained variance")
ax[1].plot(k, 100 * F_eig, "o-", label="Covariance eig", ms=8)
ax[1].plot(k, 100 * F_svd, "x--", label="SVD", ms=8)
ax[1].axhline(90, color="gray", ls=":", label="90%")
ax[1].axvline(K90_eig, color="r", ls=":", label=f"$K_{{90}}$ = {K90_eig}")
ax[1].set(xlabel="Mode K", ylabel="Cumulative explained variance (%)", title="Cumulative")
for a in ax:
    a.set_xticks(k)
    a.legend()
    a.grid(alpha=0.3)
fig.savefig("q1_variance.png", dpi=150)

# 前幾個 EOF 垂直剖面（參考用）
p = ds[lev].values
fig, ax = plt.subplots(figsize=(5, 6), constrained_layout=True)
for j in range(min(3, L)):
    ax.plot(E[:, j], p, "o-", label=f"EOF{j+1} ({100*f_eig[j]:.1f}%)")
ax.axvline(0, color="k", lw=0.8)
if p[0] < p[-1]:
    ax.invert_yaxis()
ax.set(xlabel="EOF loading", ylabel=f"{lev}", title="Leading vertical EOFs")
ax.legend()
fig.savefig("q1_eofs.png", dpi=150)
print("已存檔 q1_variance.png, q1_eofs.png")
