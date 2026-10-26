# Fermi_Dirac_Distribution_Temperature.png

**對應章節：** 9.4 量子統計學（費米能量）
**插入位置：**「有限溫度」與費米溫度的討論之後、「物理意義：教室的入座規則」之前
**課本對應：** 圖 9.6

> 產圖前請先貼上 `00_STYLE_GUIDE.md` 的風格區塊。

---

## 中文提示詞

```
【模型與符號】上排專門比較固定 μ=μ₀>0 的分布形狀，並非同一固定 N 樣品升溫；T=0 階躍兩端畫空心點，不強制指定單點佔據。下排 ε_F、T_F 使用 0 K 定義；固定 N 時 μ 隨 T 改變。

請畫一張教學用資訊圖表，主題是「費米－迪拉克分布：絕對零度是步階函數，溫度只磨圓邊緣」。

標題列文字：9.4  費米－迪拉克分布與費米能量 (Fermi–Dirac Distribution and the Fermi Energy)

導言框文字：
化學勢 μ(T)=−αkT，f=1/[e^((ε−μ(T))/kT)+1]；ε_F≡μ(0)。
T = 0 時它是步階函數：ε_F 以下全滿、以上全空。溫度升高只把 ε_F 附近幾個 kT 磨圓。
金屬的 ε_F/k 高達 10⁴–10⁵ K，所以室溫對電子而言幾乎就是絕對零度。

主體分成上下兩區。

【上區｜pill 標籤：三種溫度下的 f(ε)（圖 9.6）】
三張並排、同尺寸的平面圖，橫軸皆為 ε（只標出 μ₀ 的位置，μ₀ 在橫軸中間），
縱軸 f(ε) 刻度 0、0.5、1.0。所有曲線用紅色（#C62828）粗實線。
  (a) T = 0：完美的步階——ε < μ₀ 時 f = 1 的水平線，在 μ₀ 處垂直掉到 0，之後為 0。
  (b) T = 0.1 μ₀/k：仍接近步階，但在 μ₀ 附近變成平滑的 S 形下降；
      在 ε = 0.8 μ₀ 處 f ≈ 0.88，在 ε = 1.2 μ₀ 處 f ≈ 0.12。
  (c) T = μ₀/k：幾乎是一條緩降的斜線，ε = 0 時 f ≈ 0.73，ε = 2μ₀ 時 f ≈ 0.27。
只在 (b)、(c) 用黑色實心小圓點標出 (μ₀, 0.5)，並加小字「固定 μ₀ 的有限溫曲線通過 f(μ₀)=½；T=0 用開端點表示階躍」。
在 (b) 圖的 S 形下降段，用一個小雙箭頭標出寬度「約 6 kT（f 從 0.95 降到 0.05）」。

【下區左｜pill 標籤：教室比喻：一定要往前坐、而且一位一人】
畫一間俯視教室，每排 10 個座位，共 8 排；講台在下方標「低能量」。
前五排座位全部塗紅（有電子），第六排以後全部空白。
第五排右側用紅色粗橫線標「ε_F」，旁註：
  「50 個人進來 → 填滿到第五排 → 第五排就是費米能量」
  「100 個人進來 → 填到第十排 → 電子愈多，ε_F 愈高」
再在第五、第六排交界畫兩三個「溢到上一排的小人」（虛線外框），
標「T > 0：只有 ε_F 附近的電子能跳到上面的空位」。

【下區右｜pill 標籤：溫度的尺度】
一條水平對數溫度軸，刻度 1 K、10 K、100 K、1000 K、10⁴ K、10⁵ K。
在 300 K 處標一個綠色小三角「室溫」；
在 8.2 × 10⁴ K 處標一個紅色小三角「銅的費米溫度 T_F = ε_F/k」；
兩個三角之間用括號標「T/T_F ≈ 0.004 → 幾乎就是 T = 0」。

右上角「圖例」方框：
  紅色實線 — f_FD(ε)：費米－迪拉克分布
  黑色圓點 — (μ₀, ½)：固定化學勢的有限溫曲線中點
  紅色塗滿座位 — 被電子佔據的態
  空白座位 — 空的態

最下方一排粉彩公式盒（四個）：
1. 淺紅盒：μ(T) = −α k T，說明「(9.28) 化學勢由粒子數條件決定，ε_F=μ(0)」
2. 淺紫盒：f_FD = 1 / [e^((ε−μ(T))/kT) + 1]，說明「(9.29)」
3. 淺藍盒：T → 0：ε < ε_F 時 f = 1；ε > ε_F 時 f = 0，說明「步階函數」
4. 淺黃盒：N 型與 P 型半導體的 ε_F 位置不同，說明「第十章 PN 接面的起點」
```

## English Prompt

```
MODEL AND NOTATION: The upper plots compare fixed μ=μ₀>0, not heating one fixed-N sample. At T=0 draw open step endpoints without assigning a unique occupation at the discontinuity. Lower ε_F,T_F labels use zero-temperature definitions; μ changes with T at fixed N.

Draw an educational infographic titled "The Fermi–Dirac distribution: a step
function at T = 0, only rounded off by temperature". ALL labels in TRADITIONAL CHINESE.

Title bar: 9.4  費米－迪拉克分布與費米能量 (Fermi–Dirac Distribution and the Fermi Energy)

Intro box (Traditional Chinese):
化學勢 μ(T)=−αkT，f=1/[e^((ε−μ(T))/kT)+1]；ε_F≡μ(0)。
T = 0 時它是步階函數：ε_F 以下全滿、以上全空。溫度升高只把 ε_F 附近幾個 kT 磨圓。
金屬的 ε_F/k 高達 10⁴–10⁵ K，所以室溫對電子而言幾乎就是絕對零度。

Two bands.

TOP band, pill label 三種溫度下的 f(ε)（圖 9.6）:
Three side-by-side plots of equal size. x-axis ε in each (only μ₀ marked, at the middle
of the axis); y-axis f(ε) with ticks 0, 0.5, 1.0. All curves thick solid red (#C62828).
  (a) T = 0: a perfect step — horizontal line f = 1 for ε < μ₀, dropping vertically to 0 at μ₀.
  (b) T = 0.1 μ₀/k: still close to a step but a smooth S-shaped drop around μ₀;
      f ≈ 0.88 at ε = 0.8 μ₀ and f ≈ 0.12 at ε = 1.2 μ₀.
  (c) T = μ₀/k: almost a gently sloping straight line, f ≈ 0.73 at ε = 0 and f ≈ 0.27 at ε = 2μ₀.
In panels (b) and (c) only, mark the point (μ₀, 0.5) with a small filled black dot and add the
caption 固定 μ₀ 的有限溫曲線通過 f(μ₀)=½；T=0 用開端點表示階躍.
On the S-shaped drop of (b), a small double arrow marking the width
約 6 kT（f 從 0.95 降到 0.05）.

BOTTOM-LEFT, pill label 教室比喻：一定要往前坐、而且一位一人:
A classroom seen from above, 8 rows of 10 seats; podium at the bottom labelled 低能量.
The first five rows fully filled in red (electrons), rows six and up empty.
A thick red horizontal line to the right of row five labelled ε_F, with notes:
  50 個人進來 → 填滿到第五排 → 第五排就是費米能量
  100 個人進來 → 填到第十排 → 電子愈多，ε_F 愈高
At the boundary of rows five and six, draw two or three figures with dashed outlines
that have hopped up a row, labelled T > 0：只有 ε_F 附近的電子能跳到上面的空位.

BOTTOM-RIGHT, pill label 溫度的尺度:
A horizontal logarithmic temperature axis with ticks 1 K, 10 K, 100 K, 1000 K, 10⁴ K, 10⁵ K.
A small green triangle at 300 K labelled 室溫; a small red triangle at 8.2 × 10⁴ K labelled
銅的費米溫度 T_F = ε_F/k; a bracket between them labelled T/T_F ≈ 0.004 → 幾乎就是 T = 0.

Top-right legend "圖例":
  紅色實線 — f_FD(ε)：費米－迪拉克分布
  黑色圓點 — (μ₀, ½)：固定化學勢的有限溫曲線中點
  紅色塗滿座位 — 被電子佔據的態
  空白座位 — 空的態

Bottom pastel boxes (four):
1. light red: μ(T) = −α k T — (9.28) 化學勢由粒子數條件決定，ε_F=μ(0)
2. light purple: f_FD = 1 / [e^((ε−μ(T))/kT) + 1] — (9.29)
3. light blue: T → 0：ε < ε_F 時 f = 1；ε > ε_F 時 f = 0 — 步階函數
4. light yellow: N 型與 P 型半導體的 ε_F 位置不同 — 第十章 PN 接面的起點
```
