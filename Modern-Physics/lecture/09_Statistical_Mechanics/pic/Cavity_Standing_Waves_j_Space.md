# Cavity_Standing_Waves_j_Space.png

**對應章節：** 9.5 瑞利－金斯公式
**插入位置：** $(9.33)$ $g(j)\,dj = \pi j^2\,dj$ 之後、「推導：換成頻率」之前
**課本對應：** 圖 9.7

> 產圖前請先貼上 `00_STYLE_GUIDE.md` 的風格區塊。

---

## 中文提示詞

```
請畫一張教學用資訊圖表，主題是「空腔中的駐波怎麼數：j 空間的八分之一球殼」。

標題列文字：9.5  空腔駐波與 j 空間 (Standing Waves in a Cavity and j-Space)

導言框文字：
黑體空腔中的電磁波必須在腔壁形成節點，三個方向各容納整數個半波長。
把每一組整數 (j_x, j_y, j_z) 當成 j 空間中的一個格點，格點是均勻分布的，
只要算球殼體積，再乘上 1/8（只有正整數）與 2（兩個偏振），就數完了。

主體分成左、中、右三欄，以深藍箭頭由左向右串接。

左欄｜pill 標籤：立方空腔中的駐波
畫一個邊長 L 的立方體空腔（線框），旁邊放一張正面的二維截面圖（正方形，邊長 L）：
截面內用藍色等值線畫出一個二維駐波圖樣——沿 x 方向 3 個半波長、沿 y 方向 2 個半波長，
腔壁四邊全部是節點（波幅為零）。標註：
  「j_x = 3：x 方向 3 個半波長」
  「j_y = 2：y 方向 2 個半波長」
  「j_x = 2L/λ_x，j_y = 2L/λ_y，j_z = 2L/λ_z　(9.30)」

中欄｜pill 標籤：j 空間的格點（圖 9.7）
一張二維示意圖代表 j 空間的一個截面：橫軸 j_x、縱軸 j_y，刻度 0、5、10。
第一象限內畫規則排列的灰色小圓點（每單位一點，均勻格點），
只有第一象限有點，其他象限留白並淡淡標「j < 0 無意義」。
以原點為圓心畫兩條相鄰的四分之一圓弧，半徑分別為 j 與 j + dj（約 10），
兩弧之間塗淡藍色，並用小箭頭標 dj；從原點畫一支灰色向量 j 指到內弧。
下方用小字說明：「三維時這是一個球殼的八分之一（第一卦限）」。
旁邊三行橘色註記：
  「× 1/8：j_x、j_y、j_z 都必須 ≥ 0」
  「× 2：每個格點有兩個獨立偏振方向」
  「g(j) dj = 2 × (1/8) × 4πj² dj = πj² dj　(9.33)」

右欄｜pill 標籤：換成頻率 → 瑞利－金斯
由上而下四個淺藍圓角框，深藍箭頭相連：
  框 1：j = 2Lν/c，dj = (2L/c) dν
  框 2：g(ν) dν = (8πL³/c³) ν² dν　(9.34)
  框 3：G(ν) dν = 8πν²/c³ dν（除以 L³，與腔體大小無關）　(9.35)
  框 4：u(ν) dν = kT · G(ν) dν = 8πν²kT/c³ dν　(9.36)
框 4 旁邊用橘色虛線框強調「kT 來自古典能量均分——問題就出在這裡」。

右上角「圖例」方框：
  灰色圓點 — 一個允許的駐波（一組 j_x, j_y, j_z）
  淡藍弧帶 — j 到 j + dj 的球殼（截面）
  藍色等值線 — 腔內駐波的電場圖樣
  橘色虛線框 — 古典假設

最下方一排粉彩公式盒（三個）：
1. 淺綠盒：j_x² + j_y² + j_z² = (2L/λ)²，說明「(9.31) 三維駐波條件」
2. 淺藍盒：G(ν) = 8πν²/c³，說明「(9.35) 每單位體積的駐波密度，普朗克沿用不變」
3. 淺紅盒：∫ u(ν) dν → ∞，說明「u ∝ ν²：紫外災變」
```

## English Prompt

```
Draw an educational infographic titled "How to count standing waves in a cavity:
one eighth of a spherical shell in j-space". ALL labels in TRADITIONAL CHINESE.

Title bar: 9.5  空腔駐波與 j 空間 (Standing Waves in a Cavity and j-Space)

Intro box (Traditional Chinese):
黑體空腔中的電磁波必須在腔壁形成節點，三個方向各容納整數個半波長。
把每一組整數 (j_x, j_y, j_z) 當成 j 空間中的一個格點，格點是均勻分布的，
只要算球殼體積，再乘上 1/8（只有正整數）與 2（兩個偏振），就數完了。

Three columns linked left-to-right by dark-blue arrows.

LEFT column, pill label 立方空腔中的駐波:
A wireframe cube of side L, and next to it a frontal 2D cross-section (a square of side L).
Inside the square draw a 2D standing-wave pattern with blue contour lines — 3 half-wavelengths
along x and 2 along y — with nodes (zero amplitude) on all four walls. Labels:
  j_x = 3：x 方向 3 個半波長
  j_y = 2：y 方向 2 個半波長
  j_x = 2L/λ_x，j_y = 2L/λ_y，j_z = 2L/λ_z　(9.30)

MIDDLE column, pill label j 空間的格點（圖 9.7）:
A 2D sketch standing for a slice of j-space: x-axis j_x, y-axis j_y, ticks 0, 5, 10.
Regular grey dots fill ONLY the first quadrant (one dot per unit cell, uniform lattice);
other quadrants left empty with a faint note j < 0 無意義.
Two neighbouring quarter-circle arcs centred at the origin with radii j and j + dj (about 10);
shade the band between them light blue and mark dj with a small arrow; a grey vector j
from the origin to the inner arc. Small caption below: 三維時這是一個球殼的八分之一（第一卦限）.
Three orange notes alongside:
  × 1/8：j_x、j_y、j_z 都必須 ≥ 0
  × 2：每個格點有兩個獨立偏振方向
  g(j) dj = 2 × (1/8) × 4πj² dj = πj² dj　(9.33)

RIGHT column, pill label 換成頻率 → 瑞利－金斯:
Four light-blue rounded boxes stacked top to bottom, joined by dark-blue arrows:
  Box 1: j = 2Lν/c，dj = (2L/c) dν
  Box 2: g(ν) dν = (8πL³/c³) ν² dν　(9.34)
  Box 3: G(ν) dν = 8πν²/c³ dν（除以 L³，與腔體大小無關）　(9.35)
  Box 4: u(ν) dν = kT · G(ν) dν = 8πν²kT/c³ dν　(9.36)
Next to box 4, an orange dashed frame stressing kT 來自古典能量均分——問題就出在這裡.

Top-right legend "圖例":
  灰色圓點 — 一個允許的駐波（一組 j_x, j_y, j_z）
  淡藍弧帶 — j 到 j + dj 的球殼（截面）
  藍色等值線 — 腔內駐波的電場圖樣
  橘色虛線框 — 古典假設

Bottom pastel boxes (three):
1. light green: j_x² + j_y² + j_z² = (2L/λ)² — (9.31) 三維駐波條件
2. light blue: G(ν) = 8πν²/c³ — (9.35) 每單位體積的駐波密度，普朗克沿用不變
3. light red: ∫ u(ν) dν → ∞ — u ∝ ν²：紫外災變
```
