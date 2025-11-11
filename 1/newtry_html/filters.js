// filters.js
export function applyFilter(nodes, filter) {
  return nodes.filter(node => {
    if (filter.vmaxMin && node.Vmax < filter.vmaxMin) return false;
    if (filter.vmaxMax && node.Vmax > filter.vmaxMax) return false;
    return true;
  });
}

export function resetFilter() {
  return {};
}
