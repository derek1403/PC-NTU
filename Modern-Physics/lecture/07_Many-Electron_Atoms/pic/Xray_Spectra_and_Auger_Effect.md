# Xray_Spectra_and_Auger_Effect.png

**對應章節：** 7.9 x 射線光譜
**插入位置：**「假設與已知」之後、「推導：$K_\alpha$ 線的頻率與能量」之前
**課本對應：** 圖 7.20（x 射線光譜的來源）＋ 圖 7.21（歐傑效應）＋ 莫斯利定律

> 產圖前請先貼上 `00_STYLE_GUIDE.md` 的風格區塊。

---

## 中文提示詞

```
請畫一張教學用資訊圖表，主題是「特徵 x 射線與歐傑電子是怎麼產生的」。

標題列文字：7.9  x 射線光譜與歐傑效應 (X-Ray Spectra and the Auger Effect)

導言框文字：
高能電子把靶材原子的內層電子撞出去，留下空位；上層電子掉下來補位，
能量差以 x 射線光子放出——或交給另一個外層電子把它踢出去（歐傑效應）。
兩者的能量都只由原子能階決定，所以量它們就能辨認元素。

主體左側（約 35% 寬）｜pill 標籤：x 射線的命名（圖 7.20，不按比例）
畫一張能階圖：五條水平線由下而上標
  K（n = 1）、L（n = 2）、M（n = 3）、N（n = 4）、O（n = 5），
  K 線畫在最下方且與 L 之間的距離最大，往上間距逐漸縮小。
向下的箭頭（同一系列用同一顏色）：
  紅色 K 系列（落到 K）：K_α 從 L、K_β 從 M、K_γ 從 N
  藍色 L 系列（落到 L）：L_α 從 M、L_β 從 N、L_γ 從 O
  綠色 M 系列（落到 M）：M_α 從 N、M_β 從 O
旁邊的說明框：
  字母 = 空位所在的殼（電子最後落入的殼）
  希臘字母 = 從上方第幾層掉下來：α 上一層、β 上兩層、γ 上三層

主體中間（約 35% 寬）｜pill 標籤：兩條出路（圖 7.21）
左邊一個大圓代表原子，裡面三條短橫線代表 K、L、M 能階，橫線上有小黑點（電子）。
  一支從外面射入的黑色箭頭標「高能電子」，把 K 層上的一個電子撞出原子（黑色箭頭射出），
  K 層留下一個空心小圓標「空位」。
從這個原子分出兩支箭頭到右邊兩個小原子圖：
  上方路線，箭頭上標「x 射線放射」：
    小原子圖中 L 層一個電子往下掉進 K 層空位（向下箭頭），
    原子外畫一條紅色波浪線向外射出，標「x 射線光子 hν = B_K − B_L」。
  下方路線，箭頭上標「歐傑效應」：
    小原子圖中 L 層一個電子往下掉進 K 層空位，
    同時 L 或 M 層的另一個電子沿著橘色箭頭被射出原子，標「歐傑電子」。
    下方公式：K_Auger = (B_K − B_L) − B_射出殼
  兩條路線中間標「或」。
  底部小字：x 射線管中大部分能量其實變成熱；輕元素偏向歐傑，重元素偏向 x 射線

主體右側（約 30% 寬）｜pill 標籤：莫斯利定律與例題 7.8
畫一張座標圖：橫軸「原子序 Z」從 10 到 35，縱軸「√ν (√Hz)」。
  畫一條通過 Z = 1 處截距為零的完美直線（√ν ∝ Z − 1），
  在直線上畫幾個藍色資料點，分別標 Al (13)、Ca (20)、Fe (26)、Co (27)、Cu (29)、Zn (30)。
  Co (27) 的點放大成紅色，旁邊標
    「例題 7.8：λ = 0.180 nm → ν ≈ 1.67 × 10¹⁸ Hz → Z − 1 = 26 → Z = 27 鈷」
  圖下方說明：1913 年莫斯利：週期表依原子序（核電荷）排序，不是原子量
  再加一行應用：EDS／XRF（量 x 射線）、AES（量歐傑電子）→ 材料的元素分析

右上角「圖例」方框：
  紅色箭頭 — K 系列
  藍色箭頭 — L 系列
  綠色箭頭 — M 系列
  紅色波浪線 — x 射線光子
  橘色箭頭 — 歐傑電子

最下方一排粉彩公式盒（三個）：
1. 淺紅盒：ν(K_α) = 3cR(Z − 1)²/4　(7.21)，說明「L 電子看到的有效核電荷為 (Z − 1)e」
2. 淺藍盒：E(K_α) = (10.2 eV)(Z − 1)²　(7.22)，說明「核電荷放大的萊曼 α 線；鈷約 6.9 keV」
3. 淺黃盒：K_Auger = (B_空位 − B_填補) − B_射出，說明「歐傑電子動能同樣只由能階決定」
```

## English Prompt

```
Draw an educational infographic titled "how characteristic X-rays and Auger
electrons are produced". ALL labels in TRADITIONAL CHINESE.

Title bar: 7.9  x 射線光譜與歐傑效應 (X-Ray Spectra and the Auger Effect)

Intro box (Traditional Chinese):
高能電子把靶材原子的內層電子撞出去，留下空位；上層電子掉下來補位，
能量差以 x 射線光子放出——或交給另一個外層電子把它踢出去（歐傑效應）。
兩者的能量都只由原子能階決定，所以量它們就能辨認元素。

LEFT ~35%, pill label x 射線的命名（圖 7.20，不按比例）:
An energy-level diagram: five horizontal lines labelled from bottom to top
  K（n = 1）, L（n = 2）, M（n = 3）, N（n = 4）, O（n = 5);
  K at the very bottom with the LARGEST gap to L; gaps shrink going up.
Downward arrows (one colour per series):
  RED K series (ending on K): K_α from L, K_β from M, K_γ from N
  BLUE L series (ending on L): L_α from M, L_β from N, L_γ from O
  GREEN M series (ending on M): M_α from N, M_β from O
A side note box:
  字母 = 空位所在的殼（電子最後落入的殼）
  希臘字母 = 從上方第幾層掉下來：α 上一層、β 上兩層、γ 上三層

CENTRE ~35%, pill label 兩條出路（圖 7.21）:
On the left, a large circle representing the atom, with three short horizontal
lines inside for the K, L, M levels carrying small black dots (electrons).
  A black arrow from outside labelled 高能電子 knocks one K electron out of the
  atom (a black arrow leaving), leaving a hollow small circle on K labelled 空位.
Two arrows branch from this atom to two small atom sketches on the right:
  upper route, arrow labelled x 射線放射:
    in the small atom, an L electron drops into the K vacancy (downward arrow);
    a RED wavy line leaves the atom, labelled x 射線光子 hν = B_K − B_L.
  lower route, arrow labelled 歐傑效應:
    in the small atom, an L electron drops into the K vacancy, while another
    electron from L or M is ejected along an ORANGE arrow, labelled 歐傑電子.
    formula below: K_Auger = (B_K − B_L) − B_射出殼
  the word 或 between the two routes.
  small note at the bottom: x 射線管中大部分能量其實變成熱；輕元素偏向歐傑，重元素偏向 x 射線

RIGHT ~30%, pill label 莫斯利定律與例題 7.8:
A plot: horizontal axis 原子序 Z from 10 to 35, vertical axis √ν (√Hz).
  a perfectly straight line whose extension hits zero at Z = 1 (√ν ∝ Z − 1);
  a few BLUE data points on the line labelled Al (13), Ca (20), Fe (26),
  Co (27), Cu (29), Zn (30).
  The Co (27) point enlarged in RED, annotated
    例題 7.8：λ = 0.180 nm → ν ≈ 1.67 × 10¹⁸ Hz → Z − 1 = 26 → Z = 27 鈷
  caption under the plot: 1913 年莫斯利：週期表依原子序（核電荷）排序，不是原子量
  one more line on applications: EDS／XRF（量 x 射線）、AES（量歐傑電子）→ 材料的元素分析

Top-right legend "圖例":
  紅色箭頭 — K 系列
  藍色箭頭 — L 系列
  綠色箭頭 — M 系列
  紅色波浪線 — x 射線光子
  橘色箭頭 — 歐傑電子

Bottom pastel formula boxes (three):
1. light red: ν(K_α) = 3cR(Z − 1)²/4  (7.21) — L 電子看到的有效核電荷為 (Z − 1)e
2. light blue: E(K_α) = (10.2 eV)(Z − 1)²  (7.22) — 核電荷放大的萊曼 α 線；鈷約 6.9 keV
3. light yellow: K_Auger = (B_空位 − B_填補) − B_射出 — 歐傑電子動能同樣只由能階決定
```
