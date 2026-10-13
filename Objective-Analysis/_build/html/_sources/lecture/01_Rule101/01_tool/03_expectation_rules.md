# 期望值與變異數的運算規則 (Rules for Expectation and Variance)

期望值是「用機率加權的平均」，它是線性的；變異數不是線性的，但對**獨立**的變數可以直接相加。
這兩條是標準誤 $\sigma/\sqrt{N}$ 與樣本變異數除以 $N-1$ 的全部基礎。
本檔的大寫 $X$ 是隨機變數，小寫 $x$ 是積分變數或實現值（見 [03_notation_X_vs_x.md](../03_notation_X_vs_x.md)）。

## 結果速查

| (編號) | 規則 | 條件 |
|---|---|---|
| (a) | $\mathbb{E}[aX + b] = a\,\mathbb{E}[X] + b$ | 無 |
| (b) | $\mathbb{E}\big[\sum_i X_i\big] = \sum_i \mathbb{E}[X_i]$ | 無（不需獨立） |
| (c) | $\mathrm{Var}(X) = \mathbb{E}[X^2] - \mu^2$ | 無 |
| (d) | $\mathrm{Var}(aX + b) = a^2\,\mathrm{Var}(X)$ | 無 |
| (e) | $\mathbb{E}[X_iX_j] = \mathbb{E}[X_i]\,\mathbb{E}[X_j]$ | $X_i, X_j$ 獨立 |
| (f) | $\mathrm{Var}\big(\sum_i X_i\big) = \sum_i \mathrm{Var}(X_i)$ | 兩兩獨立 |

## 假設與已知 (Assumptions & Preliminaries)

* **【定義 1】期望值與變異數 (Expectation & Variance)：** 期望值是以機率密度 $f$ 加權的平均；變異數是「離平均多遠」平方後的期望值。

  * (a) $$\mathbb{E}[g(X)] \overset{\text{def}}{=} \int_{-\infty}^{\infty} g(x)\,f(x)\,dx$$

  * (b) $$\mu \overset{\text{def}}{=} \mathbb{E}[X]$$

  * (c) $$\mathrm{Var}(X) \overset{\text{def}}{=} \mathbb{E}\big[(X - \mu)^2\big]$$

  * (d) 多變數版本：同時有 $N$ 個隨機變數時，改用聯合密度對全部變數積分。
    $$\mathbb{E}[g(\mathbf{X})] \overset{\text{def}}{=} \int g(\mathbf{x})\,f(\mathbf{x})\,d\mathbf{x}$$

  * $X$ : 隨機變數 (Random variable)
  * $f$ : 機率密度函數 (PDF)，$\int f\,dx = 1$
  * $\mathbf{x} = (x_1,\dots,x_N)$ : $N$ 個變數排成的向量 (Vector of variables)
  * $f(\mathbf{x})$ : 聯合密度 (Joint PDF)
  * $d\mathbf{x} = dx_1\cdots dx_N$ : $N$ 維體積元 (Volume element)

* **【已知 1】積分的線性 (Linearity of the Integral)：**

  $$\int \big(a\,g + b\,h\big)\,d\mathbf{x} = a\int g\,d\mathbf{x} + b\int h\,d\mathbf{x}$$

* **【已知 2】獨立的定義 (Independence)：** 兩變數獨立，代表它們的聯合密度可以拆成各自密度的乘積，知道其中一個完全不影響另一個。

  $$f_{ij}(x_i, x_j) = f_i(x_i)\,f_j(x_j)$$

* **【已知 3】邊際密度 (Marginal Density)：** 把不關心的變數全部積掉，剩下的就是關心的那幾個變數自己的密度。這一步**不需要**獨立。

  (a) $$\int f(\mathbf{x})\,dx_1\cdots\widehat{dx_i}\cdots dx_N = f_i(x_i)$$

  (b) $$\int f(\mathbf{x})\,dx_1\cdots\widehat{dx_i}\cdots\widehat{dx_j}\cdots dx_N = f_{ij}(x_i, x_j)$$

  * $\widehat{dx_i}$ : 唯獨這個變數不積分
  * $f_i$ : $X_i$ 的邊際密度 (Marginal PDF)
  * $f_{ij}$ : $(X_i, X_j)$ 的聯合邊際密度 (Joint marginal PDF)

## proof

(a) 期望值線性：

$$\begin{gather*}
\mathbb{E}[aX + b] &\overset{\text{定義 1(a)}}{=}& \int (ax + b)\,f(x)\,dx \\
&\overset{\text{已知 1}}{=}& a\int x f\,dx + b\int f\,dx \\
&\overset{\text{定義 1(a)}}{=}& a\,\mathbb{E}[X] + b
\end{gather*}$$

(b) 和的期望值（不需要獨立）：

$$\begin{gather*}
\mathbb{E}\Big[\sum_i X_i\Big] &\overset{\text{定義 1(d)}}{=}& \int \Big(\sum_i x_i\Big) f(\mathbf{x})\,d\mathbf{x} \\
&\overset{\text{已知 1}}{=}& \sum_i \int x_i\, f(\mathbf{x})\,d\mathbf{x} \\
&\overset{\text{已知 3(a)}}{=}& \sum_i \int x_i\, f_i(x_i)\,dx_i \\
&\overset{\text{定義 1(a)}}{=}& \sum_i \mathbb{E}[X_i]
\end{gather*}$$

>『把每天的總收入拿來算平均，得到平均每天賺 300 元』的結果，跟『賣筆平均每天賺 100 元』加上『賣紙平均每天賺 200 元』是一模一樣的

(c) 展開平方：

$$\begin{gather*}
\mathrm{Var}(X) &\overset{\text{定義 1(c)}}{=}& \mathbb{E}\big[(X-\mu)^2\big] \\
&=& \mathbb{E}\big[X^2 - 2\mu X + \mu^2\big] \\
&\overset{\text{(a)(b)}}{=}& \mathbb{E}[X^2] - 2\mu\,\mathbb{E}[X] + \mu^2 \\
&\overset{\text{定義 1(b)}}{=}& \mathbb{E}[X^2] - 2\mu \cdot \mu + \mu^2 \\
&=& \mathbb{E}[X^2] - \mu^2
\end{gather*}$$

(d) 平移不改變離平均的距離，縮放 $a$ 倍則平方後變 $a^2$ 倍：

$$\begin{gather*}
\mathrm{Var}(aX + b) &\overset{\text{定義 1(c),(a)}}{=}& \mathbb{E}\left[\big((aX + b) - (a\mu + b) \big)^2\right] \\
&=& \mathbb{E}\big[(aX + b - a\mu - b)^2\big] \\
&=& \mathbb{E}\big[(aX  - a\mu )^2\big] \\
&\overset{\text{(a)}}{=}& a^2\,\mathbb{E}\big[(X - \mu)^2\big] \\
&\overset{\text{定義 1(c)}}{=}& a^2\,\mathrm{Var}(X)
\end{gather*}$$

(e) 獨立時期望值可拆：

$$\begin{gather*}
\mathbb{E}[X_iX_j] &\overset{\text{定義 1(d)}}{=}& \int x_i x_j\,f(\mathbf{x})\,d\mathbf{x} \\
&\overset{\text{已知 3(b)}}{=}& \iint x_i x_j\,f_{ij}(x_i,x_j)\,dx_i\,dx_j \\
&\overset{\text{已知 2}}{=}& \int x_i f_i(x_i)\,dx_i \int x_j f_j(x_j)\,dx_j \\
&\overset{\text{定義 1(a)}}{=}& \mathbb{E}[X_i]\,\mathbb{E}[X_j]
\end{gather*}$$

(f) 令 $\mu_i = \mathbb{E}[X_i]$，展開平方後交叉項的期望值為 $0$：

$$\begin{gather*}
\mathrm{Var}\Big(\sum_i X_i\Big) &\overset{\text{定義 1(c)}}{=}& \mathbb{E}\Big[\Big( \sum_i X_i -  \mathbb{E}\Big[\sum_i X_i \Big]\Big)^2\Big] \\
&=& \mathbb{E}\Big[\Big(\sum_i (X_i - \mu_i)\Big)^2\Big] \\
&=& \mathbb{E}\Big[\Big(\sum_i (X_i - \mu_i)\Big)\cdot \Big(\sum_j (X_j - \mu_j)\Big) \Big] \\
&=& \mathbb{E}\left[\sum_i (X_i - \mu_i)^2 + \sum_{i \neq j} (X_i - \mu_i)(X_j - \mu_j)\right] \\
&\overset{\text{(b)}}{=}& \sum_i \mathbb{E}\big[(X_i - \mu_i)^2\big] + \sum_{i \neq j} \mathbb{E}\big[(X_i - \mu_i)(X_j - \mu_j)\big] \\
&\overset{\text{(e)}}{=}& \sum_i \mathbb{E}\big[(X_i - \mu_i)^2\big] + \sum_{i \neq j} \mathbb{E}[X_i - \mu_i]\,\mathbb{E}[X_j - \mu_j] \\
&\overset{\text{(a)}}{=}& \sum_i \mathbb{E}\big[(X_i - \mu_i)^2\big] + \sum_{i \neq j} (\mathbb{E}[X_i] - \mu_i) \cdot (\mathbb{E}[X_j] - \mu_j)\\
&=& \sum_i \mathbb{E}\big[(X_i - \mu_i)^2\big] + 0 \\
&\overset{\text{定義 1(c)}}{=}& \sum_i \mathrm{Var}(X_i)
\end{gather*}$$
 
> 大氣資料常有自相關（今天熱、明天多半也熱），此時 (e) 不成立，(f) 的交叉項不為零，「變異數直接相加」會低估總變異。
