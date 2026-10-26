# Double_Well_Electron_Sharing.png

**對應章節：** 8.2 電子共享
**插入位置：**「雙位能井：一對被障壁隔開的箱子」小節末（$R \sim 0.1 \ \text{nm}$ 的條列之後）、「假設與已知」之前
**課本對應：** 圖 8.4

> 產圖前請先貼上 `00_STYLE_GUIDE.md` 的風格區塊。

---

## 中文提示詞

```
請畫一張教學用資訊圖表，主題是「H₂⁺ 中的電子：兩個位能井、一道障壁，何時才算共享」。

標題列文字：8.2  雙位能井與電子共享 (Double Well and Electron Sharing)

導言框文字：
H₂⁺ 的電子同時受兩個質子吸引，沿兩質子連線看是兩個庫侖位能井夾著一道障壁。
量子力學上這相當於一對被障壁隔開的箱子：質子離得遠時電子只能靠穿隧往返，
離得近時障壁形同消失，電子才真正被兩個質子共享。

主體左半（約 60% 寬）：兩張上下堆疊的位能圖，橫軸皆為沿兩質子連線的位置，縱軸為位能 U_e（eV）。

上圖｜pill 標籤：情況 A — R 大（R ≳ 0.42 nm）
  兩個紅色質子標「質子 a」「質子 b」，中間雙箭頭標 R。
  畫兩個深而尖的 1/r 型位能井（藍色曲線 #1565C0），兩井之間的障壁頂端**高於**
  一條水平綠色虛線（#2E7D32，標「電子能量 ≈ −13.6 eV」）。
  綠線只畫在左井內；從左井到右井畫一支穿過障壁的橘色（#EF6C00）虛線箭頭，標「穿隧（很罕見）」。
  旁邊小字：障壁又寬又高 → 電子實際上只屬於一個質子（氫原子 + 裸質子）。

下圖｜pill 標籤：情況 B — R 小（R ~ 0.1 nm）
  同樣的兩個井，但距離較近，兩井之間的障壁頂端很低（標「障壁頂 ≈ −54 eV」），
  而綠色電子能量虛線（標「電子能量 ≈ −30 eV」）**橫跨兩個井、高於障壁頂**，連成一整條。
  旁邊小字：障壁形同消失 → 電子在兩核之間自由來去 = 共享。

主體右半（約 40% 寬）：

卡 1｜pill 標籤：量子力學的圖像（圖 8.4b）
  畫一塊灰色立體方塊，上面挖了兩個漏斗狀的凹洞（代表兩個位能井），
  其中一個漏斗裡有一顆藍色小球標「電子」，兩漏斗之間的方塊表面標「障壁」。
  底下文字：一對被障壁隔開的箱子。

卡 2｜pill 標籤：障壁有多高？
  U_e(中點) = −2 · e²/[4πε₀(R/2)] = −4 × 1.44 eV·nm / R
  令它等於 −13.6 eV → R ≈ 0.42 nm
  條列：
    R > 0.42 nm：障壁高於電子能量 → 只能穿隧
    R < 0.42 nm：障壁低於電子能量 → 電子自由往返

右上角「圖例」方框：
  紅色圓點 — 質子
  藍色曲線 — 電子位能 U_e
  綠色虛線 — 電子能量
  橘色虛線箭頭 — 穿隧

最下方一排粉彩公式盒（三個）：
1. 淺藍盒：U_e = −e²/(4πε₀|r − r_a|) − e²/(4πε₀|r − r_b|)，說明「電子感受到的兩個庫侖井」
2. 淺黃盒：穿隧機率對障壁寬度呈指數敏感，說明「R 越大，電子越難跑到另一邊（第五章 5.7 穿隧效應）」
3. 淺綠盒：R ~ 0.1 nm 時電子每秒往返約 10¹⁵ 次，說明「詳見 8.3 進階探討」
```

## English Prompt

```
Draw an educational infographic titled "The electron in H₂⁺: two wells, one barrier,
and when it is truly shared". ALL labels in TRADITIONAL CHINESE.

Title bar: 8.2  雙位能井與電子共享 (Double Well and Electron Sharing)

Intro box (Traditional Chinese):
H₂⁺ 的電子同時受兩個質子吸引，沿兩質子連線看是兩個庫侖位能井夾著一道障壁。
量子力學上這相當於一對被障壁隔開的箱子：質子離得遠時電子只能靠穿隧往返，
離得近時障壁形同消失，電子才真正被兩個質子共享。

LEFT ~60%: two stacked potential plots. Horizontal axis: position along the line
joining the protons. Vertical axis: potential energy U_e (eV).

Upper plot, pill label 情況 A — R 大（R ≳ 0.42 nm）:
  Two red protons labelled 質子 a and 質子 b with a double arrow R between them.
  Two deep, sharp 1/r-shaped wells (blue curve #1565C0). The barrier top between the
  wells lies ABOVE a horizontal green dashed line (#2E7D32) labelled 電子能量 ≈ −13.6 eV.
  The green line is drawn only inside the left well. An orange (#EF6C00) dashed arrow
  passes THROUGH the barrier from the left well to the right well, labelled 穿隧（很罕見）.
  Small note: 障壁又寬又高 → 電子實際上只屬於一個質子（氫原子 + 裸質子）。

Lower plot, pill label 情況 B — R 小（R ~ 0.1 nm）:
  The same two wells but closer together; the barrier top between them is low,
  labelled 障壁頂 ≈ −54 eV. The green electron-energy dashed line (labelled
  電子能量 ≈ −30 eV) spans BOTH wells continuously and lies ABOVE the barrier top.
  Small note: 障壁形同消失 → 電子在兩核之間自由來去 = 共享。

RIGHT ~40%:

Card 1 pill: 量子力學的圖像（圖 8.4b）
  A grey 3-D block with two funnel-shaped depressions (the two wells); a small blue
  ball labelled 電子 sits inside one funnel; the block surface between the funnels is
  labelled 障壁. Caption: 一對被障壁隔開的箱子。

Card 2 pill: 障壁有多高？
  U_e(中點) = −2 · e²/[4πε₀(R/2)] = −4 × 1.44 eV·nm / R
  令它等於 −13.6 eV → R ≈ 0.42 nm
  bullets:
    R > 0.42 nm：障壁高於電子能量 → 只能穿隧
    R < 0.42 nm：障壁低於電子能量 → 電子自由往返

Top-right legend "圖例":
  紅色圓點 — 質子
  藍色曲線 — 電子位能 U_e
  綠色虛線 — 電子能量
  橘色虛線箭頭 — 穿隧

Bottom pastel boxes (three):
1. light blue: U_e = −e²/(4πε₀|r − r_a|) − e²/(4πε₀|r − r_b|) — 電子感受到的兩個庫侖井
2. light yellow: 穿隧機率對障壁寬度呈指數敏感 — R 越大，電子越難跑到另一邊（第五章 5.7 穿隧效應）
3. light green: R ~ 0.1 nm 時電子每秒往返約 10¹⁵ 次 — 詳見 8.3 進階探討
```
