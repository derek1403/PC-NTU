project/
├── index.html              # 簡潔的 HTML 入口
├── css/
│   └── style.css          # 所有 CSS 樣式
└── js/
    ├── main.js            # 主程式入口，協調所有模組
    ├── state.js           # 全域狀態管理（集中管理變數）
    ├── dataLoader.js      # 資料載入與解壓縮   
    ├── graphProcessor.js  # 圖資料處理與篩選邏輯
    ├── plotManager.js     # Plotly 3D 繪圖管理
    ├── filterUI.js        # 篩選介面與統計顯示
    ├── imageLoader.js     # 颱風圖片載入
    ├── eventHandlers.js   # UI 事件處理（點擊、按鈕）
    ├── uiControls.js      # 處理摺疊面板和開關邏輯
    ├── componentAnalysis.js   # 處理連通圖分析
    └── typhoonTracker.js  #  處理颱風路徑追蹤

state.js - 類似 Python 的全域變數管理
dataLoader.js - 處理 .gz 解壓縮和 JSON 載入
graphProcessor.js - 圖資料的篩選和處理
plotManager.js - Plotly 圖表的渲染
filterUI.js - 讀取篩選條件和更新統計
imageLoader.js - 從 Digital Typhoon 載入圖片
eventHandlers.js - 處理所有 UI 互動
main.js - 協調所有模組，應用程式入口