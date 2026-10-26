# Electron_Energy_Distribution_in_Metal.png

**對應章節：** 9.10 電子能量分布
**插入位置：** $(9.58)$ 之後、「讀圖」段落之前
**課本對應：** 投影片 9.10 節的 $n(\epsilon)$ 圖（0 K、300 K、1200 K）

> 產圖前請先貼上 `00_STYLE_GUIDE.md` 的風格區塊。

---

## 中文提示詞

```
【模型與符號】三維非交互作用自由電子、固定 N 與 V；ε_F=μ(0)。有限溫度由 N=∫g(ε)f(ε,μ,T)dε 決定 μ(T)，低溫可用 μ≈ε_F[1−π²(kT/ε_F)²/12]。n(ε)、g(ε) 單位為每能量；電子比熱公式限 kT≪ε_F。

請畫一張教學用資訊圖表，主題是「金屬中自由電子的能量分布：只有費米能量附近的電子是活的」。

標題列文字：9.10  電子能量分布 (Electron-Energy Distribution)

導言框文字：
n(ε) = g(ε) f(ε)：√ε 的態密度乘上費米－迪拉克分布。0 K 時拋物線長到 ε_F 就被砍斷；
室溫甚至 1200 K 也只在 ε_F 附近幾個 kT 內被磨圓。
被不相容原理擋住的深層電子無法吸收熱能，所以電子幾乎不貢獻比熱。

主體分成左右兩區。

左區（約 60% 寬）｜pill 標籤：0 K、300 K、1200 K 的 n(ε)
一張平面圖，橫軸 ε（只標 0 與 ε_F），縱軸 n(ε)（不標數值），淡灰色格線。
  紅色（#C62828）粗實線：從原點以 √ε 形狀上升，到 ε_F 時垂直掉到 0——這是 0 K。
  在同一張圖上，另畫兩條深淺不同的紅色細實線（300 K 較深、1200 K 較淺），
    它們和 0 K 曲線**幾乎完全重疊**，只在 ε_F 左邊一點點開始微微下彎、
    並在 ε_F 右邊拖出一小段很短的尾巴；固定 N 時依 μ(T) 計算，不強制三條線交於同一點。
  從 ε_F 處延伸一條灰白色虛線，沿著 √ε 繼續往右上方，標「g(ε)：態還在，只是沒有電子」。
  在 ε_F 附近加一個放大鏡插圖（inset），把 ε_F ± 5kT 的範圍放大：
    清楚看出 1200 K 的磨圓比 300 K 寬，並標「寬度約幾個 kT」、
    「銅：300 K 時 kT/ε_F ≈ 0.004；1200 K 時 ≈ 0.015」。
  在 ε = 0.6 ε_F 處畫一條綠色細虛線，標「0 K 平均能量 ε̄₀ = (3/5) ε_F」。

右區（約 40% 寬）：上下兩張說明卡。

卡 1｜pill 標籤：為什麼電子幾乎不貢獻比熱？
  畫一個直立的能量長條（像一個裝水的直筒），從下到上塗滿紅色代表「費米海」，
  頂端在 ε_F；在頂端下方一條很薄的亮黃色帶（厚度標 ~kT），
  標「只有這一薄層的電子能被熱激發」；
  深處一顆電子畫一支想往上跳的箭頭，箭頭末端打紅色 ✗，標「上面的態早已被佔滿（包立不相容）」。
  條列：
    古典預期：每個電子 (3/2)kT → 金屬 c_V = 4.5R
    實驗：金屬 c_V ≈ 3R
    量子：c_V,e = (π²/2)(kT/ε_F) R ≈ 0.018R（銅，300 K）

卡 2｜pill 標籤：銅的數字
  條列：
    ε_F = 7.04 eV
    ε̄₀ = (3/5) ε_F ≈ 4.22 eV
    等效理想氣體溫度 T = 2ε̄₀/3k ≈ 3.3 × 10⁴ K
  小字：「絕對零度下的電子，平均能量卻相當於三萬多 K 的氣體」。
  最下方一行連到下一章：「第十章：N 型、P 型半導體的 ε_F 位置不同 → PN 接面」。

右上角「圖例」方框：
  紅色粗實線 — 0 K 的 n(ε)
  深紅細實線 — 300 K
  淺紅細實線 — 1200 K
  灰白虛線 — 態密度 g(ε) 的延伸
  綠色虛線 — 0 K 平均能量 (3/5) ε_F

最下方一排粉彩公式盒（四個）：
1. 淺紅盒：n(ε) dε = (3N/2) ε_F^(−3/2) √ε dε / [e^((ε−μ(T))/kT) + 1]，說明「(9.58)」
2. 淺綠盒：E₀ = (3/5) N ε_F，說明「(9.59) 0 K 的總能量」
3. 淺紫盒：ε̄₀ = (3/5) ε_F，說明「(9.60) 0 K 的平均能量」
4. 淺黃盒：c_V,e ∝ T，說明「極低溫時晶格 ∝ T³ 消失得更快，電子比熱反而成為主角」
```

## English Prompt

```
MODEL AND NOTATION: 3D noninteracting free electrons at fixed N,V; ε_F=μ(0). Determine μ(T) from N=∫gf dε, or use μ≈ε_F[1−π²(kT/ε_F)²/12] at low T. n and g have inverse-energy units; the heat-capacity formula assumes kT≪ε_F.

Draw an educational infographic titled "Energy distribution of free electrons in a
metal: only the electrons near the Fermi energy are alive". ALL labels in TRADITIONAL CHINESE.

Title bar: 9.10  電子能量分布 (Electron-Energy Distribution)

Intro box (Traditional Chinese):
n(ε) = g(ε) f(ε)：√ε 的態密度乘上費米－迪拉克分布。0 K 時拋物線長到 ε_F 就被砍斷；
室溫甚至 1200 K 也只在 ε_F 附近幾個 kT 內被磨圓。
被不相容原理擋住的深層電子無法吸收熱能，所以電子幾乎不貢獻比熱。

LEFT ~60%, pill label 0 K、300 K、1200 K 的 n(ε):
A 2D plot, x-axis ε (only 0 and ε_F marked), y-axis n(ε) (no numbers), faint grey grid.
  thick solid red (#C62828): rising from the origin with a √ε shape and dropping vertically
    to 0 at ε_F — this is 0 K.
  On the same axes, two thinner red curves (300 K darker, 1200 K lighter) that coincide
    ALMOST EXACTLY with the 0 K curve, bending down only slightly just left of ε_F and
    showing a very short tail just right of ε_F; use μ(T) at fixed N; do not force a common intersection.
  From ε_F, a light-grey dashed line continuing the √ε shape to the upper right, labelled
    g(ε)：態還在，只是沒有電子.
  A magnifier inset around ε_F covering ε_F ± 5kT: the 1200 K rounding is visibly wider
    than 300 K; labels 寬度約幾個 kT and 銅：300 K 時 kT/ε_F ≈ 0.004；1200 K 時 ≈ 0.015.
  A thin green dashed vertical line at ε = 0.6 ε_F labelled 0 K 平均能量 ε̄₀ = (3/5) ε_F.

RIGHT ~40%: two stacked cards.

Card 1, pill label 為什麼電子幾乎不貢獻比熱？:
  An upright energy column (like a tall cylinder of liquid) filled red from the bottom up to
  ε_F, representing the 費米海; just below the top, a very thin bright-yellow band (thickness
  marked ~kT) labelled 只有這一薄層的電子能被熱激發; an electron deep inside with an arrow
  trying to jump up, ending in a red ✗, labelled 上面的態早已被佔滿（包立不相容）.
  Bullets:
    古典預期：每個電子 (3/2)kT → 金屬 c_V = 4.5R
    實驗：金屬 c_V ≈ 3R
    量子：c_V,e = (π²/2)(kT/ε_F) R ≈ 0.018R（銅，300 K）

Card 2, pill label 銅的數字:
  Bullets:
    ε_F = 7.04 eV
    ε̄₀ = (3/5) ε_F ≈ 4.22 eV
    等效理想氣體溫度 T = 2ε̄₀/3k ≈ 3.3 × 10⁴ K
  Small text: 絕對零度下的電子，平均能量卻相當於三萬多 K 的氣體.
  A final line linking to the next chapter: 第十章：N 型、P 型半導體的 ε_F 位置不同 → PN 接面.

Top-right legend "圖例":
  紅色粗實線 — 0 K 的 n(ε)
  深紅細實線 — 300 K
  淺紅細實線 — 1200 K
  灰白虛線 — 態密度 g(ε) 的延伸
  綠色虛線 — 0 K 平均能量 (3/5) ε_F

Bottom pastel boxes (four):
1. light red: n(ε) dε = (3N/2) ε_F^(−3/2) √ε dε / [e^((ε−μ(T))/kT) + 1] — (9.58)
2. light green: E₀ = (3/5) N ε_F — (9.59) 0 K 的總能量
3. light purple: ε̄₀ = (3/5) ε_F — (9.60) 0 K 的平均能量
4. light yellow: c_V,e ∝ T — 極低溫時晶格 ∝ T³ 消失得更快，電子比熱反而成為主角
```
