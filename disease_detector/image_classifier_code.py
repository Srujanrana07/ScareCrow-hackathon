import joblib
import numpy as np
import cv2

# Load your trained model
model = joblib.load('model.joblib')

# Provide the image file path
image_file = "data/paddy_downy_mildew/100017.jpg"
def predict_disease(image_file):
    
# Read the image from the file
    img = cv2.imread(image_file)

    # Check if the image was loaded properly
    if img is None:
        raise FileNotFoundError(f"Could not load image from {image_file}")

    # Resize the image to match model input size
    img_resized = cv2.resize(img, (224, 224))  # Adjust size as per your model requirements
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

    disease_name = disease_dict.get(disease_class, "Unknown")
    print(f"Predicted Disease: {disease_name}")
    return disease_name