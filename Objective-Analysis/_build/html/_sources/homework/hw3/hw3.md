# Objective Analysis Week 03 Homework

## Question 1. Extended Monty Hall Problem with Four Doors

A prize is hidden behind one of four doors, while the other three doors hide goats. Assume that the prize is equally likely to be behind any door. The game proceeds according to the following rules:

1. You first choose one door, but it remains closed.
2. The host knows where the prize is. From the three doors that you did not choose, the host opens two doors that both hide goats.
3. If the host has more than one possible pair of goat doors to open, the host selects one of the possible pairs at random.
4. Exactly two doors now remain closed: your original choice and one other door. You may either stay with your original choice or switch to the other unopened door.


Answer the following questions. Clearly state the events and conditional probabilities used in your reasoning.

* (a) Before the host opens any doors, what is the probability that your initial choice contains the prize?
* (b) What is the probability of winning if you always stay with your initial choice?
* (c) What is the probability of winning if you always switch to the only other unopened door?
* (d) Which strategy should you use? Explain why the host's action changes the information available to you but does not change whether your initial choice was correct.

### 中文翻譯

> **問題 1：四扇門的延伸版蒙提霍爾問題**
>
> 獎品藏在四扇門其中一扇的後面，其餘三扇門後面都是山羊。假設獎品在每一扇門後面的機率都相同。遊戲依照以下規則進行：
>
> 1. 你先選擇一扇門，但這扇門保持關閉。
> 2. 主持人知道獎品在哪裡。主持人從你沒有選的三扇門中，打開兩扇後面都是山羊的門。
> 3. 若主持人有不只一組可打開的山羊門組合，則主持人會從可能的組合中隨機選一組打開。
> 4. 此時恰好剩下兩扇門是關著的：你最初選的門，以及另一扇門。你可以選擇堅持原本的選擇，或換到另一扇未打開的門。
>
> 回答以下問題。請在推理過程中清楚寫出所使用的事件與條件機率。
>
> * (a) 在主持人打開任何門之前，你最初選的門後有獎品的機率是多少？
> * (b) 若你總是堅持最初的選擇，獲勝機率是多少？
> * (c) 若你總是換到唯一剩下的另一扇未打開的門，獲勝機率是多少？
> * (d) 你應該採用哪一種策略？請解釋為什麼主持人的行動改變了你所能得到的資訊，卻沒有改變你最初的選擇是否正確。


## Answer 1.

假設參賽者最初選擇 第 1 扇門

* $D_i$：獎品藏在第 $i$ 扇門後（$i \in \{1, 2, 3, 4\}$）。

* $O_{jk}$：主持人打開第 $j$ 扇與第 $k$ 扇門（其中 $j, k \in \{2, 3, 4\}$ 且 $j < k$），這兩扇門後面都是山羊。

### (a)

$$P(D_1) = P(D_2) = P(D_3) = P(D_4) = \frac{1}{4}$$

第 1 扇門後有獎品的機率為 $\frac{1}{4}$


### (b)

總是堅持最初選擇（Stay）的獲勝機率


$$\begin{gather*}
P(D_1 \mid O_{23}) &=& \frac{P(O_{23} \mid D_1)P(D_1)}{P(O_{23})} \\
&=& \frac{\frac{1}{3} \times \frac{1}{4}}{\frac{1}{3}} \\
&=& \frac{1}{4} \\
\end{gather*}$$

* 各情況下主持人打開 2、3 號門的條件機率（Likelihood）：
  
  * 若獎品在 1 號門（$D_1$）：2、3、4 號門後都是山羊，主持人從 $\{(2,3), (2,4), (3,4)\}$ 三組中隨機選一組打開，故 $P(O_{23} \mid D_1) = \frac{1}{3}$。
  * 若獎品在 2 號門（$D_2$）：主持人不能打開有獎品的 2 號門，故 $P(O_{23} \mid D_2) = 0$。
  * 若獎品在 3 號門（$D_3$）：主持人不能打開 3 號門，故 $P(O_{23} \mid D_3) = 0$。
  * 若獎品在 4 號門（$D_4$）：主持人只能打開剩下的兩扇山羊門（2 號與 3 號），故 $P(O_{23} \mid D_4) = 1$

$$\begin{gather*}
P(O_{23}) &=& \sum_{i=1}^{4} P(O_{23} \mid D_i)P(D_i) \\ 
&=& \left(\frac{1}{3} \times \frac{1}{4}\right) + 0 + 0 + \left(1 \times \frac{1}{4}\right) \\ 
&=& \frac{1}{12} + \frac{1}{4} \\ 
&=& \frac{1}{3}
\end{gather*}$$



### (c)


$$\begin{gather*}
P(D_4 \mid O_{23}) &=& \frac{P(O_{23} \mid D_4)P(D_4)}{P(O_{23})} \\
&=& \frac{1 \times \frac{1}{4}}{\frac{1}{3}} \\
&=& \frac{3}{4}
\end{gather*}$$

因此，總是換門的獲勝機率為 $\frac{3}{4}$

### (d)

應該選擇 換門（Switch），因為獲勝機率是 $\frac{3}{4}$，為不換門（$\frac{1}{4}$）的 3 倍。

* 主持人總是能從你未選的 3 扇門中找出至少 2 扇山羊門並打開（不論你最初有沒有猜中）。因此「有兩扇山羊門被打開」這件事本身並未提供關於「第 1 扇門是否為獎品」的新資訊，所以 $P(D_1 \mid O_{23}) = P(D_1) = \frac{1}{4}$。   
* 然而，你未選的三扇門 $\{2, 3, 4\}$ 原本合起來擁有 $\frac{3}{4}$ 的獲勝機率。主持人知情且刻意避開獎品開門的動作，對 $\{2, 3, 4\}$ 進行了篩選，將原本分散在三扇門的 $\frac{3}{4}$ 機率全部濃縮（重新分配）到唯一留下的那扇未開門（第 4 扇門）上



## Question 2. A Scalar Bayesian Analysis and the Kalman Gain

In data assimilation, a background estimate and an observation are combined to obtain an analysis estimate, which can then be used as the initial condition for numerical weather prediction. In the scalar case, suppose the observation operator is the identity, so that the background and observation represent the same physical quantity at the same location.

Let the background estimate be $x_b$ and the observation be $y$. Assume that their errors are unbiased, mutually independent, and Gaussian, with variances $\sigma_b^2$ and $\sigma_o^2$, respectively. The analysis is

$$x_a = x_b + K (y - x_b), \quad K = \frac{\sigma_b^2}{\sigma_b^2 + \sigma_o^2}$$

where $K$ is the scalar Kalman gain. Under these assumptions, this expression is both the minimum-error-variance linear estimate and the maximum a posteriori (MAP) estimate.

Answer the following questions:

* (a) In a Bayesian formulation, write the prior density $p(x)$ implied by the background estimate and the likelihood $p(y \mid x)$ implied by the observation. Use Bayes' theorem to write the posterior density $p(x \mid y)$ up to a normalization constant. Identify which density is the prior and which is the posterior.
* (b) Show that maximizing $p(x \mid y)$ is equivalent to minimizing

  $$J(x) = \frac{(x - x_b)^2}{2\sigma_b^2} + \frac{(y - x)^2}{2\sigma_o^2}$$

  Differentiate $J(x)$ and verify that its minimizer has the Kalman-gain form given above.
* (c) Given

  $$x_b = 10^{\circ}\mathrm{C}, \quad y = 15^{\circ}\mathrm{C}, \quad \sigma_b^2 = 1^{\circ}\mathrm{C}^2, \quad \sigma_o^2 = 0.5^{\circ}\mathrm{C}^2$$

  calculate the Kalman gain and the analysis value that maximizes the posterior density. Briefly explain why the analysis lies closer to either the background or the observation.

### 中文翻譯

> **問題 2：純量貝氏分析與卡爾曼增益**
>
> 在資料同化中，會將背景估計值與觀測值結合，得到分析估計值，而分析值可作為數值天氣預報的初始條件。在純量情況下，假設觀測算子為恆等算子，使得背景值與觀測值代表同一位置上的同一物理量。
>
> 令背景估計值為 $x_b$、觀測值為 $y$。假設兩者的誤差皆為無偏、彼此獨立且服從高斯分布，變異數分別為 $\sigma_b^2$ 與 $\sigma_o^2$。分析值為
>
> $$x_a = x_b + K (y - x_b), \quad K = \frac{\sigma_b^2}{\sigma_b^2 + \sigma_o^2}$$
>
> 其中 $K$ 為純量卡爾曼增益。在上述假設下，此式同時是最小誤差變異數的線性估計，也是最大後驗（MAP）估計。
>
> 回答以下問題：
>
> * (a) 在貝氏架構下，寫出由背景估計值所隱含的先驗密度 $p(x)$，以及由觀測值所隱含的概似函數 $p(y \mid x)$。利用貝氏定理寫出後驗密度 $p(x \mid y)$（可忽略正規化常數）。指出哪一個密度是先驗、哪一個是後驗。
> * (b) 證明最大化 $p(x \mid y)$ 等價於最小化的 $J(x)$。
> 
>    $$J(x) = \frac{(x - x_b)^2}{2\sigma_b^2} + \frac{(y - x)^2}{2\sigma_o^2}$$
> 
>    對 $J(x)$ 微分，並驗證其最小值解具有上面給定的卡爾曼增益形式。
> * (c) 給定 $x_b = 10^{\circ}\mathrm{C}$、$y = 15^{\circ}\mathrm{C}$、$\sigma_b^2 = 1^{\circ}\mathrm{C}^2$、$\sigma_o^2 = 0.5^{\circ}\mathrm{C}^2$，計算卡爾曼增益，以及使後驗密度最大的分析值。簡要說明為什麼分析值會比較靠近背景值或觀測值。


## Answer 2.

### (a)


先驗機率密度函數 (Prior density, $p(x)$)： 

* 由背景場估計 $x_b$ 與其誤差變異數 $\sigma_b^2$ 決定，假設為常態分佈： 

$$p(x) = \frac{1}{\sqrt{2\pi}\sigma_b} \exp\left( -\frac{(x - x_b)^2}{2\sigma_b^2} \right)$$

* 概似函數 (Likelihood density, $p(y \mid x)$)： 給定真實狀態 $x$ 下，觀測值 $y$ 的條件機率密度（誤差變異數為 $\sigma_o^2$）：

$$p(y \mid x) = \frac{1}{\sqrt{2\pi}\sigma_o} \exp\left( -\frac{(y - x)^2}{2\sigma_o^2} \right)$$


* 後驗機率密度函數 (Posterior density, $p(x \mid y)$)： 根據貝氏定理 $p(x \mid y) = \frac{p(y \mid x)p(x)}{p(y)} \propto p(y \mid x)p(x)$，省去與 $x$ 無關的正規化常數後可寫為： 

$$p(x \mid y) \propto \exp\left[ -\left( \frac{(x - x_b)^2}{2\sigma_b^2} + \frac{(y - x)^2}{2\sigma_o^2} \right) \right]$$

指認： $p(x)$ 為 Prior（先驗密度），$p(x \mid y)$ 為 Posterior（後驗密度）。

### (b)

背景誤差與觀測誤差皆為無偏、獨立的高斯分布，故

$$p(x) \propto \exp\left[-\frac{(x - x_b)^2}{2\sigma_b^2}\right], \quad p(y \mid x) \propto \exp\left[-\frac{(y - x)^2}{2\sigma_o^2}\right]$$

由貝氏定理（$p(y)$ 與 $x$ 無關，視為正規化常數）：

$$\begin{gather*}
p(x \mid y) &\propto& p(y \mid x)\,p(x) \\
&\propto& \exp\left[-\frac{(x - x_b)^2}{2\sigma_b^2} - \frac{(y - x)^2}{2\sigma_o^2}\right] \\
&=& \exp\left[-J(x)\right]
\end{gather*}$$

取負對數：

$$-\ln p(x \mid y) = J(x) + \text{const}$$

因為 $\exp(\cdot)$ 為嚴格遞增函數，$p(x \mid y)$ 越大 $\Leftrightarrow$ $J(x)$ 越小，所以最大化 $p(x \mid y)$ 等價於最小化 $J(x)$。

* 對 $J(x)$ 微分並令其為 0：

$$\begin{gather*}
\frac{dJ}{dx} &=& \frac{x - x_b}{\sigma_b^2} - \frac{y - x}{\sigma_o^2} = 0 \\
x\left(\frac{1}{\sigma_b^2} + \frac{1}{\sigma_o^2}\right) &=& \frac{x_b}{\sigma_b^2} + \frac{y}{\sigma_o^2}
\end{gather*}$$

* 兩邊同乘 $\sigma_b^2 \sigma_o^2$：

$$\begin{gather*}
x\left(\sigma_o^2 + \sigma_b^2\right) &=& \sigma_o^2 x_b + \sigma_b^2 y \\
x_a &=& \frac{\sigma_o^2 x_b + \sigma_b^2 y}{\sigma_b^2 + \sigma_o^2} \\
&=& \frac{(\sigma_b^2 + \sigma_o^2) x_b + \sigma_b^2 (y - x_b)}{\sigma_b^2 + \sigma_o^2} \\
&=& x_b + \frac{\sigma_b^2}{\sigma_b^2 + \sigma_o^2}(y - x_b) \\
&=& x_b + K(y - x_b)
\end{gather*}$$

* 二階導數檢查：

$$\frac{d^2 J}{dx^2} = \frac{1}{\sigma_b^2} + \frac{1}{\sigma_o^2} > 0$$

故此臨界點為 $J(x)$ 的最小值，即 $p(x \mid y)$ 的最大值（MAP），其形式正是 $x_a = x_b + K(y - x_b)$，$K = \dfrac{\sigma_b^2}{\sigma_b^2 + \sigma_o^2}$。

### (c)

* 卡爾曼增益：

$$K = \frac{\sigma_b^2}{\sigma_b^2 + \sigma_o^2} = \frac{1}{1 + 0.5} = \frac{2}{3} \approx 0.667$$

* 分析值（使後驗密度最大的 $x$）：

$$\begin{gather*}
x_a &=& x_b + K(y - x_b) \\
&=& 10 + \frac{2}{3}(15 - 10) \\
&=& 10 + \frac{10}{3} \\
&\approx& 13.33^{\circ}\mathrm{C}
\end{gather*}$$

* 分析誤差變異數（補充）：

$$\sigma_a^2 = (1 - K)\sigma_b^2 = \frac{1}{3}{}^{\circ}\mathrm{C}^2$$

分析值 $13.33^{\circ}\mathrm{C}$ 較靠近觀測值（$15^{\circ}\mathrm{C}$），而非背景值（$10^{\circ}\mathrm{C}$）。

* 因為觀測誤差變異數 $\sigma_o^2 = 0.5$ 小於背景誤差變異數 $\sigma_b^2 = 1$，觀測值較可信。由 (b) 可知 $x_a = \dfrac{\sigma_o^2 x_b + \sigma_b^2 y}{\sigma_b^2 + \sigma_o^2}$，即以「變異數的倒數（精確度）」加權平均，觀測值的權重 $K = \frac{2}{3}$ 是背景值權重 $1 - K = \frac{1}{3}$ 的 2 倍。
* 且 $\sigma_a^2 = \frac{1}{3}$ 小於 $\sigma_b^2$ 與 $\sigma_o^2$，表示結合兩者後的估計比任一單獨來源更準確。




## Question 3. Bayesian Interpretation of a Heavy-Rain Warning

Suppose that, according to the local climatology, the probability of heavy rainfall on a randomly selected day is

$$P(H) = 0.10$$

where $H$ denotes the occurrence of heavy rainfall. A meteorological warning system has the following characteristics:

$$P(W \mid H) = 0.90, \quad P(W \mid H^c) = 0.20$$

where $W$ denotes that the system issues a heavy-rain warning, and $H^c$ denotes that heavy rainfall does not occur. Thus, the system issues a warning on 90% of heavy-rain days and on 20% of non-heavy-rain days.

Answer the following questions:

1. Identify the prior probability of heavy rainfall, the likelihood of receiving a warning when heavy rainfall occurs, and the false-positive probability of the warning system.
2. Using the law of total probability, calculate the overall probability that the system issues a warning:

   $$P(W) = P(W \mid H)P(H) + P(W \mid H^c)P(H^c)$$

3. Use Bayes' theorem to calculate the probability that heavy rainfall will occur given that a warning has been issued:

   $$P(H \mid W) = \frac{P(W \mid H)P(H)}{P(W)}$$

4. Consider 1000 days with the same statistical characteristics. Construct a table showing the expected numbers of:
   * heavy-rain days with a warning;
   * heavy-rain days without a warning;
   * non-heavy-rain days with a warning; and
   * non-heavy-rain days without a warning.

   Use this table to verify your answer to Question 3.
5. Explain why $P(H \mid W)$ is considerably smaller than $P(W \mid H)$. What role does the climatological frequency of heavy rainfall play in interpreting the warning?
6. During the wet season, suppose the prior probability of heavy rainfall increases to $P(H) = 0.30$, while the characteristics of the warning system remain unchanged. Recalculate $P(H \mid W)$ and explain why the posterior probability changes even though the warning system itself has not changed.

### 中文翻譯

> **問題 3：豪雨特報的貝氏解讀**
>
> 假設根據當地氣候統計，隨機挑選的某一天發生豪雨的機率為 $P(H) = 0.10$，其中 $H$ 表示發生豪雨。某氣象預警系統具有以下特性：
>
> $$P(W \mid H) = 0.90, \quad P(W \mid H^c) = 0.20$$
>
> 其中 $W$ 表示系統發布豪雨特報，$H^c$ 表示沒有發生豪雨。也就是說，在豪雨日中有 90% 會發布特報，而在非豪雨日中有 20% 會發布特報。
>
> 回答以下問題：
>
> 1. 指出豪雨的先驗機率、發生豪雨時收到特報的概似機率，以及預警系統的誤報（偽陽性）機率。
> 2. 利用全機率定理，計算系統發布特報的整體機率 $P(W)$。
> 3. 利用貝氏定理，計算在已發布特報的條件下，發生豪雨的機率 $P(H \mid W)$。
> 4. 考慮 1000 天具有相同統計特性的日子，建立一個表格，列出以下各類的期望天數：
>    * 有發布特報的豪雨日；
>    * 沒有發布特報的豪雨日；
>    * 有發布特報的非豪雨日；以及
>    * 沒有發布特報的非豪雨日。
>
>    用此表格驗證你在第 3 小題的答案。
> 5. 解釋為什麼 $P(H \mid W)$ 會明顯小於 $P(W \mid H)$。豪雨的氣候頻率在解讀特報時扮演什麼角色？
> 6. 在雨季期間，假設豪雨的先驗機率提高為 $P(H) = 0.30$，而預警系統的特性維持不變。重新計算 $P(H \mid W)$，並解釋為什麼即使預警系統本身沒有改變，後驗機率仍然會改變。


## Answer 3.

* $H$：發生豪雨；$H^c$：未發生豪雨。
* $W$：系統發布豪雨特報；$W^c$：未發布特報。

### 1.

* 豪雨的先驗機率（Prior）：$P(H) = 0.10$
* 發生豪雨時收到特報的概似機率（Likelihood）：$P(W \mid H) = 0.90$
* 誤報（偽陽性）機率（False-positive）：$P(W \mid H^c) = 0.20$

### 2.

$$\begin{gather*}
P(W) &=& P(W \mid H)P(H) + P(W \mid H^c)P(H^c) \\
&=& 0.90 \times 0.10 + 0.20 \times 0.90 \\
&=& 0.09 + 0.18 \\
&=& 0.27
\end{gather*}$$

系統發布特報的整體機率為 $0.27$

### 3.

$$\begin{gather*}
P(H \mid W) &=& \frac{P(W \mid H)P(H)}{P(W)} \\
&=& \frac{0.90 \times 0.10}{0.27} \\
&=& \frac{0.09}{0.27} \\
&=& \frac{1}{3} \approx 0.333
\end{gather*}$$

在已發布特報的條件下，真的發生豪雨的機率約為 $33.3\%$

### 4.

1000 天中，豪雨日 $1000 \times 0.10 = 100$ 天，非豪雨日 $1000 \times 0.90 = 900$ 天：

|                         | 有特報 $W$              | 無特報 $W^c$            | 合計   |
| ----------------------- | ----------------------- | ----------------------- | ------ |
| 豪雨日 $H$              | $100 \times 0.9 = 90$   | $100 \times 0.1 = 10$   | $100$  |
| 非豪雨日 $H^c$          | $900 \times 0.2 = 180$  | $900 \times 0.8 = 720$  | $900$  |
| 合計                    | $270$                   | $730$                   | $1000$ |

驗證：

$$P(W) = \frac{270}{1000} = 0.27, \quad P(H \mid W) = \frac{90}{270} = \frac{1}{3}$$

與第 2、3 小題的結果一致。

### 5.

* $P(W \mid H) = 0.9$ 是「在豪雨日中，有多少比例會發布特報」（偵測率）；$P(H \mid W) = \frac{1}{3}$ 則是「在有發布特報的日子中，有多少比例真的下豪雨」，兩者的條件方向相反。
* 由表格可見，雖然誤報率只有 20%，但非豪雨日（900 天）是豪雨日（100 天）的 9 倍，因此誤報天數（180 天）反而是正確特報天數（90 天）的 2 倍，使得每 3 次特報中只有 1 次真的下豪雨。
* 豪雨的氣候頻率 $P(H)$ 就是先驗機率（base rate）。當豪雨本身是罕見事件時，即使預警系統的偵測率很高，特報的可信度（$P(H \mid W)$）仍會被大量的非豪雨日誤報稀釋。因此解讀特報時必須同時考慮系統特性與氣候背景，忽略它會犯「基本比率謬誤（base-rate fallacy）」。

### 6.

$P(H) = 0.30$，$P(H^c) = 0.70$：

$$\begin{gather*}
P(W) &=& 0.90 \times 0.30 + 0.20 \times 0.70 \\
&=& 0.27 + 0.14 \\
&=& 0.41
\end{gather*}$$

$$\begin{gather*}
P(H \mid W) &=& \frac{0.90 \times 0.30}{0.41} \\
&=& \frac{0.27}{0.41} \\
&\approx& 0.659
\end{gather*}$$

後驗機率由 $0.333$ 上升到約 $0.659$。

* 以勝算（odds）形式表示貝氏定理：

$$\frac{P(H \mid W)}{P(H^c \mid W)} = \frac{P(W \mid H)}{P(W \mid H^c)} \times \frac{P(H)}{P(H^c)}$$

* 預警系統的特性決定了概似比 $\frac{P(W \mid H)}{P(W \mid H^c)} = \frac{0.9}{0.2} = 4.5$，這在乾季與雨季都相同；改變的是先驗勝算：
  * 平時：$\frac{0.1}{0.9} \times 4.5 = 0.5$，換算為 $P(H \mid W) = \frac{0.5}{1.5} = \frac{1}{3}$
  * 雨季：$\frac{0.3}{0.7} \times 4.5 \approx 1.929$，換算為 $P(H \mid W) = \frac{1.929}{2.929} \approx 0.659$
* 後驗機率是「先驗資訊」與「觀測（特報）資訊」的結合。特報提供的證據強度不變，但雨季時豪雨本來就較常發生（先驗較高），且非豪雨日變少、誤報數量也隨之減少，所以同一個特報所代表的豪雨機率就提高了。



## Question 4. The Sleeping Beauty Paradox

Researchers put Sleeping Beauty to sleep on Sunday. They then toss a fair coin in another room.

* If **Heads**: She is woken up on Monday for an interview. Afterwards, she is given an amnesia-inducing drug and put back to sleep until the experiment ends.
* If **Tails**: She is woken up on Monday for an interview, given the amnesia drug, and put back to sleep. She is then woken up **again** on Tuesday for a second interview, and again given the drug.

During any interview, she has no idea what day it is, nor does she remember any previous awakenings. When she wakes up, the researchers ask her: "What is the probability that the coin landed Heads?"

* (a) **The 1/2 Position (No New Information)**

  From the perspective that "waking up" does not constitute new information:
  * Use Bayes' theorem to prove that her probability for Heads remains 1/2. Clearly define your prior probabilities and the likelihood of the event "she wakes up" under each coin outcome.
  * Briefly explain why the probability is not updated.
* (b) **The 1/3 Position (The Subjective Experience)**

  From the perspective of her subjective experience, prove that the probability of Heads should be updated to 1/3. Provide the following two derivations:
  * Suppose the entire experiment is repeated $2N$ times. Calculate the total number of "awakenings" she will experience, and how many of those awakenings occur when the coin is Heads.
  * List all possible mutually exclusive states she could be in upon waking (i.e., combinations of the day and the coin outcome). Apply the principle of indifference to these states (e.g., if she is told it is Monday, Heads and Tails are equally likely; if she is told it is Tails, waking up on Monday and Tuesday are indistinguishable experiences) to determine the probability of Heads.

### 中文翻譯

> **問題 4：睡美人悖論**
>
> 研究人員在星期日讓睡美人入睡，接著在另一個房間擲一枚公正的硬幣。
>
> * 若為**正面**：她會在星期一被叫醒接受訪談。之後讓她服用會導致失憶的藥物，並讓她繼續沉睡直到實驗結束。
> * 若為**反面**：她會在星期一被叫醒接受訪談，服用失憶藥物後再次入睡。接著她會在星期二**再次**被叫醒接受第二次訪談，然後再次服用藥物。
>
> 在任何一次訪談中，她都不知道當天是星期幾，也不記得之前任何一次被叫醒的經驗。每當她醒來時，研究人員都會問她：「硬幣擲出正面的機率是多少？」
>
> * (a) **1/2 立場（沒有新資訊）**
>
>   從「醒來」並不構成新資訊的觀點出發：
>   * 利用貝氏定理證明她認為正面的機率仍然是 1/2。清楚定義你的先驗機率，以及在各硬幣結果下「她醒來」這個事件的概似機率。
>   * 簡要說明為什麼機率沒有被更新。
> * (b) **1/3 立場（主觀經驗）**
>
>   從她主觀經驗的觀點出發，證明正面的機率應更新為 1/3。請提供以下兩種推導：
>   * 假設整個實驗重複進行 $2N$ 次。計算她總共會經歷幾次「醒來」，以及其中有幾次是在硬幣為正面時發生的。
>   * 列出她醒來時可能處於的所有互斥狀態（即「星期幾」與「硬幣結果」的組合）。對這些狀態套用無差異原則（例如：若告訴她今天是星期一，則正面與反面的可能性相同；若告訴她結果是反面，則在星期一醒來與在星期二醒來是無法區分的經驗），以求出正面的機率。


## Answer 4.

* $H$：硬幣為正面（Heads）；$T$：硬幣為反面（Tails）。
* $A$：「她在實驗中醒來（接受訪談）」。

### (a)

* 先驗機率：公正硬幣

$$P(H) = P(T) = \frac{1}{2}$$

* 概似機率：不論正面或反面，她都一定會至少被叫醒一次

$$P(A \mid H) = 1, \quad P(A \mid T) = 1$$

* 由貝氏定理：

$$\begin{gather*}
P(H \mid A) &=& \frac{P(A \mid H)P(H)}{P(A \mid H)P(H) + P(A \mid T)P(T)} \\
&=& \frac{1 \times \frac{1}{2}}{1 \times \frac{1}{2} + 1 \times \frac{1}{2}} \\
&=& \frac{1}{2}
\end{gather*}$$

機率沒有被更新的原因：

* 她在星期日入睡前就已經知道「自己一定會醒來」，因此「醒來」是在兩種硬幣結果下都必然發生的事件，概似比 $\frac{P(A \mid H)}{P(A \mid T)} = 1$。
* 一個在所有假設下發生機率都相同的觀測，無法區分正面或反面，不提供任何新資訊，所以後驗機率等於先驗機率 $\frac{1}{2}$。
* 此外，失憶藥物讓她無法分辨是第幾次醒來，醒來時也沒有得到任何關於日期或硬幣的額外線索。

### (b)

**推導一：重複實驗的頻率論證**

將整個實驗重複 $2N$ 次，平均而言有 $N$ 次正面、$N$ 次反面：

* 正面：每次實驗醒來 1 次（星期一），共 $N \times 1 = N$ 次醒來
* 反面：每次實驗醒來 2 次（星期一、星期二），共 $N \times 2 = 2N$ 次醒來
* 總醒來次數：$N + 2N = 3N$ 次

$$P(\text{Heads} \mid \text{醒來}) = \frac{\text{正面時的醒來次數}}{\text{總醒來次數}} = \frac{N}{3N} = \frac{1}{3}$$

從她主觀經驗來看，每一次醒來都是一個無法區分的經驗，而在所有醒來中只有 $\frac{1}{3}$ 是發生在正面的情況。

**推導二：無差異原則**

她醒來時可能處於的互斥狀態只有三種：

* $H_1$：正面、星期一
* $T_1$：反面、星期一
* $T_2$：反面、星期二

（「正面、星期二」不會發生，因為正面時她星期二不會被叫醒。）

$$P(H_1) + P(T_1) + P(T_2) = 1$$

* 若告訴她結果是反面，則星期一與星期二醒來的經驗完全無法區分，故

$$P(T_1 \mid T) = P(T_2 \mid T) \;\Rightarrow\; P(T_1) = P(T_2)$$

* 若告訴她今天是星期一，由於星期一不論硬幣結果她都會被叫醒（硬幣甚至可以在星期一訪談後才擲），正面與反面機率相同，故

$$P(H_1 \mid \text{Monday}) = P(T_1 \mid \text{Monday}) \;\Rightarrow\; P(H_1) = P(T_1)$$

* 因此 $P(H_1) = P(T_1) = P(T_2)$，代入總和為 1：

$$P(H_1) = P(T_1) = P(T_2) = \frac{1}{3}$$

$$P(\text{Heads}) = P(H_1) = \frac{1}{3}$$

