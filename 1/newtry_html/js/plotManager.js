/**
 * Plotly 繪圖管理模組
 * 負責 3D 圖表的渲染與更新
 */

import { getHighlightMode, getTyphoonTracks, getShowLandmass, getLandmassData } from './state.js';
import { assignPathColors } from './typhoonTracker.js';
import { isNodeInComponent } from './componentAnalysis.js';

/**
 * 計算節點顏色（根據所有高亮模式和選中狀態）
 * 顏色優先級: 用戶選取(紅) > 起始/最終點 > 颱風路徑 > 陸地/島嶼 > 預設
 * @param {Array} nodes - 節點陣列
 * @param {number} selectedIndex - 選中的節點索引
 * @returns {Array} 顏色陣列
 */
function calculateNodeColors(nodes, selectedIndex = null) {
  const highlightMode = getHighlightMode();
  const typhoonTracks = getTyphoonTracks();
  const showLandmass = getShowLandmass();
  const landmassData = getLandmassData();
  
  // 預先計算颱風路徑顏色映射
  const typhoonColorMap = typhoonTracks.length > 0 
    ? assignPathColors(typhoonTracks, nodes) 
    : new Map();
  
  return nodes.map((node, index) => {
    // 優先級 1: 選中的節點 → 紅色
    if (selectedIndex !== null && index === selectedIndex) {
      return '#e74c3c';
    }
    
    // 優先級 2: 高亮模式開啟時（起始點和最終點）
    if (highlightMode) {
      const hasStart = node.order && node.order.includes(1);
      const hasEnd = node.reverse_orders && node.reverse_orders.includes(1);
      
      if (hasStart && hasEnd) {
        return '#9c0bc0ff'; // 紫色（既是起點也是終點）
      }
      if (hasStart) {
        return '#04cc0eff'; // 綠色（起點）
      }
      if (hasEnd) {
        return '#e67e22'; // 橘色（終點）
      }
    }
    
    // 優先級 3: 颱風路徑追蹤
    if (typhoonColorMap.has(index)) {
      return typhoonColorMap.get(index);
    }
    
    // 優先級 4: 陸地與島嶼
    if (showLandmass && landmassData) {
      if (landmassData.mainland && isNodeInComponent(index, landmassData.mainland)) {
        return '#2ecc71'; // 綠色（陸地）
      }
      if (landmassData.largestIsland && isNodeInComponent(index, landmassData.largestIsland)) {
        return '#f39c12'; // 橘黃色（最大島嶼）
      }
    }
    
    // 預設顏色
    return '#4a90e2';
  });
}

/**
 * 計算邊的顏色
 * @param {Array} edges - 邊陣列 [[u, v], ...]
 * @param {Array} nodes - 節點陣列
 * @returns {Array} 顏色陣列
 */
function calculateEdgeColors(edges, nodes) {
  const typhoonTracks = getTyphoonTracks();
  const showLandmass = getShowLandmass();
  const landmassData = getLandmassData();
  
  // 預設顏色
  const defaultColor = 'rgba(150, 150, 150, 0.9)';
  
  // 如果沒有任何特殊標示，返回預設顏色
  if (typhoonTracks.length === 0 && !showLandmass) {
    return Array(edges.length).fill(defaultColor);
  }
  
  const edgeColors = [];
  
  for (let i = 0; i < edges.length; i++) {
    const [u, v] = edges[i];
    let color = defaultColor;
    
    // 優先級 1: 颱風路徑（按用戶輸入順序，第一個優先）
    for (const track of typhoonTracks) {
      const pathNodes = nodes.filter(node => 
        node.TC_ID && node.TC_ID.includes(track.id)
      ).map((_, idx) => nodes.findIndex(n => n === _));
      
      if (pathNodes.includes(u) && pathNodes.includes(v)) {
        color = track.color;
        break;
      }
    }
    
    // 優先級 2: 陸地與島嶼（如果沒被颱風路徑覆蓋）
    if (color === defaultColor && showLandmass && landmassData) {
      if (landmassData.mainland) {
        const mainlandSet = new Set(landmassData.mainland);
        if (mainlandSet.has(u) && mainlandSet.has(v)) {
          color = 'rgba(46, 204, 113, 0.8)'; // 綠色（陸地）
        }
      }
      
      if (color === defaultColor && landmassData.largestIsland) {
        const islandSet = new Set(landmassData.largestIsland);
        if (islandSet.has(u) && islandSet.has(v)) {
          color = 'rgba(243, 156, 18, 0.8)'; // 橘黃色（島嶼）
        }
      }
    }
    
    edgeColors.push(color);
  }
  
  return edgeColors;
}

/**
 * 構建邊的座標和顏色（用於多色邊）
 * @param {Array} edges - 邊陣列
 * @param {Array} nodes - 節點陣列
 * @param {Array} edgeColors - 邊顏色陣列
 * @returns {Array} Plotly trace 陣列
 */
function buildColoredEdgeTraces(edges, nodes, edgeColors) {
  // 將相同顏色的邊分組
  const colorGroups = new Map();
  
  for (let i = 0; i < edges.length; i++) {
    const color = edgeColors[i];
    if (!colorGroups.has(color)) {
      colorGroups.set(color, []);
    }
    colorGroups.get(color).push(edges[i]);
  }
  
  // 為每組顏色創建一個 trace
  const traces = [];
  
  for (const [color, edgeGroup] of colorGroups) {
    const x = [], y = [], z = [];
    
    for (const [u, v] of edgeGroup) {
      if (u >= nodes.length || v >= nodes.length) continue;
      x.push(nodes[u].x, nodes[v].x, null);
      y.push(nodes[u].y, nodes[v].y, null);
      z.push(nodes[u].z, nodes[v].z, null);
    }
    
    traces.push({
      x, y, z,
      mode: 'lines',
      type: 'scatter3d',
      line: { color, width: 2 },
      hoverinfo: 'skip',
      showlegend: false
    });
  }
  
  return traces;
}

/**
 * 更新 3D 圖表
 * @param {Array} nodes - 節點陣列
 * @param {Object} edgeData - 邊的資料 { edges, ... }
 * @param {number} filteredEdgeCount - 篩選後的邊數量
 */
export function updatePlot(nodes, edgeData, filteredEdgeCount, edges = null) {
  const nodeColors = calculateNodeColors(nodes);
  
  // 如果有 edges 參數，使用彩色邊
  let edgeTraces = [];
  if (edges && edges.length > 0) {
    const edgeColors = calculateEdgeColors(edges, nodes);
    edgeTraces = buildColoredEdgeTraces(edges, nodes, edgeColors);
  } else {
    // 單色邊（向後兼容）
    edgeTraces = [{
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
    }];
  }

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

  Plotly.newPlot('plot', [...edgeTraces, nodeTrace], layout, config);
}

/**
 * 更新節點顏色（用於高亮選中的節點或模式變更）
 * @param {Array} nodes - 節點陣列
 * @param {number} selectedIndex - 選中的節點索引
 */
export function updateNodeColors(nodes, selectedIndex) {
  const newColors = calculateNodeColors(nodes, selectedIndex);

  setTimeout(() => {
    try {
      // nodeTrace 是最後一個 trace
      const traceIndex = document.getElementById('plot').data.length - 1;
      Plotly.restyle('plot', { 'marker.color': [newColors] }, [traceIndex]);
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