# Drift_Velocity_and_Resistivity.png

**對應章節：** 10.5 金屬鍵
**插入位置：**「假設與已知」（【推導 1】$I = nAev_d$）之後、「推導：漂移速度」之前
**課本對應：** 圖 10.16、圖 10.17、圖 10.18

> 產圖前請先貼上 `00_STYLE_GUIDE.md` 的風格區塊。

---

## 中文提示詞

```
【模型與符號】弱電場、均勻材料與定常 Drude 弛豫近似：m d⟨v⟩/dt=−eE−m⟨v⟩/τ；定常漂移速度 ⟨v⟩=−eτE/m。aτ 指定常平均值，不是每次碰撞前末速；電流方向與電子漂移相反。

請畫一張教學用資訊圖表，主題是「從電子碰撞推導歐姆定律：漂移速度與電阻係數」。

標題列文字：10.5  漂移速度與電阻係數 (Drift Velocity and Resistivity)

導言框文字：
歐姆定律是巨觀的實驗定律；微觀上，電阻來自電子與晶格的碰撞。
電子以 10⁶ m/s 的費米速率亂跑，電場只讓它們整體緩緩漂移——
漂移速度小到每秒不到 0.1 mm。

主體左上｜pill 標籤：隨機運動 ＋ 漂移
畫一條灰色的曲折折線（電子軌跡），由十幾段長短不一、方向隨機的線段組成，
每段之間的轉折點畫一個小黑點代表碰撞；
整條軌跡從左邊起點到右邊終點有明顯的淨位移（向右），
在圖上方畫一支向左的黑色箭頭標「電場 E」，說明電子帶負電、逆著電場漂移。
用藍色（#1565C0）粗箭頭標出淨位移，標「v_d ≈ 7.4 × 10⁻⁵ m/s（集體、同方向）」；
用灰色小箭頭標出任一段，標「v_F ≈ 1.57 × 10⁶ m/s（隨機方向，平均為零）」。
標出相鄰兩次碰撞間的一段長度為「平均自由徑 λ ≈ 38 nm ≈ 150 個離子間距」。

主體右上｜pill 標籤：數一數穿過截面的電子
畫一段水平的圓柱形導線（簡潔線稿），左邊一個灰色實心的截面標「面積 A」，
右邊一個虛線截面，兩者距離用雙箭頭標「v_d t」，圓柱體標「體積 A v_d t」。
導線內散布小黑點電子，每顆附一支向右的小箭頭。
下方算式：N = n A v_d t → Q = n A e v_d t → I = Q/t = n A e v_d　(10.13)

主體中排（橫跨全寬）｜pill 標籤：推導鏈
畫一條由左到右的流程鏈，六個圓角框，框之間用深藍箭頭連接：
  [τ = λ / v_F　(10.10)] → [a = eE / m　(10.11)] → [v_d = aτ = eEλ/(m v_F)　(10.12)]
  → [I = n A e v_d　(10.13)] → [I = (ne²λ/(m v_F))(A/L) V　(10.14)]
  → [ρ = m v_F/(n e² λ)　(10.16)]
最後一框用淺綠色強調。箭頭上方用橘色小字標動作：「碰撞間加速」「代入 E = V/L」
「與 I = V/R 比較」。

主體左下｜pill 標籤：電阻係數與溫度
畫一張座標圖，橫軸溫度 T（0 到 300 K），縱軸 ρ：
  兩條曲線：高溫區都近似直線上升（標「晶格熱振動散射 ∝ T」），
  低溫區各自停在一個水平的殘餘值（標「殘餘電阻：雜質散射，與 T 無關」），
  上方曲線（紅色 #C62828）標「雜質較多」，下方曲線（綠色 #2E7D32）標「雜質較少」。
  圖下小字：「ρ ≈ ρ_thermal(T) + ρ_impurity（Matthiessen 規則）」。

主體右下｜pill 標籤：當導線比 λ 還細
畫兩段導線的剖面比較：
  左：粗導線（寬 ≫ 38 nm），電子軌跡在內部被晶格散射，很少碰到牆。
  右：奈米導線（寬約 10–20 nm），電子軌跡頻繁撞到側壁（撞擊點用紅色標出），
      標「有效 λ 受限於線寬 → 電阻係數上升」。
  小字：「先進製程（7 nm、5 nm）的銅互連線正面臨這個問題」。

右上角「圖例」方框：
  灰色折線 — 單一電子的實際軌跡
  小黑點 — 碰撞
  藍色粗箭頭 — 漂移速度 v_d
  紅／綠曲線 — 雜質較多／較少的樣本

最下方一排粉彩公式盒（四個）：
1. 淺藍盒：v_d = I/(nAe) ≈ 7.4 × 10⁻⁵ m/s，說明「例題 10.2：1 A、1 mm² 銅線」
2. 淺綠盒：λ = m v_F/(n e² ρ) ≈ 38.3 nm，說明「例題 10.3：約通過 150 個離子才碰撞一次」
3. 淺紫盒：R = ρ L / A　(10.15)，說明「ρ 是材料性質，L/A 是幾何形狀」
4. 淺黃盒：開關一按燈就亮，說明「電場以接近光速建立，不必等電子跑完全程」
```

## English Prompt

```
MODEL AND NOTATION: Weak uniform field, homogeneous material, steady Drude relaxation: m d⟨v⟩/dt=−eE−m⟨v⟩/τ, hence ⟨v⟩=−eτE/m. aτ is a steady mean drift, not a pre-collision terminal speed. Conventional current opposes electron drift.

Draw an educational infographic titled "Deriving Ohm's law from electron
collisions: drift velocity and resistivity". ALL labels in TRADITIONAL CHINESE.

Title bar: 10.5  漂移速度與電阻係數 (Drift Velocity and Resistivity)

Intro box (Traditional Chinese):
歐姆定律是巨觀的實驗定律；微觀上，電阻來自電子與晶格的碰撞。
電子以 10⁶ m/s 的費米速率亂跑，電場只讓它們整體緩緩漂移——
漂移速度小到每秒不到 0.1 mm。

TOP-LEFT, pill label 隨機運動 ＋ 漂移:
A grey zig-zag polyline (one electron's path) made of a dozen randomly oriented
segments of varying length, with a small black dot at each kink (a collision).
The path has a clear net displacement to the right. Above it, a black arrow
pointing LEFT labelled 電場 E (electrons are negative and drift against the field).
A thick blue (#1565C0) arrow shows the net displacement, labelled
v_d ≈ 7.4 × 10⁻⁵ m/s（集體、同方向）; a small grey arrow on one segment labelled
v_F ≈ 1.57 × 10⁶ m/s（隨機方向，平均為零）. Mark one segment between two
collisions as 平均自由徑 λ ≈ 38 nm ≈ 150 個離子間距.

TOP-RIGHT, pill label 數一數穿過截面的電子:
A horizontal cylindrical wire (clean line art): a grey solid cross-section on the
left labelled 面積 A, a dashed cross-section on the right, separated by a double
arrow v_d t; the cylinder labelled 體積 A v_d t. Small black electron dots inside,
each with a small rightward arrow.
Below: N = n A v_d t → Q = n A e v_d t → I = Q/t = n A e v_d  (10.13)

MIDDLE (full width), pill label 推導鏈:
A left-to-right chain of six rounded boxes joined by dark-blue arrows:
  [τ = λ / v_F  (10.10)] → [a = eE / m  (10.11)] → [v_d = aτ = eEλ/(m v_F)  (10.12)]
  → [I = n A e v_d  (10.13)] → [I = (ne²λ/(m v_F))(A/L) V  (10.14)]
  → [ρ = m v_F/(n e² λ)  (10.16)]
Highlight the last box in light green. Small orange action labels above the arrows:
碰撞間加速, 代入 E = V/L, 與 I = V/R 比較.

BOTTOM-LEFT, pill label 電阻係數與溫度:
A plot, x-axis temperature T (0 to 300 K), y-axis ρ:
  two curves, both roughly linear at high T (labelled 晶格熱振動散射 ∝ T),
  each levelling off to its own flat residual value at low T (labelled
  殘餘電阻：雜質散射，與 T 無關); upper curve red (#C62828) labelled 雜質較多,
  lower curve green (#2E7D32) labelled 雜質較少.
  Caption: ρ ≈ ρ_thermal(T) + ρ_impurity（Matthiessen 規則）.

BOTTOM-RIGHT, pill label 當導線比 λ 還細:
Two wire cross-sections compared:
  left: a thick wire (width ≫ 38 nm); electron paths scatter inside and rarely
        touch the walls.
  right: a nanowire (width about 10–20 nm); electron paths hit the side walls
        frequently (impact points in red), labelled 有效 λ 受限於線寬 → 電阻係數上升.
  Small note: 先進製程（7 nm、5 nm）的銅互連線正面臨這個問題.

Top-right legend "圖例":
  灰色折線 — 單一電子的實際軌跡
  小黑點 — 碰撞
  藍色粗箭頭 — 漂移速度 v_d
  紅／綠曲線 — 雜質較多／較少的樣本

Bottom pastel boxes (four):
1. light blue: v_d = I/(nAe) ≈ 7.4 × 10⁻⁵ m/s — 例題 10.2：1 A、1 mm² 銅線
2. light green: λ = m v_F/(n e² ρ) ≈ 38.3 nm — 例題 10.3：約通過 150 個離子才碰撞一次
3. light purple: R = ρ L / A  (10.15) — ρ 是材料性質，L/A 是幾何形狀
4. light yellow: 開關一按燈就亮 — 電場以接近光速建立，不必等電子跑完全程
```
