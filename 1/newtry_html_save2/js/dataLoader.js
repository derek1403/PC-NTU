/**
 * 資料載入模組
 * 負責載入與解壓縮 .gz / .json 資料
 */

/**
 * 載入資料檔案（支援 .json 和 .gz）
 * @param {string} filename - 檔案名稱
 * @returns {Promise<Object>} 解析後的 JSON 資料
 */
export async function loadData(filename) {
  try {
    const response = await fetch(filename);
    
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    
    if (filename.endsWith('.gz')) {
      // 載入並解壓縮 .gz 檔案
      const buffer = await response.arrayBuffer();
      const decompressed = pako.inflate(new Uint8Array(buffer), { to: 'string' });
      return JSON.parse(decompressed);
    } else {
      // 直接載入 .json 檔案
      return await response.json();
    }
  } catch (error) {
    console.error('載入資料失敗:', error);
    showLoadingError(filename, error);
    throw error;
  }
}

/**
 * 顯示載入錯誤訊息
 * @param {string} filename - 檔案名稱
 * @param {Error} error - 錯誤物件
 */
function showLoadingError(filename, error) {
  const loadingDiv = document.getElementById('loading');
  if (loadingDiv) {
    loadingDiv.innerHTML = `
      <div style="color: red;">❌ 載入失敗</div>
      <div style="font-size: 0.9em; margin-top: 10px;">
        檔案: ${filename}<br>
        錯誤: ${error.message}
      </div>
    `;
  }
}

/**
 * 隱藏載入畫面
 */
export function hideLoading() {
  const loadingDiv = document.getElementById('loading');
  if (loadingDiv) {
    loadingDiv.style.display = 'none';
  }
}