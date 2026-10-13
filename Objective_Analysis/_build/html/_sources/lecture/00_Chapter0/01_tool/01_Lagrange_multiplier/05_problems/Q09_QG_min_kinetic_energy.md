# Q09｜大氣動力：熱力風平衡下的最小動能配置

> 應用題 ★★★☆☆

## Question

考慮一個三層準地轉（Quasi-Geostrophic）大氣氣柱模型，下層、中層、上層的質量相等，其緯向風速分別為 $u_1, u_2, u_3$（單位：$\text{m/s}$）。單位面積氣柱的總動能正比於：

$$K(u_1, u_2, u_3) = \frac{1}{2}(u_1^2 + u_2^2 + u_3^2)$$

假設大氣在演化過程中必須同時滿足兩個物理限制：

* 總角動量守恆(總緯向動量守恆)：$u_1 + u_2 + u_3 = 30$
* 熱力風平衡（Thermal Wind Balance）：南北向水平溫度梯度要求高低層垂直風切固定為 $u_3 - u_1 = 12$

求使氣柱總動能 $K$ 達到最小值的平衡風場剖面 $(u_1, u_2, u_3)$。

## Question - Answer

### 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】[多約束 Lagrange 條件 (Lagrange Condition)](../02_advanced_use.md)：** 每條約束配一個乘數，極值點必使 Lagrangian 對所有變數的偏導數同時為零。

  $$\mathcal{L} = K - \lambda_1(g_1 - c_1) - \lambda_2(g_2 - c_2)$$

* **【定義 1】目標與約束 (Objective & Constraints)：**

  (a) $$K(u_1,u_2,u_3) \overset{\text{def}}{=} \frac{1}{2}(u_1^2 + u_2^2 + u_3^2)$$

  (b) $$g_1 \overset{\text{def}}{=} u_1 + u_2 + u_3 = 30\ \text{m}\cdot\text{s}^{-1}$$

  (c) $$g_2 \overset{\text{def}}{=} u_3 - u_1 = 12\ \text{m}\cdot\text{s}^{-1}$$

  * $u_1, u_2, u_3$ : 下、中、上層緯向風 (Zonal wind) $[\text{m}\cdot\text{s}^{-1}]$
  * $K$ : 單位質量動能（比例值）(Kinetic energy) $[\text{m}^2\cdot\text{s}^{-2}]$

* **【假設 1】LICQ：** 兩個約束梯度 $(1,1,1)$ 與 $(-1,0,1)$ 不平行。

### solve

(a) 由【已知 1】【定義 1】寫出方程組：

$$\left\{\begin{array}{rcl}
u_1 &=& \lambda_1 - \lambda_2 \\[4pt]
u_2 &=& \lambda_1 \\[4pt]
u_3 &=& \lambda_1 + \lambda_2 \\[4pt]
u_1 + u_2 + u_3 &=& 30 \\[4pt]
u_3 - u_1 &=& 12
\end{array}\right.$$

(b) 前三式說中層風是上下層的平均：

$$\begin{gather*}
u_1 + u_3 &\overset{\text{(a)}}{=}& 2\lambda_1 \\
u_1 + u_3 &\overset{\text{(a)}}{=}& 2u_2
\end{gather*}$$

(c) 代入約束：

$$\begin{gather*}
30 &\overset{\text{(a),(b)}}{=}& 3u_2 \\
u_2 &=& 10\ \text{m}\cdot\text{s}^{-1} \\
u_1 + u_3 &\overset{\text{(b)}}{=}& 20\ \text{m}\cdot\text{s}^{-1} \\
u_3 &\overset{\text{(a)}}{=}& 16\ \text{m}\cdot\text{s}^{-1} \\
u_1 &=& 4\ \text{m}\cdot\text{s}^{-1}
\end{gather*}$$

(d) 動能：

$$\begin{gather*}
K &\overset{\text{定義 1(a)}}{=}& \frac{1}{2}(4^2 + 10^2 + 16^2) \\
&=& 186\ \text{m}^2\cdot\text{s}^{-2}
\end{gather*}$$

(e) 判定：$K$ 是正定二次式，可行域是一條直線，唯一候選點就是全域最小值（沒有最大值）。

**結論**：$(u_1, u_2, u_3) = (4,\ 10,\ 16)\ \text{m}\cdot\text{s}^{-1}$。最省動能的剖面是**等風切**（每層增加 $6\ \text{m}\cdot\text{s}^{-1}$），也就是直線型剖面：總風切由熱力風決定之後，任何彎曲都只會多花動能。

### 物理：正壓／斜壓模態分解 (Barotropic–Baroclinic Decomposition)

三層剖面可拆成三個互相正交的垂直正規模態 (Vertical Normal Modes)：

$$\mathbf{u} = a_0\,\mathbf{e}_0 + a_1\,\mathbf{e}_1 + a_2\,\mathbf{e}_2,\qquad \mathbf{e}_0 = (1,1,1),\ \ \mathbf{e}_1 = (-1,0,1),\ \ \mathbf{e}_2 = (1,-2,1)$$

* $\mathbf{e}_0$ 正壓模態 (Barotropic)：垂直平均風，$a_0 = \frac{u_1+u_2+u_3}{3}$，被角動量約束鎖在 $10\ \text{m}\cdot\text{s}^{-1}$
* $\mathbf{e}_1$ 第一斜壓模態 (1st baroclinic)：線性風切，$a_1 = \frac{u_3-u_1}{2}$，被熱力風約束鎖在 $6\ \text{m}\cdot\text{s}^{-1}$
* $\mathbf{e}_2$ 第二斜壓模態 (2nd baroclinic)：剖面曲率，$a_2 = \frac{u_1-2u_2+u_3}{6}$，**沒有**被約束

模態正交，所以動能沒有交叉項，直接分成三塊：

$$\begin{gather*}
K &=& \frac{1}{2}\left(3a_0^2 + 2a_1^2 + 6a_2^2\right) \\
&=& \frac{1}{2}\left(3 \cdot 10^2 + 2 \cdot 6^2\right) + 3a_2^2 \\
&=& 186\ \text{m}^2\cdot\text{s}^{-2} + 3a_2^2
\end{gather*}$$

兩條約束鎖死了 $K_0$、$K_1$，「$K$ 最小」就等於「$a_2 = 0$」：消去第二斜壓模態，中層風落在上下層平均 $u_2 = \frac{u_1+u_3}{2}$，與 (b) 的結果一致。Lagrange 乘數法做的事，其實就是把沒被約束的模態歸零。
