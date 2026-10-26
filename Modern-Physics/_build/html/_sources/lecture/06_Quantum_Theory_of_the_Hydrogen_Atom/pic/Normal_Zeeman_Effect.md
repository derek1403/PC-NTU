# Normal_Zeeman_Effect.png

**對應章節：** 6.10 塞曼效應
**插入位置：** $(6.41)$ $U_m = m_l\mu_B B$ 之後、「推導：一條譜線分裂成三條」之前
**課本對應：** 圖 6.17

> 產圖前請先貼上 `00_STYLE_GUIDE.md` 的風格區塊。

---

## 中文提示詞

```
請畫一張教學用資訊圖表，主題是「正常塞曼效應：一條譜線為什麼分裂成三條」。

標題列文字：6.10  正常塞曼效應 (The Normal Zeeman Effect)

導言框文字：
沒有磁場時能量與 m_l 無關（簡併）；加了磁場之後，
不同的 m_l 得到不同的磁能 U_m = m_l μ_B B，簡併被打破。
但選擇規則 Δm_l = 0, ±1 把所有可能的躍遷壓縮成只有三種頻率。

主體左半（約 65% 寬）｜pill 標籤：l = 2 → l = 1 的能階分裂與躍遷
畫一張左右對照的能階圖：

左半邊（標「B = 0，無磁場」）：
  上方一條藍色水平能階線標「l = 2」，下方一條藍色水平能階線標「l = 1」，
  兩者之間畫一支垂直向下的黑色箭頭，標「hν₀」，旁邊小字「只有一條譜線」。

右半邊（標「B ≠ 0，加磁場」）：
  上方把 l = 2 畫成**五條**等間距的水平線，由上而下標 m_l = +2, +1, 0, −1, −2，
    間距標為 μ_B B（用大括號標出一格間距）。
  下方把 l = 1 畫成**三條**等間距的水平線，由上而下標 m_l = +1, 0, −1，
    間距同樣為 μ_B B。
  用箭頭畫出所有滿足 Δm_l = 0, ±1 的躍遷（共九條），並依 Δm_l 上色：
    Δm_l = −1：紅色（#C62828）
    Δm_l = 0 ：綠色（#2E7D32）
    Δm_l = +1：藍色（#1565C0）
  在圖旁標註：理論上有 5×3 = 15 種組合，但選擇規則只允許其中九條。

主體左半下方｜pill 標籤：光譜的結果
畫一條水平的頻率軸 ν，在軸上畫三條垂直譜線：
  左邊紅線標 ν₀ − eB/(4πm)
  中間綠線標 ν₀
  右邊藍線標 ν₀ + eB/(4πm)
三條線等間距，間距用雙箭頭標為 μ_B B / h = eB/(4πm)。
軸下方加一行字：九條躍遷只給出三種頻率——因為能量差只取決於 Δm_l。
再加一條對照：在軸的上方用灰色畫出「B = 0 時只有 ν₀ 一條線」。

主體右半（約 35% 寬）：兩個上下堆疊的說明卡。

卡 1｜pill 標籤：磁能公式
  U_m = −μ·B = (e/2m) L B cosθ = m_l (eħ/2m) B = m_l μ_B B　(6.41)
  逐條符號說明：
    U_m：磁能，單位 eV
    m_l：磁量子數，可正可負 → 磁能可增可減
    μ_B：波耳磁子 = eħ/2m ≈ 5.788×10⁻⁵ eV/T
    B：磁場強度，單位 T

卡 2｜pill 標籤：例題 6.4 — 分裂有多小
  條列：
    B = 0.300 T（1 T = 10,000 Gauss）
    Δν = eB/(4πm) ≈ 4.20×10⁹ Hz
    λ = 450 nm
    Δλ = λ²Δν/c ≈ 2.83×10⁻¹² m = 0.00283 nm
  結論（紅色框）：450 nm 分裂成 450.00283 nm 與 449.99717 nm，
  相對變化不到萬分之一——這就是為什麼萊曼、巴耳末當年看不到塞曼效應。
  小字：這類需要高解析度才看得見的結構稱為精細結構 (fine structure)。

右上角「圖例」方框：
  紅色 — Δm_l = −1（頻率變低）
  綠色 — Δm_l = 0（頻率不變）
  藍色 — Δm_l = +1（頻率變高）
  灰色 — 無磁場時的原始譜線 ν₀

最下方一排粉彩公式盒（三個）：
1. 淺藍盒：U_m = m_l μ_B B，說明「不同 m_l 得到不同磁能，簡併被打破」
2. 淺綠盒：ν = ν₀ − Δm_l · eB/(4πm)，說明「(6.43)，只有三種頻率」
3. 淺紅盒：本節只算軌道角動量，說明「真實原子還有自旋，會產生更複雜的異常塞曼效應」
```

## English Prompt

```
Draw an educational infographic titled "The normal Zeeman effect: why one spectral
line splits into three". ALL labels in TRADITIONAL CHINESE.

Title bar: 6.10  正常塞曼效應 (The Normal Zeeman Effect)

Intro box (Traditional Chinese):
沒有磁場時能量與 m_l 無關（簡併）；加了磁場之後，
不同的 m_l 得到不同的磁能 U_m = m_l μ_B B，簡併被打破。
但選擇規則 Δm_l = 0, ±1 把所有可能的躍遷壓縮成只有三種頻率。

LEFT ~65%, pill label l = 2 → l = 1 的能階分裂與躍遷:
A before/after level diagram.

Left side (labelled B = 0，無磁場):
  A blue horizontal level labelled l = 2 above, another labelled l = 1 below,
  with a single vertical black arrow between them labelled hν₀ and the note
  只有一條譜線.

Right side (labelled B ≠ 0，加磁場):
  Split l = 2 into FIVE equally spaced horizontal lines, labelled top to bottom
    m_l = +2, +1, 0, −1, −2, the spacing marked μ_B B with a brace on one gap.
  Split l = 1 into THREE equally spaced lines, labelled top to bottom
    m_l = +1, 0, −1, same spacing μ_B B.
  Draw every transition obeying Δm_l = 0, ±1 (nine of them), coloured by Δm_l:
    Δm_l = −1: red (#C62828)
    Δm_l = 0 : green (#2E7D32)
    Δm_l = +1: blue (#1565C0)
  Annotate: 理論上有 5×3 = 15 種組合，但選擇規則只允許其中九條。

Below that, pill label 光譜的結果:
A horizontal frequency axis ν carrying three vertical spectral lines:
  left, red: ν₀ − eB/(4πm)
  centre, green: ν₀
  right, blue: ν₀ + eB/(4πm)
Equally spaced; mark the spacing with a double arrow labelled μ_B B / h = eB/(4πm).
Caption below the axis: 九條躍遷只給出三種頻率——因為能量差只取決於 Δm_l。
Above the axis, in grey, show the reference case B = 0 時只有 ν₀ 一條線.

RIGHT ~35%: two stacked cards.

Card 1 pill: 磁能公式
  U_m = −μ·B = (e/2m) L B cosθ = m_l (eħ/2m) B = m_l μ_B B  (6.41)
  symbol list:
    U_m：磁能，單位 eV
    m_l：磁量子數，可正可負 → 磁能可增可減
    μ_B：波耳磁子 = eħ/2m ≈ 5.788×10⁻⁵ eV/T
    B：磁場強度，單位 T

Card 2 pill: 例題 6.4 — 分裂有多小
  bullet list:
    B = 0.300 T（1 T = 10,000 Gauss）
    Δν = eB/(4πm) ≈ 4.20×10⁹ Hz
    λ = 450 nm
    Δλ = λ²Δν/c ≈ 2.83×10⁻¹² m = 0.00283 nm
  conclusion in a red box: 450 nm 分裂成 450.00283 nm 與 449.99717 nm，
  相對變化不到萬分之一——這就是為什麼萊曼、巴耳末當年看不到塞曼效應。
  small: 這類需要高解析度才看得見的結構稱為精細結構 (fine structure)。

Top-right legend "圖例":
  紅色 — Δm_l = −1（頻率變低）
  綠色 — Δm_l = 0（頻率不變）
  藍色 — Δm_l = +1（頻率變高）
  灰色 — 無磁場時的原始譜線 ν₀

Bottom pastel boxes (three):
1. light blue: U_m = m_l μ_B B — 不同 m_l 得到不同磁能，簡併被打破
2. light green: ν = ν₀ − Δm_l · eB/(4πm) — (6.43)，只有三種頻率
3. light red: 本節只算軌道角動量 — 真實原子還有自旋，會產生更複雜的異常塞曼效應
```
