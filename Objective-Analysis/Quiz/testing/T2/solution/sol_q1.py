# T2 小考 Q1 解答：頻率學派 vs 貝氏學派
from scipy import stats
import numpy as np

d_hat = 1.0      # 觀測到的效果
sd = 0.5         # 標準誤

# (a) 頻率學派：H0: d = 0 下，觀測到 >= 1.0 的機率（單尾 p 值）
z = (d_hat - 0) / sd
p_one = 1 - stats.norm.cdf(z)          # = Phi(-z)
p_two = 2 * p_one
print("z = %.2f, 單尾 p = %.4f, 雙尾 p = %.4f" % (z, p_one, p_two))

# (b) 貝氏、平坦先驗：後驗 d | data ~ N(1.0, 0.5^2)
post_flat = 1 - stats.norm.cdf((0 - d_hat) / sd)     # P(d > 0 | data)
print("平坦先驗: P(d > 0 | data) = %.4f" % post_flat)

# (c) 資訊性先驗 d ~ N(-0.5, 0.5^2)：套用卡爾曼增益公式
mu0 = -0.5
sd0 = 0.5
K = sd0**2 / (sd0**2 + sd**2)
mu_post = mu0 + K * (d_hat - mu0)
sd_post = np.sqrt((1 - K) * sd0**2)
post_inf = 1 - stats.norm.cdf((0 - mu_post) / sd_post)
print("資訊性先驗: K = %.3f, mu_post = %.4f, sd_post = %.4f, P(d > 0 | data) = %.4f"
      % (K, mu_post, sd_post, post_inf))
print("p 值不變 = %.4f" % p_one)
