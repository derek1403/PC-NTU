/**
 * UI 事件處理模組（完全修正版）
 * ✅ 修正: 移除舊的事件監聽器,避免重複綁定
 */

import { updatePlot } from './plotManager.js';
import { loadMultipleTyphoonImages } from './imageLoader.js';
import { updateStats } from './filterUI.js';
import { getMetadata, setSelectedNodeIndex, state } from './state.js';
import { buildEdgeCoordinates } from './graphProcessor.js';

// ✅ 儲存當前綁定的節點陣列
let currentBoundNodes = null;

// ✅ 儲存事件處理函數的引用(用於移除)
let currentClickHandler = null;

/**
 * 設定節點點擊事件
 * @param {Array} nodes - 節點陣列
 */
export function setupNodeClickHandler(nodes) {
  const plotDiv = document.getElementById('plot');
  
  if (!plotDiv) {
    console.error('❌ 找不到 plot 元素');
    return;
  }
  
  // ✅ 關鍵修正: 移除舊的事件監聽器
  if (currentClickHandler) {
    try {
      plotDiv.removeListener('plotly_click', currentClickHandler);
      console.log('🗑️ 已移除舊的點擊監聽器');
    } catch (e) {
      console.warn('移除舊監聽器時出錯:', e);
    }
  }
  
  // 儲存節點陣列的參考
  currentBoundNodes = nodes;
  
  console.log('🔗 綁定節點點擊事件,節點數:', nodes.length);
  
  // ✅ 創建新的事件處理函數
  currentClickHandler = function(eventData) {
    console.log('🖱️ 偵測到點擊事件:', eventData);
    
    const point = eventData.points[0];

    // 檢查是否點擊的是節點
    if (!point) {
      console.warn('⚠️ 點擊資料為空');
      return;
    }
    
    // 動態計算 nodeTrace 的索引
    const plotData = plotDiv.data;
    
    if (!plotData || plotData.length === 0) {
      console.error('❌ Plotly data 為空');
      return;
    }
    
    const nodeTraceIndex = plotData.length - 1; // 最後一個 trace
    
    console.log(`點擊的 trace: ${point.curveNumber}, 節點 trace: ${nodeTraceIndex}`);
    
    if (point.curveNumber !== nodeTraceIndex) {
      console.log('點擊的不是節點 trace,忽略');
      return;
    }

    const nodeIndex = point.pointNumber;
    
    // 檢查索引是否有效
    if (nodeIndex < 0 || nodeIndex >= currentBoundNodes.length) {
      console.error(`❌ 無效的節點索引: ${nodeIndex}, 節點總數: ${currentBoundNodes.length}`);
      return;
    }
    
    const node = currentBoundNodes[nodeIndex];

    if (!node) {
      console.error('❌ 找不到對應的節點');
      return;
    }

    // 儲存選中的節點索引到全域狀態
    setSelectedNodeIndex(nodeIndex);

    console.log(`🔍 選中節點: index=${nodeIndex}, id=${node.id}`);

    // 重新渲染整個圖表
    refreshPlotWithSelection(currentBoundNodes, nodeIndex);

    // 顯示節點資訊
    displayNodeInfo(node);
  };
  
  // ✅ 綁定新的事件監聽器
  plotDiv.on('plotly_click', currentClickHandler);
  
  console.log('✅ 節點點擊事件綁定完成');
}

/**
 * 刷新圖表並標記選中的節點
 * @param {Array} nodes - 節點陣列
 * @param {number} selectedIndex - 選中的節點索引
 */
function refreshPlotWithSelection(nodes, selectedIndex) {
  console.log('🎨 開始刷新圖表...');
  
  if (!nodes || nodes.length === 0) {
    console.error('❌ 節點陣列為空,無法刷新圖表');
    return;
  }
  
  const edges = state.currentEdges || [];
  
  if (!edges || edges.length === 0) {
    console.warn('⚠️ 沒有邊資料,無法刷新圖表');
    return;
  }
  
  console.log(`📊 刷新資料: ${nodes.length} 個節點, ${edges.length} 條邊`);
  
  try {
    const edgeData = buildEdgeCoordinates(edges, nodes);
    
    if (!edgeData || !edgeData.x || !edgeData.y || !edgeData.z) {
      console.error('❌ 邊座標資料無效');
      return;
    }
    
    console.log('✅ 邊座標建立完成');
    
    // 重新渲染圖表
    updatePlot(nodes, edgeData, edges.length, edges);
    
    console.log('✅ 圖表已刷新（含選中節點標記）');
  } catch (error) {
    console.error('❌ 刷新圖表時發生錯誤:', error);
    console.error('錯誤堆疊:', error.stack);
  }
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
  
  const statsElement = document.getElementById('stats');
  if (statsElement) {
    infoHTML += statsElement.outerHTML;
  }

  document.getElementById('node-info').innerHTML = infoHTML;

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
    applyBtn.replaceWith(applyBtn.cloneNode(true));
    document.getElementById('apply-filter-btn').addEventListener('click', applyFilterCallback);
  }
  
  if (resetBtn) {
    resetBtn.replaceWith(resetBtn.cloneNode(true));
    document.getElementById('reset-filter-btn').addEventListener('click', resetFilterCallback);
  }
}