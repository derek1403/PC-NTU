/**
 * Plotly 繪圖管理模組（修正版）
 * 負責 3D 圖表的渲染與更新
 */

import { 
  getHighlightMode, 
  getTyphoonTracks, 
  getShowLandmass, 
  getLandmassData, 
  getSelectedNodeIndex 
} from './state.js';
import { findTyphoonPath, findPathEdges } from './typhoonTracker.js';
import { isNodeInComponent } from './componentAnalysis.js';

/**
 * 計算節點顏色（根據所有高亮模式和選中狀態）
 * 顏色優先級: 用戶選取(紅) > 起始/最終點 > 颱風路徑 > 陸地/島嶼 > 預設
 * @param {Array} nodes - 節點陣列
 * @param {number} selectedIndex - 選中的節點索引（可選，會自動從 state 讀取）
 * @returns {Array} 顏色陣列
 */
function calculateNodeColors(nodes, selectedIndex = null) {
  // ✅ 修正：從全域狀態讀取 selectedNodeIndex（同步方式）
  const finalSelectedIndex = selectedIndex !== null ? selectedIndex : getSelectedNodeIndex();
  
  const highlightMode = getHighlightMode();
  const typhoonTracks = getTyphoonTracks();
  const showLandmass = getShowLandmass();
  const landmassData = getLandmassData();
  
  // 預先計算颱風路徑節點集合（按優先級順序）
  const typhoonNodeColors = new Map();
  if (typhoonTracks && typhoonTracks.length > 0) {
    // 從後往前遍歷，這樣前面的會覆蓋後面的（優先級更高）
    for (let i = typhoonTracks.length - 1; i >= 0; i--) {
      const track = typhoonTracks[i];
      const pathIndices = findTyphoonPath(track.id, nodes);
      for (const idx of pathIndices) {
        typhoonNodeColors.set(idx, track.color);
      }
    }
  }
  
  return nodes.map((node, index) => {
    // 優先級 1: 選中的節點 → 紅色
    if (finalSelectedIndex !== null && index === finalSelectedIndex) {
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
    if (typhoonNodeColors.has(index)) {
      return typhoonNodeColors.get(index);
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
 * ✅ 修正版：計算每條邊的顏色（只標記連續 order 的邊）
 * @param {Array} edges - 邊陣列 [[u, v], ...]
 * @param {Array} nodes - 節點陣列
 * @returns {Array} 每條邊對應的顏色字串
 */
function calculateEdgeColors(edges, nodes) {
  const typhoonTracks = getTyphoonTracks();
  const showLandmass = getShowLandmass();
  const landmassData = getLandmassData();
  
  const defaultColor = 'rgba(150, 150, 150, 0.9)';
  
  // 如果沒有任何特殊標示，全部使用預設顏色
  if ((!typhoonTracks || typhoonTracks.length === 0) && !showLandmass) {
    return edges.map(() => defaultColor);
  }
  
  // ✅ 修正：預先計算所有颱風路徑的「合法邊集合」
  const typhoonEdgeSets = [];
  if (typhoonTracks && typhoonTracks.length > 0) {
    for (const track of typhoonTracks) {
      // 使用新的 findPathEdges，只返回連續 order 的邊
      const validEdges = findPathEdges(track.id, nodes, edges);
      typhoonEdgeSets.push({ color: track.color, edgeSet: validEdges });
    }
  }
  
  // 預先計算陸地和島嶼的節點集合
  const mainlandSet = (showLandmass && landmassData && landmassData.mainland) 
    ? new Set(landmassData.mainland) 
    : null;
  const islandSet = (showLandmass && landmassData && landmassData.largestIsland) 
    ? new Set(landmassData.largestIsland) 
    : null;
  
  // 為每條邊分配顏色
  return edges.map(([u, v]) => {
    // 優先級 1: 颱風路徑（第一個匹配的優先）
    for (const { color, edgeSet } of typhoonEdgeSets) {
      // ✅ 修正：檢查邊是否在「合法邊集合」中
      if (edgeSet.has(`${u}-${v}`) || edgeSet.has(`${v}-${u}`)) {
        return color;
      }
    }
    
    // 優先級 2: 陸地
    if (mainlandSet && mainlandSet.has(u) && mainlandSet.has(v)) {
      return 'rgba(46, 204, 113, 0.8)';
    }
    
    // 優先級 3: 島嶼
    if (islandSet && islandSet.has(u) && islandSet.has(v)) {
      return 'rgba(243, 156, 18, 0.8)';
    }
    
    // 預設顏色
    return defaultColor;
  });
}

/**
 * 構建邊的座標和顏色（分組渲染以提升效能）
 * @param {Array} edges - 邊陣列 [[u, v], ...]
 * @param {Array} nodes - 節點陣列
 * @param {Array} edgeColors - 每條邊的顏色
 * @returns {Array} Plotly trace 陣列
 */
function buildColoredEdgeTraces(edges, nodes, edgeColors) {
  // 將相同顏色的邊分組
  const colorGroups = new Map();
  
  for (let i = 0; i < edges.length; i++) {
    const [u, v] = edges[i];
    const color = edgeColors[i];
    
    if (!colorGroups.has(color)) {
      colorGroups.set(color, []);
    }
    colorGroups.get(color).push([u, v]);
  }
  
  // 為每組顏色創建一個 trace
  const traces = [];
  
  for (const [color, edgeGroup] of colorGroups) {
    const x = [], y = [], z = [];
    
    for (const [u, v] of edgeGroup) {
      // 安全檢查
      if (u >= nodes.length || v >= nodes.length || u < 0 || v < 0) {
        console.warn(`無效的邊: [${u}, ${v}]`);
        continue;
      }
      
      x.push(nodes[u].x, nodes[v].x, null);
      y.push(nodes[u].y, nodes[v].y, null);
      z.push(nodes[u].z, nodes[v].z, null);
    }
    
    traces.push({
      x, y, z,
      mode: 'lines',
      type: 'scatter3d',
      line: { 
        color, 
        width: color === 'rgba(150, 150, 150, 0.9)' ? 1 : 2 // 特殊顏色用較粗的線
      },
      hoverinfo: 'skip',
      showlegend: false
    });
  }
  
  return traces;
}

/**
 * 更新 3D 圖表
 * @param {Array} nodes - 節點陣列
 * @param {Object} edgeData - 邊的資料（向後兼容）
 * @param {number} filteredEdgeCount - 篩選後的邊數量
 * @param {Array} edges - 邊陣列 [[u, v], ...]（可選，用於彩色邊）
 */
export function updatePlot(nodes, edgeData, filteredEdgeCount, edges = null) {
  const nodeColors = calculateNodeColors(nodes);
  
  let edgeTraces = [];
  
  // 如果提供了 edges 陣列，使用彩色邊渲染
  if (edges && Array.isArray(edges) && edges.length > 0) {
    try {
      const edgeColors = calculateEdgeColors(edges, nodes);
      edgeTraces = buildColoredEdgeTraces(edges, nodes, edgeColors);
    } catch (error) {
      console.error('邊渲染錯誤:', error);
      // 降級到單色邊
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
  } else {
    // 向後兼容：使用單色邊
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

  try {
    //Plotly.newPlot('plot', [...edgeTraces, nodeTrace], layout, config);
    console.log(`✅ 沒有Plotly.newPlot`);
    console.log(`✅ 圖表渲染完成: ${edgeTraces.length} 個邊 trace, 1 個節點 trace`);
  } catch (error) {
    console.error('Plotly 渲染錯誤:', error);
  }
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
      const plotDiv = document.getElementById('plot');
      if (!plotDiv || !plotDiv.data) {
        console.warn('圖表尚未初始化');
        return;
      }
      
      const traceIndex = plotDiv.data.length - 1;
      Plotly.restyle('plot', { 'marker.color': [newColors] }, [traceIndex]);
    } catch (e) {
      console.error("Plotly restyle 錯誤:", e);
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