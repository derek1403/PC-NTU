# Statistical_Distribution_Overview.png

**對應章節：** 9.1 統計分布
**插入位置：**「三種粒子、三種分布」的表格之後、「假設與已知」之前
**課本對應：** 無（自製總覽圖）

> 產圖前請先貼上 `00_STYLE_GUIDE.md` 的風格區塊。

---

## 中文提示詞

```
依共用風格畫三列資訊圖，標題：
9.1  統計分布 (Statistical Distributions)
導言：大量粒子以統計描述。平均粒子數 = 態數 × 每態平均佔據數。
f(ε) 一般不是機率；費米態只能有 0 或 1 粒子時，才等於該態被佔據的機率。

上列｜從單粒子到群體
四個卡片：氫原子（單電子模型）→ 多電子原子（近似與數值計算）
→ 分子（鍵結、轉動、振動）→ 大量粒子（統計力學）。
粒子總數只標「巨觀樣品粒子數極大」，不給跨氣體與固體通用的每立方公尺數字。

中列｜n(ε)=g(ε)f(ε)
保留教室座位圖：第三排 11 個座位，重複觀察下每座平均 0.5 人，
g=11、f=0.5、n=5.5；小字「5.5 是平均人數，不是一次觀測的半個人」。
旁邊列兩個單位框：
離散：g 為簡併數、n 為平均粒子數，均無因次。
連續：dN=g(ε)f(ε)dε；g、n 的單位為每單位能量，不是每單位體積。

下列｜交換統計與古典極限
綠卡 MB：大量空座位、稀疏粒子，標「每態平均佔據遠小於1，交換效應可忽略」；
例子「一般稀薄氣體」。不畫有名字的人來暗示同種原子可被標記。
藍卡 BE：相同粒子可佔同一態，標「整數自旋，全同玻色子」；例子光子。
紅卡 FD：每態最多一人，標「半奇數自旋，全同費米子」；例子電子。
前排填滿只代表零溫基態，不作為任意溫度的規則。
共同註：「原子、分子也可服從量子統計；內部結構不是可分辨性的判準。」
移除 P⁴₂/C⁴₂ 比喻，避免把不允許重複的組合計數誤當成玻色統計。

底部公式盒：
1. n=g f：離散能階平均粒子數。
2. dN=g f dε：連續能量區間的粒子數。
3. 0≤f_FD≤1；f_BE 可大於1；MB 為非簡併近似。
配色：綠 MB、藍 BE、紅 FD。所有文字繁體中文。
```

## English Prompt

```
Use the shared three-band layout. All visible labels Traditional Chinese.
Title: 9.1  統計分布 (Statistical Distributions).
Intro: 平均粒子數 = 態數 × 每態平均佔據數.
Explain that f is a mean occupation; only a 0/1 occupation makes it a probability.

TOP: four cards 氫原子（單電子模型）, 多電子原子（近似與數值計算）,
分子（鍵結、轉動、振動）, 大量粒子（統計力學）.
Do not prescribe a universal number density for all phases.
MIDDLE: classroom with 11 seats in a row; mean occupation 0.5 per seat,
g=11, f=0.5, n=5.5. Caption 5.5 是平均人數.
Two unit boxes: 離散 g,n 無因次; 連續 dN=g f dε，g,n 單位為每單位能量.

BOTTOM: green MB card with many empty seats and sparse particles, caption
稀薄非簡併、交換效應可忽略, example 一般稀薄氣體.
Blue BE card permits multiple identical figures per seat, 整數自旋，全同玻色子.
Red FD card permits at most one per complete state, 半奇數自旋，全同費米子.
Filling all lowest rows first only illustrates the T=0 ground state.
Shared caption 原子、分子也可服從量子統計；內部結構不是可分辨性的判準.
Remove named-particle and permutation/combination comparisons.
Bottom boxes: n=g f; dN=g f dε; 0≤f_FD≤1、f_BE 可大於1、MB 為非簡併近似.
```
