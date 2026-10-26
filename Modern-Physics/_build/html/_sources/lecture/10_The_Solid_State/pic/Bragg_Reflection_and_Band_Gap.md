# Bragg_Reflection_and_Band_Gap.png

**對應章節：** 10.8 能帶：另一種分析
**插入位置：**「假設與已知」之後、「推導：布拉格反射條件」之前
**課本對應：** 課本 10.8 的 $E$–$k$ 圖與布里淵區圖（投影片未收錄，本圖為自製）

> 產圖前請先貼上 `00_STYLE_GUIDE.md` 的風格區塊。

---

## 中文提示詞

```
【模型與符號】一維近自由電子，在區邊界作兩波近似；若沿用 E_g=2U₁，約定 U₁>0。此處 U₁ 為傅立葉係數，非峰谷差。

請畫一張教學用資訊圖表，主題是「從自由電子出發：布拉格反射如何打開能隙」。

標題列文字：10.8  能帶：另一種分析 (Energy Bands: Alternative Analysis)

導言框文字：
電子是物質波，週期排列的離子就像繞射光柵。
當波數恰好 k = ±nπ/a，所有離子反射的波同相疊加，電子無法前進，
形成兩個能量不同的駐波——能隙就在這裡打開。

主體左上｜pill 標籤：布拉格反射 2a = nλ
畫一排水平等間距的離子（藍色 #1565C0 實心圓，標「+」），相鄰間距標「a」。
一列正弦波從左邊入射（向右箭頭，標「e^{ikx}」），
在每個離子處各有一支淡色的小反射波向左（標「e^{−ikx}」）。
用括號標出相鄰兩離子反射波的來回路程差「2a」，旁邊寫「2a = nλ ⇒ k = nπ/a」。
小字：「k 不滿足此條件時，各離子的反射波相位雜亂、互相抵消 → 電子自由前進」。

主體右上｜pill 標籤：k = π/a 的兩個駐波
畫一張橫軸為 x（0 到 3a）的圖，三條曲線上下分開排列、共用橫軸刻度：
  最上：晶格位能 U(x) = −2U₁cos(2πx/a)（灰色曲線），在 x = 0, a, 2a, 3a（離子處）為谷底，
    谷底下方畫藍色離子 +。
  中：|ψ₊|² ∝ cos²(πx/a)（綠色 #2E7D32），峰值正對離子，標「電子堆在離子上 → 能量較低 E₊」。
  下：|ψ₋|² ∝ sin²(πx/a)（紅色 #C62828），峰值在離子之間，標「電子堆在離子之間 → 能量較高 E₋」。
  用垂直細虛線把離子位置貫穿三條曲線，讓對齊關係一目了然。
  右側小框：「動能相同：ħ²π²/(2ma²)；位能 ⟨U⟩₊ = −U₁、⟨U⟩₋ = +U₁ ⇒ E_g = 2U₁」。

主體左下（約 55% 寬）｜pill 標籤：E–k 圖與布里淵區
畫一張座標圖，橫軸 k（標 −2π/a, −π/a, 0, π/a, 2π/a），縱軸 E：
  灰色虛線：自由電子拋物線 E = ħ²k²/2m。
  深藍色實線：晶體中的電子——大部分貼著拋物線，但在 k = ±π/a 與 ±2π/a 處斷開：
    斷口下方的曲線變平、以零斜率接到斷口；斷口上方的曲線從較高處以零斜率重新開始。
  在每個斷口處用大括號標「E_g」，並在縱軸旁用灰藍色長條標出「允許帶」、白色空白標「禁止帶」。
  用淡藍色底色塗出 −π/a < k < π/a，標「第一布里淵區」；
  用淡黃色底色塗出 π/a < |k| < 2π/a，標「第二布里淵區」。
  圖內小字：「每一區對應一條能帶；每條能帶有 N 個 k 值 × 2（自旋）= 2N 個能態」。
  右上角放一個小插圖：二維正方晶格的布里淵區——中央正方形（第一區，淡藍），
  外圍四個三角形（第二區，淡黃）。

主體右下（約 45% 寬）｜pill 標籤：有效質量由曲率決定
畫一條能帶 E(k) = E₀ − 2t cos(ka)，k 從 −π/a 到 π/a：
  在 k = 0 的底部畫一個向上開口的小拋物線輔助線，標「曲率 > 0 ⇒ m* > 0（電子）」；
  在 k = ±π/a 的頂部畫一個向下開口的小拋物線輔助線，標「曲率 < 0 ⇒ m* < 0 ⇒ 等效為電洞（+e, +|m*|）」。
  旁邊公式：m* = ħ² / (d²E/dk²)。
  小字：「能帶越平、m* 越大：Ni 的 d 能帶 m*/m ≈ 28」。

右上角「圖例」方框：
  灰色虛線 — 自由電子 E = ħ²k²/2m
  深藍實線 — 晶體中的能帶
  綠色 — |ψ₊|²（在離子上）
  紅色 — |ψ₋|²（在離子之間）
  淡藍／淡黃底 — 第一／第二布里淵區

最下方一排粉彩公式盒（四個）：
1. 淺藍盒：k = ±nπ/a　(10.17)，說明「布拉格反射條件」
2. 淺綠盒：ψ₊ ∝ cos(πx/a)，ψ₋ ∝ sin(πx/a)　(10.18)，說明「同一個 k，兩個能量」
3. 淺紅盒：E_g = 2U₁　(10.19)，說明「弱位能兩波近似：能隙 2|U₁|；餘弦位能峰谷差 4|U₁|」
4. 淺紫盒：m* = ħ²/(d²E/dk²)　(10.20)，說明「能帶頂端 m* < 0 → 電洞」
```

## English Prompt

```
MODEL AND NOTATION: 1D nearly-free electrons in the two-wave approximation near a zone boundary. E_g=2U₁ assumes U₁>0. U₁ is a Fourier coefficient, not the potential peak-to-peak range.

Draw an educational infographic titled "Starting from free electrons: how Bragg
reflection opens the band gap". ALL labels in TRADITIONAL CHINESE.

Title bar: 10.8  能帶：另一種分析 (Energy Bands: Alternative Analysis)

Intro box (Traditional Chinese):
電子是物質波，週期排列的離子就像繞射光柵。
當波數恰好 k = ±nπ/a，所有離子反射的波同相疊加，電子無法前進，
形成兩個能量不同的駐波——能隙就在這裡打開。

TOP-LEFT, pill label 布拉格反射 2a = nλ:
A horizontal row of equally spaced ions (blue #1565C0 solid circles marked "+"),
spacing labelled a. A sine wave incident from the left (rightward arrow, e^{ikx});
at each ion a faint small reflected wave going left (e^{−ikx}). Bracket the
round-trip path difference between reflections from adjacent ions as 2a, with
2a = nλ ⇒ k = nπ/a. Small text: k 不滿足此條件時，各離子的反射波相位雜亂、
互相抵消 → 電子自由前進.

TOP-RIGHT, pill label k = π/a 的兩個駐波:
A plot with x from 0 to 3a; three vertically stacked curves sharing the x ticks:
  top: lattice potential U(x) = −2U₁cos(2πx/a) (grey), with minima at
    x = 0, a, 2a, 3a (the ions), blue "+" ions drawn under the minima.
  middle: |ψ₊|² ∝ cos²(πx/a) (green #2E7D32), peaks exactly on the ions, labelled
    電子堆在離子上 → 能量較低 E₊.
  bottom: |ψ₋|² ∝ sin²(πx/a) (red #C62828), peaks midway between ions, labelled
    電子堆在離子之間 → 能量較高 E₋.
  Thin vertical dashed lines through the ion positions across all three curves.
  Side box: 動能相同：ħ²π²/(2ma²)；位能 ⟨U⟩₊ = −U₁、⟨U⟩₋ = +U₁ ⇒ E_g = 2U₁.

BOTTOM-LEFT ~55%, pill label E–k 圖與布里淵區:
A plot, x-axis k with ticks −2π/a, −π/a, 0, π/a, 2π/a, y-axis E:
  grey dashed: the free-electron parabola E = ħ²k²/2m.
  dark-blue solid: electrons in the crystal — following the parabola most of the
    way but broken at k = ±π/a and ±2π/a: below each break the curve flattens and
    meets the break with zero slope; above it the curve restarts higher, also with
    zero slope.
  Brace each break as E_g; next to the E-axis mark grey-blue bars 允許帶 and white
    gaps 禁止帶.
  Shade −π/a < k < π/a pale blue labelled 第一布里淵區 and π/a < |k| < 2π/a pale
    yellow labelled 第二布里淵區.
  Small text inside: 每一區對應一條能帶；每條能帶有 N 個 k 值 × 2（自旋）= 2N 個能態.
  Small inset in the corner: the 2-D square-lattice Brillouin zones — a central
  square (first zone, pale blue) surrounded by four triangles (second zone, pale yellow).

BOTTOM-RIGHT ~45%, pill label 有效質量由曲率決定:
A band E(k) = E₀ − 2t cos(ka) for k from −π/a to π/a:
  at the bottom (k = 0) a small upward-opening parabola guide labelled
    曲率 > 0 ⇒ m* > 0（電子）;
  at the top (k = ±π/a) a small downward-opening parabola guide labelled
    曲率 < 0 ⇒ m* < 0 ⇒ 等效為電洞（+e, +|m*|）.
  Formula beside it: m* = ħ² / (d²E/dk²).
  Small text: 能帶越平、m* 越大：Ni 的 d 能帶 m*/m ≈ 28.

Top-right legend "圖例":
  灰色虛線 — 自由電子 E = ħ²k²/2m
  深藍實線 — 晶體中的能帶
  綠色 — |ψ₊|²（在離子上）
  紅色 — |ψ₋|²（在離子之間）
  淡藍／淡黃底 — 第一／第二布里淵區

Bottom pastel boxes (four):
1. light blue: k = ±nπ/a  (10.17) — 布拉格反射條件
2. light green: ψ₊ ∝ cos(πx/a)，ψ₋ ∝ sin(πx/a)  (10.18) — 同一個 k，兩個能量
3. light red: E_g = 2U₁  (10.19) — 弱位能兩波近似：能隙 2|U₁|；餘弦位能峰谷差 4|U₁|
4. light purple: m* = ħ²/(d²E/dk²)  (10.20) — 能帶頂端 m* < 0 → 電洞
```
