"""
Model loading and inference utilities
"""
import torch
import torchvision.models as models
from torchvision.models import ResNet50_Weights
import torchvision.transforms as transforms
from PIL import Image
import json
import requests
import streamlit as st

@st.cache_resource
def load_model():
    """Load pretrained ResNet50 model"""
    # Use new weights parameter (PyTorch 2.5+)
    model = models.resnet50(weights=ResNet50_Weights.DEFAULT)
    model.eval()
    
    # Disable gradient computation to save memory
    for param in model.parameters():
        param.requires_grad = False
    
    return model

@st.cache_data
def load_imagenet_labels():
    """Load ImageNet class labels"""
    url = "https://raw.githubusercontent.com/anishathalye/imagenet-simple-labels/master/imagenet-simple-labels.json"
    try:
        response = requests.get(url)
        labels = response.json()
        return labels
    except:
        # Fallback to basic labels
        return [f"class_{i}" for i in range(1000)]

def get_image_transforms():
    """Get standard ImageNet preprocessing transforms"""
    return transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(
            mean=[0.485, 0.456, 0.406],
            std=[0.229, 0.224, 0.225]
        )
    ])

def predict(image, model, labels, top_k=5):
    """
    Perform inference on image
    
    Args:
        image: PIL Image
        model: PyTorch model
        labels: List of class labels
        top_k: Number of top predictions to return
    
    Returns:
        predictions: List of (label, probability) tuples
    """
    transform = get_image_transforms()
    
    # Preprocess image
    img_tensor = transform(image).unsqueeze(0)
    
    # Inference
    with torch.no_grad():
        outputs = model(img_tensor)
        probabilities = torch.nn.functional.softmax(outputs[0], dim=0)
    
    # Get top-k predictions
    top_probs, top_indices = torch.topk(probabilities, top_k)
    
    predictions = []
    for prob, idx in zip(top_probs, top_indices):
        label = labels[idx.item()]
        predictions.append((label, prob.item()))
    
    return predictions
