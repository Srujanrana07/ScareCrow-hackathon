import os
import joblib
import numpy as np
import cv2
from .LLM_model import get_gemini_response

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Load the saved model
model_path = os.path.join(BASE_DIR, 'disease_detector', 'models', 'paddy_image_classifier.joblib')
model = joblib.load(model_path)


# Helper function to predict disease
def predict_disease(image):
    img_resized = cv2.resize(image, (224, 224))  
    img_array = np.expand_dims(img_resized, axis=0)

    # Predict the disease
    prediction = model.predict(img_array)
    disease_class = np.argmax(prediction, axis=1)[0] 

    # Map the disease_class to a specific disease
    disease_dict = {
        0: 'paddy_bacterial_leaf_blight',
        1: 'paddy_bacterial_leaf_streak',
        2: 'paddy_bacterial_panicle_blight',
        3: 'paddy_blast',
        4: 'paddy_brown_spot',
        5: 'paddy_dead_heart',
        6: 'paddy_downy_mildew',
        7: 'paddy_hispa',
        8: 'paddy_normal',
        9: 'paddy_tungro'
    }

    disease_name = disease_dict.get(disease_class, "Unknown")

    gemini_response = get_gemini_response(disease_name)

    return disease_name, gemini_response

