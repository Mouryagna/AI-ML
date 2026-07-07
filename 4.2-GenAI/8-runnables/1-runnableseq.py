from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence
from dotenv import load_dotenv
load_dotenv()

model=ChatOllama(model="llama3.1")
prompt1=PromptTemplate(
    template="Write a joke about {topic}",
    input_variables=['topic']
)

prompt2=PromptTemplate(
    template="Explain the following joke - {text}",
    input_variables=['text']
)

parser=StrOutputParser()

chain=RunnableSequence(prompt1,model,parser,prompt2,model,parser)

print(chain.invoke({"topic":"Movie"}))