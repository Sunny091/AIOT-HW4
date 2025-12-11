# 🚀 快速開始指南

## 5 分鐘上手教學

### 方法一：直接使用線上版本

最簡單！訪問部署好的應用：

🔗 **[線上 Demo](https://your-app-url.streamlit.app)** (待部署後替換)

---

### 方法二：本地運行

#### 前置需求
- Python 3.9+
- pip

#### 三步驟安裝

```bash
# 1. 克隆專案
git clone https://github.com/your-username/image-classifier-demo.git
cd image-classifier-demo

# 2. 安裝依賴（可能需要 2-3 分鐘）
pip install -r requirements.txt

# 3. 運行（首次會下載模型 ~98MB）
streamlit run app.py
```

✅ 自動開啟瀏覽器：http://localhost:8501

---

### 方法三：使用虛擬環境（推薦）

```bash
# 創建虛擬環境
python -m venv venv

# 啟動虛擬環境
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# 安裝並運行
pip install -r requirements.txt
streamlit run app.py
```

---

## 📖 基本使用

### 1. 上傳圖片

- 點擊 "Browse files" 按鈕
- 選擇圖片檔案（JPG、PNG、JPEG）
- 或直接拖曳圖片到上傳區

### 2. 查看結果

- 自動顯示 Top-5 預測
- 查看信心分數
- 觀看視覺化圖表

### 3. 嘗試範例

- 點擊 "Try Cat"、"Try Dog" 等按鈕
- 快速體驗分類功能

### 4. 調整設定

- 側邊欄調整顯示預測數量
- 探索多個頁面

---

## 🎯 測試建議

### 適合測試的圖片類型：

✅ **動物**
- 貓、狗、鳥類
- 野生動物
- 昆蟲

✅ **車輛**
- 汽車、卡車
- 飛機、船舶
- 腳踏車、機車

✅ **食物**
- 水果、蔬菜
- 料理、甜點
- 飲料

✅ **物品**
- 家具、家電
- 工具、玩具
- 運動器材

✅ **自然**
- 花卉、樹木
- 風景、天空
- 動物棲息地

---

## ⚠️ 常見問題快速解答

### Q: 首次運行很慢？
**A**: 正常！需要下載 ResNet50 模型（~98MB），只有第一次會慢。

### Q: 出現 "module not found" 錯誤？
**A**: 
```bash
pip install -r requirements.txt --force-reinstall
```

### Q: 圖片上傳後沒反應？
**A**: 檢查圖片格式是否為 JPG/PNG，大小是否超過 200MB。

### Q: 預測結果不準確？
**A**: 
- 確保主體清晰可見
- 避免多個物體混雜
- 使用標準角度拍攝

### Q: 可以在沒有網路的環境運行嗎？
**A**: 模型下載後會快取，之後可離線使用。

---

## 🛠️ 進階使用

### 自定義模型

編輯 `utils/model.py`:

```python
# 替換為其他模型
model = models.resnet101(pretrained=True)  # ResNet101
# 或
model = models.efficientnet_b0(pretrained=True)  # EfficientNet
```

### 修改 Top-K 預設值

編輯 `app.py`:

```python
top_k = st.slider("...", value=10)  # 預設顯示 10 個
```

### 添加自訂範例圖片

1. 將圖片放入 `examples/` 資料夾
2. 編輯 `app.py` 的 `example_images` 字典
3. 重新運行

---

## 📊 效能測試

### 推論速度基準

| 環境 | 推論時間 |
|------|---------|
| CPU (Intel i5) | ~2-3s |
| CPU (Intel i7) | ~1-2s |
| GPU (NVIDIA GTX 1060) | ~0.3s |
| GPU (NVIDIA RTX 3090) | ~0.1s |

### 記憶體使用

- 模型載入：~250MB
- 單張圖片推論：~100MB
- Streamlit 應用：~200MB
- **總計**：~550MB

---

## 🎓 學習資源

### 推薦教學

1. **PyTorch 官方教學**
   - https://pytorch.org/tutorials/

2. **Streamlit 文檔**
   - https://docs.streamlit.io/

3. **ResNet 論文閱讀**
   - https://arxiv.org/abs/1512.03385

4. **ImageNet 介紹**
   - http://www.image-net.org/

### 延伸學習

- 🔍 電腦視覺基礎
- 🧠 深度學習原理
- 🎨 遷移學習技術
- 🌐 Web 應用部署

---

## 💬 需要幫助？

- 📧 Email: your.email@example.com
- 💻 GitHub Issues: [提交問題](https://github.com/your-username/image-classifier-demo/issues)
- 📚 查看完整 README: [README.md](../README.md)
- 🎓 Taica 課程: https://taicatw.net/

---

## ✅ 下一步

完成快速開始後，建議：

1. ✅ 閱讀完整 [README.md](../README.md)
2. ✅ 查看 [技術文檔](../pages/2_🔬_Model_Info.py)
3. ✅ 瀏覽 [開發對話紀錄](DEVELOPMENT_DIALOG.md)
4. ✅ 學習 [部署教學](../README.md#部署指南)
5. ✅ 嘗試 [進階功能](#進階使用)

---

<div align="center">

**🎉 恭喜！你已經成功運行 AI 影像分類器！**

[返回主頁](../README.md) | [技術文檔](../pages/2_🔬_Model_Info.py) | [關於專題](../pages/1_📊_About.py)

</div>
