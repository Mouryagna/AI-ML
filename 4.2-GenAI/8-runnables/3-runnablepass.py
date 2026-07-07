from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnablePassthrough
from dotenv import load_dotenv
load_dotenv()

model=ChatOllama(model="llama3.1")
prompt1=PromptTemplate(
    template="Tell me a good chain - {topic}",
    input_variables=['topic']
)

prompt2=PromptTemplate(
    template="Explain the joke -  {topic}",
    input_variables=['topic']
)

parser=StrOutputParser()

chain1=RunnableSequence(prompt1,model,parser)
chain2=RunnableSequence(prompt2,model,parser)

chain=RunnableParallel({
    "joke": RunnablePassthrough(),
    "explaination":chain2
})

final_chain=RunnableSequence(chain1,chain)

print(chain.invoke({"topic":"AI"}))