# Find extreme values under a constraint, using Lagrange Multiplier

## Define Lagrangian $\mathcal{L}$

To find the extreme values of a function $f(x,y)$ under the constraint $g(x,y)=c$, define the Lagrangian:

$$\mathcal{L}(x,y,\lambda) = f(x,y) - \lambda\big(g(x,y) - c\big)$$

Set all partial derivatives to $0$ and solve the equations.

$$\left\{ \begin{array}{rcl}
\dfrac{\partial \mathcal{L}}{\partial x} &=& 0 \\[8pt]
\dfrac{\partial \mathcal{L}}{\partial y} &=& 0 \\[8pt]
\dfrac{\partial \mathcal{L}}{\partial \lambda} &=& 0
\end{array} \right.$$

The first two equations say $\nabla f = \lambda \nabla g$; the last one is the constraint itself.
The solutions are only **candidates** — compare their $f$ values to decide max / min.

> Why it works: [03_proof.md](03_proof.md)　When it fails: [04_exceptions.md](04_exceptions.md)
