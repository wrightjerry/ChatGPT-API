import os
import openai
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv('API_KEY')
messages = []
system_msg = input("What type of chatbot would you like to create?\n")
messages.append({"role": "system", "content": system_msg})

print("Your new assistant is ready!")
while input != "quit()":
    message = input()
    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    print("\n" + reply + "\n")