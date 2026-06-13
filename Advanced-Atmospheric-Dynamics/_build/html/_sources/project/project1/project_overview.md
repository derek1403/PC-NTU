
# Eigenfunctions and eigenvalues of the fully compressible model.

We begin with a fully compressible nonhydrostatic model

$$\begin{gather*}
\frac{Du}{Dt} &=&  -\frac{1}{\rho} \frac{\partial p}{\partial x}, \tag{1a} \\
\frac{Dv}{Dt} &=&  -\frac{1}{\rho} \frac{\partial p}{\partial y}, \tag{1b} \\
\frac{Dw}{Dt} &=&  -\frac{1}{\rho} \frac{\partial p}{\partial z} - g, \tag{1c} \\
\frac{D\rho}{Dt} &=&  -\rho \left( \frac{\partial u}{\partial x} + \frac{\partial v}{\partial y} + \frac{\partial w}{\partial z} \right), \tag{1d} \\
\frac{D\rho}{Dt} &=&  \frac{1}{c^2} \frac{Dp}{Dt}, \tag{1e}
\end{gather*}$$

where $c^2$ is the square of sound speed and $D/Dt = \partial/\partial t + u\partial/\partial x + v\partial/\partial y + w\partial/\partial z$.

Let us divide the pressure and density into isothermal basic states and deviation parts, i.e.,

$$\begin{gather*}
P(x, y, z, t) &=&  \bar{p}(z) + p'(x, y, z, t), \\
\rho(x, y, z, t) &=&  \bar{\rho}(z) + \rho'(x, y, z, t),
\end{gather*}$$

where $\partial\bar{p}/\partial z = -\bar{\rho}g$.

With a resting basic state in an isothermal atmosphere (temperature $T_0$), (1) can be linearized in the form (with the nonlinear terms on the right hand side)



$$\begin{gather*}
\frac{\partial}{\partial t} \left(\bar{\rho}^{\frac{1}{2}}u\right) + \frac{\partial}{\partial x} \left( \frac{p'}{\bar{\rho}^{\frac{1}{2}}} \right) &=&  N_1, \tag{2a} \\
\frac{\partial}{\partial t} \left(\bar{\rho}^{\frac{1}{2}}v\right) + \frac{\partial}{\partial y} \left( \frac{p'}{\bar{\rho}^{\frac{1}{2}}} \right) &=&  N_2, \tag{2b} \\
\frac{\partial}{\partial t} \left(\bar{\rho}^{\frac{1}{2}}w\right) + \left( \frac{\partial}{\partial z} + \Gamma \right) \left( \frac{p'}{\bar{\rho}^{\frac{1}{2}}} \right) + g \left( \frac{1}{\bar{\rho}^{\frac{1}{2}}} \left(\rho' - \frac{p'}{c^2}\right) \right) &=&  N_3, \tag{2c} \\
\frac{\partial}{\partial t} \left( \frac{p'}{\bar{\rho}^{\frac{1}{2}}} \right) + c^2 \left( \frac{\partial}{\partial x} \left(\bar{\rho}^{\frac{1}{2}}u\right) + \frac{\partial}{\partial y} \left(\bar{\rho}^{\frac{1}{2}}v\right) + \left( \frac{\partial}{\partial z} - \Gamma \right) \left(\bar{\rho}^{\frac{1}{2}}w\right) \right) &=&  N_4, \tag{2d} \\
\frac{\partial}{\partial t} \left( \frac{1}{\bar{\rho}^{\frac{1}{2}}} \left(\rho' - \frac{p'}{c^2}\right) \right) - \frac{N^2}{g} \left(\bar{\rho}^{\frac{1}{2}}w\right) &=&  N_5, \tag{2e}
\end{gather*}$$

where the constant parameters in the isothermal atmosphere are

$$\begin{gather*}
c^2 &=&  \gamma R_d T_0, \tag{3a} \\
\Gamma &=&  \frac{1}{2} \left( \frac{g}{c^2} - \frac{N^2}{g} \right), \tag{3b} \\
N^2 &=&  \frac{\kappa g}{H_s}, \tag{3c}
\end{gather*}$$

and

$$\begin{gather*}
H_s &=&  R_d T_0 / g. \tag{3d}
\end{gather*}$$

The $\gamma$, $R_d$, and $\kappa$ take the usual meaning in the thermodynamics.

Now define the vectors

$$\tilde{u} = \begin{pmatrix}
\bar{\rho}^{\frac{1}{2}} u \\
\bar{\rho}^{\frac{1}{2}} v \\
\bar{\rho}^{\frac{1}{2}} w \\
p' / \bar{\rho}^{\frac{1}{2}} \\
(\rho' - p'/c^2) / \bar{\rho}^{\frac{1}{2}}
\end{pmatrix} = \begin{pmatrix}
U \\
V \\
W \\
P \\
\Pi
\end{pmatrix},$$

and

$$\tilde{N} = (N_1, N_2, N_3, N_4, N_5)^T,$$

we can write (2) as

$$\frac{\partial \tilde{u}}{\partial t} + L\tilde{u} = \tilde{N}, \tag{4}$$

Where

$$L = \begin{pmatrix}
0 & 0 & 0 & \frac{\partial}{\partial x} & 0 \\
0 & 0 & 0 & \frac{\partial}{\partial y} & 0 \\
0 & 0 & 0 & \left(\frac{\partial}{\partial z} + \Gamma\right) & g \\
c^2 \frac{\partial}{\partial x} & c^2 \frac{\partial}{\partial y} & c^2 \left(\frac{\partial}{\partial z} - \Gamma\right) & 0 & 0 \\
0 & 0 & -\frac{N^2}{g} & 0 & 0
\end{pmatrix}.$$

Next we define the inner product of the vectors $\tilde{f}$ and $\tilde{g}$ as

$$(\tilde{f}, \tilde{g}) = \frac{1}{L_x L_y L_z} \int_{0}^{L_z} \int_{0}^{L_y} \int_{0}^{L_x} \left( f_1 g_1^* + f_2 g_2^* + f_3 g_3^* + \frac{1}{c^2} f_4 g_4^* + \frac{g^2}{N^2} f_5 g_5^* \right) dxdydz, \tag{5}$$

where the $f^*$ is the complex conjugate of $f$. All the components of $\tilde{f}$ and $\tilde{g}$ are periodic in $x \text{ and } y$ and $f_3 = g_3 = 0$ at $z = 0, L_z$ (bottom and top). With the inner product (5) we can show that

$$(L\tilde{f}, \tilde{g}) = -(\tilde{f}, L\tilde{g}), \tag{6}$$

i.e., the operator $L$ is skew-Hermitian. Skew-Hermitian operator with appropriate boundary conditions have three properties that are of extreme importance in physics, both quantum and classical. The three properties are
* (1) the eigenvalues of a skew-Hermitian operator are imaginary,
* (2) the eigenfunctions of a skew-Hermitian operator are orthogonal,
* (3) the eigenfunctions of a skew-Hermitian operator form a complete set.

Finally, we note that (6) is a energy norm, it consists of the kinetic energy $\bar{\rho}/2(u^2 + v^2 + w^2)$, the elastic energy $1/(2\bar{\rho})(p'^2/c^2)$ and the thermobaric energy ( the internal energy)

$$I = \frac{\bar{\rho}}{2} \frac{g^2}{N^2} \left( \frac{\theta'}{\bar{\theta}} \right)^2,$$

or with the linearized equation of state, $(\rho - p'/c^2)\bar{\rho}^{-1/2} = -\bar{\rho}^{-1/2}(\theta'/\bar{\theta})$ ( Eckart 1960),

or with the linearized equation of state, $(\rho' - p'/c^2)\bar{\rho}^{-1/2} = -\bar{\rho}^{1/2}(\theta'/\bar{\theta})$ ( Eckart 1960),

$$I = \frac{g^2}{N^2} \frac{\left( \rho' - \frac{p'}{c^2} \right)^2}{2\bar{\rho}},$$

Thus, we can find the normalized eigenvectors $\tilde{K}_{klmn}$ of L, which satisfy

$$L\tilde{K}_{klmn} = i\nu_{klmn}\tilde{K}_{klmn} \tag{7}$$

where $\nu_{klmn}$ is real, and $k, l, m$ can be related to the wavenumbers $\bar{k}, \bar{l}, \bar{m}$ by

$$\bar{k} = \frac{2\pi k}{L_x}, \quad \bar{l} = \frac{2\pi l}{L_y}, \quad \bar{m} = \frac{2\pi m}{L_z}.$$

The $\tilde{K}_{klmn}$ form a complete space.

For a given $k, l, m$, there are six $n$’s which must be considered.

(1) The first gives zero frequency and corresponds to steady, horizontally non-divergent flow. This is really the degeneracy of the internal gravity waves with the wave number vector points in the vertical.

(2) The second frequency corresponds to Lamb waves. This solution was first discovered by Laplace (1778-1779) in discussing thermal oscillations in the atmosphere. He effectively stated that there is a mode with equivalent depth equal to the scale height of the atmosphere, and this will satisfy the tidal equations. This mode is now usually called Lamb wave, following a more complete discussion by Lamb (1910). A feature of this mode is that the velocity is everywhere parallel to the earth’s surface, i.e., $w = 0$. The propagation speed is the speed of sound and has a value of about $300\text{ m s}^{-1}$. The eigenvectors are found to be

$$\tilde{K}_{klmn} = A_{klmn} \begin{pmatrix}
\bar{k} \\
\bar{l} \\
0 \\
\nu_{klmn} \\
0
\end{pmatrix} e^{i(\bar{k}x + \bar{l}y)} e^{-\Gamma z}$$
$$ . \tag{8a}$$

with the dispersion relationship

$$\nu_{klmn}^2 = c^2 (\bar{k}^2 + \bar{l}^2), \tag{8b}$$

and the normalization factor

$$A_{klmn} = \left( \frac{(\bar{k}^2 + \bar{l}^2)(1 - e^{-2\Gamma L_z})}{\Gamma L_z} \right)^{-\frac{1}{2}}, \tag{8c}$$

(3) The remaining frequencies are the four roots (two acoustic waves and two buoyancy waves) of

$$\frac{\nu_{klmn}^4}{c^2} - \nu_{klmn}^2 \left( \bar{k}^2 + \bar{l}^2 + \bar{m}^2 + \Gamma^2 + \frac{N^2}{c^2} \right) + (\bar{k}^2 + \bar{l}^2) N^2 = 0, \tag{9a}$$

with the eigenvectors

$$\tilde{K}_{klmn} = A_{klmn} \begin{pmatrix}
\bar{k} (\bar{m} \cos \bar{m}z - \Gamma \sin \bar{m}z) \\
\bar{l} (\bar{m} \cos \bar{m}z - \Gamma \sin \bar{m}z) \\
-\frac{(\bar{m}^2 + \Gamma^2)\nu_{klmn}^2}{N^2 - \nu_{klmn}^2} i \sin \bar{m}z \\
\nu_{klmn} (\bar{m} \cos \bar{m}z - \Gamma \sin \bar{m}z) \\
\frac{N^2}{g} \frac{(\bar{m}^2 + \Gamma^2)}{N^2 - \nu_{klmn}^2} \nu_{klmn} \sin \bar{m}z
\end{pmatrix} e^{i(\bar{k}x + \bar{l}y)}$$
$$ . \tag{9b}$$

Where

$$A_{klmn} = \left( \left( \frac{\bar{m}^2 + \Gamma^2}{N^2 - \nu_{klmn}^2} \right) \left( N^2 (\bar{k}^2 + \bar{l}^2) - \frac{\nu_{klmn}^4}{c^2} \right) \right)^{-\frac{1}{2}}. \tag{9c}$$

If we take the inner product of (4) with $\tilde{K}_{klmn}$ to obtain

$$\left( \frac{\partial \tilde{u}}{\partial t}, \tilde{K}_{klmn} \right) + (L\tilde{u}, \tilde{K}_{klmn}) = (\tilde{N}, \tilde{K}_{klmn}). \tag{10}$$

With the skew-Hermitian property, we can write the second term of (10) as

$$(L\tilde{u}, \tilde{K}_{klmn}) = -(\tilde{u}, L\tilde{K}_{klmn}) = i\nu_{klmn} (\tilde{u}, \tilde{K}_{klmn}). \tag{11}$$

Now define the transform pairs of

$$\hat{u}_{klmn}(t) = (\tilde{u}, \tilde{K}_{klmn}), \tag{12a}$$

with inverse

$$\tilde{u} = \sum_{klmn} \hat{u}_{klmn}(t) \tilde{K}_{klmn}(x, y, z), \tag{12b}$$

$\tilde{N}$ and $\hat{N}_{klmn}$ can be defined similarly.

We can use (12) to write (10) as a set of scalar equations

$$\frac{d\hat{u}_{klmn}(t)}{dt} + i\nu_{klmn}\hat{u}_{klmn}(t) = \hat{N}_{klmn}, \tag{13}$$

which are the desired spectral equations. Equation (13) can be easily integrated as

$$\hat{u}_{klmn}(t + \Delta t) = \hat{u}_{klmn}(t)e^{-i\nu_{klmn}(\Delta t)} + \int_{t}^{t+\Delta t} \hat{N}_{klmn} e^{i\nu_{klmn}(t' - t - \Delta t)} dt'. \tag{14}$$

The computational procedures are:
* (1) Predict $\hat{u}_{klmn}$ in spectral space.
* (2) Transform $\hat{u}_{klmn}$ to physical space to get $\tilde{u}$.
* (3) Evaluate $\tilde{N}$ in physical space.
* (4) Transform $\tilde{N}$ to spectral space to get $\hat{N}_{klmn}$.
* (5) Go to step (1).

In step (3) and (4), the transform method of Orszag (1970) can be used. If $k$ is the truncated wave number, it is then possible to evaluate the $\hat{N}_{klmn}$ exactly using $3k + 1$ points trapezoidal quadrature, which prevents aliasing error in the calculation of the transformation of the nonlinear term. Note that the treatment of linear term in (14) is exact, which enlarge the time step of integration without the CFL constraint of the fast linear waves.

### Reference
1. Eckart, C., 1960, ”Hydrodynamics of Ocean and Atmosphere.” Pergamon, Oxford.
2. Gill, A. E., 1982, ”Atmosphere-Ocean Dynamics.” Academic Press.


### Problems and Project 1

1. With the definition of (3), derive the left hand side of (2) from (1) (i.e., the linear part of (2)).
2. Show that $L$ is skew-Hermitian with respect to the inner product (5).
3. Show that the inner product (5) is a energy norm with the kinetic energy, the elastic energy, and the internal energy.
4. Discuss the dynamics of non-divergent flow, Lamb waves, acoustic waves, and buoyancy waves.
5. What are the frequency range for the Lamb waves, acoustic waves, and buoyancy waves. (hint: $(0, \infty)$, $[1.1N, \infty)$ and $(0, N]$.)
6. Derive (14) from (13). Show that the integration of (14) allows a time step larger than that allowed by the CFL constraint of the linear waves.
7. Why the use of $3k + 1$ points trapezoidal quadrature prevent the aliasing in the transform method?
8. Plot the frequency diagram with $\nu/N$, and $\bar{k}H_s$ as coordinates and curves with different $\bar{m}H_s$, as the figure below (Figure 6-17, p174 in Gill’s book).



![](./pic/Gill_Fig.6.18.png)

**Fig. 6.18.** Dispersion diagram for an isothermal atmosphere. Waves are possible only in the stippled regions and on the line for the Lamb wave. The curves in the stippled regions give the same information as that shown in Fig. 6.17 but in a different way. Acoustic waves (modified by gravity) have frequency greater than the acoustic cutoff frequency $N_{\text{A}} \approx 1.11N$, whereas internal waves have frequency less than the buoyancy frequency $N$. $k$ is the horizontal wavenumber, $m$ the vertical wavenumber, and $H_{\text{s}}$ the scale height. The horizontal component of the group velocity is given by the slope of the curves of constant $m$. The maximum value for internal waves is $\frac{2}{7}(10)^{1/2}c_{\text{s}} \approx 0.9c_{\text{s}}$, this value being obtained when $m = 0$ and $k = 0$, i.e., for long waves.
