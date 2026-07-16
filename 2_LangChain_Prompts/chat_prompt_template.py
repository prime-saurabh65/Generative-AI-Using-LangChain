from langchain_core.prompts import ChatPromptTemplate
# from langchain.messages import SystemMessage, HumanMessage

chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful {domain} expert'),
    ('human', 'Explain in simple term, what is {topic}')
    # SystemMessage(content='You are a helpful {domain} expert'),
    # HumanMessage(content='Explain in simple term, what is {topic}')
])

prompt = chat_template.invoke({'domain':'cricket', 'topic':'dusra'})

print(prompt)