# Q15｜化學熱力學：吉布斯自由能最小化與化學平衡

> 應用題 ★★★★☆

## Question

在定溫 $T$ 與定壓 $P$ 的催化反應器中，兩種互為異構物的氣態分子 A 與 B 進行可逆反應 $\text{A} \rightleftharpoons \text{B}$。
設反應器內 A 與 B 的莫耳數分別為 $n_1 > 0$ 與 $n_2 > 0$，系統的無因次化吉布斯自由能（Gibbs Free Energy）為：

$$G(n_1, n_2) = n_1 \ln\left(\frac{n_1}{n_1 + n_2}\right) + n_2 \ln\left(\frac{n_2}{n_1 + n_2}\right) + \mu_1^\circ n_1 + \mu_2^\circ n_2$$

已知標準化學勢差為 $\mu_2^\circ - \mu_1^\circ = \ln 2$，且原子質量守恆要求總莫耳數滿足 $n_1 + n_2 = 3\ \text{mol}$。利用拉格朗日乘數法求化學平衡時的莫耳數 $(n_1, n_2)$。

（提示：先驗證 $\frac{\partial}{\partial n_1}\left[n_1 \ln\frac{n_1}{n_1+n_2} + n_2 \ln\frac{n_2}{n_1+n_2}\right] = \ln\frac{n_1}{n_1+n_2}$。）

## Question - Answer

### 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】[單約束 Lagrange 條件 (Lagrange Condition)](../01_basic_use.md)：** 約束上的極值點，必使 Lagrangian 對所有變數的偏導數同時為零。

  $$\mathcal{L} = G - \lambda(g - 3)$$

* **【定義 1】目標與約束 (Objective & Constraint)：** 前兩項是混合熵的貢獻（永遠 $\le 0$，偏好混合），後兩項是各物種本身的能量。

  (a) $$G(n_1,n_2) \overset{\text{def}}{=} n_1 \ln\frac{n_1}{N} + n_2 \ln\frac{n_2}{N} + \mu_1^\circ n_1 + \mu_2^\circ n_2$$

  (b) $$N \overset{\text{def}}{=} n_1 + n_2$$

  (c) $$g(n_1,n_2) \overset{\text{def}}{=} n_1 + n_2 = 3\ \text{mol}$$

  * $n_1, n_2$ : A、B 莫耳數 (Amount of substance) $[\text{mol}]$
  * $\mu_1^\circ, \mu_2^\circ$ : 無因次標準化學勢 (Standard chemical potential) $[\text{無單位}]$，$\mu_2^\circ - \mu_1^\circ = \ln 2$
  * $G$ : 無因次吉布斯自由能 (Gibbs free energy, in units of $RT$) $[\text{mol}]$

* **【推導 1】混合項的偏導數 (Derivative of the Mixing Term)：** 驗證提示。對 $n_1$ 微分時 $N$ 也會變，但多出來的項剛好互相抵消。

  $$\begin{gather*}
  \frac{\partial}{\partial n_1}\Big[n_1 \ln\frac{n_1}{N} + n_2 \ln\frac{n_2}{N}\Big] &\overset{\text{定義 1(b)}}{=}& \ln\frac{n_1}{N} + n_1\Big(\frac{1}{n_1} - \frac{1}{N}\Big) - \frac{n_2}{N} \\
  &=& \ln\frac{n_1}{N} + 1 - \frac{n_1 + n_2}{N} \\
  &\overset{\text{定義 1(b)}}{=}& \ln\frac{n_1}{N}
  \end{gather*}$$

  同理對 $n_2$ 微分得 $\ln\frac{n_2}{N}$。

### solve

(a) 由【已知 1】【定義 1】【推導 1】寫出方程組：

$$\left\{\begin{array}{rcl}
\ln\dfrac{n_1}{N} + \mu_1^\circ &=& \lambda \\[8pt]
\ln\dfrac{n_2}{N} + \mu_2^\circ &=& \lambda \\[8pt]
n_1 + n_2 &=& 3
\end{array}\right.$$

(b) 兩式相減消去 $\lambda$：

$$\begin{gather*}
\ln\frac{n_2}{n_1} &\overset{\text{(a)}}{=}& \mu_1^\circ - \mu_2^\circ \\
\ln\frac{n_2}{n_1} &\overset{\text{定義 1}}{=}& -\ln 2 \\
\frac{n_2}{n_1} &=& \frac{1}{2}
\end{gather*}$$

(c) 代入總量：

$$\begin{gather*}
3 &\overset{\text{(a),(b)}}{=}& n_1 + \frac{n_1}{2} \\
n_1 &=& 2\ \text{mol} \\
n_2 &=& 1\ \text{mol}
\end{gather*}$$

(d) 判定：$x \ln x$ 是凸函數，$G$ 在線段 $n_1 + n_2 = 3$ 上是凸的；端點處 $\frac{\partial G}{\partial n_i} \to -\infty$，所以最小值在內部，唯一候選點就是全域最小值。

**結論**：平衡時 $n_1 = 2\ \text{mol}$、$n_2 = 1\ \text{mol}$。(a) 說兩物種的**化學勢相等** $\mu_i = \mu_i^\circ + \ln x_i = \lambda$，這就是化學平衡條件；(b) 則是平衡常數 $K = \frac{n_2}{n_1} = e^{-(\mu_2^\circ - \mu_1^\circ)} = \frac{1}{2}$。B 的標準能量較高，所以平衡偏向 A，但混合熵讓 B 不會完全消失。
