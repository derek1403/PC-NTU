# Term_Symbol_Anatomy.png

**對應章節：** 7.8 總角動量
**插入位置：**「項符號 (Term Symbols)」小節末（單價電子原子皆為雙重態那段）之後、「例題 7.6」之前
**課本對應：** 無（自製解剖圖，整合例題 7.6、7.7）

> 產圖前請先貼上 `00_STYLE_GUIDE.md` 的風格區塊。

---

## 中文提示詞

```
請畫一張教學用資訊圖表，主題是「項符號怎麼讀：n ²ˢ⁺¹L_J 拆解」。

標題列文字：7.8  項符號解剖 (Anatomy of a Term Symbol)

導言框文字：
原子光譜早在量子力學之前就被大量量測，光譜學家留下了一套至今仍在使用的記號。
只要記得「左上 2S+1、中間 L、右下 J」，任何一個項符號都能讀出來。

主體上方中央（約 60% 寬）｜pill 標籤：拆解一個項符號
在畫面中央用很大的字排出項符號「3 ²P₃/₂」（印刷品質：3 為一般大小，
左上標 2 較小且位於 P 的左上方，右下標 3/2 較小且位於 P 的右下方）。
從四個部位各拉一條引線到四個說明框（四種顏色）：
  深藍框（指向 3）：「n = 3：價電子的主量子數」
  紅框（指向左上標 2）：「2S + 1 = 2 ⇒ S = 1/2：多重度 (multiplicity)，雙重態 doublet」
  藍框（指向 P）：「P ⇒ L = 1：總軌道量子數的字母代號」
  紫框（指向右下標 3/2）：「J = 3/2：總角動量量子數」
下方一行讀法：唸作「three doublet P three-halves」

主體上方右側（約 40% 寬）：兩張小表上下堆疊
表 1｜pill 標籤：L 的字母代號
  L：0　1　2　3　4　5
  字母：S　P　D　F　G　H
  紅色小字：這個 S 代表 L = 0，與自旋量子數 S 是兩回事（歷史撞名）
表 2｜pill 標籤：多重度的名稱
  S = 0 → 2S+1 = 1 → 單態 singlet
  S = 1/2 → 2S+1 = 2 → 雙重態 doublet
  S = 1 → 2S+1 = 3 → 三重態 triplet
  小字：L < S 時 J 只有 2L+1 個值，但仍沿用多重度的名稱（例如 ²S₁/₂ 仍叫 doublet）

主體下方左（約 55% 寬）｜pill 標籤：例題 7.6：鈉的價電子
三張並排的小卡片，每張上方是項符號（大字），下方是逐項讀出的量子數：
  卡 1「3 ²S₁/₂（基態）」：n = 3，l = 0，j = 1/2，m_j = ±1/2
  卡 2「3 ²P₁/₂」：n = 3，l = 1，j = 1/2，m_j = ±1/2
  卡 3「3 ²P₃/₂」：n = 3，l = 1，j = 3/2，m_j = ±1/2, ±3/2
  卡 2、卡 3 之間用大括號標「第一受激態 3²P 的兩個能階（自旋—軌道分裂）」。
  小字：單價電子原子的填滿核心貢獻為零 ⇒ S = 1/2、L = l、J = j，全部是雙重態

主體下方右（約 45% 寬）｜pill 標籤：例題 7.7：² P₅/₂ 為什麼不存在
  大字「2 ²P₅/₂」，上面畫一個紅色大叉 ✗。
  三行推理：
    左上標 2 ⇒ S = 1/2；P ⇒ L = 1
    J 只能從 |L − S| 到 L + S：J ∈ {1/2, 3/2}
    J 最大是 3/2，不可能是 5/2
  旁邊畫一個小的綠色勾勾 ✓ 例子「2 ²P₃/₂、2 ²P₁/₂ 才是合法的」。

右上角「圖例」方框：
  深藍 — 主量子數 n
  紅色 — 多重度 2S+1
  藍色 — 軌道字母 L
  紫色 — 總角動量 J

最下方一排粉彩公式盒（三個）：
1. 淺紅盒：2S + 1，說明「左上標：自旋的可能轉向數（多重度）」
2. 淺藍盒：L = 0, 1, 2, 3 ↔ S, P, D, F，說明「中間大寫字母」
3. 淺紫盒：|L − S| ≤ J ≤ L + S，說明「右下標必須落在這個範圍內」
```

## English Prompt

```
Draw an educational infographic titled "how to read a term symbol: dissecting
n ²ˢ⁺¹L_J". ALL labels in TRADITIONAL CHINESE.

Title bar: 7.8  項符號解剖 (Anatomy of a Term Symbol)

Intro box (Traditional Chinese):
原子光譜早在量子力學之前就被大量量測，光譜學家留下了一套至今仍在使用的記號。
只要記得「左上 2S+1、中間 L、右下 J」，任何一個項符號都能讀出來。

TOP CENTRE (~60%), pill label 拆解一個項符號:
In the middle, typeset the term symbol "3 ²P₃/₂" in very large print (print
quality: the 3 at normal size; a smaller superscript 2 placed at the UPPER LEFT
of P; a smaller subscript 3/2 placed at the LOWER RIGHT of P).
From each of the four parts draw a leader line to an explanation box (four colours):
  dark-blue box (to the 3): n = 3：價電子的主量子數
  red box (to the left superscript 2): 2S + 1 = 2 ⇒ S = 1/2：多重度 (multiplicity)，雙重態 doublet
  blue box (to the P): P ⇒ L = 1：總軌道量子數的字母代號
  purple box (to the subscript 3/2): J = 3/2：總角動量量子數
One line below: 唸作「three doublet P three-halves」

TOP RIGHT (~40%): two small stacked tables.
Table 1, pill label L 的字母代號:
  L：0　1　2　3　4　5
  字母：S　P　D　F　G　H
  small red note: 這個 S 代表 L = 0，與自旋量子數 S 是兩回事（歷史撞名）
Table 2, pill label 多重度的名稱:
  S = 0 → 2S+1 = 1 → 單態 singlet
  S = 1/2 → 2S+1 = 2 → 雙重態 doublet
  S = 1 → 2S+1 = 3 → 三重態 triplet
  small note: L < S 時 J 只有 2L+1 個值，但仍沿用多重度的名稱（例如 ²S₁/₂ 仍叫 doublet）

BOTTOM LEFT (~55%), pill label 例題 7.6：鈉的價電子:
Three small cards side by side, each with a term symbol in large type on top and
the quantum numbers read off underneath:
  card 1 "3 ²S₁/₂（基態）": n = 3，l = 0，j = 1/2，m_j = ±1/2
  card 2 "3 ²P₁/₂": n = 3，l = 1，j = 1/2，m_j = ±1/2
  card 3 "3 ²P₃/₂": n = 3，l = 1，j = 3/2，m_j = ±1/2, ±3/2
  a brace spanning cards 2 and 3 labelled 第一受激態 3²P 的兩個能階（自旋—軌道分裂）.
  small note: 單價電子原子的填滿核心貢獻為零 ⇒ S = 1/2、L = l、J = j，全部是雙重態

BOTTOM RIGHT (~45%), pill label 例題 7.7：² P₅/₂ 為什麼不存在:
  large "2 ²P₅/₂" with a big red cross ✗ over it.
  three lines of reasoning:
    左上標 2 ⇒ S = 1/2；P ⇒ L = 1
    J 只能從 |L − S| 到 L + S：J ∈ {1/2, 3/2}
    J 最大是 3/2，不可能是 5/2
  beside it a small green check mark ✓ with the example 2 ²P₃/₂、2 ²P₁/₂ 才是合法的.

Top-right legend "圖例":
  深藍 — 主量子數 n
  紅色 — 多重度 2S+1
  藍色 — 軌道字母 L
  紫色 — 總角動量 J

Bottom pastel formula boxes (three):
1. light red: 2S + 1 — 左上標：自旋的可能轉向數（多重度）
2. light blue: L = 0, 1, 2, 3 ↔ S, P, D, F — 中間大寫字母
3. light purple: |L − S| ≤ J ≤ L + S — 右下標必須落在這個範圍內
```
