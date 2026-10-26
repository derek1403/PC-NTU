# Final exam — 題目與解答

Date: 6/9/2026

依提供的兩張試卷照片轉錄；保留英文題目與配分，第 7(b) 題已勘誤，解答使用中文。原卷配分合計 **100%**。純題目版見 [final_questions.md](final_questions.md)。

**勘誤：** 第 7(b) 題的高溫熱容量極限已由無限大更正為 $3R$，兩份 Markdown 已同步修正。此修訂與第 7(a) 題為同一高溫結果。第 6 題未指定溫度與邊界條件，採零溫、非交互作用、自旋簡併為 2 的自由電子模型，另列有限粒子數的硬牆結果。

講義引用採 `lecture` 內各章的 `.md`，並在各題列出對應章節或公式；從講義延伸的一維態計數與晶胞幾何在本檔直接推導。符號 $k=k_B$，$h=2\pi\hbar$，電子質量為 $m_e$。

## Problem 1 (10%)

The Maxwell distribution of molecular velocity is

$$
n(v)\,dv=4\pi N\left(\frac{m}{2\pi kT}\right)^{3/2}v^2e^{-mv^2/(2kT)}\,dv.
$$

Please calculate the average value of (1) $1/v$ and (2) $v$.

### 解答

講義：[Chapter 9，§9.3，式 (9.14)](../../lecture/09_Statistical_Mechanics/statistical_mechanics.md)。此處 $v\geq0$ 是**速率**，不是某個帶正負號的速度分量。

令 $a=m/(2kT)$，將粒子數分布除以 $N$ 得到機率密度：

$$
p(v)=\frac{n(v)}N=\frac{4a^{3/2}}{\sqrt\pi}v^2e^{-av^2},
\qquad \langle g(v)\rangle=\int_0^\infty g(v)p(v)\,dv.
$$

用 $u=av^2$ 可得

$$
\int_0^\infty ve^{-av^2}\,dv=\frac1{2a},
\qquad
\int_0^\infty v^3e^{-av^2}\,dv=\frac1{2a^2}.
$$

因此

$$
\boxed{\left\langle\frac1v\right\rangle
=\frac{4a^{3/2}}{\sqrt\pi}\frac1{2a}
=\sqrt{\frac{2m}{\pi kT}}},
$$

$$
\boxed{\langle v\rangle
=\frac{4a^{3/2}}{\sqrt\pi}\frac1{2a^2}
=\sqrt{\frac{8kT}{\pi m}}}.
$$

兩者的單位分別為 $\mathrm{s/m}$ 與 $\mathrm{m/s}$。注意 $\langle1/v\rangle\neq1/\langle v\rangle$，其乘積為 $4/\pi$。

## Problem 2 (10%)

(a) Why can a small vibration of any potential force be approximated as a simple harmonic oscillator?

(b) What are the differences between fluorescence and phosphorescence?

### 解答 (a)：平衡點附近的 Taylor 展開

講義：[Chapter 8，§8.7，式 (8.12)–(8.15)](../../lecture/08_Molecules/molecules.md)。

設平滑位能 $U(x)$ 在 $x_0$ 有穩定、非退化極小值，故 $U'(x_0)=0$、$U''(x_0)>0$。令 $q=x-x_0$：

$$
U(x_0+q)=U(x_0)+U'(x_0)q+\frac12U''(x_0)q^2+O(q^3)
\simeq U(x_0)+\frac12\kappa q^2,
\quad \kappa=U''(x_0)>0.
$$

所以

$$
F=-\frac{dU}{dx}\simeq-\kappa q,
\qquad m\ddot q+\kappa q=0,
\qquad \boxed{\omega=\sqrt{\kappa/m}}.
$$

小振幅時高階項可忽略，因此近似簡諧運動。雙原子分子的相對振動須以縮減質量 $\mu=m_1m_2/(m_1+m_2)$ 取代 $m$。

原題的「any」有前提：必須在上述穩定平衡點附近。若 $U''(x_0)=0$（例如 $U\propto q^4$）或平衡不穩定，就不能使用此簡諧近似。

### 解答 (b)：螢光與磷光

講義：[Chapter 8，§8.8](../../lecture/08_Molecules/molecules.md)。以下以常見的單重態基態分子說明。

| 比較項目 | 螢光 fluorescence | 磷光 phosphorescence |
|---|---|---|
| 典型路徑 | 吸收後振動弛豫，再由 $S_1\to S_0$ 放光 | 先經系間轉換 $S_1\to T_1$，再由 $T_1\to S_0$ 放光 |
| 自旋 | $\Delta S=0$，通常為自旋允許躍遷 | $\Delta S=1$，為自旋禁戒躍遷，因態混合而可弱發生 |
| 壽命 | 較短，常在奈秒尺度 | 通常較長，可為微秒、毫秒至秒或更久，依材料而定 |
| 關掉激發光後 | 通常迅速消失 | 可維持餘輝 |

兩者都屬於吸收能量後的發光，並常因非輻射弛豫而使放射光子能量低於吸收光子；最重要差異是躍遷路徑、自旋選擇規則與壽命。

## Problem 3 (10%)

In a system with 2 electrons which follows the Pauli Exclusion Principle, please explain why the total wavefunction has to be antisymmetric?

### 解答

講義：[Chapter 7，§7.3](../../lecture/07_Many-Electron_Atoms/many_electron_atoms.md)；[Chapter 9，§9.4，式 (9.20)、(9.25)](../../lecture/09_Statistical_Mechanics/statistical_mechanics.md)。

以 $1=(\mathbf r_1,\sigma_1)$、$2=(\mathbf r_2,\sigma_2)$ 表示包含自旋的完整座標。在通常的玻色／費米交換對稱分類下，交換算符滿足 $P_{12}^2=1$，故交換本徵值為 $+1$ 或 $-1$。

對不同且正交歸一的單電子自旋軌域 $a,b$，兩種組合為

$$
\Psi_\pm(1,2)=\frac1{\sqrt2}
\left[\phi_a(1)\phi_b(2)\pm\phi_b(1)\phi_a(2)\right].
$$

若嘗試讓兩個電子進入同一完整單粒子態 $a=b$，反對稱組合的分子恆為零：

$$
\phi_a(1)\phi_a(2)-\phi_a(2)\phi_a(1)=0.
$$

零函數不能歸一化為物理態，因此此佔據被禁止；對稱組合則不會消失，歸一化後可成為 $\phi_a(1)\phi_a(2)$，無法自動滿足電子的包立不相容原理。電子採用反對稱交換類別：

$$
\boxed{\Psi(2,1)=-\Psi(1,2)}.
$$

嚴格來說，電子是自旋 $1/2$ 的費米子，反對稱性由自旋—統計關聯支持，包立不相容是其結果；不能僅從某一位置的機率密度相同就推出波函數必為反對稱。

**必須反對稱的是總波函數。** 若自旋部分是反對稱 singlet，空間部分可以對稱；若自旋部分是對稱 triplet，空間部分須反對稱。因此兩電子可以佔據相同空間軌域，只要自旋相反。

## Problem 4 (15%)

Consider fcc, bcc, sc, and diamond structures.

(a) What are the coordination numbers of fcc, bcc, sc, and diamond structure, respectively?

(b) Suppose identical solid sphere are distributed through space in such a way that their centers lie on the points of each of these four structures, and spheres on neighboring points just touch, without overlapping. (This is called close-packing arrangement.) Assuming that the sphere have density of one, what is the density of a set of close-packed spheres on each of these four structures?

(c) Which structure is the most dense and which one is the least dense structure?

### 解答

講義：[Chapter 10，§10.2–10.3，晶體與鑽石結構](../../lecture/10_The_Solid_State/the_solid_state.md)。下列填充率由各結構的立方晶胞幾何計算。

設慣用立方晶胞邊長為 $a$、球半徑為 $r$、晶胞內球數為 $z$。因球本身密度為 1，整體密度數值就是體積填充率：

$$
\rho=\eta=\frac{z(4\pi r^3/3)}{a^3}.
$$

| 結構 | (a) 配位數 | 晶胞內球數 $z$ | 最近鄰相切條件 | (b) 密度／填充率 |
|---|---:|---:|---|---|
| fcc 面心立方 | 12 | 4 | $4r=\sqrt2a$ | $\pi/(3\sqrt2)\simeq0.7405$ |
| bcc 體心立方 | 8 | 2 | $4r=\sqrt3a$ | $\sqrt3\pi/8\simeq0.6802$ |
| sc 簡單立方 | 6 | 1 | $2r=a$ | $\pi/6\simeq0.5236$ |
| diamond 鑽石 | 4 | 8 | $2r=\sqrt3a/4$ | $\sqrt3\pi/16\simeq0.3401$ |

晶胞球數來自：sc 的 $8\times1/8=1$；bcc 再加體心 1 顆得 2；fcc 為 $8\times1/8+6\times1/2=4$；diamond 是 fcc 加 4 顆胞內原子，共 8。

例如鑽石最近鄰位移為 $(a/4,a/4,a/4)$，故 $r=\sqrt3a/8$，代入得

$$
\eta_{\rm diamond}
=8\frac{4\pi}{3}\left(\frac{\sqrt3}{8}\right)^3
=\frac{\sqrt3\pi}{16}.
$$

(c) 在這四種結構中，**fcc 最密，diamond 最疏**。

原題將所有相切球排列都稱為 close-packing；嚴格術語下，bcc、sc、diamond 並不是最密堆積，但不影響本題填充率計算。

## Problem 5 (10%)

The ionization potential of sodium is 5.14 eV, the electron affinity of fluorine is 3.4 eV, and the equilibrium separation of NaF is 0.193 nm.

(a) How much energy is needed to form $\mathrm{Na}^+$ and $\mathrm{F}^-$ ions from neutral Na and F atoms?

(b) What is the electrostatic potential energy of the $\mathrm{Na}^+$ and $\mathrm{F}^-$ ions at their equilibrium separation?

(c) The dissociation energy of NaF is 4.99 eV. What is the energy due to exclusion-principle repulsion force?

(d) The energy of the repulsion force is $E=A/r_0^n$. Find $A$ and $n$.

### 解答

講義：[Chapter 8，§8.1，離子鍵能量帳](../../lecture/08_Molecules/molecules.md)；[Chapter 10，§10.2，式 (10.2)–(10.3) 與平衡條件](../../lecture/10_The_Solid_State/the_solid_state.md)。本題是單一 NaF 分子，不引入無限離子晶體的 Madelung 常數。

取無限分離的**中性 Na、F 原子**為能量零點，使用

$$
C\equiv\frac{e^2}{4\pi\varepsilon_0}
\simeq1.43996455\ \mathrm{eV\,nm},\qquad r_0=0.193\ \mathrm{nm}.
$$

#### (a) 形成離子的淨能量

Na 游離消耗能量，F 接受電子放出能量：

$$
\boxed{\Delta E_{\rm ion}=5.14-3.40=1.74\ \mathrm{eV}}.
$$

#### (b) 庫侖位能

$$
\boxed{U_C(r_0)=-\frac C{r_0}
=-\frac{1.43996455}{0.193}\ \mathrm{eV}
\simeq-7.461\ \mathrm{eV}}.
$$

#### (c) 排斥能

將解離能 $D=4.99\ \mathrm{eV}$ 解讀為分解至中性原子所需能量，則平衡分子的總能為 $-D$：

$$
-D=\Delta E_{\rm ion}+U_C(r_0)+U_{\rm rep}(r_0).
$$

因此

$$
\boxed{U_{\rm rep}(r_0)
=-4.99-1.74+7.4609562
=0.7309562\ \mathrm{eV}\simeq0.731\ \mathrm{eV}}.
$$

正號代表排斥提高總能量。檢查：$1.74-7.4609562+0.7309562=-4.99$。

#### (d) 求 $n$ 與 $A$

將題目在 $r_0$ 的排斥能延伸為位能函數 $U_{\rm rep}(r)=A/r^n$，則

$$
U(r)=\Delta E_{\rm ion}-\frac Cr+\frac A{r^n}.
$$

在平衡距離處 $U'(r_0)=0$：

$$
\frac C{r_0^2}-\frac{nA}{r_0^{n+1}}=0
\quad\Rightarrow\quad
n\frac A{r_0^n}=\frac C{r_0}.
$$

由 $A/r_0^n=U_{\rm rep}(r_0)$ 得

$$
\boxed{n=\frac{C/r_0}{U_{\rm rep}(r_0)}
=\frac{7.4609562}{0.7309562}\simeq10.2071\approx10.2},
$$

$$
\boxed{A=U_{\rm rep}(r_0)r_0^n
=\frac Cn r_0^{n-1}}.
$$

保留上述未四捨五入的 $n$，若長度以 nm 計，

$$
\boxed{A\simeq3.7281\times10^{-8}\ \mathrm{eV}\,\mathrm{nm}^{\,n},
\qquad n\simeq10.2071}.
$$

因 $A$ 的單位本身依賴 $n$，最穩健的數值表示為

$$
\boxed{U_{\rm rep}(r)\simeq0.7309562\ \mathrm{eV}
\left(\frac{0.193\ \mathrm{nm}}r\right)^{10.2071}}.
$$

資料未要求 $n$ 為整數；不要先取 $n=10$ 再宣稱完全符合原數據。以上多位小數用於檢查一致性，不代表輸入數據具有同等實驗精度。此外

$$
U''(r_0)=\frac{(n-1)C}{r_0^3}>0,
$$

確認此平衡點為穩定極小值。

## Problem 6 (10%)

(a) What is the Fermi energy of an N-electron system in a 1-D line with length L?

(b) What is the average energy of the electrons in this system?

### 解答

講義：[Chapter 9，§9.9–9.10](../../lecture/09_Statistical_Mechanics/statistical_mechanics.md) 提供零溫填滿電子態的計數方法。講義式 (9.56)、(9.60) 是三維結果，本題須重新做一維計數，不能沿用 $3E_F/5$。

假設 $T=0$、電子不交互作用、無外加磁場，每個空間能態容納兩個相反自旋的電子。採長度 $L$ 的硬牆盒，單粒子能階為

$$
\epsilon_j=\frac{\pi^2\hbar^2j^2}{2m_eL^2}
=\frac{h^2j^2}{8m_eL^2},\qquad j=1,2,\ldots
$$

#### (a) 費米能量

對偶數 $N=2M$，填至 $j=M=N/2$，以最高已佔據能量定義 $E_F$：

$$
\boxed{E_F=\epsilon_M
=\frac{\pi^2\hbar^2N^2}{8m_eL^2}
=\frac{h^2N^2}{32m_eL^2}}.
$$

等價地，在大量粒子的連續近似下

$$
k_F=\frac{\pi N}{2L},\qquad E_F=\frac{\hbar^2k_F^2}{2m_e}.
$$

#### (b) 平均能量

令 $\alpha=h^2/(8m_eL^2)$，偶數粒子數時的精確總能量為

$$
U=2\alpha\sum_{j=1}^M j^2
=\frac{\alpha M(M+1)(2M+1)}3.
$$

所以

$$
\boxed{\overline\epsilon=\frac UN
=\frac{\alpha(M+1)(2M+1)}6
=E_F\frac{(M+1)(2M+1)}{6M^2}}.
$$

在 $N\gg1$ 的連續近似下，

$$
\boxed{\overline\epsilon\simeq\frac13E_F
=\frac{h^2N^2}{96m_eL^2}}.
$$

也可由一維態密度 $g(\epsilon)\propto\epsilon^{-1/2}$ 驗證：

$$
\overline\epsilon=
\frac{\int_0^{E_F}\epsilon^{1/2}\,d\epsilon}
{\int_0^{E_F}\epsilon^{-1/2}\,d\epsilon}
=\frac{E_F}3.
$$

**有限系統補充：** 若 $N=2M+1$，最後一層只有一顆電子，則 $E_F=\alpha(M+1)^2$，

$$
\overline\epsilon=
\frac{2\alpha\sum_{j=1}^{M}j^2+\alpha(M+1)^2}{2M+1}.
$$

邊界條件會影響有限尺寸修正；上述 $E_F\propto(N/L)^2$ 與 $\overline\epsilon\simeq E_F/3$ 是通常考題所求的大粒子數結果。若溫度不為零，平均能量還需指定 $T$。

## Problem 7 (10%)

(a) Show that the rule of Dulong-Petit follows directly from Einstein's specific heat formula as $T\to\infty$:

$$
C_V=\frac{dU}{dT}=3N_Ak\left(\frac{hf}{kT}\right)^2
\frac{e^{hf/(kT)}}{\left(e^{hf/(kT)}-1\right)^2}.
$$

(b) Show that $C_V\to3R$ as $T\to\infty$, where $R=N_Ak$ is the molar gas constant.

### 解答 (a)：高溫極限

講義：[Chapter 9，§9.8，式 (9.51)、(9.54)](../../lecture/09_Statistical_Mechanics/statistical_mechanics.md)。

設 $x=hf/(kT)$。當 $T\to\infty$，$x\to0$，故

$$
e^x=1+x+O(x^2),\qquad e^x-1=x+O(x^2).
$$

因此

$$
\lim_{T\to\infty}C_V
=3N_Ak\lim_{x\to0}\frac{x^2e^x}{(e^x-1)^2}
=3N_Ak.
$$

題目使用 $N_A$，所以是每莫耳熱容量：

$$
\boxed{C_V\to3R\simeq24.94\ \mathrm{J\,mol^{-1}K^{-1}}},
$$

即 Dulong–Petit 定律。若樣品有 $N$ 個原子，其總熱容量極限為 $3Nk$。

### 解答 (b)：證明熱容量趨近 $3R$

令 $x=hf/(kT)$，利用 $e^x-1=2e^{x/2}\sinh(x/2)$，將題目公式改寫為

$$
\frac{C_V}{3R}
=\left(\frac{x}{2\sinh(x/2)}\right)^2.
$$

當 $T\to\infty$ 時，$x\to0$。由 $\lim_{y\to0}\sinh y/y=1$，得到

$$
\boxed{\lim_{T\to\infty}C_V=3R}.
$$

此外，$\sinh(x/2)\geq x/2$（$x>0$），所以 $0<C_V\leq3R$；熱容量在高溫時趨近有限值，而不會發散。此結果與 (a) 的 Dulong–Petit 定律一致。

## Problem 8 (15%)

For large quantum numbers, the frequency of the radiation from a hydrogen atom that drops from an initial state of quantum number n to a final state of quantum number n-1 is equal to the classical frequency of revolution of an electron in the nth Bohr orbit. This is an example of Bohr's correspondence principle. Show that a similar correspondence holds for a diatomic molecule rotating about its center of mass.

### 解答

講義：[Chapter 8，§8.6，式 (8.5)、(8.7)–(8.11)](../../lecture/08_Molecules/molecules.md)。

以固定核間距 $r$ 的剛性雙原子轉子為模型：

$$
I=\mu r^2,\qquad \mu=\frac{m_1m_2}{m_1+m_2},
\qquad E_J=\frac{\hbar^2J(J+1)}{2I}.
$$

對向下躍遷 $J\to J-1$，光子能量為

$$
h\nu_{\rm rad}=E_J-E_{J-1}
=\frac{\hbar^2}{2I}[J(J+1)-(J-1)J]
=\frac{\hbar^2J}{I}.
$$

因此

$$
\boxed{\nu_{\rm rad}=\frac{\hbar J}{2\pi I}}.
$$

古典轉子的角速度是 $\omega=L/I$；以初態角動量大小 $L_J=\hbar\sqrt{J(J+1)}$ 對應，有

$$
\nu_{\rm cl}=\frac{\omega}{2\pi}
=\frac{\hbar\sqrt{J(J+1)}}{2\pi I}.
$$

兩者比值為

$$
\boxed{\frac{\nu_{\rm rad}}{\nu_{\rm cl}}
=\sqrt{\frac{J}{J+1}}\longrightarrow1
\quad(J\to\infty)}.
$$

大轉動量子數時，量子躍遷的放射頻率趨近古典轉動頻率，符合 Bohr 對應原理。有限 $J$ 時不必完全相等。

此放射討論假設存在允許的純轉動電偶極躍遷（例如具有永久電偶極矩的異核雙原子分子，$\Delta J=\pm1$）。同核雙原子分子沒有此類電偶極純轉動譜線；能階差的數學極限仍然成立，但不代表一定發出該譜線。

## Problem 9 (10%)

Please draw an energy band diagram of a diode. Specify clearly the conduction band and valence band, the Fermi level, and the depletion region.

### 解答

講義：[Chapter 10，§10.6–10.7](../../lecture/10_The_Solid_State/the_solid_state.md)。題目未指定偏壓，畫**熱平衡、無外加偏壓的同質 p–n 接面**，p 側在左，n 側在右。

```text
Electron energy E
  ^
  |         p-type       depletion region        n-type
  |                       |             |
  | Ec  __________________
  |                       \
  |                        \
  |                         \______________________ Ec
  |
  | EF  - - - - - - - - - - - - - - - - - - - - -  EF
  |
  | Ev  __________________
  |                       \
  |                        \
  |                         \______________________ Ev
  |                       |             |
  +-----------------------|-------------|-----------> x
                         -xp     0      xn
                          <---- W ---->
```

此為定性示意，非等比例圖；真實耗盡近似中的能帶彎曲為分段曲線，並非直線折角。

- $E_c$ 是**傳導帶底**，傳導帶位於其上；$E_v$ 是**價帶頂**，價帶位於其下。兩者之間為能隙 $E_g=E_c-E_v$，同質接面的能隙近似固定。
- **費米能階 $E_F$ 在熱平衡時整條水平。** p 側 $E_F$ 靠近 $E_v$，n 側 $E_F$ 靠近 $E_c$。
- **空乏區**為 $-x_p<x<x_n$，寬度 $W=x_p+x_n$；可移動載子濃度大幅減少，p 側主要留下帶負電的固定受子離子，n 側主要留下帶正電的固定施子離子。
- 內建電場由 n 側指向 p 側。以電子能量作圖時，p 側的兩條帶邊均較 n 側高，位能障壁高度為 $eV_{\rm bi}$：

$$
E_c(p)-E_c(n)=E_v(p)-E_v(n)=eV_{\rm bi}.
$$

平衡是漂移與擴散電流互相抵銷、淨電流為零，並非個別載子停止運動。外加偏壓時應另畫能帶彎曲與準費米能階，不再以整個接面的單一水平 $E_F$ 描述。

