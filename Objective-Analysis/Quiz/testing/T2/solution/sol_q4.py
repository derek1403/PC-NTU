# T2 小考 Q4（加分題）解答：用 AR(2) 擬合週期 12 的正弦波
import numpy as np

t = np.arange(1, 121)                    # t = 1..120
z = np.sin(2 * np.pi * t / 12)

# 訓練：反應變數 t = 3..100（索引 2..99）
y = z[2:100]
lag1 = z[1:99]
lag2 = z[0:98]
X = np.column_stack([np.ones(len(y)), lag1, lag2])
beta = np.linalg.lstsq(X, y, rcond=None)[0]
print("c = %.4f, phi1 = %.4f, phi2 = %.4f" % (beta[0], beta[1], beta[2]))
print("理論值: phi1 = 2cos(2pi/12) = %.4f, phi2 = -1" % (2 * np.cos(2 * np.pi / 12)))

# 從 t = 100 開始遞迴預報 20 步
h = list(z[:100])
for s in range(20):
    h.append(beta[0] + beta[1] * h[-1] + beta[2] * h[-2])
fc = np.array(h[100:])
rmse = np.sqrt(np.mean((fc - z[100:120]) ** 2))
print("20 步預報 RMSE = %.2e" % rmse)
