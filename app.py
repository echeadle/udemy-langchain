import os
import openai
from dotenv import find_dotenv, load_dotenv
from langchain_openai import OpenAI

load_dotenv(find_dotenv())
openai.api_key = os.getenv("OPENAI_API_KEY")

llm_model = "gpt-3.5-turbo"

llm = OpenAI(temperature=0.7)

print(llm.invoke("What is the weather in WA DC"))