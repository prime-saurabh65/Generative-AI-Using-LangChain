from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

# This loads the anthropic-api-key from .env file
load_dotenv()

model = ChatAnthropic(model='claude-3-5sonnet-20241022')

result = model.invoke("What is the capital of India")

print(result.content)