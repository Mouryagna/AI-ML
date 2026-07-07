from langchain_ollama import ChatOllama
from dotenv import load_dotenv
load_dotenv()
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

prompt1=PromptTemplate(
    template="Generate Detail report on {topic}",
    input_variables=['topic']
)

prompt2=PromptTemplate(
    template="Generate a 5 pointer summary from the following text.\n {text}",
    input_variables=['text']
)

model=ChatOllama(model='llama3.1')
parser=StrOutputParser()

chain= prompt1 | model | parser | prompt2 | model |parser

result=chain.invoke({"topic": "Black Hole"})
print(result)
