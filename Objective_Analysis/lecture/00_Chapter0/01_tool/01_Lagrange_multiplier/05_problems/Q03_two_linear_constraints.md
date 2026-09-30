# Q03｜雙重限制條件：兩平面交線上離原點最近的點

> 純數字 ★★★☆☆

## Question

求函數

$$f(x,y,z)=x^2+y^2+z^2$$

在兩個限制條件

$$x+y+z=6$$

以及

$$x-y=2$$

下的極值。要求找出所有可能的極值點，並判斷其為最大值或最小值。

## Question - Answer

### 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】[多約束 Lagrange 條件 (Lagrange Condition)](../02_advanced_use.md)：** 每條約束配一個乘數，極值點必使 Lagrangian 對所有變數的偏導數同時為零。

  $$\mathcal{L} = f - \lambda_1(g_1 - c_1) - \lambda_2(g_2 - c_2)$$

* **【定義 1】目標與約束 (Objective & Constraints)：** $f$ 是到原點距離的平方；兩個平面交成一條直線。

  (a) $$f(x,y,z) \overset{\text{def}}{=} x^2 + y^2 + z^2$$

  (b) $$g_1(x,y,z) \overset{\text{def}}{=} x + y + z = 6$$

  (c) $$g_2(x,y,z) \overset{\text{def}}{=} x - y = 2$$

* **【假設 1】LICQ：** 兩個法向量不平行，處處線性獨立。

  $$\nabla g_1 = (1,1,1),\qquad \nabla g_2 = (1,-1,0)$$

### solve

(a) 由【已知 1】【定義 1】寫出方程組：

$$\left\{\begin{array}{rcl}
2x - \lambda_1 - \lambda_2 &=& 0 \\[4pt]
2y - \lambda_1 + \lambda_2 &=& 0 \\[4pt]
2z - \lambda_1 &=& 0 \\[4pt]
x + y + z &=& 6 \\[4pt]
x - y &=& 2
\end{array}\right.$$

(b) 前兩式相加消去 $\lambda_2$，再用第三式消去 $\lambda_1$：

$$\begin{gather*}
2x + 2y &\overset{\text{(a)}}{=}& 2\lambda_1 \\
2x + 2y &\overset{\text{(a)}}{=}& 4z \\
x + y &=& 2z
\end{gather*}$$

(c) 代入兩條約束：

$$\begin{gather*}
6 &\overset{\text{(a),(b)}}{=}& 2z + z \\
z &=& 2 \\
x + y &\overset{\text{(b)}}{=}& 4 \\
x &\overset{\text{(a)}}{=}& 3 \\
y &=& 1
\end{gather*}$$

(d) 函數值：

$$\begin{gather*}
f(3,1,2) &\overset{\text{定義 1(a)}}{=}& 9 + 1 + 4 \\
&=& 14
\end{gather*}$$

(e) 判定：可行域是一條直線，往兩端走 $f \to \infty$，所以沒有最大值；唯一候選點就是最小值。

**結論**：最小值 $f = 14$，在 $(3,1,2)$（此時 $\lambda_1 = 4$、$\lambda_2 = 2$）；**沒有最大值**。幾何上就是交線上離原點最近的點，最短距離 $\sqrt{14}$。
