import os

from dotenv import load_dotenv
load_dotenv()
from langchain.chat_models import init_chat_model






""" model = init_chat_model("groq:openai/gpt-oss-120b",temperature=0.7)

response = model.invoke("Hello, how are you?")

print(response.content) """