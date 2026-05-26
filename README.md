# 📄 PDF 分割工具

> 使用 Python + Tkinter 製作的 PDF 分割工具
> 提供批次分割、指定頁面輸出、空白頁排除等功能

---

## 📌 專案預覽

### 🔹 模式選擇畫面

<img src="images/01_mode_select.png" width="700">

### 🔹 批次分割畫面

<img src="images/02_split_all.png" width="700">

### 🔹 指定頁碼分割

<img src="images/03_split_selected.png" width="700">

### 🔹 分割完成畫面

<img src="images/05_complete.png" width="700">

---

# ✨ 專案特色

## 🎯 解決問題

傳統 PDF 分割流程容易發生：

* 需要手動另存每頁
* 大量 PDF 處理效率低
* 指定頁面操作繁瑣
* 空白頁需額外整理

本工具將 PDF 分割流程自動化。

---

## ⚙️ 核心功能

### 📄 PDF 分割

* 支援多檔 PDF 批次處理
* 自動建立輸出資料夾
* 每頁獨立輸出 PDF

### ✂️ 指定頁面輸出

* 支援頁碼範圍輸入
* 可輸入：

  * `1,3,5`
  * `1-5`
  * `1,3-6`

### 🧹 空白頁排除

* 自動判斷空白頁
* 可選擇略過空白頁輸出

### 📊 處理進度顯示

* 顯示目前處理狀態
* ProgressBar 即時更新

---

# 🧠 技術亮點

### 🔹 GUI 桌面工具設計

使用：

* Tkinter
* Toplevel
* Progressbar

建立桌面操作介面。

### 🔹 PDF 頁面處理

使用 `PyPDF2`

完成：

* PDF 讀取
* 頁面分割
* PDF 重新輸出

### 🔹 頁碼解析邏輯

自訂頁碼解析功能：

* 支援單頁
* 支援區間
* 自動過濾無效頁碼

---

## 🏗 技術架構

```text id="m9x4q2"
User
  ↓
Tkinter GUI
  ↓
PDF Logic Process
  ↓
PyPDF2
  ↓
Output PDF Files
```

---

## 🛠️ AI 協作開發說明

本專案採 AI 協作開發流程，透過 AI 工具協助：

* 程式邏輯優化
* GUI 流程整理
* 錯誤處理建議
* 技術文件整理

最終功能實作、測試與整合皆由本人確認與調整。

---

# 🚀 執行方式

### 🔹執行環境

* Python 3.12
* 作業系統：Windows 10
* GUI：Tkinter

---

### 🔹安裝套件

```bash id="x7k3q1"
pip install PyPDF2
```

---

### 🔹執行程式

```bash id="n8v2r5"
python V1.py
```

---

# 📦 EXE 打包部署

本專案使用 PyInstaller 打包為 Windows 可執行檔。

### 🔹PyInstaller 安裝

```bash id="t4w8z9"
pip install pyinstaller
```

### 🔹打包指令

```bash id="f2p6m1"
pyinstaller -F -w V1.py
```

---

## 👨‍💻 專案說明

此作品展示以下能力：

* Python GUI 桌面工具開發
* PDF 檔案讀取與頁面處理
* 批次檔案操作流程設計
* 頁碼解析與輸入驗證
* Tkinter GUI 互動設計
* ProgressBar 進度顯示實作
* 錯誤處理與狀態提示設計
* 模組化功能拆分與程式邏輯設計
