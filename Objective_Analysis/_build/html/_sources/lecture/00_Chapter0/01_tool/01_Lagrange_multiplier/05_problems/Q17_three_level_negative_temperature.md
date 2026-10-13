# Q17｜應用壓軸：三能階雷射的最大熵分布與負絕對溫度

> 應用題 ★★★★★

## Question

考慮固態雷射晶體中的三能階量子系統，其三個能階的能量分別為 $E_1 = 0$、$E_2 = \varepsilon$、$E_3 = 2\varepsilon$（其中 $\varepsilon > 0$），粒子處於各能階的機率分別為 $p_1, p_2, p_3 > 0$。
根據統計力學的最大熵原理（Maximum Entropy Principle），熱平衡或準平衡態會最大化吉布斯熵函數：

$$S(p_1, p_2, p_3) = -k_B \left( p_1 \ln p_1 + p_2 \ln p_2 + p_3 \ln p_3 \right)$$

今以光學幫浦（Optical Pumping）將能量注入晶體，使系統同時受到兩個守恆條件限制：

* 總機率正規化：$p_1 + p_2 + p_3 = 1$
* 高能態平均能量限制：$0\cdot p_1 + \varepsilon p_2 + 2\varepsilon p_3 = \frac{10}{7}\varepsilon$

請完成以下推導：

1. 引入拉格朗日乘數，證明各能階機率滿足等比數列關係 $p_2 = p_1 r$、$p_3 = p_1 r^2$（其中 $r = e^{-\beta\varepsilon}$，$\beta$ 為對應能量限制的乘數）。
2. 將限制條件代入並化簡為關於 $r$ 的一元二次方程式，手算出機率分布 $(p_1, p_2, p_3)$。
3. 根據統計熱力學定義 $\beta = \frac{1}{k_B T}$，求出此系統的絕對溫度 $T$，並解釋為何會出現「負絕對溫度（$T < 0$）」與「居量反轉（Population Inversion, $p_3 > p_2 > p_1$）」。

## Question - Answer

### 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】[多約束 Lagrange 條件 (Lagrange Condition)](../02_advanced_use.md)：** 每條約束配一個乘數，極值點必使 Lagrangian 對所有變數的偏導數同時為零。

  $$\frac{\partial \mathcal{L}}{\partial p_i} = 0,\qquad i = 1,2,3$$

* **【已知 2】統計溫度 (Statistical Temperature)：** 波茲曼分布中能量的「權重係數」就是倒溫度；它的正負號決定機率隨能量遞減或遞增。

  $$\beta = \frac{1}{k_B T}$$

  * $T$ : 絕對溫度 (Absolute temperature) $[\text{K}]$

* **【定義 1】目標與約束 (Objective & Constraints)：**

  (a) $$S \overset{\text{def}}{=} -k_B \sum_{i=1}^{3} p_i \ln p_i$$

  (b) $$g_1 \overset{\text{def}}{=} p_1 + p_2 + p_3 = 1$$

  (c) $$g_2 \overset{\text{def}}{=} \sum_{i=1}^{3} E_i\, p_i = \frac{10}{7}\varepsilon$$

  * $p_i$ : 第 $i$ 能階佔據機率 (Occupation probability) $[\text{無單位}]$
  * $E_i$ : 能階能量 (Energy level) $[\text{J}]$，$E_i = (i-1)\varepsilon$
  * $k_B$ : 波茲曼常數 (Boltzmann constant) $[\text{J}\cdot\text{K}^{-1}]$，$k_B \approx 1.38 \times 10^{-23}\ \text{J}\cdot\text{K}^{-1}$
  * $S$ : 吉布斯熵 (Gibbs entropy) $[\text{J}\cdot\text{K}^{-1}]$

* **【定義 2】乘數的寫法 (Scaled Multipliers)：** 把兩個乘數寫成 $k_B\alpha$、$k_B\beta$，讓 $\beta$ 的單位是 $\text{J}^{-1}$，直接對上 $\beta = 1/(k_B T)$。

  (a) $$\mathcal{L} \overset{\text{def}}{=} S - k_B\alpha\,(g_1 - 1) - k_B\beta\Big(g_2 - \frac{10}{7}\varepsilon\Big)$$

  (b) $$r \overset{\text{def}}{=} e^{-\beta\varepsilon}$$

  * $\alpha$ : 正規化乘數 (Normalization multiplier) $[\text{無單位}]$
  * $\beta$ : 能量乘數 (Energy multiplier) $[\text{J}^{-1}]$

### solve

#### 1. 等比數列

(a) 對 $p_i$ 偏微分：

$$\begin{gather*}
0 &\overset{\text{已知 1}}{=}& \frac{\partial \mathcal{L}}{\partial p_i} \\
0 &\overset{\text{定義 1,2(a)}}{=}& -k_B(\ln p_i + 1) - k_B\alpha - k_B\beta E_i \\
\ln p_i &=& -1 - \alpha - \beta E_i \\
p_i &=& e^{-1-\alpha}\, e^{-\beta E_i}
\end{gather*}$$

(b) 代入 $E_i = (i-1)\varepsilon$：

$$\begin{gather*}
p_2 &\overset{\text{(a)}}{=}& p_1\, e^{-\beta\varepsilon} \\
p_2 &\overset{\text{定義 2(b)}}{=}& p_1\, r \\
p_3 &\overset{\text{(a),定義 2(b)}}{=}& p_1\, r^2
\end{gather*}$$

#### 2. 機率分布

(c) 能量約束：把 $E_i$ 展開，再用 (b) 把 $p_2, p_3$ 換成 $p_1$ 與 $r$，最後兩邊約掉 $\varepsilon$。

$$\begin{gather*}
\frac{10}{7}\varepsilon &\overset{\text{定義 1(c)}}{=}& E_1 p_1 + E_2 p_2 + E_3 p_3 \\
\frac{10}{7}\varepsilon &\overset{\text{定義 1}}{=}& 0 \cdot p_1 + \varepsilon\, p_2 + 2\varepsilon\, p_3 \\
\frac{10}{7}\varepsilon &\overset{\text{(b)}}{=}& \varepsilon\, p_1 r + 2\varepsilon\, p_1 r^2 \\
\frac{10}{7} &=& p_1\,(r + 2r^2)
\end{gather*}$$

(d) 正規化約束：同樣把 $p_2, p_3$ 換成 $p_1$ 與 $r$。

$$\begin{gather*}
1 &\overset{\text{定義 1(b)}}{=}& p_1 + p_2 + p_3 \\
1 &\overset{\text{(b)}}{=}& p_1 + p_1 r + p_1 r^2 \\
1 &=& p_1\,(1 + r + r^2)
\end{gather*}$$

(e) (c) 除以 (d)，$p_1$ 消掉，只剩 $r$：

$$\begin{gather*}
\frac{10}{7} &\overset{\text{(c),(d)}}{=}& \frac{r + 2r^2}{1 + r + r^2} \\
10\,(1 + r + r^2) &=& 7\,(r + 2r^2) \\
10 + 10r + 10r^2 &=& 7r + 14r^2 \\
0 &=& 4r^2 - 3r - 10 \\
0 &=& (4r + 5)(r - 2) \\
r &=& 2
\end{gather*}$$

（$r = e^{-\beta\varepsilon} > 0$，捨去 $-\frac{5}{4}$。）

(f) 代回 (d) 求 $p_1$：

$$\begin{gather*}
1 &\overset{\text{(d),(e)}}{=}& p_1\,(1 + 2 + 4) \\
p_1 &=& \frac{1}{7}
\end{gather*}$$

所以 $(p_1, p_2, p_3) = \left(\frac{1}{7},\ \frac{2}{7},\ \frac{4}{7}\right)$。

#### 3. 負溫度

(g) 由 $r$ 求 $\beta$ 與 $T$：

$$\begin{gather*}
e^{-\beta\varepsilon} &\overset{\text{定義 2(b),(e)}}{=}& 2 \\
\beta &=& -\frac{\ln 2}{\varepsilon} \\
T &\overset{\text{已知 2}}{=}& \frac{1}{k_B\beta} \\
T &=& -\frac{\varepsilon}{k_B \ln 2}
\end{gather*}$$

(h) 判定：$-p\ln p$ 是凹函數，約束都是線性的，所以唯一候選點是熵的全域最大值。

**結論**：

1. $p_i \propto e^{-\beta E_i}$，即波茲曼分布，相鄰能階比值固定為 $r$。
2. $(p_1, p_2, p_3) = \left(\frac{1}{7}, \frac{2}{7}, \frac{4}{7}\right)$。
3. $T = -\dfrac{\varepsilon}{k_B \ln 2} < 0$。

為什麼是負的：溫度 $T > 0$ 時 $r < 1$，機率隨能量遞減，平均能量必小於 $\varepsilon$；$T \to \pm\infty$ 時三能階均分，平均能量恰為 $\varepsilon$。幫浦把平均能量推到 $\frac{10}{7}\varepsilon > \varepsilon$，只能靠 $r > 1$（高能階比低能階更擠），也就是 $\beta < 0$、$T < 0$。這就是**居量反轉** $p_3 > p_2 > p_1$，也是雷射能產生受激輻射放大的前提。負溫度並不比 $0\ \text{K}$ 冷，反而比任何正溫度都「熱」：與正溫度系統接觸時，能量會從它流出去。
