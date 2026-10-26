# Vibration_Rotation_Levels.png

**對應章節：** 8.7 振動能階
**插入位置：**【進階探討：振動–轉動光譜】末尾（$(8.20)$ 與 CO 數字之後）、「複雜分子的振動模式與溫室效應」之前
**課本對應：** 圖 8.20 ＋ 課本 8.7 節後半的振動–轉動光譜

> 產圖前請先貼上 `00_STYLE_GUIDE.md` 的風格區塊。

---

## 中文提示詞

```
【模型與符號】採諧振子與剛性轉子近似；Δv=±1 限線性偶極近似。P、R 支圖以 CO 的 Σ↔Σ 振轉躍遷為例，不宣稱所有分子都無 Q 支。

請畫一張教學用資訊圖表，主題是「振動能階上疊著轉動能階：振動–轉動光譜的 P 支與 R 支」。

標題列文字：8.7  振動–轉動能階與光譜 (Vibration–Rotation Levels and Spectrum)

導言框文字：
振動能階的間距（~0.1 eV）比轉動能階（~10⁻³ eV）大約兩個數量級，
所以每個振動能階上都疊著一整排緊密的轉動能階。
吸收紅外光時 Δυ = +1 與 ΔJ = ±1 必須同時成立，光譜線在 ν₀ 兩側等間距排開，正中央反而沒有線。

主體左半（約 45% 寬）｜pill 標籤：位能井中的能階（圖 8.20）
  座標圖：縱軸 U，橫軸 R。
  一條灰色粗的真實分子位能曲線（左陡、右緩、右端趨於水平）。
  井內畫約 12 條綠色（#2E7D32）水平振動能階線，每條線只畫在曲線左右兩壁之間；
    **越往上間距越小**，最上面幾條擠在一起、逼近右端水平線（解離極限）。
  在下方三條振動能階上，各畫一小簇很密的橘色（#EF6C00）短線，代表轉動能階，
    用放大框拉出來並標「轉動能階」；另外用指引線標「振動能階」。

主體右半（約 55% 寬）｜pill 標籤：υ = 0 → 1 的吸收與 P、R 支
  上方：兩組能階梯。
    下組標 υ = 0，內含 J = 0, 1, 2, 3, 4 五條橘色細線（間距由下往上逐漸變寬）。
    上組標 υ = 1，同樣內含 J = 0, 1, 2, 3, 4 五條細線。
    兩組之間的大間距用綠色雙箭頭標 hν₀。
    畫出向上的吸收箭頭：
      藍色（#1565C0）箭頭：ΔJ = +1，即 J → J+1（0→1、1→2、2→3、3→4），標「R 支」；
      紅色（#C62828）箭頭：ΔJ = −1，即 J → J−1（1→0、2→1、3→2、4→3），標「P 支」。
      J → J（ΔJ = 0）的位置畫一支灰色虛線箭頭並打叉，標「禁止」。
  下方：一條水平頻率軸 ν，中心標 ν₀（畫一條灰色虛線但**不畫譜線**，標「沒有線：ΔJ = 0 禁止」）。
    ν₀ 右側四條藍色等間距譜線，標 ν₀ + 1, 2, 3, 4 × ħ/(2πI)（R 支）；
    ν₀ 左側四條紅色等間距譜線，標 ν₀ − 1, 2, 3, 4 × ħ/(2πI)（P 支）。
    中央的空隙寬度是相鄰間距的兩倍，用雙箭頭標「2ħ/(2πI)」。

右下角小卡｜pill 標籤：CO 的數字
  ν₀ = 6.42 × 10¹³ Hz（λ ≈ 4.7 μm）
  ħ/(2πI) = 1.15 × 10¹¹ Hz，只有 ν₀ 的約 1/560
  → 低解析度下像一條線，高解析度下才展開成一排細線。

右上角「圖例」方框：
  綠色 — 振動能階
  橘色 — 轉動能階
  藍色 — R 支（ΔJ = +1）
  紅色 — P 支（ΔJ = −1）

最下方一排粉彩公式盒（三個）：
1. 淺綠盒：E_{υ,J} = (υ + ½)ħ√(k/m′) + J(J+1)ħ²/2I　(8.19)，說明「振動 + 轉動」
2. 淺藍盒：ν = ν₀ ± n ħ/(2πI)，n = 1, 2, 3, …　(8.20)，說明「P 支與 R 支，ν₀ 處沒有線」
3. 淺黃盒：越往上振動能階越密，說明「真實位能比拋物線平緩，拋物線近似只在谷底成立」
```

## English Prompt

```
MODEL AND NOTATION: Use harmonic-oscillator and rigid-rotor approximations; Δv=±1 assumes a linear dipole expansion. P/R branches illustrate CO Σ↔Σ rovibrational transitions, not a universal absence of Q branches.

Draw an educational infographic titled "Rotational levels ride on vibrational levels: the P and
R branches of a vibration–rotation spectrum". ALL labels in TRADITIONAL CHINESE.

Title bar: 8.7  振動–轉動能階與光譜 (Vibration–Rotation Levels and Spectrum)

Intro box (Traditional Chinese):
振動能階的間距（~0.1 eV）比轉動能階（~10⁻³ eV）大約兩個數量級，
所以每個振動能階上都疊著一整排緊密的轉動能階。
吸收紅外光時 Δυ = +1 與 ΔJ = ±1 必須同時成立，光譜線在 ν₀ 兩側等間距排開，正中央反而沒有線。

LEFT ~45%, pill label 位能井中的能階（圖 8.20）:
  Plot: vertical axis U, horizontal axis R.
  A thick grey true molecular potential (steep on the left, gentle on the right, flattening
  at the far right).
  About 12 green (#2E7D32) horizontal vibrational levels inside the well, each drawn only
  between the two walls; the spacing SHRINKS upward, the top few crowding toward the
  flat dissociation limit.
  On the lowest three vibrational levels, a tiny dense cluster of orange (#EF6C00) short
  lines representing rotational levels, pulled out in a zoom box labelled 轉動能階; a
  leader line labels 振動能階.

RIGHT ~55%, pill label υ = 0 → 1 的吸收與 P、R 支:
  Upper part: two ladders.
    Lower ladder labelled υ = 0 with five thin orange lines J = 0, 1, 2, 3, 4 (spacing
    widening upward). Upper ladder labelled υ = 1 with the same five lines J = 0…4.
    The big gap between the ladders marked by a green double arrow hν₀.
    Upward absorption arrows:
      blue (#1565C0): ΔJ = +1, J → J+1 (0→1, 1→2, 2→3, 3→4), labelled R 支;
      red (#C62828): ΔJ = −1, J → J−1 (1→0, 2→1, 3→2, 4→3), labelled P 支.
      A grey dashed arrow for J → J (ΔJ = 0) with a cross, labelled 禁止.
  Lower part: a horizontal frequency axis ν with ν₀ at the centre (grey dashed marker but
    NO spectral line, labelled 沒有線：ΔJ = 0 禁止).
    Four equally spaced blue lines to the right labelled ν₀ + 1, 2, 3, 4 × ħ/(2πI) (R 支);
    four equally spaced red lines to the left labelled ν₀ − 1, 2, 3, 4 × ħ/(2πI) (P 支).
    The central gap is twice the neighbour spacing, marked 2ħ/(2πI).

Bottom-right small card, pill label CO 的數字:
  ν₀ = 6.42 × 10¹³ Hz（λ ≈ 4.7 μm）
  ħ/(2πI) = 1.15 × 10¹¹ Hz，只有 ν₀ 的約 1/560
  → 低解析度下像一條線，高解析度下才展開成一排細線。

Top-right legend "圖例":
  綠色 — 振動能階
  橘色 — 轉動能階
  藍色 — R 支（ΔJ = +1）
  紅色 — P 支（ΔJ = −1）

Bottom pastel boxes (three):
1. light green: E_{υ,J} = (υ + ½)ħ√(k/m′) + J(J+1)ħ²/2I  (8.19) — 振動 + 轉動
2. light blue: ν = ν₀ ± n ħ/(2πI)，n = 1, 2, 3, …  (8.20) — P 支與 R 支，ν₀ 處沒有線
3. light yellow: 越往上振動能階越密 — 真實位能比拋物線平緩，拋物線近似只在谷底成立
```
