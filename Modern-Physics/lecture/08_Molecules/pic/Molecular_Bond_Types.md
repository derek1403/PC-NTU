# Molecular_Bond_Types.png

**對應章節：** 8.1 分子鍵
**插入位置：**「三種可能的結果：共價鍵、離子鍵、不鍵結」三點列表之後、「假設與已知」之前
**課本對應：** 圖 8.1、圖 8.2、圖 8.3

> 產圖前請先貼上 `00_STYLE_GUIDE.md` 的風格區塊。

---

## 中文提示詞

```
【模型與符號】位能曲線的井深標 D_e；自振動基態解離的能量為 D₀=D_e−E_vib,0，兩者不混用。

請畫一張教學用資訊圖表，主題是「兩顆原子靠近時的三種結果，以及唯一的判準：能量」。

標題列文字：8.1  分子鍵的三種結果 (Covalent Bond, Ionic Bond, or No Bond)

導言框文字：
兩顆原子靠近時，電子與電子、電子與另一顆原子核、原子核與原子核之間都有庫侖作用。
結果只有三種：共價鍵（共享電子）、離子鍵（轉移電子）、不鍵結。
會出現哪一種，完全取決於靠近後的總能量有沒有比分開到無窮遠時更低。

主體上半：三欄並排，每欄上方掛深藍 pill 標籤。

欄 1｜pill 標籤：共價鍵 — 共享電子（以 H₂ 為例）
  上方小圖（標「(a) 軌道模型」）：兩個紅色質子（標 +）左右相距 R，
    兩顆藍色電子沿著一條同時繞過兩個質子的「8 字形」虛線軌道運動，
    並在兩質子之間的區域畫得較密。
  下方小圖（標「(b) 量子力學模型」）：同樣兩個質子，外面包一團藍色電子雲，
    雲在兩質子之間最濃（深藍），兩端較淡（淺藍）。
  兩質子之間加一個小標籤：「電子 = 膠水」。
  底下小字：電子在兩核之間停留較久，用負電把兩個互相排斥的正電荷拉在一起。

欄 2｜pill 標籤：離子鍵 — 轉移電子（以 NaCl 為例）
  畫鈉原子（殼層示意 2, 8, 1，最外層一顆電子用橘色標出）與氯原子（2, 8, 7）。
  一支橘色彎箭頭把鈉最外層的那顆電子送到氯的最外層。
  箭頭右邊畫結果：Na⁺（2, 8，標「+」）與 Cl⁻（2, 8, 8，標「−」），
    兩者之間用紅色雙向箭頭標「庫侖吸引」。
  右下角小插圖：NaCl 晶體的立方格子（小球 Na⁺、大球 Cl⁻ 交錯排列），標「圖 8.3 NaCl 晶體」。
  底下小字：通常發生在第一族與第七族（或第二族與第六族）之間。

欄 3｜pill 標籤：不鍵結
  兩顆灰色原子，中間畫兩支向外的灰色箭頭，標「能量沒有比分開時低 → 各走各的」。

主體下半｜pill 標籤：唯一的判準 — 能量比較
  一張座標圖：橫軸「原子核間距 R」，縱軸「系統總能量 E(R)」。
  一條水平灰色虛線標「E(∞)：兩原子分開到無窮遠」。
  綠色曲線（#2E7D32）：R 很小時急遽上升、在 R₀ 處有一個低於 E(∞) 的谷、R 大時趨近 E(∞)；
    谷底標「R₀ 平衡間距」，谷底到虛線之間用雙箭頭標「E_b 鍵結能」；曲線旁標「會鍵結」。
  紅色曲線（#C62828）：從左上單調下降、由上方趨近 E(∞)，沒有任何一點低於虛線；
    曲線旁標「不會鍵結」。

右上角「圖例」方框：
  藍色雲 — 共享的電子
  橘色箭頭 — 被轉移的電子
  綠色曲線 — 有極小值低於 E(∞)：形成鍵結
  紅色曲線 — 處處高於 E(∞)：不鍵結

最下方一排粉彩公式盒（三個）：
1. 淺綠盒：min E(R) < E(∞) ⇔ 形成鍵結，說明「8.1【假設 1】：系統停在能量最低的組態」
2. 淺黃盒：E(R) − E(∞) = 5.14 − 3.61 − 1.44/R(nm)  (eV)，說明「NaCl 的能量帳：R < 0.94 nm 就划算」
3. 淺藍盒：e²/(4πε₀) ≈ 1.44 eV·nm，說明「本章最常用的數字」
```

## English Prompt

```
MODEL AND NOTATION: Label potential-well depth D_e; dissociation from the vibrational ground state is D₀=D_e−E_vib,0.

Draw an educational infographic titled "The three outcomes when two atoms approach,
and the single criterion: energy". ALL labels in TRADITIONAL CHINESE.

Title bar: 8.1  分子鍵的三種結果 (Covalent Bond, Ionic Bond, or No Bond)

Intro box (Traditional Chinese):
兩顆原子靠近時，電子與電子、電子與另一顆原子核、原子核與原子核之間都有庫侖作用。
結果只有三種：共價鍵（共享電子）、離子鍵（轉移電子）、不鍵結。
會出現哪一種，完全取決於靠近後的總能量有沒有比分開到無窮遠時更低。

UPPER HALF: three side-by-side columns, each with a dark-blue pill label.

Column 1 pill: 共價鍵 — 共享電子（以 H₂ 為例）
  Top mini-figure labelled (a) 軌道模型: two red protons (marked +) a distance R
    apart; two blue electrons travel on a dashed figure-eight orbit that loops around
    both protons, drawn denser in the region between the protons.
  Bottom mini-figure labelled (b) 量子力學模型: the same two protons wrapped in a
    blue electron cloud that is darkest between the protons and paler at the ends.
  Small tag between the protons: 電子 = 膠水
  Caption: 電子在兩核之間停留較久，用負電把兩個互相排斥的正電荷拉在一起。

Column 2 pill: 離子鍵 — 轉移電子（以 NaCl 為例）
  A sodium atom (shell sketch 2, 8, 1 with the single outer electron in orange)
  and a chlorine atom (2, 8, 7). An orange curved arrow carries sodium's outer
  electron to chlorine's outer shell. To the right, the result: Na⁺ (2, 8, marked +)
  and Cl⁻ (2, 8, 8, marked −) joined by a red double arrow labelled 庫侖吸引.
  Bottom-right inset: a small cubic NaCl lattice (small Na⁺ spheres alternating with
  large Cl⁻ spheres), labelled 圖 8.3 NaCl 晶體.
  Caption: 通常發生在第一族與第七族（或第二族與第六族）之間。

Column 3 pill: 不鍵結
  Two grey atoms with two grey arrows pointing outward, labelled
  能量沒有比分開時低 → 各走各的.

LOWER HALF, pill label 唯一的判準 — 能量比較:
  A plot: horizontal axis 原子核間距 R, vertical axis 系統總能量 E(R).
  A horizontal grey dashed line labelled E(∞)：兩原子分開到無窮遠.
  Green curve (#2E7D32): rises steeply at small R, has a well BELOW E(∞) at R₀,
    and approaches E(∞) at large R. Mark the bottom R₀ 平衡間距 and a double arrow
    between the well bottom and the dashed line labelled E_b 鍵結能. Tag: 會鍵結.
  Red curve (#C62828): decreases monotonically from the upper left and approaches
    E(∞) from ABOVE, never dipping below the dashed line. Tag: 不會鍵結.

Top-right legend "圖例":
  藍色雲 — 共享的電子
  橘色箭頭 — 被轉移的電子
  綠色曲線 — 有極小值低於 E(∞)：形成鍵結
  紅色曲線 — 處處高於 E(∞)：不鍵結

Bottom pastel boxes (three):
1. light green: min E(R) < E(∞) ⇔ 形成鍵結 — 8.1【假設 1】：系統停在能量最低的組態
2. light yellow: E(R) − E(∞) = 5.14 − 3.61 − 1.44/R(nm)  (eV) — NaCl 的能量帳：R < 0.94 nm 就划算
3. light blue: e²/(4πε₀) ≈ 1.44 eV·nm — 本章最常用的數字
```
