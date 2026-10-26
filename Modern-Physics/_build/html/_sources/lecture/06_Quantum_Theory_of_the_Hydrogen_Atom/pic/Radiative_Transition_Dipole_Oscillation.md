# Radiative_Transition_Dipole_Oscillation.png

**對應章節：** 6.8 輻射躍遷
**插入位置：**「假設與已知」之後、「推導：單一定態不會輻射」之前
**課本對應：** 課本 6.8 節配圖

> 產圖前請先貼上 `00_STYLE_GUIDE.md` 的風格區塊。

---

## 中文提示詞

```
請畫一張教學用資訊圖表，主題是「電子躍遷時為什麼會放光」。

標題列文字：6.8  輻射躍遷與電偶極振盪 (Radiative Transition and Dipole Oscillation)

導言框文字：
能階有能量差是一回事，那個能量差為什麼會變成電磁波是另一回事。
答案藏在位置期望值裡：單一定態的 ⟨x⟩ 與時間無關（不放光），
兩態疊加的 ⟨x⟩ 會出現餘弦振盪項，形成電偶極振盪，於是輻射出電磁波。

主體分成左右兩大區，中間用一個深藍色大箭頭連接。

【左區｜pill 標籤：情況 A — 單一定態（不放光）】
上半：畫一個原子示意圖（紅色原子核，外圍灰色虛線球殼），
  電子（藍色小圓）的位置期望值 ⟨x⟩ 用一個綠色實心點標在固定位置，
  旁邊畫一條水平時間軸 t，⟨x⟩ 隨時間為一條水平直線（綠色），完全不動。
下半：公式盒（淺綠）
  Ψ_n = ψ_n e^(−iE_n t/ħ)　(6.26)
  ⟨x⟩ = ∫ ψ_n* x ψ_n dx　(6.27)
  紅字標註：時間因子 e^(+iE_n t/ħ) 與 e^(−iE_n t/ħ) 恰好相消
  結論（綠色 ✓）：期望值與時間無關 → 沒有振盪 → 不輻射 → 定態是穩定的

【右區｜pill 標籤：情況 B — 兩態疊加（放光）】
上半：同樣的原子示意圖，但電子的 ⟨x⟩ 用一個橘色實心點畫在平衡位置上，
  並用左右雙箭頭表示它在該位置附近來回振盪。
  旁邊的時間軸 t 上，⟨x⟩ 畫成一條餘弦曲線（橘色），
  在曲線上標出週期 T 與振幅，並標明「平衡位置」水平虛線。
  在原子右方畫一組同心的波浪線代表放出的電磁波（藍色），標「hν」。
下半：公式盒（淺橘／淺黃）
  Ψ = aΨ_n + bΨ_m　(6.28)
  ⟨x⟩ = [與時間無關的平衡項] + 2ab cos[(E_m − E_n)t/ħ] ∫ ψ_n x ψ_m dx　(6.31)
  ν = (E_m − E_n)/h　→　hν = E_m − E_n　(6.33)
  結論（藍色）：電荷做簡諧振盪 = 振盪的電偶極 → 由古典電磁學輻射出同頻電磁波

在右區的積分項 ∫ ψ_n x ψ_m dx 下方，用紅色虛線框特別圈起來並標註：
  這個積分是振盪的「振幅」。
  若它等於零 → 沒有電偶極振盪 → 不放光（非輻射躍遷）
  → 什麼時候等於零？見 6.9 選擇規則

中間的深藍大箭頭上寫：讓電子可以在兩個能階之間跳動

右上角「圖例」方框：
  綠色 — 情況 A：單一定態，⟨x⟩ 為定值
  橘色 — 情況 B：兩態疊加，⟨x⟩ 做餘弦振盪
  藍色波浪 — 放出的電磁波
  紅色虛線框 — 決定放不放光的關鍵積分

最下方一排粉彩公式盒（三個）：
1. 淺綠盒：定態不輻射，說明「波耳當年必須用假設硬塞，這裡自動成立」
2. 淺橘盒：ν = (E_m − E_n)/h，說明「萊曼系、巴耳末系譜線的來源」
3. 淺紅盒：∫ ψ_n x ψ_m dx = 0 → 非輻射躍遷 (non-radiative transition)
```

## English Prompt

```
Draw an educational infographic titled "why an electron radiates when it makes a
transition". ALL labels in TRADITIONAL CHINESE.

Title bar: 6.8  輻射躍遷與電偶極振盪 (Radiative Transition and Dipole Oscillation)

Intro box (Traditional Chinese):
能階有能量差是一回事，那個能量差為什麼會變成電磁波是另一回事。
答案藏在位置期望值裡：單一定態的 ⟨x⟩ 與時間無關（不放光），
兩態疊加的 ⟨x⟩ 會出現餘弦振盪項，形成電偶極振盪，於是輻射出電磁波。

Two regions left/right joined by a large dark-blue arrow.

LEFT, pill label 情況 A — 單一定態（不放光）:
  top: an atom schematic (red nucleus, grey dashed shell). The electron's position
  expectation ⟨x⟩ is a green filled dot at a fixed spot. Beside it a horizontal
  time axis t on which ⟨x⟩ is a perfectly flat green line.
  bottom: a light-green formula box
    Ψ_n = ψ_n e^(−iE_n t/ħ)  (6.26)
    ⟨x⟩ = ∫ ψ_n* x ψ_n dx  (6.27)
    red note: 時間因子 e^(+iE_n t/ħ) 與 e^(−iE_n t/ħ) 恰好相消
    conclusion with a green ✓: 期望值與時間無關 → 沒有振盪 → 不輻射 → 定態是穩定的

RIGHT, pill label 情況 B — 兩態疊加（放光）:
  top: the same atom schematic, but ⟨x⟩ is an orange dot at an equilibrium position
  with a left-right double arrow showing it oscillating about that point.
  On the time axis, ⟨x⟩ is an orange cosine curve with the period T and amplitude
  marked and a dashed horizontal line labelled 平衡位置.
  To the right of the atom, concentric blue wavy arcs represent the emitted
  electromagnetic wave, labelled hν.
  bottom: a light-orange/light-yellow formula box
    Ψ = aΨ_n + bΨ_m  (6.28)
    ⟨x⟩ = [與時間無關的平衡項] + 2ab cos[(E_m − E_n)t/ħ] ∫ ψ_n x ψ_m dx  (6.31)
    ν = (E_m − E_n)/h  →  hν = E_m − E_n  (6.33)
    conclusion in blue: 電荷做簡諧振盪 = 振盪的電偶極 → 由古典電磁學輻射出同頻電磁波

Below the integral ∫ ψ_n x ψ_m dx, draw a red dashed box around it and annotate:
  這個積分是振盪的「振幅」。
  若它等於零 → 沒有電偶極振盪 → 不放光（非輻射躍遷）
  → 什麼時候等於零？見 6.9 選擇規則

The large dark-blue arrow between the regions is labelled:
  讓電子可以在兩個能階之間跳動

Top-right legend "圖例":
  綠色 — 情況 A：單一定態，⟨x⟩ 為定值
  橘色 — 情況 B：兩態疊加，⟨x⟩ 做餘弦振盪
  藍色波浪 — 放出的電磁波
  紅色虛線框 — 決定放不放光的關鍵積分

Bottom pastel boxes (three):
1. light green: 定態不輻射 — 波耳當年必須用假設硬塞，這裡自動成立
2. light orange: ν = (E_m − E_n)/h — 萊曼系、巴耳末系譜線的來源
3. light red: ∫ ψ_n x ψ_m dx = 0 → 非輻射躍遷 (non-radiative transition)
```
