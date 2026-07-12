# if you run this file, the model gets downloaded first
# this model was of size aroung 90 MBs.

from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

text = "Delhi is the capital of India"
vector = embedding.embed_query(text)

print(str(vector))