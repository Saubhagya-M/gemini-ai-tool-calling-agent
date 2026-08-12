from google import genai

from dotenv import load_dotenv,find_dotenv

import os

def get_gemini_key():
    '''
    This function a GATEWAY to MY LLM (Gemini)
    '''
    load_dotenv(find_dotenv(),override=True)
    return os.getenv('GOOGLE_API_KEY')