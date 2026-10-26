# Maxwell_Speed_Distribution.png

**對應章節：** 9.3 理想氣體中的分子能量
**插入位置：**「三種『平均』速率」的說明之後、例題 9.3 之前
**課本對應：** 圖 9.3、圖 9.4

> 產圖前請先貼上 `00_STYLE_GUIDE.md` 的風格區塊。

---

## 中文提示詞

```
請畫一張教學用資訊圖表，主題是「馬克士威爾－波茲曼速率分布與三種代表速率」。

標題列文字：9.3  馬克士威爾－波茲曼速率分布 (Maxwell–Boltzmann Speed Distribution)

導言框文字：
把能量分布用 ε = ½mv² 換成速率，就得到 n(v) ∝ v² e^(−mv²/2kT)。
同一條曲線可以定義三種「平均」速率，它們的大小不同、意義也不同；
但三者都正比於 √(T/m)——溫度愈高、分子愈輕，跑得愈快。

主體分成左右兩大區。

左區（約 50% 寬）｜pill 標籤：三種代表速率（圖 9.3）
一張平面圖，橫軸 v、縱軸 n(v)（皆不標數值），淺灰色細格線。
畫一條綠色（#2E7D32）粗實線的鐘形但右側拖長尾的曲線：
在 v = 0 為零（以 v² 的方式起步，起點斜率為零）、上升到峰值、再緩慢下降。
在曲線下方畫三條由左到右的垂直虛線，間距比例為 1 : 1.128 : 1.225：
  第一條（灰色）落在峰值正下方：v_p = √(2kT/m)，標「最可能速率」
  第二條（紫色）：v̄ = √(8kT/πm)，標「平均速率」
  第三條（橘色）：v_rms = √(3kT/m)，標「均方根速率」
三條線的標籤用引線拉到圖下方依序排列，不可互相重疊。
圖旁加一個小說明框：
  「v_rms / v̄ = √(3π/8) ≈ 1.09（例題 9.3）」
  「為什麼要用均方根？交流電壓、電流有正有負，直接平均會得到 0；
    而且 ½ m v_rms² 恰好等於平均動能 (3/2)kT」

右區（約 50% 寬）｜pill 標籤：溫度與質量的影響（圖 9.4）
一張平面圖，橫軸「分子速率 (m/s)」刻度 0、400、800、1200、1600、2000；
縱軸「在指示速率 10 m/s 之內的分子百分比」，刻度 0、1、2、3。
畫三條曲線：
  O₂（73 K）：深灰虛線，又高又窄，峰值約在 195 m/s、高度約 4.3，曲線頂端超出圖框上緣
  O₂（273 K）：綠色實線，峰值約在 377 m/s、高度約 2.2
  H₂（273 K）：紫色虛線，又矮又寬，峰值約在 1500 m/s、高度約 0.55
每條曲線旁直接標註名稱與溫度。
加一行小字：「三條曲線下的面積相同（分子總數相同），所以愈窄的愈高」。
再加兩個箭頭註解：
  O₂ 73 K → 273 K：「溫度升高，分布變寬、峰值右移」
  O₂ 273 K → H₂ 273 K：「質量變為 1/16，速率變為 4 倍」

右上角「圖例」方框：
  綠色實線 — n(v)：馬克士威爾－波茲曼速率分布
  灰色虛線 — 最可能速率 v_p
  紫色虛線 — 平均速率 v̄
  橘色虛線 — 均方根速率 v_rms

最下方一排粉彩公式盒（四個）：
1. 淺綠盒：n(v) dv = 4πN (m/2πkT)^(3/2) v² e^(−mv²/2kT) dv，說明「(9.14) 速率分布」
2. 淺紫盒：v_p : v̄ : v_rms = √2 : √(8/π) : √3，說明「(9.16)、例題 9.3、(9.15)」
3. 淺藍盒：v ∝ √(T/m)，說明「三種速率共同的標度律，係數只是數字」
4. 淺黃盒：v_rms(O₂, 273 K) ≈ 461 m/s，說明「例題 9.4：和音速 331 m/s 同一個數量級」
```

## English Prompt

```
Draw an educational infographic titled "The Maxwell–Boltzmann speed distribution
and its three characteristic speeds". ALL labels in TRADITIONAL CHINESE.

Title bar: 9.3  馬克士威爾－波茲曼速率分布 (Maxwell–Boltzmann Speed Distribution)

Intro box (Traditional Chinese):
把能量分布用 ε = ½mv² 換成速率，就得到 n(v) ∝ v² e^(−mv²/2kT)。
同一條曲線可以定義三種「平均」速率，它們的大小不同、意義也不同；
但三者都正比於 √(T/m)——溫度愈高、分子愈輕，跑得愈快。

Two halves.

LEFT half, pill label 三種代表速率（圖 9.3）:
A 2D plot, x-axis v, y-axis n(v) (no numbers), faint grey grid.
A thick solid green (#2E7D32) curve: zero at v = 0 (starting like v², zero initial slope),
rising to a peak, then a long slowly decaying right tail.
Three vertical dashed lines, left to right, spaced in the ratio 1 : 1.128 : 1.225:
  first (grey) exactly under the peak: v_p = √(2kT/m), label 最可能速率
  second (purple): v̄ = √(8kT/πm), label 平均速率
  third (orange): v_rms = √(3kT/m), label 均方根速率
Bring the three labels out with leader lines below the plot so they never overlap.
A small note box beside the plot:
  v_rms / v̄ = √(3π/8) ≈ 1.09（例題 9.3）
  為什麼要用均方根？交流電壓、電流有正有負，直接平均會得到 0；
  而且 ½ m v_rms² 恰好等於平均動能 (3/2)kT

RIGHT half, pill label 溫度與質量的影響（圖 9.4）:
A 2D plot, x-axis 分子速率 (m/s) with ticks 0, 400, 800, 1200, 1600, 2000;
y-axis 在指示速率 10 m/s 之內的分子百分比 with ticks 0, 1, 2, 3.
Three curves:
  O₂ (73 K): dark-grey dashed, tall and narrow, peak near 195 m/s with height about 4.3, its top running off the frame
  O₂ (273 K): solid green, peak near 377 m/s, height about 2.2
  H₂ (273 K): purple dashed, low and broad, peak near 1500 m/s, height about 0.55
Label each curve directly with its name and temperature.
Small text: 三條曲線下的面積相同（分子總數相同），所以愈窄的愈高.
Two arrow annotations:
  O₂ 73 K → 273 K: 溫度升高，分布變寬、峰值右移
  O₂ 273 K → H₂ 273 K: 質量變為 1/16，速率變為 4 倍

Top-right legend "圖例":
  綠色實線 — n(v)：馬克士威爾－波茲曼速率分布
  灰色虛線 — 最可能速率 v_p
  紫色虛線 — 平均速率 v̄
  橘色虛線 — 均方根速率 v_rms

Bottom pastel boxes (four):
1. light green: n(v) dv = 4πN (m/2πkT)^(3/2) v² e^(−mv²/2kT) dv — (9.14) 速率分布
2. light purple: v_p : v̄ : v_rms = √2 : √(8/π) : √3 — (9.16)、例題 9.3、(9.15)
3. light blue: v ∝ √(T/m) — 三種速率共同的標度律，係數只是數字
4. light yellow: v_rms(O₂, 273 K) ≈ 461 m/s — 例題 9.4：和音速 331 m/s 同一個數量級
```
