# Specific_Heat_Dulong_Petit_vs_Einstein.png

**對應章節：** 9.8 固體的比熱
**插入位置：**「實驗怎麼說」小節標題之下、正文之前
**課本對應：** 圖 9.10

> 產圖前請先貼上 `00_STYLE_GUIDE.md` 的風格區塊。

---

## 中文提示詞

```
請畫一張教學用資訊圖表，主題是「固體比熱：古典的 3R 只在高溫成立，量子化的振盪器解釋了低溫」。

標題列文字：9.8  固體的比熱 (Specific Heats of Solids)

導言框文字：
每個晶格原子是三個振盪器，古典能量均分給每個 kT，所以莫耳比熱 c_V = 3R（杜隆－珀蒂）。
實驗顯示高溫確實趨近 3R，但低溫時一路掉到零。
愛因斯坦把振盪器的平均能量換成普朗克的 hν/(e^(hν/kT) − 1)，低溫下降便自然出現。

主體分成左、右兩區，左上角另有一個小插圖。

左上小插圖｜pill 標籤：一個原子 = 三個振盪器
一顆紅褐色球位於中心，沿 ±x、±y、±z 六個方向各以一根彈簧連到灰色的鄰近原子。
旁註：「每個方向：動能 ½kT + 位能 ½kT = kT」「每個原子：3kT → 每 kmol：3N₀kT = 3RT」

左區（約 55% 寬）｜pill 標籤：實驗數據（圖 9.10）
一張平面圖，橫軸「絕對溫度 (K)」刻度 0、200、400、600、800、1000、1200；
縱軸「c_V (kcal/kmol·K)」刻度 0–7。
在 c_V = 5.97 處畫一條橘色（#EF6C00）水平粗虛線，標「杜隆－珀蒂 3R = 5.97」。
四條深灰色（#424242）實線代表實驗數據，每條直接標元素名：
  鉛：極陡，約 50 K 已超過 4，約 150 K 就貼近 6
  鋁：約 100 K 爬到 3.5，約 400 K 接近 5.7
  矽：從約 100 K 處 2 附近起畫，約 600 K 接近 5.5，之後緩緩貼近 6
  碳（鑽石）：最慢的 S 形曲線，300 K 約 1.4，600 K 約 4，1100 K 約 5.1
加一行小字：「所有元素高溫都趨近 3R；低溫全部掉向 0」。

右區（約 45% 寬）｜pill 標籤：愛因斯坦的普適曲線
一張平面圖，橫軸 T/θ_E（刻度 0、0.5、1.0、1.5、2.0），縱軸 c_V/3R（刻度 0、0.5、1.0）。
  橘色水平虛線：c_V/3R = 1（古典）
  藍色（#1565C0）實線：愛因斯坦公式 x² eˣ/(eˣ − 1)²，x = θ_E/T——
    在 0 附近貼著橫軸（指數式地趨近 0），約 T/θ_E = 0.25 時 0.30、0.5 時 0.72、1.0 時 0.92，之後趨近 1。
  在曲線上標兩個實心點（鑽石，θ_E ≈ 1320 K）：
    T = 300 K（T/θ_E = 0.23）→ c_V/3R ≈ 0.24，標「≈ 1.45 kcal/kmol·K」
    T = 1000 K（T/θ_E = 0.76）→ c_V/3R ≈ 0.87，標「≈ 5.2 kcal/kmol·K」
  旁邊兩個小標註：
    高溫 kT ≫ hν：e^(hν/kT) ≈ 1 + hν/kT → ε̄ → kT → c_V → 3R
    低溫 kT ≪ hν：振盪器被凍結在 n = 0 → c_V → 0
  小字：「θ_E = hν/k：鍵結愈硬、原子愈輕 → θ_E 愈高（鑽石最高、鉛最低）」

右上角「圖例」方框：
  橘色虛線 — 古典預測 3R（杜隆－珀蒂）
  深灰實線 — 實驗數據
  藍色實線 — 愛因斯坦比熱公式（量子振盪器）

最下方一排粉彩公式盒（四個）：
1. 淺黃盒：E = 3N₀kT = 3RT，說明「(9.50) 古典內能」
2. 淺紅盒：c_V = 3R = 5.97 kcal/kmol·K，說明「(9.51) 杜隆－珀蒂定律」
3. 淺藍盒：c_V = 3R (hν/kT)² e^(hν/kT) / (e^(hν/kT) − 1)²，說明「(9.54) 愛因斯坦比熱公式」
4. 淺紫盒：真實低溫 c_V ∝ T³，說明「德拜模型：計入各種頻率的晶格振動」
```

## English Prompt

```
Draw an educational infographic titled "Specific heat of solids: classical 3R holds
only at high temperature; quantized oscillators explain the low-temperature drop".
ALL labels in TRADITIONAL CHINESE.

Title bar: 9.8  固體的比熱 (Specific Heats of Solids)

Intro box (Traditional Chinese):
每個晶格原子是三個振盪器，古典能量均分給每個 kT，所以莫耳比熱 c_V = 3R（杜隆－珀蒂）。
實驗顯示高溫確實趨近 3R，但低溫時一路掉到零。
愛因斯坦把振盪器的平均能量換成普朗克的 hν/(e^(hν/kT) − 1)，低溫下降便自然出現。

Two main areas plus a small inset at the top-left.

TOP-LEFT INSET, pill label 一個原子 = 三個振盪器:
A reddish-brown sphere in the centre tied by six springs along ±x, ±y, ±z to grey neighbours.
Notes: 每個方向：動能 ½kT + 位能 ½kT = kT; 每個原子：3kT → 每 kmol：3N₀kT = 3RT

LEFT ~55%, pill label 實驗數據（圖 9.10）:
A 2D plot, x-axis 絕對溫度 (K) with ticks 0, 200, 400, 600, 800, 1000, 1200;
y-axis c_V (kcal/kmol·K) with ticks 0–7.
A thick orange (#EF6C00) horizontal dashed line at c_V = 5.97 labelled 杜隆－珀蒂 3R = 5.97.
Four dark-grey (#424242) solid curves for experimental data, each labelled directly:
  鉛 (lead): very steep, above 4 by about 50 K, hugging 6 by about 150 K
  鋁 (aluminium): about 3.5 at 100 K, about 5.7 near 400 K
  矽 (silicon): starting near 2 at about 100 K, about 5.5 near 600 K, then slowly toward 6
  碳（鑽石）(diamond): the slowest S-curve — about 1.4 at 300 K, about 4 at 600 K, about 5.1 at 1100 K
Small caption: 所有元素高溫都趨近 3R；低溫全部掉向 0.

RIGHT ~45%, pill label 愛因斯坦的普適曲線:
A 2D plot, x-axis T/θ_E (ticks 0, 0.5, 1.0, 1.5, 2.0), y-axis c_V/3R (ticks 0, 0.5, 1.0).
  orange horizontal dashed line: c_V/3R = 1 (classical)
  solid blue (#1565C0) curve: the Einstein formula x² eˣ/(eˣ − 1)², x = θ_E/T —
    hugging the axis near 0 (approaching zero exponentially), about 0.30 at T/θ_E = 0.25,
    0.72 at 0.5, 0.92 at 1.0, then approaching 1.
  Two filled dots on the curve for diamond (θ_E ≈ 1320 K):
    T = 300 K (T/θ_E = 0.23) → c_V/3R ≈ 0.24, label ≈ 1.45 kcal/kmol·K
    T = 1000 K (T/θ_E = 0.76) → c_V/3R ≈ 0.87, label ≈ 5.2 kcal/kmol·K
  Two small annotations:
    高溫 kT ≫ hν：e^(hν/kT) ≈ 1 + hν/kT → ε̄ → kT → c_V → 3R
    低溫 kT ≪ hν：振盪器被凍結在 n = 0 → c_V → 0
  Small text: θ_E = hν/k：鍵結愈硬、原子愈輕 → θ_E 愈高（鑽石最高、鉛最低）

Top-right legend "圖例":
  橘色虛線 — 古典預測 3R（杜隆－珀蒂）
  深灰實線 — 實驗數據
  藍色實線 — 愛因斯坦比熱公式（量子振盪器）

Bottom pastel boxes (four):
1. light yellow: E = 3N₀kT = 3RT — (9.50) 古典內能
2. light red: c_V = 3R = 5.97 kcal/kmol·K — (9.51) 杜隆－珀蒂定律
3. light blue: c_V = 3R (hν/kT)² e^(hν/kT) / (e^(hν/kT) − 1)² — (9.54) 愛因斯坦比熱公式
4. light purple: 真實低溫 c_V ∝ T³ — 德拜模型：計入各種頻率的晶格振動
```
