# Q11｜流體力學：固定動能下使輸送量最大的風場

> 應用題 ★★★☆☆

## Question

考慮三個彼此獨立的風場分量

$$u,\quad v,\quad w$$

假設總動能固定：

$$\frac12(u^2+v^2+w^2)=K$$

同時考慮一個代表「沿特定方向輸送能力」的量

$$F=2u+3v+6w$$

在固定總動能 $K$ 的條件下，求使 $F$ 最大的風場 $(u,v,w)$，並將結果用 $K$ 表示。

## Question - Answer

### 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】[單約束 Lagrange 條件 (Lagrange Condition)](../01_basic_use.md)：** 約束上的極值點，必使 Lagrangian 對所有變數的偏導數同時為零。

  $$\mathcal{L} = F - \lambda(g - K)$$

* **【定義 1】目標與約束 (Objective & Constraint)：** $F$ 是風向量在固定方向 $(2,3,6)$ 上的投影（乘上該方向長度 $7$）；約束把風向量限制在半徑 $\sqrt{2K}$ 的球面上。

  (a) $$F(u,v,w) \overset{\text{def}}{=} 2u + 3v + 6w$$

  (b) $$g(u,v,w) \overset{\text{def}}{=} \frac{1}{2}(u^2 + v^2 + w^2) = K$$

  * $u, v, w$ : 風場分量 (Wind components) $[\text{m}\cdot\text{s}^{-1}]$
  * $K$ : 單位質量動能 (Kinetic energy per unit mass) $[\text{m}^2\cdot\text{s}^{-2}]$
  * $F$ : 輸送指標 (Transport index) $[\text{m}\cdot\text{s}^{-1}]$

### solve

(a) 由【已知 1】【定義 1】寫出方程組：

$$\left\{\begin{array}{rcl}
2 &=& \lambda u \\[4pt]
3 &=& \lambda v \\[4pt]
6 &=& \lambda w \\[4pt]
\frac{1}{2}(u^2 + v^2 + w^2) &=& K
\end{array}\right.$$

(b) 風向量必平行於 $(2,3,6)$：

$$\begin{gather*}
(u,v,w) &\overset{\text{(a)}}{=}& \frac{1}{\lambda}(2,\ 3,\ 6)
\end{gather*}$$

(c) 代入約束解 $\lambda$：

$$\begin{gather*}
K &\overset{\text{(a),(b)}}{=}& \frac{1}{2}\cdot\frac{4 + 9 + 36}{\lambda^2} \\
\lambda^2 &=& \frac{49}{2K} \\
\lambda &=& \pm\frac{7}{\sqrt{2K}}
\end{gather*}$$

(d) 函數值：

$$\begin{gather*}
F &\overset{\text{定義 1(a),(b)}}{=}& \frac{4 + 9 + 36}{\lambda} \\
&\overset{\text{(c)}}{=}& \pm 7\sqrt{2K}
\end{gather*}$$

(e) 判定：球面是有界閉集，$F$ 的最大、最小值必存在，只能是這兩個候選點。

**結論**：

$$(u,v,w) = \frac{\sqrt{2K}}{7}(2,\ 3,\ 6),\qquad F_{\max} = 7\sqrt{2K}$$

風速大小 $\sqrt{2K}$ 由動能固定，能選的只有方向；**把整個風向量對準目標方向**時輸送最大（反向時 $F_{\min} = -7\sqrt{2K}$）。這正是 Cauchy–Schwarz 不等式 $|\mathbf{a}\cdot\mathbf{v}| \le |\mathbf{a}||\mathbf{v}|$ 的等號條件。
