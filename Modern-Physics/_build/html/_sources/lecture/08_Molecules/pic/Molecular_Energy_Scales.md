# Molecular_Energy_Scales.png

**對應章節：** 8.6 轉動能階
**插入位置：** 室溫熱能 $kT$ 的說明之後、「這一節先處理能量最小的轉動」之前
**課本對應：** 投影片「分子的能階可分成三類」＋ 圖 8.20 的層次概念

> 產圖前請先貼上 `00_STYLE_GUIDE.md` 的風格區塊。

---

## 中文提示詞

```
請畫一張教學用資訊圖表，主題是「分子的三種能階：電子、振動、轉動，差了好幾個數量級」。

標題列文字：8.6  分子能階的三個尺度 (Three Energy Scales of a Molecule)

導言框文字：
分子比原子多了振動與轉動兩種自由度。三種能態的能量差了約兩個數量級，
光譜剛好落在可見／紫外、紅外、微波三個波段。
拿來比較的基準是室溫熱能 kT ≈ 0.026 eV：比它小很多的能階室溫下大多被激發，比它大的大多待在基態。

主體左半（約 55% 寬）｜pill 標籤：層層嵌套的能階圖
  畫一個三層放大的能階圖（用放大鏡或虛線框連接各層）：
  第一層（最左，縱軸跨約 5 eV）：兩條藍色（#1565C0）粗水平線，標「電子基態」「電子受激態」，
    中間雙箭頭標「~ 數 eV」。
  第二層（中間，放大電子基態附近，縱軸跨約 1 eV）：等間距的綠色（#2E7D32）水平線，
    標 υ = 0, 1, 2, 3，間距雙箭頭標「~ 0.1 eV」。
  第三層（最右，放大 υ = 0 附近，縱軸跨約 0.01 eV）：橘色（#EF6C00）細線，
    標 J = 0, 1, 2, 3, 4，間距由下往上逐漸變寬，間距雙箭頭標「~ 10⁻³ eV」。
  在三層旁邊各畫一條紅色（#C62828）水平虛線代表 kT = 0.026 eV 的高度
    （在第一、二層中它很低；在第三層中它遠高於所有畫出的轉動能階，直接衝出圖框，標「kT 在這裡之上」）。

主體右半（約 45% 寬）：上下兩部分。

上｜pill 標籤：對應的電磁波段
  一條水平的電磁波譜色帶，由左（長波長）到右（短波長）：
    微波（標 0.1 mm ~ 1 cm，橘色框起來，對應「轉動」）
    紅外線（標 1 μm ~ 0.1 mm，綠色框起來，對應「振動」）
    可見光／紫外線（標 0.1 μm ~ 1 μm，藍色框起來，對應「電子」）
  可見光段畫出彩虹色。

下｜pill 標籤：CO 的實際數字
  三列小表：
    轉動 J = 0→1：4.75 × 10⁻⁴ eV（波長 2.6 mm）→ ≪ kT → 室溫下大多在受激態
    振動 υ = 0→1：0.266 eV（波長 4.7 μm）→ ≈ 10 kT → 室溫下幾乎都在 υ = 0
    電子：數 eV → ≫ kT → 室溫下都在基態

右上角「圖例」方框：
  藍色 — 電子能態
  綠色 — 振動能態
  橘色 — 轉動能態
  紅色虛線 — 室溫熱能 kT ≈ 0.026 eV

最下方一排粉彩公式盒（三個）：
1. 淺紅盒：kT(300 K) ≈ 2.6 × 10⁻² eV ≈ 26 meV，說明「請背起來：所有能量差都拿來跟它比」
2. 淺黃盒：E_J = J(J+1)ħ²/2I，說明「轉動，8.6」
3. 淺綠盒：E_υ = (υ + ½)hν₀，說明「振動，8.7」
```

## English Prompt

```
Draw an educational infographic titled "The three kinds of molecular energy levels:
electronic, vibrational, rotational — orders of magnitude apart". ALL labels in
TRADITIONAL CHINESE.

Title bar: 8.6  分子能階的三個尺度 (Three Energy Scales of a Molecule)

Intro box (Traditional Chinese):
分子比原子多了振動與轉動兩種自由度。三種能態的能量差了約兩個數量級，
光譜剛好落在可見／紫外、紅外、微波三個波段。
拿來比較的基準是室溫熱能 kT ≈ 0.026 eV：比它小很多的能階室溫下大多被激發，比它大的大多待在基態。

LEFT ~55%, pill label 層層嵌套的能階圖:
  A three-level zoom diagram (connected by magnifier glyphs or dashed zoom boxes):
  Level 1 (far left, vertical span ~5 eV): two thick blue (#1565C0) horizontal lines
    labelled 電子基態 and 電子受激態, double arrow between them ~ 數 eV.
  Level 2 (middle, zoom near the electronic ground state, span ~1 eV): equally spaced
    green (#2E7D32) lines labelled υ = 0, 1, 2, 3, spacing arrow ~ 0.1 eV.
  Level 3 (far right, zoom near υ = 0, span ~0.01 eV): thin orange (#EF6C00) lines
    labelled J = 0, 1, 2, 3, 4, spacing widening upward, spacing arrow ~ 10⁻³ eV.
  Beside each level draw a red (#C62828) horizontal dashed line at the height kT = 0.026 eV
    (low in levels 1 and 2; in level 3 it lies far above all drawn rotational lines and runs
    off the top of the frame, labelled kT 在這裡之上).

RIGHT ~45%: two parts.

Upper, pill label 對應的電磁波段:
  A horizontal electromagnetic-spectrum band, long wavelength on the left:
    微波 (0.1 mm ~ 1 cm, boxed in orange, tied to 轉動)
    紅外線 (1 μm ~ 0.1 mm, boxed in green, tied to 振動)
    可見光／紫外線 (0.1 μm ~ 1 μm, boxed in blue, tied to 電子)
  Show rainbow colours in the visible part.

Lower, pill label CO 的實際數字:
  Three-row mini table:
    轉動 J = 0→1：4.75 × 10⁻⁴ eV（波長 2.6 mm）→ ≪ kT → 室溫下大多在受激態
    振動 υ = 0→1：0.266 eV（波長 4.7 μm）→ ≈ 10 kT → 室溫下幾乎都在 υ = 0
    電子：數 eV → ≫ kT → 室溫下都在基態

Top-right legend "圖例":
  藍色 — 電子能態
  綠色 — 振動能態
  橘色 — 轉動能態
  紅色虛線 — 室溫熱能 kT ≈ 0.026 eV

Bottom pastel boxes (three):
1. light red: kT(300 K) ≈ 2.6 × 10⁻² eV ≈ 26 meV — 請背起來：所有能量差都拿來跟它比
2. light yellow: E_J = J(J+1)ħ²/2I — 轉動，8.6
3. light green: E_υ = (υ + ½)hν₀ — 振動，8.7
```
