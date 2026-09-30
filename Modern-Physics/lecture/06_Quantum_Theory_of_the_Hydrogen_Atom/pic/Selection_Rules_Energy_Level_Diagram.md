# Selection_Rules_Energy_Level_Diagram.png

**對應章節：** 6.9 選擇規則
**插入位置：**「假設與已知」之後、「推導：$m_l$ 的選擇規則」之前
**課本對應：** 圖 6.13

> 產圖前請先貼上 `00_STYLE_GUIDE.md` 的風格區塊。

---

## 中文提示詞

```
請畫一張教學用資訊圖表，主題是「選擇規則 Δl = ±1 允許哪些躍遷」。

標題列文字：6.9  選擇規則與允許的躍遷 (Selection Rules and Allowed Transitions)

導言框文字：
躍遷偶極積分大部分時候都等於零——不等於零反而是例外。
薛丁格方程式屬於 Sturm–Liouville 方程式，本徵函數天生正交；
插進一個 r 之後，只有 Δl = ±1、Δm_l = 0, ±1 的少數組合逃過一劫。

主體左半（約 65% 寬）｜pill 標籤：氫原子能階圖（Δl = ±1）
- 畫一張 Grotrian 型能階圖。
- 橫軸分成四個直欄，由左到右標為 l = 0 (s)、l = 1 (p)、l = 2 (d)、l = 3 (f)，
  各欄用不同顏色（綠 #2E7D32、藍 #1565C0、紫 #7B1FA2、橘 #EF6C00）作為欄標題底色。
- 縱軸為激發能量（相對基態，單位 eV），向上為正；最上方畫一條 E = 13.6 eV 的
  水平虛線標為「游離極限」。
- 在各欄畫出對應的能階水平短線，並標 n 值：
    l=0 欄：1s（能量 0，最下方）、2s、3s、4s
    l=1 欄：2p、3p、4p
    l=2 欄：3d、4d
    l=3 欄：4f
  能階高度必須正確反映 E_n = −13.6/n² eV（同一個 n 的不同 l 高度相同）。
- 用**藍色實線箭頭**畫出所有滿足 Δl = ±1 的允許躍遷（由上往下），至少包含：
    2p→1s、3p→1s、4p→1s（萊曼系）
    3s→2p、3d→2p、4s→2p、4d→2p（巴耳末系）
    4f→3d、4p→3d、4s→3p、4d→3p
- 用**灰色虛線箭頭並打上紅色 ✗** 畫出兩條被禁止的躍遷作為對比：
    2s→1s（Δl = 0，禁止）
    3d→1s（Δl = −2，禁止）
- 在圖的一角標註：選擇規則完全不限制 n，n 可以從任何值跳到任何值。

主體右半（約 35% 寬）：三個上下堆疊的說明卡。

卡 1｜pill 標籤：兩條規則
  大字置中：Δl = ±1　(6.36)
  大字置中：Δm_l = 0, ±1　(6.37)
  紅色小字：兩條必須「同時」滿足，積分才不為零，躍遷才會放光。

卡 2｜pill 標籤：Δm_l 從哪裡來（φ 積分）
  z 分量：∫₀^2π e^{i(m_l − m_l′)φ} dφ ≠ 0 只在 Δm_l = 0
  x、y 分量：cosφ = (e^{iφ} + e^{−iφ})/2 → 只在 Δm_l = ±1
  小字：這一步是完全精確的，沒有任何近似。

卡 3｜pill 標籤：Δl 從哪裡來（θ 積分）
  換元 x = cosθ 之後，積分變成 ∫₋₁¹ P_{l′}^{m} (x) · x · P_l^{m}(x) dx
  三個理由並列（各一行，用不同顏色）：
    綠：次數守恆 — 乘一個 x 只能把多項式次數推高一階
    紫：帶權正交性 — 正交多項式對低次多項式積分為零
    橘：宇稱 — x 是奇函數，把 l′ = l 的配對打掉
  結論：只剩 l′ = l ± 1。

右上角「圖例」方框：
  藍色實線箭頭 — 允許的躍遷（Δl = ±1）
  灰色虛線箭頭 + 紅 ✗ — 被選擇規則禁止的躍遷
  四種欄位顏色 — l = 0, 1, 2, 3

最下方一排粉彩公式盒（三個）：
1. 淺綠盒：Δl = 0 不允許，說明「s 態只能跳到 p 態，不能跳到另一個 s 態」
2. 淺藍盒：選擇規則不限制 n，說明「所以萊曼系可以從任何 np 掉到 1s」
3. 淺紅盒：不滿足選擇規則 ≠ 躍遷不會發生，說明「只是不會伴隨輻射，仍可透過碰撞等機制發生」
```

## English Prompt

```
Draw an educational infographic titled "which transitions the selection rule
Δl = ±1 allows". ALL labels in TRADITIONAL CHINESE.

Title bar: 6.9  選擇規則與允許的躍遷 (Selection Rules and Allowed Transitions)

Intro box (Traditional Chinese):
躍遷偶極積分大部分時候都等於零——不等於零反而是例外。
薛丁格方程式屬於 Sturm–Liouville 方程式，本徵函數天生正交；
插進一個 r 之後，只有 Δl = ±1、Δm_l = 0, ±1 的少數組合逃過一劫。

LEFT ~65%, pill label 氫原子能階圖（Δl = ±1）:
- A Grotrian-style level diagram.
- Four vertical columns labelled l = 0 (s), l = 1 (p), l = 2 (d), l = 3 (f),
  column headers filled green #2E7D32, blue #1565C0, purple #7B1FA2, orange #EF6C00.
- Vertical axis: excitation energy above the ground state in eV, positive up;
  a dashed horizontal line at E = 13.6 eV labelled 游離極限.
- Short horizontal level lines in each column, labelled by n:
    l=0 column: 1s (at 0, bottom), 2s, 3s, 4s
    l=1 column: 2p, 3p, 4p
    l=2 column: 3d, 4d
    l=3 column: 4f
  Heights must correctly follow E_n = −13.6/n² eV (same n ⇒ same height across columns).
- BLUE SOLID arrows for every allowed Δl = ±1 transition (downward), at least:
    2p→1s, 3p→1s, 4p→1s (萊曼系)
    3s→2p, 3d→2p, 4s→2p, 4d→2p (巴耳末系)
    4f→3d, 4p→3d, 4s→3p, 4d→3p
- GREY DASHED arrows with a red ✗ for two forbidden transitions, as contrast:
    2s→1s (Δl = 0，禁止)
    3d→1s (Δl = −2，禁止)
- A corner note: 選擇規則完全不限制 n，n 可以從任何值跳到任何值。

RIGHT ~35%: three stacked cards.

Card 1 pill: 兩條規則
  large centred: Δl = ±1  (6.36)
  large centred: Δm_l = 0, ±1  (6.37)
  small red: 兩條必須「同時」滿足，積分才不為零，躍遷才會放光。

Card 2 pill: Δm_l 從哪裡來（φ 積分）
  z 分量：∫₀^2π e^{i(m_l − m_l′)φ} dφ ≠ 0 只在 Δm_l = 0
  x、y 分量：cosφ = (e^{iφ} + e^{−iφ})/2 → 只在 Δm_l = ±1
  small: 這一步是完全精確的，沒有任何近似。

Card 3 pill: Δl 從哪裡來（θ 積分）
  換元 x = cosθ 之後，積分變成 ∫₋₁¹ P_{l′}^{m}(x) · x · P_l^{m}(x) dx
  three coloured reasons, one line each:
    green: 次數守恆 — 乘一個 x 只能把多項式次數推高一階
    purple: 帶權正交性 — 正交多項式對低次多項式積分為零
    orange: 宇稱 — x 是奇函數，把 l′ = l 的配對打掉
  conclusion: 只剩 l′ = l ± 1。

Top-right legend "圖例":
  藍色實線箭頭 — 允許的躍遷（Δl = ±1）
  灰色虛線箭頭 + 紅 ✗ — 被選擇規則禁止的躍遷
  四種欄位顏色 — l = 0, 1, 2, 3

Bottom pastel boxes (three):
1. light green: Δl = 0 不允許 — s 態只能跳到 p 態，不能跳到另一個 s 態
2. light blue: 選擇規則不限制 n — 所以萊曼系可以從任何 np 掉到 1s
3. light red: 不滿足選擇規則 ≠ 躍遷不會發生 — 只是不會伴隨輻射，仍可透過碰撞等機制發生
```
