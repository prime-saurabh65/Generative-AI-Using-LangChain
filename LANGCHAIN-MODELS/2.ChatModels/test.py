# Code snippet: Know which models are available to use

from google import genai

client = genai.Client(api_key="your_api_key")

for model in client.models.list():
    print(model.name)