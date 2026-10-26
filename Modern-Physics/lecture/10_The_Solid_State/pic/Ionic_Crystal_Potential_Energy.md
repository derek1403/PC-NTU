# Ionic_Crystal_Potential_Energy.png

**對應章節：** 10.2 離子晶體
**插入位置：**「推導：總位能與平衡距離」標題正下方、$(10.3)$ 之前
**課本對應：** 圖 10.7（能量帳的階梯圖為例題 10.1 的自製輔助圖）

> 產圖前請先貼上 `00_STYLE_GUIDE.md` 的風格區塊。

---

## 中文提示詞

```
請畫一張教學用資訊圖表，主題是「離子晶體的位能曲線與氯化鈉的聚合能帳本」。

標題列文字：10.2  離子晶體的位能與聚合能 (Potential Energy and Cohesive Energy of Ionic Crystals)

導言框文字：
異性離子相吸，為什麼不會無限靠近？因為電子雲一重疊，包立不相容原理
就產生急遽上升的排斥。吸引與排斥相加形成一個位能谷，
谷底的位置是平衡距離 r₀，谷底的深度是 U₀。

主體左半（約 60% 寬）｜pill 標籤：位能對離子間距 r
畫一張座標圖，橫軸 r（單位 nm，標 0 到 1.0），縱軸 U（單位 eV，標約 −15 到 +10），
r 軸畫在 U = 0 的高度。
  藍色曲線（#1565C0）U_coulomb = −αe²/(4πε₀r)：從下方負無窮慢慢爬升趨近 0。
  橘色曲線（#EF6C00）U_repulsive = B/r⁹：r 大時幾乎貼著 0，
    只在 r < 0.25 nm 左右才陡峭升起。
  紫色粗曲線（#7B1FA2）U_total = 兩者之和：形成一個位能谷。
  在谷底畫垂直虛線到橫軸，標「r₀ = 0.281 nm」；
  畫水平虛線到縱軸，標「U₀ = −7.96 eV（每離子對）」。
  在谷底旁標一個小框：「dU/dr = 0 ⇒ B = αe² r₀ⁿ⁻¹/(4πε₀ n)」。
  在橘色曲線旁標「包立排斥：電子雲重疊」，在藍色曲線旁標「庫侖吸引（長程）」。

主體右半（約 40% 寬）｜pill 標籤：例題 10.1 的能量帳（每一離子對）
畫一張垂直的能量階梯圖，縱軸向上為能量增加：
  第 0 階（中間高度，標 0）：「Na 原子 + Cl 原子」
  往上一階（+1.53 eV）：「Na⁺ + Cl⁻（離子）」，
    旁邊用小字拆解：「游離能 +5.14 eV ＋ 電子親和力 −3.61 eV」，
    向上的紅色（#C62828）箭頭標「付出 +1.53 eV」。
  從離子階往下一大段（−7.96 eV）到最低階：「NaCl 晶體」，
    向下的綠色（#2E7D32）粗箭頭標「晶格放出 −7.96 eV」。
  右側用大括號標出從「原子」到「晶體」的淨變化：−6.43 eV（每離子對）。
  下方換算框：「每個原子：−3.98 + 0.77 = −3.21 eV；實驗值 −3.28 eV」。

右上角「圖例」方框：
  藍色曲線 — 庫侖位能 U_coulomb
  橘色曲線 — 包立排斥能 U_repulsive
  紫色曲線 — 總位能 U_total
  紅色箭頭 — 需要付出的能量
  綠色箭頭 — 放出的能量

最下方一排粉彩公式盒（三個）：
1. 淺紫盒：U_total = −αe²/(4πε₀r) + B/rⁿ　(10.3)，說明「吸引 + 包立排斥」
2. 淺藍盒：U₀ = −αe²/(4πε₀r₀)·(1 − 1/n)　(10.5)，說明「n ≈ 9，排斥只修正約 11%」
3. 淺紅盒：E_cohesive = −3.21 eV/原子，說明「離子→晶體放能，但原子→離子要先付能」
```

## English Prompt

```
Draw an educational infographic titled "The potential-energy curve of an ionic
crystal and the cohesive-energy bookkeeping of NaCl". ALL labels in TRADITIONAL CHINESE.

Title bar: 10.2  離子晶體的位能與聚合能 (Potential Energy and Cohesive Energy of Ionic Crystals)

Intro box (Traditional Chinese):
異性離子相吸，為什麼不會無限靠近？因為電子雲一重疊，包立不相容原理
就產生急遽上升的排斥。吸引與排斥相加形成一個位能谷，
谷底的位置是平衡距離 r₀，谷底的深度是 U₀。

LEFT ~60%, pill label 位能對離子間距 r:
A plot: x-axis r in nm (0 to 1.0), y-axis U in eV (about −15 to +10), the r-axis
drawn at U = 0.
  Blue curve (#1565C0) U_coulomb = −αe²/(4πε₀r): rises slowly from −∞ toward 0.
  Orange curve (#EF6C00) U_repulsive = B/r⁹: essentially zero at large r, rising
    steeply only below about 0.25 nm.
  Thick purple curve (#7B1FA2) U_total = their sum, forming a potential well.
  From the bottom of the well draw a vertical dashed line to the axis labelled
  r₀ = 0.281 nm and a horizontal dashed line to the U-axis labelled
  U₀ = −7.96 eV（每離子對）.
  Small box near the minimum: dU/dr = 0 ⇒ B = αe² r₀ⁿ⁻¹/(4πε₀ n).
  Label the orange curve 包立排斥：電子雲重疊 and the blue curve 庫侖吸引（長程）.

RIGHT ~40%, pill label 例題 10.1 的能量帳（每一離子對）:
A vertical energy ladder, energy increasing upward:
  level 0 (middle height, labelled 0): Na 原子 + Cl 原子
  one step up (+1.53 eV): Na⁺ + Cl⁻（離子）, with the breakdown in small text
    游離能 +5.14 eV ＋ 電子親和力 −3.61 eV, and an upward red (#C62828) arrow
    labelled 付出 +1.53 eV.
  a long drop (−7.96 eV) from the ion level to the lowest level NaCl 晶體,
    with a thick downward green (#2E7D32) arrow labelled 晶格放出 −7.96 eV.
  A brace on the right showing the net change from atoms to crystal:
    −6.43 eV（每離子對）.
  Conversion box below: 每個原子：−3.98 + 0.77 = −3.21 eV；實驗值 −3.28 eV.

Top-right legend "圖例":
  藍色曲線 — 庫侖位能 U_coulomb
  橘色曲線 — 包立排斥能 U_repulsive
  紫色曲線 — 總位能 U_total
  紅色箭頭 — 需要付出的能量
  綠色箭頭 — 放出的能量

Bottom pastel boxes (three):
1. light purple: U_total = −αe²/(4πε₀r) + B/rⁿ  (10.3) — 吸引 + 包立排斥
2. light blue: U₀ = −αe²/(4πε₀r₀)·(1 − 1/n)  (10.5) — n ≈ 9，排斥只修正約 11%
3. light red: E_cohesive = −3.21 eV/原子 — 離子→晶體放能，但原子→離子要先付能
```
