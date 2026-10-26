# Rigid_Rotor_Levels_and_Spectrum.png

**對應章節：** 8.6 轉動能階
**插入位置：**「假設與已知」之後、「推導：轉動慣量與縮減質量」之前
**課本對應：** 圖 8.17 ＋ 式 (8.3)–(8.11)

> 產圖前請先貼上 `00_STYLE_GUIDE.md` 的風格區塊。

---

## 中文提示詞

```
【模型與符號】剛性雙原子轉子，固定 R、I=μR²；μ=m₁m₂/(m₁+m₂)，若原圖寫 m′，即同一約化質量。純轉動電偶極光譜須有永久偶極，ΔJ=±1；高 J 離心伸長不在本圖。

請畫一張教學用資訊圖表，主題是「剛性轉子：能階越往上越寬，光譜線卻等間距」。

標題列文字：8.6  轉動能階與轉動光譜 (Rotational Levels and Spectrum)

導言框文字：
雙原子分子繞質心轉動，等效於一顆質量為縮減質量 m′ 的質點在半徑 R 的圓上轉。
角動量照樣量子化 L = √(J(J+1)) ħ，於是 E_J = J(J+1)ħ²/2I；
選擇規則 ΔJ = ±1 讓吸收線的頻率 ν = ħ(J+1)/(2πI) 等間距排開。

主體分成左、中、右三區。

左區｜pill 標籤：剛性轉子 = 縮減質量
  上：兩顆球（左小灰球標 m₁，右大紅球標 m₂）用一根剛性細桿連接，總長標 R；
      桿上標出質心 CM（黑色叉號），CM 到 m₁ 標 r₁、到 m₂ 標 r₂（r₁ > r₂，因為 m₁ 較輕）；
      通過 CM、垂直於桿畫一條虛線轉軸，旁邊一支彎箭頭標 ω。
  中間一個大等號「＝」。
  下：一顆質量 m′ 的球在半徑 R 的圓上轉動，圓心為軸，標「m′ = m₁m₂/(m₁+m₂)」。
  小字：I = m₁r₁² + m₂r₂² = m′R²　(8.5)

中區｜pill 標籤：能階與光譜（圖 8.17）
  縱軸 E_J，單位 ħ²/2I。畫五條水平線，高度**必須按比例**：
    J = 0：0
    J = 1：2
    J = 2：6
    J = 3：12
    J = 4：20
  每條線右側標 J 值與能量（0, 2, 6, 12, 20）× ħ²/2I。
  用四支灰色向上箭頭畫出 J=0→1、1→2、2→3、3→4 的吸收，箭頭長度分別是 2、4、6、8 單位，
    依序向右錯開排列。
  下方畫一條水平頻率軸 ν，上面四條等間距的短垂直線，對應四支箭頭，
    標 ν = 1, 2, 3, 4 × ħ/(2πI)，相鄰間距用雙箭頭標「ħ/(2πI)，等間距」。

右區｜pill 標籤：CO 的數字（例題 8.1、8.2）
  條列：
    m′ = 1.14 × 10⁻²⁶ kg
    R = 0.113 nm → I = 1.46 × 10⁻⁴⁶ kg·m²
    E(J=1) = ħ²/I = 4.75 × 10⁻⁴ eV
    ω(J=1) = 1.02 × 10¹² rad/s（每秒約 1.6 × 10¹¹ 圈）
    ν(0→1) = 1.15 × 10¹¹ Hz，λ ≈ 2.6 mm（微波）
  紅色框：反過來用——量到 ν(0→1) 就能反推鍵長 R，化學鍵長多半是這樣量來的。

右上角「圖例」方框：
  黑色水平線 — 轉動能階 E_J
  灰色箭頭 — ΔJ = +1 的吸收躍遷
  短垂直線 — 轉動光譜線

最下方一排粉彩公式盒（三個）：
1. 淺藍盒：E_J = L²/2I = J(J+1)ħ²/2I　(8.9)，說明「J = 0 時 E = 0：轉動沒有零點能量」
2. 淺綠盒：ΔJ = ±1　(8.10)，說明「與第六章 Δl = ±1 同源；只有極性分子有純轉動光譜」
3. 淺黃盒：ν_{J→J+1} = ħ(J+1)/(2πI)　(8.11)，說明「能階間距越來越寬，譜線卻等間距」
```

## English Prompt

```
MODEL AND NOTATION: Rigid diatomic rotor: fixed R and I=μR², μ=m₁m₂/(m₁+m₂), identical to m′ in the original notation. Pure rotational electric-dipole spectra require a permanent dipole and ΔJ=±1. Exclude high-J centrifugal distortion.

Draw an educational infographic titled "The rigid rotor: levels spread apart, spectral lines
stay equally spaced". ALL labels in TRADITIONAL CHINESE.

Title bar: 8.6  轉動能階與轉動光譜 (Rotational Levels and Spectrum)

Intro box (Traditional Chinese):
雙原子分子繞質心轉動，等效於一顆質量為縮減質量 m′ 的質點在半徑 R 的圓上轉。
角動量照樣量子化 L = √(J(J+1)) ħ，於是 E_J = J(J+1)ħ²/2I；
選擇規則 ΔJ = ±1 讓吸收線的頻率 ν = ħ(J+1)/(2πI) 等間距排開。

Three regions: left, centre, right.

LEFT, pill label 剛性轉子 = 縮減質量:
  top: two balls (left small grey ball m₁, right larger red ball m₂) joined by a rigid thin
       rod of total length R; the centre of mass CM marked with a black cross on the rod,
       with r₁ from CM to m₁ and r₂ from CM to m₂ (r₁ > r₂ because m₁ is lighter); a dashed
       rotation axis through CM perpendicular to the rod, with a curved arrow labelled ω.
  a large equals sign "＝" in the middle.
  bottom: a single ball of mass m′ moving on a circle of radius R about the axis,
       labelled m′ = m₁m₂/(m₁+m₂).
  small text: I = m₁r₁² + m₂r₂² = m′R²  (8.5)

CENTRE, pill label 能階與光譜（圖 8.17）:
  Vertical axis E_J in units of ħ²/2I. Five horizontal lines whose heights MUST be to scale:
    J = 0: 0
    J = 1: 2
    J = 2: 6
    J = 3: 12
    J = 4: 20
  Label each line on the right with J and its energy (0, 2, 6, 12, 20) × ħ²/2I.
  Four grey upward arrows for J=0→1, 1→2, 2→3, 3→4 absorption, of lengths 2, 4, 6, 8 units,
    staggered to the right one after another.
  Below, a horizontal frequency axis ν with four short vertical lines, EQUALLY spaced,
    one per arrow, labelled ν = 1, 2, 3, 4 × ħ/(2πI); a double arrow between neighbours
    labelled ħ/(2πI)，等間距.

RIGHT, pill label CO 的數字（例題 8.1、8.2）:
  bullets:
    m′ = 1.14 × 10⁻²⁶ kg
    R = 0.113 nm → I = 1.46 × 10⁻⁴⁶ kg·m²
    E(J=1) = ħ²/I = 4.75 × 10⁻⁴ eV
    ω(J=1) = 1.02 × 10¹² rad/s（每秒約 1.6 × 10¹¹ 圈）
    ν(0→1) = 1.15 × 10¹¹ Hz，λ ≈ 2.6 mm（微波）
  red box: 反過來用——量到 ν(0→1) 就能反推鍵長 R，化學鍵長多半是這樣量來的。

Top-right legend "圖例":
  黑色水平線 — 轉動能階 E_J
  灰色箭頭 — ΔJ = +1 的吸收躍遷
  短垂直線 — 轉動光譜線

Bottom pastel boxes (three):
1. light blue: E_J = L²/2I = J(J+1)ħ²/2I  (8.9) — J = 0 時 E = 0：轉動沒有零點能量
2. light green: ΔJ = ±1  (8.10) — 與第六章 Δl = ±1 同源；只有極性分子有純轉動光譜
3. light yellow: ν_{J→J+1} = ħ(J+1)/(2πI)  (8.11) — 能階間距越來越寬，譜線卻等間距
```
