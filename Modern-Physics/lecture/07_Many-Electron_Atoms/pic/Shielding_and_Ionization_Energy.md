# Shielding_and_Ionization_Energy.png

**對應章節：** 7.6 解釋週期表
**插入位置：** 7.6 節「假設與已知」之後、「推導：屏蔽的粗糙模型——鈉與氬」之前
**課本對應：** 圖 7.9（鈉與氬的屏蔽）＋ 圖 7.10（游離能隨原子序的變化）＋ 例題 7.2

> 產圖前請先貼上 `00_STYLE_GUIDE.md` 的風格區塊。

---

## 中文提示詞

```
請畫一張教學用資訊圖表，主題是「屏蔽效應如何決定游離能與原子大小」。

標題列文字：7.6  屏蔽效應與游離能 (Shielding and Ionization Energy)

導言框文字：
外層電子看到的核電荷，被內層電子的負電荷部分抵消，等效成 Z_eff·e。
鈉的外層電子只看到約 +1e，氬的外層電子卻看到約 +8e——
所以氬比較小、比較難游離；週期表上游離能的鋸齒狀起伏，全由屏蔽決定。

主體左側（約 35% 寬）｜pill 標籤：粗糙模型：鈉 vs 氬（圖 7.9）
上下兩列，每列左邊是「真實」、中間一個「≈」符號、右邊是「等效」：
  上列（鈉 Na，Z = 11）：
    左：中心小圓標「+11e」，外面兩圈內層軌道（第 1 圈 2 個小黑點、第 2 圈 8 個小黑點），
        最外一圈很大、上面只有 1 個紅點。
    右：一個淺灰色大圓（代表被屏蔽的核心），中心標「+1e」，外圈 1 個紅點。
    下方標「Z_eff ≈ 11 − 10 = 1」。
  下列（氬 Ar，Z = 18）：
    左：中心小圓標「+18e」，第 1 圈 2 點、第 2 圈 8 點，第 3 圈 8 個紅點，
        整體畫得比鈉**小**。
    右：較小的灰色圓，中心標「+8e」，外圈 8 個紅點。
    下方標「Z_eff ≈ 18 − 10 = 8」。
  兩列之間紅字：氬的外層電子受的拉力約是鈉的 8 倍 → 原子較小、游離能較高。

主體中間（約 40% 寬）｜pill 標籤：第一游離能 vs 原子序（圖 7.10）
畫一張折線圖：橫軸「原子序 Z」從 1 到 20，縱軸「游離能 (eV)」從 0 到 26。
請依下列數據逐點描點並以直線相連（單位 eV）：
  1 H 13.6、2 He 24.6、3 Li 5.39、4 Be 9.32、5 B 8.30、6 C 11.3、7 N 14.5、
  8 O 13.6、9 F 17.4、10 Ne 21.6、11 Na 5.14、12 Mg 7.65、13 Al 5.99、
  14 Si 8.15、15 P 10.5、16 S 10.4、17 Cl 13.0、18 Ar 15.8、19 K 4.34、20 Ca 6.11
  三個峰值點（He、Ne、Ar）用紫色大圓點並標元素符號，標註「惰性氣體：峰」；
  三個谷底點（Li、Na、K）用紅色大圓點並標元素符號，標註「鹼金屬：谷」。
  在 Li→Ne、Na→Ar 兩段上方各畫一支淺藍色斜向箭頭，標「同週期：Z_eff 上升 → 游離能上升」；
  在 Ne→Na、Ar→K 的陡降處標「進入新殼：Z_eff 掉回 ≈ 1」。
  圖右上角一個小表格「更重的元素」：Kr 14.0、Xe 12.1（惰性氣體）；Rb 4.18、Cs 3.89（鹼金屬），
  旁註「同一族往下：n 變大、離核變遠 → 游離能下降」。

主體右側（約 25% 寬）｜pill 標籤：例題 7.2：鋰的有效電荷
  條列：
    Li：Z = 3，組態 1s² 2s¹
    E₂ = −5.39 eV，E₁ = −13.6 eV
    E_n = Z²E₁/n² ⇒ Z = 2√(5.39/13.6) ≈ 1.26
  下方畫一張小的徑向機率示意圖 P(r)：
    藍色曲線為 1s（靠近原點的單峰），
    橘色曲線為 2s（主峰在較外側，但在原點附近有一個小的內側峰，
    此小峰用紅色圓圈圈起，標「鑽入 1s 內側 → 看到更多核電荷」）。
  結論（紅框）：屏蔽不完全，Z_eff = 1.26 > 1

右上角「圖例」方框：
  紅點 — 最外層（價）電子
  黑點 — 內層電子
  紫點 — 惰性氣體（游離能峰值）
  紅色大點 — 鹼金屬（游離能谷底）

最下方一排粉彩公式盒（三個）：
1. 淺藍盒：E_n = Z²E₁/n²，說明「核電荷 Ze 的類氫能階（e² → Ze²）」
2. 淺綠盒：Z_eff = Z − σ，說明「σ ≈ 比它更靠內側的電子數」
3. 淺黃盒：同週期 Z_eff ↑ → 半徑 ↓、游離能 ↑；同族往下 n ↑ → 游離能 ↓，說明「圖 7.10、7.11 的趨勢」
```

## English Prompt

```
Draw an educational infographic titled "how shielding sets ionization energy
and atomic size". ALL labels in TRADITIONAL CHINESE.

Title bar: 7.6  屏蔽效應與游離能 (Shielding and Ionization Energy)

Intro box (Traditional Chinese):
外層電子看到的核電荷，被內層電子的負電荷部分抵消，等效成 Z_eff·e。
鈉的外層電子只看到約 +1e，氬的外層電子卻看到約 +8e——
所以氬比較小、比較難游離；週期表上游離能的鋸齒狀起伏，全由屏蔽決定。

LEFT ~35%, pill label 粗糙模型：鈉 vs 氬（圖 7.9）:
Two rows; in each row "real" on the left, a "≈" sign in the middle, "equivalent" on the right:
  upper row (鈉 Na, Z = 11):
    left: a small central circle "+11e", two inner orbits (orbit 1 with 2 small
          black dots, orbit 2 with 8 black dots), and a large outermost orbit with
          only 1 RED dot.
    right: a large light-grey disc (the shielded core) with "+1e" at its centre,
           and 1 red dot on an outer orbit.
    caption: Z_eff ≈ 11 − 10 = 1
  lower row (氬 Ar, Z = 18):
    left: a small central circle "+18e", orbit 1 with 2 dots, orbit 2 with 8 dots,
          orbit 3 with 8 RED dots; the whole atom drawn SMALLER than sodium.
    right: a smaller grey disc with "+8e" at its centre and 8 red dots around it.
    caption: Z_eff ≈ 18 − 10 = 8
  red text between the rows: 氬的外層電子受的拉力約是鈉的 8 倍 → 原子較小、游離能較高。

CENTRE ~40%, pill label 第一游離能 vs 原子序（圖 7.10）:
A line chart: horizontal axis 原子序 Z from 1 to 20, vertical axis 游離能 (eV)
from 0 to 26. Plot these points and join them with straight segments (eV):
  1 H 13.6, 2 He 24.6, 3 Li 5.39, 4 Be 9.32, 5 B 8.30, 6 C 11.3, 7 N 14.5,
  8 O 13.6, 9 F 17.4, 10 Ne 21.6, 11 Na 5.14, 12 Mg 7.65, 13 Al 5.99,
  14 Si 8.15, 15 P 10.5, 16 S 10.4, 17 Cl 13.0, 18 Ar 15.8, 19 K 4.34, 20 Ca 6.11
  The three peaks (He, Ne, Ar): large purple dots with element symbols, annotated 惰性氣體：峰.
  The three troughs (Li, Na, K): large red dots with element symbols, annotated 鹼金屬：谷.
  Above the Li→Ne and Na→Ar stretches, a light-blue slanted arrow labelled
    同週期：Z_eff 上升 → 游離能上升;
  at the sharp drops Ne→Na and Ar→K, the note 進入新殼：Z_eff 掉回 ≈ 1.
  In the chart's upper-right corner a small table 更重的元素:
    Kr 14.0, Xe 12.1 (惰性氣體); Rb 4.18, Cs 3.89 (鹼金屬),
    with the note 同一族往下：n 變大、離核變遠 → 游離能下降.

RIGHT ~25%, pill label 例題 7.2：鋰的有效電荷:
  bullet list:
    Li：Z = 3，組態 1s² 2s¹
    E₂ = −5.39 eV，E₁ = −13.6 eV
    E_n = Z²E₁/n² ⇒ Z = 2√(5.39/13.6) ≈ 1.26
  below it, a small radial-probability sketch P(r):
    blue curve for 1s (a single peak close to the origin);
    orange curve for 2s (main peak farther out, but with a small INNER peak near
    the origin; circle this small peak in red and label it
    鑽入 1s 內側 → 看到更多核電荷).
  conclusion in a red box: 屏蔽不完全，Z_eff = 1.26 > 1

Top-right legend "圖例":
  紅點 — 最外層（價）電子
  黑點 — 內層電子
  紫點 — 惰性氣體（游離能峰值）
  紅色大點 — 鹼金屬（游離能谷底）

Bottom pastel formula boxes (three):
1. light blue: E_n = Z²E₁/n² — 核電荷 Ze 的類氫能階（e² → Ze²）
2. light green: Z_eff = Z − σ — σ ≈ 比它更靠內側的電子數
3. light yellow: 同週期 Z_eff ↑ → 半徑 ↓、游離能 ↑；同族往下 n ↑ → 游離能 ↓ — 圖 7.10、7.11 的趨勢
```
