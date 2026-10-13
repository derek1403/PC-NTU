# Q08｜大氣科學：一維變分資料同化 (1D-Var)

> 應用題 ★★★☆☆

## Question

在數值天氣預報的一維變分同化（1D-Var）系統中，假設某垂直氣柱頂底的總重力位厚度已知，上下兩層的真實大氣溫度 $(T_1, T_2)$ 必須嚴格滿足由靜力厚度方程（依對數氣壓厚度加權）所推導出的強限制條件（Strong Constraint）：

$$T_1 + 2T_2 = 840\ \text{K}$$

今由無線電探空儀（Radiosonde）與衛星紅外線頻道分別測得觀測值 $T_1^o = 285\ \text{K}$（觀測誤差變異數 $\sigma_1^2 = 1\ \text{K}^2$）以及 $T_2^o = 269\ \text{K}$（觀測誤差變異數 $\sigma_2^2 = 4\ \text{K}^2$）。
為了找出最符合觀測且滿足物理守恆的分析場，需最小化加權誤差平方和（Cost Function）：

$$J(T_1, T_2) = \frac{(T_1 - 285)^2}{1} + \frac{(T_2 - 269)^2}{4}$$

請利用拉格朗日乘數法，手算出同化後的最佳分析溫度 $(T_1, T_2)$。

## Question - Answer

### 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】[單約束 Lagrange 條件 (Lagrange Condition)](../01_basic_use.md)：** 約束上的極值點，必使 Lagrangian 對所有變數的偏導數同時為零。

  $$\mathcal{L} = J - \lambda(g - c)$$

* **【定義 1】代價函數與約束 (Cost Function & Constraint)：** $J$ 量度分析場偏離觀測的程度，誤差越大的觀測權重越小；約束是分析場必須遵守的物理關係。

  (a) $$J(T_1,T_2) \overset{\text{def}}{=} \frac{(T_1 - T_1^o)^2}{\sigma_1^2} + \frac{(T_2 - T_2^o)^2}{\sigma_2^2}$$

  (b) $$g(T_1,T_2) \overset{\text{def}}{=} T_1 + 2T_2 = 840\ \text{K}$$

  * $T_1, T_2$ : 下層、上層分析溫度 (Analysis temperature) $[\text{K}]$
  * $T_1^o, T_2^o$ : 觀測溫度 (Observed temperature) $[\text{K}]$，$285\ \text{K}$、$269\ \text{K}$
  * $\sigma_1^2, \sigma_2^2$ : 觀測誤差變異數 (Observation error variance) $[\text{K}^2]$，$1\ \text{K}^2$、$4\ \text{K}^2$
  * $J$ : 代價函數 (Cost function) $[\text{無單位}]$
  * $\lambda$ : 乘數 (Lagrange multiplier) $[\text{K}^{-1}]$

### solve

(a) 由【已知 1】【定義 1】寫出方程組：

$$\left\{\begin{array}{rcl}
2(T_1 - 285) &=& \lambda \\[4pt]
\dfrac{T_2 - 269}{2} &=& 2\lambda \\[8pt]
T_1 + 2T_2 &=& 840
\end{array}\right.$$

(b) 前兩式把分析值寫成「觀測值 + 修正量」：

$$\begin{gather*}
T_1 &\overset{\text{(a)}}{=}& 285 + \frac{\lambda}{2} \\
T_2 &\overset{\text{(a)}}{=}& 269 + 4\lambda
\end{gather*}$$

(c) 代入約束解 $\lambda$：

$$\begin{gather*}
840 &\overset{\text{(a),(b)}}{=}& 285 + \frac{\lambda}{2} + 2(269 + 4\lambda) \\
840 &=& 823 + \frac{17}{2}\lambda \\
\lambda &=& 2\ \text{K}^{-1}
\end{gather*}$$

(d) 代回：

$$\begin{gather*}
T_1 &\overset{\text{(b),(c)}}{=}& 286\ \text{K} \\
T_2 &\overset{\text{(b),(c)}}{=}& 277\ \text{K} \\
J &\overset{\text{定義 1(a)}}{=}& \frac{1^2}{1} + \frac{8^2}{4} \\
J &=& 17
\end{gather*}$$

(e) 判定：$J$ 是正定二次式（碗形），限制在直線上仍是碗形，唯一的候選點就是全域最小值。

**結論**：分析場 $(T_1, T_2) = (286\ \text{K},\ 277\ \text{K})$。觀測本身違反約束 $285 + 2\cdot 269 = 823 \neq 840$，缺口 $17\ \text{K}$ 由兩層分攤：誤差大（$\sigma_2^2 = 4\ \text{K}^2$）的上層被修正 $8\ \text{K}$，誤差小的下層只修正 $1\ \text{K}$。**越不可信的觀測，被拉得越多**，這正是變分同化的核心精神。
