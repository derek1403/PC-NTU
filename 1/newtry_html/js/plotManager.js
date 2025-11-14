/**
 * Plotly 繪圖管理模組（WebGL 修正版）
 * ✅ 修正: 使用 Plotly.react() 避免 WebGL 上下文丟失
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

// ✅ 新增: 追蹤圖表是否已初始化
let isPlotInitialized = false;

/**
 * 計算節點顏色（根據所有高亮模式和選中狀態）
 */
function calculateNodeColors(nodes, selectedIndex = null) {
  const finalSelectedIndex = selectedIndex !== null ? selectedIndex : getSelectedNodeIndex();
  const highlightMode = getHighlightMode();
  const typhoonTracks = getTyphoonTracks();
  const showLandmass = getShowLandmass();
  const landmassData = getLandmassData();
  
  const typhoonNodeColors = new Map();
  if (typhoonTracks && typhoonTracks.length > 0) {
    for (let i = typhoonTracks.length - 1; i >= 0; i--) {
      const track = typhoonTracks[i];
      const pathIndices = findTyphoonPath(track.id, nodes);
      for (const idx of pathIndices) {
        typhoonNodeColors.set(idx, track.color);
      }
    }
  }
  
  return nodes.map((node, index) => {
    if (finalSelectedIndex !== null && index === finalSelectedIndex) {
      return '#e74c3c';
    }
    
    if (highlightMode) {
      const hasStart = node.order && node.order.includes(1);
      const hasEnd = node.reverse_orders && node.reverse_orders.includes(1);
      
      if (hasStart && hasEnd) {
        return '#9c0bc0ff';
      }
      if (hasStart) {
        return '#04cc0eff';
      }
      if (hasEnd) {
        return '#e67e22';
      }
    }
    
    if (typhoonNodeColors.has(index)) {
      return typhoonNodeColors.get(index);
    }
    
    if (showLandmass && landmassData) {
      if (landmassData.mainland && isNodeInComponent(index, landmassData.mainland)) {
        return '#2ecc71';
      }
      if (landmassData.largestIsland && isNodeInComponent(index, landmassData.largestIsland)) {
        return '#f39c12';
      }
    }
    
    return '#4a90e2';
  });
}

/**
 * 計算每條邊的顏色
 */
function calculateEdgeColors(edges, nodes) {
  const typhoonTracks = getTyphoonTracks();
  const showLandmass = getShowLandmass();
  const landmassData = getLandmassData();
  
  const defaultColor = 'rgba(150, 150, 150, 0.9)';
  
  if ((!typhoonTracks || typhoonTracks.length === 0) && !showLandmass) {
    return edges.map(() => defaultColor);
  }
  
  const typhoonEdgeSets = [];
  if (typhoonTracks && typhoonTracks.length > 0) {
    for (const track of typhoonTracks) {
      const validEdges = findPathEdges(track.id, nodes, edges);
      typhoonEdgeSets.push({ color: track.color, edgeSet: validEdges });
    }
  }
  
  const mainlandSet = (showLandmass && landmassData && landmassData.mainland) 
    ? new Set(landmassData.mainland) 
    : null;
  const islandSet = (showLandmass && landmassData && landmassData.largestIsland) 
    ? new Set(landmassData.largestIsland) 
    : null;
  
  return edges.map(([u, v]) => {
    for (const { color, edgeSet } of typhoonEdgeSets) {
      if (edgeSet.has(`${u}-${v}`) || edgeSet.has(`${v}-${u}`)) {
        return color;
      }
    }
    
    if (mainlandSet && mainlandSet.has(u) && mainlandSet.has(v)) {
      return 'rgba(46, 204, 113, 0.8)';
    }
    
    if (islandSet && islandSet.has(u) && islandSet.has(v)) {
      return 'rgba(243, 156, 18, 0.8)';
    }
    
    return defaultColor;
  });
}

/**
 * 構建邊的座標和顏色
 */
function buildColoredEdgeTraces(edges, nodes, edgeColors) {
  const colorGroups = new Map();
  
  for (let i = 0; i < edges.length; i++) {
    const [u, v] = edges[i];
    const color = edgeColors[i];
    
    if (!colorGroups.has(color)) {
      colorGroups.set(color, []);
    }
    colorGroups.get(color).push([u, v]);
  }
  
  const traces = [];
  
  for (const [color, edgeGroup] of colorGroups) {
    const x = [], y = [], z = [];
    
    for (const [u, v] of edgeGroup) {
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
        width: color === 'rgba(150, 150, 150, 0.9)' ? 1 : 2
      },
      hoverinfo: 'skip',
      showlegend: false
    });
  }
  
  return traces;
}

/**
 * ✅ 關鍵修正: 更新 3D 圖表（使用 Plotly.react 而非 newPlot）
 */
export function updatePlot(nodes, edgeData, filteredEdgeCount, edges = null) {
  const plotDiv = document.getElementById('plot');
  
  // ✅ WebGL 上下文檢查
  if (!plotDiv) {
    console.error('❌ 找不到 plot 元素');
    return;
  }
  
  const nodeColors = calculateNodeColors(nodes);
  
  let edgeTraces = [];
  
  if (edges && Array.isArray(edges) && edges.length > 0) {
    try {
      const edgeColors = calculateEdgeColors(edges, nodes);
      edgeTraces = buildColoredEdgeTraces(edges, nodes, edgeColors);
    } catch (error) {
      console.error('邊渲染錯誤:', error);
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
    // ✅ 關鍵修正: 第一次使用 newPlot,之後使用 react
    if (!isPlotInitialized) {
      console.log('🎨 首次渲染圖表 (使用 Plotly.newPlot)');
      Plotly.newPlot(plotDiv, [...edgeTraces, nodeTrace], layout, config);
      isPlotInitialized = true;
    } else {
      console.log('🔄 更新圖表 (使用 Plotly.react)');
      Plotly.react(plotDiv, [...edgeTraces, nodeTrace], layout, config);
    }
    
    console.log(`✅ 圖表渲染完成: ${edgeTraces.length} 個邊 trace, 1 個節點 trace`);
  } catch (error) {
    console.error('❌ Plotly 渲染錯誤:', error);
    
    // ✅ WebGL 錯誤恢復機制
    if (error.message && error.message.includes('bindFramebuffer')) {
      console.warn('⚠️ 檢測到 WebGL 錯誤,嘗試重新初始化...');
      isPlotInitialized = false;
      
      // 延遲後重試
      setTimeout(() => {
        try {
          Plotly.newPlot(plotDiv, [...edgeTraces, nodeTrace], layout, config);
          isPlotInitialized = true;
          console.log('✅ WebGL 恢復成功');
        } catch (retryError) {
          console.error('❌ WebGL 恢復失敗:', retryError);
          alert('圖表渲染失敗,請刷新頁面 (F5)');
        }
      }, 500);
    }
  }
}

/**
 * ✅ 移除此函數,改用 updatePlot 統一處理
 */
export function updateNodeColors(nodes, selectedIndex) {
  // 直接調用 updatePlot,讓它使用 Plotly.react
  const edges = window.appState?.currentEdges || [];
  if (edges.length > 0) {
    const edgeData = { x: [], y: [], z: [] };
    // 簡化處理,實際應該從 state 獲取完整資料
    updatePlot(nodes, edgeData, edges.length, edges);
  }
}

/**
 * 別名函數
 */
export function updatePlotWithHighlight(nodes, selectedIndex = null) {
  updateNodeColors(nodes, selectedIndex);
}

/**
 * ✅ 新增: 重置圖表狀態（用於 F5 刷新或重大錯誤後）
 */
export function resetPlotState() {
  isPlotInitialized = false;
  console.log('🔄 圖表狀態已重置');
}