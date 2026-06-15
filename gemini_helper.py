import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

def get_gemini_model(api_key=None):
    """
    Get Gemini model with fallback options
    Uses gemini-pro (most stable and widely available)
    """
    if api_key:
        genai.configure(api_key=api_key)
    else:
        api_key_env = os.getenv("GOOGLE_API_KEY")
        if api_key_env:
            genai.configure(api_key=api_key_env)
        else:
            raise ValueError("No API key provided")
    
    # Try different models in order of preference
    models_to_try = [
        'gemini-pro',
        'gemini-1.5-pro',
        'gemini-1.5-flash',
        'gemini-1.0-pro'
    ]
    
    for model_name in models_to_try:
        try:
            model = genai.GenerativeModel(model_name)
            # Test if model works
            test_response = model.generate_content("test")
            if test_response:
                print(f"✅ Using model: {model_name}")
                return model
        except Exception as e:
            print(f"⚠️ Model {model_name} not available: {str(e)}")
            continue
    
    # If all else fails, default to gemini-pro
    return genai.GenerativeModel('gemini-pro')

def list_available_models(api_key=None):
    """
    List all available models in your API
    """
    if api_key:
        genai.configure(api_key=api_key)
    else:
        api_key_env = os.getenv("GOOGLE_API_KEY")
        if api_key_env:
            genai.configure(api_key=api_key_env)
    
    try:
        models = genai.list_models()
        print("\n🤖 Available Models:")
        print("=" * 50)
        for model in models:
            print(f"- {model.name}")
            print(f"  Display: {model.display_name}")
            print(f"  Methods: {', '.join([m for m in dir(model) if not m.startswith('_')])}")
            print()
        return models
    except Exception as e:
        print(f"❌ Error listing models: {str(e)}")
        return None