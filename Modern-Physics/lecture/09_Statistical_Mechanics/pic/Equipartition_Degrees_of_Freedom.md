# Equipartition_Degrees_of_Freedom.png

**對應章節：** 9.3 理想氣體中的分子能量（能量均分定理）
**插入位置：**「振動為什麼是 $kT$ 而不是 $\frac{1}{2}kT$？」段落之後、【物理知識回顧】之前
**課本對應：** 課本「能量的均分」專欄（投影片第 19 頁）

> 產圖前請先貼上 `00_STYLE_GUIDE.md` 的風格區塊。

---

## 中文提示詞

```
請畫一張教學用資訊圖表，主題是「能量均分定理：每個平方項分到 ½kT」。

標題列文字：9.3  能量均分定理 (Equipartition of Energy)

導言框文字：
在溫度 T 的熱平衡下，古典系統能量公式中每一個「平方項」平均分到 ½kT——
不論質量多大、彈簧多硬。數清楚自由度，就能直接寫出平均能量。
振動同時有動能與位能兩個平方項，所以一個振子分到 kT，而不是 ½kT。

主體分成上下兩區。

【上區｜pill 標籤：常見系統的自由度】
畫一排六張等大的圓角卡片（3 × 2 排列亦可），每張卡片上方是示意圖，
下方是「自由度計算」與「平均能量」（平均能量用大號粗體）：

卡 1「單原子分子（He）」：一顆球，旁邊三支互相垂直的平移箭頭 x、y、z。
  自由度：3 平移　→　(3/2) kT
卡 2「剛體雙原子分子（O₂）」：兩顆球以短棒相連（啞鈴形），三支平移箭頭，
  加上兩個繞「垂直於鍵軸」之軸的彎曲旋轉箭頭；
  繞鍵軸本身的旋轉箭頭畫成灰色並打一個小 ✗，旁註「轉動慣量 ≈ 0，不算」。
  自由度：3 + 2 = 5　→　(5/2) kT
卡 3「剛體線性三原子分子（CO₂）」：O–C–O 排成一直線，同樣 3 平移 + 2 轉動，
  繞分子軸的旋轉打 ✗。
  自由度：3 + 2 = 5　→　(5/2) kT
  卡片角落一個紅色小警示框：「只扣兩條鍵長會誤算成 7；多出來的是彎曲振動，不是轉動」
卡 4「剛體非線性三原子分子（H₂O）」：V 字形分子，3 平移 + 3 轉動。
  自由度：3 + 3 = 6　→　3 kT
卡 5「一維諧振子」：一顆球接在牆上的彈簧，標 ½mv_x² 與 ½K(Δx)² 兩項。
  自由度：1 動能 + 1 位能　→　kT
卡 6「固體晶格中的原子」：一顆球被六根彈簧沿 ±x、±y、±z 連到鄰近原子。
  自由度：3 × (動能 + 位能) = 6　→　3 kT
  旁註：「這是 9.8 杜隆－珀蒂定律 3R 的來源」

【下區左｜pill 標籤：為什麼每個平方項都是 ½kT】
畫一條鐘形（高斯）曲線，橫軸 q，縱軸「機率 ∝ e^(−bq²/kT)」，
旁邊寫：⟨bq²⟩ = ∫ bq² e^(−bq²/kT) dq / ∫ e^(−bq²/kT) dq = ½ kT
並用綠字強調：「結果與係數 b 無關」。
小字：「前提：能量連續（古典）。當 hν ≳ kT 時這個前提失效 → 9.5、9.8」

【下區右｜pill 標籤：電機上的應用：kT/C 雜訊】
畫一個電容器符號 C，兩端電壓 V 隨時間隨機抖動的小波形（雜訊）。
標註：½ C⟨V²⟩ = ½ kT　→　V_rms = √(kT/C)
數值例：C = 1 pF、T = 300 K　→　V_rms ≈ 64 μV

右上角「圖例」方框：
  深藍直箭頭 — 平移自由度
  綠色彎箭頭 — 轉動自由度
  灰色彎箭頭加 ✗ — 不計入的轉動
  彈簧 — 振動（動能＋位能兩個平方項）

最下方一排粉彩公式盒（三個）：
1. 淺綠盒：每個平方項 ⟨bq²⟩ = ½kT，說明「能量均分定理」
2. 淺藍盒：½ m v_x² = ½ m v_y² = ½ m v_z² = ½ kT，說明「三個方向獨立且地位相同」
3. 淺黃盒：一維振子 ε̄ = kT、晶格原子 ε̄ = 3kT，說明「平均動能 = 平均位能」
```

## English Prompt

```
Draw an educational infographic titled "Equipartition: every quadratic term
gets ½kT". ALL labels in TRADITIONAL CHINESE.

Title bar: 9.3  能量均分定理 (Equipartition of Energy)

Intro box (Traditional Chinese):
在溫度 T 的熱平衡下，古典系統能量公式中每一個「平方項」平均分到 ½kT——
不論質量多大、彈簧多硬。數清楚自由度，就能直接寫出平均能量。
振動同時有動能與位能兩個平方項，所以一個振子分到 kT，而不是 ½kT。

Two bands.

TOP band, pill label 常見系統的自由度:
Six equal rounded cards (a 3 × 2 grid is fine). Each card: a sketch on top, then the
degree-of-freedom count and the average energy (average energy in large bold):

Card 1 單原子分子（He）: one sphere with three mutually perpendicular translation arrows x, y, z.
  自由度：3 平移 → (3/2) kT
Card 2 剛體雙原子分子（O₂）: dumbbell (two spheres on a short rod), three translation
  arrows, plus two curved rotation arrows about axes PERPENDICULAR to the bond;
  the rotation about the bond axis itself drawn in grey with a small ✗ and the note
  轉動慣量 ≈ 0，不算.
  自由度：3 + 2 = 5 → (5/2) kT
Card 3 剛體線性三原子分子（CO₂）: O–C–O in a straight line, again 3 translations + 2 rotations,
  rotation about the molecular axis marked ✗.
  自由度：3 + 2 = 5 → (5/2) kT
  small red warning box in the corner: 只扣兩條鍵長會誤算成 7；多出來的是彎曲振動，不是轉動
Card 4 剛體非線性三原子分子（H₂O）: bent V-shaped molecule, 3 translations + 3 rotations.
  自由度：3 + 3 = 6 → 3 kT
Card 5 一維諧振子: a ball on a spring attached to a wall, with the two terms
  ½mv_x² and ½K(Δx)² labelled.
  自由度：1 動能 + 1 位能 → kT
Card 6 固體晶格中的原子: one ball tied by six springs along ±x, ±y, ±z to neighbours.
  自由度：3 × (動能 + 位能) = 6 → 3 kT
  side note: 這是 9.8 杜隆－珀蒂定律 3R 的來源

BOTTOM-LEFT, pill label 為什麼每個平方項都是 ½kT:
A bell (Gaussian) curve, x-axis q, y-axis 機率 ∝ e^(−bq²/kT); beside it:
⟨bq²⟩ = ∫ bq² e^(−bq²/kT) dq / ∫ e^(−bq²/kT) dq = ½ kT,
with green emphasis 結果與係數 b 無關.
Small text: 前提：能量連續（古典）。當 hν ≳ kT 時這個前提失效 → 9.5、9.8

BOTTOM-RIGHT, pill label 電機上的應用：kT/C 雜訊:
A capacitor symbol C with a small randomly jittering voltage waveform V(t) (noise).
Annotations: ½ C⟨V²⟩ = ½ kT → V_rms = √(kT/C)
Numerical example: C = 1 pF、T = 300 K → V_rms ≈ 64 μV

Top-right legend "圖例":
  深藍直箭頭 — 平移自由度
  綠色彎箭頭 — 轉動自由度
  灰色彎箭頭加 ✗ — 不計入的轉動
  彈簧 — 振動（動能＋位能兩個平方項）

Bottom pastel boxes (three):
1. light green: 每個平方項 ⟨bq²⟩ = ½kT — 能量均分定理
2. light blue: ½ m v_x² = ½ m v_y² = ½ m v_z² = ½ kT — 三個方向獨立且地位相同
3. light yellow: 一維振子 ε̄ = kT、晶格原子 ε̄ = 3kT — 平均動能 = 平均位能
```
