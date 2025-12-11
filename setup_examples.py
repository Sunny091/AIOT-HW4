"""
Download example images for testing the classifier
"""
import requests
from PIL import Image
from io import BytesIO
import os

def download_image(url, save_path):
    """Download and save image from URL"""
    try:
        print(f"Downloading {save_path}...")
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        # Open and convert to RGB
        img = Image.open(BytesIO(response.content))
        img = img.convert('RGB')
        
        # Resize to reasonable size (save space)
        img.thumbnail((800, 800), Image.Resampling.LANCZOS)
        
        # Save as JPEG
        img.save(save_path, 'JPEG', quality=85)
        print(f"✓ Saved: {save_path}")
        return True
    except Exception as e:
        print(f"✗ Failed to download {save_path}: {e}")
        return False

def main():
    """Download example images"""
    
    # Create examples directory
    os.makedirs('examples', exist_ok=True)
    
    # Example URLs - using Unsplash free images
    examples = {
        'cat.jpg': 'https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba?w=800&q=80',
        'dog.jpg': 'https://images.unsplash.com/photo-1587300003388-59208cc962cb?w=800&q=80',
        'car.jpg': 'https://images.unsplash.com/photo-1494976388531-d1058494cdd8?w=800&q=80'
    }
    
    print("="*50)
    print("Downloading example images...")
    print("="*50)
    
    success_count = 0
    for filename, url in examples.items():
        save_path = os.path.join('examples', filename)
        if download_image(url, save_path):
            success_count += 1
    
    print("="*50)
    print(f"✓ Downloaded {success_count}/{len(examples)} images successfully!")
    print("="*50)
    
    if success_count == len(examples):
        print("\n✅ All example images ready!")
        print("You can now run: streamlit run app.py")
    else:
        print("\n⚠️ Some downloads failed. You can:")
        print("1. Run this script again")
        print("2. Manually add images to the examples/ folder")

if __name__ == "__main__":
    main()
