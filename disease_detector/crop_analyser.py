import joblib
import pandas as pd

print("Loading the model and encoder...")

# Load the saved model
model = joblib.load(r'disease_detector\models\crop_recommendation_model.pkl')

# Load the label encoder (assuming you saved it during training)
label_encoder = joblib.load(r'disease_detector\models\label_encoder.pkl')

print("Model and encoder loaded successfully!")

# Define the test case with feature names
test_case = pd.DataFrame({
    'N': [69],
    'P': [55],
    'K': [38],
    'temperature': [22.7],
    'humidity': [82.6],
    'ph': [5.7],
    'rainfall': [271.3]
})

print("Predicting the crop...")

# Predict using the model
prediction_encoded = model.predict(test_case)

# Decode the prediction to get the crop name
prediction_label = label_encoder.inverse_transform(prediction_encoded)

print("Prediction completed!")

# Output the result
print("Predicted Crop:", prediction_label[0])

def predict_crop(model, label_encoder, N, P, K, temperature, humidity, ph, rainfall):
    test_case = pd.DataFrame({
        'N': [N],
        'P': [P],
        'K': [K],
        'temperature': [temperature],
        'humidity': [humidity],
        'ph': [ph],
        'rainfall': [rainfall]
    })
    
    prediction_encoded = model.predict(test_case)
    prediction_label = label_encoder.inverse_transform(prediction_encoded)
    
    return prediction_label[0]

# Example usage after defining the function
predicted_crop = predict_crop(model, label_encoder, 69, 55, 38, 22.7, 82.6, 5.7, 271.3)
print("Predicted Crop:", predicted_crop)

def fun_call(N, P, K, temperature, humidity, ph, rainfall):
    predicted_crop = predict_crop(model, label_encoder, N, P, K, temperature, humidity, ph, rainfall)
    return predicted_crop
    # print("Function called successfully!")
    # print("Predicted Crop:", predicted_crop)

    