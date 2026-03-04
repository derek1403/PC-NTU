---
title: "Modern Physics (近代物理) 學習筆記"
author: "PC"
date: "2026-02-24"
subject: "Physics"
tags: ["Modern Physics", "Quantum Mechanics", "Relativity"]
---

# 近代物理 (Modern Physics) 課程筆記

> **課程簡介**
> 近代物理指的是20世紀 (1900年以後) 所發展出的物理，主要是量子的基本觀念及應用。與1900年以前所發展的古典物理有相當大的不同。本課程將從歷史背景與實驗證明出發，帶領大家了解這個由量子建構的世界。

**教科書 (Textbook):**
* “Concepts of Modern Physics”, Arthur Beiser and Kok Wai Cheah

**參考書目 (References):**
* “Modern Physics”, 6th Ed., Paul A. Tipler and Raulph A. Llewellyn

---

## 📝 目錄 (Contents)

- [x] **0. [Introduction (簡介)](./lecture/01_Introduction/introduction.ipynb)**
- [ ] **1. Relativity (相對論)**
- [ ] **2. Particle Properties of Waves (波的粒子性質)**
- [ ] **3. Wave Properties of Particles (粒子的波動性質)**
- [ ] **4. Atomic Structure (原子結構)**
- [ ] **5. Quantum Mechanics (量子力學)**
- [ ] **6. Quantum Theory of the Hydrogen Atom (氫原子的量子理論)**
- [ ] **7. Many-Electron Atoms (多電子原子)**
- [ ] **8. Molecules (分子)**
- [ ] **9. Statistical Mechanics (統計力學)**
- [ ] **10. Solid State Physics (固態物理)**

---

## 1. Introduction
*(在此填寫 1900 年代物理學遇到的兩朵烏雲：黑體輻射與光速不變的問題...)*

---

## 2. Relativity
### 2.1 歷史背景與動機
古典力學中，伽利略轉換認為時間是絕對的。然而，馬克士威方程組暗示光速 $c$ 是常數。愛因斯坦提出了狹義相對論的兩個基本公設：
1. **相對性原理**：在所有慣性座標系中，物理定律的形式都相同。
2. **光速不變原理**：在所有慣性座標系中，真空中的光速 $c$ 恆定。

### 2.2 推導：時間膨脹 (Time Dilation)



**思考實驗 (光鐘 Analogy)：**
想像一個「光鐘」，由上下兩面鏡子組成，距離為 $L$。光子在兩面鏡子間上下反射一次代表一個時間單位（滴答）。

**步驟 1：靜止座標系 (Rest Frame)**
對於與光鐘一起靜止的觀察者而言，光子上下來回的距離是 $2L$。
測量到的時間間隔 $\Delta t_0$（固有時間 proper time）為：
$$\Delta t_0 = \frac{2L}{c}$$

**步驟 2：移動座標系 (Moving Frame)**
現在光鐘以速度 $v$ 向右水平移動。對於地面的靜止觀察者而言，光子走的不再是垂直路線，而是一個「斜邊」路徑 $D$。
在這段時間 $\Delta t$ 內，光鐘向右移動了 $v \Delta t$，所以光子單趟水平移動的距離是 $\frac{v \Delta t}{2}$。

根據畢氏定理，光子單趟飛行的斜邊距離 $D$ 為：
$$D = \sqrt{L^2 + \left(\frac{v \Delta t}{2}\right)^2}$$

**步驟 3：聯立求解**
由於光速 $c$ 是不變的，光子走這段斜邊所花的時間為：
$$\frac{\Delta t}{2} = \frac{D}{c}$$
$$c \frac{\Delta t}{2} = \sqrt{L^2 + \left(\frac{v \Delta t}{2}\right)^2}$$

將兩邊平方來解出 $\Delta t$：
$$c^2 \frac{\Delta t^2}{4} = L^2 + v^2 \frac{\Delta t^2}{4}$$
$$(c^2 - v^2) \frac{\Delta t^2}{4} = L^2$$
$$\Delta t^2 = \frac{4L^2}{c^2 - v^2} = \frac{\frac{4L^2}{c^2}}{1 - \frac{v^2}{c^2}}$$

**步驟 4：代入固有時間並得出結論**
因為 $\Delta t_0^2 = \frac{4L^2}{c^2}$，代入上式並開根號：
$$\Delta t = \frac{\Delta t_0}{\sqrt{1 - \frac{v^2}{c^2}}}$$

我們定義羅倫茲因子 (Lorentz factor) $\gamma = \frac{1}{\sqrt{1 - \frac{v^2}{c^2}}}$，因為 $v < c$，所以 $\gamma \ge 1$。
最終得到時間膨脹公式：
$$\Delta t = \gamma \Delta t_0$$
**結論：** 移動中的時鐘走得比較慢（$\Delta t > \Delta t_0$）。

---

## 3. Particle Properties of Waves
*(筆記預留區：可記錄光電效應、康普頓散射等證明光具有粒子性的實驗推導...)*