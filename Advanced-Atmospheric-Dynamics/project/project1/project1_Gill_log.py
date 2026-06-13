import numpy as np
import matplotlib.pyplot as plt

# 1. 物理常數設定 (地球等溫大氣)
gamma = 1.4
S = (gamma**2) / (gamma - 1)  # 常數 S 約等於 4.9
G = 1 / gamma - 0.5           # 常數 G 約等於 0.214

# 計算聲學截斷頻率的下限 (N_A / N)
Na_N = np.sqrt(S * G**2 + 1)  # 約等於 1.107

# 2. 定義 X 軸範圍 (無因次水平波數 k*Hs)，取對數分佈
X = np.logspace(-2, 2, 1000)

plt.figure(figsize=(10, 8))

# 3. 繪製藍姆波 (Lamb Wave)
# 公式: Y = sqrt(S) * X
Y_lamb = np.sqrt(S) * X
plt.loglog(X, Y_lamb, 'k-', linewidth=3, label='Lamb Wave')

# 4. 繪製三維聲波與浮力波 (不同垂直波數 Z = m*Hs)
Z_vals = [0, 1, 3, 10]
colors = ['blue', 'orange', 'green', 'red']

for Z, color in zip(Z_vals, colors):
    # 根據方程式 A*Y^4 + B*Y^2 + C = 0 定義係數
    A = 1
    B = -(S * (X**2 + Z**2 + G**2) + 1)
    C = S * X**2
    
    # 計算根號判別式
    discriminant = np.sqrt(B**2 - 4*A*C)
    
    # 高頻根：聲波 (Acoustic Waves)
    Y2_acoustic = (-B + discriminant) / (2 * A)
    Y_acoustic = np.sqrt(Y2_acoustic)
    
    # 低頻根：浮力波/內重力波 (Buoyancy/Gravity Waves)
    Y2_gravity = (-B - discriminant) / (2 * A)
    Y_gravity = np.sqrt(Y2_gravity)
    
    # 繪圖 (只在 Z=0 時加上圖例以保持畫面整潔)
    plt.loglog(X, Y_acoustic, color=color, linestyle='--', label=f'Acoustic Wave' if Z==0 else "")
    plt.loglog(X, Y_gravity, color=color, linestyle='-.',  label=f'Gravity Wave' if Z==0 else "")

    # 標示出不同 mHs 的文字
    plt.text(1e-2, Y_acoustic[0]*1.1, f'mHs={Z}', color=color, fontsize=9)
    plt.text(1e2, Y_gravity[-1]*0.8, f'mHs={Z}', color=color, fontsize=9, ha='right')

# 5. 繪製水平參考線 (物理極限)
plt.axhline(1, color='gray', linestyle=':', linewidth=2, label='Buoyancy Limit (v/N = 1)')
plt.axhline(Na_N, color='purple', linestyle=':', linewidth=2, label=f'Acoustic Cutoff (v/N = {Na_N:.2f})')

# 6. 圖表美化與設定
plt.xlim([1e-5, 1e2])
plt.ylim([1e-5, 1e2])
plt.xlabel('Normalized Horizontal Wavenumber $( \overline{k}H_s )$', fontsize=14)
plt.ylabel('Normalized Frequency $( \\nu/N )$', fontsize=14)
plt.title('Dispersion Diagram for Atmospheric Waves (Gill Fig 6-17)', fontsize=16)
plt.legend(loc='upper left', fontsize=10)
plt.grid(True, which="both", ls="--", alpha=0.5)

plt.tight_layout()
plt.savefig('Gill_Dispersion_Diagram.png', dpi=300)  # 儲存圖像
plt.show()
plt.close()