import openai
import gradio
import os
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv('API_KEY')

messages = [{"role": "system", "content": "You are a nutritional guide expert that offers personalized nutrition advice, answers diet-related queries, and suggests healthy recipes based on individual preferences and dietary restrictions."}]

def CustomChatGPT(Question):
    messages.append({"role": "user", "content": Question})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Nutritional Guide Expert")

demo.launch(share=True)