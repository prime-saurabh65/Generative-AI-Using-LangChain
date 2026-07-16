from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
# Note: HuggingFaceEndpoint needed when you want to use HF api

from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    # tell which model you want to use:
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("What is the capital of India")

print(result.content)

