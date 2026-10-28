# HW7 Q2：AR(1) 的有效樣本數
# 執行方式：在 hw7 資料夾輸入  py hw7_q2.py
import numpy as np
import matplotlib.pyplot as plt

SEED = 2026
M = 20000                     # Monte Carlo 重複次數
N_REF = 10                    # 獨立參考樣本數
TOL = 1.01                    # 允許 1% 較大的抽樣變異數
phis = [0.0, 0.1, 0.5, 0.8, 0.9, 1.0]
rng = np.random.default_rng(SEED)


# S(rho, N) = sum_{k=1}^{N-1} (1 - k/N) rho^k
def S(rho, N):
    k = np.arange(1, N)
    return np.sum((1 - k / N) * rho**k)


# 精確有限 N 變異數
def var_mean(phi, N):
    return (1 + 2 * S(phi, N)) / N


def var_var(phi, N):
    return 2 * (1 + 2 * S(phi**2, N)) / N


# 大 N 近似：自相關和延伸到無窮
def var_mean_inf(phi, N):
    return (1 + phi) / (1 - phi) / N


def var_var_inf(phi, N):
    return 2 * (1 + phi**2) / (1 - phi**2) / N


# 找最小 N >= 10 使 var(N) <= TOL * ref；找不到回傳 None
def threshold(vfun, phi, ref, N_max=100000):
    if phi == 1.0:
        return None            # 變異數不隨 N 下降，見說明
    for N in range(N_REF, N_max + 1):
        if vfun(phi, N) <= TOL * ref:
            return N
    return None


ref_mean = 1 / N_REF          # Var(Y_bar_10)
ref_var = 2 / N_REF           # Var(V_Y,10)

print("seed =", SEED, " M =", M)
print("\n===== (a)(b) 理論門檻 =====")
print("phi   N_mean  N_mean(大N)  N_var  N_var(大N)  Var(Xbar_10)  Var(V_10)  N_eff(10)  nu_eff(10)")
N_mean, N_var, N_mean_inf, N_var_inf = {}, {}, {}, {}
for phi in phis:
    N_mean[phi] = threshold(var_mean, phi, ref_mean)
    N_var[phi] = threshold(var_var, phi, ref_var)
    if phi < 1:
        N_mean_inf[phi] = max(N_REF, int(np.ceil((1 + phi) / (1 - phi) / (TOL * ref_mean) - 1e-12)))
        N_var_inf[phi] = max(N_REF, int(np.ceil(2 * (1 + phi**2) / (1 - phi**2) / (TOL * ref_var) - 1e-12)))
    else:
        N_mean_inf[phi] = N_var_inf[phi] = None
    vm10, vv10 = var_mean(phi, 10), var_var(phi, 10)
    print("%.1f   %6s  %10s  %5s  %9s  %12.4f  %9.4f  %9.3f  %10.3f" % (
        phi, N_mean[phi], N_mean_inf[phi], N_var[phi], N_var_inf[phi],
        vm10, vv10, 1 / vm10, 2 / vv10))

# ===== (b) 圖：門檻樣本數 vs phi =====
fig, ax = plt.subplots(figsize=(7, 4.5))
fin = [p for p in phis if N_mean[p] is not None]
ax.plot(fin, [N_mean[p] for p in fin], "o-", color="C0", label="mean, exact")
ax.plot(fin, [N_mean_inf[p] for p in fin], "s--", color="C0", mfc="none", label="mean, large-N approx.")
ax.plot(fin, [N_var[p] for p in fin], "o-", color="C3", label="variance, exact")
ax.plot(fin, [N_var_inf[p] for p in fin], "s--", color="C3", mfc="none", label="variance, large-N approx.")
ax.axvline(1.0, color="gray", ls=":")
ax.annotate("phi = 1:\nno finite threshold\n(N -> infinity)", xy=(1.0, 150), xytext=(0.62, 150),
            arrowprops=dict(arrowstyle="->", color="gray"), color="gray")
ax.plot([1.0], [ax.get_ylim()[1] * 0.95], marker="^", color="k", ms=10, ls="none")
ax.set_yscale("log")
ax.set_xlabel("phi")
ax.set_ylabel("threshold sample size N")
ax.set_title("Smallest N with Var(X-estimator) <= 1.01 Var(Y-estimator, N=10)")
ax.legend()
ax.grid(alpha=0.3, which="both")
fig.tight_layout()
fig.savefig("q2_threshold.png", dpi=150)


# 產生 M 條長度 N 的 AR(1) 序列 X_1..X_N（X_0 ~ N(0,1)）
def ar1(phi, N):
    x = rng.normal(0, 1, M)
    out = np.empty((M, N))
    c = np.sqrt(1 - phi**2)
    for n in range(N):
        x = phi * x + c * rng.normal(0, 1, M)
        out[:, n] = x
    return out


def skew(a):
    a = a - a.mean()
    return np.mean(a**3) / np.mean(a**2) ** 1.5


# ===== (c) Monte Carlo =====
print("\n===== (c) Monte Carlo（每格：模擬平均 / 模擬變異數 / 理論變異數 / 偏度）=====")
phis_mc = [p for p in phis if N_mean[p] is not None]
fig, axes = plt.subplots(len(phis_mc), 2, figsize=(11, 2.6 * len(phis_mc)))
for r, phi in enumerate(phis_mc):
    Y = rng.normal(0, 1, (M, N_REF))
    X10 = ar1(phi, N_REF)
    Xm = ar1(phi, N_mean[phi])
    Xv = ar1(phi, N_var[phi])
    cases = {
        "mean": [("(i) indep., N=10", Y.mean(1), ref_mean),
                 ("(ii) AR(1), N=10", X10.mean(1), var_mean(phi, 10)),
                 ("(iii) AR(1), N=%d" % N_mean[phi], Xm.mean(1), var_mean(phi, N_mean[phi]))],
        "variance": [("(i) indep., N=10", (Y**2).mean(1), ref_var),
                     ("(ii) AR(1), N=10", (X10**2).mean(1), var_var(phi, 10)),
                     ("(iii) AR(1), N=%d" % N_var[phi], (Xv**2).mean(1), var_var(phi, N_var[phi]))],
    }
    for c, key in enumerate(["mean", "variance"]):
        ax = axes[r, c]
        allv = np.concatenate([v for _, v, _ in cases[key]])
        lo, hi = np.percentile(allv, [0.1, 99.9])
        bins = np.linspace(lo, hi, 61)             # 同一比較共用 bins
        print("\nphi = %.1f, %s estimator" % (phi, key))
        for (lab, v, vth), col in zip(cases[key], ["C0", "C1", "C2"]):
            ax.hist(v, bins=bins, density=True, histtype="step", lw=1.5, color=col, label=lab)
            print("  %-20s E = %+.4f  Var = %.5f  (theory %.5f)  skew = %+.3f" % (lab, v.mean(), v.var(ddof=1), vth, skew(v)))
        ax.set_title("phi = %.1f, %s estimator" % (phi, "mean" if key == "mean" else "variance (V)"))
        ax.legend(fontsize=7)
fig.tight_layout()
fig.savefig("q2_mc_hist.png", dpi=130)

# ===== phi = 1：示意 =====
print("\n===== phi = 1 =====")
for N in [10, 100, 1000]:
    print("N = %4d  Var(Xbar) = %.3f  Var(V) = %.3f" % (N, var_mean(1.0, N), var_var(1.0, N)))
