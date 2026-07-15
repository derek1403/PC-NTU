# 方程式索引表 (Equations Index)

本頁是 **Advanced Atmospheric Dynamics 課程自己的**方程式索引。

**用途**：撰寫新的推導時，凡是**本課程已經證明過**的式子，一律用**帶超連結的【已知】卡片**直接引用，
**不得重證**（見推導風格規範 `PC-NTU/.claude/skills/derivation-style-review/SKILL.md` §10「引用免證」）。

**單一職責原則**：本表**只收錄本課程（AAD）內部已證的方程式**。
外部知識庫（如 [Theory_Playground](https://derek1403.github.io/Theory_Playground/)）的推導由該庫自行維護索引，
本課程的 notebook 只在【已知】卡片內以超連結引用，這樣外部改動時本表不必跟著改。

引用卡片寫法：

```markdown
* **【已知 1】[動量方程式 (Momentum Equation, Navier-Stokes)](連結)：**

  $$\frac{\partial \mathbf{u}}{\partial t } + (\mathbf{u} \cdot \nabla) \mathbf{u} = \mathbf{g} - \frac{1}{\rho} \nabla P + \frac{\mu}{\rho} \nabla^2 \mathbf{u}$$
```

---

## Lecture — Week 1

| 名稱 (Name) | LaTeX Equation | 連結 (Link) | 前提／適用條件 |
|---|---|---|---|
| 萊布尼茲積分法則 (Leibniz Integral Rule) | `\frac{d}{dt} \int_{a(t)}^{b(t)} f(x,t) \, dx = \int_{a(t)}^{b(t)} \frac{\partial f}{\partial t} \, dx + f(b,t) \frac{db}{dt} - f(a,t) \frac{da}{dt}` | [week1 #leibniz-integral-rule](https://derek1403.github.io/PC-NTU/Advanced-Atmospheric-Dynamics/_build/html/lecture/week1/week1.html#leibniz-integral-rule) | 積分上下限隨時間變動；$f$ 對 $t$ 可微 |
| 雷諾傳輸定理 (Reynolds Transport Theorem, RTT) | `\frac{d}{dt} \int_{V_m} \rho \, dV = \int_{V_m} \frac{\partial \rho}{\partial t} \, dV + \oint_{\partial V_m} \rho \mathbf{u} \cdot d\mathbf{A}` | [week1 #leibniz-integral-rule](https://derek1403.github.io/PC-NTU/Advanced-Atmospheric-Dynamics/_build/html/lecture/week1/week1.html#leibniz-integral-rule) | 物質體積 $V_m$ 隨流體移動；連續體假設 |
| 連續方程式 (Continuity Equation) | `\frac{\partial \rho}{\partial t} + \nabla \cdot (\rho \mathbf{u}) = 0` | [week1 #continuity-equation](https://derek1403.github.io/PC-NTU/Advanced-Atmospheric-Dynamics/_build/html/lecture/week1/week1.html#continuity-equation) | 質量守恆；任意體積引理 |
| 動量方程式 (Momentum Equation, Navier-Stokes) | `\frac{\partial \mathbf{u}}{\partial t} + (\mathbf{u} \cdot \nabla) \mathbf{u} = \mathbf{g} - \frac{1}{\rho} \nabla P + \frac{\mu}{\rho} \nabla^2 \mathbf{u}` | [week1 #momentum-equation-navier-stokes](https://derek1403.github.io/PC-NTU/Advanced-Atmospheric-Dynamics/_build/html/lecture/week1/week1.html#momentum-equation-navier-stokes) | 只考慮重力、壓力梯度力、黏滯力；不可壓縮牛頓流體（$\nabla \cdot \mathbf{\tau} = \mu \nabla^2 \mathbf{u}$） |
| 狀態方程式 (Equation of State) | `P = \rho R_d T` | [week1 #equation-of-state](https://derek1403.github.io/PC-NTU/Advanced-Atmospheric-Dynamics/_build/html/lecture/week1/week1.html#equation-of-state) | 乾空氣；理想氣體；$R_d = R^*/M_d \approx 287 \ \text{J} \cdot \text{kg}^{-1} \cdot \text{K}^{-1}$ |
| 控制方程組 (Governing Equations) | 連續 + 動量 + 狀態方程式（閉合系統） | [week1 #governing-equations](https://derek1403.github.io/PC-NTU/Advanced-Atmospheric-Dynamics/_build/html/lecture/week1/week1.html#governing-equations) | 5 未知數（$u,v,w,\rho,P$）需 5 條方程式；斜壓大氣尚需熱力學方程式 |

## Lecture — Week 2

| 名稱 (Name) | LaTeX Equation | 連結 (Link) | 前提／適用條件 |
|---|---|---|---|
| 一般化連續方程式 (Generalized Continuity Equation) | `\frac{\partial C}{\partial t} + \nabla \cdot \vec{J}_C = 0` | [week2 #continuity-equation-diffusion](https://derek1403.github.io/PC-NTU/Advanced-Atmospheric-Dynamics/_build/html/lecture/week2/week2.html#continuity-equation-diffusion) | 任意守恆量 $C$ 與其通量 $\vec{J}_C$；無源匯項 |
| 熱傳導方程式 (Heat Conduction Equation) | `\frac{\partial T}{\partial t} = \alpha \nabla^2 T` | [week2 #heat-conduction-equation](https://derek1403.github.io/PC-NTU/Advanced-Atmospheric-Dynamics/_build/html/lecture/week2/week2.html#heat-conduction-equation) | 無巨觀流體運動（純傳導）；均質不可壓縮（$\rho, c_p, k$ 為常數）；無內部熱源；$\alpha \equiv k/(\rho c_p)$ |
| 擾動變異數的耗散 (Dissipation of Scalar Variance) | `\frac{d}{dt} \int \frac{{q'}^2}{2} \, dV = -\nu \int |\nabla q'|^2 \, dV` | [week2 #dissipation-of-scalar-variance](https://derek1403.github.io/PC-NTU/Advanced-Atmospheric-Dynamics/_build/html/lecture/week2/week2.html#dissipation-of-scalar-variance) | 雷諾分解；$\bar{\mathbf{u}} = 0$、$\nabla \bar{q} = 0$、線性化；封閉／週期邊界 |
| 雷諾數 (Reynolds Number) | `Re = \frac{\rho v l}{\mu}` | [week2 #dimensional-analysis](https://derek1403.github.io/PC-NTU/Advanced-Atmospheric-Dynamics/_build/html/lecture/week2/week2.html#dimensional-analysis) | 由白金漢 $\pi$ 定理導出（本課程只做因次分析；嚴格定義見 Theory_Playground） |
| Poiseuille 速度剖面 (Velocity Profile) | `u(r) = \frac{\Delta P}{4\ell\mu} (r_0^2 - r^2)` | [week2 #a-proof](https://derek1403.github.io/PC-NTU/Advanced-Atmospheric-Dynamics/_build/html/lecture/week2/week2.html#a-proof) | 圓管；穩態層流；無滑動邊界 $u(r_0)=0$ |
| Poiseuille 定律：總流量 (Poiseuille's Law) | `I = \frac{\pi \Delta P}{8 \ell \mu} r_0^4` | [week2 #b-proof-poiseuille-s-law](https://derek1403.github.io/PC-NTU/Advanced-Atmospheric-Dynamics/_build/html/lecture/week2/week2.html#b-proof-poiseuille-s-law) | 同上；$I \propto r_0^4$ |
| 流阻 (Fluid Resistance) | `R_{\text{fluid}} = \frac{8 \ell \mu}{\pi r_0^4}` | [week2 #d-proof](https://derek1403.github.io/PC-NTU/Advanced-Atmospheric-Dynamics/_build/html/lecture/week2/week2.html#d-proof) | 定義 $R_{\text{fluid}} \equiv \frac{\Delta P}{I}$（歐姆定律類比），再代入 Poiseuille 定律導出 |
| 穆雷定律 (Murray's Law) | `\cos\theta = \frac{r_2^4}{r_1^4}` | [week2 #murray-s-law](https://derek1403.github.io/PC-NTU/Advanced-Atmospheric-Dynamics/_build/html/lecture/week2/week2.html#murray-s-law) | 主管 $r_1$／支管 $r_2$ 串聯；總流阻對分叉角 $\theta$ 取極小 |
| 絕對角動量守恆 (Absolute Angular Momentum Conservation) | `\frac{D}{Dt}\left( v r + \frac{1}{2} f r^2 \right) = 0` | [week2 #application-to-tropical-cyclones](https://derek1403.github.io/PC-NTU/Advanced-Atmospheric-Dynamics/_build/html/lecture/week2/week2.html#application-to-tropical-cyclones) | 圓柱座標；軸對稱（$\partial P/\partial \lambda = 0$）；無摩擦；$f$-plane（$Df/Dt = 0$） |
| 原始方程式 (Primitive Equations) | `\frac{Du}{Dt} - f v - \frac{u v \tan\phi}{a} = -\frac{1}{\rho a \cos\phi} \frac{\partial P}{\partial \lambda} + F_\lambda` <br> `\frac{Dv}{Dt} + f u + \frac{u^2 \tan\phi}{a} = -\frac{1}{\rho a} \frac{\partial P}{\partial \phi} + F_\phi` <br> `\frac{\partial P}{\partial z} = -\rho g` | [week2 #primitive-equations](https://derek1403.github.io/PC-NTU/Advanced-Atmospheric-Dynamics/_build/html/lecture/week2/week2.html#primitive-equations) | 球座標；傳統／淺層近似（$R \approx a$、$w \ll u,v$）；靜力平衡；$f = 2\Omega\sin\phi$ |
| 靜力平衡 (Hydrostatic Balance) | `\frac{\partial P}{\partial z} = -\rho g` | [week2 #primitive-equations](https://derek1403.github.io/PC-NTU/Advanced-Atmospheric-Dynamics/_build/html/lecture/week2/week2.html#primitive-equations) | 垂直尺度分析：$\frac{Dw}{Dt}, 2\Omega u \cos\phi, \frac{u^2+v^2}{a} \ll g$ |

## Homework / Project（待補）

以下 notebook 的結論式尚未編入索引；需要引用時請先把該式補進本表，再於卡片內連結。

| 來源 | 頁面 |
|---|---|
| HW1 | [hw1](https://derek1403.github.io/PC-NTU/Advanced-Atmospheric-Dynamics/_build/html/homework/hw1/hw1.html) |
| HW2 | [hw2](https://derek1403.github.io/PC-NTU/Advanced-Atmospheric-Dynamics/_build/html/homework/hw2/hw2.html) |
| HW3 | [hw3](https://derek1403.github.io/PC-NTU/Advanced-Atmospheric-Dynamics/_build/html/homework/hw3/hw3.html) |
| Project 1（線性化微擾方程組、算符 $L$ 的反厄米性、色散關係、CFL 條件、無因次化） | [project1](https://derek1403.github.io/PC-NTU/Advanced-Atmospheric-Dynamics/_build/html/project/project1/project_overview.html) |
| Project 2（赤道波色散關係、Hermite／Weber 方程式、長波近似） | [project2](https://derek1403.github.io/PC-NTU/Advanced-Atmospheric-Dynamics/_build/html/project/project2/project2.html) |

---

## 維護規則

1. **新增推導後就補一列**：只要某個 notebook 證出一條可被別處引用的結論，就在本表加一列（名稱、LaTeX、連結、前提）。
2. **連結指向唯一 anchor**：Jupyter Book 的 heading anchor 取自標題中的**英文**（例如 `## 5. 圓管流體力學 (Poiseuille Flow)` → `#poiseuille-flow`）。
   通用標題（`目標 (Goal)`、`假設與已知`、`proof`）在同一份 notebook 內會重複，Sphinx 會自動改成 `#id1`、`#id2`，**不要連到那些**——請連到帶有唯一英文名的章節標題。
3. **改標題就要回來改連結**：更動 notebook 的英文標題會改變 anchor，本表對應的連結必須同步更新。
4. **不收外部條目**：Theory_Playground 等外部知識庫的式子不列入本表。
