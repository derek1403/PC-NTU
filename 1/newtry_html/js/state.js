/**
 * 全域狀態管理模組
 * 類似 Python 的全域變數，集中管理應用程式狀態
 */

// 原始資料
export const state = {
  allNodes: [],
  allEdges: [],
  metadata: {},
  
  // 當前篩選條件
  currentFilter: {
    rmwMin: null,
    rmwMax: null,
    vmaxMin: null,
    vmaxMax: null,
    ikeMin: null,
    ikeMax: null
  }
};

/**
 * 設定所有節點
 */
export function setNodes(nodes) {
  state.allNodes = nodes;
}

/**
 * 設定所有邊
 */
export function setEdges(edges) {
  state.allEdges = edges;
}

/**
 * 設定元資料
 */
export function setMetadata(metadata) {
  state.metadata = metadata;
}

/**
 * 更新篩選條件
 */
export function updateFilter(filter) {
  state.currentFilter = { ...state.currentFilter, ...filter };
}

/**
 * 重置篩選條件
 */
export function resetFilter() {
  state.currentFilter = {
    rmwMin: null,
    rmwMax: null,
    vmaxMin: null,
    vmaxMax: null,
    ikeMin: null,
    ikeMax: null
  };
}

/**
 * 取得當前篩選條件
 */
export function getCurrentFilter() {
  return state.currentFilter;
}

/**
 * 取得所有節點
 */
export function getAllNodes() {
  return state.allNodes;
}

/**
 * 取得所有邊
 */
export function getAllEdges() {
  return state.allEdges;
}

/**
 * 取得元資料
 */
export function getMetadata() {
  return state.metadata;
}