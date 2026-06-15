import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

def get_gemini_model(api_key=None):
    if api_key:
        genai.configure(api_key=api_key)
    else:
        api_key_env = os.getenv("GOOGLE_API_KEY")
        if api_key_env:
            genai.configure(api_key=api_key_env)
        else:
            raise ValueError("No API key provided")
    
    return genai.GenerativeModel('gemini-1.5-flash')