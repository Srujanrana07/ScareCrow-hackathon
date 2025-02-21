import joblib
import numpy as np
import cv2
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Adjust if needed

# Load the saved model
model_path = os.path.join(BASE_DIR, 'disease_detector', 'models', 'paddy_image_classifier.joblib')
model = joblib.load(model_path)

def predict_disease(image):
    # Resize the image to match model input size
    img_resized = cv2.resize(image, (224, 224))  # Adjust size as per your model requirements
    img_array = np.expand_dims(img_resized, axis=0)

    # Predict the disease
    prediction = model.predict(img_array)
    disease_class = np.argmax(prediction, axis=1)[0]  # Assuming it's a classification model

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

    return disease_dict.get(disease_class, "Unknown")
