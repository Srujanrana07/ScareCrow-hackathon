import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

# Load the dataset
# Change this to your actual dataset
data = pd.read_csv('disease_detector\dataset\Crop_recommendation.csv')

# Separate features and target variable
# Ensure 'label' is the column containing crop names
X = data.drop(columns=['label'])
y = data['label']

# Encode the target labels
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y_encoded, test_size=0.2, random_state=42)

# Train a RandomForest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Make predictions and evaluate
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'Model Accuracy: {accuracy * 100:.2f}%')

# Save the trained model
joblib.dump(model, 'disease_detector/models/crop_recommendation_model.pkl')

# Save the label encoder
joblib.dump(label_encoder, 'disease_detector/models/label_encoder.pkl')

print('Model and Label Encoder saved successfully!')

# Test with a new input
test_case = pd.DataFrame({
    'N': [69],
    'P': [55],
    'K': [38],
    'temperature': [22.7],
    'humidity': [82.6],
    'ph': [5.7],
    'rainfall': [271.3]
})

# Predict crop
prediction_encoded = model.predict(test_case)
prediction_label = label_encoder.inverse_transform(prediction_encoded)

print('Predicted Crop:', prediction_label[0])

def guass():
    test_case = pd.DataFrame({
        'N': [69],
        'P': [55],
        'K': [38],
        'temperature': [22.7],
        'humidity': [82.6],
        'ph': [5.7],
        'rainfall': [271.3]
    })
    # Predict crop
    prediction_encoded = model.predict(test_case)
    prediction_label = label_encoder.inverse_transform(prediction_encoded)

    print('Predicted Crop:', prediction_label[0])

guass()