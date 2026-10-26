# Radial_Probability_Density.png

**對應章節：** 6.7 電子機率密度
**插入位置：** $(6.25)$ 球殼機率之後、「極座標積分的三個陷阱」之前
**課本對應：** 圖 6.10、圖 6.11

> 產圖前請先貼上 `00_STYLE_GUIDE.md` 的風格區塊。

---

## 中文提示詞

```
請畫一張教學用資訊圖表，主題是「徑向機率密度：為什麼不能只看 |R|²」。

標題列文字：6.7  徑向機率密度 (Radial Probability Density)

導言框文字：
|R|² 是「單位體積的機率密度」，但我們真正要問的是「整層球殼的機率」，
兩者差一個球殼面積 4πr²。忘記帶 r² 會讓結論完全相反——
這正是例題 6.3 的陷阱。

主體分成上下兩大區。

【上區｜pill 標籤：兩種曲線的差別（以 1s 為例）】
畫兩張並排的平面圖，橫軸皆為 r/a₀（0 到 4，等距刻度），縱軸為機率相關量。
  左圖：|R₁₀(r)|² 對 r/a₀，曲線為單調遞減的指數衰減（紅色 #C62828），
    最大值在 r = 0。標註「最大值在原子核處」，並打一個紅色 ✗，
    小字：只看這條會得到「a₀ 處機率比 a₀/2 低」的錯誤結論。
  右圖：r²|R₁₀(r)|² 對 r/a₀，曲線先升後降，峰值恰好在 r = a₀（藍色 #1565C0），
    在 r = a₀ 處畫一條垂直虛線並標「r = a₀（波耳半徑）」，打一個綠色 ✓。
    另在 r = a₀/2 與 r = a₀ 兩處各畫一個實心點並標出高度，
    旁邊註明「P(a₀)/P(a₀/2) = 4e⁻¹ ≈ 1.47」。
  兩圖中間放一個橘色大箭頭，標「乘上球殼面積 ∝ r²」。

【下區｜pill 標籤：各能階的徑向機率密度 r²|R_nl|²】
畫一張 2×3 的小圖陣列，每個小圖橫軸為 r/a₀、縱軸為 r²|R|²（不標數值刻度，
只需正確呈現形狀與節點數），標題分別為：
  1s（n=1, l=0）：單峰，峰值在 r = a₀，無節點
  2s（n=2, l=0）：兩個峰，中間有一個節點（曲線觸零），主峰約在 r ≈ 5.2a₀
  2p（n=2, l=1）：單峰，峰值在 r = 4a₀，無節點
  3s（n=3, l=0）：三個峰，兩個節點
  3p（n=3, l=1）：兩個峰，一個節點
  3d（n=3, l=2）：單峰，峰值在 r = 9a₀，無節點
每個小圖用同一種藍色（#1565C0）曲線，並在其下用小字標出徑向節點數 = n − l − 1。
橫軸範圍：1s/2p 用 0–10 a₀；2s/3p/3d/3s 用 0–20 a₀，並標明各自範圍。

右上角「圖例」方框：
  紅色曲線 — |R|²（單位體積的機率密度）
  藍色曲線 — r²|R|²（整層球殼的機率）
  虛線 — 峰值位置
  ✗ / ✓ — 錯誤／正確的比較方式

最下方一排粉彩公式盒（四個）：
1. 淺藍盒：P(r) dr = r²|R|² dr，說明「球殼機率，(6.25)」
2. 淺綠盒：1s 的峰值在 r = a₀，說明「電子出現在波耳半徑上的機率最大」
3. 淺紫盒：徑向節點數 = n − l − 1，說明「l 越大節點越少，形狀越單純」
4. 淺紅盒：⟨1/r⟩ = 1/a₀，但 ⟨r⟩ = 1.5a₀，說明「倒數的平均不等於平均的倒數，見例題 6.2」
```

## English Prompt

```
Draw an educational infographic titled "Radial probability density: why |R|²
alone is not enough". ALL labels in TRADITIONAL CHINESE.

Title bar: 6.7  徑向機率密度 (Radial Probability Density)

Intro box (Traditional Chinese):
|R|² 是「單位體積的機率密度」，但我們真正要問的是「整層球殼的機率」，
兩者差一個球殼面積 4πr²。忘記帶 r² 會讓結論完全相反——
這正是例題 6.3 的陷阱。

TOP region, pill label 兩種曲線的差別（以 1s 為例）:
Two side-by-side plots; x-axis r/a₀ from 0 to 4 in both.
  Left: |R₁₀(r)|² versus r/a₀ — a monotonically decaying exponential curve
    (red #C62828) peaking at r = 0. Annotate 最大值在原子核處, mark a red ✗,
    small caption: 只看這條會得到「a₀ 處機率比 a₀/2 低」的錯誤結論。
  Right: r²|R₁₀(r)|² versus r/a₀ — rises then falls, peak exactly at r = a₀
    (blue #1565C0). Vertical dashed line at r = a₀ labelled r = a₀（波耳半徑）,
    mark a green ✓. Put filled dots at r = a₀/2 and r = a₀ with their heights
    indicated, annotated P(a₀)/P(a₀/2) = 4e⁻¹ ≈ 1.47.
  Between the two plots, a large orange arrow labelled 乘上球殼面積 ∝ r².

BOTTOM region, pill label 各能階的徑向機率密度 r²|R_nl|²:
A 2×3 array of small plots; x-axis r/a₀, y-axis r²|R|² (no numeric y ticks needed,
but shapes and node counts must be correct). Titles and required shapes:
  1s (n=1, l=0): single peak at r = a₀, no node
  2s (n=2, l=0): two peaks with one node (curve touching zero), main peak near r ≈ 5.2a₀
  2p (n=2, l=1): single peak at r = 4a₀, no node
  3s (n=3, l=0): three peaks, two nodes
  3p (n=3, l=1): two peaks, one node
  3d (n=3, l=2): single peak at r = 9a₀, no node
Use the same blue (#1565C0) for every curve; below each small plot write the
radial node count 徑向節點數 = n − l − 1.
x ranges: 0–10 a₀ for 1s and 2p; 0–20 a₀ for 2s, 3s, 3p, 3d; label each range.

Top-right legend "圖例":
  紅色曲線 — |R|²（單位體積的機率密度）
  藍色曲線 — r²|R|²（整層球殼的機率）
  虛線 — 峰值位置
  ✗ / ✓ — 錯誤／正確的比較方式

Bottom pastel boxes (four):
1. light blue: P(r) dr = r²|R|² dr — 球殼機率，(6.25)
2. light green: 1s 的峰值在 r = a₀ — 電子出現在波耳半徑上的機率最大
3. light purple: 徑向節點數 = n − l − 1 — l 越大節點越少，形狀越單純
4. light red: ⟨1/r⟩ = 1/a₀，但 ⟨r⟩ = 1.5a₀ — 倒數的平均不等於平均的倒數，見例題 6.2
```
