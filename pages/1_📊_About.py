"""
About Page - Project Information
"""
import streamlit as st

st.set_page_config(
    page_title="About - Image Classifier",
    page_icon="📊",
    layout="wide"
)

st.title("📊 About This Project")

st.markdown("""
## 🎯 Project Overview

This is an **AI-powered image classification system** built as part of the Taica AIGC course project. 
The system leverages deep learning to automatically recognize and categorize objects in images.

---

## 🧠 Technical Architecture

### Deep Learning Model
- **Model Name**: ResNet50 (Residual Network with 50 layers)
- **Architecture**: Deep Convolutional Neural Network (CNN)
- **Parameters**: 25.6 million trainable parameters
- **Training Dataset**: ImageNet (1.2 million images, 1000 classes)
- **Accuracy**: ~76% Top-1, ~93% Top-5 on ImageNet validation set

### Key Technologies
- **Framework**: PyTorch 2.1.0
- **Frontend**: Streamlit 1.30.0
- **Image Processing**: torchvision, Pillow
- **Visualization**: Plotly, Matplotlib

---

## 🔬 How It Works

### 1. Image Preprocessing
```
User Upload → Resize to 256x256 → Center Crop to 224x224 → Normalize
```

### 2. Model Inference
```
Preprocessed Image → ResNet50 CNN → 1000-dimensional output → Softmax → Probabilities
```

### 3. Result Display
```
Top-K Predictions → Confidence Scores → Visualization
```

---

## 📚 What is ResNet?

**ResNet (Residual Network)** is a groundbreaking deep learning architecture introduced in 2015 by Microsoft Research.

### Key Innovation: Skip Connections
ResNet introduced "skip connections" that allow gradients to flow directly through the network, 
enabling training of much deeper networks (50, 101, even 152 layers).

### Architecture Highlights
- **Residual Blocks**: Each block learns residual functions
- **Batch Normalization**: Stabilizes training
- **Global Average Pooling**: Reduces overfitting
- **No Fully Connected Layers**: Except final classification layer

---

## 🌐 ImageNet Dataset

ImageNet is one of the largest image databases in computer vision:
- **Images**: 14+ million labeled images
- **Classes**: 20,000+ categories
- **Subset for classification**: 1000 classes (ILSVRC)

Our model is trained on the 1000-class subset, which includes:
- Animals (mammals, birds, reptiles, insects)
- Vehicles (cars, planes, ships)
- Household objects (furniture, appliances)
- Food items (fruits, dishes)
- Natural objects (plants, landscapes)

---

## 🎓 Educational Value

This project demonstrates:

1. **Transfer Learning**: Using pre-trained models for new tasks
2. **Deep Learning Deployment**: Converting research models to production apps
3. **Computer Vision**: Practical image recognition applications
4. **Full-Stack AI**: From model to user interface

---

## 🚀 Future Enhancements

Potential improvements for this system:

- ✅ Custom model training for specific domains
- ✅ Real-time video classification
- ✅ Multi-label classification
- ✅ Object detection with bounding boxes
- ✅ Explainable AI (Grad-CAM visualizations)
- ✅ Mobile app deployment

---

## 👥 Credits

**Developer**: Taica AIGC Student  
**Course**: Taiwan AI Collegiate Alliance (Taica)  
**Semester**: Fall 2024  
**Framework**: Streamlit + PyTorch

---

## 📖 References

1. He, K., et al. (2016). "Deep Residual Learning for Image Recognition." CVPR 2016.
2. Deng, J., et al. (2009). "ImageNet: A Large-Scale Hierarchical Image Database." CVPR 2009.
3. PyTorch Documentation: https://pytorch.org/
4. Streamlit Documentation: https://docs.streamlit.io/

---

## 📧 Contact

For questions or collaboration:
- GitHub: [Your GitHub]
- Email: [Your Email]
- Course Website: https://taicatw.net/

---

*Built with ❤️ for AI education*
""")

st.markdown("---")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Model Parameters", "25.6M")

with col2:
    st.metric("ImageNet Classes", "1000")

with col3:
    st.metric("Top-5 Accuracy", "93%")
