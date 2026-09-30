# Three_Eigen_Equations_and_Quantum_Numbers.png

**對應章節：** 6.3 量子數
**插入位置：** 「三維問題 → 三個量子數」那段推論之後、「假設與已知」之前
**課本對應：** 無（自製對照圖）

> 產圖前請先貼上 `00_STYLE_GUIDE.md` 的風格區塊。

---

## 中文提示詞

```
請畫一張教學用「三欄對照」資訊圖表，主題是「三條本徵方程式如何各自生出一個量子數」。

標題列文字：6.3  三條本徵方程式與三個量子數 (Three Eigen Equations, Three Quantum Numbers)

導言框文字：
本徵方程式最重要的特色是：那個數字不是任何值代進去都會有解，
只有特定的值才有解——那個特定的值就是本徵值，在物理上就是量子化的來源。
氫原子是三維問題，於是有三個變數、三條方程式、三個本徵值、三個量子數。

主體：三個等寬的直欄，由左到右分別用綠色（#2E7D32）、紫色（#7B1FA2）、
藍色（#1565C0）作為該欄的主色（框線與標題底色）。
每一欄由上到下有五層，各層之間用向下的細箭頭連接：

【第 1 層｜方程式】
綠欄：Φ 的方程式　(6.12)　d²Φ/dφ² + m_l²Φ = 0
紫欄：Θ 的方程式　(6.13)　(1/sinθ)d/dθ[sinθ dΘ/dθ] + [l(l+1) − m_l²/sin²θ]Θ = 0
藍欄：R 的方程式　(6.14)　(1/r²)d/dr[r²dR/dr] + [(2m/ħ²)(e²/(4πε₀r) + E) − l(l+1)/r²]R = 0

【第 2 層｜本徵方程式形式】把每條式子改寫成「算符 × 函數 = 數字 × 函數」
綠欄：(d²/dφ²)Φ = −m_l² Φ
紫欄：Ô_θ Θ = l(l+1) Θ
藍欄：Ô_r R = (−2mE/ħ²) R
每格右側加一行小字：本徵值不是任意值都有解

【第 3 層｜邊界條件（這是量子化的真正來源，請用紅色框線強調）】
綠欄：Φ(φ) = Φ(φ + 2π)　單值條件
紫欄：|Θ(θ)| < ∞ 於 θ = 0, π　南北極必須有限
藍欄：R(r) → 0 當 r → ∞　可歸一化（束縛態）

【第 4 層｜量子數與取值範圍】
綠欄：磁量子數 m_l = 0, ±1, ±2, …, ±l
紫欄：軌道量子數 l = 0, 1, 2, …, (n−1)
藍欄：主量子數 n = 1, 2, 3, …

【第 5 層｜物理意義】
綠欄：角動量的「方向」　L_z = m_l ħ
紫欄：角動量的「大小」　L = √(l(l+1)) ħ
藍欄：能量　E_n = E_1/n²，E_1 ≈ −13.6 eV

在三欄底下橫跨全寬畫一條深藍色橫幅，白字寫：
　三維空間 → 三個變數 → 三條全微分方程式 → 三個本徵值 → 三個量子數

右上角「圖例」方框：
  綠色 — 方位角 φ 方向
  紫色 — 天頂角 θ 方向
  藍色 — 徑向 r 方向
  紅色框 — 量子化的真正來源：邊界條件

最下方一排粉彩公式盒（兩個，橫跨全寬）：
1. 淺黃盒：Ψ_{n l m_l}(r,θ,φ) = R_{nl}(r) Θ_{l m_l}(θ) Φ_{m_l}(φ)
   說明「下標不是亂寫的：Φ 只含 m_l、Θ 含 l 與 m_l、R 含 n 與 l」
2. 淺紅盒：電子的第四個量子數（自旋）不在薛丁格方程式裡
   說明「自旋要等到狄拉克方程式才會出現」
```

## English Prompt

```
Draw a three-column comparison infographic titled "how three eigen equations each
produce one quantum number". ALL labels in TRADITIONAL CHINESE.

Title bar: 6.3  三條本徵方程式與三個量子數 (Three Eigen Equations, Three Quantum Numbers)

Intro box (Traditional Chinese):
本徵方程式最重要的特色是：那個數字不是任何值代進去都會有解，
只有特定的值才有解——那個特定的值就是本徵值，在物理上就是量子化的來源。
氫原子是三維問題，於是有三個變數、三條方程式、三個本徵值、三個量子數。

Main area: three equal-width vertical columns, coloured green (#2E7D32),
purple (#7B1FA2) and blue (#1565C0) respectively (borders and header fills).
Each column has five stacked tiers joined by thin downward arrows:

TIER 1 — the equation
green: Φ 的方程式 (6.12)  d²Φ/dφ² + m_l²Φ = 0
purple: Θ 的方程式 (6.13)  (1/sinθ)d/dθ[sinθ dΘ/dθ] + [l(l+1) − m_l²/sin²θ]Θ = 0
blue: R 的方程式 (6.14)  (1/r²)d/dr[r²dR/dr] + [(2m/ħ²)(e²/(4πε₀r) + E) − l(l+1)/r²]R = 0

TIER 2 — rewritten as "operator × function = number × function"
green: (d²/dφ²)Φ = −m_l² Φ
purple: Ô_θ Θ = l(l+1) Θ
blue: Ô_r R = (−2mE/ħ²) R
small caption in each: 本徵值不是任意值都有解

TIER 3 — boundary condition (the true origin of quantization; emphasise with RED borders)
green: Φ(φ) = Φ(φ + 2π)  單值條件
purple: |Θ(θ)| < ∞ 於 θ = 0, π  南北極必須有限
blue: R(r) → 0 當 r → ∞  可歸一化（束縛態）

TIER 4 — quantum number and allowed values
green: 磁量子數 m_l = 0, ±1, ±2, …, ±l
purple: 軌道量子數 l = 0, 1, 2, …, (n−1)
blue: 主量子數 n = 1, 2, 3, …

TIER 5 — physical meaning
green: 角動量的「方向」 L_z = m_l ħ
purple: 角動量的「大小」 L = √(l(l+1)) ħ
blue: 能量 E_n = E_1/n²，E_1 ≈ −13.6 eV

Below the three columns, a full-width dark-blue banner with white text:
　三維空間 → 三個變數 → 三條全微分方程式 → 三個本徵值 → 三個量子數

Top-right legend box "圖例":
  綠色 — 方位角 φ 方向
  紫色 — 天頂角 θ 方向
  藍色 — 徑向 r 方向
  紅色框 — 量子化的真正來源：邊界條件

Bottom pastel boxes (two, full width):
1. light yellow: Ψ_{n l m_l}(r,θ,φ) = R_{nl}(r) Θ_{l m_l}(θ) Φ_{m_l}(φ)
   — 下標不是亂寫的：Φ 只含 m_l、Θ 含 l 與 m_l、R 含 n 與 l
2. light red: 電子的第四個量子數（自旋）不在薛丁格方程式裡
   — 自旋要等到狄拉克方程式才會出現
```
