# Momentum_Space_and_Energy_Distribution.png

**對應章節：** 9.3 理想氣體中的分子能量
**插入位置：** $(9.11)$ 分子能量分布之後、「推導：總能量與平均能量」之前
**課本對應：** 圖 9.1、圖 9.2

> 產圖前請先貼上 `00_STYLE_GUIDE.md` 的風格區塊。

---

## 中文提示詞

```
請畫一張教學用資訊圖表，主題是「g(ε) 數不出來時，先到動量空間去數」。

標題列文字：9.3  動量空間與分子能量分布 (Momentum Space and the Energy Distribution)

導言框文字：
10²⁵ 個分子的能階密到無法逐一列出，g(ε) 沒辦法直接數。
但動量空間是均勻、等向的——態數只正比於體積。先在動量空間數球殼，
再用 p = √(2mε) 換回能量，就得到 g(ε) ∝ √ε，乘上 e^(−ε/kT) 便是能量分布。

主體分成左、中、右三欄。

左欄｜pill 標籤：動量空間的球殼（圖 9.1）
畫三維座標軸 p_x、p_y、p_z（深藍色），空間中均勻散布淡灰色小點（代表動量態）。
以原點為中心畫一個半透明的藍色薄球殼，內半徑標 p、外半徑標 p + dp，
厚度用小雙箭頭標 dp。旁邊註明：
  「三個方向互相獨立、地位相同 → 態均勻分布」
  「球殼體積 = 4πp² dp → g(p) dp = Bp² dp」　(9.5)

中欄｜pill 標籤：變數變換三步驟
由上而下三個淺藍圓角框，用深藍箭頭連接：
  框 1：g(p) dp = B p² dp　(9.5)
  箭頭旁橘字：p = (2mε)^(1/2)，dp = (m/2ε)^(1/2) dε
  框 2：g(ε) dε = √2 m^(3/2) B √ε dε　(9.7)　　綠字：態數 ∝ √ε
  箭頭旁橘字：乘上 f_MB = A e^(−ε/kT)，再用 ∫ n dε = N 歸一化
  框 3：n(ε) dε = [2πN / (πkT)^(3/2)] √ε e^(−ε/kT) dε　(9.11)

右欄｜pill 標籤：分子能量分布（圖 9.2）
一張平面圖，橫軸 ε，刻度標 0、kT、2kT、3kT、4kT；縱軸 n(ε)（不標數值）。
畫三條曲線：
  橘色虛線：√ε（由 0 往上升，起點斜率無限大）
  紫色虛線：e^(−ε/kT)（由 1 往下衰減）
  綠色粗實線（#2E7D32）：兩者乘積 n(ε)——在 ε = 0 為零、迅速上升、
    在 ε = kT/2 達到峰值、之後拖一條長尾巴緩慢下降。
在 ε = kT/2 畫一條灰色細虛線，標「峰值 ε = ½kT」；
在 ε = 1.5kT 畫一條深藍色細虛線，標「平均值 ε̄ = (3/2)kT」，
並加小字「長尾巴把平均值往右拉」。

右上角「圖例」方框：
  綠色實線 — n(ε)：馬克士威爾－波茲曼能量分布
  橘色虛線 — √ε：態數上升
  紫色虛線 — e^(−ε/kT)：佔據機率下降
  深藍虛線 — 平均能量 (3/2)kT

最下方一排粉彩公式盒（三個）：
1. 淺綠盒：C = 2πN / (πkT)^(3/2)，說明「(9.10) 歸一化常數與 N 成正比」
2. 淺藍盒：E = (3/2) N k T，說明「(9.12) N 個分子的總能量」
3. 淺黃盒：ε̄ = (3/2) k T，說明「(9.13) 普物理想氣體動力論的結果」
```

## English Prompt

```
Draw an educational infographic titled "When g(ε) cannot be counted directly,
count in momentum space first". ALL labels in TRADITIONAL CHINESE.

Title bar: 9.3  動量空間與分子能量分布 (Momentum Space and the Energy Distribution)

Intro box (Traditional Chinese):
10²⁵ 個分子的能階密到無法逐一列出，g(ε) 沒辦法直接數。
但動量空間是均勻、等向的——態數只正比於體積。先在動量空間數球殼，
再用 p = √(2mε) 換回能量，就得到 g(ε) ∝ √ε，乘上 e^(−ε/kT) 便是能量分布。

Three columns.

LEFT column, pill label 動量空間的球殼（圖 9.1）:
3D axes p_x, p_y, p_z in dark blue; faint grey dots spread uniformly in space
(momentum states). A semi-transparent blue thin spherical shell centred at the origin,
inner radius labelled p, outer radius p + dp, thickness marked dp with a small
double arrow. Notes:
  三個方向互相獨立、地位相同 → 態均勻分布
  球殼體積 = 4πp² dp → g(p) dp = Bp² dp　(9.5)

MIDDLE column, pill label 變數變換三步驟:
Three light-blue rounded boxes stacked vertically and joined by dark-blue arrows:
  Box 1: g(p) dp = B p² dp　(9.5)
  orange arrow note: p = (2mε)^(1/2)，dp = (m/2ε)^(1/2) dε
  Box 2: g(ε) dε = √2 m^(3/2) B √ε dε　(9.7), green note 態數 ∝ √ε
  orange arrow note: 乘上 f_MB = A e^(−ε/kT)，再用 ∫ n dε = N 歸一化
  Box 3: n(ε) dε = [2πN / (πkT)^(3/2)] √ε e^(−ε/kT) dε　(9.11)

RIGHT column, pill label 分子能量分布（圖 9.2）:
A 2D plot; x-axis ε with ticks 0, kT, 2kT, 3kT, 4kT; y-axis n(ε) (no numbers).
Three curves:
  orange dashed: √ε (rising from 0 with infinite initial slope)
  purple dashed: e^(−ε/kT) (decaying from 1)
  thick solid green (#2E7D32): their product n(ε) — zero at ε = 0, rises steeply,
    peaks at ε = kT/2, then a long slowly decaying tail.
Thin grey dashed vertical line at ε = kT/2 labelled 峰值 ε = ½kT;
thin dark-blue dashed vertical line at ε = 1.5kT labelled 平均值 ε̄ = (3/2)kT,
with small text 長尾巴把平均值往右拉.

Top-right legend "圖例":
  綠色實線 — n(ε)：馬克士威爾－波茲曼能量分布
  橘色虛線 — √ε：態數上升
  紫色虛線 — e^(−ε/kT)：佔據機率下降
  深藍虛線 — 平均能量 (3/2)kT

Bottom pastel boxes (three):
1. light green: C = 2πN / (πkT)^(3/2) — (9.10) 歸一化常數與 N 成正比
2. light blue: E = (3/2) N k T — (9.12) N 個分子的總能量
3. light yellow: ε̄ = (3/2) k T — (9.13) 普物理想氣體動力論的結果
```
