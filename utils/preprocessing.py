"""
Image preprocessing utilities
"""
from PIL import Image
import io

def validate_image(uploaded_file):
    """
    Validate uploaded image file
    
    Args:
        uploaded_file: Streamlit UploadedFile object
    
    Returns:
        PIL Image or None if invalid
    """
    try:
        image = Image.open(uploaded_file)
        # Convert to RGB if necessary
        if image.mode != 'RGB':
            image = image.convert('RGB')
        return image
    except Exception as e:
        return None

def resize_for_display(image, max_width=400):
    """
    Resize image for display while maintaining aspect ratio
    
    Args:
        image: PIL Image
        max_width: Maximum width in pixels
    
    Returns:
        Resized PIL Image
    """
    width, height = image.size
    if width > max_width:
        ratio = max_width / width
        new_height = int(height * ratio)
        image = image.resize((max_width, new_height), Image.Resampling.LANCZOS)
    return image
