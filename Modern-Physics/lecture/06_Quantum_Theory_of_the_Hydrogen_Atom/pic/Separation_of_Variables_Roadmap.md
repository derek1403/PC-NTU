# Separation_of_Variables_Roadmap.png

**對應章節：** 6.2 變數分離
**插入位置：**【推導 1】偏微分改寫為全微分之後、「推導：第一步」之前
**課本對應：** 無（自製路線圖）

> 產圖前請先貼上 `00_STYLE_GUIDE.md` 的風格區塊。

---

## 中文提示詞

```
請畫一張教學用「流程路線圖」資訊圖表，主題是「變數分離法怎麼把一條偏微分方程式
拆成三條全微分方程式」。這張圖是本章的骨架圖，讀者應該光看它就能複述整章推導。

標題列文字：6.2  變數分離法路線圖 (Separation of Variables — Roadmap)

導言框文字：
偏微分方程式若想用手解出解析解，基本上只有一招：變數分離法。
它的精神是把一條含三個變數的偏微分方程式，拆成三條各自只含一個變數的全微分方程式。
以下是氫原子問題完整走完這一招的六個步驟。

主體：一條由上而下（或蛇行）的流程鏈，共六個節點，節點之間用深藍粗箭頭連接，
每個箭頭旁邊用橘色小字寫出「這一步做了什麼動作」。

節點 1（淺藍圓角框）：卡氏座標的三維薛丁格方程式　(6.1)
  ∂²Ψ/∂x² + ∂²Ψ/∂y² + ∂²Ψ/∂z² + (2m/ħ²)(E − U)Ψ = 0
  紅色小字警語：U = −e²/(4πε₀(x²+y²+z²)^(1/2))，x、y、z 被綁死，無解析解

箭頭 1 旁邊橘字：換成球座標（∇² 改寫）

節點 2（淺藍圓角框）：球座標形式　(6.3)
  (1/r²)∂/∂r[r²∂Ψ/∂r] + (1/(r²sinθ))∂/∂θ[sinθ ∂Ψ/∂θ] + (1/(r²sin²θ))∂²Ψ/∂φ²
  + (2m/ħ²)(E − U)Ψ = 0
  綠色小字：位能變成乾淨的 −e²/(4πε₀r)，只剩一個變數

箭頭 2 旁邊橘字：整體乘上 r² sin²θ

節點 3（淺藍圓角框）：(6.4)
  sin²θ ∂/∂r[r²∂Ψ/∂r] + sinθ ∂/∂θ[sinθ ∂Ψ/∂θ] + ∂²Ψ/∂φ²
  + (2mr²sin²θ/ħ²)(e²/(4πε₀r) + E)Ψ = 0
  綠色小字：第三項只含 φ、第二項只含 θ

箭頭 3 旁邊橘字：設 Ψ = R(r)Θ(θ)Φ(φ)，再除以 RΘΦ　(6.5)

節點 4（淺藍圓角框）：(6.6) 偏微分全部變成全微分
  (sin²θ/R)d/dr[r²dR/dr] + (sinθ/Θ)d/dθ[sinθ dΘ/dθ] + (1/Φ)d²Φ/dφ²
  + (2mr²sin²θ/ħ²)(e²/(4πε₀r) + E) = 0

箭頭 4 旁邊橘字：第一次分離 — 把只含 φ 的項移到右邊

節點 5（分岔）：畫成一個左右分岔。
  左分支（淺綠框）：(6.8)　−(1/Φ)d²Φ/dφ² = m_l²　→ 分離常數 m_l²
  右分支（淺黃框）：(6.7) 左邊 = m_l²，除以 sin²θ 後再分離

箭頭 5 旁邊橘字：第二次分離 — 把只含 θ 的項移到右邊

節點 6（三個並排的粉彩框，這是全圖的終點，要畫得最醒目）：
  淺綠框：Φ 的方程式　(6.12)　d²Φ/dφ² + m_l²Φ = 0
  淺紫框：Θ 的方程式　(6.13)　(1/sinθ)d/dθ[sinθ dΘ/dθ] + [l(l+1) − m_l²/sin²θ]Θ = 0
  淺藍框：R 的方程式　(6.14)　(1/r²)d/dr[r²dR/dr] + [(2m/ħ²)(e²/(4πε₀r) + E) − l(l+1)/r²]R = 0

在流程圖右側另闢一個直立的深藍 pill 標籤方框「關鍵論證」，內容：
  等號左邊只含 A、右邊只含 B，
  而等號必須在空間中每一點都成立，
  唯一的可能是兩邊各自等於同一個常數。
  → 這句話在本章用了三次：(6.7)、(6.9)、例題 6.1。

最下方一排粉彩公式盒（三個）：
1. 淺綠盒：m_l ∈ ℤ，說明「來自 Φ(φ) = Φ(φ+2π) 的單值條件」
2. 淺紫盒：l = |m_l|, |m_l|+1, …，說明「來自 Θ 在 θ=0,π 必須有限」
3. 淺藍盒：n = 1, 2, 3, …，說明「來自 R 在 r→∞ 必須可歸一化」
```

## English Prompt

```
Draw an educational FLOWCHART/ROADMAP infographic titled "how separation of
variables turns one PDE into three ODEs". ALL labels in TRADITIONAL CHINESE.
This is the backbone figure of the chapter — a reader should be able to
reconstruct the whole derivation from it alone.

Title bar: 6.2  變數分離法路線圖 (Separation of Variables — Roadmap)

Intro box (Traditional Chinese):
偏微分方程式若想用手解出解析解，基本上只有一招：變數分離法。
它的精神是把一條含三個變數的偏微分方程式，拆成三條各自只含一個變數的全微分方程式。
以下是氫原子問題完整走完這一招的六個步驟。

Main area: a top-to-bottom (or serpentine) chain of six nodes joined by thick
dark-blue arrows. Beside each arrow, small ORANGE Chinese text states the action
performed at that step.

Node 1 (light-blue rounded box): 卡氏座標的三維薛丁格方程式 (6.1)
  ∂²Ψ/∂x² + ∂²Ψ/∂y² + ∂²Ψ/∂z² + (2m/ħ²)(E − U)Ψ = 0
  small RED warning: U = −e²/(4πε₀(x²+y²+z²)^(1/2))，x、y、z 被綁死，無解析解

Arrow 1 label: 換成球座標（∇² 改寫）

Node 2: 球座標形式 (6.3)
  (1/r²)∂/∂r[r²∂Ψ/∂r] + (1/(r²sinθ))∂/∂θ[sinθ ∂Ψ/∂θ] + (1/(r²sin²θ))∂²Ψ/∂φ²
  + (2m/ħ²)(E − U)Ψ = 0
  small GREEN note: 位能變成乾淨的 −e²/(4πε₀r)，只剩一個變數

Arrow 2 label: 整體乘上 r² sin²θ

Node 3: (6.4)
  sin²θ ∂/∂r[r²∂Ψ/∂r] + sinθ ∂/∂θ[sinθ ∂Ψ/∂θ] + ∂²Ψ/∂φ²
  + (2mr²sin²θ/ħ²)(e²/(4πε₀r) + E)Ψ = 0
  small GREEN note: 第三項只含 φ、第二項只含 θ

Arrow 3 label: 設 Ψ = R(r)Θ(θ)Φ(φ)，再除以 RΘΦ (6.5)

Node 4: (6.6) 偏微分全部變成全微分
  (sin²θ/R)d/dr[r²dR/dr] + (sinθ/Θ)d/dθ[sinθ dΘ/dθ] + (1/Φ)d²Φ/dφ²
  + (2mr²sin²θ/ħ²)(e²/(4πε₀r) + E) = 0

Arrow 4 label: 第一次分離 — 把只含 φ 的項移到右邊

Node 5 (a left/right fork):
  left (light green): (6.8) −(1/Φ)d²Φ/dφ² = m_l² → 分離常數 m_l²
  right (light yellow): (6.7) 左邊 = m_l²，除以 sin²θ 後再分離

Arrow 5 label: 第二次分離 — 把只含 θ 的項移到右邊

Node 6 (three pastel boxes side by side — the visual climax, most prominent):
  light green: Φ 的方程式 (6.12)  d²Φ/dφ² + m_l²Φ = 0
  light purple: Θ 的方程式 (6.13)  (1/sinθ)d/dθ[sinθ dΘ/dθ] + [l(l+1) − m_l²/sin²θ]Θ = 0
  light blue: R 的方程式 (6.14)  (1/r²)d/dr[r²dR/dr] + [(2m/ħ²)(e²/(4πε₀r) + E) − l(l+1)/r²]R = 0

On the right side, a vertical dark-blue pill-labelled box "關鍵論證" containing:
  等號左邊只含 A、右邊只含 B，
  而等號必須在空間中每一點都成立，
  唯一的可能是兩邊各自等於同一個常數。
  → 這句話在本章用了三次：(6.7)、(6.9)、例題 6.1。

Bottom pastel formula boxes (three):
1. light green: m_l ∈ ℤ — 來自 Φ(φ) = Φ(φ+2π) 的單值條件
2. light purple: l = |m_l|, |m_l|+1, … — 來自 Θ 在 θ=0,π 必須有限
3. light blue: n = 1, 2, 3, … — 來自 R 在 r→∞ 必須可歸一化
```
