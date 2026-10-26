# Shells_and_Subshell_Capacity.png

**對應章節：** 7.5 原子結構
**插入位置：** $(7.14)$ 與殼容量表之後、「推導：填滿的殼與子殼總角動量為零」之前
**課本對應：** 表 7.3（$M$ 殼的子殼容量）＋ 式 $(7.13)$、$(7.14)$

> 產圖前請先貼上 `00_STYLE_GUIDE.md` 的風格區塊。

---

## 中文提示詞

```
請畫一張教學用資訊圖表，主題是「殼與子殼可以放幾個電子——2(2l+1) 與 2n² 是怎麼數出來的」。

標題列文字：7.5  殼與子殼的容量 (Capacity of Shells and Subshells)

導言框文字：
能量最低原理讓電子往低處擠，不相容原理規定每個量子態只能坐一個電子。
於是只要「數格子」：l 有 n 種、m_l 有 2l+1 種、m_s 有 2 種，
就得到子殼容量 2(2l+1) 與殼容量 2n²。

主體左側（約 35% 寬）｜pill 標籤：殼 (shell)：n 相同
畫四個同心半圓弧（只畫右半邊，圓心在左側一個小紅點「原子核」），由內到外：
  第 1 弧：標「K　n = 1　最多 2 個」
  第 2 弧：標「L　n = 2　最多 8 個」
  第 3 弧：標「M　n = 3　最多 18 個」（此弧用深藍粗線強調，並以虛線連到中間的表格）
  第 4 弧：標「N　n = 4　最多 32 個」
  弧線外側小字：殼代號 K, L, M, N, O… 沿用 x 射線光譜學的歷史名稱 (7.13)

主體中間（約 40% 寬）｜pill 標籤：M 殼的格子（表 7.3）
畫一張「軌域方格」圖：每一列是一個子殼，每一個方格是一個 (l, m_l) 軌域，
每個方格裡畫一對箭頭：一支向上 ↑（m_s = +1/2）、一支向下 ↓（m_s = −1/2）。
  第一列標「l = 0（3s）」：1 個方格（m_l = 0），列尾標「2」
  第二列標「l = 1（3p）」：3 個方格（m_l = −1, 0, +1），列尾標「6」
  第三列標「l = 2（3d）」：5 個方格（m_l = −2, −1, 0, +1, +2），列尾標「10」
  方格上方標出各欄的 m_l 值。
  表格下方大字：2 + 6 + 10 = 18
  三列用不同的底色：3s 淺綠、3p 淺藍、3d 淺橘。

主體右側（約 25% 寬）｜pill 標籤：數格子
一條由上而下的推導鏈：
  框 1：每個 (n, l, m_l) 軌域：m_s = ±1/2 → 最多 2 個電子（不相容原理）
  框 2：子殼：(2l + 1) 個軌域 × 2 = 2(2l + 1)
        並附小表：s 2、p 6、d 10、f 14
  框 3：殼：Σ_{l=0}^{n−1} 2(2l + 1) = (n/2)(2)[1 + 2(n − 1) + 1] = 2n²　(7.14)
        小字：等差級數：項數 n、首項 2、末項 2(2n − 1)

最下方一排粉彩公式盒（三個）：
1. 淺綠盒：N_sub = 2(2l + 1)，說明「子殼容量：s 2、p 6、d 10、f 14」
2. 淺藍盒：N_max = 2n²　(7.14)，說明「殼容量：K 2、L 8、M 18、N 32」
3. 淺紅盒：殼容量 2, 8, 18, 32 ≠ 週期長度 2, 8, 8, 18, 18, 32, 32，說明「差別來自填充順序（7.6 節）」
另在三個盒子上方放一條細長的淺紫色橫框：
  填滿的子殼：Σ m_l = 0、Σ m_s = 0 ⇒ 總角動量 L = S = 0、電荷分布球對稱
```

## English Prompt

```
Draw an educational infographic titled "how many electrons fit in a shell and a
subshell — counting out 2(2l+1) and 2n²". ALL labels in TRADITIONAL CHINESE.

Title bar: 7.5  殼與子殼的容量 (Capacity of Shells and Subshells)

Intro box (Traditional Chinese):
能量最低原理讓電子往低處擠，不相容原理規定每個量子態只能坐一個電子。
於是只要「數格子」：l 有 n 種、m_l 有 2l+1 種、m_s 有 2 種，
就得到子殼容量 2(2l+1) 與殼容量 2n²。

LEFT ~35%, pill label 殼 (shell)：n 相同:
Four concentric half-circle arcs (right half only, centred on a small red dot on
the left labelled 原子核), from inside out:
  arc 1: K　n = 1　最多 2 個
  arc 2: L　n = 2　最多 8 個
  arc 3: M　n = 3　最多 18 個 (thick dark-blue line, linked by a dashed line to the centre table)
  arc 4: N　n = 4　最多 32 個
  small note outside the arcs: 殼代號 K, L, M, N, O… 沿用 x 射線光譜學的歷史名稱 (7.13)

CENTRE ~40%, pill label M 殼的格子（表 7.3）:
An "orbital box" diagram: each row is a subshell, each square is one (l, m_l)
orbital, and each square contains a pair of arrows: one UP ↑ (m_s = +1/2) and one
DOWN ↓ (m_s = −1/2).
  row 1 labelled l = 0（3s）: 1 square (m_l = 0), row total 2
  row 2 labelled l = 1（3p）: 3 squares (m_l = −1, 0, +1), row total 6
  row 3 labelled l = 2（3d）: 5 squares (m_l = −2, −1, 0, +1, +2), row total 10
  m_l values printed above the columns.
  Below the grid in large type: 2 + 6 + 10 = 18
  Row tints: 3s light green, 3p light blue, 3d light orange.

RIGHT ~25%, pill label 數格子:
A top-to-bottom derivation chain:
  box 1: 每個 (n, l, m_l) 軌域：m_s = ±1/2 → 最多 2 個電子（不相容原理）
  box 2: 子殼：(2l + 1) 個軌域 × 2 = 2(2l + 1)
         with a mini table: s 2, p 6, d 10, f 14
  box 3: 殼：Σ_{l=0}^{n−1} 2(2l + 1) = (n/2)(2)[1 + 2(n − 1) + 1] = 2n²  (7.14)
         small note: 等差級數：項數 n、首項 2、末項 2(2n − 1)

Bottom pastel formula boxes (three):
1. light green: N_sub = 2(2l + 1) — 子殼容量：s 2、p 6、d 10、f 14
2. light blue: N_max = 2n²  (7.14) — 殼容量：K 2、L 8、M 18、N 32
3. light red: 殼容量 2, 8, 18, 32 ≠ 週期長度 2, 8, 8, 18, 18, 32, 32 — 差別來自填充順序（7.6 節）
Above these three boxes, a thin long light-purple banner:
  填滿的子殼：Σ m_l = 0、Σ m_s = 0 ⇒ 總角動量 L = S = 0、電荷分布球對稱
```
