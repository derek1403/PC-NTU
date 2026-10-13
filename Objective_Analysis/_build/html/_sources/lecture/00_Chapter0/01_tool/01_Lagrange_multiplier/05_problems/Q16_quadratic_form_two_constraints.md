# Q16｜大氣／物理壓軸：球面＋平面上的二次型極值

> 應用題 ★★★★★

## Question

考慮一個理想化的三維風場 $\mathbf{V}=(u,v,w)$。假設系統具有固定的總動能：

$$u^2+v^2+w^2=2K$$

同時，某個大尺度環境條件要求風場滿足

$$u+v+w=0$$

現在定義一個代表「對某一局地環流結構有效驅動程度」的量：

$$F = 4uv+3vw-2uw$$

請在上述兩個限制條件下，求 $F$ 的：

1. 所有可能極值點；
2. 最大值；
3. 最小值；
4. 對應的 $(u,v,w)$。

要求使用 **Lagrange multipliers** 完整求解，不可以直接猜對稱解。

## Question - Answer

### 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】[多約束 Lagrange 條件 (Lagrange Condition)](../02_advanced_use.md)：** 每條約束配一個乘數，極值點必使 Lagrangian 對所有變數的偏導數同時為零。

  $$\mathcal{L} = F - \lambda(g_1 - 2K) - \mu\, g_2$$

* **【已知 2】二次齊次函數的 Euler 定理 (Euler's Theorem for Homogeneous Functions)：** 二次齊次函數與其梯度的內積等於函數值的兩倍。

  $$\mathbf{x}\cdot\nabla F = 2F$$

* **【定義 1】目標與約束 (Objective & Constraints)：** 可行域是球面與過球心平面的交圓（有界閉集）。

  (a) $$F(u,v,w) \overset{\text{def}}{=} 4uv + 3vw - 2uw$$

  (b) $$g_1(u,v,w) \overset{\text{def}}{=} u^2 + v^2 + w^2 = 2K$$

  (c) $$g_2(u,v,w) \overset{\text{def}}{=} u + v + w = 0$$

  * $u, v, w$ : 風場分量 (Wind components) $[\text{m}\cdot\text{s}^{-1}]$
  * $K$ : 單位質量動能 (Kinetic energy per unit mass) $[\text{m}^2\cdot\text{s}^{-2}]$

* **【假設 1】LICQ：** $\nabla g_1 = 2(u,v,w)$ 與 $\nabla g_2 = (1,1,1)$ 平行需要 $u = v = w$，代入平面得全為零，不在球面上。所以 LICQ 處處成立。

### solve

(a) 由【已知 1】【定義 1】寫出方程組：

$$\left\{\begin{array}{rcl}
4v - 2w &=& 2\lambda u + \mu \\[4pt]
4u + 3w &=& 2\lambda v + \mu \\[4pt]
3v - 2u &=& 2\lambda w + \mu \\[4pt]
u^2 + v^2 + w^2 &=& 2K \\[4pt]
u + v + w &=& 0
\end{array}\right.$$

(b) 候選點上 $F$ 與 $\lambda$ 的關係：前三式分別乘 $u, v, w$ 相加。

$$\begin{gather*}
2F &\overset{\text{已知 2}}{=}& u(4v - 2w) + v(4u + 3w) + w(3v - 2u) \\
2F &\overset{\text{(a)}}{=}& 2\lambda(u^2 + v^2 + w^2) + \mu(u + v + w) \\
2F &\overset{\text{定義 1(b)(c)}}{=}& 4K\lambda \\
F &=& 2K\lambda
\end{gather*}$$

(c) 前三式直接相加，解出 $\mu$，再用 $w = -u - v$：

$$\begin{gather*}
2u + 7v + w &\overset{\text{(a),定義 1(c)}}{=}& 3\mu \\
\mu &\overset{\text{定義 1(c)}}{=}& \frac{u + 6v}{3}
\end{gather*}$$

(d) 把 $w = -u - v$ 與 $\mu$ 代入前兩式（乘 3 去分母）：

$$\begin{gather*}
6u + 18v &\overset{\text{(a),(c)}}{=}& 6\lambda u + u + 6v \\
0 &=& (5 - 6\lambda)u + 12v
\end{gather*}$$

$$\begin{gather*}
3u - 9v &\overset{\text{(a),(c)}}{=}& 6\lambda v + u + 6v \\
0 &=& 2u - (15 + 6\lambda)v
\end{gather*}$$

(e) $(u,v) \neq (0,0)$（否則 $w = 0$，違反球面），所以 (d) 的係數行列式為零：

$$\begin{gather*}
0 &\overset{\text{(d)}}{=}& -(5 - 6\lambda)(15 + 6\lambda) - 24 \\
0 &=& 36\lambda^2 + 60\lambda - 99 \\
0 &=& 12\lambda^2 + 20\lambda - 33 \\
\lambda &=& \frac{-20 \pm \sqrt{400 + 1584}}{24} \\
\lambda &=& \frac{-5 \pm 2\sqrt{31}}{6}
\end{gather*}$$

(f) 極值：

$$\begin{gather*}
F &\overset{\text{(b),(e)}}{=}& \frac{-5 \pm 2\sqrt{31}}{3}\,K
\end{gather*}$$

(g) 對應的點：由 (d) 第二式 $u = \frac{15 + 6\lambda}{2}\,v$，再用 $w = -u - v$ 與球面正規化。

* $\lambda_+ = \frac{-5 + 2\sqrt{31}}{6}$：$15 + 6\lambda_+ = 10 + 2\sqrt{31}$

  $$(u,v,w) = \pm\sqrt{\frac{2K}{124 + 22\sqrt{31}}}\ \Big(5 + \sqrt{31},\ 1,\ -(6 + \sqrt{31})\Big)$$

* $\lambda_- = \frac{-5 - 2\sqrt{31}}{6}$：$15 + 6\lambda_- = 10 - 2\sqrt{31}$

  $$(u,v,w) = \pm\sqrt{\frac{2K}{124 - 22\sqrt{31}}}\ \Big(5 - \sqrt{31},\ 1,\ \sqrt{31} - 6\Big)$$

（正規化常數：$(5 \pm \sqrt{31})^2 + 1 + (6 \pm \sqrt{31})^2 = 124 \pm 22\sqrt{31}$。）

**結論**：交圓是有界閉集且【假設 1】成立，極值點只有這四個。

1. 極值點：上面 (g) 的四個點
2. $F_{\max} = \dfrac{-5 + 2\sqrt{31}}{3}K \approx 2.05K$
3. $F_{\min} = \dfrac{-5 - 2\sqrt{31}}{3}K \approx -5.38K$
4. 最大值對應 $\lambda_+$ 那一組點，最小值對應 $\lambda_-$ 那一組點

本質上是「把對稱矩陣限制在平面 $u+v+w=0$ 上求特徵值」：$2\lambda$ 是限制後 $2\times 2$ 矩陣的特徵值，與 [Q14](Q14_inertia_principal_axes.md) 同一個結構，只是多一條平面約束。
