# 疫情題目

## 背景描述

核酸檢驗是檢驗是否感染covid-19的最準確方式，但是成本高又慢。所以有人發明快篩試劑，快篩犧牲了部分準確率但是很快又便宜。
防疫期間做的非常好的台灣多虧快篩的普及能夠及時實施居家隔離，把疫情控制下來。在機場台灣會要求一定要做快篩，但是沒有外出的人則沒有要求，只有身體不適才會強烈要求需要快篩。

相反，有些國家防疫需要加強，他們對民眾實施普篩

有些人會疑惑，擁有充足快篩的時候，台灣是否需要普篩以追查出更多病毒攜帶者讓他居家隔離呢?病毒已經大流行的國家和病毒並不盛行的國家為什麼在普篩的決策上會有差異?

我們知道在疾病不流行的國家之中實施普篩只會篩出很多很多偽陽性


## rule 101

定義
* 實際是陽性的事件 $C$
* 實際是陰性的事件 $\widetilde{C}$
* 快篩結果是陽性 $+$
* 快篩結果是陰性 $\widetilde{+}$



### 已知條件

根據實驗室統計快篩偽陽率是 $\Pr(+ \mid \widetilde{C}) \approx 0.05$ 、快篩偽陰性假設是 $\Pr(\widetilde{+}\mid C ) \approx 0$

已知該區域感染比例 $\Pr(C) = 0.001$ 


求快篩是陽性且他真的是陽性的比例 $\Pr(C \mid +)$ 

問當他真的是陽性且測出來是陰性 偽陽性預測值（False Discovery Rate, FDR）$\Pr( \widetilde{C} \mid +)$
##



$$\begin{gather*}
\Pr(C \mid +) &=& \Pr(+ \mid C) \frac{\Pr(C)}{\Pr(+)}\\
&=& \Pr(+ \mid C) \frac{\Pr(C)}{\sum_{i} \Pr(+_i)} \\
&\overset{C\text{and}\widetilde{C}\text{互斥、完全包覆}+\text{的空間}}{=}& \Pr(+ \mid C) \frac{\Pr(C)}{\Pr(+ \mid C)\Pr(C)+\Pr(+\mid \widetilde{C})\Pr(\widetilde{C})} \\
&=& \left(1-\Pr(\widetilde{+} \mid C)\right) \frac{\Pr(C)}{\left(1-\Pr(\widetilde{+} \mid C)\right)\Pr(C)+\Pr(+\mid \widetilde{C})(1-\Pr(C))} \\
&=& \left(1-0\right) \frac{0.001}{\left(1-0\right)\times 0.001 +0.05 \times (1-0.001)} \\
&=& \frac{1}{51} \\
&\approx& 2\% \\
\end{gather*}$$


**change your believe**

$$\begin{gather*}
\Pr(\widetilde{C} \mid +) &=& 1-\Pr(C \mid +) \\
&=& 1-\frac{1}{51} \\
&=& \frac{50}{51} \\
\end{gather*}$$