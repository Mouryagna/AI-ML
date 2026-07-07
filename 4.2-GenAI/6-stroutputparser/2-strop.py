from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()

model = ChatOllama(model='llama3.1')

template1=PromptTemplate(
    template="Write a detailed report on the {topic}",
    input_variables=['topic']
)

template2=PromptTemplate(
    template="Write a 5 line summary on the following text.\n {topic}",
    input_variables=['topic']
)

parser=StrOutputParser()

chain= template1 | model | parser | template2 | model | parser

result=chain.invoke({"topic": "Black Hole"})

print(result)