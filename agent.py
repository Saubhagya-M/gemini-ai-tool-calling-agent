from calc import calculator
from grade import student_grade

from google import genai

from dotenv import load_dotenv,find_dotenv

from google.genai import types # this works to integrate tools in LLM


import os

load_dotenv(find_dotenv(),override=True)

key=os.getenv("GOOGLE_API_KEY")

if not key:
    raise ValueError('GEMINI API KEY IS NOT CONFIGURED')


obj=genai.Client(api_key=key)

# print(obj)

# DEFINE THE LLM THE TOOLS and REGISTER THEM

mytools=[calculator,student_grade]


def run_agent(user_input):
    response=obj.models.generate_content(
        model='gemini-3.6-flash',
        contents=user_input,
        config=types.GenerateContentConfig(tools=mytools)
    )
    return response.text

#MAIN 
print('#############################')

print('  GEMINI AI CALCULATOR AGENT')

print('type exit to stop')


while True:
    user_input=input("\nYou: ")
    if user_input.lower()=='exit':
        print("AGENT: GOODBYE!!!")
        break

    try:
        answer=run_agent(user_input)
        print("AGENT: ",answer)
    except Exception as e:
        print("Error: ",e)
    