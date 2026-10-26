# p_Orbitals_Linear_Combination.png

**對應章節：** 8.5 複雜分子
**插入位置：**「推導：$p_x$、$p_y$ 軌域從何而來」末尾（$\left( \vec{a}\cdot\vec{r} \right)$ 性質之後）、「為什麼化學鍵用 $p_x$、$p_y$」段落之前
**課本對應：** 圖 8.9 ＋ 式 (8.2)

> 產圖前請先貼上 `00_STYLE_GUIDE.md` 的風格區塊。

---

## 中文提示詞

```
請畫一張教學用資訊圖表，主題是「化學的 p_x、p_y 軌域其實是 m_l = ±1 的線性組合」。

標題列文字：8.5  p 軌域的線性組合 (p Orbitals as Linear Combinations)

導言框文字：
m_l = ±1 的波函數 ψ_±1 繞著 z 軸成甜甜圈狀，不偏向 x 也不偏向 y。
因為 ψ_+1、ψ_−1、ψ_0 能量相同（簡併），它們的任何線性組合仍是同能量的解；
取和與差，就得到沿 x、y 軸的啞鈴 p_x、p_y——與 p_z 形狀完全相同。

主體分成左、中、右三區，以兩支深藍色粗箭頭由左向右連接。

左區｜pill 標籤：薛丁格方程式直接給的解
  上：ψ_+1 的機率分佈 |ψ_+1|² ∝ sin²θ —— 一個繞 z 軸的甜甜圈（環面），
      畫出 x、y、z 三軸，z 軸穿過甜甜圈中心，標「與 φ 無關」。
  下：ψ_−1 —— 同樣形狀的甜甜圈，標「|ψ_−1|² 與 |ψ_+1|² 相同」。
  旁註小字：m_l = ±1 的態有確定的 L_z = ±ħ，但在空間中不指向任何特定方向。

中間箭頭上方文字：線性組合 (8.2)
  ψ_px = (1/√2)(ψ_+1 + ψ_−1)
  ψ_py = (1/√2)(ψ_+1 − ψ_−1)

中區｜pill 標籤：代入後得到的形狀
  三個一樣大小的啞鈴，各自配上公式：
    p_x：沿 x 軸的啞鈴，公式 ψ_px = [1/(4√(2π) a₀^(3/2))] (x/a₀) e^(−r/2a₀)
    p_y：沿 y 軸的啞鈴，公式 ψ_py = i · [1/(4√(2π) a₀^(3/2))] (y/a₀) e^(−r/2a₀)
    p_z：沿 z 軸的啞鈴，公式 ψ_pz = ψ_0 = [1/(4√(2π) a₀^(3/2))] (z/a₀) e^(−r/2a₀)
  每個啞鈴兩瓣分別標 + 與 −（正瓣用橘色 #EF6C00，負瓣用藍色 #1565C0）。
  下方一行深藍粗體：三者是同一個函數，只是 x、y、z 互換。

右區｜pill 標籤：圖 8.9 邊界曲面總覽
  四個小圖排成一排：s（球形，單一正號）、p_x、p_y、p_z（啞鈴，標 + −），
  各自畫在小座標軸上；說明「每個軌道最多容納兩個電子；灰暗區是找到電子機率高的區域」。

右上角「圖例」方框：
  橘色 — 波函數為正的瓣
  藍色 — 波函數為負的瓣
  甜甜圈 — |ψ_±1|²（對 z 軸旋轉對稱）

最下方一排粉彩公式盒（三個）：
1. 淺藍盒：Ĥ(c₁ψ₁ + c₂ψ₂) = E(c₁ψ₁ + c₂ψ₂)，說明「簡併本徵函數的組合仍是同能量的本徵函數」
2. 淺綠盒：e^(iφ) + e^(−iφ) = 2cosφ，r sinθ cosφ = x，說明「代入後 sinθ cosφ 變成 x/r」
3. 淺紫盒：a_x p_x + a_y p_y + a_z p_z ∝ (a·r) e^(−r/2a₀)，說明「p 軌域的組合 = 指向 a 方向的 p 軌域，混成軌域的基礎」
```

## English Prompt

```
Draw an educational infographic titled "Chemistry's p_x and p_y orbitals are linear
combinations of m_l = ±1". ALL labels in TRADITIONAL CHINESE.

Title bar: 8.5  p 軌域的線性組合 (p Orbitals as Linear Combinations)

Intro box (Traditional Chinese):
m_l = ±1 的波函數 ψ_±1 繞著 z 軸成甜甜圈狀，不偏向 x 也不偏向 y。
因為 ψ_+1、ψ_−1、ψ_0 能量相同（簡併），它們的任何線性組合仍是同能量的解；
取和與差，就得到沿 x、y 軸的啞鈴 p_x、p_y——與 p_z 形狀完全相同。

Three regions left / centre / right joined by two thick dark-blue arrows.

LEFT, pill label 薛丁格方程式直接給的解:
  top: the probability density of ψ_+1, |ψ_+1|² ∝ sin²θ — a torus (doughnut) around the
       z-axis, with x, y, z axes drawn and the z-axis through the hole; note 與 φ 無關.
  bottom: ψ_−1 — the same torus, note |ψ_−1|² 與 |ψ_+1|² 相同.
  small note: m_l = ±1 的態有確定的 L_z = ±ħ，但在空間中不指向任何特定方向。

Text above the first arrow: 線性組合 (8.2)
  ψ_px = (1/√2)(ψ_+1 + ψ_−1)
  ψ_py = (1/√2)(ψ_+1 − ψ_−1)

CENTRE, pill label 代入後得到的形狀:
  Three identical-size dumbbells, each with its formula:
    p_x: dumbbell along x, ψ_px = [1/(4√(2π) a₀^(3/2))] (x/a₀) e^(−r/2a₀)
    p_y: dumbbell along y, ψ_py = i · [1/(4√(2π) a₀^(3/2))] (y/a₀) e^(−r/2a₀)
    p_z: dumbbell along z, ψ_pz = ψ_0 = [1/(4√(2π) a₀^(3/2))] (z/a₀) e^(−r/2a₀)
  Each dumbbell's two lobes marked + and − (positive lobe orange #EF6C00, negative lobe
  blue #1565C0).
  One dark-blue bold line underneath: 三者是同一個函數，只是 x、y、z 互換。

RIGHT, pill label 圖 8.9 邊界曲面總覽:
  Four small figures in a row: s (sphere, single + sign), p_x, p_y, p_z (dumbbells
  with + −), each on small axes; caption 每個軌道最多容納兩個電子；灰暗區是找到電子機率高的區域.

Top-right legend "圖例":
  橘色 — 波函數為正的瓣
  藍色 — 波函數為負的瓣
  甜甜圈 — |ψ_±1|²（對 z 軸旋轉對稱）

Bottom pastel boxes (three):
1. light blue: Ĥ(c₁ψ₁ + c₂ψ₂) = E(c₁ψ₁ + c₂ψ₂) — 簡併本徵函數的組合仍是同能量的本徵函數
2. light green: e^(iφ) + e^(−iφ) = 2cosφ，r sinθ cosφ = x — 代入後 sinθ cosφ 變成 x/r
3. light purple: a_x p_x + a_y p_y + a_z p_z ∝ (a·r) e^(−r/2a₀) — p 軌域的組合 = 指向 a 方向的 p 軌域，混成軌域的基礎
```
