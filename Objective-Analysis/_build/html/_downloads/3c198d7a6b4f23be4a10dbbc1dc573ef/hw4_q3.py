# HW4 Q3：線性迴歸三種數值方法比較（lstsq / 正規方程 / 梯度下降）
# 執行方式：在 hw4 資料夾輸入  py hw4_q3.py
import time
import numpy as np
import matplotlib.pyplot as plt

# ===== 產生資料 =====
SEED = 2026
n = 10**6
rng = np.random.default_rng(SEED)

x = rng.uniform(-1, 1, n)
eps = rng.normal(0, 0.5, n)
y = 2 + 3 * x + eps

# 設計矩陣 X = [1, x]，形狀 (n, 2)
X = np.column_stack([np.ones(n), x])


# 目標函數 J(a, b) = 1/(2n) * sum((a + b x - y)^2)
def cost(a, b):
    r = a + b * x - y
    return np.mean(r**2) / 2


# 方法 1：內建最小平方法
def fit_lstsq():
    beta = np.linalg.lstsq(X, y, rcond=None)[0]
    return beta


# 方法 2：正規方程  X^T X beta = X^T y
def fit_normal():
    XtX = X.T @ X
    Xty = X.T @ y
    beta = np.linalg.solve(XtX, Xty)
    return beta


# 方法 3：批次梯度下降
# dJ/da = mean(a + b x - y)
# dJ/db = mean((a + b x - y) * x)
def fit_gd(lr=0.1, tol=1e-6, max_iter=10000):
    a = 0.0
    b = 0.0
    n_update = 0
    converged = False
    for k in range(max_iter):
        r = a + b * x - y
        ga = np.mean(r)
        gb = np.mean(r * x)
        if np.sqrt(ga**2 + gb**2) < tol:      # 梯度夠小就停止
            converged = True
            break
        a = a - lr * ga                        # a、b 用同一個梯度同時更新
        b = b - lr * gb
        n_update = n_update + 1
    return np.array([a, b]), n_update, converged


# ===== 2. 比較擬合結果 =====
beta_ls = fit_lstsq()
beta_ne = fit_normal()
beta_gd, n_update, converged = fit_gd()

print("seed =", SEED, " n =", n)
print("%-10s %12s %12s %14s %12s %12s" % ("method", "a", "b", "J", "a - a_ls", "b - b_ls"))
names = ["lstsq", "normal", "GD"]
betas = [beta_ls, beta_ne, beta_gd]
for i in range(3):
    a, b = betas[i]
    print("%-10s %12.8f %12.8f %14.10f %12.3e %12.3e"
          % (names[i], a, b, cost(a, b), a - beta_ls[0], b - beta_ls[1]))
print("GD 更新次數 =", n_update, "  是否滿足停止條件 =", converged)

# 畫圖：取 100 筆資料 + 三條擬合直線
idx = rng.choice(n, 100, replace=False)
xg = np.linspace(-1, 1, 200)          # 遞增的 x 網格

plt.figure(figsize=(7, 5))
plt.scatter(x[idx], y[idx], s=15, color="gray", label="100 observations")
plt.plot(xg, beta_ls[0] + beta_ls[1] * xg, "b-", lw=4, label="lstsq")
plt.plot(xg, beta_ne[0] + beta_ne[1] * xg, "y--", lw=2.5, label="normal equations")
plt.plot(xg, beta_gd[0] + beta_gd[1] * xg, "r:", lw=2, label="gradient descent")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.tight_layout()
plt.savefig("q3_fit.png", dpi=150)

# ===== 3. 比較計算時間 =====
n_run = 7


def time_it(func):
    func()                              # 暖身一次（不計時）
    times = []
    for k in range(n_run):
        t0 = time.perf_counter()
        func()                          # fit_gd 每次呼叫都會重新把 a, b 設為 0
        t1 = time.perf_counter()
        times.append(t1 - t0)
    return np.median(times)


t_ls = time_it(fit_lstsq)
t_ne = time_it(fit_normal)
t_gd = time_it(fit_gd)

print("執行時間中位數（%d 次）：" % n_run)
print("  lstsq  : %.4f s" % t_ls)
print("  normal : %.4f s" % t_ne)
print("  GD     : %.4f s" % t_gd)
