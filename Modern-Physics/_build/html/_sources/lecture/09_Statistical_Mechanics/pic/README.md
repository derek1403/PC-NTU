# 第九章圖片清單 (Chapter 9 Figure Checklist)

本目錄同時存放**圖片提示詞 `.md`** 與**產出的圖片 `.png`**。
notebook 內一律以 `![](./pic/<檔名>.png)` 引用，檔名必須與提示詞 `.md` 完全一致。

**產圖流程：**
1. 打開下表中要產的那一張圖的 `.md`。
2. 先貼 [`00_STYLE_GUIDE.md`](00_STYLE_GUIDE.md) 的風格區塊（中文版或英文版擇一）。
3. 再貼該張圖 `.md` 裡對應語言的提示詞區塊。
4. 產出的圖存成同名 `.png` 放在本目錄。
5. 回來把下表的「狀態」改成 ✅。

---

## 清單

| # | 檔名 | 節 | 在 notebook 中的位置 | 內容一句話 | 狀態 |
|---|---|---|---|---|---|
| 1 | `Statistical_Distribution_Overview` | 9.1 | 「三種粒子、三種分布」表格之後 | 從原子到 $10^{25}$ 個粒子 ＋ 教室比喻 $n=gf$ ＋ 三種入座規則 | ✅ 已生成 |
| 2 | `Momentum_Space_and_Energy_Distribution` | 9.3 | $(9.11)$ 之後 | 圖 9.1、9.2：動量空間球殼 → $g(\epsilon)\propto\sqrt{\epsilon}$ → $n(\epsilon)$ 曲線（峰值 $kT/2$、平均 $\frac32 kT$） | ✅ 已生成 |
| 3 | `Maxwell_Speed_Distribution` | 9.3 | 「三種平均速率」之後 | 圖 9.3、9.4：$v_p<\bar v<v_{\rm rms}$ ＋ O$_2$ 73 K／273 K 與 H$_2$ 273 K | ✅ 已生成 |
| 4 | `Equipartition_Degrees_of_Freedom` | 9.3 | 「振動為什麼是 $kT$」段落之後 | 單原子／雙原子／CO$_2$／H$_2$O／振子／晶格原子的自由度與平均能量 ＋ $kT/C$ 雜訊 | ✅ 已生成 |
| 5 | `Three_Quantum_Statistics_Comparison` | 9.4 | 【推導 1】高能量極限之後 | 圖 9.5：同一 $\alpha$ 的 BE／MB／FD 曲線 ＋ 兩粒子同態的重新歸一化與費米子禁制 ＋ 表 9.1 精簡版 | ✅ 已生成 |
| 6 | `Fermi_Dirac_Distribution_Temperature` | 9.4 | 「有限溫度」討論之後 | 圖 9.6：$T=0$、$0.1\,\epsilon_F/k$、$\epsilon_F/k$ 三種 $f_{FD}$ ＋ 教室填座位到第五排 | ✅ 已生成 |
| 7 | `Cavity_Standing_Waves_j_Space` | 9.5 | $(9.33)$ 之後 | 圖 9.7：空腔駐波 → $j$ 空間格點、八分之一球殼、$\times 2$ 偏振 → $G(\nu)$ | ✅ 已生成 |
| 8 | `Rayleigh_Jeans_vs_Planck` | 9.6 | $(9.39)$ 之後 | 瑞利－金斯 vs 普朗克、每模式平均能量被凍結、不同溫度的 $u(\lambda)$ 與維恩位移 | ✅ 已生成 |
| 9 | `Earth_Energy_Budget_Greenhouse` | 9.6 | 「地球的能量收支與溫室效應」小節開頭 | 圖 9.8：30/51/19 與 6/45/64 的能量收支 ＋ 為何高山較冷 ＋ CO$_2$ 振盪偶極 | ✅ 已生成 |
| 10 | `Einstein_Coefficients_Three_Transitions` | 9.7 | 「假設與已知」之後 | 圖 9.9：受激吸收／自發放射／受激放射 ＋ 平衡結果 ＋ 居量反轉與雷射 | ✅ 已生成 |
| 11 | `Specific_Heat_Dulong_Petit_vs_Einstein` | 9.8 | 「實驗怎麼說」小節 | 圖 9.10：Pb、Al、Si、C 的 $c_V(T)$ ＋ 愛因斯坦普適曲線 $c_V/3R$ vs $T/\theta_E$ | ✅ 已生成 |
| 12 | `Free_Electron_Density_of_States` | 9.9 | $(9.55)$ 之後 | $g(\epsilon)\propto\sqrt{\epsilon}$ 填到 $\epsilon_F$、$N\uparrow\Rightarrow\epsilon_F\uparrow$ ＋ 表 9.2 長條圖 ＋ 銅的例題 | ✅ 已生成 |
| 13 | `Electron_Energy_Distribution_in_Metal` | 9.10 | $(9.58)$ 之後 | 0／300／1200 K 的 $n(\epsilon)$ ＋ 平均 $\frac35\epsilon_F$ ＋ 只有 $\epsilon_F$ 附近的電子被熱激發 | ✅ 已生成 |

---

## 檢查重點（產完圖後請逐張確認）

- [ ] 圖中所有中文皆為**繁體**，沒有簡體字、沒有亂碼、沒有錯字。
- [ ] 數學符號正確：$\epsilon$ 是能量、$\epsilon_F$ 有下標 F、$\nu$（頻率）不要畫成 $v$（速率）、$k$ 是小寫波茲曼常數。
- [ ] 公式排版為印刷品質（分數有橫線、根號罩住整個被開方式、指數裡的 $kT$ 沒有掉出來）。
- [ ] 本章顏色約定一致：MB 綠、BE 藍、FD 紅、古典預測橘色虛線、實驗數據深灰。
- [ ] 背景為純白，無浮水印、無簽名、無 Logo。
- [ ] 檔名與本表完全一致（大小寫、底線都要對）。

## 需要特別留意的物理正確性

| 圖 | 最容易畫錯的地方 |
|---|---|
| 2 | $n(\epsilon)$ 在 $\epsilon=0$ 為零且起始斜率無限大（$\sqrt{\epsilon}$）；峰值在 $\frac12 kT$，平均值 $\frac32 kT$ 在峰值**右邊**很遠 |
| 3 | 三條虛線順序必須是 $v_p<\bar v<v_{\rm rms}$（比例 $1:1.128:1.225$）；三條分布曲線**面積相同**，所以愈窄的愈高 |
| 4 | 剛體 CO$_2$ 是線性分子：$3$ 平移 $+2$ 轉動 $=\frac52 kT$，**不是** $\frac72 kT$；振子是 $kT$ 不是 $\frac12 kT$ |
| 5 | 三條曲線在 $\epsilon=0$：BE $\approx 9$（超出圖框）、MB $=0.90$、FD $\approx 0.47$；FD **永遠**低於 $1$；高能量處三者合一 |
| 6 | 上排固定化學勢 μ₀，有限溫曲線通過 (μ₀,0.5)；T=0 畫階躍開端點。固定粒子數的 μ(T) 另由粒子數條件求解，不宣稱都通過同一費米能。 |
| 7 | 只畫**第一卦限**（$j_x,j_y,j_z\ge0$）的格點；格點間距均勻；係數是 $\frac18\times2$ |
| 8 | 瑞利－金斯 $\propto\nu^2$ 在低頻與普朗克**重合**、高頻發散；$u(\lambda)$ 峰值隨溫度升高往短波長**且**變高 |
| 9 | 百分比必須守恆：$30+51+19=100$、$6+45=51$、$19+45=64$、$30+6+64=100$ |
| 10 | 受激放射的兩顆光子**同方向、同相位**；自發放射的光子方向任意；吸收**沒有**「自發」版本 |
| 11 | 所有元素高溫都趨近 $3R\approx5.97$ 的水平線；鑽石最慢（300 K 只有約 $1.4$）、鉛最快 |
| 12 | $g(\epsilon)$ 是**橫躺的拋物線**形狀（$\propto\sqrt{\epsilon}$），不是直線；鋁與鋅的長條明顯高於一價金屬 |
| 13 | 300 K、1200 K 的曲線與 0 K **幾乎重疊**，只在 $\epsilon_F$ 附近極窄的範圍內磨圓；虛線延伸的是 $g(\epsilon)$ 而不是電子 |

