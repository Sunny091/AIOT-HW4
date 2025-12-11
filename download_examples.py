"""
Download example images for testing
"""
import requests
from PIL import Image
from io import BytesIO
import os

def download_image(url, save_path):
    """Download image from URL and save"""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        img = Image.open(BytesIO(response.content))
        img = img.convert('RGB')
        img.save(save_path)
        print(f"✓ Downloaded: {save_path}")
        return True
    except Exception as e:
        print(f"✗ Failed to download {save_path}: {e}")
        return False

def main():
    """Download example images"""
    
    # Create examples directory
    os.makedirs('examples', exist_ok=True)
    
    # Example image URLs (use free stock photos)
    examples = {
        'cat.jpg': 'https://placekitten.com/400/300',
        'dog.jpg': 'https://placedog.net/400/300',
        'car.jpg': 'https://loremflickr.com/400/300/car'
    }
    
    print("Downloading example images...")
    print("-" * 50)
    
    for filename, url in examples.items():
        save_path = os.path.join('examples', filename)
        download_image(url, save_path)
    
    print("-" * 50)
    print("✓ All example images downloaded!")
    print("\nAlternatively, you can manually add your own images to the examples/ folder.")

if __name__ == "__main__":
    main()
