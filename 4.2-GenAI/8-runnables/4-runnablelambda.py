from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnablePassthrough,RunnableLambda
from dotenv import load_dotenv
load_dotenv()

def word_count(text):
    return len(text.split())

model=ChatOllama(model="llama3.1")
parser=StrOutputParser()
prompt=PromptTemplate(
    template="Write a joke about {topic}",
    input_variables=['topic']
)

joke_chain=RunnableSequence(prompt,model,parser)

parallel_chain=RunnableParallel(
    {"joke": RunnablePassthrough(),
     "Word_count":RunnableLambda(word_count)
})

final=RunnableSequence(joke_chain,parallel_chain)

print(final.invoke({"topic":"AI"}))