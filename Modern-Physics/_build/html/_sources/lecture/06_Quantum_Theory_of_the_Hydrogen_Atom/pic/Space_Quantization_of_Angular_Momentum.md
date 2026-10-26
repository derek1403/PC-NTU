# Space_Quantization_of_Angular_Momentum.png

**對應章節：** 6.6 磁量子數
**插入位置：** $(6.22)$ $L_z = m_l\hbar$ 之後、「空間量子化的圖像」之前
**課本對應：** 圖 6.5（含課本第 20 頁「測不準原理和空間量子化」）

> 產圖前請先貼上 `00_STYLE_GUIDE.md` 的風格區塊。

---

## 中文提示詞

```
請畫一張教學用資訊圖表，主題是「角動量的空間量子化」，以 l = 2 為例。

標題列文字：6.6  角動量的空間量子化 (Space Quantization of the Angular Momentum)

導言框文字：
l 決定角動量向量的「長度」，m_l 決定它的「方向」。
向量長度是 √(l(l+1)) ħ，但它在 z 軸上的投影必須是 ħ 的整數倍，
於是方向被鎖死在有限個離散的圓錐上。

主體左半（約 55% 寬）｜pill 標籤：l = 2 的五個允許方向
- 畫一條垂直向上的 z 軸，刻度由下而上標為 −2ħ、−ħ、0、+ħ、+2ħ（每格等距）。
- 以原點為起點，畫五個長度完全相同的向量（長度必須明顯大於 2ħ 那一格的高度，
  代表 L = √6 ħ ≈ 2.449ħ），分別指向使其 z 分量恰為 +2ħ、+ħ、0、−ħ、−2ħ 的方向。
- 五個向量分別上色：m_l=+2 紅 #C62828、m_l=+1 橘 #EF6C00、m_l=0 綠 #2E7D32、
  m_l=−1 藍 #1565C0、m_l=−2 紫 #7B1FA2，並在向量末端標註對應的 m_l 值。
- 每個向量各自畫出一個以 z 軸為中心軸的半透明圓錐面（同色、透明度高），
  表示該 m_l 之下向量可指向圓錐上的任何一點。
- 從每個向量末端往 z 軸拉一條灰色虛線，標出投影 L_z = m_l ħ。
- 在圖的一側標註：L = √6 ħ ≈ 2.449 ħ（向量長度，五個都一樣）。
- 特別強調：五個向量沒有任何一個貼齊 z 軸，即使 m_l = +2 也還有明顯夾角。

主體右半（約 45% 寬）：兩個上下堆疊的說明卡。

卡 1｜pill 標籤：為什麼 L 不能沿著 z 軸
  上半：一個打叉（紅色 ✗）的示意圖——L 向量完全貼齊 z 軸，
    電子在垂直於 z 軸的水平面上做圓周運動，該平面用紅色虛線畫出。
    標註 Δz = 0 且 Δp_z = 0。
  下半：紅色框內寫 Δz · Δp_z ≥ ħ/2，並標「違反測不準原理」。
  最下方一行綠色打勾（✓）的結論：
    |L_z|max = lħ < √(l(l+1)) ħ = L，投影恆小於長度，故 L 與 z 軸恆有夾角。

卡 2｜pill 標籤：沒有磁場時 m_l 有意義嗎？
  文字：沒有磁場時空間是等向的，任何方向都可以拿來當 z 軸，
  這時說「L 在 z 軸的投影是 2ħ」等於什麼都沒說。
  能量公式 (6.16) 完全不含 m_l → 不同 m_l 的態能量相同（簡併）。
  m_l 唯一真正現身的場合是加磁場時，那時 z 軸就是磁場方向 → 見 6.10 塞曼效應。

右上角「圖例」方框：
  五種顏色 — 分別對應 m_l = +2, +1, 0, −1, −2
  半透明圓錐 — 該 m_l 之下向量可指的所有方向
  灰色虛線 — 往 z 軸的投影 L_z

最下方一排粉彩公式盒（三個）：
1. 淺藍盒：L = √(l(l+1)) ħ，說明「向量的長度，由 l 決定」
2. 淺綠盒：L_z = m_l ħ，說明「向量在 z 軸的投影，由 m_l 決定」
3. 淺紫盒：m_l = 0, ±1, …, ±l，共 2l+1 個方向，說明「l = 2 時共五個」
```

## English Prompt

```
Draw an educational infographic titled "Space quantization of the angular
momentum", using l = 2 as the example. ALL labels in TRADITIONAL CHINESE.

Title bar: 6.6  角動量的空間量子化 (Space Quantization of the Angular Momentum)

Intro box (Traditional Chinese):
l 決定角動量向量的「長度」，m_l 決定它的「方向」。
向量長度是 √(l(l+1)) ħ，但它在 z 軸上的投影必須是 ħ 的整數倍，
於是方向被鎖死在有限個離散的圓錐上。

LEFT ~55%, pill label l = 2 的五個允許方向:
- A vertical z-axis with equally spaced ticks labelled, bottom to top,
  −2ħ, −ħ, 0, +ħ, +2ħ.
- Five vectors from the origin, ALL of exactly the same length (clearly longer
  than the +2ħ tick height, representing L = √6 ħ ≈ 2.449ħ), each oriented so its
  z-component is exactly +2ħ, +ħ, 0, −ħ, −2ħ.
- Colour them: m_l=+2 red #C62828, m_l=+1 orange #EF6C00, m_l=0 green #2E7D32,
  m_l=−1 blue #1565C0, m_l=−2 purple #7B1FA2, with the m_l value at each tip.
- Around each vector draw a highly transparent cone about the z-axis in the same
  colour, showing that the vector may point anywhere on that cone.
- Grey dashed lines from each vector tip to the z-axis marking L_z = m_l ħ.
- Annotate to one side: L = √6 ħ ≈ 2.449 ħ（向量長度，五個都一樣）.
- IMPORTANT: none of the five vectors lies along the z-axis; even m_l = +2 keeps a
  visible tilt.

RIGHT ~45%: two stacked cards.

Card 1 pill: 為什麼 L 不能沿著 z 軸
  top: a red ✗ sketch — the L vector exactly along z, the electron circling in the
    horizontal plane perpendicular to z, that plane drawn as a red dashed ellipse.
    Annotate Δz = 0 且 Δp_z = 0.
  bottom: a red box with Δz · Δp_z ≥ ħ/2 and the note 違反測不準原理.
  final line with a green ✓:
    |L_z|max = lħ < √(l(l+1)) ħ = L，投影恆小於長度，故 L 與 z 軸恆有夾角。

Card 2 pill: 沒有磁場時 m_l 有意義嗎？
  沒有磁場時空間是等向的，任何方向都可以拿來當 z 軸，
  這時說「L 在 z 軸的投影是 2ħ」等於什麼都沒說。
  能量公式 (6.16) 完全不含 m_l → 不同 m_l 的態能量相同（簡併）。
  m_l 唯一真正現身的場合是加磁場時，那時 z 軸就是磁場方向 → 見 6.10 塞曼效應。

Top-right legend "圖例":
  五種顏色 — 分別對應 m_l = +2, +1, 0, −1, −2
  半透明圓錐 — 該 m_l 之下向量可指的所有方向
  灰色虛線 — 往 z 軸的投影 L_z

Bottom pastel boxes (three):
1. light blue: L = √(l(l+1)) ħ — 向量的長度，由 l 決定
2. light green: L_z = m_l ħ — 向量在 z 軸的投影，由 m_l 決定
3. light purple: m_l = 0, ±1, …, ±l，共 2l+1 個方向 — l = 2 時共五個
```
