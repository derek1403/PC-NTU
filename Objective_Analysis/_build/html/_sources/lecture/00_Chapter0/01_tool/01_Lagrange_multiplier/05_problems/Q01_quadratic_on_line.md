# Q01｜基本題：二次函數在直線上的極值

> 純數字 ★☆☆☆☆

## Question

求函數

$$f(x,y)=x^2+2y^2$$

在限制條件

$$x+y=6$$

下的最大值與最小值。

## Question - Answer

### 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】[單約束 Lagrange 條件 (Lagrange Condition)](../01_basic_use.md)：** 約束上的極值點，必使 Lagrangian 對所有變數的偏導數同時為零；解出的只是候選點。

  $$\mathcal{L}(x,y,\lambda) = f(x,y) - \lambda\big(g(x,y) - c\big)$$

* **【定義 1】目標與約束 (Objective & Constraint)：** 一個開口向上的橢圓拋物面，被限制在一條直線上。

  (a) $$f(x,y) \overset{\text{def}}{=} x^2 + 2y^2$$

  (b) $$g(x,y) \overset{\text{def}}{=} x + y = 6$$

### solve

(a) 由【已知 1】【定義 1】寫出方程組：

$$\left\{\begin{array}{rcl}
\dfrac{\partial \mathcal{L}}{\partial x} = 2x - \lambda &=& 0 \\[8pt]
\dfrac{\partial \mathcal{L}}{\partial y} = 4y - \lambda &=& 0 \\[8pt]
x + y &=& 6
\end{array}\right.$$

(b) 消去 $\lambda$ 再代入約束：

$$\begin{gather*}
2x &\overset{\text{(a)}}{=}& 4y \\
x &=& 2y \\
6 &\overset{\text{(a)}}{=}& 2y + y \\
y &=& 2 \\
x &=& 4
\end{gather*}$$

(c) 候選點的函數值：

$$\begin{gather*}
f(4,2) &\overset{\text{定義 1(a)}}{=}& 4^2 + 2\cdot 2^2 \\
&=& 24
\end{gather*}$$

(d) 判定：沿直線 $x = 6 - y$ 往外走，函數沒有上界。

$$\begin{gather*}
f(6-y,\ y) &\overset{\text{定義 1(a)}}{=}& (6-y)^2 + 2y^2 \\
&=& 3y^2 - 12y + 36 \\
&=& 3(y-2)^2 + 24
\end{gather*}$$

**結論**：最小值 $f = 24$，在 $(4,2)$；**沒有最大值**。方程組只給出一個候選點，它不會告訴你極值是否存在（見 [04_exceptions.md](../04_exceptions.md) §2）。
