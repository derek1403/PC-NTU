# Spin_Orbit_Coupling.png

**對應章節：** 7.7 自旋—軌道耦合
**插入位置：**「假設與已知」之後、「推導：自旋在軌道磁場中的磁能」之前
**課本對應：** 圖 7.13（兩個參考座標系）＋ 圖 7.14（$2p$ 能階分裂成雙重態）

> 產圖前請先貼上 `00_STYLE_GUIDE.md` 的風格區塊。

---

## 中文提示詞

```
【模型與符號】以非相對論中心場及弱自旋—軌道耦合為模型；經典軌道磁場只說明量級與方向，不當成精確能級推導。

請畫一張教學用資訊圖表，主題是「沒有外加磁場，自旋為什麼還會感受到磁場——自旋—軌道耦合」。

標題列文字：7.7  自旋—軌道耦合 (Spin-Orbit Coupling)

導言框文字：
站在原子核上看，是電子繞著原子核轉；站在電子上看，是帶正電的原子核繞著電子轉。
繞行的正電荷就是一個電流迴路，在電子處產生磁場 B（與 L 同向）。
電子的自旋磁矩在這個「內部磁場」中有磁能 ±μ_B B，於是一個能階分裂成兩個。

主體左上（約 30% 寬）｜pill 標籤：(a) 原子核的座標系
  中央一個灰色大圓點標「+Ze」，外圍一個橢圓軌道（俯視略帶透視），
  軌道上一個黑色小圓點標「−e」，軌道上的箭頭為逆時針方向（從上方俯視）。
  從原子核往上畫一支藍色箭頭，標「軌道角動量 L」。
  小字：電子繞原子核轉

主體中上（約 30% 寬）｜pill 標籤：(b) 電子的座標系
  中央換成黑色小圓點「−e」（電子），外圍同樣的橢圓軌道，
  軌道上是灰色大圓點「+Ze」，繞行方向**與 (a) 相同**（逆時針）。
  在軌道內部、從下往上畫三到四支平行的綠色粗箭頭，標「B（原子核繞行產生）」。
  在電子上畫一支紅色箭頭 S（自旋）與一支方向相反的橘色短箭頭 μ_s。
  小字：原子核繞電子轉 = 一個電流迴路 I = ef，中心磁場 B = μ₀I/2r
  (a)、(b) 之間用一個雙向箭頭連接，箭頭上標「換座標系（運動是相對的）」，
  旁邊加一個小圖示：地球與太陽，標「就像站在地球上看太陽繞著地球轉」。

主體右上（約 40% 寬）｜pill 標籤：(c) 2p 能階分裂（圖 7.14，不按比例）
  左半「沒有自旋—軌道耦合」：上方一條藍色水平線標「2p」，下方一條標「1s」，
    一支黑色向下箭頭，旁邊標「一條譜線」。
  右半「有自旋—軌道耦合」：2p 分裂成上下兩條很接近的線，
    上線標「2p₃/₂（j = 3/2，S 與 L 大致同向，+μ_B B）」，
    下線標「2p₁/₂（j = 1/2，S 與 L 大致反向，−μ_B B）」，
    兩線間距用大括號標「ΔE ≈ 4.5 × 10⁻⁵ eV」；
    1s 標「1s₁/₂（l = 0，不分裂）」。
    兩支向下箭頭（紫色）分別從兩條 2p 線落到 1s，旁邊標「雙重態 (doublet)：兩條譜線」。
  左右兩半之間用虛線連接 2p 與它分裂出的兩條線。
  紅色小字：分裂量只有 2p → 1s 光子能量 10.2 eV 的百萬分之四左右

主體下方（橫跨全寬）｜pill 標籤：例題 7.3：氫原子 2p 的內部磁場有多強
一排五個並列的小方塊，以箭頭串起：
  r = 4a₀ ≈ 2.12 × 10⁻¹⁰ m　→　f = v/2πr ≈ 8.2 × 10¹⁴ s⁻¹　→
  B = μ₀fe/2r ≈ 0.39 T　→　U_m = μ_B B ≈ 2.3 × 10⁻⁵ eV　→　ΔE = 2U_m ≈ 4.5 × 10⁻⁵ eV（與實驗相符）
  在 B 的方塊下方加一行比較：0.39 T ≈ 4000 高斯，約為地球磁場（≈ 0.5 高斯）的數千倍

右上角「圖例」方框：
  藍色 — 軌道角動量 L
  紅色 — 自旋角動量 S
  橘色 — 自旋磁矩 μ_s
  綠色 — 軌道運動產生的磁場 B

最下方一排粉彩公式盒（三個）：
1. 淺綠盒：B = μ₀ I/2r = μ₀ f e/2r，說明「電流迴路中心的磁場」
2. 淺紅盒：U_m = ±μ_B B　(7.15)，說明「自旋在內部磁場中的兩種磁能」
3. 淺紫盒：ΔE = 2μ_B B，說明「一個能階分裂成兩個 → 精細結構」
```

## English Prompt

```
MODEL AND NOTATION: Use a nonrelativistic central field with weak spin-orbit coupling; the classical orbital-field picture motivates scales and directions, not exact fine-structure energies.

Draw an educational infographic titled "why the spin feels a magnetic field even
with no external field — spin-orbit coupling". ALL labels in TRADITIONAL CHINESE.

Title bar: 7.7  自旋—軌道耦合 (Spin-Orbit Coupling)

Intro box (Traditional Chinese):
站在原子核上看，是電子繞著原子核轉；站在電子上看，是帶正電的原子核繞著電子轉。
繞行的正電荷就是一個電流迴路，在電子處產生磁場 B（與 L 同向）。
電子的自旋磁矩在這個「內部磁場」中有磁能 ±μ_B B，於是一個能階分裂成兩個。

UPPER LEFT ~30%, pill label (a) 原子核的座標系:
  a large grey dot at the centre labelled +Ze, surrounded by an elliptical orbit
  (top view with slight perspective); a small black dot on the orbit labelled −e;
  the orbit arrow runs COUNTER-CLOCKWISE (seen from above).
  a BLUE arrow pointing up from the nucleus, labelled 軌道角動量 L.
  small caption: 電子繞原子核轉

UPPER CENTRE ~30%, pill label (b) 電子的座標系:
  now the small black dot −e (the electron) is at the centre, with the same
  elliptical orbit; the large grey dot +Ze is ON the orbit, circulating in the
  SAME counter-clockwise sense as in (a).
  inside the orbit, three or four parallel thick GREEN arrows pointing up, labelled
  B（原子核繞行產生）.
  on the electron, a RED arrow S (spin) and a shorter ORANGE arrow μ_s pointing
  the opposite way.
  small caption: 原子核繞電子轉 = 一個電流迴路 I = ef，中心磁場 B = μ₀I/2r
  Link (a) and (b) with a double-headed arrow labelled 換座標系（運動是相對的）,
  with a small Earth–Sun icon and the note 就像站在地球上看太陽繞著地球轉.

UPPER RIGHT ~40%, pill label (c) 2p 能階分裂（圖 7.14，不按比例）:
  left half 沒有自旋—軌道耦合: a blue horizontal line 2p above, a line 1s below,
    one black downward arrow, note 一條譜線.
  right half 有自旋—軌道耦合: 2p split into two very close lines,
    upper line 2p₃/₂（j = 3/2，S 與 L 大致同向，+μ_B B）,
    lower line 2p₁/₂（j = 1/2，S 與 L 大致反向，−μ_B B）,
    the gap marked with a brace ΔE ≈ 4.5 × 10⁻⁵ eV;
    the 1s line labelled 1s₁/₂（l = 0，不分裂）.
    two PURPLE downward arrows, one from each 2p line to 1s, labelled
    雙重態 (doublet)：兩條譜線.
  dashed connectors join the unsplit 2p line to its two split lines.
  small red note: 分裂量只有 2p → 1s 光子能量 10.2 eV 的百萬分之四左右

BOTTOM (full width), pill label 例題 7.3：氫原子 2p 的內部磁場有多強:
A row of five small boxes joined by arrows:
  r = 4a₀ ≈ 2.12 × 10⁻¹⁰ m → f = v/2πr ≈ 8.2 × 10¹⁴ s⁻¹ →
  B = μ₀fe/2r ≈ 0.39 T → U_m = μ_B B ≈ 2.3 × 10⁻⁵ eV → ΔE = 2U_m ≈ 4.5 × 10⁻⁵ eV（與實驗相符）
  under the B box, a comparison line: 0.39 T ≈ 4000 高斯，約為地球磁場（≈ 0.5 高斯）的數千倍

Top-right legend "圖例":
  藍色 — 軌道角動量 L
  紅色 — 自旋角動量 S
  橘色 — 自旋磁矩 μ_s
  綠色 — 軌道運動產生的磁場 B

Bottom pastel formula boxes (three):
1. light green: B = μ₀ I/2r = μ₀ f e/2r — 電流迴路中心的磁場
2. light red: U_m = ±μ_B B  (7.15) — 自旋在內部磁場中的兩種磁能
3. light purple: ΔE = 2μ_B B — 一個能階分裂成兩個 → 精細結構
```
