# Q12｜熱力學：固定總能量下的熵最大與熱平衡

> 應用題 ★★★☆☆

## Question

考慮兩個互相交換能量的區域，其溫度分別為 $T_1, T_2$。假設每個區域的熵可以寫成

$$S_i=C_i\ln T_i$$

其中 $C_1,C_2>0$ 為常數。整個系統的總能量固定，因此有

$$C_1T_1+C_2T_2=E_0$$

總熵為

$$S(T_1,T_2) = C_1\ln T_1+C_2\ln T_2$$

利用 Lagrange multiplier 求系統在**熱平衡狀態**下 $T_1,T_2$ 之間的關係。

$$\boxed{\text{平衡狀態}=\text{在固定總能量下使熵最大}}$$

## Question - Answer

### 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】[單約束 Lagrange 條件 (Lagrange Condition)](../01_basic_use.md)：** 約束上的極值點，必使 Lagrangian 對所有變數的偏導數同時為零。

  $$\mathcal{L} = S - \lambda(g - E_0)$$

* **【定義 1】目標與約束 (Objective & Constraint)：**

  (a) $$S(T_1,T_2) \overset{\text{def}}{=} C_1\ln T_1 + C_2\ln T_2$$

  (b) $$g(T_1,T_2) \overset{\text{def}}{=} C_1T_1 + C_2T_2 = E_0$$

  * $T_1, T_2$ : 溫度 (Temperature) $[\text{K}]$，皆 $> 0$
  * $C_1, C_2$ : 熱容量 (Heat capacity) $[\text{J}\cdot\text{K}^{-1}]$
  * $E_0$ : 總能量 (Total energy) $[\text{J}]$
  * $S$ : 總熵 (Total entropy) $[\text{J}\cdot\text{K}^{-1}]$
  * $\lambda$ : 乘數 (Lagrange multiplier) $[\text{K}^{-1}]$

### solve

(a) 由【已知 1】【定義 1】寫出方程組：

$$\left\{\begin{array}{rcl}
\dfrac{C_1}{T_1} &=& \lambda C_1 \\[8pt]
\dfrac{C_2}{T_2} &=& \lambda C_2 \\[8pt]
C_1T_1 + C_2T_2 &=& E_0
\end{array}\right.$$

(b) 約去 $C_i$（皆 $> 0$）：

$$\begin{gather*}
T_1 &\overset{\text{(a)}}{=}& \frac{1}{\lambda} \\
T_2 &\overset{\text{(a)}}{=}& \frac{1}{\lambda}
\end{gather*}$$

(c) 代入能量守恆：

$$\begin{gather*}
E_0 &\overset{\text{(a),(b)}}{=}& \frac{C_1 + C_2}{\lambda} \\
T_1 = T_2 &\overset{\text{(b)}}{=}& \frac{E_0}{C_1 + C_2}
\end{gather*}$$

(d) 判定：$\ln$ 是凹函數，$S$ 在線段上也是凹的；線段兩端 $T_1 \to 0$ 或 $T_2 \to 0$ 時 $S \to -\infty$。所以唯一候選點是全域最大值。

**結論**：熱平衡條件是 $T_1 = T_2 = \dfrac{E_0}{C_1 + C_2}$，也就是熱力學第零定律的「溫度相等」。乘數 $\lambda = \dfrac{1}{T}$ 正是熱力學中 $\dfrac{\partial S}{\partial E} = \dfrac{1}{T}$：每多給系統一單位能量，熵增加 $1/T$。
