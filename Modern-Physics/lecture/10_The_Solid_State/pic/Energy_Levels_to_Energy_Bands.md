# Energy_Levels_to_Energy_Bands.png

**對應章節：** 10.6 固體的能帶理論
**插入位置：**「從能階到能帶」一節末段（能帶重疊與禁止帶）之後、「假設與已知」之前
**課本對應：** 圖 10.19、圖 10.20、圖 10.21

> 產圖前請先貼上 `00_STYLE_GUIDE.md` 的風格區塊。

---

## 中文提示詞

```
【模型與符號】每原子取一個空間軌域時，N 原子形成 N 個空間態；包含兩種自旋才有 2N 個單電子態。若圖只畫能量分裂線，標明未計自旋。

請畫一張教學用資訊圖表，主題是「從原子的能階到固體的能帶」。

標題列文字：10.6  從能階到能帶 (From Energy Levels to Energy Bands)

導言框文字：
兩個原子靠近，一條能階分裂成兩條；五個原子，分裂成五條；
10²³ 個原子，分裂成 10²³ 條，擠在幾個 eV 之內，間距只有約 10⁻²³ eV——
這就是能帶。最外層的能階最先展開，內層幾乎不受影響。

主體上排｜pill 標籤：原子越多，分裂越多
畫三張並排的小座標圖，橫軸皆為「核間距」（向右增大），縱軸皆為「能量」：
  (a) 2 個原子：右側（間距大）是一條水平線；往左（間距縮小）時分裂成兩條曲線，
      一條往下（標「對稱，較低」）、一條往上（標「反對稱，較高」）。
      小字：「第八章：氫分子的能階分裂」。
  (b) 5 個原子：右側一條水平線，往左分裂成 5 條曲線，像扇子一樣展開。
  (c) N 個原子（固體）：右側一條水平線，往左展開成一整片灰藍色填滿的區域
      （#B0BEC5），標「能帶：N 條能階，準連續」。
  三圖下方一條藍色（#1565C0）說明：「能階數守恆：N 個原子 → 每條能階分裂成 N 條」。

主體下排左（約 60% 寬）｜pill 標籤：鈉的能帶對核間距
畫一張座標圖，橫軸「核間距（nm）」0 到 1.5，縱軸「能量（eV）」0 到 −35：
  2p 能階：在 −31 eV 附近一條幾乎水平的細線，只在核間距很小（< 0.2 nm）時才展開。
  3s 能階：在約 −5 eV 處，從核間距約 1 nm 開始往左展開成一個灰藍色的能帶，
    越往左越寬。
  3p、4s、3d：在 −3 到 −1 eV 附近，更早展開並且彼此重疊成一片（用不同深淺的灰藍）。
  在核間距 0.367 nm 處畫一條紅色（#C62828）垂直虛線，標「實際核間距 0.367 nm」。
  在虛線與各能帶交會處標註：「2p：仍是細線（內層不受影響）」
  「3s：已展開成能帶」「3p/4s/3d：互相重疊」。
  在圖的左下角標「1s、2s 更深，未畫出」。

主體下排右（約 40% 寬）｜pill 標籤：從虛線往上讀：兩種情形
畫兩個垂直的能帶示意柱：
  (a) 重疊的能帶：兩個灰藍色長方形上下部分交疊，中間交疊處顏色較深，
      標「重疊 → 連續的能帶」。
  (b) 禁止帶：兩個灰藍色長方形之間留一段白色空白，用大括號標「禁止帶／能隙 E_g」，
      小字「此區間內沒有任何允許的能態」。

右上角「圖例」方框：
  細水平線 — 離散的原子能階
  灰藍色填色區 — 能帶（準連續）
  紅色垂直虛線 — 固體實際的核間距
  白色空白 + 大括號 — 能隙

最下方一排粉彩公式盒（三個）：
1. 淺藍盒：1 條原子能階 → N 條能階，說明「能階數守恆」
2. 淺綠盒：ΔE ≈ W/N ≈ 數 eV / 10²³ ≈ 10⁻²³ eV，說明「遠小於 k_B T ≈ 0.026 eV，實質連續」
3. 淺黃盒：外層先展開、內層後展開，說明「外層軌域大，最早和鄰居重疊」
```

## English Prompt

```
MODEL AND NOTATION: One spatial orbital per atom yields N spatial states for N atoms, or 2N single-electron states including spin. Label energy-splitting lines as excluding spin.

Draw an educational infographic titled "From atomic energy levels to energy bands
in a solid". ALL labels in TRADITIONAL CHINESE.

Title bar: 10.6  從能階到能帶 (From Energy Levels to Energy Bands)

Intro box (Traditional Chinese):
兩個原子靠近，一條能階分裂成兩條；五個原子，分裂成五條；
10²³ 個原子，分裂成 10²³ 條，擠在幾個 eV 之內，間距只有約 10⁻²³ eV——
這就是能帶。最外層的能階最先展開，內層幾乎不受影響。

TOP row, pill label 原子越多，分裂越多:
Three small side-by-side plots, x-axis 核間距 (increasing to the right),
y-axis 能量:
  (a) 2 atoms: a single horizontal line at the right (large spacing) that splits
      into two curves toward the left — one bending down (標「對稱，較低」),
      one bending up (標「反對稱，較高」). Small text: 第八章：氫分子的能階分裂.
  (b) 5 atoms: one horizontal line on the right fanning out into 5 curves on the left.
  (c) N atoms (solid): one horizontal line on the right opening into a solid
      grey-blue filled region (#B0BEC5) on the left, labelled 能帶：N 條能階，準連續.
  Blue (#1565C0) caption under the three: 能階數守恆：N 個原子 → 每條能階分裂成 N 條.

BOTTOM-LEFT ~60%, pill label 鈉的能帶對核間距:
A plot, x-axis 核間距（nm） 0 to 1.5, y-axis 能量（eV） 0 to −35:
  2p: a nearly horizontal thin line near −31 eV, broadening only below ~0.2 nm.
  3s: near −5 eV, broadening into a grey-blue band starting around 1 nm and
      widening toward the left.
  3p, 4s, 3d: near −3 to −1 eV, broadening even earlier and overlapping one another
      (different shades of grey-blue).
  A red (#C62828) vertical dashed line at 0.367 nm labelled 實際核間距 0.367 nm.
  Where the dashed line crosses each feature, annotate: 2p：仍是細線（內層不受影響）;
  3s：已展開成能帶; 3p/4s/3d：互相重疊.
  Lower-left note: 1s、2s 更深，未畫出.

BOTTOM-RIGHT ~40%, pill label 從虛線往上讀：兩種情形:
Two vertical band columns:
  (a) overlapping bands: two grey-blue rectangles partly overlapping, the overlap
      darker, labelled 重疊 → 連續的能帶.
  (b) forbidden band: two grey-blue rectangles separated by white space, a brace
      labelled 禁止帶／能隙 E_g, small text 此區間內沒有任何允許的能態.

Top-right legend "圖例":
  細水平線 — 離散的原子能階
  灰藍色填色區 — 能帶（準連續）
  紅色垂直虛線 — 固體實際的核間距
  白色空白 + 大括號 — 能隙

Bottom pastel boxes (three):
1. light blue: 1 條原子能階 → N 條能階 — 能階數守恆
2. light green: ΔE ≈ W/N ≈ 數 eV / 10²³ ≈ 10⁻²³ eV — 遠小於 k_B T ≈ 0.026 eV，實質連續
3. light yellow: 外層先展開、內層後展開 — 外層軌域大，最早和鄰居重疊
```
