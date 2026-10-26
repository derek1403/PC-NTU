# Van_der_Waals_Dipole_Interactions.png

**對應章節：** 10.4 凡德瓦鍵
**插入位置：**「三種凡德瓦吸引」列表之後、「假設與已知」之前
**課本對應：** 圖 10.11、圖 10.12、圖 10.13、圖 10.14、圖 10.15

> 產圖前請先貼上 `00_STYLE_GUIDE.md` 的風格區塊。

---

## 中文提示詞

```
【模型與符號】α>0 為各向同性線性極化率，p_ind=αE；誘導能須含建立偶極的功，U=−αE²/2。忽略重疊與遲滯。曲線縱軸用歸一化能量大小 |U(r)|/|U(r₀)|，不是力；水分子標部分電荷 δ±。

請畫一張教學用資訊圖表，主題是「凡德瓦鍵：弱，但到處都有」。

標題列文字：10.4  凡德瓦鍵 (Van der Waals Bond)

導言框文字：
凡德瓦力的本質仍是庫侖力，只是作用的對象是電偶極。
偶極電場 ∝ 1/r³，感應偶極又正比於電場，於是交互作用能 ∝ 1/r⁶、力 ∝ 1/r⁷——
距離稍微拉開，它就急遽消失。

主體上排｜pill 標籤：三種偶極吸引
畫三格並排，偶極一律畫成一根圓角小棒，一端標「+」（紅色 #C62828 半邊）、
另一端標「−」（藍色 #1565C0 半邊）：
  (1) 極性–極性：左邊一個水分子（大球 O δ− 加兩個小球 H δ+），箭頭指向它的
      簡化版小棒；右邊幾根小棒排成三角形、長鏈、並排（正對負）。
      標「極性分子（如水）彼此相接」。
  (2) 極性–可極化：一根極性小棒靠近一個圓形分子，圓內的 + 與 − 被拉開到兩側，
      標「感應偶極 p′ = αE」。
  (3) 非極性–非極性：上方兩個電荷對稱分布的圓（標「平均而言對稱」），
      下方三組成對的圓，各自的 + − 分布瞬間不對稱且同步，中間有吸引箭頭，
      標「瞬間漲落偶極互相感應」。
  三格下方共同一條說明：「固定取向永久偶極 U∝r⁻³；誘導與非遲滯色散作用 U∝−r⁻⁶、F_r∝−r⁻⁷」。

主體中排左｜pill 標籤：衰減得有多快？
畫一張座標圖，橫軸 r/r₀（1 到 3），縱軸「|U(r)|/|U(r₀)|」（0 到 1）：
  綠色曲線（#2E7D32）1/r：離子–離子
  橘色曲線（#EF6C00）1/r³：固定偶極–偶極
  紫色曲線（#7B1FA2）1/r⁶：偶極–感應偶極（凡德瓦）
  三條在 r/r₀ = 1 處都等於 1；在 r/r₀ = 2 處分別標出 1/2、1/8、1/64。

主體中排右｜pill 標籤：凡德瓦固體的位能谷（Lennard-Jones）
畫一條 Lennard-Jones 位能曲線 U(r) = 4ε[(σ/r)¹² − (σ/r)⁶]：
  標出 U = 0 的位置 r = σ、谷底位置 r₀ = 2^(1/6) σ ≈ 1.12σ、谷底深度 −ε。
  小字：「氬：ε ≈ 0.010 eV，比 NaCl 的 7.96 eV 小近千倍」。

主體下排｜pill 標籤：氫鍵與冰的開放結構
  左：一個水分子的四面體示意——中央 O，兩支伸出的 H δ+，另外兩個淡灰色
    淚滴狀區域標「高電子機率區（未鍵結的電子對）」，四個方向各有一個鄰近水分子
    以虛線氫鍵相連，標「每個水分子可形成四個氫鍵」。
  右：兩個並排小圖——
    「冰」：水分子排成開放的六角形網格，中間留有明顯空隙；
    「液態水」：分子較無秩序但排得較緊密。
    下方比較：「冰的密度 < 水 → 冰浮在水上」。
    小字：「矽、鍺、鎵、鉍也是凝固時體積變大的少數例外」。

右上角「圖例」方框：
  紅／藍半邊小棒 — 電偶極（+ / −）
  綠色曲線 — ∝ 1/r
  橘色曲線 — ∝ 1/r³
  紫色曲線 — ∝ 1/r⁶
  虛線 — 氫鍵

最下方一排粉彩公式盒（四個）：
1. 淺藍盒：E = (1/4πε₀)[3(p·r)r/r⁵ − p/r³]　(10.6)，說明「偶極電場 ∝ 1/r³」
2. 淺綠盒：p′ = αE　(10.7)，說明「感應偶極正比於電場（α 為極化率）」
3. 淺紫盒：U = −α(1 + 3cos²θ)p²/[2(4πε₀)² r⁶]　(10.8)，說明「線性誘導模型：U<0，徑向吸引」
4. 淺紅盒：F ∝ −1/r⁷，說明「典型分子晶體：較軟、熔點較低」
```

## English Prompt

```
MODEL AND NOTATION: α>0 is isotropic linear polarizability; p_ind=αE. Including the work of induction gives U=−αE²/2. Neglect overlap and retardation. Plot normalized energy magnitudes |U(r)|/|U(r₀)|, not forces. Water carries partial δ± charges.

Draw an educational infographic titled "The van der Waals bond: weak but everywhere".
ALL labels in TRADITIONAL CHINESE.

Title bar: 10.4  凡德瓦鍵 (Van der Waals Bond)

Intro box (Traditional Chinese):
凡德瓦力的本質仍是庫侖力，只是作用的對象是電偶極。
偶極電場 ∝ 1/r³，感應偶極又正比於電場，於是交互作用能 ∝ 1/r⁶、力 ∝ 1/r⁷——
距離稍微拉開，它就急遽消失。

TOP row, pill label 三種偶極吸引:
Three panels. Draw every dipole as a small rounded rod, one half red (#C62828)
marked "+", the other half blue (#1565C0) marked "−":
  (1) polar–polar: on the left a water molecule (large O δ− ball with two small H δ+
      balls) with an arrow pointing to its simplified rod; on the right several
      rods arranged as a triangle, a chain and side by side (+ facing −).
      Label 極性分子（如水）彼此相接.
  (2) polar–polarizable: a polar rod near a round molecule whose + and − charges
      are pulled to opposite sides, labelled 感應偶極 p′ = αE.
  (3) nonpolar–nonpolar: top, two round molecules with symmetric charge, labelled
      平均而言對稱; below, three pairs of circles whose instantaneous + / −
      distributions are lopsided and in step, with attraction arrows between them,
      labelled 瞬間漲落偶極互相感應.
  Common caption under the three panels: 固定取向永久偶極 U∝r⁻³；誘導與非遲滯色散作用 U∝−r⁻⁶、F_r∝−r⁻⁷.

MIDDLE-LEFT, pill label 衰減得有多快？:
A plot, x-axis r/r₀ from 1 to 3, y-axis |U(r)|/|U(r₀)| from 0 to 1:
  green (#2E7D32) 1/r: 離子–離子
  orange (#EF6C00) 1/r³: 固定偶極–偶極
  purple (#7B1FA2) 1/r⁶: 偶極–感應偶極（凡德瓦）
  All three equal 1 at r/r₀ = 1; at r/r₀ = 2 mark their values 1/2, 1/8, 1/64.

MIDDLE-RIGHT, pill label 凡德瓦固體的位能谷（Lennard-Jones）:
A Lennard-Jones curve U(r) = 4ε[(σ/r)¹² − (σ/r)⁶]:
  mark the zero crossing r = σ, the minimum at r₀ = 2^(1/6) σ ≈ 1.12σ and the
  depth −ε. Small text: 氬：ε ≈ 0.010 eV，比 NaCl 的 7.96 eV 小近千倍.

BOTTOM row, pill label 氫鍵與冰的開放結構:
  Left: a tetrahedral water sketch — O at the centre, two protruding H δ+, and two
    pale-grey teardrop lobes labelled 高電子機率區（未鍵結的電子對）; a neighbouring
    water molecule in each of the four directions joined by dashed hydrogen bonds,
    labelled 每個水分子可形成四個氫鍵.
  Right: two small side-by-side pictures —
    冰: molecules in an open hexagonal network with clearly visible empty space;
    液態水: molecules less ordered but packed more closely.
    Comparison below: 冰的密度 < 水 → 冰浮在水上.
    Small note: 矽、鍺、鎵、鉍也是凝固時體積變大的少數例外.

Top-right legend "圖例":
  紅／藍半邊小棒 — 電偶極（+ / −）
  綠色曲線 — ∝ 1/r
  橘色曲線 — ∝ 1/r³
  紫色曲線 — ∝ 1/r⁶
  虛線 — 氫鍵

Bottom pastel boxes (four):
1. light blue: E = (1/4πε₀)[3(p·r)r/r⁵ − p/r³]  (10.6) — 偶極電場 ∝ 1/r³
2. light green: p′ = αE  (10.7) — 感應偶極正比於電場（α 為極化率）
3. light purple: U = −α(1 + 3cos²θ)p²/[2(4πε₀)² r⁶]  (10.8) — 線性誘導模型：U<0，徑向吸引
4. light red: F ∝ −1/r⁷ — 典型分子晶體：較軟、熔點較低
```
