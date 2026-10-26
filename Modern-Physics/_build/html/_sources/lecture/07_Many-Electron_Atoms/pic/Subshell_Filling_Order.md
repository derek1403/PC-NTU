# Subshell_Filling_Order.png

**對應章節：** 7.6 解釋週期表
**插入位置：**「推導：為什麼 $4s$ 比 $3d$ 先填」之後、「子殼的填充順序（圖 7.12）」之前
**課本對應：** 圖 7.12（原子中量子態的序列）＋ 投影片「過渡元素」的填充順序

> 產圖前請先貼上 `00_STYLE_GUIDE.md` 的風格區塊。

---

## 中文提示詞

```
【模型與符號】能階階梯是中性原子的近似填充次序，不是所有元素、離子的固定能量排序；標出 Cr、Cu 等例外與游離時次序可變。徑向曲線為穿透示意，峰高不代表精確數值。

請畫一張教學用資訊圖表，主題是「子殼的填充順序：為什麼 4s 比 3d 先填，週期長度又是怎麼來的」。

標題列文字：7.6  子殼的填充順序 (Order of Filling the Subshells)

導言框文字：
多電子原子中，能量不只跟 n 有關，也跟 l 有關：l 小的電子會「鑽入」內層核心，
看到較多未被屏蔽的核電荷，能量因此較低。結果 4s 比 3d 低、5s 比 4d 低、6s 比 4f 低，
填充順序一延遲，週期長度 2, 8, 8, 18, 18, 32, 32 就自動出現了。

主體左側（約 40% 寬）｜pill 標籤：能階的先後（圖 7.12，不按比例）
畫一張「階梯能階圖」：縱軸標「E（不按比例）」，向上為正；
橫向七個直欄標 n = 1, 2, 3, 4, 5, 6, 7。
在每一欄畫出該 n 的子殼短橫線，並在線旁標字母 s、p、d、f。
**各短橫線的高度請依下列「名次」由低到高排列（名次 1 最低），間距相等即可：**
  1: 1s　2: 2s　3: 2p　4: 3s　5: 3p　6: 4s　7: 3d　8: 4p　9: 5s　10: 4d
  11: 5p　12: 6s　13: 4f　14: 5d　15: 6p　16: 7s　17: 5f　18: 6d　19: 7p
  （例如 4s 的線必須畫得比 3d 低；5s 比 4d 低；6s 比 4f 低。）
用顏色區分子殼：s 綠、p 藍、d 橘、f 紫（與週期表分區配色一致）。
用三個紅色小圈分別圈出「4s 低於 3d」「5s 低於 4d」「6s 低於 4f」，並以紅字標「n 大反而先填」。

主體中間（約 25% 寬）｜pill 標籤：好記的法則：先比 n + l
畫一張斜線對角表（Madelung 圖）：
  列為 n = 1 到 7，欄為 s、p、d、f，格子內寫 1s、2s、2p、3s、3p、3d、4s、4p、4d、4f…
  （只寫存在的組合：n = 1 只有 1s；n = 2 有 2s、2p；n = 3 有 3s、3p、3d；n ≥ 4 有 s、p、d、f。）
  用一串平行的紅色斜箭頭由右上往左下穿過格子，箭頭順序給出：
  1s → 2s → 2p → 3s → 3p → 4s → 3d → 4p → 5s → 4d → 5p → 6s → 4f → 5d → 6p → 7s → 5f → 6d → 7p
  下方小字：先比 n + l，小的先填；n + l 相同時 n 小的先填。實際元素在 La、Ac 附近有例外。

主體右側（約 35% 寬）：兩張上下堆疊的卡片。
卡 1｜pill 標籤：以鉀 (Z = 19) 為例：鑽入效應
  一張小的徑向機率 P(r) 示意圖：
    原點附近畫一段淺灰色陰影區，標「[Ar] 核心（18 個電子）」。
    綠色曲線 4s：有 4 個峰，最外側的峰最高，但前 3 個小峰落在灰色核心內，
      用紅色箭頭指著小峰標「鑽入核心」。
    橘色曲線 3d：只有一個峰，主要落在灰色核心外側，核心內仍有較小的非零機率。
  下方兩行數字：
    4s：束縛能 4.34 eV → Z_eff = 4√(4.34/13.6) ≈ 2.26
    3d：束縛能 1.67 eV → Z_eff = 3√(1.67/13.6) ≈ 1.05（幾乎就是氫的 n = 3：1.51 eV）
卡 2｜pill 標籤：週期長度從哪裡來
  一張表格：
    週期 1：1s → 2
    週期 2：2s 2p → 8
    週期 3：3s 3p → 8（3d 被 4s 擠到下一週期）
    週期 4：4s 3d 4p → 18
    週期 5：5s 4d 5p → 18
    週期 6：6s 4f 5d 6p → 32
    週期 7：7s 5f 6d 7p → 32
  其中 d 子殼的格子塗橘色、標「過渡元素」；f 子殼塗紫色、標「稀土／錒系」。

右上角「圖例」方框：
  綠 — s 子殼　藍 — p 子殼　橘 — d 子殼　紫 — f 子殼
  紅圈 — n 較大卻先填的子殼

最下方一排粉彩公式盒（三個）：
1. 淺綠盒：l 小 → 徑向節點 n − l − 1 多 → 鑽入核心，說明「看到較多核電荷，能量較低」
2. 淺橘盒：l 大 → 離心項 l(l+1)ħ²/2mr² 大 → 被推到核心外，說明「幾乎完全被屏蔽，Z_eff ≈ 1」
3. 淺藍盒：1s 2s 2p 3s 3p 4s 3d 4p 5s 4d 5p 6s 4f 5d 6p 7s 5f 6d，說明「填充順序」
```

## English Prompt

```
MODEL AND NOTATION: The staircase is an approximate neutral-atom filling guide, not a universal energy ordering for all atoms or ions. Note Cr/Cu exceptions and ionization-dependent ordering. Radial curves illustrate penetration only.

Draw an educational infographic titled "the order of filling subshells: why 4s
fills before 3d, and where the period lengths come from". ALL labels in
TRADITIONAL CHINESE.

Title bar: 7.6  子殼的填充順序 (Order of Filling the Subshells)

Intro box (Traditional Chinese):
多電子原子中，能量不只跟 n 有關，也跟 l 有關：l 小的電子會「鑽入」內層核心，
看到較多未被屏蔽的核電荷，能量因此較低。結果 4s 比 3d 低、5s 比 4d 低、6s 比 4f 低，
填充順序一延遲，週期長度 2, 8, 8, 18, 18, 32, 32 就自動出現了。

LEFT ~40%, pill label 能階的先後（圖 7.12，不按比例）:
A "staircase" level diagram: vertical axis E（不按比例）, upward positive;
seven columns labelled n = 1, 2, 3, 4, 5, 6, 7.
In each column draw short horizontal bars for that n's subshells, each tagged
with its letter s, p, d, f.
**Set the bar heights by the following RANK from lowest (rank 1) to highest;
equal spacing between ranks is fine:**
  1: 1s  2: 2s  3: 2p  4: 3s  5: 3p  6: 4s  7: 3d  8: 4p  9: 5s  10: 4d
  11: 5p  12: 6s  13: 4f  14: 5d  15: 6p  16: 7s  17: 5f  18: 6d  19: 7p
  (e.g. the 4s bar MUST sit lower than 3d; 5s lower than 4d; 6s lower than 4f.)
Colour by subshell: s green, p blue, d orange, f purple (matching the periodic-table blocks).
Circle three spots in red — "4s below 3d", "5s below 4d", "6s below 4f" — with the
red note n 大反而先填.

CENTRE ~25%, pill label 好記的法則：先比 n + l:
A diagonal (Madelung) chart:
  rows n = 1 to 7, columns s, p, d, f; cells read 1s, 2s, 2p, 3s, 3p, 3d, 4s, 4p, 4d, 4f, …
  (only existing combinations: n = 1 has only 1s; n = 2 has 2s, 2p; n = 3 has 3s,
  3p, 3d; n ≥ 4 has s, p, d, f).
  A series of parallel red diagonal arrows runs from upper-right to lower-left
  through the cells, giving the order:
  1s → 2s → 2p → 3s → 3p → 4s → 3d → 4p → 5s → 4d → 5p → 6s → 4f → 5d → 6p → 7s → 5f → 6d → 7p
  small note below: 先比 n + l，小的先填；n + l 相同時 n 小的先填。實際元素在 La、Ac 附近有例外。

RIGHT ~35%: two stacked cards.
Card 1, pill label 以鉀 (Z = 19) 為例：鑽入效應:
  a small radial-probability sketch P(r):
    a light-grey shaded region near the origin labelled [Ar] 核心（18 個電子）.
    GREEN curve 4s: four peaks, the outermost tallest, but the first three small
      peaks lie inside the grey core; a red arrow points at them, labelled 鑽入核心.
    ORANGE curve 3d: a single peak mainly outside the grey core, with small nonzero penetration.
  two lines of numbers below:
    4s：束縛能 4.34 eV → Z_eff = 4√(4.34/13.6) ≈ 2.26
    3d：束縛能 1.67 eV → Z_eff = 3√(1.67/13.6) ≈ 1.05（幾乎就是氫的 n = 3：1.51 eV）
Card 2, pill label 週期長度從哪裡來:
  a table:
    週期 1：1s → 2
    週期 2：2s 2p → 8
    週期 3：3s 3p → 8（3d 被 4s 擠到下一週期）
    週期 4：4s 3d 4p → 18
    週期 5：5s 4d 5p → 18
    週期 6：6s 4f 5d 6p → 32
    週期 7：7s 5f 6d 7p → 32
  d-subshell cells tinted orange and tagged 過渡元素; f-subshell cells tinted
  purple and tagged 稀土／錒系.

Top-right legend "圖例":
  綠 — s 子殼  藍 — p 子殼  橘 — d 子殼  紫 — f 子殼
  紅圈 — n 較大卻先填的子殼

Bottom pastel formula boxes (three):
1. light green: l 小 → 徑向節點 n − l − 1 多 → 鑽入核心 — 看到較多核電荷，能量較低
2. light orange: l 大 → 離心項 l(l+1)ħ²/2mr² 大 → 被推到核心外 — 幾乎完全被屏蔽，Z_eff ≈ 1
3. light blue: 1s 2s 2p 3s 3p 4s 3d 4p 5s 4d 5p 6s 4f 5d 6p 7s 5f 6d — 填充順序
```
