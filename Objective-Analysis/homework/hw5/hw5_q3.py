# HW5 Q3：振盪訊號用 AR(1) 還是 AR(2)
# 執行方式：在 hw5 資料夾輸入  py hw5_q3.py
import numpy as np
import matplotlib.pyplot as plt

SEED = 2026
n = 400
n_train = 300
n_fc = 40                       # 預報 40 步
rng = np.random.default_rng(SEED)

t = np.arange(1, n + 1)         # t = 1..400；Python 索引 i 對應 t = i + 1
signal = np.sin(2 * np.pi * t / 20)
noise = rng.normal(0, 1, n)     # 先抽標準常態，再乘上 sigma_v


# 用 OLS 解 y = X beta，回傳係數與訓練 RMSE
def fit(X, y):
    beta = np.linalg.lstsq(X, y, rcond=None)[0]
    resid = y - X @ beta
    rmse = np.sqrt(np.mean(resid**2))
    return beta, rmse


def rmse(a, b):
    return np.sqrt(np.mean((a - b) ** 2))


sigma_list = [0.0, 0.3]
fig, axes = plt.subplots(2, 1, figsize=(10, 8))

for k in range(2):
    sigma_v = sigma_list[k]
    z = signal + sigma_v * noise

    # ===== (b) 擬合：兩個模型都用 t = 3..300 當反應變數（索引 2..299）=====
    y = z[2:300]              # z_t
    lag1 = z[1:299]           # z_{t-1}
    lag2 = z[0:298]           # z_{t-2}
    one = np.ones(len(y))

    X1 = np.column_stack([one, lag1])           # AR(1): c + phi1 z_{t-1}
    X2 = np.column_stack([one, lag1, lag2])     # AR(2): c + phi1 z_{t-1} + phi2 z_{t-2}
    beta1, rmse1 = fit(X1, y)
    beta2, rmse2 = fit(X2, y)

    # ===== (c) 從 t = 300 開始遞迴預報 40 步 =====
    # 先放入訓練資料，之後每預報一步就接在後面，下一步的落後值就會用到預報值
    h1 = list(z[:300])
    h2 = list(z[:300])
    for s in range(n_fc):
        h1.append(beta1[0] + beta1[1] * h1[-1])
        h2.append(beta2[0] + beta2[1] * h2[-1] + beta2[2] * h2[-2])
    fc1 = np.array(h1[300:])
    fc2 = np.array(h2[300:])
    obs = z[300:340]          # t = 301..340

    # AR(2) 特徵根 r^2 - phi1 r - phi2 = 0
    # 複數根才會振盪；模 = 1 表示振幅不衰減，模 < 1 表示衰減
    roots = np.roots([1, -beta2[1], -beta2[2]])

    print("\n===== sigma_v = %.1f =====" % sigma_v)
    print("AR(1): c = %.4f, phi1 = %.4f" % (beta1[0], beta1[1]))
    print("AR(2): c = %.4f, phi1 = %.4f, phi2 = %.4f" % (beta2[0], beta2[1], beta2[2]))
    print("AR(2) 特徵根 =", np.round(roots, 4), " 模 =", np.round(np.abs(roots), 4))
    print("訓練 RMSE : AR(1) = %.4f, AR(2) = %.4f" % (rmse1, rmse2))
    print("預報 RMSE : AR(1) = %.4f, AR(2) = %.4f" % (rmse(fc1, obs), rmse(fc2, obs)))

    ax = axes[k]
    ax.plot(t[280:340], z[280:340], "k.-", label="observations")
    ax.plot(t[300:340], fc1, "b--", lw=2, label="AR(1) forecast")
    ax.plot(t[300:340], fc2, "r-", lw=2, label="AR(2) forecast")
    ax.axvline(300.5, color="gray", ls=":")
    ax.set_title("sigma_v = %.1f" % sigma_v)
    ax.set_xlabel("t")
    ax.set_ylabel("z")
    ax.legend(loc="upper left", fontsize=9)

plt.tight_layout()
plt.savefig("q3_forecast.png", dpi=150)
