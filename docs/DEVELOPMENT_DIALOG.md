# Agent 開發過程對話紀錄

**專題**: AI Image Classifier  
**日期**: 2024 Fall Semester  
**對話數**: 35 則

---

## 🗣️ 開發對話全紀錄

### **[Turn 1] 專題啟動**

**[User]**: 我想為 Taica AIGC 課程做一個深度學習專題,你有什麼建議嗎?

**[Agent]**: 很好的想法!根據 Taica 課程內容,我建議你從以下四個方向選擇:
1. 生成式 AI 文本模型
2. 生成式 AI 圖片模型  
3. 分類/辨識模型
4. 語音處理模型

考慮到你需要部署到 Streamlit,我推薦**影像分類模型**,因為:
- 可以使用預訓練模型,開發快速
- CPU 可運行,無需 GPU
- 互動性強,適合 Demo
- 教育價值高

---

### **[Turn 2] 模型選擇討論**

**[User]**: 影像分類聽起來不錯!應該用什麼模型?

**[Agent]**: 我建議使用 **ResNet50**,原因如下:

**優點**:
- ✅ PyTorch 內建,無需手動下載
- ✅ 準確率高 (Top-5: 92.9%)
- ✅ CPU 推論速度快 (~2-3秒)
- ✅ 預訓練於 ImageNet (1000 類)
- ✅ 教學資源豐富

**替代方案**:
- VGG16: 較舊,參數多
- EfficientNet: 更新,但稍複雜
- MobileNet: 太輕量,準確率較低

ResNet50 是平衡效能與易用性的最佳選擇!

---

### **[Turn 3] 功能設計**

**[User]**: ResNet50 聽起來很適合!Demo 應該有哪些功能?

**[Agent]**: 我為你規劃核心功能:

**必備功能**:
1. 📤 圖片上傳介面
2. 🔍 即時分類推論
3. 📊 Top-5 預測結果
4. 📈 信心分數視覺化
5. 🎯 範例圖片快速測試

**進階功能**:
1. 多頁面設計 (主頁/關於/模型資訊)
2. 可調整 Top-K 數量
3. 圖表展示機率分佈
4. 響應式設計

先實作核心功能,有時間再加進階功能!

---

### **[Turn 4] 技術架構確認**

**[User]**: 需要用到哪些技術和套件?

**[Agent]**: 完整技術棧如下:

```
核心框架:
- Streamlit 1.30.0 (Web 介面)
- PyTorch 2.1.0 (深度學習)
- torchvision 0.16.0 (電腦視覺)

影像處理:
- Pillow 10.1.0 (圖片讀取)
- NumPy 1.24.3 (數值計算)

視覺化:
- Plotly 5.18.0 (互動圖表)
- Matplotlib 3.8.2 (靜態圖表)

輔助工具:
- requests (下載標籤)
```

全部都能用 pip 安裝,非常簡單!

---

### **[Turn 5] 專案結構規劃**

**[User]**: 專案資料夾應該怎麼組織?

**[Agent]**: 我建議這樣的結構:

```
image-classifier-demo/
├── app.py                 # 主程式
├── requirements.txt       # 依賴清單
├── README.md             # 說明文件
├── pages/                # 多頁面
│   ├── 1_📊_About.py
│   └── 2_🔬_Model_Info.py
├── utils/                # 工具模組
│   ├── model.py          # 模型載入
│   └── preprocessing.py  # 影像預處理
└── examples/             # 範例圖片
    ├── cat.jpg
    ├── dog.jpg
    └── car.jpg
```

模組化設計方便維護和擴展!

---

### **[Turn 6] 模型載入實作**

**[User]**: 開始寫程式吧!先從模型載入開始?

**[Agent]**: 沒問題!我們在 `utils/model.py` 中實作:

```python
import torch
import torchvision.models as models
import streamlit as st

@st.cache_resource
def load_model():
    model = models.resnet50(pretrained=True)
    model.eval()
    return model
```

關鍵點:
- ✅ 使用 `@st.cache_resource` 快取模型
- ✅ `pretrained=True` 自動下載權重
- ✅ `model.eval()` 設為評估模式

這樣模型只會載入一次,節省時間!

---

### **[Turn 7] ImageNet 標籤處理**

**[User]**: 模型輸出是數字,怎麼轉換成類別名稱?

**[Agent]**: 好問題!我們需要 ImageNet 標籤對應:

```python
import requests

@st.cache_data
def load_imagenet_labels():
    url = "https://raw.githubusercontent.com/anishathalye/imagenet-simple-labels/master/imagenet-simple-labels.json"
    response = requests.get(url)
    labels = response.json()
    return labels
```

這樣可以把類別索引 (0-999) 對應到實際名稱 (例如: "tabby cat")!

使用 `@st.cache_data` 避免重複下載。

---

### **[Turn 8] 影像預處理**

**[User]**: ResNet50 對輸入圖片有什麼要求?

**[Agent]**: ResNet50 需要特定的預處理:

```python
from torchvision import transforms

transform = transforms.Compose([
    transforms.Resize(256),          # 調整短邊到 256
    transforms.CenterCrop(224),      # 中心裁切 224x224
    transforms.ToTensor(),           # 轉為 Tensor
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406], # ImageNet 均值
        std=[0.229, 0.224, 0.225]    # ImageNet 標準差
    )
])
```

這是 ImageNet 的標準預處理流程!

**注意**: 輸入必須是 224x224 RGB 圖片。

---

### **[Turn 9] 推論函數實作**

**[User]**: 怎麼把圖片輸入模型並獲得預測?

**[Agent]**: 完整的推論流程:

```python
def predict(image, model, labels, top_k=5):
    # 1. 預處理
    img_tensor = transform(image).unsqueeze(0)
    
    # 2. 推論
    with torch.no_grad():
        outputs = model(img_tensor)
        probs = torch.nn.functional.softmax(outputs[0], dim=0)
    
    # 3. 取 Top-K
    top_probs, top_indices = torch.topk(probs, top_k)
    
    # 4. 格式化結果
    predictions = []
    for prob, idx in zip(top_probs, top_indices):
        label = labels[idx.item()]
        predictions.append((label, prob.item()))
    
    return predictions
```

返回 `[(標籤, 機率), ...]` 格式!

---

### **[Turn 10] Streamlit UI 設計**

**[User]**: 主頁面應該怎麼設計?

**[Agent]**: 我建議採用兩欄佈局:

```python
st.set_page_config(
    page_title="Image Classifier",
    page_icon="🖼️",
    layout="wide"
)

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📤 Upload Image")
    uploaded_file = st.file_uploader(
        "Choose an image",
        type=['jpg', 'jpeg', 'png']
    )

with col2:
    st.subheader("🔍 Results")
    # 顯示預測結果
```

**左側**: 上傳圖片  
**右側**: 顯示結果

這樣視覺上很平衡!

---

### **[Turn 11] 檔案上傳處理**

**[User]**: 使用者上傳圖片後怎麼處理?

**[Agent]**: 需要驗證和轉換:

```python
from PIL import Image

def validate_image(uploaded_file):
    try:
        image = Image.open(uploaded_file)
        if image.mode != 'RGB':
            image = image.convert('RGB')
        return image
    except:
        return None
```

**驗證重點**:
- ✅ 檢查是否為有效圖片
- ✅ 轉換為 RGB 模式
- ✅ 處理異常情況

這樣可以避免程式崩潰!

---

### **[Turn 12] 結果展示設計**

**[User]**: 預測結果應該怎麼展示比較清楚?

**[Agent]**: 我設計了三層展示:

**1. 高亮顯示 Top-1**:
```python
st.markdown(f"""
<div class="prediction-box">
    <h2>{top_label}</h2>
    <h3>{top_prob*100:.2f}% confidence</h3>
</div>
""", unsafe_allow_html=True)
```

**2. 列表顯示所有預測**:
```python
for i, (label, prob) in enumerate(predictions):
    st.write(f"{i+1}. {label} - {prob*100:.2f}%")
    st.progress(prob)
```

**3. 圖表視覺化**:
使用 Plotly 繪製水平長條圖!

層次分明,一目了然!

---

### **[Turn 13] 視覺化圖表實作**

**[User]**: Plotly 圖表怎麼畫?

**[Agent]**: 用橫向長條圖最適合:

```python
import plotly.graph_objects as go

labels_list = [pred[0] for pred in predictions]
probs_list = [pred[1] for pred in predictions]

fig = go.Figure(data=[
    go.Bar(
        x=probs_list,
        y=labels_list,
        orientation='h',
        marker=dict(
            color=probs_list,
            colorscale='Blues'
        )
    )
])

fig.update_layout(
    title=f"Top {top_k} Predictions",
    xaxis_title="Probability",
    yaxis_title="Class"
)

st.plotly_chart(fig, use_container_width=True)
```

顏色深淺表示機率高低,很直觀!

---

### **[Turn 14] 側邊欄功能**

**[User]**: 側邊欄應該放什麼內容?

**[Agent]**: 側邊欄可以放設定和說明:

```python
with st.sidebar:
    st.header("⚙️ Settings")
    top_k = st.slider(
        "Number of predictions",
        min_value=1,
        max_value=10,
        value=5
    )
    
    st.markdown("---")
    st.header("📖 Instructions")
    st.markdown("""
    1. Upload an image
    2. Wait for processing
    3. View predictions
    """)
    
    st.header("ℹ️ About")
    st.info("Using ResNet50 model...")
```

集中管理設定,不佔主畫面空間!

---

### **[Turn 15] 範例圖片功能**

**[User]**: 可以提供範例圖片讓使用者快速測試嗎?

**[Agent]**: 好主意!實作方式:

```python
st.markdown("### 🎯 Try examples:")

example_images = {
    "Cat": "examples/cat.jpg",
    "Dog": "examples/dog.jpg",
    "Car": "examples/car.jpg"
}

cols = st.columns(3)
for idx, (name, path) in enumerate(example_images.items()):
    with cols[idx]:
        if st.button(f"Try {name}"):
            uploaded_file = path
```

點擊按鈕就載入範例,方便測試!

記得準備範例圖片到 `examples/` 資料夾。

---

### **[Turn 16] 多頁面架構**

**[User]**: Streamlit 怎麼做多頁面?

**[Agent]**: Streamlit 有內建多頁面功能!

只需在 `pages/` 資料夾創建檔案:

```
pages/
├── 1_📊_About.py      # 第一個頁面
└── 2_🔬_Model_Info.py # 第二個頁面
```

**命名規則**:
- 數字決定順序
- Emoji 顯示圖標
- 底線後是頁面名稱

Streamlit 會自動生成側邊欄導航!

每個檔案都是獨立的 Streamlit app。

---

### **[Turn 17] About 頁面內容**

**[User]**: About 頁面應該寫什麼?

**[Agent]**: 我建議包含:

**專題介紹**:
- 🎯 目標與動機
- 🧠 技術架構
- 🔬 模型原理

**技術說明**:
- 如何運作
- ResNet 介紹
- ImageNet 資料集

**教育價值**:
- 遷移學習
- 部署方法
- 未來擴展

**參考資料**:
- 論文引用
- 文檔連結

這是展現專業度的重要頁面!

---

### **[Turn 18] Model Info 頁面**

**[User]**: Model Info 頁面要放哪些技術細節?

**[Agent]**: 深入的技術資訊:

**1. 架構詳解**:
- 層數結構圖
- 參數統計
- FLOPs 計算

**2. 訓練資訊**:
- 超參數設定
- 資料擴增
- 訓練時程

**3. 效能指標**:
- 準確率數據
- 推論速度
- 模型大小

**4. 程式碼示例**:
- 載入模型
- 預處理
- 推論流程

讓學習者深入了解模型!

---

### **[Turn 19] Requirements.txt 撰寫**

**[User]**: requirements.txt 應該怎麼寫?

**[Agent]**: 列出所有依賴及版本:

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

**注意事項**:
- ⚠️ 固定版本避免相容性問題
- ⚠️ torch 2.1.0 對應 torchvision 0.16.0
- ⚠️ Python 3.9+ 支援所有套件

可以用 `pip freeze > requirements.txt` 自動生成!

---

### **[Turn 20] 本地測試**

**[User]**: 程式寫好了,怎麼在本地測試?

**[Agent]**: 完整測試流程:

```bash
# 1. 安裝依賴
pip install -r requirements.txt

# 2. 運行應用
streamlit run app.py

# 3. 測試功能
```

**測試檢查清單**:
- ✅ 上傳圖片功能
- ✅ 範例圖片按鈕
- ✅ 預測結果正確
- ✅ 圖表正常顯示
- ✅ 多頁面切換
- ✅ 側邊欄互動

首次運行會下載模型 (~98MB),需要等待!

---

### **[Turn 21] 遇到錯誤處理**

**[User]**: 測試時出現 "module not found" 錯誤怎麼辦?

**[Agent]**: 常見的除錯步驟:

**1. 檢查虛擬環境**:
```bash
which python
pip list  # 確認套件已安裝
```

**2. 重新安裝**:
```bash
pip install --upgrade pip
pip install -r requirements.txt --force-reinstall
```

**3. 檢查 Python 版本**:
```bash
python --version  # 應該 >= 3.9
```

**4. 檢查 import 路徑**:
確保 `utils/` 資料夾有 `__init__.py`

還有問題的話提供完整錯誤訊息!

---

### **[Turn 22] 效能優化**

**[User]**: 推論速度有點慢,可以優化嗎?

**[Agent]**: 幾個優化建議:

**1. 使用快取** (已做):
```python
@st.cache_resource  # 模型快取
@st.cache_data      # 標籤快取
```

**2. 降低圖片解析度**:
不影響準確率,可加快處理

**3. 批次推論** (多圖):
```python
img_tensors = torch.stack([transform(img) for img in images])
```

**4. GPU 加速** (選用):
```python
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = model.to(device)
```

**5. TorchScript 編譯**:
```python
model = torch.jit.script(model)
```

CPU 上 2-3 秒已經很快了!

---

### **[Turn 23] README 文件撰寫**

**[User]**: README 應該包含哪些內容?

**[Agent]**: 完整的 README 結構:

**1. 專案標題 + 徽章**
**2. 簡介與動機**
**3. 功能特色列表**
**4. Demo 展示/截圖**
**5. 技術架構說明**
**6. 安裝與運行指南**
**7. 部署教學**
**8. 專案結構樹狀圖**
**9. 使用說明**
**10. 常見問題 FAQ**
**11. 未來擴展方向**
**12. 授權與引用**
**13. 聯絡資訊**

README 是專案的門面,要寫得詳細易懂!

我幫你產生完整版本。

---

### **[Turn 24] 部署到 Streamlit Cloud**

**[User]**: 怎麼部署到 Streamlit Cloud?

**[Agent]**: 超簡單的部署流程:

**步驟 1: 推送到 GitHub**
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/你的帳號/image-classifier-demo.git
git push -u origin main
```

**步驟 2: 登入 Streamlit Cloud**
訪問 https://share.streamlit.io

**步驟 3: 部署**
- 點 "New app"
- 選擇倉庫
- 主檔案: `app.py`
- 點 "Deploy"

**步驟 4: 等待**
首次部署 5-10 分鐘 (下載模型)

完成後會獲得永久網址!

---

### **[Turn 25] GitHub 倉庫設定**

**[User]**: GitHub 倉庫需要特別設定嗎?

**[Agent]**: 幾個建議:

**1. 添加 .gitignore**:
```
__pycache__/
*.pyc
.streamlit/
.DS_Store
*.pth
```

**2. 添加 LICENSE**:
選擇 MIT License (開源友善)

**3. 添加 README.md**:
已經準備好了!

**4. 設定 runtime.txt** (Streamlit Cloud):
```
python-3.9.18
```

**5. 添加截圖**:
`docs/screenshots/` 放 Demo 截圖

**6. 完整的 commit 訊息**:
```bash
git commit -m "feat: add image classification feature"
```

專業的倉庫會加分!

---

### **[Turn 26] 處理大檔案**

**[User]**: 模型權重檔案太大,要推到 GitHub 嗎?

**[Agent]**: **不要推**!原因:

- ❌ GitHub 單檔限制 100MB
- ❌ 倉庫會變很大
- ❌ clone 很慢

**正確做法**:

**1. 讓 torchvision 自動下載**:
```python
model = models.resnet50(pretrained=True)
```
權重會快取在 `~/.cache/torch/hub/`

**2. 添加到 .gitignore**:
```
*.pth
*.pt
*.h5
checkpoints/
```

**3. 說明文件中註明**:
"Models will be automatically downloaded on first run"

Streamlit Cloud 會自動處理!

---

### **[Turn 27] 部署後測試**

**[User]**: 部署成功了!但是運行很慢怎麼辦?

**[Agent]**: Streamlit Cloud 免費版限制:

**資源限制**:
- 1 CPU core
- 1GB RAM
- 閒置後休眠

**優化建議**:

**1. 添加載入提示**:
```python
with st.spinner("Loading model..."):
    model = load_model()
```

**2. 限制圖片大小**:
```python
st.file_uploader(..., max_file_size=5)  # 5MB
```

**3. 壓縮範例圖片**:
減少初始載入時間

**4. 加速提示**:
在 README 說明首次載入較慢

**升級方案**:
付費版提供更多資源,但免費版足夠 Demo 使用!

---

### **[Turn 28] 添加 CSS 美化**

**[User]**: 可以讓介面更漂亮嗎?

**[Agent]**: 當然!使用自定義 CSS:

```python
st.markdown("""
<style>
.main-header {
    font-size: 3rem;
    font-weight: bold;
    text-align: center;
    color: #1f77b4;
}

.prediction-box {
    background-color: #f0f2f6;
    padding: 1.5rem;
    border-radius: 10px;
    margin: 1rem 0;
}

.stButton>button {
    width: 100%;
    border-radius: 5px;
    height: 3em;
}
</style>
""", unsafe_allow_html=True)
```

**美化要點**:
- 🎨 統一配色方案
- 📏 適當留白間距
- 🔤 清晰字體層次
- 📱 響應式設計

美觀但不失專業!

---

### **[Turn 29] 錯誤處理完善**

**[User]**: 使用者可能上傳奇怪的檔案,怎麼處理?

**[Agent]**: 完整的錯誤處理:

```python
try:
    image = Image.open(uploaded_file)
    
    # 檢查格式
    if image.format not in ['JPEG', 'PNG', 'JPG']:
        st.error("❌ Invalid format!")
        return
    
    # 檢查大小
    if image.size[0] < 50 or image.size[1] < 50:
        st.error("❌ Image too small!")
        return
    
    # 轉換色彩空間
    if image.mode != 'RGB':
        image = image.convert('RGB')
    
except Exception as e:
    st.error(f"❌ Error: {str(e)}")
    return
```

**防禦要點**:
- ✅ 格式驗證
- ✅ 尺寸檢查
- ✅ 異常捕獲
- ✅ 友善錯誤訊息

讓應用更穩健!

---

### **[Turn 30] 效能監控**

**[User]**: 可以追蹤推論時間嗎?

**[Agent]**: 簡單的計時器:

```python
import time

start_time = time.time()

# 執行推論
predictions = predict(image, model, labels)

elapsed_time = time.time() - start_time

st.metric("Inference Time", f"{elapsed_time:.2f}s")
```

**更詳細的監控**:
```python
st.sidebar.metric("Model Loaded", "✅")
st.sidebar.metric("Labels Loaded", "✅")
st.sidebar.metric("Cache Status", "Active")
```

可以幫助除錯和展示效能!

---

### **[Turn 31] 文檔撰寫**

**[User]**: 需要寫 Abstract 嗎?

**[Agent]**: 是的!學術格式要求:

**中文摘要** (300字):
- 研究動機
- 方法描述
- 實驗結果
- 主要貢獻
- 未來方向

**英文 Abstract** (300 words):
- Background & Motivation
- Methods & Implementation
- Results & Discussion
- Contributions
- Future Work

我幫你寫好完整版本了!

放在 `docs/ABSTRACT.md`

---

### **[Turn 32] 測試不同圖片**

**[User]**: 測試了一些圖片,準確率不錯!有什麼建議嗎?

**[Agent]**: 很棒!幾個測試建議:

**測試類別多樣性**:
- 🐱 動物 (貓、狗、鳥)
- 🚗 車輛 (汽車、飛機)
- 🍎 食物 (水果、料理)
- 🪑 物品 (家具、工具)
- 🌳 自然 (植物、風景)

**測試邊界情況**:
- 模糊圖片
- 低解析度
- 多個物體
- 遮擋情況
- 不常見角度

**記錄結果**:
在文檔中加入測試案例表格!

---

### **[Turn 33] 準備報告**

**[User]**: 要準備繳交作業了,檢查清單有哪些?

**[Agent]**: 完整檢查清單:

**✅ 程式碼**:
- [ ] app.py 運行正常
- [ ] 所有頁面功能正常
- [ ] 無錯誤訊息
- [ ] 程式碼有適當註解

**✅ 文檔**:
- [ ] README.md 完整
- [ ] ABSTRACT.md 中英文
- [ ] 部署教學清楚
- [ ] 截圖/Demo 影片

**✅ 部署**:
- [ ] GitHub 倉庫公開
- [ ] Streamlit Cloud 運行
- [ ] 網址可訪問
- [ ] 無部署錯誤

**✅ 報告**:
- [ ] 技術架構說明
- [ ] 開發過程紀錄
- [ ] 學習心得
- [ ] 未來展望

全部打勾就可以繳交了!

---

### **[Turn 34] 學習心得分享**

**[User]**: 這個專題讓我學到很多!總結一下?

**[Agent]**: 太好了!你學會了:

**技術能力**:
- ✅ 深度學習模型應用
- ✅ PyTorch 框架使用
- ✅ Streamlit Web 開發
- ✅ Git/GitHub 協作
- ✅ 雲端部署實務

**重要概念**:
- 🧠 遷移學習
- 🖼️ 影像預處理
- 📊 模型推論流程
- 🎨 UI/UX 設計
- 📚 技術文檔撰寫

**軟實力**:
- 問題分析與解決
- 專案規劃能力
- 持續學習精神

這些都是寶貴的經驗!

---

### **[Turn 35] 未來擴展建議**

**[User]**: 完成專題後,還可以怎麼改進?

**[Agent]**: 很多延伸方向:

**短期目標** (1-2週):
- 🔍 加入 Grad-CAM 視覺化
- 📹 支援影片分類
- 🎯 添加更多模型選擇
- 📊 批次處理功能

**中期目標** (1-2月):
- 🏋️ 自定義分類器訓練
- 🎨 物體偵測整合
- 🌐 多語言支援
- 📱 行動版優化

**長期目標** (3+月):
- 🤖 整合其他 AI 模型
- 🔄 即時串流處理
- 🗄️ 資料庫記錄
- 📈 使用統計分析

持續迭代,不斷進步!

---

## 📊 開發統計

| 項目 | 數據 |
|------|------|
| **總對話數** | 35 則 |
| **開發時間** | ~3 天 |
| **代碼行數** | ~800 行 |
| **文件頁數** | ~50 頁 |
| **測試案例** | 15+ 張圖片 |

---

## 💡 關鍵收穫

1. **循序漸進**: 從簡單到複雜,逐步實作
2. **模組化設計**: 程式碼結構清晰易維護
3. **錯誤處理**: 考慮各種邊界情況
4. **文檔重要**: 好的文檔是成功的一半
5. **實務導向**: 理論結合實際應用

---

*此對話紀錄完整呈現從零到一的專題開發過程*
