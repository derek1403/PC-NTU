---
jupytext:
  formats: ipynb,md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.19.3
kernelspec:
  display_name: python313
  language: python
  name: python3
---

# Modern Physics Hw 9

```
name:葉品辰
ID:r14229017
date: 2026.06.04
```

+++

## Question 1 


The frequency of vibration of the $\text{H}_2$ molecule is $1.32 \times 10^{14}\text{ Hz}$. 

* (a) Find the relative populations of the $v = 0, 1, 2, 3,$ and $4$ vibrational states at $5000\text{ K}$. 

* (b) Can the populations of the $v = 2$ and $v = 3$ states ever be equal? If so, at what temperature does this occur?



+++

## Question 1 - Answer


### 假設與已知 (Assumptions & Preliminaries)




* **【已知 1】  波茲曼分佈（Boltzmann distribution）  ：** 在熱平衡時，處於能階 $E_v$ 的粒子數 $N_v$ 會與 $\exp(-E_v/kT)$ 成正比
   
  $$\frac{N_v}{N_0} = \frac{e^{-\frac{E_v}{kT}}}{e^{-\frac{E_0}{kT}}}$$

  * $N_{v}$ : 處於振動量子數為 $v$ 的激發態粒子數 (Number of particles in the excited state $v$) [無單位]
  * $N_{0}$ : 處於基態（$v=0$）的粒子數 (Number of particles in the ground state) [無單位]
  * $E_{v}$ : 振動量子數為 $v$ 的能階能量 (Energy of the state $v$) $[\text{J}]$
  * $E_{0}$ : 基態（零點振動）的能階能量 (Ground state energy) $[\text{J}]$
  * $k$ : 波茲曼常數 (Boltzmann constant) $k \approx 1.38 \times 10^{-23} \text{ J}\cdot\text{K}^{-1}$
  * $T$ : 系統的絕對溫度 (Absolute temperature) $[\text{K}]$

* **【已知 2】 量子諧振子的子能階與能量差（Vibrational energy levels and difference）  ：**
  
  $$\begin{gather*}
  E_v &=& (v + \frac{1}{2})h\nu \\
  E_v - E_0 &=&  (v + \frac{1}{2})h\nu  - (0 + \frac{1}{2})h\nu  \\
  E_v - E_0 &=&  vh\nu \\
  \end{gather*}$$

  * $v$ : 振動量子數 (Vibrational quantum number) $v = 0, 1, 2, \dots$ [無單位]
  * $h$ : 普朗克常數 (Planck's constant) $h \approx 6.626 \times 10^{-34} \text{ J}\cdot\text{s}$
  * $\nu $ : 分子的特徵振動頻率 (Characteristic vibrational frequency) $[\text{Hz}],[\text{s}^{-1}]$

* **【推導 1】 特定溫度與頻率下的激發態粒子比例（Derivation of excited state population ratio）  ：** 代入已知條件與特定物理量（例如 $\nu = 1.32 \times 10^{14} \text{ Hz}$, $T = 5000 \text{ K}$），計算出相對於基態的粒子分佈比例。
  
  $$\begin{gather*}
  \frac{N_v}{N_0} &\overset{\text{已知 1}}{=}& \frac{e^{-\frac{E_v}{kT}}}{e^{-\frac{E_0}{kT}}} \\
  &=& e^{-\frac{E_v - E_0}{kT}} \\
  &\overset{\text{已知 2}}{=}& e^{-\frac{vh\nu}{kT}} \\
  &\overset{\text{Q1,已知1,已知2}}{\approx} &  e^{-\frac{v \times (6.626 \times 10^{-34} \text{ J s})(1.32 \times 10^{14} \text{ s}^{-1}) }{(1.38 \times 10^{-23} \text{ J/K})(5000 \text{ K})}} \\
  &\approx&  e^{-v \cdot 1.2675} \\
  \end{gather*}$$

  * $N_{v}$ : 處於振動量子數為 $v$ 的激發態粒子數 (Number of particles in the excited state $v$) [無單位]
  * $N_{0}$ : 處於基態（$v=0$）的粒子數 (Number of particles in the ground state) [無單位]
  * $E_{v}$ : 振動量子數為 $v$ 的能階能量 (Energy of the state $v$) $[\text{J}]$
  * $E_{0}$ : 基態（零點振動）的能階能量 (Ground state energy) $[\text{J}]$
  * $k$ : 波茲曼常數 (Boltzmann constant) $k \approx 1.38 \times 10^{-23} \text{ J}\cdot\text{K}^{-1}$
  * $T$ : 系統的絕對溫度 (Absolute temperature) $[\text{K}]$
  * $v$ : 振動量子數 (Vibrational quantum number) $v = 0, 1, 2, \dots$ [無單位]
  * $h$ : 普朗克常數 (Planck's constant) $h \approx 6.626 \times 10^{-34} \text{ J}\cdot\text{s}$
  * $\nu $ : 分子的特徵振動頻率 (Characteristic vibrational frequency) $[\text{Hz}],[\text{s}^{-1}]$
  

### solve 分子佔據基態 ($v=0$) 到第四激發態 ($v=4$) 的相對比例是多少

1. $v = 0$

$$\begin{gather*}
\frac{N_v}{N_0} &\overset{\text{推導 1}}{=}& e^{-v \cdot 1.2675} \\
&\overset{\text{Q1.1.1}}{=}& e^{-0 \times 1.2675} \\
&=& e^{0} \\
&=& 1 \\
\end{gather*}$$


2. $v = 1$

$$\begin{gather*}
\frac{N_v}{N_0} &\overset{\text{推導 1}}{=}& e^{-v \cdot 1.2675} \\
&\overset{\text{Q1.1.2}}{=}& e^{-1 \times 1.2675} \\
&\approx& e^{-1.2675} \\
&\approx& 0.2815 \\
\end{gather*}$$

3. $v = 2$

$$\begin{gather*}
\frac{N_v}{N_0} &\overset{\text{推導 1}}{=}& e^{-v \cdot 1.2675} \\
&\overset{\text{Q1.1.3}}{=}& e^{-2 \times 1.2675} \\
&\approx& e^{-2.5350} \\
&\approx& 0.0793 \\
\end{gather*}$$

4. $v = 3$

$$\begin{gather*}
\frac{N_v}{N_0} &\overset{\text{推導 1}}{=}& e^{-v \cdot 1.2675} \\
&\overset{\text{Q1.1.4}}{=}& e^{-3 \times 1.2675} \\
&\approx& e^{-3.8025} \\
&\approx& 0.0223 \\
\end{gather*}$$

5. $v = 4$

$$\begin{gather*}
\frac{N_v}{N_0} &\overset{\text{推導 1}}{=}& e^{-v \cdot 1.2675} \\
&\overset{\text{Q1.1.5}}{=}& e^{-4 \times 1.2675} \\
&\approx& e^{-5.0700} \\
&\approx& 0.0063 \\
\end{gather*}$$

### $v=2$ 與 $v=3$ 粒子數相等的情況

$$\begin{gather*}
N_2 &=& N_3 \\
\frac{N_2}{N_0} &=& \frac{N_3}{N_0} \\
e^{-\frac{2h\nu}{kT}} &\overset{\text{推導 1}}{=}& e^{-\frac{3h\nu}{kT}} \\
-\frac{2h\nu}{kT} &=& -\frac{3h\nu}{kT} \\
\frac{h\nu}{kT} &=& 0 \\
\end{gather*}$$

由於 $h$ 與 $\nu$ 皆為不等於零的正實數常數，若要使上式成立，唯有當分母的溫度 $T \to \infty$ 時才有可能。

因此結論是：在任何實際的有限溫度下，這兩個態的粒子數是不可能相等的。

+++

## Question 2 


* (a) Verify that the average value of $1/v$ for an ideal-gas molecule is $\sqrt{\frac{2m}{\pi k T}}$.
* (b) Verify that the most probable speed of an ideal-gas molecule is $\sqrt{\frac{2kT}{m}}$.


+++

## Question 2 - Answer


### 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】馬克士威速率分佈（Maxwell-Boltzmann speed distribution） :** 
  
  $$f(v) = 4\pi \left(\frac{m}{2\pi kT}\right)^{\frac{3}{2}} v^2 e^{-\frac{mv^2}{2kT}}$$

  * $f(v)$ : 速率分佈函數 (Speed distribution function) $[\text{s}\cdot\text{m}^{-1}]$
  * $m$ : 氣體分子質量 (Mass of a single gas molecule) $[\text{kg}]$
  * $k$ : 波茲曼常數 (Boltzmann constant) $k \approx 1.38 \times 10^{-23} \text{ J}\cdot\text{K}^{-1}$
  * $T$ : 絕對溫度 (Absolute temperature) $[\text{K}]$
  * $v$ : 分子的熱運動速率 (Molecular speed) $[\text{m}\cdot\text{s}^{-1}]$
  
* **【已知 2】速率函數的統計平均值定義（Statistical expectation value definition） :** 
  
  $$\langle g(v) \rangle = \int_0^\infty g(v) f(v) dv$$

  * $\langle g(v) \rangle$ : 函數 $g(v)$ 的統計期望值 (Expectation value / Average value)
  * $g(v)$ : 關於速率 $v$ 的任意連續物理量函數 (Any continuous function of speed v)
  * $f(v)$ : 速率分佈函數 (Speed distribution function) $[\text{s}\cdot\text{m}^{-1}]$

* **【推導 1】積分變數變換 :** 

  * (a) 令啞變數 $x$ 與常數 $a$
  
  $$ \begin{gather*}
  x &\overset{\text{let}}{=}& av^2 \\
  dx &=& 2av \ dv \\
  \frac{1}{2a} \ dx &=& v \ dv \\
  \end{gather*}$$

  * (b) 利用變數變換求解特定積分項 

  $$\begin{gather*}
  \int_0^\infty v e^{-av^2} dv  &\overset{\text{推導 1(a)}}{=}& \frac{1}{2a} \int_0^\infty e^{-x} dx \\
  &=&  \frac{1}{2a} \int_0^\infty e^{-x} dx \\
  &=&  \frac{1}{2a} \left[ -e^{-x} \right]_0^\infty \\
  &=&  \frac{1}{2a}  \\
  \end{gather*}$$

  * $a$ : 簡化運算引入的常數係數 (Substitution constant) $a = \frac{m}{2kT}$ $[\text{s}^2\cdot\text{m}^{-2}]$
  * $x$ : 無因次變數變換代號 (Dimensionless dummy variable) [無單位]

### (a) proof $\frac{1}{v}$ 的平均值為 $\sqrt{\frac{2m}{\pi kT}}$  

$$\begin{gather*}
\langle \frac{1}{v} \rangle &\overset{\text{已知 2}}{=}& \int_0^\infty \frac{1}{v} f(v) dv \\
&\overset{\text{已知 1}}{=}& \int_0^\infty \frac{1}{v} 4\pi \left(\frac{m}{2\pi kT}\right)^{\frac{3}{2}} v^2 e^{-\frac{mv^2}{2kT}} dv \\
&=& 4\pi \left(\frac{m}{2\pi kT}\right)^{\frac{3}{2}} \int_0^\infty v e^{-\frac{mv^2}{2kT}} dv \\
&\overset{\text{推導 1}}{=}& 4\pi \left(\frac{m}{2\pi kT}\right)^{\frac{3}{2}} \frac{2kT}{2m} \\
&=& 4\pi \left(\frac{m}{2\pi kT}\right)^{\frac{3}{2}} \frac{kT}{m} \\
&=& \sqrt{\frac{2}{\pi}} \sqrt{\frac{m}{kT}} \\
&=&  \sqrt{\frac{2m}{\pi kT}} \\
\end{gather*}$$


### (b) proof 最有可能的速度 $\sqrt{\frac{2kT}{m}}$ 

$$\begin{gather*}
0 &=& \frac{d}{dv} \left[ f(v) \right]  \\
0 &\overset{\text{已知 1}}{=}& \frac{d}{dv} \left[ 4\pi \left(\frac{m}{2\pi kT}\right)^{\frac{3}{2}} v^2 e^{-\frac{mv^2}{2kT}} \right]  \\
0 &=& \frac{d}{dv} \left[ v^2 e^{-\frac{mv^2}{2kT}} \right]  \\
0 &=& 2ve^{-\frac{mv^2}{2kT}} + v^2  \left( e^{-\frac{mv^2}{2kT}} \left( - \frac{m2v}{2kT} \right) \right)\\
0 &=&  v e^{-\frac{mv^2}{2kT}} \left( 2 - \frac{mv^2}{kT} \right)  \\
0 &=&  2 - \frac{mv^2}{kT}   \\
\frac{mv^2}{kT}&=&  2     \\
v &=&  \sqrt{\frac{2kT}{m}}    \\
\end{gather*}$$

+++

## Question 3

Show that the median energy $\varepsilon_{\text{med}}$ in a free-electron gas at $T=0\text{ K}$ equal to $\frac{\varepsilon_F}{2^{\frac{2}{3}}} = 0.630\varepsilon_F$.

+++

## Question 3 - Answer



### 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】總粒子數與狀態密度的積分關係（Relation between total particle number and density of states） ：**

  $$N =\int_0^{\infty} g(\varepsilon) f_{\text{FD}}(\varepsilon)  d\varepsilon$$

  * $N$ : 系統中的總電子數 (Total number of electrons) [無單位]
  * $g(\varepsilon)$ : 能階狀態密度函數 (Density of states) $[\text{J}^{-1}],[\text{eV}^{-1}]$
  * $f_{\text{FD}}(\varepsilon)$ : 費米–狄拉克分佈函數 (Fermi-Dirac distribution function) [無單位]
  * $\varepsilon $ : 電子的能量狀態 (Energy state) $[\text{J}],[\text{eV}]$

* **【已知 2】  三維自由電子氣體的狀態密度函數（Density of states for 3D free electron gas） ：**

  $$g(\varepsilon) = C \varepsilon^{\frac{1}{2}}$$

  * $C$ : 與電子質量及普朗克常數相關的常數係數 (Proportionality constant) $[\text{J}^{-3/2}]$
  * $\varepsilon^{\frac{1}{2}}$ : 能量的二分之一次方，代表三維空間中狀態密度隨能量的開根號成正比
  * $\varepsilon $ : 電子的能量狀態 (Energy state) $[\text{J}],[\text{eV}]$

* **【已知 3】 費米–狄拉克分佈（Fermi-Dirac distribution） ：**

  $$f_{\text{FD}}(\varepsilon) = \frac{1}{e^{\frac{\varepsilon - \mu}{kT}} + 1}$$

  * $\mu $ : 化學勢 (Chemical potential) $[\text{J}],[\text{eV}]$
  * $k$ : 波茲曼常數 (Boltzmann constant) $k \approx 1.38 \times 10^{-23} \text{ J}\cdot\text{K}^{-1}$
  * $T$ : 絕對溫度 (Absolute temperature) $[\text{K}]$



* **【假設 1】絕對零度下的極限狀態（Limit behavior at absolute zero, T = 0 K） ：**  當系統處於絕對零度時，化學勢 $\mu $ 定義為費米能階 $\varepsilon _{F}$，分佈函數會簡化為階梯函數（Step function）。 

  * (a) 限制條件 $\varepsilon < \varepsilon_F$ 下的分佈函數：
    
  $$\begin{gather*}
  \int_0^{\infty} g(\varepsilon) f_{\text{FD}}(\varepsilon) \ d\varepsilon  &=& \int_0^{\varepsilon_F} g(\varepsilon) f_{\text{FD}}(\varepsilon) \ d\varepsilon + \int_{\varepsilon_F}^{\infty} g(\varepsilon) f_{\text{FD}}(\varepsilon)  \ d\varepsilon\\
  &=& \int_0^{\varepsilon_F} g(\varepsilon) \cdot f_{\text{FD}}(\varepsilon) \ d\varepsilon + \int_{\varepsilon_F}^{\infty} g(\varepsilon) \cdot  0  \ d\varepsilon\\
  &=& \int_0^{\varepsilon_F} g(\varepsilon) f_{\text{FD}}(\varepsilon)  \   d\varepsilon \\
  \end{gather*}$$

  * (b) 利用階梯函數特性拆解並化簡總粒子數積分：

  $$\begin{gather*}
  f_{\text{FD}}(\varepsilon) &\overset{\text{已知 3}}{=}& \frac{1}{e^{\frac{\varepsilon - \mu}{kT}} + 1} \\
  &\overset{\text{假設 1}}{=}& \lim\limits_{T \to 0} \frac{1}{e^{\frac{\varepsilon - \mu}{kT}} + 1} \\
  &=&  \frac{1}{0 + 1} \\
  &=&  1 \\
  \end{gather*}$$

  * $g(\varepsilon)$ : 能階狀態密度函數 (Density of states) $[\text{J}^{-1}],[\text{eV}^{-1}]$
  * $f_{\text{FD}}(\varepsilon)$ : 費米–狄拉克分佈函數 (Fermi-Dirac distribution function) [無單位]
  * $\varepsilon $ : 電子的能量狀態 (Energy state) $[\text{J}],[\text{eV}]$
  * $\varepsilon_{F}$ : 費米能階 (Fermi energy) $[\text{J}]$ 或 $[\text{eV}]$，即絕對零度時電子填充的最高能量邊界
  * $k$ : 波茲曼常數 (Boltzmann constant) $k \approx 1.38 \times 10^{-23} \text{ J}\cdot\text{K}^{-1}$
  * $T$ : 絕對溫度 (Absolute temperature) $[\text{K}]$
  * $\mu $ : 化學勢 (Chemical potential) $[\text{J}],[\text{eV}]$


### proof 

$$\begin{gather*}
N_{\text{med}} &=& \frac{1}{2} N\\
\int_0^{\varepsilon_{\text{med}}} g(\varepsilon) f_{\text{FD}}(\varepsilon)\  d\varepsilon &\overset{\text{已知 1}}{=}& \frac{1}{2} \int_0^{\infty} g(\varepsilon) f_{\text{FD}}(\varepsilon)\  d\varepsilon \\
\int_0^{\varepsilon_{\text{med}}} g(\varepsilon) f_{\text{FD}}(\varepsilon)\  d\varepsilon  &\overset{\text{假設 1(a)}}{=}& \frac{1}{2} \int_0^{\varepsilon_F} g(\varepsilon) f_{\text{FD}}(\varepsilon)\   d\varepsilon \\
\int_0^{\varepsilon_{\text{med}}} g(\varepsilon) \cdot 1 \  d\varepsilon &\overset{\text{假設 1(b)}}{=}& \frac{1}{2} \int_0^{\varepsilon_F} g(\varepsilon) \cdot 1 \ d\varepsilon \\
\int_0^{\varepsilon_{\text{med}}} C \varepsilon^{\frac{1}{2}} \  d\varepsilon &\overset{\text{已知 2}}{=}& \frac{1}{2} \int_0^{\varepsilon_F} C \varepsilon^{\frac{1}{2}} \ d\varepsilon \\
C \left[ \frac{2}{3} \varepsilon^{\frac{3}{2}} \right]_0^{\varepsilon_{\text{med}}} &=&\frac{1}{2} C \left[ \frac{2}{3} \varepsilon^{\frac{3}{2}} \right]_0^{\varepsilon_F} \\
\varepsilon_{\text{med}}^{\frac{3}{2}} &=&\frac{1}{2} \varepsilon_F^{\frac{3}{2}} \\
\varepsilon_{\text{med}} &=& 2^{-\frac{2}{3}} \varepsilon_F \\
\varepsilon_{\text{med}} &\approx& 0.630 \varepsilon_F \\
\end{gather*}$$


+++

## Question 4

The Fermi energy in silver ($\text{Ag}$) is $5.51\text{ eV}$. 

* (a) What is the average energy of the free electrons in silver at $0\text{ K}$? 
* (b) What temperature is necessary for the average molecular energy in an ideal gas to have this value? 
* (c) What is the speed of an electron with this energy?


+++

## Question 4 - Answer



### 假設與已知 (Assumptions & Preliminaries)


* **【已知 1】總粒子數與狀態密度的積分關係（Relation between total particle number and density of states） ：**
  
  $$N =\int_0^{\infty} g(\varepsilon) f_{\text{FD}}(\varepsilon)  d\varepsilon$$

  * $N$ : 系統中的總電子數 (Total number of electrons) [無單位]
  * $g(\varepsilon)$ : 能階狀態密度函數 (Density of states) $[\text{J}^{-1}],[\text{eV}^{-1}]$
  * $f_{\text{FD}}(\varepsilon)$ : 費米–狄拉克分佈函數 (Fermi-Dirac distribution function) [無單位]
  * $\varepsilon $ : 電子的能量狀態 (Energy state) $[\text{J}],[\text{eV}]$

* **【已知 2】總和粒子能量與狀態密度的積分關係 ：**
  
  $$U =\int_0^{\infty} \varepsilon g(\varepsilon) f_{\text{FD}}(\varepsilon)  d\varepsilon$$

  * $U$ : 系統中的總能量 (Total energy of the system) $[\text{J}]$
  * $g(\varepsilon)$ : 能階狀態密度函數 (Density of states) $[\text{J}^{-1}],[\text{eV}^{-1}]$
  * $f_{\text{FD}}(\varepsilon)$ : 費米–狄拉克分佈函數 (Fermi-Dirac distribution function) [無單位]
  * $\varepsilon $ : 電子的能量狀態 (Energy state) $[\text{J}],[\text{eV}]$


* **【已知 3】  三維自由電子氣體的狀態密度函數（Density of states for 3D free electron gas） ：**

  $$g(\varepsilon) = C \varepsilon^{\frac{1}{2}}$$

  * $C$ : 與電子質量及普朗克常數相關的常數係數 (Proportionality constant) $[\text{J}^{-3/2}]$
  * $\varepsilon^{\frac{1}{2}}$ : 能量的二分之一次方，代表三維空間中狀態密度隨能量的開根號成正比
  * $\varepsilon $ : 電子的能量狀態 (Energy state) $[\text{J}],[\text{eV}]$

* **【已知 4】 費米–狄拉克分佈（Fermi-Dirac distribution） ：**

  $$f_{\text{FD}}(\varepsilon) = \frac{1}{e^{\frac{\varepsilon - \mu}{kT}} + 1}$$

  * $\mu $ : 化學勢 (Chemical potential) $[\text{J}],[\text{eV}]$
  * $k$ : 波茲曼常數 (Boltzmann constant) $k \approx 1.38 \times 10^{-23} \text{ J}\cdot\text{K}^{-1}$
  * $T$ : 絕對溫度 (Absolute temperature) $[\text{K}]$



* **【假設 1】絕對零度下的極限狀態（Limit behavior at absolute zero, T = 0 K） ：**  當系統處於絕對零度時，化學勢 $\mu $ 定義為費米能階 $\varepsilon _{F}$，分佈函數會簡化為階梯函數（Step function）。 

  * (a) 限制條件 $\varepsilon < \varepsilon_F$ 下的分佈函數：
    
  $$\begin{gather*}
  \int_0^{\infty} g(\varepsilon) f_{\text{FD}}(\varepsilon) \ d\varepsilon  &=& \int_0^{\varepsilon_F} g(\varepsilon) f_{\text{FD}}(\varepsilon) \ d\varepsilon + \int_{\varepsilon_F}^{\infty} g(\varepsilon) f_{\text{FD}}(\varepsilon)  \ d\varepsilon\\
  &=& \int_0^{\varepsilon_F} g(\varepsilon) \cdot f_{\text{FD}}(\varepsilon) \ d\varepsilon + \int_{\varepsilon_F}^{\infty} g(\varepsilon) \cdot  0  \ d\varepsilon\\
  &=& \int_0^{\varepsilon_F} g(\varepsilon) f_{\text{FD}}(\varepsilon)  \   d\varepsilon \\
  \end{gather*}$$

  * (b) ：
    
  $$\begin{gather*}
  \int_0^{\infty} \varepsilon g(\varepsilon) f_{\text{FD}}(\varepsilon) \ d\varepsilon  &=& \int_0^{\varepsilon_F} \varepsilon  g(\varepsilon) f_{\text{FD}}(\varepsilon) \ d\varepsilon + \int_{\varepsilon_F}^{\infty} \varepsilon g(\varepsilon) f_{\text{FD}}(\varepsilon)  \ d\varepsilon\\
  &=& \int_0^{\varepsilon_F} \varepsilon g(\varepsilon) \cdot f_{\text{FD}}(\varepsilon) \ d\varepsilon + \int_{\varepsilon_F}^{\infty} \varepsilon g(\varepsilon) \cdot  0  \ d\varepsilon\\
  &=& \int_0^{\varepsilon_F} \varepsilon  g(\varepsilon) f_{\text{FD}}(\varepsilon)  \   d\varepsilon \\
  \end{gather*}$$


  * (c) 利用階梯函數特性拆解並化簡總粒子數積分：

  $$\begin{gather*}
  f_{\text{FD}}(\varepsilon) &\overset{\text{已知 4}}{=}& \frac{1}{e^{\frac{\varepsilon - \mu}{kT}} + 1} \\
  &\overset{\text{假設 1}}{=}& \lim\limits_{T \to 0} \frac{1}{e^{\frac{\varepsilon - \mu}{kT}} + 1} \\
  &=&  \frac{1}{0 + 1} \\
  &=&  1 \\
  \end{gather*}$$

  * $g(\varepsilon)$ : 能階狀態密度函數 (Density of states) $[\text{J}^{-1}],[\text{eV}^{-1}]$
  * $f_{\text{FD}}(\varepsilon)$ : 費米–狄拉克分佈函數 (Fermi-Dirac distribution function) [無單位]
  * $\varepsilon $ : 電子的能量狀態 (Energy state) $[\text{J}],[\text{eV}]$
  * $\varepsilon_{F}$ : 費米能階 (Fermi energy) $[\text{J}],[\text{eV}]$，即絕對零度時電子填充的最高能量邊界
  * $k$ : 波茲曼常數 (Boltzmann constant) $k \approx 1.38 \times 10^{-23} \text{ J}\cdot\text{K}^{-1} \approx 8.617 \times 10^{-5} \text{ eV}\cdot\text{K}^{-1} $
  * $T$ : 絕對溫度 (Absolute temperature) $[\text{K}]$
  * $\mu $ : 化學勢 (Chemical potential) $[\text{J}],[\text{eV}]$

* **【已知 5】 理想氣體分子平均動能 ：**
  
  $$\langle E \rangle = \frac{3}{2}kT$$

  * $\langle E \rangle$ : 理想氣體平均分子動能 (Average kinetic energy) $[\text{J}]$
  * $k$ : 波茲曼常數 (Boltzmann constant) $k \approx 1.38 \times 10^{-23} \text{ J}\cdot\text{K}^{-1} \approx 8.617 \times 10^{-5} \text{ eV}\cdot\text{K}^{-1} $
  * $T$ : 絕對溫度 (Absolute temperature) $[\text{K}]$

* **【已知 6】 非相對論動能公式-電子 ：**
  
  $$\begin{gather*}
  E &=& \frac{1}{2}m_ev^2 \\
  v &=& \sqrt{\frac{2E}{m_e}} \\
  \end{gather*}$$

  * $E$ : 電子的非相對論性動能 (Non-relativistic kinetic energy) $[\text{J}],[\text{eV}]$
  * $m_{e}$ : 電子靜止質量 (Electron rest mass) $m_e \approx 9.109 \times 10^{-31} \text{ kg}$
  * $v$ : 電子的運動速率 (Electron speed) $[\text{m}\cdot\text{s}^{-1}]$

### (a) 平均能量

$$\begin{gather*}
\langle \varepsilon \rangle &=& \frac{\text{總能量 } }{\text{總電子數 } } \\
&\overset{\text{已知 1,2}}{=}& \frac{\int_0^{\infty} \varepsilon g(\varepsilon) f_{\text{FD}}(\varepsilon) \ d\varepsilon}{\int_0^{\infty} g(\varepsilon) f_{\text{FD}}(\varepsilon) \  d\varepsilon} \\
&\overset{\text{假設 1(a)(b)}}{=}& \frac{\int_0^{\varepsilon_F} \varepsilon g(\varepsilon) f_{\text{FD}}(\varepsilon) \  d\varepsilon}{\int_0^{\varepsilon_F} g(\varepsilon) f_{\text{FD}}(\varepsilon) \ d\varepsilon} \\
&\overset{\text{假設 1(c)}}{=}& \frac{\int_0^{\varepsilon_F} \varepsilon g(\varepsilon) \cdot 1 \  d\varepsilon}{\int_0^{\varepsilon_F} g(\varepsilon) \cdot 1 \   d\varepsilon} \\
&\overset{\text{已知 3}}{=}& \frac{\int_0^{\varepsilon_F} \varepsilon C \varepsilon^{\frac{1}{2}} \  d\varepsilon}{\int_0^{\varepsilon_F} C \varepsilon^{\frac{1}{2}} \  d\varepsilon} \\
&=& \frac{\int_0^{\varepsilon_F}  \varepsilon^{\frac{3}{2}} \  d\varepsilon}{\int_0^{\varepsilon_F} \varepsilon^{\frac{1}{2}} \  d\varepsilon} \\
&=& \frac{ \left[ \frac{2}{5} \varepsilon^{\frac{5}{2}}  \right]_0^{\varepsilon_F} }{\left[ \frac{2}{3} \varepsilon^{\frac{3}{2}}  \right]_0^{\varepsilon_F}} \\
&=& \frac{  \frac{2}{5} \varepsilon_F^{\frac{5}{2}}   }{ \frac{2}{3} \varepsilon_F^{\frac{3}{2}}  } \\
&=& \frac{3}{5} \varepsilon_F^{\frac{2}{2}}    \\
&=& \frac{3}{5} \varepsilon_F    \\
&\overset{\text{Q4}}{=}& \frac{3}{5} \times 5.51\text{ eV}    \\
&\approx& 3.306 \text{ eV}
\end{gather*}$$

### (b) 達到此能量所需的理想氣體溫度


$$\begin{gather*}
\langle E \rangle &=& \langle \varepsilon \rangle \\
\frac{3}{2}kT &\overset{\text{已知 5}}{=}& \langle \varepsilon \rangle \\
T &=& \frac{2}{3} \frac{\langle \varepsilon \rangle}{k} \\
T &\overset{\text{Q4(a)}}{=}& \frac{2}{3} \frac{3.306 \text{ eV}}{8.617 \times 10^{-5} \text{ eV}\cdot\text{K}^{-1}}  \\
T&\approx& 25577 \text{ K}
\end{gather*}$$

### (c) 有此能量的電子速率

$$\begin{gather*}
v  &\overset{\text{已知 6}}{=}& \sqrt{\frac{2E}{m_e}} \\
&\overset{\text{Q4(c)}}{=}& \sqrt{\frac{2 \langle \varepsilon \rangle}{m_e}} \\
&\overset{\text{Q4(a),已知 6}}{=}& \sqrt{\frac{2 \times 3.306 \text{ eV} \times (1.602 \times 10^{-19} \text{ J}\cdot \text{ eV}^{-1}) }{9.109 \times 10^{-31} \text{ kg}}} \\
&\approx& 1.078 \times 10^6 \text{ m} \cdot \text{ s}^{-1}
\end{gather*}$$

+++

## Question 5

An electron gas at the temperature $T$ has a Fermi energy of $\varepsilon_F$. 
* (a) At what energy is there a $5.00$ percent probability that a state of that energy is occupied? 
* (b) At what energy is there a $95.00$ percent probability that a state of that energy is occupied? Express the answers in terms of $\varepsilon_F$ and $kT$.

+++

## Question 5 - Answer


### 假設與已知 (Assumptions & Preliminaries)




* **【已知 1】 費米–狄拉克分佈（Fermi-Dirac distribution） ：**

  $$\begin{gather*}
  f_{\text{FD}}(\varepsilon) &=& \frac{1}{e^{\frac{\varepsilon - \mu}{kT}} + 1} \\
  &=& \frac{1}{e^{\frac{\varepsilon - \varepsilon_F}{kT}} + 1} \\
  \end{gather*}$$

  * $\mu $ : 化學勢 (Chemical potential) $[\text{J}],[\text{eV}]$ ，在常溫近似下 $\mu \approx \varepsilon_F$
  * $k$ : 波茲曼常數 (Boltzmann constant) $k \approx 1.38 \times 10^{-23} \text{ J}\cdot\text{K}^{-1}$
  * $T$ : 絕對溫度 (Absolute temperature) $[\text{K}]$
  * $\varepsilon_{F}$ : 費米能階 (Fermi energy) $[\text{J}],[\text{eV}]$，即絕對零度時電子填充的最高能量邊界


###  (a) solve specific energy for electron occupied in $5 \%$ 

$$\begin{gather*}
\frac{1}{20} &=& f_{\text{FD}}(\varepsilon) \\
\frac{1}{20} &\overset{\text{已知 1}}{=}& \frac{1}{e^{\frac{\varepsilon - \varepsilon_F}{kT}} + 1} \\
20 &=& e^{\frac{\varepsilon - \varepsilon_F}{kT}} + 1 \\
19 &=& e^{\frac{\varepsilon - \varepsilon_F}{kT}}  \\
\ln (19) &=& \frac{\varepsilon - \varepsilon_F}{kT}  \\
kT \ln (19) + \varepsilon_F &=& \varepsilon   \\
\end{gather*}$$

###  (b) solve specific energy for electron occupied in $95 \%$ 

$$\begin{gather*}
\frac{19}{20} &=& f_{\text{FD}}(\varepsilon) \\
\frac{19}{20} &\overset{\text{已知 1}}{=}& \frac{1}{e^{\frac{\varepsilon - \varepsilon_F}{kT}} + 1} \\
\frac{20}{19} &=& e^{\frac{\varepsilon - \varepsilon_F}{kT}} + 1 \\
\frac{1}{19} &=& e^{\frac{\varepsilon - \varepsilon_F}{kT}}  \\
-\ln (19) &=& \frac{\varepsilon - \varepsilon_F}{kT}  \\
-kT \ln (19) + \varepsilon_F &=& \varepsilon   \\
\end{gather*}$$



+++
