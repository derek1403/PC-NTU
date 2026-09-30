# Q07｜材料科學：固定體積下表面積最小的長方體

> 應用題 ★★★☆☆

## Question

某種材料製成長方體，三個邊長分別為 $x,\ y,\ z$。材料體積固定為

$$xyz=V_0$$

其表面積為

$$A=2(xy+xz+yz)$$

請利用 Lagrange multiplier 求使表面積最小的 $x,y,z$，並說明結果對材料製造有什麼幾何意義。

## Question - Answer

### 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】[單約束 Lagrange 條件 (Lagrange Condition)](../01_basic_use.md)：** 約束上的極值點，必使 Lagrangian 對所有變數的偏導數同時為零；解出的只是候選點。

  $$\mathcal{L} = A - \lambda(g - V_0)$$

* **【定義 1】目標與約束 (Objective & Constraint)：** 表面積代表用料，體積代表容量。

  (a) $$A(x,y,z) \overset{\text{def}}{=} 2(xy + xz + yz)$$

  (b) $$g(x,y,z) \overset{\text{def}}{=} xyz = V_0$$

  * $x, y, z$ : 邊長 (Side lengths) $[\text{m}]$，皆 $> 0$
  * $V_0$ : 固定體積 (Fixed volume) $[\text{m}^3]$
  * $A$ : 表面積 (Surface area) $[\text{m}^2]$

### solve

(a) 由【已知 1】【定義 1】寫出方程組：

$$\left\{\begin{array}{rcl}
2(y + z) &=& \lambda yz \\[4pt]
2(x + z) &=& \lambda xz \\[4pt]
2(x + y) &=& \lambda xy \\[4pt]
xyz &=& V_0
\end{array}\right.$$

(b) 三式分別乘上 $x, y, z$，右邊都變成 $\lambda V_0$：

$$\begin{gather*}
2(xy + xz) &\overset{\text{(a)}}{=}& \lambda V_0 \\
2(xy + yz) &\overset{\text{(a)}}{=}& \lambda V_0 \\
2(xz + yz) &\overset{\text{(a)}}{=}& \lambda V_0
\end{gather*}$$

(c) 前兩式相減（其餘同理）：

$$\begin{gather*}
2(xz - yz) &\overset{\text{(b)}}{=}& 0 \\
2z(x - y) &=& 0 \\
x &=& y
\end{gather*}$$

（$z > 0$ 所以可以除。）同理 $y = z$。

(d) 代入約束：

$$\begin{gather*}
x^3 &\overset{\text{定義 1(b),(c)}}{=}& V_0 \\
x &=& V_0^{1/3} \\
A &\overset{\text{定義 1(a)}}{=}& 6 V_0^{2/3}
\end{gather*}$$

(e) 判定：任何一邊 $\to 0$ 時另外兩邊的乘積 $\to \infty$，$A \ge 2yz \to \infty$；任何一邊 $\to \infty$ 時 $A \ge 2x(y+z) \ge 4\sqrt{x V_0} \to \infty$。$A$ 在邊界都趨於無窮，唯一的候選點就是全域最小值。

**結論**：$x = y = z = V_0^{1/3}$，最小表面積 $A = 6V_0^{2/3}$。**正方體**是裝同樣體積最省料的長方體：任何拉長或壓扁都會增加表面積，也就增加材料成本與散熱面。
