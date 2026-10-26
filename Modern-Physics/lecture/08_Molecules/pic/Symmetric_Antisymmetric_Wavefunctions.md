# Symmetric_Antisymmetric_Wavefunctions.png

**對應章節：** 8.2 電子共享
**插入位置：**「推導：對稱與反對稱的分子軌域」(c) 的 $\text{He}^+$ 極限條列之後、【物理知識回顧】之前
**課本對應：** 圖 8.5、圖 8.6

> 產圖前請先貼上 `00_STYLE_GUIDE.md` 的風格區塊。

---

## 中文提示詞

```
依共用風格畫上下兩列與右側比較欄，保留綠色對稱、紅色反對稱。
標題：8.2  對稱與反對稱的分子軌域 (Symmetric and Antisymmetric Molecular Orbitals)
導言：固定兩個相同質子於對稱位置、無破壞對稱性的外場；選取鏡射算符與
哈密頓量的共同本徵態，P²=1 給出鏡射奇偶性 ±1。
以兩個實數、已歸一化的氫1s軌域作 LCAO 近似；不是分子哈密頓量的精確解。

符號框：
ψ_S=ψ_a+ψ_b、ψ_A=ψ_a−ψ_b 為未歸一化組合；
S_ab=∫ψ_aψ_b dV，φ_S,A=(ψ_a±ψ_b)/√[2(1±S_ab)] 為歸一化組合。
與正文的 ψ̃_S,A 相同，此圖以 φ 簡寫，避免過密標記。

上列五格：ψ_a、ψ_b、較大R的ψ_S、較小R的ψ_S、合核角向示意。
下列五格：ψ_a、−ψ_b、較大R的ψ_A、較小R的ψ_A、合核角向示意。
橫軸取核間連線座標 z，兩核在 ±R/2，不能把帶正負值的軸標成距離r。
前四格縱軸為未歸一化振幅ψ；曲線按指定1s函數相加減，
不可強制畫中點為最大值或兩峰間的平台。反對稱組合在中點為零。
第五格另加虛線框「合核角向示意，不是固定基底的精確徑向解」：
上格s型，下格p_z型；標精確電子態可連到He⁺ 1s/2p，
但固定氫1s基底不會直接變成精確He⁺波函數。
反對稱未歸一化組合在R=0為零；只畫R→0重新歸一化後的形狀，不把零函數畫成非零。

右欄｜歸一化後才比較機率密度
取固定R=2a₀；重疊S_ab=e^(−R/a₀)[1+R/a₀+R²/(3a₀²)]。
沿z畫灰虛線ρ_ref=(ψ_a²+ψ_b²)/2，
綠線|φ_S|²=(ψ_a²+ψ_b²+2ψ_aψ_b)/[2(1+S_ab)]，
紅線|φ_A|²=(ψ_a²+ψ_b²−2ψ_aψ_b)/[2(1−S_ab)]。
在中點註|φ_A|²=0，|φ_S|²=2ψ_a²/(1+S_ab)。
不要標「機率必定兩倍」或任意指定中點是最高峰。
振幅正負以±標出；機率密度無負值，核電荷+號另列圖例。

底部三盒：
Pφ_S=+φ_S；Pφ_A=−φ_A；
是否鍵結須比較電子動能、庫侖作用與核間排斥的總能量。
對稱/反對稱在此是鏡射奇偶性，不是交換兩個電子。
```

## English Prompt

```
Use the shared style: two rows plus a right comparison column, green symmetric
and red antisymmetric. All visible labels Traditional Chinese.
Title: 8.2  對稱與反對稱的分子軌域 (Symmetric and Antisymmetric Molecular Orbitals).
State fixed identical nuclei, mirror-symmetric Hamiltonian, no symmetry-breaking
external field, and a simultaneous energy/parity eigenbasis with P²=1.
The two real normalized hydrogen 1s orbitals are an approximate LCAO basis.

Notation box: ψ_S,A=ψ_a±ψ_b are unnormalized;
S_ab=∫ψ_aψ_b dV; φ_S,A=(ψ_a±ψ_b)/√[2(1±S_ab)] are normalized.
Caption φ is shorthand for the text's ψ̃.
Five panels per row: individual orbitals, sum/difference at larger and smaller R,
and a separately framed united-atom ANGULAR illustration.
Use internuclear coordinate z, nuclei at ±R/2; vertical axis ψ for the first
four panels. Calculate sums, do not force a central maximum or a flat plateau.
The antisymmetric midpoint is zero.
Final panel label 合核角向示意：固定基底不是精確He⁺徑向解, s-type above, p_z-type below.
Exact electronic states correlate to He⁺ 1s/2p, but the fixed hydrogen basis
does not become those exact radial functions. At R=0 the unnormalized difference
vanishes; illustrate only the renormalized limiting shape as R→0.

RIGHT: normalized density comparison at R=2a₀.
S_ab=exp(−R/a₀)[1+R/a₀+R²/(3a₀²)].
Grey (ψ_a²+ψ_b²)/2; green (ψ_a²+ψ_b²+2ψ_aψ_b)/[2(1+S_ab)];
red (ψ_a²+ψ_b²−2ψ_aψ_b)/[2(1−S_ab)].
Midpoint labels |φ_A|²=0 and |φ_S|²=2ψ_a²/(1+S_ab).
No universal factor-two probability claim, no invented central peak.
Clearly separate amplitude signs from nuclear charges and nonnegative density.
Bottom: Pφ_S=+φ_S; Pφ_A=−φ_A; 鍵結須比較完整總能量.
Mirror parity here is not electron exchange symmetry.
```
