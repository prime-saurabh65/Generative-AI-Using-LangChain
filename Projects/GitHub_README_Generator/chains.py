from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from prompts import readme_prompt

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model='gemini-3.5-flash',
    temperature=0.4
)

parser = StrOutputParser()

chain = readme_prompt | llm | parser