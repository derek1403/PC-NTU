# LS_Coupling_and_Precession.png

**對應章節：** 7.8 總角動量
**插入位置：** $(7.20)$ 與 jj 耦合說明之後、「進動：三個圓錐（圖 7.18）」之前
**課本對應：** 圖 7.18（$\vec{J}$ 在外加磁場中進動）＋ 圖 7.19（例題 7.5 的 $\vec{L}$、$\vec{S}$ 合成方式）

> 產圖前請先貼上 `00_STYLE_GUIDE.md` 的風格區塊。

---

## 中文提示詞

```
【模型與符號】角動量箭頭、圓錐與進動是向量模型示意，不是可同時精確測得的三個分量或電子軌跡；z 為選定量子化軸。LS 耦合圖限自旋—軌道作用較弱的情況。

請畫一張教學用資訊圖表，主題是「LS 耦合：多電子的角動量怎麼合成，以及三個圓錐的進動」。

標題列文字：7.8  LS 耦合與進動 (LS Coupling and Precession)

導言框文字：
輕原子中，先把所有電子的軌道角動量合成 L、所有自旋合成 S，再合成 J = L + S。
L 與 S 以固定夾角繞著 J 進動；加上外加磁場後，J 再以固定夾角繞著 B 進動——
空間中是三個圓錐的連動，方向隨時間變，夾角永遠固定。

主體左側（約 40% 寬）｜pill 標籤：三個圓錐（圖 7.18）
畫一張三維示意圖（線條圖，不要陰影）：
  垂直向上的綠色粗箭頭，標「外加磁場 B（定義 z 軸）」。
  一支紫色向量 J 從原點斜向上，與 B 夾一個固定角度；
    以 B 為軸畫一個淡紫色大圓錐輪廓（J 的頭沿著圓錐底緣的圓轉動），
    圓上畫一支繞行方向的小箭頭，標「J 繞 B 緩慢進動」。
  藍色向量 L 與紅色向量 S 從原點出發、首尾相加等於 J；
    以 J 為軸畫兩個較小的圓錐輪廓：藍色圓錐（L 的軌跡）、紅色圓錐（S 的軌跡），
    各帶一個繞行小箭頭，標「L、S 繞 J 快速進動」。
  在 J 與 B 的夾角處標「cos θ = M_J / √(𝖩(𝖩+1))，由 M_J 決定」。
  小字：沒有外加磁場時只剩內側兩個圓錐，J 的方向固定（守恆）

主體右側（約 60% 寬）｜pill 標籤：例題 7.5：l₁ = 1、l₂ = 2 兩個電子（圖 7.19）
上半：「L₁ + L₂ → L」三個並排的小向量三角形（長度以 ħ 為單位、照比例）：
  每個三角形中，藍色 L₁ 長度 √2 ≈ 1.41、淺藍色 L₂ 長度 √6 ≈ 2.45，首尾相接，
  深藍色合向量 L 從原點指到末端：
    「𝖫 = 1」：|L| = √2 ≈ 1.41，L₁ 與 L₂ 夾角 150°
    「𝖫 = 2」：|L| = √6 ≈ 2.45，L₁ 與 L₂ 夾角 106.8°
    「𝖫 = 3」：|L| = √12 ≈ 3.46，L₁ 與 L₂ 夾角 54.7°
下半左：「S₁ + S₂ → S」兩個小圖（紅色 S₁、淡紅色 S₂，長度都是 √3/2 ≈ 0.87）：
    「𝖲 = 0」：S₁ 與 S₂ 方向相反、首尾相接回到原點，合向量長度 0
    「𝖲 = 1」：S₁ 與 S₂ 夾角 70.5°，合向量 S 長度 √2 ≈ 1.41
下半右：一個結論框：
    𝖫 ∈ {1, 2, 3}（從 |l₁ − l₂| 到 l₁ + l₂）
    𝖲 ∈ {0, 1}
    𝖩 ∈ {0, 1, 2, 3, 4}（從 |𝖫 − 𝖲| 到 𝖫 + 𝖲，取聯集）
  紅色小字：只要合向量不為零，L₁、L₂ 都不會與 L 平行

右上角「圖例」方框：
  綠色 — 外加磁場 B
  紫色 — 總角動量 J
  藍色系 — 軌道角動量（L₁、L₂、L）
  紅色系 — 自旋角動量（S₁、S₂、S）

最下方一排粉彩公式盒（三個）：
1. 淺藍盒：L = Σ Lᵢ，S = Σ Sᵢ，J = L + S　(7.19)，說明「LS 耦合：先各自加總，再合成」
2. 淺紫盒：L = √(𝖫(𝖫+1))ħ，S = √(𝖲(𝖲+1))ħ，J = √(𝖩(𝖩+1))ħ　(7.20)，說明「總量子數用無襯線大寫」
3. 淺黃盒：重原子：先 jᵢ = lᵢ + sᵢ，再 J = Σ jᵢ，說明「jj 耦合（自旋—軌道耦合很強時）」
```

## English Prompt

```
MODEL AND NOTATION: Angular-momentum arrows, cones and precession are vector-model schematics, not simultaneous sharp Cartesian components or electron trajectories. z is the chosen quantization axis. LS coupling assumes weak spin-orbit coupling.

Draw an educational infographic titled "LS coupling: how many-electron angular
momenta combine, and the precession of three cones". ALL labels in TRADITIONAL
CHINESE.

Title bar: 7.8  LS 耦合與進動 (LS Coupling and Precession)

Intro box (Traditional Chinese):
輕原子中，先把所有電子的軌道角動量合成 L、所有自旋合成 S，再合成 J = L + S。
L 與 S 以固定夾角繞著 J 進動；加上外加磁場後，J 再以固定夾角繞著 B 進動——
空間中是三個圓錐的連動，方向隨時間變，夾角永遠固定。

LEFT ~40%, pill label 三個圓錐（圖 7.18）:
A 3D line sketch (no shading):
  a thick GREEN arrow pointing straight up, labelled 外加磁場 B（定義 z 軸）.
  a PURPLE vector J from the origin, tilted at a fixed angle to B;
    a large faint-purple cone outline about B (the tip of J runs around the cone's
    rim circle), with a small circulating arrow labelled J 繞 B 緩慢進動.
  a BLUE vector L and a RED vector S from the origin, adding head-to-tail to J;
    two smaller cone outlines about J: a blue cone (locus of L) and a red cone
    (locus of S), each with a small circulating arrow, labelled L、S 繞 J 快速進動.
  at the angle between J and B: cos θ = M_J / √(𝖩(𝖩+1))，由 M_J 決定.
  small note: 沒有外加磁場時只剩內側兩個圓錐，J 的方向固定（守恆）

RIGHT ~60%, pill label 例題 7.5：l₁ = 1、l₂ = 2 兩個電子（圖 7.19）:
Upper half, "L₁ + L₂ → L": three small vector triangles side by side (lengths in
units of ħ, TO SCALE). In each, a BLUE L₁ of length √2 ≈ 1.41 and a LIGHT-BLUE L₂
of length √6 ≈ 2.45 are joined head-to-tail, and a DARK-BLUE resultant L runs from
the origin to the end:
    𝖫 = 1: |L| = √2 ≈ 1.41, angle between L₁ and L₂ = 150°
    𝖫 = 2: |L| = √6 ≈ 2.45, angle between L₁ and L₂ = 106.8°
    𝖫 = 3: |L| = √12 ≈ 3.46, angle between L₁ and L₂ = 54.7°
Lower-left, "S₁ + S₂ → S": two small diagrams (RED S₁ and LIGHT-RED S₂, each of
length √3/2 ≈ 0.87):
    𝖲 = 0: S₁ and S₂ point in opposite directions and close back to the origin; resultant length 0
    𝖲 = 1: S₁ and S₂ at 70.5° to each other; resultant S of length √2 ≈ 1.41
Lower-right, a conclusion box:
    𝖫 ∈ {1, 2, 3}（從 |l₁ − l₂| 到 l₁ + l₂）
    𝖲 ∈ {0, 1}
    𝖩 ∈ {0, 1, 2, 3, 4}（從 |𝖫 − 𝖲| 到 𝖫 + 𝖲，取聯集）
  small red note: 只要合向量不為零，L₁、L₂ 都不會與 L 平行

Top-right legend "圖例":
  綠色 — 外加磁場 B
  紫色 — 總角動量 J
  藍色系 — 軌道角動量（L₁、L₂、L）
  紅色系 — 自旋角動量（S₁、S₂、S）

Bottom pastel formula boxes (three):
1. light blue: L = Σ Lᵢ, S = Σ Sᵢ, J = L + S  (7.19) — LS 耦合：先各自加總，再合成
2. light purple: L = √(𝖫(𝖫+1))ħ, S = √(𝖲(𝖲+1))ħ, J = √(𝖩(𝖩+1))ħ  (7.20) — 總量子數用無襯線大寫
3. light yellow: 重原子：先 jᵢ = lᵢ + sᵢ，再 J = Σ jᵢ — jj 耦合（自旋—軌道耦合很強時）
```
