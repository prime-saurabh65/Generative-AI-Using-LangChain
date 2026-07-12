from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

# this loads api key from .env file
load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-3.5-flash')

result = model.invoke("What is the capital of India")

# print(result.text())
print(result.content[0]["text"])

