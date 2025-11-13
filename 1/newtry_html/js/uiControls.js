/**
 * UI 控制模組（完整修正版）
 * 處理摺疊面板、開關和颱風追蹤 UI
 * ✅ 修正：強化顏色刷新機制，確保所有 UI 操作都正確更新視覺效果
 */

import { 
  state, 
  setHighlightMode, 
  getTyphoonTracks, 
  setTyphoonTracks,
  addTyphoonTrack,
  removeTyphoonTrack,
  setShowLandmass,
  setLandmassData,
  getAllNodes,
  getAllEdges
} from './state.js';
import { updatePlot } from './plotManager.js';
import { validateTyphoonId } from './typhoonTracker.js';
import { findConnectedComponents } from './componentAnalysis.js';
import { buildEdgeCoordinates } from './graphProcessor.js';

// 預設顏色列表
const DEFAULT_COLORS = [
  '#e74c3c', '#3498db', '#2ecc71', '#f39c12', '#9b59b6',
  '#1abc9c', '#e67e22', '#34495e', '#16a085', '#27ae60',
  '#2980b9', '#8e44ad', '#c0392b', '#d35400', '#7f8c8d'
];

let colorIndex = 0;

/**
 * ✅ 核心函數：統一刷新所有顏色
 * 當任何會影響顏色的操作發生時，呼叫此函數
 * 
 * 工作原理（類比）：
 * 就像重新拍一張照片 - 確保所有元素（節點顏色、邊顏色、陸地標示）都是最新狀態
 */
function refreshAllColors() {
  try {
    // ✅ 優先使用當前顯示的資料（可能是篩選後的）
    const nodes = state.currentNodes?.length > 0 ? state.currentNodes : getAllNodes();
    const edges = state.currentEdges?.length > 0 ? state.currentEdges : getAllEdges();
    
    if (!nodes || nodes.length === 0) {
      console.warn('⚠️ 沒有節點資料，跳過顏色刷新');
      return;
    }
    
    console.log('🎨 刷新顏色開始:', {
      nodes: nodes.length,
      edges: edges.length,
      highlightMode: state.highlightMode,
      typhoonTracks: state.typhoonTracks.length,
      showLandmass: state.showLandmass
    });
    
    // ✅ 重建邊的座標資料
    const edgeData = buildEdgeCoordinates(edges, nodes);
    
    // ✅ 重新渲染圖表（updatePlot 內部會根據 state 計算正確的顏色）
    updatePlot(nodes, edgeData, edges.length, edges);
    
    console.log('✅ 顏色刷新完成');
  } catch (error) {
    console.error('❌ 顏色刷新失敗:', error);
    console.error('錯誤堆疊:', error.stack);
  }
}

/**
 * ✅ 防抖版本的顏色刷新（避免短時間內重複呼叫）
 * 類比：就像相機的防手震功能，避免拍出模糊的照片
 */
let refreshTimeout = null;
function debouncedRefreshColors(delay = 100) {
  if (refreshTimeout) {
    clearTimeout(refreshTimeout);
  }
  
  refreshTimeout = setTimeout(() => {
    refreshAllColors();
    refreshTimeout = null;
  }, delay);
}

/**
 * 初始化摺疊面板
 */
export function initCollapsiblePanels() {
  // 篩選功能面板
  const filterToggle = document.getElementById('filter-toggle');
  const filterContent = document.getElementById('filter-content');
  
  if (filterToggle && filterContent) {
    filterToggle.addEventListener('click', () => {
      const isCollapsed = filterContent.classList.contains('collapsed');
      filterContent.classList.toggle('collapsed');
      filterToggle.classList.toggle('collapsed');
      
      const arrow = filterToggle.querySelector('.arrow');
      if (arrow) {
        arrow.textContent = isCollapsed ? '▼' : '▶';
      }
    });
  }

  // 功能面板
  const featureToggle = document.getElementById('feature-toggle');
  const featureContent = document.getElementById('feature-content');
  
  if (featureToggle && featureContent) {
    featureToggle.addEventListener('click', () => {
      const isCollapsed = featureContent.classList.contains('collapsed');
      featureContent.classList.toggle('collapsed');
      featureToggle.classList.toggle('collapsed');
      
      const arrow = featureToggle.querySelector('.arrow');
      if (arrow) {
        arrow.textContent = isCollapsed ? '▼' : '▶';
      }
    });
  }

  console.log('✅ 摺疊面板初始化完成');
}

/**
 * 初始化高亮開關
 */
export function initHighlightSwitch() {
  const highlightSwitch = document.getElementById('highlight-switch');
  
  if (highlightSwitch) {
    highlightSwitch.addEventListener('change', (e) => {
      const isEnabled = e.target.checked;
      setHighlightMode(isEnabled);
      
      console.log(`🎯 高亮模式: ${isEnabled ? '✅ 開啟' : '❌ 關閉'}`);
      
      // ✅ 立即刷新顏色（使用防抖避免卡頓）
      debouncedRefreshColors(50);
    });
  }

  console.log('✅ 高亮開關初始化完成');
}

/**
 * 初始化圖例顯示/隱藏按鈕
 */
export function initLegendToggle() {
  const legendToggleBtn = document.getElementById('legend-toggle-btn');
  const legendElement = document.getElementById('highlight-legend');
  
  if (legendToggleBtn && legendElement) {
    // 預設隱藏圖例
    legendElement.style.display = 'none';
    
    legendToggleBtn.addEventListener('click', () => {
      const isHidden = legendElement.style.display === 'none';
      legendElement.style.display = isHidden ? 'block' : 'none';
      legendToggleBtn.textContent = isHidden ? '隱藏圖例' : '顯示圖例';
      
      console.log(`📊 圖例: ${isHidden ? '顯示' : '隱藏'}`);
    });
  }

  console.log('✅ 圖例切換按鈕初始化完成');
}

/**
 * 初始化颱風路徑追蹤 UI
 */
export function initTyphoonTracker() {
  const addTrackBtn = document.getElementById('add-track-btn');
  
  if (addTrackBtn) {
    addTrackBtn.addEventListener('click', () => {
      addTrackUI();
    });
  }

  console.log('✅ 颱風路徑追蹤初始化完成');
}

/**
 * 新增颱風追蹤 UI
 */
function addTrackUI() {
  const container = document.getElementById('typhoon-tracks-container');
  if (!container) {
    console.error('❌ 找不到 typhoon-tracks-container 元素');
    return;
  }
  
  const trackIndex = getTyphoonTracks().length;
  const color = DEFAULT_COLORS[colorIndex % DEFAULT_COLORS.length];
  colorIndex++;

  const trackDiv = document.createElement('div');
  trackDiv.className = 'track-item';
  trackDiv.dataset.index = trackIndex;

  trackDiv.innerHTML = `
    <input type="text" class="track-input" placeholder="輸入颱風 ID (如: 201324W)">
    <input type="color" class="track-color" value="${color}">
    <button class="track-remove" title="移除">×</button>
  `;

  container.appendChild(trackDiv);

  // 綁定事件
  const input = trackDiv.querySelector('.track-input');
  const colorPicker = trackDiv.querySelector('.track-color');
  const removeBtn = trackDiv.querySelector('.track-remove');

  // ✅ 颱風 ID 輸入事件
  input.addEventListener('change', () => {
    handleTyphoonInput(input, colorPicker, trackIndex);
  });

  // ✅ 顏色選擇事件
  colorPicker.addEventListener('change', () => {
    handleColorChange(trackIndex, colorPicker.value);
  });

  // ✅ 移除按鈕事件
  removeBtn.addEventListener('click', () => {
    removeTrackUI(trackIndex, trackDiv);
  });
  
  console.log(`➕ 新增颱風追蹤 UI: 索引 ${trackIndex}, 顏色 ${color}`);
}

/**
 * ✅ 處理颱風 ID 輸入
 */
function handleTyphoonInput(input, colorPicker, trackIndex) {
  const typhoonId = input.value.trim().toUpperCase();
  
  if (!typhoonId) {
    console.warn('⚠️ 颱風 ID 為空');
    return;
  }
  
  // ✅ 使用當前顯示的節點進行驗證（考慮篩選情況）
  const nodes = state.currentNodes?.length > 0 ? state.currentNodes : getAllNodes();
  
  if (validateTyphoonId(typhoonId, nodes)) {
    // ✅ 驗證成功，新增追蹤
    addTyphoonTrack(typhoonId, colorPicker.value);
    input.classList.remove('invalid');
    input.classList.add('valid');
    
    console.log(`✅ 颱風追蹤已新增: ${typhoonId}, 顏色: ${colorPicker.value}`);
    
    // ✅ 延遲刷新，確保 state 更新完成
    setTimeout(() => {
      refreshAllColors();
    }, 50);
  } else {
    // ❌ 驗證失敗
    alert(`找不到颱風 ID: ${typhoonId}\n請確認 ID 格式正確（例如: 201324W）`);
    input.classList.add('invalid');
    input.classList.remove('valid');
    console.error(`❌ 無效的颱風 ID: ${typhoonId}`);
  }
}

/**
 * ✅ 處理顏色變更
 */
function handleColorChange(index, color) {
  const tracks = getTyphoonTracks();
  
  if (tracks[index]) {
    tracks[index].color = color;
    setTyphoonTracks(tracks);
    
    console.log(`🎨 更新颱風追蹤顏色: 索引 ${index}, 新顏色 ${color}`);
    
    // ✅ 立即刷新顏色
    debouncedRefreshColors(50);
  } else {
    console.error(`❌ 找不到索引為 ${index} 的颱風追蹤`);
  }
}

/**
 * 移除颱風追蹤 UI
 */
function removeTrackUI(index, element) {
  const tracks = getTyphoonTracks();
  const removedTrack = tracks[index];
  
  removeTyphoonTrack(index);
  element.remove();
  
  console.log(`➖ 移除颱風追蹤: 索引 ${index}, ID ${removedTrack?.id || 'unknown'}`);
  
  // ✅ 移除後立即刷新顏色
  debouncedRefreshColors(50);
  
  // ✅ 重新索引剩餘的追蹤項目
  const container = document.getElementById('typhoon-tracks-container');
  if (container) {
    const items = container.querySelectorAll('.track-item');
    items.forEach((item, i) => {
      item.dataset.index = i;
    });
  }
}

/**
 * 初始化陸地與島嶼開關
 */
export function initLandmassSwitch() {
  const landmassSwitch = document.getElementById('landmass-switch');
  const landmassInfoBtn = document.getElementById('landmass-info-btn');
  const landmassInfo = document.getElementById('landmass-info');
  
  // 預設隱藏資訊面板
  if (landmassInfo) {
    landmassInfo.style.display = 'none';
  }
  
  // 資訊按鈕切換
  if (landmassInfoBtn && landmassInfo) {
    landmassInfoBtn.addEventListener('click', () => {
      const isHidden = landmassInfo.style.display === 'none';
      landmassInfo.style.display = isHidden ? 'block' : 'none';
    });
  }
  
  // 陸地與島嶼開關
  if (landmassSwitch) {
    landmassSwitch.addEventListener('change', (e) => {
      const isEnabled = e.target.checked;
      setShowLandmass(isEnabled);
      
      console.log(`🏝️ 陸地與島嶼標示: ${isEnabled ? '✅ 開啟' : '❌ 關閉'}`);
      
      if (isEnabled) {
        // ✅ 開啟時，先更新資料再刷新顏色
        updateLandmassData();
      } else {
        // ✅ 關閉時，清空資料並刷新顏色
        setLandmassData(null);
        updateLandmassStats(null);
        debouncedRefreshColors(50);
      }
    });
  }

  console.log('✅ 陸地與島嶼開關初始化完成');
}

/**
 * ✅ 更新陸地與島嶼資料
 */
function updateLandmassData() {
  try {
    // ✅ 優先使用當前顯示的資料
    const nodes = state.currentNodes?.length > 0 ? state.currentNodes : getAllNodes();
    const edges = state.currentEdges?.length > 0 ? state.currentEdges : getAllEdges();
    
    if (!nodes || nodes.length === 0) {
      console.warn('⚠️ 沒有節點資料，無法分析陸地與島嶼');
      setLandmassData(null);
      updateLandmassStats(null);
      return;
    }
    
    if (!edges || edges.length === 0) {
      console.warn('⚠️ 沒有邊資料，無法分析連通分量');
      setLandmassData(null);
      updateLandmassStats(null);
      return;
    }
    
    console.log('🔍 開始分析連通分量...', {
      nodes: nodes.length,
      edges: edges.length
    });
    
    // ✅ 執行連通分量分析
    const result = findConnectedComponents(nodes, edges);
    setLandmassData(result);
    
    // ✅ 更新統計資訊顯示
    updateLandmassStats(result.stats);
    
    console.log('✅ 陸地與島嶼分析完成:', result.stats);
    
    // ✅ 分析完成後刷新顏色
    debouncedRefreshColors(50);
    
  } catch (error) {
    console.error('❌ 陸地與島嶼分析錯誤:', error);
    console.error('錯誤堆疊:', error.stack);
    setLandmassData(null);
    updateLandmassStats(null);
  }
}

/**
 * 更新陸地與島嶼統計資訊顯示
 */
function updateLandmassStats(stats) {
  const mainlandStats = document.getElementById('mainland-stats');
  const islandStats = document.getElementById('island-stats');
  
  if (mainlandStats) {
    if (stats && stats.mainlandNodes > 0) {
      mainlandStats.innerHTML = `
        <span>節點: ${stats.mainlandNodes}</span>
        <span>邊: ${stats.mainlandEdges}</span>
      `;
    } else {
      mainlandStats.innerHTML = '<span>無資料</span>';
    }
  }
  
  if (islandStats) {
    if (stats && stats.islandNodes > 0) {
      islandStats.innerHTML = `
        <span>節點: ${stats.islandNodes}</span>
        <span>邊: ${stats.islandEdges}</span>
      `;
    } else {
      islandStats.innerHTML = '<span>無資料</span>';
    }
  }
}

/**
 * ✅ 公開的更新函數（供 main.js 呼叫）
 */
export function updateLandmassDisplay() {
  // ✅ 只在開啟狀態下才更新
  if (state.showLandmass) {
    updateLandmassData();
  }
}

/**
 * ✅ 公開的顏色刷新函數（供其他模組呼叫）
 */
export function refreshColors() {
  refreshAllColors();
}

/**
 * ✅ 公開的防抖刷新函數（供其他模組呼叫）
 */
export function debouncedRefresh(delay = 100) {
  debouncedRefreshColors(delay);
}

/**
 * 初始化所有 UI 控制項
 */
export function initUIControls() {
  console.log('🚀 開始初始化 UI 控制項...');
  
  try {
    initCollapsiblePanels();
    initHighlightSwitch();
    initLegendToggle();
    initTyphoonTracker();
    initLandmassSwitch();
    
    console.log('✅ UI 控制項初始化完成！');
  } catch (error) {
    console.error('❌ UI 控制項初始化失敗:', error);
    console.error('錯誤堆疊:', error.stack);
  }
}