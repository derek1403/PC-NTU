# Doping_Donor_Acceptor_Levels.png

**對應章節：** 10.6 固體的能帶理論
**插入位置：**「摻雜如何移動費米能量」（$n$ 型往上、$p$ 型往下）之後、「有效質量」之前
**課本對應：** 圖 10.26、圖 10.27、圖 10.28、圖 10.29

> 產圖前請先貼上 `00_STYLE_GUIDE.md` 的風格區塊。

---

## 中文提示詞

```
請畫一張教學用資訊圖表，主題是「摻雜：用痕量雜質控制半導體」。

標題列文字：10.6  n 型與 p 型半導體 (n-type and p-type Semiconductors)

導言框文字：
在矽中摻入痕量的 V 族元素（如砷），多出的電子在傳導帶下方形成施子能階；
摻入 III 族元素（如鎵），少掉的電子在價電帶上方形成受子能階。
兩者都只離能帶邊緣數十 meV，室溫就足以把載子送進能帶。

主體左半｜pill 標籤：n 型：摻砷 (As)
  上方：二維示意的矽晶格（4×4 個灰色圓，每個圓以兩條短線與上下左右相連，
    代表共價鍵與共用電子對）。中央一個格點換成較大的綠色（#2E7D32）圓標「As⁺」，
    它的四條鍵照常；另有一顆黑色實心電子在以 As⁺ 為中心、半徑約跨過 4 個晶格的
    淡綠色大圓軌道上，標「多出的第 5 個電子（軌道半徑約 2.4 nm）」。
  下方：能帶圖（遵守風格指南）——
    灰藍實心價電帶、白色傳導帶、能隙標「1.1 eV」；
    傳導帶下方約 0.05 eV 處一排綠色短虛線，標「施子能階（約 0.05 eV）」；
    幾支向上的小箭頭從施子能階指向傳導帶，傳導帶中有數個黑色電子 ●；
    紅色虛線 E_F 畫在靠近傳導帶的位置，標「E_F 往上移」。
  旁邊小圖（圖 10.27 精神）：一塊晶體兩端接電池，多出的電子朝正極移動。

主體右半｜pill 標籤：p 型：摻鎵 (Ga)
  上方：同樣的矽晶格，中央換成紫色（#7B1FA2）圓標「Ga⁻」，
    它的四條鍵中有一條只畫一個電子，旁邊一個空心小圓圈標「電洞（少一個電子）」。
  下方：能帶圖——
    價電帶上方數十 meV 處一排紫色短虛線，標「受子能階」；
    幾支向上的小箭頭從價電帶頂端指向受子能階，價電帶頂部留下數個空心小圓 ○；
    紅色虛線 E_F 畫在靠近價電帶的位置，標「E_F 往下移」。
  旁邊小圖（圖 10.28 精神）：三個時間點的晶格，空位一格一格朝負極移動，
    標「鄰近電子遞補空位 → 看起來是電洞朝負極移動」。

主體中下方（橫跨全寬）｜pill 標籤：費米能量由電子的數目決定
畫一個教室座位的側視示意：一排排座位由前到後，學生從第一排開始坐：
  左：「20 人 → 坐到第 3 排」，E_F 標在第 3 排；
  中：「再進來 20 人 → 坐到第 8 排」，E_F 上移，標「n 型：電子變多」；
  右：「離開 10 人 → 退到第 2 排」，E_F 下移，標「p 型：電子變少（電洞變多）」。

右上角「圖例」方框：
  灰藍實心 — 價電帶（填滿）
  白底細框 — 傳導帶
  綠色短虛線 — 施子能階
  紫色短虛線 — 受子能階
  紅色虛線 — 費米能量 E_F
  ● 電子　○ 電洞

最下方一排粉彩公式盒（四個）：
1. 淺綠盒：E_d = (m*/m)(E₁/κ²) ≈ −0.026 eV，說明「類氫施子：κ = 11.7、m* ≈ 0.26m」
2. 淺藍盒：a_d = κ(m/m*)a₀ ≈ 2.4 nm，說明「軌道內包含約 2800 個矽原子」
3. 淺黃盒：摻雜 10¹⁵–10¹⁸ cm⁻³ ≪ 矽原子 5×10²² cm⁻³，說明「痕量雜質卻主宰電性」
4. 淺紫盒：n 型 E_F 靠傳導帶，p 型 E_F 靠價電帶，說明「組成元件時最重要的資訊」
```

## English Prompt

```
Draw an educational infographic titled "Doping: controlling a semiconductor with
trace impurities". ALL labels in TRADITIONAL CHINESE.

Title bar: 10.6  n 型與 p 型半導體 (n-type and p-type Semiconductors)

Intro box (Traditional Chinese):
在矽中摻入痕量的 V 族元素（如砷），多出的電子在傳導帶下方形成施子能階；
摻入 III 族元素（如鎵），少掉的電子在價電帶上方形成受子能階。
兩者都只離能帶邊緣數十 meV，室溫就足以把載子送進能帶。

LEFT half, pill label n 型：摻砷 (As):
  Top: a 2-D sketch of the silicon lattice (4×4 grey circles, each joined to its
    four neighbours by double short lines representing shared electron pairs).
    The central site replaced by a larger green (#2E7D32) circle labelled As⁺ with
    its four bonds intact; one extra solid black electron on a large pale-green
    circular orbit centred on As⁺, spanning about four lattice spacings, labelled
    多出的第 5 個電子（軌道半徑約 2.4 nm）.
  Bottom: a band diagram (style-guide conventions) —
    solid grey-blue valence band, white conduction band, gap labelled 1.1 eV;
    a row of short green dashes about 0.05 eV below the conduction band labelled
    施子能階（約 0.05 eV）; small upward arrows from the donor level to the
    conduction band, which holds several black electrons ●;
    the red dashed E_F drawn close to the conduction band, labelled E_F 往上移.
  Side mini-figure (in the spirit of Fig. 10.27): a crystal connected to a battery,
    the extra electrons moving toward the positive terminal.

RIGHT half, pill label p 型：摻鎵 (Ga):
  Top: the same silicon lattice with the central site replaced by a purple
    (#7B1FA2) circle labelled Ga⁻; one of its four bonds drawn with only one
    electron and a small open circle next to it labelled 電洞（少一個電子）.
  Bottom: a band diagram —
    a row of short purple dashes a few tens of meV above the valence band labelled
    受子能階; small upward arrows from the top of the valence band to the acceptor
    level, leaving several open circles ○ at the top of the valence band;
    the red dashed E_F drawn close to the valence band, labelled E_F 往下移.
  Side mini-figure (in the spirit of Fig. 10.28): three time-snapshots of the
    lattice in which the vacancy moves one site at a time toward the negative
    terminal, labelled 鄰近電子遞補空位 → 看起來是電洞朝負極移動.

LOWER MIDDLE (full width), pill label 費米能量由電子的數目決定:
A side view of classroom rows, students filling from the front row backward:
  left: 20 人 → 坐到第 3 排, E_F marked at row 3;
  middle: 再進來 20 人 → 坐到第 8 排, E_F moved up, labelled n 型：電子變多;
  right: 離開 10 人 → 退到第 2 排, E_F moved down, labelled p 型：電子變少（電洞變多）.

Top-right legend "圖例":
  灰藍實心 — 價電帶（填滿）
  白底細框 — 傳導帶
  綠色短虛線 — 施子能階
  紫色短虛線 — 受子能階
  紅色虛線 — 費米能量 E_F
  ● 電子　○ 電洞

Bottom pastel boxes (four):
1. light green: E_d = (m*/m)(E₁/κ²) ≈ −0.026 eV — 類氫施子：κ = 11.7、m* ≈ 0.26m
2. light blue: a_d = κ(m/m*)a₀ ≈ 2.4 nm — 軌道內包含約 2800 個矽原子
3. light yellow: 摻雜 10¹⁵–10¹⁸ cm⁻³ ≪ 矽原子 5×10²² cm⁻³ — 痕量雜質卻主宰電性
4. light purple: n 型 E_F 靠傳導帶，p 型 E_F 靠價電帶 — 組成元件時最重要的資訊
```
