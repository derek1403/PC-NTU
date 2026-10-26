# Crystal_Defects.png

**對應章節：** 10.1 晶態與非晶態固體
**插入位置：**「晶格缺陷」一節末段（缺陷成因與退火）之後、【物理知識回顧】之前
**課本對應：** 圖 10.2、圖 10.3、圖 10.4

> 產圖前請先貼上 `00_STYLE_GUIDE.md` 的風格區塊。

---

## 中文提示詞

```
請畫一張教學用資訊圖表，主題是「晶格缺陷：點、線、面，以及為什麼缺陷不一定是壞事」。

標題列文字：10.1  晶格缺陷 (Crystal Defects)

導言框文字：
完美的晶體並不存在。10²³ 個原子凝結時，若溫度不夠高或時間不夠長，
原子來不及走到能量最低的位置就被凍住，留下各種缺陷。
但受控制的缺陷（摻雜）正是半導體工業的起點。

主體上排｜pill 標籤：四種點缺陷 (Point Defects)
畫四個並排的小方格，每格是 5×5 的正方晶格，原子用白底黑框的空心圓表示：
  (a) 空位 (vacancy)：中央一個格點空著，用紅色（#C62828）虛線圓標出空位。
  (b) 間隙原子 (interstitial)：一個同種的空心圓擠在四個格點中間，
      周圍的鄰居稍微被推開（畫出輕微變形）。
  (c) 取代雜質 (substitutional impurity)：中央格點上的原子換成一個
      深灰色實心圓（外來原子），用綠色（#2E7D32）標出。
      旁邊小字：「摻雜就是有計畫地製造這種缺陷」。
  (d) 間隙雜質 (interstitial impurity)：一個小的深灰色實心圓夾在四個格點之間。
每格下方標中文名稱與英文。

主體中排｜pill 標籤：邊緣錯位的移動 (Edge Dislocation)
畫三格連環圖，從左到右：
  第 1 格：一塊方格狀晶體，上半部多插入了半個原子面，
    錯位處用「⊥」符號標示並標「錯位線」。
  第 2 格：上方左側與下方右側各有一支橘色（#EF6C00）箭頭標「外力」（剪應力）。
    上層原子的鍵結一次只換一排，⊥ 往右移動了一格。
  第 3 格：⊥ 已移出晶體右側，晶體表面留下一個台階，標「永久形變」。
格子下方一條藍色（#1565C0）說明文字：
  「一次只斷一排鍵 → 所需的力遠小於整層原子一起滑動」。
另加一行灰色小字：「加熱退火可讓錯位移出晶體，把缺陷『逼出』體外」。

主體下排左｜pill 標籤：螺旋錯位 (Screw Dislocation)
畫一塊由小立方體堆成的方塊（簡潔線稿、無陰影），
其中一側的原子面沿一條垂直的錯位線像螺旋梯一樣盤旋，
在方塊上表面形成一道台階，用紫色（#7B1FA2）螺旋箭頭標出盤旋方向。

主體下排右｜pill 標籤：缺陷從哪裡來
畫兩個小對照：
  左：「天然鑽石」——地球圖示 + 「數億年、高溫高壓、緩慢成長」→ 晶格較完美
  右：「人工快速長晶」——碼表圖示 + 「幾分鐘到幾小時」→ 缺陷較多
中間一個天平圖示：溫度 × 時間。

右上角「圖例」方框：
  白底空心圓 — 晶格原子
  深灰實心圓 — 外來雜質原子
  紅色虛線圓 — 空位
  ⊥ — 邊緣錯位線
  橘色箭頭 — 外力（剪應力）

最下方一排粉彩公式盒（三個）：
1. 淺黃盒：點缺陷 → 線缺陷 → 面缺陷，說明「空位／雜質 → 錯位 → 晶界」
2. 淺綠盒：受控缺陷 = 摻雜，說明「n 型、p 型半導體的來源（10.6）」
3. 淺紅盒：不受控缺陷，說明「增加電阻、讓金屬容易塑性變形」
```

## English Prompt

```
Draw an educational infographic titled "Crystal defects: point, line and planar —
and why defects are not always bad". ALL labels in TRADITIONAL CHINESE.

Title bar: 10.1  晶格缺陷 (Crystal Defects)

Intro box (Traditional Chinese):
完美的晶體並不存在。10²³ 個原子凝結時，若溫度不夠高或時間不夠長，
原子來不及走到能量最低的位置就被凍住，留下各種缺陷。
但受控制的缺陷（摻雜）正是半導體工業的起點。

TOP row, pill label 四種點缺陷 (Point Defects):
Four small side-by-side panels, each a 5×5 square lattice of open white circles
with black outlines:
  (a) 空位 (vacancy): the central site is empty, marked by a red (#C62828) dashed circle.
  (b) 間隙原子 (interstitial): an identical open circle squeezed between four
      sites, its neighbours slightly pushed apart.
  (c) 取代雜質 (substitutional impurity): the central atom replaced by a dark-grey
      solid circle, marked in green (#2E7D32); small note:
      摻雜就是有計畫地製造這種缺陷.
  (d) 間隙雜質 (interstitial impurity): a small dark-grey solid circle sitting
      in a gap between four sites.
Label each panel with the Chinese and English names.

MIDDLE row, pill label 邊緣錯位的移動 (Edge Dislocation):
A three-frame strip, left to right:
  Frame 1: a square-grid crystal with an extra half-plane inserted in the top half;
    the dislocation marked with the "⊥" symbol and labelled 錯位線.
  Frame 2: orange (#EF6C00) arrows labelled 外力 (shear) on the upper-left and
    lower-right; the bonds switch one row at a time and ⊥ has moved one column right.
  Frame 3: ⊥ has left the crystal on the right, leaving a surface step labelled
    永久形變.
Blue (#1565C0) caption under the strip:
  一次只斷一排鍵 → 所需的力遠小於整層原子一起滑動.
Grey small text: 加熱退火可讓錯位移出晶體，把缺陷「逼出」體外.

BOTTOM-LEFT, pill label 螺旋錯位 (Screw Dislocation):
A clean line-art block of small cubes (no shading) in which the atomic planes
spiral around a vertical dislocation line like a spiral staircase, producing a
step on the top face; show the winding with a purple (#7B1FA2) spiral arrow.

BOTTOM-RIGHT, pill label 缺陷從哪裡來:
Two small contrasting vignettes:
  left: 天然鑽石 — Earth icon + 數億年、高溫高壓、緩慢成長 → 晶格較完美
  right: 人工快速長晶 — stopwatch icon + 幾分鐘到幾小時 → 缺陷較多
A small balance icon between them labelled 溫度 × 時間.

Top-right legend "圖例":
  白底空心圓 — 晶格原子
  深灰實心圓 — 外來雜質原子
  紅色虛線圓 — 空位
  ⊥ — 邊緣錯位線
  橘色箭頭 — 外力（剪應力）

Bottom pastel boxes (three):
1. light yellow: 點缺陷 → 線缺陷 → 面缺陷 — 空位／雜質 → 錯位 → 晶界
2. light green: 受控缺陷 = 摻雜 — n 型、p 型半導體的來源（10.6）
3. light red: 不受控缺陷 — 增加電阻、讓金屬容易塑性變形
```
