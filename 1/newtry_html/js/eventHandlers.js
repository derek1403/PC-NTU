/**
 * UI 事件處理模組（修正版）
 * 負責處理節點點擊、篩選按鈕等事件
 * ✅ 修正：點擊節點時同時更新 node 和 edge 顏色
 */

import { updatePlot } from './plotManager.js';
import { loadMultipleTyphoonImages } from './imageLoader.js';
import { updateStats } from './filterUI.js';
import { getMetadata, setSelectedNodeIndex, state } from './state.js';
import { buildEdgeCoordinates } from './graphProcessor.js';

/**
 * 設定節點點擊事件
 * @param {Array} nodes - 節點陣列
 */
export function setupNodeClickHandler(nodes) {
  const plotDiv = document.getElementById('plot');
  
  // 解綁舊的事件（避免重複綁定）
  plotDiv.removeAllListeners('plotly_click');
  
  plotDiv.on('plotly_click', function(eventData) {
    const point = eventData.points[0];

    // 檢查是否點擊的是節點（nodeTrace 是最後一個 trace）
    if (!point) return;
    
    // 計算 nodeTrace 的索引（最後一個）
    const nodeTraceIndex = plotDiv.data.length - 1;
    
    if (point.curveNumber !== nodeTraceIndex) {
      return;
    }

    const nodeIndex = point.pointNumber;
    const node = nodes[nodeIndex];

    if (!node) return;

    // ✅ 修正：儲存選中的節點索引到全域狀態
    setSelectedNodeIndex(nodeIndex);

    console.log(`🔍 選中節點: index=${nodeIndex}, id=${node.id}`);

    // ✅ 修正：重新渲染整個圖表（包含 node 和 edge 的顏色）
    refreshPlotWithSelection(nodes, nodeIndex);

    // 顯示節點資訊
    displayNodeInfo(node);

  });
}

/**
 * ✅ 新增：刷新圖表並標記選中的節點
 * @param {Array} nodes - 節點陣列
 * @param {number} selectedIndex - 選中的節點索引
 */
function refreshPlotWithSelection(nodes, selectedIndex) {
  // 取得當前的邊
  const edges = state.currentEdges || [];
  
  if (edges.length === 0) {
    console.warn('沒有邊資料，無法刷新圖表');
    return;
  }
  
  // 重新建立邊的座標
  const edgeData = buildEdgeCoordinates(edges, nodes);
  
  // 重新渲染圖表（updatePlot 內部會讀取 selectedNodeIndex）
  console.log('✅ 開始 updatePlot(nodes, edgeData, edges.length, edges) X');
  updatePlot(nodes, edgeData, edges.length, edges);
  console.log('✅ 開始 updatePlot(nodes, edgeData, edges.length, edges) ');
  
  console.log('✅ 圖表已刷新（含選中節點標記）');
}

/**
 * 顯示節點資訊
 * @param {Object} node - 節點物件
 */
function displayNodeInfo(node) {
  const tcIds = node.TC_ID || [];
  const times = node.time || [];
  const orders = node.order || [];

  let infoHTML = `
    <h3>🌀 颱風狀態</h3>
    <p><b>節點 ID:</b> ${node.id}</p>
    <p><b>狀態參數:</b> ${node.info_text || 'N/A'}</p>
    <p><b>RMW:</b> ${node.RMW ? node.RMW.toFixed(1) : 'N/A'} km</p>
    <p><b>Vmax:</b> ${node.Vmax ? node.Vmax.toFixed(2) : 'N/A'} m/s</p>
    <p><b>IKE:</b> ${node.IKE ? node.IKE.toFixed(2) : 'N/A'} TJ</p>
    <p><b>座標:</b> (${node.x.toFixed(3)}, ${node.y.toFixed(3)}, ${node.z.toFixed(3)})</p>
  `;

  if (tcIds.length > 0) {
    infoHTML += `<hr style="margin: 15px 0; border: none; border-top: 1px solid #ddd;">`;
    infoHTML += `<p><b>颱風編號:</b> ${tcIds.join(', ')}</p>`;
    infoHTML += `<p><b>時間:</b> ${times[0] || 'N/A'}</p>`;
    infoHTML += `<p><b>順序:</b> ${orders.join(', ')}</p>`;
  }

  infoHTML += `<hr style="margin: 15px 0; border: none; border-top: 1px solid #ddd;">`;
  infoHTML += `<div id="image-container" class="image-container"></div>`;
  
  // 保留統計資訊
  const statsElement = document.getElementById('stats');
  if (statsElement) {
    infoHTML += statsElement.outerHTML;
  }

  document.getElementById('node-info').innerHTML = infoHTML;

  // 載入颱風圖片
  const imageContainer = document.getElementById('image-container');
  if (tcIds.length > 0 && times.length > 0 && orders.length > 0) {
    loadMultipleTyphoonImages(tcIds, times, orders, imageContainer);
  } else {
    imageContainer.innerHTML = '<div class="image-loading" style="color: #999;">⚠️ 無圖片資訊</div>';
  }
}

/**
 * 設定篩選按鈕事件
 * @param {Function} applyFilterCallback - 套用篩選的回調函數
 * @param {Function} resetFilterCallback - 重置篩選的回調函數
 */
export function setupFilterButtons(applyFilterCallback, resetFilterCallback) {
  const applyBtn = document.getElementById('apply-filter-btn');
  const resetBtn = document.getElementById('reset-filter-btn');
  
  if (applyBtn) {
    // 移除舊的事件監聽器（避免重複綁定）
    applyBtn.replaceWith(applyBtn.cloneNode(true));
    document.getElementById('apply-filter-btn').addEventListener('click', applyFilterCallback);
  }
  
  if (resetBtn) {
    resetBtn.replaceWith(resetBtn.cloneNode(true));
    document.getElementById('reset-filter-btn').addEventListener('click', resetFilterCallback);
  }
}