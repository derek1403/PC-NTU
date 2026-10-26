# Junction_Transistor_and_FET.png

**對應章節：** 10.7 半導體元件
**插入位置：**「場效電晶體」一節之後、BJT 與 FET 比較表之前
**課本對應：** 圖 10.36、圖 10.37、圖 10.38

> 產圖前請先貼上 `00_STYLE_GUIDE.md` 的風格區塊。

---

## 中文提示詞

```
請畫一張教學用資訊圖表，主題是「電晶體：用第三端控制另外兩端的電流」。

標題列文字：10.7  接面電晶體與場效電晶體 (Junction Transistor and Field-Effect Transistor)

導言框文字：
電晶體是三端元件：透過其中一端，控制另外兩端之間的電流。
接面電晶體 (BJT) 用基極改變障壁的高度，指數地控制電流，適合放大；
場效電晶體 (FET) 用閘極電壓改變空乏區的寬度，幾乎不耗電，適合當開關。

主體左半（約 55% 寬）｜pill 標籤：n-p-n 接面電晶體 (BJT)
  上：電路圖（參考圖 10.36）：一條水平的 n | p | n 長條，三段分別標
    「射極 (emitter)」「基極 (base)」「集極 (collector)」，中間 p 段畫得很窄。
    射極左側接「輸入訊號」與小電池 V₁（射極–基極順向偏壓）；
    集極右側接「輸出負載」電阻與較大的電池 V₂（基極–集極逆向偏壓）；
    基極向下接地。
  中：未加偏壓的能帶圖（參考圖 10.37a）：三區 E_F（紅色虛線）對齊，
    兩側 n 區傳導帶較低、中間 p 區傳導帶較高，像一座小山丘；
    三區下方分別標「高摻雜 n 區」「低摻雜 p 區（很薄）」「低摻雜 n 區」。
  下：加上偏壓的能帶圖（參考圖 10.37b）：
    射極側的山丘被壓低（標「V₁e：小的順向偏壓，降低障壁」），
    集極側的傳導帶大幅下降形成「瀑布」（標「V₂e：大的逆向偏壓」）。
    一串黑色電子 ● 從射極越過壓低的障壁、橫越很薄的基極（標「來不及與電洞復合」）、
    再從瀑布掉進集極（標「掉下去就爬不回來」）。
    在射極側障壁處畫一個綠色（#2E7D32）雙向小箭頭，標「基極控制這裡的高度 → 電流指數變化 → 放大」。

主體右半（約 45% 寬）｜pill 標籤：場效電晶體 (FET)
  上：結構圖（參考圖 10.38）：一條水平的 n 型通道（淺灰長方形），
    左端標「源極 (source)」、右端標「汲極 (drain)」，
    通道上方一塊 p 型閘極標「閘極 (gate)」，閘極下方有一片淡紫色（#7B1FA2）的空乏區伸入通道。
    源極與汲極間接電池與「輸出負載」；閘極接「輸入訊號」。
  下：兩個並排的剖面小圖：
    左「閘極逆向偏壓小」：空乏區薄、通道寬，一串電子 ● 順利由源極流到汲極，標「導通」。
    右「閘極逆向偏壓大」：空乏區變厚幾乎碰到通道底部，電子被擋住，標「夾止 → 關閉」。
  小字：「閘極是逆向偏壓的接面，幾乎沒有電流流入；IC 中的 MOSFET 更用氧化層完全隔開」。

主體下方（橫跨全寬）｜pill 標籤：BJT 與 FET 比較
  一張四列兩欄的表：
  | | 接面電晶體 BJT | 場效電晶體 FET |
  | 控制端 | 基極 | 閘極 |
  | 控制方式 | 電流／注入改變障壁高度 | 電壓（電場）改變空乏區寬度 |
  | 控制端電流 | 有，耗電 | 幾乎為零，省電 |
  | 典型用途 | 放大器（類比） | 開關（數位） |

右上角「圖例」方框：
  灰藍實心 — 價電帶
  白底細框 — 傳導帶
  紅色虛線 — 費米能量 E_F
  淡紫色區 — 空乏區
  ● — 電子

最下方一排粉彩公式盒（三個）：
1. 淺藍盒：I ∝ e^(e·ΔV/k_BT)，說明「基極端一點點改變 → 集極電流大幅改變」
2. 淺紫盒：閘極電壓 → 空乏區寬度 → 通道寬度，說明「用電場開關電流：場效」
3. 淺綠盒：電晶體 = 三端元件，說明「用第三端控制另外兩端的電流」
```

## English Prompt

```
Draw an educational infographic titled "Transistors: a third terminal controls
the current between the other two". ALL labels in TRADITIONAL CHINESE.

Title bar: 10.7  接面電晶體與場效電晶體 (Junction Transistor and Field-Effect Transistor)

Intro box (Traditional Chinese):
電晶體是三端元件：透過其中一端，控制另外兩端之間的電流。
接面電晶體 (BJT) 用基極改變障壁的高度，指數地控制電流，適合放大；
場效電晶體 (FET) 用閘極電壓改變空乏區的寬度，幾乎不耗電，適合當開關。

LEFT ~55%, pill label n-p-n 接面電晶體 (BJT):
  Top: a circuit (after Fig. 10.36): a horizontal n | p | n bar with the three parts
    labelled 射極 (emitter), 基極 (base), 集極 (collector); the middle p part
    drawn very narrow. On the emitter side an 輸入訊號 and a small battery V₁
    (emitter–base forward bias); on the collector side an 輸出負載 resistor and a
    larger battery V₂ (base–collector reverse bias); the base goes to ground.
  Middle: the unbiased band diagram (after Fig. 10.37a): the three red dashed E_F
    lines aligned; both n regions have a low conduction band and the p region a
    higher one, like a small hill; under the regions: 高摻雜 n 區,
    低摻雜 p 區（很薄）, 低摻雜 n 區.
  Bottom: the biased band diagram (after Fig. 10.37b): the hill on the emitter side
    lowered (labelled V₁e：小的順向偏壓，降低障壁); the collector conduction band
    dropped far down forming a "waterfall" (labelled V₂e：大的逆向偏壓). A train of
    black electrons ● crosses the lowered barrier from the emitter, crosses the thin
    base (labelled 來不及與電洞復合), then falls down the waterfall into the
    collector (labelled 掉下去就爬不回來). At the emitter-side barrier a small green
    (#2E7D32) double arrow labelled 基極控制這裡的高度 → 電流指數變化 → 放大.

RIGHT ~45%, pill label 場效電晶體 (FET):
  Top: the structure (after Fig. 10.38): a horizontal n-type channel (light-grey
    rectangle), left end 源極 (source), right end 汲極 (drain); a p-type 閘極 (gate)
    on top with a pale purple (#7B1FA2) depletion region extending down into the
    channel. A battery and 輸出負載 between source and drain; 輸入訊號 on the gate.
  Bottom: two side-by-side cross-sections:
    left 閘極逆向偏壓小: thin depletion region, wide channel, electrons ● flowing
      from source to drain, labelled 導通.
    right 閘極逆向偏壓大: depletion region thick enough to nearly reach the channel
      bottom, electrons blocked, labelled 夾止 → 關閉.
  Small note: 閘極是逆向偏壓的接面，幾乎沒有電流流入；IC 中的 MOSFET 更用氧化層完全隔開.

BOTTOM (full width), pill label BJT 與 FET 比較:
  A table with four rows and two columns:
  | | 接面電晶體 BJT | 場效電晶體 FET |
  | 控制端 | 基極 | 閘極 |
  | 控制方式 | 電流／注入改變障壁高度 | 電壓（電場）改變空乏區寬度 |
  | 控制端電流 | 有，耗電 | 幾乎為零，省電 |
  | 典型用途 | 放大器（類比） | 開關（數位） |

Top-right legend "圖例":
  灰藍實心 — 價電帶
  白底細框 — 傳導帶
  紅色虛線 — 費米能量 E_F
  淡紫色區 — 空乏區
  ● — 電子

Bottom pastel boxes (three):
1. light blue: I ∝ e^(e·ΔV/k_BT) — 基極端一點點改變 → 集極電流大幅改變
2. light purple: 閘極電壓 → 空乏區寬度 → 通道寬度 — 用電場開關電流：場效
3. light green: 電晶體 = 三端元件 — 用第三端控制另外兩端的電流
```
