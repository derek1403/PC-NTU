# Diode_Variants_LED_Tunnel_Zener.png

**對應章節：** 10.7 半導體元件
**插入位置：**「齊納二極體」一節之後、「接面電晶體」之前
**課本對應：** 圖 10.32、圖 10.33、圖 10.34、圖 10.35

> 產圖前請先貼上 `00_STYLE_GUIDE.md` 的風格區塊。

---

## 中文提示詞

```
請畫一張教學用資訊圖表，主題是「同一個 p-n 接面的三種變化：發光、穿隧、穩壓」。

標題列文字：10.7  LED、穿隧二極體與齊納二極體 (LEDs, Tunnel Diodes and Zener Diodes)

導言框文字：
從普通二極體出發：換對材料，復合的能量變成光（LED、雷射）；
把兩側摻得極濃，電子直接穿隧過窄障壁（穿隧二極體）；
設計好逆向崩潰的電壓，就得到穩壓用的齊納二極體。

主體左欄（約 33% 寬）｜pill 標籤：LED 與半導體雷射
  上：順向偏壓的 p-n 接面能帶圖（遵守風格指南），n 側傳導帶的電子 ● 越過變低的障壁，
    在接面處與 p 側價電帶的電洞 ○ 復合，從復合點射出一條波浪線光子，
    標「hν ≈ E_g」。旁註「一般矽二極體：能量變成熱；直接能隙材料（GaAs、GaN）：變成光」。
  中：一塊扁平長方體晶片（簡潔線稿，參考圖 10.32），上層 p 區、下層 n 區，
    電流 I 由上往下穿過，兩個端面標「劈開的鏡面」，
    從接面層射出一束紅色（#C62828）筆直的雷射光，標「受激輻射 → 同調光」，
    尺寸標「邊長 < 1 mm，發光層僅數 μm」。
  下：一條顏色帶（從紅外到紫外），標三個點：
    「GaAs 1.42 eV → 873 nm（近紅外）」「InGaN 2.7 eV → 459 nm（藍）」
    「GaN 3.4 eV → 365 nm（紫外）」，上方公式 λ ≈ 1240 eV·nm / E_g。

主體中欄（約 37% 寬）｜pill 標籤：穿隧二極體
  上：三張小能帶圖並排，標 (a)(b)(c)，p 區在左、n 區在右，兩側都重摻雜：
    E_F 在 p 側進入價電帶內部、在 n 側進入傳導帶內部（紅色虛線穿過能帶）。
    空乏區非常窄（標「約 10 nm」）。
    (a) 無偏壓：n 側傳導帶的填滿部分與 p 側價電帶的空態在同一能量，
        左右各一支等長的水平箭頭，標「雙向穿隧，淨電流 0」。
    (b) 小順向偏壓：n 側被抬高，只有一支由 n 指向 p 的水平箭頭，標「n → p 穿隧」。
    (c) 大順向偏壓：n 側傳導帶底已高於 p 側價電帶頂，兩者在能量上不重疊，
        水平箭頭打一個紅色 ✗，標「沒有可穿隧的態」。
  下：I–V 曲線：從原點快速上升到峰值 b，接著下降到谷值 c，之後如一般二極體指數上升；
    在 b 到 c 之間用淺紅色底標「負微分電阻」；
    同圖用灰色虛線畫出一般二極體的曲線作對照。標出 a、b、c 三點對應上方三圖。

主體右欄（約 30% 寬）｜pill 標籤：齊納二極體
  上：I–V 曲線：順向在約 0.6–0.7 V 後上升；逆向區先是幾乎為零的平線，
    到達「−V_Z（崩潰電壓）」時曲線突然垂直向下，標「銳利的崩潰轉角」。
    在垂直段旁標「電流大幅改變，電壓幾乎不變 → 穩壓」。
  下：小能帶圖：強逆向偏壓下，p 側價電帶與 n 側傳導帶在能量上重疊，
    一支水平箭頭由 p 側價電帶穿隧到 n 側傳導帶，標「齊納崩潰：穿隧」；
    小字「較高電壓時以累增崩潰為主」。
  最下方一個電路小圖：齊納二極體反接在負載兩端，標「參考電壓／穩壓／保護」。

右上角「圖例」方框：
  波浪線 — 光子
  紅色直線光束 — 雷射光
  水平箭頭 — 穿隧
  淺紅色底 — 負微分電阻區
  灰色虛線 — 一般二極體的 I–V

最下方一排粉彩公式盒（四個）：
1. 淺黃盒：hν ≈ E_g，說明「LED 的顏色由能隙決定」
2. 淺紅盒：鏡面 + 受激輻射 → 同調光，說明「LED 加上共振腔就成為雷射二極體」
3. 淺藍盒：重摻雜 → E_F 進入能帶、空乏區極窄，說明「穿隧效應（第五章）」
4. 淺綠盒：逆向崩潰電壓 V_Z 可設計，說明「單行道變成『到某電壓就放行』」
```

## English Prompt

```
Draw an educational infographic titled "Three variations on one p-n junction:
emitting light, tunnelling, regulating voltage". ALL labels in TRADITIONAL CHINESE.

Title bar: 10.7  LED、穿隧二極體與齊納二極體 (LEDs, Tunnel Diodes and Zener Diodes)

Intro box (Traditional Chinese):
從普通二極體出發：換對材料，復合的能量變成光（LED、雷射）；
把兩側摻得極濃，電子直接穿隧過窄障壁（穿隧二極體）；
設計好逆向崩潰的電壓，就得到穩壓用的齊納二極體。

LEFT column (~33%), pill label LED 與半導體雷射:
  Top: a forward-biased p-n band diagram (style-guide conventions); electrons ●
    from the n-side conduction band cross the lowered barrier and recombine with
    holes ○ in the p-side valence band at the junction; a wavy photon leaves the
    recombination point, labelled hν ≈ E_g. Side note: 一般矽二極體：能量變成熱；
    直接能隙材料（GaAs、GaN）：變成光.
  Middle: a flat rectangular chip (clean line art, after Fig. 10.32), p region on
    top, n region below, current I passing vertically; the two end faces labelled
    劈開的鏡面; a straight red (#C62828) laser beam emerging from the junction
    layer, labelled 受激輻射 → 同調光; dimensions 邊長 < 1 mm，發光層僅數 μm.
  Bottom: a colour strip from infrared to ultraviolet with three marks:
    GaAs 1.42 eV → 873 nm（近紅外）, InGaN 2.7 eV → 459 nm（藍）,
    GaN 3.4 eV → 365 nm（紫外）; formula above: λ ≈ 1240 eV·nm / E_g.

MIDDLE column (~37%), pill label 穿隧二極體:
  Top: three small band diagrams (a)(b)(c), p region left, n region right, both
    heavily doped: E_F lies INSIDE the valence band on the p side and INSIDE the
    conduction band on the n side (red dashed line crossing the bands). Very narrow
    depletion region labelled 約 10 nm.
    (a) 無偏壓: the filled part of the n-side conduction band faces empty states in
        the p-side valence band at the same energy; two equal horizontal arrows in
        opposite directions, labelled 雙向穿隧，淨電流 0.
    (b) 小順向偏壓: n side raised; a single horizontal arrow from n to p, labelled
        n → p 穿隧.
    (c) 大順向偏壓: the n-side conduction-band bottom now lies above the p-side
        valence-band top — no energy overlap; the horizontal arrow crossed with a
        red ✗, labelled 沒有可穿隧的態.
  Bottom: I–V curve rising quickly from the origin to a peak b, falling to a valley
    c, then rising exponentially like an ordinary diode; shade the b–c segment pale
    red labelled 負微分電阻; overlay a grey dashed ordinary-diode curve for
    comparison; mark points a, b, c matching the diagrams above.

RIGHT column (~30%), pill label 齊納二極體:
  Top: I–V curve: forward current rises after about 0.6–0.7 V; in reverse it is a
    nearly zero flat line until −V_Z（崩潰電壓）, where it drops vertically, labelled
    銳利的崩潰轉角; beside the vertical part: 電流大幅改變，電壓幾乎不變 → 穩壓.
  Bottom: a small band diagram under strong reverse bias: the p-side valence band
    overlaps in energy with the n-side conduction band; a horizontal arrow from the
    p-side valence band tunnels into the n-side conduction band, labelled
    齊納崩潰：穿隧; small note 較高電壓時以累增崩潰為主.
  Very bottom: a small circuit with a Zener diode reverse-connected across a load,
    labelled 參考電壓／穩壓／保護.

Top-right legend "圖例":
  波浪線 — 光子
  紅色直線光束 — 雷射光
  水平箭頭 — 穿隧
  淺紅色底 — 負微分電阻區
  灰色虛線 — 一般二極體的 I–V

Bottom pastel boxes (four):
1. light yellow: hν ≈ E_g — LED 的顏色由能隙決定
2. light red: 鏡面 + 受激輻射 → 同調光 — LED 加上共振腔就成為雷射二極體
3. light blue: 重摻雜 → E_F 進入能帶、空乏區極窄 — 穿隧效應（第五章）
4. light green: 逆向崩潰電壓 V_Z 可設計 — 單行道變成『到某電壓就放行』
```
