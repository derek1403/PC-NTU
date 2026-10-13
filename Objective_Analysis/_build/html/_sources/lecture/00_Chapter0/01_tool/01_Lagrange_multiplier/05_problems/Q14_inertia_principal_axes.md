# Q14｜古典力學：非對稱衛星的慣量主軸

> 應用題 ★★★★☆

## Question

一顆結構非對稱的科研衛星，其相對於質心的轉動慣量張量（Inertia Tensor）經地面測量後，對任意自轉軸單位向量 $\hat{n} = (n_x, n_y, n_z)$ 的轉動慣量可表為二次型：

$$I(n_x, n_y, n_z) = 5n_x^2 + 5n_y^2 + 8n_z^2 - 4n_x n_y \quad (\text{kg}\cdot\text{m}^2)$$

在單位向量限制條件 $n_x^2 + n_y^2 + n_z^2 = 1$ 下，利用拉格朗日乘數法找出此衛星可能出現的最大與最小轉動慣量，以及對應的慣量主軸方向 $(n_x, n_y, n_z)$。

## Question - Answer

### 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】[單約束 Lagrange 條件 (Lagrange Condition)](../01_basic_use.md)：** 約束上的極值點，必使 Lagrangian 對所有變數的偏導數同時為零。

  $$\mathcal{L} = I - \lambda(g - 1)$$

* **【已知 2】二次齊次函數的 Euler 定理 (Euler's Theorem for Homogeneous Functions)：** 二次齊次函數與其梯度的內積等於函數值的兩倍。

  $$\mathbf{n}\cdot\nabla I = 2I$$

* **【定義 1】目標與約束 (Objective & Constraint)：**

  (a) $$I(\mathbf{n}) \overset{\text{def}}{=} 5n_x^2 + 5n_y^2 + 8n_z^2 - 4n_x n_y$$

  (b) $$g(\mathbf{n}) \overset{\text{def}}{=} n_x^2 + n_y^2 + n_z^2 = 1$$

  * $\mathbf{n} = (n_x,n_y,n_z)$ : 轉軸單位向量 (Rotation axis) $[\text{無單位}]$
  * $I$ : 轉動慣量 (Moment of inertia) $[\text{kg}\cdot\text{m}^2]$
  * $\lambda$ : 乘數 (Lagrange multiplier) $[\text{kg}\cdot\text{m}^2]$

### solve

(a) 由【已知 1】【定義 1】寫出方程組（已約去 2）：

$$\left\{\begin{array}{rcl}
5n_x - 2n_y &=& \lambda n_x \\[4pt]
5n_y - 2n_x &=& \lambda n_y \\[4pt]
8n_z &=& \lambda n_z \\[4pt]
n_x^2 + n_y^2 + n_z^2 &=& 1
\end{array}\right.$$

這正是特徵值問題 $\mathbf{I}\,\mathbf{n} = \lambda\,\mathbf{n}$。

(b) 候選點上 $I$ 的值就是 $\lambda$：

$$\begin{gather*}
2I &\overset{\text{已知 2}}{=}& \mathbf{n}\cdot\nabla I \\
2I &\overset{\text{(a)}}{=}& \mathbf{n}\cdot 2\lambda\mathbf{n} \\
I &\overset{\text{定義 1(b)}}{=}& \lambda
\end{gather*}$$

(c) 情形 $n_z \neq 0$：第三式給 $\lambda = 8$，代入前兩式：

$$\begin{gather*}
-3n_x &\overset{\text{(a)}}{=}& 2n_y \\
-3n_y &\overset{\text{(a)}}{=}& 2n_x \\
n_x = n_y &=& 0
\end{gather*}$$

（兩式聯立的係數行列式 $9 - 4 \neq 0$，只有零解。）所以 $\mathbf{n} = (0,0,\pm 1)$，$I = 8$。

(d) 情形 $n_z = 0$：前兩式相加、相減：

$$\begin{gather*}
3(n_x + n_y) &\overset{\text{(a)}}{=}& \lambda(n_x + n_y) \\
7(n_x - n_y) &\overset{\text{(a)}}{=}& \lambda(n_x - n_y)
\end{gather*}$$

$n_x, n_y$ 不可全為零，所以：

* $\lambda = 3$：$n_x = n_y$，$\mathbf{n} = \pm\frac{1}{\sqrt{2}}(1,1,0)$，$I = 3$
* $\lambda = 7$：$n_x = -n_y$，$\mathbf{n} = \pm\frac{1}{\sqrt{2}}(1,-1,0)$，$I = 7$

(e) 判定：單位球面緊緻且 $\nabla g \neq \mathbf{0}$，全域極值必在候選點中。

**結論**：

* 最大轉動慣量 $8\ \text{kg}\cdot\text{m}^2$，主軸 $(0,0,1)$
* 最小轉動慣量 $3\ \text{kg}\cdot\text{m}^2$，主軸 $\frac{1}{\sqrt{2}}(1,1,0)$
* 中間 $7\ \text{kg}\cdot\text{m}^2$，主軸 $\frac{1}{\sqrt{2}}(1,-1,0)$（約束上的鞍點）

在單位球上找二次型的極值，就是求對稱矩陣的**特徵值與特徵向量**，而乘數 $\lambda$ 就是特徵值（也就是主轉動慣量）。客觀分析裡的 EOF 分析也是同一個數學結構。
