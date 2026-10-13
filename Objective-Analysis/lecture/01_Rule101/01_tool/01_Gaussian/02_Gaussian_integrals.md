# 高斯積分 (Gaussian Integrals)

高斯分布的正規化常數、變異數、峰度，全部歸結到同一族積分 $\int x^{n} e^{-ax^2}dx$。
只要先算出最基本的 $n=0$，其餘都能「對 $a$ 微分」一路推出來。

## 結果速查

| (編號) | 積分（$a > 0$） | 值 |
|---|---|---|
| (a) | $\int_{-\infty}^{\infty} e^{-ax^2}\,dx$ | $\sqrt{\dfrac{\pi}{a}}$ |
| (b) | $\int_{-\infty}^{\infty} x^2 e^{-ax^2}\,dx$ | $\dfrac{\sqrt{\pi}}{2}\,a^{-3/2}$ |
| (c) | $\int_{-\infty}^{\infty} x^4 e^{-ax^2}\,dx$ | $\dfrac{3\sqrt{\pi}}{4}\,a^{-5/2}$ |
| (d) | $\int_{-\infty}^{\infty} x^{2k+1} e^{-ax^2}\,dx$ | $0$ |
| (e) | $\int_{-\infty}^{\infty} g(x-c)\,dx$ | $\int_{-\infty}^{\infty} g(x)\,dx$ |

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】極座標面積元 (Polar Area Element)：** 把平面上的積分改用半徑與角度來切，每一小塊的面積是 $r\,dr\,d\theta$；多出來的 $r$ 正是讓 $e^{-ar^2}$ 可以積的關鍵。

  $$dx\,dy = r\,dr\,d\theta,\qquad x^2 + y^2 = r^2$$

* **【已知 2】積分號下微分 (Differentiation under the Integral Sign)：** 被積函數與其對參數的偏導數都連續、且積分收斂得夠快時，微分與積分可交換。

  $$\frac{d}{da}\left[\int g(x,a)\,dx\right] = \int \frac{\partial g}{\partial a}\,dx$$

* **【定義 1】基本積分 (Basic Integral)：**

  $$I(a) \overset{\text{def}}{=} \int_{-\infty}^{\infty} e^{-ax^2}\,dx$$

## proof

(a) 平方後變成二維積分，改用極座標：

$$\begin{gather*}
I(a) \cdot I(a) &\overset{\text{定義 1}}{=}& \int_{-\infty}^{\infty} e^{-ax^2}dx \int_{-\infty}^{\infty} e^{-ay^2}dy \\
&=& \iint e^{-a(x^2+y^2)}\,dx\,dy \\
&\overset{\text{已知 1}}{=}& \int_{0}^{2\pi}\int_{0}^{\infty} e^{-ar^2}\,r\,dr\,d\theta \\
&=& 2\pi \cdot \left[-\frac{1}{2a}e^{-ar^2}\right]_{0}^{\infty} \\
&=& \frac{\pi}{a}
\end{gather*}$$

$I > 0$，所以 $I(a) = \sqrt{\pi/a}$。

(b) 對 $a$ 微分一次，拉下一個 $-x^2$：

$$\begin{gather*}
\int_{-\infty}^{\infty} x^2 e^{-ax^2}\,dx &=& -\int_{-\infty}^{\infty} \frac{d}{da}\Big[e^{-ax^2}\Big] \,dx  \\
&\overset{\text{已知 2}}{=}& -\frac{d}{da}\left[\int_{-\infty}^{\infty} e^{-ax^2} \,dx \right] \\
&\overset{\text{定義 1}}{=}& -\frac{d}{da}\Big[I(a)\Big] \\
&\overset{\text{(a)}}{=}& -\frac{d}{da}\Big[\sqrt{\pi}\,a^{-1/2}\Big] \\
&=& \frac{\sqrt{\pi}}{2}\,a^{-3/2}
\end{gather*}$$

(c) 再微分一次：

$$\begin{gather*}
\int_{-\infty}^{\infty} x^4 e^{-ax^2}\,dx &=& -\int_{-\infty}^{\infty} \frac{d}{da}\left[x^2 e^{-ax^2}\right]\,dx \\
&\overset{\text{已知 2}}{=}& -\frac{d}{da}\left[\int_{-\infty}^{\infty} x^2 e^{-ax^2}\,dx\right] \\
&\overset{\text{(b)}}{=}& -\frac{d}{da}\left[\frac{\sqrt{\pi}}{2}\,a^{-3/2}\right] \\
&=& \frac{3\sqrt{\pi}}{4}\,a^{-5/2}
\end{gather*}$$

(d) $x^{2k+1}e^{-ax^2}$ 是奇函數，左右兩半互相抵消，積分為 $0$。

(e) 令 $u = x - c$，$du = dx$，積分範圍仍是 $(-\infty,\infty)$，所以平移不改變積分值。

## 在高斯分布上的用法

取 $a = \frac{1}{2\sigma^2}$，配合 (e) 把中心平移到 $\mu$：

* 由 (a)：$\int e^{-(x-\mu)^2/2\sigma^2}dx = \sigma\sqrt{2\pi}$，這就是正規化常數
* 由 (b)：$\int (x-\mu)^2 e^{-(x-\mu)^2/2\sigma^2}dx = \sigma^3\sqrt{2\pi}$，除以正規化常數得變異數 $\sigma^2$
* 由 (c)：$\int (x-\mu)^4 e^{-(x-\mu)^2/2\sigma^2}dx = 3\sigma^5\sqrt{2\pi}$，除以正規化常數得 $3\sigma^4$
