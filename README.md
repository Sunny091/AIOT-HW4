# 🖼️ AI Image Classifier - Streamlit Demo

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-app-url.streamlit.app)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.1.0-ee4c2c.svg)](https://pytorch.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **Taica AIGC 專題作業** - 基於深度學習的影像分類系統

一個使用 ResNet50 預訓練模型的即時影像分類 Web 應用程式，能夠辨識 1000 種 ImageNet 類別的物體。

---

## 📋 目錄

- [專案簡介](#專案簡介)
- [功能特色](#功能特色)
- [Demo 展示](#demo-展示)
- [技術架構](#技術架構)
- [快速開始](#快速開始)
- [本地運行](#本地運行)
- [部署指南](#部署指南)
- [專案結構](#專案結構)
- [使用說明](#使用說明)
- [常見問題](#常見問題)
- [貢獻指南](#貢獻指南)
- [授權資訊](#授權資訊)

---

## 📖 專案簡介

本專題實作了一個基於深度學習的影像分類系統，使用 **ResNet50** 卷積神經網路模型，預訓練於 ImageNet 資料集。系統透過 Streamlit 框架提供直觀的 Web 介面，讓使用者可以上傳圖片並即時獲得分類結果。

### 🎯 專題目標

- 展示深度學習在電腦視覺的實際應用
- 實現遷移學習（Transfer Learning）技術
- 打造可部署的 AI 應用程式
- 提供互動式教學演示平台

---

## ✨ 功能特色

- ✅ **即時影像分類**：上傳圖片立即獲得分類結果
- ✅ **Top-K 預測**：顯示前 K 個最可能的類別與信心分數
- ✅ **視覺化展示**：互動式圖表呈現預測機率分佈
- ✅ **多頁面架構**：主頁、關於頁面、模型資訊頁面
- ✅ **範例圖片**：內建測試圖片快速體驗
- ✅ **響應式設計**：適配不同螢幕尺寸
- ✅ **CPU 友善**：無需 GPU 即可流暢運行
- ✅ **1000 類別**：支援 ImageNet 全部分類

---

## 🎬 Demo 展示

### 主要介面

![Main Interface](docs/screenshots/main_interface.png)

### 分類結果範例

| 輸入圖片 | 預測結果 | 信心分數 |
|---------|---------|---------|
| 🐱 貓咪照片 | Tabby Cat | 92.3% |
| 🚗 汽車照片 | Sports Car | 88.7% |
| 🍎 蘋果照片 | Granny Smith | 95.1% |

### 線上 Demo

🔗 **[立即體驗線上 Demo](https://your-app-url.streamlit.app)** (請替換為實際部署網址)

---

## 🏗️ 技術架構

### 核心技術棧

| 技術 | 版本 | 用途 |
|------|------|------|
| **Python** | 3.9+ | 程式語言 |
| **PyTorch** | 2.1.0 | 深度學習框架 |
| **torchvision** | 0.16.0 | 電腦視覺工具 |
| **Streamlit** | 1.30.0 | Web 框架 |
| **Pillow** | 10.1.0 | 影像處理 |
| **Plotly** | 5.18.0 | 視覺化 |

### 模型資訊

- **模型名稱**：ResNet50
- **架構**：50 層殘差網路
- **參數量**：25.6M
- **預訓練**：ImageNet (1000 classes)
- **準確率**：Top-1: 76.1% / Top-5: 92.9%
- **輸入尺寸**：224×224×3

---

## 🚀 快速開始

### 環境需求

- Python 3.9 或更高版本
- pip 套件管理工具
- 至少 2GB 可用記憶體
- （選用）CUDA 相容 GPU

### 一鍵安裝與運行

```bash
# 1. 克隆專案
git clone https://github.com/your-username/image-classifier-demo.git
cd image-classifier-demo

# 2. 安裝依賴
pip install -r requirements.txt

# 3. 運行應用
streamlit run app.py
```

應用程式將在瀏覽器自動開啟：`http://localhost:8501`

---

## 💻 本地運行

### 詳細步驟

#### 1. 創建虛擬環境（建議）

```bash
# 使用 venv
python -m venv venv

# 啟動虛擬環境
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

#### 2. 安裝依賴套件

```bash
pip install -r requirements.txt
```

#### 3. 下載範例圖片（選用）

```bash
# 創建 examples 資料夾並放入測試圖片
mkdir -p examples
# 將你的測試圖片放入 examples/ 資料夾
```

#### 4. 啟動應用

```bash
streamlit run app.py
```

#### 5. 開啟瀏覽器

訪問 `http://localhost:8501`

### 進階設定

#### 修改 Streamlit 設定

創建 `.streamlit/config.toml`：

```toml
[theme]
primaryColor = "#1f77b4"
backgroundColor = "#ffffff"
secondaryBackgroundColor = "#f0f2f6"
textColor = "#262730"
font = "sans serif"

[server]
maxUploadSize = 200
port = 8501
```

#### GPU 加速（選用）

如果有 NVIDIA GPU：

```bash
# 安裝 GPU 版本 PyTorch
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118
```

---

## 🌐 部署指南

### 方法一：部署到 Streamlit Community Cloud

**最簡單的部署方式，完全免費！**

#### 步驟：

1. **推送代碼到 GitHub**

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/your-username/image-classifier-demo.git
git push -u origin main
```

2. **登入 Streamlit Cloud**

   訪問 [share.streamlit.io](https://share.streamlit.io)

3. **部署應用**

   - 點擊 "New app"
   - 選擇你的 GitHub 倉庫
   - 主檔案路徑：`app.py`
   - 點擊 "Deploy"

4. **等待部署完成**

   首次部署需要 5-10 分鐘下載模型

#### 注意事項：

- ✅ 免費方案有資源限制（1GB RAM）
- ✅ 應用閒置後會自動休眠
- ✅ 支援自動從 GitHub 更新
- ⚠️ ResNet50 在 CPU 上推論約 2-3 秒

### 方法二：部署到 Vercel（實驗性）

Streamlit 應用通常部署在 Streamlit Cloud，但也可嘗試 Vercel：

#### 步驟：

1. **安裝 Vercel CLI**

```bash
npm install -g vercel
```

2. **創建 `vercel.json`**

```json
{
  "builds": [
    {
      "src": "app.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "app.py"
    }
  ]
}
```

3. **部署**

```bash
vercel --prod
```

**注意**：Vercel 對 Streamlit 支援有限，建議使用 Streamlit Cloud。

### 方法三：Docker 容器化部署

#### 1. 創建 Dockerfile

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

#### 2. 構建映像

```bash
docker build -t image-classifier .
```

#### 3. 運行容器

```bash
docker run -p 8501:8501 image-classifier
```

### 方法四：部署到 Heroku

#### 步驟：

1. **創建 `Procfile`**

```
web: sh setup.sh && streamlit run app.py
```

2. **創建 `setup.sh`**

```bash
mkdir -p ~/.streamlit/
echo "[server]
headless = true
port = $PORT
enableCORS = false
" > ~/.streamlit/config.toml
```

3. **部署**

```bash
heroku login
heroku create your-app-name
git push heroku main
```

---

## 📁 專案結構

```
image-classifier-demo/
│
├── app.py                      # 主應用程式
├── requirements.txt            # Python 依賴
├── runtime.txt                 # Python 版本（Streamlit Cloud）
├── .gitignore                  # Git 忽略檔案
├── README.md                   # 專案說明文件
│
├── pages/                      # Streamlit 多頁面
│   ├── 1_📊_About.py          # 關於頁面
│   └── 2_🔬_Model_Info.py     # 模型資訊頁面
│
├── utils/                      # 工具模組
│   ├── __init__.py
│   ├── model.py               # 模型載入與推論
│   └── preprocessing.py       # 影像預處理
│
├── examples/                   # 範例圖片
│   ├── cat.jpg
│   ├── dog.jpg
│   └── car.jpg
│
├── docs/                       # 文件資料
│   ├── screenshots/           # 截圖
│   └── report.md              # 專題報告
│
└── .streamlit/                 # Streamlit 設定
    └── config.toml            # 應用設定
```

---

## 📖 使用說明

### 基本操作

1. **上傳圖片**
   - 點擊「Browse files」按鈕
   - 選擇 JPG、PNG 或 JPEG 格式圖片
   - 或拖曳圖片到上傳區域

2. **查看結果**
   - 系統自動處理並顯示預測結果
   - Top-1 預測顯示在高亮框中
   - 可查看 Top-K 所有預測與信心分數

3. **使用範例圖片**
   - 點擊「Try Cat」、「Try Dog」等按鈕
   - 快速測試系統功能

4. **調整設定**
   - 側邊欄可調整顯示預測數量（1-10）

### 進階功能

- **多頁面導航**：左側選單切換不同頁面
- **模型資訊**：查看詳細技術規格
- **關於頁面**：了解專題背景

---

## ❓ 常見問題

### Q1: 為什麼首次運行很慢？

**A**: 首次運行需要下載 ResNet50 模型（約 98MB），之後會快取在本地。

### Q2: 可以在沒有 GPU 的電腦運行嗎？

**A**: 可以！此專題特別優化為 CPU 友善，推論時間約 2-3 秒。

### Q3: 支援哪些圖片格式？

**A**: JPG、JPEG、PNG 格式，最大 200MB。

### Q4: 可以辨識多少種物體？

**A**: 1000 種 ImageNet 類別，包括動物、車輛、物品、食物等。

### Q5: 如何提升準確度？

**A**: 
- 使用清晰、高解析度圖片
- 確保主體在畫面中央
- 避免過度遮擋或模糊

### Q6: 模型可以離線使用嗎？

**A**: 模型首次下載後會快取在 `~/.cache/torch/hub/checkpoints/`，之後可離線使用。

### Q7: Streamlit Cloud 部署失敗怎麼辦？

**A**: 
- 檢查 `requirements.txt` 格式
- 確認 Python 版本相容（3.9+）
- 查看部署日誌找出錯誤

### Q8: 可以訓練自己的模型嗎？

**A**: 可以！修改 `utils/model.py` 載入你的自定義模型。

---

## 🔧 進階開發

### 自定義模型

替換為其他 torchvision 模型：

```python
# utils/model.py
import torchvision.models as models

# 使用 ResNet101
model = models.resnet101(pretrained=True)

# 使用 EfficientNet
model = models.efficientnet_b0(pretrained=True)

# 使用 Vision Transformer
model = models.vit_b_16(pretrained=True)
```

### 添加新功能

**Grad-CAM 視覺化**：顯示模型關注區域

```python
from pytorch_grad_cam import GradCAM

cam = GradCAM(model=model, target_layers=[model.layer4[-1]])
grayscale_cam = cam(input_tensor=img_tensor)
```

**批次處理**：同時處理多張圖片

```python
def batch_predict(images, model):
    img_tensors = torch.stack([transform(img) for img in images])
    with torch.no_grad():
        outputs = model(img_tensors)
    return outputs
```

---

## 🤝 貢獻指南

歡迎提交 Issue 和 Pull Request！

### 貢獻流程

1. Fork 本專案
2. 創建功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交變更 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 開啟 Pull Request

### 開發規範

- 遵循 PEP 8 程式碼風格
- 添加適當的註解和文檔
- 測試新功能後再提交

---

## 📚 學習資源

### 推薦閱讀

- [ResNet 論文](https://arxiv.org/abs/1512.03385)
- [PyTorch 官方教學](https://pytorch.org/tutorials/)
- [Streamlit 文檔](https://docs.streamlit.io/)
- [深度學習花書](https://www.deeplearningbook.org/)

### 相關課程

- Taica AIGC 課程：https://taicatw.net/
- Stanford CS231n：Convolutional Neural Networks
- Fast.ai Practical Deep Learning

---

## 📜 授權資訊

本專題採用 MIT 授權條款。詳見 [LICENSE](LICENSE) 檔案。

### 第三方授權

- **ResNet50 模型**：BSD License (Facebook AI Research)
- **ImageNet 資料**：請遵守 ImageNet 使用條款
- **Streamlit**：Apache License 2.0

---

## 👥 作者與致謝

**作者**: Taica AIGC 學生  
**指導**: Taica 課程教師團隊  
**學期**: 2024 Fall

### 特別感謝

- Taica 台灣大專院校人工智慧學程聯盟
- PyTorch 與 Streamlit 開源社群
- ImageNet 資料集維護團隊

---

## 📧 聯絡方式

- **Email**: your.email@example.com
- **GitHub**: [@your-username](https://github.com/your-username)
- **課程網站**: [Taica](https://taicatw.net/)

---

## 🌟 Star History

如果這個專題對你有幫助，請給個 ⭐️ Star！

[![Star History Chart](https://api.star-history.com/svg?repos=your-username/image-classifier-demo&type=Date)](https://star-history.com/#your-username/image-classifier-demo&Date)

---

<div align="center">

**🎓 Built with ❤️ for AI Education**

[Taica](https://taicatw.net/) | [Streamlit](https://streamlit.io/) | [PyTorch](https://pytorch.org/)

</div>
