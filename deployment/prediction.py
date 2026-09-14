# Import Libraries
import streamlit as st
import numpy as np
import tensorflow as tf
from PIL import Image

# Load CNN Model (format .h5)
model = tf.keras.models.load_model("model_cnn.h5")

# Setting the image size
img_height = 350
img_width = 350

# Class names
class_names = ["No Wildfire", "Wildfire"]  # 0 = No Wildfire, 1 = Wildfire

def preprocess_image(image):
    """Fungsi untuk memproses gambar agar sesuai dengan input model."""
    image = image.resize((img_width, img_height))  
    image = np.array(image) / 255.0  
    image = np.expand_dims(image, axis=0)  
    return image

def predict_image(image):
    """Fungsi untuk melakukan prediksi pada gambar yang sudah diproses."""
    processed_img = preprocess_image(image)
    prediction = model.predict(processed_img)[0][0]  # Take the prediction result
    
    if prediction >= 0.5:
        result = class_names[1]  # For Wildfire
    else:
        result = class_names[0]  # For No Wildfire
    
    return result, prediction

def main():
    st.title("Predict Wildfire Area")
    
    # Upload Gambar
    uploaded_file = st.file_uploader("Choose image", type=["jpg", "png", "jpeg"])
    
    if uploaded_file is not None:
        # Tampilkan gambar
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        
        # Prediksi saat tombol ditekan
        if st.button("Prediction"):
            result, confidence = predict_image(image)
            st.write(f"**Prediction Result:** {result}")

if __name__ == "__main__":
    main()
