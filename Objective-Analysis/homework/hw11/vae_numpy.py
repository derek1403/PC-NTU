# vae_numpy.py：純 numpy 的小型 VAE（單一 tanh 隱藏層的 encoder / decoder）
# 本機沒有 PyTorch，所以反向傳播手寫，並以 grad_check() 用有限差分驗證。
#
# 目標函數（與題目相同）：
#   L = 1/(2 σx² B) Σ_n ||x_n − x̂_n||²  +  1/(2B) Σ_n Σ_j (μ² + σ² − ln σ² − 1)
#   z = μ + σ ⊙ ε,  ε ~ N(0, I)        （reparameterization trick）
import numpy as np


class VAE:
    def __init__(self, n_in, n_hid, n_lat, sigma_x2, seed=0, dtype=np.float64):
        rng = np.random.default_rng(seed)
        self.rng = rng
        self.s2x = float(sigma_x2)
        self.dt = dtype

        def glorot(a, b):
            return (rng.standard_normal((a, b)) * np.sqrt(2.0 / (a + b))).astype(dtype)

        z = lambda *s: np.zeros(s, dtype)
        self.p = {
            "W1": glorot(n_in, n_hid), "b1": z(n_hid),          # encoder 隱藏層
            "Wm": glorot(n_hid, n_lat), "bm": z(n_lat),         # μ_φ
            "Wv": glorot(n_hid, n_lat), "bv": z(n_lat) - 2.0,   # ln σ_φ²（起始 σ² ≈ e⁻²）
            "W2": glorot(n_lat, n_hid), "b2": z(n_hid),         # decoder 隱藏層
            "W3": glorot(n_hid, n_in), "b3": z(n_in),           # x̂
        }
        self.m = {k: np.zeros_like(v) for k, v in self.p.items()}
        self.v = {k: np.zeros_like(v) for k, v in self.p.items()}
        self.t = 0

    # ── 前向 ────────────────────────────────────────────────────────────────
    def encode(self, x):
        p = self.p
        h = np.tanh(x @ p["W1"] + p["b1"])
        return h, h @ p["Wm"] + p["bm"], h @ p["Wv"] + p["bv"]

    def decode(self, z):
        p = self.p
        g = np.tanh(z @ p["W2"] + p["b2"])
        return g, g @ p["W3"] + p["b3"]

    def loss_grad(self, x, eps):
        """回傳 (L, L_rec, D_KL, grads)；eps 為外部給定的 N(0,1) 樣本。"""
        p, B = self.p, x.shape[0]
        h, mu, lv = self.encode(x)
        s = np.exp(0.5 * lv)
        z = mu + s * eps
        g, xh = self.decode(z)
        r = x - xh
        Lrec = np.sum(r * r) / (2 * self.s2x * B)
        KL = np.sum(mu**2 + s**2 - lv - 1) / (2 * B)

        G = {}
        dxh = -r / (self.s2x * B)
        G["W3"] = g.T @ dxh; G["b3"] = dxh.sum(0)
        dp2 = (dxh @ p["W3"].T) * (1 - g * g)
        G["W2"] = z.T @ dp2; G["b2"] = dp2.sum(0)
        dz = dp2 @ p["W2"].T
        dmu = dz + mu / B
        dlv = dz * eps * 0.5 * s + (s**2 - 1) / (2 * B)
        G["Wm"] = h.T @ dmu; G["bm"] = dmu.sum(0)
        G["Wv"] = h.T @ dlv; G["bv"] = dlv.sum(0)
        dp1 = (dmu @ p["Wm"].T + dlv @ p["Wv"].T) * (1 - h * h)
        G["W1"] = x.T @ dp1; G["b1"] = dp1.sum(0)
        return Lrec + KL, Lrec, KL, G

    # ── Adam ────────────────────────────────────────────────────────────────
    def adam_step(self, G, lr, b1=0.9, b2=0.999, e=1e-8):
        self.t += 1
        for k in self.p:
            self.m[k] = b1 * self.m[k] + (1 - b1) * G[k]
            self.v[k] = b2 * self.v[k] + (1 - b2) * G[k] ** 2
            mh = self.m[k] / (1 - b1**self.t)
            vh = self.v[k] / (1 - b2**self.t)
            self.p[k] -= (lr * mh / (np.sqrt(vh) + e)).astype(self.dt)

    def fit(self, X, epochs, lr, batch=None, log_every=0):
        M = X.shape[0]
        batch = batch or M
        hist = []
        for ep in range(epochs):
            idx = self.rng.permutation(M) if batch < M else np.arange(M)
            tot = np.zeros(3)
            for i0 in range(0, M, batch):
                xb = X[idx[i0:i0 + batch]]
                eps = self.rng.standard_normal((xb.shape[0], self.p["Wm"].shape[1])).astype(self.dt)
                L, Lr, KL, G = self.loss_grad(xb, eps)
                self.adam_step(G, lr)
                tot += np.array([L, Lr, KL]) * xb.shape[0]
            hist.append(tot / M)
            if log_every and (ep + 1) % log_every == 0:
                print(f"  epoch {ep+1:5d}: L = {hist[-1][0]:.4f}  (rec {hist[-1][1]:.4f}, KL {hist[-1][2]:.4f})",
                      flush=True)
        return np.array(hist)

    def reconstruct(self, X, batch=512):
        """確定性重建 x̂ = g_θ(μ_φ(x))。"""
        out = np.empty_like(X)
        for i0 in range(0, X.shape[0], batch):
            out[i0:i0 + batch] = self.decode(self.encode(X[i0:i0 + batch])[1])[1]
        return out


def grad_check(seed=1):
    """以中央差分驗證手寫梯度。"""
    rng = np.random.default_rng(seed)
    net = VAE(3, 5, 2, 0.7, seed=seed)
    x = rng.standard_normal((6, 3)); eps = rng.standard_normal((6, 2))
    _, _, _, G = net.loss_grad(x, eps)
    worst = 0.0
    for k, P in net.p.items():
        num = np.zeros_like(P)
        for i in np.ndindex(P.shape):
            old = P[i]
            P[i] = old + 1e-6; Lp = net.loss_grad(x, eps)[0]
            P[i] = old - 1e-6; Lm = net.loss_grad(x, eps)[0]
            P[i] = old
            num[i] = (Lp - Lm) / 2e-6
        worst = max(worst, np.max(np.abs(num - G[k])) / (np.max(np.abs(num)) + 1e-12))
    return worst


if __name__ == "__main__":
    print("max relative gradient error =", grad_check())
