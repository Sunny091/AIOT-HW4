"""
Model Information Page - Technical Details
"""
import streamlit as st
import torch
import torchvision.models as models

st.set_page_config(
    page_title="Model Info - Image Classifier",
    page_icon="🔬",
    layout="wide"
)

st.title("🔬 Model Technical Information")

# Model Architecture
st.header("🏗️ ResNet50 Architecture")

st.markdown("""
## Network Structure

ResNet50 consists of:
- **1 Convolutional Layer** (7×7, stride 2)
- **1 Max Pooling Layer** (3×3, stride 2)
- **16 Residual Blocks** organized in 4 stages
- **1 Global Average Pooling Layer**
- **1 Fully Connected Layer** (1000 classes)

### Detailed Layer Breakdown
""")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Input Stage")
    st.code("""
Input: 224×224×3 RGB Image
↓
Conv1: 7×7, 64 filters, stride=2
↓
BatchNorm + ReLU
↓
MaxPool: 3×3, stride=2
    """, language="text")
    
    st.subheader("Stage 1 (Conv2_x)")
    st.code("""
3 × Bottleneck Blocks
- 1×1, 64
- 3×3, 64
- 1×1, 256
Output: 56×56×256
    """, language="text")
    
    st.subheader("Stage 2 (Conv3_x)")
    st.code("""
4 × Bottleneck Blocks
- 1×1, 128
- 3×3, 128
- 1×1, 512
Output: 28×28×512
    """, language="text")

with col2:
    st.subheader("Stage 3 (Conv4_x)")
    st.code("""
6 × Bottleneck Blocks
- 1×1, 256
- 3×3, 256
- 1×1, 1024
Output: 14×14×1024
    """, language="text")
    
    st.subheader("Stage 4 (Conv5_x)")
    st.code("""
3 × Bottleneck Blocks
- 1×1, 512
- 3×3, 512
- 1×1, 2048
Output: 7×7×2048
    """, language="text")
    
    st.subheader("Output Stage")
    st.code("""
Global Average Pooling
↓
Fully Connected: 2048 → 1000
↓
Softmax
↓
1000 class probabilities
    """, language="text")

# Load model for inspection
st.header("📊 Model Statistics")

with st.spinner("Loading model..."):
    model = models.resnet50(pretrained=True)

# Count parameters
total_params = sum(p.numel() for p in model.parameters())
trainable_params = sum(p.numel() for p in model.parameters() if p.requires_grad)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Parameters", f"{total_params:,}")

with col2:
    st.metric("Trainable Parameters", f"{trainable_params:,}")

with col3:
    st.metric("Model Size", f"{total_params * 4 / (1024**2):.1f} MB")

# Show model structure
st.header("🔍 Detailed Model Structure")

with st.expander("Click to view full model architecture"):
    st.code(str(model), language="text")

# Performance metrics
st.header("📈 Performance Metrics")

col1, col2 = st.columns(2)

with col1:
    st.subheader("ImageNet Validation Results")
    st.markdown("""
    | Metric | Value |
    |--------|-------|
    | Top-1 Accuracy | 76.13% |
    | Top-5 Accuracy | 92.86% |
    | Inference Time (CPU) | ~50ms |
    | Inference Time (GPU) | ~5ms |
    """)

with col2:
    st.subheader("Model Characteristics")
    st.markdown("""
    | Property | Value |
    |----------|-------|
    | Input Size | 224×224×3 |
    | Layers | 50 |
    | Blocks | 16 Residual |
    | FLOPs | ~4.1 Billion |
    """)

# Training details
st.header("🎓 Training Details")

st.markdown("""
### Original Training Configuration

**Dataset**: ImageNet ILSVRC 2012
- Training Images: 1,281,167
- Validation Images: 50,000
- Classes: 1000

**Hyperparameters**:
- Optimizer: SGD with momentum (0.9)
- Learning Rate: 0.1 (with decay)
- Batch Size: 256
- Weight Decay: 0.0001
- Epochs: 90

**Data Augmentation**:
- Random resized crop (224×224)
- Random horizontal flip
- Color jitter
- Normalization (ImageNet mean/std)

**Hardware**:
- GPUs: 8× NVIDIA GPUs
- Training Time: ~1 week
""")

# Preprocessing details
st.header("🔧 Preprocessing Pipeline")

st.code("""
from torchvision import transforms

transform = transforms.Compose([
    transforms.Resize(256),           # Resize shorter side to 256
    transforms.CenterCrop(224),       # Crop center 224×224
    transforms.ToTensor(),            # Convert to [0,1] tensor
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],  # ImageNet mean
        std=[0.229, 0.224, 0.225]     # ImageNet std
    )
])
""", language="python")

# Implementation details
st.header("💻 Implementation Code")

st.subheader("Model Loading")
st.code("""
import torch
import torchvision.models as models

# Load pretrained model
model = models.resnet50(pretrained=True)
model.eval()  # Set to evaluation mode

# Move to device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = model.to(device)
""", language="python")

st.subheader("Inference")
st.code("""
# Preprocess image
img_tensor = transform(image).unsqueeze(0).to(device)

# Forward pass
with torch.no_grad():
    outputs = model(img_tensor)
    probabilities = torch.nn.functional.softmax(outputs[0], dim=0)

# Get top predictions
top_probs, top_indices = torch.topk(probabilities, k=5)
""", language="python")

# References
st.header("📚 Academic References")

st.markdown("""
### Key Papers

1. **Original ResNet Paper**  
   He, K., Zhang, X., Ren, S., & Sun, J. (2016).  
   *Deep Residual Learning for Image Recognition.*  
   IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2016.  
   [arXiv:1512.03385](https://arxiv.org/abs/1512.03385)

2. **ImageNet Challenge**  
   Russakovsky, O., et al. (2015).  
   *ImageNet Large Scale Visual Recognition Challenge.*  
   International Journal of Computer Vision (IJCV), 115(3), 211-252.

3. **Batch Normalization**  
   Ioffe, S., & Szegedy, C. (2015).  
   *Batch Normalization: Accelerating Deep Network Training.*  
   International Conference on Machine Learning (ICML), 2015.

### Additional Resources

- [PyTorch ResNet Documentation](https://pytorch.org/vision/stable/models.html#resnet)
- [Original Implementation](https://github.com/KaimingHe/deep-residual-networks)
- [Papers With Code - ResNet](https://paperswithcode.com/method/resnet)
""")

st.markdown("---")
st.info("💡 **Tip**: This page provides technical details for understanding the model. Return to the main page to try image classification!")
