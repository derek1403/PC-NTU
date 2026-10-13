# Q04｜進階對稱：球面上的 $xy+yz+zx$

> 純數字 ★★★☆☆

## Question

設實數 $x, y, z$ 滿足球面限制條件

$$x^2 + y^2 + z^2 = 12$$

求函數

$$f(x, y, z) = xy + yz + zx$$

的極大值與極小值。

> 手算看點：善用三元對稱聯立方程式相減因式分解，並觀察乘數 $\lambda$ 使變數全相等與不全相等時，分別對應到哪一種極值。

## Question - Answer

### 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】[單約束 Lagrange 條件 (Lagrange Condition)](../01_basic_use.md)：** 約束上的極值點，必使 Lagrangian 對所有變數的偏導數同時為零；解出的只是候選點。

  $$\mathcal{L} = f - \lambda(g - c)$$

* **【已知 2】和的平方展開 (Square of a Sum)：** 把 $f$ 和約束連起來的恆等式。

  $$(x+y+z)^2 = x^2 + y^2 + z^2 + 2(xy + yz + zx)$$

* **【定義 1】目標與約束 (Objective & Constraint)：**

  (a) $$f(x,y,z) \overset{\text{def}}{=} xy + yz + zx$$

  (b) $$g(x,y,z) \overset{\text{def}}{=} x^2 + y^2 + z^2 = 12$$

* **【假設 1】緊緻且正則 (Compact & Regular)：** 球面是有界閉集，全域極值存在；球面上 $\nabla g = 2(x,y,z) \neq \mathbf{0}$，所以極值點都在方程組的解裡。

### solve

(a) 由【已知 1】【定義 1】寫出方程組：

$$\left\{\begin{array}{rcl}
y + z &=& 2\lambda x \\[4pt]
x + z &=& 2\lambda y \\[4pt]
x + y &=& 2\lambda z \\[4pt]
x^2 + y^2 + z^2 &=& 12
\end{array}\right.$$

(b) 第一式減第二式（第二、三式同理）：

$$\begin{gather*}
y - x &\overset{\text{(a)}}{=}& 2\lambda (x - y) \\
0 &=& (x - y)(1 + 2\lambda)
\end{gather*}$$

同理 $(y - z)(1 + 2\lambda) = 0$。

(c) 情形 $\lambda \neq -\frac{1}{2}$：三個變數全相等。

$$\begin{gather*}
3x^2 &\overset{\text{(a),(b)}}{=}& 12 \\
x &=& \pm 2 \\
f(\pm 2, \pm 2, \pm 2) &\overset{\text{定義 1(a)}}{=}& 3 \cdot 4 \\
f(\pm 2, \pm 2, \pm 2) &=& 12
\end{gather*}$$

(d) 情形 $\lambda = -\frac{1}{2}$：第一式變成 $y + z = -x$，即 $x + y + z = 0$。

$$\begin{gather*}
2f &\overset{\text{已知 2,定義 1}}{=}& (x+y+z)^2 - (x^2+y^2+z^2) \\
2f &\overset{\text{(a)}}{=}& 0 - 12 \\
f &=& -6
\end{gather*}$$

這組解是平面 $x+y+z=0$ 與球面的交圓，例如 $(\sqrt{6},-\sqrt{6},0)$、$(\sqrt{2},\sqrt{2},-2\sqrt{2})$。

**結論**：由【假設 1】比較候選點：

* 最大值 $f = 12$，在 $(2,2,2)$、$(-2,-2,-2)$（變數全相等）
* 最小值 $f = -6$，在整個圓 $\{x+y+z=0\} \cap \{x^2+y^2+z^2=12\}$ 上（對稱性破缺）
