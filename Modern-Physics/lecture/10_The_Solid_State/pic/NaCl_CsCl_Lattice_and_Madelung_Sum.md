# NaCl_CsCl_Lattice_and_Madelung_Sum.png

**對應章節：** 10.2 離子晶體
**插入位置：** CsCl 的 $1:1$ 共用說明（「配位數……直接決定了晶體的聚合能」）之後、「假設與已知」之前
**課本對應：** 圖 10.5、圖 10.6（馬德隆殼層與收斂圖為自製）

> 產圖前請先貼上 `00_STYLE_GUIDE.md` 的風格區塊。

---

## 中文提示詞

```
請畫一張教學用資訊圖表，主題是「離子晶體的結構、配位數與馬德隆常數」。

標題列文字：10.2  離子晶體的結構與馬德隆常數 (Ionic Crystal Structures and the Madelung Constant)

導言框文字：
離子晶體會排成「每個離子周圍盡量被異性離子包圍」的結構。
要算一個離子的庫侖位能，不能只算最近鄰——庫侖力是長程力，
必須把所有殼層都加進來，結果整包成一個只由幾何決定的數 α。

主體左上｜pill 標籤：NaCl：面心立方，配位數 6
畫一個 3D 立方晶胞（球棍模型、平塗、細描邊），邊長標「0.562 nm」：
  Cl⁻：較大的綠色球（#2E7D32），佔一套面心立方格點（8 個角 + 6 個面心）
  Na⁺：較小的紫色球（#7B1FA2），佔另一套面心立方格點（錯開半個晶格）
  兩種離子沿三個軸交錯排列。
  選定晶胞中央的一個離子，用紅色（#C62828）粗線連到它上下左右前後的
  6 個異性最近鄰，標「配位數 = 6，距離 r」。

主體右上｜pill 標籤：CsCl：體心立方型，配位數 8
畫一個 3D 立方晶胞，邊長標「0.411 nm」：
  8 個角各一個綠色 Cl⁻，正中央一個橘色（#EF6C00）Cs⁺，
  用紅色粗線連出中央 Cs⁺ 到 8 個角的鍵，標「配位數 = 8」。
  其中一個角用淡色畫出它同時屬於 8 個相鄰立方體，標「每個角只算 1/8」，
  旁邊算式：8 × 1/8 = 1 個 Cl⁻ : 1 個 Cs⁺ → 1 : 1。

主體左下｜pill 標籤：以一個 Cl⁻ 為中心的鄰居殼層
畫一張表格式的殼層圖（可用同心的分層色帶 + 表格）：
  | 殼層 j | 距離 | 個數 N_j | 種類 | 貢獻 |
  | 1 | r | 6 | 異性 Na⁺ | −6 （吸引）|
  | 2 | √2 r | 12 | 同性 Cl⁻ | +12/√2 （排斥）|
  | 3 | √3 r | 8 | 異性 | −8/√3 |
  | 4 | 2r | 6 | 同性 | +6/2 |
  | 5 | √5 r | 24 | 異性 | −24/√5 |
  吸引列用藍色（#1565C0），排斥列用紅色（#C62828）。
  表下方寫：α = 6 − 12/√2 + 8/√3 − 6/2 + 24/√5 − … = 1.748

主體右下｜pill 標籤：這個級數要怎麼加？
畫一張折線圖：橫軸「加到第幾項」，縱軸「部分和」（範圍約 −5 到 10）。
  灰色折線（逐層相加）：6, −2.49, 2.13, −0.87, 9.87, 0.07, −4.17, 5.83 ——
    劇烈上下振盪，標「逐層相加：每層殼本身不是電中性，不收斂」。
  綠色折線（Evjen 中性立方體法，橫軸改為立方體大小 L = 1, 2, 3, 6, 10）：
    1.456, 1.752, 1.747, 1.7476, 1.7476 —— 迅速貼上一條水平虛線，
    標「中性區塊相加：收斂到 α = 1.7476」。
  水平紅色虛線標在 1.748。

右上角「圖例」方框：
  綠色大球 — Cl⁻
  紫色小球 — Na⁺
  橘色球 — Cs⁺
  紅色粗線 — 最近鄰（配位）
  藍色／紅色列 — 吸引／排斥殼層

最下方一排粉彩公式盒（三個）：
1. 淺藍盒：U_coulomb = −α e²/(4πε₀ r)　(10.1)，說明「一個離子與其他所有離子的庫侖位能」
2. 淺綠盒：α_NaCl = 1.748，α_CsCl = 1.763，說明「α 只由晶格幾何決定」
3. 淺黃盒：配位數 NaCl = 6，CsCl = 8，說明「最近鄰異性離子的個數」
```

## English Prompt

```
Draw an educational infographic titled "Ionic crystal structures, coordination
numbers and the Madelung constant". ALL labels in TRADITIONAL CHINESE.

Title bar: 10.2  離子晶體的結構與馬德隆常數 (Ionic Crystal Structures and the Madelung Constant)

Intro box (Traditional Chinese):
離子晶體會排成「每個離子周圍盡量被異性離子包圍」的結構。
要算一個離子的庫侖位能，不能只算最近鄰——庫侖力是長程力，
必須把所有殼層都加進來，結果整包成一個只由幾何決定的數 α。

TOP-LEFT, pill label NaCl：面心立方，配位數 6:
A 3D cubic cell (ball-and-stick, flat fills, thin outlines), edge labelled 0.562 nm:
  Cl⁻: larger green balls (#2E7D32) on one fcc lattice (8 corners + 6 face centres)
  Na⁺: smaller purple balls (#7B1FA2) on a second fcc lattice shifted by half a cell
  Ions alternate along all three axes.
  Pick the ion at the cell centre and join it with thick red (#C62828) lines to its
  6 opposite-charge nearest neighbours (up, down, left, right, front, back);
  label 配位數 = 6，距離 r.

TOP-RIGHT, pill label CsCl：體心立方型，配位數 8:
A 3D cubic cell, edge labelled 0.411 nm:
  a green Cl⁻ at each of the 8 corners, one orange (#EF6C00) Cs⁺ at the body centre,
  thick red lines from the centre to all 8 corners, labelled 配位數 = 8.
  Ghost-draw one corner shared by 8 neighbouring cubes, labelled 每個角只算 1/8,
  with the arithmetic 8 × 1/8 = 1 個 Cl⁻ : 1 個 Cs⁺ → 1 : 1.

BOTTOM-LEFT, pill label 以一個 Cl⁻ 為中心的鄰居殼層:
A shell table (optionally with concentric coloured bands beside it):
  | 殼層 j | 距離 | 個數 N_j | 種類 | 貢獻 |
  | 1 | r | 6 | 異性 Na⁺ | −6 （吸引）|
  | 2 | √2 r | 12 | 同性 Cl⁻ | +12/√2 （排斥）|
  | 3 | √3 r | 8 | 異性 | −8/√3 |
  | 4 | 2r | 6 | 同性 | +6/2 |
  | 5 | √5 r | 24 | 異性 | −24/√5 |
  Attractive rows in blue (#1565C0), repulsive rows in red (#C62828).
  Under the table: α = 6 − 12/√2 + 8/√3 − 6/2 + 24/√5 − … = 1.748

BOTTOM-RIGHT, pill label 這個級數要怎麼加？:
A line chart; x-axis 加到第幾項, y-axis 部分和 (about −5 to 10).
  Grey polyline (shell by shell): 6, −2.49, 2.13, −0.87, 9.87, 0.07, −4.17, 5.83 —
    wildly oscillating, labelled 逐層相加：每層殼本身不是電中性，不收斂.
  Green polyline (Evjen neutral cubes, x now the cube size L = 1, 2, 3, 6, 10):
    1.456, 1.752, 1.747, 1.7476, 1.7476 — quickly hugging a horizontal line,
    labelled 中性區塊相加：收斂到 α = 1.7476.
  A red horizontal dashed line at 1.748.

Top-right legend "圖例":
  綠色大球 — Cl⁻
  紫色小球 — Na⁺
  橘色球 — Cs⁺
  紅色粗線 — 最近鄰（配位）
  藍色／紅色列 — 吸引／排斥殼層

Bottom pastel boxes (three):
1. light blue: U_coulomb = −α e²/(4πε₀ r)  (10.1) — 一個離子與其他所有離子的庫侖位能
2. light green: α_NaCl = 1.748，α_CsCl = 1.763 — α 只由晶格幾何決定
3. light yellow: 配位數 NaCl = 6，CsCl = 8 — 最近鄰異性離子的個數
```
