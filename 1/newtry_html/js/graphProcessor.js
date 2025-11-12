/**
 * 圖資料處理模組
 * 負責處理、篩選圖資料
 */

/**
 * 處理圖資料格式
 * @param {Object} graphData - 原始圖資料
 * @returns {Object} { nodes, edges, metadata }
 */
export function processGraphData(graphData) {
  const nodes = graphData.nodes;
  let edges = [];
  let meta = {};

  if (Array.isArray(graphData.edges)) {
    // 邊已經是陣列格式
    edges = graphData.edges;
    meta = {
      total_nodes: nodes.length,
      total_edges: edges.length,
      sampled_edges: edges.length,
      sample_rate: 1.0
    };
  } else if (graphData.edges && graphData.edges.x) {
    // 從座標陣列重建邊列表
    edges = reconstructEdgesFromCoordinates(graphData.edges, nodes);
    meta = graphData.metadata || {
      total_nodes: nodes.length,
      total_edges: edges.length,
      sampled_edges: edges.length,
      sample_rate: 1.0
    };
  }

  return { nodes, edges, metadata: meta };
}

/**
 * 從座標陣列重建邊列表
 * @param {Object} edgeCoords - 邊的座標 {x, y, z}
 * @param {Array} nodes - 節點陣列
 * @returns {Array} 邊陣列 [[u, v], ...]
 */
function reconstructEdgesFromCoordinates(edgeCoords, nodes) {
  const edges = [];
  const { x: edgeX, y: edgeY, z: edgeZ } = edgeCoords;
  
  for (let i = 0; i < edgeX.length; i += 3) {
    if (edgeX[i] === null) continue;
    
    const x1 = edgeX[i], y1 = edgeY[i], z1 = edgeZ[i];
    const x2 = edgeX[i+1], y2 = edgeY[i+1], z2 = edgeZ[i+1];
    
    const u = nodes.findIndex(n => n.x === x1 && n.y === y1 && n.z === z1);
    const v = nodes.findIndex(n => n.x === x2 && n.y === y2 && n.z === z2);
    
    if (u !== -1 && v !== -1) {
      edges.push([u, v]);
    }
  }
  
  return edges;
}

/**
 * 篩選節點
 * @param {Array} nodes - 所有節點
 * @param {Object} filter - 篩選條件
 * @returns {Array} 篩選後的節點
 */
export function filterNodes(nodes, filter) {
  return nodes.filter(node => {
    // 颱風 ID 篩選（聯集）
    if (filter.typhoonIds && filter.typhoonIds.length > 0) {
      const nodeTyphoonIds = node.TC_ID || [];
      // 檢查節點的 TC_ID 是否包含任何一個搜尋的 ID
      const hasMatchingId = filter.typhoonIds.some(searchId => 
        nodeTyphoonIds.includes(searchId)
      );
      if (!hasMatchingId) {
        return false;
      }
    }
    
    // RMW 篩選
    if (filter.rmwMin !== null && (node.RMW === undefined || node.RMW < filter.rmwMin)) {
      return false;
    }
    if (filter.rmwMax !== null && (node.RMW === undefined || node.RMW > filter.rmwMax)) {
      return false;
    }
    
    // Vmax 篩選
    if (filter.vmaxMin !== null && (node.Vmax === undefined || node.Vmax < filter.vmaxMin)) {
      return false;
    }
    if (filter.vmaxMax !== null && (node.Vmax === undefined || node.Vmax > filter.vmaxMax)) {
      return false;
    }
    
    // IKE 篩選
    if (filter.ikeMin !== null && (node.IKE === undefined || node.IKE < filter.ikeMin)) {
      return false;
    }
    if (filter.ikeMax !== null && (node.IKE === undefined || node.IKE > filter.ikeMax)) {
      return false;
    }
    
    return true;
  });
}

/**
 * 篩選邊（保留兩端節點都有效的邊，並重新映射索引）
 * @param {Array} edges - 所有邊（使用原始節點索引）
 * @param {Array} filteredNodes - 篩選後的節點陣列
 * @param {Array} allNodes - 所有節點陣列
 * @returns {Array} 篩選後的邊（使用新索引）
 */
export function filterEdges(edges, filteredNodes, allNodes) {
  // 步驟 1: 建立「節點 ID → 新索引」的映射
  const nodeIdToNewIndex = new Map();
  filteredNodes.forEach((node, newIndex) => {
    nodeIdToNewIndex.set(node.id, newIndex);
  });
  
  // 步驟 2: 篩選並重新映射邊
  const newEdges = [];
  
  for (const [oldU, oldV] of edges) {
    // 從原始陣列取得節點 ID
    const nodeU = allNodes[oldU];
    const nodeV = allNodes[oldV];
    
    if (!nodeU || !nodeV) continue;
    
    // 檢查這兩個節點是否都在篩選後的集合中
    const newU = nodeIdToNewIndex.get(nodeU.id);
    const newV = nodeIdToNewIndex.get(nodeV.id);
    
    if (newU !== undefined && newV !== undefined) {
      newEdges.push([newU, newV]);
    }
  }
  
  return newEdges;
}

/**
 * 建立邊的座標陣列（用於 Plotly 繪圖）
 * @param {Array} edges - 邊陣列
 * @param {Array} nodes - 節點陣列
 * @returns {Object} { x, y, z } 座標陣列
 */
export function buildEdgeCoordinates(edges, nodes) {
  const edge_x = [];
  const edge_y = [];
  const edge_z = [];
  
  for (const [u, v] of edges) {
    if (u >= nodes.length || v >= nodes.length) continue;
    
    edge_x.push(nodes[u].x, nodes[v].x, null);
    edge_y.push(nodes[u].y, nodes[v].y, null);
    edge_z.push(nodes[u].z, nodes[v].z, null);
  }
  
  return { x: edge_x, y: edge_y, z: edge_z };
}