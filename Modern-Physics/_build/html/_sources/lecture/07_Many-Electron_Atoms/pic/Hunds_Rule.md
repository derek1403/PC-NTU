# Hunds_Rule.png

**對應章節：** 7.6 解釋週期表
**插入位置：** 表 7.5 之後、「推導：宏德規則的物理來源」之前
**課本對應：** 表 7.5（$Z = 5$ 到 $Z = 10$ 的 $p$ 電子自旋）

> 產圖前請先貼上 `00_STYLE_GUIDE.md` 的風格區塊。

---

## 中文提示詞

```
【模型與符號】比較同一近簡併子殼中的組態；反對稱性只給出節點，能量排序仍須計入庫侖與交換積分，不能由節點直接推出平均距離。

請畫一張教學用資訊圖表，主題是「宏德規則：同一子殼的電子先分開放、自旋平行」。

標題列文字：7.6  宏德規則 (Hund's Rule)

導言框文字：
p 子殼有三個軌域。電子進來時，會先一個軌域放一個、自旋彼此平行；
三個軌域都有人之後，才開始放自旋相反的第二個。
在固定軌域的近似下，比較庫侖與交換能，可說明同一子殼中平行自旋組態較低的能量。

主體左側（約 50% 寬）｜pill 標籤：硼到氖的 2p 電子（表 7.5）
畫一張六列的表格，每列左邊是元素名稱與原子序，中間是組態，右邊是三個並排的方格
（代表 m_l = −1, 0, +1 三個 2p 軌域），方格內畫自旋箭頭：
  硼 B（5）　1s² 2s² 2p¹　：[↑] [ ] [ ]
  碳 C（6）　1s² 2s² 2p²　：[↑] [↑] [ ]
  氮 N（7）　1s² 2s² 2p³　：[↑] [↑] [↑]　← 此列用綠框強調，標「半滿：三個都平行」
  氧 O（8）　1s² 2s² 2p⁴　：[↑↓] [↑] [↑]
  氟 F（9）　1s² 2s² 2p⁵　：[↑↓] [↑↓] [↑]
  氖 Ne（10）1s² 2s² 2p⁶　：[↑↓] [↑↓] [↑↓]　← 此列標「2p 填滿」
向上箭頭 ↑ 用紅色，向下箭頭 ↓ 用藍色。
表格下方小字：沒有外加磁場時「上」「下」沒有絕對意義，重點是「先平行、再反平行」。

主體右上（約 50% 寬）｜pill 標籤：碳的兩種排法比一比
左右兩個小框：
  左框（紅色 ✗）：兩個電子擠在同一個方格 [↑↓] [ ] [ ]，
    下方標「同一空間軌域、自旋相反：兩電子可以靠得很近 → 排斥大 → 能量較高」
  右框（綠色 ✓）：兩個電子分開 [↑] [↑] [ ]，
    下方標「不同軌域、自旋平行：被迫互相迴避 → 排斥小 → 能量較低（基態）」

主體右下｜pill 標籤：為什麼平行就會迴避（7.3 節的反對稱性）
一條由左到右的推導鏈（四個小圓角框以箭頭相連）：
  框 1：自旋平行 χ = ↑(1)↑(2)：交換後不變（對稱）
  框 2：整體 ψ = φ(r₁, r₂) χ 必須反對稱 ⇒ 空間部分 φ 反對稱
  框 3：φ = (1/√2)[φ_a(r₁)φ_b(r₂) − φ_a(r₂)φ_b(r₁)] ⇒ r₁ = r₂ 時 φ = 0；a = b 時 φ ≡ 0
  框 4（綠框）：同一子殼的不同軌域：交換項使平行自旋組態的庫侖能降低（固定軌域近似）
在框 3 下方畫一張小示意圖：橫軸「兩電子距離 |r₁ − r₂|」，
  紅色曲線（自旋平行）在距離 0 處為 0、往外才升高；
  灰色虛線（不考慮交換對稱）在距離 0 處不為 0。標「交換洞 (exchange hole)」。

右上角「圖例」方框：
  紅色 ↑ — m_s = +1/2
  藍色 ↓ — m_s = −1/2
  方格 — 一個 (n, l, m_l) 空間軌域，最多兩個電子

最下方一排粉彩公式盒（三個）：
1. 淺綠盒：先分開、再配對，說明「同子殼電子盡量佔據不同的 m_l」
2. 淺紅盒：自旋平行 ⇒ 空間反對稱 ⇒ φ(r, r) = 0，說明「全同粒子反對稱性的推論」
3. 淺藍盒：⟨e²/(4πε₀|r₁ − r₂|)⟩ 較小，說明「庫侖排斥較弱 → 總能量較低」
```

## English Prompt

```
MODEL AND NOTATION: Compare configurations within one nearly degenerate subshell. Nodes alone do not establish mean distance or energy ordering; include Coulomb and exchange energies.

Draw an educational infographic titled "Hund's rule: electrons in a subshell
spread out first, with parallel spins". ALL labels in TRADITIONAL CHINESE.

Title bar: 7.6  宏德規則 (Hund's Rule)

Intro box (Traditional Chinese):
p 子殼有三個軌域。電子進來時，會先一個軌域放一個、自旋彼此平行；
三個軌域都有人之後，才開始放自旋相反的第二個。
在固定軌域的近似下，比較庫侖與交換能，可說明同一子殼中平行自旋組態較低的能量。

LEFT ~50%, pill label 硼到氖的 2p 電子（表 7.5）:
A six-row table; each row shows the element name and atomic number on the left,
the configuration in the middle, and on the right three side-by-side squares
(the three 2p orbitals m_l = −1, 0, +1) containing spin arrows:
  硼 B（5）  1s² 2s² 2p¹ : [↑] [ ] [ ]
  碳 C（6）  1s² 2s² 2p² : [↑] [↑] [ ]
  氮 N（7）  1s² 2s² 2p³ : [↑] [↑] [↑]   ← green frame, note 半滿：三個都平行
  氧 O（8）  1s² 2s² 2p⁴ : [↑↓] [↑] [↑]
  氟 F（9）  1s² 2s² 2p⁵ : [↑↓] [↑↓] [↑]
  氖 Ne（10）1s² 2s² 2p⁶ : [↑↓] [↑↓] [↑↓] ← note 2p 填滿
Up arrows ↑ in RED, down arrows ↓ in BLUE.
small note under the table: 沒有外加磁場時「上」「下」沒有絕對意義，重點是「先平行、再反平行」。

UPPER RIGHT ~50%, pill label 碳的兩種排法比一比:
Two small frames side by side:
  left frame (red ✗): both electrons in one square [↑↓] [ ] [ ], caption
    同一空間軌域、自旋相反：兩電子可以靠得很近 → 排斥大 → 能量較高
  right frame (green ✓): electrons apart [↑] [↑] [ ], caption
    不同軌域、自旋平行：被迫互相迴避 → 排斥小 → 能量較低（基態）

LOWER RIGHT, pill label 為什麼平行就會迴避（7.3 節的反對稱性）:
A left-to-right derivation chain of four small rounded boxes joined by arrows:
  box 1: 自旋平行 χ = ↑(1)↑(2)：交換後不變（對稱）
  box 2: 整體 ψ = φ(r₁, r₂) χ 必須反對稱 ⇒ 空間部分 φ 反對稱
  box 3: φ = (1/√2)[φ_a(r₁)φ_b(r₂) − φ_a(r₂)φ_b(r₁)] ⇒ r₁ = r₂ 時 φ = 0；a = b 時 φ ≡ 0
  box 4 (green frame): 同一子殼的不同軌域：交換項使平行自旋組態的庫侖能降低（固定軌域近似）
Under box 3 a tiny sketch: horizontal axis 兩電子距離 |r₁ − r₂|;
  a RED curve (parallel spins) that is exactly 0 at zero separation and rises only
  further out; a GREY dashed curve (no exchange symmetry) that is non-zero at zero
  separation. Label the dip 交換洞 (exchange hole).

Top-right legend "圖例":
  紅色 ↑ — m_s = +1/2
  藍色 ↓ — m_s = −1/2
  方格 — 一個 (n, l, m_l) 空間軌域，最多兩個電子

Bottom pastel formula boxes (three):
1. light green: 先分開、再配對 — 同子殼電子盡量佔據不同的 m_l
2. light red: 自旋平行 ⇒ 空間反對稱 ⇒ φ(r, r) = 0 — 全同粒子反對稱性的推論
3. light blue: ⟨e²/(4πε₀|r₁ − r₂|)⟩ 較小 — 庫侖排斥較弱 → 總能量較低
```
