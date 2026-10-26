# Exchange_Symmetry_and_Pauli.png

**對應章節：** 7.3 對稱及反對稱波函數
**插入位置：** $(7.11)$、$(7.12)$ 與歸一化推導之後、「推導：反對稱 $\Longrightarrow$ 不相容原理」之前
**課本對應：** 無（自製概念圖）

> 產圖前請先貼上 `00_STYLE_GUIDE.md` 的風格區塊。

---

## 中文提示詞

```
【模型與符號】交換作用於完整的空間與自旋標記；電子總態反對稱由自旋—統計關係給定，不能只從機率密度相等推出。

請畫一張教學用資訊圖表，主題是「全同粒子不可分辨 → 對稱／反對稱波函數 → 包立不相容原理」。

標題列文字：7.3  交換對稱性與不相容原理 (Exchange Symmetry and the Exclusion Principle)

導言框文字：
兩個電子的波函數會重疊，沒有軌跡可追，原則上無法分辨誰是一號、誰是二號。
在通常三維空間中，取交換算符的本徵態；交換兩次回到原態，因此交換本徵值為 ±1。
電子屬於反對稱，於是兩個電子不能處於同一量子態。

主體上排左（約 30% 寬）｜pill 標籤：古典 vs 量子
  上半：兩顆撞球（藍色標「1」、紅色標「2」）沿兩條清楚的虛線軌跡靠近後分開，
        標「古典：盯著軌跡就分得出來」。
  下半：兩團半透明的灰色波包互相重疊成一團再分開，分開後兩團都標「?」，
        標「量子：波函數重疊，無法追蹤——全同粒子」。

主體上排中（約 35% 寬）｜pill 標籤：只有兩種可能
  一條由上而下的推導鏈（三個圓角框以箭頭相連）：
    框 1：假設：P₁₂ψ = e^{iα}ψ；因此 |ψ(2,1)|² = |ψ(1,2)|²
    框 2：再交換一次回到原狀：ψ(1,2) = e^{2iα} ψ(1,2)　→　e^{2iα} = 1
    框 3：e^{iα} = ±1
  框 3 下方分成左右兩個結果：
    綠色框：對稱 ψ(2,1) = +ψ(1,2)　(7.7)
    紅色框：反對稱 ψ(2,1) = −ψ(1,2)　(7.8)

主體上排右（約 35% 寬）｜pill 標籤：兩粒子波函數
  兩條公式（大字、排版清楚）：
    綠色：ψ_S = (1/√2)[ψ_a(1)ψ_b(2) + ψ_a(2)ψ_b(1)]　(7.11)
    紅色：ψ_A = (1/√2)[ψ_a(1)ψ_b(2) − ψ_a(2)ψ_b(1)]　(7.12)
  小字：a ≠ b 且單粒子態正交歸一時，係數才是 1/√2；同態玻色子須重新歸一化。

主體下排｜pill 標籤：一維箱中的兩粒子機率密度
兩張並排熱圖，橫軸 x₁、縱軸 x₂，範圍 0 至 L。
取 ψ_a(x)=√(2/L)sin(πx/L)、ψ_b(x)=√(2/L)sin(2πx/L)，
依上方正交雙態公式實際計算 |ψ_S|² 與 |ψ_A|²，不指定任意峰值位置或相同峰高。
左圖綠框「對稱空間態」；右圖紅框「反對稱空間態」。
共用白→淺藍→深藍色階，白色為零、深藍為高密度，單位 L⁻²。
兩圖以細灰虛線標 x₁=x₂；反對稱圖整條對角線為零。
對稱圖的對角線不是處處非零：在端點與 x₁=x₂=L/2 也為零。
旁註：此例兩個正交空間態各佔一粒子；費米子空間反對稱的示意假設自旋部分對稱。
不把空間對稱性直接等同於任意電子總態，也不畫普遍的同態機率倍數。

右上角「圖例」方框：
  綠色 — 對稱／玻色子
  紅色 — 反對稱／費米子
  灰色虛線 — x₁ = x₂（兩粒子在同一處）

最下方一排粉彩公式盒（三個）：
1. 淺紅盒：a = b ⇒ ψ_A = (1/√2)[ψ_a(1)ψ_a(2) − ψ_a(2)ψ_a(1)] = 0，說明「兩個電子不能同態——包立不相容原理」
2. 淺綠盒：費米子：自旋 1/2, 3/2, …，反對稱，費米—狄拉克分布，說明「電子、質子、中子」
3. 淺紫盒：玻色子：自旋 0, 1, 2, …，對稱，玻色—愛因斯坦分布，說明「光子、氦-4、聲子」
```

## English Prompt

```
MODEL AND NOTATION: Exchange acts on full space-and-spin labels. Electronic total-state antisymmetry uses spin-statistics, not probability-density equality alone.

Draw an educational infographic titled "indistinguishable particles →
symmetric / antisymmetric wave functions → the exclusion principle".
ALL labels in TRADITIONAL CHINESE.

Title bar: 7.3  交換對稱性與不相容原理 (Exchange Symmetry and the Exclusion Principle)

Intro box (Traditional Chinese):
兩個電子的波函數會重疊，沒有軌跡可追，原則上無法分辨誰是一號、誰是二號。
在通常三維空間中，取交換算符的本徵態；交換兩次回到原態，因此交換本徵值為 ±1。
電子屬於反對稱，於是兩個電子不能處於同一量子態。

TOP ROW LEFT (~30%), pill label 古典 vs 量子:
  upper half: two billiard balls (blue "1", red "2") approach and separate along
    two clearly drawn dashed trajectories, caption 古典：盯著軌跡就分得出來.
  lower half: two semi-transparent grey wave packets overlap into one blob and
    separate again; both outgoing packets are labelled "?", caption
    量子：波函數重疊，無法追蹤——全同粒子.

TOP ROW CENTRE (~35%), pill label 只有兩種可能:
  a top-to-bottom derivation chain of three rounded boxes joined by arrows:
    box 1: 假設：P₁₂ψ = e^{iα}ψ；因此 |ψ(2,1)|² = |ψ(1,2)|²
    box 2: 再交換一次回到原狀：ψ(1,2) = e^{2iα} ψ(1,2)  →  e^{2iα} = 1
    box 3: e^{iα} = ±1
  below box 3, two outcomes side by side:
    green box: 對稱 ψ(2,1) = +ψ(1,2)  (7.7)
    red box: 反對稱 ψ(2,1) = −ψ(1,2)  (7.8)

TOP ROW RIGHT (~35%), pill label 兩粒子波函數:
  two large, cleanly typeset formulas:
    green: ψ_S = (1/√2)[ψ_a(1)ψ_b(2) + ψ_a(2)ψ_b(1)]  (7.11)
    red: ψ_A = (1/√2)[ψ_a(1)ψ_b(2) − ψ_a(2)ψ_b(1)]  (7.12)
  small note: a ≠ b 且單粒子態正交歸一時，係數才是 1/√2；同態玻色子須重新歸一化。

BOTTOM ROW, pill label 一維箱中的兩粒子機率密度:
Two square maps, x₁ horizontally and x₂ vertically, both 0 to L.
Use ψ_a(x)=√(2/L)sin(πx/L), ψ_b(x)=√(2/L)sin(2πx/L).
Calculate |ψ_S|² and |ψ_A|² from the normalized orthogonal-state formulas.
Do not prescribe arbitrary peak locations or equal peak heights.
Green frame 對稱空間態; red frame 反對稱空間態.
Shared white→light blue→dark blue scale: white zero, dark blue high density, units L⁻².
Thin GREY dashed x₁=x₂. The antisymmetric diagonal is entirely zero.
The symmetric diagonal also has zeros at both endpoints and at x₁=x₂=L/2.
Caption: 此例兩個正交空間態各佔一粒子；費米子空間反對稱的示意假設自旋部分對稱.
Distinguish spatial symmetry from full electronic symmetry including spin.
Do not show a universal same-state probability multiplier.

Top-right legend "圖例":
  綠色 — 對稱／玻色子
  紅色 — 反對稱／費米子
  灰色虛線 — x₁ = x₂（兩粒子在同一處）

Bottom pastel formula boxes (three):
1. light red: a = b ⇒ ψ_A = (1/√2)[ψ_a(1)ψ_a(2) − ψ_a(2)ψ_a(1)] = 0 — 兩個電子不能同態——包立不相容原理
2. light green: 費米子：自旋 1/2, 3/2, …，反對稱，費米—狄拉克分布 — 電子、質子、中子
3. light purple: 玻色子：自旋 0, 1, 2, …，對稱，玻色—愛因斯坦分布 — 光子、氦-4、聲子
```
