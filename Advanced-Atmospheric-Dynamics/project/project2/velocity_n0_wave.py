import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# 1. 參數設定與解色散方程式
# ==========================================
k = 0.5
A = 1.0  # 任意振幅常數

# 針對 n=0，色散方程式化簡為 omega^2 - k*omega - 1 = 0
# (現代 e^{i(kx-wt)} 慣例下，正根為向東，負根為向西)
omega_east = (k + np.sqrt(k**2 + 4)) / 2   # Eastward IG wave (~1.2808)
omega_west = (k - np.sqrt(k**2 + 4)) / 2   # Westward IG/MRG wave (~-0.7808)

# 建立物理空間網格 (畫兩個水平波長 L = 2 * (2pi/k) = 8pi)
x = np.linspace(0, 8 * np.pi, 60)
y = np.linspace(-4, 4, 40)
X, Y = np.meshgrid(x, y)

# ==========================================
# 2. 定義計算物理空間場的函數 (完全基於你的推導)
# ==========================================
def compute_wave_fields(omega, k, X, Y, A=1.0):
    # 高斯衰減包絡
    envelope = np.exp(-Y**2 / 2)
    
    # 物理變數場 (取 t=0 瞬間，根據 e^{i(kx-wt)} 的嚴謹實部)
    u = -A * (omega + k) * Y * envelope * np.cos(k * X)
    phi = -A * (omega + k) * Y * envelope * np.cos(k * X)
    v = -A * (omega**2 - k**2) * envelope * np.sin(k * X)
    
    # 散度場解析解
    div = A * omega * (omega + k) * Y * envelope * np.sin(k * X)
    
    return u, v, phi, div

# ==========================================
# 3. 計算向東與向西的波場
# ==========================================
u_e, v_e, phi_e, div_e = compute_wave_fields(omega_east, k, X, Y, A)
u_w, v_w, phi_w, div_w = compute_wave_fields(omega_west, k, X, Y, A)

# ==========================================
# 4. 繪圖設定
# ==========================================
fig, axes = plt.subplots(2, 1, figsize=(12, 12), dpi=150)
fig.suptitle("Matsuno (1966) Fig. 6: Eigensolutions for $n=0, k=0.5$\n"
             "(Modern Convention $e^{i(kx-\\omega t)}$ with Divergence & Convergence)", 
             fontsize=16, fontweight='bold', y=0.95)

titles = [
    f"(a) Eastward moving inertio-gravity wave ($\\omega \\approx {omega_east:.2f}$)",
    f"(b) Westward moving inertio-gravity / MRG wave ($\\omega \\approx {omega_west:.2f}$)"
]

fields = [(u_e, v_e, phi_e, div_e), (u_w, v_w, phi_w, div_w)]

for i, ax in enumerate(axes):
    u, v, phi, div = fields[i]
    
    # 畫散度場 (填色)
    vmax = np.max(np.abs(div))
    cf = ax.contourf(X, Y, div, levels=20, cmap='RdBu_r', vmin=-vmax, vmax=vmax, alpha=0.6)
    
    # 畫氣壓場 phi (等值線)
    phi_max = np.max(np.abs(phi))
    levels = np.linspace(-phi_max, phi_max, 11)
    levels = levels[levels != 0] # 避開 0 線
    
    cs = ax.contour(X, Y, phi, levels=levels, colors='black', linewidths=1.5)
    

            
    # 畫赤道軸線
    ax.axhline(0, color='black', linestyle='-.', linewidth=1)
            
    # 畫風場向量 (quiver)
    step = 2
    ax.quiver(X[::step, ::step], Y[::step, ::step], 
              u[::step, ::step], v[::step, ::step], 
              pivot='middle', color='black', scale=15)
    
    ax.set_title(titles[i], fontsize=14, loc='left')
    ax.set_xlabel('Non-dimensional Zonal Coordinate ($kx$)', fontsize=12)
    ax.set_ylabel('Non-dimensional Latitudinal Coordinate ($y$)', fontsize=12)
    
    x_ticks = np.arange(0, 8.1*np.pi, 2*np.pi)
    x_labels = ['0', '$2\\pi$', '$4\\pi$', '$6\\pi$', '$8\\pi$']
    ax.set_xticks(x_ticks)
    ax.set_xticklabels(x_labels)

# 加入散度場 Colorbar
cbar_ax = fig.add_axes([0.92, 0.15, 0.02, 0.7])
cbar = fig.colorbar(cf, cax=cbar_ax)
cbar.set_label('Convergence (Blue)  <---   --->  Divergence (Red)', fontsize=12)

plt.subplots_adjust(right=0.9, hspace=0.3)
plt.savefig('./pic/velocity_n0_wave.png', bbox_inches='tight')
#plt.show()
plt.close()