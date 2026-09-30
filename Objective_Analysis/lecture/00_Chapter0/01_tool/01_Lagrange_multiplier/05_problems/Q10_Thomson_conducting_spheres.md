# Q10｜電磁學：孤立導體球的靜電能最小化 (Thomson's Theorem)

> 應用題 ★★★☆☆

## Question

三個半徑分別為 $R_1 = 1\ \text{m}$、$R_2 = 2\ \text{m}$、$R_3 = 3\ \text{m}$ 的金屬導體球彼此相距極遠（互容可忽略），並以極細的理想導線互相連接。
今將總電量 $Q = 12\ \mu\text{C}$ 注入此系統，設三球最終分配到的電荷量為 $q_1, q_2, q_3$。
根據湯姆森定理，自由電荷在導體系統中會自動調整分布，使系統總靜電位能達到極小值：

$$U(q_1, q_2, q_3) = \frac{1}{8\pi\varepsilon_0} \left( \frac{q_1^2}{R_1} + \frac{q_2^2}{R_2} + \frac{q_3^2}{R_3} \right)$$

請在電荷守恆條件 $q_1 + q_2 + q_3 = 12\ \mu\text{C}$ 下求 $(q_1, q_2, q_3)$，並說明拉格朗日乘數 $\lambda$ 在此系統中代表的物理意義。

## Question - Answer

### 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】[單約束 Lagrange 條件 (Lagrange Condition)](../01_basic_use.md)：** 約束上的極值點，必使 Lagrangian 對所有變數的偏導數同時為零。

  $$\mathcal{L} = U - \lambda\Big(\sum_i q_i - Q\Big)$$

* **【已知 2】孤立導體球的電位 (Potential of an Isolated Sphere)：** 帶電 $q$ 的孤立導體球，表面電位與電荷成正比、與半徑成反比。

  $$V = \frac{q}{4\pi\varepsilon_0 R}$$

  * $\varepsilon_0$ : 真空電容率 (Vacuum permittivity) $[\text{F}\cdot\text{m}^{-1}]$，$\frac{1}{4\pi\varepsilon_0} \approx 8.99 \times 10^{9}\ \text{m}\cdot\text{F}^{-1}$

* **【定義 1】目標與約束 (Objective & Constraint)：**

  (a) $$U \overset{\text{def}}{=} \frac{1}{8\pi\varepsilon_0} \sum_{i=1}^{3} \frac{q_i^2}{R_i}$$

  (b) $$g \overset{\text{def}}{=} q_1 + q_2 + q_3 = Q$$

  * $q_i$ : 第 $i$ 球電荷 (Charge) $[\text{C}]$
  * $R_i$ : 第 $i$ 球半徑 (Radius) $[\text{m}]$
  * $Q$ : 總電荷 (Total charge) $[\text{C}]$，$Q = 12\ \mu\text{C}$
  * $U$ : 靜電位能 (Electrostatic energy) $[\text{J}]$
  * $\lambda$ : 乘數 (Lagrange multiplier) $[\text{V}]$

### solve

(a) 由【已知 1】【定義 1】，對每個 $q_i$ 偏微分：

$$\begin{gather*}
0 &\overset{\text{已知 1}}{=}& \frac{\partial \mathcal{L}}{\partial q_i} \\
0 &\overset{\text{定義 1}}{=}& \frac{q_i}{4\pi\varepsilon_0 R_i} - \lambda \\
q_i &=& 4\pi\varepsilon_0 R_i\,\lambda
\end{gather*}$$

(b) 代入電荷守恆：

$$\begin{gather*}
Q &\overset{\text{定義 1(b),(a)}}{=}& 4\pi\varepsilon_0 \lambda\,(R_1 + R_2 + R_3) \\
\lambda &=& \frac{Q}{4\pi\varepsilon_0 (R_1 + R_2 + R_3)}
\end{gather*}$$

(c) 電荷分配（依半徑比例）：

$$\begin{gather*}
q_i &\overset{\text{(a),(b)}}{=}& Q\,\frac{R_i}{R_1 + R_2 + R_3} \\
q_i &=& 12\ \mu\text{C} \cdot \frac{R_i}{6\ \text{m}}
\end{gather*}$$

所以 $(q_1, q_2, q_3) = (2,\ 4,\ 6)\ \mu\text{C}$。

(d) 乘數的數值：

$$\begin{gather*}
\lambda &\overset{\text{(b)}}{=}& (8.99 \times 10^{9}\ \text{m}\cdot\text{F}^{-1}) \cdot \frac{12 \times 10^{-6}\ \text{C}}{6\ \text{m}} \\
&\approx& 1.8 \times 10^{4}\ \text{V}
\end{gather*}$$

(e) 判定：$U$ 是正定二次式，限制在平面上仍是碗形，唯一候選點就是全域最小值。

(f) 乘數的意義：

$$\begin{gather*}
\lambda &\overset{\text{(a)}}{=}& \frac{q_i}{4\pi\varepsilon_0 R_i} \\
&\overset{\text{已知 2}}{=}& V_i
\end{gather*}$$

**結論**：$(q_1, q_2, q_3) = (2, 4, 6)\ \mu\text{C}$，電荷與半徑成正比。$\lambda$ 就是三球**共同的電位** $V \approx 1.8 \times 10^{4}\ \text{V}$：導線連起來的導體必為等電位。另一個角度，$\lambda = \partial U_{\min}/\partial Q$，是「再多塞一點電荷要付出的能量」。
