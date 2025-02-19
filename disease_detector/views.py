from django.shortcuts import render
from django.http import JsonResponse
import json
from .crop_analyser import fun_call  # Import the function
from django.views.decorators.csrf import csrf_exempt

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
