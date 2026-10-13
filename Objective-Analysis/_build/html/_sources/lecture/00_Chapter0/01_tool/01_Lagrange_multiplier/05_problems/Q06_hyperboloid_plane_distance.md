# Q06｜微積分期末壓軸：雙曲面與平面交線到原點的距離

> 純數字 ★★★★★

## Question

在三維空間 $\mathbb{R}^3$ 中，考慮單葉雙曲面

$$x^2 + y^2 - z^2 = 1$$

與平面

$$x + y + 2z = 0$$

相交所得的曲線 $C$。

1. **存在性證明**：單葉雙曲面與平面本身都是無界（unbounded）曲面。請先用代數消去法證明交線 $C$ 是一個封閉有界（compact）的橢圓，從而保證 $C$ 上的點到原點的最大與最小距離必然存在。
2. **雙乘數求解**：利用雙重拉格朗日乘數法 $\nabla f = \lambda \nabla g + \mu \nabla h$，求曲線 $C$ 上距離原點最近與最遠的座標點，以及對應的 $d_{\min}$ 與 $d_{\max}$。

> 壓軸陷阱：在解 $(1 - \lambda)(x - y) = 0$ 時，絕大多數考生只討論 $x = y$，卻忽略了 $\lambda = 1$ 的退化分支，而這條分支剛好藏著真正的最小距離！

## Question - Answer

### 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】[多約束 Lagrange 條件 (Lagrange Condition)](../02_advanced_use.md)：** 極值點（在 LICQ 下）必使目標的梯度是各約束梯度的線性組合。

  $$\nabla f = \lambda\nabla g + \mu\nabla h$$

* **【已知 2】極值定理 (Extreme Value Theorem)：** 連續函數在有界閉集上一定取得最大值與最小值。

  $$f \in C^0(S),\ \ S \text{ 有界且閉} \quad\text{則}\quad \exists\ \mathbf{x}_{\max},\ \mathbf{x}_{\min} \in S$$

* **【定義 1】目標與約束 (Objective & Constraints)：** 用距離平方代替距離，避免根號（兩者極值點相同）。

  (a) $$f(x,y,z) \overset{\text{def}}{=} x^2 + y^2 + z^2$$

  (b) $$g(x,y,z) \overset{\text{def}}{=} x^2 + y^2 - z^2 = 1$$

  (c) $$h(x,y,z) \overset{\text{def}}{=} x + y + 2z = 0$$

* **【定義 2】旋轉 45° 的座標 (Rotated Coordinates)：** 讓交叉項 $xy$ 消失。

  (a) $$s \overset{\text{def}}{=} x + y$$

  (b) $$d \overset{\text{def}}{=} x - y$$

### solve

#### (1) 存在性

(a) 用平面消去 $z$，再改用 $s, d$ 表示：

$$\begin{gather*}
z &\overset{\text{定義 1(c)}}{=}& -\frac{x + y}{2} \\
z &\overset{\text{定義 2(a)}}{=}& -\frac{s}{2}
\end{gather*}$$

$$\begin{gather*}
1 &\overset{\text{定義 1(b)}}{=}& x^2 + y^2 - z^2 \\
1 &\overset{\text{定義 2,(a)}}{=}& \frac{s^2 + d^2}{2} - \frac{s^2}{4} \\
4 &=& s^2 + 2d^2
\end{gather*}$$

(b) $s^2 + 2d^2 = 4$ 是 $(s,d)$ 平面上的橢圓，所以 $|s| \le 2$、$|d| \le \sqrt{2}$；$x, y, z$ 都是 $s, d$ 的線性函數，也都有界。$C$ 是兩個閉集的交集，所以是閉集。$C$ 有界且閉，由【已知 2】$d_{\min}$、$d_{\max}$ 必存在。

#### (2) 雙乘數求解

(c) 由【已知 1】【定義 1】寫出方程組：

$$\left\{\begin{array}{rcl}
2x &=& 2\lambda x + \mu \\[4pt]
2y &=& 2\lambda y + \mu \\[4pt]
2z &=& -2\lambda z + 2\mu \\[4pt]
x^2 + y^2 - z^2 &=& 1 \\[4pt]
x + y + 2z &=& 0
\end{array}\right.$$

(d) 前兩式相減：

$$\begin{gather*}
2(x - y) &\overset{\text{(c)}}{=}& 2\lambda(x - y) \\
0 &=& (1 - \lambda)(x - y)
\end{gather*}$$

(e) 情形 $x = y$：

$$\begin{gather*}
z &\overset{\text{(c)}}{=}& -x \\
1 &\overset{\text{(c)}}{=}& x^2 + x^2 - x^2 \\
x &=& \pm 1 \\
f(\pm 1, \pm 1, \mp 1) &\overset{\text{定義 1(a)}}{=}& 3
\end{gather*}$$

(f) 情形 $\lambda = 1$（陷阱分支）：

$$\begin{gather*}
\mu &\overset{\text{(c)}}{=}& 2x - 2x \\
\mu &=& 0 \\
2z &\overset{\text{(c)}}{=}& -2z \\
z &=& 0 \\
x + y &\overset{\text{(c)}}{=}& 0 \\
2x^2 &\overset{\text{(c)}}{=}& 1 \\
x &=& \pm\frac{1}{\sqrt{2}} \\
f\Big(\pm\tfrac{1}{\sqrt{2}}, \mp\tfrac{1}{\sqrt{2}}, 0\Big) &\overset{\text{定義 1(a)}}{=}& 1
\end{gather*}$$

(g) LICQ 檢查：$\nabla g = (2x, 2y, -2z)$ 與 $\nabla h = (1,1,2)$ 平行需要 $x = y$ 且 $-z = 2x$，代入平面得 $x = y = z = 0$，不在 $C$ 上。所以 LICQ 處處成立，(e)(f) 已涵蓋所有極值點。

**結論**：

* 最近點 $\big(\tfrac{1}{\sqrt{2}}, -\tfrac{1}{\sqrt{2}}, 0\big)$、$\big(-\tfrac{1}{\sqrt{2}}, \tfrac{1}{\sqrt{2}}, 0\big)$，$d_{\min} = 1$（來自 $\lambda = 1$ 分支）
* 最遠點 $(1,1,-1)$、$(-1,-1,1)$，$d_{\max} = \sqrt{3}$

驗算：$C$ 上 $f = (x^2+y^2-z^2) + 2z^2 = 1 + 2z^2$，而 $z = -s/2 \in [-1,1]$，所以 $f \in [1,3]$，與上面一致。
