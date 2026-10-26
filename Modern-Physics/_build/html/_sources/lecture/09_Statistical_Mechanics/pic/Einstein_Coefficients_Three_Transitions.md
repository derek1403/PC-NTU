# Einstein_Coefficients_Three_Transitions.png

**對應章節：** 9.7 愛因斯坦的處理方法
**插入位置：**「假設與已知」之後、「推導：平衡條件下的輻射能量密度」之前
**課本對應：** 圖 9.9

> 產圖前請先貼上 `00_STYLE_GUIDE.md` 的風格區塊。

---

## 中文提示詞

```
【模型與符號】B_ij=B_ji 的圖示假設兩能級簡併度相同；一般式為 g_i B_ij=g_j B_ji。此處 g_i 是簡併度，不是連續態密度。

請畫一張教學用資訊圖表，主題是「愛因斯坦的三種躍遷：受激吸收、自發放射、受激放射」。

標題列文字：9.7  愛因斯坦係數與受激放射 (Einstein Coefficients and Stimulated Emission)

導言框文字：
兩個能階之間有三種躍遷：受激吸收、自發放射、受激放射。
只要求「熱平衡」與「平衡輻射必須是普朗克公式」，三個係數的關係就被完全鎖定：
B_ij = B_ji，A_ji/B_ji = 8πhν³/c³——受激放射必然存在，而且是雷射的根源。

主體分成左右兩區。

左區（約 60% 寬）｜pill 標籤：三種躍遷（圖 9.9）
畫兩條橫貫整個左區的水平能階線：上方標「E_j（N_j 個原子）」，下方標「E_i（N_i 個原子）」，
右端標「hν = E_j − E_i　(9.42)」。在兩線之間分成三欄：
  第一欄「受激吸收」：一支深藍粗箭頭由 E_i 向上指到 E_j；
    左側一支藍色波浪小箭頭（入射光子 hν）射向原子；
    欄內標「每秒 N_i B_ij u(ν)　(9.43)」；小字「一定要有光子進來，沒有『自發吸收』」。
  第二欄「自發放射」：一支綠色粗箭頭由 E_j 向下指到 E_i；
    一支藍色波浪小箭頭以斜向（任意方向）離開；
    欄內標「每秒 N_j A_ji」；小字「不需外來光子，方向、相位隨機」。
  第三欄「受激放射」：一支紅色粗箭頭由 E_j 向下指到 E_i；
    左側一支入射光子 hν 射入，右側射出**兩支完全平行、波形對齊（同相位）**的波浪箭頭，
    各標 hν；欄內標「每秒 N_j B_ji u(ν)」；
    小字「放出的光子與入射光子同頻率、同方向、同相位」。
三欄下方一個淺灰色長框寫平衡條件：
  「平衡：N_i B_ij u(ν) = N_j [A_ji + B_ji u(ν)]　(9.43) = (9.44)」
  「波茲曼分布：N_i / N_j = e^(hν/kT)　(9.46)」

右區（約 40% 寬）：上下兩張說明卡。

卡 1｜pill 標籤：與普朗克公式比較的結論
  三行粗體條列：
    ① B_ij = B_ji　(9.48)：受激放射與受激吸收機率相同
    ② A_ji / B_ji = 8πhν³/c³　(9.49)：頻率愈高，自發放射愈占優勢
    ③ 三個係數只要量一個，其餘兩個就能算出
  底下一個小表「熱輻射中 自發 : 受激 = e^(hν/kT) − 1」：
    可見光 500 nm、300 K　→　≈ 4.5 × 10⁴¹
    可見光 500 nm、6000 K　→　≈ 120
    微波 1 mm、300 K　→　≈ 0.05（受激勝出）

卡 2｜pill 標籤：雷射需要居量反轉
  左右兩個小能階圖對照：
    左「熱平衡」：下能階畫很多小圓點、上能階只有少數，標「N_j/N_i = e^(−hν/kT) < 1 → 吸收多於受激放射」
    右「居量反轉（pump）」：上能階圓點多於下能階，標「N_j > N_i → 光被放大」
  底下一條小時間軸：1917 愛因斯坦預測受激放射 → 1954 邁射（微波）→ 1960 紅寶石雷射（可見光）。

右上角「圖例」方框：
  藍色波浪箭頭 — 光子 hν
  深藍粗箭頭 — 受激吸收（係數 B_ij）
  綠色粗箭頭 — 自發放射（係數 A_ji）
  紅色粗箭頭 — 受激放射（係數 B_ji）

最下方一排粉彩公式盒（三個）：
1. 淺藍盒：u(ν) = (A_ji/B_ji) / [(B_ij/B_ji) e^(hν/kT) − 1]，說明「(9.47) 原子與光平衡的要求」
2. 淺綠盒：B_ij = B_ji，A_ji/B_ji = 8πhν³/c³，說明「(9.48)(9.49) 與普朗克公式逐項比對」
3. 淺紅盒：N_j B u > N_i B u ⇔ N_j > N_i，說明「熱平衡永遠做不出雷射，必須打出居量反轉」
```

## English Prompt

```
MODEL AND NOTATION: The depicted B_ij=B_ji assumes equal level degeneracies; generally g_i B_ij=g_j B_ji. Here g_i is degeneracy, not a continuous density of states.

Draw an educational infographic titled "Einstein's three transitions: induced
absorption, spontaneous emission, stimulated emission". ALL labels in TRADITIONAL CHINESE.

Title bar: 9.7  愛因斯坦係數與受激放射 (Einstein Coefficients and Stimulated Emission)

Intro box (Traditional Chinese):
兩個能階之間有三種躍遷：受激吸收、自發放射、受激放射。
只要求「熱平衡」與「平衡輻射必須是普朗克公式」，三個係數的關係就被完全鎖定：
B_ij = B_ji，A_ji/B_ji = 8πhν³/c³——受激放射必然存在，而且是雷射的根源。

LEFT ~60%, pill label 三種躍遷（圖 9.9）:
Two horizontal level lines spanning the whole left area: the upper one labelled
E_j（N_j 個原子）, the lower one E_i（N_i 個原子）, and at the right end hν = E_j − E_i　(9.42).
Between them, three columns:
  Column 1 受激吸收: a thick dark-blue arrow pointing UP from E_i to E_j;
    a small blue wavy arrow (incoming photon hν) arriving from the left;
    label 每秒 N_i B_ij u(ν)　(9.43); small text 一定要有光子進來，沒有『自發吸收』.
  Column 2 自發放射: a thick green arrow pointing DOWN from E_j to E_i;
    one blue wavy arrow leaving at an oblique (random) angle;
    label 每秒 N_j A_ji; small text 不需外來光子，方向、相位隨機.
  Column 3 受激放射: a thick red arrow pointing DOWN from E_j to E_i;
    one photon hν coming in from the left, and on the right TWO PERFECTLY PARALLEL wavy
    arrows with aligned crests (in phase) leaving, each labelled hν;
    label 每秒 N_j B_ji u(ν); small text 放出的光子與入射光子同頻率、同方向、同相位.
Under the three columns, a long light-grey box with the balance condition:
  平衡：N_i B_ij u(ν) = N_j [A_ji + B_ji u(ν)]　(9.43) = (9.44)
  波茲曼分布：N_i / N_j = e^(hν/kT)　(9.46)

RIGHT ~40%: two stacked cards.

Card 1, pill label 與普朗克公式比較的結論:
  three bold bullet lines:
    ① B_ij = B_ji　(9.48)：受激放射與受激吸收機率相同
    ② A_ji / B_ji = 8πhν³/c³　(9.49)：頻率愈高，自發放射愈占優勢
    ③ 三個係數只要量一個，其餘兩個就能算出
  below, a small table titled 熱輻射中 自發 : 受激 = e^(hν/kT) − 1:
    可見光 500 nm、300 K → ≈ 4.5 × 10⁴¹
    可見光 500 nm、6000 K → ≈ 120
    微波 1 mm、300 K → ≈ 0.05（受激勝出）

Card 2, pill label 雷射需要居量反轉:
  Two small level diagrams side by side:
    left 熱平衡: many dots on the lower level, few on the upper, labelled
      N_j/N_i = e^(−hν/kT) < 1 → 吸收多於受激放射
    right 居量反轉（pump）: more dots on the upper level than the lower, labelled
      N_j > N_i → 光被放大
  A small timeline underneath: 1917 愛因斯坦預測受激放射 → 1954 邁射（微波）→ 1960 紅寶石雷射（可見光）.

Top-right legend "圖例":
  藍色波浪箭頭 — 光子 hν
  深藍粗箭頭 — 受激吸收（係數 B_ij）
  綠色粗箭頭 — 自發放射（係數 A_ji）
  紅色粗箭頭 — 受激放射（係數 B_ji）

Bottom pastel boxes (three):
1. light blue: u(ν) = (A_ji/B_ji) / [(B_ij/B_ji) e^(hν/kT) − 1] — (9.47) 原子與光平衡的要求
2. light green: B_ij = B_ji，A_ji/B_ji = 8πhν³/c³ — (9.48)(9.49) 與普朗克公式逐項比對
3. light red: N_j B u > N_i B u ⇔ N_j > N_i — 熱平衡永遠做不出雷射，必須打出居量反轉
```
