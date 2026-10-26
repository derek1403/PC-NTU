# Fluorescence_and_Phosphorescence.png

**對應章節：** 8.8 分子的電子光譜
**插入位置：**「螢光的機制」小節末（史托克位移段落之後）、「磷光比螢光更微妙」之前
**課本對應：** 圖 8.24、圖 8.25

> 產圖前請先貼上 `00_STYLE_GUIDE.md` 的風格區塊。

---

## 中文提示詞

```
請畫一張教學用資訊圖表，主題是「螢光與磷光：同樣是分子放光，差在自旋」。

標題列文字：8.8  螢光與磷光 (Fluorescence and Phosphorescence)

導言框文字：
螢光：吸光 → 碰撞把振動能量帶走、掉到受激態谷底 → 放光；顏色與入射光無關，頻率比吸收低。
磷光：分子途中跨進三重態（S = 1），但電子躍遷要求 ΔS = 0，
掉回單重基態是「禁止」的——不是不可能，而是機率極小，所以延遲很久才發光。

主體分左右兩大區，各自是一張「能量 對 象徵座標」的位能曲線圖（縱軸「能量」、橫軸「象徵座標」）。

【左區｜pill 標籤：螢光（圖 8.24）】
  下方一條灰色粗位能曲線標「基態」，井內畫 5 條水平振動能階。
  上方一條灰色粗位能曲線標「受激態」，**整條往右偏移**（平衡鍵長較長），井內畫 5 條振動能階。
  1. 藍色（#1565C0）直線向上箭頭：從基態 υ = 0 垂直往上，打到受激態一條較高的振動能階，標「吸收」。
  2. 一串短的橘色（#EF6C00）波浪向下小箭頭：沿著受激態的振動能階一階一階往下，標「振動躍遷（碰撞，不放光）」。
  3. 綠色（#2E7D32）直線向下箭頭：從受激態谷底垂直往下，落到基態一條較高的振動能階，標「螢光」。
  旁註：綠色箭頭比藍色箭頭短 → 放射頻率比吸收頻率低（史托克位移）。
  旁註：箭頭是垂直的——電子躍遷（~10⁻¹⁵ s）比原子核振動（~10⁻¹⁴ s）快，躍遷瞬間核間距不變。
  左區下方小框：螢光筆照藍光、綠光、紫外光都發同一種顏色，因為都先掉到谷底再放光。

【右區｜pill 標籤：磷光（圖 8.25）】
  下方灰色粗曲線標「單一基態（S = 0）」，井內畫振動能階。
  上方兩條曲線：
    左上一條標「單一受激態（S = 0）」；
    右側略低、再往右偏移的一條標「三重受激態（S = 1）」，兩條曲線在某處交叉。
  1. 藍色直線向上箭頭：單一基態 → 單一受激態，標「吸收（ΔS = 0，允許）」。
  2. 橘色波浪小箭頭：在單一受激態內往下，到達與三重態交會處，再跨入三重受激態，繼續往下到谷底，
     交會處標「系統間跨越」，三重態谷底標「被困住」。
  3. 紫色（#7B1FA2）**虛線**向下箭頭：從三重態谷底到單一基態，標「禁止躍遷（ΔS = 1）→ 延遲放光 = 磷光」。
  曲線旁畫兩個小自旋示意：單一態畫 ↑↓（標「S = 0，1 種」），三重態畫 ↑↑（標「S = 1，3 種」）。

主體下方一條橫向比較表（兩欄）：
  ｜螢光｜磷光｜
  放光的態：單一受激態 → 單一基態 ／ 三重受激態 → 單一基態
  自旋：ΔS = 0（允許）／ ΔS = 1（禁止）
  壽命：約 10⁻⁹ ~ 10⁻⁸ s ／ 毫秒到數小時
  例子：螢光筆、交通標誌 ／ 夜光貼紙、夜光錶面、緊急出口標示

右上角「圖例」方框：
  藍色實線箭頭 — 吸收
  橘色波浪箭頭 — 振動躍遷（碰撞，不放光）
  綠色實線箭頭 — 螢光（允許）
  紫色虛線箭頭 — 磷光（禁止，延遲）

最下方一排粉彩公式盒（三個）：
1. 淺藍盒：∫Ψ_f* r Ψ_i dτ = [∫ψ_f* r ψ_i dV]·⟨s_f|s_i⟩，說明「偶極算符碰不到自旋 → 自旋部分必須相同」
2. 淺紫盒：ΔS = 0，說明「單重態與三重態互相正交 → 之間的輻射躍遷被禁止」
3. 淺黃盒：電注入：單重 : 三重 = 1 : 3，說明「螢光 OLED 最多 25%；加入 Ir 等重金屬增強自旋–軌道耦合，磷光 OLED 可近 100%」
```

## English Prompt

```
Draw an educational infographic titled "Fluorescence and phosphorescence: both are molecular
light emission, the difference is spin". ALL labels in TRADITIONAL CHINESE.

Title bar: 8.8  螢光與磷光 (Fluorescence and Phosphorescence)

Intro box (Traditional Chinese):
螢光：吸光 → 碰撞把振動能量帶走、掉到受激態谷底 → 放光；顏色與入射光無關，頻率比吸收低。
磷光：分子途中跨進三重態（S = 1），但電子躍遷要求 ΔS = 0，
掉回單重基態是「禁止」的——不是不可能，而是機率極小，所以延遲很久才發光。

Two large regions left / right, each an "energy vs. symbolic coordinate" potential-curve
diagram (vertical axis 能量, horizontal axis 象徵座標).

LEFT, pill label 螢光（圖 8.24）:
  A thick grey lower potential curve labelled 基態 with 5 vibrational levels inside.
  A thick grey upper curve labelled 受激態, SHIFTED to the right as a whole (longer
  equilibrium bond), with 5 vibrational levels inside.
  1. A blue (#1565C0) straight upward arrow from the ground-state υ = 0 vertically up to a
     high vibrational level of the excited state, labelled 吸收.
  2. A series of short orange (#EF6C00) wavy downward arrows stepping down the excited-state
     vibrational levels, labelled 振動躍遷（碰撞，不放光）.
  3. A green (#2E7D32) straight downward arrow from the bottom of the excited-state well
     vertically down to a higher vibrational level of the ground state, labelled 螢光.
  Note: 綠色箭頭比藍色箭頭短 → 放射頻率比吸收頻率低（史托克位移）。
  Note: 箭頭是垂直的——電子躍遷（~10⁻¹⁵ s）比原子核振動（~10⁻¹⁴ s）快，躍遷瞬間核間距不變。
  Small box under the left region: 螢光筆照藍光、綠光、紫外光都發同一種顏色，因為都先掉到谷底再放光。

RIGHT, pill label 磷光（圖 8.25）:
  A thick grey lower curve labelled 單一基態（S = 0） with vibrational levels.
  Two upper curves:
    upper-left one labelled 單一受激態（S = 0）;
    a slightly lower one shifted further right labelled 三重受激態（S = 1）; the two curves cross.
  1. A blue straight upward arrow: 單一基態 → 單一受激態, labelled 吸收（ΔS = 0，允許）.
  2. Orange wavy small arrows stepping down inside the singlet excited state to the crossing
     point, then crossing into the triplet curve and continuing down to its bottom; the crossing
     labelled 系統間跨越, the triplet bottom labelled 被困住.
  3. A purple (#7B1FA2) DASHED downward arrow from the triplet bottom to the singlet ground
     state, labelled 禁止躍遷（ΔS = 1）→ 延遲放光 = 磷光.
  Small spin sketches beside the curves: singlet ↑↓ (S = 0，1 種), triplet ↑↑ (S = 1，3 種).

A horizontal comparison table across the bottom of the main area (two columns):
  ｜螢光｜磷光｜
  放光的態：單一受激態 → 單一基態 ／ 三重受激態 → 單一基態
  自旋：ΔS = 0（允許）／ ΔS = 1（禁止）
  壽命：約 10⁻⁹ ~ 10⁻⁸ s ／ 毫秒到數小時
  例子：螢光筆、交通標誌 ／ 夜光貼紙、夜光錶面、緊急出口標示

Top-right legend "圖例":
  藍色實線箭頭 — 吸收
  橘色波浪箭頭 — 振動躍遷（碰撞，不放光）
  綠色實線箭頭 — 螢光（允許）
  紫色虛線箭頭 — 磷光（禁止，延遲）

Bottom pastel boxes (three):
1. light blue: ∫Ψ_f* r Ψ_i dτ = [∫ψ_f* r ψ_i dV]·⟨s_f|s_i⟩ — 偶極算符碰不到自旋 → 自旋部分必須相同
2. light purple: ΔS = 0 — 單重態與三重態互相正交 → 之間的輻射躍遷被禁止
3. light yellow: 電注入：單重 : 三重 = 1 : 3 — 螢光 OLED 最多 25%；加入 Ir 等重金屬增強自旋–軌道耦合，磷光 OLED 可近 100%
```
