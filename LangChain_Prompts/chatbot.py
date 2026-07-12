from langchain_openai import ChatOpenAI
from langchain.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()
# model = ChatOpenAI() -> by default it uses model: gpt-3.5-turbo,
# model="gpt-4o-mini" is less expensive, so using it here.
model = ChatOpenAI(model="gpt-4o-mini")
# print('Model:', model.model_name)


chat_history = [
    SystemMessage('You are a helpful AI assistent')
]

while True:
    user_input = input("You: ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input == "exit":
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print('AI: ', result.content)

print(chat_history)
