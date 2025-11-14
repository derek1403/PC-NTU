/**
 * UI 事件處理模組（WebGL 修正版）
 */

import { updatePlot } from './plotManager.js';
import { loadMultipleTyphoonImages } from './imageLoader.js';
import { updateStats } from './filterUI.js';
import { getMetadata, setSelectedNodeIndex, state } from './state.js';
import { buildEdgeCoordinates } from './graphProcessor.js';

let currentBoundNodes = null;
let currentClickHandler = null;

/**
 * ✅ 設定節點點擊事件（添加 WebGL 錯誤處理）
 */
export function setupNodeClickHandler(nodes) {
  const plotDiv = document.getElementById('plot');
  
  if (!plotDiv) {
    console.error('❌ 找不到 plot 元素');
    return;
  }
  
  // ✅ 檢查 WebGL 上下文是否有效
  if (!checkWebGLContext(plotDiv)) {
    console.error('❌ WebGL 上下文無效,無法綁定事件');
    return;
  }
  
  // 移除舊的事件監聽器
  if (currentClickHandler) {
    try {
      plotDiv.removeListener('plotly_click', currentClickHandler);
      console.log('🗑️ 已移除舊的點擊監聽器');
    } catch (e) {
      console.warn('移除舊監聽器時出錯:', e);
    }
  }
  
  currentBoundNodes = nodes;
  console.log('🔗 綁定節點點擊事件,節點數:', nodes.length);
  
  // 創建新的事件處理函數
  currentClickHandler = function(eventData) {
    try {
      handleNodeClick(eventData, plotDiv);
    } catch (error) {
      console.error('❌ 處理點擊事件時發生錯誤:', error);
      
      // ✅ WebGL 錯誤特殊處理
      if (error.message && error.message.includes('WebGL')) {
        alert('圖表發生錯誤,請刷新頁面 (F5)');
      }
    }
  };
  
  plotDiv.on('plotly_click', currentClickHandler);
  console.log('✅ 節點點擊事件綁定完成');
}

/**
 * ✅ 新增: 檢查 WebGL 上下文是否有效
 */
function checkWebGLContext(plotDiv) {
  try {
    // 嘗試獲取 canvas 元素
    const canvas = plotDiv.querySelector('canvas.gl-canvas');
    if (!canvas) {
      console.warn('⚠️ 找不到 WebGL canvas');
      return true; // 可能還沒渲染,允許繼續
    }
    
    // 檢查 WebGL 上下文
    const gl = canvas.getContext('webgl') || canvas.getContext('experimental-webgl');
    if (!gl) {
      console.error('❌ WebGL 上下文為 null');
      return false;
    }
    
    // 檢查上下文是否丟失
    if (gl.isContextLost()) {
      console.error('❌ WebGL 上下文已丟失');
      return false;
    }
    
    return true;
  } catch (e) {
    console.warn('⚠️ WebGL 檢查失敗:', e);
    return true; // 預設允許繼續
  }
}

/**
 * ✅ 抽取點擊處理邏輯
 */
function handleNodeClick(eventData, plotDiv) {
  console.log('🖱️ 偵測到點擊事件:', eventData);
  
  const point = eventData.points[0];

  if (!point) {
    console.warn('⚠️ 點擊資料為空');
    return;
  }
  
  const plotData = plotDiv.data;
  
  if (!plotData || plotData.length === 0) {
    console.error('❌ Plotly data 為空');
    return;
  }
  
  const nodeTraceIndex = plotData.length - 1;
  
  console.log(`點擊的 trace: ${point.curveNumber}, 節點 trace: ${nodeTraceIndex}`);
  
  if (point.curveNumber !== nodeTraceIndex) {
    console.log('點擊的不是節點 trace,忽略');
    return;
  }

  const nodeIndex = point.pointNumber;
  
  if (nodeIndex < 0 || nodeIndex >= currentBoundNodes.length) {
    console.error(`❌ 無效的節點索引: ${nodeIndex}, 節點總數: ${currentBoundNodes.length}`);
    return;
  }
  
  const node = currentBoundNodes[nodeIndex];

  if (!node) {
    console.error('❌ 找不到對應的節點');
    return;
  }

  setSelectedNodeIndex(nodeIndex);
  console.log(`🔍 選中節點: index=${nodeIndex}, id=${node.id}`);

  // ✅ 使用延遲執行,給 WebGL 時間清理
  setTimeout(() => {
    refreshPlotWithSelection(currentBoundNodes, nodeIndex);
    displayNodeInfo(node);
  }, 50);
}

/**
 * 刷新圖表並標記選中的節點
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
    
    // ✅ 現在使用 Plotly.react,不會重建 WebGL 上下文
    updatePlot(nodes, edgeData, edges.length, edges);
    
    console.log('✅ 圖表已刷新（含選中節點標記）');
  } catch (error) {
    console.error('❌ 刷新圖表時發生錯誤:', error);
    console.error('錯誤堆疊:', error.stack);
  }
}

/**
 * 顯示節點資訊
 */
function displayNodeInfo(node) {
  const tcIds = node.TC_ID || [];
  const times = node.time || [];
  const orders = node.order || [];

  let infoHTML = `
    <h3>🌀 颱風狀態</h3>
    <p><b>節點 ID:</b> ${node.id}</p>
    <p><b>RMW:</b> ${node.RMW ? (node.RMW / 1000).toFixed(0) : 'N/A'} km</p>
    <p><b>Vmax:</b> ${node.Vmax ? node.Vmax.toFixed(0) : 'N/A'} m/s</p>
    <p><b>IKE:</b> ${node.IKE ? node.IKE.toFixed(0) : 'N/A'} TJ</p>
    <p><b>座標:</b> (${node.x.toFixed(3)}, ${node.y.toFixed(3)}, ${node.z.toFixed(3)})</p>
  `;
  // 這個先不要，但是保留在註解上 <p><b>狀態參數:</b> ${node.info_text || 'N/A'}</p>

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