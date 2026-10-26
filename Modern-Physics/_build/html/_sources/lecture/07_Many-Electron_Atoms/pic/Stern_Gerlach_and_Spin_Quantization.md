# Stern_Gerlach_and_Spin_Quantization.png

**對應章節：** 7.1 電子自旋
**插入位置：**「假設與已知」之後、「推導：史坦—格拉克實驗與 $s = 1/2$」之前
**課本對應：** 圖 7.3（史坦—格拉克實驗）＋ 圖 7.2（自旋的兩個可能轉向）

> 產圖前請先貼上 `00_STYLE_GUIDE.md` 的風格區塊。

---

## 中文提示詞

```
【模型與符號】角動量箭頭、圓錐與進動是向量模型示意，不是可同時精確測得的三個分量或電子軌跡；z 為選定量子化軸。LS 耦合圖限自旋—軌道作用較弱的情況。

請畫一張教學用資訊圖表，主題是「史坦—格拉克實驗如何證明 s = 1/2」。

標題列文字：7.1  史坦—格拉克實驗與自旋量子化 (Stern–Gerlach Experiment and Spin Quantization)

導言框文字：
銀原子束穿過「不均勻」磁場，受力 F_z = μ_z ∂B/∂z，落點高度直接量出 μ_z。
古典預測是一條連續的帶，實驗卻只看到兩個分開的落點。
銀的軌道角動量 l = 0，兩個落點只能來自另一種角動量：2s + 1 = 2 ⇒ s = 1/2。

主體左半（約 60% 寬）｜pill 標籤：實驗裝置（圖 7.3）
畫一張由右往左的立體示意圖（簡潔線條、淺灰色塊，不要 3D 陰影）：
  最右邊：一個小圓柱形「爐」，標「爐：蒸發銀原子」。
  往左：一塊帶細縫的準直板，原子束（細灰線）穿過細縫，標「銀原子束」。
  中間：上下一對長條形磁極。上磁極標「N」，下緣做成尖刃狀；
    下磁極標「S」，上緣做成凹槽狀。在兩極之間畫幾條由尖刃往外散開的綠色磁力線，
    標「不均勻磁場：∂B/∂z ≠ 0」。
  最左邊：一塊直立的相片板，標「相片板」。
  在相片板旁邊放大一個小框，框內並排三個圖案：
    (1)「關閉磁場」：一條細的水平短線；
    (2)「古典預測」：一個實心灰色的菱形／透鏡狀帶（上下連續塗滿）；
    (3)「實際觀測」：上下兩個分開的空心唇形輪廓，中間是空的。
  第 (3) 個圖案用紅框強調。

主體左半下方｜pill 標籤：為什麼一定是 1/2
三個並排的小卡，用箭頭串起來：
  卡 A：銀 Z = 47：46 個電子在填滿的子殼（總角動量 0），最外層 5s 電子 l = 0
        → 若只有軌道角動量：2l + 1 = 1 個落點（不分裂）
  卡 B：任何軌道角動量的落點數 2l + 1 = 1, 3, 5, … 永遠是奇數
  卡 C（紅框）：實驗看到 2 個落點（偶數）⇒ 另一種角動量：2s + 1 = 2 ⇒ s = 1/2

主體右半（約 40% 寬）｜pill 標籤：自旋的兩個轉向（圖 7.2）
畫一個以 z 軸為中心的向量圖：
  垂直向上的 z 軸（深藍），旁邊標「磁場方向 B」（綠色）。
  兩個紅色圓錐（只畫輪廓）：上方圓錐的半頂角 54.7°，下方圓錐與 −z 軸夾 54.7°。
  在上圓錐表面畫一支紅色向量 S，標「m_s = +1/2：S_z = +ħ/2」；
  在下圓錐表面畫一支紅色向量 S，標「m_s = −1/2：S_z = −ħ/2」。
  兩支向量長度相同，標「|S| = (√3/2)ħ ≈ 0.866ħ」；
  在 z 軸上用水平虛線標出投影點 +ħ/2 與 −ħ/2。
  在每支 S 的起點畫一支橘色（#EF6C00）較短箭頭 μ_s，方向與 S 相反，
    標「μ_s 與 S 反向（電子帶負電）」。
  紅色小字：S 永遠不會剛好沿著 z 軸；「向上」只是落在與 +z 夾 54.7° 的圓錐上。

右上角「圖例」方框：
  紅色 — 自旋角動量 S
  橘色 — 自旋磁矩 μ_s
  綠色 — 磁場 B 與磁力線
  灰色 — 銀原子束

最下方一排粉彩公式盒（四個）：
1. 淺綠盒：F_z = μ_z ∂B/∂z，說明「均勻磁場只轉不推，必須有梯度」
2. 淺紅盒：S = √(s(s+1)) ħ = (√3/2)ħ　(7.1)，說明「自旋角動量的大小」
3. 淺藍盒：S_z = m_s ħ = ±ħ/2　(7.2)，說明「只有兩個轉向」
4. 淺黃盒：μ_s = −(e/m)S，μ_sz = ±μ_B　(7.3)(7.4)，說明「旋磁比是軌道的兩倍」
```

## English Prompt

```
MODEL AND NOTATION: Angular-momentum arrows, cones and precession are vector-model schematics, not simultaneous sharp Cartesian components or electron trajectories. z is the chosen quantization axis. LS coupling assumes weak spin-orbit coupling.

Draw an educational infographic titled "how the Stern–Gerlach experiment proves
s = 1/2". ALL labels in TRADITIONAL CHINESE.

Title bar: 7.1  史坦—格拉克實驗與自旋量子化 (Stern–Gerlach Experiment and Spin Quantization)

Intro box (Traditional Chinese):
銀原子束穿過「不均勻」磁場，受力 F_z = μ_z ∂B/∂z，落點高度直接量出 μ_z。
古典預測是一條連續的帶，實驗卻只看到兩個分開的落點。
銀的軌道角動量 l = 0，兩個落點只能來自另一種角動量：2s + 1 = 2 ⇒ s = 1/2。

LEFT ~60%, pill label 實驗裝置（圖 7.3）:
A clean right-to-left perspective sketch (simple lines, light-grey fills, NO 3D shading):
  far right: a small cylindrical oven labelled 爐：蒸發銀原子.
  next: a collimator plate with a narrow slit; the atom beam (thin grey line)
    passes through it, labelled 銀原子束.
  centre: a pair of long magnet poles. Upper pole labelled N with a KNIFE-EDGE
    lower rim; lower pole labelled S with a GROOVED upper rim. Between them a few
    green field lines fanning out from the knife edge, labelled
    不均勻磁場：∂B/∂z ≠ 0.
  far left: an upright photographic plate labelled 相片板.
  Next to the plate, a zoom-in box with three patterns side by side:
    (1) 關閉磁場: a thin short horizontal line;
    (2) 古典預測: a SOLID grey lens/diamond-shaped band (continuously filled top to bottom);
    (3) 實際觀測: two SEPARATE hollow lip-shaped outlines, upper and lower, empty in between.
  Pattern (3) is emphasised with a red frame.

Below it, pill label 為什麼一定是 1/2:
Three small cards side by side, linked by arrows:
  Card A: 銀 Z = 47：46 個電子在填滿的子殼（總角動量 0），最外層 5s 電子 l = 0
          → 若只有軌道角動量：2l + 1 = 1 個落點（不分裂）
  Card B: 任何軌道角動量的落點數 2l + 1 = 1, 3, 5, … 永遠是奇數
  Card C (red frame): 實驗看到 2 個落點（偶數）⇒ 另一種角動量：2s + 1 = 2 ⇒ s = 1/2

RIGHT ~40%, pill label 自旋的兩個轉向（圖 7.2）:
A vector diagram about the z axis:
  a vertical dark-blue z axis, with a green note 磁場方向 B beside it.
  two RED cones (outline only): the upper cone has a 54.7° half-angle from +z,
  the lower cone makes 54.7° with −z.
  On the upper cone surface a red vector S labelled m_s = +1/2：S_z = +ħ/2;
  on the lower cone surface a red vector S labelled m_s = −1/2：S_z = −ħ/2.
  Both vectors have the SAME length, labelled |S| = (√3/2)ħ ≈ 0.866ħ;
  horizontal dashed lines mark the projections +ħ/2 and −ħ/2 on the z axis.
  At the tail of each S, a shorter ORANGE (#EF6C00) arrow μ_s pointing OPPOSITE
    to S, labelled μ_s 與 S 反向（電子帶負電）.
  small red note: S 永遠不會剛好沿著 z 軸；「向上」只是落在與 +z 夾 54.7° 的圓錐上。

Top-right legend "圖例":
  紅色 — 自旋角動量 S
  橘色 — 自旋磁矩 μ_s
  綠色 — 磁場 B 與磁力線
  灰色 — 銀原子束

Bottom pastel formula boxes (four):
1. light green: F_z = μ_z ∂B/∂z — 均勻磁場只轉不推，必須有梯度
2. light red: S = √(s(s+1)) ħ = (√3/2)ħ  (7.1) — 自旋角動量的大小
3. light blue: S_z = m_s ħ = ±ħ/2  (7.2) — 只有兩個轉向
4. light yellow: μ_s = −(e/m)S, μ_sz = ±μ_B  (7.3)(7.4) — 旋磁比是軌道的兩倍
```
