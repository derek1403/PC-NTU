/**
 * 連通圖分析模組
 * 使用 Union-Find (並查集) 找出連通分量
 */

class UnionFind {
  constructor(n) {
    this.parent = Array.from({ length: n }, (_, i) => i);
    this.rank = Array(n).fill(0);
    this.size = Array(n).fill(1);
  }

  find(x) {
    if (this.parent[x] !== x) {
      this.parent[x] = this.find(this.parent[x]); // 路徑壓縮
    }
    return this.parent[x];
  }

  union(x, y) {
    const rootX = this.find(x);
    const rootY = this.find(y);

    if (rootX === rootY) return false;

    // 按秩合併
    if (this.rank[rootX] < this.rank[rootY]) {
      this.parent[rootX] = rootY;
      this.size[rootY] += this.size[rootX];
    } else if (this.rank[rootX] > this.rank[rootY]) {
      this.parent[rootY] = rootX;
      this.size[rootX] += this.size[rootY];
    } else {
      this.parent[rootY] = rootX;
      this.size[rootX] += this.size[rootY];
      this.rank[rootX]++;
    }

    return true;
  }

  getComponentSize(x) {
    return this.size[this.find(x)];
  }
}

/**
 * 找出圖中所有的連通分量
 * @param {Array} nodes - 節點陣列
 * @param {Array} edges - 邊陣列 [[u, v], ...]
 * @returns {Object} { components, mainland, largestIsland, stats }
 */
export function findConnectedComponents(nodes, edges) {
  const n = nodes.length;
  if (n === 0) {
    return { components: [], mainland: null, largestIsland: null, stats: null };
  }

  const uf = new UnionFind(n);

  // 建立連通分量
  for (const [u, v] of edges) {
    uf.union(u, v);
  }

  // 收集每個連通分量的節點
  const componentMap = new Map();
  for (let i = 0; i < n; i++) {
    const root = uf.find(i);
    if (!componentMap.has(root)) {
      componentMap.set(root, []);
    }
    componentMap.get(root).push(i);
  }

  // 轉換為陣列並按大小排序
  const components = Array.from(componentMap.values())
    .sort((a, b) => b.length - a.length);

  // 找出陸地（最大連通分量）
  const mainland = components.length > 0 ? components[0] : null;

  // 找出最大島嶼（第二大連通分量）
  const largestIsland = components.length > 1 ? components[1] : null;

  // 計算邊的數量
  const mainlandEdges = mainland ? countEdgesInComponent(mainland, edges) : 0;
  const islandEdges = largestIsland ? countEdgesInComponent(largestIsland, edges) : 0;

  const stats = {
    mainlandNodes: mainland ? mainland.length : 0,
    mainlandEdges: mainlandEdges,
    islandNodes: largestIsland ? largestIsland.length : 0,
    islandEdges: islandEdges,
    totalComponents: components.length
  };

  return { components, mainland, largestIsland, stats };
}

/**
 * 計算連通分量中的邊數量
 * @param {Array} componentNodes - 連通分量的節點索引
 * @param {Array} edges - 所有邊
 * @returns {number} 邊數量
 */
function countEdgesInComponent(componentNodes, edges) {
  const nodeSet = new Set(componentNodes);
  let count = 0;

  for (const [u, v] of edges) {
    if (nodeSet.has(u) && nodeSet.has(v)) {
      count++;
    }
  }

  return count;
}

/**
 * 檢查節點是否在指定的連通分量中
 * @param {number} nodeIndex - 節點索引
 * @param {Array} component - 連通分量的節點索引陣列
 * @returns {boolean}
 */
export function isNodeInComponent(nodeIndex, component) {
  return component ? component.includes(nodeIndex) : false;
}