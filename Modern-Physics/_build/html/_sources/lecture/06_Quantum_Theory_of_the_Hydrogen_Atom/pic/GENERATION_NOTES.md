# 圖片生成紀錄

日期：2026-10-25
工具：內建 image_gen（非 CLI）。12 張 PNG 均已生成，檔名與講義引用一致。
提示詞來源：00_STYLE_GUIDE.md 中文風格區塊 + 各同名 .md 中文提示詞。能階、空間量子化、徑向機率圖經重生成，精簡敘述並補充解析公式；其他圖追加電偶極近似與塞曼正負號的限定。

## 視覺檢查發現的待修項目

目前為已生成圖稿，不代表通過科學排版校對。README 的已生成與下方校對勾選項分開管理。

- Spherical_Polar_Coordinates：固定 theta 的圓錐頂點與球心不一致，出現不應有的雙錐；投影標示需修正。
- Separation_of_Variables_Roadmap：第三步導數符號需逐字複核，導言對變數分離方法的描述過強。
- Three_Eigen_Equations_and_Quantum_Numbers：需補充徑向原點邊界條件；自旋也可在 Pauli 理論中引入。
- Hydrogen_Energy_Levels：標示能量正確，但圖形高度仍不是嚴格線性比例；不可用圖上距離讀值。
- Orbital_Angular_Momentum_Quantization：徑向向量未正確沿半徑；抵消論證屬啟發式，嚴格結果來自 L² 算符本徵值。
- Space_Quantization_of_Angular_Momentum：重生成為平面半圓模型，已呈現五個投影與等長向量的關係。
- Spherical_Volume_Element：角函數歸一化的 theta 積分須含 sin(theta) 權重；繞 z 軸對稱限單一 m 本徵態。
- Radial_Probability_Density：解析公式與節點數已標示；部分曲線節點位置與刻度仍不完全吻合，應視為形狀示意。
- Radiative_Transition_Dipole_Oscillation：不振盪的期望值不排除激發態自發輻射；圖中實係數餘弦形式需限定係數與矩陣元為實數。
- Selection_Rules_Energy_Level_Diagram：部分躍遷箭頭端點及文字未對應正確能階，需按指定清單重校。
- Magnetic_Moment_of_Orbital_Electron：電流與速度箭頭應沿切線且反向；需區分向量、帶符號分量與磁矩大小。
- Normal_Zeeman_Effect：五條與三條能階已生成，圖中箭頭未完整清楚呈現九條允許躍遷；數值框有波長小數位錯字，正確應為約 450.00283、450、449.99717 nm。

原始講義與提示詞未修改。正式教學使用前需完成上述校對。

