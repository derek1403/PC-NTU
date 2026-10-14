# Objective Analysis 上機小考 T2（模擬題）

**範圍：** Week 04（頻率學派 vs 貝氏、t 分布、OLS）、Week 05（bootstrap、AR(1) 誤差、AR 模型）

**時間：** 20 分鐘（Q1 約 5 分鐘、Q2 約 7 分鐘、Q3 約 8 分鐘；Q4 為加分題）

**規定：**

* 使用 Python（`numpy`、`scipy.stats`、`matplotlib`）。每題寫一支程式，例如 `q1.py`、`q2.py`。
* 亂數一律使用 `rng = np.random.default_rng(0)`，並**依照題目寫的順序**抽亂數，這樣結果才能和解答對照。
* 數值取到小數點後 4 位。文字題用 1～2 句回答即可。

---

## Q1. p 值與後驗機率（5 分鐘）

某研究觀測到效果 $\hat d = 1.0$，標準誤 $\sigma = 0.5$。假設 $\hat d \mid d \sim \mathcal N(d,\ \sigma^2)$。

* (a) 在 $H_0: d = 0$ 下，計算觀測到 $\hat d \ge 1.0$ 的機率（單尾 p 值）。請用 `scipy.stats.norm` 計算，並寫出它等於 $\Phi(\ ?\ )$。
* (b) 使用平坦先驗，寫出 $d$ 的後驗分布，並計算 $\Pr(d > 0 \mid \hat d = 1.0)$。
* (c) 改用先驗 $d \sim \mathcal N(-0.5,\ 0.5^2)$，計算後驗平均、後驗標準差與 $\Pr(d > 0 \mid \hat d = 1.0)$。(a) 的 p 值會改變嗎？為什麼？

---

## Q2. 迴歸斜率的 Bootstrap 信賴區間（7 分鐘）

依序產生 $n = 50$ 筆資料：

```python
rng = np.random.default_rng(0)
x = rng.uniform(-1, 1, n)
eps = rng.normal(0, 1, n)
y = 1 + 0.5 * x + eps
```

* (a) 以 OLS 估計截距 $\hat a$、斜率 $\hat b$ 與 $\mathrm{SE}_{\mathrm{OLS}}(\hat b)$，並計算傳統 95% 信賴區間 $\hat b \pm t_{0.975,\,n-2}\,\mathrm{SE}_{\mathrm{OLS}}(\hat b)$。
* (b) 接著（用同一個 `rng`）進行 $B = 1000$ 次 pairs bootstrap：每次用 `idx = rng.integers(0, n, n)` 抽索引，重新擬合並保存斜率。畫出 bootstrap 斜率的直方圖，並計算 95% 百分位數信賴區間。
* (c) 比較兩個區間。在 5% 水準下能否拒絕 $H_0: b = 0$？
* (d) 這個 bootstrap 斜率分布可以直接當成 $H_0: b = 0$ 的虛無分布嗎？為什麼？

---

## Q3. AR(1) 誤差下的 t 檢定（8 分鐘）

令 $n = 100$，`x = np.linspace(-1, 1, n)`。誤差為 AR(1)：

$$\epsilon_1 \sim \mathcal N(0, 1), \qquad \epsilon_t = \phi\,\epsilon_{t-1} + u_t, \quad u_t \sim \mathcal N(0,\ 1 - \phi^2)$$

產生一組誤差時，請依序抽 `eps[0] = rng.normal(0, 1)`，再一次抽出 `u = rng.normal(0, np.sqrt(1 - phi**2), n)`，然後用迴圈算 `eps[t] = phi * eps[t-1] + u[t]`（$t = 1, \dots, n-1$）。

* (a) 對 $\phi = 0$ 與 $\phi = 0.8$（先做 $\phi = 0$，同一個 `rng` 接著做 $\phi = 0.8$），各在 $H_0$ 下產生 $M = 1000$ 組資料 $y = 1 + \epsilon$（真實斜率為 0），每組都做 OLS 與傳統 t 檢定 $|T| = |\hat b / \mathrm{SE}_{\mathrm{OLS}}| > t_{0.975,\,n-2}$。
* (b) 回報每個 $\phi$ 的：
  * 誤拒絕率（$|T|$ 超過臨界值的比例）
  * $M$ 個 $\hat b$ 的標準差，以及 $\mathrm{SE}_{\mathrm{OLS}}$ 的平均，並算出兩者的比值
* (c) 用 1～2 句話解釋 $\phi = 0.8$ 時結果為什麼會這樣。

---

## Q4.（加分題）用 AR(2) 表示正弦波

令 $z_t = \sin(2\pi t / 12)$，$t = 1, \dots, 120$（無雜訊）。

* (a) 用 $t = 3, \dots, 100$ 當反應變數，以 OLS 擬合 $z_t = c + \phi_1 z_{t-1} + \phi_2 z_{t-2}$，回報係數，並和理論值比較（理論值要寫出推導依據）。
* (b) 從 $t = 100$ 開始遞迴預報 20 步，計算 $t = 101, \dots, 120$ 的 RMSE。

---

解答在 [solution/solution.md](solution/solution.md)，**寫完再看**。
