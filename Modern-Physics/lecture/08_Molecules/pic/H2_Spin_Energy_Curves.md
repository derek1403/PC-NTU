# H2_Spin_Energy_Curves.png

**對應章節：** 8.4 氫分子
**插入位置：**「推導：哪些組合是被允許的」的結論表格之後
**課本對應：** 圖 8.8

> 產圖前請先貼上 `00_STYLE_GUIDE.md` 的風格區塊。

---

## 中文提示詞

```
【模型與符號】空間與自旋部分相乘才是電子總態，總態必須反對稱；束縛與否須比較包含電子及核間作用的總能量。

請畫一張教學用資訊圖表，主題是「H₂：自旋決定軌道，軌道決定鍵結」。

標題列文字：8.4  氫分子與自旋 (The Hydrogen Molecule and Electron Spin)

導言框文字：
兩個電子的總波函數必須反對稱（包立不相容原理）。
自旋反平行（單重態）→ 軌道必須對稱 → 電子堆在兩核之間 → 鍵結；
自旋平行（三重態）→ 軌道必須反對稱 → 中間有節面 → 互相推開。

主體左半（約 60% 寬）｜pill 標籤：H + H 的能量曲線（圖 8.8）
  橫軸：原子核間距 R（nm），刻度 0、0.1、0.2、0.3、0.4。
  縱軸：能量（eV），範圍 −6 到 +8，零點標「兩顆分開的氫原子」。
  綠色曲線（#2E7D32）E_S：R 很小時陡升，在 R₀ = 0.074 nm 處有極小值約 −4.5 eV
    （谷底深度約 4.5 至 4.7 eV），之後平滑上升趨近 0；
    曲線旁標「H + H 自旋反平行」，並畫一對小箭頭 ↑↓。
  紅色曲線（#C62828）E_A：從左上方約 +8 eV 處單調下降，由上方趨近 0，沒有極小值；
    曲線旁標「H + H 自旋平行」，並畫一對小箭頭 ↑↑。
  谷底畫垂直虛線標 R₀ = 0.074 nm，谷底到零點之間的雙箭頭標「鍵結能 4.5 eV」。

主體右半（約 40% 寬）：兩個上下堆疊的說明卡。

卡 1｜pill 標籤：只有兩種組合被允許
  畫一個 2×2 的表格：列為「軌道對稱 ψ_S／軌道反對稱 ψ_A」，欄為「自旋反對稱 s_A（S=0）／自旋對稱 s_S（S=1）」。
    ψ_S s_A：綠色打勾，標「單重態，鍵結」
    ψ_A s_S：綠色打勾，標「三重態，不鍵結」
    ψ_S s_S：灰色打叉，標「總波函數對稱，不允許」
    ψ_A s_A：灰色打叉，標「總波函數對稱，不允許」
  表格下方一行：Ψ(2,1) = −Ψ(1,2)

卡 2｜pill 標籤：H₂⁺ 與 H₂ 對照
  兩欄小表：
    電子數：1 ／ 2
    鍵長 R₀：0.106 nm ／ 0.074 nm
    鍵結能：2.65 eV ／ 4.5 eV
  下方紅字：4.5 eV < 2 × 2.65 = 5.3 eV，因為兩個電子之間互相排斥。
  再下方小字：兩個電子當膠水黏得更緊 → 鍵長變短。

右下角小插圖｜pill 標籤：為什麼沒有 H₃？
  一個鍵結軌道方框裡放兩支反平行箭頭 ↑↓（已滿），
  第三支箭頭被擋在外面、被迫進入上方標「反鍵結軌道」的方框，旁註「削弱鍵結」。

右上角「圖例」方框：
  綠色 — 自旋反平行（單重態）：鍵結
  紅色 — 自旋平行（三重態）：不鍵結
  ↑↓ — 兩個電子的自旋方向

最下方一排粉彩公式盒（三個）：
1. 淺綠盒：Ψ(1,2) = ψ_S s_A，說明「自旋反平行：鍵結」
2. 淺紅盒：Ψ(1,2) = ψ_A s_S，說明「自旋平行：不鍵結」
3. 淺紫盒：s_A = (1/√2)[↑↓ − ↓↑]，說明「自旋本身能量很小，它靠對稱性規則決定電子在空間的分佈」
```

## English Prompt

```
MODEL AND NOTATION: The product of spatial and spin parts must be antisymmetric. Assess binding using full electronic and internuclear energies.

Draw an educational infographic titled "H₂: spin fixes the orbital, the orbital fixes the
bond". ALL labels in TRADITIONAL CHINESE.

Title bar: 8.4  氫分子與自旋 (The Hydrogen Molecule and Electron Spin)

Intro box (Traditional Chinese):
兩個電子的總波函數必須反對稱（包立不相容原理）。
自旋反平行（單重態）→ 軌道必須對稱 → 電子堆在兩核之間 → 鍵結；
自旋平行（三重態）→ 軌道必須反對稱 → 中間有節面 → 互相推開。

LEFT ~60%, pill label H + H 的能量曲線（圖 8.8）:
  Horizontal axis: 原子核間距 R (nm), ticks 0, 0.1, 0.2, 0.3, 0.4.
  Vertical axis: 能量 (eV), range −6 to +8; the zero is labelled 兩顆分開的氫原子.
  Green curve (#2E7D32) E_S: very steep at small R, a minimum of about −4.5 eV at
    R₀ = 0.074 nm (well depth about 4.5–4.7 eV), then rising smoothly toward 0.
    Tag: H + H 自旋反平行, with a small arrow pair ↑↓.
  Red curve (#C62828) E_A: starting near +8 eV at the upper left and decreasing
    monotonically toward 0 from ABOVE, with NO minimum. Tag: H + H 自旋平行, with ↑↑.
  A vertical dashed line at the well bottom labelled R₀ = 0.074 nm and a double arrow
  from the bottom to the zero line labelled 鍵結能 4.5 eV.

RIGHT ~40%: two stacked cards.

Card 1 pill: 只有兩種組合被允許
  A 2×2 table. Rows: 軌道對稱 ψ_S / 軌道反對稱 ψ_A. Columns: 自旋反對稱 s_A（S=0）/
  自旋對稱 s_S（S=1）.
    ψ_S s_A: green tick, 單重態，鍵結
    ψ_A s_S: green tick, 三重態，不鍵結
    ψ_S s_S: grey cross, 總波函數對稱，不允許
    ψ_A s_A: grey cross, 總波函數對稱，不允許
  Under the table: Ψ(2,1) = −Ψ(1,2)

Card 2 pill: H₂⁺ 與 H₂ 對照
  A two-column mini table:
    電子數：1 ／ 2
    鍵長 R₀：0.106 nm ／ 0.074 nm
    鍵結能：2.65 eV ／ 4.5 eV
  Red line below: 4.5 eV < 2 × 2.65 = 5.3 eV，因為兩個電子之間互相排斥。
  Small text: 兩個電子當膠水黏得更緊 → 鍵長變短。

Bottom-right inset, pill label 為什麼沒有 H₃？:
  A box labelled 鍵結軌道 holding two antiparallel arrows ↑↓ (full). A third arrow is
  blocked and forced into a higher box labelled 反鍵結軌道, with the note 削弱鍵結.

Top-right legend "圖例":
  綠色 — 自旋反平行（單重態）：鍵結
  紅色 — 自旋平行（三重態）：不鍵結
  ↑↓ — 兩個電子的自旋方向

Bottom pastel boxes (three):
1. light green: Ψ(1,2) = ψ_S s_A — 自旋反平行：鍵結
2. light red: Ψ(1,2) = ψ_A s_S — 自旋平行：不鍵結
3. light purple: s_A = (1/√2)[↑↓ − ↓↑] — 自旋本身能量很小，它靠對稱性規則決定電子在空間的分佈
```
