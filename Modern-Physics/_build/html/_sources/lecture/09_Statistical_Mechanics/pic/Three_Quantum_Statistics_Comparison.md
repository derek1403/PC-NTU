# Three_Quantum_Statistics_Comparison.png

**對應章節：** 9.4 量子統計學
**插入位置：**【推導 1】高能量時三者趨於一致之後、「進階探討：分母的 ±1 從哪裡來？」之前
**課本對應：** 圖 9.5、表 9.1

> 產圖前請先貼上 `00_STYLE_GUIDE.md` 的風格區塊。

---

## 中文提示詞

```
請依共用風格畫教學資訊圖，保留左右雙欄、藍綠紅配色與底部公式盒。
標題：9.4  三種統計分布的比較 (Comparing the Three Distributions)
導言：本圖固定相同溫度 T 與化學勢 μ，令 α = −μ/(kT)。f 是每態平均佔據數，不是一般的機率。
在此比較條件下 f_BE > f_MB > f_FD；若固定相同總粒子數，須分別重求化學勢。

左欄（60%）｜同一 T、同一 α 的分布
橫軸 ε/kT：0 到 5；縱軸「每態平均佔據數 f」：0 到 1.2。
取 e^α = 1.11；依下列公式繪圖，不任意手畫：
藍色 f_BE = 1/(1.11e^(ε/kT)−1)，綠色 f_MB = 1/(1.11e^(ε/kT))，
紅色 f_FD = 1/(1.11e^(ε/kT)+1)。
ε=0 時三者約為 9.09、0.901、0.474；藍線超出圖框，用箭頭標「9.09，超出刻度」。
ε=kT 時約為 0.496、0.331、0.249；高能區三線接近。
f=1 畫細虛線，標「費米子佔據上限」。
圖旁註：「這是固定 μ 的函數比較，不是三種固定 N 樣品的直接比較。」

右上欄｜同態時須重新歸一化
先註明單粒子態 ψ_a 已歸一化。
綠卡：可分辨粒子的指定乘積態 ψ_M=ψ_a(1)ψ_a(2)，總機率為 1。
藍卡：ψ_B=C[ψ_a(1)ψ_a(2)+ψ_a(2)ψ_a(1)]；
由 4|C|²=1，取 C=1/2，得到 ψ_B=ψ_a(1)ψ_a(2)，總機率為 1。
紅卡：反對稱組合 ψ_a(1)ψ_a(2)−ψ_a(2)ψ_a(1)=0，無法歸一化，標「同態禁止」。
不要畫 1:2:0 的機率長條；不要把 a≠b 時的 1/√2 直接用於 a=b。
結論：「允許同態 ≠ 同態機率一律加倍；熱平衡居量須由統計分布求得。」

右下欄｜適用條件
三欄表：
MB：稀薄非簡併極限，交換效應可忽略；一般稀薄氣體。
BE：全同玻色子，整數自旋；每態可有多個粒子。
FD：全同費米子，半奇數自旋；每個完整單粒子態最多一個。
不要把 MB 說成第三種基本粒子，也不要以是否有內部結構判斷可分辨性。

底部三個公式盒：
綠 f_MB=1/(e^α e^(ε/kT))；藍 f_BE=1/(e^α e^(ε/kT)−1)；
紅 f_FD=1/(e^α e^(ε/kT)+1)。
圖例沿用藍 BE、綠 MB、紅 FD；所有顯示文字使用繁體中文。
```

## English Prompt

```
Use the shared style, the original two-column layout, blue BE / green MB / red FD,
and three pastel formula boxes. ALL visible labels must be Traditional Chinese.
Title: 9.4  三種統計分布的比較 (Comparing the Three Distributions).
Intro label: 固定相同 T 與 μ；α=−μ/(kT)；f 為每態平均佔據數.

LEFT 60%: plot x=ε/kT from 0 to 5 and y=f from 0 to 1.2.
Use e^α=1.11 and evaluate the formulas, rather than inventing curves:
blue 1/(1.11exp(x)−1), green 1/(1.11exp(x)), red 1/(1.11exp(x)+1).
At x=0 values are 9.09, 0.901, 0.474; mark blue as off-scale.
At x=1 values are 0.496, 0.331, 0.249. Show convergence at high energy.
At f=1 add 費米子佔據上限. Caption: 固定 N 時，各統計須分別求 μ.

UPPER RIGHT, label 同態時須重新歸一化:
Assume normalized ψ_a. Green card ψ_M=ψ_a(1)ψ_a(2), 總機率 1.
Blue card ψ_B=C[ψ_a(1)ψ_a(2)+ψ_a(2)ψ_a(1)];
4|C|²=1 ⇒ C=1/2 ⇒ ψ_B=ψ_a(1)ψ_a(2), 總機率 1.
Red card antisymmetric combination =0, 無法歸一化：同態禁止.
Do NOT draw 1:2:0 probability bars or use 1/√2 for equal orbitals.
Caption: 允許同態 ≠ 同態機率一律加倍.

LOWER RIGHT table: MB 稀薄非簡併、交換效應可忽略; BE 全同玻色子、整數自旋、
每態不限; FD 全同費米子、半奇數自旋、每態最多一個.
MB is a regime, not a third fundamental particle species.
Bottom boxes show the three full f_MB, f_BE, f_FD formulas with denominator
e^α e^(ε/kT), e^α e^(ε/kT)−1, e^α e^(ε/kT)+1 respectively.
```
