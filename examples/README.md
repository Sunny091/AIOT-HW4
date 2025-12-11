# 📸 Example Images

這個資料夾包含用於測試 AI Image Classifier 的範例圖片。

## 當前範例

- **cat.jpg** - 貓咪圖片（用於測試動物分類）
- **dog.jpg** - 狗狗圖片（用於測試動物分類）
- **car.jpg** - 汽車圖片（用於測試車輛分類）

## 圖片來源

所有範例圖片來自 [Unsplash](https://unsplash.com/) - 免費可商用的高品質照片。

## 如何添加更多範例

### 方法一：手動添加

1. 準備你的圖片（JPG、PNG 格式）
2. 將圖片複製到 `examples/` 資料夾
3. 在 `app.py` 中更新 `example_images` 字典：

```python
example_images = {
    "Cat": "examples/cat.jpg",
    "Dog": "examples/dog.jpg",
    "Car": "examples/car.jpg",
    "Your Image": "examples/your_image.jpg"  # 添加新圖片
}
```

### 方法二：使用下載腳本

修改 `setup_examples.py` 添加更多 URL：

```python
examples = {
    'cat.jpg': 'YOUR_IMAGE_URL',
    'dog.jpg': 'YOUR_IMAGE_URL',
    'car.jpg': 'YOUR_IMAGE_URL',
    'new_image.jpg': 'YOUR_NEW_IMAGE_URL'  # 添加新的
}
```

然後執行：
```bash
python setup_examples.py
```

## 建議的測試類別

以下是一些適合測試的 ImageNet 類別：

### 動物類
- 🐱 貓咪 (tabby cat, Persian cat)
- 🐕 狗狗 (golden retriever, German shepherd)
- 🐘 大象 (African elephant)
- 🦁 獅子 (lion)
- 🐻 熊 (brown bear)

### 車輛類
- 🚗 汽車 (sports car, convertible)
- 🚕 計程車 (taxi)
- 🚌 公車 (school bus)
- ✈️ 飛機 (airliner)
- 🚢 船隻 (container ship)

### 食物類
- 🍎 水果 (strawberry, orange)
- 🍕 食物 (pizza, hamburger)
- 🍰 甜點 (ice cream, chocolate cake)

### 物品類
- ⌚ 手錶 (digital watch)
- 💻 電腦 (laptop, desktop)
- 📱 手機 (cellular telephone)
- 🎸 樂器 (acoustic guitar, piano)

### 自然景觀
- 🌳 植物 (oak tree, daisy)
- 🏔️ 地形 (mountain, volcano)
- 🌊 水景 (seashore, lakeside)

## 圖片要求

- **格式**: JPG、PNG、JPEG
- **大小**: 建議 < 5MB（自動調整大小）
- **解析度**: 任意（會自動調整為 224x224）
- **內容**: 清晰的主體，避免多個物體

## 測試建議

1. ✅ 使用清晰、主體明確的圖片
2. ✅ 測試不同角度和背景
3. ✅ 嘗試 ImageNet 包含的 1000 個類別
4. ❌ 避免模糊或低品質圖片
5. ❌ 避免包含多個主要物體的圖片

## 授權說明

本專案使用的範例圖片來自 Unsplash，採用 [Unsplash License](https://unsplash.com/license)：
- ✅ 可自由使用
- ✅ 可商業使用
- ✅ 無需署名（但建議）

---

*如需更多資訊，請參考 [README.md](../README.md)*
