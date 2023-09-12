import os
import openai

try:
    # Set OpenAI API key
    temp_key:str = "Legg inn API nøkkel her"
    openai.api_key = temp_key
except:
    print("OpenAI API key not found. Please set the environment variable OPENAI_API_KEY to your API key.")
    exit(1)


def request_chat_completion(previous_message:dict, role:str = 'system',message :str = ''):

    if(not role == "system" or "user" or "assistant"):
        print("Invalid role")
        return None
    
    if(previous_message):
        response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            previous_message,
            {"role": role, "content": message}
        ]
        )
    else: 
        response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": role, "content": message}, 
        ]
        )

    print(response)

request_chat_completion(None,"system", "Cogito is better then Brain")