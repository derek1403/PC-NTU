// script.js
import { loadData, processGraphData } from './dataLoader.js';
import { buildEdgeCoordinates, updatePlot, onNodeClick } from './plot3D.js';
import { applyFilter, resetFilter } from './filters.js';
import { loadTyphoonImage } from './imageLoader.js';
import { initUI } from './uiHandler.js';

let allNodes = [], allEdges = [], metadata = {};

document.addEventListener('DOMContentLoaded', async () => {
  initUI(onFilterChange, onReset, onNodeClickHandler);
  await initializeGraph();
});

async function initializeGraph() {
  const graphData = await loadData('https://github.com/derek1403/PC-NTU/tree/main/1/graph_data_full.json.gz');
  const { nodes, edges, metadata: meta } = processGraphData(graphData);
  allNodes = nodes;
  allEdges = edges;
  metadata = meta;

  const edgeData = buildEdgeCoordinates(edges, nodes);
  updatePlot(nodes, edgeData, edges.length, metadata, onNodeClickHandler);
}

function onFilterChange(filter) {
  const filteredNodes = applyFilter(allNodes, filter);
  const filteredEdges = allEdges.filter(([u, v]) =>
    filteredNodes.some(n => n.id === u) && filteredNodes.some(n => n.id === v)
  );
  const edgeData = buildEdgeCoordinates(filteredEdges, filteredNodes);
  updatePlot(filteredNodes, edgeData, filteredEdges.length, metadata, onNodeClickHandler);
}

function onReset() {
  const edgeData = buildEdgeCoordinates(allEdges, allNodes);
  updatePlot(allNodes, edgeData, allEdges.length, metadata, onNodeClickHandler);
}

function onNodeClickHandler(node) {
  loadTyphoonImage(node);
}
