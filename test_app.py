"""
Test script for the image classifier application
"""
import torch
import torchvision.models as models
from PIL import Image
import sys

def test_pytorch_installation():
    """Test PyTorch installation"""
    print("Testing PyTorch...")
    print(f"PyTorch version: {torch.__version__}")
    print(f"CUDA available: {torch.cuda.is_available()}")
    if torch.cuda.is_available():
        print(f"CUDA version: {torch.version.cuda}")
    print("✓ PyTorch OK\n")

def test_model_loading():
    """Test model loading"""
    print("Testing model loading...")
    try:
        model = models.resnet50(pretrained=True)
        model.eval()
        print(f"Model loaded successfully")
        print(f"Total parameters: {sum(p.numel() for p in model.parameters()):,}")
        print("✓ Model loading OK\n")
        return model
    except Exception as e:
        print(f"✗ Model loading failed: {e}\n")
        return None

def test_inference(model):
    """Test inference with dummy image"""
    print("Testing inference...")
    try:
        # Create dummy image
        dummy_img = Image.new('RGB', (224, 224), color='red')
        
        # Preprocess
        from torchvision import transforms
        transform = transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], 
                               std=[0.229, 0.224, 0.225])
        ])
        
        img_tensor = transform(dummy_img).unsqueeze(0)
        
        # Inference
        with torch.no_grad():
            outputs = model(img_tensor)
            probs = torch.nn.functional.softmax(outputs[0], dim=0)
        
        top_prob, top_idx = torch.topk(probs, 1)
        
        print(f"Inference successful")
        print(f"Top prediction: class {top_idx.item()}, prob {top_prob.item():.4f}")
        print("✓ Inference OK\n")
        return True
    except Exception as e:
        print(f"✗ Inference failed: {e}\n")
        return False

def test_imports():
    """Test all required imports"""
    print("Testing imports...")
    try:
        import streamlit
        import plotly
        import numpy
        import matplotlib
        from PIL import Image
        print("✓ All imports OK\n")
        return True
    except ImportError as e:
        print(f"✗ Import failed: {e}\n")
        return False

def main():
    """Run all tests"""
    print("="*50)
    print("Image Classifier Test Suite")
    print("="*50 + "\n")
    
    # Run tests
    test_imports()
    test_pytorch_installation()
    model = test_model_loading()
    
    if model:
        test_inference(model)
    
    print("="*50)
    print("All tests completed!")
    print("="*50)

if __name__ == "__main__":
    main()
