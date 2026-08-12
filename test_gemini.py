from google import genai

from dotenv import load_dotenv,find_dotenv

import os

status=load_dotenv(find_dotenv(),override=True)

print(f"My .env is loaded: {status} and my key is {os.getenv('GOOGLE_API_KEY')}")

obj=genai.Client(api_key=os.getenv('GOOGLE_API_KEY'))

ask=input('whats your question?')

response=obj.models.generate_content(
    model='gemini-3.6-flash',
    contents=ask
)

print(f"The response is :- {response.text}")