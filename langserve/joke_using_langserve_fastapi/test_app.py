from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

def configure():
    load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv('openai_api_key')
model = ChatOpenAI(model="gpt-3.5-turbo-16k")

prompt = ChatPromptTemplate.from_template("Tell me interesting joke on the topic: {topic} ")

chain = prompt | model