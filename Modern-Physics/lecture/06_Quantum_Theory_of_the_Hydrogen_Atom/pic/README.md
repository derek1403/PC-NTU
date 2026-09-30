# 第六章圖片清單 (Chapter 6 Figure Checklist)

本目錄同時存放**圖片提示詞 `.md`** 與**產出的圖片 `.png`**。
notebook 內一律以 `![](./pic/<檔名>.png)` 引用，檔名必須與提示詞 `.md` 完全一致。

**產圖流程：**
1. 打開下表中要產的那一張圖的 `.md`。
2. 先貼 [`00_STYLE_GUIDE.md`](00_STYLE_GUIDE.md) 的風格區塊（中文版或英文版擇一）。
3. 再貼該張圖 `.md` 裡對應語言的提示詞區塊。
4. 產出的圖存成同名 `.png` 放在本目錄。
5. 回來把下表的「狀態」改成 ✅。

---

## 清單

| # | 檔名 | 節 | 在 notebook 中的位置 | 內容一句話 | 狀態 |
|---|---|---|---|---|---|
| 1 | `Spherical_Polar_Coordinates` | 6.1 | 庫侖位能 $(6.2)$ 之後 | 圖 6.1：$r,\theta,\phi$ 的定義、座標轉換式、固定 $\theta$／固定 $\phi$ 的軌跡 | ⬜ 待生成 |
| 2 | `Separation_of_Variables_Roadmap` | 6.2 | 【推導 1】之後 | 本章骨架圖：$(6.1)\to(6.3)\to(6.4)\to(6.5)\to(6.6)\to$ 兩次分離 $\to(6.12)(6.13)(6.14)$ | ⬜ 待生成 |
| 3 | `Three_Eigen_Equations_and_Quantum_Numbers` | 6.3 | 「三維 → 三個量子數」推論之後 | 三欄對照：方程式／本徵形式／邊界條件／量子數／物理意義 | ⬜ 待生成 |
| 4 | `Hydrogen_Energy_Levels` | 6.4 | $E_n = E_1/n^2$ 之後 | $n=1\sim5$ 能階梯、游離連續區、與波耳模型的知識論對比 | ⬜ 待生成 |
| 5 | `Orbital_Angular_Momentum_Quantization` | 6.5 | 「假設與已知」之後 | 動能徑向／切向分解 ＋ 抵消論證三步 $\to L=\sqrt{l(l+1)}\hbar$ | ⬜ 待生成 |
| 6 | `Space_Quantization_of_Angular_Momentum` | 6.6 | $(6.22)$ 之後 | 圖 6.5：$l=2$ 的五個圓錐 ＋ 為何 $\vec{L}$ 不能沿 $z$ 軸（測不準） | ⬜ 待生成 |
| 7 | `Spherical_Volume_Element` | 6.7 | 「假設與已知」之後 | $dV=(dr)(r\,d\theta)(r\sin\theta\,d\phi)$ 三個邊長的幾何來源 ＋ 積分三陷阱 | ⬜ 待生成 |
| 8 | `Radial_Probability_Density` | 6.7 | $(6.25)$ 之後 | $\lvert R\rvert^2$ vs $r^2\lvert R\rvert^2$ 的差別 ＋ 1s/2s/2p/3s/3p/3d 曲線 | ⬜ 待生成 |
| 9 | `Radiative_Transition_Dipole_Oscillation` | 6.8 | 「假設與已知」之後 | 單一定態不振盪 vs 兩態疊加出現 $\cos(2\pi\nu t)$ → 電偶極輻射 | ⬜ 待生成 |
| 10 | `Selection_Rules_Energy_Level_Diagram` | 6.9 | 「假設與已知」之後 | 圖 6.13：$n\times l$ 能階格點，$\Delta l=\pm1$ 允許／禁止的躍遷 | ⬜ 待生成 |
| 11 | `Magnetic_Moment_of_Orbital_Electron` | 6.10 | 「假設與已知」之後 | 圖 6.16：電流迴路 $\mu=IA$ → 軌道電子 $\vec\mu=-(e/2m)\vec L$ | ⬜ 待生成 |
| 12 | `Normal_Zeeman_Effect` | 6.10 | $(6.41)$ 之後 | 圖 6.17：$l=2$（5 條）→ $l=1$（3 條）分裂，最終只剩三條譜線 | ⬜ 待生成 |

---

## 檢查重點（產完圖後請逐張確認）

- [ ] 圖中所有中文皆為**繁體**，沒有簡體字、沒有亂碼、沒有錯字。
- [ ] 數學符號正確：$\theta$ 是天頂角、$\phi$ 是方位角、$\hbar$ 有橫槓、$\varepsilon_0$ 有下標零。
- [ ] 公式排版為印刷品質（分數有橫線、根號罩住整個被開方式）。
- [ ] 同一個物理量在整張圖中維持同一個顏色。
- [ ] 背景為純白，無浮水印、無簽名、無 Logo。
- [ ] 檔名與本表完全一致（大小寫、底線都要對）。

## 需要特別留意的物理正確性

| 圖 | 最容易畫錯的地方 |
|---|---|
| 4 | 能階間距必須反映 $1/n^2$：$n$ 越大越密、越靠近 $E=0$ |
| 6 | 五個向量**長度必須完全相同**，且**沒有任何一個貼齊 $z$ 軸** |
| 7 | $\phi$ 方向的弧長半徑是 $r\sin\theta$，**不是** $r$ |
| 8 | 徑向節點數 $= n-l-1$；2p 峰值在 $4a_0$、3d 峰值在 $9a_0$ |
| 10 | 同一個 $n$ 的不同 $l$ 必須畫在**同一高度**（能量簡併） |
| 12 | $l=2$ 分裂成 5 條、$l=1$ 分裂成 3 條，但譜線只剩 **3** 條 |
