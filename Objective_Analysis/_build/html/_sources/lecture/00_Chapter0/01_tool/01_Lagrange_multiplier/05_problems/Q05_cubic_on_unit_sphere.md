# Q05｜微積分期末壓軸：單位球上的 $x^2y+yz^2$

> 純數字 ★★★★★

## Question

求函數

$$f(x,y,z)=x^2y+yz^2$$

在限制條件

$$x^2+y^2+z^2=1$$

下的所有極值。要求：

1. 找出所有可能的 critical points。
2. 計算各點的 $f$ 值。
3. 判斷全域最大值與全域最小值。
4. 說明為什麼你找到的結果確實包含所有可能的極值。

## Question - Answer

### 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】[單約束 Lagrange 條件 (Lagrange Condition)](../01_basic_use.md)：** 約束上的極值點，必使 Lagrangian 對所有變數的偏導數同時為零；解出的只是候選點。

  $$\mathcal{L} = f - \lambda(g - c)$$

* **【已知 2】極值定理 (Extreme Value Theorem)：** 連續函數在有界閉集上一定取得最大值與最小值。

  $$f \in C^0(S),\ \ S \text{ 有界且閉} \quad\text{則}\quad \exists\ \mathbf{x}_{\max},\ \mathbf{x}_{\min} \in S$$

* **【定義 1】目標與約束 (Objective & Constraint)：**

  (a) $$f(x,y,z) \overset{\text{def}}{=} x^2y + yz^2 = y\,(x^2 + z^2)$$

  (b) $$g(x,y,z) \overset{\text{def}}{=} x^2 + y^2 + z^2 = 1$$

* **【假設 1】約束正則 (Regular Constraint)：** 單位球上 $\nabla g$ 處處不為零，加上 $f, g$ 都是多項式（$C^1$），[03_proof.md](../03_proof.md) 的前提全部成立。

  $$\nabla g = 2(x,y,z) \neq \mathbf{0}$$

### solve

(a) 由【已知 1】【定義 1】寫出方程組：

$$\left\{\begin{array}{rcl}
2xy &=& 2\lambda x \\[4pt]
x^2 + z^2 &=& 2\lambda y \\[4pt]
2yz &=& 2\lambda z \\[4pt]
x^2 + y^2 + z^2 &=& 1
\end{array}\right.$$

(b) 第一、三式因式分解（不可同除）：

$$\begin{gather*}
0 &\overset{\text{(a)}}{=}& 2x(y - \lambda) \\
0 &\overset{\text{(a)}}{=}& 2z(y - \lambda)
\end{gather*}$$

所以不是 $\lambda = y$，就是 $x = z = 0$。

(c) 情形 $\lambda \neq y$，即 $x = z = 0$：

$$\begin{gather*}
y^2 &\overset{\text{(a)}}{=}& 1 \\
y &=& \pm 1 \\
f(0, \pm 1, 0) &\overset{\text{定義 1(a)}}{=}& 0
\end{gather*}$$

（第二式給 $\lambda = 0 \neq y$，相容。）

(d) 情形 $\lambda = y$：

$$\begin{gather*}
x^2 + z^2 &\overset{\text{(a),(b)}}{=}& 2y^2 \\
1 &\overset{\text{(a)}}{=}& 2y^2 + y^2 \\
y &=& \pm\frac{1}{\sqrt{3}}
\end{gather*}$$

代回 $f$：

$$\begin{gather*}
f &\overset{\text{定義 1(a)}}{=}& y\,(x^2 + z^2) \\
&\overset{\text{(d)}}{=}& 2y^3 \\
&=& \pm\frac{2}{3\sqrt{3}}
\end{gather*}$$

對應的點是兩個圓：$y = \pm\frac{1}{\sqrt{3}}$、$x^2 + z^2 = \frac{2}{3}$。

(e) 回答四個要求：

1. Critical points：$(0,\pm 1,0)$，以及圓 $\{y = \pm\tfrac{1}{\sqrt{3}},\ x^2+z^2 = \tfrac{2}{3}\}$ 上所有點。
2. 函數值：分別為 $0$ 與 $\pm\frac{2}{3\sqrt{3}} = \pm\frac{2\sqrt{3}}{9}$。
3. 全域最大值 $\frac{2\sqrt{3}}{9}$（圓 $y = \frac{1}{\sqrt{3}}$ 上），全域最小值 $-\frac{2\sqrt{3}}{9}$（圓 $y = -\frac{1}{\sqrt{3}}$ 上）。
4. 完整性：由【已知 2】全域極值存在；由【假設 1】它們必滿足 (a)；而 (b) 的兩個分支 $x = z = 0$ 與 $\lambda = y$ 已窮盡所有可能。所以不會漏解。

**結論**：$f_{\max} = \frac{2\sqrt{3}}{9}$、$f_{\min} = -\frac{2\sqrt{3}}{9}$，極值點各是一整個圓（$f$ 對 $x$–$z$ 平面旋轉對稱）。
