import os
from openai import OpenAI
from dotenv import find_dotenv, load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv(find_dotenv())

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
llm_model = "gpt-3.5-turbo"
chat_model = ChatOpenAI(temperature=0.7, model=llm_model)

# OpenAI Completion Endpoint
def get_completion(prompt, model=llm_model):
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(model=model,
    messages=messages,
    temperature=0)
    return response.choices[0].message.content

# Translate text, review
customer_review = """
  Your product is terrible! I don't knnow how
  you were able to get this to market.
  I don't want this!  Actually no one should want this.
  Seriously! Give me my money back now!
"""

prompt = """
 Rewrite the customer review message in a polite tone, and then
 please translate the new review message into French. 
"""
rewrite =get_completion(prompt=prompt)
print(rewrite)
