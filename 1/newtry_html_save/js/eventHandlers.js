/**
 * UI 事件處理模組
 * 負責處理節點點擊、篩選按鈕等事件
 */

import { updateNodeColors } from './plotManager.js';
import { loadMultipleTyphoonImages } from './imageLoader.js';
import { updateStats } from './filterUI.js';
import { getMetadata } from './state.js';

/**
 * 設定節點點擊事件
 * @param {Array} nodes - 節點陣列
 */
export function setupNodeClickHandler(nodes) {
  const plotDiv = document.getElementById('plot');
  const nodeTraceIndex = 1; // nodeTrace 是第二個軌跡

  plotDiv.on('plotly_click', function(eventData) {
    const point = eventData.points[0];

    if (!point || point.curveNumber !== nodeTraceIndex) {
      return;
    }

    const nodeIndex = point.pointNumber;
    const node = nodes[nodeIndex];

    if (!node) return;

    // 高亮選中的節點
    updateNodeColors(nodes, nodeIndex);

    // 顯示節點資訊
    displayNodeInfo(node);
  });
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
  document.getElementById('apply-filter-btn').addEventListener('click', applyFilterCallback);
  document.getElementById('reset-filter-btn').addEventListener('click', resetFilterCallback);
}