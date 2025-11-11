/**
 * 主程式入口
 * 協調各模組，初始化應用程式
 */

import { loadData, hideLoading } from './dataLoader.js';
import { processGraphData, filterNodes, filterEdges, buildEdgeCoordinates } from './graphProcessor.js';
import { updatePlot } from './plotManager.js';
import { readFilterFromUI, resetFilterUI, updateStats } from './filterUI.js';
import { setupNodeClickHandler, setupFilterButtons } from './eventHandlers.js';
import { 
  setNodes, 
  setEdges, 
  setMetadata, 
  updateFilter,
  getAllNodes, 
  getAllEdges, 
  getMetadata,
  getCurrentFilter 
} from './state.js';

/**
 * 套用篩選
 */
function applyFilter() {
  // 從 UI 讀取篩選條件
  const filter = readFilterFromUI();
  updateFilter(filter);

  console.log('套用篩選:', filter);

  // 取得原始資料
  const allNodes = getAllNodes();
  const allEdges = getAllEdges();
  const metadata = getMetadata();

  // 篩選節點
  const filteredNodes = filterNodes(allNodes, filter);
  const filteredNodeIds = filteredNodes.map(n => n.id);

  // 篩選邊
  const filteredEdges = filterEdges(allEdges, filteredNodeIds);

  // 建立邊的座標
  const edgeData = buildEdgeCoordinates(filteredEdges, allNodes);

  // 更新圖表
  updatePlot(filteredNodes, edgeData, filteredEdges.length);

  // 更新統計資訊
  updateStats(
    filteredNodes.length, 
    filteredEdges.length, 
    metadata.total_nodes, 
    metadata.total_edges
  );

  // 重新綁定點擊事件（因為節點可能改變）
  setupNodeClickHandler(filteredNodes);

  console.log(`✅ 篩選完成: ${filteredNodes.length} 節點, ${filteredEdges.length} 邊`);
}

/**
 * 重置篩選
 */
function resetFilter() {
  // 重置 UI 和狀態
  resetFilterUI();

  console.log('重置篩選');

  // 取得原始資料
  const allNodes = getAllNodes();
  const allEdges = getAllEdges();
  const metadata = getMetadata();

  // 顯示所有資料
  const edgeData = buildEdgeCoordinates(allEdges, allNodes);
  updatePlot(allNodes, edgeData, allEdges.length);

  // 更新統計資訊
  updateStats(
    allNodes.length, 
    allEdges.length, 
    metadata.total_nodes, 
    metadata.total_edges
  );

  // 重新綁定點擊事件
  setupNodeClickHandler(allNodes);

  console.log('✅ 已重置篩選');
}

/**
 * 初始化應用程式
 */
async function initialize() {
  try {
    // 載入資料
    console.log('📥 開始載入資料...');
    const graphData = await loadData('https://raw.githubusercontent.com/derek1403/PC-NTU/main/1/graph_data_full.json.gz'); //../graph_data_full.json.gz 會有error 這只是目錄查詢系統
    
    console.log('📊 原始資料:', graphData);
    
    // 處理資料
    const { nodes, edges, metadata } = processGraphData(graphData);
    
    // 儲存到全域狀態
    setNodes(nodes);
    setEdges(edges);
    setMetadata(metadata);
    
    console.log('📊 處理後:', { nodes: nodes.length, edges: edges.length });
    
    // 隱藏載入畫面
    hideLoading();

    // 初始渲染
    const edgeData = buildEdgeCoordinates(edges, nodes);
    updatePlot(nodes, edgeData, edges.length);

    // 更新統計資訊
    updateStats(nodes.length, edges.length, metadata.total_nodes, metadata.total_edges);

    // 設定事件處理
    setupNodeClickHandler(nodes);
    setupFilterButtons(applyFilter, resetFilter);

    console.log('✅ 應用程式初始化完成！');

  } catch (error) {
    console.error('❌ 初始化失敗:', error);
  }
}

// 啟動應用程式
initialize();