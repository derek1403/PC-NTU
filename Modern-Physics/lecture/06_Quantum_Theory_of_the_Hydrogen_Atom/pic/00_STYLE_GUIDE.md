# 00 共用視覺規範 (Shared Visual Style Guide)

本目錄下每一份 `*.md` 都是給 GPT / Gemini 產圖用的提示詞。**每次產圖時，請把本檔的「風格區塊」連同該張圖自己的提示詞一起貼給模型。**

風格範本取自本課程既有的最佳範例：
`PC-NTU/Modern-Physics/lecture/05_Quantum_Mechanics/pic/Finite_Potential_Wall.png`

---

## 中文風格區塊（貼給模型時複製這一段）

```
【全域風格規範 — 請嚴格遵守】

輸出形式：一張橫幅資訊圖表（教學用），純白背景，寬高比約 4:3 到 5:4，
建議輸出 1600×1200 像素以上，線條與文字必須銳利可讀。

版面骨架（由上到下）：
1. 左上角：深藍色（#1F3864）圓角矩形標題列，白色粗體字，格式為
   「6.x  中文標題 (English Title)」，中英文之間空兩格。
2. 標題列下方：淺藍色（#EAF1FB）圓角矩形導言框，深藍細框線，
   內含 2–4 行中文導言，說明這張圖要回答什麼問題。
3. 右上角（若該圖有多種顏色編碼）：白底細框「圖例」方框，
   逐條列出色塊／線型對應的意義。
4. 主體區：物理示意圖或座標圖，佔畫面最大面積。
5. 各個小節上方：深藍色圓角 pill 標籤（白色字，例如「參數定義與物理意義」
   「波函數形狀示意」），用來切分主體區的不同段落。
6. 最下方：一排粉彩色圓角方框（淺綠 #E8F5E9、淺紫 #F3E5F5、淺藍 #E3F2FD、
   淺紅 #FFEBEE、淺黃 #FFF8E1），每個框內放一條公式與一句中文說明。

配色規則：
- 主色：深藍 #1F3864（標題列、pill 標籤、座標軸標記）
- 分區／分類色：綠 #2E7D32、橘 #EF6C00、紫 #7B1FA2、紅 #C62828、藍 #1565C0
- 同一個物理量在整張圖中必須用同一個顏色，不可換色。
- 背景一律純白，不要漸層、不要陰影、不要 3D 效果。

字體與文字：
- 所有標示文字一律使用「繁體中文」，不可出現簡體字。
- 中文用黑體（思源黑體 / Noto Sans TC 一類），英文與數學符號用
  襯線體並呈 LaTeX 排版風格（斜體變數、正體函數名、正確的上下標與分數）。
- 數學式必須排版正確：分數要有橫線，根號要罩住整個被開方式，
  上下標位置正確，希臘字母正確（θ 天頂角、φ 方位角、ψ 波函數、
  ħ 約化普朗克常數、ε₀ 真空電容率）。
- 文字大小分三級：標題列最大、pill 標籤與軸標籤次之、說明文字最小，
  但最小的字也必須清楚可讀。

嚴禁事項：
- 不要出現任何浮水印、簽名、Logo、頁碼。
- 不要出現拼錯或亂碼的中文字；寧可少寫字，也不要寫錯字。
- 不要把公式畫成圖片式的手寫體，必須是印刷排版品質。
- 不要用深色背景。
```

## English Style Block (paste this when prompting in English)

```
[GLOBAL STYLE SPEC — follow strictly]

Output: a single landscape educational infographic on a pure white background,
aspect ratio roughly 4:3 to 5:4, rendered at 1600×1200 px or larger,
with crisp, fully legible lines and text.

Layout skeleton (top to bottom):
1. Top-left: a dark-blue (#1F3864) rounded-rectangle title bar with bold white
   text, formatted as "6.x  <Chinese title> (<English Title>)", two spaces
   between the Chinese and English parts.
2. Below the title bar: a light-blue (#EAF1FB) rounded-rectangle intro box with
   a thin dark-blue border, holding 2-4 lines of Traditional Chinese text that
   state the question this figure answers.
3. Top-right (only if the figure uses colour coding): a white "圖例" (legend)
   box with a thin border, listing each colour swatch / line style and meaning.
4. Main area: the physics diagram or plot, occupying the largest share of the canvas.
5. Above each sub-section: a dark-blue rounded "pill" label with white text
   (e.g. "參數定義與物理意義"), used to segment the main area.
6. Bottom row: a strip of pastel rounded boxes (light green #E8F5E9,
   light purple #F3E5F5, light blue #E3F2FD, light red #FFEBEE,
   light yellow #FFF8E1), each containing one formula plus a one-line
   Traditional Chinese caption.

Colour rules:
- Primary: dark blue #1F3864 (title bar, pill labels, axis annotations)
- Category colours: green #2E7D32, orange #EF6C00, purple #7B1FA2,
  red #C62828, blue #1565C0
- One physical quantity keeps ONE colour throughout the whole figure.
- Pure white background. No gradients, no drop shadows, no 3D effects.

Typography:
- ALL labels must be in TRADITIONAL Chinese characters. No Simplified Chinese.
- Chinese in a sans-serif face (Noto Sans TC style); English and mathematics in
  a serif face typeset in LaTeX style (italic variables, upright function names,
  correct sub/superscripts and fractions).
- Mathematics must be typeset correctly: real fraction bars, radicals covering
  the whole radicand, correct sub/superscript placement, correct Greek letters
  (θ polar angle, φ azimuthal angle, ψ wave function, ħ reduced Planck constant,
  ε₀ vacuum permittivity).
- Three text sizes: title bar largest, pill labels and axis labels next,
  captions smallest — but even the smallest must be clearly legible.

Do NOT:
- add any watermark, signature, logo, or page number;
- render garbled or misspelled Chinese characters (write less rather than wrong);
- render formulas in a handwritten style — they must look typeset;
- use a dark background.
```

---

## 使用流程

1. 打開想產的那一張圖的 `.md`。
2. 把本檔的風格區塊（中文版或英文版擇一）貼給模型。
3. 接著貼該張圖 `.md` 裡對應語言的提示詞區塊。
4. 產出後存成 `.md` 檔名同名的 `.png`，直接放在本目錄下，notebook 就會自動吃到。
5. 回到 `README.md` 把該列的狀態改成「已完成」。

## 檔名規則

`<圖片檔名>.md` 對應 `<圖片檔名>.png`，notebook 內以 `![](./pic/<圖片檔名>.png)` 引用。
**產出的 PNG 檔名必須與 `.md` 完全一致**，否則 notebook 會顯示破圖。
