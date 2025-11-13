/**
 * 颱風路徑追蹤模組（修正版）
 * 追蹤特定颱風 ID 的完整路徑，只標記連續 order 的邊
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
 * ✅ 修正版：找出路徑中**連續 order** 的所有邊
 * 只有當兩個節點在颱風路徑中相鄰（order 連續）時，才算是路徑上的邊
 * 
 * @param {string} typhoonId - 颱風 ID
 * @param {Array} nodes - 所有節點
 * @param {Array} edges - 所有邊 [[u, v], ...]
 * @returns {Set} 路徑上的邊集合（用 "u-v" 字串表示）
 */
export function findPathEdges(typhoonId, nodes, edges) {
  // 步驟 1: 找出颱風的所有節點（帶 order 資訊）
  const pathNodes = [];
  
  for (let i = 0; i < nodes.length; i++) {
    const node = nodes[i];
    const tcIndex = node.TC_ID ? node.TC_ID.indexOf(typhoonId) : -1;
    
    if (tcIndex !== -1) {
      pathNodes.push({
        nodeIndex: i,
        order: node.order[tcIndex]
      });
    }
  }

  if (pathNodes.length === 0) {
    return new Set();
  }

  // 步驟 2: 按 order 排序
  pathNodes.sort((a, b) => a.order - b.order);

  // 步驟 3: 建立「節點索引 → 在路徑中的位置」的映射
  const nodeIndexToPathPosition = new Map();
  pathNodes.forEach((node, pathPos) => {
    nodeIndexToPathPosition.set(node.nodeIndex, pathPos);
  });

  // 步驟 4: 檢查每條邊，只保留「路徑中相鄰節點」的邊
  const validEdges = new Set();

  for (const [u, v] of edges) {
    const posU = nodeIndexToPathPosition.get(u);
    const posV = nodeIndexToPathPosition.get(v);

    // 兩個節點都在路徑中
    if (posU !== undefined && posV !== undefined) {
      // 檢查它們在路徑中是否相鄰（位置差為 1）
      if (Math.abs(posU - posV) === 1) {
        // 用字串表示邊（雙向）
        validEdges.add(`${u}-${v}`);
        validEdges.add(`${v}-${u}`);
      }
    }
  }

  return validEdges;
}

/**
 * 為多個颱風路徑分配顏色（節點）
 * @param {Array} typhoonTracks - 颱風追蹤配置 [{ id, color }, ...]
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
 * ✅ 修正版：為多個颱風路徑的邊分配顏色
 * 只有連續 order 的邊會被上色
 * 
 * @param {Array} typhoonTracks - 颱風追蹤配置 [{ id, color }, ...]
 * @param {Array} nodes - 所有節點
 * @param {Array} edges - 所有邊
 * @returns {Array} 每條邊對應的顏色（與 edges 陣列順序一致），null 表示預設顏色
 */
export function assignPathEdgeColors(typhoonTracks, nodes, edges) {
  // 為每條邊初始化顏色為 null（預設）
  const edgeColors = new Array(edges.length).fill(null);

  // 按照用戶輸入順序（優先級從低到高，後面的會覆蓋前面的）
  for (const track of typhoonTracks) {
    const validEdges = findPathEdges(track.id, nodes, edges);

    // 為每條邊檢查是否在路徑中
    edges.forEach(([u, v], edgeIndex) => {
      if (validEdges.has(`${u}-${v}`) || validEdges.has(`${v}-${u}`)) {
        edgeColors[edgeIndex] = track.color;
      }
    });
  }

  return edgeColors;
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