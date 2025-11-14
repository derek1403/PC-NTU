/**
 * 颱風路徑追蹤模組（完整修正版）
 * 追蹤特定颱風 ID 的完整路徑，只標記連續 order 的邊
 * ✅ 修正：處理颱風回到相同 state 的情況（同一節點被經過多次）
 */

/**
 * ✅ 完整修正版：找出颱風的完整路徑
 * 關鍵修正：同一個節點可能被同一個颱風經過多次，要分別記錄每次訪問
 * 
 * @param {string} typhoonId - 颱風 ID
 * @param {Array} nodes - 節點陣列（當前顯示的）
 * @returns {Array} 路徑上的節點索引陣列（指向 nodes），按 order 排序
 */
export function findTyphoonPath(typhoonId, nodes) {
  // ✅ 修正：收集所有訪問記錄（包括多次訪問同一節點）
  const candidateNodes = [];
  
  for (let i = 0; i < nodes.length; i++) {
    const node = nodes[i];
    
    if (!node.TC_ID || !Array.isArray(node.TC_ID)) {
      continue;
    }
    
    // ✅ 關鍵修正：遍歷所有 TC_ID，找出所有匹配的位置
    node.TC_ID.forEach((id, tcIndex) => {
      if (id === typhoonId) {
        candidateNodes.push({
          nodeIndex: i,
          tcIndex: tcIndex,
          order: node.order[tcIndex],
          reverseOrder: node.reverse_orders ? node.reverse_orders[tcIndex] : undefined
        });
      }
    });
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
 * ✅ 完整修正版：找出路徑中**連續 order** 的所有邊
 * 關鍵修正：同一個節點可能被颱風經過多次，每次有不同的 order
 * 
 * 核心邏輯：
 * 1. 收集所有「(節點索引, order)」配對（一個節點可能有多個 order）
 * 2. 按 order 排序
 * 3. 檢查每條邊是否連接 order 連續的節點
 * 
 * @param {string} typhoonId - 颱風 ID
 * @param {Array} nodes - 節點陣列（當前顯示的）
 * @param {Array} edges - 邊陣列（索引對應到 nodes）[[u, v], ...]
 * @returns {Set} 路徑上的邊集合（用 "u-v" 字串表示）
 */
export function findPathEdges(typhoonId, nodes, edges) {
  console.log(`🔍 尋找颱風 ${typhoonId} 的路徑邊...`);
  
  // ✅ 步驟 1：收集所有「(節點索引, order)」配對
  const pathVisits = []; // [{ nodeIndex, order, tcIndex }, ...]
  
  for (let i = 0; i < nodes.length; i++) {
    const node = nodes[i];
    
    if (!node.TC_ID || !Array.isArray(node.TC_ID)) {
      continue;
    }
    
    // ✅ 關鍵修正：遍歷所有 TC_ID，找出所有匹配的位置
    node.TC_ID.forEach((id, tcIndex) => {
      if (id === typhoonId) {
        const order = node.order[tcIndex];
        
        if (order !== undefined && order !== null) {
          pathVisits.push({
            nodeIndex: i,
            order: order,
            tcIndex: tcIndex
          });
        }
      }
    });
  }

  if (pathVisits.length === 0) {
    console.warn(`⚠️ 颱風 ${typhoonId} 沒有找到任何節點`);
    return new Set();
  }

  console.log(`📍 颱風 ${typhoonId} 有 ${pathVisits.length} 次節點訪問`);

  // ✅ 步驟 2：按 order 排序
  pathVisits.sort((a, b) => a.order - b.order);

  // 除錯資訊：顯示路徑訪問順序
  if (pathVisits.length <= 20) {
    console.log('📊 路徑訪問順序:', pathVisits.map(v => 
      `節點${v.nodeIndex}(order=${v.order})`
    ).join(' → '));
  } else {
    console.log(`📊 路徑訪問順序: ${pathVisits.length} 個節點 (過多，省略顯示)`);
  }

  // ✅ 步驟 3：建立「節點索引 → 所有 order」的映射
  const nodeIndexToOrders = new Map();
  
  pathVisits.forEach(visit => {
    if (!nodeIndexToOrders.has(visit.nodeIndex)) {
      nodeIndexToOrders.set(visit.nodeIndex, []);
    }
    nodeIndexToOrders.get(visit.nodeIndex).push(visit.order);
  });

  // ✅ 步驟 4：檢查每條邊，判斷是否連接 order 連續的節點
  const validEdges = new Set();
  let foundEdges = 0;

  for (const [u, v] of edges) {
    const ordersU = nodeIndexToOrders.get(u);
    const ordersV = nodeIndexToOrders.get(v);

    // 至少有一個節點不在路徑中
    if (!ordersU || !ordersV) {
      continue;
    }

    // ✅ 關鍵修正：檢查是否存在「order 相差 1」的配對
    let isConnected = false;
    
    for (const orderU of ordersU) {
      for (const orderV of ordersV) {
        if (Math.abs(orderU - orderV) === 1) {
          isConnected = true;
          break;
        }
      }
      if (isConnected) break;
    }

    if (isConnected) {
      validEdges.add(`${u}-${v}`);
      validEdges.add(`${v}-${u}`);
      foundEdges++;
    }
  }

  console.log(`✅ 颱風 ${typhoonId} 找到 ${foundEdges} 條連續路徑的邊`);

  return validEdges;
}

/**
 * 為多個颱風路徑分配顏色（節點）
 * @param {Array} typhoonTracks - 颱風追蹤配置 [{ id, color }, ...]
 * @param {Array} nodes - 節點陣列（當前顯示的）
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
 * @param {Array} nodes - 節點陣列（當前顯示的）
 * @param {Array} edges - 邊陣列（索引對應到 nodes）
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
 * @param {Array} nodes - 節點陣列（當前顯示的）
 * @returns {boolean}
 */
export function validateTyphoonId(typhoonId, nodes) {
  const exists = nodes.some(node => 
    node.TC_ID && node.TC_ID.includes(typhoonId)
  );
  
  if (!exists) {
    console.warn(`⚠️ 颱風 ID ${typhoonId} 在當前顯示的節點中不存在`);
  }
  
  return exists;
}

/**
 * ✅ 新增：取得颱風的詳細統計資訊（包含多次訪問的處理）
 * @param {string} typhoonId - 颱風 ID
 * @param {Array} nodes - 節點陣列
 * @returns {Object|null} 統計資訊
 */
export function getTyphoonStats(typhoonId, nodes) {
  const pathVisits = [];
  
  // 收集所有訪問記錄
  for (let i = 0; i < nodes.length; i++) {
    const node = nodes[i];
    
    if (!node.TC_ID || !Array.isArray(node.TC_ID)) {
      continue;
    }
    
    node.TC_ID.forEach((id, tcIndex) => {
      if (id === typhoonId) {
        pathVisits.push({
          nodeIndex: i,
          node: node,
          order: node.order[tcIndex]
        });
      }
    });
  }
  
  if (pathVisits.length === 0) {
    return null;
  }

  // 按 order 排序
  pathVisits.sort((a, b) => a.order - b.order);

  // 計算統計資訊
  const rmwValues = pathVisits.map(v => v.node.RMW).filter(v => v !== undefined);
  const vmaxValues = pathVisits.map(v => v.node.Vmax).filter(v => v !== undefined);
  const ikeValues = pathVisits.map(v => v.node.IKE).filter(v => v !== undefined);

  return {
    visitCount: pathVisits.length, // 訪問次數（可能大於節點數）
    uniqueNodeCount: new Set(pathVisits.map(v => v.nodeIndex)).size, // 唯一節點數
    avgRMW: rmwValues.length > 0 
      ? rmwValues.reduce((a, b) => a + b, 0) / rmwValues.length 
      : null,
    avgVmax: vmaxValues.length > 0 
      ? vmaxValues.reduce((a, b) => a + b, 0) / vmaxValues.length 
      : null,
    avgIKE: ikeValues.length > 0 
      ? ikeValues.reduce((a, b) => a + b, 0) / ikeValues.length 
      : null,
    maxVmax: vmaxValues.length > 0 ? Math.max(...vmaxValues) : null,
    minVmax: vmaxValues.length > 0 ? Math.min(...vmaxValues) : null,
    orders: pathVisits.map(v => v.order) // 完整的 order 序列
  };
}