# Total_Angular_Momentum_Vector_Addition.png

**對應章節：** 7.8 總角動量
**插入位置：** $(7.18)$ 之後、「推導：$\vec{L}$ 與 $\vec{S}$ 的夾角是固定的」之前
**課本對應：** 圖 7.15（$l = 1$ 時 $\vec{L}$ 與 $\vec{S}$ 合成 $\vec{J}$ 的兩種方式）＋ 圖 7.16（$\vec{J}$ 的空間量子化）

> 產圖前請先貼上 `00_STYLE_GUIDE.md` 的風格區塊。

---

## 中文提示詞

```
【模型與符號】角動量箭頭、圓錐與進動是向量模型示意，不是可同時精確測得的三個分量或電子軌跡；z 為選定量子化軸。LS 耦合圖限自旋—軌道作用較弱的情況。

請畫一張教學用資訊圖表，主題是「J = L + S：大小與方向都被量子化（以 l = 1 為例）」。

標題列文字：7.8  總角動量的向量合成 (Adding L and S into J)

導言框文字：
總角動量是軌道與自旋角動量的向量和 J = L + S。三個向量的長度都被量子化，
三角形三邊固定，L 與 S 的夾角也就固定了；所謂「平行」「反平行」其實都不是真的平行。
J 的方向同樣被量子化：J 在 z 軸上的投影只能是 m_j ħ。

主體左半（約 50% 寬）｜pill 標籤：兩種合成方式（圖 7.15）
畫兩個並排的向量三角形，長度以 ħ 為單位、**必須照比例**：
  左三角形，標題「j = 3/2」：
    藍色向量 L：長度 √2 ≈ 1.41，從原點出發；
    紅色向量 S：長度 √3/2 ≈ 0.87，接在 L 的箭頭後方；
    紫色向量 J：長度 √15/2 ≈ 1.94，從原點指到 S 的箭頭端。
    L 與 S 之間的夾角（兩向量尾對尾時）為 65.9°，在圖上用小弧標出「65.9°」。
    旁註「S 與 L『大致同向』」。
  右三角形，標題「j = 1/2」：
    藍色 L：長度 1.41；紅色 S：長度 0.87；紫色 J：長度 √3/2 ≈ 0.87。
    L 與 S 的夾角為 144.7°，標出「144.7°」。
    旁註「S 與 L『大致反向』，但不是 180°」。
  兩個三角形下方共用一張小表：
    |L| = √(l(l+1)) ħ = √2 ħ　|S| = √(s(s+1)) ħ = (√3/2) ħ
    j = 3/2：|J| = (√15/2) ħ，L·S = +ħ²/2
    j = 1/2：|J| = (√3/2) ħ，L·S = −ħ²
  紅色小字：三邊長度固定 → 夾角固定（國中幾何）

主體右半（約 50% 寬）｜pill 標籤：J 的空間量子化（圖 7.16）
畫兩張並排的「圓錐圖」，都以垂直向上的 z 軸為中心（深藍色，旁標「z（磁場方向）」）：
  左圖「j = 3/2：四個轉向」：
    以原點為圓心畫一個半徑 1.94 的淺灰虛線半圓（向量長度的軌跡）。
    四支紫色向量，長度都是 1.94，在 z 軸上的投影分別為 +3/2、+1/2、−1/2、−3/2，
    與 +z 軸的夾角分別為 39.2°、75.0°、105.0°、140.8°。
    在 z 軸上用水平虛線標出四個投影點，並標 m_j = +3/2, +1/2, −1/2, −3/2。
    每支向量畫出以 z 軸為軸的淡紫色圓錐輪廓，表示向量可以落在圓錐上任何位置。
  右圖「j = 1/2：兩個轉向」：
    半徑 0.87 的虛線半圓；兩支紫色向量，長度 0.87，投影 +1/2、−1/2，
    與 +z 軸的夾角 54.7°、125.3°。
  兩張圖的長度比例必須一致（j = 3/2 的向量明顯較長）。
  紅色小字：沒有任何一支 J 剛好沿著 z 軸；沒有磁場時 z 軸無意義

右上角「圖例」方框：
  藍色 — 軌道角動量 L
  紅色 — 自旋角動量 S
  紫色 — 總角動量 J
  灰色虛線半圓 — 向量長度的軌跡

最下方一排粉彩公式盒（三個）：
1. 淺紫盒：J = L + S　(7.16)，說明「總角動量是向量和」
2. 淺藍盒：J = √(j(j+1)) ħ，j = l ± 1/2　(7.17)，說明「由最大投影與數態數目推出」
3. 淺黃盒：J_z = m_j ħ，m_j = −j, …, +j　(7.18)，說明「方向的量子化：共 2j + 1 個」
```

## English Prompt

```
MODEL AND NOTATION: Angular-momentum arrows, cones and precession are vector-model schematics, not simultaneous sharp Cartesian components or electron trajectories. z is the chosen quantization axis. LS coupling assumes weak spin-orbit coupling.

Draw an educational infographic titled "J = L + S: both magnitude and direction
are quantized (example l = 1)". ALL labels in TRADITIONAL CHINESE.

Title bar: 7.8  總角動量的向量合成 (Adding L and S into J)

Intro box (Traditional Chinese):
總角動量是軌道與自旋角動量的向量和 J = L + S。三個向量的長度都被量子化，
三角形三邊固定，L 與 S 的夾角也就固定了；所謂「平行」「反平行」其實都不是真的平行。
J 的方向同樣被量子化：J 在 z 軸上的投影只能是 m_j ħ。

LEFT ~50%, pill label 兩種合成方式（圖 7.15）:
Two vector triangles side by side, lengths in units of ħ and DRAWN TO SCALE:
  left triangle, heading j = 3/2:
    BLUE vector L, length √2 ≈ 1.41, from the origin;
    RED vector S, length √3/2 ≈ 0.87, attached head-to-tail after L;
    PURPLE vector J, length √15/2 ≈ 1.94, from the origin to the tip of S.
    The angle between L and S (tail to tail) is 65.9°, marked with a small arc "65.9°".
    side note S 與 L『大致同向』.
  right triangle, heading j = 1/2:
    blue L length 1.41; red S length 0.87; purple J length √3/2 ≈ 0.87.
    The angle between L and S is 144.7°, marked "144.7°".
    side note S 與 L『大致反向』，但不是 180°.
  A shared mini table under both triangles:
    |L| = √(l(l+1)) ħ = √2 ħ   |S| = √(s(s+1)) ħ = (√3/2) ħ
    j = 3/2：|J| = (√15/2) ħ，L·S = +ħ²/2
    j = 1/2：|J| = (√3/2) ħ，L·S = −ħ²
  small red note: 三邊長度固定 → 夾角固定（國中幾何）

RIGHT ~50%, pill label J 的空間量子化（圖 7.16）:
Two side-by-side "cone diagrams", each centred on a vertical dark-blue z axis
labelled z（磁場方向）:
  left diagram j = 3/2：四個轉向:
    a light-grey dashed half-circle of radius 1.94 centred at the origin (locus of
    the vector tip).
    four PURPLE vectors, all of length 1.94, with z-projections +3/2, +1/2, −1/2,
    −3/2 and angles from +z of 39.2°, 75.0°, 105.0°, 140.8°.
    horizontal dashed lines mark the four projection points on the z axis, labelled
    m_j = +3/2, +1/2, −1/2, −3/2.
    for each vector a faint purple cone outline about the z axis, showing the
    vector can lie anywhere on that cone.
  right diagram j = 1/2：兩個轉向:
    dashed half-circle of radius 0.87; two purple vectors of length 0.87 with
    projections +1/2 and −1/2, at 54.7° and 125.3° from +z.
  Both diagrams use the SAME length scale (the j = 3/2 vectors are clearly longer).
  small red note: 沒有任何一支 J 剛好沿著 z 軸；沒有磁場時 z 軸無意義

Top-right legend "圖例":
  藍色 — 軌道角動量 L
  紅色 — 自旋角動量 S
  紫色 — 總角動量 J
  灰色虛線半圓 — 向量長度的軌跡

Bottom pastel formula boxes (three):
1. light purple: J = L + S  (7.16) — 總角動量是向量和
2. light blue: J = √(j(j+1)) ħ, j = l ± 1/2  (7.17) — 由最大投影與數態數目推出
3. light yellow: J_z = m_j ħ, m_j = −j, …, +j  (7.18) — 方向的量子化：共 2j + 1 個
```
