# 專題摘要 / Abstract

## 中文摘要

本專題實作了一個基於深度學習的即時影像分類系統,旨在展示卷積神經網路在電腦視覺領域的實際應用。研究動機源自於深度學習技術在影像辨識任務上的突破性進展,以及將學術研究成果轉化為實用應用程式的需求。本系統採用 ResNet50 深度殘差網路作為核心分類模型,該模型預訓練於包含 120 萬張圖片的 ImageNet 大型視覺資料庫,能夠辨識 1000 種不同類別的物體。

在技術實現方面,本專題運用遷移學習技術,直接使用預訓練模型進行推論,無需額外訓練即可達到高準確率。系統架構採用 PyTorch 深度學習框架處理模型推論,搭配 Streamlit Web 框架建構互動式使用者介面。影像預處理流程包含尺寸調整、中心裁切與標準化正規化,確保輸入符合模型要求。系統實作了完整的前後端整合,支援即時圖片上傳、批次推論與結果視覺化展示。

實驗結果顯示,本系統在標準 CPU 環境下單張圖片推論時間約 2-3 秒,能夠提供前五名預測結果與對應信心分數。系統成功部署於 Streamlit Community Cloud 平台,實現了雲端化的 AI 服務。使用者介面設計注重直觀性與教育性,除了主要分類功能外,另提供模型技術資訊與專題說明頁面,有助於學習者理解深度學習模型的運作原理。

本專題的主要貢獻在於展示了如何將前沿深度學習技術轉化為可部署的實用應用,證明了遷移學習在降低 AI 應用開發門檻的有效性。系統採用輕量化設計,無需 GPU 硬體即可運行,大幅提升了可及性。未來可延伸方向包括：整合 Grad-CAM 視覺化技術解釋模型決策過程、支援即時影片串流分類、實作自定義分類器微調功能,以及擴展至物體偵測與語義分割等進階電腦視覺任務。本專題不僅是技術實作練習,更是連結理論與實務的重要橋樑,為後續深入研究奠定基礎。

**關鍵字**: 深度學習、影像分類、ResNet、遷移學習、Streamlit、電腦視覺

---

## English Abstract

This project implements a real-time image classification system based on deep learning, aiming to demonstrate the practical application of convolutional neural networks in computer vision. The research motivation stems from the breakthrough progress of deep learning technology in image recognition tasks and the need to transform academic research results into practical applications. The system employs ResNet50, a deep residual network, as the core classification model. This model is pretrained on ImageNet, a large-scale visual database containing 1.2 million images, capable of recognizing 1000 different object categories.

In terms of technical implementation, this project utilizes transfer learning techniques, directly using pretrained models for inference without requiring additional training while achieving high accuracy. The system architecture adopts the PyTorch deep learning framework for model inference, combined with the Streamlit web framework to construct an interactive user interface. The image preprocessing pipeline includes resizing, center cropping, and standardized normalization to ensure inputs meet model requirements. The system implements complete frontend-backend integration, supporting real-time image upload, batch inference, and result visualization.

Experimental results demonstrate that the system achieves single-image inference time of approximately 2-3 seconds in standard CPU environments, providing top-5 predictions with corresponding confidence scores. The system has been successfully deployed on the Streamlit Community Cloud platform, achieving cloud-based AI services. The user interface design emphasizes intuitiveness and educational value. Beyond the main classification functionality, it provides additional pages for model technical information and project description, helping learners understand the operating principles of deep learning models.

The main contribution of this project lies in demonstrating how to transform cutting-edge deep learning technology into deployable practical applications, proving the effectiveness of transfer learning in lowering the barriers to AI application development. The system adopts a lightweight design that can run without GPU hardware, significantly improving accessibility. Future extension directions include: integrating Grad-CAM visualization techniques to explain model decision-making processes, supporting real-time video stream classification, implementing custom classifier fine-tuning functionality, and expanding to advanced computer vision tasks such as object detection and semantic segmentation. This project is not only a technical implementation exercise but also an important bridge connecting theory and practice, laying the foundation for subsequent in-depth research.

**Keywords**: Deep Learning, Image Classification, ResNet, Transfer Learning, Streamlit, Computer Vision

---

## 研究亮點 / Research Highlights

### 技術創新點
1. ✅ **遷移學習應用**: 有效運用預訓練模型,大幅縮短開發時程
2. ✅ **CPU 優化**: 無需昂貴 GPU 硬體即可部署,降低使用門檻
3. ✅ **端到端整合**: 完整實現從模型推論到 Web 介面的全流程
4. ✅ **教育導向設計**: 提供豐富技術文檔,兼具實用與教學價值

### 實用價值
- 📱 **即時推論**: 上傳圖片後 2-3 秒內獲得結果
- 🌐 **雲端部署**: 支援 Streamlit Cloud 一鍵部署
- 📊 **視覺化展示**: 直觀的圖表呈現預測機率分佈
- 🔧 **易於擴展**: 模組化設計便於替換模型或新增功能

### 學術貢獻
- 📚 展示深度學習在實務應用的完整工作流程
- 🎓 提供開源教學範例,促進 AI 教育普及
- 🔬 驗證遷移學習在影像分類任務的有效性
- 💡 為後續研究提供可複製的基準實作

---

## 專題規格 / Project Specifications

| 項目 | 規格 |
|------|------|
| **模型** | ResNet50 (25.6M parameters) |
| **資料集** | ImageNet ILSVRC2012 (1000 classes) |
| **準確率** | Top-1: 76.1% / Top-5: 92.9% |
| **推論速度** | ~2-3s per image (CPU) |
| **框架** | PyTorch 2.1.0 + Streamlit 1.30.0 |
| **部署平台** | Streamlit Cloud / Local / Docker |
| **輸入格式** | JPG, PNG, JPEG (max 200MB) |
| **輸出** | Top-K predictions + confidence scores |

---

## 引用格式 / Citation

如在研究中使用本專題,請引用:

```bibtex
@misc{taica_image_classifier_2024,
  title={AI Image Classifier: A ResNet50-based Deep Learning Demo},
  author={Your Name},
  year={2024},
  publisher={Taica AIGC Project},
  howpublished={\url{https://github.com/your-username/image-classifier-demo}}
}
```

---

*本摘要撰寫遵循學術論文格式,包含研究動機、方法、結果與貢獻等要素*
