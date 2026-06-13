import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D



# 1. 物理常數設定 (地球等溫大氣)
gamma = 1.4
S = (gamma**2) / (gamma - 1)  # 常數 S 約等於 4.9
G = 1 / gamma - 0.5           # 常數 G 約等於 0.214

# 計算聲學截斷頻率下限 (Na / N)
Na_N = np.sqrt(S * G**2 + 1)  # 約等於 1.107

# 2. 定義 X 軸範圍 (無因次水平波數 k*Hs)，採線性分佈
X = np.linspace(0.001, 1.25, 1000)

# 建立圖表 (加寬畫布以容納右側的 Legend)
fig, ax = plt.subplots(figsize=(12, 7))

# 3. 繪製邊界灰色區域 (波傳播允許區)
A_fill = 1
B_fill = -(S * (X**2 + 0**2 + G**2) + 1)
C_fill = S * X**2

# 聲波區域
Y2_ac_min = (-B_fill + np.sqrt(B_fill**2 - 4*A_fill*C_fill)) / (2 * A_fill)
ax.fill_between(X, np.sqrt(Y2_ac_min), 2.0, color='lightgray', alpha=0.3)

# 浮力波區域
Y2_gr_max = (-B_fill - np.sqrt(B_fill**2 - 4*A_fill*C_fill)) / (2 * A_fill)
ax.fill_between(X, 0, np.sqrt(Y2_gr_max), color='lightgray', alpha=0.3)

# 4. 繪製重要物理極限參考線
line_buo     = ax.axhline(1, color='purple', linestyle=':', linewidth=2, label=r'Buoyancy Limit ($\omega/N = 1$)')
line_aco_cut = ax.axhline(Na_N, color='brown', linestyle=':', linewidth=2, label=r'Acoustic Cutoff ($\omega/N \approx 1.11$)')

acoustic_lines = []
gravity_lines  = []


# 5. 繪製藍姆波 (Lamb Wave)
Y_lamb = np.sqrt(S) * X
line_lamb, = ax.plot(X, Y_lamb, color='black', linestyle='-', linewidth=2.5, label='Lamb Wave')

# 6. 繪製三維聲波與浮力波
Z_vals = [0, 0.4, 0.8, 1.2]
colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red']

for Z, color in zip(Z_vals, colors):
    A = 1
    B = -(S * (X**2 + Z**2 + G**2) + 1)
    C = S * X**2
    discriminant = np.sqrt(B**2 - 4*A*C)
    
    # 高頻根：聲波 (Acoustic Waves)
    Y2_acoustic = (-B + discriminant) / (2 * A)
    Y_acoustic = np.sqrt(Y2_acoustic)
    
    # 低頻根：浮力波 (Internal Gravity Waves)
    Y2_gravity = (-B - discriminant) / (2 * A)
    Y_gravity = np.sqrt(Y2_gravity)
    
    # 畫線 (實線代表聲波，虛線代表浮力波)
    la, =ax.plot(X, Y_acoustic, color=color, linestyle='-', linewidth=2, 
            label=f'Acoustic ($mH_s={Z}$)')
    
    lg, =ax.plot(X, Y_gravity, color=color, linestyle='--', linewidth=2, 
            label=f'Gravity ($mH_s={Z}$)')
    
    acoustic_lines.append((la, Z, color, Y_acoustic))
    gravity_lines.append( (lg, Z, color, Y_gravity) )

## text 

ax.text(0.28, 0.6,'Lamb wave', fontsize=12, fontweight='bold',
        rotation=55, ha='center', backgroundcolor='white')

ax.text(0.1, 1.7,'Acoustic waves', fontsize=12, fontweight='bold', color='dimgray')

ax.text(0.6,0.2,'Internal gravity waves', fontsize=12, fontweight='bold', color='dimgray')

## 讓我可以手動調整每個text的位置
for Z, color in zip(Z_vals, colors):
    if Z == 0:
        ax.text(0.1, 1.2,f'$mH_s={Z}$', fontsize=12, fontweight='bold', color=color )
        ax.text(0.4,0.8,f'$mH_s={Z}$', fontsize=12, fontweight='bold', color=color,rotation=30)
    elif Z == 0.4:
        ax.text(0.1, 1.5,f'$mH_s={Z}$', fontsize=12, fontweight='bold', color=color)
        ax.text(0.45,0.7,f'$mH_s={Z}$', fontsize=12, fontweight='bold', color=color,rotation=25)
    elif Z == 0.8:
        #ax.text(0.1, 0.9,f'$mH_s={Z}$', fontsize=12, fontweight='bold', color=color)
        ax.text(0.5,0.55,f'$mH_s={Z}$', fontsize=12, fontweight='bold', color=color,rotation=20)
    elif Z == 1.2:
        #ax.text(0.1, 0.5,f'$mH_s={Z}$', fontsize=12, fontweight='bold', color=color)
        ax.text(0.55,0.45,f'$mH_s={Z}$', fontsize=12, fontweight='bold', color=color,rotation=20)
    
 
    

# 7. 圖表外觀設定 (完整邊框與線性座標)
ax.set_xlim([0, 1.2])
ax.set_ylim([0, 1.8])

# 增強刻度與邊框粗細
ax.tick_params(axis='both', labelsize=12)
for spine in ax.spines.values():
    spine.set_linewidth(1.5)

ax.set_xlabel(r'Normalized Horizontal Wavenumber ($\overline{k}H_s$)', fontsize=14)
ax.set_ylabel(r'Normalized Frequency ($\omega / N$)', fontsize=14)
ax.set_title('Dispersion Diagram for Atmospheric Waves', fontsize=16, pad=15)

# ================= 新增右側 Y 軸 =================
ax_right = ax.twinx()  # 建立共用 x 軸的右側座標系
ax_right.set_ylim(ax.get_ylim())  # 確保右側 Y 軸的範圍與左側完全一致

# 設定右側特定的刻度位置與標籤
ax_right.set_yticks([1.0, Na_N])
ax_right.set_yticklabels(['$N$', '$N_A$'], fontsize=14, fontweight='bold') 
# 若您想直接顯示 1.1N，可將標籤改為 ['N', '1.1N']

# 調整右側刻度與邊框的樣式，使其與主圖表一致
ax_right.tick_params(axis='y', labelsize=12, color='black')
for spine in ax_right.spines.values():
    spine.set_linewidth(1.5)
# ===============================================


# 8. 將 Legend 移至圖表外部右側

# ── Legend：ncols=2，column-major 填充 ────────────────────────────────────────
# matplotlib ncols=2 填充順序（column-major）：
#   col1: 位置1,2,3,4,5,6   col2: 位置7,8,9,10,11,12
# 想要的 row 配對：
#   row1: Buoyancy(col1) | Acoustic Cutoff(col2)
#   row2: Acoustic mHs=0 | Gravity mHs=0
#   row3: Acoustic mHs=0.4 | Gravity mHs=0.4
#   row4: Acoustic mHs=0.8 | Gravity mHs=0.8
#   row5: Acoustic mHs=1.2 | Gravity mHs=1.2
#   row6: Lamb | (空白)
# → 傳入順序要按 column-major：先把 col1 全部列出，再列 col2

empty = Line2D([], [], color='none')

# col1（左欄）
col1_handles = [
    line_buo,
    acoustic_lines[0][0],
    acoustic_lines[1][0],
    acoustic_lines[2][0],
    acoustic_lines[3][0],
    line_lamb,
]
col1_labels = [
    r'Buoyancy Limit ($\omega/N=1$)',
    r'Acoustic ($mH_s=0$)',
    r'Acoustic ($mH_s=0.4$)',
    r'Acoustic ($mH_s=0.8$)',
    r'Acoustic ($mH_s=1.2$)',
    'Lamb Wave',
]

# col2（右欄）
col2_handles = [
    line_aco_cut,
    gravity_lines[0][0],
    gravity_lines[1][0],
    gravity_lines[2][0],
    gravity_lines[3][0],
    empty,
]
col2_labels = [
    r'Acoustic Cutoff ($\omega/N\approx1.11$)',
    r'Gravity ($mH_s=0$)',
    r'Gravity ($mH_s=0.4$)',
    r'Gravity ($mH_s=0.8$)',
    r'Gravity ($mH_s=1.2$)',
    '',
]

ax.legend(
    col1_handles + col2_handles,
    col1_labels  + col2_labels,
    ncols=2,
    bbox_to_anchor=(1.02, 1),
    loc='upper left',
    fontsize=10,
    frameon=True, edgecolor='black', fancybox=False,
    handlelength=2.5,
    columnspacing=1.0,
)
# 自動調整佈局以防止右側 Legend 被裁切
plt.tight_layout()

plt.savefig('Gill_Dispersion_Diagram_Linear.png', dpi=300)  # 儲存圖像
#plt.show()
plt.close()