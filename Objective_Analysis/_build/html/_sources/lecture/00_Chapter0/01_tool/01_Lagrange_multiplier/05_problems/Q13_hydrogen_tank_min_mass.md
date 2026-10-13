# Q13｜結構工程：異質材料儲氫槽的輕量化設計

> 應用題 ★★★☆☆

## Question

航太工程師欲設計一個圓柱形高壓液態氫燃料槽（半徑為 $r$、圓柱段長度為 $L$），其內部容積固定為

$$V = \pi r^2 L = 48\pi\ \text{m}^3$$

為了承受端面應力集中，上下兩個圓形端蓋必須採用高密度鈦合金鍛造，其單位面積質量為 $3\rho_0$；圓柱側壁則採用碳纖維複合材料纏繞，單位面積質量僅為 $\rho_0$。因此儲氫槽的總結構質量為：

$$M(r, L) = \rho_0 (2\pi r L) + 3\rho_0 (2\pi r^2) = 2\pi\rho_0 (rL + 3r^2)$$

請利用拉格朗日乘數法，求出使燃料槽總質量 $M$ 最小的尺寸 $(r, L)$ 與最佳長徑比 $\frac{L}{2r}$。

## Question - Answer

### 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】[單約束 Lagrange 條件 (Lagrange Condition)](../01_basic_use.md)：** 約束上的極值點，必使 Lagrangian 對所有變數的偏導數同時為零。

  $$\mathcal{L} = M - \lambda(V - V_0)$$

* **【定義 1】目標與約束 (Objective & Constraint)：** 側壁便宜、端蓋貴三倍，所以最佳形狀會往「細長」偏。

  (a) $$M(r,L) \overset{\text{def}}{=} 2\pi\rho_0 (rL + 3r^2)$$

  (b) $$V(r,L) \overset{\text{def}}{=} \pi r^2 L = 48\pi\ \text{m}^3$$

  * $r$ : 半徑 (Radius) $[\text{m}]$
  * $L$ : 圓柱段長度 (Length) $[\text{m}]$
  * $\rho_0$ : 側壁面密度 (Areal density) $[\text{kg}\cdot\text{m}^{-2}]$
  * $M$ : 結構質量 (Structural mass) $[\text{kg}]$
  * $\lambda$ : 乘數 (Lagrange multiplier) $[\text{kg}\cdot\text{m}^{-3}]$

### solve

(a) 由【已知 1】【定義 1】寫出方程組：

$$\left\{\begin{array}{rcl}
2\pi\rho_0 (L + 6r) &=& 2\pi\lambda\, rL \\[4pt]
2\pi\rho_0\, r &=& \pi\lambda\, r^2 \\[4pt]
\pi r^2 L &=& 48\pi
\end{array}\right.$$

(b) 第二式解出 $\lambda$（$r > 0$）：

$$\begin{gather*}
\lambda &\overset{\text{(a)}}{=}& \frac{2\rho_0}{r}
\end{gather*}$$

(c) 代入第一式：

$$\begin{gather*}
2\pi\rho_0 (L + 6r) &\overset{\text{(a),(b)}}{=}& 2\pi\cdot\frac{2\rho_0}{r}\cdot rL \\
L + 6r &=& 2L \\
L &=& 6r
\end{gather*}$$

(d) 代入容積：

$$\begin{gather*}
48 &\overset{\text{(a),(c)}}{=}& 6r^3 \\
r &=& 2\ \text{m} \\
L &\overset{\text{(c)}}{=}& 12\ \text{m} \\
\frac{L}{2r} &=& 3
\end{gather*}$$

(e) 質量與判定：

$$\begin{gather*}
M &\overset{\text{定義 1(a)}}{=}& 2\pi\rho_0 (2 \cdot 12 + 3 \cdot 2^2)\ \text{m}^2 \\
&=& 72\pi\rho_0\ \text{m}^2
\end{gather*}$$

$r \to 0$ 時 $rL = 48/r \to \infty$，$r \to \infty$ 時 $3r^2 \to \infty$，所以唯一候選點是全域最小值。

**結論**：$r = 2\ \text{m}$、$L = 12\ \text{m}$，長徑比 $\frac{L}{2r} = 3$，最小質量 $72\pi\rho_0\ \text{m}^2$。
對照組：若端蓋與側壁同材質（係數 $3 \to 1$），同樣算法會得到 $L = 2r$、長徑比 $1$。端蓋貴三倍，最佳形狀就拉長三倍。
