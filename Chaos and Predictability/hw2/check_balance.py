"""
檢驗系統是否達到統計平衡
"""

import numpy as np
import matplotlib.pyplot as plt
import h5py
from pathlib import Path
import glob

def load_diagnostics(directory):
    """載入診斷數據"""
    files = sorted(Path(directory).glob('*.h5'))
    
    times = []
    KE = []
    
    for file in files:
        with h5py.File(file, 'r') as f:
            if 'tasks/kinetic_energy' in f:
                times.extend(f['scales/sim_time'][:])
                KE.extend(f['tasks/kinetic_energy'][:, 0, 0])
    
    return np.array(times), np.array(KE)

def check_equilibrium(times, quantity, name='Quantity', 
                     split_ratio=0.5, threshold=0.1):
    """
    檢查是否達到統計平衡
    
    參數:
    - times: 時間陣列
    - quantity: 物理量時間序列
    - name: 量的名稱
    - split_ratio: 分割點(0.5 = 中點)
    - threshold: 判斷閾值(0.1 = 10%)
    """
    
    print(f"\n{'='*70}")
    print(f"統計平衡分析: {name}")
    print(f"{'='*70}")
    
    # 找分割點
    split_idx = int(len(times) * split_ratio)
    
    # 分成兩段
    q_first = quantity[:split_idx]
    q_second = quantity[split_idx:]
    t_first = times[:split_idx]
    t_second = times[split_idx:]
    
    # 計算統計量
    mean_first = np.mean(q_first)
    mean_second = np.mean(q_second)
    std_first = np.std(q_first)
    std_second = np.std(q_second)
    
    # 相對差異
    rel_diff = abs(mean_second - mean_first) / mean_first if mean_first != 0 else np.inf
    
    # 變異係數
    cv_first = std_first / mean_first if mean_first != 0 else 0
    cv_second = std_second / mean_second if mean_second != 0 else 0
    
    print(f"\n時間範圍:")
    print(f"  前半段: t ∈ [{t_first[0]:.2f}, {t_first[-1]:.2f}]")
    print(f"  後半段: t ∈ [{t_second[0]:.2f}, {t_second[-1]:.2f}]")
    
    print(f"\n統計量:")
    print(f"  前半段平均: {mean_first:.6e}")
    print(f"  後半段平均: {mean_second:.6e}")
    print(f"  相對差異:   {rel_diff:.2%}")
    
    print(f"\n波動性:")
    print(f"  前半段變異係數: {cv_first:.2%}")
    print(f"  後半段變異係數: {cv_second:.2%}")
    
    print(f"\n判斷:")
    if rel_diff < threshold:
        print(f"  ✅ 達到統計平衡 (相對差異 {rel_diff:.2%} < {threshold:.0%})")
        equilibrium = True
    else:
        print(f"  ❌ 尚未達到平衡 (相對差異 {rel_diff:.2%} > {threshold:.0%})")
        print(f"     建議: 延長模擬時間")
        equilibrium = False
    
    if cv_second > 0.5:
        print(f"  ⚠️  注意: 後半段波動很大 (變異係數 {cv_second:.2%})")
        print(f"     這可能是湍流/混沌特徵(正常),或數值不穩定(異常)")
    
    return equilibrium, {
        'mean_first': mean_first,
        'mean_second': mean_second,
        'rel_diff': rel_diff,
        'cv_second': cv_second
    }

def plot_equilibrium_analysis(times, quantity, name='Quantity', 
                               split_ratio=0.5, savefig=None):
    """繪製平衡分析圖"""
    
    split_idx = int(len(times) * split_ratio)
    
    fig, axes = plt.subplots(2, 1, figsize=(12, 8))
    
    # 上圖: 完整時間序列
    axes[0].plot(times, quantity, 'b-', linewidth=0.5, alpha=0.7)
    axes[0].axvline(times[split_idx], color='r', linestyle='--', 
                    label=f'Split at t={times[split_idx]:.1f}')
    
    # 標註平均值
    peak_index = np.argmax(quantity)
    steady_state_mean = np.mean(quantity[peak_index:])
    tolerance , new_start_point = 0.01 , -1
    for i in range(peak_index, len(quantity)):
        if abs(quantity[i] - steady_state_mean) <= tolerance:
            new_start_point = i
            break
    if new_start_point == -1:
        print("警告：在最大值點之後，未找到與平均值相交的點。請檢查 tolerance 設定或數據。")
        return 
    
    data_after_new_start = quantity[new_start_point:]
    length_after_new_start = len(data_after_new_start)
    mid_point_index = new_start_point + length_after_new_start // 2
    mean_first = np.mean(quantity[new_start_point : mid_point_index])
    mean_second = np.mean(quantity[mid_point_index : ])
    

    axes[0].axhline(mean_first, color='g', linestyle=':', 
                    xmax=split_ratio, label=f'Mean (first) = {mean_first:.3e}')
    axes[0].axhline(mean_second, color='orange', linestyle=':', 
                    xmin=split_ratio, label=f'Mean (second) = {mean_second:.3e}')
    
    axes[0].set_ylabel(name, fontsize=12)
    axes[0].set_title(f'{name} Time Series', fontsize=14)
    axes[0].legend(loc='best')
    axes[0].grid(True, alpha=0.3)
    
    # 下圖: 移動平均
    window = max(len(times) // 50, 1)
    moving_avg = np.convolve(quantity, np.ones(window)/window, mode='valid')
    t_moving = times[:len(moving_avg)]
    
    axes[1].plot(times, quantity, 'b-', linewidth=0.5, alpha=0.3, label='Raw')
    axes[1].plot(t_moving, moving_avg, 'r-', linewidth=2, label=f'Moving average (window={window})')
    axes[1].axhline(mean_second, color='g', linestyle='--', 
                    label=f'Equilibrium mean = {mean_second:.3e}')
    
    axes[1].set_xlabel('Time', fontsize=12)
    axes[1].set_ylabel(name, fontsize=12)
    axes[1].set_title(f'{name} with Moving Average', fontsize=14)
    axes[1].legend(loc='best')
    axes[1].grid(True, alpha=0.3)
    
    plt.tight_layout()
    
    if savefig:
        plt.savefig(savefig, dpi=150, bbox_inches='tight')
        print(f"\n圖片已保存: {savefig}")
    
    plt.show()

def main():
    """主分析流程"""
    
    print("="*70)
    print("動力平衡檢驗")
    print("="*70)
    
    # 檢查可用的診斷數據
    diagnostics_dirs = ['diagnostics', 'diagnostics_high_ra_stable', 
                       'diagnostics_highRayleigh','snapshots', 'snapshots_highRa','diagnostics_lowRayleigh']
    
    available_dirs = [d for d in diagnostics_dirs if Path(d).exists()]
    
    if not available_dirs:
        print("\n❌ 找不到診斷數據目錄!")
        print("請確認以下目錄之一存在:")
        for d in diagnostics_dirs:
            print(f"  - {d}/")
        return
    
    print(f"\n找到 {len(available_dirs)} 個診斷數據目錄:")
    for d in available_dirs:
        print(f"  - {d}/")
    
    # 分析每個目錄
    for diag_dir in available_dirs:
        print(f"\n{'='*70}")
        print(f"分析目錄: {diag_dir}")
        print(f"{'='*70}")
        
        try:
            # 載入數據
            times, KE = load_diagnostics(diag_dir)
            
            if len(times) == 0:
                print(f"  ⚠️  目錄為空或無有效數據")
                continue
            
            print(f"\n數據摘要:")
            print(f"  時間範圍: [{times[0]:.2f}, {times[-1]:.2f}]")
            print(f"  數據點數: {len(times)}")
            print(f"  平均時間間隔: {np.mean(np.diff(times)):.4f}")
            
            # 檢查平衡
            equilibrium, stats = check_equilibrium(times, KE, 
                                                   name='Kinetic Energy',
                                                   split_ratio=0.5,
                                                   threshold=0.1)
            
            # 繪圖
            plot_equilibrium_analysis(times, KE, 
                                     name='Kinetic Energy',
                                     savefig=f'equilibrium_{diag_dir.replace("/", "_")}.png')
            
        except Exception as e:
            print(f"  ❌ 處理失敗: {e}")
            import traceback
            traceback.print_exc()
    
    print("\n" + "="*70)
    print("分析完成!")
    print("="*70)
    print("\n建議:")
    print("1. 如果「達到統計平衡」→ 可以進行比較分析")
    print("2. 如果「尚未達到平衡」→ 延長模擬時間")
    print("3. 如果「波動很大」但平均穩定 → 這是湍流特徵,仍算平衡")

if __name__ == '__main__':
    main()