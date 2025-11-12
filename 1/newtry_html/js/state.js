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
    ikeMax: null,
    typhoonIds: [] // 颱風 ID 陣列
  },
  
  // 高亮模式（顯示起始點和最終點）
  highlightMode: false,
  
  // 當前選中的節點索引
  selectedNodeIndex: null,
  
  // 颱風路徑追蹤
  typhoonTracks: [], // [{ id, color }, ...]
  
  // 陸地與島嶼顯示
  showLandmass: false,
  landmassData: null, // { mainland, largestIsland, stats }
  
  // 當前顯示的邊（供陸地與島嶼分析使用）
  currentEdges: []
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
    ikeMax: null,
    typhoonIds: []
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

/**
 * 設定高亮模式
 */
export function setHighlightMode(enabled) {
  state.highlightMode = enabled;
}

/**
 * 取得高亮模式狀態
 */
export function getHighlightMode() {
  return state.highlightMode;
}

/**
 * 設定選中的節點索引
 */
export function setSelectedNodeIndex(index) {
  state.selectedNodeIndex = index;
}

/**
 * 取得選中的節點索引
 */
export function getSelectedNodeIndex() {
  return state.selectedNodeIndex;
}

/**
 * 設定颱風追蹤列表
 */
export function setTyphoonTracks(tracks) {
  state.typhoonTracks = tracks;
}

/**
 * 取得颱風追蹤列表
 */
export function getTyphoonTracks() {
  return state.typhoonTracks;
}

/**
 * 新增颱風追蹤
 */
export function addTyphoonTrack(id, color) {
  state.typhoonTracks.push({ id, color });
}

/**
 * 移除颱風追蹤
 */
export function removeTyphoonTrack(index) {
  state.typhoonTracks.splice(index, 1);
}

/**
 * 設定陸地與島嶼顯示模式
 */
export function setShowLandmass(enabled) {
  state.showLandmass = enabled;
}

/**
 * 取得陸地與島嶼顯示模式
 */
export function getShowLandmass() {
  return state.showLandmass;
}

/**
 * 設定陸地與島嶼資料
 */
export function setLandmassData(data) {
  state.landmassData = data;
}

/**
 * 取得陸地與島嶼資料
 */
export function getLandmassData() {
  return state.landmassData;
}