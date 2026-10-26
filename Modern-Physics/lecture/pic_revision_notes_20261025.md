# Ch7–Ch10 圖片描述修訂紀錄（2026-10-25）

對照正文修訂版，局部修正圖片提示詞中的假設、符號、歸一化與公式。未產生或更動 PNG；原圖名、章節對應與共用視覺風格保留。
26 份圖片提示詞同步修改中英文，另同步 4 份 README 檢查清單。三份歸一化／統計描述牽涉整個示意邏輯，因此重整其圖內文字；其餘以局部替換與模型註記為主。

原始 Markdown 備份：D:\Users\admin\Desktop\pc\githup\Scientific Image Generation\pic_revision_20261025\originals
逐檔差異：D:\Users\admin\Desktop\pc\githup\Scientific Image Generation\pic_revision_20261025\diffs

## Ch7（8 份）

- Exchange_Symmetry_and_Pauli.md：交換作用於完整的空間與自旋標記；電子總態反對稱由自旋—統計關係給定，不能只從機率密度相等推出。
- Hunds_Rule.md：比較同一近簡併子殼中的組態；反對稱性只給出節點，能量排序仍須計入庫侖與交換積分，不能由節點直接推出平均距離。
- LS_Coupling_and_Precession.md：角動量箭頭、圓錐與進動是向量模型示意，不是可同時精確測得的三個分量或電子軌跡；z 為選定量子化軸。LS 耦合圖限自旋—軌道作用較弱的情況。
- README.md：同步圖片清單與物理檢查項目，維持原有待生成狀態
- Spin_Orbit_Coupling.md：以非相對論中心場及弱自旋—軌道耦合為模型；經典軌道磁場只說明量級與方向，不當成精確能級推導。
- Stern_Gerlach_and_Spin_Quantization.md：角動量箭頭、圓錐與進動是向量模型示意，不是可同時精確測得的三個分量或電子軌跡；z 為選定量子化軸。LS 耦合圖限自旋—軌道作用較弱的情況。
- Subshell_Filling_Order.md：能階階梯是中性原子的近似填充次序，不是所有元素、離子的固定能量排序；標出 Cr、Cu 等例外與游離時次序可變。徑向曲線為穿透示意，峰高不代表精確數值。
- Total_Angular_Momentum_Vector_Addition.md：角動量箭頭、圓錐與進動是向量模型示意，不是可同時精確測得的三個分量或電子軌跡；z 為選定量子化軸。LS 耦合圖限自旋—軌道作用較弱的情況。

## Ch8（8 份）

- H2plus_Energy_Curves.md：採 Born–Oppenheimer 近似固定兩核，R 為核間距；電子能與包含核間斥力的總能分開標示，基態能量曲線井深不含振動零點修正。
- H2_Spin_Energy_Curves.md：空間與自旋部分相乘才是電子總態，總態必須反對稱；束縛與否須比較包含電子及核間作用的總能量。
- Molecular_Bond_Types.md：位能曲線的井深標 D_e；自振動基態解離的能量為 D₀=D_e−E_vib,0，兩者不混用。
- Parabolic_Approximation_Two_Body_Oscillator.md：只在平衡距離附近作諧振近似，μ=m₁m₂/(m₁+m₂)（原 m′）；圖中位能零點、井深 D_e 與零點振動能須分開。
- README.md：同步圖片清單與物理檢查項目，維持原有待生成狀態
- Rigid_Rotor_Levels_and_Spectrum.md：剛性雙原子轉子，固定 R、I=μR²；μ=m₁m₂/(m₁+m₂)，若原圖寫 m′，即同一約化質量。純轉動電偶極光譜須有永久偶極，ΔJ=±1；高 J 離心伸長不在本圖。
- Symmetric_Antisymmetric_Wavefunctions.md：補上鏡射假設、重疊歸一化與合核近似限制
- Vibration_Rotation_Levels.md：採諧振子與剛性轉子近似；Δv=±1 限線性偶極近似。P、R 支圖以 CO 的 Σ↔Σ 振轉躍遷為例，不宣稱所有分子都無 Q 支。

## Ch9（7 份）

- Einstein_Coefficients_Three_Transitions.md：B_ij=B_ji 的圖示假設兩能級簡併度相同；一般式為 g_i B_ij=g_j B_ji。此處 g_i 是簡併度，不是連續態密度。
- Electron_Energy_Distribution_in_Metal.md：三維非交互作用自由電子、固定 N 與 V；ε_F=μ(0)。有限溫度由 N=∫g(ε)f(ε,μ,T)dε 決定 μ(T)，低溫可用 μ≈ε_F[1−π²(kT/ε_F)²/12]。n(ε)、g(ε) 單位為每能量；電子比熱公式限 kT≪ε_F。
- Fermi_Dirac_Distribution_Temperature.md：上排專門比較固定 μ=μ₀>0 的分布形狀，並非同一固定 N 樣品升溫；T=0 階躍兩端畫空心點，不強制指定單點佔據。下排 ε_F、T_F 使用 0 K 定義；固定 N 時 μ 隨 T 改變。
- Free_Electron_Density_of_States.md：三維非交互作用自由電子模型，g(ε) 已包含兩種自旋；增加 N 的比較固定 V。ε_F 是 0 K 費米能，g 的單位為每能量。
- README.md：同步圖片清單與物理檢查項目，維持原有待生成狀態
- Statistical_Distribution_Overview.md：區分平均佔據數、機率與態密度；修正MB分類
- Three_Quantum_Statistics_Comparison.md：重算同態歸一化；移除1:2:0機率長條；明列固定T與μ

## Ch10（7 份）

- Bragg_Reflection_and_Band_Gap.md：一維近自由電子，在區邊界作兩波近似；若沿用 E_g=2U₁，約定 U₁>0。此處 U₁ 為傅立葉係數，非峰谷差。
- Conductor_Insulator_Semiconductor_Bands.md：以本質、近熱平衡材料作能帶示意；有限溫度化學勢約在能隙中央，但不必恰在正中央。態數若含自旋須明寫。
- Drift_Velocity_and_Resistivity.md：弱電場、均勻材料與定常 Drude 弛豫近似：m d⟨v⟩/dt=−eE−m⟨v⟩/τ；定常漂移速度 ⟨v⟩=−eτE/m。aτ 指定常平均值，不是每次碰撞前末速；電流方向與電子漂移相反。
- Energy_Levels_to_Energy_Bands.md：每原子取一個空間軌域時，N 原子形成 N 個空間態；包含兩種自旋才有 2N 個單電子態。若圖只畫能量分裂線，標明未計自旋。
- PN_Junction_Bias_Band_Diagrams.md：平衡圖只用一條水平 E_F；偏壓圖改以電子、電洞準費米能級 E_Fn、E_Fp 標示兩側，不能畫成全域單一平衡 E_F。理想二極體式限低注入、定溫，忽略耗盡區復合、串聯電阻與崩潰。
- README.md：同步圖片清單與物理檢查項目，維持原有待生成狀態
- Van_der_Waals_Dipole_Interactions.md：α>0 為各向同性線性極化率，p_ind=αE；誘導能須含建立偶極的功，U=−αE²/2。忽略重疊與遲滯。曲線縱軸用歸一化能量大小 |U(r)|/|U(r₀)|，不是力；水分子標部分電荷 δ±。

## 檢查

已確認：圖名不變、每份保留兩個提示詞區塊、備份原始位元內容、逐檔輸出差異。既有圖片是否已呈現這些修正，需於後續產圖時另行檢查。
