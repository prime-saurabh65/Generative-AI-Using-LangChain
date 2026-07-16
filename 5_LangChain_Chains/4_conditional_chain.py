from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableBranch, RunnableLambda, RunnablePassthrough
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-3.1-flash-lite')

parser = StrOutputParser()

class Feedback(BaseModel):
    sentiment: Literal['positive', 'negative'] = Field(description='Give the sentiment of the feedback')

parser2 = PydanticOutputParser(pydantic_object=Feedback)

prompt1 = PromptTemplate(
    template='Classify the sentiment of the following feedback into positive or negative \n {feedback} \n {format_instruction}',
    input_variables=['feedback'],
    partial_variables={'format_instruction': parser2.get_format_instructions()}
)

classifier_chain = prompt1 | model | parser2
# result = classifier_chain.invoke({'feedback': 'This is a terrible smartphone'}).sentiment
# print(result)

prompt2 = PromptTemplate(
    template='Write an appropriate short response of 2 lines to this positive feedback \n {feedback}',
    input_variables=['feedback']
)

prompt3 = PromptTemplate(
    template='Write an appropriate short response of 2 lines to this negative feedback \n {feedback}',
    input_variables=['feedback']
)

branch_chain = (
    RunnablePassthrough.assign(sentiment=classifier_chain)
    | RunnableBranch(
        (
            lambda x: x["sentiment"].sentiment == "positive",
            prompt2 | model | parser,
        ),
        (
            lambda x: x["sentiment"].sentiment == "negative",
            prompt3 | model | parser,
        ),
        RunnableLambda(lambda x: "Could not find sentiment"),
    )
)

chain = branch_chain

result = chain.invoke({'feedback': "This is a wonderful smartphone"})
print(result)

visualize = chain.get_graph().draw_ascii()
print(visualize)