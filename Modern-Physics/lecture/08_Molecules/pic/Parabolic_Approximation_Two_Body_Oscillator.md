# Parabolic_Approximation_Two_Body_Oscillator.png

**對應章節：** 8.7 振動能階
**插入位置：**「假設與已知」之後、「推導：拋物線近似」之前
**課本對應：** 圖 8.18、圖 8.19

> 產圖前請先貼上 `00_STYLE_GUIDE.md` 的風格區塊。

---

## 中文提示詞

```
【模型與符號】只在平衡距離附近作諧振近似，μ=m₁m₂/(m₁+m₂)（原 m′）；圖中位能零點、井深 D_e 與零點振動能須分開。

請畫一張教學用資訊圖表，主題是「任何位能井的谷底都像拋物線，兩顆原子的振動等效於一顆縮減質量」。

標題列文字：8.7  拋物線近似與二體振盪器 (Parabolic Approximation and the Two-Body Oscillator)

導言框文字：
在平衡位置 R₀ 做泰勒展開：一次項因為平衡而為零，三次以上的項在小振幅下可忽略，
剩下的就是 U ≈ U₀ + ½k(R − R₀)²——虎克定律。
兩顆原子同時振動時，只要把質量換成縮減質量 m′，就和一端固定在牆上的彈簧一樣。

主體左半（約 55% 寬）｜pill 標籤：拋物線近似（圖 8.18）
  座標圖：橫軸 R，縱軸 U。
  灰色粗曲線（真實位能）：R 很小時陡升，在 R₀ 有谷底 U₀，R 大時緩慢上升、趨近水平（解離極限）。
  黑色細曲線（拋物線 ½k(R − R₀)² + U₀）：與灰色曲線在谷底幾乎重合，離開谷底後明顯分開
    （左邊比真實曲線緩、右邊比真實曲線陡）。
  在谷底附近畫一個淡綠色（#E8F5E9）方框，標「小振幅區：兩者幾乎重合」。
  R₀ 與 U₀ 分別在軸上標出。
  圖下方用一條展開式，把每一項畫成小方塊並上色：
    U(R) = U(R₀)【綠框，標「常數 U₀」】
         + U′(R₀)(R−R₀)【灰框打紅叉，標「平衡 → U′ = 0」】
         + ½U″(R₀)(R−R₀)²【橘框，標「= ½k(R−R₀)²」】
         + ⅙U‴(R₀)(R−R₀)³ + …【灰框打紅叉，標「小振幅 → 忽略」】

主體右半（約 45% 寬）：上下兩部分。

上｜pill 標籤：二體振盪器（圖 8.19）
  左：兩顆球 m₁（小，灰）與 m₂（大，灰）之間接一根彈簧（標「力常數 k」），兩顆球上方各有一支雙向箭頭表示都在振動。
  中間一個大等號「＝」。
  右：一顆球 m′ 接一根相同的彈簧（同樣標「力常數 k」），彈簧另一端固定在一面垂直牆上，球上方一支雙向箭頭。
  下方標：m′ = m₁m₂/(m₁ + m₂)。

下｜pill 標籤：量子化後的振動能階
  在一個小拋物線位能井中畫四條**等間距**的水平線，標 υ = 0, 1, 2, 3 與 E = ½hν₀、³⁄₂hν₀、⁵⁄₂hν₀、⁷⁄₂hν₀；
  最下面那條（υ = 0）與谷底之間用紅色（#C62828）雙箭頭標「零點能量 ½hν₀ ≠ 0」；
  相鄰兩條之間用雙箭頭標「間距恆為 hν₀」。
  小字提醒：υ（upsilon，振動量子數）≠ ν（nu，頻率）。

右上角「圖例」方框：
  灰色粗線 — 真實的分子位能
  黑色細線 — 拋物線近似
  紅叉 — 被消去或忽略的項

最下方一排粉彩公式盒（三個）：
1. 淺綠盒：U = U₀ + ½k(R − R₀)²　(8.12)、F = −k(R − R₀)　(8.13)，說明「谷底附近永遠是虎克定律」
2. 淺藍盒：ν₀ = (1/2π)√(k/m′)　(8.15)，說明「二體問題：m 換成 m′ 就好」
3. 淺黃盒：E_υ = (υ + ½)ħ√(k/m′)　(8.17)，說明「第五章的諧振子，等間距、有零點能量」
```

## English Prompt

```
MODEL AND NOTATION: Harmonic approximation only near equilibrium; μ=m₁m₂/(m₁+m₂), formerly m′. Distinguish potential zero, well depth D_e and vibrational zero-point energy.

Draw an educational infographic titled "Every potential well looks like a parabola at the
bottom, and two vibrating atoms act like one reduced mass". ALL labels in TRADITIONAL CHINESE.

Title bar: 8.7  拋物線近似與二體振盪器 (Parabolic Approximation and the Two-Body Oscillator)

Intro box (Traditional Chinese):
在平衡位置 R₀ 做泰勒展開：一次項因為平衡而為零，三次以上的項在小振幅下可忽略，
剩下的就是 U ≈ U₀ + ½k(R − R₀)²——虎克定律。
兩顆原子同時振動時，只要把質量換成縮減質量 m′，就和一端固定在牆上的彈簧一樣。

LEFT ~55%, pill label 拋物線近似（圖 8.18）:
  Plot: horizontal axis R, vertical axis U.
  Thick grey curve (true potential): steep at small R, a well bottom U₀ at R₀, rising slowly
    at large R and levelling off (dissociation limit).
  Thin black curve (parabola ½k(R − R₀)² + U₀): nearly coincident with the grey curve at the
    bottom, clearly diverging away from it (shallower than the true curve on the left, steeper
    on the right).
  A pale green (#E8F5E9) box around the bottom labelled 小振幅區：兩者幾乎重合.
  R₀ and U₀ marked on the axes.
  Under the plot, the expansion with each term in a coloured tile:
    U(R) = U(R₀) [green tile, 常數 U₀]
         + U′(R₀)(R−R₀) [grey tile with a red cross, 平衡 → U′ = 0]
         + ½U″(R₀)(R−R₀)² [orange tile, = ½k(R−R₀)²]
         + ⅙U‴(R₀)(R−R₀)³ + … [grey tile with a red cross, 小振幅 → 忽略]

RIGHT ~45%: two parts.

Upper, pill label 二體振盪器（圖 8.19）:
  left: two balls m₁ (small, grey) and m₂ (larger, grey) joined by a spring labelled
        力常數 k, each ball with a double-headed arrow above showing it vibrates.
  a large equals sign "＝".
  right: one ball m′ on the same spring (also labelled 力常數 k), the other end fixed to a
        vertical wall, one double-headed arrow above the ball.
  below: m′ = m₁m₂/(m₁ + m₂).

Lower, pill label 量子化後的振動能階:
  Inside a small parabolic well, four EQUALLY spaced horizontal lines labelled
  υ = 0, 1, 2, 3 and E = ½hν₀, ³⁄₂hν₀, ⁵⁄₂hν₀, ⁷⁄₂hν₀. A red (#C62828) double arrow between the
  well bottom and the υ = 0 line labelled 零點能量 ½hν₀ ≠ 0; a double arrow between adjacent
  lines labelled 間距恆為 hν₀.
  Small reminder: υ（upsilon，振動量子數）≠ ν（nu，頻率）.

Top-right legend "圖例":
  灰色粗線 — 真實的分子位能
  黑色細線 — 拋物線近似
  紅叉 — 被消去或忽略的項

Bottom pastel boxes (three):
1. light green: U = U₀ + ½k(R − R₀)²  (8.12)、F = −k(R − R₀)  (8.13) — 谷底附近永遠是虎克定律
2. light blue: ν₀ = (1/2π)√(k/m′)  (8.15) — 二體問題：m 換成 m′ 就好
3. light yellow: E_υ = (υ + ½)ħ√(k/m′)  (8.17) — 第五章的諧振子，等間距、有零點能量
```
