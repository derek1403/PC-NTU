import numpy as np
import matplotlib.pyplot as plt

# 1. 設定繪圖參數與無因次波數陣列
k_vals = np.linspace(0, 5, 500)
n_modes = [1, 2, 3]

# 建立圖表與軸物件
fig, ax = plt.subplots(figsize=(13, 8), dpi=150)

# 2. 繪製 n = -1 的克耳文波 (Kelvin Wave)
# 色散關係: omega = k
omega_kelvin = k_vals
line_Kelvin_wave = ax.plot(k_vals, omega_kelvin, color='purple', linestyle='-', linewidth=2.5, 
        label='Kelvin wave ($n=-1$)')

# 3. 繪製 n = 0 的混合羅斯貝-重力波 (MRG / Yanai Wave) 與 n=0 向東慣性重力波
# 色散方程式退化為: omega^2 - k*omega - 1 = 0
omega_mrg = (k_vals - np.sqrt(k_vals**2 + 4)) / 2    # 向西傳播 (低頻)
omega_eig_0 = (k_vals + np.sqrt(k_vals**2 + 4)) / 2  # 向東傳播 (高頻)

line_MRG_wave = ax.plot(k_vals, omega_mrg, color='forestgreen', linestyle='-', linewidth=2.5, 
        label='Mixed Rossby-Gravity wave ($n=0$)')
line_EIG_0_wave = ax.plot(k_vals, omega_eig_0, color='crimson', linestyle='-', linewidth=1.5, 
        label='Eastward Inertio-Gravity wave ($n=0$)')

# 4. 繪製 n >= 1 的羅斯貝波與慣性重力波
# 色散方程式: omega^3 - (k^2 + 2n + 1)omega - k = 0
colors = ['#1f77b4', '#ff7f0e', '#2ca02c'] # 針對不同 n 給予不同深淺標示

for idx, n in enumerate(n_modes):
    omega_eig = np.zeros_like(k_vals)
    omega_rossby = np.zeros_like(k_vals)
    omega_wig = np.zeros_like(k_vals)
    
    for i, k in enumerate(k_vals):
        # 建立三次方程式係數: [1*w^3, 0*w^2, -(k^2+2n+1)*w, -k = 0]
        coeffs = [1, 0, -(k**2 + 2*n + 1), -k]
        roots = np.sort(np.roots(coeffs))
        
        # 根據我們現代的定義：
        # 根 0 (最負): Westward IG
        # 根 1 (微負): Equatorial Rossby
        # 根 2 (最正): Eastward IG
        omega_wig[i] = roots[0]
        omega_rossby[i] = roots[1]
        omega_eig[i] = roots[2]
        
    # 為了避免 legend 重複出現太多次，只在 n=1 時加上標籤
    label_eig = 'Eastward IG waves ($n \geq 1$)' if n == 1 else None
    label_rossby = 'Equatorial Rossby waves ($n \geq 1$)' if n == 1 else None
    label_wig = 'Westward IG waves ($n \geq 1$)' if n == 1 else None
    
    line_EIG_wave = ax.plot(k_vals, omega_eig, color='crimson', linestyle='--', alpha=0.8, label=label_eig)
    line_Rossby_wave = ax.plot(k_vals, omega_rossby, color='royalblue', linestyle='-', linewidth=2, label=label_rossby)
    line_WIG_wave = ax.plot(k_vals, omega_wig, color='darkorange', linestyle='--', alpha=0.8, label=label_wig)
    
    # 在曲線上標註 n 的數值 (仿造古老圖表的貼心設計)
    k_idx = 100 # 取 k=1.0 附近標註
    
   
    

## 
ax.text(0.5, 2, f'$n=1$', color='crimson', fontsize=10, rotation=15)
ax.text(0.5, 2.4, f'$n=2$', color='crimson', fontsize=10, rotation=15)
ax.text(0.5, 2.8, f'$n=3$', color='crimson', fontsize=10, rotation=15)

##
ax.text(1, -0.45, f'$n=1$', color='royalblue', fontsize=10)
#ax.text(1, -0.4, f'$n=2$', color='royalblue', fontsize=10)
ax.text(1, 0.05, f'$n=3$', color='royalblue', fontsize=10)

##
ax.text(0.5, -1.65, f'$n=1$', color='darkorange', fontsize=10) #, rotation=-10 
ax.text(0.5, -2.15, f'$n=2$', color='darkorange', fontsize=10)
ax.text(0.5, -2.6, f'$n=3$', color='darkorange', fontsize=10)



# 5. 標註 n=0 與 n=-1 的文字
ax.text(1.0, 0.85, '$n=-1$', color='purple', fontsize=10, rotation=35)
ax.text(1.5, -0.7, '$n=0$', color='forestgreen', fontsize=10)
ax.text(1.0, 1.4, '$n=0$', color='crimson', fontsize=10, rotation=30)

# 6. 圖表網格、零線與外觀美化
ax.axhline(0, color='black', linewidth=1)
ax.axvline(0, color='black', linewidth=1)
ax.set_xlim(0, 5)
ax.set_ylim(-4, 4)

ax.set_xlabel('Non-dimensional Zonal Wavenumber ($k$)', fontsize=14, fontweight='bold')
ax.set_ylabel('Non-dimensional Frequency ($\omega$)', fontsize=14, fontweight='bold')
ax.set_title('Dispersion Relation of Equatorial Waves \n (Modern Convention: $e^{i(kx-\omega t)}$)', 
             fontsize=16, fontweight='bold', pad=15)

ax.grid(True, linestyle=':', alpha=0.6)


col1_handles = [line_EIG_wave[0], line_EIG_0_wave[0] ,  line_Kelvin_wave[0]]
col1_labels = ['Eastward IG waves ($n \geq 1$)','Eastward Inertio-Gravity wave ($n=0$)', 'Kelvin wave ($n=-1$)']
col2_handles = [  line_WIG_wave[0] ,line_MRG_wave[0], line_Rossby_wave[0],]
col2_labels = [ 'Westward IG waves ($n \geq 1$)' ,'Mixed Rossby-Gravity wave ($n=0$)','Equatorial Rossby waves ($n \geq 1$)',]


"""# 將 Legend 移至圖表外部右側
ax.legend(
    bbox_to_anchor=(1.04, 1), loc='upper left', borderaxespad=0., 
          fontsize=12, frameon=True, edgecolor='black')
"""


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




plt.tight_layout()
plt.savefig('Equatorial_Waves_Dispersion_Diagram.png', dpi=300)  # 儲存圖像
#plt.show()
plt.close()