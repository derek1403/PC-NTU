/**
 * UI 控制模組
 * 處理摺疊面板、開關和颱風追蹤 UI
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
  getAllNodes
} from './state.js';
import { updatePlotWithHighlight } from './plotManager.js';
import { validateTyphoonId } from './typhoonTracker.js';
import { findConnectedComponents } from './componentAnalysis.js';

// 預設顏色列表
const DEFAULT_COLORS = [
  '#e74c3c', '#3498db', '#2ecc71', '#f39c12', '#9b59b6',
  '#1abc9c', '#e67e22', '#34495e', '#16a085', '#27ae60',
  '#2980b9', '#8e44ad', '#c0392b', '#d35400', '#7f8c8d'
];

let colorIndex = 0;

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
      
      console.log(`高亮模式: ${isEnabled ? '開啟' : '關閉'}`);
      
      refreshPlotColors();
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
    legendElement.style.display = 'none';
    
    legendToggleBtn.addEventListener('click', () => {
      const isHidden = legendElement.style.display === 'none';
      legendElement.style.display = isHidden ? 'block' : 'none';
      
      console.log(`圖例: ${isHidden ? '顯示' : '隱藏'}`);
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

  input.addEventListener('change', () => {
    const typhoonId = input.value.trim();
    if (typhoonId) {
      const nodes = getAllNodes();
      if (validateTyphoonId(typhoonId, nodes)) {
        addTyphoonTrack(typhoonId, colorPicker.value);
        input.classList.remove('invalid');
        refreshPlotColors();
      } else {
        alert(`找不到颱風 ID: ${typhoonId}`);
        input.classList.add('invalid');
      }
    }
  });

  colorPicker.addEventListener('change', () => {
    updateTrackColor(trackIndex, colorPicker.value);
  });

  removeBtn.addEventListener('click', () => {
    removeTrackUI(trackIndex, trackDiv);
  });
}

/**
 * 更新颱風追蹤的顏色
 */
function updateTrackColor(index, color) {
  const tracks = getTyphoonTracks();
  if (tracks[index]) {
    tracks[index].color = color;
    setTyphoonTracks(tracks);
    refreshPlotColors();
  }
}

/**
 * 移除颱風追蹤 UI
 */
function removeTrackUI(index, element) {
  removeTyphoonTrack(index);
  element.remove();
  refreshPlotColors();
  
  // 重新索引剩餘的追蹤項目
  const container = document.getElementById('typhoon-tracks-container');
  const items = container.querySelectorAll('.track-item');
  items.forEach((item, i) => {
    item.dataset.index = i;
  });
}

/**
 * 初始化陸地與島嶼開關
 */
export function initLandmassSwitch() {
  const landmassSwitch = document.getElementById('landmass-switch');
  const landmassInfoBtn = document.getElementById('landmass-info-btn');
  const landmassInfo = document.getElementById('landmass-info');
  
  if (landmassInfo) {
    landmassInfo.style.display = 'none';
  }
  
  if (landmassInfoBtn && landmassInfo) {
    landmassInfoBtn.addEventListener('click', () => {
      const isHidden = landmassInfo.style.display === 'none';
      landmassInfo.style.display = isHidden ? 'block' : 'none';
    });
  }
  
  if (landmassSwitch) {
    landmassSwitch.addEventListener('change', (e) => {
      const isEnabled = e.target.checked;
      setShowLandmass(isEnabled);
      
      console.log(`陸地與島嶼標示: ${isEnabled ? '開啟' : '關閉'}`);
      
      if (isEnabled) {
        updateLandmassData();
      }
      
      refreshPlotColors();
    });
  }

  console.log('✅ 陸地與島嶼開關初始化完成');
}

/**
 * 更新陸地與島嶼資料
 */
function updateLandmassData() {
  const nodes = getAllNodes();
  if (!nodes || nodes.length === 0) return;
  
  // 從 state 取得當前顯示的邊（需要從 main.js 傳入）
  // 這裡我們需要修改 main.js 來儲存當前的 filteredEdges
  const edges = state.currentEdges || [];
  
  const result = findConnectedComponents(nodes, edges);
  setLandmassData(result);
  
  // 更新統計資訊顯示
  updateLandmassStats(result.stats);
}

/**
 * 更新陸地與島嶼統計資訊顯示
 */
function updateLandmassStats(stats) {
  const mainlandStats = document.getElementById('mainland-stats');
  const islandStats = document.getElementById('island-stats');
  
  if (mainlandStats && stats) {
    mainlandStats.innerHTML = `
      <span>節點: ${stats.mainlandNodes}</span>
      <span>邊: ${stats.mainlandEdges}</span>
    `;
  }
  
  if (islandStats && stats) {
    islandStats.innerHTML = `
      <span>節點: ${stats.islandNodes}</span>
      <span>邊: ${stats.islandEdges}</span>
    `;
  }
}

/**
 * 刷新圖表顏色（根據所有模式）
 */
function refreshPlotColors() {
  const nodes = getAllNodes();
  if (!nodes || nodes.length === 0) return;

  updatePlotWithHighlight(nodes, state.selectedNodeIndex);
}

/**
 * 公開的更新函數（供 main.js 呼叫）
 */
export function updateLandmassDisplay() {
  updateLandmassData();
  refreshPlotColors();
}

/**
 * 初始化所有 UI 控制項
 */
export function initUIControls() {
  initCollapsiblePanels();
  initHighlightSwitch();
  initLegendToggle();
  initTyphoonTracker();
  initLandmassSwitch();
  console.log('✅ UI 控制項初始化完成');
}