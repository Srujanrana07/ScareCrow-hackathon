import os
import joblib
import numpy as np
import cv2
# from django.shortcuts import render
# from django.http import JsonResponse
# from django.conf import settings
# from django.views.decorators.csrf import csrf_exempt
# from dotenv import load_dotenv
# import google.generativeai as genai
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

#     chat_session = gemini_model.start_chat(
#         history=[]
#     )

#     response = chat_session.send_message(f"What is the cure for {disease_dict.get(disease_class, 'Unknown')}?")
#     if response:
#         return disease_dict.get(disease_class, "Unknown"), response.text
#     else:
#         return "Unknown", "Cure information not available."

# # View for handling disease prediction without using forms
# @csrf_exempt
# def predict_disease_view(request):
#     if request.method == 'POST' and request.FILES.get('image'):
#         # Get the image from the request
#         uploaded_file = request.FILES['image']
        
#         # Convert the file to a numpy array for OpenCV
#         img_array = np.frombuffer(uploaded_file.read(), np.uint8)
#         image = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

#         # Call the prediction function
#         disease, cure = predict_disease(image)

#         # Return the disease and the cure response
#         return JsonResponse({
#             "disease": disease,
#             "cure": cure
#         })
    
#     return JsonResponse({"error": "Invalid request. Please upload an image."}, status=400)
