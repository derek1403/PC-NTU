# Fine_Structure_and_Anomalous_Zeeman.png

**對應章節：** 7.1 電子自旋
**插入位置：**「薛丁格方程式解釋不了的兩件事」兩段文字之後、「這兩個現象有一個共通點」之前
**課本對應：** 圖 7.1（並加入 H_α 精細結構的示意）

> 產圖前請先貼上 `00_STYLE_GUIDE.md` 的風格區塊。

---

## 中文提示詞

```
請畫一張教學用資訊圖表，主題是「薛丁格方程式解釋不了的兩個光譜現象」。

標題列文字：7.1  精細結構與異常塞曼效應 (Fine Structure and the Anomalous Zeeman Effect)

導言框文字：
第六章的三個量子數預測：H_α 是一條線、磁場中每條譜線分裂成等間距的三條。
高解析度的實驗卻看到：H_α 是兩條線，而許多譜線在磁場中分裂成四條、六條。
兩個現象都跟磁有關——暗示電子身上還有另一個磁矩來源。

主體左半（約 40% 寬）｜pill 標籤：謎題一：精細結構
畫兩條水平的「光譜底片」長條（深灰色底、譜線為白色細線，類似課本圖 7.1 的風格）：
  上方長條標「低解析度：理論預測」：中央一條白線，下方標 656.3 nm。
  下方長條標「高解析度：實際觀測」：同一位置附近有兩條非常靠近的白線，
    用雙箭頭標出間距「≈ 0.14 Å = 0.014 nm」。
  在兩條長條右側畫一個小型能階示意：n = 3 與 n = 2 兩條水平線，
    n = 2 那條在放大鏡框內被畫成兩條很接近的線（標「分裂量 ~10⁻⁵ eV」），
    兩支向下箭頭分別落到這兩條線上，對應下方的兩條譜線。
  底部小字（紅色）：第六章的 E_n = E₁/n² 只跟 n 有關，無法給出兩條線。

主體右半（約 60% 寬）｜pill 標籤：謎題二：異常塞曼效應（圖 7.1）
畫三組上下成對的光譜底片長條（每組上方標「沒有磁場」、下方標「施加磁場」），
每組上方都只有一條中央白線，下方顯示分裂後的白線，並以細斜線把上方的線連到下方各條線：
  第 1 組｜標「預期（正常塞曼效應）」：
    下方三條等間距白線，位置為 −1、0、+1（以 μ_B B 為單位），
    下方用中括號標「預期的分裂：3 條，間距 eB/4πm」。
  第 2 組｜標「實際：鈉 D₁ 線（589.6 nm）」：
    下方四條白線，位置為 −4/3、−2/3、+2/3、+4/3（以 μ_B B 為單位，中央沒有線）。
  第 3 組｜標「實際：鈉 D₂ 線（589.0 nm）」：
    下方六條白線，位置為 −5/3、−1、−1/3、+1/3、+1、+5/3（以 μ_B B 為單位）。
  三組的水平刻度必須一致（同一個 μ_B B 對應同樣的長度），讓讀者一眼看出間距不同。
  每組下方用紅字標出條數：「3 條」「4 條」「6 條」。

右上角「圖例」方框：
  白色細線 — 光譜底片上的譜線
  中括號 — 正常塞曼效應預期的分裂範圍
  紅色字 — 與第六章預測不符之處

最下方一排粉彩公式盒（三個）：
1. 淺藍盒：ν = ν₀ − Δm_l · eB/(4πm)，Δm_l = 0, ±1，說明「(6.43) 只預測三條等間距譜線」
2. 淺黃盒：ΔE_精細 ~ 10⁻⁵ eV ~ μ_B B（B ≈ 0.4 T），說明「精細結構的大小恰好是磁能的量級」
3. 淺紅盒：除了軌道磁矩 μ_L 之外還有別的磁矩，說明「→ 電子自旋（7.1）；異常塞曼效應在 7.8 節以 Landé g 因子解決」
```

## English Prompt

```
Draw an educational infographic titled "two spectral phenomena that
Schrödinger's three quantum numbers cannot explain". ALL labels in
TRADITIONAL CHINESE.

Title bar: 7.1  精細結構與異常塞曼效應 (Fine Structure and the Anomalous Zeeman Effect)

Intro box (Traditional Chinese):
第六章的三個量子數預測：H_α 是一條線、磁場中每條譜線分裂成等間距的三條。
高解析度的實驗卻看到：H_α 是兩條線，而許多譜線在磁場中分裂成四條、六條。
兩個現象都跟磁有關——暗示電子身上還有另一個磁矩來源。

LEFT ~40%, pill label 謎題一：精細結構:
Two horizontal "spectrogram strips" (dark-grey background, spectral lines as thin
WHITE vertical lines, in the style of textbook Fig. 7.1):
  upper strip labelled 低解析度：理論預測 — one central white line, tagged 656.3 nm.
  lower strip labelled 高解析度：實際觀測 — two very close white lines at the same
    place, with a double arrow marking the gap "≈ 0.14 Å = 0.014 nm".
  To the right, a small level sketch: horizontal lines n = 3 and n = 2; inside a
    magnifier frame the n = 2 line is drawn as two very close lines labelled
    分裂量 ~10⁻⁵ eV; two downward arrows land on these two lines, matching the
    two spectral lines.
  small red caption at the bottom: 第六章的 E_n = E₁/n² 只跟 n 有關，無法給出兩條線。

RIGHT ~60%, pill label 謎題二：異常塞曼效應（圖 7.1）:
Three pairs of spectrogram strips (top strip of each pair labelled 沒有磁場,
bottom strip labelled 施加磁場). Each top strip has a single central white
line; each bottom strip shows the split lines, with thin slanted lines
connecting the top line to every bottom line:
  Pair 1, labelled 預期（正常塞曼效應）:
    three equally spaced lines at −1, 0, +1 (in units of μ_B B);
    a bracket below labelled 預期的分裂：3 條，間距 eB/4πm.
  Pair 2, labelled 實際：鈉 D₁ 線（589.6 nm）:
    four lines at −4/3, −2/3, +2/3, +4/3 (units of μ_B B; NO central line).
  Pair 3, labelled 實際：鈉 D₂ 線（589.0 nm）:
    six lines at −5/3, −1, −1/3, +1/3, +1, +5/3 (units of μ_B B).
  The horizontal scale must be IDENTICAL in all three pairs (the same μ_B B is the
  same length) so the different spacings are obvious at a glance.
  Under each pair, in red: 3 條 / 4 條 / 6 條.

Top-right legend "圖例":
  白色細線 — 光譜底片上的譜線
  中括號 — 正常塞曼效應預期的分裂範圍
  紅色字 — 與第六章預測不符之處

Bottom pastel formula boxes (three):
1. light blue: ν = ν₀ − Δm_l · eB/(4πm), Δm_l = 0, ±1 — (6.43) 只預測三條等間距譜線
2. light yellow: ΔE_精細 ~ 10⁻⁵ eV ~ μ_B B（B ≈ 0.4 T）— 精細結構的大小恰好是磁能的量級
3. light red: 除了軌道磁矩 μ_L 之外還有別的磁矩 — → 電子自旋（7.1）；異常塞曼效應在 7.8 節以 Landé g 因子解決
```
