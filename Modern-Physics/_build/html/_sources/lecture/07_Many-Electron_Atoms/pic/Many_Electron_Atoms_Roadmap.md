# Many_Electron_Atoms_Roadmap.png

**對應章節：** 7.1 電子自旋（本章開頭）
**插入位置：** 7.1 節開頭「本章要處理的事情可以濃縮成三件」的條列之後、「薛丁格方程式解釋不了的兩件事」之前
**課本對應：** 無（自製路線圖）

> 產圖前請先貼上 `00_STYLE_GUIDE.md` 的風格區塊。

---

## 中文提示詞

```
請畫一張教學用「流程路線圖」資訊圖表，主題是「第七章多電子原子的整體骨架」。
讀者光看這張圖，就應該能說出本章每一節在做什麼、彼此怎麼接起來。

標題列文字：7.1  多電子原子路線圖 (Many-Electron Atoms — Roadmap)

導言框文字：
第六章只有一個電子、三個量子數。電子一多，需要補上第四個量子數「自旋」，
再加上「包立不相容原理」與「能量最低原理」，就能把整張週期表重建出來；
自旋與軌道的耦合則解釋了光譜的精細結構，內殼躍遷則產生 x 射線。

主體區最上方一條橫向的細長灰框｜pill 標籤：課程的順序
  五個小圓角框由左到右以箭頭相連：
  氫原子（單電子，第六章）→ 多電子原子（第七章，本圖重點，用深藍粗框標出）
  → 分子（第八章）→ 大量粒子的統計（第九章）→ 固體（第十章）

主體區左側（約 25% 寬）：起點
  淺藍圓角框「第六章的成果」：n、l、m_l 三個量子數；E_n = E₁/n²
  下方紅色圓角框「兩個解釋不了的實驗」：
    ① 精細結構：H_α 656.3 nm 其實是兩條線
    ② 異常塞曼效應：譜線分裂成 4 條、6 條，而非 3 條
  兩框之間以紅色虛線箭頭指向右邊的「7.1 自旋」。

主體區中央：節點「7.1 電子自旋」（淺紫大框，全圖的樞紐）
  內容：第四個量子數 m_s = ±1/2；S = (√3/2)ħ；μ_sz = ±μ_B
  從這個節點分出三條路線，每條路線用不同顏色的粗箭頭：

  路線 A（綠色 #2E7D32，往右上）｜pill 標籤：結構——重建週期表
    依序四個節點：
    「7.2 / 7.3 不相容原理與反對稱波函數」：ψ_A = 0 當兩電子同態
    「7.5 殼與子殼」：子殼容量 2(2l+1)，殼容量 2n²
    「7.6 屏蔽與填充順序」：4s 先於 3d；宏德規則
    「7.4 週期表」：週期長度 2, 8, 8, 18, 18, 32, 32 自動出現（終點，畫成週期表小圖示）

  路線 B（紫色 #7B1FA2，往右）｜pill 標籤：光譜——回收兩個謎題
    依序三個節點：
    「7.7 自旋—軌道耦合」：站在電子上看，原子核繞行產生 B ≈ 0.4 T
    「7.8 總角動量」：J = L + S，j = l ± 1/2；LS 耦合；項符號 n ²ˢ⁺¹L_J
    終點框（綠色勾勾）：「精細結構 ✓、異常塞曼效應 ✓（Landé g 因子）」
    從終點框畫一條紫色虛線回到左側紅色框，標「謎題解決」。

  路線 C（橘色 #EF6C00，往右下）｜pill 標籤：內殼——x 射線
    兩個節點：
    「7.9 x 射線光譜」：E(K_α) = (10.2 eV)(Z − 1)²
    「歐傑效應」：能量交給另一個電子 → 元素分析

最下方一排粉彩公式盒（四個，代表重建週期表的四個原料）：
1. 淺藍盒：n, l, m_l，說明「薛丁格方程式的三個本徵值（第六章）」
2. 淺紫盒：m_s = ±1/2，說明「自旋——第四個量子數」
3. 淺紅盒：(n, l, m_l, m_s)ᵢ ≠ (n, l, m_l, m_s)ⱼ，說明「包立不相容原理」
4. 淺綠盒：E_total → 最小，說明「能量最低原理」
```

## English Prompt

```
Draw an educational FLOWCHART/ROADMAP infographic titled "the backbone of
Chapter 7, many-electron atoms". ALL labels in TRADITIONAL CHINESE. A reader
should be able to explain what every section does and how they connect from
this figure alone.

Title bar: 7.1  多電子原子路線圖 (Many-Electron Atoms — Roadmap)

Intro box (Traditional Chinese):
第六章只有一個電子、三個量子數。電子一多，需要補上第四個量子數「自旋」，
再加上「包立不相容原理」與「能量最低原理」，就能把整張週期表重建出來；
自旋與軌道的耦合則解釋了光譜的精細結構，內殼躍遷則產生 x 射線。

Top strip of the main area (thin grey frame), pill label 課程的順序:
  five small rounded boxes joined left-to-right by arrows:
  氫原子（單電子，第六章）→ 多電子原子（第七章，highlighted with a thick dark-blue border）
  → 分子（第八章）→ 大量粒子的統計（第九章）→ 固體（第十章）

LEFT ~25% of the main area: the starting point
  light-blue rounded box "第六章的成果": n、l、m_l 三個量子數；E_n = E₁/n²
  below it a RED rounded box "兩個解釋不了的實驗":
    ① 精細結構：H_α 656.3 nm 其實是兩條線
    ② 異常塞曼效應：譜線分裂成 4 條、6 條，而非 3 條
  a red dashed arrow from these boxes to the central node "7.1 自旋".

CENTRE: node "7.1 電子自旋" (large light-purple box, the hub of the figure)
  content: 第四個量子數 m_s = ±1/2；S = (√3/2)ħ；μ_sz = ±μ_B
  Three routes leave this hub, each a thick arrow of its own colour:

  Route A (GREEN #2E7D32, upper right), pill label 結構——重建週期表
    four nodes in order:
    "7.2 / 7.3 不相容原理與反對稱波函數": ψ_A = 0 當兩電子同態
    "7.5 殼與子殼": 子殼容量 2(2l+1)，殼容量 2n²
    "7.6 屏蔽與填充順序": 4s 先於 3d；宏德規則
    "7.4 週期表": 週期長度 2, 8, 8, 18, 18, 32, 32 自動出現
      (end node, drawn as a small periodic-table icon)

  Route B (PURPLE #7B1FA2, to the right), pill label 光譜——回收兩個謎題
    three nodes in order:
    "7.7 自旋—軌道耦合": 站在電子上看，原子核繞行產生 B ≈ 0.4 T
    "7.8 總角動量": J = L + S，j = l ± 1/2；LS 耦合；項符號 n ²ˢ⁺¹L_J
    end box with a green check mark: 精細結構 ✓、異常塞曼效應 ✓（Landé g 因子）
    a purple dashed arrow from this end box back to the red box on the left,
    labelled 謎題解決.

  Route C (ORANGE #EF6C00, lower right), pill label 內殼——x 射線
    two nodes:
    "7.9 x 射線光譜": E(K_α) = (10.2 eV)(Z − 1)²
    "歐傑效應": 能量交給另一個電子 → 元素分析

Bottom pastel formula boxes (four — the four ingredients that rebuild the periodic table):
1. light blue: n, l, m_l — 薛丁格方程式的三個本徵值（第六章）
2. light purple: m_s = ±1/2 — 自旋——第四個量子數
3. light red: (n, l, m_l, m_s)ᵢ ≠ (n, l, m_l, m_s)ⱼ — 包立不相容原理
4. light green: E_total → 最小 — 能量最低原理
```
