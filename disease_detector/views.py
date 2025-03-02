from django.shortcuts import render
from django.http import JsonResponse
import json
from .crop_analyser import fun_call  # Import the function
from .image_classifier_code import predict_disease
from .LLM_model import get_chatbot_response, get_gemini_response
from django.views.decorators.csrf import csrf_exempt
import numpy as np
import cv2

def home(request):
    return render(request, 'index.html')

@csrf_exempt  # Disable CSRF for testing (Not recommended for production)
def predict_crop_view(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)

            # Extract input values
            N = float(data["N"])
            P = float(data["P"])
            K = float(data["K"])
            temperature = float(data["temperature"])
            humidity = float(data["humidity"])
            ph = float(data["ph"])
            rainfall = float(data["rainfall"])

            # Call the crop prediction function
            predicted_crop = fun_call(N, P, K, temperature, humidity, ph, rainfall)

            print("Predicted Crop:", predicted_crop) 
            return JsonResponse({"result": predicted_crop})  # Ensure output is sent correctly

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "Invalid request method"}, status=405)


def index2(request):
    return render(request, 'index2.html')


@csrf_exempt
def detect_disease(request):
    if request.method == "POST" and request.FILES.get("image"):
        image_file = request.FILES["image"].read()
        image_np = np.frombuffer(image_file, np.uint8)
        image = cv2.imdecode(image_np, cv2.IMREAD_COLOR)

        if image is None:
            return JsonResponse({"error": "Invalid image file"}, status=400)

        # Predict disease + Gemini API Call
        disease_name, gemini_response = predict_disease(image, request)

        crop_name = "Paddy" if "paddy" in disease_name.lower() else "Unknown"

        # Store cure in session
        request.session["current_cure"] = gemini_response
        request.session["current_disease"] = disease_name

        return JsonResponse({
            "crop": crop_name,
            "disease": disease_name,
            "cure": gemini_response
        })

    return JsonResponse({"error": "Invalid request"}, status=400)


# Add new chatbot endpoint
@csrf_exempt
def ask_question(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            question = data.get("question", "")
            
            # Retrieve cure information from session
            cure_text = request.session.get('current_cure', '')
            disease_name = request.session.get('current_disease', '')
            
            if not cure_text:
                return JsonResponse({"error": "No cure information found. Please analyze an image first."})
            
            # Get chatbot response
            answer = get_chatbot_response(question, request)
            return JsonResponse({
                "answer": answer,
                "disease": disease_name
            })
            
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    
    return JsonResponse({"error": "Invalid request method"}, status=405)