/**
 * 颱風路徑追蹤模組
 * 追蹤特定颱風 ID 的完整路徑
 */

/**
 * 找出颱風的完整路徑
 * @param {string} typhoonId - 颱風 ID
 * @param {Array} nodes - 所有節點
 * @returns {Array} 路徑上的節點索引陣列，按 order 排序
 */
export function findTyphoonPath(typhoonId, nodes) {
  // 找出所有包含該颱風 ID 的節點
  const candidateNodes = [];
  
  for (let i = 0; i < nodes.length; i++) {
    const node = nodes[i];
    const tcIndex = node.TC_ID ? node.TC_ID.indexOf(typhoonId) : -1;
    
    if (tcIndex !== -1) {
      candidateNodes.push({
        nodeIndex: i,
        tcIndex: tcIndex,
        order: node.order[tcIndex],
        reverseOrder: node.reverse_orders[tcIndex]
      });
    }
  }

  if (candidateNodes.length === 0) {
    return [];
  }

  // 按 order 排序
  candidateNodes.sort((a, b) => a.order - b.order);

  // 返回節點索引陣列
  return candidateNodes.map(n => n.nodeIndex);
}

/**
 * 找出路徑中的所有邊
 * @param {Array} pathNodeIndices - 路徑上的節點索引陣列
 * @param {Array} edges - 所有邊 [[u, v], ...]
 * @returns {Array} 路徑上的邊索引陣列
 */
export function findPathEdges(pathNodeIndices, edges) {
  const nodeSet = new Set(pathNodeIndices);
  const pathEdges = [];

  for (let i = 0; i < edges.length; i++) {
    const [u, v] = edges[i];
    if (nodeSet.has(u) && nodeSet.has(v)) {
      pathEdges.push(i);
    }
  }

  return pathEdges;
}

/**
 * 為多個颱風路徑分配顏色
 * @param {Array} typhoonTracks - 颱風追蹤配置 [{ id, color, path }, ...]
 * @param {Array} nodes - 所有節點
 * @returns {Map} 節點索引 -> 顏色的映射
 */
export function assignPathColors(typhoonTracks, nodes) {
  const nodeColorMap = new Map();

  // 按照用戶輸入順序（優先級從高到低）
  for (let i = typhoonTracks.length - 1; i >= 0; i--) {
    const track = typhoonTracks[i];
    const path = findTyphoonPath(track.id, nodes);

    for (const nodeIndex of path) {
      nodeColorMap.set(nodeIndex, track.color);
    }
  }

  return nodeColorMap;
}

/**
 * 為多個颱風路徑的邊分配顏色
 * @param {Array} typhoonTracks - 颱風追蹤配置
 * @param {Array} nodes - 所有節點
 * @param {Array} edges - 所有邊
 * @returns {Map} 邊索引 -> 顏色的映射
 */
export function assignPathEdgeColors(typhoonTracks, nodes, edges) {
  const edgeColorMap = new Map();

  // 按照用戶輸入順序（優先級從高到低）
  for (let i = typhoonTracks.length - 1; i >= 0; i--) {
    const track = typhoonTracks[i];
    const path = findTyphoonPath(track.id, nodes);
    const pathEdges = findPathEdges(path, edges);

    for (const edgeIndex of pathEdges) {
      edgeColorMap.set(edgeIndex, track.color);
    }
  }

  return edgeColorMap;
}

/**
 * 驗證颱風 ID 是否存在
 * @param {string} typhoonId - 颱風 ID
 * @param {Array} nodes - 所有節點
 * @returns {boolean}
 */
export function validateTyphoonId(typhoonId, nodes) {
  return nodes.some(node => 
    node.TC_ID && node.TC_ID.includes(typhoonId)
  );
}