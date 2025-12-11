# 🚀 Streamlit Community Cloud 完整部署教學

## 📋 目錄
- [部署前準備](#部署前準備)
- [步驟一：建立 GitHub 倉庫](#步驟一建立-github-倉庫)
- [步驟二：推送程式碼](#步驟二推送程式碼)
- [步驟三：部署到 Streamlit Cloud](#步驟三部署到-streamlit-cloud)
- [常見問題](#常見問題)
- [部署檢查清單](#部署檢查清單)

---

## 🎯 部署前準備

### 必要條件
✅ GitHub 帳號（https://github.com）  
✅ 專案程式碼已完成  
✅ 已確認本地可運行  

### 檢查專案檔案
確保你的專案包含：
- `app.py` - 主程式
- `requirements.txt` - 依賴清單
- `runtime.txt` - Python 版本（python-3.9.18）
- `utils/` 資料夾 - 工具模組
- `pages/` 資料夾 - 多頁面

---

## 📝 步驟一：建立 GitHub 倉庫

### 1.1 登入 GitHub
前往 https://github.com 並登入

### 1.2 創建新倉庫

1. 點擊右上角 **"+"** → **"New repository"**

2. 填寫倉庫資訊：
   ```
   Repository name: image-classifier-demo
   Description: AI Image Classifier using ResNet50 - Taica AIGC Project
   
   ☑️ Public（選擇公開）
   ☐ 不要勾選 "Add a README file"
   ☐ 不要勾選 "Add .gitignore"
   ☐ 不要勾選 "Choose a license"
   ```

3. 點擊 **"Create repository"** 按鈕

4. 記下倉庫網址：
   ```
   https://github.com/你的GitHub帳號/image-classifier-demo.git
   ```

---

## 💻 步驟二：推送程式碼

### 2.1 在專案目錄初始化 Git

打開終端機，進入你的專案資料夾：

```bash
# 進入專案目錄（根據你的實際路徑調整）
cd /path/to/your/image-classifier-demo

# 或者如果專案在當前目錄
cd image-classifier-demo
```

### 2.2 設定 Git 使用者資訊（首次使用需要）

```bash
git config user.email "your.email@example.com"
git config user.name "Your Name"
```

### 2.3 初始化 Git 倉庫

```bash
# 初始化 Git
git init

# 查看檔案狀態
git status
```

### 2.4 添加所有檔案

```bash
# 添加所有檔案到暫存區
git add .

# 確認要提交的檔案
git status
```

### 2.5 提交變更

```bash
git commit -m "Initial commit: Taica AIGC Image Classifier Project"
```

### 2.6 連接遠端倉庫

**重要**：將 `你的GitHub帳號` 替換為你的實際 GitHub 使用者名稱

```bash
git remote add origin https://github.com/你的GitHub帳號/image-classifier-demo.git

# 查看遠端設定
git remote -v
```

### 2.7 推送到 GitHub

```bash
# 設定主分支為 main
git branch -M main

# 推送到 GitHub
git push -u origin main
```

### 2.8 處理認證問題

如果出現認證錯誤，使用以下方法之一：

#### 方法 A：使用 Personal Access Token（推薦）

1. 前往 GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. 點擊 "Generate new token (classic)"
3. 設定：
   - Note: `Streamlit Deploy`
   - Expiration: `90 days` 或自訂
   - 勾選 `repo` 權限
4. 點擊 "Generate token" 並**複製 token**（只會顯示一次！）

5. 使用 token 推送：
```bash
git remote set-url origin https://你的token@github.com/你的帳號/image-classifier-demo.git
git push -u origin main
```

#### 方法 B：使用 GitHub CLI（如果已安裝）

```bash
gh auth login
git push -u origin main
```

---

## 🌐 步驟三：部署到 Streamlit Cloud

### 3.1 訪問 Streamlit Community Cloud

打開瀏覽器前往：**https://share.streamlit.io**

### 3.2 登入/註冊

1. 點擊 **"Sign in"** 或 **"Continue with GitHub"**
2. 使用你的 GitHub 帳號登入
3. 授權 Streamlit 存取你的 GitHub 倉庫

### 3.3 部署新應用

#### 方式一：從 Streamlit Cloud 首頁部署

1. 登入後點擊 **"New app"** 按鈕

2. 填寫部署設定：
   ```
   Repository: 你的帳號/image-classifier-demo
   Branch: main
   Main file path: app.py
   ```

3. （可選）點擊 "Advanced settings" 可以設定：
   - Python version（預設會讀取 runtime.txt）
   - Secrets（如果需要 API keys）

4. 點擊 **"Deploy!"** 按鈕

#### 方式二：從 URL 直接部署

在瀏覽器訪問（替換成你的帳號）：
```
https://share.streamlit.io/你的帳號/image-classifier-demo/main/app.py
```

### 3.4 等待部署完成

部署過程約需 **5-10 分鐘**，你會看到以下階段：

```
🔄 正在克隆倉庫...
🔄 正在安裝 Python 依賴...（這步會比較久，約 3-5 分鐘）
🔄 正在下載 ResNet50 模型...（約 98MB）
🔄 正在啟動應用...
✅ 部署完成！
```

### 3.5 獲取應用網址

部署成功後，你會獲得一個永久網址，格式如：
```
https://你的帳號-image-classifier-demo-app-abc123.streamlit.app
```

或更簡潔的：
```
https://image-classifier-demo.streamlit.app
```

### 3.6 測試應用

1. 點擊應用網址
2. 上傳一張測試圖片
3. 確認預測功能正常
4. 測試所有頁面（About、Model Info）

---

## ⚠️ 常見問題與解決方案

### 問題 1: `git push` 被拒絕

**錯誤訊息**：
```
remote: Permission denied
fatal: Authentication failed
```

**解決方案**：
使用 Personal Access Token（見步驟 2.8）

---

### 問題 2: requirements.txt 安裝失敗

**錯誤訊息**：
```
ERROR: Could not find a version that satisfies the requirement...
```

**解決方案**：
1. 檢查 `requirements.txt` 內容是否正確：
```bash
cat requirements.txt
```

應該包含：
```txt
streamlit==1.30.0
torch==2.1.0
torchvision==0.16.0
Pillow==10.1.0
numpy==1.24.3
matplotlib==3.8.2
plotly==5.18.0
requests==2.31.0
```

2. 如果有錯誤，修改後重新推送：
```bash
git add requirements.txt
git commit -m "Fix requirements.txt"
git push origin main
```

---

### 問題 3: 記憶體不足（MemoryError）

**錯誤訊息**：
```
MemoryError: Unable to allocate...
Killed
```

**原因**：
Streamlit Community Cloud 免費版限制 1GB RAM

**解決方案**：
我們的專案已經過優化，應該在 1GB 內運行。如果仍然超出：

1. 檢查是否有不必要的大檔案
2. 確認沒有同時載入多個模型
3. 考慮升級到 Streamlit Cloud Teams（付費方案）

---

### 問題 4: 應用持續重啟

**症狀**：
應用不斷顯示 "Rerunning..." 或自動重新整理

**解決方案**：
1. 檢查程式碼是否有無限迴圈
2. 查看 Streamlit Cloud 日誌找出錯誤
3. 確認所有依賴都已正確安裝

---

### 問題 5: 模型下載失敗

**錯誤訊息**：
```
Error downloading model weights from torch hub
```

**解決方案**：
1. 重新部署（可能是暫時的網路問題）
2. 在 Streamlit Cloud dashboard 點擊 "Reboot app"
3. 確認 PyTorch 和 torchvision 版本相容

---

### 問題 6: 檔案找不到（FileNotFoundError）

**錯誤訊息**：
```
FileNotFoundError: [Errno 2] No such file or directory: 'examples/cat.jpg'
```

**解決方案**：
1. 確認 `examples/` 資料夾已經推送到 GitHub
2. 檢查檔案路徑是否正確（區分大小寫）
3. 可以暫時註解掉範例圖片功能

---

## ✅ 部署檢查清單

### 部署前檢查
- [ ] GitHub 帳號已創建
- [ ] 本地專案可正常運行
- [ ] 所有檔案已添加到 Git
- [ ] requirements.txt 正確無誤
- [ ] runtime.txt 存在（內容：python-3.9.18）

### GitHub 推送檢查
- [ ] Git 使用者資訊已設定
- [ ] 遠端倉庫已添加
- [ ] 程式碼已成功推送到 GitHub
- [ ] 可以在 GitHub 網頁看到所有檔案

### Streamlit Cloud 部署檢查
- [ ] 已註冊 Streamlit Cloud 帳號
- [ ] 已授權 GitHub 存取
- [ ] 倉庫和分支選擇正確
- [ ] Main file path 設為 app.py
- [ ] 部署成功無錯誤

### 部署後測試
- [ ] 應用可以正常開啟
- [ ] 可以上傳圖片
- [ ] 預測功能正常
- [ ] 所有頁面可訪問
- [ ] 視覺化圖表正常顯示

---

## 📊 部署後的工作

### 1. 更新文檔中的網址

在所有文檔中搜尋並替換：
```
your-app-url.streamlit.app
→
你的實際應用網址
```

需要更新的檔案：
- README.md
- docs/ABSTRACT.md
- docs/PROJECT_REPORT.md
- TAICA_PROJECT_COMPLETE.md
- EXECUTIVE_SUMMARY.md

### 2. 添加徽章到 README

在 README.md 開頭添加：
```markdown
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://你的應用網址)
```

### 3. 測試所有功能

- [ ] 上傳不同類型的圖片
- [ ] 測試範例圖片按鈕
- [ ] 調整設定（Top-K slider）
- [ ] 切換到 About 頁面
- [ ] 切換到 Model Info 頁面
- [ ] 檢查視覺化圖表

### 4. 準備 Demo 說明

記錄以下資訊：
- ✅ 應用網址
- ✅ GitHub 倉庫網址
- ✅ 主要功能清單
- ✅ 技術亮點
- ✅ 測試結果截圖

---

## 🔄 更新應用（之後需要修改時）

### 修改程式碼後更新

```bash
# 1. 修改程式碼
nano app.py  # 或使用你喜歡的編輯器

# 2. 測試修改
streamlit run app.py

# 3. 提交變更
git add .
git commit -m "更新：添加新功能"

# 4. 推送到 GitHub
git push origin main

# 5. Streamlit Cloud 會自動重新部署（約 2-3 分鐘）
```

### 手動重新部署

如果自動部署沒有觸發：
1. 前往 Streamlit Cloud dashboard
2. 找到你的應用
3. 點擊 "..." → "Reboot app"

---

## 🎯 快速部署命令總結

```bash
# === 完整部署流程（複製貼上執行） ===

# 1. 進入專案目錄
cd /path/to/your/image-classifier-demo

# 2. 設定 Git（首次需要，替換成你的資訊）
git config user.email "your.email@example.com"
git config user.name "Your Name"

# 3. 初始化並提交
git init
git add .
git commit -m "Initial commit: Taica AIGC Image Classifier Project"

# 4. 連接 GitHub（替換成你的帳號）
git remote add origin https://github.com/你的帳號/image-classifier-demo.git

# 5. 推送到 GitHub
git branch -M main
git push -u origin main

# 6. 接著前往 https://share.streamlit.io 完成部署
```

---

## 📱 分享你的應用

### 方式一：直接分享連結
```
https://你的應用網址.streamlit.app
```

### 方式二：二維碼（QR Code）
使用線上工具生成 QR Code：
- https://www.qr-code-generator.com/
- 輸入你的應用網址
- 下載 QR Code 圖片

### 方式三：嵌入到網頁
```html
<iframe src="https://你的應用網址.streamlit.app" 
        width="100%" height="600"></iframe>
```

---

## 🎓 進階設定

### 設定自訂網域（可選）

1. 在 Streamlit Cloud dashboard
2. 進入 App settings → General
3. 修改 "App URL" 為你想要的名稱

### 設定環境變數

如果需要 API keys 或敏感資訊：
1. 進入 App settings → Secrets
2. 添加 TOML 格式的設定：
```toml
[api]
key = "your-api-key"
```

3. 在程式中使用：
```python
import streamlit as st
api_key = st.secrets["api"]["key"]
```

### 啟用 GitHub Actions（進階）

創建 `.github/workflows/deploy.yml` 實現自動化測試。

---

## 📞 需要幫助？

### 官方資源
- **Streamlit 文檔**: https://docs.streamlit.io/
- **Streamlit Cloud 指南**: https://docs.streamlit.io/streamlit-community-cloud
- **社群論壇**: https://discuss.streamlit.io/
- **GitHub Issues**: 搜尋類似問題

### 查看日誌
在 Streamlit Cloud dashboard：
1. 找到你的應用
2. 點擊 "Manage app"
3. 查看 "Logs" 標籤頁

### 聯絡支援
如果遇到平台問題：
- 前往 https://discuss.streamlit.io/
- 創建新主題描述問題
- Streamlit 團隊通常會在 24 小時內回覆

---

## 🎉 恭喜！

完成以上步驟後，你的 AI Image Classifier 就成功部署到 Streamlit Community Cloud 了！

### 下一步
- ✅ 測試所有功能
- ✅ 更新文檔中的網址
- ✅ 準備 Demo 簡報
- ✅ 分享給老師和同學
- ✅ 準備繳交作業

---

<div align="center">

## 🚀 立即開始部署！

**估計時間：20 分鐘**

1. 推送到 GitHub (5 分鐘)
2. 部署到 Streamlit Cloud (10 分鐘)
3. 測試與分享 (5 分鐘)

---

**祝你部署順利！** 🎊

如有問題，請參考 [常見問題](#常見問題) 部分

</div>
