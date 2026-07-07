from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence,RunnableParallel
from dotenv import load_dotenv
load_dotenv()

model=ChatOllama(model="llama3.1")
prompt1=PromptTemplate(
    template="Generate a tweet about the {topic}",
    input_variables=['topic']
)

prompt2=PromptTemplate(
    template="Generate the Linkedin post about the  {topic}",
    input_variables=['topic']
)

parser=StrOutputParser()

chain1=RunnableSequence(prompt1,model,parser)
chain2=RunnableSequence(prompt2,model,parser)

chain=RunnableParallel({
    "X": chain1,
    "Linkedin":chain2
})

print(chain.invoke({"topic":"AI"}))