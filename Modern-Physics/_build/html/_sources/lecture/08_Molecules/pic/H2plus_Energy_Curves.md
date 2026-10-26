# H2plus_Energy_Curves.png

**對應章節：** 8.3 H₂⁺ 分子離子
**插入位置：**「推導：兩個極限」之後、「讀圖 8.7」之前
**課本對應：** 圖 8.7

> 產圖前請先貼上 `00_STYLE_GUIDE.md` 的風格區塊。

---

## 中文提示詞

```
【模型與符號】採 Born–Oppenheimer 近似固定兩核，R 為核間距；電子能與包含核間斥力的總能分開標示，基態能量曲線井深不含振動零點修正。

請畫一張教學用資訊圖表，主題是「H₂⁺ 的能量曲線：對稱態有谷、反對稱態沒有」。

標題列文字：8.3  H₂⁺ 的能量曲線 (Energy Curves of the H₂⁺ Molecular Ion)

導言框文字：
總能量 = 電子能量 + 質子位能。兩端由極限決定：R → ∞ 時都是 −13.6 eV（一顆氫原子），
R → 0 時對稱態變成 He⁺ 的 1s（−54.4 eV）、反對稱態變成 He⁺ 的 2p（−13.6 eV）。
只有對稱態的總能量在 0.106 nm 處低於 −13.6 eV，形成 2.65 eV 的鍵。

主體左半（約 65% 寬）：能量曲線圖（重繪圖 8.7）
  橫軸：原子核間距 R（nm），刻度 0、0.1、0.2、0.3、0.4。
  縱軸：能量（eV），範圍約 −55 到 +30，刻度每 10 eV 一格，並特別標出 −13.6 與 −16.3。
  五條曲線（同一物理量全圖同色）：
  1. U_p 質子位能（黑色粗線）：U_p = 1.44/R(nm) eV，R → 0 時衝向 +∞；
     參考點：R = 0.1 nm 約 14 eV、R = 0.2 nm 約 7 eV、R = 0.4 nm 約 3.6 eV。
  2. E_S 對稱態電子能量（綠色 #2E7D32 細線）：R = 0 時 −54.4 eV，單調上升，
     R = 0.106 nm 時約 −30 eV，R 大時趨近 −13.6 eV。
  3. E_A 反對稱態電子能量（紅色 #C62828 細線）：R = 0 時 −13.6 eV，往右先下降，
     在約 0.1–0.2 nm 有一個約 −19 到 −20 eV 的淺谷，之後緩慢回升趨近 −13.6 eV。
  4. E_S^total 對稱態總能量（綠色粗線）：R 小時很高，向右下降，在 R = 0.106 nm 有極小值
     −16.3 eV，之後緩慢上升趨近 −13.6 eV。參考點：0.05 nm 約 −12 eV、0.08 nm 約 −16 eV、
     0.15 nm 約 −15.8 eV、0.2 nm 約 −15 eV、0.3 nm 約 −14 eV。
  5. E_A^total 反對稱態總能量（紅色粗線）：從左上方單調下降，由上方趨近 −13.6 eV，
     **沒有任何極小值、處處高於 −13.6 eV**。
  兩條水平虛線：−13.6 eV（標「孤立氫原子的總能量」）與 −16.3 eV。
  一條垂直虛線：R = 1.06 × 10⁻¹⁰ m（標在曲線谷底上方）。
  在兩條水平虛線之間畫一支雙箭頭，標「鍵結能 = 2.65 eV」。
  左端 R = 0 處標兩個點：E_S 的 −54.4 eV（標「He⁺ 1s」）與 E_A 的 −13.6 eV（標「He⁺ 2p」）。

主體右半（約 35% 寬）：三個上下堆疊的說明卡。

卡 1｜pill 標籤：兩個極限
  R → ∞：E_e → −13.6 eV，U_p → 0
  R → 0：E_S → Z²E₁ = 4 × (−13.6) = −54.4 eV
          E_A → Z²E₁/2² = −13.6 eV
          U_p → +∞

卡 2｜pill 標籤：數字檢查（R₀ = 0.106 nm）
  U_p(R₀) = 1.44/0.106 ≈ 13.6 eV
  E_S(R₀) = −16.3 − 13.6 ≈ −29.9 eV
  結論：共享讓電子能量降了約 16 eV，質子互斥吃掉 13.6 eV，淨賺 2.65 eV。

卡 3｜pill 標籤：鍵結能不是 16.3 eV
  鍵結能 = E(∞) − E(R₀) = (−13.6) − (−16.3) ≈ 2.65 eV
  是兩條虛線的差，不是谷底的絕對值。

右上角「圖例」方框：
  黑色粗線 — U_p 質子位能
  綠色細線 — E_S 電子能量（對稱態）
  綠色粗線 — E_S^total = E_S + U_p
  紅色細線 — E_A 電子能量（反對稱態）
  紅色粗線 — E_A^total = E_A + U_p

最下方一排粉彩公式盒（三個）：
1. 淺藍盒：U_p = e²/(4πε₀R)　(8.1)，說明「兩質子的庫侖排斥」
2. 淺綠盒：E^total(R) = E_e(R) + U_p(R)，說明「原子核固定近似：先固定 R 解電子」
3. 淺紅盒：E_A^total > −13.6 eV 處處成立，說明「反對稱態不會形成鍵結」
```

## English Prompt

```
MODEL AND NOTATION: Fix nuclei at separation R in the Born–Oppenheimer approximation. Distinguish electronic energy from total energy including nuclear repulsion; the well depth excludes vibrational zero-point correction.

Draw an educational infographic titled "Energy curves of H₂⁺: the symmetric state has a
well, the antisymmetric state does not". ALL labels in TRADITIONAL CHINESE.

Title bar: 8.3  H₂⁺ 的能量曲線 (Energy Curves of the H₂⁺ Molecular Ion)

Intro box (Traditional Chinese):
總能量 = 電子能量 + 質子位能。兩端由極限決定：R → ∞ 時都是 −13.6 eV（一顆氫原子），
R → 0 時對稱態變成 He⁺ 的 1s（−54.4 eV）、反對稱態變成 He⁺ 的 2p（−13.6 eV）。
只有對稱態的總能量在 0.106 nm 處低於 −13.6 eV，形成 2.65 eV 的鍵。

LEFT ~65%: the energy-curve plot (a redraw of textbook Fig. 8.7).
  Horizontal axis: 原子核間距 R (nm), ticks 0, 0.1, 0.2, 0.3, 0.4.
  Vertical axis: 能量 (eV), range about −55 to +30, ticks every 10 eV, with −13.6 and
  −16.3 explicitly marked.
  Five curves (each quantity keeps one colour):
  1. U_p 質子位能 (thick black): U_p = 1.44/R(nm) eV, shooting to +∞ as R → 0;
     reference points R = 0.1 nm ≈ 14 eV, 0.2 nm ≈ 7 eV, 0.4 nm ≈ 3.6 eV.
  2. E_S symmetric electronic energy (thin green #2E7D32): −54.4 eV at R = 0, rising
     monotonically, about −30 eV at R = 0.106 nm, approaching −13.6 eV at large R.
  3. E_A antisymmetric electronic energy (thin red #C62828): −13.6 eV at R = 0, first
     dipping to a shallow trough of about −19 to −20 eV around 0.1–0.2 nm, then slowly
     returning toward −13.6 eV.
  4. E_S^total symmetric total energy (thick green): high at small R, falling to a
     MINIMUM of −16.3 eV at R = 0.106 nm, then rising slowly toward −13.6 eV.
     Reference points: 0.05 nm ≈ −12 eV, 0.08 nm ≈ −16 eV, 0.15 nm ≈ −15.8 eV,
     0.2 nm ≈ −15 eV, 0.3 nm ≈ −14 eV.
  5. E_A^total antisymmetric total energy (thick red): decreasing monotonically from the
     upper left and approaching −13.6 eV from ABOVE — NO minimum, everywhere above −13.6 eV.
  Two horizontal dashed lines at −13.6 eV (labelled 孤立氫原子的總能量) and −16.3 eV.
  One vertical dashed line at R = 1.06 × 10⁻¹⁰ m (label above the well bottom).
  A double arrow between the two horizontal dashed lines labelled 鍵結能 = 2.65 eV.
  At R = 0 mark two dots: E_S at −54.4 eV (labelled He⁺ 1s) and E_A at −13.6 eV (labelled He⁺ 2p).

RIGHT ~35%: three stacked cards.

Card 1 pill: 兩個極限
  R → ∞：E_e → −13.6 eV，U_p → 0
  R → 0：E_S → Z²E₁ = 4 × (−13.6) = −54.4 eV
          E_A → Z²E₁/2² = −13.6 eV
          U_p → +∞

Card 2 pill: 數字檢查（R₀ = 0.106 nm）
  U_p(R₀) = 1.44/0.106 ≈ 13.6 eV
  E_S(R₀) = −16.3 − 13.6 ≈ −29.9 eV
  conclusion: 共享讓電子能量降了約 16 eV，質子互斥吃掉 13.6 eV，淨賺 2.65 eV。

Card 3 pill: 鍵結能不是 16.3 eV
  鍵結能 = E(∞) − E(R₀) = (−13.6) − (−16.3) ≈ 2.65 eV
  是兩條虛線的差，不是谷底的絕對值。

Top-right legend "圖例":
  黑色粗線 — U_p 質子位能
  綠色細線 — E_S 電子能量（對稱態）
  綠色粗線 — E_S^total = E_S + U_p
  紅色細線 — E_A 電子能量（反對稱態）
  紅色粗線 — E_A^total = E_A + U_p

Bottom pastel boxes (three):
1. light blue: U_p = e²/(4πε₀R)  (8.1) — 兩質子的庫侖排斥
2. light green: E^total(R) = E_e(R) + U_p(R) — 原子核固定近似：先固定 R 解電子
3. light red: E_A^total > −13.6 eV 處處成立 — 反對稱態不會形成鍵結
```
