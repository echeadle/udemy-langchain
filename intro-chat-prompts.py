import os
from openai import OpenAI
from dotenv import find_dotenv, load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

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
tone = """Proper British English in a nice, warm, respectful tone"""
language = "French"
prompt = f"""
 Rewrite the {customer_review} message in a {tone}, and then
 please translate the new review message into {language}. 
"""
rewrite =get_completion(prompt=prompt)
# print(rewrite)
# This is done with OpenAI not langchain. 
# ===== Using LangChain & prompt templates - Still ChatAPI ====

chat_model = ChatOpenAI(temperature=0.7, model=llm_model)

template_string = f"""
  Translate the following text {customer_review} into italiano in a
  polite tone.
"""

prompt_template = ChatPromptTemplate.from_template(template_string)

translation_message = prompt_template.format_messages(
    customer_review = customer_review
)

response = chat_model.invoke(translation_message)
print(response.content)