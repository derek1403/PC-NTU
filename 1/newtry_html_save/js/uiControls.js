/**
 * UI 控制模組
 * 處理摺疊面板和開關邏輯
 */

import { state, setHighlightMode } from './state.js';
import { getAllNodes } from './state.js';
import { updatePlotWithHighlight } from './plotManager.js';

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
      
      // 更新箭頭方向
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
      
      // 更新箭頭方向
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
      
      // 更新圖表顏色
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
    // 預設隱藏圖例
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
 * 刷新圖表顏色（根據高亮模式）
 */
function refreshPlotColors() {
  const nodes = getAllNodes();
  if (!nodes || nodes.length === 0) return;

  // 呼叫 plotManager 更新顏色
  updatePlotWithHighlight(nodes, state.selectedNodeIndex);
}

/**
 * 初始化所有 UI 控制項
 */
export function initUIControls() {
  initCollapsiblePanels();
  initHighlightSwitch();
  initLegendToggle();
  console.log('✅ UI 控制項初始化完成');
}