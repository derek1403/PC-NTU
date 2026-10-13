# Q02｜基礎暖身：橢圓上的 $x^2y$ 與分類討論

> 純數字 ★★☆☆☆

## Question

求目標函數

$$f(x, y) = x^2 y$$

在橢圓限制條件

$$x^2 + 2y^2 = 6$$

下的絕對極大值與絕對極小值，並列出所有發生極值的座標點 $(x, y)$。

> 手算看點：分類討論 $\nabla f = \lambda \nabla g$ 時，避免直接同除變數而漏掉座標軸上的臨界點。

## Question - Answer

### 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】[單約束 Lagrange 條件 (Lagrange Condition)](../01_basic_use.md)：** 約束上的極值點，必使 Lagrangian 對所有變數的偏導數同時為零；解出的只是候選點。

  $$\mathcal{L}(x,y,\lambda) = f(x,y) - \lambda\big(g(x,y) - c\big)$$

* **【已知 2】極值定理 (Extreme Value Theorem)：** 連續函數在有界閉集上一定取得最大值與最小值。橢圓是有界閉集，所以本題的全域極值必定存在。

  $$f \in C^0(S),\ \ S \text{ 有界且閉} \quad\text{則}\quad \exists\ \mathbf{x}_{\max},\ \mathbf{x}_{\min} \in S$$

* **【定義 1】目標與約束 (Objective & Constraint)：**

  (a) $$f(x,y) \overset{\text{def}}{=} x^2 y$$

  (b) $$g(x,y) \overset{\text{def}}{=} x^2 + 2y^2 = 6$$

* **【假設 1】約束正則 (Regular Constraint)：** 橢圓上 $\nabla g$ 處處不為零（只有原點會讓它為零，而原點不在橢圓上），所以每個極值點都會出現在方程組的解裡。

  $$\nabla g = (2x,\ 4y) \neq \mathbf{0}$$

### solve

(a) 由【已知 1】【定義 1】寫出方程組：

$$\left\{\begin{array}{rclcl}
\dfrac{\partial \mathcal{L}}{\partial x} &=& 2xy - 2\lambda x &=& 0 \\[8pt]
\dfrac{\partial \mathcal{L}}{\partial y} &=& x^2 - 4\lambda y &=& 0 \\[8pt]
& &x^2 + 2y^2 &=& 6
\end{array}\right.$$

(b) 第一式因式分解，**不可**同除 $x$：

$$\begin{gather*}
0 &\overset{\text{(a)}}{=}& 2xy - 2\lambda x \\
0 &=& 2x(y - \lambda)
\end{gather*}$$

所以 $x = 0$ 或 $\lambda = y$。

(c) 情形 $x = 0$：

$$\begin{gather*}
2y^2 &\overset{\text{(a)}}{=}& 6 \\
y &=& \pm\sqrt{3} \\
f(0,\pm\sqrt{3}) &\overset{\text{定義 1(a)}}{=}& 0
\end{gather*}$$

（第二式 $0 = 4\lambda y$ 給 $\lambda = 0$，相容。）

(d) 情形 $\lambda = y$：

$$\begin{gather*}
x^2 &\overset{\text{(a),(b)}}{=}& 4y^2 \\
6 &\overset{\text{(a)}}{=}& 4y^2 + 2y^2 \\
y &=& \pm 1 \\
x &=& \pm 2 \\
f(\pm 2, y) &\overset{\text{定義 1(a)}}{=}& 4y
\end{gather*}$$

(e) 比較候選點：$f \in \{0,\ 4,\ -4\}$。

**結論**：由【已知 2】【假設 1】全域極值必在上列候選點中。

* 最大值 $f = 4$，在 $(2,1)$、$(-2,1)$
* 最小值 $f = -4$，在 $(2,-1)$、$(-2,-1)$

$(0,\pm\sqrt{3})$ 只是局部極值（見 [04_exceptions.md](../04_exceptions.md) §1）。若在 (b) 直接同除 $x$，會漏掉它們，雖然這題不影響答案，但在別題可能正好漏掉全域極值。
