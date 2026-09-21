# Chaos and Predictability 2026 - homework 1

```
name:葉品辰
ID:r14229017
date: 2026.09.21
```

## Exercise 1

Prove that the error growth of the differential equation

$$\frac{dx}{dt} = f(x)$$

is independent of the current state, i.e., $\delta x = \delta x(t)$, if and only if $f(x)$ is linear.

## Exercise 1 - Answer

### 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 一階自治常微分方程 (First-order autonomous ODE) ：** 題目給定的控制方程式，其右端只依賴當前狀態 $x$，不顯含時間 $t$。

  $$\frac{dx}{dt} = f(x)$$

  * $x$ : 系統的當前狀態 (Current state of the system) [無單位]
  * $t$ : 時間 (Time) $[\text{s}]$
  * $f$ : 控制方程式右端的傾向函數 (Tendency function) $[\text{s}^{-1}]$

* **【假設 1】 $f$ 連續可微 (Continuously differentiable, $f \in C^{1}$)：** 必要性方向（(b) 小節）需要對 $x$ 取一次導數，這是全題唯一用到的正則性前提，故先於此攤開。

  $$f'(x) = \frac{df}{dx} \quad \text{對所有 } x \text{ 存在且連續}$$

  * $f'$ : 傾向函數對狀態的一階導數 (First derivative of the tendency function) $[\text{s}^{-1}]$

* **【定義 1】 線性 (Linear)：** 本題所謂「$f(x)$ 為線性」，指 $f$ 是 $x$ 的一次函數，即存在與 $x$ 無關的常數 $A$、$b$ 使得下式成立。

  $$f(x) \overset{\text{def}}{=} Ax + b$$

  註：嚴格線性代數意義下，$b \neq 0$ 時 $f$ 應稱為仿射 (affine)，$b = 0$ 才是齊次線性 (homogeneous linear)。本題「誤差成長與當前狀態無關」所對應的恰是上式這一類一次函數（常數項 $b$ 在相減時會自動消去），故以下一律以上式作為「線性」的定義。

  * $A$ : 一次項係數，即誤差的成長率 (Linear coefficient / error growth rate) $[\text{s}^{-1}]$
  * $b$ : 常數項 (Constant term) $[\text{s}^{-1}]$

* **【定義 2】 誤差 (Error / perturbation)：** 取一條與基準軌跡 $x$ 由同一組方程支配的孿生軌跡 $\tilde{x}$，兩者之差即為誤差。

  * (a) 誤差的定義：

  $$\delta x \overset{\text{def}}{=} \tilde{x} - x$$

  * (b) 孿生軌跡同樣受【已知 1】支配，故其傾向為：

  $$\begin{gather*}
  \frac{d\tilde{x}}{dt} &\overset{\text{已知 1}}{=}& f(\tilde{x}) \\
  &\overset{\text{定義 2(a)}}{=}& f(x + \delta x)
  \end{gather*}$$

  * $\tilde{x}$ : 孿生（擾動）軌跡的狀態 (State of the twin / perturbed trajectory) [無單位]
  * $\delta x$ : 誤差，即兩條軌跡的狀態之差 (Error between the two trajectories) [無單位]

* **【定義 3】 誤差成長與當前狀態無關 (Independent of the current state)：** 題目所謂 $\delta x = \delta x(t)$，意指誤差的演化方程完全不含基準狀態 $x$，因此誤差只由初始誤差與時間決定。

  * (a) 誤差傾向對當前狀態的偏導數為零：

  $$\frac{\partial}{\partial x}\left[\frac{d\,\delta x}{dt}\right] = 0$$

  * (b) 等價敘述（其一）：誤差的傾向只由誤差本身決定：

  $$\frac{d\,\delta x}{dt} = g(\delta x)$$

  * (c) 等價敘述（其二）：故其解只是時間的函數，即題目要的敘述：

  $$\delta x = \delta x(t)$$

  * $g$ : 只依賴誤差、不依賴當前狀態的傾向函數 (Error-only tendency function) $[\text{s}^{-1}]$

* **【推導 1】 誤差演化方程通式 (General error evolution equation)：** 把孿生軌跡與基準軌跡的傾向相減，得到不依賴任何額外條件的誤差演化方程；這是 (a)(b) 兩個方向共同的起手式。

  $$\begin{gather*}
  \frac{d\,\delta x}{dt} &\overset{\text{定義 2(a)}}{=}& \frac{d}{dt}\left[\tilde{x} - x\right] \\
  &=& \frac{d\tilde{x}}{dt} - \frac{dx}{dt} \\
  &\overset{\text{定義 2(b),已知 1}}{=}& f(x + \delta x) - f(x)
  \end{gather*}$$

  * $\delta x$ : 誤差，即兩條軌跡的狀態之差 (Error between the two trajectories) [無單位]
  * $\tilde{x}$ : 孿生（擾動）軌跡的狀態 (State of the twin / perturbed trajectory) [無單位]
  * $f$ : 控制方程式右端的傾向函數 (Tendency function) $[\text{s}^{-1}]$

### (a) proof 充分性 (Sufficiency)：若 $f$ 為線性，則誤差成長與當前狀態無關

由【推導 1】的通式起手，代入【定義 1】的線性形式。

$$\begin{gather*}
\frac{d\,\delta x}{dt} &\overset{\text{推導 1}}{=}& f(x + \delta x) - f(x) \\
&\overset{\text{定義 1}}{=}& \left[A(x + \delta x) + b\right] - \left[Ax + b\right] \\
&=& Ax + A\,\delta x + b - Ax - b \\
&=& A\,\delta x
\end{gather*}$$

上式右端只含 $\delta x$ 而不含 $x$，故誤差傾向對當前狀態的偏導數為零。

$$\begin{gather*}
\frac{\partial}{\partial x}\left[\frac{d\,\delta x}{dt}\right] &\overset{\text{Q1(a)}}{=}& \frac{\partial}{\partial x}\left[A\,\delta x\right] \\
&=& 0
\end{gather*}$$

此即【定義 3(a)】，等價於【定義 3(c)】的 $\delta x = \delta x(t)$。故**充分性**成立。

### (b) proof 必要性 (Necessity)：若誤差成長與當前狀態無關，則 $f$ 為線性

由【定義 3(a)】起手，代入【推導 1】的通式，並依【假設 1】對 $x$ 微分。

$$\begin{gather*}
0 &\overset{\text{定義 3(a)}}{=}& \frac{\partial}{\partial x}\left[\frac{d\,\delta x}{dt}\right] \\
0 &\overset{\text{推導 1}}{=}& \frac{\partial}{\partial x}\left[f(x + \delta x) - f(x)\right] \\
0 &\overset{\text{假設 1}}{=}& f'(x + \delta x) - f'(x) \\
f'(x + \delta x) &=& f'(x)
\end{gather*}$$

上式對任意基準狀態 $x$ 與任意誤差 $\delta x$ 皆成立，即 $f'$ 在整個定義域上取同一個值，故 $f'$ 為常數；令此常數為 $A$，積分回去即得 $f$ 的一般形式。

$$\begin{gather*}
f'(x) &\overset{\text{let}}{=}& A \\
f(x) &=& \int A \, dx \\
f(x) &=& Ax + b
\end{gather*}$$

其中積分常數即為 $b$。此形式恰為【定義 1】所定義的線性函數，故**必要性**成立。

### (c) conclusion 合併為若且唯若 (If and only if)

前兩個小節各自獨立地證完一個方向：

* 由 (a) 得**充分性**：$f$ 為線性 $\Longrightarrow$ 誤差成長與當前狀態無關。
* 由 (b) 得**必要性**：誤差成長與當前狀態無關 $\Longrightarrow$ $f$ 為線性。

兩個方向皆已成立，**此時**才可將兩者合併，寫成題目所要求的若且唯若。

$$\delta x = \delta x(t) \iff f(x) = Ax + b$$

$\blacksquare$

## Exercise 2

Consider the Lorenz '63 model:

$$\begin{gather*}
\frac{dx}{dt} &=& \sigma(y - x), \\
\frac{dy}{dt} &=& x(\rho - z) - y, \\
\frac{dz}{dt} &=& xy - \beta z.
\end{gather*}$$

Assume that $\sigma = 10$, $\beta = \frac{8}{3}$, and $\rho = 24.74$.

* (a) Derive the linearized error evolution matrix $\mathbf{A}$ such that

  $$\frac{d}{dt}(\delta \mathbf{x}) = \mathbf{A} \delta \mathbf{x}.$$

* (b) Compute the eigenvalues of $\mathbf{A}$ (using python). What is the physical significance of the eigenvalues of the linear operator $\mathbf{A}$ in this context?

* (c) Compute the determinant of $\mathbf{A}$ (using python). What is the meaning of $\det(\mathbf{A})$ here?

## Exercise 2 - Answer

### 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 Lorenz '63 模式 (Lorenz '63 model)：** 題目給定的三維控制方程組；為求後續推導清楚，以下一律寫成矩陣（向量）形式，不再使用大括號聯立式。

  $$\frac{d}{dt}\begin{bmatrix} x \\ y \\ z \end{bmatrix} = \begin{bmatrix} \sigma(y - x) \\ x(\rho - z) - y \\ xy - \beta z \end{bmatrix}$$

  * $x$ : 對流翻轉的強度 (Intensity of convective overturning) [無單位]
  * $y$ : 上升流與下沉流之間的溫度差 (Temperature difference between ascending and descending currents) [無單位]
  * $z$ : 垂直溫度剖面偏離線性的程度 (Distortion of the vertical temperature profile) [無單位]
  * $t$ : 無因次時間 (Nondimensional time) [無單位]
  * $\sigma$ : 普朗特數 (Prandtl number) [無單位]
  * $\rho$ : 正規化瑞利數 (Normalized Rayleigh number) [無單位]
  * $\beta$ : 對流胞的幾何比例因子 (Geometric factor of the convection cell) [無單位]

* **【已知 2】 特徵值問題與線性系統通解 (Eigenvalue problem and general solution)：** 對任一常數方陣，其特徵值與特徵向量決定了線性系統解的結構；(b) 小節的物理意義由此卡片支撐。

  * (a) 特徵值與特徵向量的定義式：

  $$\mathbf{M}\mathbf{v}_i = \lambda_i \mathbf{v}_i$$

  * (b) 當 $\mathbf{M}$ 的特徵向量張滿整個空間時，線性系統的通解為各特徵方向上指數解的疊加：

  $$\delta\mathbf{x}(t) = \sum_{i=1}^{3} c_i \mathbf{v}_i e^{\lambda_i t}$$

  * $\mathbf{M}$ : 任一常數方陣 (An arbitrary constant square matrix) [無單位]
  * $\lambda_i$ : 第 $i$ 個特徵值，即該特徵方向上的指數成長率 (The $i$-th eigenvalue / growth rate) [無單位]，為無因次時間的倒數
  * $\mathbf{v}_i$ : 第 $i$ 個特徵向量 (The $i$-th eigenvector) [無單位]
  * $c_i$ : 由初始誤差決定的展開係數 (Expansion coefficient determined by the initial error) [無單位]

* **【已知 3】 行列式與跡 (Determinant and trace)：** 兩者都由特徵值決定，但回答的是**不同**的問題；(c) 小節會分別用到，不可混為一談。

  * (a) 行列式等於各特徵值之積，代表線性算子把空間中一個體積元縮放的倍率：

  $$\det(\mathbf{M}) = \lambda_1 \lambda_2 \lambda_3$$

  * (b) 跡等於各特徵值之和，亦等於原向量場的散度，代表相空間體積的**瞬時**收縮率：

  $$\begin{gather*}
  \mathrm{tr}(\mathbf{M}) &=& \lambda_1 + \lambda_2 + \lambda_3 \\
  &=& \nabla \cdot \mathbf{f}
  \end{gather*}$$

  * (c) 由 (b) 對時間積分，得體積元隨時間的演變：

  $$V(t) = V(0)\, e^{\mathrm{tr}(\mathbf{M})\, t}$$

  * $\mathbf{f}$ : 【已知 1】右端的向量場 (Vector field on the right-hand side of 已知 1) [無單位]
  * $V$ : 相空間（誤差空間）中的體積元 (Volume element in phase / error space) [無單位]

* **【假設 1】 題目給定參數 (Given parameters)：** 題目指定的三個無因次參數值。

  * (a) 普朗特數：

  $$\sigma = 10$$

  * (b) 對流胞的幾何比例因子：

  $$\beta = \frac{8}{3}$$

  * (c) 正規化瑞利數：

  $$\rho = 24.74$$

* **【假設 2】 孿生軌跡 (Twin trajectory)：** 擾動後的狀態 $(x + \delta x,\, y + \delta y,\, z + \delta z)$ 與基準軌跡由**同一組**方程支配，即同樣滿足【已知 1】。

  $$\frac{d}{dt}\begin{bmatrix} x + \delta x \\ y + \delta y \\ z + \delta z \end{bmatrix} = \begin{bmatrix} \sigma\left[(y + \delta y) - (x + \delta x)\right] \\ (x + \delta x)\left[\rho - (z + \delta z)\right] - (y + \delta y) \\ (x + \delta x)(y + \delta y) - \beta(z + \delta z) \end{bmatrix}$$

* **【假設 3】 小擾動線性化 (Small perturbation / tangent linear approximation)：** 誤差遠小於狀態變數本身的特徵尺度，故誤差的二次項相對於一次項可捨棄。

  * (a) 誤差的量級前提（$x, y, z$ 為無因次量，其特徵尺度為 $O(1)$）：

  $$\lvert \delta x \rvert,\ \lvert \delta y \rvert,\ \lvert \delta z \rvert \ll 1$$

  * (b) 故 $\delta y$ 的方程中，二次項相對於一次項可捨棄：

  $$\begin{gather*}
  \lvert \delta z \rvert &\overset{\text{假設 3(a)}}{\ll}& 1 \\
  \lvert \delta x \rvert \lvert \delta z \rvert &\ll& \lvert \delta x \rvert \\
  \lvert \delta x \, \delta z \rvert &\ll& \lvert \delta x \rvert
  \end{gather*}$$

  * (c) 同理，$\delta z$ 的方程中，二次項相對於一次項可捨棄：

  $$\begin{gather*}
  \lvert \delta y \rvert &\overset{\text{假設 3(a)}}{\ll}& 1 \\
  \lvert \delta x \rvert \lvert \delta y \rvert &\ll& \lvert \delta x \rvert \\
  \lvert \delta x \, \delta y \rvert &\ll& \lvert \delta x \rvert
  \end{gather*}$$

* **【假設 4】 評估的基準狀態點 (Reference state for evaluation)：** 下文 (a) 將顯示 $\mathbf{A}$ 的元素依賴當前狀態，故求數值前必須先指定一個基準點；(b)(c) 兩小節一律取原點。

  $$(x,\ y,\ z) = (0,\ 0,\ 0)$$

* **【定義 1】 誤差向量 (Error vector)：** 把三個分量的誤差收束成一個向量。

  $$\delta\mathbf{x} \overset{\text{def}}{=} \begin{bmatrix} \delta x \\ \delta y \\ \delta z \end{bmatrix}$$

  * $\delta x$ : $x$ 分量的誤差 (Error in the $x$ component) [無單位]
  * $\delta y$ : $y$ 分量的誤差 (Error in the $y$ component) [無單位]
  * $\delta z$ : $z$ 分量的誤差 (Error in the $z$ component) [無單位]

* **【定義 2】 線性化誤差演化矩陣 (Linearized error evolution matrix)：** 題目所要求的 $\mathbf{A}$，定義為使誤差演化寫成線性形式的那個矩陣；其具體元素留待 (a) 小節推導。

  $$\frac{d}{dt}\left[\delta\mathbf{x}\right] \overset{\text{def}}{=} \mathbf{A}\,\delta\mathbf{x}$$

  * $\mathbf{A}$ : 線性化誤差演化矩陣，即【已知 1】向量場的 Jacobian 矩陣 (Linearized error evolution matrix / Jacobian matrix) [無單位]

### (a) derive 線性化誤差演化矩陣 $\mathbf{A}$

把【假設 2】的孿生軌跡方程逐分量減去【已知 1】的基準軌跡方程，展開後依【假設 3】捨去二次項，再把一次項提成矩陣乘向量。

$$\begin{gather*}
\frac{d}{dt}\left[\delta\mathbf{x}\right] &\overset{\text{定義 1}}{=}& \frac{d}{dt}\begin{bmatrix} \delta x \\ \delta y \\ \delta z \end{bmatrix} \\
\frac{d}{dt}\left[\delta\mathbf{x}\right] &\overset{\text{假設 2,已知 1}}{=}& \begin{bmatrix} \sigma\left[(y + \delta y) - (x + \delta x)\right] - \sigma(y - x) \\ (x + \delta x)\left[\rho - (z + \delta z)\right] - (y + \delta y) - \left[x(\rho - z) - y\right] \\ (x + \delta x)(y + \delta y) - \beta(z + \delta z) - \left[xy - \beta z\right] \end{bmatrix} \\
\frac{d}{dt}\left[\delta\mathbf{x}\right] &=& \begin{bmatrix} \sigma(\delta y - \delta x) \\ \rho\,\delta x - z\,\delta x - x\,\delta z - \delta y \\ y\,\delta x + x\,\delta y - \beta\,\delta z \end{bmatrix} + \begin{bmatrix} 0 \\ -\delta x\,\delta z \\ \delta x\,\delta y \end{bmatrix} \\
\frac{d}{dt}\left[\delta\mathbf{x}\right] &\overset{\text{假設 3(b)(c)}}{\approx}& \begin{bmatrix} -\sigma\,\delta x + \sigma\,\delta y \\ (\rho - z)\,\delta x - \delta y - x\,\delta z \\ y\,\delta x + x\,\delta y - \beta\,\delta z \end{bmatrix} \\
\frac{d}{dt}\left[\delta\mathbf{x}\right] &=& \begin{bmatrix} -\sigma & \sigma & 0 \\ \rho - z & -1 & -x \\ y & x & -\beta \end{bmatrix} \begin{bmatrix} \delta x \\ \delta y \\ \delta z \end{bmatrix} \\
\frac{d}{dt}\left[\delta\mathbf{x}\right] &\overset{\text{定義 1}}{=}& \begin{bmatrix} -\sigma & \sigma & 0 \\ \rho - z & -1 & -x \\ y & x & -\beta \end{bmatrix} \delta\mathbf{x}
\end{gather*}$$

與【定義 2】逐項對照，即得題目所求的線性化誤差演化矩陣。

$$\mathbf{A} = \begin{bmatrix} -\sigma & \sigma & 0 \\ \rho - z & -1 & -x \\ y & x & -\beta \end{bmatrix}$$

注意 $\mathbf{A} = \mathbf{A}(x, y, z)$ 的第二、三列含有當前狀態 $x, y, z$，故 $\mathbf{A}$ 並非常數矩陣，而是隨基準軌跡所在的位置改變。這正是 Exercise 1 的反面實例：Lorenz 模式的向量場含有 $xz$、$xy$ 等非線性項，不滿足 Exercise 1 的【定義 1】，因此其誤差成長必然依賴當前狀態。

### (b) solve $\mathbf{A}$ 的特徵值與其物理意義

把【假設 1】的參數與【假設 4】的基準點代入 (a) 的結果。

$$\begin{gather*}
\mathbf{A} &\overset{\text{Q2(a)}}{=}& \begin{bmatrix} -\sigma & \sigma & 0 \\ \rho - z & -1 & -x \\ y & x & -\beta \end{bmatrix} \\
&\overset{\text{假設 1,假設 4}}{=}& \begin{bmatrix} -10 & 10 & 0 \\ 24.74 - 0 & -1 & -0 \\ 0 & 0 & -\frac{8}{3} \end{bmatrix} \\
&=& \begin{bmatrix} -10 & 10 & 0 \\ 24.74 & -1 & 0 \\ 0 & 0 & -\frac{8}{3} \end{bmatrix}
\end{gather*}$$

以附錄的 `solve_eigen.py` 解【已知 2(a)】的特徵值問題，得三個特徵值與其對應的特徵向量。

1. 收縮最快的方向：

$$\lambda_1 \approx -21.860012$$

$$\mathbf{v}_1 \approx \begin{bmatrix} -0.644612 \\ 0.764510 \\ 0 \end{bmatrix}$$

2. 唯一的成長方向：

$$\lambda_2 \approx +10.860012$$

$$\mathbf{v}_2 \approx \begin{bmatrix} -0.432281 \\ -0.901739 \\ 0 \end{bmatrix}$$

3. 沿 $z$ 軸的收縮方向：

$$\lambda_3 \approx -2.666667$$

$$\mathbf{v}_3 \approx \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}$$

**物理意義：** 由【已知 2(b)】，誤差在第 $i$ 個特徵方向上依 $e^{\lambda_i t}$ 演化，故 $\lambda_i$ 就是誤差在該方向上的**瞬時指數成長率**。

* $\lambda_2 \approx +10.860012 > 0$：沿 $\mathbf{v}_2$ 方向的誤差會指數放大，此為不穩定方向 (unstable direction)。其 e-folding time 為

  $$\frac{1}{\lambda_2} \approx 0.092081$$

  即誤差每經過約 $0.092081$ 個無因次時間單位就放大 $e$ 倍。這就是可預報度 (predictability) 存在上限的直接來源：初始誤差無論多小，都會在有限時間內成長到與訊號同量級。

* $\lambda_1 \approx -21.860012 < 0$ 與 $\lambda_3 \approx -2.666667 < 0$：沿 $\mathbf{v}_1$、$\mathbf{v}_3$ 方向的誤差會指數衰減，此為穩定（收縮）方向 (stable direction)。一正二負，代表此基準狀態點為鞍點 (saddle point)。

* 三個特徵值皆為實數（虛部為零），故此基準點附近的誤差只有單純的成長與衰減，沒有旋轉；若特徵值出現共軛複數對，其虛部即代表誤差在該平面上的旋轉頻率。

* 由 (a) 已知 $\mathbf{A} = \mathbf{A}(x, y, z)$，故以上成長率是**該基準狀態點上的局部、瞬時**成長率，而非整條軌跡的全域 Lyapunov 指數；換到別的狀態點，$\mathbf{A}$ 與其特徵值都會改變。

### (c) solve $\mathbf{A}$ 的行列式與其意義

沿第一列作餘因子展開，先得符號式，再代入【假設 4】與【假設 1】求值。

$$\begin{gather*}
\det(\mathbf{A}) &\overset{\text{Q2(a)}}{=}& \begin{vmatrix} -\sigma & \sigma & 0 \\ \rho - z & -1 & -x \\ y & x & -\beta \end{vmatrix} \\
&=& -\sigma\left[(-1)(-\beta) - (-x)(x)\right] - \sigma\left[(\rho - z)(-\beta) - (-x)(y)\right] \\
&=& -\sigma\left(\beta + x^{2}\right) - \sigma\left[-\beta(\rho - z) + xy\right] \\
&=& \sigma\left[\beta(\rho - z) - \beta - x^{2} - xy\right] \\
&\overset{\text{假設 4}}{=}& \sigma\left(\beta\rho - \beta\right) \\
&=& \sigma\beta(\rho - 1) \\
&\overset{\text{假設 1}}{=}& 10 \times \frac{8}{3} \times (24.74 - 1) \\
&\approx& 633.066667
\end{gather*}$$

此值與附錄 `solve_eigen.py` 的輸出 $633.0666666666666$ 相符，亦可由【已知 3(a)】用 (b) 的三個特徵值交叉驗證。

$$\begin{gather*}
\lambda_1 \lambda_2 \lambda_3 &\overset{\text{Q2(b)}}{\approx}& (-21.860012) \times (10.860012) \times (-2.666667) \\
&\approx& 633.066667
\end{gather*}$$

**意義：**

* 由【已知 3(a)】，$\det(\mathbf{A}) = \lambda_1 \lambda_2 \lambda_3$，代表線性算子 $\mathbf{A}$ 作用在誤差空間時，把一個體積元縮放的倍率。

* $\det(\mathbf{A}) \neq 0$，故 $\mathbf{A}$ 可逆、三個特徵值皆非零：切線性方程 $\frac{d}{dt}\left[\delta\mathbf{x}\right] = \mathbf{A}\,\delta\mathbf{x}$ 唯一的平衡點是 $\delta\mathbf{x} = \mathbf{0}$，不存在任何中性（$\lambda = 0$）方向。

* 由符號式 $\det(\mathbf{A}) = \sigma\beta(\rho - 1)$ 可見，只要 $\rho > 1$ 就有 $\det(\mathbf{A}) > 0$。三個實特徵值之積為正而其中恰有一正二負，對應 (b) 所判定的鞍點 —— 這就是 $\rho > 1$ 時 Lorenz 系統的原點失去穩定性的代數判據。

**釐清（$\det$ 與 $\mathrm{tr}$ 不可混為一談）：** 相空間體積隨時間的**瞬時收縮率**是由跡決定的，而非行列式。

$$\begin{gather*}
\mathrm{tr}(\mathbf{A}) &\overset{\text{Q2(a)}}{=}& -\sigma - 1 - \beta \\
&\overset{\text{假設 1}}{=}& -10 - 1 - \frac{8}{3} \\
&\approx& -13.666667
\end{gather*}$$

$\mathrm{tr}(\mathbf{A}) \approx -13.666667 < 0$，且此值與基準狀態點 $(x, y, z)$ 完全無關，故 Lorenz 系統在**任何**狀態下都是耗散的 (dissipative)：由【已知 3(c)】，誤差空間的體積依 $e^{-13.666667\,t}$ 收縮，最終塌陷到零體積的吸引子上。體積的收縮由 $\mathrm{tr}(\mathbf{A})$ 負責，$\det(\mathbf{A})$ 描述的則是算子 $\mathbf{A}$ 本身的體積縮放倍率。

### 附錄 (Appendix)：solve_eigen.py

執行方式為在本資料夾下直接執行 `py solve_eigen.py`；要更換基準狀態點，只需修改 `x`、`y`、`z` 三行。

```python
import numpy as np

# Lorenz '63 參數
sigma = 10.0
beta = 8.0 / 3.0
rho = 24.74

# 評估的基準狀態點
x = 0.0
y = 0.0
z = 0.0

# 定義矩陣 A
A = np.array([[  -sigma, sigma,   0.0],
              [rho - z,   -1.0,    -x],
              [      y,      x, -beta]])

# 計算特徵值 (Eigenvalues)
eigenvalues, eigenvectors = np.linalg.eig(A)
det_A = np.linalg.det(A)
trace_A = np.trace(A)

print("特徵值：", eigenvalues)
print("特徵向量：", eigenvectors)
print("矩陣 A 的行列式為：", det_A)
print("矩陣 A 的跡為：", trace_A)
```

執行結果：

```
特徵值： [-21.86001222  10.86001222  -2.66666667]
特徵向量： [[-0.64461164 -0.4322811   0.        ]
 [ 0.76451019 -0.9017389   0.        ]
 [ 0.          0.          1.        ]]
矩陣 A 的行列式為： 633.0666666666666
矩陣 A 的跡為： -13.666666666666666
```
