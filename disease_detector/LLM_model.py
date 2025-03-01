import google.generativeai as genai
import os
from dotenv import load_dotenv
import re

load_dotenv()

# Configure Gemini API Key
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

# Helper function to get response from Gemini
def get_gemini_response(disease_name):
    try:
        # Construct the prompt
        prompt = f"What are its causes? What is the and possible treatments {disease_name}?"

        # Define the generation configuration
        generation_config = {
            "temperature": 1,
            "top_p": 0.95,
            "top_k": 64,
            "max_output_tokens": 512,
            "response_mime_type": "text/plain",
        }

        # Instantiate the generative model
        gemini_model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",  
            generation_config=generation_config
        )

        chat_session = gemini_model.start_chat(
            history=[]
        )

        response = chat_session.send_message(f"What are its causes? What is the and possible treatments {disease_name}?")
        if response:
            return clean_text(response.text, disease_name)
        else:
            return "Cure information not available."
    
    except Exception as e:
        return f"Error fetching details from Gemini: {str(e)}"

def clean_text(text, disease_name):
    """
    Cleans the Gemini API response by:
    - Removing asterisks (*) and double asterisks (**)
    - Fixing bullet points
    - Ensuring proper line breaks for readability
    """
    
    # Remove markdown asterisks (*, **)
    text = re.sub(r'\*+', '', text)
    
    # Add double newlines before major sections
    text = re.sub(r'(Causes of .*?:)', r'\n\n\1\n', text)
    text = re.sub(r'(Possible Treatments for .*?:)', r'\n\n\1\n', text)

    # Replace inline bullet points with proper list formatting
    text = re.sub(r'(\n\s*•?\s*)\*', r'\n•', text)

    # Ensure newlines before each bullet point
    text = re.sub(r'(\n\s*)(\w)', r'\1\n\2', text)

    # Fix excessive spaces and newlines
    text = re.sub(r'\s+\n', '\n', text)
    text = re.sub(r'\n+', '\n', text)

    return text.strip()