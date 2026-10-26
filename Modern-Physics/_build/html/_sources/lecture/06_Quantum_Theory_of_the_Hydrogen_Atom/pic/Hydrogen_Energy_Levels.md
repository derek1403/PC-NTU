# Hydrogen_Energy_Levels.png

**對應章節：** 6.4 主量子數
**插入位置：** $E_n = E_1/n^2$ 公式之後、「為什麼能量必須是負的」之前
**課本對應：** 課本第四章能階圖的量子力學版本

> 產圖前請先貼上 `00_STYLE_GUIDE.md` 的風格區塊。

---

## 中文提示詞

```
請畫一張教學用資訊圖表，主題是「氫原子的能階與主量子數」。

標題列文字：6.4  氫原子能階與主量子數 (Hydrogen Energy Levels and the Principal Quantum Number)

導言框文字：
古典上總能量可以是任何值，但被束縛在原子內的電子能量必為負值——
正能量對應的是已經游離的電子。這裡的量子化不是假設，
而是硬解薛丁格方程式後，連帶拉蓋爾級數必須截斷所導致的結果。

主體左半（佔約 60% 寬）：能階圖
- 縱軸為能量 E，單位 eV，向上為正；橫軸不具意義（僅作排版）。
- 在 E = 0 處畫一條水平的粗黑線，標為「游離極限 E = 0」。
- E = 0 以上用淺灰色網底填滿，標為「游離連續區（電子已脫離原子）」，
  並用小字註明「能量可為任意正值，不再量子化」。
- E = 0 以下畫出五條水平藍色（#1565C0）能階線，由下往上依序標註：
    n = 1，E₁ = −13.60 eV（最下方，線畫最粗，標為「基態」）
    n = 2，E₂ = −3.40 eV
    n = 3，E₃ = −1.51 eV
    n = 4，E₄ = −0.85 eV
    n = 5，E₅ = −0.54 eV
- 能階間距必須正確反映 1/n² 的關係：n 越大線越密、越靠近 E = 0。
- 在 n = 5 上方用一組漸密的細虛線暗示 n → ∞ 的堆積，標為「n → ∞」。
- 在能階圖左側用一個大括號涵蓋所有能階，旁邊直立寫「束縛態 E < 0」。

主體右半（佔約 40% 寬）：三個上下堆疊的說明卡，各自上方掛深藍 pill 標籤。

卡 1｜pill 標籤：能階公式
  E_n = −(m e⁴)/(32π²ε₀²ħ²) · (1/n²) = E₁/n²
  下方逐條列出符號說明：
    E_n：第 n 能階的電子能量，單位 eV
    E₁：基態能量，E₁ ≈ −13.6 eV
    n：主量子數，n = 1, 2, 3, …
    m：電子質量；e：基本電荷；ε₀：真空電容率；ħ：約化普朗克常數

卡 2｜pill 標籤：與波耳模型的差別
  用左右對照的兩個小方框：
  左（淺紅框）標題「波耳 1913」：先假設電子軌道上形成駐波 2πr = nλ，
    量子化是被人為塞進去的前提。
  右（淺綠框）標題「薛丁格 1926」：什麼都沒假設，只是把庫侖位能代進微分方程式，
    量子化是「級數不截斷就會發散」的純數學後果。
  下方一行深藍粗體字：數值完全相同，但知識論地位天差地遠。

卡 3｜pill 標籤：能量為什麼是負的
  文字：把電子從距離 r 移到無窮遠必須由外界作功，故束縛態能量為負；
  若能量為正，代表電子已經逃離原子核，即游離態。

右上角「圖例」方框：
  藍色實線 — 束縛態能階（量子化）
  粗黑線 — 游離極限 E = 0
  灰色網底 — 游離連續區（不量子化）

最下方一排粉彩公式盒（三個）：
1. 淺藍盒：E₂ − E₁ = 10.2 eV，說明「n=2 掉到 n=1，放出萊曼系第一條譜線」
2. 淺綠盒：E_∞ − E₁ = 13.6 eV，說明「氫原子的游離能」
3. 淺紫盒：能量與 l、m_l 完全無關，說明「同一個 n 之下所有 l、m_l 態能量相同（簡併）」
```

## English Prompt

```
Draw an educational infographic titled "Hydrogen energy levels and the principal
quantum number". ALL labels in TRADITIONAL CHINESE.

Title bar: 6.4  氫原子能階與主量子數 (Hydrogen Energy Levels and the Principal Quantum Number)

Intro box (Traditional Chinese):
古典上總能量可以是任何值，但被束縛在原子內的電子能量必為負值——
正能量對應的是已經游離的電子。這裡的量子化不是假設，
而是硬解薛丁格方程式後，連帶拉蓋爾級數必須截斷所導致的結果。

LEFT ~60%: the energy-level diagram.
- Vertical axis: energy E in eV, positive upward. Horizontal axis carries no meaning.
- A thick black horizontal line at E = 0 labelled 游離極限 E = 0.
- Above E = 0, a light grey hatched band labelled 游離連續區（電子已脫離原子）
  with a small note 能量可為任意正值，不再量子化.
- Below E = 0, five blue (#1565C0) horizontal level lines, from bottom up:
    n = 1，E₁ = −13.60 eV  (thickest line, labelled 基態)
    n = 2，E₂ = −3.40 eV
    n = 3，E₃ = −1.51 eV
    n = 4，E₄ = −0.85 eV
    n = 5，E₅ = −0.54 eV
- Level spacing MUST correctly show the 1/n² crowding: higher n packs closer to E = 0.
- Above n = 5, a set of progressively denser dashed lines suggesting the n → ∞
  accumulation, labelled n → ∞.
- A large brace on the left spanning all levels, labelled vertically 束縛態 E < 0.

RIGHT ~40%: three stacked explanation cards, each with a dark-blue pill label.

Card 1 pill: 能階公式
  E_n = −(m e⁴)/(32π²ε₀²ħ²) · (1/n²) = E₁/n²
  symbol list:
    E_n：第 n 能階的電子能量，單位 eV
    E₁：基態能量，E₁ ≈ −13.6 eV
    n：主量子數，n = 1, 2, 3, …
    m：電子質量；e：基本電荷；ε₀：真空電容率；ħ：約化普朗克常數

Card 2 pill: 與波耳模型的差別
  two side-by-side small boxes:
  left (light red) 波耳 1913: 先假設電子軌道上形成駐波 2πr = nλ，
    量子化是被人為塞進去的前提。
  right (light green) 薛丁格 1926: 什麼都沒假設，只是把庫侖位能代進微分方程式，
    量子化是「級數不截斷就會發散」的純數學後果。
  one dark-blue bold line below: 數值完全相同，但知識論地位天差地遠。

Card 3 pill: 能量為什麼是負的
  把電子從距離 r 移到無窮遠必須由外界作功，故束縛態能量為負；
  若能量為正，代表電子已經逃離原子核，即游離態。

Top-right legend "圖例":
  藍色實線 — 束縛態能階（量子化）
  粗黑線 — 游離極限 E = 0
  灰色網底 — 游離連續區（不量子化）

Bottom pastel boxes (three):
1. light blue: E₂ − E₁ = 10.2 eV — n=2 掉到 n=1，放出萊曼系第一條譜線
2. light green: E_∞ − E₁ = 13.6 eV — 氫原子的游離能
3. light purple: 能量與 l、m_l 完全無關 — 同一個 n 之下所有 l、m_l 態能量相同（簡併）
```
