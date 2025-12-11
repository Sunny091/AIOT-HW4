"""
Streamlit Image Classifier Demo
Using ResNet50 pretrained on ImageNet
"""
import streamlit as st
import plotly.graph_objects as go
from PIL import Image
import os

from utils.model import load_model, load_imagenet_labels, predict
from utils.preprocessing import validate_image, resize_for_display

# Page configuration
st.set_page_config(
    page_title="Image Classifier Demo",
    page_icon="🖼️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        color: #1f77b4;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.2rem;
        text-align: center;
        color: #666;
        margin-bottom: 2rem;
    }
    .prediction-box {
        background-color: #f0f2f6;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<p class="main-header">🖼️ AI Image Classifier</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Powered by ResNet50 Deep Learning Model</p>', unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.header("⚙️ Settings")
    top_k = st.slider("Number of predictions to show", min_value=1, max_value=10, value=5)
    
    st.markdown("---")
    st.header("📖 Instructions")
    st.markdown("""
    1. Upload an image (JPG, PNG, JPEG)
    2. Wait for the model to process
    3. View top predictions and confidence scores
    
    **Supported formats:** JPG, PNG, JPEG  
    **Max file size:** 200MB
    """)
    
    st.markdown("---")
    st.header("ℹ️ About")
    st.info("""
    This demo uses **ResNet50**, a 50-layer deep convolutional neural network 
    pretrained on ImageNet dataset (1000 classes).
    
    **Model:** ResNet50  
    **Dataset:** ImageNet  
    **Classes:** 1000 categories
    """)

# Main content
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📤 Upload Image")
    
    # File uploader
    uploaded_file = st.file_uploader(
        "Choose an image file",
        type=['jpg', 'jpeg', 'png'],
        help="Upload an image to classify"
    )
    
    # Example images
    st.markdown("### 🎯 Or try example images:")
    example_images = {
        "Cat": "examples/cat.jpg",
        "Dog": "examples/dog.jpg",
        "Car": "examples/car.jpg"
    }
    
    example_cols = st.columns(3)
    for idx, (name, path) in enumerate(example_images.items()):
        with example_cols[idx]:
            if st.button(f"Try {name}", key=f"example_{name}"):
                if os.path.exists(path):
                    uploaded_file = path

with col2:
    st.subheader("🔍 Classification Results")

# Processing
if uploaded_file is not None:
    # Load and validate image
    if isinstance(uploaded_file, str):
        # Example image
        image = Image.open(uploaded_file)
    else:
        # Uploaded image
        image = validate_image(uploaded_file)
    
    if image is None:
        st.error("❌ Invalid image file. Please upload a valid image.")
    else:
        # Display image
        with col1:
            st.image(image, caption="Uploaded Image", use_column_width=True)
        
        # Load model and predict
        with st.spinner("🔄 Loading model and analyzing image..."):
            model = load_model()
            labels = load_imagenet_labels()
            predictions = predict(image, model, labels, top_k=top_k)
        
        # Display results
        with col2:
            st.success("✅ Classification complete!")
            
            # Top prediction highlight
            top_label, top_prob = predictions[0]
            st.markdown(f"""
            <div class="prediction-box">
                <h3>🏆 Top Prediction</h3>
                <h2>{top_label}</h2>
                <h3>{top_prob*100:.2f}% confidence</h3>
            </div>
            """, unsafe_allow_html=True)
            
            # All predictions table
            st.markdown("### 📊 All Predictions")
            for i, (label, prob) in enumerate(predictions):
                st.write(f"**{i+1}. {label}** - {prob*100:.2f}%")
                st.progress(prob)
            
            # Visualization
            st.markdown("### 📈 Probability Distribution")
            
            labels_list = [pred[0] for pred in predictions]
            probs_list = [pred[1] for pred in predictions]
            
            fig = go.Figure(data=[
                go.Bar(
                    x=probs_list,
                    y=labels_list,
                    orientation='h',
                    marker=dict(
                        color=probs_list,
                        colorscale='Blues',
                        showscale=False
                    )
                )
            ])
            
            fig.update_layout(
                title=f"Top {top_k} Predictions",
                xaxis_title="Probability",
                yaxis_title="Class",
                height=400,
                yaxis={'categoryorder': 'total ascending'}
            )
            
            st.plotly_chart(fig, use_container_width=True)

else:
    with col2:
        st.info("👈 Please upload an image or select an example to begin classification.")
        st.markdown("""
        ### What this model can recognize:
        
        - **Animals**: cats, dogs, birds, fish, insects
        - **Vehicles**: cars, trucks, airplanes, boats
        - **Objects**: furniture, electronics, tools
        - **Food**: fruits, vegetables, dishes
        - **Nature**: plants, flowers, landscapes
        
        *And 990+ more categories!*
        """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666;'>
    <p>🎓 Taica AIGC Project | Built with Streamlit & PyTorch</p>
    <p>Model: ResNet50 pretrained on ImageNet</p>
</div>
""", unsafe_allow_html=True)
