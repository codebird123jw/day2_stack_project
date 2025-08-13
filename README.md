# 瀏覽器前進/後退模擬 - Python Stack 實作

## 📌 專案簡介
這是一個使用 **Python** 與 **Stack（堆疊）資料結構** 實作的瀏覽器歷史模擬系統。  
透過兩個堆疊（`back_stack` 與 `forward_stack`），實現類似 Google Chrome、Firefox 的 **前進 / 後退** 功能。

此專案同時展示：
- 陣列 vs Linked List 的差異理解
- Stack 原理與應用
- Python OOP 實作
- 簡易 CLI 互動介面

---

## 📂 專案結構
day2_stack_project/
├── stack.py # Stack 類別實作
├── browser_history.py # 瀏覽器前進/後退模擬
└── README.md # 專案說明文件


---

## 🛠 使用技術
- **Python 3.10+**
- **Stack 資料結構**
- **物件導向程式設計 (OOP)**

---

## 🚀 功能特色
1. **Stack 實作**
   - `push(item)`：新增元素
   - `pop()`：移除並回傳頂端元素
   - `peek()`：查看頂端元素但不移除
   - `is_empty()`：檢查是否為空
   - `size()`：回傳堆疊大小

2. **瀏覽器歷史功能**
   - `visit(url)`：訪問新頁面
   - `back()`：回到上一頁
   - `forward()`：前進到下一頁

3. **CLI 互動模式**
   - 可透過終端輸入指令：
     ```
     visit <網址>
     back
     forward
     quit
     ```

---

## 📸 執行範例
輸入指令 (visit/back/forward/quit): visit google.com
訪問：google.com

輸入指令 (visit/back/forward/quit): visit youtube.com
訪問：youtube.com

輸入指令 (visit/back/forward/quit): back
回到：google.com

輸入指令 (visit/back/forward/quit): forward
前進到：youtube.com
