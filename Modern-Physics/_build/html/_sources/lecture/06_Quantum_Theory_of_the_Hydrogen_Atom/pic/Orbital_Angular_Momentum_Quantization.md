# Orbital_Angular_Momentum_Quantization.png

**對應章節：** 6.5 軌道量子數
**插入位置：**「假設與已知」之後、「推導：把總能量拆開代回 $(6.14)$」之前
**課本對應：** 課本 6.5 節配圖

> 產圖前請先貼上 `00_STYLE_GUIDE.md` 的風格區塊。

---

## 中文提示詞

```
請畫一張教學用資訊圖表，主題是「動能的徑向／切向分解，如何逼出角動量量子化」。

標題列文字：6.5  軌道角動量的量子化 (Quantization of the Orbital Angular Momentum)

導言框文字：
軌道量子數 l 來自 Θ 的方程式，卻同時出現在 R 的方程式裡——這件事給了關鍵線索。
既然 R 的方程式只能跟 r 有關，那些牽涉到非徑向資訊的項就必須互相抵消，
角動量的量子化條件因此被逼了出來。

主體分成左右兩大區。

【左區｜pill 標籤：動能的分解】
畫一個以原子核（紅色實心圓，標「原子核 +e」）為中心的示意圖。
外圍畫一條灰色虛線圓弧代表電子的機率分布區域。
在圓弧上某一點畫一個藍色小圓代表電子（標「電子 −e」），並從電子畫出兩個互相垂直的向量：
  - 綠色（#2E7D32）向量沿半徑方向（指離原子核），標為 v_radial，旁邊標 KE_radial
  - 橘色（#EF6C00）向量沿圓弧切線方向，標為 v_orbital，旁邊標 KE_orbital
兩向量之間畫直角符號。
從原子核到電子畫一條細線標為 r。
在電子上方另畫一個紫色（#7B1FA2）向量垂直於運動平面，標為角動量 L = m v_orbital r。
下方放一個淺綠色公式盒：KE = KE_radial + KE_orbital，
說明「兩個互相垂直的分量，動能可直接相加」。

【右區｜pill 標籤：抵消論證（本節的核心）】
畫成三個由上而下、以深藍箭頭串接的步驟框：

步驟框 1（淺藍）：把 E = KE + U 與 U = −e²/(4πε₀r) 代回 (6.14)，位能項恰好被消掉，得 (6.19)：
  (1/r²)d/dr[r²dR/dr] + (2m/ħ²)[ KE_radial + KE_orbital − l(l+1)ħ²/(2mr²) ]R = 0
  在方括號中把 KE_orbital 與 l(l+1)ħ²/(2mr²) 兩項各用一個紅色虛線圈起來。

步驟框 2（淺黃）：R 的方程式只能跟 r 有關 → 被紅圈圈起來的兩項必須互相抵消，得 (6.20)：
  KE_orbital = l(l+1)ħ²/(2mr²)
  旁邊小字：這是本章第三次用到「必須對所有 r 成立」的論證

步驟框 3（淺紫）：與古典結果 KE_orbital = L²/(2mr²) 比較，得 (6.21)：
  L = √(l(l+1)) ħ

在右區最下方放一條深藍橫幅，白字寫：
　角動量也被量子化了——而且不是波耳猜的 L = nħ

右上角「圖例」方框：
  綠色 — 徑向運動（KE_radial）
  橘色 — 切向運動（KE_orbital）
  紫色 — 角動量向量 L
  紅色虛線圈 — 必須互相抵消的非徑向項

最下方一排粉彩公式盒（四個）：
1. 淺綠盒：l = 0 → L = 0，說明「s 態電子沒有軌道角動量，波耳模型不允許這種狀態」
2. 淺藍盒：l = 1 → L = √2 ħ ≈ 1.414 ħ
3. 淺紫盒：l = 2 → L = √6 ħ ≈ 2.449 ħ
4. 淺紅盒：l = 0, 1, 2, …, (n−1)，說明「上限來自徑向方程式，見 6.3」
```

## English Prompt

```
Draw an educational infographic titled "how splitting the kinetic energy into
radial and tangential parts forces angular-momentum quantization".
ALL labels in TRADITIONAL CHINESE.

Title bar: 6.5  軌道角動量的量子化 (Quantization of the Orbital Angular Momentum)

Intro box (Traditional Chinese):
軌道量子數 l 來自 Θ 的方程式，卻同時出現在 R 的方程式裡——這件事給了關鍵線索。
既然 R 的方程式只能跟 r 有關，那些牽涉到非徑向資訊的項就必須互相抵消，
角動量的量子化條件因此被逼了出來。

LEFT region, pill label 動能的分解:
A schematic centred on the nucleus (red filled circle labelled 原子核 +e).
A grey dashed circular arc represents the electron's probability region.
On the arc, a small blue circle is the electron (labelled 電子 −e), with two
mutually perpendicular vectors drawn from it:
  - green (#2E7D32) along the radius pointing away from the nucleus, labelled
    v_radial, annotated KE_radial
  - orange (#EF6C00) along the arc tangent, labelled v_orbital, annotated KE_orbital
Draw a right-angle mark between them.
A thin line from nucleus to electron labelled r.
A purple (#7B1FA2) vector perpendicular to the orbital plane labelled
角動量 L = m v_orbital r.
Below, a light-green formula box: KE = KE_radial + KE_orbital
with caption 兩個互相垂直的分量，動能可直接相加.

RIGHT region, pill label 抵消論證（本節的核心）:
Three step boxes stacked top to bottom, joined by dark-blue arrows.

Step 1 (light blue): 把 E = KE + U 與 U = −e²/(4πε₀r) 代回 (6.14)，位能項恰好被消掉，得 (6.19)：
  (1/r²)d/dr[r²dR/dr] + (2m/ħ²)[ KE_radial + KE_orbital − l(l+1)ħ²/(2mr²) ]R = 0
  Circle BOTH KE_orbital and l(l+1)ħ²/(2mr²) inside the bracket with red dashed ovals.

Step 2 (light yellow): R 的方程式只能跟 r 有關 → 被紅圈圈起來的兩項必須互相抵消，得 (6.20)：
  KE_orbital = l(l+1)ħ²/(2mr²)
  small caption: 這是本章第三次用到「必須對所有 r 成立」的論證

Step 3 (light purple): 與古典結果 KE_orbital = L²/(2mr²) 比較，得 (6.21)：
  L = √(l(l+1)) ħ

A dark-blue banner at the bottom of the right region, white text:
　角動量也被量子化了——而且不是波耳猜的 L = nħ

Top-right legend "圖例":
  綠色 — 徑向運動（KE_radial）
  橘色 — 切向運動（KE_orbital）
  紫色 — 角動量向量 L
  紅色虛線圈 — 必須互相抵消的非徑向項

Bottom pastel boxes (four):
1. light green: l = 0 → L = 0 — s 態電子沒有軌道角動量，波耳模型不允許這種狀態
2. light blue: l = 1 → L = √2 ħ ≈ 1.414 ħ
3. light purple: l = 2 → L = √6 ħ ≈ 2.449 ħ
4. light red: l = 0, 1, 2, …, (n−1) — 上限來自徑向方程式，見 6.3
```
