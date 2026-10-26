# Free_Electron_Density_of_States.png

**對應章節：** 9.9 金屬中的自由電子
**插入位置：** $(9.55)$ 電子態數及其說明之後、「推導：費米能量」之前
**課本對應：** 表 9.2（另含自製的態密度示意）

> 產圖前請先貼上 `00_STYLE_GUIDE.md` 的風格區塊。

---

## 中文提示詞

```
【模型與符號】三維非交互作用自由電子模型，g(ε) 已包含兩種自旋；增加 N 的比較固定 V。ε_F 是 0 K 費米能，g 的單位為每能量。

請畫一張教學用資訊圖表，主題是「金屬中的自由電子：態密度 ∝ √ε，電子填到 ε_F 為止」。

標題列文字：9.9  金屬中的自由電子 (Free Electrons in a Metal)

導言框文字：
把金屬當成一個箱子，價電子的物質波在箱中形成駐波；沿用 j 空間的數法，
只是係數 2 從「兩個偏振」變成「兩個自旋」，就得到態密度 g(ε) ∝ √ε。
T ≈ 0 時電子從最低能量一路填到 ε_F；ε_F 只由電子密度 N/V 決定。

主體分成左、中、右三欄。

左欄｜pill 標籤：箱子裡的電子駐波
畫一個邊長 L 的立方體（淡灰色金屬塊），內部畫幾條紅色（#C62828）的駐波曲線，
兩端都在箱壁上成為節點。旁邊一個小原子示意：銅原子的內層電子畫成灰色、
最外層一顆 4s 電子畫成紅色並有箭頭指向金屬內部，標「只有價電子是自由電子」。
三行換算鏈（深藍箭頭相連）：
  j = 2L/λ　→　λ = h/p（德布羅依）　→　p = √(2mε)
  j = 2L√(2mε)/h，dj = (L/h)√(2m/ε) dε
  g(j) dj = πj² dj（因子 2 = 自旋 ±½）

中欄｜pill 標籤：態密度與費米能量（T = 0）
一張平面圖，橫軸能量 ε、縱軸 g(ε)。
畫一條紅色實線 g(ε) ∝ √ε——形狀是「橫躺的拋物線」（起點斜率無限大、之後逐漸變平）。
從 ε = 0 到 ε = ε_F 的曲線下面積塗上淡紅色，標「已填滿的態：面積 = N」；
ε_F 處畫一條紅色垂直粗線並標 ε_F；ε_F 以上的曲線下方留白，標「空的態」。
再畫第二條稍高的垂直虛線 ε_F′，在 ε_F 到 ε_F′ 之間塗淡紫色，
標「電子更多（N 變大）→ 只能往上填 → ε_F 升高」。
旁邊加教室比喻小圖：三排座位，第一排 1 個單位寬、第二排 √2 倍寬、第三排 √3 倍寬，
標「能量愈高，那一排的座位愈多」。

右欄（上下兩張卡）：

卡 1｜pill 標籤：表 9.2 一些金屬的費米能量
一張水平長條圖，九種金屬由上到下：Li 4.72、Na 3.12、Al 11.8、K 2.14、Cs 1.53、
Cu 7.04、Zn 11.0、Ag 5.51、Au 5.54（單位 eV，長條末端標數值）。
長條顏色依價電子數區分：1 個價電子用藍色、2 個（Zn）用紫色、3 個（Al）用橘色。
下方小字：「ε_F 由電子密度決定 = 原子密度 × 價電子數；Al、Zn 因價電子多而特別高」。

卡 2｜pill 標籤：例題 9.8 銅
條列：
  N/V = 8.48 × 10²⁸ 電子/m³（每個原子一個 4s 電子）
  ε_F = (h²/2m)(3N/8πV)^(2/3) ≈ 7.04 eV
  最高速率 √(2ε_F/m) ≈ 1.6 × 10⁶ m/s
  T_F = ε_F/k ≈ 8.2 × 10⁴ K
紅色結論框：「古典平均動能 (3/2)kT 不能外推描述 0 K 量子氣體；自由電子模型下銅在 0 K 填到約 7 eV——
  這是包立不相容原理撐出來的簡併電子氣」。

右上角「圖例」方框：
  紅色實線 — 態密度 g(ε) ∝ √ε
  淡紅色填色 — T = 0 時被電子佔滿的態
  淡紫色填色 — 增加電子後新填入的態
  長條顏色 — 藍：1 價、紫：2 價、橘：3 價

最下方一排粉彩公式盒（三個）：
1. 淺紅盒：g(ε) dε = (8√2 π V m^(3/2) / h³) √ε dε，說明「(9.55) 電子態的數目」
2. 淺藍盒：N = ∫₀^(ε_F) g(ε) dε，說明「步階函數讓積分上限從 ∞ 縮成 ε_F」
3. 淺黃盒：ε_F = (h²/2m)(3N/8πV)^(2/3)，說明「(9.56) 只依賴電子密度 N/V」
```

## English Prompt

```
MODEL AND NOTATION: 3D noninteracting free-electron model; g includes both spins. Hold V fixed when increasing N. ε_F denotes the zero-temperature Fermi energy; g has inverse-energy units.

Draw an educational infographic titled "Free electrons in a metal: density of states
∝ √ε, filled up to ε_F". ALL labels in TRADITIONAL CHINESE.

Title bar: 9.9  金屬中的自由電子 (Free Electrons in a Metal)

Intro box (Traditional Chinese):
把金屬當成一個箱子，價電子的物質波在箱中形成駐波；沿用 j 空間的數法，
只是係數 2 從「兩個偏振」變成「兩個自旋」，就得到態密度 g(ε) ∝ √ε。
T ≈ 0 時電子從最低能量一路填到 ε_F；ε_F 只由電子密度 N/V 決定。

Three columns.

LEFT column, pill label 箱子裡的電子駐波:
A cube of side L (a light-grey metal block) with a few red (#C62828) standing-wave curves
inside, each with nodes on the walls. Beside it a small atom sketch: copper's inner-shell
electrons in grey and the single outermost 4s electron in red with an arrow pointing into
the metal, labelled 只有價電子是自由電子.
A three-line conversion chain joined by dark-blue arrows:
  j = 2L/λ → λ = h/p（德布羅依）→ p = √(2mε)
  j = 2L√(2mε)/h，dj = (L/h)√(2m/ε) dε
  g(j) dj = πj² dj（因子 2 = 自旋 ±½）

MIDDLE column, pill label 態密度與費米能量（T = 0）:
A 2D plot, x-axis energy ε, y-axis g(ε).
A red solid curve g(ε) ∝ √ε — shaped like a sideways parabola (infinite initial slope,
flattening afterwards). Shade the area under the curve from ε = 0 to ε = ε_F light red,
labelled 已填滿的態：面積 = N; a thick red vertical line at ε_F labelled ε_F; leave the area
above ε_F unshaded, labelled 空的態.
A second, slightly higher vertical dashed line ε_F′, with the band between ε_F and ε_F′ shaded
light purple, labelled 電子更多（N 變大）→ 只能往上填 → ε_F 升高.
A small classroom-analogy sketch alongside: three rows of seats with widths 1, √2, √3,
labelled 能量愈高，那一排的座位愈多.

RIGHT column, two stacked cards:

Card 1, pill label 表 9.2 一些金屬的費米能量:
A horizontal bar chart of nine metals, top to bottom: Li 4.72, Na 3.12, Al 11.8, K 2.14,
Cs 1.53, Cu 7.04, Zn 11.0, Ag 5.51, Au 5.54 (eV, value printed at each bar end).
Bar colours by valence: one valence electron blue, two (Zn) purple, three (Al) orange.
Small caption: ε_F 由電子密度決定 = 原子密度 × 價電子數；Al、Zn 因價電子多而特別高.

Card 2, pill label 例題 9.8 銅:
Bullets:
  N/V = 8.48 × 10²⁸ 電子/m³（每個原子一個 4s 電子）
  ε_F = (h²/2m)(3N/8πV)^(2/3) ≈ 7.04 eV
  最高速率 √(2ε_F/m) ≈ 1.6 × 10⁶ m/s
  T_F = ε_F/k ≈ 8.2 × 10⁴ K
A red conclusion box: 古典平均動能 (3/2)kT 不能外推描述 0 K 量子氣體；自由電子模型下銅在 0 K 填到約 7 eV——
這是包立不相容原理撐出來的簡併電子氣.

Top-right legend "圖例":
  紅色實線 — 態密度 g(ε) ∝ √ε
  淡紅色填色 — T = 0 時被電子佔滿的態
  淡紫色填色 — 增加電子後新填入的態
  長條顏色 — 藍：1 價、紫：2 價、橘：3 價

Bottom pastel boxes (three):
1. light red: g(ε) dε = (8√2 π V m^(3/2) / h³) √ε dε — (9.55) 電子態的數目
2. light blue: N = ∫₀^(ε_F) g(ε) dε — 步階函數讓積分上限從 ∞ 縮成 ε_F
3. light yellow: ε_F = (h²/2m)(3N/8πV)^(2/3) — (9.56) 只依賴電子密度 N/V
```
