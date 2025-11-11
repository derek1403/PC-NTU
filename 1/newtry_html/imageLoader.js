// imageLoader.js
export function loadTyphoonImage(node) {
  const infoDiv = document.getElementById('node-info');
  const imagePath = `images/${node.name}.png`;
  infoDiv.innerHTML = `
    <h3>${node.name}</h3>
    <p>Vmax: ${node.Vmax} kt</p>
    <img src="${imagePath}" alt="${node.name}" width="300">
  `;
}
