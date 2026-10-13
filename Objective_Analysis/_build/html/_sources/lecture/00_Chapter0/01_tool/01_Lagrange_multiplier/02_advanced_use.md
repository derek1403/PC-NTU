# Find extreme values under multiple constraints, using Lagrange Multipliers

## Define Lagrangian $\mathcal{L}$

To find the extreme values of $f(x,y)$ under the constraints $g_1(x,y)=c_1$ and $g_2(x,y)=c_2$, define the Lagrangian with one multiplier per constraint:

$$\mathcal{L}(x,y,\lambda_1,\lambda_2) = f(x,y) - \lambda_1\big(g_1(x,y) - c_1\big) - \lambda_2\big(g_2(x,y) - c_2\big)$$

Set all partial derivatives to $0$ and solve the equations.

$$\left\{ \begin{array}{rcl}
\dfrac{\partial \mathcal{L}}{\partial x} &=& 0 \\[8pt]
\dfrac{\partial \mathcal{L}}{\partial y} &=& 0 \\[8pt]
\dfrac{\partial \mathcal{L}}{\partial \lambda_1} &=& 0 \\[8pt]
\dfrac{\partial \mathcal{L}}{\partial \lambda_2} &=& 0
\end{array} \right.$$

## For more constraints and more variables

Let $\mathbf{x}=[x_1,x_2,\dots,x_m]$ with $k$ constraints $g_n(\mathbf{x}) = c_n$ ($k < m$):

$$\mathcal{L}(\mathbf{x},\lambda_1,\dots,\lambda_k) = f(\mathbf{x}) - \sum_{n=1}^{k}\lambda_n\big(g_n(\mathbf{x}) - c_n\big)$$

$$\left\{ \begin{array}{rcl}
\dfrac{\partial \mathcal{L}}{\partial x_1} &=& 0 \\[8pt]
&\vdots& \\[8pt]
\dfrac{\partial \mathcal{L}}{\partial x_m} &=& 0 \\[8pt]
\dfrac{\partial \mathcal{L}}{\partial \lambda_1} &=& 0 \\[8pt]
&\vdots& \\[8pt]
\dfrac{\partial \mathcal{L}}{\partial \lambda_k} &=& 0
\end{array} \right.$$

That is $m + k$ equations for $m + k$ unknowns; the first $m$ say $\nabla f = \sum_{n} \lambda_n \nabla g_n$.
Requires the gradients $\nabla g_1,\dots,\nabla g_k$ to be linearly independent at the extremum (LICQ).

> Why it works: [03_proof.md](03_proof.md)　When it fails: [04_exceptions.md](04_exceptions.md)
