# Conductor_Insulator_Semiconductor_Bands.png

**對應章節：** 10.6 固體的能帶理論
**插入位置：**「導體、絕緣體與半導體」三點列表與「溫度升高時」的比較段落之後、「補充例題 10.B」之前
**課本對應：** 圖 10.22、圖 10.23、圖 10.24、圖 10.25

> 產圖前請先貼上 `00_STYLE_GUIDE.md` 的風格區塊。

---

## 中文提示詞

```
【模型與符號】以本質、近熱平衡材料作能帶示意；有限溫度化學勢約在能隙中央，但不必恰在正中央。態數若含自旋須明寫。

請畫一張教學用資訊圖表，主題是「看最上面的能帶有沒有填滿：導體、絕緣體與半導體」。

標題列文字：10.6  導體、絕緣體與半導體的能帶 (Bands of Conductors, Insulators and Semiconductors)

導言框文字：
用包立不相容原理把電子一個一個填進能帶，然後只問一件事：
最上面那個有電子的能帶，填滿了沒有？沒填滿是導體；
填滿而且能隙大是絕緣體；填滿但能隙小是半導體。

主體左半（約 45% 寬）｜pill 標籤：碳與矽的能帶從哪裡來（數能態）
畫一張座標圖，橫軸「核間距」（向右增大），縱軸「能量」：
  右側兩條水平細線：上方標「2p（碳）/ 3p（矽）：6N 個能態」，
    下方標「2s（碳）/ 3s（矽）：2N 個能態」。
  往左，兩條線各自展開成灰藍色的帶，並在中間交疊成一個大的帶，標「8N 個能態」。
  再往左，這個大帶分裂成上下兩支：
    上支（白底細框）標「傳導帶：4N 個能態（空）」，
    下支（灰藍實心）標「價電帶：4N 個能態（被 4N 個價電子填滿）」。
  畫兩條垂直虛線：
    靠左的一條標「碳（鑽石）」，在它與兩帶交會處用大括號標「E_g ≈ 6 eV」；
    靠右的一條標「矽」，大括號標「E_g ≈ 1.1 eV」。
  小字：「碳原子較小 → 平衡間距較小 → 能隙較大」。

主體右半（約 55% 寬）｜pill 標籤：三種固體的能帶圖
畫三個並排的能帶柱（遵守風格指南的能帶畫法），每柱下方標名稱：

  (1) 金屬：固體鈉
      下方三條細線標 1s、2s、2p（內層，已填滿）。
      上方 3s 能帶畫成一個長方形，下半灰藍實心、上半白色，
      分界處一條紅色虛線標「E_F」，旁註「3s 只填一半：2N 個能態、N 個電子」。
      一支小箭頭表示 E_F 附近的電子輕易跳進上方空態，標「一點電壓就能導電」。

  (2) 絕緣體：鑽石
      下方灰藍實心的價電帶，上方白色的傳導帶，中間大空白用大括號標「6 eV」。
      紅色虛線 E_F 畫在能隙內，標「本質材料，低溫極限示意」；0 K 在能隙內的位置不由佔據唯一決定。
      旁邊一個小插圖：塞滿車子的高速公路，標「完全塞車：法拉利也跑不快」。

  (3) 半導體：矽
      同樣的結構，但能隙只有「1.1 eV」，畫得明顯較窄。
      傳導帶底部有 2–3 個黑色實心小圓點（電子），價電帶頂部有對應的 2–3 個空心小圓圈（電洞），
      一支彎曲的橘色（#EF6C00）箭頭從價電帶指向傳導帶，標「熱激發」。
      紅色虛線 E_F 畫在能隙中央附近（本質半導體近似）。

  三柱下方一行比較：「溫度上升：金屬電阻 ↑（散射變多）；半導體電阻 ↓（載子以指數增加）」。

右上角「圖例」方框：
  灰藍實心 — 被電子填滿的能態
  白底細框 — 空的能態
  紅色虛線 — 費米能量 E_F
  ● — 電子　○ — 電洞

最下方一排粉彩公式盒（四個）：
1. 淺藍盒：鈉 3s：2N 能態 / N 電子 = 半滿，說明「導體」
2. 淺紫盒：碳 2s+2p：8N → 4N + 4N，4N 個價電子恰好填滿下方，說明「絕緣體或半導體」
3. 淺綠盒：k_B T ≈ 0.026 eV（室溫），說明「遠小於 6 eV，卻足以讓少數電子跨過 1.1 eV」
4. 淺紅盒：f ≈ e^(−E_g/2k_BT)：矽 6×10⁻¹⁰、鑽石 4×10⁻⁵¹，說明「補充例題 10.B」
```

## English Prompt

```
MODEL AND NOTATION: Illustrate intrinsic materials near thermal equilibrium. Finite-T chemical potential is approximately, not necessarily exactly, midgap. State counts must specify spin inclusion.

Draw an educational infographic titled "Is the top band full? Conductors,
insulators and semiconductors". ALL labels in TRADITIONAL CHINESE.

Title bar: 10.6  導體、絕緣體與半導體的能帶 (Bands of Conductors, Insulators and Semiconductors)

Intro box (Traditional Chinese):
用包立不相容原理把電子一個一個填進能帶，然後只問一件事：
最上面那個有電子的能帶，填滿了沒有？沒填滿是導體；
填滿而且能隙大是絕緣體；填滿但能隙小是半導體。

LEFT ~45%, pill label 碳與矽的能帶從哪裡來（數能態）:
A plot, x-axis 核間距 (increasing to the right), y-axis 能量:
  On the right two thin horizontal lines: upper 2p（碳）/ 3p（矽）：6N 個能態,
    lower 2s（碳）/ 3s（矽）：2N 個能態.
  Toward the left each broadens into a grey-blue band and the two merge into one
    large band labelled 8N 個能態.
  Further left this large band splits into two branches:
    upper branch (white with thin outline) 傳導帶：4N 個能態（空）,
    lower branch (solid grey-blue) 價電帶：4N 個能態（被 4N 個價電子填滿）.
  Two vertical dashed lines:
    the left one labelled 碳（鑽石）, with a brace across the gap E_g ≈ 6 eV;
    the right one labelled 矽, with a brace E_g ≈ 1.1 eV.
  Small note: 碳原子較小 → 平衡間距較小 → 能隙較大.

RIGHT ~55%, pill label 三種固體的能帶圖:
Three side-by-side band columns following the style guide's band conventions,
each named underneath:

  (1) 金屬：固體鈉
      Three thin lines at the bottom labelled 1s, 2s, 2p (core, filled).
      The 3s band as a rectangle, lower half solid grey-blue, upper half white,
      with a red dashed line E_F at the boundary; note 3s 只填一半：2N 個能態、N 個電子.
      A small arrow showing an electron near E_F hopping into the empty states
      above, labelled 一點電壓就能導電.

  (2) 絕緣體：鑽石
      Solid grey-blue valence band, white conduction band, a wide gap braced 6 eV.
      Red dashed E_F inside the gap, labelled 本質材料，低溫極限示意; its precise in-gap location at 0 K is not fixed by occupations alone.
      Small inset: a completely jammed highway, labelled 完全塞車：法拉利也跑不快.

  (3) 半導體：矽
      The same structure but with a visibly narrower gap labelled 1.1 eV.
      2–3 solid black dots (electrons) at the bottom of the conduction band and
      2–3 matching open circles (holes) at the top of the valence band; a curved
      orange (#EF6C00) arrow from valence to conduction band labelled 熱激發.
      Red dashed E_F near mid-gap (intrinsic approximation).

  Comparison line under the three columns:
  溫度上升：金屬電阻 ↑（散射變多）；半導體電阻 ↓（載子以指數增加）.

Top-right legend "圖例":
  灰藍實心 — 被電子填滿的能態
  白底細框 — 空的能態
  紅色虛線 — 費米能量 E_F
  ● — 電子　○ — 電洞

Bottom pastel boxes (four):
1. light blue: 鈉 3s：2N 能態 / N 電子 = 半滿 — 導體
2. light purple: 碳 2s+2p：8N → 4N + 4N，4N 個價電子恰好填滿下方 — 絕緣體或半導體
3. light green: k_B T ≈ 0.026 eV（室溫） — 遠小於 6 eV，卻足以讓少數電子跨過 1.1 eV
4. light red: f ≈ e^(−E_g/2k_BT)：矽 6×10⁻¹⁰、鑽石 4×10⁻⁵¹ — 補充例題 10.B
```
