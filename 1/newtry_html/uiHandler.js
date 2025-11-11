// uiHandler.js
export function initUI(onFilterChange, onReset, onNodeClick) {
  const filterButton = document.getElementById('filter-btn');
  const resetButton = document.getElementById('reset-btn');

  if (filterButton) {
    filterButton.addEventListener('click', () => {
      const vmaxMin = parseFloat(document.getElementById('vmin').value) || null;
      const vmaxMax = parseFloat(document.getElementById('vmax').value) || null;
      onFilterChange({ vmaxMin, vmaxMax });
    });
  }

  if (resetButton) {
    resetButton.addEventListener('click', () => onReset());
  }
}
