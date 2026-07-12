# This is for only if you want to download the model locally and use it:
# If you run this file, model "meta-llama/Llama-3.1-8B-Instruct" get downloaded.

from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

llm = HuggingFacePipeline.from_model_id(
    model_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
    pipeline_kwargs=dict(
        temperatue=0.5,
        max_new_tokens=100
    )
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("What is the capital of India")

print(result.content)