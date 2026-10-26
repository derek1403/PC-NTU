# PN_Junction_Bias_Band_Diagrams.png

**對應章節：** 10.7 半導體元件
**插入位置：**「無偏壓、逆向偏壓與順向偏壓」三段說明之後、「這就是電子學中最常見的二極體 I–V 曲線」之前
**課本對應：** 圖 10.30、圖 10.31

> 產圖前請先貼上 `00_STYLE_GUIDE.md` 的風格區塊。

---

## 中文提示詞

```
【模型與符號】平衡圖只用一條水平 E_F；偏壓圖改以電子、電洞準費米能級 E_Fn、E_Fp 標示兩側，不能畫成全域單一平衡 E_F。理想二極體式限低注入、定溫，忽略耗盡區復合、串聯電阻與崩潰。

請畫一張教學用資訊圖表，主題是「p-n 接面：空乏區、費米能量對齊，以及偏壓如何升降障壁」。

標題列文字：10.7  p-n 接面二極體 (The p-n Junction Diode)

導言框文字：
電子與電洞擴散後留下帶電的離子，建立起阻止擴散的內建電場；
平衡時兩側費米能量一樣高，接面形成一道障壁。
逆向偏壓把障壁拉高，順向偏壓把障壁壓低——這就是二極體的單行道。

主體上排左｜pill 標籤：接面的形成
畫一個橫向長方塊，左半標「p 區」（散布空心小圓 ○ 電洞），右半標「n 區」（散布黑色實心小點 ● 電子）。
中間一段無載子的窄帶標「空乏區」：其左側（p 側）畫幾個帶圈的「−」（受子離子），
右側（n 側）畫幾個帶圈的「+」（施子離子）。
一支橘色（#EF6C00）箭頭由 n 側指向 p 側，標「內建電場：阻止繼續擴散」。
上方一個小對照：「氮氣／氧氣會混合到均勻；電子與電洞帶電，所以不會」。

主體上排右｜pill 標籤：費米能量就像水位
畫兩個水桶，右桶水位高（標「n 型 E_F 高」）、左桶水位低（標「p 型 E_F 低」），
接通水管後兩桶水位相等，標「平衡時兩側 E_F 一樣高」。

主體中排｜pill 標籤：三種偏壓下的能帶圖
畫三個並排的能帶圖，縱軸標「電子能量」，每圖都包含：
上方傳導帶邊緣（深灰線）、下方價電帶（灰藍實心），左側 p 區、右側 n 區，
接面處能帶呈階梯式下降（p 側高、n 側低），以及紅色虛線 E_F。
  (a) 無偏壓：E_F 為一條貫穿兩側的水平紅色虛線。障壁高度標「eV₀」。
      在傳導帶處畫兩支箭頭：
        藍色（#1565C0）箭頭 i_t：p 側傳導帶的一顆電子沿斜坡滑到 n 側；
        橘色（#EF6C00）箭頭 i_r：n 側一顆高能電子爬過障壁到 p 側。
      兩支箭頭等粗，標「i_t = i_r，淨電流 0」。
  (b) 逆向偏壓（p 接負、n 接正）：p 側能帶被抬高，障壁變高，標「e(V₀ + |V|)」；
      E_Fp 高於 E_Fn，兩者相差 e|V|。橘色 i_r 箭頭變得很細，藍色 i_t 不變，
      標「很小的逆向電流，幾乎與電壓無關」。
  (c) 順向偏壓（p 接正、n 接負）：障壁變低，標「e(V₀ − V)」；
      E_Fn 高於 E_Fp。橘色 i_r 箭頭變得非常粗，標「大量電子越過障壁」；
      旁註「電子由 n 往 p；傳統電流由 p 往 n」。
  每圖下方畫對應的外接電池符號與 + − 號。

主體下排｜pill 標籤：I–V 曲線
畫一張座標圖，橫軸 V（左逆向、右順向），縱軸 I：
  順向區曲線指數上升；逆向區曲線貼近一條很小的負值水平線，標「−I₀（熱產生電流）」。
  曲線旁寫：I = I₀(e^(eV/k_BT) − 1)。
  在順向區標一個小三角：「每增加約 60 mV，電流 ×10」。

右側一個紅框警語卡：
  「能帶圖畫的是電子能量：哪裡帶正電，電子能量就低；哪裡帶負電，電子能量就高。」

右上角「圖例」方框：
  藍色箭頭 — 熱產生電流 i_t
  橘色箭頭 — 復合電流 i_r
  紅色虛線 — 平衡 E_F／偏壓下準費米能級 E_Fn、E_Fp
  ● 電子　○ 電洞　⊕ 施子離子　⊖ 受子離子

最下方一排粉彩公式盒（四個）：
1. 淺藍盒：i_t 與偏壓無關，說明「少數載子『下坡』滑過接面」
2. 淺紅盒：i_r = i_t e^(eV/k_BT)，說明「翻越障壁的電子數由波茲曼因子決定」
3. 淺綠盒：I = I₀(e^(eV/k_BT) − 1)，說明「理想二極體方程式」
4. 淺黃盒：k_BT ln10 / e ≈ 60 mV，說明「室溫下每 60 mV 電流放大十倍」
```

## English Prompt

```
MODEL AND NOTATION: Use one flat E_F only at equilibrium; biased diagrams use electron/hole quasi-Fermi levels E_Fn and E_Fp on the respective sides, not one global equilibrium E_F. Ideal diode law assumes low injection and fixed T, neglecting depletion recombination, series resistance and breakdown.

Draw an educational infographic titled "The p-n junction: depletion region,
Fermi-level alignment, and how bias raises or lowers the barrier".
ALL labels in TRADITIONAL CHINESE.

Title bar: 10.7  p-n 接面二極體 (The p-n Junction Diode)

Intro box (Traditional Chinese):
電子與電洞擴散後留下帶電的離子，建立起阻止擴散的內建電場；
平衡時兩側費米能量一樣高，接面形成一道障壁。
逆向偏壓把障壁拉高，順向偏壓把障壁壓低——這就是二極體的單行道。

TOP-LEFT, pill label 接面的形成:
A horizontal slab: left half labelled p 區 with scattered open circles ○ (holes),
right half labelled n 區 with scattered solid dots ● (electrons). A narrow
carrier-free strip in the middle labelled 空乏區: on its p side a few circled "−"
(acceptor ions), on its n side a few circled "+" (donor ions). An orange
(#EF6C00) arrow from the n side to the p side labelled 內建電場：阻止繼續擴散.
Small comparison above: 氮氣／氧氣會混合到均勻；電子與電洞帶電，所以不會.

TOP-RIGHT, pill label 費米能量就像水位:
Two buckets: the right one with a high water level (n 型 E_F 高), the left one low
(p 型 E_F 低); after a pipe connects them the levels are equal, labelled
平衡時兩側 E_F 一樣高.

MIDDLE row, pill label 三種偏壓下的能帶圖:
Three side-by-side band diagrams, y-axis 電子能量, each containing a conduction-
band edge (dark-grey line) on top, a solid grey-blue valence band below, p region
on the left, n region on the right, bands stepping DOWN from p side (high) to
n side (low) at the junction, and a red dashed E_F.
  (a) 無偏壓: E_F is one straight horizontal red dashed line through both sides;
      barrier height labelled eV₀. In the conduction band draw two arrows:
        blue (#1565C0) i_t: an electron in the p-side conduction band sliding down
        the slope to the n side;
        orange (#EF6C00) i_r: an energetic n-side electron climbing over the barrier
        to the p side.
      Equal thickness, labelled i_t = i_r，淨電流 0.
  (b) 逆向偏壓 (p negative, n positive): p-side bands raised, barrier higher,
      labelled e(V₀ + |V|); E_Fp above E_Fn by e|V|. The orange i_r arrow becomes
      very thin, the blue i_t unchanged; label 很小的逆向電流，幾乎與電壓無關.
  (c) 順向偏壓 (p positive, n negative): barrier lower, labelled e(V₀ − V);
      E_Fn above E_Fp. The orange i_r arrow becomes very thick, labelled
      大量電子越過障壁; side note 電子由 n 往 p；傳統電流由 p 往 n.
  Under each diagram show the battery symbol with + and − on the correct sides.

BOTTOM row, pill label I–V 曲線:
A plot, x-axis V (reverse on the left, forward on the right), y-axis I:
  exponential rise in forward bias; in reverse bias the curve hugs a small negative
  constant labelled −I₀（熱產生電流）. Next to the curve: I = I₀(e^(eV/k_BT) − 1).
  A small marker in the forward region: 每增加約 60 mV，電流 ×10.

RIGHT side, a red-bordered warning card:
  能帶圖畫的是電子能量：哪裡帶正電，電子能量就低；哪裡帶負電，電子能量就高。

Top-right legend "圖例":
  藍色箭頭 — 熱產生電流 i_t
  橘色箭頭 — 復合電流 i_r
  紅色虛線 — 平衡 E_F／偏壓下準費米能級 E_Fn、E_Fp
  ● 電子　○ 電洞　⊕ 施子離子　⊖ 受子離子

Bottom pastel boxes (four):
1. light blue: i_t 與偏壓無關 — 少數載子『下坡』滑過接面
2. light red: i_r = i_t e^(eV/k_BT) — 翻越障壁的電子數由波茲曼因子決定
3. light green: I = I₀(e^(eV/k_BT) − 1) — 理想二極體方程式
4. light yellow: k_BT ln10 / e ≈ 60 mV — 室溫下每 60 mV 電流放大十倍
```
