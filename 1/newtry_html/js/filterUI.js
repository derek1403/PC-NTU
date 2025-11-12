/**
 * 篩選介面邏輯模組
 * 負責讀取篩選條件並更新狀態
 */

import { updateFilter, resetFilter as resetStateFilter, getCurrentFilter } from './state.js';

/**
 * 解析颱風 ID 輸入
 * @param {string} input - 用戶輸入的字串
 * @returns {Array} 颱風 ID 陣列
 */
function parseTyphoonIds(input) {
  if (!input || input.trim() === '') {
    return [];
  }
  
  // 用逗號分隔，並移除空白
  return input
    .split(',')
    .map(id => id.trim())
    .filter(id => id !== '');
}

/**
 * 從 UI 讀取篩選條件
 * @returns {Object} 篩選條件物件
 */
export function readFilterFromUI() {
  const rmwMin = document.getElementById('rmw-min').value;
  const rmwMax = document.getElementById('rmw-max').value;
  const vmaxMin = document.getElementById('vmax-min').value;
  const vmaxMax = document.getElementById('vmax-max').value;
  const ikeMin = document.getElementById('ike-min').value;
  const ikeMax = document.getElementById('ike-max').value;
  
  // 讀取颱風 ID 搜尋
  const typhoonSearchInput = document.getElementById('typhoon-search').value;
  const typhoonIds = parseTyphoonIds(typhoonSearchInput);

  return {
    rmwMin: rmwMin ? parseFloat(rmwMin) : null,
    rmwMax: rmwMax ? parseFloat(rmwMax) : null,
    vmaxMin: vmaxMin ? parseFloat(vmaxMin) : null,
    vmaxMax: vmaxMax ? parseFloat(vmaxMax) : null,
    ikeMin: ikeMin ? parseFloat(ikeMin) : null,
    ikeMax: ikeMax ? parseFloat(ikeMax) : null,
    typhoonIds: typhoonIds
  };
}

/**
 * 重置 UI 篩選條件
 */
export function resetFilterUI() {
  document.getElementById('rmw-min').value = '';
  document.getElementById('rmw-max').value = '';
  document.getElementById('vmax-min').value = '';
  document.getElementById('vmax-max').value = '';
  document.getElementById('ike-min').value = '';
  document.getElementById('ike-max').value = '';
  document.getElementById('typhoon-search').value = '';
  
  resetStateFilter();
}

/**
 * 更新統計資訊顯示
 * @param {number} nodeCount - 顯示的節點數
 * @param {number} edgeCount - 顯示的邊數
 * @param {number} totalNodes - 總節點數
 * @param {number} totalEdges - 總邊數
 */
export function updateStats(nodeCount, edgeCount, totalNodes, totalEdges) {
  const filter = getCurrentFilter();
  const filterActive = filter.rmwMin !== null || filter.rmwMax !== null ||
                        filter.vmaxMin !== null || filter.vmaxMax !== null ||
                        filter.ikeMin !== null || filter.ikeMax !== null ||
                        (filter.typhoonIds && filter.typhoonIds.length > 0);

  let statsHTML = `<b>📊 資料統計:</b><br>`;
  
  if (filterActive) {
    statsHTML += `顯示節點: ${nodeCount} / ${totalNodes}<br>`;
    statsHTML += `顯示邊: ${edgeCount} / ${totalEdges}<br>`;
    
    // 顯示搜尋的颱風 ID
    if (filter.typhoonIds && filter.typhoonIds.length > 0) {
      statsHTML += `<span style="color: #3498db;">🔍 搜尋: ${filter.typhoonIds.join(', ')}</span><br>`;
    }
    
    statsHTML += `<span style="color: #e74c3c;">🎯 篩選已啟用</span>`;
  } else {
    statsHTML += `節點數: ${nodeCount}<br>`;
    statsHTML += `邊數: ${edgeCount}`;
  }

  const statsElement = document.getElementById('stats');
  if (statsElement) {
    statsElement.innerHTML = statsHTML;
  }
}