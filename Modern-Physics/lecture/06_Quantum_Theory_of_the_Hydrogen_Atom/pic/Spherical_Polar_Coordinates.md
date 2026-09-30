# Spherical_Polar_Coordinates.png

**對應章節：** 6.1 氫原子的薛丁格方程式
**插入位置：** 「氫原子的庫侖位能」公式 $(6.2)$ 之後、「為什麼不能用卡氏座標硬解」之前
**課本對應：** 圖 6.1

> 產圖前請先貼上 `00_STYLE_GUIDE.md` 的風格區塊。

---

## 中文提示詞

```
請畫一張教學用資訊圖表，主題是「球狀極座標與卡氏座標的關係」。

標題列文字：6.1  球狀極座標 (Spherical Polar Coordinates)

導言框文字（淺藍框內）：
宇宙中大部分的交互作用都是點對點的，因而天生球狀對稱。
氫原子的庫侖位能只依賴距離 r，若用卡氏座標會寫成 (x²+y²+z²)^(−1/2)，
把三個變數綁死；改用球座標後位能只剩一個變數，方程式才解得下去。

主體分成左中右三格，各自上方掛一個深藍 pill 標籤：

【左格】pill 標籤：(a) 座標定義
畫一個三維直角座標系，三軸標為 x、y、z（z 軸朝上，x 軸朝左前方，y 軸朝右）。
從原點 O 拉出一條藍色（#1565C0）向量到空間中一點 P，向量長度標為 r。
- 標出 r 與 z 軸之間的夾角，用綠色（#2E7D32）弧線標為 θ（天頂角）。
- 把該向量往 xy 平面投影，畫成灰色虛線；投影線長度標為 r sinθ。
- 標出投影線與 x 軸之間的夾角，用橘色（#EF6C00）弧線標為 φ（方位角）。
- 用細灰虛線畫出 P 點到三個座標軸的垂足，標出 x、y、z 三個分量。
右下角放一個淺藍色公式盒，內容為三條轉換式：
  x = r sinθ cosφ
  y = r sinθ sinφ
  z = r cosθ
並附一行小字：只需三個變數即可定義三維空間中的一點。

【中格】pill 標籤：(b) 固定 θ 的軌跡
同一個三維座標系。以 z 軸為中心軸畫一個綠色（#2E7D32）圓錐面（半透明），
圓錐的半頂角標為 θ。在球面上把圓錐與球面相交所得的「緯線圓」用綠色粗線畫出來，
並用箭頭標註：此圓所在的平面垂直於 z 軸。
小字說明：固定 θ 時，向量可指向這個圓上的任何一點。

【右格】pill 標籤：(c) 固定 φ 的軌跡
同一個三維座標系。畫一個橘色（#EF6C00）半平面，該半平面包含整條 z 軸，
與 xz 平面的夾角標為 φ。半平面與球面相交所得的「經線半圓」用橘色粗線畫出來。
小字說明：固定 φ 時，向量落在這個包含 z 軸的半平面上。

右上角放「圖例」方框：
  藍色實線 — 位置向量 r
  綠色 — 天頂角 θ（與 z 軸的夾角），0 ≤ θ ≤ π
  橘色 — 方位角 φ（投影後與 x 軸的夾角），0 ≤ φ < 2π
  灰色虛線 — 投影輔助線

最下方一排粉彩公式盒（四個）：
1. 淺綠盒：r = (x²+y²+z²)^(1/2)，說明「到原點的距離，單位 m」
2. 淺紫盒：0 ≤ θ ≤ π，說明「天頂角只跑半圈，從北極到南極」
3. 淺藍盒：0 ≤ φ < 2π，說明「方位角繞完整一圈，φ 與 φ+2π 是同一點」
4. 淺紅盒：U = −e²/(4πε₀r)，說明「庫侖位能只依賴 r 一個變數」
```

## English Prompt

```
Draw an educational infographic on "Spherical polar coordinates and their
relation to Cartesian coordinates". ALL labels in TRADITIONAL CHINESE.

Title bar text: 6.1  球狀極座標 (Spherical Polar Coordinates)

Intro box (light blue) text, in Traditional Chinese:
宇宙中大部分的交互作用都是點對點的，因而天生球狀對稱。
氫原子的庫侖位能只依賴距離 r，若用卡氏座標會寫成 (x²+y²+z²)^(−1/2)，
把三個變數綁死；改用球座標後位能只剩一個變數，方程式才解得下去。

Main area split into three panels, each with a dark-blue pill label above it:

[LEFT] pill: (a) 座標定義
A 3-D Cartesian frame with axes x, y, z (z up, x toward lower-left front,
y to the right). A blue (#1565C0) vector from origin O to a point P, length
labelled r.
- Green (#2E7D32) arc marking the angle between r and the z-axis, labelled θ.
- Grey dashed projection of the vector onto the xy-plane; its length labelled
  r sinθ.
- Orange (#EF6C00) arc marking the angle between that projection and the x-axis,
  labelled φ.
- Thin grey dashed drop lines from P to each axis, with x, y, z components marked.
A light-blue formula box in the lower right with the three transformations:
  x = r sinθ cosφ ; y = r sinθ sinφ ; z = r cosθ
plus one small Chinese line: 只需三個變數即可定義三維空間中的一點。

[MIDDLE] pill: (b) 固定 θ 的軌跡
Same frame. A semi-transparent green (#2E7D32) cone about the z-axis, half-apex
angle labelled θ. Its intersection with the sphere — a latitude circle — drawn
as a thick green curve, with an arrow noting that this circle's plane is
perpendicular to the z-axis.
Caption: 固定 θ 時，向量可指向這個圓上的任何一點。

[RIGHT] pill: (c) 固定 φ 的軌跡
Same frame. A semi-transparent orange (#EF6C00) half-plane containing the entire
z-axis, its angle from the xz-plane labelled φ. Its intersection with the sphere
— a meridian semicircle — drawn as a thick orange curve.
Caption: 固定 φ 時，向量落在這個包含 z 軸的半平面上。

Top-right legend box "圖例":
  藍色實線 — 位置向量 r
  綠色 — 天頂角 θ（與 z 軸的夾角），0 ≤ θ ≤ π
  橘色 — 方位角 φ（投影後與 x 軸的夾角），0 ≤ φ < 2π
  灰色虛線 — 投影輔助線

Bottom pastel formula boxes (four):
1. light green: r = (x²+y²+z²)^(1/2) — 到原點的距離，單位 m
2. light purple: 0 ≤ θ ≤ π — 天頂角只跑半圈，從北極到南極
3. light blue: 0 ≤ φ < 2π — 方位角繞完整一圈，φ 與 φ+2π 是同一點
4. light red: U = −e²/(4πε₀r) — 庫侖位能只依賴 r 一個變數
```
