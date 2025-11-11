// dataLoader.js
export async function loadData(filename) {
  const response = await fetch(filename);
  if (filename.endsWith('.gz')) {
    const buffer = await response.arrayBuffer();
    const decompressed = pako.inflate(new Uint8Array(buffer), { to: 'string' });
    return JSON.parse(decompressed);
  } else {
    return await response.json();
  }
}

export function processGraphData(graphData) {
  const nodes = graphData.nodes;
  let edges = [];
  let meta = {};
  if (Array.isArray(graphData.edges)) {
    edges = graphData.edges;
    meta = { total_nodes: nodes.length, total_edges: edges.length };
  }
  return { nodes, edges, metadata: meta };
}
