# Spherical_Volume_Element.png

**對應章節：** 6.7 電子機率密度
**插入位置：**「假設與已知」之後、「推導：球殼機率」之前
**課本對應：** 課本第 22 頁「體積元素 (volume element)」

> 產圖前請先貼上 `00_STYLE_GUIDE.md` 的風格區塊。

---

## 中文提示詞

```
請畫一張教學用資訊圖表，主題是「球座標的體積元素 dV 三個邊長從哪裡來」。

標題列文字：6.7  球座標的體積元素 (Volume Element in Spherical Coordinates)

導言框文字：
在卡氏座標中，微小體積就是 dV = dx dy dz，三個邊都是長度。
但在球座標中，θ 與 φ 是角度不是長度，走一格角度實際走多遠取決於離軸多遠。
把三個邊長各自換算好，才會得到 dV = r² sinθ dr dθ dφ。

主體左半（約 60% 寬）｜pill 標籤：三個邊長的來源
- 畫一個三維球座標系（z 軸朝上，x、y 軸如常）。
- 畫出半徑為 r 的球面的一小塊（用淺灰色網格暗示球面），
  並在球面上某點 (r, θ, φ) 附近畫出一個放大的「曲面小盒子」。
- 小盒子的三個邊分別用不同顏色的粗線與雙箭頭標註：
    紅色（#C62828）：沿半徑方向，長度標為 dr
    綠色（#2E7D32）：沿 θ 方向的圓弧，長度標為 r dθ
    橘色（#EF6C00）：沿 φ 方向的圓弧，長度標為 r sinθ dφ
- 為了說明綠色邊：另畫一條從原點出發、半徑為 r 的大圓弧（綠色細線，
  位於包含 z 軸的平面上），標註「沿 θ 走的是半徑為 r 的大圓，弧長 = r dθ」。
- 為了說明橘色邊：把該點投影到 xy 平面，畫出半徑為 r sinθ 的小圓（橘色細線），
  並用灰色虛線標出投影距離 r sinθ，標註
  「沿 φ 走的是投影後半徑為 r sinθ 的小圓，弧長 = r sinθ dφ」。
  特別提醒：這裡的半徑不是 r，是 r sinθ。
- 小盒子旁放一個淺藍色公式盒：
    dV = (dr)(r dθ)(r sinθ dφ) = r² sinθ dr dθ dφ

主體右半（約 40% 寬）：兩個上下堆疊的說明卡。

卡 1｜pill 標籤：極座標積分的三個陷阱
  用三條紅色編號列出：
  1. 積分元素不是 dr dθ dφ，前面一定要帶 r² sinθ
  2. 上下限不同：r 從 0 到 ∞、θ 從 0 到 π、φ 從 0 到 2π
  3. 球殼機率的 r² 來自球殼面積，不能省略

卡 2｜pill 標籤：球殼機率
  公式：P(r) dr = r² |R|² dr　(6.25)
  推導提示（三行小字）：
    把 |Ψ|² = |R|²|Θ|²|Φ|² 乘上 dV，
    對 θ 積 0→π、對 φ 積 0→2π，
    Θ 與 Φ 已歸一化故兩個角度積分皆為 1。
  下方一行深藍粗體字：剩下的就是 r²|R|² dr。

右上角「圖例」方框：
  紅色 — 徑向邊 dr
  綠色 — θ 方向邊 r dθ（大圓，半徑 r）
  橘色 — φ 方向邊 r sinθ dφ（小圓，半徑 r sinθ）
  灰色虛線 — 投影輔助線

最下方一排粉彩公式盒（三個）：
1. 淺綠盒：θ → 0 或 π 時 sinθ → 0，說明「南北極的經線收攏成一點，體積趨近於零」
2. 淺藍盒：∫|Ψ|² dV = 1，說明「歸一化條件，全空間找到電子的機率為 100%」
3. 淺紫盒：|Φ|² = 1/(2π)，說明「與 φ 無關 → 機率分布必定對 z 軸旋轉對稱」
```

## English Prompt

```
Draw an educational infographic titled "where the three edge lengths of the
spherical volume element come from". ALL labels in TRADITIONAL CHINESE.

Title bar: 6.7  球座標的體積元素 (Volume Element in Spherical Coordinates)

Intro box (Traditional Chinese):
在卡氏座標中，微小體積就是 dV = dx dy dz，三個邊都是長度。
但在球座標中，θ 與 φ 是角度不是長度，走一格角度實際走多遠取決於離軸多遠。
把三個邊長各自換算好，才會得到 dV = r² sinθ dr dθ dφ。

LEFT ~60%, pill label 三個邊長的來源:
- A 3-D spherical frame (z up).
- A patch of the sphere of radius r suggested with a light grey mesh, and near a
  point (r, θ, φ) an enlarged curvilinear "box".
- The box's three edges drawn as thick coloured lines with double-headed arrows:
    red (#C62828) along the radius, labelled dr
    green (#2E7D32) along the θ arc, labelled r dθ
    orange (#EF6C00) along the φ arc, labelled r sinθ dφ
- To explain the green edge: draw a thin green great-circle arc of radius r from
  the origin, lying in the plane containing the z-axis, annotated
  沿 θ 走的是半徑為 r 的大圓，弧長 = r dθ.
- To explain the orange edge: project the point onto the xy-plane, draw the small
  circle of radius r sinθ (thin orange), with a grey dashed line marking the
  projected distance r sinθ, annotated
  沿 φ 走的是投影後半徑為 r sinθ 的小圓，弧長 = r sinθ dφ.
  Emphasise: 這裡的半徑不是 r，是 r sinθ.
- Beside the box, a light-blue formula box:
    dV = (dr)(r dθ)(r sinθ dφ) = r² sinθ dr dθ dφ

RIGHT ~40%: two stacked cards.

Card 1 pill: 極座標積分的三個陷阱
  three red numbered lines:
  1. 積分元素不是 dr dθ dφ，前面一定要帶 r² sinθ
  2. 上下限不同：r 從 0 到 ∞、θ 從 0 到 π、φ 從 0 到 2π
  3. 球殼機率的 r² 來自球殼面積，不能省略

Card 2 pill: 球殼機率
  formula: P(r) dr = r² |R|² dr  (6.25)
  three small hint lines:
    把 |Ψ|² = |R|²|Θ|²|Φ|² 乘上 dV，
    對 θ 積 0→π、對 φ 積 0→2π，
    Θ 與 Φ 已歸一化故兩個角度積分皆為 1。
  one dark-blue bold line: 剩下的就是 r²|R|² dr。

Top-right legend "圖例":
  紅色 — 徑向邊 dr
  綠色 — θ 方向邊 r dθ（大圓，半徑 r）
  橘色 — φ 方向邊 r sinθ dφ（小圓，半徑 r sinθ）
  灰色虛線 — 投影輔助線

Bottom pastel boxes (three):
1. light green: θ → 0 或 π 時 sinθ → 0 — 南北極的經線收攏成一點，體積趨近於零
2. light blue: ∫|Ψ|² dV = 1 — 歸一化條件，全空間找到電子的機率為 100%
3. light purple: |Φ|² = 1/(2π) — 與 φ 無關 → 機率分布必定對 z 軸旋轉對稱
```
