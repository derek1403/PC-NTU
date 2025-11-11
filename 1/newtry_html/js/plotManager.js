/**
 * Plotly 繪圖管理模組
 * 負責 3D 圖表的渲染與更新
 */

import { getHighlightMode } from './state.js';

/**
 * 計算節點顏色（根據高亮模式和選中狀態）
 * @param {Array} nodes - 節點陣列
 * @param {number} selectedIndex - 選中的節點索引
 * @returns {Array} 顏色陣列
 */
function calculateNodeColors(nodes, selectedIndex = null) {
  const highlightMode = getHighlightMode();
  
  return nodes.map((node, index) => {
    // 優先級 1: 選中的節點 → 紅色
    if (selectedIndex !== null && index === selectedIndex) {
      return '#e74c3c'; // 紅色
    }
    
    // 優先級 2: 高亮模式開啟時
    if (highlightMode) {
      // 起始點 (order === 1) → 藍色
      console.log(node.order.includes(1))
      console.log(node.order )
      console.log('a' )
      if (node.order.includes(1)) {
        //return '#3498db'; // 藍色
        return '#cc0404ff'; // 藍色
      }
      console.log('b' )
      // 最終點 (reverse_order === 1) → 橘色
      if (node.reverse_order.includes(1)) {
        return '#e67e22'; // 橘色
      }
    }
    
    // 預設顏色
    return '#4a90e2'; // 淺藍色
  });
}

/**
 * 更新 3D 圖表
 * @param {Array} nodes - 節點陣列
 * @param {Object} edgeData - 邊的座標 {x, y, z}
 * @param {number} filteredEdgeCount - 篩選後的邊數量
 */
export function updatePlot(nodes, edgeData, filteredEdgeCount) {
  const nodeColors = calculateNodeColors(nodes);
  
  // 邊的軌跡
  const edgeTrace = {
    x: edgeData.x,
    y: edgeData.y,
    z: edgeData.z,
    mode: 'lines',
    type: 'scatter3d',
    line: { 
      color: 'rgba(150, 150, 150, 0.9)',
      width: 1
    },
    hoverinfo: 'skip',
    name: `時間演化 (${filteredEdgeCount} 條邊)`
  };

  // 節點的軌跡
  const nodeTrace = {
    x: nodes.map(n => n.x),
    y: nodes.map(n => n.y),
    z: nodes.map(n => n.z),
    mode: 'markers',
    type: 'scatter3d',
    marker: {
      size: 5,
      color: nodeColors,
      opacity: 0.8,
      line: { width: 0.5, color: 'white' }
    },
    hovertext: nodes.map(n => n.info_text || `Node ${n.id}`),
    hoverinfo: 'text',
    name: `颱風狀態 (${nodes.length} 個)`
  };

  // 圖表配置
  const layout = {
    margin: { l: 0, r: 0, t: 0, b: 0 },
    scene: { 
      xaxis: { title: 'Layout X', showgrid: true },
      yaxis: { title: 'Layout Y', showgrid: true },
      zaxis: { title: 'Layout Z', showgrid: true },
      camera: {
        eye: { x: 1.5, y: 1.5, z: 1.5 }
      },
      bgcolor: '#f8f9fa'
    },
    hovermode: 'closest',
    showlegend: true,
    legend: {
      x: 0.02,
      y: 0.98,
      bgcolor: 'rgba(255,255,255,0.9)'
    }
  };

  const config = {
    responsive: true,
    displayModeBar: true,
    displaylogo: false
  };

  Plotly.newPlot('plot', [edgeTrace, nodeTrace], layout, config);
}

/**
 * 更新節點顏色（用於高亮選中的節點或高亮模式變更）
 * @param {Array} nodes - 節點陣列
 * @param {number} selectedIndex - 選中的節點索引
 */
export function updateNodeColors(nodes, selectedIndex) {
  const newColors = calculateNodeColors(nodes, selectedIndex);

  setTimeout(() => {
    try {
      Plotly.restyle('plot', { 'marker.color': [newColors] }, [1]); // nodeTrace 是第二個 (index=1)
    } catch (e) {
      console.error("Plotly restyle error:", e);
    }
  }, 0);
}

/**
 * 更新節點顏色（含高亮模式）- 別名函數
 * @param {Array} nodes - 節點陣列
 * @param {number} selectedIndex - 選中的節點索引
 */
export function updatePlotWithHighlight(nodes, selectedIndex = null) {
  updateNodeColors(nodes, selectedIndex);
}