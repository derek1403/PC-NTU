# Rayleigh_Jeans_vs_Planck.png

**對應章節：** 9.6 普朗克輻射定律
**插入位置：** $(9.39)$ 光子分布函數與「$\alpha = 0$」的說明之後、「推導：維恩位移定律」之前
**課本對應：** 無（自製；綜合第二章黑體輻射曲線與本章 $(9.36)$–$(9.41)$）

> 產圖前請先貼上 `00_STYLE_GUIDE.md` 的風格區塊。

---

## 中文提示詞

```
請畫一張教學用資訊圖表，主題是「瑞利－金斯與普朗克只差在每個駐波的平均能量」。

標題列文字：9.6  普朗克輻射定律 (Planck Radiation Law)

導言框文字：
兩個公式用的是同一個駐波密度 G(ν) = 8πν²/c³；差別只在每個駐波分到多少能量。
古典能量均分給每個駐波 kT，高頻模式無窮多 → 紫外災變；
普朗克讓能量只能是 nhν，高頻模式被凍結 → ε̄ = hν/(e^(hν/kT) − 1)。

主體分成上、下兩區。

【上區左（約 55% 寬）｜pill 標籤：同一溫度下的 u(ν)】
一張平面圖，橫軸「頻率 ν」，在軸上標出 hν = kT、hν = 2.82kT、hν = 5kT、hν = 10kT 的位置；
縱軸「能量密度 u(ν)」（不標數值）。
  橘色粗虛線（#EF6C00）：瑞利－金斯 u ∝ ν²，一路往上衝出圖框上緣，
    在衝出處標「→ ∞ 紫外災變」。
  藍色粗實線（#1565C0）：普朗克曲線——低頻與橘色虛線幾乎重合、
    在 hν ≈ 2.82kT 達到峰值、之後指數下降到接近零。
  在低頻重合區畫一個淡灰色框，標「hν ≪ kT：兩者一致（對應原理）」。
  在高頻區兩條線分離的地方畫一個淡紅色框，標「hν ≫ kT：古典失敗」。

【上區右（約 45% 寬）｜pill 標籤：每個駐波的平均能量】
一張平面圖，橫軸 hν/kT（刻度 0、1、2、3、4、5），縱軸 ε̄/kT（刻度 0、0.5、1）。
  橘色水平虛線：ε̄ = kT（古典，不論頻率都一樣）
  藍色實線：ε̄ = hν/(e^(hν/kT) − 1)，在 0 處從 1 開始、單調下降，
    在 hν/kT = 1 時約 0.58、在 hν/kT = 5 時約 0.034。
  兩條線之間的空白區域淡淡塗灰，標「高頻模式被凍結：一個量子 hν 的門檻遠高於熱能」。
旁邊一個小框寫出平均能量的推導骨架：
  ε̄ = Σ nhν e^(−nhν/kT) / Σ e^(−nhν/kT) = hν/(e^(hν/kT) − 1)
  並註明「分母 1/(e^(hν/kT) − 1) 就是 α = 0 的波色－愛因斯坦分布（光子數不守恆）」

【下區｜pill 標籤：不同溫度的 u(λ)——維恩位移與 T⁴】
一張寬平面圖，橫軸「波長 λ (nm)」刻度 0、500、1000、1500、2000、2500、3000；
縱軸 u(λ)（不標數值）。底部 380–750 nm 範圍畫一條彩虹色的可見光帶。
畫四條藍色系由淺到深的曲線，溫度分別為 3000 K、4000 K、5000 K、6000 K：
  溫度愈高，曲線整體愈高、峰值愈往左（短波長）移；
  峰值位置分別約在 966 nm、724 nm、580 nm、483 nm，各畫一個小圓點。
  用一條灰色虛線把四個峰值串起來（形狀為雙曲線 λ_max ∝ 1/T）。
  圖旁註記：「λ_max T = 2.898 × 10⁻³ m·K（維恩）」與「曲線下面積 ∝ T⁴（史蒂芬－波茲曼）」。

右上角「圖例」方框：
  橘色虛線 — 古典：瑞利－金斯、ε̄ = kT
  藍色實線 — 普朗克（光子 = 波色子）
  灰色虛線 — 各溫度峰值的連線（維恩位移）
  彩虹帶 — 可見光 380–750 nm

最下方一排粉彩公式盒（四個）：
1. 淺藍盒：ε̄ = hν / (e^(hν/kT) − 1)，說明「(9.37) 振盪器的平均能量」
2. 淺綠盒：u(ν) dν = (8πh/c³) ν³ dν / (e^(hν/kT) − 1)，說明「(9.38) 普朗克輻射公式」
3. 淺紫盒：λ_max T = hc/(4.965k) = 2.898 × 10⁻³ m·K，說明「(9.40) 由 du/dλ = 0」
4. 淺黃盒：R = eσT⁴，σ = 2π⁵k⁴/(15h³c²)，說明「(9.41) 由 ∫u dν 與 R = (c/4)U」
```

## English Prompt

```
Draw an educational infographic titled "Rayleigh–Jeans versus Planck: they differ
only in the average energy per standing wave". ALL labels in TRADITIONAL CHINESE.

Title bar: 9.6  普朗克輻射定律 (Planck Radiation Law)

Intro box (Traditional Chinese):
兩個公式用的是同一個駐波密度 G(ν) = 8πν²/c³；差別只在每個駐波分到多少能量。
古典能量均分給每個駐波 kT，高頻模式無窮多 → 紫外災變；
普朗克讓能量只能是 nhν，高頻模式被凍結 → ε̄ = hν/(e^(hν/kT) − 1)。

Two bands.

UPPER-LEFT (~55%), pill label 同一溫度下的 u(ν):
A 2D plot, x-axis 頻率 ν with the positions hν = kT, hν = 2.82kT, hν = 5kT, hν = 10kT marked;
y-axis 能量密度 u(ν) (no numbers).
  thick orange dashed (#EF6C00): Rayleigh–Jeans u ∝ ν², shooting out of the top of the frame,
    labelled → ∞ 紫外災變 where it exits.
  thick solid blue (#1565C0): the Planck curve — nearly coincident with the orange line at
    low frequency, peaking at hν ≈ 2.82kT, then decaying exponentially toward zero.
  A light-grey box over the low-frequency overlap labelled hν ≪ kT：兩者一致（對應原理）.
  A light-red box where the curves separate at high frequency labelled hν ≫ kT：古典失敗.

UPPER-RIGHT (~45%), pill label 每個駐波的平均能量:
A 2D plot, x-axis hν/kT (ticks 0–5), y-axis ε̄/kT (ticks 0, 0.5, 1).
  orange horizontal dashed line: ε̄ = kT (classical, same for every frequency)
  solid blue curve: ε̄ = hν/(e^(hν/kT) − 1), starting at 1 at the origin and decreasing
    monotonically: about 0.58 at hν/kT = 1 and about 0.034 at hν/kT = 5.
  Shade the gap between the two curves light grey, labelled
    高頻模式被凍結：一個量子 hν 的門檻遠高於熱能.
A small side box with the skeleton of the derivation:
  ε̄ = Σ nhν e^(−nhν/kT) / Σ e^(−nhν/kT) = hν/(e^(hν/kT) − 1)
  and the note 分母 1/(e^(hν/kT) − 1) 就是 α = 0 的波色－愛因斯坦分布（光子數不守恆）

LOWER band, pill label 不同溫度的 u(λ)——維恩位移與 T⁴:
A wide 2D plot, x-axis 波長 λ (nm) with ticks 0, 500, 1000, 1500, 2000, 2500, 3000;
y-axis u(λ) (no numbers). A rainbow-coloured visible band along the bottom from 380 to 750 nm.
Four curves in blue shades from light to dark for T = 3000 K, 4000 K, 5000 K, 6000 K:
  hotter curves are higher overall and peak further left (shorter wavelength);
  peaks at about 966 nm, 724 nm, 580 nm, 483 nm, each marked with a small dot.
  A grey dashed line through the four peaks (a hyperbola, λ_max ∝ 1/T).
  Notes: λ_max T = 2.898 × 10⁻³ m·K（維恩） and 曲線下面積 ∝ T⁴（史蒂芬－波茲曼）.

Top-right legend "圖例":
  橘色虛線 — 古典：瑞利－金斯、ε̄ = kT
  藍色實線 — 普朗克（光子 = 波色子）
  灰色虛線 — 各溫度峰值的連線（維恩位移）
  彩虹帶 — 可見光 380–750 nm

Bottom pastel boxes (four):
1. light blue: ε̄ = hν / (e^(hν/kT) − 1) — (9.37) 振盪器的平均能量
2. light green: u(ν) dν = (8πh/c³) ν³ dν / (e^(hν/kT) − 1) — (9.38) 普朗克輻射公式
3. light purple: λ_max T = hc/(4.965k) = 2.898 × 10⁻³ m·K — (9.40) 由 du/dλ = 0
4. light yellow: R = eσT⁴，σ = 2π⁵k⁴/(15h³c²) — (9.41) 由 ∫u dν 與 R = (c/4)U
```
