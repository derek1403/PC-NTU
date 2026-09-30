# Magnetic_Moment_of_Orbital_Electron.png

**對應章節：** 6.10 塞曼效應
**插入位置：**「假設與已知」之後、「推導：磁偶極在磁場中的位能」之前
**課本對應：** 圖 6.16

> 產圖前請先貼上 `00_STYLE_GUIDE.md` 的風格區塊。

---

## 中文提示詞

```
請畫一張教學用資訊圖表，主題是「軌道電子的磁矩：從電流迴路到 μ = −(e/2m)L」。

標題列文字：6.10  軌道電子的磁矩 (Magnetic Moment of an Orbital Electron)

導言框文字：
電子在軌道上繞行，等效於一個電流迴路，因而具有磁偶極矩。
把磁矩與角動量各自用「繞行頻率 f 與半徑 r」表示，兩式相除後 f 與 r² 全部消掉，
留下一個只與電子本身有關的普適比值 −e/2m。

主體上區分成左右兩格，各自上方掛深藍 pill 標籤。

【左格】pill 標籤：(a) 電流迴路的磁矩
- 畫一個水平放置的圓形迴路（藍色 #1565C0），迴路上用箭頭標出電流方向 I。
- 迴路內部用淺藍網底填滿，標為面積 A = πr²，圓心到迴路畫一條半徑標為 r。
- 從圓心垂直於迴路平面向上畫一個紫色（#7B1FA2）粗向量，標為 μ = I A，
  並在向量旁畫一個右手定則的小圖示（四指沿電流、拇指沿 μ）。
- 下方公式盒（淺藍）：μ = I A = I πr²

【右格】pill 標籤：(b) 軌道電子的磁矩
- 畫同樣的圓形迴路，但這次迴路上跑的是一個藍色小圓（電子，標「−e」），
  用橘色箭頭標出電子的運動方向 v，並註明「每秒繞行 f 次」。
- 特別畫出：電流方向（紅色箭頭）與電子運動方向（橘色箭頭）**相反**，
  旁邊小字「電子帶負電，故 I = −e f」。
- 從圓心垂直向上畫一個綠色（#2E7D32）粗向量標為角動量 L = m v r，
  並從圓心垂直**向下**畫一個紫色粗向量標為磁矩 μ。
- 用一條紅色雙箭頭標註兩者反向，旁邊寫「μ 與 L 方向相反」。
- 下方公式盒（淺紫）：μ = (−e f)(πr²)　與　L = m(2πf r)r = 2πm f r²

主體下區｜pill 標籤：兩式相除
畫一個橫跨全寬的推導條，分三步用深藍箭頭串接：
  步驟 1：μ / L = [(−e f)(πr²)] / [2πm f r²]
  步驟 2：把 f 與 r² 消掉（用紅色斜線把分子分母的 f 與 r² 各自劃掉）
  步驟 3（放大字級，深藍粗體）：μ = −(e/2m) L　(6.39)
在步驟 3 下方加一行小字：
  比值 e/2m 稱為旋磁比 (gyromagnetic ratio)，是只跟電子本身有關的普適常數，
  與軌道半徑、繞行頻率完全無關。

右上角「圖例」方框：
  紅色箭頭 — 電流方向 I
  橘色箭頭 — 電子運動方向 v
  綠色向量 — 角動量 L
  紫色向量 — 磁偶極矩 μ

最下方一排粉彩公式盒（四個）：
1. 淺藍盒：μ = I A，說明「電流迴路的磁矩，古典電磁學」
2. 淺綠盒：L = m v r，說明「古典角動量」
3. 淺紫盒：μ = −(e/2m) L，說明「(6.39)，負號來自電子帶負電」
4. 淺黃盒：μ_B = eħ/2m ≈ 9.274×10⁻²⁴ J/T ≈ 5.788×10⁻⁵ eV/T，說明「波耳磁子，(6.42)」
```

## English Prompt

```
Draw an educational infographic titled "Magnetic moment of an orbital electron:
from a current loop to μ = −(e/2m)L". ALL labels in TRADITIONAL CHINESE.

Title bar: 6.10  軌道電子的磁矩 (Magnetic Moment of an Orbital Electron)

Intro box (Traditional Chinese):
電子在軌道上繞行，等效於一個電流迴路，因而具有磁偶極矩。
把磁矩與角動量各自用「繞行頻率 f 與半徑 r」表示，兩式相除後 f 與 r² 全部消掉，
留下一個只與電子本身有關的普適比值 −e/2m。

TOP region split left/right, each with a dark-blue pill label.

[LEFT] pill: (a) 電流迴路的磁矩
- A horizontal circular loop (blue #1565C0) with an arrow marking the current
  direction I.
- The loop interior filled with a light-blue tint labelled 面積 A = πr², with a
  radius line labelled r.
- From the centre, perpendicular to the loop plane and pointing up, a thick purple
  (#7B1FA2) vector labelled μ = I A, with a small right-hand-rule icon beside it
  (fingers along the current, thumb along μ).
- Formula box below (light blue): μ = I A = I πr²

[RIGHT] pill: (b) 軌道電子的磁矩
- The same loop, but now a small blue circle (the electron, labelled −e) travels
  along it, with an ORANGE arrow marking the electron's velocity v and the note
  每秒繞行 f 次.
- Explicitly show that the current direction (RED arrow) is OPPOSITE to the
  electron's motion (orange arrow), with the small note 電子帶負電，故 I = −e f.
- From the centre, a thick GREEN (#2E7D32) vector pointing UP labelled
  角動量 L = m v r, and a thick PURPLE vector pointing DOWN labelled 磁矩 μ.
- A red double-headed arrow annotating μ 與 L 方向相反.
- Formula box below (light purple): μ = (−e f)(πr²)　與　L = m(2πf r)r = 2πm f r²

BOTTOM region, pill label 兩式相除:
A full-width derivation strip in three steps joined by dark-blue arrows:
  Step 1: μ / L = [(−e f)(πr²)] / [2πm f r²]
  Step 2: cancel f and r² (draw red strike-through slashes over the f and r²
          in both numerator and denominator)
  Step 3 (enlarged, dark-blue bold): μ = −(e/2m) L  (6.39)
Small line under step 3:
  比值 e/2m 稱為旋磁比 (gyromagnetic ratio)，是只跟電子本身有關的普適常數，
  與軌道半徑、繞行頻率完全無關。

Top-right legend "圖例":
  紅色箭頭 — 電流方向 I
  橘色箭頭 — 電子運動方向 v
  綠色向量 — 角動量 L
  紫色向量 — 磁偶極矩 μ

Bottom pastel boxes (four):
1. light blue: μ = I A — 電流迴路的磁矩，古典電磁學
2. light green: L = m v r — 古典角動量
3. light purple: μ = −(e/2m) L — (6.39)，負號來自電子帶負電
4. light yellow: μ_B = eħ/2m ≈ 9.274×10⁻²⁴ J/T ≈ 5.788×10⁻⁵ eV/T — 波耳磁子，(6.42)
```
