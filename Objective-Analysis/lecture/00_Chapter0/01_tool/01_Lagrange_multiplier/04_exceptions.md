# 拉格朗日乘數法的適用範圍 (When Does It Apply?)

[01_basic_use.md](01_basic_use.md)／[02_advanced_use.md](02_advanced_use.md) 的方程組是從 [03_proof.md](03_proof.md) 的前提推出來的。
前提一旦不成立，方法就會**多給**（把不是極值的點當成候選點）、**少給**（漏掉真正的極值點），甚至**亂給**（極值根本不存在也照樣解出點來）。
以下五種情況各舉一例，文末附總表。

---

## 1. 只是必要條件：解出來的點不一定是極值 (Necessary, Not Sufficient)

$\nabla f = \lambda\nabla g$ 只說「在這裡往切向走，$f$ 的一階變化為零」，就像單變數的 $f'=0$，也可能是反曲點或鞍點。

**例（反曲點）**：求 $f = x^3 + y$ 在 $y = 0$ 上的極值。

$$\begin{gather*}
\frac{\partial}{\partial x}\Big[x^3 + y - \lambda y\Big] &=& 3x^2 \\
\frac{\partial}{\partial y}\Big[x^3 + y - \lambda y\Big] &=& 1 - \lambda
\end{gather*}$$

令兩式為零得唯一候選點 $(0,0)$，但沿約束 $f = x^3$ 在兩側異號，它**不是**極值（這題根本沒有極值）。

**例（局部而非全域）**：[Q02](05_problems/Q02_cubic_on_ellipse.md) 的方程組會解出 $(0,\pm\sqrt{3})$，$f = 0$。它們是局部極值，但全域最大最小是 $\pm 4$，只有把所有候選點的 $f$ 值列出來比較才分得出來。

**對策**：列出所有候選點的 $f$ 值比較；需要判斷局部極值時，看約束切空間上的二階條件（bordered Hessian）。

---

## 2. 極值可能根本不存在 (Existence Is Not Guaranteed)

方法只負責回答「**如果**極值存在，它會在哪裡」，不負責證明存在。可行域無界（非緊緻）時，$f$ 可能一路往 $\pm\infty$ 跑。

**例**：[Q01](05_problems/Q01_quadratic_on_line.md) 求 $f = x^2 + 2y^2$ 在直線 $x+y=6$ 上的極值，方程組只解出一點 $(4,2)$，$f=24$。
但沿直線 $x = 6 - y$ 往外走，$f = (6-y)^2 + 2y^2 \to \infty$，所以**沒有最大值**，$(4,2)$ 只能是最小值。

**對策**：先確認可行域緊緻（有界閉集，連續函數必有最大最小），例如 [Q06](05_problems/Q06_hyperboloid_plane_distance.md) 要先證明交線是橢圓；
或者用凸性、$f\to\infty$ 之類的論證，判斷唯一的候選點是哪一種極值。

---

## 3. 邊界與不等式約束抓不到 (Boundaries and Inequalities)

方程組只描述**等式**約束**內部**的點。題目若另有 $x \ge 0$ 之類的不等式，極值可能卡在邊界上，這時 $\nabla f \neq \lambda \nabla g$ 也無妨。

**例**：兩點電荷 $q_1+q_2 = Q > 0$，$q_1, q_2 \ge 0$，求位能 $U \propto q_1 q_2$ 的極值。

$$\begin{gather*}
\frac{\partial}{\partial q_1}\Big[q_1q_2 - \lambda(q_1+q_2-Q)\Big] &=& q_2 - \lambda \\
\frac{\partial}{\partial q_2}\Big[q_1q_2 - \lambda(q_1+q_2-Q)\Big] &=& q_1 - \lambda
\end{gather*}$$

令兩式為零得 $q_1 = q_2 = Q/2$，這是**最大值** $U \propto Q^2/4$。**最小值** $U = 0$ 在端點 $(Q,0)$、$(0,Q)$，方程組完全看不到。
（若拿掉 $q_i \ge 0$，$q_1 q_2 = q_1(Q - q_1) \to -\infty$，連最小值都不存在，又回到第 2 點。）

**對策**：邊界另外代入比較；不等式約束系統化的處理方式是 KKT 條件 (Karush–Kuhn–Tucker)。

---

## 4. 違反 LICQ：約束梯度線性相依 (LICQ Violation)

證明的關鍵一步（[03_proof.md](03_proof.md)【已知 2】【已知 5】）需要約束面在極值點上光滑，也就是各 $\nabla g_n$ 線性獨立（單一約束時即 $\nabla g \neq \mathbf{0}$）。
這個條件不成立時，真正的極值點可能**無法**寫成 $\nabla f = \sum \lambda_n \nabla g_n$，方法就會漏掉它。

**例**：求 $f(x,y) = x$ 在下列兩條約束下的最小值。

### 假設與已知 (Assumptions & Preliminaries)

* **【定義 1】目標與約束 (Objective & Constraints)：** 一條三次曲線與 $x$ 軸，兩者只交於一點。

  (a) $$f(x,y) \overset{\text{def}}{=} x$$

  (b) $$g_1(x,y) \overset{\text{def}}{=} (x-1)^3 - y = 0$$

  (c) $$g_2(x,y) \overset{\text{def}}{=} y = 0$$

* **【已知 1】多約束 Lagrange 條件 (Lagrange Condition)：** 極值點若滿足 LICQ，必使 Lagrangian 對 $x, y$ 的偏導數為零。（見 [02_advanced_use.md](02_advanced_use.md)。）

  $$\mathcal{L} = f - \lambda_1 g_1 - \lambda_2 g_2$$

### solve

(a) 可行域：代入 (c) 到 (b)，只剩一個點，所以它就是最小值點。

$$\begin{gather*}
0 &\overset{\text{定義 1(b)(c)}}{=}& (x-1)^3 \\
x &=& 1
\end{gather*}$$

可行域 $= \{(1,0)\}$，最小值 $f = 1$。

(b) 檢查 LICQ：兩個梯度在 $(1,0)$ 互為反向，線性相依。

$$\begin{gather*}
\nabla g_1(1,0) &\overset{\text{定義 1(b)}}{=}& \big(3(x-1)^2,\ -1\big)\Big|_{(1,0)} \\
\nabla g_1(1,0) &=& (0,\ -1) \\
\nabla g_2(1,0) &\overset{\text{定義 1(c)}}{=}& (0,\ 1)
\end{gather*}$$

(c) 硬套方程組：在真正的極值點上得到矛盾。

$$\begin{gather*}
0 &\overset{\text{已知 1}}{=}& \frac{\partial \mathcal{L}}{\partial x}\bigg|_{(1,0)} \\
0 &\overset{\text{定義 1}}{=}& 1 - 3\lambda_1 (1-1)^2 \\
0 &=& 1
\end{gather*}$$

**結論**：極值點 $(1,0)$ 真實存在，但方程組在該點無解。原因是兩條約束在 $(1,0)$ 相切，$\nabla g_1, \nabla g_2$ 都只指向 $y$ 方向，而 $\nabla f = (1,0)$ 指向 $x$ 方向，怎麼組合都湊不出來。

**對策**：另外列出所有違反 LICQ 的可行點（解 $\nabla g_n$ 線性相依 ＋ 約束），把它們也當候選點比較。

---

## 5. 函數不可微 (Non-differentiable Points)

$\nabla f$、$\nabla g$ 不存在的點，方程組根本寫不出來，自然也不會出現在解裡。

**例**：求 $f(x,y) = |x| + |y|$ 在 $x + 2y = 2$ 上的最小值。
在任一象限內部 $\nabla f = (\pm 1, \pm 1)$，而 $\nabla g = (1, 2)$，兩者永遠不平行，所以方程組**無解**。
但真正的最小值 $f = 1$ 就在 $(0,1)$，剛好落在 $f$ 不可微的 $y$ 軸上。

**對策**：把不可微的點與可行域的交集單獨列為候選點。

---

## 總表 (Summary)

| 情況 | 症狀 | 對策 |
|---|---|---|
| 1. 只是必要條件 | 解出的點不是極值（鞍點、反曲點） | 比較所有候選點的 $f$ 值；或看二階條件 |
| 2. 極值不存在 | 可行域無界，某一側解不出或只解出一點 | 先證緊緻；或用凸性／趨勢判斷 |
| 3. 邊界、不等式 | 極值在端點上，方程組漏掉 | 邊界另外代入；KKT |
| 4. 違反 LICQ | 真正的極值點讓方程組無解（如 $1=0$） | 解出所有 $\nabla g_n$ 線性相依的可行點，一併比較 |
| 5. 不可微 | 梯度不存在，方程組寫不出來 | 不可微點另外列入候選 |

> 實務上的最終答案 = 比較以下三者的 $f$ 值：方程組的解、邊界／不可微點、違反 LICQ 的點。
