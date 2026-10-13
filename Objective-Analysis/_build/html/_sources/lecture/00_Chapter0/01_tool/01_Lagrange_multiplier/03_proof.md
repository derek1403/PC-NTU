# 拉格朗日乘數法的證明 (Proof of the Lagrange Multiplier Method)

## 幾何直覺 (Geometric Intuition)

想像沿著一條環狀步道（約束 $g = c$）爬山（目標 $f$）。只要步道**穿過** $f$ 的等高線，就還能沿步道往更高或更低處走；
只有當步道與等高線**相切**時，往任何允許的方向走 $f$ 都不再改變，這裡才可能是極值點。
「相切」就是兩者法向量平行，也就是 $\nabla f \parallel \nabla g$：

$$\nabla f = \lambda \nabla g$$

下面把這句話嚴格化：先證單一約束，再推廣到多重約束。

---

## 1. 單一約束 (Single Constraint)

### 假設與已知 (Assumptions & Preliminaries)

* **【假設 1】正則的局部極值點 (Regular Local Extremum)：** $f$ 與 $g$ 在 $\mathbb{R}^m$ 上一階連續可微，$\mathbf{x}^*$ 是 $f$ 在約束面 $S$ 上的局部極值點，而且約束的梯度在該點不為零（約束面在該點是光滑的，有明確的切平面）。

  (a) $$f,\ g \in C^1(\mathbb{R}^m)$$

  (b) $$S = \{\mathbf{x} : g(\mathbf{x}) = c\},\qquad \mathbf{x}^* \in S$$

  (c) $$\nabla g(\mathbf{x}^*) \neq \mathbf{0}$$

  * $\mathbf{x}$ : 位置向量 (Position vector)，$\mathbf{x} = [x_1,\dots,x_m]$
  * $S$ : 約束面 (Constraint surface)
  * $c$ : 約束常數 (Constraint constant)

* **【已知 1】連鎖律 (Chain Rule)：** 純量場沿一條曲線的變化率，等於梯度與曲線速度的內積。

  $$\frac{d}{dt}\Big[h\big(\mathbf{r}(t)\big)\Big] = \nabla h\big(\mathbf{r}(t)\big)\cdot\mathbf{r}'(t)$$

  * $h$ : 任意 $C^1$ 純量函數 (Scalar function)
  * $\mathbf{r}(t)$ : 參數曲線 (Parametric curve)

* **【已知 2】切向量都能實現 (Tangent Vectors are Realizable)：** 在【假設 1】下，任何與 $\nabla g(\mathbf{x}^*)$ 垂直的方向 $\mathbf{v}$，都能找到一條**完全躺在** $S$ 上、通過 $\mathbf{x}^*$、且初速為 $\mathbf{v}$ 的曲線。（隱函數定理 (Implicit Function Theorem) 的推論。）

  $$\mathbf{v}\cdot\nabla g(\mathbf{x}^*) = 0 \quad\text{則存在}\quad \mathbf{r}(t) \in S,\ \ \mathbf{r}(0) = \mathbf{x}^*,\ \ \mathbf{r}'(0) = \mathbf{v}$$

* **【已知 3】正交補 (Orthogonal Complement)：** 在 $\mathbb{R}^m$ 中，若一個向量垂直於「所有與 $\mathbf{a}$ 垂直的向量」，它只能與 $\mathbf{a}$ 平行。

  $$\mathbf{w}\cdot\mathbf{v} = 0 \ \ \text{對所有滿足 } \mathbf{v}\cdot\mathbf{a} = 0 \text{ 的 } \mathbf{v} \quad\text{則}\quad \mathbf{w} = \lambda\mathbf{a}$$

* **【已知 4】單變數極值的一階條件 (First-order Condition)：** 可微的單變數函數在內部局部極值點的導數為零。

  $$\phi(0)\ \text{為局部極值} \quad\text{則}\quad \phi'(0) = 0$$

* **【定義 1】約束面上的曲線 (Curve on the Constraint Surface)：** 任取一條落在 $S$ 上、通過 $\mathbf{x}^*$ 的光滑曲線，並記其初速為 $\mathbf{v}$。

  (a) $$\mathbf{r}(t) \in S \quad \forall t$$

  (b) $$\mathbf{r}(0) \overset{\text{def}}{=} \mathbf{x}^*$$

  (c) $$\mathbf{v} \overset{\text{def}}{=} \mathbf{r}'(0)$$

### proof

(a) $\nabla g$ 垂直於切向量：曲線始終在 $S$ 上，所以 $g(\mathbf{r}(t))$ 是常數。

$$\begin{gather*}
0 &=& \frac{d}{dt}\Big[c\Big] \\
&\overset{\text{定義 1(a)}}{=}& \frac{d}{dt}\Big[g\big(\mathbf{r}(t)\big)\Big]_{t=0} \\
&\overset{\text{已知 1}}{=}& \nabla g\big(\mathbf{r}(0)\big)\cdot\mathbf{r}'(0) \\
&\overset{\text{定義 1(b)(c)}}{=}& \nabla g(\mathbf{x}^*)\cdot\mathbf{v}
\end{gather*}$$

(b) $\nabla f$ 也垂直於切向量：$\phi(t) = f(\mathbf{r}(t))$ 在 $t=0$ 取得局部極值。

$$\begin{gather*}
0 &\overset{\text{假設 1(b),已知 4}}{=}& \frac{d}{dt}\Big[f\big(\mathbf{r}(t)\big)\Big]_{t=0} \\
&\overset{\text{已知 1}}{=}& \nabla f\big(\mathbf{r}(0)\big)\cdot\mathbf{r}'(0) \\
&\overset{\text{定義 1(b)(c)}}{=}& \nabla f(\mathbf{x}^*)\cdot\mathbf{v}
\end{gather*}$$

(c) 由【已知 2】，(a) 中的 $\mathbf{v}$ 可以取遍所有與 $\nabla g(\mathbf{x}^*)$ 垂直的方向，而 (b) 說 $\nabla f(\mathbf{x}^*)$ 與它們全部垂直：

$$\begin{gather*}
\nabla f(\mathbf{x}^*) &\overset{\text{(a),(b),已知 2,3}}{=}& \lambda\,\nabla g(\mathbf{x}^*)
\end{gather*}$$

這正是 $\frac{\partial \mathcal{L}}{\partial x_i} = 0$；再加上約束本身 $\frac{\partial \mathcal{L}}{\partial \lambda} = 0$，就是 [01_basic_use.md](01_basic_use.md) 的聯立方程組。$\blacksquare$

---

## 2. 多重約束 (Multiple Constraints)

### 假設與已知 (Assumptions & Preliminaries)

* **【假設 2】線性獨立約束條件 (LICQ, Linear Independence Constraint Qualification)：** 有 $k < m$ 條約束，$\mathbf{x}^*$ 是 $f$ 在它們交集上的局部極值點，而且各約束的梯度在 $\mathbf{x}^*$ **線性獨立**（交集在該點是光滑的 $m-k$ 維曲面）。

  (a) $$S = \{\mathbf{x} : g_n(\mathbf{x}) = c_n,\ n = 1,\dots,k\},\qquad \mathbf{x}^* \in S$$

  (b) $$\sum_{n=1}^{k} a_n \nabla g_n(\mathbf{x}^*) = \mathbf{0} \quad\text{只有}\quad a_1 = \dots = a_k = 0$$

* **【已知 5】多約束下切向量都能實現 (Tangent Vectors are Realizable)：** 在【假設 2】下，任何同時垂直於所有 $\nabla g_n(\mathbf{x}^*)$ 的方向，都是某條落在 $S$ 上的曲線的初速。（隱函數定理的推論；【已知 2】的推廣。）

  $$\mathbf{v}\cdot\nabla g_n(\mathbf{x}^*) = 0\ \ \forall n \quad\text{則存在}\quad \mathbf{r}(t) \in S,\ \ \mathbf{r}(0) = \mathbf{x}^*,\ \ \mathbf{r}'(0) = \mathbf{v}$$

* **【已知 6】多向量的正交補 (Orthogonal Complement of a Span)：** 若一個向量垂直於「所有同時垂直 $\mathbf{a}_1,\dots,\mathbf{a}_k$ 的向量」，它必落在 $\mathbf{a}_1,\dots,\mathbf{a}_k$ 張成的子空間內。

  $$\mathbf{w} \in \Big(\{\mathbf{a}_1,\dots,\mathbf{a}_k\}^{\perp}\Big)^{\perp} = \operatorname{span}\{\mathbf{a}_1,\dots,\mathbf{a}_k\}$$

### proof

把第 1 節的 (a)(b) 對每一條 $g_n$ 各做一次（曲線落在交集上，所以每個 $g_n(\mathbf{r}(t))$ 都是常數），得到 $\nabla g_n(\mathbf{x}^*)\cdot\mathbf{v} = 0$ 與 $\nabla f(\mathbf{x}^*)\cdot\mathbf{v} = 0$。由【已知 5】$\mathbf{v}$ 取遍整個切空間：

$$\begin{gather*}
\nabla f(\mathbf{x}^*) &\overset{\text{已知 5,6}}{=}& \sum_{n=1}^{k}\lambda_n\,\nabla g_n(\mathbf{x}^*)
\end{gather*}$$

【假設 2(b)】保證這組 $\lambda_n$ **唯一**。這就是 [02_advanced_use.md](02_advanced_use.md) 的 $\frac{\partial \mathcal{L}}{\partial x_i} = 0$。$\blacksquare$

> LICQ 用在【已知 5】：若梯度線性相依，交集可能在 $\mathbf{x}^*$ 退化成尖點或孤立點，「切空間」比 $\{\nabla g_n\}^{\perp}$ 小，(c) 那一步就推不過去。反例見 [04_exceptions.md](04_exceptions.md)。
